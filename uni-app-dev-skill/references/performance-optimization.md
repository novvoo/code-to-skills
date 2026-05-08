# Performance Optimization Guide

## Overview

uni-app x on Android is essentially a native Kotlin application. While the framework provides native-level performance, poor coding practices can still cause lag. This guide covers critical optimization strategies specific to uni-app x's native rendering.

## 1. Minimize DOM Count and Depth

**This is the #1 performance rule for native rendering.**

On Android, every view element creates a native View object. Unlike web browsers which can handle thousands of DOM elements, native rendering is much more sensitive to DOM count.

### Problem Example: Calendar
A typical web calendar creates a view for each day (30+ views), with nested views for lunar date, holidays, etc. This results in hundreds of DOM elements and causes severe lag on Android.

### Solution: Use Draw API
Native Android calendar apps draw the entire month as a single view using Draw API. uni-app x provides the same capability:

```vue
<template>
  <view class="calendar-container">
    <native-view ref="calendarView" :init="onCalendarInit" style="width: 750rpx; height: 800rpx;"></native-view>
  </view>
</template>

<script setup lang="uts">
const calendarView = ref<UniNativeViewElement | null>(null)

const onCalendarInit = (e : UniNativeViewInitEvent) => {
  const element = e.element
  // Get DrawableContext for custom drawing
  const ctx = element.getDrawableContext()!
  
  // Clear previous content
  ctx.reset()
  
  // Set pen style
  ctx.strokeStyle = "#333333"
  ctx.lineWidth = 1
  
  // Draw calendar grid
  ctx.moveTo(50, 100)
  ctx.lineTo(700, 100)
  ctx.stroke()
  
  // Draw text
  ctx.fillStyle = "#000000"
  ctx.font = "14px"
  ctx.fillText("1", 60, 140)
  ctx.fillText("2", 160, 140)
  // ... draw all days
  
  // Update canvas
  ctx.update()
}
</script>
```

### Real-World Example: Slider Component
The first version of uni-app x's slider used 7 views (moving view + colored width views). When a page had many sliders, it became very laggy. After rewriting with Draw API, it uses only 1 view, and 100 sliders on one page run smoothly.

## 2. Use list-view for Long Lists

**NEVER use scroll-view + v-for for lists with more than ~20 items.**

scroll-view renders ALL items in the DOM, causing:
- Slow initial render
- High memory usage
- Scroll lag with many items

list-view implements virtual scrolling - only visible items are rendered:

```vue
<!-- BAD: Renders ALL items -->
<scroll-view scroll-y>
  <view v-for="item in 1000items" :key="item.id">
    <text>{{ item.name }}</text>
  </view>
</scroll-view>

<!-- GOOD: Only renders visible items -->
<list-view style="flex: 1" @scrolltolower="loadMore">
  <list-item v-for="item in dataList" :key="item.id">
    <text>{{ item.name }}</text>
  </list-item>
</list-view>
```

### List Item Optimization

1. **Keep list items flat** - Avoid deep component nesting inside list items
2. **Don't wrap view/text in custom components** - Use built-in components directly
3. **Extract interactive parts** - Make favorite/like buttons separate components to minimize re-render scope

```vue
<!-- BAD: Entire list re-renders when favorite changes -->
<list-view style="flex: 1">
  <list-item v-for="item in list" :key="item.id">
    <view @click="toggleFavorite(item)">
      <text>{{ item.name }}</text>
      <text>{{ item.isFavorite ? '★' : '☆' }}</text>
    </view>
  </list-item>
</list-view>

<!-- GOOD: Only FavoriteButton re-renders -->
<list-view style="flex: 1">
  <list-item v-for="item in list" :key="item.id">
    <text>{{ item.name }}</text>
    <FavoriteButton :item="item" @toggle="toggleFavorite" />
  </list-item>
</list-view>
```

## 3. Optimize Layout Efficiency

HBuilderX prints page initialization data when running on Android:
- DOM count
- Layout passes
- Render time

### Layout Optimization Rules

1. **Specify explicit width/height** - Avoid auto-sizing when possible. Parent nodes without explicit dimensions must wait for all children to calculate, which is expensive.

2. **Specify main axis dimension** - Reduces recursive depth in flex layout.

3. **Pre-size text components** - Text measurement is expensive. Give `<text>` explicit width/height to skip measurement.

4. **Pre-size images** - Always specify image dimensions to reduce layout passes.

5. **CSS unit performance ranking**: `px` > `rpx` > `%`. When using percentages, ensure parent has explicit dimensions.

```vue
<!-- BAD: Multiple layout passes needed -->
<view style="flex: 1;">
  <text>{{ longText }}</text>
  <image src="..." />
</view>

<!-- GOOD: Explicit dimensions reduce layout passes -->
<view style="flex: 1;">
  <text style="width: 690rpx; height: 80rpx;">{{ longText }}</text>
  <image src="..." style="width: 690rpx; height: 400rpx;" mode="aspectFill" />
</view>
```

## 4. Control Vue Update Scope

Vue's reactivity system triggers re-renders when data changes. While updates are differential, computing diffs still takes time.

### Strategies

1. **Split large data into smaller reactive objects** - If a large object has a frequently-changing property, extract it.

```uts
// BAD: Updating one field triggers diff on entire object
const bigData = reactive({
  list: [...], // 1000 items
  selectedId: -1, // changes frequently
  filters: {...}
})

// GOOD: Separate frequently-changing data
const listData = reactive({ list: [...] })
const selectionData = reactive({ selectedId: -1 })
const filterData = reactive({ filters: {...} })
```

2. **Use shallowRef for large data** - Avoids deep reactivity overhead.

```uts
const bigList = shallowRef<ItemType[]>([])
// Only triggers update when entire array is replaced
bigList.value = newList
```

3. **Use computed for derived data** - Computed values are cached.

```uts
const filteredList = computed(() => {
  return listData.list.filter(item => item.category === currentCategory.value)
})
```

## 5. Avoid Unnecessary Component Abstraction

Creating too many component instances causes performance loss. This is especially important in lists.

**Rule of thumb:** If a component is used fewer than ~10 times on screen, abstraction overhead is negligible. But in a list of 100+ items, each with many sub-components, removing one unnecessary component layer can save hundreds of component instances.

**NEVER wrap basic components (view, text) in custom components** when they're used in large quantities.

## 6. Use DOM API for Gesture Animations

For smooth gesture-driven animations (drag, swipe), bypass Vue's reactivity system and use DOM API directly:

```vue
<template>
  <view ref="dragView" class="draggable" @touchstart="onTouchStart" @touchmove="onTouchMove" @touchend="onTouchEnd">
    <text>Drag me</text>
  </view>
</template>

<script setup lang="uts">
const dragView = ref<UniElement | null>(null)
let startX = 0
let startY = 0
let offsetX = 0
let offsetY = 0

const onTouchStart = (e : UniTouchEvent) => {
  startX = e.touches[0].clientX - offsetX
  startY = e.touches[0].clientY - offsetY
}

const onTouchMove = (e : UniTouchEvent) => {
  offsetX = e.touches[0].clientX - startX
  offsetY = e.touches[0].clientY - startY
  
  // Direct DOM manipulation - bypasses Vue diff, ensures 60fps
  dragView.value!.style.setProperty('transform', `translate(${offsetX}px, ${offsetY}px)`)
}

const onTouchEnd = () => {
  // Optionally sync back to reactive data
}
</script>
```

## 7. Image Optimization

1. **Always specify dimensions** - Reduces layout recalculations
2. **Use lazy-load** - `lazy-load="true"` for images below the fold
3. **Use appropriate resolution** - Don't load 4x images for 1x displays
4. **Use webp format** - Smaller file size (supported on Android/Web)
5. **Compress images** - Use build tools to compress static images

## 8. Network Optimization

1. **Batch API calls** - Reduce number of requests
2. **Use request caching** - Cache responses with uni.setStorage
3. **Implement pagination** - Load data on demand with list-view's scrolltolower
4. **Use uni.request interceptor** - Add global loading/error handling

```uts
// Request interceptor
uni.addInterceptor('request', {
  invoke(args) {
    // Add auth token
    args.header = args.header || {}
    args.header['Authorization'] = `Bearer ${getToken()}`
  },
  success(res) {
    // Global success handling
  },
  fail(err) {
    // Global error handling
    console.error('Request failed:', err)
  }
})
```

## 9. Memory Management

1. **Release native resources** - Always clean up in onUnmounted
2. **Remove event listeners** - Use uni.offXxx to remove listeners
3. **Clear timers** - Clear setTimeout/setInterval in onUnmounted
4. **Avoid circular references** - Be careful with closures holding references

```uts
onMounted(() => {
  uni.onNetworkStatusChange(networkListener)
})

onUnmounted(() => {
  uni.offNetworkStatusChange(networkListener)
  if (timer !== null) {
    clearTimeout(timer)
  }
  player?.release()
  player = null
})
```

## 10. Engine Size

uni-app x's Android engine is only 7.51MB, significantly smaller than other cross-platform frameworks. This is because:
- No JavaScript engine on Android (UTS compiles to Kotlin)
- No heavy runtime (unlike Flutter's Dart VM)
- No bridge communication overhead

## Performance Monitoring

Use uni.getPerformance() to monitor runtime performance:

```uts
const performance = uni.getPerformance()
const observer = performance.createObserver(
  (entryList : PerformanceObserverEntryList) => {
    console.log('Performance entries:', JSON.stringify(entryList.getEntries()))
  }
)
observer.observe({
  entryTypes: ['render', 'navigation']
} as PerformanceObserverOptions)
```

## Summary Checklist

- [ ] DOM count per page < 200 (check HBuilderX console)
- [ ] Using list-view instead of scroll-view + v-for for lists
- [ ] All images have explicit width/height
- [ ] Text components have explicit dimensions where possible
- [ ] Using px/rpx instead of % when parent dimensions are unknown
- [ ] Large data split into smaller reactive objects
- [ ] Using shallowRef for large arrays
- [ ] No unnecessary component wrapping in lists
- [ ] Using DOM API for gesture animations
- [ ] Native resources released in onUnmounted
- [ ] Event listeners cleaned up
- [ ] Timers cleared
