# DOM API and Draw API Reference

## Overview

Each uvue page has a DOM (Document Object Model) in memory, similar to browser DOM. The DOM represents the page's element structure as a logical tree where each branch endpoint is a node (UniElement).

**Important:** Currently, DOM API does NOT support creating or deleting DOM elements. It only supports getting UniElement objects and manipulating their styles/properties.

## When to Use DOM API

1. **Gesture Animations** - Touch-driven position updates need 16ms per frame. Vue's diff mechanism adds overhead; DOM API bypasses it for smooth 60fps animations.
2. **Draw API** - Native high-performance drawing capabilities require getting UniElement first.

## Getting DOM Elements

### Method 1: uni.getElementById

```uts
// Get element by id attribute
const element = uni.getElementById("myView")
if (element !== null) {
  // Manipulate element
  element.style.setProperty("background-color", "red")
}
```

### Method 2: this.$refs (Composition API)

```vue
<template>
  <view ref="myView" id="myView" class="container">
    <text>Hello</text>
  </view>
</template>

<script setup lang="uts">
// For built-in components (view, text, etc.)
const myView = ref<UniElement | null>(null)

// For built-in components with specific type
const slider = ref<UniSliderElement | null>(null)

// For custom components
const childComponent = ref<ComponentPublicInstance | null>(null)

onMounted(() => {
  // Access element after mount
  console.log(myView.value?.style)
})
</script>
```

### Method 3: this.$refs (Options API)

```vue
<script>
export default {
  onReady() {
    const element = this.$refs['myView'] as UniElement
    element.style.setProperty("background-color", "red")
  }
}
</script>
```

## UniElement API

### Properties

| Property | Type | Description |
|:-|:-|:-|
| id | string | Element ID |
| style | CSSStyleDeclaration | Element style object |
| dataset | Map<string, any> | Custom data attributes |
| offsetWidth | number | Element width (px) |
| offsetHeight | number | Element height (px) |
| offsetLeft | number | Left offset from offset parent |
| offsetTop | number | Top offset from offset parent |
| clientWidth | number | Visible width (px) |
| clientHeight | number | Visible height (px) |
| scrollWidth | number | Scroll width (px) |
| scrollHeight | number | Scroll height (px) |
| scrollTop | number | Vertical scroll position |
| scrollLeft | number | Horizontal scroll position |
| parentNode | UniElement \| null | Parent element |
| childNodes | UniElement[] | Child elements |
| firstChild | UniElement \| null | First child |
| lastChild | UniElement \| null | Last child |
| nextSibling | UniElement \| null | Next sibling |
| previousSibling | UniElement \| null | Previous sibling |

### Methods

| Method | Description |
|:-|:-|
| getBoundingClientRect() | Get element position and size (returns DOMRect) |
| getAndroidView() | Get Android native View object (app-android only) |
| getIOSView() | Get iOS native UIView object (app-ios only) |
| getDrawableContext() | Get Draw API context for custom rendering |

### Style Manipulation

```uts
const element = uni.getElementById("myView")!

// Set single property
element.style.setProperty("background-color", "#ff0000")
element.style.setProperty("width", "200px")
element.style.setProperty("transform", "translateX(100px)")

// Get property value
const bgColor = element.style.getPropertyValue("background-color")

// Remove property
element.style.removeProperty("transform")
```

### CSSStyleDeclaration

```uts
const style = element.style

// Properties
style.width = "200px"
style.height = "100px"
style.backgroundColor = "#ff0000"
style.color = "#ffffff"
style.fontSize = "16px"
style.marginTop = "10px"
style.padding = "20px"
style.opacity = "0.8"
style.transform = "scale(1.5)"
style.transition = "all 0.3s ease"

// Get computed style (after layout)
const rect = element.getBoundingClientRect()
console.log(rect.left, rect.top, rect.width, rect.height)
```

## Draw API

The Draw API provides high-performance custom rendering by drawing directly onto a native view. This is essential for complex visual elements that would require too many DOM nodes.

### Basic Usage

```vue
<template>
  <view>
    <native-view ref="drawView" :init="onDrawInit" style="width: 750rpx; height: 750rpx; background-color: #ffffff;"></native-view>
    <button @click="redraw">Redraw</button>
  </view>
</template>

<script setup lang="uts">
const drawView = ref<UniNativeViewElement | null>(null)
let ctx : DrawableContext | null = null
let isRed = true

const onDrawInit = (e : UniNativeViewInitEvent) => {
  ctx = e.element.getDrawableContext()!
  drawContent()
}

const drawContent = () => {
  if (ctx === null) return
  
  // Clear previous content
  ctx!.reset()
  
  // Set pen style
  ctx!.strokeStyle = isRed ? "#FF0000" : "#0000FF"
  ctx!.fillStyle = isRed ? "#FF0000" : "#0000FF"
  ctx!.lineWidth = 2
  
  // Draw lines
  ctx!.moveTo(50, 40)
  ctx!.lineTo(200, 40)
  ctx!.stroke()
  
  // Draw rectangle
  ctx!.fillRect(50, 80, 200, 100)
  
  // Draw text
  ctx!.fillText("Hello Draw API", 50, 220)
  
  // Draw circle (using arc)
  ctx!.beginPath()
  ctx!.arc(150, 350, 50, 0, Math.PI * 2)
  ctx!.fill()
  
  // Update canvas
  ctx!.update()
  
  isRed = !isRed
}

const redraw = () => {
  drawContent()
}
</script>
```

### DrawableContext Methods

| Method | Description |
|:-|:-|
| reset() | Clear all drawn content |
| moveTo(x, y) | Move pen to position |
| lineTo(x, y) | Draw line to position |
| stroke() | Stroke the current path |
| fill() | Fill the current path |
| fillRect(x, y, w, h) | Draw filled rectangle |
| strokeRect(x, y, w, h) | Draw rectangle outline |
| fillText(text, x, y) | Draw text |
| beginPath() | Start new path |
| closePath() | Close current path |
| arc(x, y, r, startAngle, endAngle) | Draw arc/circle |
| quadraticCurveTo(cpx, cpy, x, y) | Draw quadratic bezier curve |
| bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y) | Draw cubic bezier curve |
| update() | Apply all drawing operations to canvas |

### DrawableContext Properties

| Property | Description |
|:-|:-|
| strokeStyle | Stroke color |
| fillStyle | Fill color |
| lineWidth | Line width |
| font | Font specification |
| textAlign | Text alignment |
| textBaseline | Text baseline |

## ResizeObserver

Monitor element size changes:

```uts
const observer = new UniResizeObserver((entry : UniResizeObserverEntry) => {
  console.log('Size changed:', entry.borderBoxSize)
  console.log('Width:', entry.contentRect.width)
  console.log('Height:', entry.contentRect.height)
})

// Start observing
const element = uni.getElementById("myView")!
observer.observe(element)

// Stop observing
observer.disconnect()
```

## SelectorQuery

Query element information after layout (more accurate than synchronous DOM API):

```uts
uni.createSelectorQuery().select('.my-class').boundingClientRect((rect) => {
  console.log('Element rect:', rect)
}).exec()

uni.createSelectorQuery().selectAll('.item').boundingClientRect((rects) => {
  console.log('All items:', rects)
}).exec()

uni.createSelectorQuery().select('.scroll-view').scrollOffset((res) => {
  console.log('Scroll position:', res.scrollTop)
}).exec()

// Combined query
uni.createSelectorQuery()
  .select('.header').boundingClientRect()
  .select('.content').boundingClientRect()
  .exec((res) => {
    const headerRect = res[0]
    const contentRect = res[1]
    console.log('Header:', headerRect, 'Content:', contentRect)
  })
```

## Important Notes

1. **Layout is asynchronous** - After modifying DOM, synchronous DOM API may return pre-layout values. Use `uni.createSelectorQuery()` for accurate post-layout measurements.

2. **No DOM creation/deletion** - You cannot create or remove DOM elements via API. Use Vue's v-if/v-for for conditional rendering.

3. **Vue conflict** - Directly manipulating DOM styles may conflict with Vue's reactivity system. For gesture animations, this is acceptable since you're bypassing Vue intentionally.

4. **getAndroidView()/getIOSView()** - These methods return the actual native View/UIView object, allowing full native API access. Use with caution.

5. **Performance** - DOM API operations are synchronous and fast. Use them when Vue's reactivity overhead is too much (e.g., 60fps animations).
