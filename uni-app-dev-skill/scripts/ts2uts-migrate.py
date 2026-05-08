#!/usr/bin/env python3
"""
TypeScript to UTS Migration Helper
Analyzes TypeScript/Vue files and suggests UTS-compatible changes.
"""

import os
import sys
import re
import argparse
from typing import List, Tuple

class MigrationIssue:
    def __init__(self, line: int, col: int, severity: str, code: str, message: str, suggestion: str):
        self.line = line
        self.col = col
        self.severity = severity  # 'error' or 'warning'
        self.code = code
        self.message = message
        self.suggestion = suggestion
    
    def __str__(self) -> str:
        prefix = "ERROR" if self.severity == "error" else "WARN"
        return f"  L{self.line}:{self.col} [{prefix}] [{self.code}] {self.message}\n         Suggestion: {self.suggestion}"


def check_undefined(content: str) -> List[MigrationIssue]:
    """Check for undefined usage (UTS110111119)."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\bundefined\b', line):
            # Skip comments
            stripped = line.strip()
            if stripped.startswith('//') or stripped.startswith('*') or stripped.startswith('/*'):
                continue
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111119',
                message="undefined is not supported in UTS",
                suggestion="Use null instead of undefined"
            ))
    return issues


def check_any_type(content: str) -> List[MigrationIssue]:
    """Check for implicit any usage."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        stripped = line.strip()
        if stripped.startswith('//'):
            continue
        # Check for : any
        if re.search(r':\s*any\b', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='warning', code='UTS-TYPE',
                message="any type has different semantics in UTS",
                suggestion="Use specific type or generic instead"
            ))
    return issues


def check_eval(content: str) -> List[MigrationIssue]:
    """Check for eval() usage."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\beval\s*\(', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111130',
                message="eval() is not supported in UTS",
                suggestion="Refactor to avoid dynamic code execution"
            ))
    return issues


def check_new_function(content: str) -> List[MigrationIssue]:
    """Check for new Function() usage."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'new\s+Function\s*\(', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111131',
                message="new Function() is not supported in UTS",
                suggestion="Use regular function declarations instead"
            ))
    return issues


def check_prototype(content: str) -> List[MigrationIssue]:
    """Check for prototype usage."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\.prototype\b', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111159',
                message="prototype is not supported in UTS",
                suggestion="Use class syntax instead of prototype"
            ))
    return issues


def check_typeof_type_guard(content: str) -> List[MigrationIssue]:
    """Check for typeof type guards."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\btypeof\s+\w+\s*===?\s*[\'"]', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='warning', code='UTS110111140',
                message="typeof type guard has limited support in UTS",
                suggestion="Use instanceof or explicit type checks instead"
            ))
    return issues


def check_symbol(content: str) -> List[MigrationIssue]:
    """Check for Symbol usage."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\bSymbol\b', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111160',
                message="Symbol is not supported in UTS",
                suggestion="Use string or number keys instead"
            ))
    return issues


def check_generator(content: str) -> List[MigrationIssue]:
    """Check for generator functions."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'function\s*\*', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111170',
                message="Generator functions are not supported in UTS",
                suggestion="Use async/await or callback patterns instead"
            ))
    return issues


def check_delete_operator(content: str) -> List[MigrationIssue]:
    """Check for delete operator."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\bdelete\s+', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='warning', code='UTS110111180',
                message="delete operator is not supported in UTS",
                suggestion="Set property to null instead of using delete"
            ))
    return issues


def check_as_const(content: str) -> List[MigrationIssue]:
    """Check for as const usage."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\bas\s+const\b', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='error', code='UTS110111190',
                message="as const is not supported in UTS",
                suggestion="Use explicit type annotations instead"
            ))
    return issues


def check_dynamic_access(content: str) -> List[MigrationIssue]:
    """Check for dynamic property access with variables."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        # obj[variable] pattern (not obj['literal'])
        if re.search(r'\w+\[\s*\w+\s*\]', line) and not re.search(r'\w+\[\s*[\'"]', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='warning', code='UTS110111150',
                message="Dynamic property access with variable key may not work in UTS",
                suggestion="Use Map<string, T> for dynamic key access"
            ))
    return issues


def check_interface_vs_type(content: str) -> List[MigrationIssue]:
    """Check for interface usage that should be type."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'\binterface\s+\w+\s*\{', line):
            issues.append(MigrationIssue(
                line=i, col=0, severity='info', code='UTS-STYLE',
                message="Consider using 'type' instead of 'interface' for object shapes in UTS",
                suggestion="type X = { ... } is preferred over interface X { ... } in UTS"
            ))
    return issues


def check_console_log_type(content: str) -> List[MigrationIssue]:
    """Check for console.log with non-primitive types that may cause issues."""
    issues = []
    for i, line in enumerate(content.split('\n'), 1):
        if re.search(r'console\.log\(', line):
            # Check if logging a complex object directly
            if re.search(r'console\.log\(\s*\w+\s*\)', line):
                pass  # This is fine
    return issues


def analyze_file(filepath: str) -> List[MigrationIssue]:
    """Analyze a single file for UTS migration issues."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return []
    
    all_issues = []
    all_issues.extend(check_undefined(content))
    all_issues.extend(check_any_type(content))
    all_issues.extend(check_eval(content))
    all_issues.extend(check_new_function(content))
    all_issues.extend(check_prototype(content))
    all_issues.extend(check_typeof_type_guard(content))
    all_issues.extend(check_symbol(content))
    all_issues.extend(check_generator(content))
    all_issues.extend(check_delete_operator(content))
    all_issues.extend(check_as_const(content))
    all_issues.extend(check_dynamic_access(content))
    all_issues.extend(check_interface_vs_type(content))
    
    return all_issues


def analyze_project(project_dir: str):
    """Analyze entire project for UTS migration issues."""
    print(f"Analyzing project for UTS migration: {project_dir}")
    print("=" * 60)
    
    total_errors = 0
    total_warnings = 0
    total_info = 0
    files_analyzed = 0
    
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules' and d != 'unpackage']
        
        for f in files:
            if f.endswith(('.ts', '.js', '.vue', '.uvue')):
                filepath = os.path.join(root, f)
                issues = analyze_file(filepath)
                
                if issues:
                    rel_path = os.path.relpath(filepath, project_dir)
                    print(f"\n{rel_path}:")
                    for issue in issues:
                        print(str(issue))
                        if issue.severity == 'error':
                            total_errors += 1
                        elif issue.severity == 'warning':
                            total_warnings += 1
                        else:
                            total_info += 1
                
                files_analyzed += 1
    
    print("\n" + "=" * 60)
    print(f"Analysis complete: {files_analyzed} files analyzed")
    print(f"  Errors: {total_errors}")
    print(f"  Warnings: {total_warnings}")
    print(f"  Info: {total_info}")
    
    if total_errors > 0:
        print("\nCritical issues must be fixed before UTS compilation will succeed.")
    
    return total_errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze TypeScript/Vue files for UTS migration issues")
    parser.add_argument("project_dir", help="Path to project directory")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.project_dir):
        print(f"Error: '{args.project_dir}' is not a directory")
        sys.exit(1)
    
    errors = analyze_project(args.project_dir)
    sys.exit(1 if errors > 0 else 0)
