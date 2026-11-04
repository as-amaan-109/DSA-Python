# Python Logical Operators

> A complete learning guide covering Logical AND, Logical OR, Logical NOT, truth tables, combined conditions, Boolean logic, truthy and falsy values, short-circuit evaluation, and practical programming applications in Python.

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [Learning Objectives](#2-learning-objectives)
3. [What Are Logical Operators?](#3-what-are-logical-operators)
4. [Logical Operator Overview](#4-logical-operator-overview)
5. [Boolean Values](#5-boolean-values)
6. [Logical AND Operator](#6-logical-and-operator)
7. [Logical OR Operator](#7-logical-or-operator)
8. [Logical NOT Operator](#8-logical-not-operator)
9. [Logical Operator Truth Tables](#9-logical-operator-truth-tables)
10. [Combining Logical Operators](#10-combining-logical-operators)
11. [Logical Operators with Comparison Operators](#11-logical-operators-with-comparison-operators)
12. [Logical Operators with Conditional Statements](#12-logical-operators-with-conditional-statements)
13. [Operator Precedence](#13-operator-precedence)
14. [Short-Circuit Evaluation](#14-short-circuit-evaluation)
15. [Truthy and Falsy Values](#15-truthy-and-falsy-values)
16. [Logical Operators with Non-Boolean Values](#16-logical-operators-with-non-boolean-values)
17. [Difference Between Logical and Bitwise Operators](#17-difference-between-logical-and-bitwise-operators)
18. [Understanding the Python Program](#18-understanding-the-python-program)
19. [Twelve Examples Explained](#19-twelve-examples-explained)
20. [Twelve Solved Programming Problems](#20-twelve-solved-programming-problems)
21. [Ten Unsolved Practice Questions](#21-ten-unsolved-practice-questions)
22. [Dry Run and Output Prediction](#22-dry-run-and-output-prediction)
23. [Common Programming Mistakes](#23-common-programming-mistakes)
24. [Error Handling and Input Validation](#24-error-handling-and-input-validation)
25. [Best Practices](#25-best-practices)
26. [Real-World Applications](#26-real-world-applications)
27. [Logical Operators in DSA](#27-logical-operators-in-dsa)
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

Logical operators are important components of Python programming. They are used to combine conditions, reverse Boolean results, and create complex decision-making expressions.

Python provides three logical operators:

- `and` – Logical AND.
- `or` – Logical OR.
- `not` – Logical NOT.

For example, consider a program that checks whether a person is eligible for an activity.

The person must satisfy two conditions:

1. The person's age must be at least 18.
2. The person must have a valid identity card.

Both conditions must be true.

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access Granted")
else:
    print("Access Denied")
```

**Output:**

```text
Access Granted
```

The `and` operator combines both conditions.

Now consider another situation where a student can receive a reward by winning either a coding competition or a mathematics competition.

```python
coding_winner = False
maths_winner = True

if coding_winner or maths_winner:
    print("Student receives a reward.")
else:
    print("Student does not receive a reward.")
```

**Output:**

```text
Student receives a reward.
```

The `or` operator returns a truthy result because at least one condition is true.

Finally, consider a program that checks whether a user is not eligible.

```python
is_eligible = False

print(not is_eligible)
```

**Output:**

```text
True
```

The `not` operator reverses the truth value.

## 1.1 Why Are Logical Operators Important?

Real-world programs frequently need to evaluate multiple conditions together.

For example:

- A student must pass an examination and meet an attendance requirement.
- A customer must have sufficient balance and a valid account.
- A user must enter a correct username or a valid recovery method.
- A person must not be blocked to access a system.
- A number must satisfy multiple mathematical conditions.

Logical operators help programmers express these requirements clearly.

## 1.2 Where Are Logical Operators Used?

| Area | Example Usage |
|---|---|
| Basic Python | Combining conditions |
| Education | Checking marks and attendance |
| Banking | Validating transactions |
| Authentication | Checking access requirements |
| Shopping | Checking discounts and eligibility |
| Gaming | Checking player status |
| Web development | Form validation |
| Searching | Combining conditions |
| DSA | Loop and algorithm conditions |
| Software systems | Permission and rule validation |

---

# 2. Learning Objectives

After completing this topic, you should be able to understand and use all three Python logical operators.

## 2.1 Basic Concepts

- Understand what logical operators are.
- Understand the purpose of logical AND.
- Understand the purpose of logical OR.
- Understand the purpose of logical NOT.
- Understand Boolean values.
- Understand truth tables.

## 2.2 Logical AND

- Use `and` to combine conditions.
- Understand why both conditions must be true.
- Evaluate multiple AND conditions.
- Apply AND to practical eligibility checks.

## 2.3 Logical OR

- Use `or` to combine conditions.
- Understand why at least one condition must be true.
- Evaluate multiple OR conditions.
- Apply OR to alternative conditions.

## 2.4 Logical NOT

- Use `not` to reverse a Boolean result.
- Reverse comparison conditions.
- Understand negation.
- Apply NOT to validation problems.

## 2.5 Advanced Concepts

- Combine multiple logical operators.
- Understand operator precedence.
- Understand short-circuit evaluation.
- Understand truthy and falsy values.
- Understand why `and` and `or` can return operands.
- Understand the difference between logical and bitwise operators.

## 2.6 Programming Skills

After completing this topic, you should be able to:

1. Check whether both numbers satisfy a condition.
2. Check whether at least one condition is true.
3. Validate a range.
4. Check age eligibility.
5. Validate student marks and attendance.
6. Check divisibility by multiple numbers.
7. Identify numbers outside a range.
8. Check whether a year is a leap year.
9. Validate triangle sides.
10. Write programs involving multiple conditions.

---

# 3. What Are Logical Operators?

Logical operators are used to combine or reverse conditions.

They are commonly used with comparison operators and Boolean expressions.

Python provides three logical operators:

| Operator | Name | Purpose |
|---|---|---|
| `and` | Logical AND | True when both operands are truthy |
| `or` | Logical OR | True when at least one operand is truthy |
| `not` | Logical NOT | Reverses the truth value |

## 3.1 General Syntax

### Logical AND

```python
condition1 and condition2
```

### Logical OR

```python
condition1 or condition2
```

### Logical NOT

```python
not condition
```

## 3.2 Example

```python
a = 10
b = 20

result = a < 20 and b > 10

print(result)
```

**Output:**

```text
True
```

Both conditions are true, so the final result is true.

## 3.3 How Do Logical Operators Work?

Consider:

```python
age = 25
has_id = True

result = age >= 18 and has_id

print(result)
```

Python evaluates:

1. `age >= 18`.
2. The result is `True`.
3. The second operand `has_id` is evaluated.
4. Its value is `True`.
5. Both operands are truthy, so the AND expression returns the second operand, which is `True`.

For Boolean operands, the result is straightforwardly `True` or `False`.

**Important:** In Python, `and` and `or` can return one of their operands rather than always returning a Boolean object. This behavior is explained in a later section.

---

# 4. Logical Operator Overview

## 4.1 Logical AND (`and`)

Returns a truthy result when both operands are truthy.

Example:

```python
print(True and True)
```

Output:

```text
True
```

## 4.2 Logical OR (`or`)

Returns a truthy result when at least one operand is truthy.

Example:

```python
print(True or False)
```

Output:

```text
True
```

## 4.3 Logical NOT (`not`)

Reverses the truth value of an operand.

Example:

```python
print(not True)
```

Output:

```text
False
```

## 4.4 Quick Comparison

| Expression | Result |
|---|---|
| `True and True` | `True` |
| `True and False` | `False` |
| `False or True` | `True` |
| `False or False` | `False` |
| `not True` | `False` |
| `not False` | `True` |

---

# 5. Boolean Values

Boolean values represent two truth states:

- `True`
- `False`

Python uses the built-in `bool` data type for Boolean values.

## 5.1 Example

```python
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
print(type(is_student))
```

**Output:**

```text
True
False
<class 'bool'>
```

## 5.2 Boolean Values from Comparisons

Comparison operators generally produce Boolean results.

```python
a = 10
b = 20

print(a < b)
print(a > b)
print(a == b)
```

**Output:**

```text
True
False
False
```

## 5.3 Storing a Comparison Result

```python
age = 20

is_eligible = age >= 18

print(is_eligible)
```

**Output:**

```text
True
```

The comparison result is stored in `is_eligible`.

## 5.4 Why Are Boolean Values Important?

Logical operators work with the truth values of their operands.

Boolean values are commonly used in:

- Conditional statements.
- Loop conditions.
- Input validation.
- Authentication logic.
- Mathematical checks.
- Application rules.
- Algorithmic decision-making.

---

# 6. Logical AND Operator

The logical AND operator is represented by:

```python
and
```

It combines two or more expressions.

For Boolean operands, it returns `True` only when every operand is true.

If any operand is false, the complete AND expression evaluates to false.

## 6.1 Syntax

```python
condition1 and condition2
```

## 6.2 Example 1: Both Conditions True

```python
a = 10
b = 20

print(a < 20 and b > 10)
```

**Output:**

```text
True
```

### Explanation

First condition:

```python
a < 20
```

Result:

```text
True
```

Second condition:

```python
b > 10
```

Result:

```text
True
```

Combined expression:

```python
True and True
```

Final result:

```text
True
```

## 6.3 Example 2: One Condition False

```python
a = 10
b = 5

print(a > 5 and b > 10)
```

**Output:**

```text
False
```

### Explanation

First condition:

```python
10 > 5
```

Result: `True`.

Second condition:

```python
5 > 10
```

Result: `False`.

Combined expression:

```python
True and False
```

Final result:

```text
False
```

## 6.4 Example 3: Both Conditions False

```python
a = 5
b = 8

print(a > 10 and b > 10)
```

**Output:**

```text
False
```

Both conditions are false.

## 6.5 Example 4: Three Conditions

```python
age = 22
has_id = True
has_ticket = True

result = age >= 18 and has_id and has_ticket

print(result)
```

**Output:**

```text
True
```

All three conditions are truthy.

## 6.6 Practical Example: Student Eligibility

A student must satisfy both conditions:

- Marks must be at least 40.
- Attendance must be at least 75%.

```python
marks = 75
attendance = 80

if marks >= 40 and attendance >= 75:
    print("Student is eligible.")
else:
    print("Student is not eligible.")
```

**Output:**

```text
Student is eligible.
```

## 6.7 Practical Example: Access Control

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access Granted.")
else:
    print("Access Denied.")
```

**Output:**

```text
Access Granted.
```

## 6.8 Important Points

- `and` combines multiple conditions.
- For Boolean operands, both must be true to produce `True`.
- One false operand makes the Boolean result false.
- It is useful when all requirements must be satisfied.
- Python evaluates the second operand only when necessary.

---

# 7. Logical OR Operator

The logical OR operator is represented by:

```python
or
```

It combines conditions and returns a truthy result when at least one operand is truthy.

For Boolean operands, OR returns `False` only when all operands are false.

## 7.1 Syntax

```python
condition1 or condition2
```

## 7.2 Example 1: First Condition True

```python
a = 20
b = 5

print(a > 10 or b > 10)
```

**Output:**

```text
True
```

The first condition is true, so the complete OR expression is true.

## 7.3 Example 2: Second Condition True

```python
a = 5
b = 20

print(a > 10 or b > 10)
```

**Output:**

```text
True
```

The second condition is true.

## 7.4 Example 3: Both Conditions True

```python
a = 20
b = 30

print(a > 10 or b > 10)
```

**Output:**

```text
True
```

Both conditions are true.

## 7.5 Example 4: Both Conditions False

```python
a = 5
b = 8

print(a > 10 or b > 10)
```

**Output:**

```text
False
```

Neither condition is true.

## 7.6 Example 5: Three Conditions

```python
is_admin = False
is_teacher = True
is_manager = False

result = is_admin or is_teacher or is_manager

print(result)
```

**Output:**

```text
True
```

At least one condition is true.

## 7.7 Practical Example: Alternative Login Methods

A simplified application may allow a user to proceed through either of two available verification methods.

```python
email_verified = False
phone_verified = True

if email_verified or phone_verified:
    print("At least one verification method is complete.")
else:
    print("Verification required.")
```

**Output:**

```text
At least one verification method is complete.
```

## 7.8 Practical Example: Temperature Alert

```python
temperature = 45

if temperature < 0 or temperature > 40:
    print("Temperature is outside the example range.")
else:
    print("Temperature is within the example range.")
```

**Output:**

```text
Temperature is outside the example range.
```

## 7.9 Important Points

- `or` combines alternative conditions.
- For Boolean operands, at least one true operand makes the result true.
- The result is false only when all operands are false.
- It is useful when multiple alternative conditions are acceptable.
- Python can skip evaluating the second operand when the first is truthy.

---

# 8. Logical NOT Operator

The logical NOT operator is represented by:

```python
not
```

It reverses the truth value of an expression.

For Boolean operands:

- `not True` returns `False`.
- `not False` returns `True`.

## 8.1 Syntax

```python
not condition
```

## 8.2 Example 1: True Becomes False

```python
value = True

print(not value)
```

**Output:**

```text
False
```

## 8.3 Example 2: False Becomes True

```python
value = False

print(not value)
```

**Output:**

```text
True
```

## 8.4 Example 3: NOT with a Comparison

```python
age = 16

print(not (age >= 18))
```

**Output:**

```text
True
```

### Explanation

First, Python evaluates:

```python
age >= 18
```

Result:

```text
False
```

Then:

```python
not False
```

Result:

```text
True
```

## 8.5 Example 4: NOT with Equality

```python
number = 10

print(not (number == 10))
```

**Output:**

```text
False
```

## 8.6 Practical Example: Checking an Inactive Account

```python
is_active = False

if not is_active:
    print("Account is inactive.")
else:
    print("Account is active.")
```

**Output:**

```text
Account is inactive.
```

## 8.7 Practical Example: Checking an Empty List

```python
numbers = []

if not numbers:
    print("The list is empty.")
else:
    print("The list contains values.")
```

**Output:**

```text
The list is empty.
```

The empty list is falsy, so `not numbers` evaluates to `True`.

## 8.8 Important Points

- `not` reverses truth values.
- It is a unary operator because it operates on one operand.
- It can be used with comparison expressions.
- It is useful for checking the opposite of a condition.
- It is frequently used in validation and control flow.

---

# 9. Logical Operator Truth Tables

Truth tables describe how logical operations behave for all possible combinations of Boolean inputs.

They are essential for understanding logical operators.

## 9.1 AND Truth Table

The AND operator returns true only when both values are true.

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Explanation

| Condition | Result |
|---|---|
| Both true | True |
| First true, second false | False |
| First false, second true | False |
| Both false | False |

## 9.2 OR Truth Table

The OR operator returns true when at least one value is true.

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Explanation

| Condition | Result |
|---|---|
| Both true | True |
| First true, second false | True |
| First false, second true | True |
| Both false | False |

## 9.3 NOT Truth Table

The NOT operator reverses a Boolean value.

| A | not A |
|---|---|
| True | False |
| False | True |

## 9.4 Combined Truth Table

| A | B | A and B | A or B | not A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

## 9.5 Easy Way to Remember

**AND:**

Both conditions must be true.

**OR:**

At least one condition must be true.

**NOT:**

Reverse the Boolean result.

---

# 10. Combining Logical Operators

Python allows multiple logical operators to be used in a single expression.

This helps create more detailed conditions.

## 10.1 AND with OR

```python
age = 20
has_id = True
is_guest = False

result = (age >= 18 and has_id) or is_guest

print(result)
```

**Output:**

```text
True
```

### Explanation

First:

```python
age >= 18 and has_id
```

Both conditions are true, so the expression is true.

Next:

```python
True or False
```

Final result:

```text
True
```

## 10.2 OR with AND

```python
has_email = False
has_phone = True
is_blocked = False

result = (has_email or has_phone) and not is_blocked

print(result)
```

**Output:**

```text
True
```

### Explanation

1. At least one contact method is available.
2. The user is not blocked.
3. Both requirements are satisfied.

## 10.3 Multiple AND Conditions

```python
age = 25
marks = 80
attendance = 90

result = age >= 18 and marks >= 40 and attendance >= 75

print(result)
```

**Output:**

```text
True
```

## 10.4 Multiple OR Conditions

```python
is_admin = False
is_teacher = False
is_manager = True

result = is_admin or is_teacher or is_manager

print(result)
```

**Output:**

```text
True
```

## 10.5 Combining AND, OR, and NOT

```python
age = 20
has_id = True
is_blocked = False
has_permission = False

result = (age >= 18 and has_id) and not is_blocked or has_permission

print(result)
```

**Output:**

```text
True
```

Parentheses should be used when they make the intended grouping clearer.

---

# 11. Logical Operators with Comparison Operators

Logical operators are frequently combined with comparison operators.

Comparison operators create conditions, while logical operators combine those conditions.

## 11.1 AND with Comparison

```python
age = 25

result = age >= 18 and age <= 60

print(result)
```

**Output:**

```text
True
```

The age is between 18 and 60, including both boundaries.

## 11.2 OR with Comparison

```python
number = 15

result = number < 0 or number > 100

print(result)
```

**Output:**

```text
False
```

The number is neither below zero nor above 100.

## 11.3 NOT with Comparison

```python
marks = 30

result = not (marks >= 40)

print(result)
```

**Output:**

```text
True
```

The student has not reached the passing mark.

## 11.4 Checking Even and Positive

```python
number = 10

if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number does not satisfy both conditions.")
```

**Output:**

```text
The number is positive and even.
```

## 11.5 Checking Odd or Negative

```python
number = -5

if number % 2 != 0 or number < 0:
    print("The number is odd or negative.")
else:
    print("Neither condition is satisfied.")
```

**Output:**

```text
The number is odd or negative.
```

## 11.6 Checking a Range

```python
number = 50

if number >= 1 and number <= 100:
    print("Number is within the range.")
else:
    print("Number is outside the range.")
```

**Output:**

```text
Number is within the range.
```

For a simple inclusive range, Python also supports:

```python
1 <= number <= 100
```

---

# 12. Logical Operators with Conditional Statements

Logical operators are widely used with conditional statements.

They help programs evaluate multiple requirements before selecting a block of code.

## 12.1 Using AND with if-else

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access Granted")
else:
    print("Access Denied")
```

**Output:**

```text
Access Granted
```

Both requirements must be satisfied.

## 12.2 Using OR with if-else

```python
is_admin = False
is_teacher = True

if is_admin or is_teacher:
    print("Access Granted")
else:
    print("Access Denied")
```

**Output:**

```text
Access Granted
```

At least one condition is true.

## 12.3 Using NOT with if-else

```python
is_locked = True

if not is_locked:
    print("Account is available.")
else:
    print("Account is locked.")
```

**Output:**

```text
Account is locked.
```

## 12.4 Using Multiple Logical Operators

```python
age = 25
has_id = True
is_blocked = False

if age >= 18 and has_id and not is_blocked:
    print("User can continue.")
else:
    print("User cannot continue.")
```

**Output:**

```text
User can continue.
```

## 12.5 Why Are Logical Operators Important in Conditions?

They help write programs involving:

- Multiple eligibility rules.
- Student result calculations.
- Login conditions.
- Product discounts.
- Permission checking.
- Data validation.
- Search filters.
- Algorithm termination conditions.

---

# 13. Operator Precedence

Operator precedence determines which operation is evaluated first when an expression contains multiple operators.

Python has a defined precedence order for logical operators.

For the three logical operators:

1. `not`
2. `and`
3. `or`

Comparison expressions also have higher precedence than logical `not`, `and`, and `or`.

## 13.1 Example Without Parentheses

```python
result = True or False and False

print(result)
```

**Output:**

```text
True
```

### Explanation

AND has higher precedence than OR.

First:

```python
False and False
```

Result:

```text
False
```

Then:

```python
True or False
```

Final result:

```text
True
```

## 13.2 Example with Parentheses

```python
result = (True or False) and False

print(result)
```

**Output:**

```text
False
```

Parentheses change the evaluation order.

## 13.3 Comparison of Expressions

| Expression | Evaluation Order |
|---|---|
| `not A and B` | `not A`, then AND |
| `A and B or C` | AND, then OR |
| `A or B and C` | AND, then OR |
| `(A or B) and C` | Parentheses, then AND |
| `A and (B or C)` | Parentheses, then AND |

## 13.4 Practical Example

```python
age = 20
has_id = True
is_blocked = False

result = age >= 18 and has_id or not is_blocked

print(result)
```

**Output:**

```text
True
```

Because `and` has higher precedence than `or`, the expression is evaluated as:

```python
(age >= 18 and has_id) or (not is_blocked)
```

## 13.5 Why Should We Use Parentheses?

Parentheses:

- Make expressions easier to understand.
- Show the intended grouping.
- Reduce ambiguity for readers.
- Help prevent logical mistakes.
- Make debugging easier.

**Best practice:** Even when parentheses are not strictly necessary, use them when they clarify the intended logic.

---

# 14. Short-Circuit Evaluation

Short-circuit evaluation is an important feature of Python's logical operators.

It means Python may stop evaluating an expression when the final result is already determined.

## 14.1 Short-Circuit Evaluation with AND

For AND:

- If the first operand is falsy, Python does not need to evaluate the second operand.
- The final result is already determined by the first operand.

### Example

```python
result = False and True

print(result)
```

**Output:**

```text
False
```

The second operand is not needed to determine the result.

### Function Example

```python
def first_condition():
    print("First condition evaluated.")
    return False


def second_condition():
    print("Second condition evaluated.")
    return True


result = first_condition() and second_condition()

print("Final Result:", result)
```

**Output:**

```text
First condition evaluated.
Final Result: False
```

The second function is never called.

## 14.2 Short-Circuit Evaluation with OR

For OR:

- If the first operand is truthy, Python does not need to evaluate the second operand.
- The final result is already determined by the first operand.

### Example

```python
result = True or False

print(result)
```

**Output:**

```text
True
```

### Function Example

```python
def first_condition():
    print("First condition evaluated.")
    return True


def second_condition():
    print("Second condition evaluated.")
    return False


result = first_condition() or second_condition()

print("Final Result:", result)
```

**Output:**

```text
First condition evaluated.
Final Result: True
```

The second function is not called.

## 14.3 Practical Example: Avoiding Division by Zero

```python
number = 10
divisor = 0

if divisor != 0 and number / divisor > 2:
    print("Condition satisfied.")
else:
    print("Invalid division or condition not satisfied.")
```

**Output:**

```text
Invalid division or condition not satisfied.
```

Because the first condition is false, Python skips the second condition.

This prevents division by zero.

## 14.4 Important Points

- AND stops when it encounters a falsy operand.
- OR stops when it encounters a truthy operand.
- The second operand may never be evaluated.
- Short-circuit evaluation can prevent unnecessary calculations.
- It can help avoid errors.
- Do not place important side effects in expressions that may be skipped unexpectedly.

---

# 15. Truthy and Falsy Values

Python does not restrict logical operators to Boolean values.

Many other values can also be used in logical expressions.

Python evaluates such values according to their truth value.

These values are divided into two categories:

- Truthy values.
- Falsy values.

## 15.1 What Is a Truthy Value?

A truthy value is a value that Python treats as true in a Boolean context.

Examples:

```python
bool(10)
bool(-5)
bool("Python")
bool([1, 2, 3])
bool({"name": "Amaan"})
```

All these expressions return:

```text
True
```

## 15.2 What Is a Falsy Value?

A falsy value is a value that Python treats as false in a Boolean context.

Common examples:

| Value | Boolean Result |
|---|---|
| `False` | False |
| `None` | False |
| `0` | False |
| `0.0` | False |
| `""` | False |
| `[]` | False |
| `()` | False |
| `{}` | False |
| `set()` | False |
| `range(0)` | False |

## 15.3 Example

```python
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))
```

**Output:**

```text
False
True
False
True
False
True
```

## 15.4 Practical Example: Empty List Validation

```python
numbers = []

if not numbers:
    print("No elements found.")
else:
    print("Elements are available.")
```

**Output:**

```text
No elements found.
```

## 15.5 Practical Example: Checking User Input

```python
username = ""

if username:
    print("Username provided.")
else:
    print("Username is empty.")
```

**Output:**

```text
Username is empty.
```

## 15.6 Important Points

- Empty containers are falsy.
- Non-empty containers are generally truthy.
- Zero is falsy.
- Non-zero numbers are truthy.
- Empty strings are falsy.
- Non-empty strings are truthy.
- `None` is falsy.
- Python uses truth-value testing in logical expressions.

---

# 16. Logical Operators with Non-Boolean Values

Python's `and` and `or` operators do not always return `True` or `False`.

They return one of their operands.

This is an important Python-specific behavior.

## 16.1 AND Returns an Operand

General behavior:

```python
x and y
```

- If `x` is falsy, it returns `x`.
- Otherwise, it returns `y`.

### Example

```python
first = ""
second = "Python"

print(first and second)
```

**Output:**

```text

```

The first operand is an empty string, which is falsy. Therefore, it is returned.

Another example:

```python
first = "Python"
second = "DSA"

print(first and second)
```

**Output:**

```text
DSA
```

The first value is truthy, so the second operand is evaluated and returned.

## 16.2 OR Returns an Operand

General behavior:

```python
x or y
```

- If `x` is truthy, it returns `x`.
- Otherwise, it returns `y`.

### Example

```python
first = "Python"
second = "DSA"

print(first or second)
```

**Output:**

```text
Python
```

The first operand is truthy, so it is returned.

Another example:

```python
first = ""
second = "Python"

print(first or second)
```

**Output:**

```text
Python
```

The first operand is falsy, so Python evaluates and returns the second operand.

## 16.3 NOT Always Returns a Boolean

Unlike `and` and `or`, `not` always produces a Boolean result.

```python
print(not 0)
print(not 10)
print(not "")
print(not "Python")
```

**Output:**

```text
True
False
True
False
```

## 16.4 Example from the Python Program

```python
first = ""
second = "Python"

print("Empty String or Python:", first or second)
print("Python and DSA:", second and "DSA")
print("Not Empty String:", not first)
```

**Output:**

```text
Empty String or Python: Python
Python and DSA: DSA
Not Empty String: True
```

## 16.5 Common Uses

This behavior is sometimes used for providing default values.

```python
username = ""
display_name = username or "Guest"

print(display_name)
```

**Output:**

```text
Guest
```

However, remember that `or` treats every falsy value as a reason to use the fallback.

If only `None` should trigger a default, use an explicit `is None` check instead.

---

# 17. Difference Between Logical and Bitwise Operators

Logical operators and bitwise operators are different.

Although some bitwise operators use symbols such as `&` and `|`, they do not have the same purpose as `and` and `or`.

## 17.1 Logical AND vs Bitwise AND

Logical AND:

```python
print(True and False)
```

Output:

```text
False
```

Bitwise AND:

```python
print(5 & 3)
```

Output:

```text
1
```

The bitwise operation works on binary representations.

## 17.2 Logical OR vs Bitwise OR

Logical OR:

```python
print(True or False)
```

Output:

```text
True
```

Bitwise OR:

```python
print(5 | 3)
```

Output:

```text
7
```

## 17.3 Comparison Table

| Logical Operator | Bitwise Operator |
|---|---|
| `and` | `&` |
| `or` | `|` |
| `not` | `~` for integer bitwise inversion |
| Used for truth-value logic | Used for bit-level operations |
| Supports truth-value testing | Operates on integer bits or compatible overloaded types |
| `True and False` | `5 & 3` |
| Supports short-circuit evaluation | Does not use logical short-circuit behavior |

**Important:** Do not replace `and` with `&` or `or` with `|` in ordinary conditional logic.

---

# 18. Understanding the Python Program

**File Name:** `01_logical_operators.py`

The Python program is organized into different sections to make learning and practice easier.

## 18.1 Module Documentation

The program begins with a module-level docstring.

It explains:

- The topic name.
- The purpose of the program.
- The logical operators covered.
- The sections included.
- The menu structure.

This documentation helps developers understand the file.

## 18.2 Import Section

The program imports:

```python
import math
```

The `math` module provides mathematical functions.

This program uses:

```python
math.isfinite()
```

to check whether a floating-point input is finite.

It rejects:

- Positive infinity.
- Negative infinity.
- NaN.

## 18.3 Helper Functions

The program defines four reusable helper functions.

| Function | Purpose |
|---|---|
| `print_heading()` | Displays formatted section headings. |
| `read_int()` | Reads an integer and handles invalid input. |
| `read_float()` | Reads a finite floating-point value. |
| `read_text()` | Reads non-empty text. |

### Why Are Helper Functions Useful?

1. Reduce repeated code.
2. Improve readability.
3. Make input validation reusable.
4. Separate input handling from calculation.
5. Make the program easier to maintain.

## 18.4 Section 1: Twelve Examples

The first section contains twelve examples.

| No. | Example | Concept |
|---:|---|---|
| 1 | AND with both conditions true | `and` |
| 2 | AND with one condition false | `and` |
| 3 | OR with at least one true condition | `or` |
| 4 | OR with both conditions false | `or` |
| 5 | NOT reverses true | `not` |
| 6 | NOT reverses false | `not` |
| 7 | AND with comparison operators | Combined conditions |
| 8 | OR with comparison operators | Alternative conditions |
| 9 | NOT with comparison | Negation |
| 10 | Combined logical expressions | `and`, `or` |
| 11 | Logical operators with non-Boolean values | Truthiness |
| 12 | Short-circuit evaluation | Lazy operand evaluation |

## 18.5 Section 2: Twelve Solved Problems

The second section contains twelve practical programs.

They cover:

1. Both numbers positive.
2. At least one number positive.
3. Number outside a range.
4. Age eligibility range.
5. Student passing conditions.
6. Divisibility by both 3 and 5.
7. Divisibility by 3 or 5.
8. Checking whether a number is not zero.
9. Checking whether a number is outside an inclusive range.
10. Largest of three numbers.
11. Leap year validation.
12. Valid triangle validation.

## 18.6 `SOLVED_PROBLEMS` Dictionary

The program uses a dictionary named:

```python
SOLVED_PROBLEMS
```

It maps problem numbers to:

- A problem description.
- A function that executes the selected problem.

This makes the solved-problem section easier to manage.

## 18.7 `show_solved_problems()`

This function displays all twelve available problems.

It allows users to select a problem based on its number.

## 18.8 `run_solved_problems()`

This function:

1. Displays the problem list.
2. Accepts a problem number.
3. Validates the selection.
4. Executes the selected problem.
5. Returns to the problem list.
6. Allows the user to return to the main menu.

## 18.9 Section 3: Ten Unsolved Practice Questions

This section displays ten independent practice questions.

Each question includes a small hint.

The purpose is to help students practise logical reasoning independently.

## 18.10 Section 4: Learning Checklist

This section displays the important concepts of the topic.

It helps learners review their progress.

## 18.11 Section 5: Main Menu

The main menu connects every program section.

| Option | Action |
|---:|---|
| 1 | View twelve examples |
| 2 | Practise twelve solved problems |
| 3 | View ten unsolved questions |
| 4 | View learning checklist |
| 0 | Exit |

The program continues until the user selects `0`.

---

# 19. Twelve Examples Explained

This section explains the twelve examples from `01_logical_operators.py`.

## Example 1: Logical AND – Both Conditions True

**Concept:** `and`

Purpose:

- Understand AND behavior.
- Combine two comparisons.
- Verify that both conditions are satisfied.

Code:

```python
a = 10
b = 20

print(a < 20 and b > 10)
```

Output:

```text
True
```

Explanation:

- `a < 20` is `True`.
- `b > 10` is `True`.
- Both are true, so the result is `True`.

## Example 2: Logical AND – One Condition False

**Concept:** `and`

Code:

```python
a = 10
b = 5

print(a > 5 and b > 10)
```

Output:

```text
False
```

Explanation:

- `a > 5` is `True`.
- `b > 10` is `False`.
- AND returns a falsy result because the second operand is false.

## Example 3: Logical OR – At Least One True

**Concept:** `or`

Code:

```python
a = 5
b = 20

print(a > 10 or b > 10)
```

Output:

```text
True
```

Explanation:

- `a > 10` is `False`.
- `b > 10` is `True`.
- At least one operand is true, so the result is true.

## Example 4: Logical OR – Both False

**Concept:** `or`

Code:

```python
a = 5
b = 8

print(a > 10 or b > 10)
```

Output:

```text
False
```

Neither operand is true.

## Example 5: Logical NOT – True Becomes False

**Concept:** `not`

Code:

```python
value = True

print(not value)
```

Output:

```text
False
```

NOT reverses the truth value.

## Example 6: Logical NOT – False Becomes True

**Concept:** `not`

Code:

```python
value = False

print(not value)
```

Output:

```text
True
```

NOT converts a false truth value into true.

## Example 7: AND with Comparison Operators

**Concept:** `and` with `>=` and `<=`

Code:

```python
age = 25

result = age >= 18 and age <= 60

print(result)
```

Output:

```text
True
```

Both range conditions are satisfied.

## Example 8: OR with Comparison Operators

**Concept:** `or` with `<` and `>`

Code:

```python
temperature = 45

result = temperature < 0 or temperature > 40

print(result)
```

Output:

```text
True
```

The temperature is above the example range.

## Example 9: NOT with Comparison

**Concept:** `not`

Code:

```python
age = 16

result = not (age >= 18)

print(result)
```

Output:

```text
True
```

The age condition is false, and NOT reverses that result.

## Example 10: Combined Logical Conditions

**Concept:** `and` and `or`

Code:

```python
age = 20
has_id = True
is_guest = False

result = (age >= 18 and has_id) or is_guest

print(result)
```

Output:

```text
True
```

Explanation:

- The age requirement is satisfied.
- The identity requirement is satisfied.
- The guest condition is false.
- The left side of OR is already true.

Final result: `True`.

## Example 11: Logical Operators with Non-Boolean Values

**Concept:** Truthy and falsy values.

Code:

```python
first = ""
second = "Python"

print("Empty String or Python:", first or second)
print("Python and DSA:", second and "DSA")
print("Not Empty String:", not first)
```

Output:

```text
Empty String or Python: Python
Python and DSA: DSA
Not Empty String: True
```

Explanation:

- An empty string is falsy.
- `"Python"` is truthy.
- OR returns `"Python"`.
- AND returns `"DSA"` because the first operand is truthy.
- NOT applied to an empty string returns `True`.

## Example 12: Short-Circuit Evaluation

**Concept:** Short-circuit evaluation.

The program defines two functions:

- `first_condition()`
- `second_condition()`

Each function displays a message when it executes.

### AND Example

```python
result = first_condition() and second_condition()
```

The first function returns `False`.

Therefore, the second function is not executed.

### OR Example

```python
result = second_condition() or first_condition()
```

The second function returns `True`.

Therefore, the first function is not executed.

The example demonstrates how Python can avoid unnecessary evaluation.

---

# 20. Twelve Solved Programming Problems

This section explains the twelve practical problems included in the Python program.

Each problem contains:

1. Problem statement.
2. Required logical operator.
3. Logic.
4. Example code.
5. Expected output.
6. Explanation.
7. Learning point.

---

## Problem 1: Check Whether Both Numbers Are Positive

**Concept:** Logical AND (`and`)

### Problem Statement

Accept two numbers and check whether both numbers are positive.

### Logic

1. Accept the first number.
2. Accept the second number.
3. Check whether the first number is greater than zero.
4. Check whether the second number is greater than zero.
5. Combine both conditions using AND.

### Example Code

```python
a = 10
b = 20

if a > 0 and b > 0:
    print("Both numbers are positive.")
else:
    print("Both numbers are not positive.")
```

### Output

```text
Both numbers are positive.
```

### Dry Run

| Condition | Result |
|---|---|
| `10 > 0` | True |
| `20 > 0` | True |
| AND result | True |

### Explanation

Both numbers are greater than zero.

Therefore, both conditions are satisfied.

### Learning Point

AND is useful when every requirement must be satisfied.

---

## Problem 2: Check Whether At Least One Number Is Positive

**Concept:** Logical OR (`or`)

### Problem Statement

Accept two numbers and check whether at least one is positive.

### Logic

1. Accept two numbers.
2. Check whether the first number is positive.
3. Check whether the second number is positive.
4. Combine using OR.

### Example Code

```python
a = -10
b = 20

if a > 0 or b > 0:
    print("At least one number is positive.")
else:
    print("Neither number is positive.")
```

### Output

```text
At least one number is positive.
```

### Explanation

- The first number is negative.
- The second number is positive.
- At least one condition is true.

### Learning Point

OR is useful when any one of multiple requirements can be sufficient.

---

## Problem 3: Check Whether a Number Is Outside a Range

**Concept:** Logical OR (`or`)

### Problem Statement

Accept a number and two range limits. Check whether the number is outside the range.

### Logic

1. Read the number.
2. Read the lower limit.
3. Read the upper limit.
4. Check that the range is valid.
5. Check whether the number is below the lower limit OR above the upper limit.

### Example Code

```python
number = 25
lower = 10
upper = 20

if lower > upper:
    print("Invalid range.")
elif number < lower or number > upper:
    print("The number is outside the range.")
else:
    print("The number is within the range.")
```

### Output

```text
The number is outside the range.
```

### Explanation

The number `25` is greater than the upper limit `20`.

Therefore, the outside-range condition is true.

### Learning Point

OR is useful for checking whether one of several invalid conditions is satisfied.

---

## Problem 4: Check Age Eligibility Range

**Concept:** Logical AND (`and`)

### Problem Statement

Accept a person's age and check whether it lies between 18 and 60, inclusive.

### Logic

1. Accept age.
2. Reject negative age.
3. Check whether age is at least 18.
4. Check whether age is at most 60.
5. Combine both using AND.

### Example Code

```python
age = 25

if age < 0:
    print("Invalid age.")
elif age >= 18 and age <= 60:
    print("Age is within the eligibility range.")
else:
    print("Age is outside the eligibility range.")
```

### Output

```text
Age is within the eligibility range.
```

### Explanation

Both conditions are satisfied:

```python
age >= 18
age <= 60
```

The age `25` is inside the permitted range.

### Learning Point

AND is useful for checking inclusive ranges.

---

## Problem 5: Check Student Passing Conditions

**Concept:** Logical AND (`and`) and NOT (`not`)

### Problem Statement

A student must satisfy two requirements:

- Marks must be at least 40.
- Attendance must be at least 75%.

Validate the inputs and check both conditions.

### Logic

1. Read marks.
2. Read attendance.
3. Check that marks are between 0 and 100.
4. Check that attendance is between 0 and 100.
5. Check both passing conditions using AND.
6. Display the result.

### Example Code

```python
marks = 75
attendance = 80

if not (0 <= marks <= 100):
    print("Invalid marks.")
elif not (0 <= attendance <= 100):
    print("Invalid attendance.")
elif marks >= 40 and attendance >= 75:
    print("Result: PASS")
else:
    print("Result: FAIL")
```

### Output

```text
Result: PASS
```

### Dry Run

| Condition | Result |
|---|---|
| Marks within 0–100 | True |
| Attendance within 0–100 | True |
| Marks at least 40 | True |
| Attendance at least 75 | True |
| Final result | PASS |

### Explanation

Both the marks requirement and attendance requirement are satisfied.

### Learning Point

AND is useful when multiple eligibility conditions must be fulfilled.

---

## Problem 6: Check Divisibility by Both 3 and 5

**Concept:** Logical AND (`and`) and modulus (`%`)

### Problem Statement

Accept an integer and check whether it is divisible by both 3 and 5.

### Logic

1. Read an integer.
2. Calculate the remainder when divided by 3.
3. Calculate the remainder when divided by 5.
4. Check whether both remainders are zero.

### Example Code

```python
number = 30

if number % 3 == 0 and number % 5 == 0:
    print(number, "is divisible by both 3 and 5.")
else:
    print(number, "is not divisible by both 3 and 5.")
```

### Output

```text
30 is divisible by both 3 and 5.
```

### Explanation

```text
30 % 3 = 0
30 % 5 = 0
```

Both conditions are true.

### Learning Point

AND is useful when a number must satisfy multiple mathematical conditions.

---

## Problem 7: Check Divisibility by 3 or 5

**Concept:** Logical OR (`or`) and modulus (`%`)

### Problem Statement

Accept an integer and check whether it is divisible by 3 or 5.

### Logic

1. Read an integer.
2. Check divisibility by 3.
3. Check divisibility by 5.
4. Combine using OR.

### Example Code

```python
number = 14

if number % 3 == 0 or number % 5 == 0:
    print(number, "is divisible by 3 or 5.")
else:
    print(number, "is divisible by neither 3 nor 5.")
```

### Output

```text
14 is divisible by neither 3 nor 5.
```

### Explanation

```text
14 % 3 = 2
14 % 5 = 4
```

Neither remainder is zero, so both conditions are false.

### Learning Point

OR is useful for checking alternative mathematical conditions.

---

## Problem 8: Check Whether a Number Is Not Zero

**Concept:** Logical NOT (`not`)

### Problem Statement

Accept a number and check whether it is not equal to zero.

### Logic

1. Read the number.
2. Check whether it equals zero.
3. Reverse the result using NOT.
4. Display the result.

### Example Code

```python
number = 10

if not (number == 0):
    print("The number is not zero.")
else:
    print("The number is zero.")
```

### Output

```text
The number is not zero.
```

### Explanation

First:

```python
number == 0
```

returns `False`.

Then:

```python
not False
```

returns `True`.

### Learning Point

NOT is useful when checking the opposite of a condition.

---

## Problem 9: Check Whether a Number Is Not Within a Range

**Concept:** Logical NOT (`not`) and chained comparison

### Problem Statement

Accept a number and two limits. Check whether the number is outside an inclusive range.

### Logic

1. Read the number.
2. Read the lower and upper limits.
3. Validate the range.
4. Check whether the number belongs to the range.
5. Reverse the result using NOT.

### Example Code

```python
number = 25
lower = 10
upper = 20

if lower > upper:
    print("Invalid range.")
elif not (lower <= number <= upper):
    print("The number is outside the inclusive range.")
else:
    print("The number is within the inclusive range.")
```

### Output

```text
The number is outside the inclusive range.
```

### Explanation

The range condition:

```python
10 <= 25 <= 20
```

is false.

NOT reverses it to true.

### Learning Point

NOT is useful for negating a complete condition.

---

## Problem 10: Find the Largest of Three Numbers

**Concept:** Logical AND (`and`) and comparison operators

### Problem Statement

Accept three numbers and find the largest value.

### Logic

1. Read three numbers.
2. Check whether the first is greater than or equal to both others.
3. Otherwise check whether the second is greater than or equal to both others.
4. Otherwise select the third.

### Example Code

```python
a = 10
b = 50
c = 30

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)
```

### Output

```text
Largest number: 50
```

### Explanation

The first condition is false.

The second condition is true because:

```python
50 >= 10
50 >= 30
```

Therefore, the largest value is `50`.

### Learning Point

AND can combine multiple comparisons to identify the maximum value.

---

## Problem 11: Check Leap Year

**Concept:** Logical AND (`and`), OR (`or`), and NOT (`not`)

### Problem Statement

Accept a year and determine whether it is a leap year.

The standard leap-year rules are:

1. A year divisible by 400 is a leap year.
2. Otherwise, a year divisible by 4 is a leap year only when it is not divisible by 100.

### Logic

1. Accept a positive year.
2. Check divisibility by 400.
3. Alternatively, check divisibility by 4.
4. Exclude years divisible by 100 unless they are divisible by 400.

### Example Code

```python
year = 2024

if year <= 0:
    print("Please enter a valid positive year.")
elif year % 400 == 0 or (
    year % 4 == 0 and not (year % 100 == 0)
):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```

### Output

```text
2024 is a leap year.
```

### Examples

| Year | Result |
|---:|---|
| 2024 | Leap year |
| 2023 | Not a leap year |
| 2000 | Leap year |
| 1900 | Not a leap year |
| 2400 | Leap year |

### Explanation

For 2024:

```text
2024 % 4 = 0
2024 % 100 != 0
```

Both required conditions are satisfied.

### Learning Point

The leap-year problem is a useful exercise for combining AND, OR, and NOT.

---

## Problem 12: Check Valid Triangle

**Concept:** Logical AND (`and`) and OR (`or`)

### Problem Statement

Accept three side lengths and check whether they can form a valid triangle.

For three positive lengths `a`, `b`, and `c`, all three triangle inequalities must hold:

```text
a + b > c
a + c > b
b + c > a
```

### Logic

1. Accept the three sides.
2. Check that all sides are positive.
3. Check the first triangle inequality.
4. Check the second triangle inequality.
5. Check the third triangle inequality.
6. Combine all three using AND.

### Example Code

```python
a = 3
b = 4
c = 5

if a <= 0 or b <= 0 or c <= 0:
    print("All triangle sides must be positive.")
elif (a + b > c) and (a + c > b) and (b + c > a):
    print("The given sides form a valid triangle.")
else:
    print("The given sides do not form a valid triangle.")
```

### Output

```text
The given sides form a valid triangle.
```

### Explanation

Check the inequalities:

```text
3 + 4 > 5
3 + 5 > 4
4 + 5 > 3
```

All three conditions are true.

Therefore, the side lengths form a valid triangle.

### Learning Point

Logical operators help validate multiple mathematical requirements together.

---

# 21. Ten Unsolved Practice Questions

Solve these questions independently using logical operators.

Try to identify the correct logical operator before writing the program.

## Question 1: Check Whether Both Numbers Are Even

**Concept:** AND (`and`)

Write a program that:

1. Accepts two integers.
2. Checks whether the first number is even.
3. Checks whether the second number is even.
4. Displays whether both are even.

**Hint:** Use modulus with AND.

## Question 2: Check Whether At Least One Number Is Even

**Concept:** OR (`or`)

Write a program that accepts two integers and checks whether at least one is even.

**Hint:** Use two remainder conditions with OR.

## Question 3: Check an Inclusive Range

**Concept:** AND (`and`)

Write a program that accepts a number and two limits.

Check whether the number is within the inclusive range.

**Hint:** Use both lower-bound and upper-bound comparisons.

## Question 4: Check Whether a Number Is Outside a Range

**Concept:** OR (`or`) or NOT (`not`)

Write a program that accepts a number and two limits.

Display whether the number is outside the range.

**Hint:** Check whether it is below the lower limit or above the upper limit.

## Question 5: Check Age and Membership Eligibility

**Concept:** AND (`and`)

Write a program that accepts a person's age and membership status.

The person must:

- Be at least 18 years old.
- Have active membership.

Display whether both requirements are satisfied.

**Hint:** Combine the age comparison and Boolean membership value with AND.

## Question 6: Check Divisibility by Both 2 and 7

**Concept:** AND (`and`)

Write a program that accepts an integer and checks whether it is divisible by both 2 and 7.

**Hint:** Use two modulus operations with AND.

## Question 7: Check Divisibility by 4 or 6

**Concept:** OR (`or`)

Write a program that accepts a number and checks whether it is divisible by 4 or 6.

**Hint:** Use OR between the two divisibility conditions.

## Question 8: Check Leap Year

**Concept:** AND, OR, and NOT

Write a program that accepts a year and checks whether it is a leap year.

**Hint:** Follow the standard divisibility rules.

## Question 9: Check Whether a Number Is Outside a Range Using NOT

**Concept:** NOT (`not`)

Write a program that accepts a number and two limits.

Use NOT with a chained comparison to determine whether the number is outside the range.

**Hint:**

```python
not (lower <= number <= upper)
```

## Question 10: Check Whether Three Sides Form a Valid Triangle

**Concept:** AND and OR

Write a program that accepts three positive side lengths.

Check all three triangle inequalities.

**Hint:** All three triangle inequalities must be true, and no side can be zero or negative.

---

# 22. Dry Run and Output Prediction

Dry running means manually tracing the execution of a program to predict its result.

It is important for practical examinations, debugging, and interviews.

## Question 1

Predict the output:

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

### Dry Run

| Expression | Result |
|---|---|
| `True and False` | False |
| `True or False` | True |
| `not True` | False |

**Answer:**

```text
False
True
False
```

## Question 2

Predict the output:

```python
a = 10
b = 20

print(a < 20 and b > 10)
print(a > 20 or b > 10)
```

**Answer:**

```text
True
True
```

## Question 3

Predict the output:

```python
number = 15

print(number > 10 and number < 20)
print(number < 5 or number > 20)
```

**Answer:**

```text
True
False
```

## Question 4

Predict the output:

```python
value = False

print(not value)
print(not not value)
```

**Answer:**

```text
True
False
```

## Question 5

Predict the output:

```python
print(True or False and False)
```

**Answer:**

```text
True
```

AND is evaluated before OR.

## Question 6

Predict the output:

```python
first = ""
second = "Python"

print(first or second)
print(first and second)
```

**Answer:**

```text
Python

```

The second line prints an empty string.

## Question 7

Predict the output:

```python
marks = 80
attendance = 70

print(marks >= 40 and attendance >= 75)
```

**Answer:**

```text
False
```

## Question 8

Predict the output:

```python
number = 15

print(number % 3 == 0 and number % 5 == 0)
```

**Answer:**

```text
True
```

## Question 9

Predict the output:

```python
number = 10

print(not (number == 10))
print(not (number != 10))
```

**Answer:**

```text
False
True
```

## Question 10

Predict the output:

```python
a = 5
b = 10
c = 15

print(a < b and b < c)
print(a > b or b > c)
```

**Answer:**

```text
True
False
```

---

# 23. Common Programming Mistakes

Understanding common mistakes helps you write accurate logical expressions.

## Mistake 1: Using `&` Instead of `and`

Incorrect for ordinary conditional logic:

```python
if age >= 18 & has_id:
    print("Access Granted")
```

Correct:

```python
if age >= 18 and has_id:
    print("Access Granted")
```

Use `and` for logical conditions.

## Mistake 2: Using `|` Instead of `or`

Incorrect for ordinary conditional logic:

```python
if is_admin | is_teacher:
    print("Access Granted")
```

Correct:

```python
if is_admin or is_teacher:
    print("Access Granted")
```

Bitwise OR and logical OR are different operations.

## Mistake 3: Forgetting Parentheses

For complicated expressions, unclear grouping can cause logical mistakes.

Less readable:

```python
result = age >= 18 and has_id or is_guest
```

Clearer:

```python
result = (age >= 18 and has_id) or is_guest
```

Parentheses make the intended grouping easier to understand.

## Mistake 4: Using OR Instead of AND

Suppose a student must satisfy both marks and attendance requirements.

Incorrect:

```python
if marks >= 40 or attendance >= 75:
    print("PASS")
```

This allows the student to pass even when only one condition is satisfied.

Correct:

```python
if marks >= 40 and attendance >= 75:
    print("PASS")
```

## Mistake 5: Incorrect Range Validation

Incorrect:

```python
if number >= 10 or number <= 20:
    print("Within range")
```

This condition does not correctly check whether the number is between 10 and 20.

Correct:

```python
if number >= 10 and number <= 20:
    print("Within range")
```

Or:

```python
if 10 <= number <= 20:
    print("Within range")
```

## Mistake 6: Forgetting NOT Changes the Condition

```python
value = True

print(not value)
```

Output:

```text
False
```

NOT reverses the truth value.

## Mistake 7: Assuming AND and OR Always Return Boolean Values

Example:

```python
print("Python" or "DSA")
```

Output:

```text
Python
```

OR returns an operand.

## Mistake 8: Ignoring Short-Circuit Evaluation

Incorrect:

```python
number = 10
divisor = 0

if number / divisor > 2 and divisor != 0:
    print("Valid")
```

This attempts division before validating the divisor.

Correct:

```python
if divisor != 0 and number / divisor > 2:
    print("Valid")
```

The first condition protects the second operation.

## Mistake 9: Comparing the Wrong Conditions

Read the problem statement carefully.

For example:

- "Both conditions" usually means AND.
- "At least one condition" usually means OR.
- "Not satisfied" often involves NOT.
- "Between two values" generally means two bounds combined with AND.

## Mistake 10: Ignoring Boundary Values

When checking an inclusive range, use the appropriate operators.

For example:

```python
0 <= marks <= 100
```

includes both `0` and `100`.

---

# 24. Error Handling and Input Validation

Input validation ensures that user-provided values satisfy the expected requirements.

## 24.1 Handling Invalid Integer Input

```python
try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Please enter a valid integer.")
```

If invalid text is entered, Python raises a `ValueError`.

## 24.2 Validating Age

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18 and age <= 60:
    print("Age is within the example range.")
else:
    print("Age is outside the example range.")
```

## 24.3 Validating Student Marks and Attendance

```python
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

if not (0 <= marks <= 100):
    print("Invalid marks.")
elif not (0 <= attendance <= 100):
    print("Invalid attendance.")
elif marks >= 40 and attendance >= 75:
    print("PASS")
else:
    print("FAIL")
```

## 24.4 Validating a Number Before Division

```python
number = 100
divisor = 0

if divisor != 0 and number / divisor > 5:
    print("Condition satisfied.")
else:
    print("Invalid divisor or condition not satisfied.")
```

## 24.5 Validating a Range

```python
lower = 10
upper = 50
number = 30

if lower > upper:
    print("Invalid range.")
elif lower <= number <= upper:
    print("Number is within range.")
else:
    print("Number is outside range.")
```

## 24.6 Why Is Validation Important?

Input validation:

- Prevents invalid information from being accepted.
- Helps avoid mathematical errors.
- Improves program reliability.
- Makes application behavior predictable.
- Helps detect invalid data early.

---

# 25. Best Practices

Follow these practices when writing logical expressions.

1. Use `and` when all required conditions must be satisfied.
2. Use `or` when at least one condition is sufficient.
3. Use `not` when the opposite of a condition is required.
4. Use meaningful variable names.
5. Keep conditions readable.
6. Use parentheses when grouping is important.
7. Understand operator precedence.
8. Check whether inputs have valid data types.
9. Use chained comparisons for straightforward range checks.
10. Put safe validation conditions before risky calculations.
11. Remember that `and` and `or` can return operands.
12. Understand when short-circuit evaluation skips an expression.
13. Avoid using bitwise operators in place of logical operators.
14. Test expressions with both true and false cases.
15. Test boundary values.
16. Avoid overly complicated conditions.
17. Break complex conditions into smaller Boolean variables when necessary.

---

# 26. Real-World Applications

Logical operators are used in almost every software application.

## 26.1 Student Result Systems

A student must satisfy both passing criteria.

```python
marks = 80
attendance = 85

if marks >= 40 and attendance >= 75:
    print("Student passed.")
else:
    print("Student failed.")
```

Output:

```text
Student passed.
```

## 26.2 Authentication Systems

```python
username_correct = True
password_correct = True
account_blocked = False

if username_correct and password_correct and not account_blocked:
    print("Login successful.")
else:
    print("Login failed.")
```

Output:

```text
Login successful.
```

This is a simplified example of combining authentication conditions, not a complete secure login system.

## 26.3 Shopping Applications

```python
purchase_amount = 2000
is_member = True

if purchase_amount >= 1000 and is_member:
    print("Discount criteria satisfied.")
else:
    print("Discount criteria not satisfied.")
```

Output:

```text
Discount criteria satisfied.
```

## 26.4 Banking Applications

```python
balance = 5000
withdrawal = 2000
account_active = True

if account_active and balance >= withdrawal:
    print("Transaction can proceed.")
else:
    print("Transaction cannot proceed.")
```

Output:

```text
Transaction can proceed.
```

## 26.5 Game Development

```python
health = 50
has_lives = True

if health > 0 and has_lives:
    print("Player continues.")
else:
    print("Game Over.")
```

Output:

```text
Player continues.
```

## 26.6 Temperature Monitoring

```python
temperature = 45

if temperature < 0 or temperature > 40:
    print("Temperature alert!")
else:
    print("Temperature is normal.")
```

Output:

```text
Temperature alert!
```

The temperature limits are illustrative for the example.

## 26.7 Inventory Management

```python
stock = 5
minimum_stock = 10
is_order_pending = False

if stock < minimum_stock and not is_order_pending:
    print("Place a new order.")
else:
    print("No new order is required.")
```

Output:

```text
Place a new order.
```

## 26.8 Access Permissions

```python
is_admin = False
is_teacher = True
is_blocked = False

if (is_admin or is_teacher) and not is_blocked:
    print("Access Granted.")
else:
    print("Access Denied.")
```

Output:

```text
Access Granted.
```

---

# 27. Logical Operators in DSA

Logical operators are important when implementing algorithms and solving DSA problems.

They allow multiple requirements to be combined into a single condition.

## 27.1 Loop Conditions

```python
left = 0
right = 5

while left < right:
    print(left, right)
    left += 1
    right -= 1
```

The loop runs while the left pointer is smaller than the right pointer.

## 27.2 Array Range Checking

```python
index = 3
size = 10

if index >= 0 and index < size:
    print("Valid index.")
else:
    print("Invalid index.")
```

Output:

```text
Valid index.
```

This is a common condition for validating array indexes.

## 27.3 Searching

```python
numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Element found.")
else:
    print("Element not found.")
```

Output:

```text
Element found.
```

The search condition uses equality comparison, and the result controls the program flow.

## 27.4 Two-Pointer Technique

```python
left = 0
right = 5

while left < right:
    left += 1
    right -= 1

print(left, right)
```

The `left < right` condition determines whether the two pointers have crossed.

## 27.5 Sliding Window

```python
left = 0
right = 3
size = 10

while right < size and left <= right:
    print("Window:", left, right)
    left += 1
    right += 1
```

AND combines two conditions to control the window.

## 27.6 Divisibility Problems

```python
number = 30

if number % 2 == 0 and number % 3 == 0:
    print("Divisible by both 2 and 3.")
```

This is useful in number theory and mathematical programming.

## 27.7 Important DSA Applications

| DSA Topic | Logical Operator Usage |
|---|---|
| Array Traversal | Combining index limits |
| Linear Search | Loop and condition control |
| Binary Search | Combining boundary conditions |
| Two Pointers | Checking pointer positions |
| Sliding Window | Validating window conditions |
| Number Theory | Multiple divisibility checks |
| Greedy Algorithms | Combining eligibility conditions |
| Graph Algorithms | Checking traversal conditions |
| Dynamic Programming | Combining decision conditions |
| Recursion | Checking base conditions |

---

# 28. Time and Space Complexity

Logical operators are generally efficient, but the overall cost depends on the expressions being evaluated.

## 28.1 Simple Boolean AND

Example:

```python
a = True
b = False

result = a and b
```

For simple Boolean operands, this is O(1).

## 28.2 Simple Boolean OR

Example:

```python
result = True or False
```

For simple Boolean operands, this is O(1).

## 28.3 Logical NOT

Example:

```python
result = not True
```

This is O(1) for a simple Boolean value.

## 28.4 Combined Comparisons

Example:

```python
age >= 18 and age <= 60
```

For ordinary numeric operands, both comparisons and the logical operation are generally treated as O(1).

## 28.5 Conditions Involving Function Calls

Consider:

```python
if calculate_value() > 10 and check_status():
    print("Valid")
```

The complexity depends on the functions being called.

Because AND short-circuits, `check_status()` may not execute.

## 28.6 Summary

| Operation | Typical Complexity |
|---|---|
| Boolean AND | O(1) |
| Boolean OR | O(1) |
| Boolean NOT | O(1) |
| Simple numeric condition | O(1) |
| Chained numeric condition | O(1) |
| Logical expression with function calls | Depends on called functions |

Logical operators generally require O(1) auxiliary space for simple expressions, excluding memory used by functions or other operands.

---

# 29. Interview and Viva Questions

Prepare the following questions for college practical examinations and programming interviews.

## Section A: Basic Concepts

**Q1. What are logical operators?**

Logical operators combine or reverse conditions.

**Q2. How many logical operators are available in Python?**

Three fundamental logical operators.

**Q3. Name the three logical operators.**

`and`, `or`, and `not`.

**Q4. What is the purpose of AND?**

AND combines conditions and produces a truthy result when both operands are truthy.

**Q5. What is the purpose of OR?**

OR produces a truthy result when at least one operand is truthy.

**Q6. What is the purpose of NOT?**

NOT reverses the truth value.

**Q7. What are Boolean values?**

`True` and `False`.

**Q8. What is the Boolean data type in Python?**

The `bool` data type.

**Q9. Can logical operators be combined with comparison operators?**

Yes.

**Q10. Where are logical operators used?**

They are used in conditions, loops, validation, and algorithmic expressions.

## Section B: Logical AND

**Q11. When does Boolean AND return true?**

When both operands are true.

**Q12. What is the result of `True and True`?**

`True`.

**Q13. What is the result of `True and False`?**

`False`.

**Q14. What is the result of `False and True`?**

`False`.

**Q15. What is the result of `False and False`?**

`False`.

**Q16. Can AND combine more than two conditions?**

Yes.

**Q17. Give an example of AND with comparisons.**

```python
age >= 18 and age <= 60
```

**Q18. What happens if the first operand of AND is falsy?**

Python returns that operand without evaluating the second operand.

**Q19. Where is AND used in student result programs?**

It can check whether marks and attendance requirements are both satisfied.

**Q20. Why is AND useful for range validation?**

Because both the lower-bound and upper-bound conditions must be satisfied.

## Section C: Logical OR

**Q21. When does Boolean OR return true?**

When at least one operand is true.

**Q22. What is the result of `True or False`?**

`True`.

**Q23. What is the result of `False or True`?**

`True`.

**Q24. What is the result of `False or False`?**

`False`.

**Q25. Can OR combine more than two conditions?**

Yes.

**Q26. What happens if the first operand of OR is truthy?**

Python returns that operand without evaluating the second operand.

**Q27. Where is OR useful?**

When any one of multiple alternative conditions is sufficient.

**Q28. Can OR be used to identify values outside a range?**

Yes. A value is outside the range when it is below the lower limit or above the upper limit.

**Q29. What is the result of `True or False and False`?**

`True`, because AND has higher precedence than OR.

**Q30. Does OR always return a Boolean value?**

No. It may return one of its operands.

## Section D: Logical NOT

**Q31. What is the purpose of NOT?**

It reverses the truth value of an operand.

**Q32. What is the result of `not True`?**

`False`.

**Q33. What is the result of `not False`?**

`True`.

**Q34. Is NOT a unary operator?**

Yes. It operates on one operand.

**Q35. What is the result of `not 0`?**

`True`, because zero is falsy.

**Q36. What is the result of `not "Python"`?**

`False`, because a non-empty string is truthy.

**Q37. Can NOT be used with a comparison expression?**

Yes.

**Q38. What is the result of `not (10 == 10)`?**

`False`.

**Q39. Does NOT always return a Boolean?**

Yes.

**Q40. Where is NOT used?**

It is used to reverse conditions and check whether something is absent, false, or not satisfied.

## Section E: Advanced and Practical Questions

**Q41. What is short-circuit evaluation?**

It is the behavior in which Python stops evaluating a logical expression when the result is already determined.

**Q42. What is truthy?**

A value that Python treats as true in a Boolean context.

**Q43. What is falsy?**

A value that Python treats as false in a Boolean context.

**Q44. Give examples of falsy values.**

`False`, `None`, `0`, `0.0`, empty strings, empty lists, and empty dictionaries.

**Q45. What is the precedence order of logical operators?**

`not` has higher precedence than `and`, which has higher precedence than `or`.

**Q46. What is the difference between `and` and `&`?**

`and` performs logical short-circuit evaluation, whereas `&` performs bitwise AND for integer operands and supported types.

**Q47. Can AND and OR return values other than Boolean values?**

Yes. They can return their operands.

**Q48. Why are parentheses useful in logical expressions?**

They make grouping and intended evaluation order clear.

**Q49. Where are logical operators used in DSA?**

They are used in loop conditions, index validation, searching, sliding windows, and algorithmic decisions.

**Q50. Why should logical operators be understood before learning loops?**

Loops frequently depend on conditions involving multiple expressions.

---

# 30. Practice Test

Use this section to test your understanding of logical operators.

## Part A: Predict the Output

### Question 1

```python
print(True and True)
```

### Question 2

```python
print(True and False)
```

### Question 3

```python
print(False or True)
```

### Question 4

```python
print(not True)
```

### Question 5

```python
a = 10
b = 20

print(a < 20 and b > 10)
```

### Question 6

```python
number = 15

print(number % 3 == 0 or number % 5 == 0)
```

### Question 7

```python
marks = 80
attendance = 60

print(marks >= 40 and attendance >= 75)
```

### Question 8

```python
print(not "")
```

### Question 9

```python
print("Python" or "DSA")
```

### Question 10

```python
print(False or True and False)
```

## Part B: Identify the Correct Operator

1. Both conditions must be true.
2. At least one condition must be true.
3. Reverse a Boolean result.
4. Check whether a value is not within a range.
5. Check whether a number is divisible by both 2 and 5.
6. Check whether a user is either an administrator or a teacher.
7. Check whether marks and attendance requirements are satisfied.
8. Check whether a number is positive or negative.
9. Check whether a user is not blocked.
10. Stop evaluating when the result is already determined.

## Part C: Programming Challenges

1. Check whether two numbers are positive.
2. Check whether at least one number is negative.
3. Check whether a number is between 1 and 100.
4. Check whether a student meets marks and attendance requirements.
5. Check whether a number is divisible by 2 and 3.
6. Check whether a year is a leap year.
7. Check whether a number is outside an inclusive range.
8. Check whether a user satisfies an access condition.
9. Validate three sides of a triangle.
10. Build a simple eligibility program using AND, OR, and NOT.

---

# 31. Quick Revision Notes

## Logical AND

```python
True and True
```

Result:

```text
True
```

Both operands must be truthy.

## Logical OR

```python
True or False
```

Result:

```text
True
```

At least one operand must be truthy.

## Logical NOT

```python
not True
```

Result:

```text
False
```

The truth value is reversed.

## Truth Tables

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

## Operator Precedence

```text
not
and
or
```

## Short-Circuit Rules

- AND stops when the left operand is falsy.
- OR stops when the left operand is truthy.
- NOT evaluates and reverses the truth value.

## Important Reminders

- Logical operators combine conditions.
- AND requires both operands to be truthy.
- OR requires at least one operand to be truthy.
- NOT reverses truth values.
- AND and OR can return operands.
- NOT always returns a Boolean.
- Empty containers are falsy.
- Non-empty containers are generally truthy.
- Parentheses improve readability.
- Logical operators are different from bitwise operators.

---

# 32. Important Terminology

| Term | Meaning |
|---|---|
| Logical operator | Operator used to combine or reverse conditions |
| AND | Logical operation requiring both operands to be truthy |
| OR | Logical operation requiring at least one operand to be truthy |
| NOT | Logical operation that reverses a truth value |
| Boolean | Python data type containing `True` and `False` |
| Truth table | Table showing results for possible Boolean combinations |
| Condition | Expression used to make a decision |
| Truthy | Value treated as true in a Boolean context |
| Falsy | Value treated as false in a Boolean context |
| Short-circuit | Stopping evaluation when the result is already determined |
| Operand | Value used by an operator |
| Precedence | Priority determining operator evaluation order |
| Negation | Reversing the truth value of an expression |
| Conditional statement | Statement that executes code based on a condition |
| Validation | Checking whether data satisfies specified requirements |
| Expression | Combination of values, operators, and function calls |
| Boolean logic | Reasoning based on true and false values |
| Bitwise operator | Operator that manipulates individual bits |

---

# 33. Learning Checklist

Complete this checklist after studying the topic.

## Basic Concepts

- [ ] I understand what logical operators are.
- [ ] I know the three logical operators.
- [ ] I understand Boolean values.
- [ ] I can read a logical expression.
- [ ] I can predict Boolean results.

## Logical AND

- [ ] I understand the AND operator.
- [ ] I know the AND truth table.
- [ ] I can combine two conditions using AND.
- [ ] I can combine three or more conditions using AND.
- [ ] I can use AND for range validation.

## Logical OR

- [ ] I understand the OR operator.
- [ ] I know the OR truth table.
- [ ] I can combine alternative conditions using OR.
- [ ] I can use OR to identify values outside a range.

## Logical NOT

- [ ] I understand the NOT operator.
- [ ] I know the NOT truth table.
- [ ] I can reverse comparison conditions.
- [ ] I can use NOT for validation.

## Advanced Concepts

- [ ] I understand combined logical expressions.
- [ ] I understand operator precedence.
- [ ] I understand short-circuit evaluation.
- [ ] I understand truthy and falsy values.
- [ ] I know that AND and OR can return operands.
- [ ] I understand the difference between logical and bitwise operators.

## Programming Practice

- [ ] I can check whether both numbers are positive.
- [ ] I can check whether at least one number is positive.
- [ ] I can validate a range.
- [ ] I can check student eligibility.
- [ ] I can check divisibility by multiple values.
- [ ] I can write a leap-year program.
- [ ] I can validate a triangle.
- [ ] I have practised all twelve solved problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I have completed the practice test.

---

# 34. How to Run the Python Program

Make sure Python is installed on your computer.

Open a terminal in the Logical Operators folder.

## 34.1 Run the Program

```bash
python 01_logical_operators.py
```

On systems where `python3` is used:

```bash
python3 01_logical_operators.py
```

## 34.2 Expected Main Menu

The program provides the following options:

```text
1. View 12 Logical Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

## 34.3 Recommended Usage

### Step 1: Study the Examples

Select option `1`.

Understand how AND, OR, and NOT behave with different conditions.

### Step 2: Practise Solved Problems

Select option `2`.

Choose a problem and execute it.

Try different inputs, especially combinations where one condition is false.

### Step 3: Attempt Unsolved Questions

Select option `3`.

Read all ten questions and solve them independently.

### Step 4: Review the Checklist

Select option `4`.

Identify which concepts need further revision.

### Step 5: Exit

Select option `0` when you finish.

---

# 35. Recommended Learning Sequence

Follow this sequence to understand logical operators properly.

| Order | Topic | What to Learn |
|---:|---|---|
| 1 | Boolean Values | Understand `True` and `False` |
| 2 | Logical AND | Combine conditions requiring all to be true |
| 3 | Logical OR | Combine alternative conditions |
| 4 | Logical NOT | Reverse a condition |
| 5 | Truth Tables | Understand every Boolean combination |
| 6 | Combined Conditions | Use multiple logical operators |
| 7 | Comparison Integration | Combine comparison and logical operators |
| 8 | Conditional Statements | Apply logical expressions in decisions |
| 9 | Operator Precedence | Understand evaluation order |
| 10 | Short-Circuit Evaluation | Understand skipped evaluation |
| 11 | Truthy and Falsy Values | Understand non-Boolean operands |
| 12 | Practical Problems | Solve real programming exercises |

## Before Moving to the Next Topic

Make sure that:

1. You understand all three logical operators.
2. You can reproduce their truth tables.
3. You can combine comparison and logical operators.
4. You understand short-circuit evaluation.
5. You know the precedence order.
6. You understand truthy and falsy values.
7. You can solve range and eligibility problems.
8. You have completed the twelve solved problems.
9. You have attempted the ten unsolved questions.
10. You have revised the viva questions.

---

# 36. Topic Completion Summary

In this topic, you learned how Python evaluates logical expressions using logical operators.

You covered:

- Logical AND (`and`).
- Logical OR (`or`).
- Logical NOT (`not`).
- Boolean values.
- Truth tables.
- Combining logical operators.
- Logical operators with comparisons.
- Logical operators with conditional statements.
- Operator precedence.
- Short-circuit evaluation.
- Truthy and falsy values.
- Logical operators with non-Boolean values.
- Difference between logical and bitwise operators.
- Input validation.
- Real-world applications.
- DSA applications.
- Dry runs and output prediction.
- Interview and viva questions.

Logical operators are essential for writing programs that make decisions based on multiple conditions.

You will use them frequently in conditions, loops, functions, searching, sorting, and Data Structures and Algorithms.

Do not just memorize the three operators. Practise writing conditions and predicting exactly how Python evaluates them.

**Complete the examples, execute the twelve solved problems, and attempt the ten unsolved questions before moving to the next topic.**

---

## Navigation

**Previous Topic:** [Comparison Operators](../03-Comparison-Operators/README.md)

**Next Topic:** [Bitwise Operators](../05-Bitwise-Operators/README.md)

**Parent Section:** [Operators and Expressions](../README.md)
