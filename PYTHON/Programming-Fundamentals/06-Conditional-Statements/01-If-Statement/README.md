# Python If Statement – Complete Detailed Guide

## Week 1 – Programming Fundamentals

**Section:** 06 – Conditional Statements  
**Topic:** 01 – If Statement  
**Python File:** `01_if.py`  
**Documentation File:** `README.md`  
**Level:** Beginner to Intermediate

---

# Table of Contents

1. Introduction to Conditional Statements
2. What Is Decision-Making?
3. What Is an If Statement?
4. Why Do We Need If Statements?
5. Syntax of the If Statement
6. Components of an If Statement
7. Understanding Conditions
8. Boolean Values
9. Truthy and Falsy Values
10. Comparison Operators
11. Arithmetic Operators in If Conditions
12. Logical Operators in If Conditions
13. Membership Operators in If Conditions
14. Identity Operators in If Conditions
15. Indentation in Python
16. If Blocks and Code Suites
17. How Python Executes an If Statement
18. If Statement Without Else
19. Multiple Statements Inside If
20. Multiple Independent If Statements
21. Using Pass in an If Block
22. Taking User Input
23. If Statements With Integer Values
24. If Statements With Floating-Point Values
25. If Statements With String Values
26. If Statements With Lists
27. If Statements With Tuples and Dictionaries
28. If Statements With Functions
29. Nested If – Introduction
30. If Statements in Real-World Applications
31. Explanation of 12 Topic Examples
32. Twelve Solved Programming Problems
33. Ten Unsolved Practice Questions
34. Dry Run and Trace Tables
35. Flowchart and Algorithm
36. Common Programming Mistakes
37. Debugging Techniques
38. Best Practices
39. Practical Applications
40. If Statements and Data Structures
41. If Statements and Algorithms
42. Time and Space Complexity
43. Mini Project – Student Eligibility Checker
44. Practice Test
45. Viva and Interview Questions
46. Important Glossary
47. Quick Revision Notes
48. Learning Checklist
49. How to Run the Python Program
50. Repository Folder Structure
51. Previous and Next Topics
52. Final Summary

---

# 1. Introduction to Conditional Statements

Python is a programming language used to develop applications, websites, automation programs, data-processing systems and many other software solutions.

A Python program contains instructions that tell the computer what operations to perform.

In a simple program, instructions are commonly executed in sequence. However, real-world programs often need to make decisions.

For example:

- A student should receive a pass message only when their marks meet the required threshold.
- A shopping application should apply a discount only when the order value satisfies a particular rule.
- A program should display an even-number message only when a number is divisible by two.
- A user should receive an access message only when the required condition is satisfied.
- A system should check product availability before processing an order.
- A program should calculate a special benefit only when the user meets the eligibility criteria.

These situations require decision-making.

Python provides conditional statements to control which instructions execute based on conditions.

The main conditional structures covered in this section are:

1. `if`
2. `if-else`
3. `if-elif-else`
4. Nested `if`
5. Conditional expressions
6. `match-case`

This topic introduces the basic `if` statement.

The `if` statement is the foundation of conditional programming in Python.

## 1.1 Meaning of Conditional Statements

A conditional statement is a programming construct that allows a program to execute certain instructions depending on whether a condition is satisfied.

Example:

```python
marks = 65

if marks >= 40:
    print("Student has passed.")
```

Output:

```text
Student has passed.
```

Python evaluates:

```python
marks >= 40
```

Since the condition evaluates to `True`, the indented statement executes.

Now change the marks:

```python
marks = 25

if marks >= 40:
    print("Student has passed.")
```

Output:

```text
```

The condition is false, so the statement inside the block is skipped.

## 1.2 Why Are Conditional Statements Important?

Conditional statements allow programs to respond differently to different situations.

Without conditions, a program would not be able to select actions according to changing input values.

Consider:

```python
print("You are eligible.")
```

This program always displays the same message.

It does not check whether the user actually satisfies any eligibility condition.

Now use an `if` statement:

```python
age = 16

if age >= 18:
    print("You meet the example age requirement.")
```

The program displays the message only when the condition is satisfied.

## 1.3 Benefits of Conditional Statements

1. Decision-making.
2. Input validation.
3. Eligibility checking.
4. Number classification.
5. Logical control.
6. Application flow management.
7. Error prevention.
8. Real-world rule implementation.
9. Algorithm development.
10. Better program flexibility.

---

# 2. What Is Decision-Making?

Decision-making means selecting an action according to a condition.

In programming, a condition is evaluated to determine whether a particular operation should execute.

Consider a student result system.

The rule is:

- Marks of 40 or above satisfy the example pass condition.
- Marks below 40 do not satisfy it.

The condition is:

```python
marks >= 40
```

When marks are 75:

```text
75 >= 40

True
```

When marks are 25:

```text
25 >= 40

False
```

Python uses these truth values to determine whether the `if` block executes.

## 2.1 Real-World Decision-Making Examples

| Situation | Condition | Action |
|---|---|---|
| Student result | Marks >= 40 | Display pass message |
| Age checking | Age >= 18 | Display example eligibility message |
| Shopping | Price >= 1000 | Apply example discount |
| Number checking | Number % 2 == 0 | Display even message |
| Login | Credentials match | Display success message |
| Inventory | Quantity > 0 | Display available message |
| Temperature | Temperature > 30 | Display hot message |
| Attendance | Attendance >= 75 | Display threshold message |
| Banking | Balance >= withdrawal | Continue transaction |
| Product validation | Product exists | Continue processing |

## 2.2 Decision-Making Process

A simple decision-making process contains these steps:

1. Receive input or obtain a variable value.
2. Evaluate a condition.
3. Determine whether the condition is truthy.
4. Execute the selected instructions when appropriate.
5. Continue with the remaining program instructions.

Example:

```python
number = 15

if number > 10:
    print("Number is greater than 10.")
```

---

# 3. What Is an If Statement?

The Python `if` statement is a conditional control-flow statement.

It executes its body when its condition evaluates to a truthy value.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

The condition is true, so the block executes.

Now consider:

```python
age = 15

if age >= 18:
    print("Adult")
```

Output:

```text
```

The condition is false, so the block is skipped.

## 3.1 Definition

An `if` statement is a Python control-flow statement that executes a block of code when a specified condition evaluates to a truthy value.

## 3.2 Important Characteristics

- `if` is a reserved Python keyword.
- The condition is written after `if`.
- A colon is required after the condition.
- The body is identified using indentation.
- The condition can be a comparison expression.
- The condition can contain logical operators.
- The condition can test strings and collections.
- The condition can call a function.
- Multiple statements can belong to one `if` block.
- A basic `if` statement does not require `else`.
- A false condition causes Python to skip the block.
- Execution continues after the block.

---

# 4. Why Do We Need If Statements?

Suppose a program needs to display a message when a student passes.

Without an `if` statement:

```python
print("Student has passed.")
```

The message is displayed every time.

With an `if` statement:

```python
marks = 80

if marks >= 40:
    print("Student has passed.")
```

Now the message depends on marks.

Another example:

```python
number = 12

if number % 2 == 0:
    print("The number is even.")
```

The message is displayed only when the number is divisible by two.

## 4.1 Problems Solved Using If Statements

1. Checking whether a number is positive.
2. Checking whether a number is even.
3. Finding whether a user meets a condition.
4. Applying discounts.
5. Checking whether a value exists.
6. Validating a password condition.
7. Checking whether a list contains elements.
8. Determining whether a year satisfies a mathematical rule.
9. Checking whether a triangle is valid.
10. Selecting whether a calculation should be performed.

---

# 5. Syntax of the If Statement

The general syntax is:

```python
if condition:
    statement
```

Example:

```python
number = 10

if number > 0:
    print("Positive number")
```

## 5.1 Syntax Components

| Component | Description |
|---|---|
| `if` | Starts the conditional statement |
| `condition` | Expression evaluated by Python |
| `:` | Marks the beginning of the suite |
| Indented body | Statements controlled by the condition |

## 5.2 The If Keyword

`if` is a reserved keyword.

Correct:

```python
if number > 0:
    print("Positive")
```

Incorrect:

```python
if = 10
```

The second example is invalid because `if` cannot be used as an ordinary variable name.

## 5.3 The Condition

A condition is an expression Python evaluates.

Example:

```python
age = 20

if age >= 18:
    print("Eligible according to the example rule.")
```

## 5.4 The Colon

Every `if` header must end with a colon.

Correct:

```python
if number > 0:
    print("Positive")
```

Incorrect:

```python
if number > 0
    print("Positive")
```

The incorrect form produces a syntax error.

## 5.5 The Indented Statement

The body contains the operations that execute when the condition is truthy.

Example:

```python
marks = 85

if marks >= 40:
    print("Pass")
    print("Congratulations")
```

Both print statements belong to the same block.

---

# 6. Components of an If Statement

Consider:

```python
number = 25

if number > 10:
    print("Number is greater than 10.")
```

The program contains the following components:

**Variable assignment**

```python
number = 25
```

Stores a value.

**Conditional keyword**

```python
if
```

Begins the conditional statement.

**Condition**

```python
number > 10
```

Checks whether the number is greater than 10.

**Colon**

```python
:
```

Marks the beginning of the conditional suite.

**Indented body**

```python
print("Number is greater than 10.")
```

Executes when the condition is truthy.

---

# 7. Understanding Conditions

A condition is an expression whose truth value is evaluated by Python.

Examples:

```python
age >= 18
```

```python
number > 0
```

```python
marks == 100
```

```python
name == "Amaan"
```

```python
number % 2 == 0
```

A condition can be simple or complex.

## 7.1 Simple Condition

```python
number = 15

if number > 10:
    print("Number is greater than 10.")
```

## 7.2 Equality Condition

```python
code = 1234

if code == 1234:
    print("Code matched.")
```

## 7.3 Not-Equal Condition

```python
number = 10

if number != 0:
    print("Number is not zero.")
```

## 7.4 Greater-Than Condition

```python
marks = 85

if marks > 40:
    print("Marks are greater than 40.")
```

## 7.5 Less-Than Condition

```python
temperature = 15

if temperature < 20:
    print("Temperature is below 20.")
```

## 7.6 Greater-Than-or-Equal Condition

```python
age = 18

if age >= 18:
    print("The example age condition is satisfied.")
```

## 7.7 Less-Than-or-Equal Condition

```python
score = 50

if score <= 50:
    print("Score is at most 50.")
```

---

# 8. Boolean Values in If Statements

Python has a Boolean data type called `bool`.

It contains two values:

```python
True
False
```

Boolean values are often produced by comparisons.

Example:

```python
a = 10
b = 5

result = a > b

print(result)
print(type(result))
```

Output:

```text
True
<class 'bool'>
```

## 8.1 True Condition

```python
is_active = True

if is_active:
    print("Account is active.")
```

Output:

```text
Account is active.
```

## 8.2 False Condition

```python
is_active = False

if is_active:
    print("Account is active.")
```

Output:

```text
```

## 8.3 Direct Boolean Variable

Recommended:

```python
is_logged_in = True

if is_logged_in:
    print("Welcome back.")
```

This is generally clearer than:

```python
if is_logged_in == True:
    print("Welcome back.")
```

---

# 9. Truthy and Falsy Values

Python allows many objects to be used directly in conditions.

An object is **truthy** when it evaluates to true in a Boolean context.

An object is **falsy** when it evaluates to false.

## 9.1 Common Falsy Values

| Value | Meaning |
|---|---|
| `False` | Boolean false |
| `None` | No value |
| `0` | Integer zero |
| `0.0` | Floating-point zero |
| `0j` | Complex zero |
| `""` | Empty string |
| `[]` | Empty list |
| `()` | Empty tuple |
| `{}` | Empty dictionary |
| `set()` | Empty set |
| `range(0)` | Empty range |

## 9.2 Truthy Integer

```python
value = 10

if value:
    print("Truthy integer.")
```

## 9.3 Falsy Integer

```python
value = 0

if value:
    print("Truthy integer.")
```

Output:

```text
```

## 9.4 Truthy String

```python
name = "Python"

if name:
    print("Name is available.")
```

## 9.5 Falsy String

```python
name = ""

if name:
    print("Name is available.")
```

Output:

```text
```

## 9.6 Truthy List

```python
numbers = [10, 20, 30]

if numbers:
    print("List contains data.")
```

## 9.7 Falsy List

```python
numbers = []

if numbers:
    print("List contains data.")
```

Output:

```text
```

## 9.8 Truthiness and None

Example:

```python
value = 0

if value is not None:
    print("A value is present.")
```

Output:

```text
A value is present.
```

This is different from:

```python
value = 0

if value:
    print("A truthy value is present.")
```

The second block does not execute.

Use `is not None` when checking specifically for `None`.

Do not use a truthiness check when zero or an empty collection is a valid value that must be preserved.

---

# 10. Comparison Operators in If Conditions

Comparison operators compare two values and produce a Boolean result.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal | `a == b` |
| `!=` | Not equal | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal | `a >= b` |
| `<=` | Less than or equal | `a <= b` |

## 10.1 Equal To

```python
a = 10
b = 10

if a == b:
    print("Both numbers are equal.")
```

## 10.2 Not Equal To

```python
a = 10
b = 20

if a != b:
    print("Numbers are different.")
```

## 10.3 Greater Than

```python
a = 50
b = 20

if a > b:
    print("First number is greater.")
```

## 10.4 Less Than

```python
a = 10
b = 20

if a < b:
    print("First number is smaller.")
```

## 10.5 Greater Than or Equal

```python
marks = 40

if marks >= 40:
    print("Minimum mark condition satisfied.")
```

## 10.6 Less Than or Equal

```python
age = 18

if age <= 18:
    print("Age is 18 or below.")
```

## 10.7 Comparison Operator Practice Table

| First value | Second value | Expression | Result |
|---:|---:|---|---|
| 10 | 5 | `10 == 5` | False |
| 10 | 10 | `10 == 10` | True |
| 20 | 10 | `20 != 10` | True |
| 5 | 10 | `5 > 10` | False |
| 5 | 10 | `5 < 10` | True |
| 10 | 10 | `10 >= 10` | True |
| 10 | 10 | `10 <= 10` | True |

---

# 11. Arithmetic Operators in If Conditions

Arithmetic operators can be used to calculate values before comparing them.

Common arithmetic operators:

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Modulo |
| `**` | Exponentiation |

## 11.1 Addition

```python
a = 10
b = 20

if a + b > 25:
    print("The sum is greater than 25.")
```

## 11.2 Subtraction

```python
a = 50
b = 20

if a - b == 30:
    print("Difference is 30.")
```

## 11.3 Multiplication

```python
a = 5
b = 4

if a * b == 20:
    print("Product is 20.")
```

## 11.4 Division

```python
a = 20
b = 2

if a / b == 10:
    print("Division result is 10.")
```

## 11.5 Modulo

```python
number = 12

if number % 2 == 0:
    print("Even number.")
```

## 11.6 Floor Division

```python
number = 25

if number // 5 == 5:
    print("Floor division result is 5.")
```

## 11.7 Exponentiation

```python
number = 2

if number ** 3 == 8:
    print("The cube is 8.")
```

---

# 12. Logical Operators in If Conditions

Logical operators combine or reverse conditions.

Python provides:

- `and`
- `or`
- `not`

## 12.1 AND Operator

The `and` operator requires both conditions to be truthy for the combined result to be truthy.

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Both conditions are satisfied.")
```

Output:

```text
Both conditions are satisfied.
```

### AND Truth Table

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Practical Example

```python
marks = 80
attendance = 85

if marks >= 40 and attendance >= 75:
    print("Both example requirements are satisfied.")
```

## 12.2 OR Operator

The `or` operator returns a truthy result when at least one operand is truthy.

Example:

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount condition is satisfied.")
```

Output:

```text
Discount condition is satisfied.
```

### OR Truth Table

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

## 12.3 NOT Operator

The `not` operator reverses the truth value of its operand.

Example:

```python
is_raining = False

if not is_raining:
    print("It is not raining.")
```

Output:

```text
It is not raining.
```

### NOT Truth Table

| A | not A |
|---|---|
| True | False |
| False | True |

## 12.4 Combining Three Logical Operators

```python
age = 20
has_id = True
is_banned = False

if age >= 18 and has_id and not is_banned:
    print("Example access condition satisfied.")
```

All three requirements are checked.

---

# 13. Membership Operators in If Conditions

Membership operators check whether an item exists in a collection.

Python provides:

- `in`
- `not in`

## 13.1 IN Operator

```python
fruits = ["Apple", "Banana", "Mango"]

if "Mango" in fruits:
    print("Mango is available.")
```

Output:

```text
Mango is available.
```

## 13.2 NOT IN Operator

```python
fruits = ["Apple", "Banana", "Mango"]

if "Orange" not in fruits:
    print("Orange is not available.")
```

Output:

```text
Orange is not available.
```

## 13.3 Membership in a String

```python
name = "Python Programming"

if "Python" in name:
    print("Python exists in the string.")
```

## 13.4 Membership in a Dictionary

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" in student:
    print("Marks key exists.")
```

For dictionaries, membership tests keys by default.

---

# 14. Identity Operators in If Conditions

Identity operators check whether two references point to the same object.

Python provides:

- `is`
- `is not`

Example:

```python
value = None

if value is None:
    print("Value is None.")
```

Output:

```text
Value is None.
```

## 14.1 IS Operator

```python
a = None

if a is None:
    print("No value is assigned.")
```

## 14.2 IS NOT Operator

```python
a = 10

if a is not None:
    print("A value is available.")
```

## 14.3 Equality and Identity Are Different

`==` checks equality of values.

`is` checks object identity.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Possible output:

```text
True
False
```

The lists contain equal values, but they are distinct list objects.

Use `is None` or `is not None` for checking `None`.

Do not use `is` as a replacement for ordinary value comparison.

---

# 15. Indentation in Python

Indentation means the spaces at the beginning of a line.

Python uses indentation to identify code blocks.

Example:

```python
number = 10

if number > 0:
    print("Positive")
```

The `print()` statement belongs to the `if` block because it is indented.

## 15.1 Standard Indentation

The recommended standard is four spaces per indentation level.

## 15.2 Correct Indentation

```python
number = 10

if number > 0:
    print("Positive")
    print("Number is greater than zero.")

print("Program completed.")
```

Output:

```text
Positive
Number is greater than zero.
Program completed.
```

## 15.3 Missing Indentation

Incorrect:

```python
number = 10

if number > 0:
print("Positive")
```

This produces an `IndentationError`.

Correct:

```python
number = 10

if number > 0:
    print("Positive")
```

## 15.4 Unexpected Indentation

Incorrect:

```python
number = 10

    if number > 0:
        print("Positive")
```

Correct:

```python
number = 10

if number > 0:
    print("Positive")
```

## 15.5 Mixing Tabs and Spaces

Python expects consistent indentation.

Use four spaces for each indentation level and configure your editor accordingly.

Mixing tabs and spaces inconsistently can cause `TabError` or indentation errors.

---

# 16. If Blocks and Code Suites

A suite is the group of statements controlled by a compound statement.

In an `if` statement, the indented statements form the suite.

Example:

```python
marks = 85

if marks >= 40:
    print("Pass")
    print("Congratulations")
    print("Result recorded")
```

All three statements belong to the same suite.

## 16.1 One Statement

```python
if True:
    print("One statement.")
```

## 16.2 Multiple Statements

```python
if True:
    print("First statement.")
    print("Second statement.")
    print("Third statement.")
```

## 16.3 Statement Outside the Block

```python
if True:
    print("Inside the if block.")

print("Outside the if block.")
```

## 16.4 Empty If Block and Pass

An empty suite is not valid.

Use `pass` when an intentionally empty placeholder is required.

```python
if True:
    pass
```

`pass` does not perform an operation.

It allows the program to remain syntactically valid until real instructions are added.

---

# 17. How Python Executes an If Statement

Consider:

```python
number = 15

print("Step 1")

if number > 10:
    print("Step 2")
    print("Step 3")

print("Step 4")
```

Output:

```text
Step 1
Step 2
Step 3
Step 4
```

Execution:

1. Assign 15 to `number`.
2. Print `Step 1`.
3. Evaluate `number > 10`.
4. Obtain `True`.
5. Execute the indented body.
6. Print `Step 2`.
7. Print `Step 3`.
8. Leave the block.
9. Print `Step 4`.

When the condition is false, steps 6 and 7 are skipped.

---

# 18. If Statement Without Else

A simple `if` statement does not need an `else` branch.

Example:

```python
temperature = 35

if temperature > 30:
    print("Temperature is above 30.")
```

When the condition is false, Python skips the block and continues after it.

Example:

```python
temperature = 20

if temperature > 30:
    print("Temperature is above 30.")

print("Temperature check completed.")
```

Output:

```text
Temperature check completed.
```

This is an important difference between an `if` statement and an `if-else` statement.

The `if-else` topic will explain how to perform an alternative action.

---

# 19. Multiple Statements Inside If

One condition can control multiple statements.

Example:

```python
price = 1500

if price >= 1000:
    discount = price * 0.10
    final_price = price - discount
    print("Discount:", discount)
    print("Final price:", final_price)
```

Output:

```text
Discount: 150.0
Final price: 1350.0
```

All these statements execute when the condition is true.

## 19.1 Variables Created Inside an If Block

Python does not create a separate block scope for ordinary `if` statements.

A variable assigned inside an executed `if` block can be available afterward.

Example:

```python
if True:
    message = "Hello"

print(message)
```

Output:

```text
Hello
```

But consider:

```python
if False:
    message = "Hello"

print(message)
```

This raises:

```text
NameError
```

The assignment never executed, so the name was not created by that statement.

For predictable code, initialize variables before conditional assignment when they may be needed afterward.

---

# 20. Multiple Independent If Statements

Python allows multiple independent `if` statements.

Each one is evaluated separately.

Example:

```python
number = 12

if number > 0:
    print("Positive.")

if number % 2 == 0:
    print("Even.")

if number > 10:
    print("Greater than 10.")
```

Output:

```text
Positive.
Even.
Greater than 10.
```

All three conditions are true.

## 20.1 Independent Conditions

Consider:

```python
number = 15

if number > 0:
    print("Positive")

if number % 2 != 0:
    print("Odd")

if number > 10:
    print("Greater than 10")
```

All three blocks execute.

## 20.2 Independent If Versus If-Else

Multiple independent `if` statements are not the same as an `if-elif-else` chain.

Independent `if` statements can all execute.

An `if-elif-else` chain selects one matching branch at most.

This difference will become especially important in the next topics.

---

# 21. Using Pass in an If Block

The `pass` statement is a placeholder.

Example:

```python
number = 10

if number > 0:
    pass
```

The program executes without performing an operation inside that block.

## 21.1 Why Use Pass?

It is useful when:

- Designing program structure.
- Creating a temporary placeholder.
- Planning a block before implementing its logic.
- Writing a function or conditional body that will be completed later.

Example:

```python
marks = 80

if marks >= 40:
    pass

print("Program completed.")
```

The `if` body does nothing.

---

# 22. Taking User Input in If Statements

Input makes conditional programs interactive.

The `input()` function receives text from the user.

Example:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
```

Sample input:

```text
Enter your age: 20
```

Output:

```text
Adult
```

## 22.1 Integer Input

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number.")
```

## 22.2 Float Input

```python
temperature = float(input("Enter temperature: "))

if temperature > 30:
    print("Hot temperature.")
```

## 22.3 String Input

```python
name = input("Enter your name: ").strip()

if name:
    print("Name entered:", name)
```

## 22.4 Input Validation

User input may be invalid.

A beginner program can use `try-except` to handle conversion errors.

```python
try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("Example age condition satisfied.")

except ValueError:
    print("Please enter a valid integer.")
```

The `if` statement checks the resulting integer.

The exception handler deals with input that cannot be converted.

---

# 23. If Statements With Integer Values

Integer values are commonly checked using comparison and arithmetic operators.

## Example 1: Positive Number

```python
number = 25

if number > 0:
    print("Positive number.")
```

## Example 2: Even Number

```python
number = 24

if number % 2 == 0:
    print("Even number.")
```

## Example 3: Divisible by Five

```python
number = 50

if number % 5 == 0:
    print("Divisible by 5.")
```

## Example 4: Greater Than 100

```python
number = 150

if number > 100:
    print("Number exceeds 100.")
```

## Example 5: Multiple of Three

```python
number = 27

if number % 3 == 0:
    print("Multiple of 3.")
```

## Example 6: Last Digit Is Five

```python
number = 125

if number % 10 == 5:
    print("Last digit is 5.")
```

The modulo operator is useful for many number-based conditions.

---

# 24. If Statements With Floating-Point Values

Floating-point numbers are used for decimal values.

Example:

```python
temperature = 35.5

if temperature > 30.0:
    print("Temperature is above 30.")
```

## 24.1 Positive Float

```python
number = 5.75

if number > 0:
    print("Positive decimal number.")
```

## 24.2 Price Validation

```python
price = 199.99

if price > 0:
    print("Valid positive price.")
```

## 24.3 Floating-Point Equality

Be careful when comparing floating-point results for exact equality.

Some decimal fractions cannot be represented exactly in binary floating-point.

Example:

```python
result = 0.1 + 0.2

print(result)
```

Typical output:

```text
0.30000000000000004
```

An exact comparison with `0.3` may therefore be false.

For approximate comparison, Python provides `math.isclose()`.

```python
import math

result = 0.1 + 0.2

if math.isclose(result, 0.3):
    print("Values are approximately equal.")
```

---

# 25. If Statements With String Values

Strings can be tested using comparison operators and string methods.

## 25.1 Equality

```python
name = "Amaan"

if name == "Amaan":
    print("Name matched.")
```

## 25.2 String Not Equal

```python
name = "Python"

if name != "Java":
    print("Name is not Java.")
```

## 25.3 Starts With

```python
name = "Python"

if name.startswith("P"):
    print("String starts with P.")
```

## 25.4 Ends With

```python
filename = "program.py"

if filename.endswith(".py"):
    print("Python file detected.")
```

## 25.5 Case-Insensitive Comparison

```python
answer = "YES"

if answer.lower() == "yes":
    print("User answered yes.")
```

## 25.6 Empty String

```python
name = ""

if not name:
    print("Name is empty.")
```

## 25.7 Non-Empty String

```python
name = "Python"

if name:
    print("Name is available.")
```

---

# 26. If Statements With Lists

Lists are checked using truthiness and membership operators.

## 26.1 Check Whether a List Contains Values

```python
numbers = [10, 20, 30]

if numbers:
    print("List is not empty.")
```

## 26.2 Check Whether a List Is Empty

```python
numbers = []

if not numbers:
    print("List is empty.")
```

## 26.3 Membership

```python
fruits = ["Apple", "Banana", "Mango"]

if "Mango" in fruits:
    print("Mango found.")
```

## 26.4 Check First Element

```python
numbers = [10, 20, 30]

if numbers and numbers[0] > 5:
    print("First element is greater than 5.")
```

The first condition ensures the list is non-empty before indexing it.

Because `and` short-circuits, the second condition is not evaluated when the list is empty.

## 26.5 Check List Length

```python
numbers = [10, 20, 30]

if len(numbers) >= 3:
    print("List has at least three elements.")
```

---

# 27. If Statements With Tuples and Dictionaries

## 27.1 Tuple Truthiness

```python
values = (10, 20, 30)

if values:
    print("Tuple contains values.")
```

## 27.2 Tuple Membership

```python
values = (10, 20, 30)

if 20 in values:
    print("20 exists in the tuple.")
```

## 27.3 Dictionary Truthiness

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if student:
    print("Student information exists.")
```

## 27.4 Dictionary Key Membership

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" in student:
    print("Marks information exists.")
```

## 27.5 Dictionary Value Checking

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if 85 in student.values():
    print("The value 85 exists.")
```

Remember that `key in dictionary` checks keys, not values.

---

# 28. If Statements With Functions

A function can be called inside an `if` condition.

Example:

```python
def is_positive(number):
    return number > 0


value = 10

if is_positive(value):
    print("Positive number.")
```

The function returns a Boolean result.

Python uses that result to decide whether the block executes.

## 28.1 Function Returning True

```python
def has_permission():
    return True


if has_permission():
    print("Permission granted.")
```

## 28.2 Function Returning False

```python
def has_permission():
    return False


if has_permission():
    print("Permission granted.")
```

The block is skipped.

## 28.3 Function With Input

```python
def is_even(number):
    return number % 2 == 0


number = 12

if is_even(number):
    print("Even number.")
```

Functions allow reusable conditions.

---

# 29. Nested If – Introduction

A nested `if` means an `if` statement inside another `if` statement.

Example:

```python
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Example access condition satisfied.")
```

The inner condition is checked only when the outer condition is true.

This topic is introduced here because it uses the basic `if` statement.

A complete explanation and practice set will be provided in:

`04-Nested-If/README.md`

---

# 30. If Statements in Real-World Applications

Conditional statements are used throughout software development.

## 30.1 Student Result Systems

```python
marks = 85

if marks >= 40:
    print("Pass.")
```

## 30.2 Shopping Applications

```python
price = 1500

if price >= 1000:
    print("Discount available.")
```

## 30.3 Inventory Systems

```python
quantity = 10

if quantity > 0:
    print("Product is available.")
```

## 30.4 User Authentication

```python
is_authenticated = True

if is_authenticated:
    print("User can access the protected feature.")
```

## 30.5 Banking Applications

```python
balance = 10000
withdrawal = 2000

if balance >= withdrawal:
    print("Sufficient balance.")
```

A real banking application must also implement transactional integrity, authentication and other security controls.

## 30.6 File Processing

```python
filename = "notes.py"

if filename.endswith(".py"):
    print("Python file.")
```

## 30.7 Data Validation

```python
age = 22

if age >= 0:
    print("Age value is non-negative.")
```

---

# 31. Explanation of 12 Topic Examples

This section explains all twelve examples included in `01_if.py`.

## Example 1 – Basic If Statement

Code:

```python
age = 20

if age >= 18:
    print("You are eligible as an adult.")

print("Age:", age)
```

Output:

```text
You are eligible as an adult.
Age: 20
```

Explanation:

1. The variable `age` receives the value 20.
2. Python checks `age >= 18`.
3. The expression evaluates to true.
4. The indented message executes.
5. The final age message also executes because it is outside the block.

Dry run:

| Step | Operation | Value |
|---|---|---|
| 1 | Assign age | 20 |
| 2 | Evaluate `20 >= 18` | True |
| 3 | Execute block | Yes |
| 4 | Print age | 20 |

Learning concept: Basic conditional execution.

## Example 2 – False Condition

Code:

```python
age = 15

print("Age:", age)

if age >= 18:
    print("You are an adult.")

print("Program continues after the if statement.")
```

Output:

```text
Age: 15
Program continues after the if statement.
```

Explanation:

1. The age is 15.
2. The condition `15 >= 18` is false.
3. The indented message is skipped.
4. The statement outside the block executes.

Learning concept: Skipping a false conditional block.

## Example 3 – Check Positive Number

Code:

```python
number = 25

print("Number:", number)

if number > 0:
    print("The number is positive.")
```

Output:

```text
Number: 25
The number is positive.
```

Dry run:

```text
number = 25

number > 0

25 > 0

True
```

Learning concept: Using the greater-than operator.

## Example 4 – Check Even Number

Code:

```python
number = 24

print("Number:", number)

if number % 2 == 0:
    print("The number is even.")
```

Output:

```text
Number: 24
The number is even.
```

Calculation:

```text
24 % 2 = 0

0 == 0

True
```

Learning concept: Using modulo for even-number checking.

## Example 5 – Voting Eligibility

Code:

```python
age = 20

print("Age:", age)

if age >= 18:
    print("You meet the example age requirement for voting.")
```

Output:

```text
Age: 20
You meet the example age requirement for voting.
```

Learning concept: Checking an age threshold.

This is an illustrative programming rule, not a complete statement of voting law.

## Example 6 – Greater Number

Code:

```python
a = 25
b = 40

largest = a

if b > largest:
    largest = b

print("First number:", a)
print("Second number:", b)
print("Greater number:", largest)
```

Output:

```text
First number: 25
Second number: 40
Greater number: 40
```

Dry run:

| Step | Variable | Value |
|---|---|---:|
| 1 | `a` | 25 |
| 2 | `b` | 40 |
| 3 | `largest = a` | 25 |
| 4 | `b > largest` | True |
| 5 | Update largest | 40 |

Learning concept: Conditional variable update.

## Example 7 – Apply Discount

Code:

```python
price = 2000

final_price = price

if price >= 1000:
    final_price = price * 0.90
    print("10 percent discount applied.")

print("Original price:", price)
print("Final price:", final_price)
```

Output:

```text
10 percent discount applied.
Original price: 2000
Final price: 1800.0
```

Calculation:

```text
Discounted price = 2000 * 0.90

Discounted price = 1800
```

Learning concept: Conditional calculation.

## Example 8 – Check String Starts With a Character

Code:

```python
name = "Python"

print("Name:", name)

if name.startswith("P"):
    print("The name starts with P.")
```

Output:

```text
Name: Python
The name starts with P.
```

Learning concept: Using a string method in a condition.

## Example 9 – Check List Membership

Code:

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

search_item = "Mango"

if search_item in fruits:
    print("Fruit found in the list.")
```

Output:

```text
Fruit found in the list.
```

Learning concept: Membership operator.

## Example 10 – Multiple Independent If Conditions

Code:

```python
number = 12

if number > 0:
    print("The number is positive.")

if number % 2 == 0:
    print("The number is even.")

if number > 10:
    print("The number is greater than 10.")
```

Output:

```text
The number is positive.
The number is even.
The number is greater than 10.
```

All three conditions are evaluated independently.

Learning concept: Independent conditional statements.

## Example 11 – If With AND Operator

Code:

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Both conditions are satisfied.")
```

Output:

```text
Both conditions are satisfied.
```

Both conditions are true.

Learning concept: Logical AND.

## Example 12 – If With OR Operator

Code:

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount condition is satisfied.")
```

Output:

```text
Discount condition is satisfied.
```

At least one operand is true.

Learning concept: Logical OR.

---

# 32. Twelve Solved Programming Problems

The Python file contains twelve interactive solved problems.

Each problem below explains the algorithm, important condition, example input, output and learning objective.

## Problem 1 – Check Positive Number

Objective:

Write a program that accepts a number and displays a message when it is positive.

Code:

```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
```

Sample input:

```text
Enter a number: 25
```

Output:

```text
The number is positive.
```

Algorithm:

1. Start.
2. Read a number.
3. Check whether the number is greater than zero.
4. If the condition is true, print the positive message.
5. End.

Important condition:

```python
number > 0
```

Test cases:

| Input | Condition | Expected behavior |
|---:|---|---|
| 10 | True | Display positive message |
| 5.5 | True | Display positive message |
| 0 | False | Skip message |
| -10 | False | Skip message |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 2 – Check Even Number

Objective:

Check whether an integer is even.

Code:

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even.")
```

Sample input:

```text
Enter an integer: 24
```

Output:

```text
The number is even.
```

Algorithm:

1. Read an integer.
2. Calculate the remainder after division by 2.
3. Compare the remainder with zero.
4. Display the even message when the condition is true.

Condition:

```python
number % 2 == 0
```

Test cases:

| Input | Expected behavior |
|---:|---|
| 2 | Even message |
| 12 | Even message |
| 7 | No message |
| 0 | Even message |
| -4 | Even message |

Note: Zero and negative even integers are also mathematically even.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 3 – Voting Eligibility

Objective:

Check whether the user's age satisfies an example minimum-age threshold of 18.

Code:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You meet the example minimum age requirement.")
```

Sample input:

```text
Enter your age: 20
```

Output:

```text
You meet the example minimum age requirement.
```

Algorithm:

1. Read age.
2. Check whether age is at least 18.
3. Display the message when true.
4. End.

Test cases:

| Age | Condition |
|---:|---|
| 15 | False |
| 17 | False |
| 18 | True |
| 20 | True |
| 25 | True |

This example does not model every legal voting requirement.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 4 – Divisibility by 5 and 11

Objective:

Check whether a number is divisible by both 5 and 11.

Code:

```python
number = int(input("Enter an integer: "))

if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11.")
```

Sample input:

```text
Enter an integer: 55
```

Output:

```text
The number is divisible by both 5 and 11.
```

Explanation:

The first condition is:

```python
number % 5 == 0
```

The second condition is:

```python
number % 11 == 0
```

The `and` operator requires both conditions to be true.

Test cases:

| Input | Divisible by 5 | Divisible by 11 | Message |
|---:|---|---|---|
| 55 | True | True | Display |
| 110 | True | True | Display |
| 25 | True | False | Skip |
| 33 | False | True | Skip |
| 7 | False | False | Skip |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 5 – Largest of Two Numbers

Objective:

Find the greater of two numbers using an `if` statement.

Code:

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

largest = a

if b > largest:
    largest = b

print("Largest number:", largest)
```

Sample input:

```text
Enter first number: 25
Enter second number: 40
```

Output:

```text
Largest number: 40.0
```

Explanation:

Initially, the program assumes the first number is the largest.

Then it compares the second number with the current largest.

If the second number is greater, the value is updated.

Dry run:

| Step | Operation | Result |
|---|---|---:|
| 1 | `a = 25` | 25 |
| 2 | `b = 40` | 40 |
| 3 | `largest = a` | 25 |
| 4 | `b > largest` | True |
| 5 | `largest = b` | 40 |

Test cases:

- First number greater.
- Second number greater.
- Both numbers equal.
- One negative and one positive.
- Both negative.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 6 – Largest of Three Numbers

Objective:

Find the largest among three numbers using independent `if` statements.

Code:

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest number:", largest)
```

Sample input:

```text
Enter first number: 10
Enter second number: 50
Enter third number: 30
```

Output:

```text
Largest number: 50.0
```

Explanation:

1. Assume the first value is largest.
2. Compare the second value.
3. Update the result if needed.
4. Compare the third value.
5. Update the result if needed.
6. Display the largest value.

Dry run:

| Step | Operation | Largest |
|---|---|---:|
| 1 | Initial value | 10 |
| 2 | Compare 50 with 10 | 50 |
| 3 | Compare 30 with 50 | 50 |
| 4 | Final result | 50 |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 7 – Leap Year Check

Objective:

Check whether a year is a leap year.

Gregorian calendar rule:

A year is a leap year when:

- It is divisible by 400; or
- It is divisible by 4 and not divisible by 100.

Code:

```python
year = int(input("Enter a year: "))

is_leap_year = (
    year % 400 == 0
    or
    (year % 4 == 0 and year % 100 != 0)
)

if is_leap_year:
    print("The year is a leap year.")
```

Sample input:

```text
Enter a year: 2024
```

Output:

```text
The year is a leap year.
```

Test cases:

| Year | Expected result |
|---:|---|
| 2024 | Leap year |
| 2023 | Not a leap year |
| 2000 | Leap year |
| 1900 | Not a leap year |
| 2400 | Leap year |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 8 – Grade Calculator

Objective:

Assign a grade based on marks.

Example grading scale:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89 | B |
| 60–74 | C |
| 40–59 | D |
| 0–39 | F |

Code:

```python
marks = float(input("Enter marks between 0 and 100: "))

grade = None

if marks < 0 or marks > 100:
    print("Invalid marks.")

if 0 <= marks <= 100:

    if marks >= 90:
        grade = "A"

    if 75 <= marks < 90:
        grade = "B"

    if 60 <= marks < 75:
        grade = "C"

    if 40 <= marks < 60:
        grade = "D"

    if marks < 40:
        grade = "F"

if grade is not None:
    print("Grade:", grade)
```

Sample input:

```text
Enter marks between 0 and 100: 85
```

Output:

```text
Grade: B
```

Explanation:

The program validates the range first.

Then it checks the possible grade ranges.

Each range is mutually exclusive, so at most one grade is assigned.

Test cases:

| Marks | Grade |
|---:|---|
| 95 | A |
| 80 | B |
| 65 | C |
| 50 | D |
| 30 | F |
| -5 | Invalid |
| 110 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 9 – Positive, Negative or Zero

Objective:

Classify a number into one of three categories.

Code:

```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")

if number < 0:
    print("Negative")

if number == 0:
    print("Zero")
```

Sample input:

```text
Enter a number: -15
```

Output:

```text
Negative
```

Explanation:

The program checks three independent conditions.

Exactly one of these conditions will be true for an ordinary real number.

Test cases:

| Input | Result |
|---:|---|
| 10 | Positive |
| -10 | Negative |
| 0 | Zero |
| 2.5 | Positive |
| -2.5 | Negative |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 10 – Discount Calculator

Objective:

Apply a 10% discount when the price is at least 1000.

Code:

```python
price = float(input("Enter product price: "))

final_price = price
discount_amount = 0

if price >= 1000:
    discount_amount = price * 0.10
    final_price = price - discount_amount

print("Original price:", price)
print("Discount amount:", discount_amount)
print("Final price:", final_price)
```

Sample input:

```text
Enter product price: 2000
```

Output:

```text
Original price: 2000.0
Discount amount: 200.0
Final price: 1800.0
```

Explanation:

1. The original price is stored.
2. The final price initially equals the original.
3. The condition checks whether the price is at least 1000.
4. The discount is calculated.
5. The final price is updated.
6. The values are displayed.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

This is an illustrative discount policy.

## Problem 11 – Basic Login Check

Objective:

Demonstrate how an `if` statement can check two example credentials.

Code:

```python
correct_username = "student"
correct_password = "python123"

username = input("Enter username: ").strip()
password = input("Enter password: ")

is_valid = (
    username == correct_username
    and password == correct_password
)

if is_valid:
    print("Login successful. Welcome!")

if not is_valid:
    print("Incorrect username or password.")
```

Sample input:

```text
Enter username: student
Enter password: python123
```

Output:

```text
Login successful. Welcome!
```

Explanation:

The username comparison and password comparison must both be true.

The program uses `and` to combine them.

Security note:

This example is only for learning conditional statements. Real applications should never store plain-text passwords as shown here. They require secure password hashing, proper authentication and other protections.

Complexity:

- Time: O(n + m) for comparing strings of lengths n and m in the general case.
- Auxiliary space: O(n + m) for the input strings and related values.

## Problem 12 – Triangle Validity Checker

Objective:

Check whether three positive lengths can form a triangle.

Triangle inequality:

The sum of any two sides must be greater than the third side.

Conditions:

```python
a + b > c
a + c > b
b + c > a
```

All sides must also be positive.

Code:

```python
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

is_valid = (
    a > 0
    and b > 0
    and c > 0
    and a + b > c
    and a + c > b
    and b + c > a
)

if is_valid:
    print("Valid triangle.")

if not is_valid:
    print("Invalid triangle.")
```

Sample input:

```text
Enter first side: 3
Enter second side: 4
Enter third side: 5
```

Output:

```text
Valid triangle.
```

Explanation:

1. Check that each side is positive.
2. Check that the first two sides sum to more than the third.
3. Check that the first and third sides sum to more than the second.
4. Check that the second and third sides sum to more than the first.
5. All requirements must be true.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

---

# 33. Ten Unsolved Practice Questions

Attempt these problems independently before checking external solutions.

## Question 1 – Divisible by 3

Accept an integer.

Display a message only when it is divisible by 3.

Hint:

```python
number % 3 == 0
```

## Question 2 – Multiple of 4 and 6

Accept an integer.

Display a message when it is divisible by both 4 and 6.

Hint:

Use the `and` operator.

## Question 3 – Scholarship Eligibility

Accept a student's marks.

Display a scholarship eligibility message when marks are at least 85.

Hint:

```python
marks >= 85
```

## Question 4 – Last Digit Is 5

Accept an integer.

Display a message when its last digit is 5.

Hint:

```python
number % 10 == 5
```

Consider how modulo behaves for negative numbers when testing the program.

## Question 5 – Smallest of Three Numbers

Accept three numbers.

Use independent `if` statements to determine the smallest value.

Try values with:

- First value smallest.
- Second value smallest.
- Third value smallest.
- Equal values.

## Question 6 – Discount Calculator

Accept a product price.

Apply a 15% discount only when the price is at least 2500.

Otherwise, keep the original price.

## Question 7 – Century Year

Accept a year.

Display a message when it is divisible by 100.

Hint:

```python
year % 100 == 0
```

Remember that every century year is not necessarily a leap year.

## Question 8 – Uppercase Character

Accept a character.

Display a message when it is an uppercase English alphabet character.

Hint:

```python
"A" <= character <= "Z"
```

Check that the user entered exactly one character.

## Question 9 – Equilateral Triangle

Accept three side lengths.

Display a message when all three sides are equal and positive.

Hint:

```python
a == b and b == c
```

Also check that the lengths are positive.

## Question 10 – Multiple Conditions

Accept an integer.

Display separate messages when:

- The number is positive.
- The number is even.
- The number is greater than 100.

Use three independent `if` statements.

---

# 34. Dry Run and Trace Tables

A dry run means executing a program manually using sample values and recording what happens at each step.

Dry runs help understand conditions and predict outputs.

## 34.1 Dry Run – Positive Number

Code:

```python
number = 10

if number > 0:
    print("Positive")
```

Trace:

| Step | Operation | Value |
|---|---|---|
| 1 | Assign number | 10 |
| 2 | Evaluate `number > 0` | True |
| 3 | Execute body | Yes |
| 4 | Display | Positive |

## 34.2 Dry Run – False Condition

Code:

```python
number = -5

if number > 0:
    print("Positive")
```

Trace:

| Step | Operation | Value |
|---|---|---|
| 1 | Assign number | -5 |
| 2 | Evaluate `number > 0` | False |
| 3 | Execute body | No |
| 4 | Output from block | None |

## 34.3 Dry Run – Even Number

Code:

```python
number = 18

if number % 2 == 0:
    print("Even")
```

Trace:

| Step | Operation | Result |
|---|---|---|
| 1 | `18 % 2` | 0 |
| 2 | `0 == 0` | True |
| 3 | Enter body | Yes |
| 4 | Print | Even |

## 34.4 Dry Run – AND Condition

Code:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Eligible.")
```

Trace:

| Expression | Result |
|---|---|
| `age >= 18` | True |
| `has_id` | True |
| Combined AND condition | True |
| Execute block | Yes |

## 34.5 Dry Run – OR Condition

Code:

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount available.")
```

Trace:

| Expression | Result |
|---|---|
| `is_member` | False |
| `has_coupon` | True |
| Combined OR condition | True |
| Execute block | Yes |

---

# 35. Flowchart and Algorithm

## 35.1 Basic If Statement Flowchart

```text
             START
               |
               v
        Initialize Values
               |
               v
       Evaluate Condition
               |
               v
        Is it Truthy?
           /       \
         Yes        No
          |          |
          v          |
     Execute If      |
        Block        |
          |          |
          +----+-----+
               |
               v
              END
```

## 35.2 Algorithm – Positive Number

1. Start.
2. Read a number.
3. Check whether the number is greater than zero.
4. If true, display the positive message.
5. Continue to the end.
6. Stop.

## 35.3 Algorithm – Even Number

1. Start.
2. Read an integer.
3. Calculate the remainder when divided by two.
4. Check whether the remainder is zero.
5. If true, display the even message.
6. Stop.

## 35.4 Algorithm – Largest of Three

1. Start.
2. Read three numbers.
3. Assume the first number is largest.
4. Compare the second number with the current largest.
5. Update the largest value if needed.
6. Compare the third number with the current largest.
7. Update the largest value if needed.
8. Display the largest value.
9. Stop.

---

# 36. Common Programming Mistakes

## Mistake 1 – Missing Colon

Incorrect:

```python
if number > 0
    print("Positive")
```

Correct:

```python
if number > 0:
    print("Positive")
```

Reason:

Python requires a colon at the end of the `if` header.

## Mistake 2 – Missing Indentation

Incorrect:

```python
if number > 0:
print("Positive")
```

Correct:

```python
if number > 0:
    print("Positive")
```

Reason:

The statement must be indented as part of the `if` body.

## Mistake 3 – Using Assignment Instead of Equality

Incorrect:

```python
if number = 10:
    print("Ten")
```

Correct:

```python
if number == 10:
    print("Ten")
```

Reason:

`=` assigns a value.

`==` compares two values.

## Mistake 4 – Using Lowercase Boolean Literals

Incorrect:

```python
is_active = true
```

Correct:

```python
is_active = True
```

Reason:

Python's Boolean literals use capital letters.

## Mistake 5 – Comparing With the Wrong Operator

Incorrect for checking whether marks are at least 40:

```python
if marks > 40:
    print("Pass")
```

This excludes exactly 40.

Correct when 40 is included:

```python
if marks >= 40:
    print("Pass")
```

## Mistake 6 – Forgetting Input Conversion

Incorrect:

```python
age = input("Enter age: ")

if age >= 18:
    print("Adult")
```

The input is a string, so comparing it with an integer raises a `TypeError`.

Correct:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
```

## Mistake 7 – Incorrect Logical Operator

Incorrect when both conditions are required:

```python
if age >= 18 or has_id:
    print("Eligible")
```

This allows either condition to make the combined condition true.

Correct when both are required:

```python
if age >= 18 and has_id:
    print("Eligible")
```

## Mistake 8 – Uninitialized Variable

Problem:

```python
if marks >= 40:
    result = "Pass"

print(result)
```

When marks are below 40, `result` is never assigned.

The final print can raise `NameError`.

Safer structure:

```python
result = "Not Passed"

if marks >= 40:
    result = "Pass"

print(result)
```

## Mistake 9 – Confusing Independent If Statements With If-Elif

Separate `if` statements are all checked.

Do not assume that one true condition prevents the remaining independent conditions from executing.

## Mistake 10 – Empty If Block

Incorrect:

```python
if number > 0:
```

Use a valid statement or `pass`:

```python
if number > 0:
    pass
```

---

# 37. Debugging Techniques

Debugging means identifying and correcting problems in a program.

## 37.1 Print the Condition

```python
number = 10

condition = number > 0

print("Condition:", condition)

if condition:
    print("Positive")
```

## 37.2 Print Variable Values

```python
marks = 75

print("Marks:", marks)

if marks >= 40:
    print("Pass")
```

## 37.3 Inspect the Type

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

Convert the input when an integer is needed:

```python
age = int(age)
```

## 37.4 Use Intermediate Variables

Instead of one long condition:

```python
if age >= 18 and has_id and not is_banned:
    print("Allowed")
```

You can write:

```python
age_ok = age >= 18
id_ok = has_id
account_ok = not is_banned

if age_ok and id_ok and account_ok:
    print("Allowed")
```

This makes debugging easier.

## 37.5 Check Boundary Values

For an age threshold of 18, test:

- 17
- 18
- 19

For a marks threshold of 40, test:

- 39
- 40
- 41

Boundary testing detects mistakes involving `>` and `>=`.

---

# 38. Best Practices

1. Use four spaces for indentation.
2. Write meaningful variable names.
3. Keep conditions easy to understand.
4. Use `==` for equality comparisons.
5. Convert user input to the appropriate type.
6. Test both true and false conditions.
7. Test boundary values.
8. Use `and` when all required conditions must hold.
9. Use `or` when any one of the conditions is sufficient.
10. Use `is None` when checking for `None`.
11. Initialize values that must be used after the conditional block.
12. Avoid unnecessary complicated expressions.
13. Break long conditions into smaller variables.
14. Use parentheses when they improve readability.
15. Avoid mixing tabs and spaces.
16. Use `pass` only as a meaningful placeholder.
17. Validate user input before processing.
18. Do not assume that input is always correct.
19. Avoid hardcoded credentials in real applications.
20. Keep business rules separate from presentation where useful.

---

# 39. Practical Applications

## 39.1 Student Result System

```python
marks = 75

if marks >= 40:
    print("Pass")
```

## 39.2 Shopping Discount

```python
price = 1500

if price >= 1000:
    print("Discount available.")
```

## 39.3 Inventory Management

```python
quantity = 10

if quantity > 0:
    print("Product available.")
```

## 39.4 File Extension Check

```python
filename = "program.py"

if filename.endswith(".py"):
    print("Python file.")
```

## 39.5 Number Validation

```python
number = 25

if number > 0:
    print("Valid positive value.")
```

## 39.6 Access Check

```python
is_authenticated = True

if is_authenticated:
    print("Access allowed.")
```

---

# 40. If Statements and Data Structures

Conditional statements are widely used with data structures.

## 40.1 Arrays and Lists

```python
numbers = [10, 20, 30, 40]

if numbers:
    print("The list contains elements.")
```

## 40.2 Searching in a List

```python
numbers = [10, 20, 30, 40]

target = 30

if target in numbers:
    print("Target found.")
```

## 40.3 Stack

```python
stack = [10, 20, 30]

if stack:
    print("Stack is not empty.")
```

Before popping from a stack, checking that it is non-empty prevents an invalid operation.

## 40.4 Queue

```python
queue = [10, 20, 30]

if queue:
    print("Queue contains elements.")
```

## 40.5 Dictionary

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" in student:
    print("Marks key exists.")
```

## 40.6 Set

```python
numbers = {10, 20, 30}

if 20 in numbers:
    print("Value found in set.")
```

---

# 41. If Statements and Algorithms

Conditions are used in almost every algorithm.

## 41.1 Linear Search

```python
numbers = [10, 20, 30, 40]

target = 30

for number in numbers:
    if number == target:
        print("Target found.")
```

The `if` statement checks whether the current element matches the target.

## 41.2 Binary Search

A complete binary search requires repeated decisions.

Basic condition:

```python
if arr[mid] == target:
    print("Target found.")
```

Other decisions determine whether the search continues in the left half or right half.

## 41.3 Finding Maximum

```python
numbers = [10, 50, 20, 40]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
```

Output:

```text
50
```

The condition updates the maximum value.

## 41.4 Finding Minimum

```python
numbers = [10, 50, 20, 40]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print(minimum)
```

Output:

```text
10
```

## 41.5 Counting Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)
```

Output:

```text
3
```

## 41.6 Filtering Positive Numbers

```python
numbers = [-5, 10, -2, 20, 0, 7]

positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print(positive_numbers)
```

Output:

```text
[10, 20, 7]
```

---

# 42. Time and Space Complexity

The complexity of an `if` statement depends on the condition and the work performed in its body.

## 42.1 Simple If Condition

```python
number = 10

if number > 0:
    print("Positive")
```

For a basic integer comparison:

- Time complexity: O(1)
- Auxiliary space: O(1)

## 42.2 If With a Constant-Time Logical Condition

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Eligible")
```

For these simple checks:

- Time complexity: O(1)
- Auxiliary space: O(1)

## 42.3 If With Membership in a List

```python
numbers = [10, 20, 30, 40]

if 30 in numbers:
    print("Found")
```

List membership requires a search.

Worst-case time complexity:

- O(n)

Auxiliary space for the membership check:

- O(1), excluding the existing list.

## 42.4 If With Membership in a Set

```python
numbers = {10, 20, 30, 40}

if 30 in numbers:
    print("Found")
```

Set membership is expected O(1) on average, though worst-case behavior can be different.

## 42.5 Important Rule

Do not assume every condition takes O(1).

The condition may call a function, scan a list, perform a calculation or execute other operations.

The complexity depends on those operations.

---

# 43. Mini Project – Student Eligibility Checker

## Project Introduction

Create a basic student eligibility checker.

The program accepts:

- Student age.
- Examination marks.
- Attendance percentage.

It checks the conditions and displays messages.

The example rules are:

- Age must be at least 18.
- Marks must be at least 40.
- Attendance must be at least 75%.

These are illustrative programming rules, not universal academic or legal requirements.

## Project Code

```python
print("=" * 50)
print("STUDENT ELIGIBILITY CHECKER")
print("=" * 50)

age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))

if age >= 18:
    print("Age requirement satisfied.")

if marks >= 40:
    print("Marks requirement satisfied.")

if attendance >= 75:
    print("Attendance requirement satisfied.")

if age >= 18 and marks >= 40 and attendance >= 75:
    print("All example eligibility requirements are satisfied.")

print("=" * 50)
```

## Sample Input

```text
Enter age: 20
Enter marks: 85
Enter attendance percentage: 90
```

## Output

```text
==================================================
STUDENT ELIGIBILITY CHECKER
==================================================
Age requirement satisfied.
Marks requirement satisfied.
Attendance requirement satisfied.
All example eligibility requirements are satisfied.
==================================================
```

## Project Explanation

1. Read the student's age.
2. Read examination marks.
3. Read attendance percentage.
4. Check each condition independently.
5. Display the corresponding messages.
6. Check whether all three conditions are satisfied.
7. Display the final eligibility message.

## Project Challenges

1. Add input validation.
2. Display which requirement was not satisfied.
3. Calculate the student's average.
4. Add a grade.
5. Store multiple student records.
6. Create a reusable function for checking eligibility.
7. Add an option to repeat the calculation.
8. Save results in a text file.

---

# 44. Practice Test

Try solving these questions without looking at the answers.

## Question 1

What is the output?

```python
number = 10

if number > 0:
    print("Positive")
```

## Question 2

What is the output?

```python
number = -5

if number > 0:
    print("Positive")

print("Completed")
```

## Question 3

What is the output?

```python
number = 12

if number % 2 == 0:
    print("Even")
```

## Question 4

What is the output?

```python
age = 18

if age >= 18:
    print("Adult")
```

## Question 5

What is the output?

```python
a = 10
b = 20

if a > b:
    print("A")

if b > a:
    print("B")
```

## Question 6

What is the output?

```python
value = 0

if value:
    print("Truthy")

print("Finished")
```

## Question 7

What is the output?

```python
numbers = []

if numbers:
    print("Not empty")

print("Done")
```

## Question 8

What is the output?

```python
name = "Python"

if "P" in name:
    print("Found")
```

## Question 9

What is the output?

```python
a = True
b = False

if a and b:
    print("Both true")

if a or b:
    print("At least one true")
```

## Question 10

What is the output?

```python
number = 100

if number >= 100:
    print("At least 100")

print("End")
```

## Practice Test Answers

| Question | Answer |
|---|---|
| 1 | `Positive` |
| 2 | `Completed` |
| 3 | `Even` |
| 4 | `Adult` |
| 5 | `B` |
| 6 | `Finished` |
| 7 | `Done` |
| 8 | `Found` |
| 9 | `At least one true` |
| 10 | `At least 100`, followed by `End` |

---

# 45. Viva and Interview Questions

## Basic Questions

**Q1. What is an if statement in Python?**

An `if` statement executes an indented block when its condition evaluates to a truthy value.

**Q2. Why are conditional statements required?**

They allow programs to make decisions based on conditions.

**Q3. What is the syntax of an if statement?**

```python
if condition:
    statement
```

**Q4. Which keyword is used to create an if statement?**

`if`.

**Q5. Is a colon compulsory after an if condition?**

Yes.

**Q6. What is indentation?**

Indentation means spaces at the beginning of a line that define a code block.

**Q7. How many spaces are commonly recommended for one indentation level?**

Four spaces.

**Q8. Does Python require an else block with every if statement?**

No.

**Q9. What happens when an if condition is true?**

The indented body executes.

**Q10. What happens when an if condition is false?**

The indented body is skipped.

## Boolean and Condition Questions

**Q11. What is a Boolean value?**

A value representing either `True` or `False`.

**Q12. What are the two Boolean values in Python?**

`True` and `False`.

**Q13. Which operator checks equality?**

`==`.

**Q14. Which operator checks inequality?**

`!=`.

**Q15. What does `>=` mean?**

Greater than or equal to.

**Q16. What does `<=` mean?**

Less than or equal to.

**Q17. What is a condition?**

An expression tested by Python to obtain a truth value.

**Q18. Can a string be used as an if condition?**

Yes. A non-empty string is truthy.

**Q19. Is an empty list truthy or falsy?**

Falsy.

**Q20. Is zero truthy or falsy?**

Falsy.

## Logical Operator Questions

**Q21. Name the logical operators in Python.**

`and`, `or` and `not`.

**Q22. What does AND do?**

It produces a truthy result only when both operands are truthy.

**Q23. What does OR do?**

It produces a truthy result when at least one operand is truthy.

**Q24. What does NOT do?**

It reverses the truth value of its operand.

**Q25. Can multiple conditions be combined in an if statement?**

Yes.

**Q26. What is short-circuit evaluation?**

It is the behavior in which the right operand is not evaluated when the left operand already determines the result of `and` or `or`.

**Q27. Can membership operators be used in if conditions?**

Yes.

**Q28. Can identity operators be used in if conditions?**

Yes.

**Q29. What is the difference between `==` and `is`?**

`==` checks value equality, while `is` checks object identity.

**Q30. How should None be checked?**

Use `is None` or `is not None`.

## Intermediate Questions

**Q31. Can an if block contain multiple statements?**

Yes.

**Q32. What is an if block?**

It is the indented suite controlled by the condition.

**Q33. What is the purpose of pass?**

It provides a placeholder statement that performs no operation.

**Q34. What happens when indentation is missing?**

Python may raise an `IndentationError`.

**Q35. Can if statements be nested?**

Yes.

**Q36. Can one program contain multiple independent if statements?**

Yes.

**Q37. Do independent if statements behave exactly like an if-elif chain?**

No. Each independent statement is evaluated separately.

**Q38. Can a function call be used inside an if condition?**

Yes.

**Q39. Can an if statement check whether a list is empty?**

Yes, by testing its truth value.

**Q40. Can an if condition contain arithmetic operations?**

Yes.

## Interview-Level Questions

**Q41. What is the output of this code?**

```python
if 10 > 5:
    print("Yes")
```

Answer: `Yes`.

**Q42. What is the output of this code?**

```python
if 10 < 5:
    print("Yes")
```

Answer: No output.

**Q43. What is the output?**

```python
if []:
    print("A")

if [1]:
    print("B")
```

Answer: `B`.

**Q44. What is the output?**

```python
if 0:
    print("A")

if 1:
    print("B")
```

Answer: `B`.

**Q45. What is the output?**

```python
if not None:
    print("Yes")
```

Answer: `Yes`, because `None` is falsy and `not None` is true.

**Q46. What is the output?**

```python
if "Python":
    print("Available")
```

Answer: `Available`.

**Q47. Can an if statement return a value directly?**

An `if` statement is a statement, not a value-producing conditional expression. It can assign a value inside its body, but it does not itself return an expression value.

**Q48. What is the difference between a statement and an expression?**

An expression produces a value. A statement performs an instruction or controls execution.

**Q49. Why should conditions be kept readable?**

Readable conditions reduce logical mistakes and make debugging easier.

**Q50. Where are if statements used in DSA?**

They are used in searching, sorting, traversal, validation, counting, classification and many other algorithmic operations.

---

# 46. Important Glossary

| Term | Meaning |
|---|---|
| Conditional Statement | A statement that controls execution based on a condition |
| If Statement | A statement that executes a block when a condition is truthy |
| Condition | An expression tested by Python |
| Boolean | Data type containing True and False |
| Truthy | A value that evaluates to true in a Boolean context |
| Falsy | A value that evaluates to false in a Boolean context |
| Indentation | Spaces or tabs defining a code block |
| Code Block | A group of related statements |
| Suite | The body of a compound statement |
| Comparison Operator | An operator that compares values |
| Logical Operator | An operator that combines or reverses truth values |
| Membership Operator | An operator that checks membership |
| Identity Operator | An operator that checks object identity |
| Modulo | Operator that calculates a remainder |
| Short-Circuit | Skipping an unnecessary logical operand |
| Nested If | An if statement inside another if statement |
| SyntaxError | Error caused by invalid Python syntax |
| IndentationError | Error caused by incorrect indentation |
| TypeError | Error involving incompatible types or operations |
| NameError | Error caused by using an undefined name |
| Debugging | Identifying and correcting programming errors |

---

# 47. Quick Revision Notes

Remember these points:

1. `if` is a Python conditional keyword.
2. It is used for decision-making.
3. The condition is written after `if`.
4. A colon is compulsory.
5. The block must be indented.
6. Four spaces per indentation level are recommended.
7. The body executes when the condition is truthy.
8. The body is skipped when the condition is falsy.
9. A basic `if` statement does not require `else`.
10. Multiple statements can belong to one block.
11. Multiple independent `if` statements can all execute.
12. `pass` can be used as a placeholder.
13. Comparison operators return Boolean results.
14. Logical operators combine conditions.
15. Membership operators can check collections.
16. Identity operators can check for `None`.
17. Empty strings and collections are falsy.
18. Non-empty strings and collections are generally truthy.
19. Input should be converted to the required type.
20. Boundary values should be tested.
21. A function can be called in a condition.
22. If statements are used in algorithms.
23. Conditions should remain readable.
24. Use `==` for equality.
25. Use `is None` for None checks.

### Important Syntax

```python
if condition:
    statement
```

### Important Examples

```python
# Positive number
if number > 0:
    print("Positive")

# Even number
if number % 2 == 0:
    print("Even")

# Age threshold
if age >= 18:
    print("Condition satisfied")

# Membership
if "Python" in languages:
    print("Found")

# Logical AND
if age >= 18 and has_id:
    print("Eligible")

# Logical OR
if is_member or has_coupon:
    print("Offer available")

# None check
if value is None:
    print("No value")
```

---

# 48. Learning Checklist

Complete this checklist after studying the topic.

- [ ] Understand conditional statements.
- [ ] Understand decision-making in programming.
- [ ] Define the Python if statement.
- [ ] Learn the syntax of if.
- [ ] Identify all components of an if statement.
- [ ] Understand how conditions are evaluated.
- [ ] Understand Boolean values.
- [ ] Understand truthy and falsy values.
- [ ] Learn comparison operators.
- [ ] Use arithmetic operators in conditions.
- [ ] Use logical AND.
- [ ] Use logical OR.
- [ ] Use logical NOT.
- [ ] Use membership operators.
- [ ] Understand identity operators.
- [ ] Understand the purpose of indentation.
- [ ] Write correct if blocks.
- [ ] Use pass when required.
- [ ] Read and convert user input.
- [ ] Check positive numbers.
- [ ] Check even numbers.
- [ ] Check age thresholds.
- [ ] Check string conditions.
- [ ] Check list membership.
- [ ] Use multiple independent if statements.
- [ ] Understand nested if at a basic level.
- [ ] Find the largest of two values.
- [ ] Find the largest of three values.
- [ ] Check leap years.
- [ ] Calculate grades.
- [ ] Validate triangle sides.
- [ ] Debug syntax errors.
- [ ] Debug indentation errors.
- [ ] Test boundary values.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved problems.
- [ ] Complete the mini project.
- [ ] Revise all 50 viva questions.

---

# 49. How to Run the Python Program

The corresponding program file is:

```text
01_if.py
```

## Step 1 – Open the Folder

Navigate to:

```text
06-Conditional-Statements/
    01-If-Statement/
```

## Step 2 – Open the Terminal

Open PowerShell or the integrated VS Code terminal inside this folder.

## Step 3 – Run the Program

```powershell
python 01_if.py
```

If your system uses the Python launcher, you can also try:

```powershell
py 01_if.py
```

## Step 4 – View the Main Menu

The program displays:

```text
=================================================================
                       PYTHON - IF STATEMENT
=================================================================

1. View 12 Topic Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit

Enter your choice:
```

## Step 5 – Select an Option

| Option | Action |
|---|---|
| 1 | View 12 topic examples |
| 2 | Practice 12 solved problems |
| 3 | View 10 unsolved questions |
| 4 | View learning checklist |
| 0 | Exit the program |

---

# 50. Repository Folder Structure

The topic folder should contain:

```text
01-If-Statement/
│
├── 01_if.py
│
└── README.md
```

The parent section is organized as follows:

```text
06-Conditional-Statements/
│
├── README.md
│
├── 01-If-Statement/
│   ├── README.md
│   └── 01_if.py
│
├── 02-If-Else/
│   ├── README.md
│   └── 01_if_else.py
│
├── 03-If-Elif-Else/
│   ├── README.md
│   └── 01_if_elif_else.py
│
├── 04-Nested-If/
│   ├── README.md
│   └── 01_nested_if.py
│
├── 05-Conditional-Expressions/
│   ├── README.md
│   └── 01_ternary_operator.py
│
├── 06-Practice-Problems/
│   ├── README.md
│   ├── 01-positive-negative/
│   ├── 02-even-odd/
│   ├── 03-largest-number/
│   ├── 04-leap-year/
│   ├── 05-grade-calculator/
│   └── 06-voting-eligibility/
│
└── 07-Match-Case/
    ├── README.md
    └── 01_match_case.py
```

---

# 51. Previous and Next Topics

## Previous Section

**08 – Expressions**

Folder:

```text
08-Expressions/
```

Topics completed:

1. Expressions
2. Operator Precedence
3. Operator Associativity
4. Parentheses and Grouping
5. Conditional Expressions

## Current Section

**06 – Conditional Statements**

Current topic:

**01 – If Statement**

Folder:

```text
01-If-Statement/
```

## Next Topic

**02 – If-Else**

Folder:

```text
02-If-Else/
```

The next topic will explain how to execute one block when a condition is true and an alternative block when that condition is false.

---

# 52. Final Summary

The Python `if` statement is one of the most important concepts in programming because it introduces decision-making.

In this topic, you learned:

- What conditional statements are.
- Why decision-making is required.
- What an `if` statement does.
- How to write the correct syntax.
- How conditions are evaluated.
- What Boolean values mean.
- What truthy and falsy values are.
- How comparison operators work.
- How arithmetic operators are used in conditions.
- How logical operators combine conditions.
- How membership operators check collections.
- How identity operators check object identity.
- Why indentation is important.
- How code blocks execute.
- What happens when a condition is false.
- How to use multiple statements inside an `if` block.
- How independent `if` statements work.
- How to use `pass`.
- How to accept user input.
- How to work with integers, floats, strings, lists and dictionaries.
- How functions can be used in conditions.
- How to solve practical problems.
- How to perform dry runs.
- How to debug conditional programs.
- How `if` statements are used in DSA.

## Final Advice

Do not memorize only the syntax.

Understand how Python evaluates conditions, why a block executes, and why it is skipped.

Practice with different input values, especially boundary values such as 0, 18, 40 and 100.

Learn to write conditions independently before moving to complex combinations.

**The basic `if` statement is the foundation for every next topic in Conditional Statements. Build this foundation properly, then move to `if-else`, `if-elif-else` and nested conditions.**

---

**END OF README – TOPIC 01: IF STATEMENT**