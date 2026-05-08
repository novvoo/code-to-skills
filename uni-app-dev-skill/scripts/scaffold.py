#!/usr/bin/env python3
"""
uni-app Project Scaffolding Script
Creates a new uni-app x project with recommended structure.
"""

import os
import sys
import json
import argparse


def create_project(project_name: str, output_dir: str, template: str = "default"):
    """Create a new uni-app x project."""
    
    project_dir = os.path.join(output_dir, project_name)
    
    if os.path.exists(project_dir):
        print(f"Error: Directory '{project_dir}' already exists!")
        sys.exit(1)
    
    # Create directory structure
    dirs = [
        "pages/index",
        "static/tab",
        "static/images",
        "components",
        "api",
        "store",
        "utils",
    ]
    
    if template == "tabbar":
        dirs.extend([
            "pages/category",
            "pages/cart",
            "pages/user",
        ])
    elif template == "subpackage":
        dirs.extend([
            "pages-sub/detail",
            "pages-sub/search",
        ])
    
    for d in dirs:
        os.makedirs(os.path.join(project_dir, d), exist_ok=True)
    
    # Create pages.json
    pages_config = create_pages_json(template)
    with open(os.path.join(project_dir, "pages.json"), "w", encoding="utf-8") as f:
        json.dump(pages_config, f, indent=2, ensure_ascii=False)
    
    # Create manifest.json
    manifest_config = create_manifest_json(project_name)
    with open(os.path.join(project_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest_config, f, indent=2, ensure_ascii=False)
    
    # Create App.uvue
    create_app_uvue(project_dir)
    
    # Create store
    create_store(project_dir)
    
    # Create index page
    create_index_page(project_dir)
    
    # Create common CSS
    create_common_css(project_dir)
    
    # Create API module
    create_api_module(project_dir)
    
    # Create utils
    create_utils(project_dir)
    
    if template == "tabbar":
        create_tabbar_pages(project_dir)
    elif template == "subpackage":
        create_subpackage_pages(project_dir)
    
    print(f"Project '{project_name}' created successfully at {project_dir}")
    print(f"Template: {template}")
    print(f"\nNext steps:")
    print(f"  1. Open the project in HBuilderX")
    print(f"  2. Run on target platform (Web/Android/iOS/Mini Program)")


def create_pages_json(template: str) -> dict:
    """Create pages.json configuration."""
    config = {
        "pages": [
            {
                "path": "pages/index/index",
                "style": {
                    "navigationBarTitleText": "Home",
                    "navigationBarBackgroundColor": "#FFFFFF",
                    "navigationBarTextStyle": "black"
                }
            }
        ],
        "globalStyle": {
            "navigationBarTextStyle": "black",
            "navigationBarTitleText": "uni-app x",
            "navigationBarBackgroundColor": "#FFFFFF",
            "backgroundColor": "#F8F8F8"
        }
    }
    
    if template == "tabbar":
        config["pages"].extend([
            {
                "path": "pages/category/category",
                "style": {"navigationBarTitleText": "Category"}
            },
            {
                "path": "pages/cart/cart",
                "style": {"navigationBarTitleText": "Cart"}
            },
            {
                "path": "pages/user/user",
                "style": {"navigationBarTitleText": "My"}
            }
        ])
        config["tabBar"] = {
            "color": "#999999",
            "selectedColor": "#007AFF",
            "backgroundColor": "#FFFFFF",
            "list": [
                {"pagePath": "pages/index/index", "text": "Home", "iconPath": "static/tab/home.png", "selectedIconPath": "static/tab/home-active.png"},
                {"pagePath": "pages/category/category", "text": "Category", "iconPath": "static/tab/category.png", "selectedIconPath": "static/tab/category-active.png"},
                {"pagePath": "pages/cart/cart", "text": "Cart", "iconPath": "static/tab/cart.png", "selectedIconPath": "static/tab/cart-active.png"},
                {"pagePath": "pages/user/user", "text": "My", "iconPath": "static/tab/user.png", "selectedIconPath": "static/tab/user-active.png"}
            ]
        }
    elif template == "subpackage":
        config["subPackages"] = [
            {
                "root": "pages-sub",
                "pages": [
                    {"path": "detail/detail", "style": {"navigationBarTitleText": "Detail"}},
                    {"path": "search/search", "style": {"navigationBarTitleText": "Search"}}
                ]
            }
        ]
        config["preloadRule"] = {
            "pages/index/index": {
                "network": "all",
                "packages": ["pages-sub"]
            }
        }
    
    return config


def create_manifest_json(project_name: str) -> dict:
    """Create manifest.json configuration."""
    return {
        "name": project_name,
        "appid": "__UNI__CustomAppId",
        "description": "A uni-app x project",
        "versionName": "1.0.0",
        "versionCode": 100,
        "uni-app-x": {},
        "vueVersion": "3"
    }


def create_app_uvue(project_dir: str):
    """Create App.uvue entry file."""
    content = '''<script setup lang="uts">
  import { state } from '@/store/index.uts'

  onLaunch((_: OnLaunchOptions) => {
    console.log('App Launch')
  })

  onShow(() => {
    console.log('App Show')
  })

  onHide(() => {
    console.log('App Hide')
  })
</script>

<style>
  /* Global styles */
  @import "./common/uni.css";
</style>
'''
    with open(os.path.join(project_dir, "App.uvue"), "w", encoding="utf-8") as f:
        f.write(content)


def create_store(project_dir: str):
    """Create store module."""
    content = '''export type State = {
  globalNum: number
  token: string | null
  userInfo: UserInfo | null
}

export type UserInfo = {
  id: string
  name: string
  avatar: string
}

export const state = reactive({
  globalNum: 0,
  token: null as string | null,
  userInfo: null as UserInfo | null
} as State)

export const setGlobalNum = (num: number): void => {
  state.globalNum = num
}

export const setToken = (newToken: string | null): void => {
  state.token = newToken
}

export const setUserInfo = (info: UserInfo | null): void => {
  state.userInfo = info
}
'''
    with open(os.path.join(project_dir, "store", "index.uts"), "w", encoding="utf-8") as f:
        f.write(content)


def create_index_page(project_dir: str):
    """Create index page."""
    content = '''<template>
  <view class="container">
    <view class="header">
      <text class="title">Hello uni-app x</text>
      <text class="subtitle">Cross-platform development made easy</text>
    </view>
    
    <view class="content">
      <view class="card" v-for="(item, index) in features" :key="index">
        <text class="card-title">{{ item.title }}</text>
        <text class="card-desc">{{ item.desc }}</text>
      </view>
    </view>
    
    <view class="footer">
      <text class="counter">Count: {{ globalNum }}</text>
      <button type="primary" @click="increment">Increment</button>
    </view>
  </view>
</template>

<script setup lang="uts">
  import { state, setGlobalNum } from '@/store/index.uts'

  type FeatureItem = {
    title: string
    desc: string
  }

  const features = ref<FeatureItem[]>([
    { title: 'UTS Language', desc: 'Type-safe cross-platform language' },
    { title: 'Native Rendering', desc: 'Native performance on all platforms' },
    { title: 'Conditional Compilation', desc: 'Platform-specific code at build time' },
    { title: 'UTS Plugins', desc: 'Extend with native capabilities' }
  ])

  const globalNum = computed(() => state.globalNum)

  const increment = () => {
    setGlobalNum(state.globalNum + 1)
  }
</script>

<style scoped>
  .container {
    flex: 1;
    background-color: #f5f5f5;
  }
  
  .header {
    padding: 40rpx 30rpx;
    background-color: #007AFF;
  }
  
  .title {
    font-size: 40rpx;
    font-weight: bold;
    color: #ffffff;
  }
  
  .subtitle {
    font-size: 28rpx;
    color: rgba(255, 255, 255, 0.8);
    margin-top: 10rpx;
  }
  
  .content {
    padding: 20rpx;
  }
  
  .card {
    background-color: #ffffff;
    border-radius: 16rpx;
    padding: 30rpx;
    margin-bottom: 20rpx;
  }
  
  .card-title {
    font-size: 32rpx;
    font-weight: bold;
    color: #333333;
  }
  
  .card-desc {
    font-size: 26rpx;
    color: #999999;
    margin-top: 10rpx;
  }
  
  .footer {
    padding: 20rpx 30rpx;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  
  .counter {
    font-size: 30rpx;
    color: #333333;
  }
</style>
'''
    with open(os.path.join(project_dir, "pages", "index", "index.uvue"), "w", encoding="utf-8") as f:
        f.write(content)


def create_common_css(project_dir: str):
    """Create common CSS file."""
    os.makedirs(os.path.join(project_dir, "common"), exist_ok=True)
    content = '''/* Common CSS Variables */
:root {
  --primary-color: #007AFF;
  --success-color: #4CD964;
  --warning-color: #F0AD4E;
  --error-color: #E64340;
  --text-color: #333333;
  --text-color-secondary: #999999;
  --bg-color: #f5f5f5;
  --border-color: #e5e5e5;
  --font-size-xs: 20rpx;
  --font-size-sm: 24rpx;
  --font-size-md: 28rpx;
  --font-size-lg: 32rpx;
  --font-size-xl: 36rpx;
  --spacing-xs: 10rpx;
  --spacing-sm: 15rpx;
  --spacing-md: 20rpx;
  --spacing-lg: 30rpx;
  --spacing-xl: 40rpx;
  --border-radius-sm: 8rpx;
  --border-radius-md: 16rpx;
  --border-radius-lg: 24rpx;
}

/* Common utility classes */
.flex-row {
  display: flex;
  flex-direction: row;
}

.flex-column {
  display: flex;
  flex-direction: column;
}

.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.flex-1 {
  flex: 1;
}

.text-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.text-center {
  text-align: center;
}

.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}

.safe-area-top {
  padding-top: env(safe-area-inset-top);
}
'''
    with open(os.path.join(project_dir, "common", "uni.css"), "w", encoding="utf-8") as f:
        f.write(content)


def create_api_module(project_dir: str):
    """Create API module template."""
    content = '''export type RequestOptions = {
  url: string
  method?: string
  data?: UTSJSONObject | null
  header?: UTSJSONObject | null
  timeout?: number
}

export type ApiResponse<T> = {
  code: number
  message: string
  data: T | null
}

const BASE_URL = 'https://api.example.com'

export function request<T>(options: RequestOptions): Promise<ApiResponse<T>> {
  return new Promise((resolve, reject) => {
    uni.request({
      url: BASE_URL + options.url,
      method: options.method ?? 'GET',
      data: options.data ?? {},
      header: options.header ?? {},
      timeout: options.timeout ?? 60000,
      success(res) {
        if (res.statusCode === 200) {
          resolve(res.data as ApiResponse<T>)
        } else {
          reject(new Error(`HTTP Error: ${res.statusCode}`))
        }
      },
      fail(err) {
        reject(new Error(err.errMsg))
      }
    })
  })
}

export function get<T>(url: string, data?: UTSJSONObject | null): Promise<ApiResponse<T>> {
  return request<T>({ url, method: 'GET', data })
}

export function post<T>(url: string, data?: UTSJSONObject | null): Promise<ApiResponse<T>> {
  return request<T>({ url, method: 'POST', data })
}
'''
    with open(os.path.join(project_dir, "api", "index.uts"), "w", encoding="utf-8") as f:
        f.write(content)


def create_utils(project_dir: str):
    """Create utility module template."""
    content = '''/**
 * Format date to string
 */
export function formatDate(timestamp: number, format: string = 'YYYY-MM-DD'): string {
  const date = new Date(timestamp)
  const year = date.getFullYear()
  const month = (date.getMonth() + 1).toString().padStart(2, '0')
  const day = date.getDate().toString().padStart(2, '0')
  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')
  const seconds = date.getSeconds().toString().padStart(2, '0')
  
  return format
    .replace('YYYY', year.toString())
    .replace('MM', month)
    .replace('DD', day)
    .replace('HH', hours)
    .replace('mm', minutes)
    .replace('ss', seconds)
}

/**
 * Debounce function
 */
export function debounce(fn: () => void, delay: number): () => void {
  let timer: number | null = null
  return () => {
    if (timer !== null) {
      clearTimeout(timer)
    }
    timer = setTimeout(() => {
      fn()
      timer = null
    }, delay)
  }
}

/**
 * Throttle function
 */
export function throttle(fn: () => void, interval: number): () => void {
  let lastTime: number = 0
  return () => {
    const now = Date.now()
    if (now - lastTime >= interval) {
      fn()
      lastTime = now
    }
  }
}

/**
 * Validate phone number (China)
 */
export function isValidPhone(phone: string): boolean {
  return /^1[3-9]\d{9}$/.test(phone)
}

/**
 * Validate email
 */
export function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}
'''
    with open(os.path.join(project_dir, "utils", "index.uts"), "w", encoding="utf-8") as f:
        f.write(content)


def create_tabbar_pages(project_dir: str):
    """Create tab bar pages."""
    pages = {
        "category": ("Category", "Browse categories"),
        "cart": ("Cart", "Your shopping cart"),
        "user": ("My", "Personal center")
    }
    
    for page_name, (title, desc) in pages.items():
        page_dir = os.path.join(project_dir, "pages", page_name)
        os.makedirs(page_dir, exist_ok=True)
        
        content = f'''<template>
  <view class="container">
    <text class="title">{title}</text>
    <text class="desc">{desc}</text>
  </view>
</template>

<script setup lang="uts">
  // {title} page
</script>

<style scoped>
  .container {{
    flex: 1;
    justify-content: center;
    align-items: center;
  }}
  
  .title {{
    font-size: 36rpx;
    font-weight: bold;
    color: #333333;
  }}
  
  .desc {{
    font-size: 28rpx;
    color: #999999;
    margin-top: 10rpx;
  }}
</style>
'''
        with open(os.path.join(page_dir, f"{page_name}.uvue"), "w", encoding="utf-8") as f:
            f.write(content)


def create_subpackage_pages(project_dir: str):
    """Create subpackage pages."""
    pages = {
        "detail": ("Detail", "Item detail page"),
        "search": ("Search", "Search page")
    }
    
    for page_name, (title, desc) in pages.items():
        page_dir = os.path.join(project_dir, "pages-sub", page_name)
        os.makedirs(page_dir, exist_ok=True)
        
        content = f'''<template>
  <view class="container">
    <text class="title">{title}</text>
    <text class="desc">{desc}</text>
  </view>
</template>

<script setup lang="uts">
  // {title} page
</script>

<style scoped>
  .container {{
    flex: 1;
    justify-content: center;
    align-items: center;
  }}
  
  .title {{
    font-size: 36rpx;
    font-weight: bold;
    color: #333333;
  }}
  
  .desc {{
    font-size: 28rpx;
    color: #999999;
    margin-top: 10rpx;
  }}
</style>
'''
        with open(os.path.join(page_dir, f"{page_name}.uvue"), "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new uni-app x project")
    parser.add_argument("name", help="Project name")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    parser.add_argument("-t", "--template", choices=["default", "tabbar", "subpackage"], default="default", help="Project template")
    
    args = parser.parse_args()
    create_project(args.name, args.output, args.template)
