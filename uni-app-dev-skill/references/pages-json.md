# pages.json and manifest.json Configuration Reference

## pages.json

`pages.json` is the core configuration file for uni-app projects. It defines pages, tab bar, navigation bar, and other global settings. It MUST be placed in the project root directory.

**Critical Rule:** All pages MUST be registered in pages.json. Unregistered pages are ignored during compilation and will NOT be included in the build output.

## Complete Structure

```json
{
  "pages": [...],
  "globalStyle": {...},
  "tabBar": {...},
  "condition": {...},
  "subPackages": [...],
  "preloadRule": {...},
  "workers": "...",
  "easycom": {...},
  "uniStatistics": {...},
  "topWindow": {...},
  "leftWindow": {...},
  "rightWindow": {...}
}
```

## pages (Required)

Array of page configurations. **First item is the home page.**

```json
{
  "pages": [
    {
      "path": "pages/index/index",
      "style": {
        "navigationBarTitleText": "Home",
        "navigationBarBackgroundColor": "#007AFF",
        "navigationBarTextStyle": "white",
        "backgroundColor": "#f5f5f5",
        "backgroundTextStyle": "dark",
        "enablePullDownRefresh": true,
        "onReachBottomDistance": 50,
        "disableScroll": false,
        "usingComponents": {},
        "restartStrategy": "homePage",
        "maxWidth": 1190,
        "pageOrientation": "portrait",
        "animationType": "pop-in",
        "animationDuration": 300
      }
    }
  ]
}
```

### Page Style Options

| Property | Type | Default | Description |
|:-|:-|:-|:-|
| navigationBarTitleText | string | - | Navigation bar title text |
| navigationBarBackgroundColor | HexColor | #F7F7F7 | Navigation bar background color |
| navigationBarTextStyle | string | "black" | Navigation bar text color: "black" / "white" |
| backgroundColor | HexColor | #FFFFFF | Page background color |
| backgroundTextStyle | string | "dark" | Pull-down loading style: "dark" / "light" |
| enablePullDownRefresh | boolean | false | Enable pull-down refresh |
| onReachBottomDistance | number | 50 | Distance from bottom to trigger reach-bottom event (px) |
| disableScroll | boolean | false | Disable page scrolling |
| usingComponents | Object | {} | Custom component declarations |
| restartStrategy | string | "homePage" | Restart strategy: "homePage" / "homePageAndLatestPage" |
| maxWidth | number | 1190 | Maximum page width for responsive layout |
| pageOrientation | string | "portrait" | Screen orientation: "portrait" / "landscape" / "auto" |
| animationType | string | "pop-in" | Page enter animation |
| animationDuration | number | 300 | Animation duration (ms) |
| app-plus | Object | {} | App-specific page configuration |
| h5 | Object | {} | H5-specific page configuration |
| mp-weixin | Object | {} | WeChat Mini Program specific configuration |

## globalStyle

Default page style. Individual page styles override globalStyle.

```json
{
  "globalStyle": {
    "navigationBarTextStyle": "black",
    "navigationBarTitleText": "My App",
    "navigationBarBackgroundColor": "#FFFFFF",
    "backgroundColor": "#F8F8F8",
    "backgroundTextStyle": "dark",
    "enablePullDownRefresh": false,
    "maxWidth": 1190,
    "rpxCalcMaxDeviceWidth": 960,
    "rpxCalcBaseDeviceWidth": 375,
    "rpxCalcIncludeWidth": 750
  }
}
```

## tabBar

Tab bar configuration for bottom navigation.

```json
{
  "tabBar": {
    "color": "#999999",
    "selectedColor": "#007AFF",
    "backgroundColor": "#FFFFFF",
    "borderStyle": "black",
    "fontSize": "10px",
    "iconWidth": "24px",
    "height": "50px",
    "spacing": "3px",
    "list": [
      {
        "pagePath": "pages/home/home",
        "text": "Home",
        "iconPath": "static/tab/home.png",
        "selectedIconPath": "static/tab/home-active.png"
      },
      {
        "pagePath": "pages/user/user",
        "text": "My",
        "iconPath": "static/tab/user.png",
        "selectedIconPath": "static/tab/user-active.png"
      }
    ]
  }
}
```

### TabBar Properties

| Property | Type | Required | Description |
|:-|:-|:-|:-|
| color | HexColor | Yes | Tab text color (unselected) |
| selectedColor | HexColor | Yes | Tab text color (selected) |
| backgroundColor | HexColor | Yes | Tab bar background color |
| borderStyle | string | No | Border style: "black" / "white" |
| list | Array | Yes | Tab list (2-5 items) |
| fontSize | string | No | Tab text font size |
| iconWidth | string | No | Tab icon width |
| height | string | No | Tab bar height (default 50px, not including safe area) |
| spacing | string | No | Spacing between icon and text |

### TabBar Item Properties

| Property | Type | Required | Description |
|:-|:-|:-|:-|
| pagePath | string | Yes | Page path (must be registered in pages) |
| text | string | Yes | Tab text |
| iconPath | string | Yes | Icon path (unselected) |
| selectedIconPath | string | Yes | Icon path (selected) |
| redDot | boolean | No | Show red dot |
| badge | string | No | Badge text |

## subPackages

Split the app into sub-packages for faster first-load time.

```json
{
  "subPackages": [
    {
      "root": "pages-sub",
      "pages": [
        {
          "path": "detail/detail",
          "style": { "navigationBarTitleText": "Detail" }
        },
        {
          "path": "search/search",
          "style": { "navigationBarTitleText": "Search" }
        }
      ]
    }
  ]
}
```

## preloadRule

Pre-load sub-packages when specific pages are visited.

```json
{
  "preloadRule": {
    "pages/index/index": {
      "network": "all",
      "packages": ["pages-sub"]
    }
  }
}
```

## easycom

Auto-import components without manual import statements.

```json
{
  "easycom": {
    "autoscan": true,
    "custom": {
      "^uni-(.*)": "@dcloudio/uni-ui/lib/uni-$1/uni-$1.vue",
      "^my-(.*)": "@/components/my-$1/my-$1.uvue"
    }
  }
}
```

**Default easycom rules:**
- Components in `/components/组件名称/组件名称.uvue` are auto-imported
- Components in `/uni_modules/插件ID/components/组件名称/组件名称.uvue` are auto-imported

## Window Configuration (PC/Tablet)

```json
{
  "topWindow": {
    "path": "windows/top-window.uvue",
    "style": { "height": "60px" }
  },
  "leftWindow": {
    "path": "windows/left-window.uvue",
    "style": { "width": "350px" },
    "matchMedia": { "minWidth": 768 }
  },
  "rightWindow": {
    "path": "windows/right-window.uvue",
    "style": { "width": "350px" },
    "matchMedia": { "minWidth": 1024 }
  }
}
```

## condition

Development-only launch configurations for testing specific pages.

```json
{
  "condition": {
    "current": 0,
    "list": [
      {
        "name": "Detail Page",
        "path": "pages/detail/detail",
        "query": "id=123"
      }
    ]
  }
}
```

---

## manifest.json

`manifest.json` configures app metadata, platform-specific settings, and module permissions.

## Complete Structure

```json
{
  "name": "My App",
  "appid": "__UNI__XXXXXXX",
  "description": "App description",
  "versionName": "1.0.0",
  "versionCode": 100,
  "uni-app-x": {},
  "vueVersion": "3",
  "locale": "zh-Hans",
  "h5": {},
  "mp-weixin": {},
  "mp-alipay": {},
  "mp-baidu": {},
  "mp-toutiao": {},
  "mp-qq": {},
  "app-android": {},
  "app-ios": {}
}
```

### Core Properties

| Property | Type | Required | Description |
|:-|:-|:-|:-|
| name | string | Yes | App name |
| appid | string | Yes | DCloud app ID (format: __UNI__XXXXXXX) |
| description | string | No | App description |
| versionName | string | Yes | Version name (e.g., "1.0.0") |
| versionCode | number | Yes | Version code (integer, e.g., 100) |
| uni-app-x | Object | No | uni-app x specific config |
| vueVersion | string | Yes | Vue version ("3") |
| locale | string | No | Default language (e.g., "zh-Hans", "en") |

### uni-app-x Configuration

```json
{
  "uni-app-x": {
    "vapor": true,
    "styleIsolationVersion": "2"
  }
}
```

### H5 Configuration

```json
{
  "h5": {
    "title": "My App",
    "template": "index.html",
    "router": {
      "mode": "history",
      "base": "/"
    },
    "devServer": {
      "port": 8080,
      "proxy": {
        "/api": {
          "target": "http://localhost:3000",
          "changeOrigin": true
        }
      }
    },
    "publicPath": "/",
    "sdkConfigs": {
      "maps": {}
    },
    "async": {
      "timeout": 20000
    }
  }
}
```

### WeChat Mini Program Configuration

```json
{
  "mp-weixin": {
    "appid": "wx1234567890abcdef",
    "darkmode": true,
    "setting": {
      "urlCheck": false,
      "es6": true,
      "postcss": true,
      "minified": true
    },
    "usingComponents": true,
    "resizable": true,
    "requiredPrivateInfos": [
      "getLocation",
      "onLocationChange"
    ],
    "permission": {
      "scope.userLocation": {
        "desc": "Your location is used for demo"
      }
    }
  }
}
```

### Android Configuration

```json
{
  "app-android": {
    "distribute": {
      "modules": {
        "uni-payment": {
          "alipay": {},
          "wxpay": { "appid": "" }
        },
        "uni-location": {
          "system": {},
          "tencent": {}
        },
        "uni-push": {},
        "uni-map": { "tencent": {} }
      },
      "icons": {
        "ldpi": "package/icon36.png",
        "mdpi": "package/icon48.png",
        "hdpi": "package/icon72.png",
        "xhdpi": "package/icon96.png",
        "xxhdpi": "package/icon144.png",
        "xxxhdpi": "package/icon192.png"
      },
      "splashScreens": {
        "default": {}
      },
      "abi": ["armeabi-v7a", "arm64-v8a"],
      "minSdkVersion": 21,
      "targetSdkVersion": 33
    }
  }
}
```

### iOS Configuration

```json
{
  "app-ios": {
    "distribute": {
      "modules": {
        "uni-payment": {
          "alipay": {},
          "wxpay": {
            "appid": "",
            "universalLink": ""
          }
        },
        "uni-location": {
          "system": {},
          "tencent": {}
        },
        "uni-push": {},
        "uni-map": { "tencent": {} }
      },
      "icons": {
        "appstore": "package/icon1024.png"
      },
      "splashScreens": {}
    }
  }
}
```

## Common Patterns

### Basic App with TabBar
```json
{
  "pages": [
    { "path": "pages/home/home", "style": { "navigationBarTitleText": "Home" } },
    { "path": "pages/user/user", "style": { "navigationBarTitleText": "My" } }
  ],
  "globalStyle": {
    "navigationBarTextStyle": "black",
    "navigationBarTitleText": "My App",
    "navigationBarBackgroundColor": "#FFFFFF",
    "backgroundColor": "#F8F8F8"
  },
  "tabBar": {
    "color": "#999999",
    "selectedColor": "#007AFF",
    "backgroundColor": "#FFFFFF",
    "list": [
      { "pagePath": "pages/home/home", "text": "Home", "iconPath": "static/tab/home.png", "selectedIconPath": "static/tab/home-active.png" },
      { "pagePath": "pages/user/user", "text": "My", "iconPath": "static/tab/user.png", "selectedIconPath": "static/tab/user-active.png" }
    ]
  }
}
```

### App with SubPackages
```json
{
  "pages": [
    { "path": "pages/index/index", "style": { "navigationBarTitleText": "Home" } }
  ],
  "subPackages": [
    {
      "root": "pages-user",
      "pages": [
        { "path": "profile/profile", "style": { "navigationBarTitleText": "Profile" } },
        { "path": "settings/settings", "style": { "navigationBarTitleText": "Settings" } }
      ]
    }
  ],
  "preloadRule": {
    "pages/index/index": {
      "network": "all",
      "packages": ["pages-user"]
    }
  }
}
```

### Custom Navigation Bar
```json
{
  "pages": [
    {
      "path": "pages/index/index",
      "style": {
        "navigationStyle": "custom",
        "navigationBarTitleText": "",
        "enablePullDownRefresh": true
      }
    }
  ]
}
```
