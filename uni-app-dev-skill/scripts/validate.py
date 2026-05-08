#!/usr/bin/env python3
"""
uni-app Code Validator Script
Validates uni-app x project files for common issues.
"""

import os
import sys
import json
import re
import argparse
from typing import List, Tuple

class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
    
    def add_error(self, msg: str):
        self.errors.append(msg)
    
    def add_warning(self, msg: str):
        self.warnings.append(msg)
    
    def add_info(self, msg: str):
        self.info.append(msg)
    
    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0
    
    def __str__(self) -> str:
        lines = []
        if self.errors:
            lines.append(f"Errors ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"   - {e}")
        if self.warnings:
            lines.append(f"Warnings ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"   - {w}")
        if self.info:
            lines.append(f"Info ({len(self.info)}):")
            for i in self.info:
                lines.append(f"   - {i}")
        if not self.errors and not self.warnings:
            lines.append("No issues found!")
        return "\n".join(lines)


def validate_pages_json(project_dir: str) -> ValidationResult:
    """Validate pages.json configuration."""
    result = ValidationResult()
    pages_json_path = os.path.join(project_dir, "pages.json")
    
    if not os.path.exists(pages_json_path):
        result.add_error("pages.json not found in project root")
        return result
    
    try:
        with open(pages_json_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Remove conditional compilation comments for JSON parsing
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
            content = re.sub(r'//.*', '', content)
            # Remove trailing commas
            content = re.sub(r',\s*([}\]])', r'\1', content)
            config = json.loads(content)
    except json.JSONDecodeError as e:
        result.add_error(f"pages.json is not valid JSON: {e}")
        return result
    
    # Check required fields
    if "pages" not in config:
        result.add_error("pages.json missing required 'pages' field")
        return result
    
    if not isinstance(config["pages"], list):
        result.add_error("'pages' must be an array")
        return result
    
    if len(config["pages"]) == 0:
        result.add_error("'pages' array is empty - at least one page required")
    
    # Validate each page
    for i, page in enumerate(config["pages"]):
        if not isinstance(page, dict):
            result.add_error(f"pages[{i}] must be an object")
            continue
        
        if "path" not in page:
            result.add_error(f"pages[{i}] missing required 'path' field")
            continue
        
        # Check if page file exists
        page_path = page["path"]
        for ext in [".uvue", ".vue"]:
            full_path = os.path.join(project_dir, page_path + ext)
            if os.path.exists(full_path):
                break
        else:
            result.add_warning(f"Page file not found: {page_path}.uvue or .vue")
        
        # Check for common style issues
        if "style" in page:
            style = page["style"]
            if "navigationBarTitleText" not in style:
                result.add_info(f"pages[{i}] ({page_path}): No navigationBarTitleText set")
    
    # Validate tabBar
    if "tabBar" in config:
        tab_bar = config["tabBar"]
        if "list" not in tab_bar:
            result.add_error("tabBar missing required 'list' field")
        else:
            tab_list = tab_bar["list"]
            if len(tab_list) < 2:
                result.add_error("tabBar.list must have at least 2 items")
            if len(tab_list) > 5:
                result.add_error("tabBar.list must have at most 5 items")
            
            for j, tab in enumerate(tab_list):
                if "pagePath" not in tab:
                    result.add_error(f"tabBar.list[{j}] missing 'pagePath'")
                elif "pages" in config:
                    page_paths = [p.get("path", "") for p in config["pages"]]
                    if tab["pagePath"] not in page_paths:
                        result.add_error(f"tabBar.list[{j}] pagePath '{tab['pagePath']}' not found in pages")
                
                if "text" not in tab:
                    result.add_warning(f"tabBar.list[{j}] missing 'text'")
    
    # Validate subPackages
    if "subPackages" in config:
        for k, sub in enumerate(config["subPackages"]):
            if "root" not in sub:
                result.add_error(f"subPackages[{k}] missing 'root' field")
            if "pages" not in sub:
                result.add_error(f"subPackages[{k}] missing 'pages' field")
    
    # Check for duplicate page paths
    if "pages" in config:
        paths = [p.get("path", "") for p in config["pages"]]
        duplicates = [p for p in paths if paths.count(p) > 1]
        if duplicates:
            result.add_error(f"Duplicate page paths: {set(duplicates)}")
    
    return result


def validate_manifest_json(project_dir: str) -> ValidationResult:
    """Validate manifest.json configuration."""
    result = ValidationResult()
    manifest_path = os.path.join(project_dir, "manifest.json")
    
    if not os.path.exists(manifest_path):
        result.add_error("manifest.json not found in project root")
        return result
    
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
            content = re.sub(r'//.*', '', content)
            content = re.sub(r',\s*([}\]])', r'\1', content)
            config = json.loads(content)
    except json.JSONDecodeError as e:
        result.add_error(f"manifest.json is not valid JSON: {e}")
        return result
    
    # Check required fields
    required_fields = ["name", "appid", "versionName", "versionCode"]
    for field in required_fields:
        if field not in config:
            result.add_error(f"manifest.json missing required field: {field}")
    
    # Validate appid format
    if "appid" in config:
        appid = config["appid"]
        if not re.match(r'^__UNI__[A-Za-z0-9]+$', str(appid)):
            result.add_warning(f"appid '{appid}' doesn't match expected format __UNI__XXXXXXX")
    
    # Check vueVersion
    if "vueVersion" in config:
        if config["vueVersion"] != "3":
            result.add_warning("uni-app x requires vueVersion to be '3'")
    else:
        result.add_info("vueVersion not specified, defaulting to Vue 3")
    
    return result


def validate_uvue_file(filepath: str) -> ValidationResult:
    """Validate a single .uvue file."""
    result = ValidationResult()
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        result.add_error(f"Cannot read file: {e}")
        return result
    
    filename = os.path.basename(filepath)
    
    # Check for template section
    if "<template>" not in content:
        result.add_warning(f"{filename}: Missing <template> section")
    
    # Check for script section
    if "<script" not in content:
        result.add_warning(f"{filename}: Missing <script> section")
    
    # Check for common UTS issues
    # 1. Check for undefined usage
    if re.search(r'\bundefined\b', content):
        result.add_warning(f"{filename}: Uses 'undefined' - UTS does not support undefined, use null instead")
    
    # 2. Check for dynamic property access
    if re.search(r'\w+\[\s*[\'"].*?[\'"]\s*\]', content):
        # This is a rough check - dynamic property access like obj['key'] is OK
        # but obj[variable] is not allowed in UTS
        pass
    
    # 3. Check for eval usage
    if re.search(r'\beval\s*\(', content):
        result.add_error(f"{filename}: Uses eval() - not supported in UTS")
    
    # 4. Check for new Function
    if re.search(r'new\s+Function\s*\(', content):
        result.add_error(f"{filename}: Uses new Function() - not supported in UTS")
    
    # 5. Check for prototype usage
    if re.search(r'\.prototype\b', content):
        result.add_warning(f"{filename}: Uses .prototype - not supported in UTS, use class instead")
    
    # 6. Check for text directly in view (should be in <text> tags)
    # This is a rough heuristic
    if re.search(r'<view[^>]*>[^<\n\s{][^<]*</view>', content):
        text_match = re.search(r'<view[^>]*>([^<\n\s{][^<]*)</view>', content)
        if text_match and not text_match.group(1).strip().startswith('<'):
            result.add_warning(f"{filename}: Text directly in <view> - should be wrapped in <text> tag")
    
    # 7. Check for :active pseudo-class
    if re.search(r':active', content):
        result.add_warning(f"{filename}: Uses :active pseudo-class - not supported on native, use hover-class instead")
    
    # 8. Check for #id selector in CSS
    style_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
    if style_match:
        css_content = style_match.group(1)
        if re.search(r'#[a-zA-Z]', css_content):
            result.add_warning(f"{filename}: Uses #id selector in CSS - not supported on native, use class selector instead")
        if re.search(r'[a-zA-Z]+\s*\{', css_content) and not re.search(r'\.[a-zA-Z]', css_content):
            # Tag selector detected
            pass
    
    # 9. Check for unclosed conditional compilation
    ifdef_count = len(re.findall(r'#ifdef|#ifndef', content))
    endif_count = len(re.findall(r'#endif', content))
    if ifdef_count != endif_count:
        result.add_error(f"{filename}: Unclosed conditional compilation - {ifdef_count} #ifdef/#ifndef but {endif_count} #endif")
    
    # 10. Check for nested conditional compilation
    # Simple check - doesn't handle all edge cases
    lines = content.split('\n')
    depth = 0
    for line in lines:
        if '#ifdef' in line or '#ifndef' in line:
            depth += 1
            if depth > 1:
                result.add_error(f"{filename}: Nested conditional compilation is not supported")
                break
        if '#endif' in line:
            depth -= 1
    
    return result


def validate_project(project_dir: str) -> ValidationResult:
    """Validate entire uni-app x project."""
    overall = ValidationResult()
    
    print(f"Validating project: {project_dir}")
    print("=" * 50)
    
    # Validate pages.json
    print("\n1. Checking pages.json...")
    result = validate_pages_json(project_dir)
    print(result)
    overall.errors.extend(result.errors)
    overall.warnings.extend(result.warnings)
    overall.info.extend(result.info)
    
    # Validate manifest.json
    print("\n2. Checking manifest.json...")
    result = validate_manifest_json(project_dir)
    print(result)
    overall.errors.extend(result.errors)
    overall.warnings.extend(result.warnings)
    overall.info.extend(result.info)
    
    # Validate .uvue files
    print("\n3. Checking .uvue files...")
    for root, dirs, files in os.walk(project_dir):
        # Skip node_modules and hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules' and d != 'unpackage']
        for f in files:
            if f.endswith('.uvue') or f.endswith('.vue'):
                filepath = os.path.join(root, f)
                result = validate_uvue_file(filepath)
                if result.has_errors or result.warnings:
                    overall.errors.extend(result.errors)
                    overall.warnings.extend(result.warnings)
                    overall.info.extend(result.info)
                    print(f"  {os.path.relpath(filepath, project_dir)}:")
                    print(result)
    
    print("\n" + "=" * 50)
    print(f"Summary: {len(overall.errors)} errors, {len(overall.warnings)} warnings, {len(overall.info)} info")
    
    return overall


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate uni-app x project")
    parser.add_argument("project_dir", help="Path to uni-app x project directory")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.project_dir):
        print(f"Error: '{args.project_dir}' is not a directory")
        sys.exit(1)
    
    result = validate_project(args.project_dir)
    
    if args.strict and result.warnings:
        sys.exit(1)
    elif result.has_errors:
        sys.exit(1)
    else:
        sys.exit(0)
