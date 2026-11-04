# Variables in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Variables  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Learning Objectives](#2-learning-objectives)
3. [What Is a Variable?](#3-what-is-a-variable)
4. [Why Are Variables Important?](#4-why-are-variables-important)
5. [Creating and Assigning Variables](#5-creating-and-assigning-variables)
6. [Updating Variable Values](#6-updating-variable-values)
7. [Variable Naming](#7-variable-naming)
8. [Multiple Variables and Assignment](#8-multiple-variables-and-assignment)
9. [Swapping Variables](#9-swapping-variables)
10. [Variables and Data Types](#10-variables-and-data-types)
11. [Displaying Variables](#11-displaying-variables)
12. [Variable Tracing and Dry Runs](#12-variable-tracing-and-dry-runs)
13. [Common Programming Patterns](#13-common-programming-patterns)
14. [Common Errors and Debugging](#14-common-errors-and-debugging)
15. [Recommended Learning Order](#15-recommended-learning-order)
16. [Topic Folder Structure](#16-topic-folder-structure)
17. [How to Run the Programs](#17-how-to-run-the-programs)
18. [Practice Strategy](#18-practice-strategy)
19. [Frequently Asked Questions](#19-frequently-asked-questions)
20. [Completion Checklist](#20-completion-checklist)
21. [Next Steps](#21-next-steps)

---

# 1. Introduction

Variables are one of the first and most important concepts in Python programming. A program uses variables to refer to values, store information for later use, perform calculations, update results, and communicate the meaning of data.

For example, a program that calculates the total cost of a purchase can store the price per item, quantity, and total cost in separate variables:

```python
price_per_item = 100
quantity = 4
total_cost = price_per_item * quantity

print(total_cost)
```

Output:

```text
400
```

The variable names make the calculation easier to understand than writing the entire expression as unexplained numbers.

This folder introduces four connected topics: variable basics, variable naming, multiple variables, and variable swapping. Together, they teach you how to create variable names, use them clearly, assign multiple values, and exchange values safely.

# 2. Learning Objectives

After completing the Variables section, you should be able to:

- Explain what a variable represents in Python.
- Assign values to names and update them during execution.
- Use variables in arithmetic expressions and formulas.
- Distinguish assignment (`=`) from equality comparison (`==`).
- Follow valid identifier rules and Python naming conventions.
- Choose meaningful variable names using `snake_case`.
- Assign multiple values and unpack tuples or lists.
- Use starred unpacking when a sequence contains a variable number of values.
- Swap values with a temporary variable and with tuple assignment.
- Understand how variables refer to objects in Python.
- Trace variable changes step by step.
- Test calculations and handle relevant edge cases.

# 3. What Is a Variable?

A variable is a name that refers to an object in a Python program. At a beginner level, it is useful to think of a variable as a named place for information, while remembering that Python names refer to objects rather than acting as permanently typed boxes.

Example:

```python
student_name = "Amaan"
student_age = 20
average_marks = 84.5
is_enrolled = True
```

| Variable | Value | Purpose |
|---|---|---|
| `student_name` | `"Amaan"` | Identifies a student's name |
| `student_age` | `20` | Represents age in years |
| `average_marks` | `84.5` | Represents a calculated average |
| `is_enrolled` | `True` | Represents a true/false condition |

The examples use different value types. The dedicated Data Types section explains those types in detail.

## Assignment

The assignment operator `=` binds a variable name to the value or object produced by the expression on the right:

```python
age = 20
next_year_age = age + 1
```

The expression `age + 1` is evaluated, and the result is assigned to `next_year_age`.

# 4. Why Are Variables Important?

Variables help programs store, reuse, and update information.

### Store Information

```python
student_name = "Amaan"
city_name = "Nagpur"
```

### Perform Calculations

```python
length = 8
width = 5
area = length * width
```

### Reuse Values

```python
price = 100
discount = price * 0.10
final_price = price - discount
```

### Update Results

```python
score = 50
score = score + 10
print(score)
```

Output:

```text
60
```

### Make Code Readable

Compare the following:

```python
a = 100
b = 4
c = a * b
```

with:

```python
price_per_item = 100
quantity = 4
total_cost = price_per_item * quantity
```

The second version explains the meaning of each value without requiring the reader to infer it.

# 5. Creating and Assigning Variables

The basic syntax is:

```python
variable_name = value
```

Examples:

```python
name = "Sara"
age = 19
price = 99.50
is_student = True
```

The right-hand side may be a literal, another variable, or an expression:

```python
a = 10
b = 20
total = a + b
print(total)
```

Output:

```text
30
```

## Assignment Is Not Comparison

- `=` assigns a value.
- `==` checks whether two values are equal.

```python
age = 20
is_twenty = age == 20
print(is_twenty)
```

Output:

```text
True
```

Use `==` when testing equality in a condition; `=` is used to assign a value.

# 6. Updating Variable Values

A variable can be assigned a new value during program execution.

```python
score = 40
print(score)

score = 65
print(score)
```

Output:

```text
40
65
```

A variable can also be updated using its current value:

```python
balance = 1000
balance = balance + 500
balance -= 200

print(balance)
```

Output:

```text
1300
```

Common compound assignment operators include `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, and `**=`. They combine an operation with assignment.

# 7. Variable Naming

A variable name is an identifier used to refer to an object. Good names make a program easier to read, debug, and maintain.

## Identifier Rules

- An identifier cannot start with a digit.
- It may contain letters, digits, and underscores.
- Spaces and hyphens are not allowed within identifiers.
- Reserved Python keywords cannot be used as ordinary variable names.
- Identifiers are case-sensitive.

Examples:

| Name | Valid? | Reason |
|---|---|---|
| `student_name` | Yes | Uses letters and underscore |
| `marks2` | Yes | The digit is not first |
| `_counter` | Yes | Leading underscore is permitted |
| `2marks` | No | Begins with a digit |
| `student name` | No | Contains a space |
| `total-marks` | No | Contains a hyphen |
| `class` | No | Reserved keyword |

## Naming Convention: `snake_case`

Python conventionally uses lowercase words separated by underscores for ordinary variables and functions:

```python
first_name = "Amaan"
total_marks = 420
number_of_students = 45
```

## Meaningful Names

Prefer `total_cost` over `x` when the value represents a purchase total. Short names such as `x` and `y` can still be appropriate in short mathematical examples when their meaning is clear.

## Boolean Names

Boolean names often use prefixes that make a condition easy to understand:

```python
is_active = True
has_permission = False
can_vote = True
```

## Constants

Uppercase names are commonly used for values intended to remain fixed:

```python
SECONDS_PER_MINUTE = 60
MAX_ATTEMPTS = 3
```

This is a convention, not automatic enforcement by Python.

## Avoid Shadowing Built-ins

Avoid using names such as `list`, `sum`, and `max` for unrelated variables if you need the built-in functions later. For example, use `numbers` instead of `list` for a collection.

For more detail, see [Variable Naming](02_variable_naming/README.md).

# 8. Multiple Variables and Assignment

Python lets you assign several values in one statement.

```python
student_name, student_age, course_name = "Amaan", 20, "Diploma"
```

The values are assigned to their corresponding names from left to right.

## Chained Assignment

```python
first_count = second_count = third_count = 0
```

This assigns the same object to all three names. Be careful with mutable objects, such as lists, because all names in a chained assignment would refer to the same list object if assigned one list literal or one list variable.

## Tuple and List Unpacking

```python
student_record = ("Sara", 19, "Diploma")
student_name, student_age, course_name = student_record
```

The number of target names normally must match the number of unpacked values.

## Starred Unpacking

```python
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
```

Result:

```text
first = 10
middle = [20, 30, 40]
last = 50
```

## Useful Built-in Functions

- `zip()` combines corresponding values from multiple iterables and stops at the shortest iterable by default.
- `enumerate()` yields index-value pairs while iterating.
- `divmod(a, b)` returns the quotient and remainder as a tuple, subject to Python's division rules.

For additional examples, see [Multiple Variables](03_multiple_variables/README.md).

# 9. Swapping Variables

Swapping means exchanging the values associated with two variable names.

Before:

```python
a = 10
b = 20
```

After the swap:

```text
a = 20
b = 10
```

## Method 1: Temporary Variable

```python
a = 10
b = 20

temporary_value = a
a = b
b = temporary_value
```

The temporary variable preserves the original value of `a` before `a` is overwritten.

## Method 2: Tuple Assignment

```python
a = 10
b = 20

a, b = b, a
```

Python evaluates the right-hand side before unpacking the resulting values into the left-hand targets. This is the concise, idiomatic Python approach for a simple swap.

## Incorrect Sequential Swap

```python
a = 5
b = 10

a = b
b = a
```

Both variables end up as `10`, because the original value of `a` has been overwritten. Preserve it with a temporary variable or use tuple assignment.

## Swapping List Elements

```python
numbers = [10, 20, 30]
numbers[0], numbers[2] = numbers[2], numbers[0]
```

Result:

```text
[30, 20, 10]
```

Validate indices and handle empty or short lists when writing a general-purpose solution.

For detailed swapping methods, trace tables, and practice, see [Variable Swap](04_variable_swap/README.md).

# 10. Variables and Data Types

A variable name refers to an object, and that object has a type. Python is dynamically typed: a name can be reassigned to an object of another type.

```python
value = 10
print(type(value))

value = "Python"
print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

This does not mean all values behave identically. The operations available depend on the object's type. The next section, `02-Data-Types`, covers types such as `int`, `float`, `str`, `bool`, `complex`, and `None` in detail.

# 11. Displaying Variables

The `print()` function displays values:

```python
name = "Amaan"
age = 20

print(name)
print(age)
print("Name:", name, "Age:", age)
```

F-strings provide a readable way to place variable values inside text:

```python
price = 35.5
quantity = 4
total_cost = price * quantity

print(f"Quantity: {quantity}")
print(f"Total cost: {total_cost:.2f}")
```

Output:

```text
Quantity: 4
Total cost: 142.00
```

The `.2f` formatting displays two digits after the decimal point; it does not permanently change the underlying numeric value.

# 12. Variable Tracing and Dry Runs

A dry run manually follows a program and records how values change.

Consider:

```python
x = 5
x = x + 3
x = x * 2
x = x - 4
print(x)
```

| Step | Statement | Value of `x` |
|---:|---|---:|
| 1 | `x = 5` | 5 |
| 2 | `x = x + 3` | 8 |
| 3 | `x = x * 2` | 16 |
| 4 | `x = x - 4` | 12 |

Output:

```text
12
```

Trace tables help find mistaken assignments, overwritten values, and incorrect assumptions about execution order.

# 13. Common Programming Patterns

Variables are used in several recurring patterns.

## Accumulator

```python
total = 0
for value in [10, 20, 30]:
    total += value
```

The variable `total` accumulates a result.

## Counter

```python
count = 0
for _ in range(5):
    count += 1
```

The variable `count` tracks how many times an operation has occurred.

## Multiple Result Assignment

```python
def calculate(a, b):
    return a + b, a - b

total, difference = calculate(10, 4)
```

The function returns a tuple and the calling statement unpacks it.

## State Update

```python
first, second = 0, 1
first, second = second, first + second
```

Both variables are updated together using their original right-hand-side values.

# 14. Common Errors and Debugging

## Using a Name Before Assignment

```python
print(total)
```

If `total` has not been defined in the current scope, Python raises a `NameError`.

## Confusing `=` and `==`

Use `=` for assignment and `==` for equality comparison.

## Inconsistent Capitalization

`student_name` and `Student_Name` are different identifiers. Use consistent spelling and capitalization.

## Incorrect Unpacking

```python
a, b = [10, 20, 30]
```

This raises `ValueError` because two targets cannot unpack three values without a starred target.

## Overwriting a Value During Swapping

Preserve the original value with a temporary variable or use tuple assignment.

## Shadowing a Built-in Name

Using `sum` as an unrelated variable name can make the built-in `sum()` unavailable through that name in the current scope. Prefer a name such as `total_sum` when that better communicates the intended value.

# 15. Recommended Learning Order

Follow this order so each topic builds on the previous one.

| Order | Topic folder | Main learning goal |
|---:|---|---|
| 1 | `01_variable_basics` | Create, assign, update, and use variables |
| 2 | `02_variable_naming` | Follow identifier rules and choose readable names |
| 3 | `03_multiple_variables` | Assign, unpack, and handle multiple values |
| 4 | `04_variable_swap` | Exchange values safely and apply swapping to collections |

Read the matching `README.md`, run its `.py` file, predict the output before execution, and attempt the unsolved questions yourself.

# 16. Topic Folder Structure

The expected structure for this section is:

```text
01-Variables/
│
├── README.md
│
├── 01_variable_basics/
│   ├── 01_variable_basics.py
│   └── README.md
│
├── 02_variable_naming/
│   ├── 02_variable_naming.py
│   └── README.md
│
├── 03_multiple_variables/
│   ├── 03_multiple_variables.py
│   └── README.md
│
└── 04_variable_swap/
    ├── 04_variable_swap.py
    └── README.md
```

Each minor topic folder contains a runnable Python file named after the topic and a `README.md` for its notes and explanations.

# 17. How to Run the Programs

Run commands from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\01_variable_basics\01_variable_basics.py"
```

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\02_variable_naming\02_variable_naming.py"
```

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\03_multiple_variables\03_multiple_variables.py"
```

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\04_variable_swap\04_variable_swap.py"
```

Each program includes an interactive menu with guided examples, solved problems, unsolved questions, and a checklist. Follow the prompts in the terminal.

# 18. Practice Strategy

Use this process for each topic:

1. Read the `README.md` and understand the definitions.
2. Run the Python examples.
3. Predict the output before running each example.
4. Trace the important variables manually.
5. Rewrite a solution without looking at the source code.
6. Try modified inputs and relevant edge cases.
7. Complete the unsolved practice questions.
8. Explain why the code works and what each variable represents.

Do not focus only on memorizing code. The goal is to understand how variable values are assigned, updated, and used.

# 19. Frequently Asked Questions

### Q1. What is a variable in Python?

A variable is a name that refers to an object in a Python program.

### Q2. Can a variable be reassigned to a different type?

Yes. Python is dynamically typed, so a name can be reassigned to an object of another type.

### Q3. What is the difference between `=` and `==`?

`=` assigns a value, while `==` tests equality.

### Q4. Which naming style should I use?

Use descriptive `snake_case` names for ordinary variables and uppercase names by convention for constants.

### Q5. What is multiple assignment?

It assigns multiple values to multiple target names in one statement, such as `a, b = 10, 20`.

### Q6. What is unpacking?

Unpacking assigns the elements of an iterable, such as a tuple or list, to separate variable names.

### Q7. How do I swap variables in Python?

For a simple swap, use `a, b = b, a`. A temporary variable is also a valid approach.

### Q8. Why is variable tracing useful?

It helps you understand assignment order and locate mistakes in calculations or updates.

### Q9. Should each minor topic have its own README?

Yes. In this repository structure, each minor topic has its own `.py` file and a `README.md`, while this parent README provides the overview and navigation for the entire Variables section.

### Q10. What comes after Variables?

After completing all four topic folders, continue to `02-Data-Types`, starting with `01_int`.

# 20. Completion Checklist

## Variable Basics

- [ ] I can create and assign variables.
- [ ] I can update values using arithmetic expressions.
- [ ] I understand compound assignment operators.
- [ ] I can display variables using `print()` and f-strings.

## Variable Naming

- [ ] I can recognize valid and invalid identifiers.
- [ ] I know that Python keywords cannot be used as ordinary variable names.
- [ ] I use consistent `snake_case` naming.
- [ ] I avoid unnecessarily shadowing built-in names.

## Multiple Variables

- [ ] I understand multiple and chained assignment.
- [ ] I can unpack tuples and lists.
- [ ] I understand starred unpacking.
- [ ] I know how to use `zip()`, `enumerate()`, and `divmod()` appropriately.

## Variable Swapping

- [ ] I can swap values using a temporary variable.
- [ ] I can swap values using tuple assignment.
- [ ] I understand why the incorrect sequential swap fails.
- [ ] I can swap list elements safely after validating indices.

## Overall Practice

- [ ] I have run all four topic programs.
- [ ] I have read their individual README files.
- [ ] I have attempted their unsolved questions.
- [ ] I can explain the main concepts without copying the notes.

# 21. Next Steps

After completing the four Variables topics:

1. Review variable assignment, naming, unpacking, and swapping.
2. Recreate important examples independently.
3. Test your solutions with different inputs.
4. Complete the unsolved practice questions.
5. Continue to `02-Data-Types/01_int/` and begin learning Python integer values and operations.

**Completion goal:** You should be able to name variables clearly, assign and update values, handle multiple values, and exchange values safely in Python.
