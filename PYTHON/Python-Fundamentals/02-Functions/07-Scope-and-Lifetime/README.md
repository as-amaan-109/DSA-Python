# Scope and Lifetime in Python

**Part 2: Python Fundamentals**  
**Section: 02 – Functions**  
**Topic: 07 – Scope and Lifetime**

---

# 1. Introduction

In Python, scope determines where a variable can be accessed in a program, while lifetime determines how long that variable or its associated object remains available.

When we create variables inside functions, outside functions, or inside nested functions, their accessibility can be different.

Understanding scope and lifetime is important because it helps us:

- Avoid variable naming conflicts.
- Understand local and global variables.
- Share information between functions.
- Modify variables from different scopes.
- Understand nested functions.
- Create closures.
- Write cleaner and more maintainable programs.

### Example

```python
message = "Global Message"

def display_message():
    local_message = "Local Message"

    print(message)
    print(local_message)

display_message()
```

**Output:**

```text
Global Message
Local Message
```

Here:

- `message` is a global variable.
- `local_message` is a local variable.
- Both variables can be accessed inside the function.

However, `local_message` cannot normally be accessed directly outside `display_message()`.

## Learning Objectives

After completing this topic, you should be able to:

1. Understand variable scope.
2. Understand variable lifetime.
3. Identify local variables.
4. Identify global variables.
5. Understand enclosing scope.
6. Understand built-in scope.
7. Apply the LEGB rule.
8. Use the `global` keyword.
9. Use the `nonlocal` keyword.
10. Understand variable shadowing.
11. Understand nested functions.
12. Create and use closures.
13. Understand how mutable global objects behave.
14. Solve practical programming problems using scope concepts.

---

# 2. What Is Scope in Python?

Scope is the region of a program where a variable or name can be accessed.

Python has four main levels of name lookup:

1. Local Scope
2. Enclosing Scope
3. Global Scope
4. Built-in Scope

These four levels form the **LEGB rule**.

### Example

```python
name = "Global Name"

def display():
    name = "Local Name"
    print(name)

display()

print(name)
```

**Output:**

```text
Local Name
Global Name
```

### Explanation

Inside the function, Python finds the local variable first.

Outside the function, Python accesses the global variable.

The two variables have the same spelling, but they belong to different scopes.

---

# 3. Local Scope

A variable created inside a function is normally local to that function.

It can be accessed inside the function where it is defined.

### Example

```python
def display_message():
    message = "Hello Python"

    print(message)

display_message()
```

**Output:**

```text
Hello Python
```

### Explanation

- `display_message()` defines a function.
- `message` is created inside that function.
- The variable is accessible inside the function.
- It cannot normally be referenced by that name from outside the function.

### Trying to Access a Local Variable Outside

```python
def display():
    number = 100
    print(number)

display()

# This raises NameError:
# print(number)
```

**Output before the error:**

```text
100
```

The final statement raises a `NameError` because `number` is not defined in the global scope.

### Important Points

- Local variables are defined inside functions.
- They are normally accessible only within their defining function.
- Each function call creates its own local execution context.
- A local variable can have the same name as a global variable.
- A local variable can be returned and used outside its function.

### Returning a Local Value

```python
def get_number():
    number = 500
    return number

result = get_number()

print(result)
```

**Output:**

```text
500
```

The local name `number` is not exposed outside the function, but its returned value can be used.

---

# 4. Global Scope

A variable defined at the module level is commonly called a global variable.

It can generally be accessed by functions defined in that module.

### Example

```python
college = "ABC Polytechnic"

def display_college():
    print(college)

display_college()
print(college)
```

**Output:**

```text
ABC Polytechnic
ABC Polytechnic
```

### Explanation

- `college` is defined outside the function.
- It belongs to the module's global scope.
- The function can read it without a special declaration.
- The global name can also be accessed directly outside the function.

### Important Points

- Global variables are defined at module level.
- Functions can read global variables.
- Reassigning a global name inside a function requires a `global` declaration.
- Global state should be used carefully because many parts of a program may depend on it.

---

# 5. Local Variables vs Global Variables

| Feature | Local Variable | Global Variable |
|---|---|---|
| Definition | Inside a function | At module level |
| Accessibility | Within its local scope | Throughout the module, subject to name resolution |
| Reassignment | Local function assignment | Requires `global` inside a function |
| Lifetime | Associated with function execution and references | Usually available while the module remains loaded |
| Common use | Temporary calculations | Shared module-level state |

### Example

```python
message = "Global message"

def display():
    local_message = "Local message"

    print(message)
    print(local_message)

display()
```

**Output:**

```text
Global message
Local message
```

Both types of variables can be used inside a function, but they have different scopes.

---

# 6. Variable Shadowing

Variable shadowing happens when a local name has the same identifier as a name in an outer scope.

The local name takes precedence when Python looks up that name inside the local function.

### Example

```python
theme = "light"

def change_theme():
    theme = "dark"
    print("Local theme:", theme)

change_theme()

print("Global theme:", theme)
```

**Output:**

```text
Local theme: dark
Global theme: light
```

### Explanation

1. The global variable `theme` contains `"light"`.
2. The function creates its own local variable named `theme`.
3. Inside the function, Python finds the local variable first.
4. The global variable remains unchanged.

### Important Point

Creating a local variable with the same name does not automatically modify the global variable.

---

# 7. The global Keyword

The `global` keyword allows a function to refer to and reassign a name in the module's global scope.

### Syntax

```python
def function_name():
    global variable_name

    variable_name = new_value
```

### Example

```python
counter = 0

def increment():
    global counter

    counter += 1

increment()
increment()

print(counter)
```

**Output:**

```text
2
```

### Explanation

- `counter` is defined at module level.
- `global counter` tells Python that assignments to this name refer to the module-level binding.
- Each function call increases the global counter.

### Without the global Keyword

```python
counter = 0

def increment():
    counter = counter + 1
```

Calling `increment()` raises an `UnboundLocalError`.

Why?

Python treats `counter` as local because the function assigns to that name. The local variable is read before it has been assigned.

### Correct Version

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()

print(counter)
```

**Output:**

```text
1
```

### When Should You Use global?

Use `global` when a function genuinely needs to reassign a module-level variable.

However, prefer returning values or using an object with clearly controlled state when possible.

---

# 8. The Enclosing Scope

Enclosing scope exists when one function is defined inside another function.

The inner function can generally read variables defined in its enclosing function.

### Example

```python
def outer_function():
    message = "Message from outer function"

    def inner_function():
        print(message)

    inner_function()

outer_function()
```

**Output:**

```text
Message from outer function
```

### Explanation

- `outer_function()` is the outer function.
- `inner_function()` is nested inside it.
- `message` belongs to the enclosing function.
- The inner function can access it.

### Important Points

- Enclosing scope occurs with nested functions.
- Inner functions can read names from their enclosing functions.
- The enclosing function's variable does not automatically become global.
- The `nonlocal` keyword is used when an inner function needs to reassign an existing enclosing binding.

---

# 9. The nonlocal Keyword

The `nonlocal` keyword allows an inner function to reassign a variable from an enclosing function scope.

It does not refer to the module-level global scope.

### Syntax

```python
def outer_function():
    value = 10

    def inner_function():
        nonlocal value
        value = 20

    inner_function()

    return value
```

### Example

```python
def outer_function():
    counter = 0

    def inner_function():
        nonlocal counter

        counter += 1

    inner_function()
    inner_function()

    return counter

print(outer_function())
```

**Output:**

```text
2
```

### Explanation

1. The outer function creates `counter`.
2. The inner function declares `nonlocal counter`.
3. The inner function updates the enclosing variable.
4. The outer function returns the updated value.

### Important Rules

- `nonlocal` is used inside nested functions.
- The referenced name must already exist in an enclosing function scope.
- It cannot be used to reassign a module-level global variable.
- It changes an existing enclosing binding rather than creating a new local binding for that name.

### global vs nonlocal

| Feature | global | nonlocal |
|---|---|---|
| Refers to | Module-level name | Enclosing function name |
| Used inside | Function | Nested function |
| Reassigns | Global binding | Enclosing binding |
| Requires enclosing function variable | No | Yes |
| Typical use | Shared module state | Nested function state |

---

# 10. Understanding the LEGB Rule

Python uses the LEGB rule to resolve names.

LEGB means:

- L – Local
- E – Enclosing
- G – Global
- B – Built-in

Python searches for a name in this order.

### 10.1 Local Scope

Python first searches inside the current function.

```python
def display():
    message = "Local"

    print(message)

display()
```

### 10.2 Enclosing Scope

If the name is not local, Python searches the enclosing function scopes.

```python
def outer():
    message = "Enclosing"

    def inner():
        print(message)

    inner()

outer()
```

### 10.3 Global Scope

If the name is not found locally or in enclosing scopes, Python searches the module's global namespace.

```python
message = "Global"

def display():
    print(message)

display()
```

### 10.4 Built-in Scope

Finally, Python checks built-in names such as:

- `print()`
- `len()`
- `sum()`
- `max()`
- `min()`
- `range()`

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

**Output:**

```text
3
```

Python finds `len()` in the built-in namespace.

### LEGB Summary

| Order | Scope | Example |
|---|---|---|
| 1 | Local | Variable inside current function |
| 2 | Enclosing | Variable inside outer function |
| 3 | Global | Variable at module level |
| 4 | Built-in | `print()`, `len()`, `sum()` |

---

# 11. Variable Lifetime

Variable lifetime describes how long a variable binding or the object it references remains available.

### Local Variables

Local variables are created during function execution.

When the function returns, its local execution frame normally becomes eligible for cleanup.

However, objects referenced by that frame may remain alive if another reference still exists.

### Example

```python
def calculate():
    number = 100
    return number

result = calculate()

print(result)
```

**Output:**

```text
100
```

The local name `number` is not directly accessible outside `calculate()`, but the returned integer is available through `result`.

### Global Variables

Global variables are associated with the module's namespace.

They generally remain available while the module remains loaded and references to their objects are retained.

### Example

```python
college = "ABC Polytechnic"

def display():
    print(college)

display()
print(college)
```

### Variables in Closures

A closure can retain access to variables from an enclosing function even after that enclosing function has returned.

### Example

```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = create_counter()

print(counter())
print(counter())
print(counter())
```

**Output:**

```text
1
2
3
```

The returned inner function retains access to the enclosing `count` binding.

---

# 12. Nested Functions

A nested function is a function defined inside another function.

### Example

```python
def outer_function():
    print("Outer function started")

    def inner_function():
        print("Inner function executed")

    inner_function()

    print("Outer function completed")

outer_function()
```

**Output:**

```text
Outer function started
Inner function executed
Outer function completed
```

### Uses of Nested Functions

- Organizing related logic.
- Restricting helper functions to a specific outer function.
- Creating closures.
- Managing state.
- Hiding implementation details from other parts of a module.

### Important Point

An inner function is not automatically available as a global name.

It is defined in the local namespace of its enclosing function.

---

# 13. Closures in Python

A closure is a function that remembers and retains access to variables from its enclosing scope.

This allows a function to use information from an earlier function call even after the outer function has finished executing.

### Example

```python
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))
```

**Output:**

```text
20
30
```

### Explanation

1. `create_multiplier()` receives a multiplier.
2. It defines the nested function `multiply()`.
3. The nested function refers to `multiplier`.
4. The outer function returns the nested function.
5. The returned function remembers the enclosing variable.

### Why Are Closures Useful?

Closures are useful for:

- Creating function factories.
- Preserving state between function calls.
- Creating reusable configurations.
- Building decorators.
- Creating callbacks.
- Encapsulating related functionality.

### Another Example – Greeting Factory

```python
def create_greeter(prefix):
    def greet(name):
        return f"{prefix}, {name}!"

    return greet


hello = create_greeter("Hello")
welcome = create_greeter("Welcome")

print(hello("Amaan"))
print(welcome("Amaan"))
```

**Output:**

```text
Hello, Amaan!
Welcome, Amaan!
```

---

# 14. Mutable Global Objects

A global variable may refer to a mutable object such as a list or dictionary.

If a function modifies that existing object without rebinding its name, the `global` keyword is generally not required.

### Example

```python
events = []

def add_event(event):
    events.append(event)

add_event("Application started")
add_event("User logged in")

print(events)
```

**Output:**

```text
['Application started', 'User logged in']
```

### Explanation

- `events` is a global name.
- The function accesses the existing list.
- `.append()` mutates that list.
- The function does not reassign the global name `events`.

### Reassignment Requires global

```python
events = []

def replace_events():
    global events

    events = ["New event"]

replace_events()

print(events)
```

**Output:**

```text
['New event']
```

The function assigns a new list to the global name, so the `global` declaration is necessary.

---

# 15. Shadowing Built-in Names

Avoid using built-in function names as variable names.

Incorrect:

```python
list = [10, 20, 30]

# This fails because list now refers to a list object:
# numbers = list((1, 2, 3))
```

The global name `list` shadows the built-in `list()` constructor.

Correct:

```python
numbers = [10, 20, 30]

result = list((1, 2, 3))

print(result)
```

**Output:**

```text
[1, 2, 3]
```

### Common Built-in Names to Avoid

- `list`
- `dict`
- `str`
- `int`
- `float`
- `sum`
- `max`
- `min`
- `input`
- `print`

Using descriptive names makes programs easier to understand and prevents accidental shadowing.

---

# SECTION 1: TWELVE TOPIC EXAMPLES

All examples are included in:

`07_scope_and_lifetime.py`

## Example 01 – Local Scope

**Concept:** A variable defined inside a function.

```python
def display_message():
    local_message = "I am a local variable."

    print(local_message)

display_message()
```

**Output:**

```text
I am a local variable.
```

**Explanation:** `local_message` belongs to the function's local scope and cannot normally be accessed directly outside it.

## Example 02 – Global Scope

**Concept:** Reading a global variable inside a function.

```python
GLOBAL_GREETING = "Hello from global scope"

def display_greeting():
    print(GLOBAL_GREETING)

display_greeting()
```

**Output:**

```text
Hello from global scope
```

**Explanation:** The function reads the module-level variable without needing `global`.

## Example 03 – Variable Shadowing

**Concept:** A local variable with the same name as a global variable takes precedence inside the local scope.

```python
theme = "light"

def display_theme():
    theme = "dark"

    print("Local theme:", theme)

display_theme()

print("Global theme:", theme)
```

**Output:**

```text
Local theme: dark
Global theme: light
```

**Explanation:** The local `theme` shadows the global `theme`; assigning to the local name does not change the global one.

## Example 04 – global Keyword

**Concept:** Reassigning a global variable.

```python
counter = 0

def increment():
    global counter

    counter += 1

increment()
increment()
increment()

print(counter)
```

**Output:**

```text
3
```

**Explanation:** `global counter` tells Python to use the module-level binding when the function assigns to `counter`.

## Example 05 – Function Parameters Are Local

**Concept:** A function parameter behaves as a local name.

```python
name = "Global Name"

def display(name):
    print("Function name:", name)

display("Amaan")

print("Global name:", name)
```

**Output:**

```text
Function name: Amaan
Global name: Global Name
```

**Explanation:** The function parameter `name` is local to the function call and does not reassign the global variable.

## Example 06 – Enclosing Scope

**Concept:** Accessing a variable from an outer function.

```python
def outer_function():
    message = "Message from enclosing scope"

    def inner_function():
        print(message)

    inner_function()

outer_function()
```

**Output:**

```text
Message from enclosing scope
```

**Explanation:** The inner function reads a variable defined in its enclosing function.

## Example 07 – nonlocal Keyword

**Concept:** Reassigning a variable from the enclosing function.

```python
def outer_function():
    counter = 0

    def inner_function():
        nonlocal counter
        counter += 1
        return counter

    print(inner_function())
    print(inner_function())
    print(inner_function())

outer_function()
```

**Output:**

```text
1
2
3
```

**Explanation:** `nonlocal` allows the inner function to update the enclosing function's `counter`.

## Example 08 – LEGB Rule

**Concept:** Understanding local, enclosing, global, and built-in name lookup.

```python
message = "Global value"

def outer_function():
    message = "Enclosing value"

    def inner_function():
        message = "Local value"

        print("Local:", message)

    inner_function()

    print("Enclosing:", message)

outer_function()

print("Global:", message)
print("Built-in:", len([10, 20, 30]))
```

**Output:**

```text
Local: Local value
Enclosing: Enclosing value
Global: Global value
Built-in: 3
```

**Explanation:** Python resolves names using the LEGB order.

## Example 09 – Local Variable Lifetime

**Concept:** Local variables are initialized during function calls.

```python
def counter():
    count = 0
    count += 1

    return count

print(counter())
print(counter())
```

**Output:**

```text
1
1
```

**Explanation:** A fresh local `count` is created on every call. Its previous local value is not retained automatically.

## Example 10 – Closures

**Concept:** A returned function retains access to an enclosing variable.

```python
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))
```

**Output:**

```text
20
30
```

**Explanation:** Each returned function remembers its own enclosing multiplier.

## Example 11 – Mutable Global Object

**Concept:** Modifying an existing global list.

```python
events = []

def add_event(event):
    events.append(event)

add_event("Application started")
add_event("User logged in")

print(events)
```

**Output:**

```text
['Application started', 'User logged in']
```

**Explanation:** Mutating an existing global list does not require rebinding its global name.

## Example 12 – Global Variable Reassignment

**Concept:** Replacing a global value using `global`.

```python
message = "Hello Python"

def update_message():
    global message

    message = "Welcome to Python"

update_message()

print(message)
```

**Output:**

```text
Welcome to Python
```

**Explanation:** The function uses `global` to reassign the module-level `message` variable.

---

# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS

## Problem 01 – Calculate Average Using Local Variables

**Problem Statement:**

Write a function that accepts any number of values and calculates their total, count, and average using local variables.

**Code:**

```python
def calculate_average(*numbers):
    if not numbers:
        return None

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return average


print(calculate_average(10, 20, 30, 40))
```

**Output:**

```text
25.0
```

**Explanation:**

1. The function accepts multiple numbers.
2. `total` stores their sum.
3. `count` stores the number of values.
4. `average` stores the calculated average.
5. The result is returned.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding argument storage.

## Problem 02 – Global Visit Counter

**Problem Statement:**

Create a global counter that increases whenever a visitor is recorded.

**Code:**

```python
visit_count = 0

def record_visit():
    global visit_count

    visit_count += 1

    return visit_count


record_visit()
record_visit()
record_visit()

print("Total visits:", visit_count)
```

**Output:**

```text
Total visits: 3
```

**Explanation:**

The `global` keyword allows the function to update the module-level counter.

**Complexity:**

- Time per call: O(1)
- Auxiliary Space: O(1)

## Problem 03 – Local vs Global Variables

**Problem Statement:**

Create a global variable and a local variable with the same name. Display both values.

**Code:**

```python
message = "Global message"

def compare_messages():
    message = "Local message"

    print("Inside function:", message)

compare_messages()

print("Outside function:", message)
```

**Output:**

```text
Inside function: Local message
Outside function: Global message
```

**Explanation:**

The local variable shadows the global variable inside the function without changing the global binding.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1), excluding string storage.

## Problem 04 – Nonlocal Counter

**Problem Statement:**

Create a counter using a nested function and the `nonlocal` keyword.

**Code:**

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count

        count += 1

        return count

    return increment


counter = make_counter()

print(counter())
print(counter())
print(counter())
```

**Output:**

```text
1
2
3
```

**Explanation:**

The inner function maintains access to the outer function's `count` variable and updates it through `nonlocal`.

**Complexity:**

- Time per increment: O(1)
- Auxiliary Space: O(1)

## Problem 05 – Multiplier Closure

**Problem Statement:**

Create a function that returns another function. The returned function must remember its multiplier.

**Code:**

```python
def make_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply


double = make_multiplier(2)

print(double(10))
print(double(25))
```

**Output:**

```text
20
50
```

**Explanation:**

The nested function retains access to `multiplier` through a closure.

**Complexity:**

- Time per multiplication: O(1), under standard bounded numeric-operation assumptions.
- Auxiliary Space: O(1), excluding the resulting numeric object.

## Problem 06 – Personalized Greeting

**Problem Statement:**

Create a greeting factory that remembers a greeting prefix.

**Code:**

```python
def make_greeter(prefix):
    def greet(name):
        return f"{prefix}, {name}!"

    return greet


welcome = make_greeter("Welcome")

print(welcome("Amaan"))
print(welcome("Rahul"))
```

**Output:**

```text
Welcome, Amaan!
Welcome, Rahul!
```

**Explanation:**

The returned function retains the enclosing `prefix` variable, so the same greeting can be reused.

**Complexity:**

- Time: O(n), where n is the length of the output string.
- Auxiliary Space: O(n), for the generated string.

## Problem 07 – Score Checker Closure

**Problem Statement:**

Create a function that returns a score checker using an enclosing minimum score.

**Code:**

```python
def make_score_checker(minimum_score):
    def is_eligible(score):
        return score >= minimum_score

    return is_eligible


checker = make_score_checker(40)

print(checker(60))
print(checker(30))
```

**Output:**

```text
True
False
```

**Explanation:**

The returned function remembers the minimum score and checks future inputs against it.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1), excluding function object storage.

## Problem 08 – Invoice Calculator Closure

**Problem Statement:**

Create an invoice calculator that remembers a tax rate.

**Code:**

```python
def make_invoice_calculator(tax_rate):
    def calculate_total(amount):
        return amount * (1 + tax_rate / 100)

    return calculate_total


calculator = make_invoice_calculator(18)

print(calculator(1000))
```

**Output:**

```text
1180.0
```

**Explanation:**

The calculator remembers the enclosing tax rate and applies it to the amount.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 09 – Local Configuration

**Problem Statement:**

Create a configuration dictionary using local variables and return it.

**Code:**

```python
def create_configuration(theme, language, notifications):
    settings = {
        "theme": theme,
        "language": language,
        "notifications": notifications
    }

    return settings


result = create_configuration(
    "dark",
    "English",
    True
)

print(result)
```

**Output:**

```text
{
    'theme': 'dark',
    'language': 'English',
    'notifications': True
}
```

**Explanation:**

All configuration parameters and the dictionary are local to the function. The dictionary is returned to the caller.

**Complexity:**

- Time: O(1), for fixed-size fields.
- Auxiliary Space: O(1), excluding string storage.

## Problem 10 – Discount Calculator Closure

**Problem Statement:**

Create a discount calculator that remembers a discount percentage.

**Code:**

```python
def make_discount_calculator(discount_rate):
    def calculate_price(price):
        return price - (price * discount_rate / 100)

    return calculate_price


calculator = make_discount_calculator(20)

print(calculator(1000))
```

**Output:**

```text
800.0
```

**Explanation:**

The enclosing function stores the discount percentage. The returned function uses it whenever a price is supplied.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 11 – Global Event Logger

**Problem Statement:**

Create a global event log and write a function that appends new events to it.

**Code:**

```python
event_log = []

def log_event(event):
    event_log.append(event)

    return len(event_log)


log_event("Application started")
log_event("User logged in")
log_event("Data saved")

print(event_log)
```

**Output:**

```text
['Application started', 'User logged in', 'Data saved']
```

**Explanation:**

The function modifies the existing global list using `.append()`. It does not reassign the global name, so `global` is not required.

**Complexity:**

- Time per append: O(1) amortized.
- Auxiliary Space: O(n), for the stored event references.

## Problem 12 – Accumulator Closure

**Problem Statement:**

Create an accumulator that remembers a running total through a nested function.

**Code:**

```python
def make_accumulator(initial_value=0):
    total = initial_value

    def add(value):
        nonlocal total

        total += value

        return total

    return add


accumulator = make_accumulator(100)

print(accumulator(10))
print(accumulator(20))
print(accumulator(30))
```

**Output:**

```text
110
130
160
```

**Explanation:**

- The outer function creates `total`.
- The inner function accesses and modifies it using `nonlocal`.
- The returned closure preserves the running total between calls.

**Complexity:**

- Time per addition: O(1)
- Auxiliary Space: O(1), excluding the resulting numeric objects.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these problems independently.

## Question 01 – Local Average Calculator

Write a function that uses local variables to calculate the total and average of a student's marks.

Example:

```text
Marks: 80, 90, 70

Expected Total: 240
Expected Average: 80
```

## Question 02 – Global Application Counter

Create a global application counter that increases whenever a function is called.

Display the final count.

## Question 03 – Global and Local Comparison

Create a global variable and a local variable with the same name.

Display both values and explain why they are different.

## Question 04 – Nonlocal Counter

Create a counter using a nested function and `nonlocal`.

The counter should retain its previous value between calls.

## Question 05 – Multiplier Factory

Write a function factory that creates a multiplier function using a closure.

Example:

```text
Multiplier: 5
Input: 10
Expected Output: 50
```

## Question 06 – Custom Greeting

Create a greeting function using a closure that remembers a custom greeting prefix.

## Question 07 – Score Checker

Write a function that remembers a minimum passing score and checks whether supplied marks satisfy it.

## Question 08 – Invoice Calculator

Create an invoice calculator that remembers a tax percentage using a closure.

## Question 09 – Independent Configuration

Write a function that creates and returns an independent configuration dictionary using local variables.

## Question 10 – Running Accumulator

Create an accumulator using `nonlocal` that remembers a running total across multiple calls.

---

# SECTION 4: COMMON MISTAKES

## Mistake 01 – Accessing a Local Variable Outside Its Function

Incorrect:

```python
def display():
    number = 100

display()

# print(number)
```

The variable is local to `display()`.

Correct:

```python
def display():
    number = 100
    return number

result = display()

print(result)
```

## Mistake 02 – Modifying a Global Name Without global

Incorrect:

```python
counter = 0

def increment():
    counter = counter + 1
```

This causes `UnboundLocalError` because the local variable is read before assignment.

Correct:

```python
counter = 0

def increment():
    global counter
    counter += 1
```

## Mistake 03 – Using global Instead of nonlocal

Incorrect:

```python
def outer():
    count = 0

    def inner():
        # global count would refer to module scope,
        # not this enclosing variable.
        pass
```

Correct:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()

    return count
```

## Mistake 04 – Using nonlocal Without an Enclosing Binding

Incorrect:

```python
def outer():
    def inner():
        nonlocal count
```

This causes a `SyntaxError` because there is no existing binding named `count` in an enclosing function scope.

Correct:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()

    return count
```

## Mistake 05 – Assuming Local Variables Automatically Preserve Values

Incorrect expectation:

```python
def counter():
    count = 0
    count += 1
    return count

print(counter())
print(counter())
```

Output:

```text
1
1
```

Each call creates a new local variable.

To preserve state, use a closure or an object.

## Mistake 06 – Shadowing Built-in Names

Incorrect:

```python
list = [1, 2, 3]
```

This shadows the built-in `list` name.

Correct:

```python
numbers = [1, 2, 3]
```

## Mistake 07 – Using global Unnecessarily

A function can modify an existing global list without rebinding its name.

```python
events = []

def add_event(event):
    events.append(event)
```

A `global` declaration is unnecessary in this example.

---

# SECTION 5: BEST PRACTICES

1. Prefer local variables for temporary calculations.
2. Use global variables sparingly.
3. Use `global` only when module-level reassignment is genuinely needed.
4. Use `nonlocal` to manage state in nested functions when appropriate.
5. Avoid shadowing built-in names.
6. Choose descriptive variable names.
7. Keep nested functions focused.
8. Use closures when a function needs to remember configuration or state.
9. Return values instead of relying on unnecessary global variables.
10. Understand that object lifetime depends on references, not just variable scope.
11. Avoid unnecessary shared mutable global state.
12. Document functions that change shared state.

### Recommended Approach

Instead of relying on global state:

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Consider a closure:

```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

The closure keeps the counter's state isolated within its own function object.

---

# SECTION 6: REAL-WORLD APPLICATIONS

## 1. Login Session Management

Closures can preserve information about a session.

## 2. Application Configuration

Functions can remember configuration settings such as theme and language.

## 3. Banking Applications

An account object or closure can retain a balance between operations.

## 4. Shopping Cart

A function or object can retain a running collection of selected products.

## 5. Event Logging

A module-level list or dedicated logger can maintain application events.

## 6. Decorators

Closures are a key concept behind many Python decorators.

## 7. Callback Functions

Closures allow callbacks to remember information from the scope where they were created.

## 8. Factory Functions

A factory function creates customized functions using enclosing variables.

---

# SECTION 7: CONNECTION WITH DSA

Scope and lifetime concepts help when designing algorithms that preserve or share state.

### 1. Recursive Algorithms

Local variables help keep each recursive call's data separate.

### 2. Backtracking

Each function call can have its own local state, while controlled shared state may be maintained when needed.

### 3. Dynamic Programming

A memoization dictionary can be stored in an enclosing scope so repeated calls share cached results.

### 4. Graph Traversal

A visited set can be maintained by an enclosing function or passed explicitly to recursive calls.

### 5. Closures in Algorithms

A closure can hold configuration or reusable state for a search or filtering operation.

### 6. Accumulators

Closures can maintain running totals without a global variable.

**Important:** Scope does not directly determine algorithm complexity. The number of operations and data structures used determine time and space complexity.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

Scope itself does not determine algorithm complexity. The operations performed by functions and closures are what matter.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Read a local variable | O(1) | O(1) |
| Read a global variable | O(1) average | O(1) |
| Update a numeric counter | O(1), under bounded integer assumptions | O(1) |
| Append to a list | O(1) amortized | O(1) auxiliary per append |
| Create a simple closure | O(1) | O(1), for fixed captured variables |
| Call a closure | Depends on its body | Depends on its body |
| Sum n numbers | O(n) | O(1), excluding input storage |
| Store n log events | O(n) overall | O(n) |
| Search n values | O(n) | O(1) for iterative linear search |

Python integers can grow to arbitrary precision, so arithmetic operations may require additional time and storage for very large values.

---

# SECTION 9: MINI PROJECT – USER SESSION AND ACTIVITY TRACKER

## Project Objective

Build a small session tracker using local variables, global variables, nested functions, and closures.

The program should:

- Store application-wide information.
- Create independent user sessions.
- Track actions performed by each user.
- Remember each session's activity count.
- Return session information.
- Display user activity.

### Project Code

```python
from typing import Callable, Dict, Any


APPLICATION_NAME = "Python Learning Portal"
TOTAL_SESSIONS = 0


def create_session(username: str) -> Callable[..., Dict[str, Any]]:
    """Create a user session with private activity state."""

    activities = []
    login_count = 0

    def manage_session(
        action: str,
        *,
        activity: str = ""
    ) -> Dict[str, Any]:
        nonlocal login_count

        login_count += 1

        if action == "record":
            if not activity.strip():
                raise ValueError("Activity cannot be empty.")

            activities.append(activity)

        elif action != "view":
            raise ValueError("Unknown session action.")

        return {
            "application": APPLICATION_NAME,
            "username": username,
            "login_count": login_count,
            "activities": list(activities),
            "total_activities": len(activities)
        }

    return manage_session


def start_application() -> None:
    """Run the session tracking application."""

    global TOTAL_SESSIONS

    print("=" * 45)
    print(APPLICATION_NAME.center(45))
    print("=" * 45)

    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    TOTAL_SESSIONS += 1

    session = create_session(username)

    while True:
        print("\n1. Record activity")
        print("2. View session")
        print("3. Exit session")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                activity = input("Enter activity: ")

                result = session(
                    "record",
                    activity=activity
                )

                print(
                    "Activity recorded:",
                    result["total_activities"]
                )

            elif choice == "2":
                result = session("view")

                print("\n========== SESSION DETAILS ==========")
                print("Application:", result["application"])
                print("Username:", result["username"])
                print("Session operations:", result["login_count"])
                print("Activities:")

                for index, item in enumerate(
                    result["activities"],
                    start=1
                ):
                    print(f"{index}. {item}")

                print(
                    "Total activities:",
                    result["total_activities"]
                )

            elif choice == "3":
                print("Session ended.")
                break

            else:
                print("Invalid choice.")

        except ValueError as error:
            print("Error:", error)

    print("Total sessions created:", TOTAL_SESSIONS)


if __name__ == "__main__":
    start_application()
```

### Sample Input

```text
Enter username: Amaan

1. Record activity
2. View session
3. Exit session

Enter choice: 1
Enter activity: Learned Python functions

Enter choice: 1
Enter activity: Practiced DSA

Enter choice: 2
```

### Sample Output

```text
========== SESSION DETAILS ==========
Application: Python Learning Portal
Username: Amaan
Session operations: 3
Activities:
1. Learned Python functions
2. Practiced DSA
Total activities: 2
```

### Concepts Used

- Global variables.
- Local variables.
- Nested functions.
- Enclosing scope.
- `global` keyword.
- `nonlocal` keyword.
- Closures.
- Mutable objects.
- Function return values.

---

# SECTION 10: 50 VIVA QUESTIONS AND ANSWERS

## Basic Scope Concepts

**Q1. What is scope in Python?**

Ans: Scope defines where a variable or name can be accessed.

**Q2. What is the lifetime of a variable?**

Ans: It describes how long a variable binding or its referenced object remains available.

**Q3. What are the four main scopes in Python's LEGB rule?**

Ans: Local, Enclosing, Global, and Built-in.

**Q4. What is local scope?**

Ans: It is the scope of names defined inside a function.

**Q5. What is global scope?**

Ans: It is the module-level scope.

**Q6. What is enclosing scope?**

Ans: It is the scope of an outer function containing a nested function.

**Q7. What is built-in scope?**

Ans: It contains names provided by Python, such as `print()` and `len()`.

**Q8. What does LEGB stand for?**

Ans: Local, Enclosing, Global, Built-in.

**Q9. Can a function access a global variable?**

Ans: Yes, it can normally read a global variable.

**Q10. Can a local variable be accessed directly outside its function?**

Ans: Normally no.

## global Keyword

**Q11. What is the global keyword?**

Ans: It declares that a name in a function refers to a module-level global binding.

**Q12. Why is global used?**

Ans: It allows a function to reassign a global variable.

**Q13. Is global required to read a global variable?**

Ans: No.

**Q14. What happens if a function reassigns a global variable without global?**

Ans: Python treats the name as local and an attempt to read it before assignment may cause `UnboundLocalError`.

**Q15. Can a function modify a global list without global?**

Ans: Yes, when it mutates the existing list without rebinding the global name.

**Q16. Can global be used to reassign a global integer?**

Ans: Yes.

**Q17. Can a function have more than one global declaration?**

Ans: Yes, although a single declaration is usually clearer.

**Q18. What is global variable shadowing?**

Ans: It occurs when a local variable has the same name as a global variable.

**Q19. Does changing a local shadowing variable change the global variable?**

Ans: No.

**Q20. Should global variables be used everywhere?**

Ans: No. Excessive global state makes programs harder to maintain.

## Enclosing and nonlocal Scope

**Q21. What is the nonlocal keyword?**

Ans: It declares that a name refers to an existing binding in an enclosing function scope.

**Q22. Why is nonlocal used?**

Ans: It allows a nested function to reassign a variable in an outer function.

**Q23. Can nonlocal modify a global variable?**

Ans: No. It refers to an enclosing function scope.

**Q24. Can nonlocal be used outside nested functions?**

Ans: No. It requires a suitable enclosing function binding.

**Q25. What happens when nonlocal refers to a nonexistent enclosing variable?**

Ans: Python raises a `SyntaxError`.

**Q26. What is a nested function?**

Ans: A function defined inside another function.

**Q27. Can an inner function read an outer function variable?**

Ans: Yes.

**Q28. What is the difference between global and nonlocal?**

Ans: `global` refers to a module-level binding, while `nonlocal` refers to an enclosing function binding.

**Q29. Can an inner function call an outer function's local variables?**

Ans: It can access enclosing names that are in scope.

**Q30. Does a nested function automatically become global?**

Ans: No.

## Lifetime and Closures

**Q31. What happens to local variables after a function returns?**

Ans: Their local bindings in that function frame are no longer accessible through that function call. Referenced objects may remain alive if other references exist.

**Q32. What happens to a global variable when a function ends?**

Ans: It remains available as long as its module-level binding and references remain available.

**Q33. What is a closure?**

Ans: A function that retains access to variables from its enclosing lexical scope.

**Q34. What is the main advantage of a closure?**

Ans: It can preserve state or configuration without using global variables.

**Q35. Can a closure remember a value after the outer function returns?**

Ans: Yes.

**Q36. What is a function factory?**

Ans: A function that creates and returns another function.

**Q37. Give an example of a closure.**

Ans: A multiplier function that remembers its multiplier.

**Q38. Are closures useful in decorators?**

Ans: Yes. Closures are a key concept behind decorators.

**Q39. Can two closures remember different values?**

Ans: Yes. Each closure can have its own enclosing state.

**Q40. Can a closure modify an enclosing variable?**

Ans: Yes, using `nonlocal` when reassignment is required.

## Practical and Advanced Questions

**Q41. What is variable shadowing?**

Ans: It occurs when a name in a more local scope takes precedence over a name with the same identifier in an outer scope.

**Q42. What is an unbound local error?**

Ans: It occurs when a local variable is accessed before it has been assigned.

**Q43. What is the difference between mutating an object and rebinding its name?**

Ans: Mutating changes the existing object; rebinding assigns a name to a different object.

**Q44. Does mutating a global list require global?**

Ans: No, provided the function does not rebind the list name.

**Q45. What happens when a local variable uses the name list?**

Ans: It shadows the built-in `list` name within its scope.

**Q46. What is the built-in scope?**

Ans: It contains built-in names supplied by Python.

**Q47. Can scope affect code readability?**

Ans: Yes. Clear variable scopes reduce unintended interactions.

**Q48. Where are closures commonly used?**

Ans: Decorators, callbacks, function factories, and stateful functions.

**Q49. Does scope determine algorithm time complexity?**

Ans: No. Time complexity depends on the operations performed by the algorithm.

**Q50. Why is scope and lifetime important in software development?**

Ans: It helps developers manage state, avoid naming conflicts, control variable access, and write reliable functions.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Scope | Region where a name can be accessed |
| Lifetime | Duration a binding or object remains available |
| Local Variable | Variable defined in a function's local scope |
| Global Variable | Module-level variable |
| Enclosing Scope | Scope of an outer function |
| Built-in Scope | Scope containing Python's built-in names |
| LEGB | Local, Enclosing, Global, Built-in |
| global | Declares a module-level binding |
| nonlocal | Declares an enclosing function binding |
| Variable Shadowing | A local name takes precedence over an outer name |
| Nested Function | Function inside another function |
| Closure | Function retaining access to enclosing variables |
| Function Factory | Function that returns another function |
| UnboundLocalError | Error caused by reading a local variable before assignment |

---

# SECTION 12: QUICK REVISION NOTES

Remember these important points:

1. Scope determines where a name can be accessed.
2. Lifetime determines how long a binding or object remains available.
3. Variables inside functions are normally local.
4. Variables at module level are global.
5. Inner functions can access enclosing variables.
6. Python resolves names using the LEGB rule.
7. `global` allows reassignment of a module-level name.
8. `nonlocal` allows reassignment of an enclosing function name.
9. A local variable can shadow a global variable.
10. A closure remembers variables from its enclosing scope.
11. Modifying an existing global list does not require global.
12. Objects can remain alive when references to them still exist.

### Important Syntax

**Local Variable**

```python
def display():
    number = 100
    print(number)
```

**Global Variable**

```python
number = 100

def display():
    print(number)
```

**global**

```python
number = 0

def increment():
    global number
    number += 1
```

**nonlocal**

```python
def outer():
    number = 0

    def inner():
        nonlocal number
        number += 1
```

**Closure**

```python
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier

    return multiply
```

---

# SECTION 13: LEARNING CHECKLIST

Before moving to the next topic, make sure you can:

- [ ] Explain variable scope.
- [ ] Explain variable lifetime.
- [ ] Identify local variables.
- [ ] Identify global variables.
- [ ] Understand variable shadowing.
- [ ] Read global variables inside functions.
- [ ] Reassign global variables using global.
- [ ] Understand enclosing scope.
- [ ] Use nonlocal in nested functions.
- [ ] Explain the LEGB rule.
- [ ] Understand nested functions.
- [ ] Explain how closures retain enclosing bindings.
- [ ] Create a counter using nonlocal.
- [ ] Create a multiplier using a closure.
- [ ] Understand mutable global objects.
- [ ] Avoid shadowing built-in names.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Complete the User Session and Activity Tracker mini project.
- [ ] Answer the 50 viva questions.

---

# SECTION 14: HOW TO RUN THIS FILE

### File Location

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 07-Scope-and-Lifetime/
            ├── README.md
            └── 07_scope_and_lifetime.py
```

### Run Command

Open PowerShell or the VS Code terminal from your repository root.

Execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/07-Scope-and-Lifetime/07_scope_and_lifetime.py
```

### Main Menu

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

---

# FINAL LEARNING GOAL

After completing this topic, you should understand how Python manages variable accessibility and lifetime across different scopes.

You should be comfortable with local and global variables, nested functions, `global`, `nonlocal`, the LEGB rule, and closures.

These concepts are important for writing reusable functions, managing state, understanding decorators, and developing larger Python applications.

**Next Topic: 08 – Lambda Functions**

In the next topic, we will study anonymous functions, lambda syntax, single-expression functions, lambda with `map()`, `filter()`, `sorted()`, and practical functional programming examples.