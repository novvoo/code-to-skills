# uni-app CSS Reference

## Overview

uni-app x uses a subset of CSS for styling. On native platforms (Android/iOS), CSS is rendered by the native rendering engine, not a web view. This means some CSS features may differ from standard web browsers.

**Critical Differences from Web:**
1. Default layout is **flex** (not block)
2. Only **class selectors** supported on native (no tag, #id, [attr])
3. **Styles do NOT inherit** on native platforms
4. Text styles must be applied directly to `<text>` components
5. Use `hover-class` instead of CSS `:active` pseudo-class
6. CSS pseudo-elements (`::before`, `::after`) not supported on native

## Units

| Unit | Description | Example |
|:-|:-|:-|
| rpx | Responsive pixel (750rpx = screen width) | `width: 750rpx` |
| px | Logical pixel | `width: 100px` |
| % | Percentage of parent | `width: 50%` |
| vh/vw | Viewport height/width percentage | `height: 100vh` |
| em/rem | Relative font size | `font-size: 1.5em` |

### rpx Design Philosophy
- Design based on 750px wide screen
- 1rpx = screen width / 750 on all devices
- On 375px wide device: 1rpx = 0.5px
- On 414px wide device: 1rpx ≈ 0.552px
- **Performance:** px > rpx > percentage

## Box Model

### Display
```css
/* Supported values */
display: flex;        /* Primary layout mode */
display: none;        /* Hide element */

/* Note: block, inline, inline-block have limited support on native */
```

### Flexbox (Primary Layout)
```css
.container {
  display: flex;
  flex-direction: row;          /* row | column | row-reverse | column-reverse */
  flex-wrap: nowrap;            /* nowrap | wrap | wrap-reverse */
  justify-content: flex-start;  /* flex-start | flex-end | center | space-between | space-around | space-evenly */
  align-items: stretch;         /* stretch | flex-start | flex-end | center | baseline */
  align-content: flex-start;    /* flex-start | flex-end | center | space-between | space-around */
}

.item {
  flex: 1;                      /* Grow factor */
  flex-grow: 1;                 /* Grow factor */
  flex-shrink: 1;               /* Shrink factor */
  flex-basis: auto;             /* Initial size */
  align-self: center;           /* Override align-items for this item */
  order: 0;                     /* Display order */
}
```

**Important:** Default flex-direction is `column` in uni-app x (unlike web which defaults to `row`).

### Width and Height
```css
.element {
  width: 750rpx;
  height: 200px;
  min-width: 100px;
  max-width: 100%;
  min-height: 50px;
  max-height: 80vh;
}
```

### Padding and Margin
```css
.element {
  padding: 10px;                    /* All sides */
  padding: 10px 20px;              /* Vertical | Horizontal */
  padding: 10px 20px 30px;         /* Top | Horizontal | Bottom */
  padding: 10px 20px 30px 40px;    /* Top | Right | Bottom | Left */
  
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 30px;
  padding-left: 40px;
  
  margin: 10px;
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 30px;
  margin-left: 40px;
}
```

### Border
```css
.element {
  border: 1px solid #cccccc;
  border-width: 1px;
  border-style: solid;       /* solid | dashed | dotted */
  border-color: #cccccc;
  border-radius: 8px;
  
  border-top: 1px solid #ccc;
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: #ccc;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}
```

## Positioning

### Position
```css
.element {
  position: relative;    /* relative | absolute | fixed */
  top: 10px;
  right: 20px;
  bottom: 30px;
  left: 40px;
  z-index: 10;
}

/* Fixed positioning for overlays */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 999;
}
```

**Note:** `position: sticky` is NOT supported on native platforms.

## Typography

### Font
```css
.text {
  font-size: 28rpx;
  font-weight: bold;        /* normal | bold | 100-900 */
  font-style: normal;       /* normal | italic */
  font-family: "SimHei";    /* Font family */
  line-height: 1.5;         /* Line height multiplier */
  letter-spacing: 1px;      /* Character spacing */
}
```

### Text
```css
.text {
  color: #333333;
  text-align: center;       /* left | center | right */
  text-decoration: underline;  /* none | underline | line-through */
  text-decoration-color: #ff0000;
  text-decoration-line: underline;
  text-decoration-style: solid;  /* solid | dashed | dotted */
  text-decoration-thickness: 2px;
  text-overflow: ellipsis;  /* clip | ellipsis */
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  white-space: nowrap;      /* normal | nowrap | pre | pre-line | pre-wrap */
  word-break: break-all;    /* normal | break-all | break-word */
  word-wrap: break-word;    /* normal | break-word */
  overflow-wrap: break-word;
}
```

**Important:** On native platforms, text styles do NOT inherit from parent. Always apply text styles directly to `<text>` components.

## Background

```css
.element {
  background-color: #ffffff;
  background-image: url('/static/bg.png');
  background-size: cover;       /* contain | cover | auto | <width> <height> */
  background-position: center;  /* top | center | bottom | left | right */
  background-repeat: no-repeat; /* repeat | no-repeat | repeat-x | repeat-y */
}
```

## Visual Effects

### Opacity
```css
.element {
  opacity: 0.8;    /* 0.0 to 1.0 */
}
```

### Box Shadow
```css
.element {
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
  /* offset-x | offset-y | blur-radius | spread-radius | color */
}
```

### Transform
```css
.element {
  transform: translate(10px, 20px);
  transform: scale(1.5);
  transform: rotate(45deg);
  transform: skew(10deg, 20deg);
  transform-origin: center center;  /* top left | center | bottom right | <x> <y> */
}
```

### Transition
```css
.element {
  transition: all 0.3s ease;
  transition-property: opacity, transform;
  transition-duration: 300ms;
  transition-timing-function: ease;  /* linear | ease | ease-in | ease-out | ease-in-out */
  transition-delay: 0ms;
}
```

### Visibility
```css
.element {
  visibility: visible;    /* visible | hidden */
  /* hidden: takes up space but invisible */
  /* display: none: does not take up space */
}
```

### Overflow
```css
.element {
  overflow: hidden;       /* visible | hidden | scroll | auto */
  overflow-x: hidden;
  overflow-y: scroll;
}
```

## Safe Area

```css
.safe-area {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* Full screen with safe area */
.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
}
```

## Pointer Events

```css
.element {
  pointer-events: auto;    /* auto | none */
  /* none: element does not receive touch/click events */
}
```

## CSS Variables

```css
/* Define in App.uvue for global use */
:root {
  --primary-color: #007AFF;
  --text-color: #333333;
  --bg-color: #f5f5f5;
  --font-size-sm: 24rpx;
  --font-size-md: 28rpx;
  --font-size-lg: 32rpx;
  --spacing-sm: 10rpx;
  --spacing-md: 20rpx;
  --spacing-lg: 30rpx;
  --border-radius: 8px;
}

.element {
  color: var(--primary-color);
  font-size: var(--font-size-md);
  padding: var(--spacing-md);
  border-radius: var(--border-radius);
}
```

## Conditional Compilation in CSS

```css
/* Platform-specific styles */
/* #ifdef APP-PLUS */
.native-only {
  padding-top: env(safe-area-inset-top);
}
/* #endif */

/* #ifdef H5 */
.web-only {
  cursor: pointer;
}
/* #endif */

/* #ifdef MP-WEIXIN */
.mini-program-only {
  -webkit-overflow-scrolling: touch;
}
/* #endif */
```

## Common Layout Patterns

### Centered Content
```css
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### Horizontal List
```css
.horizontal-list {
  display: flex;
  flex-direction: row;
  overflow-x: scroll;
}

.horizontal-list .item {
  flex-shrink: 0;  /* Prevent items from shrinking */
  margin-right: 20rpx;
}
```

### Sticky Header
```css
/* Note: position: sticky not supported on native */
/* Use scroll-view's sticky-header component instead */
```

### Full Height Page
```css
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.page-header {
  /* Fixed height header */
}

.page-content {
  flex: 1;  /* Takes remaining space */
}

.page-footer {
  /* Fixed height footer */
}
```

## Unsupported CSS Features

The following CSS features are NOT supported or have limited support on native platforms:

- `position: sticky` - Not supported on native
- `float` - Not supported (use flexbox instead)
- `display: grid` - Limited support
- `display: inline-block` - Limited support
- `::before` / `::after` pseudo-elements - Not supported on native
- `:hover` / `:active` pseudo-classes - Not supported on native (use hover-class)
- `calc()` - Limited support
- `filter` - Limited support
- `backdrop-filter` - Limited support
- `clip-path` - Not supported
- `writing-mode` - Limited support
- CSS columns - Not supported
- `resize` - Not supported
- `cursor` - Web only
- `outline` - Not supported
- `column-count` / `column-gap` - Not supported
- `box-sizing` - Limited support

## Best Practices

1. **Use rpx for responsive design** - Ensures consistent sizing across devices
2. **Use flexbox as primary layout** - Most reliable cross-platform layout
3. **Apply text styles directly to `<text>`** - No inheritance on native
4. **Avoid web-only CSS** - Check compatibility before using advanced features
5. **Use env(safe-area-inset-*)** - Handle notch and home indicator
6. **Minimize CSS complexity** - Native rendering has different performance characteristics
7. **Test on all target platforms** - CSS rendering may differ between Web and native
8. **Use conditional compilation** - For platform-specific styles
9. **Prefer px over %** - Better performance when parent dimensions are unknown
10. **Specify explicit dimensions** - Reduces layout calculation passes
