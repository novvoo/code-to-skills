# MUI Styling Reference (Source-Derived from v9)

Deep dive into MUI's styling approaches based on the actual source code in `@mui/system/src/` and `@mui/styled-engine/`.

---

## Styling Approaches Comparison

| Approach | Best For | Runtime Cost | Reusability | Theme Access |
|----------|----------|-------------|-------------|-------------|
| **sx prop** | One-off styles, rapid prototyping | Low (cached) | Low | Yes |
| **styled()** | Reusable styled components | Medium | High | Yes |
| **Theme overrides** | App-wide consistency | None (merged at creation) | Global | Yes |
| **Pigment CSS** | Production performance | Zero (build-time) | High | Yes |
| **CSS Layers** | Specificity control | None | Medium | Yes |

---

## sx Prop

From `@mui/system/src/styleFunctionSx/`:

The sx prop is a superset of CSS that provides theme-aware shortcuts. It's available on all MUI components and on Box.

### All Shorthand Mappings

From `defaultSxConfig.js` and `AliasesCSSProperties.ts`:

| sx Shorthand | CSS Property | Theme Mapping |
|-------------|-------------|---------------|
| `m` | margin | `theme.spacing(value)` |
| `mt` | marginTop | `theme.spacing(value)` |
| `mr` | marginRight | `theme.spacing(value)` |
| `mb` | marginBottom | `theme.spacing(value)` |
| `ml` | marginLeft | `theme.spacing(value)` |
| `mx` | marginLeft + marginRight | `theme.spacing(value)` |
| `my` | marginTop + marginBottom | `theme.spacing(value)` |
| `margin` | margin | Direct CSS value |
| `p` | padding | `theme.spacing(value)` |
| `pt` | paddingTop | `theme.spacing(value)` |
| `pr` | paddingRight | `theme.spacing(value)` |
| `pb` | paddingBottom | `theme.spacing(value)` |
| `pl` | paddingLeft | `theme.spacing(value)` |
| `px` | paddingLeft + paddingRight | `theme.spacing(value)` |
| `py` | paddingTop + paddingBottom | `theme.spacing(value)` |
| `padding` | padding | Direct CSS value |
| `bgcolor` | backgroundColor | `theme.palette[value]` |
| `color` | color | `theme.palette[value]` |
| `gap` | gap | `theme.spacing(value)` |
| `columnGap` | columnGap | `theme.spacing(value)` |
| `rowGap` | rowGap | `theme.spacing(value)` |
| `borderRadius` | borderRadius | `theme.shape.borderRadius * value` (if number) |
| `boxShadow` | boxShadow | `theme.shadows[value]` (if number) |
| `zIndex` | zIndex | `theme.zIndex[value]` (if string) |
| `typography` | fontFamily + fontWeight + fontSize + lineHeight + letterSpacing | `theme.typography[value]` |
| `displayPrint` | display (print media) | Direct CSS value |
| `fontFamily` | fontFamily | `theme.typography[value]` (if string) |
| `fontSize` | fontSize | Direct CSS value |
| `fontStyle` | fontStyle | Direct CSS value |
| `fontWeight` | fontWeight | Direct CSS value |
| `letterSpacing` | letterSpacing | Direct CSS value |
| `lineHeight` | lineHeight | Direct CSS value |
| `textAlign` | textAlign | Direct CSS value |
| `textTransform` | textTransform | Direct CSS value |
| `minWidth` | minWidth | Direct CSS value |
| `maxWidth` | maxWidth | Direct CSS value |
| `minHeight` | minHeight | Direct CSS value |
| `maxHeight` | maxHeight | Direct CSS value |
| `width` | width | Direct CSS value |
| `height` | height | Direct CSS value |
| `overflow` | overflow | Direct CSS value |
| `textOverflow` | textOverflow | Direct CSS value |
| `visibility` | visibility | Direct CSS value |
| `whiteSpace` | whiteSpace | Direct CSS value |

### Palette Value Resolution

When you use a string value for `color`, `bgcolor`, or `borderColor`, MUI resolves it through the palette:

```tsx
// These are equivalent:
<Box sx={{ color: 'primary.main' }} />
<Box sx={{ color: (theme) => theme.palette.primary.main }} />

// Grey scale
<Box sx={{ bgcolor: 'grey.100' }} />
<Box sx={{ bgcolor: 'text.primary' }} />
<Box sx={{ bgcolor: 'background.default' }} />
<Box sx={{ bgcolor: 'action.hover' }} />

// Custom palette colors (with augmentation)
<Box sx={{ color: 'brand.main' }} />
```

### Spacing Value Resolution

Number values for margin/padding/gap go through `theme.spacing()`:

```tsx
<Box sx={{ p: 2 }} />    // padding: 16px (2 * 8px)
<Box sx={{ p: 0.5 }} />  // padding: 4px (0.5 * 8px)
<Box sx={{ p: '16px' }} />  // padding: 16px (string bypasses spacing)
<Box sx={{ gap: 2 }} />  // gap: 16px
```

### Responsive Values

```tsx
// Object syntax — breakpoint keys from theme.breakpoints.keys
<Box sx={{
  fontSize: { xs: '0.875rem', sm: '1rem', md: '1.125rem', lg: '1.25rem', xl: '1.5rem' },
  display: { xs: 'none', md: 'flex' },
  p: { xs: 1, sm: 2, md: 3 },
}} />

// Array syntax — maps to [xs, sm, md, lg, xl]
<Box sx={[{ p: 1 }, { p: 2 }, { p: 3 }]} />

// Callback syntax — access full theme
<Box sx={(theme) => ({
  bgcolor: theme.palette.mode === 'dark' ? 'grey.900' : 'grey.50',
  color: theme.palette.text.primary,
})} />
```

### Pseudo-selectors and Pseudo-classes

```tsx
<Box sx={{
  '&:hover': { bgcolor: 'primary.light' },
  '&:focus-visible': { outline: '2px solid', outlineColor: 'primary.main' },
  '&:active': { transform: 'scale(0.98)' },
  '&::before': { content: '""', display: 'block' },
  '&::after': { content: '"→"', ml: 1 },
}} />

// MUI state classes
<Button sx={{
  '&.Mui-disabled': { bgcolor: 'grey.200', color: 'grey.500' },
  '&.Mui-focusVisible': { boxShadow: 2 },
}} />

// Target child MUI components
<Box sx={{
  '& .MuiTextField-root': { mb: 2 },
  '& .MuiOutlinedInput-root': { borderRadius: 2 },
  '& .MuiInputLabel-root': { fontWeight: 600 },
}} />
```

### MUI State Classes Reference

Common state classes available on all MUI components:

| Class | When Applied |
|-------|-------------|
| `.Mui-disabled` | Component is disabled |
| `.Mui-focusVisible` | Keyboard focus |
| `.Mui-error` | Error state |
| `.Mui-selected` | Selected state |
| `.Mui-checked` | Checked state (Checkbox, Radio) |
| `.Mui-expanded` | Expanded state (Accordion, Drawer) |
| `.Mui-active` | Active state (Slider, Step) |
| `.Mui-completed` | Completed state (Step) |
| `.Mui-hidden` | Hidden state |
| `.Mui-required` | Required field |
| `.Mui-filled` | Input has value |
| `.Mui-readOnly` | Read-only state |

### Composition with Arrays

```tsx
// Merge multiple sx objects (later ones override)
<Box sx={[
  { p: 2, bgcolor: 'grey.100' },
  highlight && { bgcolor: 'primary.light' },
  { '&:hover': { bgcolor: 'grey.200' } },
]} />

// Conditional styles
<Box sx={[
  baseStyles,
  isActive && activeStyles,
  isDisabled && disabledStyles,
]} />
```

---

## styled() API

From `@mui/system/src/createStyled/createStyled.d.ts`:

### Basic Usage

```tsx
import { styled } from '@mui/material/styles';

// Style a MUI component
const StyledButton = styled(Button)(({ theme }) => ({
  borderRadius: 20,
  textTransform: 'none',
  fontWeight: 600,
}));

// Style an HTML element
const StyledDiv = styled('div')(({ theme }) => ({
  padding: theme.spacing(2),
  backgroundColor: theme.palette.background.paper,
}));

// Style a third-party component
const StyledLink = styled(Link)(({ theme }) => ({
  color: theme.palette.primary.main,
  textDecoration: 'none',
}));
```

### With Dynamic Props

```tsx
import { styled } from '@mui/material/styles';

const StyledCard = styled(Card, {
  shouldForwardProp: (prop) => prop !== 'highlighted' && prop !== 'variant2',
})<{ highlighted?: boolean; variant2?: 'solid' | 'outline' }>(
  ({ theme, highlighted, variant2 }) => ({
    border: highlighted ? `2px solid ${theme.palette.primary.main}` : '1px solid',
    borderColor: highlighted ? theme.palette.primary.main : theme.palette.divider,
    borderRadius: theme.shape.borderRadius * 2,
    transition: theme.transitions.create(['border', 'box-shadow']),
    ...(variant2 === 'solid' && {
      backgroundColor: theme.palette.primary.main,
      color: theme.palette.primary.contrastText,
    }),
    ...(variant2 === 'outline' && {
      backgroundColor: 'transparent',
      border: `2px solid ${theme.palette.primary.main}`,
    }),
  }),
);
```

### Composing styled Components

```tsx
const BaseButton = styled(Button)(({ theme }) => ({
  borderRadius: 20,
  textTransform: 'none',
}));

const PrimaryButton = styled(BaseButton)(({ theme }) => ({
  backgroundColor: theme.palette.primary.main,
  '&:hover': { backgroundColor: theme.palette.primary.dark },
}));
```

### shouldForwardProp

Control which props are forwarded to the DOM element:

```tsx
const StyledBox = styled(Box, {
  shouldForwardProp: (prop) => !['customColor', 'customSize'].includes(prop),
})<{ customColor?: string; customSize?: number }>(
  ({ theme, customColor, customSize }) => ({
    backgroundColor: customColor || theme.palette.background.paper,
    padding: customSize || theme.spacing(2),
  }),
);
```

---

## CSS Layers (MUI v9)

MUI v9 supports CSS `@layer` for specificity management.

### Default Layer Order

```css
@layer reset, mui, mui-custom, components, utilities;
```

### Enabling CSS Layers

```tsx
const theme = createTheme({
  cssVariables: {
    cssLayer: true,
  },
});
```

### Custom Layer Order

```css
/* In your global CSS */
@layer reset, base, mui, mui-custom, components, utilities, app;

/* Your custom styles in a specific layer */
@layer app {
  .my-custom-class { color: red; }
}
```

### Why CSS Layers Matter

Without layers, specificity battles between MUI styles and custom styles require `!important` or increasing specificity. With layers, you can guarantee your styles win regardless of specificity:

```css
/* Even though .MuiButton-root has higher specificity, this wins because it's in a later layer */
@layer app {
  .MuiButton-root { border-radius: 0; }
}
```

---

## Pigment CSS (Zero-Runtime)

From `@mui/material-pigment-css/`:

Pigment CSS is MUI's zero-runtime CSS-in-JS solution. Styles are extracted at build time, eliminating runtime overhead.

### Installation

```bash
npm install @mui/material-pigment-css
```

### Usage

```tsx
// Instead of @mui/material, import from @mui/material-pigment-css
import Box from '@mui/material-pigment-css/Box';
import Stack from '@mui/material-pigment-css/Stack';

// styled works the same way, but styles are extracted at build time
import { styled } from '@mui/material-pigment-css/styles';

const StyledCard = styled(Card)(({ theme }) => ({
  borderRadius: 12,
  padding: theme.spacing(2),
}));

// css function for one-off styles
import { css } from '@mui/material-pigment-css';

const className = css({
  color: 'primary.main',
  padding: 2,
});
```

### Vite Configuration

```typescript
// vite.config.ts
import pigment from '@mui/material-pigment-css/vite';

export default defineConfig({
  plugins: [react(), pigment()],
});
```

### Next.js Configuration

```javascript
// next.config.mjs
import pigment from '@mui/material-pigment-css/nextjs';

const nextConfig = pigment({
  reactStrictMode: true,
});

export default nextConfig;
```

### Limitations

- No dynamic styles based on props (use CSS custom properties instead)
- No `sx` prop callback with runtime values
- Theme values must be static (extracted at build time)
- Component state classes still work (hover, focus, etc.)

---

## Styled Engine

From `@mui/styled-engine/src/index.d.ts`:

MUI uses `@emotion/styled` as the default styled engine. You can switch to `styled-components`:

### Switching to styled-components

```bash
npm install @mui/styled-engine-sc styled-components
```

```json
// package.json resolutions
{
  "resolutions": {
    "@mui/styled-engine": "npm:@mui/styled-engine-sc@latest"
  }
}
```

---

## Common Styling Patterns

### Custom Scrollbar

```tsx
<Box sx={{
  overflow: 'auto',
  '&::-webkit-scrollbar': { width: 6, height: 6 },
  '&::-webkit-scrollbar-track': { bgcolor: 'transparent' },
  '&::-webkit-scrollbar-thumb': {
    bgcolor: 'grey.400',
    borderRadius: 3,
    '&:hover': { bgcolor: 'grey.600' },
  },
  scrollbarWidth: 'thin',
  scrollbarColor: 'grey.400 transparent',
}} />
```

### Truncate Text

```tsx
// Single line
<Typography sx={{
  overflow: 'hidden',
  textOverflow: 'ellipsis',
  whiteSpace: 'nowrap',
  maxWidth: 200,
}} />

// Multi-line
<Typography sx={{
  display: '-webkit-box',
  WebkitLineClamp: 3,
  WebkitBoxOrient: 'vertical',
  overflow: 'hidden',
}} />
```

### Sticky Header

```tsx
<AppBar sx={{
  position: 'sticky',
  top: 0,
  zIndex: (theme) => theme.zIndex.appBar,
}} />
```

### Glassmorphism

```tsx
<Box sx={{
  backdropFilter: 'blur(10px)',
  bgcolor: 'rgba(255, 255, 255, 0.7)',
  border: '1px solid rgba(255, 255, 255, 0.3)',
  borderRadius: 2,
  p: 3,
}} />
```

### Gradient Text

```tsx
<Typography sx={{
  background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
  backgroundClip: 'text',
  WebkitBackgroundClip: 'text',
  WebkitTextFillColor: 'transparent',
}} />
```

### Responsive Grid of Cards

```tsx
<Box sx={{
  display: 'grid',
  gridTemplateColumns: {
    xs: '1fr',
    sm: 'repeat(2, 1fr)',
    md: 'repeat(3, 1fr)',
    lg: 'repeat(4, 1fr)',
  },
  gap: 3,
}}>
  {cards.map(card => <Card key={card.id} {...card} />)}
</Box>
```

### Hover Card Lift

```tsx
<Card sx={{
  transition: (theme) => theme.transitions.create(['transform', 'box-shadow']),
  '&:hover': {
    transform: 'translateY(-4px)',
    boxShadow: 8,
  },
}} />
```

---

## Migration from Other Styling Solutions

### From styled-components

```tsx
// Before
import styled from 'styled-components';
const Button = styled.button`background: ${props => props.theme.primary};`;

// After (MUI styled)
import { styled } from '@mui/material/styles';
const Button = styled(MuiButton)(({ theme }) => ({
  background: theme.palette.primary.main,
}));
```

### From inline styles

```tsx
// Before
<div style={{ padding: 16, backgroundColor: '#f5f5f5' }} />

// After
<Box sx={{ p: 2, bgcolor: 'grey.100' }} />
```

### From CSS modules

```tsx
// Before
import styles from './Component.module.css';
<div className={styles.container} />

// After
<Box sx={{ p: 2, bgcolor: 'background.paper', borderRadius: 1 }} />
```

### From Tailwind CSS

```tsx
// Before
<div className="p-4 bg-gray-100 rounded-lg shadow-md hover:bg-gray-200" />

// After
<Box sx={{
  p: 1,
  bgcolor: 'grey.100',
  borderRadius: 1,
  boxShadow: 2,
  '&:hover': { bgcolor: 'grey.200' },
}} />
```
