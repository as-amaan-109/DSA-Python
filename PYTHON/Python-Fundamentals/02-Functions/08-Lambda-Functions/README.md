# Lambda Functions in Python

**Part 2: Python Fundamentals**  
**Section: 02 – Functions**  
**Topic: 08 – Lambda Functions**

---

# 1. Introduction

A lambda function is a small anonymous function in Python that is defined using the `lambda` keyword.

Unlike a normal function created with `def`, a lambda function contains a single expression.

Lambda functions are useful when a short function is needed temporarily, especially when working with functions such as:

- `map()`
- `filter()`
- `sorted()`
- `reduce()`

### Example

```python
square = lambda number: number * number

print(square(5))
print(square(8))
```

**Output:**

```text
25
64
```

### Explanation

- `lambda` creates a function.
- `number` is the parameter.
- `number * number` is the expression.
- The result of the expression is returned automatically.

### Learning Objectives

After completing this topic, you should be able to:

1. Understand lambda functions.
2. Understand anonymous functions.
3. Write lambda expressions.
4. Create lambda functions with multiple parameters.
5. Use default parameters in lambda functions.
6. Use conditional expressions in lambda functions.
7. Pass lambda functions as arguments.
8. Use lambda with `map()`.
9. Use lambda with `filter()`.
10. Use lambda with `sorted()`.
11. Use lambda with `reduce()`.
12. Create closures using lambda.
13. Understand late binding in lambda functions.
14. Solve programming problems using lambda expressions.

---

# 2. What Is a Lambda Function?

A lambda function is an anonymous function that can accept arguments and evaluate a single expression.

It is sometimes called an inline function because it can be defined directly where it is needed.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
add = lambda a, b: a + b

result = add(10, 20)

print(result)
```

**Output:**

```text
30
```

### Explanation

- `lambda` is the keyword.
- `a, b` are parameters.
- `a + b` is the expression.
- The expression's value is returned automatically.

### Equivalent Normal Function

Using `def`:

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Using `lambda`:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Both functions perform the same calculation.

### Important Points

- Lambda functions are created using the `lambda` keyword.
- They can accept zero or more parameters.
- Their body contains a single expression.
- The expression's value is returned automatically.
- Lambda functions are useful for short operations.
- They do not require an explicit `return` statement.

---

# 3. Why Are Lambda Functions Called Anonymous Functions?

The word *anonymous* means that the function is created without a function name in its definition.

### Normal Function

```python
def greet(name):
    return "Hello " + name

print(greet("Amaan"))
```

### Lambda Function

```python
greet = lambda name: "Hello " + name

print(greet("Amaan"))
```

**Output:**

```text
Hello Amaan
```

The lambda expression itself does not define a function name like `def greet(...)`.

However, the resulting function object can be stored in a variable such as `greet`.

### Important Point

A lambda function is not necessarily used only once. It can be stored in a variable and called multiple times.

---

# 4. Lambda Function with One Parameter

A lambda function can accept one parameter.

### Example

```python
square = lambda number: number ** 2

print(square(4))
print(square(6))
```

**Output:**

```text
16
36
```

### Explanation

The function accepts one number and returns its square.

### Another Example

```python
double = lambda number: number * 2

print(double(10))
print(double(25))
```

**Output:**

```text
20
50
```

---

# 5. Lambda Function with Multiple Parameters

A lambda function can accept multiple parameters.

### Example

```python
add = lambda a, b: a + b

print(add(10, 20))
```

**Output:**

```text
30
```

### Example with Three Parameters

```python
calculate_total = lambda a, b, c: a + b + c

print(calculate_total(10, 20, 30))
```

**Output:**

```text
60
```

### Important Point

Lambda functions can accept multiple arguments, but their body must still contain only one expression.

---

# 6. Lambda Functions with Default Arguments

Lambda functions can also define default parameter values.

### Example

```python
greet = lambda name, message="Hello": f"{message}, {name}!"

print(greet("Amaan"))
print(greet("Amaan", "Welcome"))
```

**Output:**

```text
Hello, Amaan!
Welcome, Amaan!
```

### Explanation

- `name` is required.
- `message` has a default value.
- The default can be replaced by supplying another value.

### Another Example

```python
power = lambda number, exponent=2: number ** exponent

print(power(5))
print(power(2, 3))
```

**Output:**

```text
25
8
```

---

# 7. Conditional Expressions in Lambda

A lambda function cannot contain an ordinary multi-statement `if-else` block.

However, it can use a conditional expression.

### Syntax

```python
lambda condition_input: value_if_true if condition else value_if_false
```

### Example: Even or Odd

```python
check = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

**Output:**

```text
Even
Odd
```

### Example: Positive or Negative

```python
check_number = lambda number: (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

print(check_number(10))
print(check_number(-5))
print(check_number(0))
```

**Output:**

```text
Positive
Negative
Zero
```

### Important Point

Conditional expressions allow a lambda function to select a result based on a condition.

For complicated conditions, a normal `def` function is usually easier to read.

---

# 8. Lambda as an Argument to Another Function

A lambda function can be passed as an argument to another function.

This is useful when a function needs a small operation provided by the caller.

### Example

```python
def calculate(operation, a, b):
    return operation(a, b)


result = calculate(
    lambda x, y: x + y,
    10,
    20
)

print(result)
```

**Output:**

```text
30
```

### Explanation

1. `calculate()` receives a function as an argument.
2. The lambda function performs the addition.
3. The result is returned by `calculate()`.

### Another Example

```python
def apply_operation(operation, number):
    return operation(number)


result = apply_operation(
    lambda value: value ** 2,
    5
)

print(result)
```

**Output:**

```text
25
```

This style is often called passing a function as an argument.

---

# 9. Lambda with map()

The `map()` function applies a given function to every element of an iterable.

A lambda function is frequently used with `map()` for short transformations.

### Syntax

```python
map(function, iterable)
```

In Python 3, `map()` returns an iterator. Use `list()` when you need to display or store all results as a list.

### Example: Square Every Number

```python
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number ** 2, numbers)
)

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

### Example: Convert Numbers to Strings

```python
numbers = [10, 20, 30]

result = list(
    map(lambda number: str(number), numbers)
)

print(result)
```

**Output:**

```text
['10', '20', '30']
```

### Example: Convert Celsius to Fahrenheit

Formula:

```text
Fahrenheit = (Celsius × 9/5) + 32
```

```python
celsius_values = [0, 20, 30, 40]

fahrenheit_values = list(
    map(
        lambda temperature: temperature * 9 / 5 + 32,
        celsius_values
    )
)

print(fahrenheit_values)
```

**Output:**

```text
[32.0, 68.0, 86.0, 104.0]
```

### When Is map() Useful?

- Transforming numbers.
- Converting data types.
- Processing strings.
- Applying the same calculation to multiple values.
- Performing collection transformations.

---

# 10. Lambda with filter()

The `filter()` function selects elements that satisfy a condition.

A lambda function can provide the condition.

### Syntax

```python
filter(function, iterable)
```

In Python 3, `filter()` returns an iterator. Use `list()` to materialize its results.

### Example: Filter Even Numbers

```python
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)
```

**Output:**

```text
[10, 20, 30]
```

### Example: Filter Positive Numbers

```python
numbers = [-10, 20, -5, 30, 0]

positive_numbers = list(
    filter(lambda number: number > 0, numbers)
)

print(positive_numbers)
```

**Output:**

```text
[20, 30]
```

### Example: Filter Long Words

```python
words = ["Python", "C", "Java", "JavaScript", "Go"]

long_words = list(
    filter(lambda word: len(word) > 4, words)
)

print(long_words)
```

**Output:**

```text
['Python', 'JavaScript']
```

### When Is filter() Useful?

- Selecting even or odd numbers.
- Filtering positive values.
- Finding long words.
- Selecting eligible students.
- Filtering products by price.
- Extracting records that satisfy conditions.

---

# 11. Difference Between map() and filter()

Both functions process iterables, but their purposes are different.

| Feature | map() | filter() |
|---|---|---|
| Purpose | Transform elements | Select elements |
| Function result | Transformed value | Truth value |
| Output size | Generally one output per input | Zero or more selected inputs |
| Returns in Python 3 | Iterator | Iterator |
| Common use | Square numbers | Select even numbers |

### map() Example

```python
numbers = [1, 2, 3, 4]

result = list(
    map(lambda x: x * 2, numbers)
)

print(result)
```

**Output:**

```text
[2, 4, 6, 8]
```

### filter() Example

```python
numbers = [1, 2, 3, 4]

result = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(result)
```

**Output:**

```text
[2, 4]
```

Remember:

- `map()` changes values.
- `filter()` selects values.

---

# 12. Lambda with sorted()

The `sorted()` function returns a new sorted list.

A lambda function can be used with the `key` parameter to define the sorting rule.

### Syntax

```python
sorted(iterable, key=function, reverse=False)
```

### Example: Sort by String Length

```python
words = ["Python", "C", "JavaScript", "Java", "Go"]

result = sorted(
    words,
    key=lambda word: len(word)
)

print(result)
```

**Output:**

```text
['C', 'Go', 'Java', 'Python', 'JavaScript']
```

### Example: Sort by Absolute Value

```python
numbers = [-10, 5, -2, 8, -1]

result = sorted(
    numbers,
    key=lambda number: abs(number)
)

print(result)
```

**Output:**

```text
[-1, -2, 5, 8, -10]
```

### Example: Sort Dictionaries by Marks

```python
students = [
    {"name": "Amaan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Ali", "marks": 78}
]

result = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

print(result)
```

**Output:**

```text
[
    {'name': 'Rahul', 'marks': 92},
    {'name': 'Amaan', 'marks': 85},
    {'name': 'Ali', 'marks': 78}
]
```

### Important Points

- `key` defines how elements are compared for ordering.
- `reverse=True` sorts in descending order.
- `sorted()` returns a new list.
- The original iterable is not modified by `sorted()`.

---

# 13. Lambda with reduce()

The `reduce()` function repeatedly combines elements of an iterable to produce a single result.

It is available in the `functools` module.

### Import

```python
from functools import reduce
```

### Syntax

```python
reduce(function, iterable)
```

An optional initializer can also be supplied:

```python
reduce(function, iterable, initializer)
```

### Example: Sum of Numbers

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda total, number: total + number,
    numbers
)

print(result)
```

**Output:**

```text
15
```

### How Does It Work?

The function combines values one at a time:

```text
Step 1: 1 + 2 = 3
Step 2: 3 + 3 = 6
Step 3: 6 + 4 = 10
Step 4: 10 + 5 = 15
```

Final result:

```text
15
```

### Example: Product of Numbers

```python
from functools import reduce

numbers = [2, 3, 4, 5]

result = reduce(
    lambda total, number: total * number,
    numbers
)

print(result)
```

**Output:**

```text
120
```

### Example: Reduce with an Initial Value

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(
    lambda total, number: total + number,
    numbers,
    10
)

print(result)
```

**Output:**

```text
20
```

The initial value `10` is used as the starting accumulator.

### Important Points

- `reduce()` combines elements into one result.
- It is imported from `functools`.
- Without an initializer, the first element becomes the initial accumulator.
- An empty iterable without an initializer raises `TypeError`.
- Providing an initializer allows the function to handle an empty iterable.

---

# 14. Lambda Functions with Closures

A lambda function can access variables from its enclosing scope.

This allows lambda functions to behave like closures.

### Example

```python
def create_multiplier(multiplier):
    return lambda number: number * multiplier


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
2. It creates a lambda function.
3. The lambda references the enclosing variable `multiplier`.
4. The lambda is returned.
5. The returned function retains access to that variable.

### Uses of Lambda Closures

- Creating reusable function factories.
- Preserving configuration.
- Building callbacks.
- Creating simple customized operations.

---

# 15. Late Binding in Lambda Functions

Late binding is an important concept when lambda functions are created inside loops.

A lambda that refers to a loop variable usually looks up that variable when the lambda is called, not when it is created.

### Example with Late Binding

```python
functions = []

for multiplier in range(1, 4):
    functions.append(
        lambda number: number * multiplier
    )

for function in functions:
    print(function(10))
```

**Output:**

```text
30
30
30
```

### Why Does This Happen?

All three lambda functions refer to the same loop variable `multiplier`.

After the loop finishes, its final value is `3`.

Therefore, all functions use `3` when called.

### Correct Solution: Default Argument Capture

```python
functions = []

for multiplier in range(1, 4):
    functions.append(
        lambda number, multiplier=multiplier: number * multiplier
    )

for function in functions:
    print(function(10))
```

**Output:**

```text
10
20
30
```

### Explanation

The default parameter captures the current value when each lambda is created.

This avoids the common late-binding problem in loop-created lambdas.

---

# 16. Lambda Functions vs Normal Functions

| Feature | Lambda Function | Normal Function |
|---|---|---|
| Definition | `lambda` | `def` |
| Name | Anonymous expression, can be assigned to a variable | Defined with a function name |
| Body | Single expression | Multiple statements |
| Return | Automatically returns expression result | Uses `return` when needed |
| Documentation | Limited inline documentation | Supports docstrings |
| Complex logic | Not recommended | Suitable |
| Common use | Short operations | Reusable and complex logic |

### Lambda Example

```python
square = lambda number: number ** 2

print(square(5))
```

### Normal Function Example

```python
def square(number):
    result = number ** 2
    return result

print(square(5))
```

Both produce:

```text
25
```

### When Should You Use Lambda?

Use lambda when:

- The operation is short.
- You need a small function temporarily.
- You are passing a function as an argument.
- You are using `map()`, `filter()`, or `sorted()`.

### When Should You Use def?

Use normal functions when:

- Logic has multiple steps.
- Conditions are complicated.
- You need descriptive docstrings.
- The function will be reused in many places.
- Code readability would improve with a named function.

**Best Practice:** Do not force every short function into lambda syntax. Readability is more important than reducing the number of lines.

---

# SECTION 1: TWELVE TOPIC EXAMPLES

All these examples are included in:

`08_lambda_functions.py`

## Example 01 – Basic Lambda Function

**Concept:** Creating a simple lambda function.

```python
square = lambda number: number * number

print("Square of 5:", square(5))
print("Square of 8:", square(8))
```

**Output:**

```text
Square of 5: 25
Square of 8: 64
```

**Explanation:** The lambda accepts a number and returns its square.

## Example 02 – Multiple Parameters

**Concept:** Passing multiple parameters to a lambda.

```python
add = lambda first, second: first + second

subtract = lambda first, second: first - second

print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))
```

**Output:**

```text
Addition: 30
Subtraction: 10
```

**Explanation:** A lambda can have multiple parameters separated by commas.

## Example 03 – Lambda as an Argument

**Concept:** Passing a lambda function to another function.

```python
def calculate(operation, first, second):
    return operation(first, second)


result = calculate(
    lambda a, b: a + b,
    10,
    5
)

print("Result:", result)
```

**Output:**

```text
Result: 15
```

**Explanation:** The lambda is supplied as the operation to perform.

## Example 04 – Lambda with Default Argument

**Concept:** Using a default parameter.

```python
greet = lambda name, message="Hello": f"{message}, {name}!"

print(greet("Amaan"))
print(greet("Amaan", "Welcome"))
```

**Output:**

```text
Hello, Amaan!
Welcome, Amaan!
```

**Explanation:** When no custom message is supplied, the lambda uses `"Hello"`.

## Example 05 – Conditional Lambda

**Concept:** Returning different values using a conditional expression.

```python
check_number = lambda number: (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

numbers = [10, -5, 0, 25, -12]

for number in numbers:
    print(number, check_number(number))
```

**Output:**

```text
10 Positive
-5 Negative
0 Zero
25 Positive
-12 Negative
```

**Explanation:** The expression checks the number and selects the correct result.

## Example 06 – Lambda with sorted()

**Concept:** Sorting strings by length.

```python
words = ["Python", "C", "JavaScript", "Java", "Go"]

sorted_words = sorted(
    words,
    key=lambda word: len(word)
)

print(sorted_words)
```

**Output:**

```text
['C', 'Go', 'Java', 'Python', 'JavaScript']
```

**Explanation:** The lambda returns each word's length, which is used as the sorting key.

## Example 07 – Lambda with map()

**Concept:** Transforming values using lambda.

```python
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number ** 2, numbers)
)

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

**Explanation:** Each number is passed through the lambda and its square is collected into a list.

## Example 08 – Lambda with filter()

**Concept:** Selecting even numbers.

```python
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)
```

**Output:**

```text
[10, 20, 30]
```

**Explanation:** Only elements for which the lambda returns a truthy value are retained.

## Example 09 – Lambda with reduce()

**Concept:** Combining elements into one result.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda result, number: result + number,
    numbers
)

print(total)
```

**Output:**

```text
15
```

**Explanation:** The lambda adds each element to the accumulated result.

## Example 10 – Lambda with Dictionaries

**Concept:** Sorting student dictionaries by marks.

```python
students = [
    {"name": "Amaan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Ali", "marks": 78}
]

sorted_students = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

for student in sorted_students:
    print(student["name"], student["marks"])
```

**Output:**

```text
Rahul 92
Amaan 85
Ali 78
```

**Explanation:** The lambda retrieves the `marks` field from each dictionary.

## Example 11 – Lambda Closure

**Concept:** Creating functions that remember an enclosing variable.

```python
def create_multiplier(multiplier):
    return lambda number: number * multiplier


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

**Explanation:** Each lambda retains access to its own multiplier.

## Example 12 – Lambda Late Binding

**Concept:** Capturing loop values using default parameters.

```python
multipliers = []

for multiplier in range(1, 4):
    multipliers.append(
        lambda number, multiplier=multiplier: number * multiplier
    )

results = [
    function(10)
    for function in multipliers
]

print(results)
```

**Output:**

```text
[10, 20, 30]
```

**Explanation:** The default argument preserves the multiplier value for each lambda when it is created.

---

# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS

## Problem 01 – Square of a Number

**Problem Statement:**

Write a lambda function that returns the square of a number.

**Code:**

```python
square = lambda number: number ** 2

number = int(input("Enter a number: "))

print("Square:", square(number))
```

**Sample Input:**

```text
Enter a number: 5
```

**Output:**

```text
Square: 25
```

**Explanation:**

The lambda accepts one value and returns its square using the exponent operator.

**Complexity:**

- Time: O(1), under ordinary bounded integer assumptions.
- Auxiliary Space: O(1), excluding large-integer storage.

## Problem 02 – Add Two Numbers

**Problem Statement:**

Create a lambda function that accepts two numbers and returns their sum.

**Code:**

```python
add = lambda a, b: a + b

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("Sum:", add(first, second))
```

**Sample Input:**

```text
Enter first number: 10
Enter second number: 20
```

**Output:**

```text
Sum: 30.0
```

**Explanation:**

The lambda receives two parameters and evaluates their addition.

**Complexity:**

- Time: O(1), under bounded numeric assumptions.
- Auxiliary Space: O(1).

## Problem 03 – Maximum of Two Numbers

**Problem Statement:**

Write a lambda function that returns the greater of two values.

**Code:**

```python
maximum = lambda a, b: a if a >= b else b

print(maximum(10, 20))
print(maximum(50, 30))
```

**Output:**

```text
20
50
```

**Explanation:**

A conditional expression selects the greater value.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 04 – Even or Odd

**Problem Statement:**

Write a lambda function that checks whether a number is even or odd.

**Code:**

```python
check = lambda number: "Even" if number % 2 == 0 else "Odd"

number = int(input("Enter an integer: "))

print(check(number))
```

**Sample Input:**

```text
Enter an integer: 15
```

**Output:**

```text
Odd
```

**Explanation:**

The remainder operator checks whether the number is divisible by two.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1)

## Problem 05 – Square List Elements Using map()

**Problem Statement:**

Use `map()` and lambda to calculate the square of every list element.

**Code:**

```python
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number ** 2, numbers)
)

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

**Explanation:**

`map()` applies the lambda to each element and produces an iterator. `list()` collects the results.

**Complexity:**

- Time: O(n), for bounded-size integer operations.
- Auxiliary Space: O(n), for the output list and result storage.

## Problem 06 – Filter Even Numbers

**Problem Statement:**

Use `filter()` with lambda to extract even values from a list.

**Code:**

```python
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)
```

**Output:**

```text
[10, 20, 30]
```

**Explanation:**

The lambda returns `True` for even values. The filter iterator produces only those selected values.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(n) in the worst case for the output list.

## Problem 07 – Filter Long Words

**Problem Statement:**

Use lambda and `filter()` to select words whose length is at least five characters.

**Code:**

```python
words = [
    "Python",
    "C",
    "Java",
    "JavaScript",
    "Go"
]

minimum_length = 5

result = list(
    filter(
        lambda word: len(word) >= minimum_length,
        words
    )
)

print(result)
```

**Output:**

```text
['Python', 'JavaScript']
```

**Explanation:**

The function checks the length of each word and keeps only qualifying strings.

**Complexity:**

- Time: O(L), where L is the total length of the strings inspected.
- Auxiliary Space: O(L) in the worst case for the selected string references and output list, excluding the original input.

## Problem 08 – Sort by Absolute Value

**Problem Statement:**

Use `sorted()` and lambda to sort integers according to their absolute values.

**Code:**

```python
numbers = [-10, 5, -2, 8, -1]

result = sorted(
    numbers,
    key=lambda number: abs(number)
)

print(result)
```

**Output:**

```text
[-1, -2, 5, 8, -10]
```

**Explanation:**

The lambda returns the absolute value of each number. The original signed values are retained in the result.

**Complexity:**

- Time: O(n log n)
- Auxiliary Space: O(n) for the returned list and sorting storage.

## Problem 09 – Sort Students by Marks

**Problem Statement:**

Sort student records according to marks in descending order.

**Code:**

```python
students = [
    {"name": "Amaan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Ali", "marks": 78},
    {"name": "Sara", "marks": 95}
]

result = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

for student in result:
    print(student["name"], student["marks"])
```

**Output:**

```text
Sara 95
Rahul 92
Amaan 85
Ali 78
```

**Explanation:**

The lambda extracts the marks field from each student dictionary. `reverse=True` arranges the students from highest to lowest marks.

**Complexity:**

- Time: O(n log n), plus the cost of key evaluation.
- Auxiliary Space: O(n) for the sorted result and sorting storage.

## Problem 10 – Product Using reduce()

**Problem Statement:**

Use `reduce()` and lambda to calculate the product of all elements in a list.

**Code:**

```python
from functools import reduce

numbers = [2, 3, 4, 5]

result = reduce(
    lambda total, number: total * number,
    numbers
)

print(result)
```

**Output:**

```text
120
```

**Explanation:**

Each value is multiplied with the accumulated result.

**Complexity:**

- Time: O(n), under bounded numeric assumptions.
- Auxiliary Space: O(1) additional working storage, excluding input and numeric result size.

## Problem 11 – Lambda Calculator

**Problem Statement:**

Create a calculator using a dictionary of lambda functions.

The calculator should support:

- Addition
- Subtraction
- Multiplication
- Division

**Code:**

```python
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator not in operations:
    print("Invalid operator.")

elif operator == "/" and second == 0:
    print("Division by zero is not allowed.")

else:
    result = operations[operator](first, second)
    print("Result:", result)
```

**Sample Input:**

```text
Enter first number: 20
Enter second number: 5
Enter operator (+, -, *, /): /
```

**Output:**

```text
Result: 4.0
```

**Explanation:**

Each dictionary value is a lambda function. The selected operator determines which function is executed.

**Complexity:**

- Time: O(1), under bounded numeric assumptions.
- Auxiliary Space: O(1), for the fixed operation dictionary.

## Problem 12 – Multiplier Factory

**Problem Statement:**

Create a lambda-based function factory that remembers a multiplier.

**Code:**

```python
def create_multiplier(multiplier):
    return lambda number: number * multiplier


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

**Explanation:**

Each returned lambda retains access to the multiplier from its enclosing function call.

**Complexity:**

- Time: O(1), under bounded numeric assumptions.
- Auxiliary Space: O(1), excluding function object storage.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these questions independently.

### Question 01 – Cube of a Number

Write a lambda function that calculates the cube of a number.

Example:

```text
Input: 3
Expected Output: 27
```

### Question 02 – Number Classification

Write a lambda function that classifies a number as Positive, Negative, or Zero.

Example:

```text
Input: -10
Expected Output: Negative
```

### Question 03 – Celsius to Fahrenheit

Use `map()` and lambda to convert all Celsius temperatures in a list into Fahrenheit.

Example:

```text
Input: [0, 20, 30]
Expected Output: [32.0, 68.0, 86.0]
```

### Question 04 – Divisible by Five

Use `filter()` and lambda to extract numbers divisible by five.

Example:

```text
Input: [10, 12, 15, 18, 20]
Expected Output: [10, 15, 20]
```

### Question 05 – Sort by Last Character

Use `sorted()` and lambda to sort a list of words according to their last character.

Example:

```text
Input: ["Apple", "Banana", "Mango"]
Expected Output: Depends on last-character alphabetical order.
```

### Question 06 – Student Ranking

Sort student dictionaries according to marks in ascending order using lambda.

### Question 07 – Sum Using reduce()

Use `reduce()` and lambda to calculate the sum of list elements.

Example:

```text
Input: [10, 20, 30]
Expected Output: 60
```

### Question 08 – Lambda Calculator

Create a dictionary containing lambda functions for addition, subtraction, multiplication, and division.

### Question 09 – Exponent Factory

Create a lambda-based function factory that remembers a custom exponent.

Example:

```text
Exponent: 3
Input: 4
Expected Output: 64
```

### Question 10 – Late Binding

Create multiple lambda functions inside a loop. Use default argument capture so each lambda remembers the correct loop value.

Example:

```text
Multipliers: 1, 2, 3
Input: 10

Expected Results:
10
20
30
```

---

# SECTION 4: COMMON MISTAKES

## Mistake 01 – Writing Multiple Statements Inside Lambda

Incorrect:

```python
# This is invalid syntax:
# result = lambda number: total = number * 2
```

A lambda expression cannot contain an assignment statement like this.

Correct:

```python
double = lambda number: number * 2

print(double(10))
```

## Mistake 02 – Forgetting the Colon

Incorrect:

```python
# lambda number number * 2
```

Correct:

```python
double = lambda number: number * 2
```

## Mistake 03 – Forgetting the Conditional Else

Incorrect:

```python
# This is an incomplete conditional expression:
# check = lambda number: "Even" if number % 2 == 0
```

Correct:

```python
check = lambda number: (
    "Even" if number % 2 == 0 else "Odd"
)
```

## Mistake 04 – Not Converting map() to a List

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

In Python 3, the result is a map iterator, not a ready-made list of transformed values.

Correct:

```python
result = list(
    map(lambda x: x * 2, numbers)
)

print(result)
```

## Mistake 05 – Not Converting filter() to a List

Correct:

```python
numbers = [1, 2, 3, 4]

result = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(result)
```

## Mistake 06 – Importing reduce() Incorrectly

Incorrect:

```python
# reduce() is not directly available as a built-in function.
```

Correct:

```python
from functools import reduce
```

## Mistake 07 – Late Binding in Loops

Incorrect:

```python
functions = []

for multiplier in range(1, 4):
    functions.append(
        lambda number: number * multiplier
    )
```

All three functions use the final value of `multiplier` when called after the loop.

Correct:

```python
functions = []

for multiplier in range(1, 4):
    functions.append(
        lambda number, multiplier=multiplier:
        number * multiplier
    )
```

---

# SECTION 5: BEST PRACTICES

1. Use lambda functions for short expressions.
2. Use `def` for complicated logic.
3. Give lambda variables meaningful names when storing them.
4. Use `map()` when transforming every element.
5. Use `filter()` when selecting elements.
6. Use `sorted()` with a lambda key when custom sorting is needed.
7. Import `reduce()` from `functools`.
8. Use `list()` when you need to materialize map or filter results.
9. Avoid deeply nested conditional expressions.
10. Use default argument capture to avoid common late-binding problems.
11. Prefer readable code over unnecessarily short code.
12. Use a normal named function when the operation requires comments, multiple statements, or detailed documentation.

### Recommended Style

Good:

```python
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda number: number ** 2, numbers)
)
```

For more complicated logic, prefer:

```python
def calculate_discounted_price(price, discount):
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount <= 100:
        raise ValueError("Invalid discount.")

    return price - (price * discount / 100)
```

---

# SECTION 6: REAL-WORLD APPLICATIONS

Lambda functions are used in many Python applications.

## 1. Data Processing

`map()` and lambda can transform data values.

## 2. Data Filtering

`filter()` can select records that satisfy a condition.

## 3. Student Management Systems

Lambda functions can sort student records according to marks.

## 4. E-Commerce Applications

Product records can be sorted by price or rating using a lambda key.

## 5. Report Generation

Lambda functions can select and order report data.

## 6. Financial Applications

Small calculations can be represented as lambda expressions.

## 7. Data Science

Lambda functions are often used for simple transformations and sorting in data-processing workflows.

## 8. Functional Programming

Lambda functions are useful when functions are passed to other functions as arguments.

---

# SECTION 7: CONNECTION WITH DSA

Lambda functions can make short DSA operations easier to express.

### 1. Sorting

```python
numbers = [5, 2, 8, 1, 4]

result = sorted(
    numbers,
    key=lambda number: number
)

print(result)
```

### 2. Filtering

```python
numbers = [10, 15, 20, 25, 30]

result = list(
    filter(lambda number: number > 20, numbers)
)

print(result)
```

### 3. Mapping

```python
numbers = [1, 2, 3, 4]

result = list(
    map(lambda number: number * number, numbers)
)

print(result)
```

### 4. Finding Maximum by a Key

```python
students = [
    {"name": "Amaan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Ali", "marks": 78}
]

top_student = max(
    students,
    key=lambda student: student["marks"]
)

print(top_student)
```

### 5. Greedy Algorithms

Lambda functions can define custom sorting keys, such as sorting intervals by ending time.

### 6. Priority Queues

A custom key can help arrange records by priority.

**Important:** Lambda functions do not automatically make algorithms faster. The underlying algorithm determines time complexity.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

Lambda syntax does not determine the time complexity of an operation. The work performed by the lambda and the surrounding function determines the complexity.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Simple square lambda | O(1), under bounded numeric assumptions | O(1) |
| Addition lambda | O(1), under bounded numeric assumptions | O(1) |
| Conditional comparison | O(1), under bounded-value assumptions | O(1) |
| map() over n elements | O(n), excluding costly function body operations | O(1) for iterator state; O(n) if collected into a list |
| filter() over n elements | O(n), excluding predicate costs | O(1) for iterator state; O(n) worst case if collected |
| sorted() over n elements | O(n log n) | O(n) for sorting storage and returned list |
| reduce() over n values | O(n), under bounded operation assumptions | O(1) additional working space, excluding input and result size |
| Join n strings | O(L), where L is total output length | O(L) |
| Dictionary sorting | O(n log n), plus key evaluation costs | O(n) |

Here:

- `n` is the number of elements.
- `L` is the total length of strings being processed.

---

# SECTION 9: MINI PROJECT – STUDENT MARKS ANALYZER USING LAMBDA

## Project Objective

Build a Student Marks Analyzer using lambda functions.

The program should:

- Store student records.
- Sort students by marks.
- Filter students who passed.
- Calculate grade categories.
- Find the highest scorer.
- Display processed results.

### Project Code

```python
from typing import Any, Dict, List


students: List[Dict[str, Any]] = [
    {"name": "Amaan", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Ali", "marks": 35},
    {"name": "Sara", "marks": 95},
    {"name": "Zoya", "marks": 68}
]


def analyze_students(records):
    """Analyze student records using lambda expressions."""

    passed = list(
        filter(
            lambda student: student["marks"] >= 40,
            records
        )
    )

    failed = list(
        filter(
            lambda student: student["marks"] < 40,
            records
        )
    )

    ranked = sorted(
        records,
        key=lambda student: student["marks"],
        reverse=True
    )

    highest_scorer = max(
        records,
        key=lambda student: student["marks"]
    ) if records else None

    graded = list(
        map(
            lambda student: {
                **student,
                "grade": (
                    "A" if student["marks"] >= 90
                    else "B" if student["marks"] >= 80
                    else "C" if student["marks"] >= 70
                    else "D" if student["marks"] >= 60
                    else "E" if student["marks"] >= 40
                    else "F"
                )
            },
            records
        )
    )

    return {
        "passed": passed,
        "failed": failed,
        "ranked": ranked,
        "highest_scorer": highest_scorer,
        "graded": graded
    }


def display_report(report):
    """Display the student analysis report."""

    print("\n========== STUDENT MARKS ANALYZER ==========")

    print("\n1. Students Ranked by Marks")

    for rank, student in enumerate(
        report["ranked"],
        start=1
    ):
        print(
            f"{rank}. {student['name']} "
            f"- {student['marks']}"
        )

    print("\n2. Passed Students")

    for student in report["passed"]:
        print(student["name"], "-", student["marks"])

    print("\n3. Failed Students")

    for student in report["failed"]:
        print(student["name"], "-", student["marks"])

    print("\n4. Highest Scorer")

    if report["highest_scorer"]:
        top = report["highest_scorer"]

        print(
            top["name"],
            "-",
            top["marks"]
        )

    print("\n5. Student Grades")

    for student in report["graded"]:
        print(
            student["name"],
            "-",
            student["grade"]
        )


def main():
    report = analyze_students(students)
    display_report(report)


if __name__ == "__main__":
    main()
```

### Expected Output

```text
========== STUDENT MARKS ANALYZER ==========

1. Students Ranked by Marks
1. Sara - 95
2. Rahul - 92
3. Amaan - 85
4. Zoya - 68
5. Ali - 35

2. Passed Students
Amaan - 85
Rahul - 92
Sara - 95
Zoya - 68

3. Failed Students
Ali - 35

4. Highest Scorer
Sara - 95

5. Student Grades
Amaan - B
Rahul - A
Ali - F
Sara - A
Zoya - D
```

### Concepts Used

- Lambda expressions.
- `map()`.
- `filter()`.
- `sorted()`.
- `max()` with a key function.
- Dictionary operations.
- Conditional expressions.
- Function composition.

---

# SECTION 10: 50 VIVA QUESTIONS AND ANSWERS

## Basic Concepts

**Q1. What is a lambda function in Python?**

Ans: A lambda function is a small anonymous function created using the `lambda` keyword.

**Q2. Why is a lambda function called anonymous?**

Ans: It is defined without a function name in its expression.

**Q3. What is the syntax of a lambda function?**

Ans: `lambda arguments: expression`.

**Q4. Can a lambda function accept multiple arguments?**

Ans: Yes.

**Q5. Can a lambda function have zero arguments?**

Ans: Yes.

**Q6. Can a lambda function return a value?**

Ans: Yes. It automatically returns the evaluated expression.

**Q7. Is an explicit return statement needed in a lambda?**

Ans: No.

**Q8. Can we store a lambda function in a variable?**

Ans: Yes.

**Q9. Can lambda functions be passed as arguments?**

Ans: Yes.

**Q10. Can a lambda function use default arguments?**

Ans: Yes.

## Lambda and Normal Functions

**Q11. What is the main difference between lambda and def?**

Ans: Lambda defines a single-expression anonymous function, while `def` defines a regular function that can contain multiple statements.

**Q12. Can a lambda function contain multiple statements?**

Ans: No. Its body is a single expression.

**Q13. Can a lambda function use an if expression?**

Ans: Yes, using a conditional expression.

**Q14. Can lambda functions be used with multiple parameters?**

Ans: Yes.

**Q15. Can a lambda expression access a global variable?**

Ans: Yes, subject to normal Python name-resolution rules.

**Q16. Can a lambda expression access an enclosing variable?**

Ans: Yes.

**Q17. Can lambda functions be used as callbacks?**

Ans: Yes.

**Q18. Are lambda functions always better than normal functions?**

Ans: No. For complex logic, normal functions are often more readable.

**Q19. Can lambda functions be used with dictionaries?**

Ans: Yes, for example as sorting keys or dictionary values.

**Q20. What happens when a lambda expression is evaluated?**

Ans: Python creates a function object.

## map(), filter(), sorted() and reduce()

**Q21. What is map() used for?**

Ans: It applies a function to each element of an iterable.

**Q22. What does map() return in Python 3?**

Ans: It returns a map iterator.

**Q23. Why do we use list() with map()?**

Ans: To collect the results into a list.

**Q24. What is filter() used for?**

Ans: It selects elements that satisfy a condition.

**Q25. What does filter() return in Python 3?**

Ans: It returns a filter iterator.

**Q26. What is the difference between map() and filter()?**

Ans: `map()` transforms values, while `filter()` selects values.

**Q27. What is sorted() used for?**

Ans: It returns a new sorted list.

**Q28. What is the key parameter in sorted()?**

Ans: It specifies a function used to calculate a comparison key for each element.

**Q29. What does reverse=True do in sorted()?**

Ans: It arranges the result in descending order.

**Q30. What is reduce() used for?**

Ans: It repeatedly combines values from an iterable into a single result.

**Q31. Which module contains reduce()?**

Ans: `functools`.

**Q32. What happens when reduce() receives an empty iterable without an initializer?**

Ans: It raises a `TypeError`.

**Q33. Can reduce() use an initializer?**

Ans: Yes.

**Q34. Can lambda be used with reduce()?**

Ans: Yes.

**Q35. Can lambda be used to sort dictionary records?**

Ans: Yes, through the `key` parameter of `sorted()`.

## Closures and Advanced Concepts

**Q36. What is a lambda closure?**

Ans: A lambda function that retains access to variables from its enclosing scope.

**Q37. Can a lambda function remember an enclosing variable?**

Ans: Yes.

**Q38. What is late binding?**

Ans: A name referenced by a closure is looked up when the function is called, rather than necessarily when it is created.

**Q39. How can we avoid common late-binding problems in loop-created lambdas?**

Ans: Capture the current value using a default parameter.

**Q40. Can multiple lambda functions have different captured values?**

Ans: Yes.

**Q41. What is a conditional expression?**

Ans: An expression that selects one of two values based on a condition.

**Q42. Can a lambda function use a conditional expression?**

Ans: Yes.

**Q43. Is a lambda function a normal Python function object?**

Ans: Yes. It is a function object created by a lambda expression.

**Q44. Can a lambda function be used inside a list?**

Ans: Yes. It can be stored as an element of a list.

**Q45. Can a lambda function be stored as a dictionary value?**

Ans: Yes.

## Practical and DSA Questions

**Q46. How can lambda help in sorting student records?**

Ans: It can provide a key function that extracts marks from each student dictionary.

**Q47. What is the time complexity of sorting n elements?**

Ans: Typically O(n log n).

**Q48. What is the time complexity of applying a simple map operation to n values?**

Ans: O(n), excluding the cost of more complex operations inside the mapping function.

**Q49. Does using lambda automatically improve performance?**

Ans: No. Lambda is mainly a concise way to create function objects.

**Q50. Why are lambda functions important in Python development?**

Ans: They provide a concise way to express small operations, especially in functional-style processing and sorting.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Lambda | Keyword used to create an anonymous function |
| Anonymous Function | Function defined without a name in its expression |
| Expression | Code that evaluates to a value |
| Conditional Expression | Expression that selects a result based on a condition |
| map() | Applies a function to iterable elements |
| filter() | Selects elements satisfying a condition |
| sorted() | Returns a new sorted list |
| reduce() | Combines iterable values into a single result |
| Iterator | Object that produces values one at a time |
| Closure | Function retaining access to enclosing variables |
| Late Binding | Looking up a referenced variable when a function is called |
| Key Function | Function used to determine sorting order |
| Default Capture | Capturing a current value through a default parameter |

---

# SECTION 12: QUICK REVISION NOTES

Remember these important points:

1. Lambda functions are created using the `lambda` keyword.
2. Lambda functions contain a single expression.
3. Lambda expressions return their result automatically.
4. Lambda functions can accept multiple parameters.
5. Default parameters are allowed.
6. Conditional expressions can be used in lambdas.
7. `map()` transforms iterable elements.
8. `filter()` selects iterable elements.
9. `sorted()` can use lambda as a key function.
10. `reduce()` combines iterable values.
11. `reduce()` is imported from `functools`.
12. A lambda can retain access to enclosing variables.
13. Loop-created lambdas can have late-binding issues.
14. Default argument capture can preserve loop values.
15. Normal functions are preferable for complicated logic.

### Important Syntax

**Basic Lambda**

```python
square = lambda number: number ** 2
```

**Multiple Parameters**

```python
add = lambda a, b: a + b
```

**Conditional Lambda**

```python
check = lambda number: "Even" if number % 2 == 0 else "Odd"
```

**map()**

```python
result = list(
    map(lambda x: x * 2, numbers)
)
```

**filter()**

```python
result = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

**sorted()**

```python
result = sorted(
    students,
    key=lambda student: student["marks"]
)
```

**reduce()**

```python
from functools import reduce

result = reduce(
    lambda a, b: a + b,
    numbers
)
```

**Lambda Closure**

```python
def create_multiplier(multiplier):
    return lambda number: number * multiplier
```

**Default Argument Capture**

```python
functions = [
    lambda number, value=value: number * value
    for value in range(1, 4)
]
```

---

# SECTION 13: LEARNING CHECKLIST

Before moving to the next topic, make sure you can:

- [ ] Explain lambda functions.
- [ ] Write a basic lambda expression.
- [ ] Create a lambda function with multiple parameters.
- [ ] Use default parameters in lambda.
- [ ] Use conditional expressions.
- [ ] Pass lambda functions as arguments.
- [ ] Use lambda with map().
- [ ] Use lambda with filter().
- [ ] Use lambda with sorted().
- [ ] Use lambda with reduce().
- [ ] Explain why reduce() comes from functools.
- [ ] Sort dictionaries using lambda.
- [ ] Create closures using lambda.
- [ ] Explain late binding.
- [ ] Capture loop values using default arguments.
- [ ] Differentiate lambda and normal functions.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Complete the Student Marks Analyzer mini project.
- [ ] Answer the 50 viva questions.

---

# SECTION 14: HOW TO RUN THIS FILE

### File Location

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 08-Lambda-Functions/
            ├── README.md
            └── 08_lambda_functions.py
```

### Run Command

Open PowerShell or the VS Code terminal from your repository root.

Execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/08-Lambda-Functions/08_lambda_functions.py
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

After completing this topic, you should understand how to write small anonymous functions and use them to transform, filter, sort, and process data.

You should also understand lambda closures and late binding.

These concepts are useful in Python development, data processing, functional programming, and DSA problem-solving.

**Next Topic: 09 – Recursion**

In the next topic, we will study recursive functions, base cases, recursive cases, call stack, factorial, Fibonacci, recursion trees, and the difference between recursion and iteration.