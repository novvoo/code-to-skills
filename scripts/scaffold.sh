#!/bin/bash
# MUI Project Scaffolding Script
# Usage: bash scaffold.sh [project-name] [template]
# Templates: basic, dashboard, form, data-grid

set -e

PROJECT_NAME="${1:-mui-app}"
TEMPLATE="${2:-basic}"
TARGET_DIR="$(pwd)/$PROJECT_NAME"

echo "🚀 Scaffolding MUI project: $PROJECT_NAME (template: $TEMPLATE)"

# Create project directory
mkdir -p "$TARGET_DIR/src"
cd "$TARGET_DIR"

# Create package.json
cat > package.json << 'PKGJSON'
{
  "name": "PROJECT_NAME_PLACEHOLDER",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  }
}
PKGJSON
sed -i "s/PROJECT_NAME_PLACEHOLDER/$PROJECT_NAME/" package.json

# Create tsconfig.json
cat > tsconfig.json << 'TSCONFIG'
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src"]
}
TSCONFIG

# Create vite.config.ts
cat > vite.config.ts << 'VITECONFIG'
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
});
VITECONFIG

# Create index.html
cat > index.html << 'HTML'
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MUI App</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
HTML

# Create main.tsx
cat > src/main.tsx << 'MAINTSX'
import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import App from './App';

const theme = createTheme();

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </React.StrictMode>,
);
MAINTSX

# Create template-specific App.tsx
case "$TEMPLATE" in
  basic)
    cat > src/App.tsx << 'APPBASIC'
import { Container, Typography, Box, Button, Stack } from '@mui/material';

export default function App() {
  return (
    <Container maxWidth="sm">
      <Box sx={{ my: 8, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Typography variant="h3" component="h1" gutterBottom>
          Welcome to MUI
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 4, textAlign: 'center' }}>
          Your Material UI app is ready. Start building!
        </Typography>
        <Stack direction="row" spacing={2}>
          <Button variant="contained" color="primary">Get Started</Button>
          <Button variant="outlined" color="primary">Learn More</Button>
        </Stack>
      </Box>
    </Container>
  );
}
APPBASIC
    ;;
  dashboard)
    cat > src/App.tsx << 'APPDASHBOARD'
import * as React from 'react';
import {
  Box, AppBar, Toolbar, Typography, Drawer, List, ListItem,
  ListItemIcon, ListItemText, IconButton, Divider, Container, Grid, Card, CardContent, Paper
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PeopleIcon from '@mui/icons-material/People';
import SettingsIcon from '@mui/icons-material/Settings';

const DRAWER_WIDTH = 240;

export default function App() {
  const [mobileOpen, setMobileOpen] = React.useState(false);

  const drawer = (
    <Box>
      <Toolbar><Typography variant="h6">Dashboard</Typography></Toolbar>
      <Divider />
      <List>
        <ListItem button><ListItemIcon><DashboardIcon /></ListItemIcon><ListItemText primary="Overview" /></ListItem>
        <ListItem button><ListItemIcon><PeopleIcon /></ListItemIcon><ListItemText primary="Users" /></ListItem>
        <ListItem button><ListItemIcon><SettingsIcon /></ListItemIcon><ListItemText primary="Settings" /></ListItem>
      </List>
    </Box>
  );

  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar position="fixed" sx={{ zIndex: theme => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <IconButton color="inherit" edge="start" onClick={() => setMobileOpen(!mobileOpen)} sx={{ mr: 2, display: { md: 'none' } }}>
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap>My Dashboard</Typography>
        </Toolbar>
      </AppBar>
      <Drawer variant="temporary" open={mobileOpen} onClose={() => setMobileOpen(false)}
        sx={{ display: { xs: 'block', md: 'none' }, '& .MuiDrawer-paper': { boxSizing: 'border-box', width: DRAWER_WIDTH } }}>
        {drawer}
      </Drawer>
      <Drawer variant="permanent" open sx={{ display: { xs: 'none', md: 'block' }, '& .MuiDrawer-paper': { boxSizing: 'border-box', width: DRAWER_WIDTH } }}>
        {drawer}
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1 }}>
        <Toolbar />
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Grid container spacing={3}>
            <Grid size={{ xs: 12, md: 4 }}>
              <Card><CardContent><Typography color="text.secondary" gutterBottom>Users</Typography><Typography variant="h4">1,234</Typography></CardContent></Card>
            </Grid>
            <Grid size={{ xs: 12, md: 4 }}>
              <Card><CardContent><Typography color="text.secondary" gutterBottom>Revenue</Typography><Typography variant="h4">$12.3K</Typography></CardContent></Card>
            </Grid>
            <Grid size={{ xs: 12, md: 4 }}>
              <Card><CardContent><Typography color="text.secondary" gutterBottom>Orders</Typography><Typography variant="h4">567</Typography></CardContent></Card>
            </Grid>
            <Grid size={{ xs: 12 }}>
              <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: 240 }}>
                <Typography variant="h6" gutterBottom>Recent Activity</Typography>
              </Paper>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </Box>
  );
}
APPDASHBOARD
    ;;
  form)
    cat > src/App.tsx << 'APPFORM'
import * as React from 'react';
import {
  Container, Box, Typography, TextField, Button, MenuItem, Stack, FormControlLabel, Checkbox, Alert
} from '@mui/material';

const roles = ['Developer', 'Designer', 'Manager', 'QA Engineer'];

export default function App() {
  const [submitted, setSubmitted] = React.useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{ my: 8 }}>
        <Typography variant="h4" component="h1" gutterBottom>Create Account</Typography>
        {submitted && <Alert severity="success" sx={{ mb: 2 }}>Account created successfully!</Alert>}
        <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
          <Stack spacing={2}>
            <TextField label="Full Name" variant="outlined" fullWidth required />
            <TextField label="Email" type="email" variant="outlined" fullWidth required />
            <TextField label="Password" type="password" variant="outlined" fullWidth required helperText="Minimum 8 characters" />
            <TextField select label="Role" variant="outlined" fullWidth defaultValue="">
              {roles.map(role => <MenuItem key={role} value={role}>{role}</MenuItem>)}
            </TextField>
            <FormControlLabel control={<Checkbox required />} label="I agree to the terms and conditions" />
            <Button type="submit" variant="contained" size="large" fullWidth>Create Account</Button>
          </Stack>
        </Box>
      </Box>
    </Container>
  );
}
APPFORM
    ;;
  data-grid)
    cat > src/App.tsx << 'APPGRID'
import { Box, Container, Typography } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'name', headerName: 'Name', width: 200, editable: true },
  { field: 'email', headerName: 'Email', width: 250 },
  { field: 'role', headerName: 'Role', width: 150, type: 'singleSelect', valueOptions: ['Admin', 'Editor', 'Viewer'], editable: true },
  { field: 'status', headerName: 'Status', width: 120 },
];

const rows = [
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', role: 'Admin', status: 'Active' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', role: 'Editor', status: 'Active' },
  { id: 3, name: 'Charlie Brown', email: 'charlie@example.com', role: 'Viewer', status: 'Inactive' },
  { id: 4, name: 'Diana Prince', email: 'diana@example.com', role: 'Admin', status: 'Active' },
  { id: 5, name: 'Eve Wilson', email: 'eve@example.com', role: 'Editor', status: 'Active' },
];

export default function App() {
  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>User Management</Typography>
        <Box sx={{ height: 400, width: '100%', mt: 2 }}>
          <DataGrid
            rows={rows}
            columns={columns}
            initialState={{ pagination: { paginationModel: { pageSize: 5 } } }}
            pageSizeOptions={[5, 10]}
            checkboxSelection
            disableRowSelectionOnClick
          />
        </Box>
      </Box>
    </Container>
  );
}
APPGRID
    ;;
  *)
    echo "Unknown template: $TEMPLATE. Using basic."
    cat > src/App.tsx << 'APPBASIC'
import { Container, Typography, Box, Button, Stack } from '@mui/material';

export default function App() {
  return (
    <Container maxWidth="sm">
      <Box sx={{ my: 8, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Typography variant="h3" component="h1" gutterBottom>Welcome to MUI</Typography>
        <Stack direction="row" spacing={2}>
          <Button variant="contained">Get Started</Button>
          <Button variant="outlined">Learn More</Button>
        </Stack>
      </Box>
    </Container>
  );
}
APPBASIC
    ;;
esac

# Install dependencies
echo "📦 Installing dependencies..."
npm install react react-dom @mui/material @emotion/react @emotion/styled @mui/icons-material

case "$TEMPLATE" in
  data-grid)
    npm install @mui/x-data-grid
    ;;
  dashboard)
    npm install @mui/icons-material
    ;;
esac

npm install -D typescript @types/react @types/react-dom @vitejs/plugin-react vite

echo ""
echo "✅ Project '$PROJECT_NAME' created successfully!"
echo "   Template: $TEMPLATE"
echo "   Location: $TARGET_DIR"
echo ""
echo "   Next steps:"
echo "   cd $PROJECT_NAME"
echo "   npm run dev"
