# MUI Theming Reference (Source-Derived from v9)

Complete API reference for the MUI theming system — derived from the actual source code in `@mui/system/src/createTheme/` and `@mui/material/src/styles/`.

---

## Theme Object Structure

From `@mui/system/src/createTheme/createTheme.d.ts`:

```typescript
interface Theme {
  breakpoints: Breakpoints;
  direction: 'ltr' | 'rtl';
  mixins: Mixins;
  components?: Components;
  palette: Palette;
  shadows: Shadows;
  spacing: Spacing;
  shape: Shape;
  transitions: Transitions;
  typography: Typography;
  zIndex: ZIndex;
  cssVariables?: CssVariablesThemeOptions;
  colorSchemes?: ColorSchemes;
  vars?: Record<string, any>; // CSS variable values (when cssVariables: true)
}
```

---

## createTheme()

From `@mui/system/src/createTheme/createTheme.ts`:

```tsx
import { createTheme } from '@mui/material/styles';

// Basic usage — extends default theme
const theme = createTheme();

// With customizations
const theme = createTheme({
  palette: { primary: { main: '#1976d2' } },
  typography: { fontFamily: '"Inter", sans-serif' },
});

// With CSS variables
const theme = createTheme({
  cssVariables: true,
  colorSchemes: {
    light: { palette: { primary: { main: '#1976d2' } } },
    dark: { palette: { primary: { main: '#90caf9' } } },
  },
});

// Extend theme with custom properties
declare module '@mui/material/styles' {
  interface Theme {
    status: { danger: string };
  }
  interface ThemeOptions {
    status?: { danger?: string };
  }
}

const theme = createTheme({
  status: { danger: '#e53e3e' },
});
```

### createTheme Options

From the source type definitions:

```typescript
interface ThemeOptions {
  breakpoints?: BreakpointsOptions;
  direction?: 'ltr' | 'rtl';
  mixins?: MixinsOptions;
  components?: Components;
  palette?: PaletteOptions;
  shadows?: Shadows;
  spacing?: SpacingOptions;
  shape?: ShapeOptions;
  transitions?: TransitionsOptions;
  typography?: TypographyOptions;
  zIndex?: ZIndexOptions;
  cssVariables?: boolean | CssVariablesThemeOptions;
  colorSchemes?: ColorSchemesOptions;
}
```

---

## Breakpoints

From `@mui/system/src/createBreakpoints/createBreakpoints.d.ts`:

### Default Values

```typescript
{
  keys: ['xs', 'sm', 'md', 'lg', 'xl'],
  values: {
    xs: 0,     // Extra small: 0px+
    sm: 600,   // Small: 600px+
    md: 900,   // Medium: 900px+
    lg: 1200,  // Large: 1200px+
    xl: 1536,  // Extra large: 1536px+
  },
  unit: 'px',
}
```

### Custom Breakpoints

```tsx
const theme = createTheme({
  breakpoints: {
    values: {
      mobile: 0,
      tablet: 640,
      laptop: 1024,
      desktop: 1280,
    },
  },
});
```

### Breakpoint Methods

```typescript
interface Breakpoints {
  keys: string[];
  values: Record<string, number>;
  up: (key: string | number) => string;       // '@media (min-width:XXXpx)'
  down: (key: string | number) => string;     // '@media (max-width:XXXpx)'
  between: (start, end) => string;            // '@media (min-width:X) and (max-width:Y)'
  only: (key: string) => string;              // '@media (min-width:X) and (max-width:Y)'
  not: (key: string) => string;               // Inverse of only
}
```

```tsx
// Usage in sx prop
<Box sx={{
  display: { xs: 'none', md: 'flex' },  // hidden on mobile, flex on desktop
  fontSize: { sm: '14px', lg: '18px' },
}} />

// Usage in styled
const StyledBox = styled(Box)(({ theme }) => ({
  padding: theme.spacing(2),
  [theme.breakpoints.up('md')]: { padding: theme.spacing(4) },
}));

// Usage in useMediaQuery
const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
```

---

## Palette

From `@mui/material/src/styles/createPalette.d.ts`:

### Default Light Palette

```typescript
{
  mode: 'light',
  primary: {
    main: '#1976d2',
    light: '#42a5f5',
    dark: '#1565c0',
    contrastText: '#fff',
  },
  secondary: {
    main: '#9c27b0',
    light: '#ba68c8',
    dark: '#7b1fa2',
    contrastText: '#fff',
  },
  error: {
    main: '#d32f2f',
    light: '#ef5350',
    dark: '#c62828',
    contrastText: '#fff',
  },
  warning: {
    main: '#ed6c02',
    light: '#ff9800',
    dark: '#e65100',
    contrastText: '#fff',
  },
  info: {
    main: '#0288d1',
    light: '#03a9f4',
    dark: '#01579b',
    contrastText: '#fff',
  },
  success: {
    main: '#2e7d32',
    light: '#4caf50',
    dark: '#1b5e20',
    contrastText: '#fff',
  },
  grey: {
    50: '#fafafa', 100: '#f5f5f5', 200: '#eeeeee', 300: '#e0e0e0',
    400: '#bdbdbd', 500: '#9e9e9e', 600: '#757575', 700: '#616161',
    800: '#424242', 900: '#212121',
    A100: '#f5f5f5', A200: '#eeeeee', A400: '#bdbdbd', A700: '#616161',
  },
  text: {
    primary: 'rgba(0, 0, 0, 0.87)',
    secondary: 'rgba(0, 0, 0, 0.6)',
    disabled: 'rgba(0, 0, 0, 0.38)',
  },
  background: {
    paper: '#fff',
    default: '#fff',
  },
  action: {
    active: 'rgba(0, 0, 0, 0.54)',
    hover: 'rgba(0, 0, 0, 0.04)',
    hoverOpacity: 0.04,
    selected: 'rgba(0, 0, 0, 0.08)',
    selectedOpacity: 0.08,
    disabled: 'rgba(0, 0, 0, 0.26)',
    disabledBackground: 'rgba(0, 0, 0, 0.12)',
    disabledOpacity: 0.38,
    focus: 'rgba(0, 0, 0, 0.12)',
    focusOpacity: 0.12,
    activatedOpacity: 0.12,
  },
  divider: 'rgba(0, 0, 0, 0.12)',
  ContrastDefaultThreshold: 3,
  ContrastTextPrimaryThreshold: 4.5,
  ContrastTextSecondaryThreshold: 3,
}
```

### Custom Palette

```tsx
const theme = createTheme({
  palette: {
    primary: {
      main: '#ff5252',    // Custom primary
      light: '#ff8a80',
      dark: '#d50000',
      contrastText: '#fff',
    },
    // Add custom color intention
    brand: {
      main: '#1a237e',
      light: '#534bae',
      dark: '#000051',
      contrastText: '#fff',
    },
  },
});

// TypeScript augmentation for custom colors
declare module '@mui/material/styles' {
  interface Palette {
    brand: Palette['primary'];
  }
  interface PaletteOptions {
    brand?: PaletteOptions['primary'];
  }
}
```

### Dark Mode

```tsx
// Method 1: Static dark theme
const darkTheme = createTheme({ palette: { mode: 'dark' } });

// Method 2: CSS Variables (recommended for runtime switching)
const theme = createTheme({
  cssVariables: true,
  colorSchemes: {
    light: { palette: { primary: { main: '#1976d2' } } },
    dark: { palette: { primary: { main: '#90caf9' } } },
  },
});

// Method 3: useColorScheme hook
import { useColorScheme } from '@mui/material/styles';

function ThemeToggle() {
  const { mode, setMode } = useColorScheme();
  return <IconButton onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}>...</IconButton>;
}
```

---

## Typography

From `@mui/material/src/styles/createTypography.d.ts`:

### Default Typography Scale

```typescript
{
  fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
  fontSize: 14,  // Base font size in pixels
  htmlFontSize: 16,  // <html> font size
  h1: { fontWeight: 300, fontSize: '6rem', lineHeight: 1.167, letterSpacing: '-0.01562em' },
  h2: { fontWeight: 300, fontSize: '3.75rem', lineHeight: 1.2, letterSpacing: '-0.00833em' },
  h3: { fontWeight: 400, fontSize: '3rem', lineHeight: 1.167, letterSpacing: '0em' },
  h4: { fontWeight: 400, fontSize: '2.125rem', lineHeight: 1.235, letterSpacing: '0.00735em' },
  h5: { fontWeight: 400, fontSize: '1.5rem', lineHeight: 1.334, letterSpacing: '0em' },
  h6: { fontWeight: 500, fontSize: '1.25rem', lineHeight: 1.6, letterSpacing: '0.0075em' },
  subtitle1: { fontWeight: 400, fontSize: '1rem', lineHeight: 1.75, letterSpacing: '0.00938em' },
  subtitle2: { fontWeight: 500, fontSize: '0.875rem', lineHeight: 1.57, letterSpacing: '0.00714em' },
  body1: { fontWeight: 400, fontSize: '1rem', lineHeight: 1.5, letterSpacing: '0.00938em' },
  body2: { fontWeight: 400, fontSize: '0.875rem', lineHeight: 1.43, letterSpacing: '0.01071em' },
  button: { fontWeight: 500, fontSize: '0.875rem', lineHeight: 1.75, letterSpacing: '0.02857em', textTransform: 'uppercase' },
  caption: { fontWeight: 400, fontSize: '0.75rem', lineHeight: 1.66, letterSpacing: '0.03333em' },
  overline: { fontWeight: 400, fontSize: '0.75rem', lineHeight: 2.66, letterSpacing: '0.08333em', textTransform: 'uppercase' },
}
```

### Custom Typography

```tsx
const theme = createTheme({
  typography: {
    fontFamily: '"Inter", "Roboto", "Helvetica", "Arial", sans-serif',
    h1: { fontSize: '2.5rem', fontWeight: 700 },
    // Add custom variant
    customTitle: { fontSize: '1.75rem', fontWeight: 600, lineHeight: 1.3 },
  },
});

// TypeScript augmentation
declare module '@mui/material/styles' {
  interface TypographyVariants { customTitle: React.CSSProperties; }
  interface TypographyVariantsOptions { customTitle?: React.CSSProperties; }
}
declare module '@mui/material/Typography' {
  interface TypographyPropsVariantOverrides { customTitle: true; }
}
```

### responsiveFontSizes()

Automatically scale typography across breakpoints:

```tsx
import { createTheme, responsiveFontSizes } from '@mui/material/styles';

let theme = createTheme();
theme = responsiveFontSizes(theme, {
  factor: 2,           // Scaling factor (default: 2)
  breakpoints: ['sm', 'md', 'lg'],  // Breakpoints to scale
  variants: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],  // Variants to scale
});
```

---

## Spacing

From `@mui/system/src/spacing/spacing.ts`:

### Default

Base unit: **8px**

```typescript
spacing: (factor: number) => `${8 * factor}px`
// spacing(0) = '0px'
// spacing(0.5) = '4px'
// spacing(1) = '8px'
// spacing(2) = '16px'
// spacing(3) = '24px'
// spacing(4) = '32px'
```

### Custom Spacing

```tsx
const theme = createTheme({
  spacing: 4,  // 4px base unit (spacing(2) = '8px')
});

// Or custom function
const theme = createTheme({
  spacing: (factor) => `${0.25 * factor}rem`,  // 0.25rem base
});
```

### Usage

```tsx
// In sx prop
<Box sx={{ p: 2, m: 1, gap: 2 }} />  // padding: 16px, margin: 8px, gap: 16px

// In styled
const StyledBox = styled(Box)(({ theme }) => ({
  padding: theme.spacing(2, 3),  // '16px 24px'
  margin: theme.spacing(1, 2, 3, 4),  // '8px 16px 24px 32px'
}));
```

---

## Shape

From `@mui/system/src/createTheme/shape.ts`:

```typescript
{
  borderRadius: 4,  // Default border radius in pixels
}
```

```tsx
const theme = createTheme({
  shape: { borderRadius: 8 },
});

// Usage
<Box sx={{ borderRadius: (theme) => theme.shape.borderRadius * 2 }} />
```

---

## Shadows

From `@mui/material/src/styles/shadows.js`:

25 elevation levels (0-24):

```typescript
shadows: [
  'none',  // 0
  '0px 2px 1px -1px rgba(0,0,0,0.2),0px 1px 1px 0px rgba(0,0,0,0.14),0px 1px 3px 0px rgba(0,0,0,0.12)',  // 1
  '0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12)',  // 2
  // ... 3-23
  '0px 11px 15px -7px rgba(0,0,0,0.2),0px 24px 38px 3px rgba(0,0,0,0.14),0px 9px 46px 8px rgba(0,0,0,0.12)',  // 24
]
```

```tsx
// Usage in sx
<Box sx={{ boxShadow: 1 }} />  // theme.shadows[1]
<Box sx={{ boxShadow: 24 }} />  // theme.shadows[24]

// Custom shadows
const theme = createTheme({
  shadows: [...shadows.slice(0, 24), '0px 20px 60px rgba(0,0,0,0.3)'],  // Override level 24
});
```

---

## zIndex

From `@mui/material/src/styles/zIndex.d.ts`:

```typescript
{
  mobileStepper: 1000,
  fab: 1050,
  speedDial: 1050,
  appBar: 1100,
  drawer: 1200,
  modal: 1300,
  snackbar: 1400,
  tooltip: 1500,
}
```

```tsx
// Usage
<Box sx={{ zIndex: (theme) => theme.zIndex.drawer }} />
<AppBar sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }} />
```

---

## Transitions

From `@mui/material/src/styles/transitions.d.ts`:

```typescript
{
  easing: {
    easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
    easeOut: 'cubic-bezier(0.0, 0, 0.2, 1)',
    easeIn: 'cubic-bezier(0.4, 0, 1, 1)',
    sharp: 'cubic-bezier(0.4, 0, 0.6, 1)',
  },
  duration: {
    shortest: 150,
    shorter: 200,
    short: 250,
    standard: 300,
    complex: 375,
    enteringScreen: 225,
    leavingScreen: 195,
  },
}
```

```tsx
// Usage in styled
const StyledBox = styled(Box)(({ theme }) => ({
  transition: theme.transitions.create('transform', {
    easing: theme.transitions.easing.easeInOut,
    duration: theme.transitions.duration.standard,
  }),
  '&:hover': { transform: 'scale(1.05)' },
}));

// Usage in sx
<Box sx={{
  transition: (theme) => theme.transitions.create('background-color'),
  '&:hover': { bgcolor: 'primary.light' },
}} />
```

---

## Component Overrides

### Style Overrides

```tsx
const theme = createTheme({
  components: {
    // Override styles for a component
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8,
          textTransform: 'none',
          fontWeight: 600,
        },
        containedPrimary: {
          '&:hover': {
            backgroundColor: '#1565c0',
          },
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: { marginTop: 8, marginBottom: 8 },
      },
    },
    MuiChip: {
      styleOverrides: {
        root: { borderRadius: 4 },
      },
    },
  },
});
```

### Default Props

```tsx
const theme = createTheme({
  components: {
    MuiButton: {
      defaultProps: {
        disableElevation: true,
        variant: 'contained',
      },
    },
    MuiTextField: {
      defaultProps: {
        variant: 'outlined',
        size: 'small',
      },
    },
    MuiDialog: {
      defaultProps: {
        maxWidth: 'md',
      },
    },
  },
});
```

### Custom Variants

```tsx
const theme = createTheme({
  components: {
    MuiButton: {
      variants: [
        {
          props: { variant: 'gradient' },
          style: {
            background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
            color: 'white',
            border: 0,
          },
        },
        {
          props: { variant: 'gradient', size: 'large' },
          style: {
            fontSize: '1.125rem',
            padding: '12px 32px',
          },
        },
      ],
    },
  },
});

// TypeScript augmentation
declare module '@mui/material/Button' {
  interface ButtonPropsVariantOverrides { gradient: true }
}
```

---

## CSS Variables Mode

From `@mui/system/src/cssVars/` and `@mui/material/src/styles/`:

### Enabling CSS Variables

```tsx
const theme = createTheme({
  cssVariables: true,  // Simple enable
});

// Or with options
const theme = createTheme({
  cssVariables: {
    cssVarPrefix: 'mui',     // CSS variable prefix: --mui-*
    colorSchemeStorageKey: 'mui-color-scheme',
    modeStorageKey: 'mui-mode',
    rootSelector: ':root',
    disableCssVarsPrepend: false,
  },
});
```

### Accessing CSS Variables

When `cssVariables: true`, theme values are available as CSS variables:

```css
/* Generated CSS variables */
--mui-palette-primary-main: #1976d2;
--mui-palette-background-default: #fff;
--mui-spacing-2: 16px;
--mui-shape-borderRadius: 4px;
```

```tsx
// In custom CSS
<Box sx={{
  bgcolor: 'var(--mui-palette-primary-main)',
  p: 'var(--mui-spacing-2)',
}} />

// Theme vars object (available when cssVariables: true)
const { vars } = theme;
// vars.palette.primary.main → 'var(--mui-palette-primary-main)'
```

### InitColorSchemeScript

From `@mui/system/src/InitColorSchemeScript/InitColorSchemeScript.tsx`:

Prevents flash of incorrect theme on SSR:

```tsx
import InitColorSchemeScript from '@mui/material/InitColorSchemeScript';

// In your HTML template
<html>
  <head>
    <InitColorSchemeScript
      defaultMode="system"
      attribute="data-color-scheme"
      modeStorageKey="mui-mode"
      colorSchemeStorageKey="mui-color-scheme"
    />
  </head>
  <body>
    <ThemeProvider theme={theme}>
      <App />
    </ThemeProvider>
  </body>
</html>
```

**Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultMode` | `'system'` \| `'light'` \| `'dark'` | `'system'` | Default mode |
| `defaultLightColorScheme` | `string` | `'light'` | Default light scheme |
| `defaultDarkColorScheme` | `string` | `'dark'` | Default dark scheme |
| `attribute` | `'class'` \| `'data'` \| `string` | `'data-color-scheme'` | DOM attribute |
| `colorSchemeNode` | `string` | `'document.documentElement'` | Target node |
| `modeStorageKey` | `string` | `'mode'` | localStorage key |
| `colorSchemeStorageKey` | `string` | `'color-scheme'` | localStorage key |
| `nonce` | `string` | — | CSP nonce |

### useColorScheme Hook

```tsx
import { useColorScheme } from '@mui/material/styles';

function ThemeToggle() {
  const { mode, setMode, systemMode, colorScheme, setColorScheme } = useColorScheme();

  return (
    <IconButton onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}>
      {mode === 'dark' ? <LightModeIcon /> : <DarkModeIcon />}
    </IconButton>
  );
}
```

**Return values:**

| Value | Type | Description |
|-------|------|-------------|
| `mode` | `'system'` \| `'light'` \| `'dark'` | Current mode |
| `setMode` | `(mode) => void` | Set mode |
| `systemMode` | `'light'` \| `'dark'` \| `null` | System preference |
| `colorScheme` | `string` | Current color scheme name |
| `setColorScheme` | `(scheme) => void` | Set color scheme |
| `allColorSchemes` | `string[]` | All available schemes |

---

## Theme Utility Functions

### responsiveFontSizes()

```tsx
import { createTheme, responsiveFontSizes } from '@mui/material/styles';

let theme = createTheme();
theme = responsiveFontSizes(theme, {
  factor: 2,
  breakpoints: ['sm', 'md', 'lg'],
  variants: ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
});
```

### adaptV4Theme()

Migrate v4 theme to v5+ format:

```tsx
import { adaptV4Theme, createTheme } from '@mui/material/styles';

const v4Theme = { palette: { primary: { blue: '#1976d2' } } };
const theme = createTheme(adaptV4Theme(v4Theme));
```

### createMuiStrictModeTheme()

For React.StrictMode compatibility:

```tsx
import { unstable_createMuiStrictModeTheme } from '@mui/material/styles';

const theme = unstable_createMuiStrictModeTheme();
```

---

## RTL Support

```tsx
import { CacheProvider } from '@emotion/react';
import createCache from '@emotion/cache';
import { prefixer } from 'stylis';
import rtlPlugin from 'stylis-plugin-rtl';

const rtlCache = createCache({ key: 'muirtl', stylisPlugins: [prefixer, rtlPlugin] });
const ltrCache = createCache({ key: 'mui' });

<CacheProvider value={direction === 'rtl' ? rtlCache : ltrCache}>
  <ThemeProvider theme={createTheme({ direction })}>
    <App />
  </ThemeProvider>
</CacheProvider>
```
