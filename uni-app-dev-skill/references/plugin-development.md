# UTS Plugin Development Guide

## Overview

UTS plugins allow developers to extend uni-app and uni-app x with native capabilities. A single UTS plugin can work across Android, iOS, HarmonyOS, Web, and Mini Programs.

**Key Advantages over Native Language Plugins:**
1. Unified language (UTS) - one language for all platforms
2. Unified development tool (HBuilderX) - no need for Android Studio/Xcode
3. Simple import - regular import, supports tree-shaking
4. Unified debugging - frontend and native code debug together in HBuilderX
5. Supports both uni-app and uni-app x

## Plugin Types

1. **API Plugin** - Extends native API capabilities (e.g., getBatteryInfo, lottie)
2. **Component Plugin** - Extends native UI components (e.g., map, video, custom views)

## API Plugin Development

### Directory Structure

```
uni_modules/my-plugin/
├── package.json              # Plugin metadata
├── readme.md                 # Documentation
├── changelog.md              # Version history
├── utssdk/
│   ├── interface.uts         # Cross-platform API declaration (REQUIRED)
│   ├── index.uts             # Web/MP implementation (optional)
│   ├── app-android/
│   │   ├── index.uts         # Android implementation
│   │   ├── config.json       # Android dependencies
│   │   ├── libs/             # jar/aar/so files
│   │   ├── assets/           # Android assets
│   │   ├── res/              # Android resources
│   │   └── AndroidManifest.xml  # Android manifest entries
│   ├── app-ios/
│   │   ├── index.uts         # iOS implementation
│   │   └── Info.plist        # iOS plist entries
│   └── app-harmony/
│       ├── index.uts         # HarmonyOS implementation
│       ├── module.json5      # HarmonyOS module config
│       └── resources/        # HarmonyOS resources
└── static/                   # Plugin static assets
```

### interface.uts - API Declaration

This file declares the public API that all platforms must implement:

```uts
// Function declarations
export function getBatteryLevel() : number
export function showToast(msg : string) : void

// Type declarations
export type BatteryInfo = {
  level : number;
  isCharging : boolean;
}

export function getBatteryInfo() : BatteryInfo

// Class declarations
export class NativePlayer {
  constructor(url : string)
  play() : void
  pause() : void
  stop() : void
  getDuration() : number
  getCurrentPosition() : number
}
```

### package.json

```json
{
  "id": "my-plugin",
  "displayName": "My Plugin",
  "version": "1.0.0",
  "description": "Plugin description",
  "keywords": ["battery", "native"],
  "repository": "",
  "engines": {
    "HBuilderX": "^3.6.0"
  },
  "dcloudext": {
    "type": "uts",
    "sale": {
      "regular": {
        "price": "0.00"
      }
    },
    "contact": {
      "qq": ""
    },
    "declaration": {
      "ads": "",
      "data": "",
      "permissions": ""
    }
  },
  "uni_modules": {
    "dependencies": [],
    "encrypt": [],
    "platforms": {
      "cloud": {
        "tcb": "y",
        "ali": "y"
      },
      "client": {
        "App": {
          "app-vue": "y",
          "app-vue2": "y",
          "app-uvue": "y",
          "app-harmony": "y"
        },
        "H5-mobile": "y",
        "H5-Pc": "y",
        "MiniProgram": {
          "WeChat": "y",
          "Alipay": "y"
        }
      }
    }
  }
}
```

### Android Implementation

```uts
// utssdk/app-android/index.uts
import BatteryManager from 'android.os.BatteryManager'
import Context from 'android.content.Context'
import Intent from 'android.content.Intent'
import IntentFilter from 'android.content.IntentFilter'

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

export class NativePlayer {
  private mediaPlayer : android.media.MediaPlayer | null = null
  
  constructor(url : string) {
    this.mediaPlayer = new android.media.MediaPlayer()
    this.mediaPlayer!.setDataSource(url)
    this.mediaPlayer!.prepare()
  }
  
  play() : void {
    this.mediaPlayer?.start()
  }
  
  pause() : void {
    this.mediaPlayer?.pause()
  }
  
  stop() : void {
    this.mediaPlayer?.stop()
    this.mediaPlayer?.release()
    this.mediaPlayer = null
  }
  
  getDuration() : number {
    return this.mediaPlayer?.getDuration() ?? 0
  }
  
  getCurrentPosition() : number {
    return this.mediaPlayer?.getCurrentPosition() ?? 0
  }
}
```

### Android config.json

```json
{
  "minSdkVersion": "21",
  "dependencies": [
    "androidx.core:core-ktx:1.6.0",
    "com.google.code.gson:gson:2.8.9"
  ]
}
```

### iOS Implementation

```uts
// utssdk/app-ios/index.uts
import UIDevice from 'UIKit.UIDevice'
import AVFoundation from 'AVFoundation'

export function getBatteryLevel() : number {
  UIDevice.current.isBatteryMonitoringEnabled = true
  return UIDevice.current.batteryLevel * 100
}

export function getBatteryInfo() : BatteryInfo {
  UIDevice.current.isBatteryMonitoringEnabled = true
  return {
    level: UIDevice.current.batteryLevel * 100,
    isCharging: UIDevice.current.batteryState == UIDevice.BatteryState.charging
  } as BatteryInfo
}
```

### HarmonyOS Implementation

```uts
// utssdk/app-harmony/index.uts
import batteryInfo from '@ohos.batteryInfo'

export function getBatteryLevel() : number {
  return batteryInfo.batterySOC
}

export function getBatteryInfo() : BatteryInfo {
  return {
    level: batteryInfo.batterySOC,
    isCharging: batteryInfo.chargingStatus == batteryInfo.BatteryChargeState.ENABLE
  } as BatteryInfo
}
```

### Web Implementation

```uts
// utssdk/index.uts (or utssdk/web/index.uts)
export function getBatteryLevel() : number {
  // Web fallback - may not be available
  return 100
}

export function getBatteryInfo() : BatteryInfo {
  return {
    level: 100,
    isCharging: false
  } as BatteryInfo
}
```

### Using the Plugin

```vue
<script setup lang="uts">
// Direct import - no need for uni.requireNativePlugin
import { getBatteryLevel, getBatteryInfo, NativePlayer } from '@/uni_modules/my-plugin'

const batteryLevel = ref(0)
const batteryInfo = ref<BatteryInfo | null>(null)

onLoad(() => {
  batteryLevel.value = getBatteryLevel()
  batteryInfo.value = getBatteryInfo()
})

let player : NativePlayer | null = null
const playAudio = (url : string) => {
  player = new NativePlayer(url)
  player!.play()
}
</script>
```

## Component Plugin Development

### Standard Mode (HBuilderX 4.31+)

Standard mode uses `<native-view>` component to bridge native views into the uvue page.

**Directory Structure:**
```
uni_modules/my-component/
├── package.json
├── components/
│   └── my-button/
│       └── my-button.uvue     # Vue component wrapping native-view
├── utssdk/
│   ├── interface.uts          # API declaration
│   ├── app-android/
│   │   └── index.uts          # Android native view implementation
│   ├── app-ios/
│   │   └── index.uts          # iOS native view implementation
│   └── app-harmony/
│       └── index.uts          # HarmonyOS native view implementation
└── static/
```

**Component File (my-button.uvue):**
```vue
<template>
  <view class="container">
    <native-view 
      ref="nativeViewRef" 
      :init="onNativeViewInit" 
      @click="onNativeClick"
      style="width: 200rpx; height: 80rpx;"
    ></native-view>
  </view>
</template>

<script setup lang="uts">
import { MyNativeButton } from '../../utssdk/index.uts'

const nativeViewRef = ref<UniNativeViewElement | null>(null)
let nativeButton : MyNativeButton | null = null

const onNativeViewInit = (e : UniNativeViewInitEvent) => {
  nativeButton = new MyNativeButton(e.element)
}

const onNativeClick = (e : UniNativeViewEvent) => {
  console.log('Native button clicked')
}

// Expose methods for parent component
const updateText = (text : string) => {
  nativeButton?.updateText(text)
}

defineExpose({
  updateText
})
</script>

<style>
.container { padding: 10rpx; }
</style>
```

**Android Implementation:**
```uts
// utssdk/app-android/index.uts
import Button from 'android.widget.Button'
import View from 'android.view.View'
import Color from 'android.graphics.Color'
import LinearLayout from 'android.widget.LinearLayout'

export class MyNativeButton {
  element : UniNativeViewElement
  button : Button
  
  constructor(element : UniNativeViewElement) {
    this.element = element
    this.button = new Button(element.getAndroidContext())
    
    // Configure native view
    this.button.setText("Click Me")
    this.button.setTextColor(Color.WHITE)
    this.button.setBackgroundColor(Color.parseColor("#007AFF"))
    
    // Bind native view to element
    element.bindAndroidView(this.button)
  }
  
  updateText(text : string) : void {
    this.button.setText(text)
  }
  
  setOnClickListener(listener : View.OnClickListener) : void {
    this.button.setOnClickListener(listener)
  }
}
```

**iOS Implementation:**
```uts
// utssdk/app-ios/index.uts
import UIButton from 'UIKit.UIButton'
import UIColor from 'UIKit.UIColor'

export class MyNativeButton {
  element : UniNativeViewElement
  button : UIButton
  
  constructor(element : UniNativeViewElement) {
    this.element = element
    this.button = UIButton(type = UIButton.ButtonType.system)
    this.button.setTitle("Click Me", forState = UIControl.State.normal)
    this.button.setTitleColor(UIColor.white, forState = UIControl.State.normal)
    this.button.backgroundColor = UIColor(red = 0, green = 0.478, blue = 1, alpha = 1)
    element.bindIOSView(this.button)
  }
  
  updateText(text : string) : void {
    this.button.setTitle(text, forState = UIControl.State.normal)
  }
}
```

### uni-app Compatible Mode (HBuilderX 3.6.18+)

For plugins that need to work in both uni-app (nvue) and uni-app x. Uses special lifecycle hooks:
- NVBeforeLoad: Before component loads
- NVLoad: Return native view instance
- NVLoaded: Native view loaded
- NVLayouted: Native view layout complete
- NVBeforeUnload: Before unloading
- NVUnloaded: After unloading

This mode is more complex and should only be used when you need uni-app nvue compatibility.

## UTSAndroid / UTSiOS Platform APIs

### UTSAndroid

```uts
import UTSAndroid from 'io.dcloud.uts.UTSAndroid'

// Get application context
const context = UTSAndroid.getAppContext()

// Run on UI thread
UTSAndroid.onUIThread(() => {
  // UI operations must run on main thread
})

// Run on background thread
UTSAndroid.offUIThread(() => {
  // Heavy computation
})

// Get current activity
const activity = UTSAndroid.getUniActivity()

// Request permissions
UTSAndroid.requestSystemPermission(
  activity!,
  ["android.permission.CAMERA"],
  () => { /* granted */ },
  () => { /* denied */ }
)
```

### UTSiOS

```uts
import UTSiOS from 'io.dcloud.uts.UTSiOS'

// Get current ViewController
const vc = UTSiOS.getCurrentViewController()

// Get key window
const window = UTSiOS.getKeyWindow()

// Run on main thread
UTSiOS.onMainThread(() => {
  // UI operations
})
```

## Kotlin to UTS Conversion Guide

When converting Kotlin code to UTS:

| Kotlin | UTS |
|:-|:-|
| `import android.os.Build` | `import Build from 'android.os.Build'` |
| `fun getDeviceModel(): String` | `function getDeviceModel(): string` |
| `val` | `const` |
| `var` | `let` |
| `fun` | `function` |
| `: String` (Kotlin type) | `: string` (UTS type, lowercase) |
| `null` | `null` (same) |
| `!!` (non-null assertion) | `!` (non-null assertion) |
| `as` (cast) | `as` (cast, same) |
| `is` (type check) | `isinstanceof()` or `instanceof` |

## Debugging Tips

1. **Android**: UTS plugins support hot reload and console.log in HBuilderX
2. **iOS (HBuilderX 3.6.9+)**: Supports local compilation and real device debugging
3. **iOS (before 3.6.9)**: Requires cloud packaging for custom base
4. **HarmonyOS**: Currently requires manual operation in DevEco Studio
5. **Compiled output**: Check `unpackage/` directory for generated Kotlin/Swift code
6. **Console logging**: Use `console.log()` in UTS code, outputs to HBuilderX console

## Common Issues

1. **Import error**: Make sure `interface.uts` exports match platform implementations
2. **Type mismatch**: UTS is strictly typed, ensure all types match between interface and implementation
3. **Android dependency conflict**: Use Maven repository instead of local jar/aar when possible
4. **iOS framework not found**: Add framework dependencies in `Info.plist` or implementation
5. **Native view not showing**: Ensure `bindAndroidView()` / `bindIOSView()` is called in constructor
6. **Memory leak**: Always release native resources (MediaPlayer, etc.) when component unloads
