# MUI X: Advanced Components Reference

MUI X provides advanced, feature-rich components that go beyond the core Material UI library. These components handle complex use cases like data-heavy tables, date/time selection, and data visualization.

> **Note**: MUI X packages are in a separate repository (https://github.com/mui/mui-x) but follow the same API patterns as core MUI.

---

## Packages

| Package | Component | License |
|---------|-----------|---------|
| `@mui/x-data-grid` | DataGrid, DataGridPro, DataGridPremium | MIT / Commercial |
| `@mui/x-date-pickers` | DatePicker, TimePicker, DateTimePicker, DateRangePicker | MIT / Commercial |
| `@mui/x-charts` | BarChart, LineChart, PieChart, ScatterChart, SparkLineChart | MIT |
| `@mui/x-tree-view` | TreeView, RichTreeView, SimpleTreeView | MIT |
| `@mui/x-scheduler` | Scheduler | Commercial |
| `@mui/x-chat` | Chat | Commercial |

### Installation

```bash
# Data Grid
npm install @mui/x-data-grid

# Data Grid Pro (requires license)
npm install @mui/x-data-grid-pro

# Date Pickers (requires dayjs or date-fns or luxon)
npm install @mui/x-date-pickers dayjs
# or
npm install @mui/x-date-pickers date-fns

# Charts
npm install @mui/x-charts

# Tree View
npm install @mui/x-tree-view
```

---

## DataGrid

The DataGrid is a fast, feature-rich data table component. It comes in three versions:
- **DataGrid** (MIT) — Community version with core features
- **DataGridPro** (Commercial) — Advanced features: row grouping, Excel export, row reordering, clipboard
- **DataGridPremium** (Commercial) — All Pro features + aggregation, row pinning, Excel export with styling

### Column Definition

```typescript
interface GridColDef {
  field: string;                    // Required — data field name
  headerName?: string;              // Column header text
  width?: number;                   // Column width (default: 100)
  minWidth?: number;                // Minimum width (default: 50)
  maxWidth?: number;                // Maximum width
  flex?: number;                    // Flex grow factor
  hide?: boolean;                   // Hide column
  sortable?: boolean;               // Enable sorting (default: true)
  filterable?: boolean;             // Enable filtering (default: true)
  editable?: boolean;               // Enable editing (default: false)
  type?: string;                    // 'string' | 'number' | 'date' | 'dateTime' | 'boolean' | 'singleSelect' | 'custom'
  valueOptions?: any[];             // Options for singleSelect type
  valueGetter?: (params) => any;    // Custom value getter
  valueFormatter?: (params) => string; // Custom value formatter
  renderCell?: (params) => ReactNode;  // Custom cell renderer
  renderHeader?: (params) => ReactNode; // Custom header renderer
  cellClassName?: string | ((params) => string); // Cell CSS class
  headerClassName?: string;         // Header CSS class
  align?: 'left' | 'right' | 'center'; // Cell alignment
  headerAlign?: 'left' | 'right' | 'center'; // Header alignment
  description?: string;             // Column description (tooltip)
  disableColumnMenu?: boolean;      // Disable column menu
  disableReorder?: boolean;         // Disable column reorder
  resizable?: boolean;              // Enable resize (default: true)
  sortable?: boolean;               // Enable sort
  filterOperators?: GridFilterOperator[]; // Custom filter operators
}
```

### Row Definition

```typescript
interface GridRowModel {
  id: string | number;  // Required — unique row ID
  [field: string]: any; // Data fields matching column definitions
}
```

### Basic DataGrid

```tsx
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'firstName', headerName: 'First name', width: 150, editable: true },
  { field: 'lastName', headerName: 'Last name', width: 150, editable: true },
  {
    field: 'age',
    headerName: 'Age',
    type: 'number',
    width: 110,
    editable: true,
  },
  {
    field: 'fullName',
    headerName: 'Full name',
    description: 'This column has a value getter and is not sortable.',
    sortable: false,
    width: 200,
    valueGetter: (value, row) => `${row.firstName || ''} ${row.lastName || ''}`,
  },
];

const rows = [
  { id: 1, lastName: 'Snow', firstName: 'Jon', age: 14 },
  { id: 2, lastName: 'Lannister', firstName: 'Cersei', age: 31 },
  { id: 3, lastName: 'Lannister', firstName: 'Jaime', age: 31 },
];

<DataGrid
  rows={rows}
  columns={columns}
  initialState={{
    pagination: { paginationModel: { pageSize: 5 } },
  }}
  pageSizeOptions={[5, 10, 25]}
  checkboxSelection
  disableRowSelectionOnClick
/>
```

### DataGrid with Custom Cell Renderer

```tsx
const columns = [
  { field: 'name', headerName: 'Name', width: 200 },
  {
    field: 'status',
    headerName: 'Status',
    width: 150,
    renderCell: (params) => (
      <Chip
        label={params.value}
        color={params.value === 'Active' ? 'success' : params.value === 'Inactive' ? 'error' : 'warning'}
        size="small"
      />
    ),
  },
  {
    field: 'actions',
    headerName: 'Actions',
    width: 120,
    renderCell: (params) => (
      <Stack direction="row" spacing={1}>
        <IconButton size="small" onClick={() => handleEdit(params.row)}><EditIcon fontSize="small" /></IconButton>
        <IconButton size="small" onClick={() => handleDelete(params.row)}><DeleteIcon fontSize="small" /></IconButton>
      </Stack>
    ),
  },
];
```

### DataGrid Key Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `rows` | `GridRowModel[]` | `[]` | Row data |
| `columns` | `GridColDef[]` | `[]` | Column definitions |
| `autoHeight` | `boolean` | `false` | Auto height based on rows |
| `checkboxSelection` | `boolean` | `false` | Show row checkboxes |
| `columnBuffer` | `number` | `3` | Extra columns rendered outside viewport |
| `density` | `'compact'` \| `'standard'` \| `'comfortable'` | `'standard'` | Row density |
| `disableColumnFilter` | `boolean` | `false` | Disable column filtering |
| `disableColumnMenu` | `boolean` | `false` | Disable column menus |
| `disableColumnSelector` | `boolean` | `false` | Disable column selector |
| `disableDensitySelector` | `boolean` | `false` | Disable density selector |
| `disableRowSelectionOnClick` | `boolean` | `false` | Disable selection on click |
| `editMode` | `'cell'` \| `'row'` | `'cell'` | Edit mode |
| `filterMode` | `'client'` \| `'server'` | `'client'` | Filter mode |
| `headerHeight` | `number` | `56` | Header row height |
| `hideFooter` | `boolean` | `false` | Hide footer |
| `hideFooterPagination` | `boolean` | `false` | Hide pagination |
| `hideFooterRowCount` | `boolean` | `false` | Hide row count |
| `hideFooterSelectedRowCount` | `boolean` | `false` | Hide selected row count |
| `initialState` | `object` | — | Initial state (uncontrolled) |
| `loading` | `boolean` | `false` | Loading state |
| `localeText` | `object` | — | Localization text |
| `onCellClick` | `(params, event) => void` | — | Cell click handler |
| `onCellEditStart` | `(params) => void` | — | Cell edit start |
| `onCellEditStop` | `(params) => void` | — | Cell edit stop |
| `onColumnOrderChange` | `(params) => void` | — | Column reorder |
| `onFilterModelChange` | `(model) => void` | — | Filter change |
| `onPaginationModelChange` | `(model) => void` | — | Pagination change |
| `onRowClick` | `(params, event) => void` | — | Row click handler |
| `onRowSelectionModelChange` | `(model) => void` | — | Selection change |
| `onSortModelChange` | `(model) => void` | — | Sort change |
| `pageSizeOptions` | `number[]` | `[25, 50, 100]` | Page size options |
| `pagination` | `boolean` | `false` | Enable pagination |
| `paginationMode` | `'client'` \| `'server'` | `'client'` | Pagination mode |
| `processRowUpdate` | `(newRow, oldRow) => Promise<GridRowModel>` | — | Row update processor |
| `rowHeight` | `number` | `52` | Row height |
| `rowSelection` | `boolean` | `true` | Enable row selection |
| `rowSpacingType` | `'margin'` \| `'border'` | `'margin'` | Row spacing type |
| `rowsLoadingMode` | `'client'` \| `'server'` | — | Server-side loading |
| `sortingMode` | `'client'` \| `'server'` | `'client'` | Sorting mode |
| `slotProps` | `object` | — | Props for slots |
| `slots` | `object` | — | Custom slot components |

### DataGrid Slots

| Slot | Default Component | Description |
|------|------------------|-------------|
| `toolbar` | `null` | Toolbar above the grid |
| `footer` | `GridFooter` | Footer with pagination |
| `loadingOverlay` | `GridLoadingOverlay` | Loading overlay |
| `noRowsOverlay` | `GridNoRowsOverlay` | Empty state overlay |
| `noResultsOverlay` | `GridNoResultsOverlay` | No results overlay |
| `columnMenu` | `GridColumnMenu` | Column header menu |
| `pagination` | `GridPagination` | Pagination component |
| `baseButton` | `Button` | Base button |
| `baseCheckbox` | `Checkbox` | Base checkbox |
| `baseTextField` | `TextField` | Base text field |
| `baseSelect` | `Select` | Base select |
| `baseSwitch` | `Switch` | Base switch |
| `baseIconButton` | `IconButton` | Base icon button |
| `baseTooltip` | `Tooltip` | Base tooltip |
| `cell` | `GridCell` | Data cell |
| `row` | `GridRow` | Data row |

### Server-Side Data

```tsx
<DataGrid
  rows={rows}
  columns={columns}
  paginationMode="server"
  sortingMode="server"
  filterMode="server"
  rowCount={totalCount}
  paginationModel={paginationModel}
  onPaginationModelChange={setPaginationModel}
  sortModel={sortModel}
  onSortModelChange={setSortModel}
  filterModel={filterModel}
  onFilterModelChange={setFilterModel}
  loading={isLoading}
/>
```

### DataGrid with Toolbar

```tsx
import { DataGrid, GridToolbar } from '@mui/x-data-grid';

<DataGrid
  rows={rows}
  columns={columns}
  slots={{ toolbar: GridToolbar }}
  slotProps={{
    toolbar: {
      showQuickFilter: true,
      quickFilterProps: { debounceMs: 500 },
    },
  }}
  initialState={{
    columns: { columnVisibilityModel: { id: false } },
    filter: { filterModel: { items: [] } },
    sorting: { sortModel: [{ field: 'name', sort: 'asc' }] },
  }}
  disableColumnSelector
  disableDensitySelector
/>
```

### DataGrid Pro Features

```tsx
import { DataGridPro } from '@mui/x-data-grid-pro';

<DataGridPro
  rows={rows}
  columns={columns}
  // Row grouping
  initialState={{
    rowGrouping: { model: ['status'] },
  }}
  // Tree data
  treeData
  getTreeDataPath={(row) => row.path}
  groupingColDef={{ headerName: 'Hierarchy' }}
  // Row reordering
  rowReordering
  onRowOrderChange={handleRowOrder}
  // Clipboard
  clipboardCopy
  // Column pinning
  initialState={{
    pinnedColumns: { left: ['id'], right: ['actions'] },
  }}
  // Detail panel
  getDetailPanelContent={(row) => <DetailPanel row={row} />}
  getDetailPanelHeight={({ row }) => 'auto'}
/>
```

---

## Date Pickers

### Adapter Setup

```tsx
// With dayjs
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

<LocalizationProvider dateAdapter={AdapterDayjs}>
  <App />
</LocalizationProvider>

// With date-fns
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
<LocalizationProvider dateAdapter={AdapterDateFns}>
  <App />
</LocalizationProvider>

// With luxon
import { AdapterLuxon } from '@mui/x-date-pickers/AdapterLuxon';
<LocalizationProvider dateAdapter={AdapterLuxon}>
  <App />
</LocalizationProvider>
```

### DatePicker

```tsx
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

<DatePicker
  label="Birth Date"
  value={value}
  onChange={(newValue) => setValue(newValue)}
  slotProps={{
    textField: { fullWidth: true, size: 'small' },
  }}
/>
```

**Key Props:**

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `Dayjs` \| `Date` \| `null` | — | Selected date |
| `defaultValue` | `Dayjs` \| `Date` \| `null` | — | Default date |
| `onChange` | `(value) => void` | — | Change handler |
| `disableFuture` | `boolean` | `false` | Disable future dates |
| `disablePast` | `boolean` | `false` | Disable past dates |
| `minDate` | `Dayjs` \| `Date` | — | Minimum date |
| `maxDate` | `Dayjs` \| `Date` | — | Maximum date |
| `open` | `boolean` | — | Controlled open state |
| `onOpen` | `() => void` | — | Open handler |
| `onClose` | `() => void` | — | Close handler |
| `disabled` | `boolean` | `false` | Disabled |
| `readOnly` | `boolean` | `false` | Read only |
| `format` | `string` | Locale default | Date format string |
| `views` | `('year'` \| `'month'` \| `'day')[]` | `['year', 'month', 'day']` | Available views |
| `openTo` | `'year'` \| `'month'` \| `'day'` | `'day'` | Initial view |
| `slotProps` | `object` | — | Props for slots |
| `slots` | `object` | — | Custom slot components |
| `timezone` | `string` | Default timezone | Timezone |

### TimePicker

```tsx
import { TimePicker } from '@mui/x-date-pickers/TimePicker';

<TimePicker
  label="Start Time"
  value={value}
  onChange={(newValue) => setValue(newValue)}
  ampm={false}  // 24-hour format
  minTime={dayjs().hour(8).minute(0)}
  maxTime={dayjs().hour(18).minute(0)}
/>
```

### DateTimePicker

```tsx
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';

<DateTimePicker
  label="Appointment Date & Time"
  value={value}
  onChange={(newValue) => setValue(newValue)}
/>
```

### DateRangePicker (Pro)

```tsx
import { DateRangePicker } from '@mui/x-date-pickers-pro/DateRangePicker';

<DateRangePicker
  value={value}
  onChange={(newValue) => setValue(newValue)}
  localeText={{ start: 'Check-in', end: 'Check-out' }}
/>
```

### Date Pickers in Forms (react-hook-form)

```tsx
import { Controller } from 'react-hook-form';

<Controller
  name="startDate"
  control={control}
  render={({ field: { onChange, value }, fieldState: { error } }) => (
    <DatePicker
      label="Start Date"
      value={value}
      onChange={onChange}
      slotProps={{
        textField: {
          error: !!error,
          helperText: error?.message,
          fullWidth: true,
        },
      }}
    />
  )}
/>
```

---

## Charts

### BarChart

```tsx
import { BarChart } from '@mui/x-charts/BarChart';

<BarChart
  xAxis={[{ scaleType: 'band', data: ['Group A', 'Group B', 'Group C'] }]}
  series={[
    { data: [4, 3, 5], label: 'Series 1' },
    { data: [1, 6, 3], label: 'Series 2' },
    { data: [2, 5, 6], label: 'Series 3' },
  ]}
  width={500}
  height={300}
/>
```

### LineChart

```tsx
import { LineChart } from '@mui/x-charts/LineChart';

<LineChart
  xAxis={[{ data: [1, 2, 3, 5, 8, 10] }]}
  series={[
    { data: [2, 5.5, 2, 8.5, 1.5, 5], label: 'Series A' },
    { data: [1, 3, 4, 2, 6, 3], label: 'Series B' },
  ]}
  width={500}
  height={300}
/>
```

### PieChart

```tsx
import { PieChart } from '@mui/x-charts/PieChart';

<PieChart
  series={[
    {
      data: [
        { id: 0, value: 10, label: 'series A' },
        { id: 1, value: 15, label: 'series B' },
        { id: 2, value: 20, label: 'series C' },
      ],
      innerRadius: 30,  // Donut chart
      paddingAngle: 2,
      cornerRadius: 4,
    },
  ]}
  width={400}
  height={200}
/>
```

### ScatterChart

```tsx
import { ScatterChart } from '@mui/x-charts/ScatterChart';

<ScatterChart
  series={[
    { data: [{ x: 1, y: 3, id: 0 }, { x: 2, y: 5, id: 1 }], label: 'Group A' },
    { data: [{ x: 1.5, y: 4, id: 2 }, { x: 3, y: 2, id: 3 }], label: 'Group B' },
  ]}
  width={500}
  height={300}
/>
```

### SparkLineChart

```tsx
import { SparkLineChart } from '@mui/x-charts/SparkLineChart';

<SparkLineChart data={[1, 4, 2, 5, 7, 2, 4, 6]} width={200} height={60} />
```

### Charts Common Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `series` | `Series[]` | `[]` | Data series |
| `width` | `number` | — | Chart width |
| `height` | `number` | — | Chart height |
| `margin` | `{ top, right, bottom, left }` | — | Chart margin |
| `xAxis` | `AxisConfig[]` | — | X-axis configuration |
| `yAxis` | `AxisConfig[]` | — | Y-axis configuration |
| `colors` | `string[]` \| `palette` | `'blueberryTwilightPalette'` | Color palette |
| `tooltip` | `{ trigger }` | — | Tooltip config |
| `legend` | `{ position, direction }` | — | Legend config |
| `grid` | `{ vertical, horizontal }` | — | Grid lines |
| `topAxis` | `string` | — | Top axis ID |
| `leftAxis` | `string` | — | Left axis ID |
| `rightAxis` | `string` | — | Right axis ID |
| `bottomAxis` | `string` | — | Bottom axis ID |
| `skipAnimation` | `boolean` | `false` | Skip animation |
| `slotProps` | `object` | — | Props for slots |
| `slots` | `object` | — | Custom slot components |

### Available Color Palettes

```tsx
import { blueberryTwilightPalette, mangoFusionPalette, cheerfulFiestaPalette, lavenderPalette, macaronPalette } from '@mui/x-charts/colorPalettes';

<BarChart colors={mangoFusionPalette} ... />
```

---

## Tree View

### SimpleTreeView (Uncontrolled)

```tsx
import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import TreeItem from '@mui/x-tree-view/TreeItem';

<SimpleTreeView>
  <TreeItem itemId="1" label="Root">
    <TreeItem itemId="2" label="Child 1" />
    <TreeItem itemId="3" label="Child 2">
      <TreeItem itemId="4" label="Grandchild" />
    </TreeItem>
  </TreeItem>
</SimpleTreeView>
```

### RichTreeView (Data-Driven)

```tsx
import { RichTreeView } from '@mui/x-tree-view/RichTreeView';

const ITEMS = [
  { id: '1', label: 'Root', children: [
    { id: '2', label: 'Child 1' },
    { id: '3', label: 'Child 2', children: [
      { id: '4', label: 'Grandchild' },
    ]},
  ]},
];

<RichTreeView items={ITEMS} />
```

### Tree View Key Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `expandedItems` | `string[]` | — | Controlled expanded items |
| `defaultExpandedItems` | `string[]` | `[]` | Default expanded items |
| `selectedItems` | `string` \| `string[]` | — | Controlled selected items |
| `onExpandedItemsChange` | `(event, itemIds) => void` | — | Expand change handler |
| `onSelectedItemsChange` | `(event, itemIds) => void` | — | Select change handler |
| `multiSelect` | `boolean` | `false` | Multiple selection |
| `checkboxSelection` | `boolean` | `false` | Checkbox selection |
| `disabledItemsFocusable` | `boolean` | `false` | Focusable disabled items |
| `expansionTrigger` | `'content'` \| `'iconContainer'` | `'content'` | Click target for expand |
| `slots` | `object` | — | Custom slot components |
| `slotProps` | `object` | — | Props for slots |

---

## Common Integration Patterns

### DataGrid with Full CRUD

```tsx
<DataGrid
  rows={rows}
  columns={columns}
  processRowUpdate={async (newRow, oldRow) => {
    const response = await updateRow(newRow);
    return response;
  }}
  onProcessRowUpdateError={(error) => {
    snackbar.showError(error.message);
  }}
  editMode="row"
  slots={{ toolbar: EditToolbar }}
/>
```

### Date Pickers with Form Validation

```tsx
<LocalizationProvider dateAdapter={AdapterDayjs}>
  <Controller
    name="startDate"
    control={control}
    rules={{ required: 'Start date is required' }}
    render={({ field: { onChange, value }, fieldState: { error } }) => (
      <DatePicker
        label="Start Date"
        value={value}
        onChange={onChange}
        disablePast
        slotProps={{
          textField: {
            error: !!error,
            helperText: error?.message,
            fullWidth: true,
            required: true,
          },
        }}
      />
    )}
  />
</LocalizationProvider>
```

### Charts with Responsive Container

```tsx
import { ResponsiveChartContainer } from '@mui/x-charts';

<Box sx={{ width: '100%', height: 400 }}>
  <BarChart
    xAxis={[{ scaleType: 'band', data: categories }]}
    series={series}
    height={400}
  />
</Box>
```
