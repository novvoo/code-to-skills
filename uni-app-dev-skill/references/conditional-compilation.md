# Conditional Compilation Reference

## Overview

Conditional compilation is a core feature of uni-app that allows developers to include platform-specific code within the same source file. During compilation, code that doesn't match the target platform is automatically removed, resulting in **zero runtime overhead**.

This is essential for cross-platform development because:
1. Different platforms have different APIs and capabilities
2. Some features only exist on specific platforms
3. Performance optimizations may differ per platform
4. UI/UX conventions vary across platforms

## Syntax

### JavaScript/UTS
```uts
// #ifdef PLATFORM
/* platform-specific code */
// #endif

// #ifndef PLATFORM
/* code for all platforms EXCEPT this one */
// #endif
```

### Template (HTML/uvue)
```html
<!-- #ifdef PLATFORM -->
<view>Platform-specific content</view>
<!-- #endif -->

<!-- #ifndef PLATFORM -->
<view>Content for all platforms except this one</view>
<!-- #endif -->
```

### CSS
```css
/* #ifdef PLATFORM */
.platform-class { color: red; }
/* #endif */

/* #ifndef PLATFORM */
.not-platform-class { color: blue; }
/* #endif */
```

### JSON (pages.json / manifest.json)
```json
{
  "style": {
    "navigationBarTitleText": "Default Title",
    /* #ifdef APP-PLUS */
    "navigationBarBackgroundColor": "#007AFF",
    /* #endif */
    /* #ifdef H5 */
    "navigationBarBackgroundColor": "#FFFFFF",
    /* #endif */
    "app-plus": {}
  }
}
```

## Platform Identifiers

### App Platforms
| Identifier | Description |
|:-|:-|
| APP-PLUS | App platform (Android + iOS) |
| APP-ANDROID | Android only |
| APP-IOS | iOS only |
| APP-HARMONY | HarmonyOS only |
| APP | Same as APP-PLUS |
| APP-UVUE | uni-app x native rendering (Android + iOS) |
| APP-NVUE | uni-app nvue native rendering |

### Web Platform
| Identifier | Description |
|:-|:-|
| H5 | Web (browser) platform |

### Mini Program Platforms
| Identifier | Description |
|:-|:-|
| MP | Any mini program platform |
| MP-WEIXIN | WeChat Mini Program |
| MP-ALIPAY | Alipay Mini Program |
| MP-BAIDU | Baidu Mini Program |
| MP-TOUTIAO | Toutiao/Douyin Mini Program |
| MP-QQ | QQ Mini Program |
| MP-KUAISHOU | Kuaishou Mini Program |
| MP-JD | JD Mini Program |
| MP-LARK | Lark/Feishu Mini Program |
| MP-XHS | Xiaohongshu Mini Program |

### Project Type
| Identifier | Description |
|:-|:-|
| UNI-APP-X | uni-app x project (vs uni-app) |

## Combining Platforms

Use `||` (OR) operator to target multiple platforms:

```uts
// #ifdef APP-ANDROID || APP-IOS
// Code for Android OR iOS
// #endif

// #ifdef APP-ANDROID || APP-IOS || WEB || MP-WEIXIN || APP-HARMONY
// Code for most platforms
// #endif

// #ifndef MP-WEIXIN
// Code for all platforms EXCEPT WeChat
// #endif
```

**Important:** Only `||` (OR) is supported. `&&` (AND) is NOT supported.

## Complete Usage Examples

### 1. Platform-Specific API Calls

```uts
// #ifdef APP-ANDROID
import Build from 'android.os.Build'
console.log('Device model:', Build.MODEL)
// #endif

// #ifdef APP-IOS
import UIDevice from 'UIKit.UIDevice'
console.log('Device model:', UIDevice.current.model)
// #endif

// #ifdef H5
console.log('User Agent:', navigator.userAgent)
// #endif

// #ifdef MP-WEIXIN
const systemInfo = wx.getSystemInfoSync()
console.log('WeChat version:', systemInfo.version)
// #endif
```

### 2. Platform-Specific UI Components

```html
<template>
  <view class="container">
    <!-- Common content for all platforms -->
    <text>Common content</text>
    
    <!-- Android-specific layout -->
    <!-- #ifdef APP-ANDROID -->
    <view class="android-specific">
      <text>Android feature</text>
    </view>
    <!-- #endif -->
    
    <!-- iOS-specific layout -->
    <!-- #ifdef APP-IOS -->
    <view class="ios-specific">
      <text>iOS feature</text>
    </view>
    <!-- #endif -->
    
    <!-- Web-specific layout -->
    <!-- #ifdef H5 -->
    <view class="web-specific">
      <a href="/about">About</a>
    </view>
    <!-- #endif -->
    
    <!-- Mini Program specific -->
    <!-- #ifdef MP-WEIXIN -->
    <button open-type="share">Share to Friends</button>
    <!-- #endif -->
    
    <!-- All App platforms -->
    <!-- #ifdef APP-PLUS -->
    <view class="app-only">
      <text>Native app feature</text>
    </view>
    <!-- #endif -->
  </view>
</template>
```

### 3. Platform-Specific Styles

```css
/* Common styles */
.container {
  padding: 20rpx;
}

/* #ifdef APP-PLUS */
.container {
  padding-top: env(safe-area-inset-top);
}
/* #endif */

/* #ifdef H5 */
.container {
  max-width: 750px;
  margin: 0 auto;
  cursor: pointer;
}
/* #endif */

/* #ifdef MP-WEIXIN */
.container {
  -webkit-overflow-scrolling: touch;
}
/* #endif */

/* #ifdef APP-ANDROID */
.text {
  font-family: "Roboto";
}
/* #endif */

/* #ifdef APP-IOS */
.text {
  font-family: "PingFang SC";
}
/* #endif */
```

### 4. Platform-Specific Code Logic

```uts
function getPlatformInfo(): string {
  // #ifdef APP-ANDROID
  return 'Android Native App'
  // #endif
  
  // #ifdef APP-IOS
  return 'iOS Native App'
  // #endif
  
  // #ifdef H5
  return 'Web Application'
  // #endif
  
  // #ifdef MP-WEIXIN
  return 'WeChat Mini Program'
  // #endif
  
  // #ifdef APP-HARMONY
  return 'HarmonyOS App'
  // #endif
  
  return 'Unknown Platform'
}
```

### 5. Platform-Specific Component Import

```html
<template>
  <view>
    <!-- #ifdef APP-PLUS -->
    <map :latitude="lat" :longitude="lng" :markers="markers" :scale="15" />
    <!-- #endif -->
    
    <!-- #ifdef H5 -->
    <iframe :src="mapUrl" style="width:100%;height:300px;"></iframe>
    <!-- #endif -->
    
    <!-- #ifdef MP-WEIXIN -->
    <map :latitude="lat" :longitude="lng" :markers="markers" :scale="15" show-location />
    <!-- #endif -->
  </view>
</template>
```

### 6. Platform-Specific Configuration in pages.json

```json
{
  "pages": [
    {
      "path": "pages/index/index",
      "style": {
        "navigationBarTitleText": "Home",
        "app-plus": {
          "titleNView": {
            "buttons": [
              { "text": "Scan", "float": "right" }
            ]
          }
        },
        "h5": {
          "titleNView": false
        },
        "mp-weixin": {
          "navigationStyle": "custom"
        }
      }
    }
  ]
}
```

### 7. Distinguishing uni-app x from uni-app

```uts
// #ifdef UNI-APP-X
// Code specific to uni-app x project
// Uses UTS language features
// #endif

// #ifndef UNI-APP-X
// Code specific to uni-app project
// Uses JavaScript features
// #endif
```

### 8. Native Rendering vs WebView Rendering

```css
/* #ifdef APP-UVUE || APP-NVUE */
/* Native rendering styles */
.text {
  /* Must specify all text styles directly */
  color: #333333;
  font-size: 28rpx;
}
/* #endif */

/* #ifndef APP-UVUE || APP-NVUE */
/* WebView rendering styles */
.text {
  /* Can use inheritance */
  color: inherit;
}
/* #endif */
```

## Rules and Limitations

1. **Must use exact syntax** - `// #ifdef`, `// #endif`, `<!-- #ifdef -->`, `/* #ifdef */`
2. **Case sensitive** - Platform identifiers must be uppercase
3. **Cannot nest** - Conditional compilation blocks cannot be nested
4. **Must be properly closed** - Every `#ifdef` must have a matching `#endif`
5. **Works in all file types** - .uts, .uvue, .css, .json
6. **OR operator only** - Use `||` for combining, `&&` is NOT supported
7. **No else clause** - Use `#ifndef` for the "else" case
8. **Compile-time only** - Code is removed at build time, no runtime check
9. **No partial expressions** - Must wrap complete statements/blocks
10. **JSON comments** - JSON conditional compilation uses `/* */` style comments (non-standard JSON)

## Runtime Platform Detection

For cases where compile-time conditional compilation isn't suitable, use runtime detection:

```uts
// Get platform at runtime
const systemInfo = uni.getSystemInfoSync()
const platform = systemInfo.platform  // 'android', 'ios', 'devtools'

switch (platform) {
  case 'android':
    console.log('Running on Android')
    break
  case 'ios':
    console.log('Running on iOS')
    break
  default:
    console.log('Running in developer tools')
    break
}

// Check environment
if (process.env.NODE_ENV === 'development') {
  console.log('Development mode')
} else {
  console.log('Production mode')
}
```

**Note:** Prefer compile-time conditional compilation over runtime detection for better performance and smaller bundle size.

## Debugging Tips

1. Use `console.log` inside conditional blocks to verify which platform code runs
2. Check compiled output to ensure correct code is included
3. Test on all target platforms regularly
4. Use `#ifndef` sparingly - explicit `#ifdef` is clearer
5. Keep platform-specific code minimal - maximize shared code
6. When using conditional compilation in JSON, remember that standard JSON doesn't support comments - HBuilderX's compiler handles this specially
