# Python Assignment Operators

> A complete learning guide covering basic assignment, variable reassignment, multiple assignment, augmented assignment, arithmetic assignment, and bitwise assignment operators in Python.

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [Learning Objectives](#2-learning-objectives)
3. [What Is Assignment?](#3-what-is-assignment)
4. [Basic Assignment Operator (=)](#4-basic-assignment-operator-)
5. [Variable Reassignment](#5-variable-reassignment)
6. [Multiple Assignment](#6-multiple-assignment)
7. [Chained Assignment](#7-chained-assignment)
8. [Variable Swapping](#8-variable-swapping)
9. [Augmented Assignment Operators](#9-augmented-assignment-operators)
10. [Arithmetic Assignment Operators](#10-arithmetic-assignment-operators)
11. [Bitwise Assignment Operators](#11-bitwise-assignment-operators)
12. [Normal Assignment vs Augmented Assignment](#12-normal-assignment-vs-augmented-assignment)
13. [Assignment vs Comparison](#13-assignment-vs-comparison)
14. [Assignment with Different Data Types](#14-assignment-with-different-data-types)
15. [Mutable Objects and Assignment](#15-mutable-objects-and-assignment)
16. [Walrus Operator](#16-walrus-operator)
17. [Operator Summary](#17-operator-summary)
18. [Understanding the Python Program](#18-understanding-the-python-program)
19. [Twelve Examples Explained](#19-twelve-examples-explained)
20. [Twelve Solved Programming Problems](#20-twelve-solved-programming-problems)
21. [Ten Unsolved Practice Questions](#21-ten-unsolved-practice-questions)
22. [Dry Run and Output Prediction](#22-dry-run-and-output-prediction)
23. [Common Programming Mistakes](#23-common-programming-mistakes)
24. [Error Handling and Input Validation](#24-error-handling-and-input-validation)
25. [Best Practices](#25-best-practices)
26. [Real-World Applications](#26-real-world-applications)
27. [Assignment Operators in DSA](#27-assignment-operators-in-dsa)
28. [Time and Space Complexity](#28-time-and-space-complexity)
29. [Interview and Viva Questions](#29-interview-and-viva-questions)
30. [Practice Test](#30-practice-test)
31. [Quick Revision Notes](#31-quick-revision-notes)
32. [Important Terminology](#32-important-terminology)
33. [Learning Checklist](#33-learning-checklist)
34. [How to Run the Python Program](#34-how-to-run-the-python-program)
35. [Recommended Learning Sequence](#35-recommended-learning-sequence)
36. [Topic Completion Summary](#36-topic-completion-summary)

---

# 1. Introduction

Assignment operators are fundamental components of Python programming. They are used to assign values to variables and update existing variable values.

Whenever we create a variable, store a result, update a counter, calculate a total, or modify a value during program execution, we are performing an assignment operation.

Consider the following example:

```python
number = 10
```

Here, Python associates the name `number` with the integer object `10`.

We can use the variable later:

```python
number = 10

print(number)
```

**Output:**

```text
10
```

Now suppose we want to increase the value by 5.

We can write:

```python
number = 10

number = number + 5

print(number)
```

**Output:**

```text
15
```

Python also provides a shorter way to write this operation:

```python
number = 10

number += 5

print(number)
```

**Output:**

```text
15
```

This shorter form is called augmented assignment.

Assignment operators are especially important because they are used repeatedly in:

- Mathematical calculations.
- Counting and accumulation.
- Updating student marks.
- Managing bank balances.
- Updating product inventory.
- Processing user input.
- Game development.
- Data manipulation.
- Bit manipulation.
- Loops and algorithms.
- Data Structures and Algorithms.

## 1.1 Why Are Assignment Operators Important?

A program rarely calculates something just once. Most programs continuously update values.

For example, consider a shopping application:

1. The customer adds a product.
2. The product quantity increases.
3. The shopping cart total changes.
4. A discount is applied.
5. The final amount is stored.

These operations require variables to be updated.

Assignment operators make such updates easier to write and understand.

## 1.2 Where Will You Use Them?

| Area | Example Usage |
|---|---|
| Basic Python | Storing values in variables |
| Mathematics | Updating calculation results |
| Conditions | Maintaining values used in conditions |
| Loops | Increasing or decreasing counters |
| Lists | Updating collections |
| DSA | Updating indexes and pointers |
| Bit manipulation | Enabling and toggling bits |
| Web development | Updating application state |
| Game development | Updating scores and health |
| Database applications | Updating calculated values |

---

# 2. Learning Objectives

After completing this topic, you should be able to understand and apply the following concepts.

## 2.1 Basic Concepts

- Understand what assignment means.
- Understand the role of the `=` symbol.
- Assign integer, float, string, and Boolean values.
- Reassign an existing variable.
- Understand how variables refer to objects.

## 2.2 Multiple Assignment

- Assign multiple values in one statement.
- Assign the same value to multiple variables.
- Understand chained assignment.
- Swap two variables.
- Rotate three variables.
- Understand unpacking.

## 2.3 Arithmetic Assignment

Learn and use:

- `+=` Addition assignment.
- `-=` Subtraction assignment.
- `*=` Multiplication assignment.
- `/=` Division assignment.
- `//=` Floor division assignment.
- `%=` Modulus assignment.
- `**=` Exponentiation assignment.

## 2.4 Bitwise Assignment

Learn and use:

- `&=` Bitwise AND assignment.
- `|=` Bitwise OR assignment.
- `^=` Bitwise XOR assignment.
- `<<=` Left shift assignment.
- `>>=` Right shift assignment.

## 2.5 Programming Skills

After practising the examples and problems, you should be able to:

1. Read and understand assignment statements.
2. Predict the output of an assignment operation.
3. Trace variable values step by step.
4. Identify incorrect assignments.
5. Handle invalid input.
6. Prevent division-by-zero errors.
7. Write reusable programs.
8. Apply assignment operations in DSA questions.

---

# 3. What Is Assignment?

Assignment is the process of associating a variable name with an object or value.

In Python, we use the assignment statement to bind a name to a value.

## 3.1 General Syntax

```python
variable_name = value
```

### Components

| Component | Description |
|---|---|
| Variable name | Name used to refer to the value |
| `=` | Assignment symbol |
| Value | Data assigned to the variable |

## 3.2 Example

```python
name = "Amaan"
age = 22
percentage = 85.5
is_student = True

print(name)
print(age)
print(percentage)
print(is_student)
```

**Output:**

```text
Amaan
22
85.5
True
```

## 3.3 How Does Assignment Work?

Consider:

```python
number = 50
```

Python performs these conceptual steps:

1. Evaluates the expression on the right-hand side.
2. Obtains the resulting object.
3. Binds the variable name `number` to that object.
4. Makes the variable available for subsequent statements.

## 3.4 Assignment Is Not the Same as Mathematical Equality

In mathematics:

```text
x = 10
```

usually expresses that x has a value of 10.

In Python, the statement assigns a value to a name.

For example:

```python
x = 10
x = x + 5

print(x)
```

**Output:**

```text
15
```

Python first evaluates `x + 5`, then assigns the result back to `x`.

**Important:** Python's assignment symbol `=` is not an ordinary equality comparison. Use `==` when checking whether two values are equal.

---

# 4. Basic Assignment Operator (=)

The basic assignment symbol is used to assign a value to a variable.

## 4.1 Syntax

```python
variable = value
```

## 4.2 Example 1: Integer Assignment

```python
number = 100

print(number)
```

**Output:**

```text
100
```

**Explanation:**

- The integer value `100` is assigned to `number`.
- The `print()` function displays the current value.

## 4.3 Example 2: String Assignment

```python
language = "Python"

print(language)
```

**Output:**

```text
Python
```

## 4.4 Example 3: Float Assignment

```python
price = 99.50

print(price)
```

**Output:**

```text
99.5
```

## 4.5 Example 4: Boolean Assignment

```python
is_logged_in = True

print(is_logged_in)
```

**Output:**

```text
True
```

## 4.6 Example 5: Expression Assignment

Python can calculate an expression before assigning its result.

```python
total = 10 + 20 * 2

print(total)
```

**Output:**

```text
50
```

**Explanation:**

1. Multiplication is evaluated first.
2. `20 * 2` produces `40`.
3. `10 + 40` produces `50`.
4. The final result is assigned to `total`.

## 4.7 Example 6: Function Result Assignment

A variable can also receive the result returned by a function.

```python
length = len("Python")

print(length)
```

**Output:**

```text
6
```

Here, `len()` calculates the string length, and that result is assigned to `length`.

## 4.8 Important Points

- The left side of a basic assignment statement must be a valid assignment target.
- The right side can contain a value, variable, function call, or expression.
- The right-hand expression is evaluated before its result is assigned.
- A variable can be assigned a different object later.
- Assignment does not automatically mean making a copy of an object.

---

# 5. Variable Reassignment

Variable reassignment means assigning a new value to a variable that already exists.

## 5.1 Example

```python
number = 10

print(number)

number = 50

print(number)
```

**Output:**

```text
10
50
```

## 5.2 Step-by-Step Explanation

| Step | Statement | Value of `number` |
|---:|---|---:|
| 1 | `number = 10` | 10 |
| 2 | `print(number)` | 10 |
| 3 | `number = 50` | 50 |
| 4 | `print(number)` | 50 |

The second assignment changes the object associated with the variable name.

## 5.3 Reassignment with Arithmetic

```python
marks = 60

marks = marks + 10

print(marks)
```

**Output:**

```text
70
```

## 5.4 Reassignment with a Different Data Type

Python is dynamically typed, so a variable can refer to different types of objects at different times.

```python
value = 100

print(value)

value = "Python"

print(value)
```

**Output:**

```text
100
Python
```

The variable name is not permanently restricted to an integer.

## 5.5 Practical Example: Updating Student Marks

```python
student_marks = 65

print("Original Marks:", student_marks)

student_marks = 85

print("Updated Marks:", student_marks)
```

**Output:**

```text
Original Marks: 65
Updated Marks: 85
```

## 5.6 Practical Example: Updating a Product Price

```python
product_price = 500

print("Old Price:", product_price)

product_price = 450

print("New Price:", product_price)
```

**Output:**

```text
Old Price: 500
New Price: 450
```

## 5.7 Key Takeaways

- Reassignment updates the binding of a variable name.
- The previous object may still exist if another reference points to it.
- A variable does not need to retain the same data type.
- Reassignment is different from modifying a mutable object in place.

---

# 6. Multiple Assignment

Multiple assignment allows us to assign values to multiple variables in a single statement.

## 6.1 Syntax

```python
a, b, c = 10, 20, 30
```

## 6.2 Example

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

**Output:**

```text
10
20
30
```

## 6.3 How Does It Work?

Python evaluates the right-hand side and distributes the values to the assignment targets.

| Variable | Assigned Value |
|---|---:|
| `a` | 10 |
| `b` | 20 |
| `c` | 30 |

## 6.4 Multiple Assignment with Different Data Types

```python
name, age, percentage = "Amaan", 22, 85.5

print(name)
print(age)
print(percentage)
```

**Output:**

```text
Amaan
22
85.5
```

## 6.5 Multiple Assignment Using Expressions

```python
a, b, c = 10 + 5, 20 * 2, 100 // 5

print(a)
print(b)
print(c)
```

**Output:**

```text
15
40
20
```

## 6.6 Multiple Assignment from a List

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)
```

**Output:**

```text
10
20
30
```

This is called iterable unpacking.

## 6.7 Multiple Assignment from a Tuple

```python
student = ("Amaan", 22, "Computer Science")

name, age, branch = student

print(name)
print(age)
print(branch)
```

**Output:**

```text
Amaan
22
Computer Science
```

## 6.8 Number of Targets Must Match

This works:

```python
a, b, c = 10, 20, 30
```

This normally raises a `ValueError`:

```python
a, b, c = 10, 20
```

The number of assignment targets does not match the number of unpacked values.

## 6.9 Using the Starred Target

Python supports extended unpacking using `*`.

```python
first, *middle, last = [10, 20, 30, 40, 50]

print(first)
print(middle)
print(last)
```

**Output:**

```text
10
[20, 30, 40]
50
```

This is an additional unpacking technique. It is not one of the main examples in the current Python program.

---

# 7. Chained Assignment

Chained assignment allows the same value or object to be assigned to multiple variables in a single statement.

## 7.1 Syntax

```python
a = b = c = value
```

## 7.2 Example

```python
x = y = z = 100

print(x)
print(y)
print(z)
```

**Output:**

```text
100
100
100
```

## 7.3 Explanation

Python evaluates the right-hand value and assigns it to all the targets.

All three names refer to the same integer object in this example.

## 7.4 Chained Assignment with Strings

```python
a = b = c = "Python"

print(a)
print(b)
print(c)
```

**Output:**

```text
Python
Python
Python
```

## 7.5 Chained Assignment with Mutable Objects

Be careful when assigning one mutable object to multiple variables.

```python
a = b = []

a.append(10)

print(a)
print(b)
```

**Output:**

```text
[10]
[10]
```

Both variables refer to the same list.

Changing the list through either name is visible through the other name.

## 7.6 Creating Independent Lists

Use separate list objects when independent modification is required.

```python
a = []
b = []

a.append(10)

print(a)
print(b)
```

**Output:**

```text
[10]
[]
```

## 7.7 Multiple Assignment vs Chained Assignment

| Multiple Assignment | Chained Assignment |
|---|---|
| Can assign different values | Assigns the same value or object to multiple targets |
| `a, b = 10, 20` | `a = b = 10` |
| Values are distributed | One right-hand value is bound to each target |
| Useful for unpacking | Useful for initializing several names |

---

# 8. Variable Swapping

Variable swapping means exchanging the values of two or more variables.

Python supports swapping through multiple assignment.

## 8.1 Swapping Two Variables

```python
a = 10
b = 20

a, b = b, a

print("A:", a)
print("B:", b)
```

**Output:**

```text
A: 20
B: 10
```

## 8.2 Step-by-Step Explanation

Before swapping:

| Variable | Value |
|---|---:|
| `a` | 10 |
| `b` | 20 |

The statement is:

```python
a, b = b, a
```

Python evaluates the values on the right before assigning the targets on the left.

After swapping:

| Variable | Value |
|---|---:|
| `a` | 20 |
| `b` | 10 |

## 8.3 Swapping with a Temporary Variable

A traditional method uses a third variable.

```python
a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)
```

**Output:**

```text
20 10
```

## 8.4 Swapping Without a Temporary Variable

Python's multiple assignment makes this easy:

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

**Output:**

```text
20 10
```

## 8.5 Rotating Three Variables

```python
a = 10
b = 20
c = 30

a, b, c = c, a, b

print(a, b, c)
```

**Output:**

```text
30 10 20
```

## 8.6 Practical Applications of Swapping

Swapping is useful in:

- Sorting algorithms.
- Reversing arrays.
- Two-pointer techniques.
- Selection sort.
- Bubble sort.
- Rearranging values.
- Rotating elements.

---

# 9. Augmented Assignment Operators

Augmented assignment combines an operation with assignment.

It provides a shorter way to update an existing variable.

## 9.1 General Syntax

```python
variable operator= value
```

For example:

```python
number += 5
```

This is equivalent to the following for ordinary integer calculations:

```python
number = number + 5
```

## 9.2 Why Do We Need Augmented Assignment?

Consider a counter.

Without augmented assignment:

```python
count = 0

count = count + 1
count = count + 1
count = count + 1

print(count)
```

**Output:**

```text
3
```

Using augmented assignment:

```python
count = 0

count += 1
count += 1
count += 1

print(count)
```

**Output:**

```text
3
```

The second version is shorter and easier to read.

## 9.3 Categories of Augmented Assignment

| Category | Operators |
|---|---|
| Arithmetic | `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` |
| Bitwise | `&=`, `|=`, `^=`, `<<=`, `>>=` |
| Matrix multiplication | `@=` where supported by the operand type |

The current learning program focuses on the arithmetic and bitwise operators listed above.

---

# 10. Arithmetic Assignment Operators

Arithmetic assignment operators perform mathematical calculations and assign the result to the original variable.

## 10.1 Addition Assignment (`+=`)

The addition assignment operator adds another value to the current variable.

### Syntax

```python
variable += value
```

Equivalent arithmetic form:

```python
variable = variable + value
```

### Example 1: Basic Calculation

```python
number = 10

number += 5

print(number)
```

**Output:**

```text
15
```

### Dry Run

| Step | Operation | Value |
|---:|---|---:|
| 1 | `number = 10` | 10 |
| 2 | `number += 5` | 15 |
| 3 | `print(number)` | 15 |

### Example 2: Adding Marks

```python
marks = 70

marks += 15

print("Updated Marks:", marks)
```

**Output:**

```text
Updated Marks: 85
```

### Example 3: Adding to Bank Balance

```python
balance = 5000

balance += 1000

print("Current Balance:", balance)
```

**Output:**

```text
Current Balance: 6000
```

### Example 4: Updating a Counter

```python
count = 0

count += 1

print(count)
```

**Output:**

```text
1
```

### Important Points

- `+=` adds the right-hand value to the current value.
- The result is assigned back to the target.
- It is commonly used for counters and running totals.
- It can also work with types such as lists and strings when their types support the operation.

---

## 10.2 Subtraction Assignment (`-=`)

The subtraction assignment operator subtracts another value from the current variable.

### Syntax

```python
variable -= value
```

Equivalent form:

```python
variable = variable - value
```

### Example 1: Basic Calculation

```python
number = 50

number -= 10

print(number)
```

**Output:**

```text
40
```

### Dry Run

| Step | Operation | Value |
|---:|---|---:|
| 1 | `number = 50` | 50 |
| 2 | `number -= 10` | 40 |
| 3 | `print(number)` | 40 |

### Example 2: Reducing Student Marks

```python
marks = 90

marks -= 5

print("Updated Marks:", marks)
```

**Output:**

```text
Updated Marks: 85
```

### Example 3: Reducing Product Stock

```python
stock = 100

stock -= 25

print("Remaining Stock:", stock)
```

**Output:**

```text
Remaining Stock: 75
```

### Example 4: Decreasing a Counter

```python
count = 10

count -= 1

print(count)
```

**Output:**

```text
9
```

### Important Points

- `-=` reduces the current value.
- It is commonly used in inventory and countdown programs.
- It can produce negative values if the subtraction exceeds the original value.
- Validate business rules when negative values are not allowed.

---

## 10.3 Multiplication Assignment (`*=`)

The multiplication assignment operator multiplies the existing value by another value.

### Syntax

```python
variable *= value
```

Equivalent form:

```python
variable = variable * value
```

### Example 1: Basic Calculation

```python
number = 10

number *= 5

print(number)
```

**Output:**

```text
50
```

### Example 2: Calculating Product Price

```python
price = 100
quantity = 5

price *= quantity

print("Total Price:", price)
```

**Output:**

```text
Total Price: 500
```

### Example 3: Doubling a Number

```python
number = 12

number *= 2

print(number)
```

**Output:**

```text
24
```

### Example 4: Calculating a Scale Factor

```python
size = 15

size *= 3

print(size)
```

**Output:**

```text
45
```

### Important Points

- `*=` multiplies the current value.
- It is useful for repeated multiplication.
- It can be used for numeric values and other compatible types.
- The resulting type depends on the operands.

---

## 10.4 Division Assignment (`/=`)

The division assignment operator divides the existing value by another value.

### Syntax

```python
variable /= value
```

Equivalent form:

```python
variable = variable / value
```

### Example 1: Basic Calculation

```python
number = 100

number /= 4

print(number)
```

**Output:**

```text
25.0
```

### Why Is the Result `25.0`?

Python's `/` operator performs true division.

It returns a floating-point result, even when the mathematical answer is a whole number.

### Example 2: Dividing an Amount

```python
amount = 1200
people = 4

amount /= people

print("Amount Per Person:", amount)
```

**Output:**

```text
Amount Per Person: 300.0
```

### Example 3: Dividing a Distance

```python
distance = 100
distance /= 2

print(distance)
```

**Output:**

```text
50.0
```

### Example 4: Division by Zero Validation

```python
number = 100
divisor = 0

if divisor != 0:
    number /= divisor
    print(number)
else:
    print("Division by zero is not allowed.")
```

**Output:**

```text
Division by zero is not allowed.
```

### Important Points

- `/=` performs true division.
- The result is usually a `float`.
- Division by zero raises `ZeroDivisionError`.
- Validate the divisor before the calculation.

---

## 10.5 Floor Division Assignment (`//=`)

The floor division assignment operator performs floor division and assigns the result back.

### Syntax

```python
variable //= value
```

Equivalent form:

```python
variable = variable // value
```

### Example 1: Basic Calculation

```python
number = 25

number //= 4

print(number)
```

**Output:**

```text
6
```

### Explanation

```text
25 / 4 = 6.25
25 // 4 = 6
```

Floor division rounds the result down to the nearest whole-number value when using integer operands.

### Example 2: Complete Groups

```python
items = 23
group_size = 5

items //= group_size

print("Complete Groups:", items)
```

**Output:**

```text
Complete Groups: 4
```

### Example 3: Number of Complete Weeks

```python
days = 30

days //= 7

print("Complete Weeks:", days)
```

**Output:**

```text
Complete Weeks: 4
```

### Example 4: Negative Floor Division

```python
number = -7

number //= 2

print(number)
```

**Output:**

```text
-4
```

### Important Difference

Floor division rounds toward negative infinity, not toward zero.

For example:

```python
print(-7 // 2)
```

Output:

```text
-4
```

### Important Points

- `//=` performs floor division.
- It is useful for calculating complete groups.
- The result depends on the types of the operands.
- For integer operands, the result is an integer.
- Always validate a divisor that could be zero.

---

## 10.6 Modulus Assignment (`%=`)

The modulus assignment operator calculates the remainder and assigns it back to the original variable.

### Syntax

```python
variable %= value
```

Equivalent form:

```python
variable = variable % value
```

### Example 1: Basic Calculation

```python
number = 17

number %= 5

print(number)
```

**Output:**

```text
2
```

### Explanation

```text
17 = 5 × 3 + 2
```

The remainder is `2`.

### Example 2: Checking Even or Odd

```python
number = 14

number %= 2

print(number)
```

**Output:**

```text
0
```

Since the remainder is `0`, the original number was even.

### Example 3: Finding Remaining Items

```python
items = 23
group_size = 5

items %= group_size

print("Remaining Items:", items)
```

**Output:**

```text
Remaining Items: 3
```

### Example 4: Extracting the Last Digit

```python
number = 12345

number %= 10

print(number)
```

**Output:**

```text
5
```

### Important Points

- `%=` calculates a remainder.
- It is often used in even/odd checks.
- It is useful for extracting digits.
- It helps solve grouping and cyclic-index problems.
- The divisor must not be zero.

---

## 10.7 Exponentiation Assignment (`**=`)

The exponentiation assignment operator raises a value to a specified power.

### Syntax

```python
variable **= power
```

Equivalent form:

```python
variable = variable ** power
```

### Example 1: Square

```python
number = 5

number **= 2

print(number)
```

**Output:**

```text
25
```

### Example 2: Cube

```python
number = 3

number **= 3

print(number)
```

**Output:**

```text
27
```

### Example 3: Fourth Power

```python
number = 2

number **= 4

print(number)
```

**Output:**

```text
16
```

### Example 4: Power of Zero

```python
number = 10

number **= 0

print(number)
```

**Output:**

```text
1
```

For a non-zero number, raising it to the power of zero produces `1`.

### Important Points

- `**=` performs exponentiation.
- It is useful for squares, cubes, and other powers.
- Large exponents can produce very large integers.
- The resulting type depends on the operands.

---

# 11. Bitwise Assignment Operators

Bitwise assignment operators perform operations on the binary representation of integer values.

They are useful when a program needs to manipulate individual bits.

## 11.1 Binary Number Basics

Computers represent data using binary digits:

- `0`
- `1`

Each binary digit is called a bit.

Example:

```text
Decimal 5 = Binary 0101
Decimal 8 = Binary 1000
Decimal 10 = Binary 1010
Decimal 12 = Binary 1100
```

## 11.2 Bitwise Operator Truth Table

| A | B | AND (`&`) | OR (`|`) | XOR (`^`) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

The assignment variants apply these operations and assign their results back.

---

## 11.3 Bitwise AND Assignment (`&=`)

Bitwise AND returns `1` only when both corresponding bits are `1`.

### Syntax

```python
variable &= value
```

### Example

```python
number = 12

number &= 10

print(number)
```

**Binary calculation:**

```text
12 = 1100
10 = 1010
------------
     1000
```

**Output:**

```text
8
```

### Step-by-Step Explanation

1. Convert `12` into binary: `1100`.
2. Convert `10` into binary: `1010`.
3. Compare corresponding bits.
4. Apply the AND truth table.
5. Obtain `1000`.
6. Convert `1000` into decimal: `8`.
7. Assign the result back to `number`.

### Practical Example: Checking a Particular Bit

```python
permissions = 12
mask = 4

result = permissions & mask

print(result)
```

**Output:**

```text
4
```

A non-zero result indicates that the selected bit is set.

---

## 11.4 Bitwise OR Assignment (`|=`)

Bitwise OR returns `1` when at least one corresponding bit is `1`.

### Syntax

```python
variable |= value
```

### Example

```python
number = 12

number |= 10

print(number)
```

**Binary calculation:**

```text
12 = 1100
10 = 1010
------------
     1110
```

**Output:**

```text
14
```

### Practical Example: Enabling Flags

```python
flags = 8
mask = 3

flags |= mask

print(flags)
```

**Output:**

```text
11
```

OR assignment can set selected bits without clearing bits that were already set.

---

## 11.5 Bitwise XOR Assignment (`^=`)

Bitwise XOR returns `1` when corresponding bits are different.

### Syntax

```python
variable ^= value
```

### Example

```python
number = 12

number ^= 10

print(number)
```

**Binary calculation:**

```text
12 = 1100
10 = 1010
------------
     0110
```

**Output:**

```text
6
```

### Practical Example: Toggling a Flag

```python
flags = 12
mask = 10

flags ^= mask

print(flags)
```

**Output:**

```text
6
```

XOR assignment toggles each bit selected by a `1` in the mask.

---

## 11.6 Left Shift Assignment (`<<=`)

Left shift moves the binary digits toward the left by the specified number of positions.

### Syntax

```python
variable <<= positions
```

### Example

```python
number = 5

number <<= 1

print(number)
```

**Binary calculation:**

```text
5 = 0101

Shift left by 1:

   = 1010
```

**Output:**

```text
10
```

### Explanation

For non-negative integers:

```text
5 << 1 = 5 × 2
5 << 2 = 5 × 4
5 << 3 = 5 × 8
```

### Example: Shifting by Two Positions

```python
number = 3

number <<= 2

print(number)
```

**Output:**

```text
12
```

Binary:

```text
3  = 0011
<< 2
     1100
```

---

## 11.7 Right Shift Assignment (`>>=`)

Right shift moves binary digits toward the right.

### Syntax

```python
variable >>= positions
```

### Example

```python
number = 20

number >>= 2

print(number)
```

**Binary calculation:**

```text
20 = 10100

Shift right by 2:

    = 00101
```

**Output:**

```text
5
```

### Example: Right Shift by One Position

```python
number = 16

number >>= 1

print(number)
```

**Output:**

```text
8
```

For non-negative integers, right shift by one position corresponds to floor division by two.

### Important Points About Bitwise Assignment

- Bitwise operators work on integer operands.
- Binary representation helps explain their results.
- `&=` can be used for testing or retaining selected bits.
- `|=` can enable bits.
- `^=` can toggle bits.
- `<<=` shifts bits to the left.
- `>>=` shifts bits to the right.
- Bit manipulation is useful in DSA and low-level programming.

---

# 12. Normal Assignment vs Augmented Assignment

Python allows an operation to be written in two common ways.

## 12.1 Addition Comparison

Normal assignment:

```python
number = 10
number = number + 5

print(number)
```

Augmented assignment:

```python
number = 10
number += 5

print(number)
```

Both produce:

```text
15
```

## 12.2 Operator Comparison Table

| Normal Assignment | Augmented Assignment |
|---|---|
| `x = x + 5` | `x += 5` |
| `x = x - 5` | `x -= 5` |
| `x = x * 5` | `x *= 5` |
| `x = x / 5` | `x /= 5` |
| `x = x // 5` | `x //= 5` |
| `x = x % 5` | `x %= 5` |
| `x = x ** 5` | `x **= 5` |
| `x = x & 5` | `x &= 5` |
| `x = x | 5` | `x |= 5` |
| `x = x ^ 5` | `x ^= 5` |
| `x = x << 1` | `x <<= 1` |
| `x = x >> 1` | `x >>= 1` |

## 12.3 Advantages of Augmented Assignment

1. Reduces repeated variable names.
2. Makes updates easier to read.
3. Is convenient for counters.
4. Is convenient for accumulated totals.
5. Is common in loops and algorithms.
6. Makes bitwise updates easier to recognize.

## 12.4 Important Technical Difference

For ordinary immutable numeric values, the two forms usually produce the same result.

However, augmented assignment is not guaranteed to behave identically to a normal assignment expression.

For mutable objects, augmented assignment may modify an object in place.

Example:

```python
numbers = [1, 2]

numbers += [3, 4]

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4]
```

For a built-in list, `+=` extends the existing list.

This behavior is important when multiple variables refer to the same mutable object.

---

# 13. Assignment vs Comparison

One of the most common beginner mistakes is confusing `=` with `==`.

## 13.1 Assignment (`=`)

Used to assign a value.

```python
number = 10
```

## 13.2 Equality Comparison (`==`)

Used to check whether two values are equal.

```python
number = 10

print(number == 10)
```

**Output:**

```text
True
```

## 13.3 Comparison Table

| Symbol | Name | Purpose | Example |
|---|---|---|---|
| `=` | Assignment | Store a value | `x = 10` |
| `==` | Equality | Check equality | `x == 10` |
| `!=` | Inequality | Check difference | `x != 10` |

## 13.4 Common Syntax Error

Incorrect:

```python
number = 10

if number = 10:
    print("Equal")
```

Correct:

```python
number = 10

if number == 10:
    print("Equal")
```

---

# 14. Assignment with Different Data Types

Python supports assignment with different built-in data types.

## 14.1 Integer Assignment

```python
number = 100
number += 50

print(number)
```

Output:

```text
150
```

## 14.2 Float Assignment

```python
price = 100.5
price += 20.5

print(price)
```

Output:

```text
121.0
```

## 14.3 String Assignment

```python
message = "Hello"

message += " Python"

print(message)
```

Output:

```text
Hello Python
```

String addition joins two strings together.

## 14.4 List Assignment

```python
numbers = [1, 2, 3]

numbers += [4, 5]

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

## 14.5 Boolean Assignment

```python
is_active = True

is_active = False

print(is_active)
```

Output:

```text
False
```

**Important:** Not every augmented operator works with every data type. The operation must be supported by the operand types.

---

# 15. Mutable Objects and Assignment

Understanding mutable and immutable objects helps prevent unexpected behavior.

## 15.1 What Is a Mutable Object?

A mutable object can be modified after it is created.

Examples:

- Lists.
- Dictionaries.
- Sets.

## 15.2 What Is an Immutable Object?

An immutable object cannot be modified after creation.

Examples:

- Integers.
- Floats.
- Strings.
- Tuples.
- Booleans.

## 15.3 Assignment and Object References

Consider:

```python
a = [10, 20]
b = a

a.append(30)

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[10, 20, 30]
```

Both names refer to the same list object.

## 15.4 Augmented Assignment with Lists

```python
numbers = [1, 2]

numbers += [3, 4]

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

For lists, `+=` extends the list.

## 15.5 Creating a Separate List

```python
a = [10, 20]
b = a.copy()

a.append(30)

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[10, 20]
```

Here, `b` refers to a separate shallow copy of the list.

---

# 16. Walrus Operator (`:=`)

The walrus operator is an assignment expression introduced in Python 3.8.

It assigns a value to a variable as part of a larger expression.

## 16.1 Syntax

```python
variable := expression
```

## 16.2 Example

```python
if (length := len("Python")) > 5:
    print("Length:", length)
```

Output:

```text
Length: 6
```

## 16.3 Explanation

1. `len("Python")` calculates the length.
2. `:=` assigns that result to `length`.
3. The condition compares `length` with `5`.
4. The condition evaluates to `True`.
5. The print statement displays the result.

## 16.4 Difference Between `=` and `:=`

| `=` | `:=` |
|---|---|
| Assignment statement | Assignment expression |
| Assigns a value in a statement | Assigns a value within an expression |
| Used for normal assignment | Used when assignment and expression evaluation are needed together |

**Note:** This is an optional advanced concept. It is not included as one of the twelve examples in the current learning program.

---

# 17. Operator Summary

## 17.1 Complete Assignment Operator Table

| Operator | Name | General Form | Example Result |
|---|---|---|---|
| `=` | Assignment | `x = value` | Assigns value |
| `+=` | Addition assignment | `x += y` | `10 + 5 = 15` |
| `-=` | Subtraction assignment | `x -= y` | `10 - 5 = 5` |
| `*=` | Multiplication assignment | `x *= y` | `10 * 5 = 50` |
| `/=` | Division assignment | `x /= y` | `10 / 5 = 2.0` |
| `//=` | Floor division assignment | `x //= y` | `10 // 3 = 3` |
| `%=` | Modulus assignment | `x %= y` | `10 % 3 = 1` |
| `**=` | Exponentiation assignment | `x **= y` | `2 ** 3 = 8` |
| `&=` | AND assignment | `x &= y` | `12 & 10 = 8` |
| `|=` | OR assignment | `x |= y` | `12 | 10 = 14` |
| `^=` | XOR assignment | `x ^= y` | `12 ^ 10 = 6` |
| `<<=` | Left shift assignment | `x <<= n` | `5 << 1 = 10` |
| `>>=` | Right shift assignment | `x >>= n` | `20 >> 2 = 5` |

## 17.2 Arithmetic Assignment Summary

| Operator | Operation | Common Use |
|---|---|---|
| `+=` | Addition | Counters and totals |
| `-=` | Subtraction | Countdown and stock reduction |
| `*=` | Multiplication | Product and scaling |
| `/=` | True division | Splitting amounts |
| `//=` | Floor division | Complete groups |
| `%=` | Remainder | Even/odd and digit operations |
| `**=` | Power | Squares and cubes |

## 17.3 Bitwise Assignment Summary

| Operator | Operation | Common Use |
|---|---|---|
| `&=` | Bitwise AND | Select or retain bits |
| `|=` | Bitwise OR | Enable bits |
| `^=` | Bitwise XOR | Toggle bits |
| `<<=` | Left shift | Shift bits left |
| `>>=` | Right shift | Shift bits right |

---

# 18. Understanding the Python Program

**File Name:** `01_assignment_operators.py`

The program is organized into multiple sections to make the topic easier to learn, revise, and practise.

## 18.1 Module Documentation

The program begins with a module-level docstring.

It explains:

- The topic name.
- The purpose of the program.
- The examples included.
- The practical problems included.
- How to use the menu.

Module documentation makes the file easier to understand when revisiting it later.

## 18.2 Import Section

The program imports:

```python
import math
```

The `math` module provides mathematical utilities.

In this program, `math.isfinite()` is used to check whether a floating-point input is a finite number.

It helps reject values such as:

- `float("inf")`
- `float("-inf")`
- `float("nan")`

## 18.3 Helper Functions

The program defines reusable helper functions.

### A. `print_heading()`

Purpose:

- Displays section headings.
- Separates different parts of the program.
- Improves console readability.

### B. `read_int()`

Purpose:

- Accepts an integer from the user.
- Converts the input into an integer.
- Handles invalid integer input.

### C. `read_float()`

Purpose:

- Accepts floating-point input.
- Converts the input into a float.
- Checks whether the result is finite.
- Handles invalid numeric input.

### D. `read_text()`

Purpose:

- Accepts textual input.
- Can be used for names and other text values.

### Why Are Helper Functions Useful?

Without helper functions, the same input-validation logic would need to be repeated in several problems.

Using helper functions:

1. Reduces code duplication.
2. Improves readability.
3. Makes input handling consistent.
4. Makes the program easier to maintain.
5. Separates input logic from calculation logic.

## 18.4 Section 1: Twelve Examples

The first section demonstrates twelve examples of assignment operations.

| No. | Example | Concept |
|---:|---|---|
| 1 | Basic assignment | `=` |
| 2 | Variable reassignment | `=` |
| 3 | Multiple assignment and unpacking | Multiple assignment |
| 4 | Chained assignment | `a = b = c` |
| 5 | Addition assignment | `+=` |
| 6 | Subtraction assignment | `-=` |
| 7 | Multiplication assignment | `*=` |
| 8 | Division assignment | `/=` |
| 9 | Floor division and modulus assignment | `//=`, `%=` |
| 10 | Exponentiation assignment | `**=` |
| 11 | Bitwise assignment | `&=`, `|=`, `^=` |
| 12 | Shift assignment | `<<=`, `>>=` |

Each example has a separate purpose and demonstrates how the corresponding assignment operation changes a value.

## 18.5 Section 2: Twelve Solved Problems

This section contains twelve practical problems.

The user can select a problem and execute it.

These problems apply assignment operators to real-world-style calculations.

## 18.6 `SOLVED_PROBLEMS` Dictionary

The program uses a dictionary named:

```python
SOLVED_PROBLEMS
```

It stores the available solved-problem descriptions.

A dictionary makes it convenient to associate a problem number with a description.

## 18.7 `show_solved_problems()`

This function displays the solved-problem list.

It allows the user to see which questions are available before selecting one.

## 18.8 `run_solved_problems()`

This function handles the selection and execution of solved problems.

It provides a common interface for running the individual problem solutions.

## 18.9 Section 3: Ten Unsolved Questions

This section displays ten questions for independent practice.

Its purpose is to help users apply the concepts without immediately looking at complete solutions.

## 18.10 Section 4: Learning Checklist

The checklist provides a way to review the important assignment concepts.

It helps identify topics that need more practice.

## 18.11 Section 5: Main Menu

The main menu connects all the learning sections.

The menu provides the following options:

| Option | Action |
|---:|---|
| 1 | View twelve assignment operator examples |
| 2 | Practise twelve solved problems |
| 3 | View ten unsolved practice questions |
| 4 | View learning checklist |
| 0 | Exit the program |

The program continues displaying the menu until the user selects the exit option.

---

# 19. Twelve Examples Explained

This section provides the learning purpose of each example in `01_assignment_operators.py`.

## Example 1: Basic Assignment

**Concept:** `=`

Purpose:

- Understand how values are assigned to variables.
- Learn the basic assignment statement.
- Display the stored value.

Expected understanding:

```python
number = 100
```

The variable `number` refers to the integer value `100`.

## Example 2: Variable Reassignment

**Concept:** Reassignment

Purpose:

- Understand how a variable receives another value.
- Observe how its current binding changes.

Expected understanding:

```python
number = 10
number = 50
```

After the second statement, `number` refers to `50`.

## Example 3: Multiple Assignment and Unpacking

**Concept:** Multiple assignment

Purpose:

- Assign different values to different variables.
- Understand positional value distribution.
- Learn basic unpacking.

Expected understanding:

```python
a, b, c = 10, 20, 30
```

The variables receive their corresponding values.

## Example 4: Chained Assignment

**Concept:** Chained assignment

Purpose:

- Assign one value to multiple variables.
- Understand how chained assignment works.

Expected understanding:

```python
a = b = c = 100
```

All three names are assigned the same value.

## Example 5: Addition Assignment

**Concept:** `+=`

Purpose:

- Increase a variable's value.
- Understand the addition assignment operation.

Expected understanding:

```python
number = 10
number += 5
```

Updated result: `15`.

## Example 6: Subtraction Assignment

**Concept:** `-=`

Purpose:

- Reduce a variable's value.
- Understand subtraction assignment.

Expected understanding:

```python
number = 50
number -= 10
```

Updated result: `40`.

## Example 7: Multiplication Assignment

**Concept:** `*=`

Purpose:

- Multiply an existing variable.
- Understand multiplication assignment.

Expected understanding:

```python
number = 10
number *= 5
```

Updated result: `50`.

## Example 8: Division Assignment

**Concept:** `/=`

Purpose:

- Divide an existing value.
- Understand true division.
- Observe floating-point output.

Expected understanding:

```python
number = 100
number /= 4
```

Updated result: `25.0`.

## Example 9: Floor Division and Modulus Assignment

**Concept:** `//=` and `%=`

Purpose:

- Calculate complete groups.
- Find the remainder.
- Understand the difference between floor division and modulus.

Example:

```python
number = 23
number //= 5
```

Result: `4`.

Another example:

```python
number = 23
number %= 5
```

Result: `3`.

## Example 10: Exponentiation Assignment

**Concept:** `**=`

Purpose:

- Calculate powers.
- Understand square and cube calculations.

Example:

```python
number = 5
number **= 3
```

Result: `125`.

## Example 11: Bitwise Assignment

**Concept:** `&=`, `|=`, `^=`

Purpose:

- Perform bitwise AND.
- Perform bitwise OR.
- Perform bitwise XOR.
- Understand binary calculations.

## Example 12: Shift Assignment

**Concept:** `<<=` and `>>=`

Purpose:

- Shift bits toward the left.
- Shift bits toward the right.
- Understand the effect of shift positions.

---

# 20. Twelve Solved Programming Problems

This section explains the twelve practical problems included in the Python file.

Each problem includes:

1. Problem statement.
2. Required operator.
3. Logic.
4. Example code.
5. Expected output.
6. Step-by-step explanation.
7. Important learning point.

---

## Problem 1: Update Student Score

**Operator:** `+=`

### Problem Statement

A student has an initial score. Ask for the current score and additional marks, then update the score using addition assignment.

### Logic

1. Read the initial score.
2. Read the additional marks.
3. Add the additional marks using `+=`.
4. Display the updated score.

### Example Code

```python
score = 70
additional_marks = 10

score += additional_marks

print("Updated Score:", score)
```

### Output

```text
Updated Score: 80
```

### Dry Run

| Step | Score | Additional Marks |
|---|---:|---:|
| Initial | 70 | 10 |
| After `+=` | 80 | 10 |

### Explanation

Initially, the score is `70`.

The additional marks are `10`.

The statement:

```python
score += additional_marks
```

performs:

```python
score = score + additional_marks
```

The updated score becomes `80`.

### Learning Point

The `+=` operator is commonly used for updating counters, accumulated marks, and totals.

---

## Problem 2: Reduce Product Stock

**Operator:** `-=`

### Problem Statement

A shop has a certain number of products in stock. Reduce the available stock by the quantity sold.

### Logic

1. Read the available stock.
2. Read the quantity sold.
3. Subtract the sold quantity using `-=`.
4. Display the remaining stock.

### Example Code

```python
stock = 100
sold = 25

stock -= sold

print("Remaining Stock:", stock)
```

### Output

```text
Remaining Stock: 75
```

### Dry Run

| Step | Stock | Sold |
|---|---:|---:|
| Initial | 100 | 25 |
| After `-=` | 75 | 25 |

### Explanation

The original stock is `100`.

The sold quantity is `25`.

After subtraction, the remaining stock is `75`.

### Learning Point

The `-=` operator is commonly used in inventory systems, countdowns, and resource management.

---

## Problem 3: Calculate Total Using Multiplication Assignment

**Operator:** `*=`

### Problem Statement

Calculate the total cost by multiplying a unit price by the quantity purchased.

### Logic

1. Read the unit price.
2. Read the quantity.
3. Multiply using `*=`.
4. Display the total amount.

### Example Code

```python
total = 50
quantity = 4

total *= quantity

print("Total Amount:", total)
```

### Output

```text
Total Amount: 200
```

### Dry Run

| Step | Total | Quantity |
|---|---:|---:|
| Initial | 50 | 4 |
| After `*=` | 200 | 4 |

### Explanation

The initial amount is `50`.

The quantity is `4`.

The calculation becomes:

```text
50 × 4 = 200
```

### Learning Point

The `*=` operator is useful in shopping applications, pricing calculations, and scaling operations.

---

## Problem 4: Divide an Amount

**Operator:** `/=`

### Problem Statement

Divide a total amount equally among a given number of people.

### Logic

1. Read the total amount.
2. Read the number of people.
3. Check that the number of people is not zero.
4. Divide using `/=`.
5. Display the amount per person.

### Example Code

```python
amount = 1200
people = 4

if people > 0:
    amount /= people
    print("Amount Per Person:", amount)
else:
    print("Number of people must be greater than zero.")
```

### Output

```text
Amount Per Person: 300.0
```

### Dry Run

| Step | Amount | People |
|---|---:|---:|
| Initial | 1200 | 4 |
| After `/=` | 300.0 | 4 |

### Explanation

The amount is `1200`.

The number of people is `4`.

Each person receives:

```text
1200 / 4 = 300.0
```

### Learning Point

Always validate the divisor before performing division.

---

## Problem 5: Calculate Complete Groups

**Operator:** `//=`

### Problem Statement

A collection contains a certain number of items. Find the number of complete groups that can be created when each group has a fixed size.

### Logic

1. Read the total number of items.
2. Read the group size.
3. Check that the group size is greater than zero.
4. Apply floor division assignment.
5. Display complete groups.

### Example Code

```python
items = 23
group_size = 5

items //= group_size

print("Complete Groups:", items)
```

### Output

```text
Complete Groups: 4
```

### Explanation

A group contains five items.

There are twenty-three items.

Four complete groups can be created:

```text
23 // 5 = 4
```

Three items remain.

### Learning Point

Floor division is useful when calculating complete groups, pages, boxes, or batches.

---

## Problem 6: Find Remaining Items

**Operator:** `%=`

### Problem Statement

Find the number of items left after forming as many complete groups as possible.

### Logic

1. Read total items.
2. Read the group size.
3. Check that the group size is not zero.
4. Apply modulus assignment.
5. Display the remaining items.

### Example Code

```python
items = 23
group_size = 5

items %= group_size

print("Remaining Items:", items)
```

### Output

```text
Remaining Items: 3
```

### Explanation

The division is:

```text
23 = 5 × 4 + 3
```

The remainder is `3`.

### Learning Point

The `%=` operator is useful for calculating remainders, extracting digits, and checking divisibility.

---

## Problem 7: Calculate a Power

**Operator:** `**=`

### Problem Statement

Calculate the power of a number using exponentiation assignment.

### Logic

1. Read the base.
2. Read the exponent.
3. Apply `**=`.
4. Display the result.

### Example Code

```python
number = 9

number **= 2

print("Square:", number)
```

### Output

```text
Square: 81
```

### Explanation

The square of nine is:

```text
9 × 9 = 81
```

### Learning Point

The `**=` operator is useful for mathematical calculations involving powers.

---

## Problem 8: Apply a Bitwise AND Mask

**Operator:** `&=`

### Problem Statement

Apply a bitwise AND mask to an integer and display the result.

### Logic

1. Read an integer.
2. Read the mask.
3. Apply AND assignment.
4. Display the result.

### Example Code

```python
number = 12
mask = 10

number &= mask

print("Result:", number)
```

### Output

```text
Result: 8
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     1000
```

### Learning Point

AND assignment is useful when selecting or retaining particular bits.

---

## Problem 9: Enable Flags

**Operator:** `|=`

### Problem Statement

Use bitwise OR assignment to enable selected bits in a flag value.

### Logic

1. Read the original flag value.
2. Read the mask.
3. Apply OR assignment.
4. Display the updated flags.

### Example Code

```python
flags = 8
mask = 3

flags |= mask

print("Updated Flags:", flags)
```

### Output

```text
Updated Flags: 11
```

### Binary Calculation

```text
8 = 1000
3 = 0011
-----------
    1011
```

### Learning Point

OR assignment can enable selected bits while retaining previously enabled bits.

---

## Problem 10: Toggle a Flag

**Operator:** `^=`

### Problem Statement

Toggle selected bits in a flag value using XOR assignment.

### Logic

1. Read the original flag value.
2. Read a bit mask.
3. Apply XOR assignment.
4. Display the updated value.

### Example Code

```python
flags = 12
mask = 10

flags ^= mask

print("Updated Flags:", flags)
```

### Output

```text
Updated Flags: 6
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     0110
```

### Learning Point

XOR assignment is useful for toggling specific bits.

---

## Problem 11: Left and Right Shift Assignment

**Operators:** `<<=` and `>>=`

### Problem Statement

Perform left shift and right shift assignment operations on integer values.

### Left Shift Example

```python
number = 5

number <<= 1

print("Left Shift:", number)
```

**Output:**

```text
Left Shift: 10
```

### Right Shift Example

```python
number = 20

number >>= 2

print("Right Shift:", number)
```

**Output:**

```text
Right Shift: 5
```

### Explanation

Left shift moves bits toward the left.

Right shift moves bits toward the right.

### Learning Point

Shift assignment is useful in binary calculations and bit manipulation problems.

---

## Problem 12: Swap Three Values

**Concept:** Multiple assignment

### Problem Statement

Take three values and rotate their values using multiple assignment.

### Logic

1. Read three variables.
2. Store the values using multiple assignment.
3. Perform the rotation.
4. Display the updated values.

### Example Code

```python
a = 10
b = 20
c = 30

a, b, c = c, a, b

print("A:", a)
print("B:", b)
print("C:", c)
```

### Output

```text
A: 30
B: 10
C: 20
```

### Dry Run

| Variable | Before | After |
|---|---:|---:|
| `a` | 10 | 30 |
| `b` | 20 | 10 |
| `c` | 30 | 20 |

### Explanation

The right-hand side is evaluated first:

```python
c, a, b
```

The resulting values are then assigned to:

```python
a, b, c
```

### Learning Point

Multiple assignment is useful for swapping, rotating, and unpacking values.

---

# 21. Ten Unsolved Practice Questions

Solve the following questions independently.

Do not immediately copy a solution. First identify the required assignment operator and then write the logic.

## Question 1: Update Bank Balance

**Concept:** `+=`

Write a program that:

1. Accepts the initial bank balance.
2. Accepts a deposit amount.
3. Updates the balance using `+=`.
4. Displays the final balance.

Example:

```text
Initial Balance: 5000
Deposit Amount: 1500
Updated Balance: 6500
```

**Hint:** Use addition assignment.

## Question 2: Reduce Product Stock

**Concept:** `-=`

Write a program that:

1. Accepts the available product stock.
2. Accepts the quantity sold.
3. Reduces stock using `-=`.
4. Displays remaining stock.

**Hint:** Validate that the quantity sold does not exceed available stock.

## Question 3: Calculate Total Price

**Concept:** `*=`

Write a program that accepts:

- Product price.
- Product quantity.

Calculate the total price using multiplication assignment.

**Hint:** Store the unit price in a variable and multiply it by the quantity.

## Question 4: Divide an Amount

**Concept:** `/=`

Write a program that divides an amount equally among a group of people.

Requirements:

- Accept the total amount.
- Accept the number of people.
- Check for division by zero.
- Display the amount per person.

## Question 5: Find Complete Groups

**Concept:** `//=`

Write a program that calculates how many complete groups can be made from a given quantity of items.

Example:

```text
Total Items: 47
Items Per Group: 6
Complete Groups: 7
```

## Question 6: Find Remaining Items

**Concept:** `%=`

Write a program that calculates the remaining items after creating complete groups.

Example:

```text
Total Items: 47
Items Per Group: 6
Remaining Items: 5
```

## Question 7: Calculate Exponentiation

**Concept:** `**=`

Write a program that accepts a base and exponent and calculates the result using exponentiation assignment.

Example:

```text
Base: 2
Exponent: 5
Result: 32
```

## Question 8: Enable Flags

**Concept:** `|=`

Write a program that accepts an original flag value and a mask.

Use OR assignment to enable the selected bits.

Display the resulting flag value.

## Question 9: Toggle a Bit

**Concept:** `^=`

Write a program that accepts an integer and a mask.

Apply XOR assignment to toggle the selected bits.

Display the result.

## Question 10: Rotate Three Values

**Concept:** Multiple assignment

Write a program that accepts three values and rotates them in this order:

- The third value becomes the first.
- The first value becomes the second.
- The second value becomes the third.

Use multiple assignment without using a temporary variable.

---

# 22. Dry Run and Output Prediction

Dry running means manually tracing a program to understand how variable values change.

It is an important programming skill.

## 22.1 Question 1

Predict the output:

```python
x = 10
x += 5
x *= 2
x -= 4

print(x)
```

### Dry Run

| Step | Operation | Value of x |
|---:|---|---:|
| 1 | `x = 10` | 10 |
| 2 | `x += 5` | 15 |
| 3 | `x *= 2` | 30 |
| 4 | `x -= 4` | 26 |

**Answer:**

```text
26
```

## 22.2 Question 2

Predict the output:

```python
a = 20
b = 5

a //= b
b += 2

print(a, b)
```

### Dry Run

| Step | Operation | a | b |
|---:|---|---:|---:|
| 1 | Initial | 20 | 5 |
| 2 | `a //= b` | 4 | 5 |
| 3 | `b += 2` | 4 | 7 |

**Answer:**

```text
4 7
```

## 22.3 Question 3

Predict the output:

```python
number = 17

number %= 5
number += 10

print(number)
```

### Dry Run

| Step | Operation | Value |
|---:|---|---:|
| 1 | `number = 17` | 17 |
| 2 | `number %= 5` | 2 |
| 3 | `number += 10` | 12 |

**Answer:**

```text
12
```

## 22.4 Question 4

Predict the output:

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

**Answer:**

```text
20 10
```

## 22.5 Question 5

Predict the output:

```python
number = 5

number <<= 2

print(number)
```

**Answer:**

```text
20
```

---

# 23. Common Programming Mistakes

Understanding common mistakes is an important part of learning assignment operators.

## Mistake 1: Confusing `=` and `==`

Incorrect:

```python
if number = 10:
    print("Equal")
```

Correct:

```python
if number == 10:
    print("Equal")
```

`=` assigns a value, while `==` performs equality comparison.

## Mistake 2: Division by Zero

Incorrect:

```python
number = 10
number /= 0
```

This raises:

```text
ZeroDivisionError
```

Correct:

```python
number = 10
divisor = 0

if divisor != 0:
    number /= divisor
    print(number)
else:
    print("Cannot divide by zero.")
```

## Mistake 3: Incorrect Variable Names

Incorrect:

```python
total marks = 100
```

Correct:

```python
total_marks = 100
```

Variable names cannot contain spaces.

## Mistake 4: Mismatched Multiple Assignment

Incorrect:

```python
a, b, c = 10, 20
```

This raises a `ValueError` because there are three targets but only two values.

Correct:

```python
a, b, c = 10, 20, 30
```

## Mistake 5: Forgetting to Store an Updated Value

Incorrect:

```python
number = 10

number + 5

print(number)
```

Output:

```text
10
```

Correct:

```python
number = 10

number += 5

print(number)
```

Output:

```text
15
```

## Mistake 6: Forgetting Input Conversion

The `input()` function returns a string.

Incorrect:

```python
number = input("Enter a number: ")
number += 5
```

Correct:

```python
number = int(input("Enter a number: "))
number += 5

print(number)
```

## Mistake 7: Assuming `/=` Produces an Integer

```python
number = 10
number /= 2

print(number)
```

Output:

```text
5.0
```

True division returns a floating-point result.

## Mistake 8: Using Bitwise Operations with Incompatible Types

Incorrect:

```python
value = "Python"
value &= 5
```

Bitwise AND is not supported between a string and an integer.

Use integer operands for bitwise operations.

## Mistake 9: Ignoring Mutable Object References

```python
a = []
b = a

a.append(10)

print(b)
```

Output:

```text
[10]
```

Both names refer to the same list.

## Mistake 10: Using an Invalid Shift Count

Bit shifting requires a non-negative shift count.

An expression such as:

```python
number <<= -1
```

raises a `ValueError`.

---

# 24. Error Handling and Input Validation

Input validation ensures that a program receives acceptable data before performing an operation.

## 24.1 Handling Invalid Integer Input

```python
try:
    number = int(input("Enter an integer: "))
    print(number)
except ValueError:
    print("Please enter a valid integer.")
```

If the user enters text that cannot be converted into an integer, Python raises a `ValueError`.

## 24.2 Handling Division by Zero

```python
number = 100
divisor = 0

try:
    number /= divisor
    print(number)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

## 24.3 Validating a Positive Quantity

```python
quantity = int(input("Enter quantity: "))

if quantity > 0:
    print("Valid quantity")
else:
    print("Quantity must be positive")
```

## 24.4 Validating Floating-Point Input

The learning program uses `math.isfinite()` to reject non-finite floating-point values.

Example:

```python
import math

value = float(input("Enter a value: "))

if math.isfinite(value):
    print("Valid finite number:", value)
else:
    print("Enter a finite number.")
```

### Why Is Validation Important?

- Prevents unexpected program termination.
- Improves the user experience.
- Prevents invalid calculations.
- Makes programs more reliable.
- Helps maintain correct application data.

---

# 25. Best Practices

Follow these practices while writing Python programs.

1. Use meaningful variable names.
2. Prefer augmented assignment when it makes an update clearer.
3. Use multiple assignment when it improves readability.
4. Validate input before calculations.
5. Check for zero before division.
6. Use integer operands for the bitwise examples.
7. Avoid unnecessarily complicated assignment statements.
8. Keep code readable and properly formatted.
9. Understand mutable and immutable objects.
10. Test programs with multiple inputs.
11. Use comments when bitwise operations are not obvious.
12. Avoid chained assignment with mutable objects when separate objects are required.
13. Use clear conditions to validate quantities and balances.
14. Keep input handling separate from calculation logic.
15. Use helper functions to reduce repeated code.

---

# 26. Real-World Applications

Assignment operators are used throughout software development.

## 26.1 Banking Applications

Updating bank balances:

```python
balance = 5000

balance += 1000
balance -= 500

print("Current Balance:", balance)
```

Output:

```text
Current Balance: 5500
```

## 26.2 Shopping Applications

Calculating the total price:

```python
total = 100
quantity = 3

total *= quantity

print("Total Price:", total)
```

Output:

```text
Total Price: 300
```

## 26.3 Inventory Management

Updating product stock:

```python
stock = 200

stock -= 15

print("Remaining Stock:", stock)
```

Output:

```text
Remaining Stock: 185
```

## 26.4 Game Development

Updating player score:

```python
score = 0

score += 100

print("Player Score:", score)
```

Output:

```text
Player Score: 100
```

## 26.5 Game Health Management

```python
health = 100

health -= 20

print("Remaining Health:", health)
```

Output:

```text
Remaining Health: 80
```

## 26.6 Permission Systems

Enabling flags:

```python
permissions = 8
permissions |= 3

print(permissions)
```

Output:

```text
11
```

## 26.7 Counter Applications

```python
visitors = 0

visitors += 1
visitors += 1
visitors += 1

print("Total Visitors:", visitors)
```

Output:

```text
Total Visitors: 3
```

---

# 27. Assignment Operators in DSA

Assignment operators are essential when learning Data Structures and Algorithms.

You will use them in many algorithmic patterns.

## 27.1 Counter Updates

Counters are used to count how many times an operation occurs.

```python
count = 0

count += 1
count += 1
count += 1

print(count)
```

Output:

```text
3
```

Applications:

- Counting array elements.
- Counting loop iterations.
- Counting occurrences.
- Tracking comparisons.

## 27.2 Running Sum

A running sum maintains the total of values processed so far.

```python
total = 0

total += 10
total += 20
total += 30

print(total)
```

Output:

```text
60
```

Applications:

- Array sum.
- Prefix sum.
- Subarray problems.
- Statistical calculations.

## 27.3 Updating an Array Index

```python
index = 0

index += 1

print(index)
```

Output:

```text
1
```

Applications:

- Array traversal.
- String traversal.
- Loop counters.
- Searching.

## 27.4 Two-Pointer Technique

```python
left = 0
right = 5

left += 1
right -= 1

print(left, right)
```

Output:

```text
1 4
```

Applications:

- Pair sum problems.
- Reversing arrays.
- Palindrome checking.
- Sorting-based problems.
- Sliding boundaries.

## 27.5 Bit Manipulation

```python
number = 5

number <<= 1

print(number)
```

Output:

```text
10
```

Applications:

- Bit masks.
- Set-bit counting.
- Binary flags.
- Subset generation.
- Bitwise optimization.

## 27.6 Inventory-Like Array Updates

```python
stock = 50

stock -= 3

print(stock)
```

Output:

```text
47
```

This is conceptually similar to updating values stored in data structures.

## 27.7 Why Should You Learn Assignment Operators Before DSA?

Because DSA questions frequently involve:

- Updating indexes.
- Maintaining counters.
- Calculating sums.
- Updating pointers.
- Modifying values.
- Managing bit masks.
- Repeating calculations inside loops.

A strong understanding of assignment operations makes these problems easier.

---

# 28. Time and Space Complexity

Assignment statements are generally constant-time operations for common built-in scalar values, but the cost depends on the operation and operand types.

## 28.1 Basic Assignment

Example:

```python
x = 10
```

This is generally an O(1) name-binding operation.

## 28.2 Integer Arithmetic Assignment

Example:

```python
x += 5
```

For ordinary fixed-size integer reasoning, this is commonly treated as O(1).

However, Python integers can grow arbitrarily large, so operations on very large integers depend on their size.

## 28.3 Bitwise Assignment

Example:

```python
x &= mask
```

The cost depends on the size of the integer operands.

For ordinary small integers, it is generally efficient.

## 28.4 List Augmented Assignment

Example:

```python
numbers += [4, 5]
```

For lists, this operation extends the list.

Its cost depends on how many elements are added and whether additional memory allocation is required.

## 28.5 Space Complexity

Simple assignment does not automatically create a deep copy of an object.

For example:

```python
a = [1, 2, 3]
b = a
```

Both names refer to the same list.

Creating a copy requires a separate operation.

### Complexity Summary

| Operation | Typical Learning-Level Complexity |
|---|---|
| Basic name assignment | O(1) |
| Integer counter update | Usually treated as O(1) |
| Integer bitwise operation | Depends on integer size |
| List extension using `+=` | Depends on added elements |
| Assigning another reference | O(1) |
| Copying a list | O(n) |

---

# 29. Interview and Viva Questions

Prepare the following questions for college viva, practical examinations, and technical interviews.

## Section A: Basic Concepts

### Q1. What is an assignment operator?

An assignment operator is used to assign a value to a variable.

### Q2. Which symbol is used for basic assignment in Python?

The `=` symbol.

### Q3. What is the purpose of assignment?

Assignment associates a variable name with a value or object.

### Q4. What is variable reassignment?

Assigning a new value or object to an existing variable name.

### Q5. Can a Python variable be reassigned?

Yes. Python variables can be reassigned during program execution.

### Q6. Can a variable store different data types at different times?

Yes. Python is dynamically typed.

### Q7. What is multiple assignment?

Assigning values to multiple variables in one statement.

### Q8. What is chained assignment?

Assigning the same value or object to multiple variables in one statement.

### Q9. What is unpacking?

Unpacking distributes values from an iterable into multiple assignment targets.

### Q10. What is augmented assignment?

It combines an operation with assignment.

## Section B: Arithmetic Assignment

### Q11. What does `+=` mean?

It adds a value to the existing variable and assigns the result back.

### Q12. What does `-=` mean?

It subtracts a value and assigns the result back.

### Q13. What does `*=` mean?

It multiplies the existing value and assigns the result back.

### Q14. What does `/=` mean?

It performs true division and assigns the result back.

### Q15. What does `//=` mean?

It performs floor division and assigns the result back.

### Q16. What does `%=` mean?

It calculates a remainder and assigns the result back.

### Q17. What does `**=` mean?

It performs exponentiation and assigns the result back.

### Q18. What is the difference between `/=` and `//=`?

`/=` performs true division, while `//=` performs floor division.

### Q19. What is the result of `number = 10; number += 5`?

The result is `15`.

### Q20. What is the result of `number = 17; number %= 5`?

The result is `2`.

## Section C: Multiple Assignment

### Q21. How do you assign multiple values in Python?

Use comma-separated assignment targets and values.

```python
a, b = 10, 20
```

### Q22. How do you swap two variables in Python?

```python
a, b = b, a
```

### Q23. Is a temporary variable required for swapping in Python?

No. Multiple assignment can swap two variables without a temporary variable.

### Q24. What happens if the number of unpacked values does not match the targets?

Python raises a `ValueError` in ordinary unpacking.

### Q25. Can multiple assignment use different data types?

Yes.

### Q26. What happens in `a = b = []`?

Both variables refer to the same list object.

### Q27. Why can chained assignment with mutable objects be risky?

Because changes made through one variable may also appear through the other variable.

### Q28. What is the difference between multiple assignment and chained assignment?

Multiple assignment can distribute different values, whereas chained assignment binds multiple targets to the same value or object.

### Q29. Can expressions be used in multiple assignment?

Yes. Each expression is evaluated before assignment.

### Q30. Can a list be unpacked into variables?

Yes, if the unpacking targets match the elements or use valid starred unpacking.

## Section D: Bitwise Assignment

### Q31. What is a bitwise assignment operator?

It performs a bitwise operation and assigns the result back to the target.

### Q32. What does `&=` mean?

Bitwise AND assignment.

### Q33. What does `|=` mean?

Bitwise OR assignment.

### Q34. What does `^=` mean?

Bitwise XOR assignment.

### Q35. What does `<<=` mean?

Left shift assignment.

### Q36. What does `>>=` mean?

Right shift assignment.

### Q37. What is a bit mask?

A value used to select, enable, disable, or toggle particular bits.

### Q38. What is the result of `12 & 10`?

The result is `8`.

### Q39. What is the result of `12 | 10`?

The result is `14`.

### Q40. What is the result of `12 ^ 10`?

The result is `6`.

## Section E: Advanced and Practical Questions

### Q41. What is the difference between `=` and `==`?

`=` assigns a value; `==` checks equality.

### Q42. What happens when division by zero is attempted?

Python raises `ZeroDivisionError`.

### Q43. What is the walrus operator?

The `:=` operator is an assignment expression that assigns a value within an expression.

### Q44. Does augmented assignment always create a new object?

No. Depending on the object type and implementation, it can modify a mutable object in place.

### Q45. What is the difference between mutable and immutable objects?

Mutable objects can be changed after creation. Immutable objects cannot be changed after creation.

### Q46. Give examples of mutable Python objects.

Lists, dictionaries, and sets.

### Q47. Give examples of immutable Python objects.

Integers, floats, strings, tuples, and Booleans.

### Q48. Where are assignment operators used in DSA?

They are used for counters, running sums, indexes, pointers, and bit manipulation.

### Q49. Why is `+=` commonly used in loops?

It is a convenient way to update counters and accumulated totals.

### Q50. Why should you understand assignment operators before learning loops?

Loops repeatedly update variables such as counters, indexes, and accumulated values.

---

# 30. Practice Test

Use this test to check whether you understand the topic.

## Part A: Predict the Output

### Question 1

```python
x = 10
x += 5

print(x)
```

### Question 2

```python
x = 20
x -= 7

print(x)
```

### Question 3

```python
x = 5
x *= 4

print(x)
```

### Question 4

```python
x = 25
x //= 4

print(x)
```

### Question 5

```python
x = 25
x %= 4

print(x)
```

### Question 6

```python
x = 2
x **= 5

print(x)
```

### Question 7

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

### Question 8

```python
x = 5
x <<= 2

print(x)
```

### Question 9

```python
x = 20
x >>= 2

print(x)
```

### Question 10

```python
a = 10
b = 5

a += b
b *= 2

print(a, b)
```

## Part B: Identify the Operator

1. Add a value to an existing variable.
2. Subtract a value from an existing variable.
3. Multiply an existing variable.
4. Divide an existing variable.
5. Find a remainder and assign it.
6. Raise an existing variable to a power.
7. Perform bitwise AND and assign the result.
8. Enable selected bits.
9. Toggle selected bits.
10. Shift the binary representation to the right.

## Part C: Programming Challenges

1. Update a bank balance after a deposit and withdrawal.
2. Calculate the total value of products in a cart.
3. Divide a bill equally among friends.
4. Calculate complete groups and remaining items.
5. Swap three variables.
6. Apply a bit mask to an integer.
7. Enable a permission flag.
8. Toggle a selected bit.
9. Calculate a number's cube.
10. Build a simple score counter using `+=`.

---

# 31. Quick Revision Notes

## 31.1 Basic Assignment

```python
x = 10
```

Assigns `10` to `x`.

## 31.2 Reassignment

```python
x = 20
```

Assigns another value to `x`.

## 31.3 Multiple Assignment

```python
a, b = 10, 20
```

Assigns two different values.

## 31.4 Chained Assignment

```python
a = b = 100
```

Assigns the same value or object to both names.

## 31.5 Swapping

```python
a, b = b, a
```

Exchanges the values.

## 31.6 Arithmetic Assignment

```python
x += 5
x -= 5
x *= 5
x /= 5
x //= 5
x %= 5
x **= 5
```

## 31.7 Bitwise Assignment

```python
x &= 5
x |= 5
x ^= 5
x <<= 1
x >>= 1
```

## 31.8 Important Reminders

- `=` assigns a value.
- `==` compares two values.
- `/=` performs true division.
- `//=` performs floor division.
- `%=` calculates the remainder.
- `**=` calculates a power.
- `&=` performs bitwise AND.
- `|=` performs bitwise OR.
- `^=` performs bitwise XOR.
- `<<=` shifts bits to the left.
- `>>=` shifts bits to the right.
- Check for zero before division.
- Use multiple assignment for swapping.
- Be careful when multiple variables reference the same mutable object.

---

# 32. Important Terminology

| Term | Meaning |
|---|---|
| Assignment | Associating a variable name with a value or object |
| Reassignment | Assigning another value or object to an existing name |
| Variable | A name used to refer to an object |
| Assignment statement | A Python statement that performs assignment |
| Augmented assignment | Combining an operation with assignment |
| Operand | A value on which an operator works |
| Multiple assignment | Assigning multiple values to multiple targets |
| Chained assignment | Assigning one value or object to multiple targets |
| Unpacking | Distributing values from an iterable |
| Mutable | An object that can be changed |
| Immutable | An object that cannot be changed after creation |
| Bit | A binary digit, either `0` or `1` |
| Bitwise operation | An operation performed on binary representations |
| Bit mask | A value used to select or modify particular bits |
| Floor division | Division rounded down to the nearest integer value for integer operands |
| Remainder | The amount left after division |
| Exponentiation | Raising a number to a power |
| Variable swapping | Exchanging values between variables |
| Input validation | Checking whether input is acceptable |
| Exception | An event that interrupts normal program execution |

---

# 33. Learning Checklist

Complete this checklist after studying the topic.

## Basic Assignment

- [ ] I understand basic assignment (`=`).
- [ ] I understand variable reassignment.
- [ ] I can assign integer values.
- [ ] I can assign float values.
- [ ] I can assign string values.
- [ ] I can assign Boolean values.
- [ ] I understand assignment using expressions.

## Multiple Assignment

- [ ] I can assign multiple values in one statement.
- [ ] I understand chained assignment.
- [ ] I understand unpacking.
- [ ] I can swap two variables.
- [ ] I can rotate three values.
- [ ] I understand mutable object references.

## Arithmetic Assignment

- [ ] I understand addition assignment (`+=`).
- [ ] I understand subtraction assignment (`-=`).
- [ ] I understand multiplication assignment (`*=`).
- [ ] I understand division assignment (`/=`).
- [ ] I understand floor division assignment (`//=`).
- [ ] I understand modulus assignment (`%=`).
- [ ] I understand exponentiation assignment (`**=`).

## Bitwise Assignment

- [ ] I understand bitwise AND assignment (`&=`).
- [ ] I understand bitwise OR assignment (`|=`).
- [ ] I understand bitwise XOR assignment (`^=`).
- [ ] I understand left shift assignment (`<<=`).
- [ ] I understand right shift assignment (`>>=`).
- [ ] I can read basic binary calculations.

## Programming Practice

- [ ] I can update a counter using `+=`.
- [ ] I can reduce a value using `-=`.
- [ ] I can calculate totals using `*=`.
- [ ] I can divide values safely.
- [ ] I can calculate complete groups using `//=`.
- [ ] I can calculate remainders using `%=`.
- [ ] I can use multiple assignment for swapping.
- [ ] I have practised all twelve solved problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I have completed the practice test.

---

# 34. How to Run the Python Program

Make sure Python is installed on your computer.

Open a terminal in the Assignment Operators folder.

## 34.1 Run the Program

```bash
python 01_assignment_operators.py
```

On systems where `python3` is used:

```bash
python3 01_assignment_operators.py
```

## 34.2 Expected Main Menu

The program provides the following learning options:

```text
1. View 12 Assignment Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

## 34.3 Recommended Usage

### Step 1: Study Examples

Select option `1`.

Read the twelve examples carefully and understand the result of each operation.

### Step 2: Practise Solved Problems

Select option `2`.

Run the solved problems and experiment with different inputs.

### Step 3: Attempt Practice Questions

Select option `3`.

Read the ten unsolved questions and try solving them independently.

### Step 4: Review the Checklist

Select option `4`.

Check which concepts you have understood and which require more practice.

### Step 5: Exit

Select option `0` when you finish the practice session.

---

# 35. Recommended Learning Sequence

Follow this sequence to study Assignment Operators properly.

| Order | Topic | What to Do |
|---:|---|---|
| 1 | Assignment (`=`) | Understand basic variable assignment |
| 2 | Reassignment | Practise updating existing variables |
| 3 | Multiple Assignment | Assign different values to multiple variables |
| 4 | Chained Assignment | Assign the same value to multiple names |
| 5 | Variable Swapping | Practise exchanging variable values |
| 6 | `+=` and `-=` | Practise increasing and decreasing values |
| 7 | `*=` and `/=` | Practise multiplication and division |
| 8 | `//=` and `%=` | Practise groups and remainders |
| 9 | `**=` | Practise powers |
| 10 | Bitwise Assignment | Understand binary operations |
| 11 | Shift Assignment | Practise left and right shifts |
| 12 | Practical Problems | Solve real-world calculation problems |

## Before Moving to the Next Topic

Make sure that:

1. You understand the difference between assignment and comparison.
2. You can use all arithmetic assignment operators.
3. You understand multiple assignment.
4. You can solve basic bitwise assignment questions.
5. You have completed the solved examples.
6. You have attempted the unsolved questions.

---

# 36. Topic Completion Summary

In this topic, you learned how to assign values to variables and update those values using Python assignment operators.

You covered:

- Basic assignment.
- Variable reassignment.
- Multiple assignment.
- Chained assignment.
- Variable swapping.
- Augmented assignment.
- Arithmetic assignment operators.
- Bitwise assignment operators.
- Normal assignment vs augmented assignment.
- Assignment vs comparison.
- Mutable and immutable objects.
- The walrus operator.
- Input validation and error handling.
- Real-world applications.
- DSA applications.
- Dry runs and output prediction.
- Programming practice.
- Interview and viva questions.

Assignment operators are among the most frequently used features in Python. You will use them while learning conditions, loops, functions, arrays, strings, searching, sorting, and Data Structures and Algorithms.

The most important thing is not just memorizing the operators. You should understand how every operation changes the value of a variable.

**Practise the examples, execute all twelve solved problems, and attempt the ten unsolved questions before moving forward.**

---

## Navigation

**Previous Topic:** [Arithmetic Operators](../01-Arithmetic-Operators/README.md)

**Next Topic:** [Comparison Operators](../03-Comparison-Operators/README.md)

**Parent Section:** [Operators and Expressions](../README.md)
