# UTS Language Reference (Uni Type Script)

## Overview

UTS (Uni Type Script) is the primary development language for uni-app x. It is a TypeScript-like language that compiles to different targets:
- **Web**: Compiles to JavaScript
- **Android**: Compiles to Kotlin
- **iOS**: Compiles to Swift
- **HarmonyOS**: Compiles to ArkTS

UTS is stricter than JavaScript/TypeScript and provides type safety while maintaining a familiar syntax for web developers. It uses **nominal typing** (type compatibility based on explicit declarations), not structural typing like TypeScript.

## Basic Types

### Primitive Types
```uts
// Boolean
let isDone: boolean = false

// Number (cross-platform number type)
let count: number = 42
let price: number = 9.99

// String
let name: string = "uni-app"
let greeting: string = `Hello, ${name}!`

// Null (NOT undefined - undefined is not supported in UTS)
let n: null = null
```

### Platform-Specific Number Types
On Android/iOS, you can use platform-specific number types via conditional compilation:

```uts
// #ifdef APP-ANDROID
let intVal: Int = 42
let longVal: Long = 42L
let doubleVal: Double = 3.14
// #endif

// #ifdef APP-IOS
let intVal: Int = 42
let doubleVal: Double = 3.14
// #endif
```

### Special String Types (Type Aliases)
UTS provides type aliases for string values with specific semantic meanings:

| Type Alias | Description | Example |
|:-|:-|:-|
| string.ClassString | CSS class name string | hover-class value |
| string.ColorString | CSS color string | "#ff0000", "red" |
| string.ImageURIString | Image resource URI | src of image |
| string.VideoURIString | Video resource URI | src of video |
| string.HTMLURIString | HTML page URI | src of web-view |
| string.PageURIString | Page path URI | url of navigator |
| string.IDString | Element ID string | id attribute |

### Array Types
```uts
// Array declaration
let numbers: number[] = [1, 2, 3, 4, 5]
let names: Array<string> = ["Alice", "Bob", "Charlie"]

// Array operations
numbers.push(6)           // Add element
numbers.pop()             // Remove last
numbers.length            // Get length
numbers.indexOf(3)        // Find index
numbers.splice(0, 1)      // Remove at index

// IMPORTANT: Array index out of bounds throws exception on native!
// Always check bounds before accessing
let index = 10
if (index >= 0 && index < numbers.length) {
  console.log(numbers[index])
}
```

### Map and Set
```uts
// Map
let userMap = new Map<string, number>()
userMap.set("Alice", 25)
userMap.set("Bob", 30)
console.log(userMap.get("Alice"))  // 25
console.log(userMap.has("Bob"))    // true
userMap.delete("Bob")

// Set
let uniqueIds = new Set<string>()
uniqueIds.add("id1")
uniqueIds.add("id2")
uniqueIds.add("id1")  // Duplicate, ignored
console.log(uniqueIds.size)  // 2
```

### UTSJSONObject
```uts
// UTSJSONObject is the cross-platform JSON object type
let obj = new UTSJSONObject()
obj["name"] = "Alice"
obj["age"] = 25

// Parse JSON string
const data = JSON.parse('{"name":"Bob","age":30}') as UTSJSONObject
console.log(data["name"])  // "Bob"

// Stringify
const jsonStr = JSON.stringify(data)
```

## Type Definitions

### type (Preferred for Object Types)
```uts
// Always use type for object shapes
type UserInfo = {
  name: string
  age: number
  avatar?: string           // Optional property
  address: string | null    // Nullable property
}

// Union types
type Status = 'loading' | 'success' | 'error'
type Result = SuccessResult | ErrorResult

// Intersection types
type Employee = UserInfo & {
  department: string
  salary: number
}
```

### Enum
```uts
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT"
}

let dir: Direction = Direction.Up

// Numeric enum
enum HttpStatus {
  OK = 200,
  NotFound = 404,
  ServerError = 500
}
```

### Generic Types
```uts
// Generic function
function getFirst<T>(arr: T[]): T | null {
  if (arr.length > 0) {
    return arr[0]
  }
  return null
}

// Generic type
type ApiResponse<T> = {
  code: number
  message: string
  data: T | null
}

// Generic class
class DataStore<T> {
  private items: T[] = []
  
  add(item: T): void {
    this.items.push(item)
  }
  
  get(index: number): T | null {
    if (index >= 0 && index < this.items.length) {
      return this.items[index]
    }
    return null
  }
  
  getAll(): T[] {
    return [...this.items]
  }
}
```

## Classes

```uts
class Animal {
  // Properties (must be initialized or declared with type)
  name: string
  age: number
  
  // Constructor
  constructor(name: string, age: number) {
    this.name = name
    this.age = age
  }
  
  // Method
  speak(): string {
    return `${this.name} says hello`
  }
  
  // Static method
  static create(name: string): Animal {
    return new Animal(name, 0)
  }
}

// Inheritance
class Dog extends Animal {
  breed: string
  
  constructor(name: string, age: number, breed: string) {
    super(name, age)
    this.breed = breed
  }
  
  // Override method
  speak(): string {
    return `${this.name} barks!`
  }
  
  // New method
  fetch(item: string): string {
    return `${this.name} fetches ${item}`
  }
}
```

## Null Safety

```uts
// Nullable type
let name: string | null = null

// Safe access with ?.
let length = name?.length  // Returns number | null

// Null coalescing
let displayName = name ?? "Unknown"

// Non-null assertion (use carefully!)
let definiteName = name!  // Throws if null

// Safe call pattern
function processName(name: string | null): string {
  if (name !== null) {
    return name.toUpperCase()  // TypeScript-style narrowing
  }
  return "UNKNOWN"
}
```

## Conditional Compilation in UTS

```uts
// #ifdef APP-ANDROID
import Build from 'android.os.Build'
console.log(Build.MODEL)
// #endif

// #ifdef APP-IOS
import UIKit from 'UIKit'
console.log(UIDevice.current.model)
// #endif

// #ifndef APP-PLUS
// Code for all platforms except native app
console.log("Web or Mini Program")
// #endif
```

## Native API Access

### Android
```uts
// Import Android classes
import Build from 'android.os.Build'
import Context from 'android.content.Context'
import Toast from 'android.widget.Toast'
import Uri from 'android.net.Uri'

// Use Android APIs
function getDeviceModel(): string {
  return Build.MODEL
}

function makePhoneCall(phoneNumber: string): void {
  const intent = new Intent(Intent.ACTION_DIAL)
  intent.setData(Uri.parse("tel:" + phoneNumber))
  startActivity(intent)
}
```

### iOS
```uts
// Import iOS frameworks
import UIKit from 'UIKit'
import Foundation from 'Foundation'

// Use iOS APIs
function getDeviceModel(): string {
  return UIDevice.currentDevice.model
}
```

### HarmonyOS
```uts
// Import HarmonyOS modules
// #ifdef APP-HARMONY
import deviceInfo from '@ohos.deviceInfo'
// #endif
```

## Import Differences: Kotlin/Swift vs UTS

| Kotlin | UTS |
|:-|:-|
| `import android.os.Build` | `import Build from 'android.os.Build'` |
| `fun getDeviceModel(): String` | `function getDeviceModel(): string` |
| `val` | `const` |
| `var` | `let` |
| `fun` | `function` |
| `: String` (uppercase) | `: string` (lowercase) |
| `null` | `null` (same) |
| `!!` (non-null assertion) | `!` (non-null assertion) |
| `as` (cast) | `as` (cast, same) |

## Common Patterns

### Async Operations
```uts
async function loadData(): Promise<void> {
  try {
    const res = await uni.request({
      url: 'https://api.example.com/data',
      method: 'GET'
    })
    items.value = res.data as ItemType[]
  } catch (e) {
    console.error(e)
    uni.showToast({ title: 'Load failed', icon: 'error' })
  }
}
```

### Event Handling
```uts
function onItemClick(item: ItemType): void {
  uni.navigateTo({
    url: `/pages/detail/detail?id=${item.id}`
  })
}

function onInputChange(e: UniInputEvent): void {
  const value = e.detail.value
  searchQuery.value = value
}
```

### Reactive Data with Type Safety
```uts
type State = {
  list: ItemType[]
  loading: boolean
  error: string | null
}

const state = reactive<State>({
  list: [],
  loading: false,
  error: null
})
```

### State Management Module
```uts
// store/index.uts
export type State = {
  globalNum: number
  userInfo: UserInfo | null
  token: string
}

export const state = reactive({
  globalNum: 0,
  userInfo: null as UserInfo | null,
  token: ''
} as State)

export const setGlobalNum = (num: number): void => {
  state.globalNum = num
}

export const setUserInfo = (info: UserInfo | null): void => {
  state.userInfo = info
}

export const setToken = (newToken: string): void => {
  state.token = newToken
}
```

### Using State in Pages
```vue
<script setup lang="uts">
import { state, setGlobalNum } from '@/store/index.uts'

// Computed from global state
const globalNum = computed(() => state.globalNum)

const plus = () => {
  setGlobalNum(state.globalNum + 1)
}
</script>
```

## Important Restrictions

1. **No undefined** - Use `null` instead
2. **No structural typing** - Use explicit type relationships
3. **No dynamic property access** - `obj[variable]` not allowed, use Maps
4. **No eval() or new Function()** - Not supported for security
5. **No prototype chain** - Classes are compiled to native classes
6. **No variable hoisting** - Declare before use
7. **No Symbol type** - Not supported
8. **No generators** - `function*` and `yield` not supported
9. **No as const** - Use explicit type annotations
10. **No interface merging** - Each interface is independent
11. **No typeof type guard** - Use `instanceof` instead
12. **No delete operator** - Set to null instead
13. **No labeled statements** - No labeled break/continue
14. **Array bounds checking** - Out-of-bounds access throws exception
15. **Strict null checks** - Must handle nullable types explicitly
16. **No function overloading** - Use different names or generics
17. **No with statement** - Not supported
18. **No destructuring defaults in params** - Use null coalescing

See `uts-ts-differences.md` for complete migration guide with error codes.
