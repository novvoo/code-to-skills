# UTS vs TypeScript Differences Reference

## Overview

UTS (Uni Type Script) is a strongly-typed language that compiles to different targets (JavaScript, Kotlin, Swift, ArkTS). While it adopts TypeScript-like syntax, it has significant constraints to ensure cross-platform compatibility and native performance.

**Key Principle:** UTS uses nominal typing (type compatibility based on explicit declarations), not structural typing (type compatibility based on shape) like TypeScript.

## Critical Differences

### 1. No undefined - Use null Instead

**Error Code:** UTS110111119

UTS does not support `undefined`. All variables must be initialized before use. Use `null` for absent values.

```ts
// TypeScript - OK
let name: string | undefined
let age: number  // implicitly undefined

// UTS - ERROR
let name: string | undefined  // Error!
let age: number  // Error: must initialize

// UTS - Correct
let name: string | null = null
let age: number = 0
```

### 2. No Structural Typing - Use Explicit type/extends

**Error Code:** UTS110111120

Even if two types have identical structure, they cannot be assigned to each other without explicit relationship.

```ts
// TypeScript - OK (structural typing)
type Point2D = { x: number; y: number }
type Point3D = { x: number; y: number; z: number }
const p2: Point2D = { x: 1, y: 2 } as Point3D  // OK in TS

// UTS - ERROR (nominal typing)
type Point2D = { x: number; y: number }
type Point3D = { x: number; y: number; z: number }
const p2: Point2D = { x: 1, y: 2 } as Point3D  // Error!

// UTS - Correct: Use extends
type Point2D = { x: number; y: number }
type Point3D = Point2D & { z: number }
const p3: Point3D = { x: 1, y: 2, z: 3 }
const p2: Point2D = p3  // OK, Point3D extends Point2D
```

### 3. Use type Instead of interface for Object Types

**Error Code:** UTS110111121

In UTS, prefer `type` over `interface` for defining object shapes. `interface` has limitations in UTS.

```uts
// Preferred
type UserInfo = {
  name: string
  age: number
  avatar?: string  // Optional property
}

// Less preferred (limited support)
interface IUserInfo {
  name: string
  age: number
}
```

### 4. No Variable Hoisting

**Error Code:** UTS110111122

All variables and functions must be declared before use. No hoisting like JavaScript.

```ts
// JavaScript - OK (hoisting)
console.log(myVar)  // undefined
var myVar = 5

// UTS - ERROR
console.log(myVar)  // Error: not defined
let myVar = 5

// UTS - Correct
let myVar = 5
console.log(myVar)
```

### 5. No Dynamic Property Access

**Error Code:** UTS110111123

Cannot use variable as property key: `obj[variable]`. Use Map instead.

```ts
// TypeScript - OK
const key = "name"
const obj = { name: "Alice", age: 25 }
console.log(obj[key])  // "Alice"

// UTS - ERROR
const key = "name"
const obj = { name: "Alice", age: 25 }
console.log(obj[key])  // Error!

// UTS - Correct: Use Map
const map = new Map<string, any>()
map.set("name", "Alice")
map.set("age", 25)
console.log(map.get("name"))  // "Alice"
```

### 6. No eval() or new Function()

**Error Code:** UTS110111124

Dynamic code execution is not supported for security and performance.

### 7. No Prototype Manipulation

**Error Code:** UTS110111159

UTS has no prototype concept. Cannot assign to prototype.

```ts
// TypeScript - OK
function Person(name) { this.name = name }
Person.prototype.greet = function() { return "Hi " + this.name }

// UTS - Correct: Use class
class Person {
  name: string = ""
  constructor(name: string) { this.name = name }
  greet(): string { return "Hi " + this.name }
}
```

### 8. No with Statement

**Error Code:** UTS110111125

The `with` statement is not supported.

### 9. No Labeled Statements

**Error Code:** UTS110111126

Labeled `break` and `continue` are not supported.

### 10. No delete Operator

**Error Code:** UTS110111127

Cannot delete object properties. Set to null instead.

### 11. Strict null Checks

**Error Code:** UTS110111128

Nullable types must be explicitly handled.

```uts
let name: string | null = getName()
// Must check null before use
if (name !== null) {
  console.log(name.length)  // OK
}
// Or use null coalescing
const length = name?.length ?? 0
```

### 12. No as const Assertions

**Error Code:** UTS110111129

`as const` is not supported. Use explicit type annotations.

### 13. No Namespace Merging

**Error Code:** UTS110111130

Cannot merge namespace declarations.

### 14. No Function Overloading by Type

**Error Code:** UTS110111131

Unlike TypeScript, UTS does not support function overloading with different parameter types.

```ts
// TypeScript - OK
function add(a: number, b: number): number
function add(a: string, b: string): string
function add(a: any, b: any): any { return a + b }

// UTS - Use different function names or union types
function addNumbers(a: number, b: number): number { return a + b }
function addStrings(a: string, b: string): string { return a + b }
// Or use generic
function add<T>(a: T, b: T): T { return a + b as T }
```

### 15. No typeof Operator for Type Guards

**Error Code:** UTS110111132

Use `instanceof` or `isinstanceof()` instead.

### 16. No Symbol Type

**Error Code:** UTS110111133

Symbol is not supported in UTS.

### 17. No Iterator/Generator

**Error Code:** UTS110111134

`function*` and `yield` are not supported.

### 18. No Destructuring with Default Values in Function Parameters

```uts
// TypeScript - OK
function greet({ name = "World", age = 0 }: { name?: string; age?: number }) {}

// UTS - Use explicit defaults
function greet(options: { name?: string; age?: number }) {
  const name = options.name ?? "World"
  const age = options.age ?? 0
}
```

### 19. Array Index Out of Bounds Throws Exception

```uts
const arr: number[] = [1, 2, 3]
console.log(arr[5])  // Throws IndexOutOfBoundsException on Android/iOS

// Correct: Check bounds first
let index = 5
if (index >= 0 && index < arr.length) {
  console.log(arr[index])
} else {
  console.log("Index out of bounds")
}
```

### 20. No Implicit any

All types must be explicitly declared. No implicit `any` type.

## Type System Summary

| Feature | TypeScript | UTS |
|:-|:-|:-|
| Structural typing | Yes | No (nominal typing) |
| undefined | Yes | No (use null) |
| Variable hoisting | Yes | No |
| Dynamic property access | Yes | No (use Map) |
| eval() | Yes | No |
| Prototype | Yes | No |
| as const | Yes | No |
| typeof type guard | Yes | No (use instanceof) |
| Symbol | Yes | No |
| Generator | Yes | No |
| Function overloading | Yes | Limited |
| Interface merging | Yes | No |
| delete operator | Yes | No |
| Labeled statements | Yes | No |

## Migration Checklist

When converting TypeScript code to UTS:

- [ ] Replace all `undefined` with `null`
- [ ] Add explicit type annotations everywhere
- [ ] Replace `interface` with `type` for object shapes
- [ ] Replace `obj[dynamicKey]` with `Map.get(key)`
- [ ] Remove `eval()` and `new Function()`
- [ ] Convert prototype code to classes
- [ ] Remove `as const` assertions
- [ ] Replace `typeof` checks with `instanceof`
- [ ] Add null checks for all nullable values
- [ ] Initialize all variables at declaration
- [ ] Replace destructuring defaults with null coalescing
- [ ] Add array bounds checking
- [ ] Remove generator functions
- [ ] Remove labeled break/continue
- [ ] Remove delete operator (set to null instead)
