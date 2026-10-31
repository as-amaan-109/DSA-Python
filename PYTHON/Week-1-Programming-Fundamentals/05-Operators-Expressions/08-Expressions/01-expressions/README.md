# Python Expressions

**Week:** 01 – Programming Fundamentals  
**Main Topic:** Operators and Expressions  
**Subtopic:** Expressions  
**Folder:** `01-expressions`  
**Python File:** `01_expressions.py`  
**Level:** Beginner to Intermediate

---

# 1. Introduction to Expressions

Expressions are one of the most important concepts in Python programming.

An expression is a combination of values, variables, operators, function calls, and other Python constructs that produces a value.

In simple words, an expression is something Python evaluates to obtain a result.

### Example 1: Basic Expression

```python
10 + 20
```

**Output:**

```text
30
```

Here:

- `10` is the first operand.
- `20` is the second operand.
- `+` is the arithmetic operator.
- `10 + 20` is the expression.
- `30` is the resulting value.

### Example 2: Expression Using Variables

```python
a = 10
b = 20

result = a + b

print(result)
```

**Output:**

```text
30
```

Explanation:

1. A variable `a` stores `10`.
2. A variable `b` stores `20`.
3. Python evaluates `a + b`.
4. The resulting value is `30`.
5. The value is assigned to `result`.

### Example 3: Expression Using Multiple Operators

```python
a = 10
b = 5
c = 2

result = a + b * c

print(result)
```

**Output:**

```text
20
```

Python evaluates multiplication before addition:

```text
a + b * c
10 + 5 * 2
10 + 10
20
```

This example introduces operator precedence, which will be studied separately in the next subtopic.

### Why Are Expressions Important?

Almost every practical Python program uses expressions.

Expressions are used for:

- Mathematical calculations.
- Comparing values.
- Making decisions.
- Combining conditions.
- Joining strings.
- Repeating strings.
- Accessing collection elements.
- Extracting parts of a collection.
- Calling functions.
- Creating new collections.
- Performing data transformations.

Understanding expressions is essential before learning advanced Python programming and Data Structures and Algorithms.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand the meaning of an expression.
2. Identify values and operands.
3. Identify operators inside expressions.
4. Understand how Python evaluates expressions.
5. Write arithmetic expressions.
6. Write expressions using multiple operators.
7. Understand comparison expressions.
8. Understand logical expressions.
9. Perform string concatenation using expressions.
10. Perform string repetition using expressions.
11. Use function calls as expressions.
12. Access list elements using indexing expressions.
13. Extract collection elements using slicing expressions.
14. Use membership expressions.
15. Understand list comprehension expressions.
16. Understand the difference between expressions and statements.
17. Use expressions inside variables.
18. Use expressions inside `print()` statements.
19. Use expressions inside conditional statements.
20. Write expressions for real-world calculations.
21. Evaluate expressions step by step.
22. Understand expression results and data types.
23. Identify common expression-related mistakes.
24. Solve 12 practical programming problems.
25. Attempt 10 additional practice questions.

---

# 3. Prerequisites

Before learning expressions, you should understand these Python fundamentals.

| Concept | Why It Is Required |
|---|---|
| Variables | To store values used in expressions |
| Data Types | To understand integers, floats, strings, and Boolean values |
| Arithmetic Operators | To perform calculations |
| Comparison Operators | To compare values |
| Logical Operators | To combine conditions |
| Membership Operators | To check whether an element exists |
| Strings | To work with text expressions |
| Lists | To access and transform collections |
| Functions | To understand function-call expressions |
| Conditional Statements | To use expressions in decision-making |

You have already studied most of these concepts in the previous folders of this repository.

---

# 4. What Is an Expression?

An expression is a valid combination of Python elements that Python evaluates to produce a value.

These elements may include:

- Constants and literal values.
- Variables.
- Operators.
- Function calls.
- Collection access.
- Slicing.
- Comprehensions.
- Other expressions.

### Basic Examples

```python
10 + 20
```

Result: `30`

```python
100 - 50
```

Result: `50`

```python
5 * 4
```

Result: `20`

```python
20 / 4
```

Result: `5.0`

```python
10 > 5
```

Result: `True`

### Expression Using a Variable

```python
age = 22

age >= 18
```

Result: `True`

### Expression Using a Function

```python
len("Python")
```

Result: `6`

### Expression Using a List

```python
numbers = [10, 20, 30]

numbers[1]
```

Result: `20`

Each example contains a valid expression that Python evaluates to obtain a result.

---

# 5. Components of an Expression

An expression may contain different components.

The most common components are:

1. Operands.
2. Operators.
3. Values.
4. Variables.
5. Function calls.
6. Collection operations.

## 5.1 Operands

Operands are the values or objects on which an operator performs an operation.

Example:

```python
10 + 20
```

Here:

- `10` is an operand.
- `20` is an operand.

## 5.2 Operators

Operators perform operations on operands.

Example:

```python
10 + 20
```

Here, `+` is the operator.

## 5.3 Values

Values are the actual data used in an expression.

Examples:

```python
100
25.5
"Python"
True
None
```

## 5.4 Variables

Variables provide names that refer to objects used in expressions.

Example:

```python
a = 10
b = 20

result = a + b
```

Here, `a` and `b` are variable names used in the expression `a + b`.

## 5.5 Function Calls

A function call can be used inside an expression.

Example:

```python
message = "Python Programming"

length = len(message)

print(length)
```

**Output:**

```text
19
```

The function call `len(message)` produces a value that is used in the assignment.

---

# 6. Types of Expressions in Python

Python supports many types of expressions.

The following are important for beginners.

| Expression Type | Purpose | Example |
|---|---|---|
| Arithmetic | Mathematical calculations | `10 + 20` |
| Comparison | Compare values | `10 > 5` |
| Logical | Combine conditions | `True and False` |
| Bitwise | Perform bit-level operations | `5 & 3` |
| Membership | Check collection membership | `10 in numbers` |
| Identity | Check object identity | `a is b` |
| String | Combine or repeat text | `"Py" + "thon"` |
| Function call | Call a function and use its result | `len("Python")` |
| Indexing | Access a collection element | `numbers[0]` |
| Slicing | Extract part of a collection | `numbers[1:4]` |
| Comprehension | Create collections from iterables | `[x * 2 for x in values]` |
| Conditional | Select a value based on a condition | `"Pass" if marks >= 40 else "Fail"` |

These categories are not mutually exclusive. A single expression can combine multiple operations.

For example:

```python
result = (10 + 20) * 2 > 50
```

This expression combines arithmetic and comparison operations.

---

# 7. Arithmetic Expressions

Arithmetic expressions perform mathematical calculations.

Python provides the following arithmetic operators:

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `11 // 5` | `2` |
| `%` | Modulus | `11 % 5` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Example 1: Addition

```python
a = 10
b = 20

result = a + b

print(result)
```

**Output:**

```text
30
```

### Example 2: Subtraction

```python
a = 50
b = 20

result = a - b

print(result)
```

**Output:**

```text
30
```

### Example 3: Multiplication

```python
a = 10
b = 5

result = a * b

print(result)
```

**Output:**

```text
50
```

### Example 4: Division

```python
a = 20
b = 4

result = a / b

print(result)
```

**Output:**

```text
5.0
```

### Example 5: Multiple Arithmetic Operators

```python
a = 10
b = 5
c = 2

result = a + b * c

print(result)
```

**Output:**

```text
20
```

Multiplication is evaluated before addition.

### Practical Applications

Arithmetic expressions are used in:

- Calculating marks.
- Calculating averages.
- Calculating salaries.
- Calculating discounts.
- Calculating tax.
- Calculating areas and perimeters.
- Converting units.
- Solving numerical problems.

---

# 8. Expressions Using Multiple Operators

Python allows multiple operators to be used in a single expression.

Example:

```python
a = 10
b = 5
c = 2

result = a + b * c - 4

print(result)
```

**Output:**

```text
16
```

### Step-by-Step Evaluation

Original expression:

```text
a + b * c - 4
```

Substitute the values:

```text
10 + 5 * 2 - 4
```

Multiplication:

```text
10 + 10 - 4
```

Addition:

```text
20 - 4
```

Subtraction:

```text
16
```

### Another Example

```python
x = 20
y = 10
z = 5

result = x / y + z * 2

print(result)
```

**Output:**

```text
12.0
```

### Important Point

When an expression contains multiple operators, Python follows its operator precedence and associativity rules.

These rules will be covered in dedicated subtopics:

- Operator Precedence.
- Operator Associativity.
- Parentheses and Grouping.

---

# 9. Comparison Expressions

Comparison expressions compare values and return Boolean results.

The result is either:

- `True`
- `False`

### Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Example

```python
age = 22

result = age >= 18

print(result)
```

**Output:**

```text
True
```

### Example 2: Marks Comparison

```python
marks = 75

result = marks >= 40

print(result)
```

**Output:**

```text
True
```

### Example 3: Two Values

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
```

**Output:**

```text
False
True
True
False
```

### Practical Applications

Comparison expressions are used for:

- Checking age eligibility.
- Checking passing marks.
- Comparing prices.
- Checking salary limits.
- Validating input ranges.
- Comparing two numbers.

---

# 10. Logical Expressions

Logical expressions combine or reverse conditions.

Python provides three logical operators:

- `and`
- `or`
- `not`

### Example 1: AND Expression

```python
age = 22
has_id = True

result = age >= 18 and has_id

print(result)
```

**Output:**

```text
True
```

Both conditions are true.

### Example 2: OR Expression

```python
marks = 85
attendance = 60

result = marks >= 90 or attendance >= 75

print(result)
```

**Output:**

```text
False
```

Neither condition is true.

### Example 3: NOT Expression

```python
is_raining = False

result = not is_raining

print(result)
```

**Output:**

```text
True
```

### Practical Application

A student may need to satisfy more than one condition to pass.

```python
marks = 65
attendance = 80

passed = marks >= 40 and attendance >= 75

print(passed)
```

**Output:**

```text
True
```

Both marks and attendance requirements are satisfied.

---

# 11. String Concatenation Expressions

String concatenation means joining two or more strings.

Python uses the `+` operator for concatenation.

### Syntax

```python
string1 + string2
```

### Example 1: Joining Two Strings

```python
first_name = "Amaan"

last_name = "Syed"

full_name = first_name + " " + last_name

print(full_name)
```

**Output:**

```text
Amaan Syed
```

### Explanation

The expression combines:

- First name.
- A space.
- Last name.

The resulting string is `"Amaan Syed"`.

### Example 2: Joining Multiple Strings

```python
first = "Python"

second = "is"

third = "easy"

message = first + " " + second + " " + third

print(message)
```

**Output:**

```text
Python is easy
```

### Example 3: Concatenation with Variables

```python
language = "Python"

topic = "Expressions"

message = "Learning " + language + " " + topic

print(message)
```

**Output:**

```text
Learning Python Expressions
```

### Important Rule

The `+` operator can concatenate strings, but it does not automatically convert every data type into a string.

Incorrect:

```python
age = 22

# message = "Age: " + age
```

This raises a `TypeError`.

Correct:

```python
age = 22

message = "Age: " + str(age)

print(message)
```

**Output:**

```text
Age: 22
```

You can also use f-strings:

```python
age = 22

message = f"Age: {age}"

print(message)
```

---

# 12. String Repetition Expressions

Python allows strings to be repeated using the `*` operator and an integer.

### Syntax

```python
string * number
```

### Example 1

```python
message = "Python "

result = message * 3

print(result)
```

**Output:**

```text
Python Python Python
```

### Example 2

```python
symbol = "*"

result = symbol * 10

print(result)
```

**Output:**

```text
**********
```

### Example 3: Pattern Printing

```python
for i in range(1, 6):
    print("*" * i)
```

**Output:**

```text
*
**
***
****
*****
```

### Example 4: Repeating a Message

```python
message = "Welcome "

print(message * 4)
```

**Output:**

```text
Welcome Welcome Welcome Welcome
```

### Practical Applications

String repetition is useful for:

- Pattern printing.
- Creating separators.
- Generating simple text layouts.
- Displaying repeated symbols.
- Creating basic console designs.

### Important Rule

The repetition count must be an integer.

---

# 13. Function Call Expressions

A function call can be used as an expression because it produces a return value.

### Example

```python
message = "Python Programming"

result = len(message)

print(result)
```

**Output:**

```text
19
```

Here:

```python
len(message)
```

is a function call expression.

The function returns the length of the string.

### Example 2: Using `max()`

```python
numbers = [10, 40, 20, 30]

result = max(numbers)

print(result)
```

**Output:**

```text
40
```

### Example 3: Using `min()`

```python
numbers = [10, 40, 20, 30]

result = min(numbers)

print(result)
```

**Output:**

```text
10
```

### Example 4: Using `sum()`

```python
numbers = [10, 20, 30, 40]

result = sum(numbers)

print(result)
```

**Output:**

```text
100
```

### Example 5: Nested Function Calls

```python
text = "  Python  "

result = len(text.strip())

print(result)
```

**Output:**

```text
6
```

The inner function call removes surrounding whitespace.

The outer function call calculates the resulting string length.

### Important Point

A function may return:

- An integer.
- A float.
- A string.
- A Boolean.
- A list.
- A dictionary.
- Another object.
- `None`.

Not every function returns a useful non-None value.

---

# 14. List Indexing Expressions

Indexing expressions access a particular element from a collection.

Lists use square brackets for indexing.

### Syntax

```python
list_name[index]
```

Python list indexing starts from zero.

| Index | Position |
|---|---|
| `0` | First element |
| `1` | Second element |
| `2` | Third element |
| `3` | Fourth element |
| `-1` | Last element |

### Example

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[2]

print(result)
```

**Output:**

```text
30
```

### Explanation

The list contains:

```text
Index:  0   1   2   3   4
Value: 10  20  30  40  50
```

The expression `numbers[2]` accesses the third element.

### Negative Indexing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])
```

**Output:**

```text
50
40
```

### Important Rule

Using an invalid list index raises `IndexError`.

For example:

```python
numbers = [10, 20, 30]

# numbers[5] raises IndexError
```

---

# 15. List Slicing Expressions

Slicing is used to extract a portion of a sequence.

### Syntax

```python
sequence[start:stop:step]
```

| Parameter | Meaning |
|---|---|
| `start` | Starting index, included |
| `stop` | Ending boundary, excluded |
| `step` | Difference between selected indices |

### Example 1: Basic Slicing

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[1:4]

print(result)
```

**Output:**

```text
[20, 30, 40]
```

### Explanation

Python selects indexes:

```text
1, 2, 3
```

Index `4` is excluded.

### Example 2: Starting from the Beginning

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

**Output:**

```text
[10, 20, 30]
```

### Example 3: From an Index to the End

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
```

**Output:**

```text
[30, 40, 50]
```

### Example 4: Step

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])
```

**Output:**

```text
[10, 30, 50]
```

### Example 5: Reverse a List

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
```

**Output:**

```text
[50, 40, 30, 20, 10]
```

### Important Point

Slicing usually creates a new outer sequence of the same sequence type.

For a list, the new list contains references to the selected elements. It is not necessarily a deep copy of nested objects.

---

# 16. Membership Expressions

A membership expression checks whether an element exists inside a supported collection.

### Example

```python
languages = ["Python", "Java", "C++"]

result = "Python" in languages

print(result)
```

**Output:**

```text
True
```

### Using `not in`

```python
languages = ["Python", "Java", "C++"]

result = "Ruby" not in languages

print(result)
```

**Output:**

```text
True
```

### Using Membership in an IF Condition

```python
allowed_roles = ["admin", "editor", "viewer"]

role = "editor"

if role in allowed_roles:
    print("Access allowed")
else:
    print("Access denied")
```

**Output:**

```text
Access allowed
```

### Practical Applications

- Checking registered users.
- Searching products.
- Checking allowed values.
- Validating file extensions.
- Checking available subjects.
- Filtering data.

For more detailed membership concepts, refer to:

`../06-Membership-Operators/README.md`

---

# 17. List Comprehension Expressions

A list comprehension provides a concise way to create a list based on an iterable.

### General Syntax

```python
[expression for item in iterable]
```

An optional condition can also be included:

```python
[expression for item in iterable if condition]
```

### Example 1: Squares of Numbers

```python
numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

### Step-by-Step Explanation

1. Python reads an element from `numbers`.
2. The current element is assigned to `number`.
3. The expression `number * number` is evaluated.
4. The result is added to the new list.
5. The process repeats for every element.

### Example 2: Extract Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

### Example 3: Convert Strings to Uppercase

```python
names = ["amaan", "rahul", "arjun"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)
```

**Output:**

```text
['AMAAN', 'RAHUL', 'ARJUN']
```

### Important Difference

A list comprehension is an expression that creates a list.

It can be used wherever an expression is accepted.

---

# 18. Expressions Inside Print Statements

Expressions can be evaluated directly inside `print()`.

### Example 1

```python
print(10 + 20)
```

**Output:**

```text
30
```

### Example 2

```python
a = 10
b = 5

print(a * b)
```

**Output:**

```text
50
```

### Example 3

```python
name = "Amaan"

print("Hello " + name)
```

**Output:**

```text
Hello Amaan
```

### Example 4: Multiple Expressions

```python
a = 10
b = 20

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
```

**Output:**

```text
Sum: 30
Difference: -10
Product: 200
```

### Example 5: F-Strings

```python
name = "Amaan"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```text
My name is Amaan and I am 22 years old.
```

Expressions can also be placed inside f-string replacement fields:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

**Output:**

```text
Sum = 30
```

---

# 19. Expressions Inside Conditional Statements

Expressions are commonly used as conditions in `if`, `elif`, and `while` statements.

### Example 1: Positive Number

```python
number = 10

if number > 0:
    print("Positive number")
```

**Output:**

```text
Positive number
```

The expression `number > 0` produces a Boolean result.

### Example 2: Even or Odd

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**

```text
Odd
```

The expression:

```python
number % 2 == 0
```

checks whether the number is divisible by two.

### Example 3: Student Eligibility

```python
age = 22
attendance = 85

if age >= 18 and attendance >= 75:
    print("Eligible")
else:
    print("Not eligible")
```

**Output:**

```text
Eligible
```

### Example 4: While Condition

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

**Output:**

```text
1
2
3
```

The expression `count <= 3` is evaluated before each iteration.

---

# 20. Expressions and Data Types

The result of an expression has a data type.

Different operations can produce different result types.

### Example 1: Integer Result

```python
result = 10 + 20

print(result)
print(type(result))
```

**Output:**

```text
30
<class 'int'>
```

### Example 2: Float Result

```python
result = 10 / 2

print(result)
print(type(result))
```

**Output:**

```text
5.0
<class 'float'>
```

### Example 3: Boolean Result

```python
result = 10 > 5

print(result)
print(type(result))
```

**Output:**

```text
True
<class 'bool'>
```

### Example 4: String Result

```python
result = "Python" + " Programming"

print(result)
print(type(result))
```

**Output:**

```text
Python Programming
<class 'str'>
```

### Example 5: List Result

```python
numbers = [1, 2, 3]

result = [number * 2 for number in numbers]

print(result)
print(type(result))
```

**Output:**

```text
[2, 4, 6]
<class 'list'>
```

### Remember

An expression's result type depends on the operation and the objects involved.

---

# 21. Expressions vs Statements

Expressions and statements are related but different concepts.

### What Is an Expression?

An expression is a piece of Python code that can be evaluated to produce a value.

Examples:

```python
10 + 20
```

```python
a > b
```

```python
len("Python")
```

### What Is a Statement?

A statement is a complete instruction that Python executes.

Examples:

```python
a = 10
```

```python
print("Hello")
```

```python
if a > 5:
    print("Greater")
```

### Important Difference

| Expression | Statement |
|---|---|
| Produces a value | Performs an instruction |
| Can be used as part of larger expressions | Forms a unit of program execution |
| Examples: `10 + 20`, `a > b` | Examples: assignment and `if` statement |
| Often used inside statements | Can contain expressions |

### Example: Assignment

```python
a = 10 + 20
```

Here:

- `10 + 20` is an expression.
- `a = 10 + 20` is an assignment statement.

### Example: If Statement

```python
age = 22

if age >= 18:
    print("Eligible")
```

Here:

- `age >= 18` is an expression.
- The complete `if` construct is a compound statement.

### Important Technical Note

Python also supports assignment expressions using the `:=` operator.

These are different from ordinary assignment statements.

Example:

```python
if (length := len("Python")) > 5:
    print(length)
```

**Output:**

```text
6
```

Assignment expressions are an advanced topic. For now, focus on understanding ordinary expressions and statements.

---

# 22. Understanding Expression Evaluation

Expression evaluation means calculating the result of an expression.

Consider:

```python
a = 10
b = 5
c = 2

result = a + b * c
```

The expression is:

```text
a + b * c
```

Python evaluates it according to its precedence rules.

### Dry Run

| Step | Operation | Result |
|---|---|---|
| 1 | `b * c` | `10` |
| 2 | `a + 10` | `20` |
| 3 | Assign result | `20` |

### Another Example

```python
a = 20
b = 10
c = 5

result = (a + b) * c
```

**Output:**

```text
150
```

Dry run:

```text
(20 + 10) * 5
30 * 5
150
```

### Why Do Parentheses Matter?

Parentheses make the intended grouping explicit.

They are useful when an expression contains multiple operations.

The next topic will cover operator precedence and evaluation order in more detail.

---

# 23. Expressions Using Parentheses

Parentheses can group parts of an expression.

### Example 1

```python
result = (10 + 20) * 2

print(result)
```

**Output:**

```text
60
```

### Example 2

```python
result = 10 + (20 * 2)

print(result)
```

**Output:**

```text
50
```

### Example 3: Average

```python
a = 10
b = 20
c = 30

average = (a + b + c) / 3

print(average)
```

**Output:**

```text
20.0
```

### Best Practice

Use parentheses to make complicated expressions easier to read and understand.

---

# 24. Expressions in Real-World Mathematical Formulas

Expressions are useful for translating mathematical formulas into Python code.

## 24.1 Area of Rectangle

Formula:

\[
A = l \times w
\]

Python:

```python
length = 10
width = 5

area = length * width

print(area)
```

Output:

```text
50
```

## 24.2 Perimeter of Rectangle

Formula:

\[
P = 2(l+w)
\]

Python:

```python
length = 10
width = 5

perimeter = 2 * (length + width)

print(perimeter)
```

Output:

```text
30
```

## 24.3 Average

Formula:

\[
Average = \frac{a+b+c}{3}
\]

Python:

```python
a = 70
b = 80
c = 90

average = (a + b + c) / 3

print(average)
```

Output:

```text
80.0
```

## 24.4 Simple Interest

Formula:

\[
SI = \frac{P \times R \times T}{100}
\]

Python:

```python
principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print(simple_interest)
```

Output:

```text
1000.0
```

## 24.5 Celsius to Fahrenheit

Formula:

\[
F = \frac{9C}{5} + 32
\]

Python:

```python
celsius = 25

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)
```

Output:

```text
77.0
```

## 24.6 Percentage

Formula:

\[
Percentage = \frac{Obtained Marks}{Maximum Marks} \times 100
\]

Python:

```python
obtained_marks = 420
maximum_marks = 500

percentage = (obtained_marks / maximum_marks) * 100

print(percentage)
```

Output:

```text
84.0
```

### Important Point

When converting mathematical formulas into Python, identify the correct operators and use parentheses to preserve the intended calculation.

---

# 25. Expressions with User Input

Expressions frequently use values entered by users.

Remember that the `input()` function returns a string.

If you need numerical calculations, convert the input to an appropriate numeric type.

### Example 1: Addition

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a + b

print("Sum:", result)
```

### Example Output

```text
Enter first number: 10
Enter second number: 20
Sum: 30
```

### Example 2: Average

```python
a = float(input("Enter first mark: "))
b = float(input("Enter second mark: "))
c = float(input("Enter third mark: "))

average = (a + b + c) / 3

print("Average:", average)
```

### Example Output

```text
Enter first mark: 70
Enter second mark: 80
Enter third mark: 90
Average: 80.0
```

### Example 3: Comparison

```python
age = int(input("Enter your age: "))

result = age >= 18

print("Eligible:", result)
```

### Common Mistake

Incorrect:

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

If the user enters `10` and `20`, the output is:

```text
1020
```

This happens because the inputs are strings and `+` concatenates them.

Correct:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

---

# 26. Expressions with Functions

Expressions can use both built-in functions and user-defined functions.

### Example 1: Built-in Function

```python
numbers = [10, 20, 30, 40]

result = sum(numbers)

print(result)
```

Output:

```text
100
```

### Example 2: User-Defined Function

```python
def square(number):
    return number * number


result = square(5)

print(result)
```

Output:

```text
25
```

### Example 3: Function Inside an Expression

```python
def square(number):
    return number * number


result = square(5) + square(3)

print(result)
```

Output:

```text
34
```

Step by step:

```text
square(5) + square(3)
25 + 9
34
```

### Important Point

The returned values of function calls can be used as operands in larger expressions.

---

# 27. Important Rules and Edge Cases

## Rule 1: Division by Zero

```python
# result = 10 / 0
```

This raises `ZeroDivisionError`.

Always validate denominators when they can come from user input.

## Rule 2: Integer Division and Normal Division Are Different

```python
print(10 / 3)
print(10 // 3)
```

Output:

```text
3.3333333333333335
3
```

## Rule 3: String and Integer Addition

```python
# "Age: " + 22
```

This raises `TypeError`.

Convert the number or use an f-string.

## Rule 4: Invalid Indexing

```python
numbers = [10, 20, 30]

# numbers[5]
```

This raises `IndexError`.

## Rule 5: Slicing Stop Is Excluded

```python
numbers = [10, 20, 30, 40]

print(numbers[1:3])
```

Output:

```text
[20, 30]
```

## Rule 6: Comparison Expressions Return Boolean Values

```python
print(10 > 5)
```

Output:

```text
True
```

## Rule 7: Some Functions Return None

```python
result = print("Hello")

print(result)
```

Output:

```text
Hello
None
```

## Rule 8: Floating-Point Arithmetic Can Be Approximate

```python
result = 0.1 + 0.2

print(result)
```

The result may display:

```text
0.30000000000000004
```

This happens because many decimal fractions cannot be represented exactly in binary floating-point format.

When comparing approximate floating-point results, consider `math.isclose()`.

## Rule 9: Empty Collections Are Different from None

```python
numbers = []

print(numbers)
print(numbers is None)
```

Output:

```text
[]
False
```

## Rule 10: Assignment Is Not Ordinary Value Evaluation

```python
a = 10
```

This is an assignment statement.

The expression on the right-hand side produces a value that is assigned to the name.

---

# 28. Time Complexity of Common Expressions

Not every expression has the same computational cost.

The cost depends on the operation and the objects involved.

| Operation | Typical Complexity |
|---|---|
| Basic integer addition | Constant-time for bounded machine-size values; Python integers are arbitrary precision |
| Basic multiplication | Depends on integer sizes |
| List indexing | \(O(1)\) |
| List slicing | \(O(k)\), where \(k\) is the output length |
| String concatenation | Depends on the total string lengths |
| String repetition | Depends on output length |
| List comprehension | Depends on number of input elements and work per element |
| List membership | \(O(n)\) worst case |
| Set membership | Average \(O(1)\) |
| Dictionary key lookup | Average \(O(1)\) |
| `len()` on built-in list or string | \(O(1)\) |

### Why Is Complexity Important?

When working with large data, understanding operation costs can help you build faster programs.

For example:

- List indexing is usually constant time.
- Searching a large list is linear in the worst case.
- Set membership is generally average-case constant time.
- Creating a list of transformed elements requires processing all input elements.

These differences become especially important in DSA.

---

# 29. Twelve Examples Explained

The Python file `01_expressions.py` contains twelve examples.

Each example demonstrates a different way to form and evaluate an expression.

## Example 1: Basic Arithmetic Expression

**Objective:** Perform addition using an expression.

```python
a = 10
b = 5

result = a + b

print(result)
```

**Output:**

```text
15
```

**Explanation:**

1. Store two numbers.
2. Use the `+` operator.
3. Evaluate the expression.
4. Store the result.
5. Print the result.

**Concept:** Arithmetic expressions.

## Example 2: Multiple Operator Expression

```python
a = 10
b = 5
c = 2

result = a + b * c

print(result)
```

**Output:**

```text
20
```

**Explanation:**

Python evaluates multiplication before addition.

**Concept:** Multiple operators inside one expression.

## Example 3: Division Expression

```python
a = 20
b = 4

result = a / b

print(result)
print(type(result).__name__)
```

**Output:**

```text
5.0
float
```

**Explanation:**

The `/` operator performs normal division and returns a floating-point result.

**Concept:** Division expressions and data types.

## Example 4: Comparison Expression

```python
age = 22
voting_age = 18

result = age >= voting_age

print(result)
```

**Output:**

```text
True
```

**Explanation:**

The expression checks whether the age is greater than or equal to the required age.

**Concept:** Comparison expressions.

## Example 5: Logical Expression

```python
age = 22
has_id = True

result = age >= 18 and has_id

print(result)
```

**Output:**

```text
True
```

**Explanation:**

Both eligibility conditions are satisfied.

**Concept:** Logical expressions.

## Example 6: String Concatenation Expression

```python
first_name = "Amaan"
last_name = "Syed"

full_name = first_name + " " + last_name

print(full_name)
```

**Output:**

```text
Amaan Syed
```

**Explanation:**

The `+` operator joins the strings with a space between them.

**Concept:** String concatenation.

## Example 7: String Repetition Expression

```python
message = "Python "

result = message * 3

print(result)
```

**Output:**

```text
Python Python Python
```

**Explanation:**

The string is repeated three times.

**Concept:** String repetition.

## Example 8: Function Call Expression

```python
language = "Python Programming"

result = len(language)

print(result)
```

**Output:**

```text
19
```

**Explanation:**

The `len()` function returns the number of characters in the string, including the space.

**Concept:** Function call expressions.

## Example 9: List Indexing Expression

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[2]

print(result)
```

**Output:**

```text
30
```

**Explanation:**

List indexing starts from zero. Index 2 refers to the third element.

**Concept:** Indexing expressions.

## Example 10: List Slicing Expression

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[1:4]

print(result)
```

**Output:**

```text
[20, 30, 40]
```

**Explanation:**

The expression selects values at indexes 1, 2, and 3. The stop index 4 is excluded.

**Concept:** Slicing expressions.

## Example 11: Membership Expression

```python
languages = ["Python", "Java", "C++"]

result = "Python" in languages

print(result)
```

**Output:**

```text
True
```

**Explanation:**

The expression checks whether `"Python"` exists in the list.

**Concept:** Membership expressions.

## Example 12: List Comprehension Expression

```python
numbers = [1, 2, 3, 4, 5, 6]

result = [number * number for number in numbers]

print(result)
```

**Output:**

```text
[1, 4, 9, 16, 25, 36]
```

**Explanation:**

1. Take each number from the original list.
2. Multiply the number by itself.
3. Store the result in a new list.
4. Repeat for every element.

**Concept:** List comprehension expressions.

---

# 30. Twelve Solved Problems

The Python program contains twelve interactive solved problems.

## Problem 1: Addition of Two Numbers

**Problem Statement:**

Take two numbers from the user and calculate their sum using an arithmetic expression.

### Logic

1. Read the first number.
2. Read the second number.
3. Add both numbers.
4. Store the result.
5. Display the sum.

### Code

```python
a = 10
b = 20

result = a + b

print("Sum:", result)
```

**Output:**

```text
Sum: 30
```

### Dry Run

| Variable | Value |
|---|---:|
| `a` | 10 |
| `b` | 20 |
| Expression | `a + b` |
| Result | 30 |

### Concept

Arithmetic expressions and variable usage.

---

## Problem 2: Multiple Operator Expression

**Problem Statement:**

Take three values and evaluate the expression:

\[
a + b \times c
\]

### Code

```python
a = 10
b = 5
c = 2

result = a + b * c

print(result)
```

**Output:**

```text
20
```

### Dry Run

```text
10 + 5 * 2
10 + 10
20
```

### Concept

Multiple operators and expression evaluation.

---

## Problem 3: Average of Three Numbers

**Problem Statement:**

Take three numbers from the user and calculate their average.

### Formula

\[
Average = \frac{a+b+c}{3}
\]

### Code

```python
a = 70
b = 80
c = 90

average = (a + b + c) / 3

print("Average:", average)
```

**Output:**

```text
Average: 80.0
```

### Dry Run

```text
(70 + 80 + 90) / 3
240 / 3
80.0
```

### Concept

Mathematical expressions and parentheses.

---

## Problem 4: Area of a Rectangle

**Problem Statement:**

Calculate the area of a rectangle using length and width.

### Formula

\[
Area = Length \times Width
\]

### Code

```python
length = 10
width = 5

area = length * width

print("Area:", area)
```

**Output:**

```text
Area: 50
```

### Dry Run

```text
10 * 5
50
```

### Concept

Multiplication expressions and mathematical formulas.

---

## Problem 5: Perimeter of a Rectangle

**Problem Statement:**

Calculate the perimeter of a rectangle.

### Formula

\[
Perimeter = 2(Length+Width)
\]

### Code

```python
length = 10
width = 5

perimeter = 2 * (length + width)

print("Perimeter:", perimeter)
```

**Output:**

```text
Perimeter: 30
```

### Dry Run

```text
2 * (10 + 5)
2 * 15
30
```

### Concept

Expressions with grouping parentheses.

---

## Problem 6: Celsius to Fahrenheit

**Problem Statement:**

Convert a temperature from Celsius to Fahrenheit.

### Formula

\[
F = \frac{9C}{5}+32
\]

### Code

```python
celsius = 25

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)
```

**Output:**

```text
Fahrenheit: 77.0
```

### Dry Run

```text
(25 * 9 / 5) + 32
(225 / 5) + 32
45 + 32
77.0
```

### Concept

Multiple arithmetic operations.

---

## Problem 7: Simple Interest

**Problem Statement:**

Calculate simple interest using the principal amount, annual interest rate, and time.

### Formula

\[
SI = \frac{P \times R \times T}{100}
\]

### Code

```python
principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
```

**Output:**

```text
Simple Interest: 1000.0
```

### Dry Run

```text
(10000 * 5 * 2) / 100
100000 / 100
1000.0
```

### Concept

Financial calculations using arithmetic expressions.

---

## Problem 8: Calculate Discounted Price

**Problem Statement:**

Calculate the final price after applying a discount percentage.

### Formula

\[
Discount = \frac{OriginalPrice \times DiscountPercentage}{100}
\]

\[
FinalPrice = OriginalPrice - Discount
\]

### Code

```python
original_price = 2000
discount_percentage = 10

discount = original_price * discount_percentage / 100

final_price = original_price - discount

print("Discount:", discount)
print("Final Price:", final_price)
```

**Output:**

```text
Discount: 200.0
Final Price: 1800.0
```

### Dry Run

```text
Discount = 2000 * 10 / 100
Discount = 200

Final Price = 2000 - 200
Final Price = 1800
```

### Concept

Multiple expressions and real-world price calculations.

---

## Problem 9: Calculate Bill with Tax

**Problem Statement:**

Calculate the final bill after adding tax.

### Formula

\[
Tax = \frac{BillAmount \times TaxPercentage}{100}
\]

\[
TotalBill = BillAmount + Tax
\]

### Code

```python
amount = 1000
tax_percentage = 18

tax_amount = amount * tax_percentage / 100

total_bill = amount + tax_amount

print("Tax:", tax_amount)
print("Total Bill:", total_bill)
```

**Output:**

```text
Tax: 180.0
Total Bill: 1180.0
```

### Dry Run

```text
Tax = 1000 * 18 / 100
Tax = 180

Total = 1000 + 180
Total = 1180
```

### Concept

Arithmetic expressions and financial calculations.

---

## Problem 10: Convert Seconds into Minutes and Seconds

**Problem Statement:**

Take a number of seconds and convert it into minutes and remaining seconds.

### Formulas

\[
Minutes = TotalSeconds // 60
\]

\[
RemainingSeconds = TotalSeconds \% 60
\]

### Code

```python
total_seconds = 125

minutes = total_seconds // 60

remaining_seconds = total_seconds % 60

print("Minutes:", minutes)
print("Remaining Seconds:", remaining_seconds)
```

**Output:**

```text
Minutes: 2
Remaining Seconds: 5
```

### Dry Run

```text
125 // 60 = 2

125 % 60 = 5
```

Therefore:

```text
2 minutes and 5 seconds
```

### Concept

Floor division and modulus expressions.

---

## Problem 11: Student Pass or Fail

**Problem Statement:**

Check whether a student passes based on marks and attendance.

Conditions:

- Marks must be at least 40.
- Attendance must be at least 75%.

### Code

```python
marks = 65

attendance = 80

passed = marks >= 40 and attendance >= 75

if passed:
    print("PASS")
else:
    print("FAIL")
```

**Output:**

```text
PASS
```

### Dry Run

| Condition | Result |
|---|---|
| `marks >= 40` | `True` |
| `attendance >= 75` | `True` |
| Both using `and` | `True` |

### Concept

Comparison and logical expressions.

---

## Problem 12: Palindrome Check

**Problem Statement:**

Check whether the entered word or sentence is a palindrome, ignoring uppercase and lowercase differences and ordinary spaces.

A palindrome reads the same forward and backward.

Examples:

```text
madam
level
radar
```

### Code

```python
text = "Madam"

normalized = text.casefold().replace(" ", "")

reversed_text = normalized[::-1]

is_palindrome = normalized == reversed_text

print(is_palindrome)
```

**Output:**

```text
True
```

### Step-by-Step Explanation

Original value:

```text
Madam
```

Convert to case-insensitive form:

```text
madam
```

Remove ordinary spaces:

```text
madam
```

Reverse the text:

```text
madam
```

Compare both strings:

```text
madam == madam
```

Result:

```text
True
```

### Important Limitation

The supplied program removes ordinary spaces and ignores case. It does not remove punctuation or every type of whitespace.

For example, `"A man, a plan"` is not automatically normalized into punctuation-free text by that program.

### Concept

String methods, slicing expressions, and comparison expressions.

---

# 31. Ten Unsolved Practice Questions

Attempt these questions independently before referring to other solutions.

| No. | Practice Question | Hint |
|---|---|---|
| 1 | Take two numbers and calculate their difference. | Use subtraction |
| 2 | Take three numbers and calculate their product. | Use multiplication |
| 3 | Calculate the average of five subject marks. | Add and divide by five |
| 4 | Calculate the area of a triangle. | Use `0.5 * base * height` |
| 5 | Convert kilometres into metres. | Multiply by 1000 |
| 6 | Calculate the final price after a discount. | Calculate and subtract discount |
| 7 | Find the quotient and remainder of two integers. | Use `//` and `%` |
| 8 | Check whether a number is positive. | Use a comparison expression |
| 9 | Check whether a student satisfies two conditions. | Use `and` |
| 10 | Reverse a string using a slicing expression. | Use `text[::-1]` |

## Additional Challenge Problems

### Challenge 1: Electricity Bill

Calculate an electricity bill using units consumed and price per unit.

### Challenge 2: Shopping Total

Calculate the total price of multiple products and apply a discount.

### Challenge 3: Speed Calculation

Calculate speed using distance and time.

Formula:

\[
Speed = \frac{Distance}{Time}
\]

### Challenge 4: Percentage Calculator

Take obtained marks and total marks and calculate percentage.

### Challenge 5: Even and Odd

Use the modulus expression to check whether an entered number is even or odd.

### Challenge 6: Largest of Three Numbers

Use comparison expressions to find the largest number.

### Challenge 7: String Length Check

Check whether a string contains more than ten characters.

### Challenge 8: Word Counter

Use string methods to count whitespace-separated words.

### Challenge 9: Temperature Conversion

Convert Fahrenheit into Celsius.

### Challenge 10: Palindrome Challenge

Write a palindrome program that ignores case, spaces, and punctuation.

---

# 32. Common Mistakes and Their Solutions

## Mistake 1: Forgetting Operator Precedence

Incorrect expectation:

```python
result = 10 + 5 * 2
```

The result is `20`, not `30`.

Use parentheses when necessary:

```python
result = (10 + 5) * 2
```

Result:

```text
30
```

## Mistake 2: Performing String and Integer Addition

Incorrect:

```python
age = 22

# "Age: " + age
```

Correct:

```python
print("Age:", age)
```

Or:

```python
print("Age: " + str(age))
```

Or:

```python
print(f"Age: {age}")
```

## Mistake 3: Forgetting Input Conversion

Incorrect:

```python
a = input("Enter number: ")
b = input("Enter number: ")

print(a + b)
```

For inputs `10` and `20`, this produces `1020`.

Correct:

```python
a = int(input("Enter number: "))
b = int(input("Enter number: "))

print(a + b)
```

## Mistake 4: Division by Zero

Incorrect:

```python
result = 10 / 0
```

This raises `ZeroDivisionError`.

Correct:

```python
denominator = 0

if denominator != 0:
    result = 10 / denominator
else:
    print("Cannot divide by zero")
```

## Mistake 5: Invalid List Index

Incorrect:

```python
numbers = [10, 20, 30]

# print(numbers[5])
```

Correct:

```python
if len(numbers) > 5:
    print(numbers[5])
else:
    print("Index does not exist")
```

## Mistake 6: Confusing Indexing and Slicing

Indexing returns one element.

```python
numbers[2]
```

Slicing returns a portion of a collection.

```python
numbers[1:4]
```

## Mistake 7: Forgetting That Slicing Stop Is Exclusive

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Index 4 is excluded.

## Mistake 8: Forgetting String Case

```python
print("python" == "Python")
```

Output:

```text
False
```

## Mistake 9: Assuming Every Function Returns a Value

```python
def display():
    print("Hello")

result = display()

print(result)
```

Output:

```text
Hello
None
```

## Mistake 10: Incorrect Parentheses

Compare:

```python
a = 10
b = 20
c = 30

print((a + b) * c)
print(a + b * c)
```

Output:

```text
900
610
```

Parentheses change the grouping.

---

# 33. Best Practices

Follow these practices while writing Python expressions.

1. Use meaningful variable names.
2. Keep complicated expressions readable.
3. Use parentheses to communicate grouping.
4. Convert user input to the required data type.
5. Validate values before performing calculations.
6. Avoid division by zero.
7. Use `==` for value comparisons.
8. Use `is` for identity checks.
9. Use f-strings for readable string formatting.
10. Use slicing carefully.
11. Understand indexing before accessing list elements.
12. Break very complicated expressions into smaller calculations.
13. Avoid repeating expensive calculations unnecessarily.
14. Use built-in functions when they make code simpler.
15. Check output types when operations may return different data types.
16. Be careful with floating-point calculations.
17. Use descriptive intermediate variables.
18. Test expressions with positive, negative, and boundary values.
19. Handle invalid input.
20. Write expressions that another programmer can easily understand.

### Example: Readable vs Unreadable Expression

Less readable:

```python
result = ((a + b) * (c - d) / e) + f ** 2
```

More readable:

```python
sum_values = a + b
difference = c - d
product = sum_values * difference
division_result = product / e
square_result = f ** 2

result = division_result + square_result
```

The second version is easier to debug and maintain.

---

# 34. Debugging and Troubleshooting

When an expression produces an unexpected result, follow these steps.

## Step 1: Print Input Values

```python
print(a)
print(b)
```

## Step 2: Check Data Types

```python
print(type(a))
print(type(b))
```

## Step 3: Print Intermediate Results

```python
first_result = a + b

print("First result:", first_result)
```

## Step 4: Check Parentheses

Review the grouping of operators.

## Step 5: Check Input Conversion

Remember that `input()` returns a string.

## Step 6: Check Division

Make sure the denominator is not zero.

## Step 7: Check Index Boundaries

Verify that list indexes are valid.

## Step 8: Check Slicing Boundaries

Remember that the stopping index is excluded.

## Step 9: Check Function Return Values

```python
result = some_function()

print(result)
print(type(result))
```

## Step 10: Test a Smaller Expression

Break a complicated expression into simpler parts and inspect each result.

---

# 35. Practice Test

Solve these questions without executing the code first.

## Question 1

What is the output?

```python
a = 10
b = 20

print(a + b)
```

## Question 2

What is the output?

```python
a = 10
b = 5
c = 2

print(a + b * c)
```

## Question 3

What is the output?

```python
print(20 / 4)
```

## Question 4

What is the output?

```python
print(10 > 5)
```

## Question 5

What is the output?

```python
print(True and False)
```

## Question 6

What is the output?

```python
first = "Python"
second = "Programming"

print(first + " " + second)
```

## Question 7

What is the output?

```python
print("Hi " * 3)
```

## Question 8

What is the output?

```python
print(len("Python"))
```

## Question 9

What is the output?

```python
numbers = [10, 20, 30, 40]

print(numbers[2])
```

## Question 10

What is the output?

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

## Question 11

What is the output?

```python
languages = ["Python", "Java"]

print("Python" in languages)
```

## Question 12

What is the output?

```python
numbers = [1, 2, 3, 4]

result = [x * 2 for x in numbers]

print(result)
```

## Answer Key

| Question | Answer |
|---|---|
| 1 | `30` |
| 2 | `20` |
| 3 | `5.0` |
| 4 | `True` |
| 5 | `False` |
| 6 | `Python Programming` |
| 7 | `Hi Hi Hi` |
| 8 | `6` |
| 9 | `30` |
| 10 | `[20, 30, 40]` |
| 11 | `True` |
| 12 | `[2, 4, 6, 8]` |

---

# 36. Viva Questions and Answers

Prepare these questions for college practical examinations and technical interviews.

## A. Basic Questions

**Q1. What is an expression in Python?**

An expression is a combination of Python elements that produces a value when evaluated.

**Q2. Give an example of an expression.**

`10 + 20` is an arithmetic expression.

**Q3. What are operands?**

Operands are the values or objects on which operators perform operations.

**Q4. What are operators?**

Operators are symbols or keywords that perform operations on operands.

**Q5. Can an expression contain variables?**

Yes.

**Q6. Can an expression contain function calls?**

Yes.

**Q7. What does an expression produce?**

An expression produces a value or an object.

**Q8. Can an expression produce a Boolean result?**

Yes. A comparison expression such as `10 > 5` produces `True`.

**Q9. Can expressions be used inside print statements?**

Yes.

**Q10. Can expressions be used in conditional statements?**

Yes.

## B. Arithmetic and Comparison Questions

**Q11. What is an arithmetic expression?**

An expression that performs mathematical calculations.

**Q12. Which operator performs addition?**

`+`.

**Q13. Which operator performs multiplication?**

`*`.

**Q14. What is the difference between `/` and `//`?**

`/` performs normal division, while `//` performs floor division.

**Q15. What does the modulus operator do?**

It returns the remainder of division.

**Q16. What is an exponentiation expression?**

An expression that uses `**` to calculate a power.

**Q17. What is a comparison expression?**

An expression that compares values and returns a Boolean result.

**Q18. What is a logical expression?**

An expression that uses logical operators to combine or reverse conditions.

**Q19. What is the output of `10 > 5`?**

`True`.

**Q20. What is the output of `True and False`?**

`False`.

## C. String and Collection Questions

**Q21. What is string concatenation?**

Joining two or more strings into one string.

**Q22. Which operator is used for string concatenation?**

`+`.

**Q23. How do you repeat a string?**

Use the `*` operator with an integer.

**Q24. What does `len()` do?**

It returns the length of an object that supports the built-in length operation.

**Q25. What is a function call expression?**

A function call used to obtain a return value.

**Q26. What is indexing?**

Accessing a particular element using its position.

**Q27. What is slicing?**

Extracting a portion of a sequence.

**Q28. Does list indexing start from zero?**

Yes.

**Q29. Is the stopping index included in slicing?**

No.

**Q30. What is a list comprehension?**

A concise expression for creating a list from an iterable.

## D. Expressions and Statements

**Q31. What is the difference between expressions and statements?**

An expression is evaluated to produce a value, while a statement is a complete instruction executed by Python.

**Q32. Is `10 + 20` an expression?**

Yes.

**Q33. Is `a = 10` an ordinary expression?**

No. It is an assignment statement.

**Q34. Is `len("Python")` an expression?**

Yes.

**Q35. What is an assignment expression?**

An expression that uses `:=` to assign a value while producing that value.

**Q36. What is expression evaluation?**

The process of calculating or determining the result of an expression.

**Q37. Can multiple operators appear in one expression?**

Yes.

**Q38. Why are parentheses used in expressions?**

They group parts of an expression and make the intended evaluation clearer.

## E. Practical Questions

**Q39. How do you calculate the average of three numbers?**

Use `(a + b + c) / 3`.

**Q40. How do you calculate the area of a rectangle?**

Use `length * width`.

**Q41. How do you calculate simple interest?**

Use `(principal * rate * time) / 100`.

**Q42. How do you convert Celsius to Fahrenheit?**

Use `(celsius * 9 / 5) + 32`.

**Q43. How do you check whether a number is even?**

Check whether `number % 2 == 0`.

**Q44. How do you reverse a string using slicing?**

Use `text[::-1]`.

**Q45. How can a list comprehension create squares?**

Use `[x * x for x in numbers]`.

**Q46. What is the result of a function without an explicit return statement?**

`None`.

**Q47. What error occurs when dividing an integer by zero?**

`ZeroDivisionError`.

**Q48. What error occurs when accessing an invalid list index?**

`IndexError`.

**Q49. Why should user input be converted before numerical calculations?**

Because `input()` returns a string.

**Q50. Why are expressions important in programming?**

They allow programs to calculate values, compare information, make decisions, and transform data.

---

# 37. Connection with Data Structures and Algorithms (DSA)

Expressions are used throughout DSA.

Almost every algorithm contains expressions for:

- Calculations.
- Comparisons.
- Indexing.
- Loop conditions.
- Updates.
- Searching.
- Filtering.
- Data transformation.

## 37.1 Array Indexing

```python
numbers = [10, 20, 30, 40]

middle = numbers[2]

print(middle)
```

Output:

```text
30
```

The indexing expression accesses a specific array-like list element.

## 37.2 Searching Conditions

```python
numbers = [10, 20, 30, 40]

target = 30

for number in numbers:

    if number == target:
        print("Element found")
        break
```

Output:

```text
Element found
```

The expression `number == target` performs the comparison.

## 37.3 Even and Odd Problems

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

The expression `number % 2 == 0` identifies even values.

## 37.4 Finding Squares

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

This is a simple data transformation.

## 37.5 Two-Pointer Algorithm

Expressions are used to update indexes and check conditions in two-pointer algorithms.

```python
numbers = [1, 2, 4, 6, 8]

left = 0
right = len(numbers) - 1

target = 10

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print("Pair found:", numbers[left], numbers[right])
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1
```

**Output:**

```text
Pair found: 2 8
```

### Important Expressions in This Algorithm

```python
len(numbers) - 1
```

Calculates the last index.

```python
left < right
```

Checks whether the pointers have crossed.

```python
numbers[left] + numbers[right]
```

Calculates the sum of the selected values.

```python
current_sum == target
```

Checks whether the desired sum has been found.

### DSA Topics to Study Next

1. Array Indexing.
2. Linear Search.
3. Binary Search.
4. Two-Pointer Technique.
5. Sorting.
6. Filtering.
7. List Comprehensions.
8. Mathematical Problems.
9. String Manipulation.
10. Time and Space Complexity.

---

# 38. Interview Preparation

Practise these coding tasks to strengthen your understanding of expressions.

### Coding Task 1: Arithmetic Calculator

Take two numbers and display their sum, difference, product, and division.

### Coding Task 2: Average Calculator

Calculate the average of five numbers.

### Coding Task 3: Rectangle Calculator

Calculate area and perimeter.

### Coding Task 4: Temperature Converter

Convert Celsius to Fahrenheit.

### Coding Task 5: Discount Calculator

Calculate a discounted product price.

### Coding Task 6: Student Result

Check whether a student passes based on marks and attendance.

### Coding Task 7: Reverse a String

Use slicing to reverse a string.

### Coding Task 8: Find Even Numbers

Use a list comprehension to extract even numbers.

### Coding Task 9: Find Maximum Value

Use a built-in function or comparison expressions to find the largest number.

### Coding Task 10: Palindrome Checker

Use string normalization and slicing to check a palindrome.

### Interview Checklist

- [ ] Explain expressions.
- [ ] Explain operands and operators.
- [ ] Explain arithmetic expressions.
- [ ] Explain comparison expressions.
- [ ] Explain logical expressions.
- [ ] Explain string concatenation.
- [ ] Explain function call expressions.
- [ ] Explain indexing and slicing.
- [ ] Explain list comprehensions.
- [ ] Explain expressions versus statements.
- [ ] Solve mathematical expression problems.
- [ ] Write expressions for DSA algorithms.

---

# 39. Mini Project: Student Marks Calculator

Create a small program that calculates a student's results.

### Requirements

1. Enter five subject marks.
2. Calculate total marks.
3. Calculate average.
4. Calculate percentage.
5. Check whether the student passed.
6. Display the result.

### Example Code

```python
subject1 = 80
subject2 = 75
subject3 = 90
subject4 = 85
subject5 = 70

total = (
    subject1
    + subject2
    + subject3
    + subject4
    + subject5
)

average = total / 5

maximum_marks = 500

percentage = (total / maximum_marks) * 100

passed = (
    subject1 >= 40
    and subject2 >= 40
    and subject3 >= 40
    and subject4 >= 40
    and subject5 >= 40
)

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)

if passed:
    print("Result: PASS")
else:
    print("Result: FAIL")
```

### Output

```text
Total Marks: 400
Average: 80.0
Percentage: 80.0
Result: PASS
```

### Your Extension Tasks

1. Take marks from the user.
2. Validate each mark between 0 and 100.
3. Calculate the highest mark.
4. Calculate the lowest mark.
5. Display the grade based on percentage.
6. Display which subjects have marks below 40.

---

# 40. Glossary

| Term | Meaning |
|---|---|
| Expression | Code that produces a value when evaluated |
| Operand | A value or object used by an operator |
| Operator | Symbol or keyword that performs an operation |
| Arithmetic Expression | Expression used for mathematical calculations |
| Comparison Expression | Expression used to compare values |
| Logical Expression | Expression using logical operators |
| Concatenation | Joining strings |
| Repetition | Repeating a string or sequence |
| Function Call | Calling a function to obtain its result |
| Indexing | Accessing an element by position |
| Slicing | Extracting part of a sequence |
| List Comprehension | Expression for creating a list |
| Evaluation | Calculating an expression's result |
| Statement | A complete Python instruction |
| Assignment | Associating a name with an object |
| Boolean | A value that is either `True` or `False` |
| Parentheses | Symbols used for grouping expressions |
| Precedence | Rules determining which operation is evaluated first |
| Associativity | Rules determining grouping when operators share precedence |
| Data Type | Classification of a value or object |
| Type Conversion | Converting one type to another |
| Return Value | Value produced by a function |
| Condition | Expression used to control a decision |
| List | Ordered, mutable collection |
| Iterable | Object that can provide elements one at a time |

---

# 41. Quick Revision Notes

### Arithmetic Expression

```python
10 + 20
```

### Multiple Operators

```python
a + b * c
```

### Comparison Expression

```python
age >= 18
```

### Logical Expression

```python
marks >= 40 and attendance >= 75
```

### String Concatenation

```python
"Python" + " Programming"
```

### String Repetition

```python
"Python " * 3
```

### Function Call

```python
len("Python")
```

### List Indexing

```python
numbers[2]
```

### List Slicing

```python
numbers[1:4]
```

### Membership Expression

```python
10 in numbers
```

### List Comprehension

```python
[x * x for x in numbers]
```

### Average

```python
(a + b + c) / 3
```

### Area of Rectangle

```python
length * width
```

### Simple Interest

```python
(principal * rate * time) / 100
```

### Celsius to Fahrenheit

```python
(celsius * 9 / 5) + 32
```

### Important Points

1. Expressions produce values.
2. Expressions can contain different operators.
3. Function calls can be part of expressions.
4. Comparison expressions produce Boolean results.
5. String concatenation uses `+`.
6. String repetition uses `*`.
7. List indexing starts at zero.
8. Slicing excludes the stop index.
9. List comprehensions create new lists.
10. Parentheses can make expressions easier to understand.
11. Input values must be converted for numerical calculations.
12. Expressions are used throughout DSA algorithms.

---

# 42. Learning Checklist

Complete the following checklist before moving to the next topic.

## Basic Concepts

- [ ] I understand what an expression is.
- [ ] I understand operands.
- [ ] I understand operators.
- [ ] I can identify values and variables.
- [ ] I understand expression evaluation.

## Expression Types

- [ ] I can write arithmetic expressions.
- [ ] I can write multiple operator expressions.
- [ ] I can write comparison expressions.
- [ ] I can write logical expressions.
- [ ] I can concatenate strings.
- [ ] I can repeat strings.
- [ ] I can use function call expressions.
- [ ] I can use indexing expressions.
- [ ] I can use slicing expressions.
- [ ] I can use membership expressions.
- [ ] I can create list comprehension expressions.

## Advanced Understanding

- [ ] I understand expressions versus statements.
- [ ] I understand expression evaluation.
- [ ] I understand the role of parentheses.
- [ ] I understand expression result types.
- [ ] I understand expressions inside conditions.
- [ ] I understand functions inside expressions.
- [ ] I can convert mathematical formulas into Python expressions.

## Programming Practice

- [ ] I have executed all 12 examples.
- [ ] I have solved all 12 problems.
- [ ] I have attempted all 10 unsolved questions.
- [ ] I have completed the practice test.
- [ ] I have built the Student Marks Calculator.
- [ ] I can explain every expression in my code.

## DSA Preparation

- [ ] I understand expressions in searching.
- [ ] I understand expressions in indexing.
- [ ] I understand expressions in loops.
- [ ] I understand expressions in comparisons.
- [ ] I have practised list transformations.

---

# 43. How to Run the Python Program

The folder contains:

```text
01-expressions/
│
├── README.md
│
└── 01_expressions.py
```

### Step 1: Open PowerShell or VS Code Terminal

Navigate to the project folder.

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\08-Expressions\01-expressions"
```

### Step 2: Run the Python File

```powershell
python 01_expressions.py
```

### Step 3: Select a Menu Option

The program displays:

```text
=============================================================
                     PYTHON EXPRESSIONS
=============================================================

1. View 12 Expression Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

### Step 4: Follow the Learning Order

Recommended order:

1. Select option `1` and understand the examples.
2. Select option `2` and practise the solved problems.
3. Select option `3` and solve the questions independently.
4. Select option `4` and revise your checklist.

### Step 5: Experiment with Expressions

Change values, operators, indexes, and inputs.

Observe how the results change.

---

# 44. Folder Structure

The completed folder should have the following structure:

```text
08-Expressions/
│
├── README.md
│
├── 01-expressions/
│   │
│   ├── README.md
│   │
│   └── 01_expressions.py
│
├── 02-operator-precedence/
│
├── 03-operator-associativity/
│
├── 04-parentheses-and-grouping/
│
└── 05-conditional-expressions/
```

### File Responsibilities

| File | Purpose |
|---|---|
| `README.md` | Complete theoretical study material |
| `01_expressions.py` | Executable examples and interactive problems |

---

# 45. Navigation

### Previous Topic

[07 - Identity Operators](../../07-Identity-Operators/README.md)

### Current Topic

**08.1 - Expressions**

### Next Topic

[08.2 - Operator Precedence](../02-operator-precedence/README.md)

### Expressions Main Folder

[08 - Expressions](../README.md)

### Parent Folder

[05 - Operators and Expressions](../../README.md)

---

# 46. Final Summary

Expressions are a fundamental part of Python programming.

An expression is a combination of values, variables, operators, function calls, and other Python constructs that produces a value.

In this topic, you studied:

1. Basic expressions.
2. Arithmetic expressions.
3. Multiple operator expressions.
4. Comparison expressions.
5. Logical expressions.
6. String concatenation.
7. String repetition.
8. Function call expressions.
9. List indexing.
10. List slicing.
11. Membership expressions.
12. List comprehensions.
13. Expressions inside print statements.
14. Expressions inside conditional statements.
15. Expressions and data types.
16. Expressions versus statements.
17. Expression evaluation.
18. Mathematical formulas in Python.

Expressions are used in almost every Python program. They are essential for calculations, conditions, searching, data transformation, and algorithm development.

**Before moving to the next subtopic, run the Python file, complete all twelve solved problems, attempt the ten unsolved questions, and revise the viva questions.**

Keep practising Python every day. Strong fundamentals make advanced programming and DSA much easier.