---
name: material-ui
description: "Build React UIs with Material UI (MUI) — the comprehensive Material Design component library. Use this skill whenever the user mentions MUI, Material UI, Material Design components, @mui/material, or wants to build React interfaces with pre-built accessible components like DataGrid, AppBar, Drawer, Dialog, Snackbar, Tabs, Stepper, etc. Also trigger when the user asks about MUI theming, sx prop, styled API, CSS layers, Pigment CSS, or MUI X advanced components (Data Grid, Date Pickers, Charts). Even if the user just says 'React UI components' or 'Material Design', use this skill."
argument-hint: "Describe the MUI component, layout, or feature you want to build"
---

# Material UI (MUI) Development Skill

> **Source**: https://github.com/mui/material-ui | **Version**: v9.x (master branch)
> This skill is derived from the actual MUI source code, including precise Props APIs, default values, CSS class keys, and theme configuration.

## When to Use This Skill

- Building any React UI with Material Design components
- Creating layouts with AppBar, Drawer, Grid, Container, Stack
- Implementing forms with TextField, Select, Checkbox, Radio, Autocomplete
- Adding navigation with Tabs, Breadcrumbs, Stepper, BottomNavigation
- Displaying data with Table, DataGrid, Card, List, Accordion
- Showing feedback with Dialog, Snackbar, Alert, Progress, Badge
- Customizing themes: palette, typography, spacing, shadows, component overrides
- Styling with sx prop, styled API, CSS layers, Pigment CSS
- Using MUI X: DataGrid, Date Pickers, Charts, Tree View

---

## Installation

```bash
# Core packages (MUI v9)
npm install @mui/material @mui/system @emotion/react @emotion/styled

# Icons
npm install @mui/icons-material

# MUI X advanced components
npm install @mui/x-data-grid          # DataGrid
npm install @mui/x-date-pickers dayjs  # Date Pickers
npm install @mui/x-charts              # Charts
npm install @mui/x-tree-view           # Tree View

# Pigment CSS (zero-runtime, optional)
npm install @mui/material-pigment-css
```

### Peer Dependencies

MUI v9 requires:
- `react` >= 17.0.0
- `react-dom` >= 17.0.0
- `@types/react` >= 17.0.0 (TypeScript projects)

---

## Quick Start

```tsx
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

const theme = createTheme();

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Stack direction="row" spacing={2} sx={{ p: 3 }}>
        <Button variant="contained">Primary</Button>
        <Button variant="outlined">Outlined</Button>
        <Button variant="text">Text</Button>
      </Stack>
    </ThemeProvider>
  );
}
```

---

## Component Architecture (Source-Derived)

### Slot Pattern (MUI v9 Standard)

MUI v9 uses the **slot pattern** for component customization. Every composable sub-element is a named slot with `slots.*` and `slotProps.*` props.

```tsx
// Slot pattern — the standard way to customize sub-components
<Dialog
  slots={{ transition: Fade }}         // Override the transition component
  slotProps={{
    backdrop: { sx: { bgcolor: 'rgba(0,0,0,0.8)' } },  // Props for the backdrop slot
    paper: { elevation: 24 },                            // Props for the paper slot
  }}
/>

// Slot pattern on Autocomplete
<Autocomplete
  slots={{ popper: CustomPopper, paper: CustomPaper }}
  slotProps={{ clearIndicator: { size: 'small' } }}
/>
```

**Slot naming convention** (from source code):
| Component | Key Slots |
|-----------|-----------|
| Dialog | `container`, `backdrop`, `paper`, `transition`, `root` |
| Drawer | `root`, `docked`, `paper`, `backdrop`, `transition` |
| Snackbar | `root`, `content`, `clickAwayListener`, `transition` |
| Autocomplete | `root`, `paper`, `popper`, `clearIndicator`, `popupIndicator`, `listbox`, `loading`, `noOptions`, `tag` |
| Tabs | `root`, `scroller`, `scrollbarSize`, `tabScrollButton`, `flexContainer`, `indicator` |
| Tooltip | `popper`, `transition`, `tooltip`, `arrow`, `touch` |
| TextField | `root`, `input`, `inputLabel`, `htmlInput`, `helperText`, `formControl` |
| Button | `root`, `startIcon`, `endIcon`, `loadingIndicator` |
| AppBar | `root` |
| Chip | `root`, `label`, `avatar`, `icon`, `deleteIcon` |
| Badge | `root`, `badge` |
| Slider | `root`, `track`, `thumb`, `valueLabel`, `mark`, `markLabel`, `input` |
| Switch | `root`, `switchBase`, `thumb`, `track`, `input` |
| Pagination | `root`, `ul` |
| Accordion | `root`, `heading`, `transition`, `region` |
| Fab | `root`, `startIcon`, `endIcon`, `loadingIndicator` |
| Rating | `root`, `item`, `label`, `icon`, `emptyIcon`, `decimal`, `visuallyHidden` |

### Component Default Values (Source-Derived)

These are the exact default values from the MUI v9 source code type definitions:

| Component | Prop | Default |
|-----------|------|---------|
| **Button** | `color` | `'primary'` |
| **Button** | `variant` | `'text'` |
| **Button** | `size` | `'medium'` |
| **Button** | `loading` | `null` |
| **Button** | `loadingPosition` | `'center'` |
| **Button** | `disableElevation` | `false` |
| **Button** | `disableFocusRipple` | `false` |
| **Button** | `fullWidth` | `false` |
| **TextField** | `color` | `'primary'` |
| **TextField** | `size` | `'medium'` |
| **TextField** | `variant` | `'outlined'` |
| **TextField** | `disabled` | `false` |
| **TextField** | `error` | `false` |
| **TextField** | `fullWidth` | `false` |
| **TextField** | `multiline` | `false` |
| **TextField** | `required` | `false` |
| **Dialog** | `fullWidth` | `false` |
| **Dialog** | `fullScreen` | `false` |
| **Dialog** | `maxWidth` | `'sm'` |
| **Dialog** | `keepMounted` | `false` |
| **Dialog** | `scroll` | `'paper'` |
| **AppBar** | `color` | `'primary'` |
| **AppBar** | `position` | `'fixed'` |
| **AppBar** | `elevation` | `4` |
| **AppBar** | `enableColorOnDark` | `false` |
| **Drawer** | `anchor` | `'left'` |
| **Drawer** | `variant` | `'temporary'` |
| **Drawer** | `elevation` | `16` |
| **Snackbar** | `anchorOrigin` | `{ vertical: 'bottom', horizontal: 'left' }` |
| **Snackbar** | `autoHideDuration` | `null` |
| **Tabs** | `orientation` | `'horizontal'` |
| **Tabs** | `variant` | `'standard'` |
| **Tabs** | `scrollButtons` | `'auto'` |
| **Tabs** | `indicatorColor` | `'primary'` |
| **Tabs** | `textColor` | `'primary'` |
| **Tabs** | `centered` | `false` |
| **Tooltip** | `placement` | `'bottom'` |
| **Tooltip** | `enterDelay` | `100` |
| **Tooltip** | `enterTouchDelay` | `700` |
| **Tooltip** | `leaveDelay` | `0` |
| **Tooltip** | `leaveTouchDelay` | `1500` |
| **Tooltip** | `disableFocusListener` | `false` |
| **Tooltip** | `disableHoverListener` | `false` |
| **Tooltip** | `disableTouchListener` | `false` |
| **Tooltip** | `arrow` | `false` |
| **Chip** | `color` | `'default'` |
| **Chip** | `variant` | `'filled'` |
| **Chip** | `size` | `'medium'` |
| **Chip** | `disabled` | `false` |
| **Autocomplete** | `size` | `'medium'` |
| **Autocomplete** | `autoHighlight` | `false` |
| **Autocomplete** | `autoSelect` | `false` |
| **Autocomplete** | `blurOnSelect` | `false` |
| **Autocomplete** | `clearOnBlur` | `false` |
| **Autocomplete** | `clearOnEscape` | `false` |
| **Autocomplete** | `disableCloseOnSelect` | `false` |
| **Autocomplete** | `disabled` | `false` |
| **Autocomplete** | `disableListWrap` | `false` |
| **Autocomplete** | `freeSolo` | `false` |
| **Autocomplete** | `includeInputInList` | `false` |
| **Autocomplete** | `openOnFocus` | `false` |
| **Avatar** | `variant` | `'circular'` |
| **Badge** | `color` | `'default'` |
| **Badge** | `variant` | `'standard'` |
| **Badge** | `overlap` | `'rectangular'` |
| **Badge** | `max` | `99` |
| **Badge** | `invisible` | `false` |
| **Badge** | `showZero` | `false` |
| **IconButton** | `color` | `'default'` |
| **IconButton** | `size` | `'medium'` |
| **IconButton** | `loading` | `null` |
| **Fab** | `color` | `'default'` |
| **Fab** | `size` | `'large'` |
| **Fab** | `variant` | `'circular'` |
| **Rating** | `max` | `5` |
| **Rating** | `min` | `1` |
| **Rating** | `size` | `'medium'` |
| **Slider** | `color` | `'primary'` |
| **Slider** | `orientation` | `'horizontal'` |
| **Slider** | `size` | `'medium'` |
| **Slider** | `min` | `0` |
| **Slider** | `max` | `100` |
| **Slider** | `step` | `1` |
| **Slider** | `track` | `'normal'` |
| **Switch** | `color` | `'primary'` |
| **Switch** | `size` | `'medium'` |
| **Select** | `variant` | `'outlined'` |
| **Table** | `size` | `'medium'` |
| **Table** | `stickyHeader` | `false` |
| **Pagination** | `variant` | `'standard'` |
| **Pagination** | `shape` | `'circular'` |
| **Pagination** | `size` | `'medium'` |
| **Pagination** | `color` | `'standard'` |
| **Accordion** | `defaultExpanded` | `false` |
| **Accordion** | `disabled` | `false` |
| **Accordion** | `disableGutters` | `false` |
| **Stepper** | `activeStep` | `0` |
| **Stepper** | `orientation` | `'horizontal'` |
| **Stepper** | `alternativeLabel` | `false` |
| **Stepper** | `nonLinear` | `false` |
| **ToggleButton** | `color` | `'standard'` |
| **ToggleButton** | `size` | `'medium'` |
| **ToggleButtonGroup** | `color` | `'standard'` |
| **ToggleButtonGroup** | `orientation` | `'horizontal'` |
| **ToggleButtonGroup** | `size` | `'medium'` |
| **Toolbar** | `variant` | `'regular'` |

---

## Component Variants (Source-Derived)

Exact variant/color/size options from MUI v9 type definitions:

| Component | `variant` Options | `color` Options | `size` Options |
|-----------|-------------------|-----------------|----------------|
| **Button** | `'text'` \| `'outlined'` \| `'contained'` | `'inherit'` \| `'primary'` \| `'secondary'` \| `'success'` \| `'error'` \| `'info'` \| `'warning'` | `'small'` \| `'medium'` \| `'large'` |
| **Fab** | `'circular'` \| `'extended'` | `'inherit'` \| `'primary'` \| `'secondary'` \| `'success'` \| `'error'` \| `'info'` \| `'warning'` | `'small'` \| `'medium'` \| `'large'` |
| **Chip** | `'filled'` \| `'outlined'` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'small'` \| `'medium'` |
| **Alert** | `'standard'` \| `'filled'` \| `'outlined'` | `'success'` \| `'info'` \| `'warning'` \| `'error'` | — |
| **Avatar** | `'circular'` \| `'rounded'` \| `'square'` | — | — |
| **Badge** | `'standard'` \| `'dot'` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | — |
| **TextField** | `'outlined'` \| `'filled'` \| `'standard'` | `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'small'` \| `'medium'` |
| **FormControl** | `'standard'` \| `'outlined'` \| `'filled'` | `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'small'` \| `'medium'` |
| **Select** | `'outlined'` \| `'filled'` \| `'standard'` | `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'small'` \| `'medium'` |
| **AppBar** | — | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` \| `'transparent'` | — |
| **Drawer** | `'permanent'` \| `'persistent'` \| `'temporary'` | — | — |
| **Tabs** | `'standard'` \| `'scrollable'` \| `'fullWidth'` | — | — |
| **Pagination** | `'text'` \| `'outlined'` | `'standard'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'small'` \| `'medium'` \| `'large'` |
| **ToggleButton** | `'standard'` \| `'filled'` \| `'outlined'` | `'standard'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'small'` \| `'medium'` \| `'large'` |
| **CircularProgress** | `'determinate'` \| `'indeterminate'` | `'inherit'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | — |
| **LinearProgress** | `'buffer'` \| `'determinate'` \| `'indeterminate'` | `'inherit'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | — |
| **Skeleton** | `'circular'` \| `'rectangular'` \| `'rounded'` \| `'text'` | — | — |
| **MobileStepper** | `'text'` \| `'dots'` \| `'progress'` | — | — |
| **Divider** | `'fullWidth'` \| `'inset'` \| `'middle'` | — | — |
| **TableCell** | `'head'` \| `'body'` \| `'footer'` | — | `'small'` \| `'medium'` |

> **Note**: All variant/color/size props support **module augmentation** via `OverridableStringUnion`. You can add custom values:
> ```tsx
> declare module '@mui/material/Button' {
>   interface ButtonPropsVariantOverrides { gradient: true }
>   interface ButtonPropsColorOverrides { brand: true }
> }
> // Now <Button variant="gradient" color="brand" /> is valid TypeScript
> ```

---

## CSS Class Keys (Source-Derived)

Every MUI component generates CSS classes that can be used with `styled()` or the `sx` prop's `& .` selector. These are the exact class keys from `generateUtilityClasses()` in the source:

### Layout Components
| Component | CSS Class Keys |
|-----------|---------------|
| **Box** | `root` |
| **Stack** | `root`, `directionRow`, `directionRowReverse`, `directionColumn`, `directionColumnReverse`, `spacing1`–`spacing10`, `alignItemsFlexStart`, `alignItemsCenter`, `alignItemsFlexEnd`, `alignItemsStretch`, `alignItemsBaseline`, `justifyContentCenter`, `justifyContentFlexStart`, `justifyContentFlexEnd`, `justifyContentSpaceBetween`, `justifyContentSpaceAround`, `flexWrapWrap`, `flexWrapWrapReverse`, `flexWrapNoWrap` |
| **Grid** | `root`, `container`, `item`, `directionRow`, `directionRowReverse`, `directionColumn`, `directionColumnReverse`, `wrapWrap`, `wrapNowrap`, `wrapReverse`, `gridSizeXs`–`gridSizeMd`, `gridOffsetXs`–`gridOffsetMd`, `gridItem`, `zeroColumns` |
| **Container** | `root`, `maxWidthXs`, `maxWidthSm`, `maxWidthMd`, `maxWidthLg`, `maxWidthXl`, `maxWidthFalse`, `disableGutters` |

### Input Components
| Component | CSS Class Keys |
|-----------|---------------|
| **TextField** | `root`, `error`, `marginDense`, `marginNormal`, `fullWidth`, `multiline` |
| **Button** | `root`, `text`, `textPrimary`, `textSecondary`, `textSuccess`, `textError`, `textInfo`, `textWarning`, `outlined`, `outlinedPrimary`, `outlinedSecondary`, `outlinedSuccess`, `outlinedError`, `outlinedInfo`, `outlinedWarning`, `contained`, `containedPrimary`, `containedSecondary`, `containedSuccess`, `containedError`, `containedInfo`, `containedWarning`, `disableElevation`, `focusVisible`, `disabled`, `colorInherit`, `textSizeSmall`, `textSizeMedium`, `textSizeLarge`, `outlinedSizeSmall`, `outlinedSizeMedium`, `outlinedSizeLarge`, `containedSizeSmall`, `containedSizeMedium`, `containedSizeLarge`, `sizeMedium`, `sizeSmall`, `sizeLarge`, `fullWidth`, `startIcon`, `endIcon`, `iconSizeSmall`, `iconSizeMedium`, `iconSizeLarge`, `loading`, `loadingIndicator`, `loadingPositionStart`, `loadingPositionEnd`, `loadingPositionCenter` |
| **IconButton** | `root`, `edgeStart`, `edgeEnd`, `colorInherit`, `colorPrimary`, `colorSecondary`, `colorDefault`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `sizeSmall`, `sizeMedium`, `sizeLarge`, `loading`, `loadingIndicator` |
| **Select** | `root`, `select`, `filled`, `outlined`, `standard`, `disabled`, `focused`, `icon`, `iconOpen`, `iconFilled`, `iconOutlined`, `iconStandard`, `nativeInput`, `error`, `multiple`, `sizeSmall` |
| **Checkbox** | `root`, `checked`, `disabled`, `indeterminate`, `colorPrimary`, `colorSecondary`, `sizeSmall`, `sizeMedium` |
| **Switch** | `root`, `edgeStart`, `edgeEnd`, `switchBase`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `sizeSmall`, `sizeMedium`, `checked`, `disabled`, `input`, `thumb`, `track` |
| **Slider** | `root`, `active`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `dragging`, `focusVisible`, `mark`, `markActive`, `marked`, `markLabel`, `markLabelActive`, `sizeSmall`, `sizeMedium`, `thumb`, `thumbSizeSmall`, `track`, `trackInverted`, `trackFalse`, `valueLabel`, `valueLabelOpen`, `valueLabelCircle`, `valueLabelLabel`, `vertical` |
| **Autocomplete** | `root`, `expanded`, `fullWidth`, `focused`, `focusVisible`, `tag`, `tagSizeSmall`, `tagSizeMedium`, `hasPopupIcon`, `hasClearIcon`, `inputRoot`, `input`, `inputFocused`, `endAdornment`, `clearIndicator`, `popupIndicator`, `popupIndicatorOpen`, `popper`, `popperDisablePortal`, `paper`, `listbox`, `listboxDense`, `option`, `groupLabel`, `groupUl`, `loading`, `noOptions`, `error`, `inputFocused` |

### Navigation Components
| Component | CSS Class Keys |
|-----------|---------------|
| **AppBar** | `root`, `positionFixed`, `positionAbsolute`, `positionSticky`, `positionStatic`, `positionRelative`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `colorTransparent`, `colorInherit` |
| **Drawer** | `root`, `docked`, `paper`, `paperAnchorLeft`, `paperAnchorRight`, `paperAnchorTop`, `paperAnchorBottom`, `paperAnchorDockedLeft`, `paperAnchorDockedRight`, `paperAnchorDockedTop`, `paperAnchorDockedBottom`, `modal` |
| **Tabs** | `root`, `vertical`, `flexContainer`, `flexContainerVertical`, `centered`, `scroller`, `fixed`, `scrollableX`, `scrollableY`, `hideScrollbar`, `scrollButtons`, `scrollButtonsHideMobile`, `indicator`, `sizeSmall`, `sizeMedium`, `sizeLarge` |
| **Tab** | `root`, `labelIcon`, `textColorInherit`, `textColorPrimary`, `textColorSecondary`, `selected`, `disabled`, `fullWidth`, `wrapped`, `iconWrapper` |
| **Stepper** | `root`, `horizontal`, `vertical`, `alternativeLabel`, `padding` |
| **Step** | `root`, `horizontal`, `vertical`, `alternativeLabel`, `completed` |
| **StepLabel** | `root`, `horizontal`, `vertical`, `label`, `active`, `completed`, `error`, `disabled`, `iconContainer`, `alternativeLabel`, `labelContainer` |
| **Pagination** | `root`, `ul`, `outlined`, `text`, `colorPrimary`, `colorSecondary`, `colorStandard`, `sizeSmall`, `sizeMedium`, `sizeLarge` |

### Feedback Components
| Component | CSS Class Keys |
|-----------|---------------|
| **Dialog** | `root`, `scrollPaper`, `scrollBody`, `container`, `paper`, `paperScrollPaper`, `paperScrollBody`, `paperWidthFalse`, `paperWidthXs`, `paperWidthSm`, `paperWidthMd`, `paperWidthLg`, `paperWidthXl`, `paperFullWidth`, `paperFullScreen` |
| **Snackbar** | `root`, `anchorOriginTopLeft`, `anchorOriginTopCenter`, `anchorOriginTopRight`, `anchorOriginBottomLeft`, `anchorOriginBottomCenter`, `anchorOriginBottomRight`, `anchorOriginTopLeft`, `anchorOriginTopCenter`, `anchorOriginTopRight` |
| **Alert** | `root`, `action`, `icon`, `message`, `filled`, `filledSuccess`, `filledInfo`, `filledWarning`, `filledError`, `outlined`, `outlinedSuccess`, `outlinedInfo`, `outlinedWarning`, `outlinedError`, `standard`, `standardSuccess`, `standardInfo`, `standardWarning`, `standardError` |
| **Tooltip** | `tooltip`, `touch`, `tooltipPlacementLeft`, `tooltipPlacementRight`, `tooltipPlacementTop`, `tooltipPlacementBottom`, `arrow`, `popper`, `popperInteractive`, `popperArrow` |
| **Badge** | `root`, `badge`, `badgeColorDefault`, `badgeColorPrimary`, `badgeColorSecondary`, `badgeColorError`, `badgeColorInfo`, `badgeColorSuccess`, `badgeColorWarning`, `invisible`, `badgeVariantStandard`, `badgeVariantDot`, `badgeOverlapRectangular`, `badgeOverlapCircular`, `anchorOriginTopRight`, `anchorOriginTopLeft`, `anchorOriginBottomRight`, `anchorOriginBottomLeft` |
| **Progress** | `root`, `colorPrimary`, `colorSecondary`, `determinate`, `indeterminate`, `buffer`, `query`, `dashed`, `dashedColorPrimary`, `dashedColorSecondary`, `bar`, `barColorPrimary`, `barColorSecondary`, `bar1Determinate`, `bar1Buffer`, `bar2Buffer`, `bar1Indeterminate`, `bar2Indeterminate` |

### Data Display Components
| Component | CSS Class Keys |
|-----------|---------------|
| **Card** | `root`, `outlined` |
| **Chip** | `root`, `sizeSmall`, `sizeMedium`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `clickable`, `clickableColorPrimary`, `clickableColorSecondary`, `deletable`, `deletableColorPrimary`, `deletableColorSecondary`, `outlined`, `filled`, `outlinedPrimary`, `outlinedSecondary`, `filledPrimary`, `filledSecondary`, `avatar`, `avatarSmall`, `avatarMedium`, `avatarColorPrimary`, `avatarColorSecondary`, `icon`, `iconSmall`, `iconMedium`, `iconColorPrimary`, `iconColorSecondary`, `label`, `labelSmall`, `labelMedium`, `deleteIcon`, `deleteIconSmall`, `deleteIconMedium`, `deleteIconColorPrimary`, `deleteIconColorSecondary`, `focusVisible` |
| **Table** | `root`, `stickyHeader`, `sizeSmall`, `sizeMedium` |
| **TableCell** | `root`, `head`, `body`, `footer`, `sizeSmall`, `sizeMedium`, `stickyHeader`, `paddingCheckbox`, `paddingNone`, `alignLeft`, `alignCenter`, `alignRight`, `alignJustify` |
| **Accordion** | `root`, `rounded`, `expanded`, `disabled`, `disableGutters`, `region`, `heading` |
| **Avatar** | `root`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `circular`, `rounded`, `square`, `img`, `fallback` |
| **Typography** | `root`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `subtitle1`, `subtitle2`, `body1`, `body2`, `button`, `caption`, `overline`, `alignLeft`, `alignCenter`, `alignRight`, `alignJustify`, `noWrap`, `gutterBottom`, `paragraph`, `colorInherit`, `colorPrimary`, `colorSecondary`, `colorTextPrimary`, `colorTextSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `displayInline`, `displayBlock` |

---

## Theme System (Source-Derived)

### Default Theme Values

From `@mui/system/src/createTheme/` and `@mui/material/src/styles/`:

```typescript
const defaultTheme = {
  // Breakpoints (from createBreakpoints.ts)
  breakpoints: {
    keys: ['xs', 'sm', 'md', 'lg', 'xl'],
    values: { xs: 0, sm: 600, md: 900, lg: 1200, xl: 1536 },
    unit: 'px',
  },

  // Spacing (from spacing.ts) — 8px base unit
  spacing: (factor: number) => `${8 * factor}px`,  // spacing(2) = '16px'

  // Shape (from shape.ts)
  shape: {
    borderRadius: 4,
  },

  // zIndex (from zIndex.d.ts)
  zIndex: {
    mobileStepper: 1000,
    fab: 1050,
    speedDial: 1050,
    appBar: 1100,
    drawer: 1200,
    modal: 1300,
    snackbar: 1400,
    tooltip: 1500,
  },

  // Shadows (from shadows.js) — 25 elevation levels
  shadows: [
    'none',                                                    // 0
    '0px 2px 1px -1px rgba(0,0,0,0.2),0px 1px 1px 0px rgba(0,0,0,0.14),0px 1px 3px 0px rgba(0,0,0,0.12)',  // 1
    // ... 2-24
  ],

  // Palette (from createPalette.ts)
  palette: {
    mode: 'light',
    primary: { main: '#1976d2', light: '#42a5f5', dark: '#1565c0', contrastText: '#fff' },
    secondary: { main: '#9c27b0', light: '#ba68c8', dark: '#7b1fa2', contrastText: '#fff' },
    error: { main: '#d32f2f', light: '#ef5350', dark: '#c62828', contrastText: '#fff' },
    warning: { main: '#ed6c02', light: '#ff9800', dark: '#e65100', contrastText: '#fff' },
    info: { main: '#0288d1', light: '#03a9f4', dark: '#01579b', contrastText: '#fff' },
    success: { main: '#2e7d32', light: '#4caf50', dark: '#1b5e20', contrastText: '#fff' },
    grey: { 50: '#fafafa', 100: '#f5f5f5', 200: '#eeeeee', 300: '#e0e0e0', 400: '#bdbdbd', 500: '#9e9e9e', 600: '#757575', 700: '#616161', 800: '#424242', 900: '#212121', A100: '#f5f5f5', A200: '#eeeeee', A400: '#bdbdbd', A700: '#616161' },
    text: { primary: 'rgba(0, 0, 0, 0.87)', secondary: 'rgba(0, 0, 0, 0.6)', disabled: 'rgba(0, 0, 0, 0.38)' },
    background: { paper: '#fff', default: '#fff' },
    action: { active: 'rgba(0, 0, 0, 0.54)', hover: 'rgba(0, 0, 0, 0.04)', hoverOpacity: 0.04, selected: 'rgba(0, 0, 0, 0.08)', selectedOpacity: 0.08, disabled: 'rgba(0, 0, 0, 0.26)', disabledBackground: 'rgba(0, 0, 0, 0.12)', disabledOpacity: 0.38, focus: 'rgba(0, 0, 0, 0.12)', focusOpacity: 0.12, activatedOpacity: 0.12 },
    divider: 'rgba(0, 0, 0, 0.12)',
  },

  // Typography (from createTypography.ts)
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    fontSize: 14,
    htmlFontSize: 16,
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
  },

  // Transitions
  transitions: {
    easing: { easeInOut: 'cubic-bezier(0.4, 0, 0.2, 1)', easeOut: 'cubic-bezier(0.0, 0, 0.2, 1)', easeIn: 'cubic-bezier(0.4, 0, 1, 1)', sharp: 'cubic-bezier(0.4, 0, 0.6, 1)' },
    duration: { shortest: 150, shorter: 200, short: 250, standard: 300, complex: 375, enteringScreen: 225, leavingScreen: 195 },
  },
};
```

### Dark Mode with CSS Variables

MUI v9 supports CSS variables mode for runtime theme switching without re-render:

```tsx
import { createTheme, ThemeProvider } from '@mui/material/styles';
import InitColorSchemeScript from '@mui/material/InitColorSchemeScript';

const theme = createTheme({
  cssVariables: true,
  colorSchemes: {
    light: { palette: { primary: { main: '#1976d2' } } },
    dark: { palette: { primary: { main: '#90caf9' } } },
  },
});

// In your layout/root (for SSR flash prevention):
<html>
  <head>
    <InitColorSchemeScript defaultMode="system" />
  </head>
  <body>
    <ThemeProvider theme={theme}>
      <App />
    </ThemeProvider>
  </body>
</html>
```

**InitColorSchemeScript Props** (from source):
| Prop | Default | Description |
|------|---------|-------------|
| `defaultMode` | `'system'` | Default mode when storage is empty: `'system'` \| `'light'` \| `'dark'` |
| `defaultLightColorScheme` | `'light'` | Default light color scheme |
| `defaultDarkColorScheme` | `'dark'` | Default dark color scheme |
| `colorSchemeNode` | `'document.documentElement'` | Node to attach color-scheme attribute |
| `modeStorageKey` | `'mode'` | localStorage key for mode |
| `colorSchemeStorageKey` | `'color-scheme'` | localStorage key for color scheme |
| `attribute` | `'data-color-scheme'` | DOM attribute for color scheme. `'class'` \| `'data'` \| custom string |
| `nonce` | — | CSP nonce for inline script |

### useColorScheme Hook

```tsx
import { useColorScheme } from '@mui/material/styles';

function ThemeToggle() {
  const { mode, setMode, systemMode } = useColorScheme();
  return (
    <IconButton onClick={() => setMode(mode === 'dark' ? 'light' : 'dark')}>
      {mode === 'dark' ? <LightMode /> : <DarkMode />}
    </IconButton>
  );
}
```

---

## Styling System (Source-Derived)

### sx Prop — All Shorthand Mappings

From `@mui/system/src/styleFunctionSx/defaultSxConfig.js` and `AliasesCSSProperties.ts`:

| sx Shorthand | CSS Property | Theme Mapping |
|-------------|-------------|---------------|
| `m` | margin | `theme.spacing(value)` |
| `mt` | marginTop | `theme.spacing(value)` |
| `mr` | marginRight | `theme.spacing(value)` |
| `mb` | marginBottom | `theme.spacing(value)` |
| `ml` | marginLeft | `theme.spacing(value)` |
| `mx` | marginLeft + marginRight | `theme.spacing(value)` |
| `my` | marginTop + marginBottom | `theme.spacing(value)` |
| `p` | padding | `theme.spacing(value)` |
| `pt` | paddingTop | `theme.spacing(value)` |
| `pr` | paddingRight | `theme.spacing(value)` |
| `pb` | paddingBottom | `theme.spacing(value)` |
| `pl` | paddingLeft | `theme.spacing(value)` |
| `px` | paddingLeft + paddingRight | `theme.spacing(value)` |
| `py` | paddingTop + paddingBottom | `theme.spacing(value)` |
| `bgcolor` | backgroundColor | `theme.palette[value]` |
| `color` | color | `theme.palette[value]` |
| `gap` | gap | `theme.spacing(value)` |
| `borderRadius` | borderRadius | `theme.shape.borderRadius * value` (if number) |
| `boxShadow` | boxShadow | `theme.shadows[value]` (if number) |
| `zIndex` | zIndex | `theme.zIndex[value]` (if string) |
| `typography` | fontFamily + fontWeight + fontSize + lineHeight + letterSpacing | `theme.typography[value]` |
| `displayPrint` | display (print media) | Direct CSS value |

### sx Prop — Responsive Values

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

### styled() API

From `@mui/system/src/createStyled/createStyled.d.ts`:

```tsx
import { styled } from '@mui/material/styles';

// Style a MUI component
const StyledButton = styled(Button)(({ theme }) => ({
  borderRadius: 20,
  textTransform: 'none',
  fontWeight: 600,
}));

// With dynamic props
const StyledCard = styled(Card, { shouldForwardProp: (prop) => prop !== 'highlighted' })<{
  highlighted?: boolean;
}>(({ theme, highlighted }) => ({
  border: highlighted ? `2px solid ${theme.palette.primary.main}` : 'none',
  transition: theme.transitions.create('border'),
}));

// Compose multiple style overrides
const CustomButton = styled(Button)(({ theme }) => ({
  ...theme.components?.MuiButton?.styleOverrides?.root,
  borderRadius: 20,
}));
```

### CSS Layers (MUI v9)

MUI v9 uses CSS `@layer` to manage specificity:

```css
/* MUI's default layer order */
@layer reset, mui, mui-custom, components, utilities;
```

```tsx
// Configure layers in your theme
const theme = createTheme({
  cssVariables: {
    cssLayer: true,  // Enable CSS layers
  },
});
```

---

## Layout Patterns

### Responsive Sidebar + Content

```tsx
import Box from '@mui/material/Box';
import AppBar from '@mui/material/AppBar';
import Drawer from '@mui/material/Drawer';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

const DRAWER_WIDTH = 240;

export default function ResponsiveLayout() {
  const [mobileOpen, setMobileOpen] = React.useState(false);

  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar position="fixed" sx={{ zIndex: (t) => t.zIndex.drawer + 1 }}>
        <Toolbar>
          <IconButton color="inherit" edge="start" onClick={() => setMobileOpen(!mobileOpen)} sx={{ mr: 2, display: { sm: 'none' } }}>
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap>My App</Typography>
        </Toolbar>
      </AppBar>

      {/* Mobile drawer */}
      <Drawer variant="temporary" open={mobileOpen} onClose={() => setMobileOpen(false)}
        sx={{ display: { xs: 'block', sm: 'none' }, '& .MuiDrawer-paper': { boxSizing: 'border-box', width: DRAWER_WIDTH } }}>
        {sidebarContent}
      </Drawer>

      {/* Desktop drawer */}
      <Drawer variant="permanent" sx={{ display: { xs: 'none', sm: 'block' }, '& .MuiDrawer-paper': { boxSizing: 'border-box', width: DRAWER_WIDTH } }} open>
        {sidebarContent}
      </Drawer>

      <Box component="main" sx={{ flexGrow: 1, p: 3, width: { sm: `calc(100% - ${DRAWER_WIDTH}px)` } }}>
        <Toolbar />
        {mainContent}
      </Box>
    </Box>
  );
}
```

### Dashboard Shell with Mini Variant Drawer

```tsx
import { styled, useTheme, Theme, CSSObject } from '@mui/material/styles';
import MuiDrawer from '@mui/material/Drawer';

const DRAWER_WIDTH = 240;
const DRAWER_WIDTH_COLLAPSED = 64;

const openedMixin = (theme: Theme): CSSObject => ({
  width: DRAWER_WIDTH,
  transition: theme.transitions.create('width', { easing: theme.transitions.easing.sharp, duration: theme.transitions.duration.enteringScreen }),
  overflowX: 'hidden',
});

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create('width', { easing: theme.transitions.easing.sharp, duration: theme.transitions.duration.leavingScreen }),
  overflowX: 'hidden',
  width: DRAWER_WIDTH_COLLAPSED,
  [theme.breakpoints.up('sm')]: { width: DRAWER_WIDTH_COLLAPSED },
});

const MiniDrawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({ width: DRAWER_WIDTH, flexShrink: 0, whiteSpace: 'nowrap', boxSizing: 'border-box', ...(open && openedMixin(theme)), ...(!open && closedMixin(theme)) }),
);
```

---

## Best Practices

### Performance

1. **Avoid inline sx objects in render** — extract to constants:
   ```tsx
   // Bad — new object every render
   <Box sx={{ p: 2, bgcolor: 'grey.100' }} />

   // Good — stable reference
   const boxSx = { p: 2, bgcolor: 'grey.100' } as const;
   <Box sx={boxSx} />
   ```

2. **Use `styled()` for frequently re-rendered components** — styled generates a class name once, sx generates it per render.

3. **Use CSS variables mode** for dark mode — avoids full theme re-creation:
   ```tsx
   const theme = createTheme({ cssVariables: true });
   ```

4. **Lazy-load MUI X components**:
   ```tsx
   const DataGrid = React.lazy(() => import('@mui/x-data-grid').then(m => ({ default: m.DataGrid })));
   ```

### Accessibility

MUI components include ARIA attributes by default. Maintain this by:
- Always providing `label` or `aria-label` for icon-only buttons
- Using `TextField` with `label` prop (not placeholder alone)
- Providing `alt` text for images in `CardMedia`
- Using semantic HTML via `component` prop: `<Box component="nav">`, `<Box component="main">`

### TypeScript

```tsx
import type { Theme } from '@mui/material/styles';

// Typed styled component
const StyledCard = styled(Card)(({ theme }: { theme: Theme }) => ({
  borderRadius: theme.shape.borderRadius * 2,
}));

// Typed sx callback
<Box sx={(theme: Theme) => ({ bgcolor: theme.palette.background.paper })} />

// Module augmentation for custom variants
declare module '@mui/material/Button' {
  interface ButtonPropsVariantOverrides { gradient: true }
  interface ButtonPropsColorOverrides { brand: true }
}
```

---

## Reference Files

For detailed information beyond this overview, consult these reference files:

- **`references/components.md`** — Complete component catalog with full Props API, slot names, CSS class keys, and code examples for all 50+ MUI components
- **`references/theming.md`** — Full theming API reference: palette, typography, spacing, breakpoints, shadows, zIndex, component overrides, CSS variables
- **`references/styling.md`** — Deep dive into sx prop syntax, styled API patterns, CSS layers, Pigment CSS migration guide
- **`references/mui-x.md`** — MUI X advanced components: DataGrid configuration, Date Pickers, Charts API
- **`references/css-classes.md`** — Complete CSS class keys for every MUI component (extracted from `*Classes.ts` source files), with usage examples for styled/sx/theme overrides

Read the relevant reference file when you need specific prop details, advanced configuration, or migration guidance.
