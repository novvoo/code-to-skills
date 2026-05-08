# MUI Component Catalog (Source-Derived from v9)

Complete reference for all Material UI components with **exact Props APIs, default values, slot names, CSS class keys, and code examples** — derived from the actual MUI v9 source code type definitions.

---

## Table of Contents

1. [Layout](#layout)
2. [Inputs](#inputs)
3. [Navigation](#navigation)
4. [Feedback](#feedback)
5. [Data Display](#data-display)
6. [Surfaces](#surfaces)
7. [Utils](#utils)
8. [Lab Components](#lab-components)

---

## Layout

### Box

The universal container — renders as `<div>` by default, accepts all `sx` prop values.

**Slots:** `root`

**CSS Classes:** `root`

```tsx
import Box from '@mui/material/Box';

<Box sx={{ p: 2, bgcolor: 'grey.100', borderRadius: 1 }}>
  Content
</Box>

// Change rendered element
<Box component="section" sx={{ mb: 4 }}>
  Semantic HTML section
</Box>
```

### Stack

One-dimensional layout — vertical by default.

**Slots:** `root`

**CSS Classes:** `root`, `directionRow`, `directionRowReverse`, `directionColumn`, `directionColumnReverse`, `spacing1`–`spacing10`, `alignItemsFlexStart`, `alignItemsCenter`, `alignItemsFlexEnd`, `alignItemsStretch`, `alignItemsBaseline`, `justifyContentCenter`, `justifyContentFlexStart`, `justifyContentFlexEnd`, `justifyContentSpaceBetween`, `justifyContentSpaceAround`, `flexWrapWrap`, `flexWrapWrapReverse`, `flexWrapNoWrap`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `'row'` \| `'row-reverse'` \| `'column'` \| `'column-reverse'` \| responsive object | `'column'` | Layout direction |
| `spacing` | `number` \| `string` \| responsive object | `0` | Space between items (uses theme.spacing) |
| `divider` | `ReactElement` | — | Element inserted between children |
| `useFlexGap` | `boolean` | `false` | Use CSS flexbox gap instead of margin |
| `justifyContent` | CSS flexbox justify | — | Horizontal alignment |
| `alignItems` | CSS flexbox align | — | Vertical alignment |

```tsx
import Stack from '@mui/material/Stack';

<Stack direction="column" spacing={2}>
  <Item />
  <Item />
</Stack>

// Responsive direction
<Stack direction={{ xs: 'column', md: 'row' }} spacing={2}>
  <Item />
</Stack>

// With divider
<Stack direction="row" spacing={1} divider={<Divider orientation="vertical" flexItem />}>
  <Item />
  <Item />
</Stack>
```

### Grid (v2)

Two-dimensional layout using CSS Grid. MUI v9 uses Grid v2 with `size` prop.

**Slots:** `root`

**CSS Classes:** `root`, `container`, `item`, `directionRow`, `directionRowReverse`, `directionColumn`, `directionColumnReverse`, `wrapWrap`, `wrapNowrap`, `wrapReverse`, `gridSizeXs`–`gridSizeMd`, `gridOffsetXs`–`gridOffsetMd`, `gridItem`, `zeroColumns`

**Key Props (Grid container):**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `container` | `boolean` | `false` | If true, the component is a grid container |
| `spacing` | `number` \| `string` \| responsive object | `0` | Space between items |
| `direction` | `'row'` \| `'row-reverse'` \| `'column'` \| `'column-reverse'` | `'row'` | Grid direction |
| `wrap` | `'wrap'` \| `'nowrap'` \| `'wrap-reverse'` | `'wrap'` | Grid wrapping |
| `columns` | `number` \| responsive object | `12` | Number of columns |

**Key Props (Grid item):**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `size` | `'auto'` \| `'grow'` \| `number` \| responsive object | — | Column span. `{ xs: 12, md: 8 }` |
| `offset` | `'auto'` \| `number` \| responsive object | — | Column offset |

```tsx
import Grid from '@mui/material/Grid';

<Grid container spacing={2}>
  <Grid size={{ xs: 12, md: 8 }}>
    Main content
  </Grid>
  <Grid size={{ xs: 12, md: 4 }}>
    Sidebar
  </Grid>
</Grid>

// Auto-sizing
<Grid container spacing={2}>
  <Grid size="grow">Fills remaining space</Grid>
  <Grid size="auto">Auto-sized</Grid>
  <Grid size={4}>Fixed 4 columns</Grid>
</Grid>
```

### Container

Centers content horizontally with max-width breakpoints.

**Slots:** `root`

**CSS Classes:** `root`, `maxWidthXs`, `maxWidthSm`, `maxWidthMd`, `maxWidthLg`, `maxWidthXl`, `maxWidthFalse`, `disableGutters`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `maxWidth` | `'xs'` \| `'sm'` \| `'md'` \| `'lg'` \| `'xl'` \| `false` | `'lg'` | Max width |
| `disableGutters` | `boolean` | `false` | Remove horizontal padding |
| `fixed` | `boolean` | `false` | Set max-width to breakpoint min-width |

```tsx
import Container from '@mui/material/Container';

<Container maxWidth="md">
  <Typography>Centered content</Typography>
</Container>
```

---

## Inputs

### Button

**Slots:** `root`, `startIcon`, `endIcon`, `loadingIndicator`

**CSS Classes:** `root`, `text`, `textPrimary`, `textSecondary`, `textSuccess`, `textError`, `textInfo`, `textWarning`, `outlined`, `outlinedPrimary`, `outlinedSecondary`, `outlinedSuccess`, `outlinedError`, `outlinedInfo`, `outlinedWarning`, `contained`, `containedPrimary`, `containedSecondary`, `containedSuccess`, `containedError`, `containedInfo`, `containedWarning`, `disableElevation`, `focusVisible`, `disabled`, `colorInherit`, `textSizeSmall`, `textSizeMedium`, `textSizeLarge`, `outlinedSizeSmall`, `outlinedSizeMedium`, `outlinedSizeLarge`, `containedSizeSmall`, `containedSizeMedium`, `containedSizeLarge`, `sizeMedium`, `sizeSmall`, `sizeLarge`, `fullWidth`, `startIcon`, `endIcon`, `iconSizeSmall`, `iconSizeMedium`, `iconSizeLarge`, `loading`, `loadingIndicator`, `loadingPositionStart`, `loadingPositionEnd`, `loadingPositionCenter`

**Complete Props (from ButtonOwnProps):**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | — | Button content |
| `classes` | `Partial<ButtonClasses>` | — | Override styles |
| `color` | `'inherit'` \| `'primary'` \| `'secondary'` \| `'success'` \| `'error'` \| `'info'` \| `'warning'` + custom | `'primary'` | Color |
| `disabled` | `boolean` | `false` | Disabled state |
| `disableElevation` | `boolean` | `false` | Remove shadow |
| `disableFocusRipple` | `boolean` | `false` | Disable keyboard focus ripple |
| `endIcon` | `ReactNode` | — | Icon after children |
| `fullWidth` | `boolean` | `false` | Full container width |
| `href` | `string` | — | URL (renders `<a>`) |
| `loading` | `boolean` \| `null` | `null` | Show loading indicator |
| `loadingIndicator` | `ReactNode` | `<CircularProgress color="inherit" size={16} />` | Custom loading indicator |
| `loadingPosition` | `'start'` \| `'end'` \| `'center'` | `'center'` | Loading indicator position |
| `size` | `'small'` \| `'medium'` \| `'large'` + custom | `'medium'` | Size |
| `startIcon` | `ReactNode` | — | Icon before children |
| `variant` | `'text'` \| `'outlined'` \| `'contained'` + custom | `'text'` | Variant |

```tsx
import Button from '@mui/material/Button';
import SaveIcon from '@mui/icons-material/Save';

// Basic variants
<Button variant="contained">Contained</Button>
<Button variant="outlined">Outlined</Button>
<Button variant="text">Text</Button>

// With icons
<Button variant="contained" startIcon={<SaveIcon />}>Save</Button>
<Button variant="contained" endIcon={<ArrowForward />}>Next</Button>

// Loading state
<Button variant="contained" loading={isSubmitting}>Submit</Button>
<Button variant="contained" loading loadingPosition="start" startIcon={<SaveIcon />}>Save</Button>

// Link button
<Button variant="text" href="/about">About</Button>

// Custom color via module augmentation
declare module '@mui/material/Button' {
  interface ButtonPropsColorOverrides { brand: true }
}
```

### IconButton

**Slots:** `root`, `loadingIndicator`

**CSS Classes:** `root`, `edgeStart`, `edgeEnd`, `colorInherit`, `colorPrimary`, `colorSecondary`, `colorDefault`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `sizeSmall`, `sizeMedium`, `sizeLarge`, `loading`, `loadingIndicator`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `'inherit'` \| `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` + custom | `'default'` | Color |
| `size` | `'small'` \| `'medium'` \| `'large'` + custom | `'medium'` | Size |
| `edge` | `'start'` \| `'end'` \| `false` | `false` | Edge alignment |
| `loading` | `boolean` \| `null` | `null` | Loading state |
| `loadingIndicator` | `ReactNode` | `<CircularProgress color="inherit" size={16} />` | Custom loading indicator |
| `disableRipple` | `boolean` | `false` | Disable ripple effect |
| `disableFocusRipple` | `boolean` | `false` | Disable focus ripple |

```tsx
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

<IconButton aria-label="delete" onClick={handleDelete}>
  <DeleteIcon />
</IconButton>

<IconButton color="primary" size="small">
  <SettingsIcon fontSize="small" />
</IconButton>

<IconButton loading={isSaving}>
  <SaveIcon />
</IconButton>
```

### TextField

**Slots:** `root`, `input`, `inputLabel`, `htmlInput`, `helperText`, `formControl`

**CSS Classes:** `root`, `error`, `marginDense`, `marginNormal`, `fullWidth`, `multiline`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `autoComplete` | `string` | — | HTML autocomplete attribute |
| `autoFocus` | `boolean` | `false` | Auto focus on mount |
| `color` | `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` + custom | `'primary'` | Color |
| `defaultValue` | `unknown` | — | Default value (uncontrolled) |
| `disabled` | `boolean` | `false` | Disabled state |
| `error` | `boolean` | `false` | Error state |
| `fullWidth` | `boolean` | `false` | Full container width |
| `helperText` | `ReactNode` | — | Helper text below input |
| `id` | `string` | — | HTML id |
| `InputLabelProps` | `object` | — | Props for InputLabel |
| `inputProps` | `object` | — | Props for native input element |
| `InputProps` | `object` | — | Props for Input component |
| `label` | `ReactNode` | — | Label text |
| `margin` | `'none'` \| `'dense'` \| `'normal'` | `'none'` | Margin |
| `maxRows` | `number` \| `string` | — | Max rows (multiline) |
| `minRows` | `number` \| `string` | — | Min rows (multiline) |
| `multiline` | `boolean` | `false` | Multiline input |
| `name` | `string` | — | Input name |
| `onChange` | `(event) => void` | — | Change handler |
| `placeholder` | `string` | — | Placeholder text |
| `required` | `boolean` | `false` | Required field |
| `rows` | `number` \| `string` | — | Fixed rows (multiline) |
| `select` | `boolean` | `false` | Render as Select |
| `SelectProps` | `object` | — | Props for Select |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `type` | `string` | — | Input type |
| `value` | `unknown` | — | Input value (controlled) |
| `variant` | `'outlined'` \| `'filled'` \| `'standard'` | `'outlined'` | Variant |

```tsx
import TextField from '@mui/material/TextField';

// Basic
<TextField label="Name" variant="outlined" />

// With validation
<TextField label="Email" type="email" error={!isValid} helperText={error} required />

// Multiline
<TextField label="Description" multiline rows={4} />

// Select
<TextField select label="Role" value={role} onChange={handleChange}>
  <MenuItem value="admin">Admin</MenuItem>
  <MenuItem value="user">User</MenuItem>
</TextField>

// Small dense field
<TextField label="Search" size="small" fullWidth />
```

### Select

**Slots:** inherits from `OutlinedInput` / `FilledInput` / `Input`

**CSS Classes:** `root`, `select`, `filled`, `outlined`, `standard`, `disabled`, `focused`, `icon`, `iconOpen`, `iconFilled`, `iconOutlined`, `iconStandard`, `nativeInput`, `error`, `multiple`, `sizeSmall`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `autoWidth` | `boolean` | `false` | Width adjusts to content |
| `children` | `ReactNode` | — | MenuItems |
| `defaultValue` | `unknown` | — | Default value |
| `displayEmpty` | `boolean` | `false` | Display when value is empty |
| `IconComponent` | `ComponentType` | `ArrowDropDownIcon` | Dropdown icon |
| `input` | `Element` | — | Custom input element |
| `inputProps` | `object` | — | Props for input |
| `label` | `ReactNode` | — | Label |
| `labelId` | `string` | — | ID of label element |
| `MenuProps` | `Partial<MenuProps>` | — | Props for Menu |
| `multiple` | `boolean` | `false` | Multiple selection |
| `native` | `boolean` | `false` | Use native select |
| `onChange` | `(event) => void` | — | Change handler |
| `onClose` | `(event) => void` | — | Close handler |
| `onOpen` | `(event) => void` | — | Open handler |
| `open` | `boolean` | — | Controlled open state |
| `renderValue` | `(value) => ReactNode` | — | Custom render for selected value |
| `SelectDisplayProps` | `object` | — | Props for display div |
| `value` | `unknown` | — | Selected value |
| `variant` | `'outlined'` \| `'filled'` \| `'standard'` | `'outlined'` | Variant |

```tsx
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';

<FormControl fullWidth>
  <InputLabel>Age</InputLabel>
  <Select value={age} label="Age" onChange={handleChange}>
    <MenuItem value={10}>Ten</MenuItem>
    <MenuItem value={20}>Twenty</MenuItem>
    <MenuItem value={30}>Thirty</MenuItem>
  </Select>
</FormControl>

// Multiple select
<Select multiple value={names} onChange={handleChange} renderValue={(selected) => selected.join(', ')}>
  {names.map(name => <MenuItem key={name} value={name}><Checkbox checked={names.includes(name)} /> <ListItemText primary={name} /></MenuItem>)}
</Select>
```

### Checkbox

**CSS Classes:** `root`, `checked`, `disabled`, `indeterminate`, `colorPrimary`, `colorSecondary`, `sizeSmall`, `sizeMedium`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `checked` | `boolean` | — | Checked state |
| `checkedIcon` | `ReactNode` | — | Custom checked icon |
| `color` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'primary'` | Color |
| `disabled` | `boolean` | `false` | Disabled |
| `disableRipple` | `boolean` | `false` | Disable ripple |
| `icon` | `ReactNode` | — | Custom unchecked icon |
| `indeterminate` | `boolean` | `false` | Indeterminate state |
| `indeterminateIcon` | `ReactNode` | — | Custom indeterminate icon |
| `onChange` | `(event, checked) => void` | — | Change handler |
| `required` | `boolean` | `false` | Required |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `sx` | `SxProps<Theme>` | — | System props |

```tsx
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';

<FormControlLabel control={<Checkbox defaultChecked />} label="Accept terms" />
<Checkbox icon={<BookmarkBorder />} checkedIcon={<Bookmark />} checked={checked} />
```

### Switch

**Slots:** `root`, `switchBase`, `thumb`, `track`, `input`

**CSS Classes:** `root`, `edgeStart`, `edgeEnd`, `switchBase`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `sizeSmall`, `sizeMedium`, `checked`, `disabled`, `input`, `thumb`, `track`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `checked` | `boolean` | — | Checked state |
| `checkedIcon` | `ReactNode` | — | Custom checked icon |
| `color` | `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` \| `'default'` | `'primary'` | Color |
| `disabled` | `boolean` | `false` | Disabled |
| `edge` | `'start'` \| `'end'` \| `false` | `false` | Edge alignment |
| `icon` | `ReactNode` | — | Custom unchecked icon |
| `onChange` | `(event, checked) => void` | — | Change handler |
| `required` | `boolean` | `false` | Required |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |

### Radio

**CSS Classes:** `root`, `checked`, `disabled`, `colorPrimary`, `colorSecondary`, `sizeSmall`, `sizeMedium`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `checked` | `boolean` | — | Selected state |
| `checkedIcon` | `ReactNode` | — | Custom checked icon |
| `color` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'primary'` | Color |
| `disabled` | `boolean` | `false` | Disabled |
| `icon` | `ReactNode` | — | Custom unchecked icon |
| `onChange` | `(event) => void` | — | Change handler |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `value` | `unknown` | — | Radio value |

### Slider

**Slots:** `root`, `track`, `thumb`, `valueLabel`, `mark`, `markLabel`, `input`

**CSS Classes:** `root`, `active`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `dragging`, `focusVisible`, `mark`, `markActive`, `marked`, `markLabel`, `markLabelActive`, `sizeSmall`, `sizeMedium`, `thumb`, `thumbSizeSmall`, `track`, `trackInverted`, `trackFalse`, `valueLabel`, `valueLabelOpen`, `valueLabelCircle`, `valueLabelLabel`, `vertical`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | `'primary'` | Color |
| `defaultValue` | `number` \| `number[]` | — | Default value |
| `disabled` | `boolean` | `false` | Disabled |
| `disableSwap` | `boolean` | `false` | Prevent thumb swap on range |
| `marks` | `boolean` \| `Mark[]` | `false` | Show marks |
| `max` | `number` | `100` | Maximum value |
| `min` | `number` | `0` | Minimum value |
| `onChange` | `(event, value) => void` | — | Change handler |
| `onChangeCommitted` | `(event, value) => void` | — | Change committed handler |
| `orientation` | `'horizontal'` \| `'vertical'` | `'horizontal'` | Orientation |
| `shiftStep` | `number` | `10` | Step when shift is held |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `step` | `number` | `1` | Step increment |
| `track` | `'normal'` \| `'inverted'` \| `false` | `'normal'` | Track display |
| `value` | `number` \| `number[]` | — | Controlled value |
| `valueLabelDisplay` | `'on'` \| `'auto'` \| `'off'` | `'off'` | Value label display |
| `valueLabelFormat` | `string` \| `(value, index) => string` | — | Value label format |

### Autocomplete

**Slots:** `root`, `paper`, `popper`, `clearIndicator`, `popupIndicator`, `listbox`, `loading`, `noOptions`, `tag`

**CSS Classes:** `root`, `expanded`, `fullWidth`, `focused`, `focusVisible`, `tag`, `tagSizeSmall`, `tagSizeMedium`, `hasPopupIcon`, `hasClearIcon`, `inputRoot`, `input`, `inputFocused`, `endAdornment`, `clearIndicator`, `popupIndicator`, `popupIndicatorOpen`, `popper`, `popperDisablePortal`, `paper`, `listbox`, `listboxDense`, `option`, `groupLabel`, `groupUl`, `loading`, `noOptions`, `error`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `autoComplete` | `boolean` | `false` | Auto complete |
| `autoHighlight` | `boolean` | `false` | Auto highlight first option |
| `autoSelect` | `boolean` | `false` | Auto select highlighted option on blur |
| `blurOnSelect` | `boolean` \| `'mouse'` \| `'touch'` | `false` | Blur on select |
| `clearOnBlur` | `boolean` | `false` | Clear input on blur |
| `clearOnEscape` | `boolean` | `false` | Clear on Escape |
| `clearIcon` | `ReactNode` | `<ClearIcon fontSize="small" />` | Clear icon |
| `closeText` | `string` | `'Close'` | ARIA close label |
| `disableCloseOnSelect` | `boolean` | `false` | Keep open on select |
| `disabled` | `boolean` | `false` | Disabled |
| `disableListWrap` | `boolean` | `false` | Disable list wrap |
| `filterOptions` | `(options, state) => Option[]` | — | Custom filter function |
| `filterSelectedOptions` | `boolean` | `false` | Filter selected options |
| `freeSolo` | `boolean` | `false` | Allow free text input |
| `getOptionDisabled` | `(option) => boolean` | — | Disable specific options |
| `getOptionKey` | `(option) => string \| number` | — | Unique key for options |
| `getOptionLabel` | `(option) => string` | — | Display label for option |
| `groupBy` | `(option) => string` | — | Group options |
| `includeInputInList` | `boolean` | `false` | Include input in list |
| `inputValue` | `string` | — | Controlled input value |
| `isOptionEqualToValue` | `(option, value) => boolean` | — | Equality check |
| `limitTags` | `number` | `-1` | Max visible tags (-1 = all) |
| `loading` | `boolean` | `false` | Loading state |
| `loadingText` | `ReactNode` | `'Loading…'` | Loading text |
| `multiple` | `boolean` | `false` | Multiple selection |
| `noOptionsText` | `ReactNode` | `'No options'` | No options text |
| `onChange` | `(event, value, reason) => void` | — | Change handler |
| `onInputChange` | `(event, value, reason) => void` | — | Input change handler |
| `onOpen` | `(event) => void` | — | Open handler |
| `onClose` | `(event, reason) => void` | — | Close handler |
| `open` | `boolean` | — | Controlled open state |
| `openOnFocus` | `boolean` | `false` | Open on focus |
| `openText` | `string` | `'Open'` | ARIA open label |
| `options` | `Option[]` | `[]` | Available options |
| `popupIcon` | `ReactNode` | `<ArrowDropDownIcon />` | Popup icon |
| `renderGroup` | `(params) => ReactNode` | — | Custom group render |
| `renderInput` | `(params) => ReactNode` | — | **Required** — Custom input render |
| `renderOption` | `(params, option, state) => ReactNode` | — | Custom option render |
| `renderTags` | `(value, getTagProps) => ReactNode` | — | Custom tags render |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `value` | `Option` \| `Option[]` | — | Controlled value |

```tsx
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';

// Basic
<Autocomplete
  options={top100Films}
  getOptionLabel={(option) => option.title}
  renderInput={(params) => <TextField {...params} label="Movie" />}
/>

// Multiple with custom render
<Autocomplete
  multiple
  options={skills}
  getOptionLabel={(option) => option.name}
  defaultValue={[skills[0]]}
  renderInput={(params) => <TextField {...params} label="Skills" placeholder="Add skill" />}
  renderTags={(value, getTagProps) => value.map((option, index) => <Chip label={option.name} {...getTagProps({ index })} />)}
/>

// Free solo
<Autocomplete freeSolo options={suggestions} renderInput={(params) => <TextField {...params} label="Search" />} />

// Async
<Autocomplete
  options={options}
  loading={isLoading}
  onInputChange={(e, value) => { if (value) fetchOptions(value); }}
  renderInput={(params) => (
    <TextField {...params} label="Search" InputProps={{ ...params.InputProps, endAdornment: (<>{isLoading ? <CircularProgress size={20} /> : null}{params.InputProps.endAdornment}</>) }} />
  )}
/>
```

### Rating

**Slots:** `root`, `item`, `label`, `icon`, `emptyIcon`, `decimal`, `visuallyHidden`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultValue` | `number` | `null` | Default value |
| `emptyIcon` | `ReactNode` | `<StarBorder fontSize="inherit" />` | Empty icon |
| `emptyLabelText` | `ReactNode` | `'Empty'` | Empty label text |
| `getLabelText` | `(value) => string` | — | ARIA label function |
| `highlightSelectedOnly` | `boolean` | `false` | Highlight only selected |
| `icon` | `ReactNode` | `<Star fontSize="inherit" />` | Filled icon |
| `max` | `number` | `5` | Maximum rating |
| `min` | `number` | `1` | Minimum rating |
| `onChange` | `(event, value) => void` | — | Change handler |
| `onChangeActive` | `(event, value) => void` | — | Hover change handler |
| `precision` | `number` | `1` | Minimum step |
| `readOnly` | `boolean` | `false` | Read only |
| `size` | `'small'` \| `'medium'` \| `'large'` + custom | `'medium'` | Size |
| `value` | `number` \| `null` | — | Controlled value |

---

## Navigation

### AppBar

**Slots:** `root`

**CSS Classes:** `root`, `positionFixed`, `positionAbsolute`, `positionSticky`, `positionStatic`, `positionRelative`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `colorTransparent`, `colorInherit`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `color` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` \| `'transparent'` \| `'inherit'` | `'primary'` | Color |
| `enableColorOnDark` | `boolean` | `false` | Allow color in dark mode |
| `elevation` | `number` | `4` | Shadow elevation (0-24) |
| `position` | `'fixed'` \| `'absolute'` \| `'sticky'` \| `'static'` \| `'relative'` | `'fixed'` | Position |

### Drawer

**Slots:** `root`, `docked`, `paper`, `backdrop`, `transition`

**CSS Classes:** `root`, `docked`, `paper`, `paperAnchorLeft`, `paperAnchorRight`, `paperAnchorTop`, `paperAnchorBottom`, `paperAnchorDockedLeft`, `paperAnchorDockedRight`, `paperAnchorDockedTop`, `paperAnchorDockedBottom`, `modal`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `anchor` | `'left'` \| `'top'` \| `'right'` \| `'bottom'` | `'left'` | Side |
| `children` | `ReactNode` | — | Drawer content |
| `elevation` | `number` | `16` | Shadow elevation |
| `ModalProps` | `object` | — | Props for Modal |
| `onClose` | `(event) => void` | — | Close handler |
| `open` | `boolean` | `false` | Open state |
| `PaperProps` | `object` | — | Props for Paper |
| `SlideProps` | `object` | — | Props for Slide |
| `variant` | `'permanent'` \| `'persistent'` \| `'temporary'` | `'temporary'` | Variant |

### Tabs

**Slots:** `root`, `scroller`, `scrollbarSize`, `tabScrollButton`, `flexContainer`, `indicator`

**CSS Classes:** `root`, `vertical`, `flexContainer`, `flexContainerVertical`, `centered`, `scroller`, `fixed`, `scrollableX`, `scrollableY`, `hideScrollbar`, `scrollButtons`, `scrollButtonsHideMobile`, `indicator`, `sizeSmall`, `sizeMedium`, `sizeLarge`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `Ref<TabsActions>` | — | Ref for imperative actions |
| `centered` | `boolean` | `false` | Center tabs |
| `children` | `ReactNode` | — | Tab elements |
| `indicatorColor` | `'primary'` \| `'secondary'` \| `string` | `'primary'` | Indicator color |
| `onChange` | `(event, value) => void` | — | Tab change handler |
| `orientation` | `'horizontal'` \| `'vertical'` | `'horizontal'` | Orientation |
| `scrollButtons` | `'auto'` \| `true` \| `false` | `'auto'` | Show scroll buttons |
| `selectionFollowsFocus` | `boolean` | `false` | Select on focus |
| `slotProps` | `object` | — | Props for slots |
| `slots` | `object` | — | Custom slot components |
| `TabIndicatorProps` | `object` | — | Props for indicator |
| `TabScrollButtonProps` | `object` | — | Props for scroll button |
| `textColor` | `'primary'` \| `'secondary'` \| `'inherit'` | `'primary'` | Text color |
| `value` | `number` \| `string` | — | Active tab |
| `variant` | `'standard'` \| `'scrollable'` \| `'fullWidth'` | `'standard'` | Variant |

### Stepper

**CSS Classes:** `root`, `horizontal`, `vertical`, `alternativeLabel`, `padding`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `activeStep` | `number` | `0` | Active step index |
| `alternativeLabel` | `boolean` | `false` | Labels below icons |
| `children` | `ReactNode` | — | Step elements |
| `connector` | `ReactElement` \| `null` | `<StepConnector />` | Step connector |
| `nonLinear` | `boolean` | `false` | Allow steps in any order |
| `orientation` | `'horizontal'` \| `'vertical'` | `'horizontal'` | Orientation |

### Pagination

**CSS Classes:** `root`, `ul`, `outlined`, `text`, `colorPrimary`, `colorSecondary`, `colorStandard`, `sizeSmall`, `sizeMedium`, `sizeLarge`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `boundaryCount` | `number` | `1` | Pages at start/end |
| `color` | `'standard'` \| `'primary'` \| `'secondary'` | `'standard'` | Color |
| `count` | `number` | `1` | Total pages |
| `defaultPage` | `number` | `1` | Default page |
| `disabled` | `boolean` | `false` | Disabled |
| `getItemAriaLabel` | `(type, page, selected) => string` | — | ARIA label |
| `hideNextButton` | `boolean` | `false` | Hide next button |
| `hidePrevButton` | `boolean` | `false` | Hide prev button |
| `onChange` | `(event, page) => void` | — | Page change handler |
| `page` | `number` | — | Current page (controlled) |
| `renderItem` | `(params) => ReactNode` | — | Custom item render |
| `shape` | `'circular'` \| `'rounded'` | `'circular'` | Shape |
| `showFirstButton` | `boolean` | `false` | Show first button |
| `showLastButton` | `boolean` | `false` | Show last button |
| `siblingCount` | `number` | `1` | Pages around current |
| `size` | `'small'` \| `'medium'` \| `'large'` | `'medium'` | Size |
| `variant` | `'text'` \| `'outlined'` | `'text'` | Variant |

---

## Feedback

### Dialog

**Slots:** `container`, `backdrop`, `paper`, `transition`, `root`

**CSS Classes:** `root`, `scrollPaper`, `scrollBody`, `container`, `paper`, `paperScrollPaper`, `paperScrollBody`, `paperWidthFalse`, `paperWidthXs`, `paperWidthSm`, `paperWidthMd`, `paperWidthLg`, `paperWidthXl`, `paperFullWidth`, `paperFullScreen`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `aria-describedby` | `string` | — | ID of descriptive element |
| `aria-labelledby` | `string` | — | ID of label element |
| `children` | `ReactNode` | — | Dialog content |
| `fullScreen` | `boolean` | `false` | Full screen |
| `fullWidth` | `boolean` | `false` | Full width |
| `keepMounted` | `boolean` | `false` | Keep in DOM when closed |
| `maxWidth` | `'xs'` \| `'sm'` \| `'md'` \| `'lg'` \| `'xl'` \| `false` | `'sm'` | Max width |
| `onClose` | `(event, reason) => void` | — | Close handler |
| `open` | `boolean` | — | Open state |
| `PaperProps` | `object` | — | Props for Paper |
| `scroll` | `'paper'` \| `'body'` | `'paper'` | Scroll target |
| `TransitionComponent` | `ComponentType` | `Fade` | Transition component |
| `transitionDuration` | `number` \| `{ appear, enter, exit }` | — | Transition duration |
| `TransitionProps` | `object` | — | Props for transition |

```tsx
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';

<Dialog open={open} onClose={handleClose} maxWidth="md" fullWidth>
  <DialogTitle>Confirm Action</DialogTitle>
  <DialogContent>
    <Typography>Are you sure?</Typography>
  </DialogContent>
  <DialogActions>
    <Button onClick={handleClose}>Cancel</Button>
    <Button variant="contained" onClick={handleConfirm}>Confirm</Button>
  </DialogActions>
</Dialog>
```

### Snackbar

**Slots:** `root`, `content`, `clickAwayListener`, `transition`

**CSS Classes:** `root`, `anchorOriginTopLeft`, `anchorOriginTopCenter`, `anchorOriginTopRight`, `anchorOriginBottomLeft`, `anchorOriginBottomCenter`, `anchorOriginBottomRight`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `ReactNode` | — | Action element |
| `anchorOrigin` | `{ vertical, horizontal }` | `{ vertical: 'bottom', horizontal: 'left' }` | Position |
| `autoHideDuration` | `number` \| `null` | `null` | Auto-close duration (ms) |
| `children` | `ReactNode` | — | Content |
| `ContentProps` | `object` | — | Props for SnackbarContent |
| `disableWindowBlurListener` | `boolean` | `false` | Disable pause on window blur |
| `key` | `any` | — | Key for re-triggering |
| `message` | `ReactNode` | — | Message text |
| `onClose` | `(event, reason) => void` | — | Close handler |
| `onOpen` | `(event) => void` | — | Open handler |
| `open` | `boolean` | — | Open state |
| `resumeHideDuration` | `number` | — | Resume auto-hide after focus |
| `slotProps` | `object` | — | Props for slots |
| `slots` | `object` | — | Custom slot components |
| `TransitionComponent` | `ComponentType` | `Grow` | Transition component |
| `transitionDuration` | `number` \| `{ enter, exit }` | — | Transition duration |

### Alert

**CSS Classes:** `root`, `action`, `icon`, `message`, `filled`, `filledSuccess`, `filledInfo`, `filledWarning`, `filledError`, `outlined`, `outlinedSuccess`, `outlinedInfo`, `outlinedWarning`, `outlinedError`, `standard`, `standardSuccess`, `standardInfo`, `standardWarning`, `standardError`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `action` | `ReactNode` | — | Action element |
| `children` | `ReactNode` | — | Content |
| `closeText` | `string` | `'Close'` | ARIA close label |
| `color` | `'success'` \| `'info'` \| `'warning'` \| `'error'` + custom | — | Override severity color |
| `icon` | `ReactNode` | — | Custom icon |
| `onClose` | `(event) => void` | — | Close handler |
| `severity` | `'success'` \| `'info'` \| `'warning'` \| `'error'` | `'success'` | Severity |
| `variant` | `'standard'` \| `'filled'` \| `'outlined'` + custom | `'standard'` | Variant |

### Tooltip

**Slots:** `popper`, `transition`, `tooltip`, `arrow`, `touch`

**CSS Classes:** `tooltip`, `touch`, `tooltipPlacementLeft`, `tooltipPlacementRight`, `tooltipPlacementTop`, `tooltipPlacementBottom`, `arrow`, `popper`, `popperInteractive`, `popperArrow`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `arrow` | `boolean` | `false` | Show arrow |
| `children` | `ReactElement` | — | Target element |
| `describeChild` | `boolean` | `false` | Describe child instead of label |
| `disableFocusListener` | `boolean` | `false` | Disable on focus |
| `disableHoverListener` | `boolean` | `false` | Disable on hover |
| `disableInteractive` | `boolean` | `false` | Disable interactive |
| `disableTouchListener` | `boolean` | `false` | Disable on touch |
| `enterDelay` | `number` | `100` | Show delay (ms) |
| `enterNextDelay` | `number` | `0` | Delay between shows |
| `enterTouchDelay` | `number` | `700` | Touch show delay |
| `followCursor` | `boolean` | `false` | Follow cursor |
| `id` | `string` | — | HTML id |
| `leaveDelay` | `number` | `0` | Hide delay (ms) |
| `leaveTouchDelay` | `number` | `1500` | Touch hide delay |
| `onClose` | `(event) => void` | — | Close handler |
| `onOpen` | `(event) => void` | — | Open handler |
| `open` | `boolean` | — | Controlled open state |
| `placement` | `'bottom'` \| `'left'` \| `'right'` \| `'top'` + start/end variants | `'bottom'` | Placement |
| `PopperComponent` | `ComponentType` | `Popper` | Popper component |
| `PopperProps` | `object` | — | Props for Popper |
| `slotProps` | `object` | — | Props for slots |
| `slots` | `object` | — | Custom slot components |
| `title` | `ReactNode` | — | **Required** — Tooltip content |
| `TransitionComponent` | `ComponentType` | `Grow` | Transition component |
| `TransitionProps` | `object` | — | Props for transition |

### Badge

**Slots:** `root`, `badge`

**CSS Classes:** `root`, `badge`, `badgeColorDefault`, `badgeColorPrimary`, `badgeColorSecondary`, `badgeColorError`, `badgeColorInfo`, `badgeColorSuccess`, `badgeColorWarning`, `invisible`, `badgeVariantStandard`, `badgeVariantDot`, `badgeOverlapRectangular`, `badgeOverlapCircular`, `anchorOriginTopRight`, `anchorOriginTopLeft`, `anchorOriginBottomRight`, `anchorOriginBottomLeft`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `anchorOrigin` | `{ vertical, horizontal }` | `{ vertical: 'top', horizontal: 'right' }` | Badge position |
| `badgeContent` | `ReactNode` | — | Badge content |
| `children` | `ReactElement` | — | Target element |
| `color` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` + custom | `'default'` | Color |
| `invisible` | `boolean` | `false` | Hide badge |
| `max` | `number` | `99` | Max number display |
| `overlap` | `'rectangular'` \| `'circular'` | `'rectangular'` | Overlap shape |
| `showZero` | `boolean` | `false` | Show when content is 0 |
| `variant` | `'standard'` \| `'dot'` + custom | `'standard'` | Variant |

---

## Data Display

### Typography

**CSS Classes:** `root`, `h1`–`h6`, `subtitle1`, `subtitle2`, `body1`, `body2`, `button`, `caption`, `overline`, `alignLeft`, `alignCenter`, `alignRight`, `alignJustify`, `noWrap`, `gutterBottom`, `paragraph`, `colorInherit`, `colorPrimary`, `colorSecondary`, `colorTextPrimary`, `colorTextSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `displayInline`, `displayBlock`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `align` | `'inherit'` \| `'left'` \| `'center'` \| `'right'` \| `'justify'` | `'inherit'` | Text alignment |
| `children` | `ReactNode` | — | Content |
| `color` | `'initial'` \| `'inherit'` \| `'primary'` \| `'secondary'` \| `'textPrimary'` \| `'textSecondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` | — | Color |
| `component` | `elementType` | — | Rendered element |
| `display` | `'initial'` \| `'block'` \| `'inline'` | `'initial'` | Display mode |
| `gutterBottom` | `boolean` | `false` | Bottom margin |
| `noWrap` | `boolean` | `false` | Truncate with ellipsis |
| `paragraph` | `boolean` | `false` | Bottom margin (paragraph) |
| `variant` | `'h1'` \| `'h2'` \| `'h3'` \| `'h4'` \| `'h5'` \| `'h6'` \| `'subtitle1'` \| `'subtitle2'` \| `'body1'` \| `'body2'` \| `'caption'` \| `'button'` \| `'overline'` \| `'inherit'` + custom | `'body1'` | Typography variant |
| `variantMapping` | `object` | — | Variant to element mapping |

### Chip

**Slots:** `root`, `label`, `avatar`, `icon`, `deleteIcon`

**CSS Classes:** `root`, `sizeSmall`, `sizeMedium`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `disabled`, `clickable`, `clickableColorPrimary`, `clickableColorSecondary`, `deletable`, `deletableColorPrimary`, `deletableColorSecondary`, `outlined`, `filled`, `outlinedPrimary`, `outlinedSecondary`, `filledPrimary`, `filledSecondary`, `avatar`, `avatarSmall`, `avatarMedium`, `avatarColorPrimary`, `avatarColorSecondary`, `icon`, `iconSmall`, `iconMedium`, `iconColorPrimary`, `iconColorSecondary`, `label`, `labelSmall`, `labelMedium`, `deleteIcon`, `deleteIconSmall`, `deleteIconMedium`, `deleteIconColorPrimary`, `deleteIconColorSecondary`, `focusVisible`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `avatar` | `ReactElement` | — | Avatar element |
| `clickable` | `boolean` | — | Clickable |
| `color` | `'default'` \| `'primary'` \| `'secondary'` \| `'error'` \| `'info'` \| `'success'` \| `'warning'` + custom | `'default'` | Color |
| `deleteIcon` | `ReactElement` | — | Custom delete icon |
| `disabled` | `boolean` | `false` | Disabled |
| `icon` | `ReactElement` | — | Icon element |
| `label` | `ReactNode` | — | Chip label |
| `onClick` | `(event) => void` | — | Click handler |
| `onDelete` | `(event) => void` | — | Delete handler |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `variant` | `'filled'` \| `'outlined'` + custom | `'filled'` | Variant |

### Table

**CSS Classes:** `root`, `stickyHeader`, `sizeSmall`, `sizeMedium`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | — | Table content |
| `padding` | `'normal'` \| `'checkbox'` \| `'none'` | `'normal'` | Cell padding |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `stickyHeader` | `boolean` | `false` | Sticky header |

### TableCell

**CSS Classes:** `root`, `head`, `body`, `footer`, `sizeSmall`, `sizeMedium`, `stickyHeader`, `paddingCheckbox`, `paddingNone`, `alignLeft`, `alignCenter`, `alignRight`, `alignJustify`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `align` | `'center'` \| `'inherit'` \| `'justify'` \| `'left'` \| `'right'` | `'inherit'` | Alignment |
| `padding` | `'checkbox'` \| `'none'` \| `'normal'` | `'normal'` | Padding |
| `size` | `'small'` \| `'medium'` + custom | `'medium'` | Size |
| `sortDirection` | `'asc'` \| `'desc'` \| `false` | — | Sort direction |
| `stickyHeader` | `boolean` | `false` | Sticky header |
| `variant` | `'body'` \| `'footer'` \| `'head'` | — | Cell type |

### Card

**CSS Classes:** `root`, `outlined`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `raised` | `boolean` | `false` | Elevated shadow |

### Avatar

**CSS Classes:** `root`, `colorDefault`, `colorPrimary`, `colorSecondary`, `colorError`, `colorInfo`, `colorSuccess`, `colorWarning`, `circular`, `rounded`, `square`, `img`, `fallback`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `alt` | `string` | — | Alt text |
| `children` | `ReactNode` | — | Content (when no src) |
| `imgProps` | `object` | — | Props for img |
| `sizes` | `string` | — | srcset sizes |
| `src` | `string` | — | Image URL |
| `srcSet` | `string` | — | srcset |
| `variant` | `'circular'` \| `'rounded'` \| `'square'` | `'circular'` | Shape |

### Accordion

**Slots:** `root`, `heading`, `transition`, `region`

**CSS Classes:** `root`, `rounded`, `expanded`, `disabled`, `disableGutters`, `region`, `heading`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | — | Content |
| `defaultExpanded` | `boolean` | `false` | Default expanded |
| `disabled` | `boolean` | `false` | Disabled |
| `disableGutters` | `boolean` | `false` | Remove padding |
| `expanded` | `boolean` | — | Controlled expanded state |
| `onChange` | `(event, expanded) => void` | — | Change handler |
| `square` | `boolean` | `false` | Remove border radius |
| `TransitionComponent` | `ComponentType` | `Collapse` | Transition component |
| `TransitionProps` | `object` | — | Props for transition |

---

## Surfaces

### Paper

**CSS Classes:** `root`, `rounded`, `outlined`, `elevation0`–`elevation24`

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `children` | `ReactNode` | — | Content |
| `elevation` | `number` | `1` | Shadow elevation (0-24) |
| `square` | `boolean` | `false` | Remove border radius |
| `variant` | `'elevation'` \| `'outlined'` | `'elevation'` | Variant |

### AppBar (see Navigation section)

### Card (see Data Display section)

---

## Utils

### CssBaseline

Normalizes browser styles and applies theme background.

```tsx
import CssBaseline from '@mui/material/CssBaseline';

<ThemeProvider theme={theme}>
  <CssBaseline />  {/* Place at root */}
  <App />
</ThemeProvider>

// Scoped CSS baseline
import ScopedCssBaseline from '@mui/material/ScopedCssBaseline';
<ScopedCssBaseline>
  <MyComponent />
</ScopedCssBaseline>
```

### GlobalStyles

Apply global CSS using the theme.

```tsx
import GlobalStyles from '@mui/material/GlobalStyles';

<GlobalStyles styles={(theme) => ({
  body: { bgcolor: theme.palette.background.default },
  '::-webkit-scrollbar': { width: 8 },
  '::-webkit-scrollbar-thumb': { bgcolor: theme.palette.grey[400], borderRadius: 4 },
})} />
```

### useMediaQuery

From `@mui/system/src/useMediaQuery/useMediaQuery.ts`:

```tsx
import useMediaQuery from '@mui/material/useMediaQuery';

function MyComponent() {
  const isMobile = useMediaQuery('(max-width:600px)');
  const isDark = useMediaQuery((theme) => theme.breakpoints.down('md'));
  return isMobile ? <MobileLayout /> : <DesktopLayout />;
}
```

**Options (UseMediaQueryOptions):**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultMatches` | `boolean` | `false` | SSR default value |
| `matchMedia` | `typeof window.matchMedia` | — | Custom matchMedia |
| `noSsr` | `boolean` | `false` | Skip SSR double-render |
| `ssrMatchMedia` | `(query) => { matches }` | — | Server-side matchMedia |

### useScrollTrigger

```tsx
import useScrollTrigger from '@mui/material/useScrollTrigger';

function ElevationScroll({ children }) {
  const trigger = useScrollTrigger({ disableHysteresis: true, threshold: 0 });
  return React.cloneElement(children, { elevation: trigger ? 4 : 0 });
}
```

---

## Lab Components

From `@mui/labs` — components in development:

| Component | Description |
|-----------|-------------|
| `LoadingButton` | Button with built-in loading state |
| `Timeline` / `TimelineItem` / `TimelineSeparator` / `TimelineConnector` / `TimelineContent` / `TimelineDot` | Timeline layout |
| `TreeView` / `TreeItem` | Tree navigation (replaced by `@mui/x-tree-view`) |
| `Masonry` | Masonry grid layout |
| `TabContext` / `TabList` / `TabPanel` | Tab state management |
| `ToggleButton` / `ToggleButtonGroup` | Toggle selection (now in core) |

> **Note**: `ToggleButton` and `ToggleButtonGroup` have been promoted to `@mui/material` in v9. Use `@mui/material/ToggleButton` instead of `@mui/lab/ToggleButton`.
