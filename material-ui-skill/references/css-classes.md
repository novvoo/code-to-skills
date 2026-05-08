# MUI Component CSS Class Keys Reference (Source-Derived from v9)

Complete list of all CSS class keys for every MUI component, extracted from the `*Classes.ts` source files. Use these with `styled()`, `sx` prop, or `theme.components` overrides.

---

## How to Use CSS Classes

### In styled()

```tsx
const StyledButton = styled(Button)(({ theme }) => ({
  [`&.${buttonClasses.root}`]: { borderRadius: 20 },
  [`&.${buttonClasses.disabled}`]: { opacity: 0.5 },
}));
```

### In sx prop

```tsx
<Button sx={{
  [`&.${buttonClasses.disabled}`]: { bgcolor: 'grey.200' },
}} />
```

### In theme overrides

```tsx
const theme = createTheme({
  components: {
    MuiButton: {
      styleOverrides: {
        root: { borderRadius: 20 },
        disabled: { opacity: 0.5 },
      },
    },
  },
});
```

### Import class keys utility

```tsx
import { buttonClasses } from '@mui/material/Button';
import { dialogClasses } from '@mui/material/Dialog';
// Each component exports its own *Classes object
```

---

## Complete Class Keys by Component

### Accordion
`root`, `heading`, `rounded`, `expanded`, `disabled`, `gutters`, `region`

### Alert
`root`, `action`, `icon`, `message`, `filled`, `colorSuccess`, `colorInfo`, `colorWarning`, `colorError`, `outlined`, `standard`

### AppBar
`root`, `positionFixed`, `positionAbsolute`, `positionSticky`, `positionStatic`, `positionRelative`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorInherit`, `colorTransparent`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`

### Autocomplete
`root`, `expanded`, `fullWidth`, `focused`, `focusVisible`, `tag`, `tagSizeSmall`, `tagSizeMedium`, `hasPopupIcon`, `hasClearIcon`, `inputRoot`, `input`, `inputFocused`, `endAdornment`, `clearIndicator`, `popupIndicator`, `popupIndicatorOpen`, `popper`, `popperDisablePortal`, `paper`, `listbox`, `loading`, `noOptions`, `option`, `groupLabel`, `groupUl`

### Avatar
`root`, `colorDefault`, `circular`, `rounded`, `square`, `img`, `fallback`

### AvatarGroup
`root`, `avatar`

### Backdrop
`root`, `invisible`

### Badge
`root`, `badge`, `dot`, `standard`, `anchorOriginTopRight`, `anchorOriginBottomRight`, `anchorOriginTopLeft`, `anchorOriginBottomLeft`, `invisible`, `colorError`, `colorInfo`, `colorPrimary`, `colorSecondary`, `colorSuccess`, `colorWarning`, `overlapRectangular`, `overlapCircular`, `anchorOriginTopLeftCircular`, `anchorOriginTopLeftRectangular`, `anchorOriginTopRightCircular`, `anchorOriginTopRightRectangular`, `anchorOriginBottomLeftCircular`, `anchorOriginBottomLeftRectangular`, `anchorOriginBottomRightCircular`, `anchorOriginBottomRightRectangular`

### Breadcrumbs
`root`, `ol`, `li`, `separator`

### Button
`root`, `text`, `outlined`, `contained`, `disableElevation`, `focusVisible`, `disabled`, `colorInherit`, `colorPrimary`, `colorSecondary`, `colorSuccess`, `colorError`, `colorInfo`, `colorWarning`, `sizeMedium`, `sizeSmall`, `sizeLarge`, `fullWidth`, `startIcon`, `endIcon`, `icon`, `loading`, `loadingWrapper`, `loadingIconPlaceholder`, `loadingIndicator`, `loadingPositionCenter`, `loadingPositionStart`, `loadingPositionEnd`

### ButtonBase
`root`, `disabled`, `focusVisible`

### ButtonGroup
`root`, `contained`, `outlined`, `text`, `disableElevation`, `disabled`, `firstButton`, `fullWidth`, `horizontal`, `vertical`, `colorPrimary`, `colorSecondary`, `grouped`, `lastButton`, `middleButton`

### CardActionArea
`root`, `focusVisible`, `focusHighlight`

### CardActions
`root`, `spacing`

### CardHeader
`root`, `avatar`, `action`, `content`, `title`, `subheader`

### CardMedia
`root`, `media`, `img`

### Checkbox
`root`, `checked`, `disabled`, `indeterminate`, `colorPrimary`, `colorSecondary`, `sizeSmall`, `sizeMedium`

### Chip
`root`, `sizeSmall`, `sizeMedium`, `colorDefault`, `colorError`, `colorInfo`, `colorPrimary`, `colorSecondary`, `colorSuccess`, `colorWarning`, `disabled`, `clickable`, `deletable`, `outlined`, `filled`, `avatar`, `icon`, `label`, `deleteIcon`, `focusVisible`

### CircularProgress
`root`, `determinate`, `indeterminate`, `colorPrimary`, `colorSecondary`, `svg`, `track`, `circle`, `circleDisableShrink`

### Collapse
`root`, `horizontal`, `vertical`, `entered`, `hidden`, `wrapper`, `wrapperInner`

### Container
`root`, `disableGutters`, `fixed`, `maxWidthXs`, `maxWidthSm`, `maxWidthMd`, `maxWidthLg`, `maxWidthXl`

### Dialog
`root`, `backdrop`, `scrollPaper`, `scrollBody`, `container`, `paper`, `paperWidthFalse`, `paperWidthXs`, `paperWidthSm`, `paperWidthMd`, `paperWidthLg`, `paperWidthXl`, `paperFullWidth`, `paperFullScreen`

### DialogActions
`root`, `spacing`

### DialogContent
`root`, `dividers`

### Divider
`root`, `absolute`, `fullWidth`, `inset`, `middle`, `flexItem`, `vertical`, `withChildren`, `textAlignRight`, `textAlignLeft`, `wrapper`, `wrapperVertical`

### Drawer
`root`, `docked`, `paper`, `anchorLeft`, `anchorRight`, `anchorTop`, `anchorBottom`, `modal`

### Fab
`root`, `primary`, `secondary`, `extended`, `circular`, `focusVisible`, `disabled`, `colorInherit`, `sizeSmall`, `sizeMedium`, `sizeLarge`, `info`, `error`, `warning`, `success`

### FilledInput
`root`, `underline`, `input`, `adornedStart`, `adornedEnd`, `sizeSmall`, `multiline`, `hiddenLabel`

### FormControl
`root`, `marginNone`, `marginNormal`, `marginDense`, `fullWidth`, `disabled`

### FormControlLabel
`root`, `labelPlacementStart`, `labelPlacementTop`, `labelPlacementBottom`, `disabled`, `label`, `error`, `required`, `asterisk`

### FormGroup
`root`, `row`, `error`

### FormHelperText
`root`, `error`, `disabled`, `sizeSmall`, `sizeMedium`, `contained`, `focused`, `filled`, `required`

### FormLabel
`root`, `colorSecondary`, `focused`, `disabled`, `error`, `filled`, `required`, `asterisk`

### Grid
`root`, `container`

### Icon
`root`, `colorPrimary`, `colorSecondary`, `colorAction`, `colorError`, `colorDisabled`, `fontSizeInherit`, `fontSizeSmall`, `fontSizeMedium`, `fontSizeLarge`

### IconButton
`root`, `disabled`, `colorInherit`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `edgeStart`, `edgeEnd`, `sizeSmall`, `sizeMedium`, `sizeLarge`, `loading`, `loadingIndicator`, `loadingWrapper`

### ImageList
`root`, `masonry`, `quilted`, `standard`, `woven`

### ImageListItem
`root`, `img`, `standard`, `woven`, `masonry`, `quilted`

### ImageListItemBar
`root`, `positionBottom`, `positionTop`, `positionBelow`, `actionPositionLeft`, `actionPositionRight`, `titleWrap`, `title`, `subtitle`, `actionIcon`

### InputAdornment
`root`, `filled`, `standard`, `outlined`, `positionStart`, `positionEnd`, `disablePointerEvents`, `hiddenLabel`, `sizeSmall`

### InputBase
`root`, `formControl`, `focused`, `disabled`, `adornedStart`, `adornedEnd`, `error`, `sizeSmall`, `multiline`, `colorSecondary`, `fullWidth`, `hiddenLabel`, `readOnly`, `input`, `inputTypeSearch`

### InputLabel
`root`, `focused`, `disabled`, `error`, `required`, `asterisk`, `formControl`, `sizeSmall`, `shrink`, `animated`, `standard`, `filled`, `outlined`

### LinearProgress
`root`, `colorPrimary`, `colorSecondary`, `determinate`, `indeterminate`, `buffer`, `query`, `dashed`, `bar`, `bar1`, `bar2`

### Link
`root`, `underlineNone`, `underlineHover`, `underlineAlways`, `button`, `focusVisible`

### List
`root`, `padding`, `dense`, `subheader`

### ListItem
`root`, `dense`, `alignItemsFlexStart`, `divider`, `gutters`, `padding`, `secondaryAction`

### ListItemButton
`root`, `focusVisible`, `dense`, `alignItemsFlexStart`, `disabled`, `divider`, `gutters`, `selected`

### ListItemIcon
`root`, `alignItemsFlexStart`

### ListItemText
`root`, `multiline`, `dense`, `inset`, `primary`, `secondary`

### ListSubheader
`root`, `colorPrimary`, `colorInherit`, `gutters`, `inset`, `sticky`

### MenuItem
`root`, `focusVisible`, `dense`, `disabled`, `divider`, `gutters`, `selected`

### MobileStepper
`root`, `positionBottom`, `positionTop`, `positionStatic`, `dots`, `dot`, `dotActive`, `progress`

### Modal
`root`, `hidden`, `backdrop`

### NativeSelect
`root`, `select`, `multiple`, `filled`, `outlined`, `standard`, `disabled`, `icon`, `iconOpen`, `iconFilled`, `iconOutlined`, `iconStandard`, `nativeInput`, `error`

### Pagination
`root`, `ul`, `outlined`, `text`

### PaginationItem
`root`, `page`, `sizeSmall`, `sizeLarge`, `text`, `outlined`, `rounded`, `ellipsis`, `firstLast`, `previousNext`, `focusVisible`, `disabled`, `selected`, `icon`, `colorPrimary`, `colorSecondary`

### Paper
`root`, `rounded`, `outlined`, `elevation`, `elevation0`–`elevation24`

### Radio
`root`, `checked`, `disabled`, `colorPrimary`, `colorSecondary`, `sizeSmall`

### RadioGroup
`root`, `row`, `error`

### Rating
`root`, `sizeSmall`, `sizeMedium`, `sizeLarge`, `readOnly`, `disabled`, `focusVisible`, `visuallyHidden`, `pristine`, `label`, `labelEmptyValueActive`, `icon`, `iconEmpty`, `iconFilled`, `iconHover`, `iconFocus`, `iconActive`, `decimal`

### Select
`root`, `select`, `multiple`, `filled`, `outlined`, `standard`, `disabled`, `focused`, `icon`, `iconOpen`, `nativeInput`, `error`

### Skeleton
`root`, `text`, `rectangular`, `rounded`, `circular`, `pulse`, `wave`, `withChildren`, `fitContent`, `heightAuto`

### Slider
`root`, `active`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `dragging`, `focusVisible`, `mark`, `markActive`, `marked`, `markLabel`, `markLabelActive`, `rail`, `sizeSmall`, `thumb`, `track`, `trackInverted`, `trackFalse`, `valueLabel`, `valueLabelOpen`, `valueLabelCircle`, `valueLabelLabel`, `vertical`

### Snackbar
`root`, `anchorOriginTopCenter`, `anchorOriginBottomCenter`, `anchorOriginTopRight`, `anchorOriginBottomRight`, `anchorOriginTopLeft`, `anchorOriginBottomLeft`

### SpeedDial
`root`, `fab`, `directionUp`, `directionDown`, `directionLeft`, `directionRight`, `actions`, `actionsClosed`

### SpeedDialAction
`fab`, `fabClosed`, `staticTooltip`, `staticTooltipClosed`, `staticTooltipLabel`, `tooltipPlacementLeft`, `tooltipPlacementRight`

### SpeedDialIcon
`root`, `icon`, `iconOpen`, `iconWithOpenIconOpen`, `openIcon`, `openIconOpen`

### Step
`root`, `horizontal`, `vertical`, `alternativeLabel`, `completed`

### StepButton
`root`, `horizontal`, `vertical`, `touchRipple`

### StepConnector
`root`, `horizontal`, `vertical`, `alternativeLabel`, `active`, `completed`, `disabled`, `line`

### StepContent
`root`, `last`, `transition`

### StepIcon
`root`, `active`, `completed`, `error`, `text`

### StepLabel
`root`, `horizontal`, `vertical`, `label`, `active`, `completed`, `error`, `disabled`, `iconContainer`, `alternativeLabel`, `labelContainer`

### Stepper
`root`, `horizontal`, `vertical`, `nonLinear`, `alternativeLabel`

### SvgIcon
`root`, `colorPrimary`, `colorSecondary`, `colorAction`, `colorError`, `colorDisabled`, `fontSizeInherit`, `fontSizeSmall`, `fontSizeMedium`, `fontSizeLarge`

### Switch
`root`, `edgeStart`, `edgeEnd`, `switchBase`, `colorPrimary`, `colorSecondary`, `sizeSmall`, `sizeMedium`, `checked`, `disabled`, `input`, `thumb`, `track`

### Tab
`root`, `labelIcon`, `textColorInherit`, `textColorPrimary`, `textColorSecondary`, `selected`, `disabled`, `fullWidth`, `wrapped`, `icon`

### TableCell
`root`, `head`, `body`, `footer`, `sizeSmall`, `sizeMedium`, `paddingCheckbox`, `paddingNone`, `alignLeft`, `alignCenter`, `alignRight`, `alignJustify`, `stickyHeader`

### TablePagination
`root`, `toolbar`, `spacer`, `selectLabel`, `selectRoot`, `select`, `selectIcon`, `input`, `menuItem`, `displayedRows`, `actions`

### TableRow
`root`, `selected`, `hover`, `head`, `footer`

### TableSortLabel
`root`, `active`, `icon`, `directionDesc`, `directionAsc`

### Tabs
`root`, `vertical`, `list`, `centered`, `scroller`, `fixed`, `scrollableX`, `scrollableY`, `hideScrollbar`, `scrollButtons`, `scrollButtonsHideMobile`, `indicator`

### ToggleButton
`root`, `disabled`, `selected`, `standard`, `primary`, `secondary`, `sizeSmall`, `sizeMedium`, `sizeLarge`, `fullWidth`

### ToggleButtonGroup
`root`, `selected`, `horizontal`, `vertical`, `disabled`, `grouped`, `fullWidth`, `firstButton`, `lastButton`, `middleButton`

### Toolbar
`root`, `gutters`, `regular`, `dense`

### Tooltip
`popper`, `popperInteractive`, `popperArrow`, `popperClose`, `tooltip`, `tooltipArrow`, `touch`, `tooltipPlacementLeft`, `tooltipPlacementRight`, `tooltipPlacementTop`, `tooltipPlacementBottom`, `arrow`

### Typography
`root`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `subtitle1`, `subtitle2`, `body1`, `body2`, `inherit`, `button`, `caption`, `overline`, `alignLeft`, `alignRight`, `alignCenter`, `alignJustify`, `noWrap`, `gutterBottom`
