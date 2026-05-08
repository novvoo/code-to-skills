# uni-app API Reference

## Navigation APIs

### uni.navigateTo(Object)
Navigate to a new page (push to stack). Max 10 pages in stack.

```uts
uni.navigateTo({
  url: '/pages/detail/detail?id=123&name=test',
  animationType: 'pop-in',      // pop-in / slide-in-bottom / fade-in / zoom-out / zoom-fade-out
  animationDuration: 300,
  success(res) { console.log('navigated') },
  fail(err) { console.error(err) }
})
```

### uni.redirectTo(Object)
Replace current page (remove current from stack).

```uts
uni.redirectTo({
  url: '/pages/login/login'
})
```

### uni.reLaunch(Object)
Close all pages and open target page.

```uts
uni.reLaunch({
  url: '/pages/index/index'
})
```

### uni.switchTab(Object)
Switch to tab bar page (closes all non-tab pages).

```uts
uni.switchTab({
  url: '/pages/my/my'
})
```

### uni.navigateBack(Object)
Go back in page stack.

```uts
uni.navigateBack({
  delta: 1  // Go back N pages
})
```

### getCurrentPages()
Get current page stack array.

```uts
const pages = getCurrentPages()
const currentPage = pages[pages.length - 1] as UniPage
const route = currentPage.route  // Current page path
```

## Networking APIs

### uni.request(Object)
HTTP network request.

```uts
uni.request({
  url: 'https://api.example.com/data',
  method: 'GET',  // GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS
  data: { key: 'value' },
  header: { 'Authorization': 'Bearer token' },
  timeout: 60000,
  success(res) {
    console.log(res.statusCode)  // HTTP status code
    console.log(res.data)        // Response data
  },
  fail(err) {
    console.error(err)
  }
})
```

**Async/Await pattern:**
```uts
async function fetchData(): Promise<void> {
  try {
    const res = await uni.request({
      url: 'https://api.example.com/data',
      method: 'GET'
    })
    console.log(res.data)
  } catch (e) {
    console.error(e)
  }
}
```

### uni.uploadFile(Object)
Upload file.

```uts
uni.uploadFile({
  url: 'https://api.example.com/upload',
  filePath: '/tmp/image.png',
  name: 'file',
  header: { 'Authorization': 'Bearer token' },
  formData: { 'userId': '123' },
  success(res) {
    console.log(res.data)  // Server response
  }
})
```

### uni.downloadFile(Object)
Download file.

```uts
uni.downloadFile({
  url: 'https://example.com/file.pdf',
  success(res) {
    if (res.statusCode === 200) {
      console.log('Saved to:', res.tempFilePath)
    }
  }
})
```

### uni.connectSocket / uni.onSocketOpen / uni.onSocketMessage / uni.onSocketClose / uni.sendSocketMessage
WebSocket communication.

```uts
uni.connectSocket({
  url: 'wss://example.com/ws',
  success() { console.log('Connected') }
})

uni.onSocketOpen(() => {
  console.log('WebSocket opened')
  uni.sendSocketMessage({ data: 'Hello' })
})

uni.onSocketMessage((res) => {
  console.log('Received:', res.data)
})

uni.onSocketClose(() => {
  console.log('WebSocket closed')
})
```

## Storage APIs

### uni.setStorage / uni.getStorage / uni.removeStorage
Async storage operations.

```uts
// Set
uni.setStorage({
  key: 'token',
  data: 'abc123',
  success() { console.log('Saved') }
})

// Get
uni.getStorage({
  key: 'token',
  success(res) { console.log(res.data) }
})

// Remove
uni.removeStorage({
  key: 'token',
  success() { console.log('Removed') }
})
```

### uni.setStorageSync / uni.getStorageSync / uni.removeStorageSync
Synchronous storage operations.

```uts
uni.setStorageSync('token', 'abc123')
const token = uni.getStorageSync('token')  // Returns 'abc123'
uni.removeStorageSync('token')
uni.clearStorageSync()  // Clear all
```

## UI Feedback APIs

### uni.showToast(Object)
Show toast message.

```uts
uni.showToast({
  title: 'Success',
  icon: 'success',  // success / error / fail / exception / loading / none
  duration: 1500,
  mask: false
})
```

### uni.hideToast()
Hide toast.

### uni.showLoading / uni.hideLoading
Show/hide loading indicator.

```uts
uni.showLoading({
  title: 'Loading...',
  mask: true  // Prevent touch events
})

// After operation completes
uni.hideLoading()
```

### uni.showModal(Object)
Show modal dialog.

```uts
uni.showModal({
  title: 'Confirm',
  content: 'Are you sure?',
  showCancel: true,
  cancelText: 'Cancel',
  confirmText: 'OK',
  success(res) {
    if (res.confirm) {
      console.log('Confirmed')
    } else {
      console.log('Cancelled')
    }
  }
})
```

### uni.showActionSheet(Object)
Show action sheet.

```uts
uni.showActionSheet({
  itemList: ['Camera', 'Album', 'Cancel'],
  success(res) {
    console.log('Selected:', res.tapIndex)
  }
})
```

## Navigation Bar APIs

### uni.setNavigationBarTitle
```uts
uni.setNavigationBarTitle({ title: 'New Title' })
```

### uni.setNavigationBarColor
```uts
uni.setNavigationBarColor({
  frontColor: '#ffffff',
  backgroundColor: '#007AFF',
  animation: { duration: 300, timingFunc: 'easeIn' }
})
```

### uni.showNavigationBarLoading / uni.hideNavigationBarLoading
Show/hide navigation bar loading indicator.

## Tab Bar APIs

### uni.setTabBarBadge / uni.removeTabBarBadge
```uts
uni.setTabBarBadge({ index: 0, text: '5' })
uni.removeTabBarBadge({ index: 0 })
```

### uni.setTabBarStyle
```uts
uni.setTabBarStyle({
  color: '#999999',
  selectedColor: '#007AFF',
  backgroundColor: '#ffffff',
  borderStyle: 'white'
})
```

### uni.setTabBarItem
```uts
uni.setTabBarItem({
  index: 0,
  text: 'Home',
  iconPath: '/static/tab/home.png',
  selectedIconPath: '/static/tab/home-active.png'
})
```

### uni.showTabBar / uni.hideTabBar
Show/hide tab bar.

## Media APIs

### uni.chooseImage(Object)
Choose image from album or camera.

```uts
uni.chooseImage({
  count: 9,
  sizeType: ['original', 'compressed'],
  sourceType: ['album', 'camera'],
  success(res) {
    const tempFilePaths = res.tempFilePaths
    console.log('Selected:', tempFilePaths)
  }
})
```

### uni.previewImage(Object)
Preview images full screen.

```uts
uni.previewImage({
  current: 0,
  urls: ['https://example.com/1.jpg', 'https://example.com/2.jpg']
})
```

### uni.getImageInfo(Object)
Get image dimensions and path.

```uts
uni.getImageInfo({
  src: '/static/image.png',
  success(res) {
    console.log('Width:', res.width, 'Height:', res.height)
  }
})
```

### uni.chooseVideo(Object)
Choose video from album or camera.

```uts
uni.chooseVideo({
  sourceType: ['album', 'camera'],
  maxDuration: 60,
  camera: 'back',
  success(res) {
    console.log('Video:', res.tempFilePath)
    console.log('Duration:', res.duration, 'seconds')
    console.log('Size:', res.size, 'bytes')
  }
})
```

### uni.compressImage(Object)
Compress image.

```uts
uni.compressImage({
  src: '/tmp/image.png',
  quality: 80,
  success(res) {
    console.log('Compressed:', res.tempFilePath)
  }
})
```

## Location APIs

### uni.getLocation(Object)
Get current location.

```uts
uni.getLocation({
  type: 'gcj02',  // wgs84 / gcj02
  altitude: true,
  success(res) {
    console.log('Latitude:', res.latitude)
    console.log('Longitude:', res.longitude)
    console.log('Accuracy:', res.accuracy)
    console.log('Altitude:', res.altitude)
  }
})
```

### uni.openLocation(Object)
Open map with location marker.

```uts
uni.openLocation({
  latitude: 39.908823,
  longitude: 116.397470,
  name: 'Tiananmen Square',
  address: 'Beijing, China',
  scale: 15
})
```

### uni.onLocationChange / uni.offLocationChange
Real-time location monitoring.

```uts
uni.onLocationChange((res) => {
  console.log('Location update:', res.latitude, res.longitude)
})

// Stop monitoring
uni.offLocationChange()
```

## Device APIs

### uni.getSystemInfoSync()
Get device and system information synchronously.

```uts
const info = uni.getSystemInfoSync()
console.log('Brand:', info.deviceBrand)       // Apple, Huawei, etc.
console.log('Model:', info.deviceModel)       // iPhone 15, etc.
console.log('Platform:', info.platform)       // android, ios, devtools
console.log('System:', info.osName)           // Android, iOS
console.log('Version:', info.osVersion)       // 17.0
console.log('SDK Version:', info.sdkVersion)
console.log('App Version:', info.appVersion)
console.log('Status Bar Height:', info.statusBarHeight)
console.log('Window Width:', info.windowWidth)
console.log('Window Height:', info.windowHeight)
console.log('Safe Area:', info.safeArea)
console.log('Pixel Ratio:', info.devicePixelRatio)
```

### uni.getDeviceInfo()
Get device information.

```uts
const deviceInfo = uni.getDeviceInfo()
console.log('Device Brand:', deviceInfo.deviceBrand)
console.log('Device Model:', deviceInfo.deviceModel)
console.log('Device Type:', deviceInfo.deviceType)  // phone / tablet / pc
```

### uni.getWindowInfo()
Get window information.

```uts
const windowInfo = uni.getWindowInfo()
console.log('Window Width:', windowInfo.windowWidth)
console.log('Window Height:', windowInfo.windowHeight)
console.log('Status Bar Height:', windowInfo.statusBarHeight)
console.log('Safe Area:', windowInfo.safeArea)
console.log('Pixel Ratio:', windowInfo.pixelRatio)
```

### uni.getAppBaseInfo()
Get app base information.

```uts
const appInfo = uni.getAppBaseInfo()
console.log('App Version:', appInfo.appVersion)
console.log('Language:', appInfo.language)
console.log('Theme:', appInfo.theme)  // light / dark
```

### uni.getNetworkType(Object)
Get current network type.

```uts
uni.getNetworkType({
  success(res) {
    console.log('Network:', res.networkType)  // wifi / 2g / 3g / 4g / 5g / unknown / none
  }
})
```

### uni.onNetworkStatusChange(Callback)
Monitor network status changes.

```uts
uni.onNetworkStatusChange((res) => {
  console.log('Connected:', res.isConnected)
  console.log('Type:', res.networkType)
})
```

### uni.makePhoneCall(Object)
Make phone call.

```uts
uni.makePhoneCall({
  phoneNumber: '10086'
})
```

### uni.vibrateShort / uni.vibrateLong
Vibrate device.

```uts
uni.vibrateShort({ type: 'heavy' })  // heavy / medium / light
uni.vibrateLong()
```

### uni.setClipboardData / uni.getClipboardData
Clipboard operations.

```uts
uni.setClipboardData({
  data: 'Hello World',
  showToast: true
})

uni.getClipboardData({
  success(res) { console.log(res.data) }
})
```

### uni.scanCode(Object)
Scan QR code / barcode.

```uts
uni.scanCode({
  onlyFromCamera: true,
  scanType: ['qrCode', 'barCode'],
  success(res) {
    console.log('Result:', res.result)
    console.log('Type:', res.scanType)
  }
})
```

### uni.setScreenBrightness / uni.getScreenBrightness
Screen brightness control.

```uts
uni.setScreenBrightness({ value: 0.8 })
uni.getScreenBrightness({ success(res) { console.log(res.value) } })
```

### uni.setKeepScreenOn
Prevent screen from sleeping.

```uts
uni.setKeepScreenOn({ keepScreenOn: true })
```

## File APIs

### uni.getFileSystemManager()
Get file system manager.

```uts
const fs = uni.getFileSystemManager()

// Read file
fs.readFile({
  filePath: '/static/data.json',
  encoding: 'utf-8',
  success(res) { console.log(res.data) }
})

// Write file
fs.writeFile({
  filePath: `${wx.env.USER_DATA_PATH}/test.txt`,
  data: 'Hello World',
  encoding: 'utf-8',
  success() { console.log('Written') }
})

// Check if file exists
fs.access({
  path: '/static/data.json',
  success() { console.log('Exists') },
  fail() { console.log('Not found') }
})

// Read directory
fs.readdir({
  dirPath: '/static/',
  success(res) { console.log(res.files) }
})

// Get file info
fs.stat({
  path: '/static/data.json',
  success(res) { console.log('Size:', res.stats.size) }
})
```

### uni.saveFile / uni.getSavedFileList / uni.removeSavedFile
Save/manage persistent files.

```uts
uni.saveFile({
  tempFilePath: '/tmp/download.pdf',
  success(res) { console.log('Saved:', res.savedFilePath) }
})
```

## Animation APIs

### uni.createAnimation(Object)
Create animation instance.

```uts
const animation = uni.createAnimation({
  duration: 400,
  timingFunction: 'ease-out',
  delay: 0,
  transformOrigin: '50% 50% 0'
})

// Chain animations
animation.opacity(0).scale(0.5).step()
animation.opacity(1).scale(1).step()

// Apply to data
this.animationData = animation.export()
```

**Animation methods:**
- `opacity(value)` - Set opacity
- `scale(sx, sy?)` - Scale
- `rotate(angle)` - Rotate (degrees)
- `translate(tx, ty?)` - Translate
- `skew(ax, ay?)` - Skew
- `rotate3d(x, y, z, angle)` - 3D rotate
- `step(options?)` - Complete animation step

## Event Bus

### uni.$on / uni.$emit / uni.$off
Global event bus for cross-component communication.

```uts
// Subscribe to event
uni.$on('user-login', (data) => {
  console.log('User logged in:', data)
})

// Emit event
uni.$emit('user-login', { userId: '123', name: 'Alice' })

// Unsubscribe
uni.$off('user-login')

// One-time subscription
uni.$once('user-login', (data) => {
  console.log('First login:', data)
})
```

## Interceptor APIs

### uni.addInterceptor / uni.removeInterceptor
Intercept API calls.

```uts
// Add request interceptor
uni.addInterceptor('request', {
  invoke(args) {
    // Before request
    args.header = args.header || {}
    args.header['Authorization'] = `Bearer ${getToken()}`
    console.log('Request:', args.url)
  },
  success(res) {
    console.log('Response:', res.statusCode)
  },
  fail(err) {
    console.error('Request failed:', err)
  },
  complete() {
    console.log('Request complete')
  }
})

// Remove interceptor
uni.removeInterceptor('request')
```

## Page APIs

### uni.$setPageStyle
Dynamically modify page style.

```uts
uni.$setPageStyle({
  style: {
    navigationBarTitleText: 'New Title',
    navigationBarBackgroundColor: '#FF0000'
  }
})
```

## DOM APIs

### uni.getElementById
Get DOM element by ID.

```uts
const element = uni.getElementById("myView")
if (element !== null) {
  element.style.setProperty("background-color", "red")
}
```

### uni.createSelectorQuery
Query element information after layout.

```uts
uni.createSelectorQuery().select('.my-class').boundingClientRect((rect) => {
  console.log('Element position:', rect)
}).exec()
```

### uni.createIntersectionObserver
Observe element visibility.

```uts
const observer = uni.createIntersectionObserver(this, { thresholds: [0.5] })
observer.relativeToViewport().observe('.target', (res) => {
  console.log('Visibility ratio:', res.intersectionRatio)
  if (res.intersectionRatio > 0.5) {
    console.log('Element is visible')
  }
})
```

## Other Useful APIs

### uni.openLocation(Object)
Open map with location.

### uni.onAccelerometerChange / uni.startAccelerometer / uni.stopAccelerometer
Accelerometer.

### uni.onCompassChange / uni.startCompass / uni.stopCompass
Compass.

### uni.onGyroscopeChange / uni.startGyroscope / uni.stopGyroscope
Gyroscope.

### uni.createOffscreenCanvas(Object)
Create offscreen canvas.

### uni.getEnterOptionsSync()
Get app launch options.

### uni.onAppShow / uni.onAppHide
App show/hide lifecycle.

### uni.exit(Object)
Exit app (Android only).

### uni.report(Object)
Statistical event reporting.

```uts
uni.report({
  name: 'event-name',
  options: { key: 'value' },
  success(res) { console.log(res) },
  fail(err) { console.error(err) }
})
```
