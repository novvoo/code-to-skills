---
name: uni-app-dev
version: "2.0.0"
author: DCloud uni-app Source Analysis
description: >
  uni-app / uni-app x 跨平台应用开发专家。基于 DCloud 官方 uni-app 源码深度分析构建，提供项目搭建、组件开发、API 集成、UTS 语言、条件编译、插件开发、性能优化、多端部署等全方位指导。
  Activate when users need help with: uni-app, uni-app x, UTS, uvue, DCloud, HBuilderX, cross-platform development,
  WeChat mini-program, HarmonyOS development, conditional compilation, pages.json, manifest.json, uni_modules,
  easycom, list-view, scroll-view, native plugin, native component, Draw API, native-view, rpx, App.uvue,
  onLaunch, onLoad, uni.navigateTo, uni.request, uni.showToast, uni.getSystemInfoSync, 跨平台开发, 小程序开发,
  微信小程序, 鸿蒙开发, 条件编译, 原生插件, 原生组件, 跨端适配, 多端发布
keywords:
  - uni-app
  - uni-app x
  - uvue
  - UTS
  - DCloud
  - HBuilderX
  - cross-platform
  - mini-program
  - WeChat
  - HarmonyOS
  - conditional-compilation
  - native-plugin
  - Draw-API
  - easycom
  - list-view
  - 跨平台开发
  - 小程序开发
  - 鸿蒙开发
  - 原生插件
  - 多端发布
tags:
  - mobile-development
  - cross-platform
  - uni-app
  - mini-program
  - native
  - uts
  - dcloud
---

# uni-app 跨平台开发专家 / uni-app Development Expert

## Capabilities / 核心能力

1. **Project Scaffolding / 项目脚手架** - Creating and configuring uni-app / uni-app x projects (创建和配置项目)
2. **Component Development / 组件开发** - Using built-in components and creating custom components with easycom (内置组件使用 + easycom 自定义组件)
3. **API Integration / API 集成** - Using uni.xxx APIs for networking, storage, media, device access (网络/存储/媒体/设备等 50+ API)
4. **UTS Language / UTS 语言** - Writing type-safe code with UTS, understanding TS-to-UTS migration pitfalls (UTS 强类型编程 + TS 迁移陷阱)
5. **Conditional Compilation / 条件编译** - Platform-specific code with #ifdef / #ifndef across all file types (跨文件类型平台差异化代码)
6. **Configuration / 配置管理** - pages.json, manifest.json, App.uvue, and other project configuration (项目配置文件完整参考)
7. **Cross-Platform Deployment / 多端部署** - Building for Web, Android, iOS, WeChat Mini Program, HarmonyOS (Web/Android/iOS/小程序/鸿蒙)
8. **Performance Optimization / 性能优化** - DOM minimization, list virtualization, Draw API, layout optimization (DOM 最小化/虚拟列表/Draw API/布局优化)
9. **Plugin Development / 插件开发** - Creating UTS API plugins and UTS component plugins (UTS API 插件 + UTS 组件插件，标准模式 & 兼容模式)
10. **State Management / 状态管理** - Reactive store pattern, globalData, provide/inject (reactive 全局状态/globalData/provide+inject)
11. **DOM Manipulation / DOM 操作** - UniElement, Draw API, SelectorQuery, IntersectionObserver (元素获取/高性能绘制/选择器查询/可见性检测)
12. **Debugging & Troubleshooting / 调试排错** - Common UTS compilation errors, runtime issues, platform quirks (UTS 编译错误/运行时问题/平台差异)

## Core Knowledge Base

### Project Structure

A typical uni-app x project structure:

```
project-root/
├── pages/                    # Page files (.uvue)
│   ├── index/
│   │   └── index.uvue        # Home page
│   └── detail/
│       └── detail.uvue       # Detail page
├── static/                   # Static assets (copied as-is to build output)
├── components/               # Custom components (auto-imported via easycom)
├── store/                    # State management (reactive modules)
│   └── index.uts             # Global state
├── api/                      # API request modules
├── utils/                    # Utility functions
├── App.uvue                  # App root component (lifecycle, globalData, global styles)
├── main.uts                  # App entry file
├── pages.json                # Page routing & navigation config
├── manifest.json             # App manifest config (platform-specific settings)
├── uni.scss                  # Global style variables
└── uni_modules/              # UTS plugins (each is a self-contained module)
    └── my-plugin/
        ├── package.json
        ├── utssdk/
        │   ├── interface.uts         # Cross-platform API declaration
        │   ├── app-android/          # Android implementation
        │   ├── app-ios/              # iOS implementation
        │   ├── app-harmony/          # HarmonyOS implementation
        │   └── web/                  # Web implementation
        └── components/               # UTS component files
```

### App.uvue - Application Root

App.uvue is the application entry point. It does NOT have a `<template>` section. It supports:

1. **Application Lifecycle** - onLaunch, onAppShow, onAppHide, onExit, onError, onLastPageBackPress
2. **Global Data** - globalData object accessible via `getApp().globalData`
3. **Global Methods** - Methods accessible via `getApp().vm?.methodName()`
4. **Global Styles** - CSS that applies to all pages

```vue
<script setup lang="uts">
import { state, updateGlobalData, setLifeCycleNum } from '@/store/index.uts'

// #ifdef APP-ANDROID || APP-HARMONY
let firstBackTime = 0
// #endif

onLaunch((res : OnLaunchOptions) => {
  console.log('App Launch', res.path)
  updateGlobalData('launchOptions', res)
})

onAppShow((options : OnShowOptions) => {
  console.log('App Show', options.path)
})

onAppHide(() => {
  console.log('App Hide')
})

// #ifdef APP-ANDROID || APP-HARMONY
onLastPageBackPress(() => {
  if (firstBackTime == 0) {
    uni.showToast({ title: '再按一次退出应用', position: 'bottom' })
    firstBackTime = Date.now()
    setTimeout(() => { firstBackTime = 0 }, 2000)
  } else if (Date.now() - firstBackTime < 2000) {
    uni.exit()
  }
})

onExit(() => {
  console.log('App Exit')
  // Clean up event listeners here to avoid memory leaks
})
// #endif

onError((err : any) => {
  console.error('App Error', err)
})

defineExpose({
  increaseLifeCycleNum: () => {
    setLifeCycleNum(state.lifeCycleNum + 100)
  }
})
</script>

<style>
  @import "./common/uni.css";
  /* Global styles apply to all pages */
  .global-text { color: #007AFF; font-size: 18px; font-weight: bold; }
</style>
```

**Important Notes:**
- Application lifecycle can ONLY be listened to in App.uvue, not in pages
- `getApp()` returns a `UniApp` type; call methods via `getApp().vm?.methodName()`
- globalData structure is defined by initial values; cannot add/delete properties later
- onExit must clean up on/off event listeners to prevent memory leaks (Android hot-exit)

### Page File (.uvue) Structure

Each page follows Vue SFC specification with UTS:

```vue
<template>
  <view class="content">
    <text>{{ title }}</text>
    <button @click="handleClick">Click Me</button>
  </view>
</template>

<script setup lang="uts">
  // Composition API with UTS
  const title = ref("Hello uni-app x")
  
  const handleClick = () : void => {
    console.log("Button clicked")
  }
  
  onLoad((options : OnLoadOptions) => {
    console.log("Page loaded with options:", options)
  })
  
  onReady(() => {
    console.log("Page ready, DOM is available")
  })
</script>

<style>
  .content {
    width: 750rpx;
    background-color: #ffffff;
  }
</style>
```

### Page Lifecycle

| Composition API | Options API | Description |
|:-|:-|:-|
| onLoad | onLoad | Page loaded, receive URL parameters |
| onPageShow | onShow | Page becomes visible |
| onReady | onReady | Page initial render complete |
| onPageHide | onHide | Page hidden |
| onUnload | onUnload | Page unloaded |
| onPullDownRefresh | onPullDownRefresh | Pull-down refresh triggered |
| onReachBottom | onReachBottom | Reach page bottom |
| onPageScroll | onPageScroll | Page scroll event |
| onResize | onResize | Page size changed |
| onBackPress | onBackPress | Back button pressed (return true to prevent) |

**CRITICAL:** In Composition API, `onShow` becomes `onPageShow` and `onHide` becomes `onPageHide`. This is different from Options API!

Lifecycle flow: pages.json config → DOM creation → onLoad → onShow (transition animation starts) → onReady → transition animation ends

**Props and onLoad:** When a page receives URL parameters AND has props defined, the props will receive the URL parameters. Both `onLoad(options)` and `props.title` will work.

### Conditional Compilation

Use preprocessor directives for platform-specific code:

```
// In template
<!-- #ifdef APP -->
<view>App-only content</view>
<!-- #endif -->

<!-- #ifdef H5 -->
<view>H5-only content</view>
<!-- #endif -->

<!-- #ifdef MP-WEIXIN -->
<view>WeChat Mini Program only</view>
<!-- #endif -->

// In script/UTS
// #ifdef APP
console.log("Running on native app")
// #endif

// #ifndef H5
console.log("Not running on H5")
// #endif

// Combine with OR operator
// #ifdef APP-ANDROID || APP-IOS
console.log("Running on Android or iOS")
// #endif

/* In style */
/* #ifdef APP */
.app-only { color: red; }
/* #endif */

/* In JSON (pages.json / manifest.json) */
/* #ifdef APP-PLUS */
"navigationBarBackgroundColor": "#007AFF",
/* #endif */
```

Platform identifiers:
- APP / APP-PLUS: Native app (Android + iOS)
- APP-ANDROID: Android only
- APP-IOS: iOS only
- APP-HARMONY: HarmonyOS only
- H5: Web browser
- MP / MP-WEIXIN: WeChat Mini Program
- MP-ALIPAY: Alipay Mini Program
- MP-BAIDU: Baidu Mini Program
- MP-TOUTIAO: Toutiao Mini Program
- MP-QQ: QQ Mini Program
- WEB: Web platform (H5 + Mini Programs)
- UNI-APP-X: uni-app x project type (vs uni-app)

**Rules:**
- Only `||` (OR) operator supported for combining platforms, no `&&`
- Cannot nest conditional compilation blocks
- Must use exact syntax: `// #ifdef`, `// #endif`, `<!-- #ifdef -->`, `/* #ifdef */`
- Case sensitive - platform identifiers must be uppercase
- Compile-time only - code is removed at build time, zero runtime overhead

### Built-in Components

**Basic Components:**
- `<view>`: Container component (like div). Type: UniViewElement
- `<text>`: Text display. MUST wrap text content, no direct text in view. Type: UniTextElement
- `<image>`: Image display with mode (aspectFit/aspectFill/etc). Type: UniImageElement
- `<button>`: Button with built-in styles and types (primary/default/warn)
- `<input>`: Single-line input. Type: UniInputElement
- `<textarea>`: Multi-line input. Type: UniTextAreaElement
- `<scroll-view>`: Scrollable container with scroll events
- `<swiper>` / `<swiper-item>`: Carousel/slider with autoplay
- `<list-view>` / `<list-item>`: High-performance virtual scrolling list
- `<grid-view>`: Virtual scrolling grid layout
- `<waterflow>` / `<flow-item>`: Waterfall/masonry layout

**Form Components:**
- `<checkbox>` / `<checkbox-group>`: Checkboxes
- `<radio>` / `<radio-group>`: Radio buttons
- `<picker>`: Selector (date/time/region/custom)
- `<picker-view>` / `<picker-view-column>`: Custom picker
- `<slider>`: Slider
- `<switch>`: Toggle switch
- `<form>`: Form container
- `<label>`: Form label

**Navigation & Layout:**
- `<navigator>`: Page navigation link
- `<tabbar>`: Tab bar
- `<navigation-bar>`: Navigation bar
- `<sticky>` / `<sticky-header>` / `<sticky-section>`: Sticky positioning

**Media Components:**
- `<video>`: Video player
- `<camera>`: Camera
- `<map>`: Map
- `<canvas>`: Canvas drawing
- `<web-view>`: Embedded web page
- `<audio>`: Audio playback
- `<animation-view>`: Lottie animation

**Advanced Components (uni-app x):**
- `<native-view>`: Bridge for embedding native views (key for UTS component development)
- `<movable-area>` / `<movable-view>`: Draggable elements
- `<cover-view>` / `<cover-image>`: Overlay on native components
- `<rich-text>`: Rich text rendering
- `<progress>`: Progress bar
- `<snapshot>`: Screenshot component
- `<page-container>`: Page popup container
- `<root-portal>`: Portal rendering
- `<share-element>`: Shared element transition
- `<open-container>`: Container with open/close animation
- `<draggable-sheet>`: Draggable bottom sheet

**List Performance Components (uni-app x):**
- `<list-view>`: Virtual scrolling list (MUST use for long lists, never scroll-view + v-for)
- `<list-item>`: List item with recycling support
- `<list-builder>`: Builder pattern list
- `<grid-view>`: Virtual scrolling grid
- `<grid-builder>`: Builder pattern grid
- `<waterflow>`: Waterfall layout
- `<nested-scroll>` / `<nested-scroll-header>` / `<nested-scroll-body>`: Nested scrolling

**Gesture Components (uni-app x):**
- `<tap-gesture-handler>`: Tap gesture
- `<double-tap-gesture-handler>`: Double tap
- `<long-press-gesture-handler>`: Long press
- `<pan-gesture-handler>`: Pan/drag gesture
- `<scale-gesture-handler>`: Pinch/scale gesture
- `<force-press-gesture-handler>`: Force press (iOS)
- `<horizontal-drag-gesture-handler>`: Horizontal drag
- `<vertical-drag-gesture-handler>`: Vertical drag

### Key APIs

**Navigation:**
- `uni.navigateTo({ url })`: Navigate to new page (can go back)
- `uni.redirectTo({ url })`: Redirect (replace current page)
- `uni.reLaunch({ url })`: Restart to a page
- `uni.switchTab({ url })`: Switch to tab page
- `uni.navigateBack({ delta })`: Go back delta pages

**Networking:**
- `uni.request({ url, method, data, header, success, fail })`: HTTP request
- `uni.uploadFile({ url, filePath, name })`: Upload file
- `uni.downloadFile({ url })`: Download file
- `uni.connectSocket({ url })`: WebSocket connection

**Storage:**
- `uni.setStorageSync(key, data)`: Sync set storage
- `uni.getStorageSync(key)`: Sync get storage
- `uni.removeStorageSync(key)`: Sync remove storage
- `uni.clearStorageSync()`: Sync clear storage

**UI Feedback:**
- `uni.showToast({ title, icon })`: Show toast
- `uni.showLoading({ title })`: Show loading
- `uni.hideLoading()`: Hide loading
- `uni.showModal({ title, content })`: Show modal dialog
- `uni.showActionSheet({ itemList })`: Show action sheet

**Media:**
- `uni.chooseImage({ count, sourceType })`: Choose image
- `uni.previewImage({ urls, current })`: Preview images
- `uni.chooseVideo({ sourceType })`: Choose video
- `uni.saveImageToPhotosAlbum({ filePath })`: Save to album

**Device:**
- `uni.getSystemInfoSync()`: Get system info
- `uni.getWindowInfo()`: Get window info (statusBarHeight, safeArea, etc.)
- `uni.getDeviceInfo()`: Get device info
- `uni.getNetworkType()`: Get network type
- `uni.makePhoneCall({ phoneNumber })`: Make phone call
- `uni.scanCode({ scanType })`: Scan QR/barcode
- `uni.getLocation({ type })`: Get location
- `uni.vibrateShort()`: Short vibration

**DOM Access (uni-app x):**
- `uni.getElementById(id)`: Get UniElement by ID
- `uni.createSelectorQuery()`: Selector query for layout info
- `uni.createIntersectionObserver()`: Intersection observer for visibility detection

**Page:**
- `uni.pageScrollTo({ scrollTop, duration })`: Scroll to position
- `uni.startPullDownRefresh()`: Start pull-down refresh
- `uni.stopPullDownRefresh()`: Stop pull-down refresh
- `getCurrentPages()`: Get page stack

### State Management

uni-app x does NOT support Pinia or Vuex. Use the reactive store pattern:

```uts
// store/index.uts
export type State = {
  globalNum: number
  userInfo: UserInfo | null
  isDarkMode: boolean
}

export const state = reactive({
  globalNum: 0,
  userInfo: null as UserInfo | null,
  isDarkMode: false
} as State)

export const setGlobalNum = (num : number) : void => {
  state.globalNum = num
}

export const setUserInfo = (info : UserInfo | null) : void => {
  state.userInfo = info
}
```

Usage in pages:
```vue
<script setup lang="uts">
import { state, setGlobalNum } from '@/store/index.uts'

// Read state directly (reactive)
const count = computed(() => state.globalNum)

// Modify state via exported functions
const increment = () : void => {
  setGlobalNum(state.globalNum + 1)
}
</script>
```

Alternative: globalData in App.uvue:
```uts
// Access via getApp()
const app = getApp()
const str = app.globalData.str
app.globalData.str = 'new value'
```

### UTS Plugin Development

#### API Plugin Structure
```
uni_modules/my-api-plugin/
├── package.json
├── utssdk/
│   ├── interface.uts          # Cross-platform API declaration
│   ├── index.uts              # Web implementation (optional)
│   ├── app-android/
│   │   ├── index.uts          # Android implementation
│   │   ├── config.json        # Android dependencies config
│   │   ├── libs/              # jar/aar/so files
│   │   ├── assets/            # Android assets
│   │   ├── res/               # Android resources
│   │   └── AndroidManifest.xml # Android manifest entries
│   ├── app-ios/
│   │   ├── index.uts          # iOS implementation
│   │   └── Info.plist         # iOS plist entries
│   └── app-harmony/
│       ├── index.uts          # HarmonyOS implementation
│       └── module.json5       # HarmonyOS module config
└── readme.md
```

#### interface.uts - API Declaration
```uts
export function getBatteryLevel() : number
export function showToast(msg : string) : void
export type BatteryInfo = {
  level : number;
  isCharging : boolean;
}
export function getBatteryInfo() : BatteryInfo
```

#### Android Implementation Example
```uts
// utssdk/app-android/index.uts
import BatteryManager from 'android.os.BatteryManager'
import Context from 'android.content.Context'

export function getBatteryLevel() : number {
  const context = UTSAndroid.getAppContext()!
  const manager = context.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
  return manager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
}

export function getBatteryInfo() : BatteryInfo {
  const context = UTSAndroid.getAppContext()!
  const manager = context.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
  return {
    level: manager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY),
    isCharging: manager.isCharging()
  } as BatteryInfo
}
```

#### iOS Implementation Example
```uts
// utssdk/app-ios/index.uts
import UIDevice from 'UIKit.UIDevice'

export function getBatteryLevel() : number {
  UIDevice.current.isBatteryMonitoringEnabled = true
  return UIDevice.current.batteryLevel * 100
}
```

#### UTS Component Plugin (Standard Mode - HBuilderX 4.31+)

Standard mode uses `<native-view>` component to bridge native views:

```vue
<!-- components/my-button/my-button.uvue -->
<template>
  <native-view ref="nativeView" :init="onNativeViewInit" @click="onClick"></native-view>
</template>

<script setup lang="uts">
import { MyNativeButton } from '../../utssdk/index.uts'

const nativeView = ref<UniNativeViewElement | null>(null)
let nativeButton : MyNativeButton | null = null

const onNativeViewInit = (e : UniNativeViewInitEvent) => {
  nativeButton = new MyNativeButton(e.element)
}

const onClick = (e : UniNativeViewEvent) => {
  console.log('Button clicked')
}

defineExpose({
  updateText: (text : string) => {
    nativeButton?.updateText(text)
  }
})
</script>
```

Android implementation:
```uts
// utssdk/app-android/index.uts
import Button from 'android.widget.Button'
import View from 'android.view.View'

export class MyNativeButton {
  element : UniNativeViewElement
  button : Button
  
  constructor(element : UniNativeViewElement) {
    this.element = element
    this.button = new Button(element.getAndroidContext())
    element.bindAndroidView(this.button)
    this.button.setText("Click Me")
  }
  
  updateText(text : string) : void {
    this.button.setText(text)
  }
}
```

### UTS vs TypeScript - Critical Differences

When migrating from TypeScript to UTS, be aware of these critical constraints:

**1. No undefined - use null instead**
```uts
// WRONG (TS style)
let value: string | undefined
// CORRECT (UTS)
let value: string | null = null
```

**2. Conditions must be boolean**
```uts
// WRONG
if (1) { }
while ("") { }
const value = arr || []
// CORRECT
if (x > 0) { }
while (isValid) { }
const value = arr != null ? arr : []
```

**3. Object literals default to UTSJSONObject - use type**
```uts
// WRONG - inferred as UTSJSONObject
const person = { name: "John", age: 30 }
console.log(person.name) // Error!

// CORRECT - use type definition
type Person = { name: string; age: number }
const person: Person = { name: "John", age: 30 }
console.log(person.name) // OK
```

**4. Use type instead of interface for object literals**
```uts
// WRONG
interface Person { name: string }
const p: Person = { name: "John" } // Error!

// CORRECT
type Person = { name: string }
const p: Person = { name: "John" } // OK
```

**5. No variable hoisting - declare before use**
```uts
// WRONG
foo() // Error: used before declaration
function foo() { }

// CORRECT
function foo() { }
foo()
```

**6. No nested object types in type definitions**
```uts
// WRONG
type News = { author: { name: string } }
// CORRECT
type Author = { name: string }
type News = { author: Author }
```

**7. No index signatures - use class with declared fields**
```uts
// WRONG
class Point { [key: string]: number }
// CORRECT
class Point { x: number = 0; y: number = 0 }
```

**8. No Function.apply/call/bind**
```uts
// WRONG
greet.call(person, "Hello")
// CORRECT
class Person { greet(greeting: string) { } }
let person = new Person()
person.greet("Hello")
```

**9. No generator functions**
```uts
// WRONG
function* counter() { yield 1 }
// CORRECT
async function processItems() { for (let i = 0; i < 5; i++) { await process(i) } }
```

**10. No delete operator - use null assignment**
```uts
// WRONG
delete person.age
// CORRECT
person.age = null
```

**11. No as const, no utility types (Partial, Required, etc.)**
```uts
// WRONG
let x = "hello" as const
type UserUpdate = Partial<User>
// CORRECT
let x: string = "hello"
type UserUpdate = { id?: number; name?: string }
```

**12. throw only Error instances**
```uts
// WRONG
throw "error message"
throw 404
// CORRECT
throw new Error("error message")
```

**13. Array out-of-bounds throws exception on native (not undefined)**
```uts
let arr: number[] = [1, 2, 3]
console.log(arr[5]) // Kotlin/Swift: throws IndexOutOfBoundsException
// Always check bounds first
if (index >= 0 && index < arr.length) { console.log(arr[index]) }
```

**14. Class inheritance requires explicit constructor**
```uts
// WRONG
class Child extends Parent { }
// CORRECT
class Child extends Parent {
  constructor() { super() }
}
```

**15. No prototype modification, no # private fields**
```uts
// WRONG
C.prototype.method = function() { }
class C { #foo = 42 }
// CORRECT
class C { private foo: number = 42 }
```

### DOM Manipulation & Draw API

uni-app x provides DOM access for two key scenarios:

**1. Gesture-driven animations (skip Vue diff for 16ms frame budget)**
```uts
const element = uni.getElementById('box')!
element.style.setProperty('transform', `translate(${x}px, ${y}px)`)
```

**2. Draw API for high-performance custom rendering**
```vue
<template>
  <view id="drawableView" class="drawableView" @click="drawLine"></view>
</template>

<script setup lang="uts">
const drawLine = () : void => {
  const element = uni.getElementById('drawableView')!
  const ctx = element.getDrawableContext()!
  ctx.reset()
  ctx.strokeStyle = "#FF0000"
  ctx.lineWidth = 10
  ctx.moveTo(50, 40)
  ctx.lineTo(200, 40)
  ctx.stroke()
  ctx.update()
}
</script>
```

### Performance Optimization

**1. Minimize DOM count and depth**
- Android is extremely sensitive to DOM count
- Use Draw API for complex custom rendering (calendar, slider, etc.)
- Example: uni-app x's slider component went from 7 views to 1 view using Draw API

**2. Use list-view for long lists**
- NEVER use scroll-view + v-for for large datasets
- list-view provides virtual scrolling with item recycling
- Keep list item components simple - avoid deep component nesting in list items

**3. Optimize layout efficiency**
- Specify explicit width/height when possible (reduces layout passes)
- Use px > rpx > % for CSS unit performance
- Specify image dimensions to reduce layout recalculations
- Give text components explicit dimensions (text measurement is expensive)

**4. Control Vue update scope**
- Separate frequently-updated data from large static data
- Extract interactive parts (like favorite button) into separate components to avoid full list re-render

**5. Avoid unnecessary component abstraction in lists**
- In a 100-item list, removing one component wrapper saves 100 instances
- Don't wrap basic components (view, text) in custom components

**6. Use onReady for DOM operations**
- onLoad: DOM not yet rendered, cannot access elements
- onReady: DOM rendered, safe to access elements

**7. HBuilderX performance monitoring**
- Each page shows DOM count, layout passes, render time in console
- Debug mode is slower than release builds

### pages.json Configuration

```json
{
  "globalStyle": {
    "navigationBarBackgroundColor": "#F8F8F8",
    "navigationBarTextStyle": "black",
    "navigationBarTitleText": "My App",
    "backgroundColor": "#ffffff",
    "backgroundColorContent": "#ffffff",
    "enablePullDownRefresh": false
  },
  "pages": [
    {
      "path": "pages/index/index",
      "style": {
        "navigationBarTitleText": "Home",
        "enablePullDownRefresh": true,
        "onReachBottomDistance": 50
      }
    }
  ],
  "tabBar": {
    "color": "#7A7E83",
    "selectedColor": "#3cc51f",
    "backgroundColor": "#ffffff",
    "list": [
      {
        "pagePath": "pages/index/index",
        "iconPath": "static/home.png",
        "selectedIconPath": "static/home-active.png",
        "text": "Home"
      }
    ]
  },
  "subPackages": [
    {
      "root": "pages-sub",
      "pages": [
        { "path": "detail/detail", "style": { "navigationBarTitleText": "Detail" } }
      ]
    }
  ],
  "easycom": {
    "autoscan": true,
    "custom": {
      "^uni-(.*)": "@dcloudio/uni-ui/lib/uni-$1/uni-$1.uvue"
    }
  }
}
```

Key rules:
- First page in `pages` array is the app's home page
- All pages must be registered in `pages` array
- File extensions should NOT be included in path
- Tab bar requires minimum 2, maximum 5 tabs
- Navigation bar height: 44px (excluding status bar)
- Tab bar height: 50px (excluding safe area)
- Use subPackages for code splitting

### CSS Subset (uni-app x)

uni-app x uses a CSS subset (UCSS) with key differences:

**Supported Units:** px, rpx (750rpx = screen width), %, vh/vw

**Key Differences from Web CSS:**
1. Only flex layout and absolute positioning on native
2. Only class selectors (no tag, #id, [attr] selectors)
3. Styles do NOT inherit from parent to child on native
4. Text styles MUST be applied directly to `<text>` component
5. Default layout is flex (not block like web)

**CSS Variables:**
- `--status-bar-height`: Status bar height
- `--window-top`: Navigation bar height + status bar height
- `--window-bottom`: Tab bar height + safe area

**Not Supported on Native:**
- CSS Grid, float, position:sticky
- ::before/::after pseudo-elements
- :hover/:active pseudo-classes (use hover-class on view)
- @keyframes (use animation-view for Lottie)
- CSS filters, backdrop-filter, clip-path

### Component Communication

**Props (Parent to Child):**
```vue
<!-- Parent -->
<ChildComponent :title="pageTitle" :count="itemCount" />

<!-- Child -->
<script setup lang="uts">
const props = defineProps({
  title: { type: String, required: true },
  count: { type: Number, default: 0 }
})
</script>
```

**Events (Child to Parent):**
```vue
<!-- Child -->
<script setup lang="uts">
const emit = defineEmits(['update', 'delete'])
const handleClick = () => {
  emit('update', { id: 1, name: 'updated' })
}
</script>

<!-- Parent -->
<ChildComponent @update="handleUpdate" />
```

**Provide/Inject (Deep Communication):**
```vue
<!-- Ancestor -->
<script setup lang="uts">
provide('theme', 'dark')
provide('getUserInfo', () => userInfo)
</script>

<!-- Descendant -->
<script setup lang="uts">
const theme = inject('theme') as string
const getUserInfo = inject('getUserInfo') as () => UserInfo
</script>
```

**Parent-Child Method Calls:**
```vue
<!-- Parent -->
<script setup lang="uts">
const childRef = ref<ComponentPublicInstance | null>(null)
const callChildMethod = () => {
  childRef.value?.$callMethod('childMethod', 'param')
}
</script>

<!-- Child -->
<script setup lang="uts">
const childMethod = (param : string) => {
  console.log(param)
}
defineExpose({ childMethod })
</script>
```

**IMPORTANT:** In Composition API, child methods are NOT automatically exposed to parent. Must use `defineExpose` to explicitly expose methods.

### Easycom Auto-import

Components matching the pattern are auto-imported:

Convention: `components/组件名称/组件名称.uvue` is auto-imported without manual import.

Custom patterns in pages.json:
```json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "^uni-(.*)": "@dcloudio/uni-ui/lib/uni-$1/uni-$1.uvue"
    }
  }
}
```

### vue vs uvue File Priority

- In uni-app x: `.uvue` takes priority over `.vue`
- In uni-app: only `.vue` is supported
- A `.vue` file with `lang="ts"` can work in both uni-app and uni-app x
- Use `UNI-APP-X` conditional compilation to differentiate project types

### Common Patterns

**Network Request with Loading:**
```uts
async function loadData() {
  uni.showLoading({ title: 'Loading...' })
  try {
    const res = await uni.request({
      url: 'https://api.example.com/data',
      method: 'GET'
    })
    dataList.value = res.data as Item[]
  } catch (e) {
    uni.showToast({ title: 'Failed to load', icon: 'none' })
  } finally {
    uni.hideLoading()
  }
}
```

**Pull-down Refresh:**
```uts
// Enable in pages.json: "enablePullDownRefresh": true
onPullDownRefresh(async () => {
  await refreshData()
  uni.stopPullDownRefresh()
})
```

**Virtual Scrolling List:**
```vue
<template>
  <list-view style="flex: 1" @scrolltolower="loadMore">
    <list-item v-for="item in dataList" :key="item.id">
      <view class="item">
        <text>{{ item.title }}</text>
      </view>
    </list-item>
  </list-view>
</template>
```

**Custom Navigation Bar:**
```json
// pages.json
{ "path": "pages/index/index", "style": { "navigationStyle": "custom" } }
```

```vue
<template>
  <view class="page">
    <view :style="{ height: statusBarHeight + 'px', backgroundColor: '#007AFF' }"></view>
    <view class="nav-bar" :style="{ height: '44px', backgroundColor: '#007AFF' }">
      <text class="nav-title">Custom Title</text>
    </view>
    <view class="content">...</view>
  </view>
</template>

<script setup lang="uts">
const statusBarHeight = ref(0)
onLoad(() => {
  const windowInfo = uni.getWindowInfo()
  statusBarHeight.value = windowInfo.statusBarHeight
})
</script>
```

### Platform Differences Reference

| Feature | APP-Android | APP-iOS | H5 | MP-WEIXIN |
|:-|:-|:-|:-|:-|
| Rendering | Native | Native | WebView | WebView |
| Language | UTS→Kotlin | UTS→Swift | UTS→JS | UTS→JS |
| DOM Access | uni.getElementById | uni.getElementById | document.getElementById | SelectorQuery |
| Navigation Bar | Native | Native | CSS | Native |
| Status Bar | Native | Native | CSS | Native |
| Tab Bar | Native | Native | CSS | Native |
| Network | uni.request | uni.request | fetch/XMLHttpRequest | wx.request |
| Storage | Native | Native | localStorage | wx.storage |
| Engine Size | 7.51M | - | - | - |
| Min Android | Android 5 | - | Chrome 64 | - |
| Min iOS | - | iOS 12 | Safari 11.1 | - |

### Troubleshooting Common Issues

1. **Page not found**: Ensure page is registered in pages.json
2. **Component not rendering**: Check easycom config or manual import
3. **Style not applying**: Verify CSS property is in supported subset; text styles must be on `<text>` directly
4. **API not available on platform**: Check API compatibility table, use conditional compilation
5. **Performance issues on Android**: Reduce DOM count, use list-view, consider Draw API
6. **UTS compilation error "Variable must be initialized"**: All variables must be initialized before use, even with null
7. **UTS error "Object literal default to UTSJSONObject"**: Add explicit type annotation with `type`
8. **Conditions must be boolean**: Replace `if (value)` with `if (value != null)` or `if (value > 0)`
9. **Array index out of bounds**: Always check bounds before accessing arrays on native platforms
10. **Hot reload not working**: Restart dev server, clear build cache in HBuilderX
11. **Memory leak on Android**: Clean up on/off event listeners in onExit lifecycle
12. **Page lifecycle not firing**: Application lifecycle only works in App.uvue, not in pages

## Instructions / 使用指引

When helping users with uni-app development / 协助用户进行 uni-app 开发时：

1. **Always specify the platform / 明确目标平台** - Different platforms have different capabilities. Use conditional compilation when needed. (不同平台能力不同，必要时使用条件编译)
2. **Prefer uni-app x conventions / 优先使用 uni-app x 规范** - Use .uvue files, UTS language, and native components when targeting app platforms. (App 平台优先使用 .uvue 文件和 UTS 语言)
3. **Use list-view for long lists / 长列表必须用 list-view** - NEVER use v-for with scroll-view for large datasets. (禁止 scroll-view + v-for 处理大数据列表)
4. **Check API compatibility / 检查 API 兼容性** - Not all APIs are available on all platforms. Reference the compatibility tables. (不是所有 API 都全端可用，查看兼容性表)
5. **Provide complete code examples / 提供完整代码示例** - Include template, script, and style sections. (包含 template、script、style 完整三段)
6. **Follow pages.json rules / 遵循 pages.json 规则** - All pages must be registered, first page is home page. (所有页面必须注册，第一个是首页)
7. **Use rpx for responsive design / 使用 rpx 响应式设计** - 750rpx equals screen width on all platforms. (750rpx 等于屏幕宽度)
8. **Handle null safety / 处理空安全** - UTS requires explicit null handling with `| null` and `??` operator. No undefined. (UTS 必须显式处理 null，不支持 undefined)
9. **Optimize for native rendering / 优化原生渲染性能** - Minimize DOM depth, use native components when possible. (最小化 DOM 层级，优先使用原生组件)
10. **Test on multiple platforms / 多端测试** - Always verify behavior on Web, Android, iOS, and Mini Programs. (务必在 Web/Android/iOS/小程序上验证)
11. **Use type instead of interface / 用 type 代替 interface** - For object literal types in UTS, always use `type` keyword. (UTS 中对象类型必须用 type 关键字)
12. **Declare before use / 先声明后使用** - No variable hoisting in UTS; all variables and functions must be declared before use. (UTS 无变量提升，必须先声明后使用)
13. **Use defineExpose / 使用 defineExpose** - Child component methods must be explicitly exposed via defineExpose in Composition API. (组合式 API 中子组件方法必须显式暴露)
14. **Use onPageShow/onPageHide / 注意生命周期命名** - In Composition API, onShow→onPageShow, onHide→onPageHide. (组合式 API 中 onShow 改为 onPageShow)
15. **Consider Draw API / 考虑 Draw API** - For complex custom rendering (calendar, chart, etc.), use Draw API instead of many DOM elements. (复杂自定义渲染用 Draw API 代替大量 DOM 元素)

## Reference Files / 参考文档

The `references/` directory contains detailed documentation extracted from the uni-app source code (基于 uni-app 源码深度提取的参考文档):

| File | Description | 描述 |
|:-|:-|:-|
| `components.md` | Complete component reference with props, events, and examples | 完整组件参考：属性、事件、示例 |
| `api-reference.md` | Full API reference with parameters and return types | API 完整参考：参数、返回值、用法 |
| `uts-language.md` | UTS language specification, syntax guide, and TS migration guide | UTS 语言规范、语法指南、TS 迁移 |
| `uts-ts-differences.md` | Complete UTS vs TypeScript differences with error codes and fixes | UTS 与 TS 差异对照：错误码 + 修复方案 |
| `css-reference.md` | Supported CSS properties and values | 支持的 CSS 属性和值 |
| `pages-json.md` | Complete pages.json and manifest.json configuration reference | pages.json 和 manifest.json 完整配置参考 |
| `conditional-compilation.md` | Conditional compilation directives and platform identifiers | 条件编译指令和平台标识符 |
| `plugin-development.md` | UTS plugin development guide (API plugins and component plugins) | UTS 插件开发指南（API 插件 + 组件插件） |
| `performance-optimization.md` | Performance optimization strategies and best practices | 性能优化策略和最佳实践 |
| `dom-api.md` | DOM manipulation, Draw API, and UniElement reference | DOM 操作、Draw API、UniElement 参考 |
