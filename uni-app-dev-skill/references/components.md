# uni-app Components Reference

## Overview

Components are the basic building blocks of the view layer. Each component is a self-contained, reusable UI module with its own template, script, and style. uni-app x components follow Vue SFC specification but use `.uvue` file extension and UTS language.

**Key Differences from Web:**
- Text MUST be wrapped in `<text>` tags, not placed directly in `<view>`
- Text styles do NOT inherit from parent on native platforms
- Only class selectors are supported in CSS (no tag, #id, [attr])
- Default layout is flex (not block)
- Use `hover-class` instead of CSS `:active` pseudo-class

## Basic Components

### view
Basic view container, similar to HTML div. The most fundamental layout component.

**Type:** UniViewElement

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| hover-class | string | "none" | Press style class. "none" = no press effect |
| hover-stop-propagation | boolean | false | Prevent ancestor nodes from showing press effect |
| hover-start-time | number | 50 | Delay before press effect appears (ms) |
| hover-stay-time | number | 400 | Duration press effect stays after release (ms) |
| flatten | boolean | false | Flatten component (HarmonyOS Vapor 5.0+) |

**Why use hover-class instead of :active?**
CSS `:active` pseudo-class triggers too easily and doesn't disappear during scrolling. `hover-class` provides better touch feedback. App platforms don't support CSS pseudo-classes.

**Example:**
```vue
<template>
  <view class="container" hover-class="hover-active" :hover-stay-time="200">
    <text>Tap me</text>
  </view>
</template>

<style>
.container { padding: 20rpx; background-color: #ffffff; }
.hover-active { background-color: #f0f0f0; opacity: 0.8; }
</style>
```

### text
Text display component. In uni-app x, ALL visible text MUST be wrapped in `<text>` tags.

**Type:** UniTextElement

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| selectable | boolean | false | Whether text is selectable |
| space | string | - | Display consecutive spaces: ensp / emsp / nbsp |
| decode | boolean | false | Whether to decode HTML entities (&amp; &lt; &gt; &nbsp;) |
| max-lines | number | - | Maximum lines to display (Vapor 5.0+) |

**CRITICAL:** Text styles do NOT inherit from parent on native. Always apply text styles directly to the `<text>` component.

```vue
<!-- WRONG: text won't inherit color from parent -->
<view style="color: red;">
  <text>This text is NOT red on native!</text>
</view>

<!-- CORRECT: apply styles directly to text -->
<view>
  <text style="color: red;">This text IS red</text>
</view>
```

**text internal layout:** The `<text>` component uses inline layout internally, so multiple `<text>` elements will flow horizontally by default.

### image
Image display component with multiple resize modes.

**Type:** UniImageElement

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| src | string | - | Image resource URL (local or remote) |
| mode | string | scaleToFill | Resize mode (see below) |
| lazy-load | boolean | false | Lazy load when entering viewport |
| fade-show | boolean | true | Show fade animation when loaded |
| webp | boolean | false | Support webp format (MP only) |
| show-menu-by-longpress | boolean | false | Show context menu on long press |

**Mode Values:**
| Mode | Description |
|:-|:-|
| scaleToFill | Stretch to fill (default, may distort) |
| aspectFit | Scale to fit maintaining aspect ratio (may have blank areas) |
| aspectFill | Scale to fill maintaining aspect ratio (may crop) |
| widthFix | Width fixed, height auto-calculated |
| heightFix | Height fixed, width auto-calculated |
| top / bottom / center | No scaling, align to edge |
| left / right | No scaling, align horizontally |

**Events:** @error, @load

**Performance Tip:** Always specify width and height for images to reduce layout recalculations.

```vue
<template>
  <image 
    src="/static/logo.png" 
    mode="aspectFit" 
    style="width: 200rpx; height: 200rpx;"
    @error="onImageError"
    @load="onImageLoad"
  />
</template>
```

### button
Button component with built-in styles.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| size | string | default | Button size: default / mini |
| type | string | default | Button type: default / primary / warn |
| plain | boolean | false | Hollow/outlined style |
| disabled | boolean | false | Disabled state |
| loading | boolean | false | Show loading indicator |
| form-type | string | - | Form action: submit / reset |
| hover-class | string | "button-hover" | Press feedback style |
| hover-start-time | number | 20 | Press effect delay (ms) |
| hover-stay-time | number | 70 | Press effect duration (ms) |

```vue
<button type="primary" @click="submit">Submit</button>
<button type="warn" plain>Delete</button>
<button size="mini" loading>Saving...</button>
<button disabled>Disabled</button>
```

### input
Single-line text input component.

**Type:** UniInputElement

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| value | string | - | Input value (v-model) |
| type | string | text | Input type: text / number / digit / tel / idcard / safe-password |
| password | boolean | false | Password mode |
| placeholder | string | - | Placeholder text |
| placeholder-style | string | - | Placeholder inline style |
| placeholder-class | string | "input-placeholder" | Placeholder CSS class |
| disabled | boolean | false | Disabled state |
| maxlength | number | 140 | Maximum character count (-1 = unlimited) |
| cursor | number | - | Cursor position |
| focus | boolean | false | Auto focus |
| confirm-type | string | done | Keyboard confirm button: send / search / next / go / done |
| adjust-position | boolean | true | Auto adjust page position when keyboard appears |
| cursor-color | string | - | Cursor color |

**Events:** @input, @focus, @blur, @confirm, @keyboardheightchange

```vue
<template>
  <input 
    v-model="searchText" 
    type="text" 
    placeholder="Search..." 
    confirm-type="search"
    @confirm="doSearch"
    @input="onInputChange"
  />
</template>

<script setup lang="uts">
const searchText = ref('')
const onInputChange = (e : UniInputEvent) => {
  searchText.value = e.detail.value
}
const doSearch = () => {
  console.log('Searching:', searchText.value)
}
</script>
```

### textarea
Multi-line text input component.

**Type:** UniTextAreaElement

**Props:** Similar to input plus:
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| auto-height | boolean | false | Auto grow height |
| fixed | boolean | false | Fixed position (keyboard won't push up) |
| show-confirm-bar | boolean | true | Show keyboard confirm bar |

### scroll-view
Scrollable container with scroll event monitoring.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| scroll-x | boolean | false | Allow horizontal scroll |
| scroll-y | boolean | false | Allow vertical scroll |
| scroll-top | number | - | Set vertical scroll position |
| scroll-left | number | - | Set horizontal scroll position |
| scroll-into-view | string | - | Scroll to child element by id |
| scroll-with-animation | boolean | false | Animate scroll |
| enable-back-to-top | boolean | false | Tap status bar to scroll to top |
| lower-threshold | number | 50 | Threshold for scrolltolower event |
| upper-threshold | number | 50 | Threshold for scrolltoupper event |
| refresher-enabled | boolean | false | Enable pull-to-refresh |
| refresher-threshold | number | 45 | Pull-to-refresh threshold |
| refresher-default-style | string | "black" | Refresh indicator style: black / white / none |
| refresher-background | string | "#fff" | Refresh indicator background |

**Events:** @scroll, @scrolltolower, @scrolltoupper, @refresherrefresh, @refresherrestore, @refresherabort

**IMPORTANT:** Do NOT use scroll-view + v-for for long lists. Use `<list-view>` instead for virtual scrolling.

```vue
<template>
  <scroll-view 
    scroll-y 
    style="flex: 1"
    refresher-enabled
    :refresher-triggered="isRefreshing"
    @refresherrefresh="onRefresh"
    @scrolltolower="loadMore"
  >
    <view v-for="item in items" :key="item.id">
      <text>{{ item.title }}</text>
    </view>
  </scroll-view>
</template>
```

### list-view / list-item (HIGH PERFORMANCE)
Virtual scrolling list for large datasets. Items are recycled when off-screen.

**Props (list-view):**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| scroll-y | boolean | true | Allow vertical scroll |
| lower-threshold | number | 50 | Threshold for scrolltolower |
| refresher-enabled | boolean | false | Enable pull-to-refresh |
| refresher-threshold | number | 45 | Pull-to-refresh threshold |

**Events:** @scrolltolower, @scroll, @refresherrefresh

**CRITICAL:** Always use list-view for lists with more than ~20 items. scroll-view + v-for renders ALL items and causes severe performance issues on native.

```vue
<template>
  <list-view style="flex: 1" @scrolltolower="loadMore" refresher-enabled @refresherrefresh="onRefresh">
    <list-item v-for="item in dataList" :key="item.id" class="list-item">
      <view class="item-content">
        <text class="item-title">{{ item.title }}</text>
        <text class="item-desc">{{ item.description }}</text>
      </view>
    </list-item>
  </list-view>
</template>

<script setup lang="uts">
type ListItem = { id: number; title: string; description: string }
const dataList = ref<ListItem[]>([])
const loadMore = () => { /* fetch more data */ }
const onRefresh = () => { /* refresh data */ }
</script>
```

**Performance Tips for list-view:**
- Keep list-item components flat - avoid deep component nesting
- Don't wrap view/text in custom components inside list items
- Extract interactive parts (like favorite button) into separate components to minimize re-render scope

### swiper / swiper-item
Carousel/slider component with autoplay support.

**Props (swiper):**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| indicator-dots | boolean | false | Show indicator dots |
| indicator-color | string | "rgba(0,0,0,.3)" | Indicator dot color |
| indicator-active-color | string | "#000000" | Active indicator color |
| autoplay | boolean | false | Auto play |
| current | number | 0 | Current slide index |
| interval | number | 5000 | Auto play interval (ms) |
| duration | number | 500 | Transition duration (ms) |
| circular | boolean | false | Loop mode |
| vertical | boolean | false | Vertical direction |
| previous-margin | string | "0px" | Previous slide exposed width |
| next-margin | string | "0px" | Next slide exposed width |

**Events:** @change, @transition, @animationfinish

### navigator
Page navigation link component.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| url | string | - | Target page URL (must be registered in pages.json) |
| open-type | string | navigate | Navigation type: navigate / redirect / switchTab / reLaunch / navigateBack |
| delta | number | 1 | Pages to go back (for navigateBack) |
| hover-class | string | "navigator-hover" | Press feedback style |
| animation-type | string | pop-in | Animation type (Android) |
| animation-duration | number | 300 | Animation duration (ms) |

```vue
<navigator url="/pages/detail/detail?id=123" hover-class="none">
  <text>Go to Detail</text>
</navigator>
<navigator url="/pages/index/index" open-type="switchTab">
  <text>Go Home</text>
</navigator>
```

## Form Components

### checkbox / checkbox-group
Multi-select checkboxes.

```vue
<template>
  <checkbox-group @change="onCheckChange">
    <checkbox value="apple" :checked="true" /> <text>Apple</text>
    <checkbox value="banana" /> <text>Banana</text>
    <checkbox value="orange" disabled /> <text>Orange (disabled)</text>
  </checkbox-group>
</template>
```

### radio / radio-group
Single-select radio buttons.

```vue
<template>
  <radio-group @change="onRadioChange">
    <radio value="male" :checked="true" /> <text>Male</text>
    <radio value="female" /> <text>Female</text>
  </radio-group>
</template>
```

### picker
Selector component for date, time, region, or custom data.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| mode | string | selector | Type: selector / multiSelector / time / date / region |
| range | array | - | Options for selector mode |
| range-key | string | - | Key to display from range objects |
| value | number/array | 0 | Selected index/indices |
| disabled | boolean | false | Disabled state |

```vue
<template>
  <picker mode="selector" :range="options" @change="onPickerChange">
    <text>{{ selectedOption }}</text>
  </picker>
  
  <picker mode="date" :value="date" @change="onDateChange">
    <text>{{ date }}</text>
  </picker>
  
  <picker mode="region" @change="onRegionChange">
    <text>{{ region }}</text>
  </picker>
</template>
```

### switch
Toggle switch component.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| checked | boolean | false | Whether checked |
| disabled | boolean | false | Disabled state |
| color | string | "#007aff" | Switch color (checked state) |

### slider
Slider component.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| min | number | 0 | Minimum value |
| max | number | 100 | Maximum value |
| step | number | 1 | Step size |
| value | number | 0 | Current value |
| activeColor | string | "#007aff" | Active track color |
| backgroundColor | string | "#e9e9e9" | Background track color |
| blockSize | number | 28 | Block size (px) |
| show-value | boolean | false | Show current value |

## Media Components

### video
Video player component.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| src | string | - | Video URL |
| autoplay | boolean | false | Auto play |
| loop | boolean | false | Loop playback |
| muted | boolean | false | Muted |
| controls | boolean | true | Show controls |
| poster | string | - | Poster image URL |
| direction | number | 0 | Full-screen direction (0=auto, 90, -90) |
| show-fullscreen-btn | boolean | true | Show fullscreen button |
| show-play-btn | boolean | true | Show play/pause button |
| enable-progress-gesture | boolean | true | Allow gesture to control progress |

**Events:** @play, @pause, @ended, @timeupdate, @fullscreenchange, @error, @waiting

### map
Map component (requires platform-specific configuration).

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| latitude | number | 39.92 | Center latitude |
| longitude | number | 116.46 | Center longitude |
| scale | number | 16 | Zoom level (3-20) |
| markers | array | - | Marker points |
| polyline | array | - | Route lines |
| circles | array | - | Circles |
| controls | array | - | Controls on map |
| show-location | boolean | false | Show current location |

### canvas
Canvas drawing component.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| type | string | - | Canvas type: 2d / webgl |
| canvas-id | string | - | Unique identifier |
| disable-scroll | boolean | false | Disable scroll when touching canvas |

**Events:** @touchstart, @touchmove, @touchend, @longtap, @error

### web-view
Embedded web page component. Takes up the entire page area.

**Props:**
| Name | Type | Default | Description |
|:-|:-|:-|:-|
| src | string | - | Web page URL |
| allow | string | - | Feature policy |
| sandbox | string | - | Sandbox policy |

**Events:** @message, @load, @error

**Note:** web-view automatically fills the entire page. Other components cannot coexist on the same page.

## Layout Components (uni-app x)

### grid-view
Virtual scrolling grid layout.

```vue
<grid-view :columns="2" style="flex: 1">
  <view v-for="item in gridData" :key="item.id" class="grid-item">
    <text>{{ item.title }}</text>
  </view>
</grid-view>
```

### waterflow / flow-item
Waterfall/masonry layout for variable-height items.

```vue
<waterflow style="flex: 1" @scrolltolower="loadMore">
  <flow-item v-for="item in flowData" :key="item.id">
    <image :src="item.cover" mode="widthFix" />
    <text>{{ item.title }}</text>
  </flow-item>
</waterflow>
```

### nested-scroll / nested-scroll-header / nested-scroll-body
Nested scrolling container for complex scroll interactions (e.g., sticky header + scrollable body).

## Gesture Components (uni-app x)

Gesture components provide native gesture recognition:

- `<tap-gesture-handler>`: Tap gesture
- `<double-tap-gesture-handler>`: Double tap
- `<long-press-gesture-handler>`: Long press (500ms)
- `<pan-gesture-handler>`: Pan/drag gesture
- `<scale-gesture-handler>`: Pinch/scale gesture
- `<force-press-gesture-handler>`: Force press (iOS only)
- `<horizontal-drag-gesture-handler>`: Horizontal drag
- `<vertical-drag-gesture-handler>`: Vertical drag

```vue
<template>
  <view class="gesture-area">
    <tap-gesture-handler @tap="onTap">
      <view><text>Tap me</text></view>
    </tap-gesture-handler>
    
    <pan-gesture-handler @pan="onPan">
      <view :style="{ transform: `translate(${x}px, ${y}px)` }">
        <text>Drag me</text>
      </view>
    </pan-gesture-handler>
  </view>
</template>
```

## Advanced Components

### native-view (uni-app x)
Bridge component for embedding native views. Essential for UTS component plugin development.

```vue
<template>
  <native-view ref="nativeView" :init="onInit" @click="onClick"></native-view>
</template>

<script setup lang="uts">
const nativeView = ref<UniNativeViewElement | null>(null)

const onInit = (e : UniNativeViewInitEvent) => {
  // Get native element and bind native view
  const element = e.element
  // Android: element.bindAndroidView(nativeView)
  // iOS: element.bindIOSView(nativeView)
}

const onClick = (e : UniNativeViewEvent) => {
  console.log('Native view clicked', e.type)
}
</script>
```

### progress
Progress bar component.

**Props:** percent, stroke-width, activeColor, backgroundColor, active, show-info, active-mode

### rich-text
Rich text rendering from HTML string.

```vue
<rich-text :nodes="htmlContent" @itemclick="onItemClick"></rich-text>
```

### movable-area / movable-view
Draggable elements within a bounded area.

```vue
<movable-area style="width: 100%; height: 400rpx;">
  <movable-view direction="all" :x="30" :y="30">
    <text>Drag me</text>
  </movable-view>
</movable-area>
```

### cover-view / cover-image
Overlay on native components (map, video, etc.). These are the only components that can overlay native components.

### snapshot
Screenshot component. Renders child components to an image.

### page-container
Page popup container for modal-like pages.

### root-portal
Portal rendering to root level, useful for dialogs and overlays.

### share-element
Shared element transition animation between pages.

### open-container
Container with open/close animation.

### draggable-sheet
Draggable bottom sheet component.
