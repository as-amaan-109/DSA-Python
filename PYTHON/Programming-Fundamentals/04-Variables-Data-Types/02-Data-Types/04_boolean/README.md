# Python Boolean Data Type — Complete Study Notes

**Week:** 1 — Programming Fundamentals  
**Part:** Variables and Data Types  
**Topic:** Boolean Data Type  
**Code File:** `04_boolean.py`

---

# Table of Contents

1. Introduction to Boolean
2. Boolean Values
3. Boolean Data Type and `type()`
4. Comparison Operators
5. Logical Operators
6. Truth Tables
7. Truthy and Falsy Values
8. Converting Values to Boolean
9. Boolean Values and User Input
10. Conditional Statements
11. Chained Comparisons
12. Short-Circuit Evaluation
13. Operator Precedence
14. Equality and Identity
15. `all()` and `any()`
16. Boolean Values in Arithmetic
17. Boolean Expressions in Real Applications
18. Twelve Solved Problems with Logic
19. Five Unsolved Practice Problems
20. Common Errors and Mistakes
21. Best Practices
22. Quick Revision Table
23. Important Interview and Viva Questions
24. Final Learning Checklist
25. How to Run the Program

---

# 1. Introduction to Boolean

A **Boolean** is a data type that represents one of two logical values:

- `True`
- `False`

Boolean values are used when a program needs to represent a condition, decision or logical result.

For example, a program might check whether:

- A number is greater than zero.
- A student has passed an examination.
- A person meets a particular age requirement.
- A username matches an expected value.
- A number is divisible by another number.
- All required conditions are satisfied.

### Example

```python
is_student = True
has_completed_course = False

print(is_student)
print(has_completed_course)
```

Output:

```text
True
False
```

A Boolean is especially important in decision-making and control flow.

For example:

```python
age = 20

if age >= 18:
    print("The age requirement is satisfied.")
else:
    print("The age requirement is not satisfied.")
```

Output:

```text
The age requirement is satisfied.
```

The comparison `age >= 18` produces a Boolean result. Python uses that result to choose which branch to execute.

## Where are Booleans used?

Booleans are used in:

- `if`, `elif` and `while` statements
- Input validation
- Search and filtering
- Login-condition demonstrations
- Game conditions
- Eligibility checks
- Form validation
- Database filtering
- Data analysis
- Testing and debugging

---

# 2. Boolean Values

Python has two Boolean literals:

```python
True
False
```

**Important:** The first letter must be uppercase, and the remaining letters must be lowercase.

Correct:

```python
is_active = True
is_completed = False

print(is_active)
print(is_completed)
```

Output:

```text
True
False
```

Incorrect:

```python
# true = 1       # Here, "true" is treated as an ordinary variable name.
# false = 0      # Here, "false" is treated as an ordinary variable name.

# print(Truee)   # NameError unless a variable named Truee exists.
```

`True` and `False` are reserved Boolean values. Lowercase names such as `true` and `false` are not Boolean literals.

## Boolean variables

Variables that represent a condition are commonly named using descriptive terms.

```python
is_logged_in = True
has_permission = False
is_valid = True
can_continue = False

print(is_logged_in)
print(has_permission)
print(is_valid)
print(can_continue)
```

Names beginning with `is_`, `has_` or `can_` can make conditions easier to understand. They are naming conventions, not compulsory rules.

---

# 3. Boolean Data Type and `type()`

The name of Python's Boolean data type is `bool`.

```python
value1 = True
value2 = False

print(type(value1))
print(type(value2))
```

Output:

```text
<class 'bool'>
<class 'bool'>
```

You can check whether a value belongs to the Boolean type by using `isinstance()`.

```python
print(isinstance(True, bool))
print(isinstance(False, bool))
```

Output:

```text
True
True
```

## Boolean results from expressions

Boolean values are frequently created by comparisons and logical operations.

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
```

Output:

```text
True
False
True
False
```

The result of each comparison is either `True` or `False`.

---

# 4. Comparison Operators

Comparison operators compare two values and produce a Boolean result.

Consider the following variables:

```python
a = 10
b = 20
```

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `a == b` | `False` |
| `!=` | Not equal to | `a != b` | `True` |
| `>` | Greater than | `a > b` | `False` |
| `<` | Less than | `a < b` | `True` |
| `>=` | Greater than or equal to | `a >= b` | `False` |
| `<=` | Less than or equal to | `a <= b` | `True` |

## Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

Output:

```text
False
True
False
True
False
True
```

## Difference between `=` and `==`

This is one of the most important distinctions in Python.

### Assignment operator: `=`

Assignment stores a value in a variable.

```python
age = 20
```

### Equality operator: `==`

Equality compares two values.

```python
print(age == 20)
```

Output:

```text
True
```

Do not confuse assignment with comparison.

## Example: Checking a passing mark

```python
marks = 65

passed = marks >= 40

print(passed)
```

Output:

```text
True
```

The expression `marks >= 40` is evaluated to determine whether the marks meet the specified condition.

---

# 5. Logical Operators

Logical operators allow you to combine Boolean expressions.

Python provides three primary logical operators:

- `and`
- `or`
- `not`

## 5.1 The `and` operator

The `and` operator returns `True` when both operands are truthy. When used with Boolean expressions, both conditions must be true for the combined condition to be true.

### Example

```python
age = 22
has_id = True

result = age >= 18 and has_id

print(result)
```

Output:

```text
True
```

Both conditions are satisfied:

1. `age >= 18` is `True`.
2. `has_id` is `True`.

Therefore, the combined condition is true.

### Example: One condition fails

```python
age = 16
has_id = True

result = age >= 18 and has_id

print(result)
```

Output:

```text
False
```

The first condition is false, so the combined condition is false.

### Real-world-style example

```python
marks = 80
attendance = 90

eligible = marks >= 40 and attendance >= 75

print(eligible)
```

Output:

```text
True
```

The variable `eligible` is true because both numerical conditions are satisfied.

This is only an example of combining conditions, not a universal educational rule.

## 5.2 The `or` operator

The `or` operator returns `True` when at least one operand is truthy. It returns `False` only when both operands are falsy.

### Example

```python
has_email = False
has_phone = True

contact_available = has_email or has_phone

print(contact_available)
```

Output:

```text
True
```

The phone condition is true, so the combined condition is true.

### Example: Both conditions are false

```python
has_email = False
has_phone = False

print(has_email or has_phone)
```

Output:

```text
False
```

## 5.3 The `not` operator

The `not` operator returns the opposite truth value of its operand.

| Expression | Result |
|---|---|
| `not True` | `False` |
| `not False` | `True` |
| `not (10 > 5)` | `False` |
| `not (10 < 5)` | `True` |

Example:

```python
is_raining = False

print(not is_raining)
```

Output:

```text
True
```

### Example: Check that a value is not zero

```python
number = 10

is_nonzero = not (number == 0)

print(is_nonzero)
```

Output:

```text
True
```

A clearer alternative for the same condition is:

```python
print(number != 0)
```

---

# 6. Truth Tables

A truth table shows the result of a logical operation for each possible combination of Boolean inputs.

## 6.1 AND truth table

| A | B | A `and` B |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

Both conditions must be true.

## 6.2 OR truth table

| A | B | A `or` B |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

At least one condition must be true.

## 6.3 NOT truth table

| A | `not A` |
|---|---|
| `False` | `True` |
| `True` | `False` |

The `not` operator reverses the truth value.

## Example program

```python
values = [False, True]

for a in values:
    for b in values:
        print(a, "AND", b, "=", a and b)
        print(a, "OR", b, "=", a or b)

print("NOT True =", not True)
print("NOT False =", not False)
```

Study the output and compare it with the truth tables.

---

# 7. Truthy and Falsy Values

In Python, values can be evaluated in a Boolean context, such as an `if` statement.

A **falsy value** behaves as false in a Boolean context.

A **truthy value** behaves as true in a Boolean context.

The `bool()` built-in function converts a value to its truth value.

## Common falsy values

| Value | Boolean conversion |
|---|---|
| `False` | `False` |
| `None` | `False` |
| `0` | `False` |
| `0.0` | `False` |
| `""` | `False` |
| `[]` | `False` |
| `()` | `False` |
| `{}` | `False` |
| `set()` | `False` |

## Common truthy values

| Value | Boolean conversion |
|---|---|
| `True` | `True` |
| `1` | `True` |
| `-1` | `True` |
| `2.5` | `True` |
| `"Python"` | `True` |
| `"False"` | `True` |
| `"0"` | `True` |
| `[0]` | `True` |
| `(0,)` | `True` |
| `{"name": "Amaan"}` | `True` |

An important rule is that most non-empty strings and collections are truthy. Numeric zero and empty collections are falsy.

## Example 1: Using `bool()`

```python
print(bool(True))
print(bool(False))
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hello"))
```

Output:

```text
True
False
False
True
False
True
```

## Example 2: Empty and non-empty lists

```python
empty_list = []
nonempty_list = [0]

print(bool(empty_list))
print(bool(nonempty_list))
```

Output:

```text
False
True
```

The list `[0]` is non-empty, so it is truthy even though the number inside it is zero.

## Example 3: Using truthiness in conditions

```python
name = ""

if name:
    print("A name was provided.")
else:
    print("The name is empty.")
```

Output:

```text
The name is empty.
```

This approach is useful for checking whether a string or collection is empty.

---

# 8. Converting Values to Boolean

The `bool()` function returns the truth value of a given object.

## Syntax

```python
bool(value)
```

### Example 1: Numeric values

```python
print(bool(0))
print(bool(1))
print(bool(-10))
```

Output:

```text
False
True
True
```

Every non-zero numeric value is truthy, including negative values.

### Example 2: Strings

```python
print(bool(""))
print(bool("Python"))
print(bool("False"))
print(bool("0"))
```

Output:

```text
False
True
True
True
```

**Important:** `bool("False")` is `True` because `"False"` is a non-empty string. Python does not interpret the text as the Boolean literal `False`.

### Example 3: Collections

```python
print(bool([]))
print(bool([1, 2, 3]))
print(bool({}))
print(bool({"name": "Amaan"}))
```

Output:

```text
False
True
False
True
```

## Why does `bool("False")` return `True`?

The string contains five characters. It is not empty, so its truth value is true.

Compare:

```python
print(bool("False"))
print(bool(False))
```

Output:

```text
True
False
```

The first expression converts a string to its truth value. The second evaluates a Boolean literal.

### Important distinction

`bool(value)` does not generally parse words such as `"true"`, `"false"`, `"yes"` and `"no"` into their intended meanings.

When your program needs to interpret textual answers, parse them explicitly.

---

# 9. Boolean Values and User Input

The `input()` function returns a string, even when a user types `0` or `1`.

Suppose the user types:

```text
False
```

This does not automatically create a Boolean value.

```python
answer = input("Enter True or False: ")

print(answer)
print(type(answer))
```

If the user enters `False`, the type is still `str`.

## Incorrect approach

```python
answer = "False"

result = bool(answer)

print(result)
```

Output:

```text
True
```

This result may not match the user's intended answer.

## Correct approach: Parse the accepted text

```python
answer = input("Do you agree? (yes/no): ").strip().lower()

if answer in ("yes", "y", "true", "1"):
    result = True
elif answer in ("no", "n", "false", "0"):
    result = False
else:
    result = None
    print("Invalid answer.")

print("Result:", result)
```

Possible output for `no`:

```text
Result: False
```

In this example, `None` indicates that no valid Boolean result was obtained.

## Why use `.strip().lower()`?

- `strip()` removes leading and trailing whitespace.
- `lower()` normalizes letter case.
- Membership checks test against a known set of accepted values.

For example, `YES`, `Yes` and ` yes ` are all accepted by this parsing approach.

**Best practice:** Define the exact textual answers your program accepts rather than relying on `bool()` to parse user intentions.

---

# 10. Conditional Statements

Boolean expressions are commonly used with `if`, `elif` and `else`.

## 10.1 The `if` statement

An `if` statement executes a block when the condition is truthy.

```python
age = 20

if age >= 18:
    print("Age requirement satisfied.")
```

Output:

```text
Age requirement satisfied.
```

## 10.2 The `if-else` statement

An `if-else` statement chooses between two branches.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

## 10.3 The `if-elif-else` statement

Use `elif` when multiple mutually exclusive cases need to be checked.

```python
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Needs improvement")
```

Output:

```text
Grade B
```

The first condition is checked first. If it is false, Python checks the next condition.

The thresholds in this example are illustrative and not a universal grading system.

## 10.4 Conditional expressions

A conditional expression chooses between two values.

```python
age = 20

category = "Adult" if age >= 18 else "Minor"

print(category)
```

Output:

```text
Adult
```

This form can be useful for a short, simple choice. For complex conditions, a normal `if-else` statement is often easier to read.

---

# 11. Chained Comparisons

Python allows you to chain comparisons.

Instead of writing:

```python
marks >= 40 and marks <= 100
```

you can write:

```python
40 <= marks <= 100
```

Both expressions check whether `marks` is within the inclusive range from 40 through 100.

## Example

```python
marks = 75

print(40 <= marks <= 100)
print(80 <= marks <= 100)
```

Output:

```text
True
False
```

## Checking a temperature range

```python
temperature = 25

is_comfortable = 18 <= temperature <= 30

print(is_comfortable)
```

Output:

```text
True
```

The range comparison includes both endpoints.

### Common mistake

```python
# Incorrect for checking a range:
# 1 <= number <= 100
```

The expression above is actually **correct** for checking a range. A more common incorrect approach is to write:

```python
# Incorrect:
# 1 <= number >= 100
```

The second form means `number` must be at least 1 and also at least 100. It does not check whether the number is between 1 and 100.

Use:

```python
1 <= number <= 100
```

---

# 12. Short-Circuit Evaluation

Python's `and` and `or` operators use short-circuit evaluation.

This means Python can determine the result without evaluating every operand.

## 12.1 Short-circuit with `and`

For `A and B`, if `A` is falsy, Python does not need to evaluate `B` to determine the result.

```python
denominator = 0

result = denominator != 0 and 100 / denominator > 5

print(result)
```

Output:

```text
False
```

The division is not evaluated because `denominator != 0` is false.

This prevents a `ZeroDivisionError`.

## 12.2 Short-circuit with `or`

For `A or B`, if `A` is truthy, Python does not need to evaluate `B` to determine the result.

```python
result = True or (10 / 0 > 1)

print(result)
```

Output:

```text
True
```

The division is not evaluated because the first operand is already truthy.

## 12.3 Why is short-circuiting useful?

It can:

- Avoid errors in expressions whose later part is unsafe to evaluate.
- Prevent unnecessary work.
- Support safe conditional checks.
- Make combined expressions efficient.

A common pattern is:

```python
if denominator != 0 and numerator / denominator > 2:
    print("The quotient is greater than 2.")
```

The first condition ensures the denominator is not zero before the division is attempted.

**Important:** Short-circuit evaluation depends on the order of the operands. Put the guarding condition before the operation it protects.

---

# 13. Operator Precedence

Operator precedence determines which operations are evaluated first.

For common Boolean expressions, the important ordering is:

1. Parentheses
2. Comparisons
3. `not`
4. `and`
5. `or`

Use parentheses whenever they make the intended condition clearer.

## Example

```python
result = True or False and False

print(result)
```

Output:

```text
True
```

The `and` operation is evaluated before the `or` operation:

```python
result = True or (False and False)
```

Which becomes:

```python
True or False
```

The final result is `True`.

## Another example

```python
age = 20
has_id = False

result = age >= 18 and has_id

print(result)
```

Output:

```text
False
```

The age condition is true, but the `has_id` condition is false.

## Best practice

For more complicated conditions, use parentheses to communicate intent explicitly.

```python
result = (age >= 18) and (has_id is True)
```

For Boolean variables, the clearer and more idiomatic form is often simply:

```python
result = (age >= 18) and has_id
```

---

# 14. Equality and Identity

Python has two different concepts:

- Equality: `==`
- Identity: `is`

## 14.1 Equality

The `==` operator checks whether two values are equal according to the type's equality rules.

```python
first = [1, 2]
second = [1, 2]

print(first == second)
```

Output:

```text
True
```

The lists contain the same values in the same order, so they compare equal.

## 14.2 Identity

The `is` operator checks whether two references point to the same object.

```python
first = [1, 2]
second = [1, 2]
alias = first

print(first is second)
print(first is alias)
```

Output:

```text
False
True
```

The `second` list is a separate list object. The `alias` variable refers to the same object as `first`.

## 14.3 Use `is None`

A standard and recommended pattern is:

```python
value = None

if value is None:
    print("No value is available.")
```

Output:

```text
No value is available.
```

Use `is None` or `is not None` when checking specifically for `None`.

### Important distinction

Avoid using `is` as a substitute for value equality. Use `==` when comparing ordinary values and `is` when identity is what matters.

---

# 15. `all()` and `any()`

Python provides two helpful built-in functions for working with multiple conditions.

## 15.1 The `all()` function

`all(iterable)` returns `True` when every item in the iterable is truthy. It returns `False` as soon as it encounters a falsy item.

```python
values = [True, True, True]

print(all(values))
```

Output:

```text
True
```

Now consider:

```python
values = [True, False, True]

print(all(values))
```

Output:

```text
False
```

### Example: Every student has passed

```python
marks = [70, 85, 60]

all_passed = all(mark >= 40 for mark in marks)

print(all_passed)
```

Output:

```text
True
```

Each mark satisfies the condition `mark >= 40`.

## 15.2 The `any()` function

`any(iterable)` returns `True` when at least one item is truthy. It returns `False` when every item is falsy.

```python
values = [False, True, False]

print(any(values))
```

Output:

```text
True
```

### Example: At least one mark is 90 or above

```python
marks = [70, 85, 95]

has_high_score = any(mark >= 90 for mark in marks)

print(has_high_score)
```

Output:

```text
True
```

### Empty iterable behavior

```python
print(all([]))
print(any([]))
```

Output:

```text
True
False
```

`all([])` is true because there is no item that violates the condition. `any([])` is false because there is no item that satisfies it.

### When should you use these functions?

Use `all()` when every condition must hold. Use `any()` when at least one condition must hold.

They are especially useful for validation, filtering, testing and collections of data.

---

# 16. Boolean Values in Arithmetic

In Python, `bool` is a subclass of `int`.

As a result, Boolean values can participate in arithmetic operations:

- `True` behaves numerically like `1`.
- `False` behaves numerically like `0`.

## Example

```python
print(True + True)
print(True + False)
print(False + False)
print(True * 10)
```

Output:

```text
2
1
0
10
```

This is valid Python behavior.

## Boolean values and equality

```python
print(True == 1)
print(False == 0)
```

Output:

```text
True
True
```

The results can surprise beginners because Boolean and integer values are different types, even though these comparisons are true.

```python
print(type(True))
print(type(1))
```

Output:

```text
<class 'bool'>
<class 'int'>
```

**Best practice:** Do not rely on Boolean arithmetic when a direct condition, counter or integer expression would make your intention clearer.

---

# 17. Boolean Expressions in Real Applications

Boolean expressions are essential to many programming tasks.

The following examples demonstrate how multiple conditions can be combined.

## 17.1 Eligibility condition

```python
age = 20
has_permission = True

eligible = age >= 18 and has_permission

print(eligible)
```

Output:

```text
True
```

Both conditions must be satisfied.

## 17.2 Alternative contact methods

```python
has_email = False
has_phone = True

contact_available = has_email or has_phone

print(contact_available)
```

Output:

```text
True
```

At least one contact method is available.

## 17.3 Range checking

```python
marks = 75

valid_marks = 0 <= marks <= 100

print(valid_marks)
```

Output:

```text
True
```

This checks whether the marks fall within the range from 0 to 100.

## 17.4 Basic input validation

```python
username = input("Enter a username: ").strip()

is_valid = bool(username)

print("Is the username non-empty?", is_valid)
```

Output depends on the user's input.

This only checks whether the username contains non-whitespace text after trimming. It is not a complete username validation rule.

## 17.5 Combining multiple requirements

```python
marks = 85
attendance = 90
has_submitted_project = True

requirements_met = (
    marks >= 40
    and attendance >= 75
    and has_submitted_project
)

print(requirements_met)
```

Output:

```text
True
```

The final result is true only when every specified requirement is satisfied.

---

# 18. Twelve Solved Problems with Logic

The `04_boolean.py` program contains twelve selectable solved problems. Use the menu to test each solution with different inputs.

## Problem 1: Positive, Negative or Zero

**Question:** Determine whether an integer is positive, negative or zero.

Example:

```text
Input: -5
Output: The number is negative.
```

### Logic

1. Compare the number with zero.
2. If it is greater than zero, it is positive.
3. If it is less than zero, it is negative.
4. Otherwise, the number is zero.

```python
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Concepts used:** Comparison operators and conditional statements.

## Problem 2: Even or Odd

**Question:** Determine whether a number is even or odd.

Example:

```text
Input: 8
Output: The number is even.
```

### Logic

An integer is even if its remainder after division by 2 is zero.

```python
number = int(input("Enter an integer: "))

is_even = number % 2 == 0

print("Even:", is_even)
```

For `8`, the expression `8 % 2 == 0` evaluates to `True`.

**Concepts used:** Modulo operator and Boolean expressions.

## Problem 3: Basic Voting Eligibility

**Question:** Check whether the entered age and citizenship answer meet the example's eligibility conditions.

Example:

```text
Age: 20
Eligible citizen: yes
Result: True
```

### Logic

1. Read the age.
2. Read an explicit yes/no answer.
3. Check that the age is at least 18.
4. Combine the two conditions using `and`.

```python
age = int(input("Enter your age: "))
is_citizen = input("Eligible citizen? (yes/no): ").strip().lower() == "yes"

eligible = age >= 18 and is_citizen

print(eligible)
```

This is a programming exercise, not a complete statement of any jurisdiction's voting law or eligibility requirements.

**Concepts used:** Boolean input parsing and `and`.

## Problem 4: Check a Number Range

**Question:** Determine whether an integer is between 1 and 100, inclusive.

Example:

```text
Input: 50
Output: True
```

### Logic

Use a chained comparison:

```python
number = int(input("Enter an integer: "))

in_range = 1 <= number <= 100

print(in_range)
```

The result is true for 1 and 100 as well as all integers between them.

**Concepts used:** Chained comparisons.

## Problem 5: Divisible by Both 3 and 5

**Question:** Check whether an integer is divisible by both 3 and 5.

Example:

```text
Input: 30
Output: True
```

### Logic

Both remainders must equal zero.

```python
number = int(input("Enter an integer: "))

result = number % 3 == 0 and number % 5 == 0

print(result)
```

A multiple of 15 satisfies both conditions.

**Concepts used:** Modulo, equality and `and`.

## Problem 6: Largest of Two Numbers

**Question:** Find the larger of two integers, or report when they are equal.

Example:

```text
First number: 20
Second number: 15
Largest: 20
```

### Logic

1. Compare the first number with the second.
2. If the first is greater, choose it.
3. Otherwise, check whether the second is greater.
4. If neither is greater, the numbers are equal.

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > second:
    print(first)
elif second > first:
    print(second)
else:
    print("Both are equal.")
```

**Concepts used:** Comparisons and `if-elif-else`.

## Problem 7: Largest of Three Numbers

**Question:** Find the largest among three integers.

Example:

```text
Numbers: 10, 25, 15
Largest: 25
```

### Logic

Compare each candidate with the other two values.

```python
first = int(input("First number: "))
second = int(input("Second number: "))
third = int(input("Third number: "))

if first >= second and first >= third:
    largest = first
elif second >= first and second >= third:
    largest = second
else:
    largest = third

print("Largest:", largest)
```

The `>=` operators also handle equal values.

**Concepts used:** Comparison operators and `and`.

## Problem 8: Leap Year Checker

**Question:** Determine whether a year is a leap year under the Gregorian calendar rules.

A leap year is:

- Divisible by 400, or
- Divisible by 4 but not divisible by 100.

### Logic

```python
year = int(input("Enter a year: "))

is_leap_year = (
    year % 400 == 0
    or (year % 4 == 0 and year % 100 != 0)
)

print(is_leap_year)
```

Examples:

| Year | Leap year? |
|---:|---|
| 2024 | `True` |
| 1900 | `False` |
| 2000 | `True` |
| 2023 | `False` |

**Concepts used:** `and`, `or`, modulo and grouping with parentheses.

## Problem 9: Student Pass Requirements

**Question:** Check whether marks and attendance satisfy two illustrative thresholds.

Conditions:

- Marks must be at least 40.
- Attendance must be at least 75%.

### Logic

```python
marks = int(input("Enter marks out of 100: "))
attendance = int(input("Enter attendance percentage: "))

passed = marks >= 40 and attendance >= 75

print("Meets both requirements:", passed)
```

Input validation should ensure marks and attendance are in the intended range.

The thresholds are examples for practising Boolean expressions, not universal school or college regulations.

**Concepts used:** Multiple conditions and `and`.

## Problem 10: Vowel Checker

**Question:** Check whether a single alphabetic character is a vowel.

Example:

```text
Input: E
Output: True
```

### Logic

1. Read the character.
2. Check that exactly one alphabetic character was provided.
3. Normalize its case.
4. Check whether it belongs to `"aeiou"`.

```python
character = input("Enter one letter: ").strip()

if len(character) == 1 and character.isalpha():
    print(character.lower() in "aeiou")
else:
    print("Enter exactly one alphabetic character.")
```

This exercise checks the English vowels `a`, `e`, `i`, `o` and `u`.

**Concepts used:** `len()`, `isalpha()`, `lower()` and membership.

## Problem 11: Combine Username and Password Conditions

**Question:** Demonstrate a Boolean login condition that requires both the username and the password to match expected example values.

Example:

```text
Username: student
Password: python123
Login accepted: True
```

### Logic

1. Compare the entered username with the demo username.
2. Compare the entered password with the demo password.
3. Combine both comparisons using `and`.

```python
username = input("Username: ")
password = input("Password: ")

username_matches = username == "student"
password_matches = password == "python123"

can_login = username_matches and password_matches

print(can_login)
```

This example is only for learning Boolean logic. Real applications should use secure authentication, password hashing and appropriate credential-handling practices rather than hard-coded passwords.

**Concepts used:** Equality and `and`.

## Problem 12: Check Triangle Validity

**Question:** Determine whether three positive side lengths can form a triangle.

For three positive side lengths, each pair must sum to more than the remaining side.

### Logic

```python
a = int(input("First side: "))
b = int(input("Second side: "))
c = int(input("Third side: "))

valid = (
    a > 0
    and b > 0
    and c > 0
    and a + b > c
    and a + c > b
    and b + c > a
)

print("Valid triangle:", valid)
```

Example:

```text
Sides: 3, 4, 5
Valid triangle: True
```

The supplied program uses `all()` to combine the triangle inequality tests.

**Concepts used:** Comparisons, `and` and `all()`.

---

# 19. Five Unsolved Practice Problems

Try these independently before looking up solutions. Write the code in a separate practice file if necessary.

## Practice 1: Prime Number Checker

Write a program to determine whether an integer is a prime number.

Example:

```text
Input: 7
Output: True
```

Hints:

- Numbers below 2 are not prime.
- Check candidate divisors starting from 2.
- A number is not prime if it has a divisor other than 1 and itself.
- Use a Boolean variable or a loop's `else` clause to represent the result.

## Practice 2: Password Condition Checker

Write an educational password-strength checker that verifies whether a string:

- Contains at least eight characters.
- Contains at least one digit.
- Contains at least one uppercase character.
- Contains at least one lowercase character.

Combine the conditions into one Boolean result.

Example:

```text
Input: Python123
Output: Meets the listed conditions.
```

These conditions are only for practising strings and Boolean expressions. They do not constitute a complete password security policy.

## Practice 3: Right-Angled Triangle Checker

Given three positive side lengths, determine whether they form a right-angled triangle.

Hint:

- Identify the largest side.
- Check the Pythagorean relationship using squared lengths.
- Ensure the sides form a valid triangle.

For example, `3, 4, 5` forms a right-angled triangle.

## Practice 4: Check Whether a String Contains a Letter and a Digit

Write a program that checks whether the input contains both:

- At least one alphabetic character.
- At least one digit.

Example:

```text
Input: Python123
Output: True
```

Hint: Use `any()` with `isalpha()` and `isdigit()`.

## Practice 5: Grade Classifier

Write a program that takes marks and attendance and reports a grade or eligibility message based on rules you define.

Your program should:

- Validate the input range.
- Combine Boolean conditions.
- Use `if`, `elif` and `else`.
- Document the grading thresholds you selected.

Test boundary values as well as ordinary values.

---

# 20. Common Errors and Mistakes

## Mistake 1: Writing `true` instead of `True`

```python
# Incorrect as a Boolean literal:
# result = true

# Correct:
result = True
```

Python is case-sensitive.

## Mistake 2: Using `=` instead of `==`

```python
age = 20

# Comparison:
print(age == 20)
```

Use `=` to assign a value and `==` to compare values.

## Mistake 3: Thinking `bool("False")` returns `False`

```python
print(bool("False"))
```

Output:

```text
True
```

The string is non-empty. Parse known textual answers explicitly if you intend to interpret them as Boolean values.

## Mistake 4: Forgetting to combine every required condition

Incorrect:

```python
marks = 80
attendance = 50

result = marks >= 40
```

This checks the marks condition only.

Correct for a rule requiring both thresholds:

```python
result = marks >= 40 and attendance >= 75
```

## Mistake 5: Incorrect range comparisons

Incorrect:

```python
# This does not check whether number is between 1 and 100:
# number >= 1 and number >= 100
```

Correct:

```python
1 <= number <= 100
```

## Mistake 6: Confusing `and` and `or`

Use `and` when every condition must be true.

Use `or` when at least one condition must be true.

## Mistake 7: Ignoring operator precedence

For complex conditions, parentheses can clarify which expressions are meant to be evaluated together.

```python
result = (age >= 18) and (has_id or has_permission)
```

This means the age condition must be true and at least one of the other two conditions must be true.

## Mistake 8: Treating `is` as the same as `==`

Use `==` for value equality.

Use `is` when checking object identity, such as `value is None`.

## Mistake 9: Forgetting to validate numeric input

The `int()` function raises a `ValueError` for text such as `"hello"`. Use input-validation logic and exception handling when your program must handle invalid input gracefully.

---

# 21. Best Practices

1. Use `True` and `False` with the correct capitalization.
2. Give Boolean variables descriptive names such as `is_valid` or `has_permission`.
3. Use `and` for requirements that must all be satisfied.
4. Use `or` when any one of several conditions may satisfy the requirement.
5. Use parentheses to clarify complex conditions.
6. Put safe guard conditions before potentially unsafe expressions in short-circuit checks.
7. Parse textual Boolean input explicitly instead of relying on `bool()`.
8. Use `all()` and `any()` to express conditions over collections clearly.
9. Check `value is None` when testing specifically for `None`.
10. Avoid relying on Boolean arithmetic when a direct expression is more readable.
11. Validate user input before using it in calculations.
12. Test normal cases, boundary cases and invalid input.

---

# 22. Quick Revision Table

| Concept | Syntax | Purpose |
|---|---|---|
| Boolean values | `True`, `False` | Represent truth values |
| Type | `bool` | Boolean data type |
| Equality | `a == b` | Compare values for equality |
| Inequality | `a != b` | Check whether values differ |
| Greater than | `a > b` | Compare magnitude or ordering |
| Less than | `a < b` | Compare magnitude or ordering |
| AND | `a and b` | Both conditions must be true |
| OR | `a or b` | At least one condition must be true |
| NOT | `not a` | Reverse the truth value |
| Boolean conversion | `bool(value)` | Convert an object to its truth value |
| Chained comparison | `1 <= n <= 100` | Check an inclusive range |
| Conditional | `if condition:` | Execute a branch when true |
| Short-circuit AND | `a and b` | Skips `b` when `a` is falsy |
| Short-circuit OR | `a or b` | Skips `b` when `a` is truthy |
| All conditions | `all(values)` | True when all items are truthy |
| Any condition | `any(values)` | True when at least one item is truthy |
| Identity check | `value is None` | Checks whether value is `None` |
| Conditional expression | `a if condition else b` | Choose between two values |

---

# 23. Important Interview and Viva Questions

## Q1. What is a Boolean data type?

A Boolean is a data type representing logical truth values. In Python, it has two values: `True` and `False`.

## Q2. What is the name of Python's Boolean type?

Its type name is `bool`.

```python
print(type(True))
```

## Q3. What is the difference between `=` and `==`?

`=` assigns a value to a variable. `==` compares two values for equality.

## Q4. What are logical operators?

The three primary logical operators are `and`, `or` and `not`.

## Q5. What is the difference between `and` and `or`?

`and` requires both operands to be truthy to return a truthy result. `or` requires at least one operand to be truthy.

## Q6. What does `not` do?

It returns the opposite truth value of its operand.

## Q7. What is a falsy value?

A falsy value behaves as false in a Boolean context. Examples include `False`, `None`, `0`, `""`, `[]` and `{}`.

## Q8. What is a truthy value?

A truthy value behaves as true in a Boolean context. Examples include `True`, `1`, `"Python"` and `[0]`.

## Q9. Why does `bool("False")` return `True`?

Because `"False"` is a non-empty string. `bool()` evaluates the string's truth value instead of parsing the word.

## Q10. What is short-circuit evaluation?

Short-circuit evaluation allows Python to stop evaluating a logical expression when the result is already determined.

## Q11. What is the difference between `is` and `==`?

`==` compares values. `is` checks object identity.

## Q12. What is the purpose of `all()`?

`all()` returns `True` if every element in the iterable is truthy. It returns `False` if any element is falsy.

## Q13. What is the purpose of `any()`?

`any()` returns `True` if at least one element in the iterable is truthy. It returns `False` when all elements are falsy.

## Q14. Is `bool` a subclass of `int` in Python?

Yes. `bool` is a subclass of `int`, so `True` and `False` have numeric behavior corresponding to 1 and 0. However, use them primarily as logical values.

## Q15. What is a chained comparison?

A chained comparison combines multiple comparisons, such as `1 <= number <= 100`, to check a range.

## Q16. What is a conditional expression?

It selects one of two expressions based on a condition.

```python
result = "Pass" if marks >= 40 else "Fail"
```

## Q17. What is the output of `bool([])`?

It is `False` because an empty list is falsy.

## Q18. What is the output of `bool([0])`?

It is `True` because the list contains an element and is non-empty.

---

# 24. Final Learning Checklist

Before moving to the next data type, check whether you can:

- [ ] Explain Boolean values and the `bool` type.
- [ ] Use the comparison operators correctly.
- [ ] Explain the difference between `=` and `==`.
- [ ] Combine conditions using `and`, `or` and `not`.
- [ ] Read and understand truth tables.
- [ ] Identify common truthy and falsy values.
- [ ] Explain why `bool("False")` returns `True`.
- [ ] Parse yes/no input explicitly.
- [ ] Write `if`, `elif` and `else` conditions.
- [ ] Use chained comparisons.
- [ ] Explain short-circuit evaluation.
- [ ] Understand operator precedence.
- [ ] Distinguish equality from object identity.
- [ ] Use `all()` and `any()`.
- [ ] Solve the twelve supplied problems.
- [ ] Attempt all five unsolved questions.

---

# 25. How to Run the Program

Open PowerShell in the root directory of the `DSA-Python` repository.

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"

python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\04_boolean\04_boolean.py"
```

The program presents the following menu:

1. View 12 Boolean examples
2. Practice 12 solved problems
3. View 5 unsolved questions
4. View learning checklist
0. Exit

Run the Boolean examples first. Then try the solved problems with different values, including boundary cases. Finally, solve the unsolved questions independently.

---

## Final Advice

Boolean logic is one of the foundations of programming. It is used in conditionals, loops, validation, searching, algorithms and decision-making.

Do not just memorize `and`, `or` and `not`. Practise predicting the result of expressions, checking edge cases and explaining why each condition evaluates to `True` or `False`.
