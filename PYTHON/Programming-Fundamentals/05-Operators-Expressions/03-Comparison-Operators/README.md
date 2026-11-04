# Python Comparison Operators

> A complete learning guide covering equality, inequality, greater than, less than, chained comparisons, string comparisons, Boolean comparisons, and practical programming applications in Python.

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [Learning Objectives](#2-learning-objectives)
3. [What Are Comparison Operators?](#3-what-are-comparison-operators)
4. [Comparison Operator Overview](#4-comparison-operator-overview)
5. [Equal To Operator (==)](#5-equal-to-operator-)
6. [Not Equal To Operator (!=)](#6-not-equal-to-operator-)
7. [Greater Than Operator (>)](#7-greater-than-operator-)
8. [Less Than Operator (<)](#8-less-than-operator-)
9. [Greater Than or Equal To Operator (>=)](#9-greater-than-or-equal-to-operator-)
10. [Less Than or Equal To Operator (<=)](#10-less-than-or-equal-to-operator-)
11. [Comparison Operators with Different Data Types](#11-comparison-operators-with-different-data-types)
12. [String Comparison](#12-string-comparison)
13. [Lexicographical Comparison](#13-lexicographical-comparison)
14. [Chained Comparison](#14-chained-comparison)
15. [Boolean and Numeric Comparison](#15-boolean-and-numeric-comparison)
16. [Comparison Results and Boolean Values](#16-comparison-results-and-boolean-values)
17. [Difference Between Assignment and Comparison](#17-difference-between-assignment-and-comparison)
18. [Comparison Operators with Conditional Statements](#18-comparison-operators-with-conditional-statements)
19. [Understanding the Python Program](#19-understanding-the-python-program)
20. [Twelve Examples Explained](#20-twelve-examples-explained)
21. [Twelve Solved Programming Problems](#21-twelve-solved-programming-problems)
22. [Ten Unsolved Practice Questions](#22-ten-unsolved-practice-questions)
23. [Dry Run and Output Prediction](#23-dry-run-and-output-prediction)
24. [Common Programming Mistakes](#24-common-programming-mistakes)
25. [Error Handling and Input Validation](#25-error-handling-and-input-validation)
26. [Best Practices](#26-best-practices)
27. [Real-World Applications](#27-real-world-applications)
28. [Comparison Operators in DSA](#28-comparison-operators-in-dsa)
29. [Time and Space Complexity](#29-time-and-space-complexity)
30. [Interview and Viva Questions](#30-interview-and-viva-questions)
31. [Practice Test](#31-practice-test)
32. [Quick Revision Notes](#32-quick-revision-notes)
33. [Important Terminology](#33-important-terminology)
34. [Learning Checklist](#34-learning-checklist)
35. [How to Run the Python Program](#35-how-to-run-the-python-program)
36. [Recommended Learning Sequence](#36-recommended-learning-sequence)
37. [Topic Completion Summary](#37-topic-completion-summary)

---

# 1. Introduction

Comparison operators are important components of Python programming. They are used to compare two values and determine the relationship between them.

A comparison operation evaluates two operands and produces a Boolean result:

- `True`
- `False`

For example:

```python
a = 10
b = 20

print(a < b)
```

**Output:**

```text
True
```

Python compares the values of `a` and `b`.

Since `10` is less than `20`, the result is `True`.

Now consider another example:

```python
a = 50
b = 30

print(a == b)
```

**Output:**

```text
False
```

The values are different, so the equality comparison returns `False`.

Comparison operators are commonly used in:

- Decision-making programs.
- Student result systems.
- Voting eligibility checks.
- Login validation.
- Product price comparisons.
- Age verification.
- Number classification.
- Searching and sorting.
- Conditional statements.
- Data Structures and Algorithms.

## 1.1 Why Are Comparison Operators Important?

A computer program frequently needs to make decisions.

For example, consider a student result system:

1. Accept the student's marks.
2. Compare the marks with the passing criteria.
3. If the marks satisfy the condition, display PASS.
4. Otherwise, display FAIL.

The comparison operator helps the program make that decision.

Example:

```python
marks = 75

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

**Output:**

```text
PASS
```

Without comparison operators, programs would not be able to perform many common logical decisions.

## 1.2 Where Are Comparison Operators Used?

| Area | Example Usage |
|---|---|
| Basic Python | Comparing two numbers |
| Conditional statements | Checking whether a condition is true |
| Education systems | Checking pass or fail |
| Banking | Checking account limits |
| Authentication | Validating information |
| Shopping | Comparing product prices |
| Applications | Checking user eligibility |
| Searching | Finding matching values |
| Sorting | Comparing elements |
| DSA | Searching and ordering data |

---

# 2. Learning Objectives

After completing this topic, you should be able to understand and use all Python comparison operators.

## 2.1 Basic Concepts

- Understand what comparison operators are.
- Understand how comparisons work.
- Identify the six comparison operators.
- Understand Boolean results.
- Predict the results of comparison expressions.

## 2.2 Individual Comparison Operators

Learn and use:

- `==` Equal to.
- `!=` Not equal to.
- `>` Greater than.
- `<` Less than.
- `>=` Greater than or equal to.
- `<=` Less than or equal to.

## 2.3 Advanced Comparison Concepts

- Compare integer and floating-point values.
- Compare strings.
- Understand case-sensitive comparisons.
- Understand lexicographical comparison.
- Use chained comparisons.
- Compare Boolean and numeric values.
- Understand assignment versus equality comparison.

## 2.4 Programming Skills

After completing the topic, you should be able to:

1. Compare two numbers.
2. Find the greater number.
3. Find the smaller number.
4. Find the largest of three numbers.
5. Check age eligibility.
6. Check examination results.
7. Validate a numerical range.
8. Compare strings.
9. Compare string lengths.
10. Write programs using comparison operators.

---

# 3. What Are Comparison Operators?

Comparison operators are symbols used to compare two values.

They determine whether one value is equal to, different from, greater than, or less than another value.

## 3.1 General Syntax

```python
value1 comparison_operator value2
```

### Example

```python
a = 10
b = 20

result = a < b

print(result)
```

**Output:**

```text
True
```

## 3.2 Components of a Comparison

| Component | Meaning |
|---|---|
| `a` | First operand |
| `<` | Comparison operator |
| `b` | Second operand |
| `result` | Variable storing the Boolean result |

## 3.3 How Does Comparison Work?

Consider:

```python
number = 15

print(number > 10)
```

Python performs the following conceptual steps:

1. Reads the value of `number`.
2. Reads the comparison value `10`.
3. Applies the greater-than operation.
4. Evaluates whether `15` is greater than `10`.
5. Returns `True`.

## 3.4 Comparison Results

Comparison operators normally return Boolean values.

```python
print(10 == 10)
print(10 == 20)
print(20 > 10)
print(5 < 2)
```

**Output:**

```text
True
False
True
False
```

**Important:** A comparison does not directly modify the compared variables. It evaluates their relationship and produces a result.

---

# 4. Comparison Operator Overview

Python provides six fundamental comparison operators.

| Operator | Name | Meaning | Example |
|---|---|---|---|
| `==` | Equal to | Checks whether values are equal | `10 == 10` |
| `!=` | Not equal to | Checks whether values are different | `10 != 20` |
| `>` | Greater than | Checks whether the left value is greater | `20 > 10` |
| `<` | Less than | Checks whether the left value is smaller | `10 < 20` |
| `>=` | Greater than or equal to | Checks whether the left value is greater or equal | `10 >= 10` |
| `<=` | Less than or equal to | Checks whether the left value is smaller or equal | `10 <= 20` |

## 4.1 Comparison Truth Table

| Expression | Result |
|---|---|
| `10 == 10` | `True` |
| `10 == 20` | `False` |
| `10 != 20` | `True` |
| `10 != 10` | `False` |
| `20 > 10` | `True` |
| `10 > 20` | `False` |
| `10 < 20` | `True` |
| `20 < 10` | `False` |
| `10 >= 10` | `True` |
| `5 >= 10` | `False` |
| `10 <= 10` | `True` |
| `20 <= 10` | `False` |

---

# 5. Equal To Operator (==)

The equal-to operator checks whether two values are equal.

It returns:

- `True` when both values compare equal.
- `False` when the values are not equal.

## 5.1 Syntax

```python
value1 == value2
```

## 5.2 Example 1: Equal Integers

```python
a = 10
b = 10

print(a == b)
```

**Output:**

```text
True
```

**Explanation:**

Both variables contain numerically equal values.

Therefore, the equality comparison returns `True`.

## 5.3 Example 2: Different Integers

```python
a = 10
b = 20

print(a == b)
```

**Output:**

```text
False
```

The values are different.

## 5.4 Example 3: Equal Floating-Point Numbers

```python
a = 10.5
b = 10.5

print(a == b)
```

**Output:**

```text
True
```

## 5.5 Example 4: Integer and Float Comparison

```python
a = 10
b = 10.0

print(a == b)
```

**Output:**

```text
True
```

Python considers these numeric values equal.

The data types are different, but their numeric values are equal.

## 5.6 Example 5: String Equality

```python
first = "Python"
second = "Python"

print(first == second)
```

**Output:**

```text
True
```

## 5.7 Example 6: Case-Sensitive String Equality

```python
first = "Python"
second = "python"

print(first == second)
```

**Output:**

```text
False
```

The uppercase `P` and lowercase `p` are different characters.

## 5.8 Practical Example: Checking Password Text

```python
stored_password = "python123"
entered_password = "python123"

if entered_password == stored_password:
    print("Password matches.")
else:
    print("Password does not match.")
```

**Output:**

```text
Password matches.
```

This example demonstrates equality checking only. A real authentication system should use secure password storage and verification techniques rather than storing plain-text passwords.

## 5.9 Important Points

- `==` checks equality.
- It returns a Boolean result.
- It can compare compatible data types.
- Integer `10` and float `10.0` compare equal.
- String comparison is case-sensitive.
- `==` is different from assignment (`=`).

---

# 6. Not Equal To Operator (!=)

The not-equal operator checks whether two values are different.

It returns:

- `True` when values are not equal.
- `False` when values are equal.

## 6.1 Syntax

```python
value1 != value2
```

## 6.2 Example 1: Different Integers

```python
a = 10
b = 20

print(a != b)
```

**Output:**

```text
True
```

## 6.3 Example 2: Equal Integers

```python
a = 50
b = 50

print(a != b)
```

**Output:**

```text
False
```

## 6.4 Example 3: Different Strings

```python
first = "Hello"
second = "Python"

print(first != second)
```

**Output:**

```text
True
```

## 6.5 Example 4: Checking Different Values

```python
age = 22

print(age != 18)
```

**Output:**

```text
True
```

## 6.6 Practical Example: Checking Whether Two Numbers Are Different

```python
a = 100
b = 200

if a != b:
    print("Numbers are different.")
else:
    print("Numbers are equal.")
```

**Output:**

```text
Numbers are different.
```

## 6.7 Practical Example: Rejecting an Invalid Code

```python
correct_code = 1234
entered_code = 5678

if entered_code != correct_code:
    print("Incorrect code.")
else:
    print("Code matches.")
```

**Output:**

```text
Incorrect code.
```

## 6.8 Important Points

- `!=` checks whether two values are unequal.
- It returns a Boolean result.
- It can be used in conditional statements.
- It is useful for checking mismatched values.
- It is commonly used in validation.

---

# 7. Greater Than Operator (>)

The greater-than operator checks whether the left-hand value is greater than the right-hand value.

It returns:

- `True` when the left value is greater.
- `False` otherwise.

## 7.1 Syntax

```python
value1 > value2
```

## 7.2 Example 1: First Number Is Greater

```python
a = 50
b = 30

print(a > b)
```

**Output:**

```text
True
```

## 7.3 Example 2: First Number Is Smaller

```python
a = 10
b = 20

print(a > b)
```

**Output:**

```text
False
```

## 7.4 Example 3: Equal Numbers

```python
a = 25
b = 25

print(a > b)
```

**Output:**

```text
False
```

The greater-than operator does not include equality.

## 7.5 Example 4: Comparing Floating-Point Values

```python
a = 45.8
b = 42.5

print(a > b)
```

**Output:**

```text
True
```

## 7.6 Practical Example: Checking the Highest Marks

```python
student_1 = 85
student_2 = 75

if student_1 > student_2:
    print("Student 1 has higher marks.")
else:
    print("Student 1 does not have higher marks.")
```

**Output:**

```text
Student 1 has higher marks.
```

## 7.7 Practical Example: Checking Minimum Balance

```python
balance = 5000

if balance > 1000:
    print("Balance is above 1000.")
else:
    print("Balance is not above 1000.")
```

**Output:**

```text
Balance is above 1000.
```

## 7.8 Important Points

- `>` checks whether the left value is strictly greater.
- Equal values produce `False`.
- It is useful for comparing marks, prices, ages, and scores.
- It is frequently used in searching and sorting algorithms.

---

# 8. Less Than Operator (<)

The less-than operator checks whether the left-hand value is smaller than the right-hand value.

It returns:

- `True` when the left value is smaller.
- `False` otherwise.

## 8.1 Syntax

```python
value1 < value2
```

## 8.2 Example 1: First Number Is Smaller

```python
a = 15
b = 25

print(a < b)
```

**Output:**

```text
True
```

## 8.3 Example 2: First Number Is Greater

```python
a = 50
b = 30

print(a < b)
```

**Output:**

```text
False
```

## 8.4 Example 3: Equal Numbers

```python
a = 20
b = 20

print(a < b)
```

**Output:**

```text
False
```

## 8.5 Example 4: Comparing Prices

```python
price_1 = 100
price_2 = 150

print(price_1 < price_2)
```

**Output:**

```text
True
```

## 8.6 Practical Example: Checking Age

```python
age = 16

if age < 18:
    print("You are below 18 years.")
else:
    print("You are 18 years or older.")
```

**Output:**

```text
You are below 18 years.
```

## 8.7 Practical Example: Checking Available Stock

```python
stock = 5
minimum_stock = 10

if stock < minimum_stock:
    print("Stock is running low.")
else:
    print("Stock is sufficient.")
```

**Output:**

```text
Stock is running low.
```

## 8.8 Important Points

- `<` checks whether the left value is strictly smaller.
- Equal values produce `False`.
- It is useful for minimum limits and threshold checks.
- It is commonly used in loops and algorithms.

---

# 9. Greater Than or Equal To Operator (>=)

The greater-than-or-equal operator checks whether the left-hand value is greater than or equal to the right-hand value.

It returns `True` when either condition is satisfied:

1. The left value is greater.
2. Both values are equal.

## 9.1 Syntax

```python
value1 >= value2
```

## 9.2 Example 1: Greater Value

```python
a = 100
b = 50

print(a >= b)
```

**Output:**

```text
True
```

## 9.3 Example 2: Equal Values

```python
a = 100
b = 100

print(a >= b)
```

**Output:**

```text
True
```

## 9.4 Example 3: Smaller Value

```python
a = 40
b = 50

print(a >= b)
```

**Output:**

```text
False
```

## 9.5 Practical Example: Voting Eligibility

```python
age = 18

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
```

**Output:**

```text
Eligible to vote.
```

The value `18` is included because the operator checks both greater-than and equality.

## 9.6 Practical Example: Passing Marks

```python
marks = 40

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

**Output:**

```text
PASS
```

## 9.7 Practical Example: Minimum Purchase Requirement

```python
purchase_amount = 1500
minimum_amount = 1000

if purchase_amount >= minimum_amount:
    print("Minimum purchase requirement satisfied.")
else:
    print("Minimum purchase requirement not satisfied.")
```

**Output:**

```text
Minimum purchase requirement satisfied.
```

## 9.8 Important Points

- `>=` includes equality.
- It is useful for minimum eligibility requirements.
- It is commonly used in examination results.
- It helps validate age, balance, quantity, and score limits.

---

# 10. Less Than or Equal To Operator (<=)

The less-than-or-equal operator checks whether the left-hand value is smaller than or equal to the right-hand value.

It returns `True` when either condition is satisfied:

1. The left value is smaller.
2. Both values are equal.

## 10.1 Syntax

```python
value1 <= value2
```

## 10.2 Example 1: Smaller Value

```python
a = 40
b = 50

print(a <= b)
```

**Output:**

```text
True
```

## 10.3 Example 2: Equal Values

```python
a = 50
b = 50

print(a <= b)
```

**Output:**

```text
True
```

## 10.4 Example 3: Greater Value

```python
a = 60
b = 50

print(a <= b)
```

**Output:**

```text
False
```

## 10.5 Practical Example: Checking Age Limit

```python
age = 17

if age <= 18:
    print("Age is within the limit.")
else:
    print("Age is above the limit.")
```

**Output:**

```text
Age is within the limit.
```

## 10.6 Practical Example: Checking Maximum Stock

```python
stock = 80
maximum_stock = 100

if stock <= maximum_stock:
    print("Stock is within the permitted limit.")
else:
    print("Maximum stock limit exceeded.")
```

**Output:**

```text
Stock is within the permitted limit.
```

## 10.7 Important Points

- `<=` includes equality.
- It is useful for maximum limits.
- It can validate quantities and scores.
- It is commonly used in range checks.

---

# 11. Comparison Operators with Different Data Types

Python supports comparison between many compatible data types.

However, the behavior depends on the types being compared.

## 11.1 Integer Comparison

```python
a = 10
b = 20

print(a < b)
print(a == b)
```

**Output:**

```text
True
False
```

## 11.2 Float Comparison

```python
a = 10.5
b = 10.5

print(a == b)
print(a >= b)
```

**Output:**

```text
True
True
```

## 11.3 Integer and Float Comparison

```python
a = 10
b = 10.0

print(a == b)
print(a <= b)
```

**Output:**

```text
True
True
```

Python considers equal numeric values equal even when one is an integer and the other is a float.

## 11.4 String Comparison

```python
first = "Python"
second = "Java"

print(first == second)
```

**Output:**

```text
False
```

## 11.5 Boolean Comparison

```python
print(True == True)
print(True == False)
```

**Output:**

```text
True
False
```

## 11.6 Incompatible Type Comparison

For example:

```python
number = 10
text = "Python"

print(number > text)
```

In Python 3, this raises a `TypeError` because integers and strings do not have a general ordering relationship.

Use compatible values when performing ordering comparisons.

## 11.7 Floating-Point Precision

Floating-point values are represented using finite binary precision. Some decimal values cannot be represented exactly.

For example:

```python
result = 0.1 + 0.2

print(result)
print(result == 0.3)
```

The output is typically:

```text
0.30000000000000004
False
```

For approximate numerical comparisons, use `math.isclose()`.

```python
import math

result = 0.1 + 0.2

print(math.isclose(result, 0.3))
```

**Output:**

```text
True
```

**Important:** Exact equality is appropriate for many integer and string comparisons. For approximate floating-point calculations, use a suitable tolerance.

---

# 12. String Comparison

Python supports comparison operators for strings.

String comparison can be performed using:

- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`

## 12.1 String Equality

```python
first = "Python"
second = "Python"

print(first == second)
```

**Output:**

```text
True
```

## 12.2 String Inequality

```python
first = "Python"
second = "Java"

print(first != second)
```

**Output:**

```text
True
```

## 12.3 Case-Sensitive Comparison

```python
first = "Python"
second = "python"

print(first == second)
```

**Output:**

```text
False
```

The uppercase and lowercase letters are different characters.

## 12.4 Case-Insensitive Comparison

When a case-insensitive comparison is required, normalize both strings before comparing them.

```python
first = "Python"
second = "PYTHON"

print(first.lower() == second.lower())
```

**Output:**

```text
True
```

## 12.5 Important Points

- String equality compares character sequences.
- String comparisons are case-sensitive by default.
- Leading and trailing spaces are significant.
- Strings are compared lexicographically when ordering comparisons are used.
- Use `.lower()` or `.casefold()` for suitable case-insensitive comparisons.

---

# 13. Lexicographical Comparison

Lexicographical comparison means comparing strings according to the ordering of their characters.

Python compares strings using their Unicode code points.

In most everyday English examples, this behavior resembles dictionary ordering, but uppercase and lowercase characters can affect the result.

## 13.1 Example

```python
first = "Apple"
second = "Banana"

print(first < second)
```

**Output:**

```text
True
```

The first differing characters are `A` and `B`.

Their ordering makes `"Apple"` smaller than `"Banana"`.

## 13.2 Another Example

```python
first = "Cat"
second = "Car"

print(first > second)
```

**Output:**

```text
True
```

The first two characters match. The third character `t` is greater than `r`.

## 13.3 Case-Sensitive Ordering

```python
print("Apple" < "apple")
```

**Output:**

```text
True
```

The uppercase and lowercase versions have different Unicode code points.

## 13.4 Strings with Different Lengths

```python
print("App" < "Apple")
```

**Output:**

```text
True
```

When one string is a prefix of the other, the shorter string is considered smaller.

## 13.5 Practical Example: Sorting Names

```python
name_1 = "Amaan"
name_2 = "Rahul"

if name_1 < name_2:
    print(name_1, "comes first.")
else:
    print(name_2, "comes first.")
```

**Output:**

```text
Amaan comes first.
```

## 13.6 Important Points

- Python uses lexicographical ordering for string comparisons.
- Comparison is based on Unicode code points.
- Case affects the result.
- If the starting characters match, comparison continues with the next character.
- If one string is a prefix of another, the shorter one is smaller.

---

# 14. Chained Comparison

Python allows multiple comparisons to be combined into a single expression.

This is called chained comparison.

## 14.1 Syntax

```python
lower <= value <= upper
```

## 14.2 Example 1: Number Within a Range

```python
number = 15

print(10 < number < 20)
```

**Output:**

```text
True
```

The number must be greater than `10` and less than `20`.

Both conditions are satisfied.

## 14.3 Example 2: Number Outside a Range

```python
number = 25

print(10 < number < 20)
```

**Output:**

```text
False
```

## 14.4 Example 3: Inclusive Range

```python
marks = 75

print(0 <= marks <= 100)
```

**Output:**

```text
True
```

Both boundary values are included in the range.

## 14.5 Example 4: Age Validation

```python
age = 22

if 18 <= age <= 60:
    print("Age is within the permitted range.")
else:
    print("Age is outside the permitted range.")
```

**Output:**

```text
Age is within the permitted range.
```

## 14.6 Example 5: Three-Value Comparison

```python
a = 10
b = 20
c = 30

print(a < b < c)
```

**Output:**

```text
True
```

## 14.7 Equivalent Form

For ordinary comparison expressions:

```python
10 < number < 20
```

has the same Boolean result as:

```python
10 < number and number < 20
```

However, Python evaluates the middle expression only once in a chained comparison. This can matter when expressions have side effects.

## 14.8 Important Points

- Chained comparisons make range checks readable.
- They can contain more than two comparisons.
- Each comparison must satisfy the chain.
- They are useful for validating ranges.
- They avoid repeating the middle variable.

---

# 15. Boolean and Numeric Comparison

In Python, Boolean values are a subtype of integers.

Their numeric behavior is:

| Boolean | Numeric Value |
|---|---:|
| `False` | 0 |
| `True` | 1 |

## 15.1 Example: True and 1

```python
print(True == 1)
```

**Output:**

```text
True
```

## 15.2 Example: False and 0

```python
print(False == 0)
```

**Output:**

```text
True
```

## 15.3 Example: True and False

```python
print(True > False)
```

**Output:**

```text
True
```

## 15.4 Example: Boolean and Integer Comparison

```python
print(True < 2)
print(False < 1)
```

**Output:**

```text
True
True
```

## 15.5 Important Note

Although Boolean values can participate in numeric comparisons, using them as numbers should be done only when it makes the program clearer.

For normal Boolean conditions, use `True` and `False` directly.

---

# 16. Comparison Results and Boolean Values

Comparison expressions return Boolean values.

Python has two Boolean constants:

- `True`
- `False`

## 16.1 Example

```python
a = 10
b = 20

result = a < b

print(result)
print(type(result))
```

**Output:**

```text
True
<class 'bool'>
```

## 16.2 Storing a Comparison Result

```python
age = 20

eligible = age >= 18

print(eligible)
```

**Output:**

```text
True
```

The comparison result is assigned to `eligible`.

## 16.3 Using a Comparison Result Later

```python
marks = 80

passed = marks >= 40

if passed:
    print("Student passed.")
else:
    print("Student failed.")
```

**Output:**

```text
Student passed.
```

## 16.4 Important Points

- Comparison operations normally return Boolean results.
- Boolean results can be stored in variables.
- They can be used in `if`, `elif`, and `while` statements.
- They are important for program decision-making.

---

# 17. Difference Between Assignment and Comparison

One of the most common beginner mistakes is confusing `=` and `==`.

## 17.1 Assignment Operator (`=`)

It assigns a value to a variable.

```python
number = 10

print(number)
```

**Output:**

```text
10
```

## 17.2 Equality Operator (`==`)

It compares two values.

```python
number = 10

print(number == 10)
```

**Output:**

```text
True
```

## 17.3 Comparison Table

| Symbol | Name | Purpose |
|---|---|---|
| `=` | Assignment | Assign a value |
| `==` | Equality | Check whether values are equal |
| `!=` | Inequality | Check whether values are different |

## 17.4 Common Mistake

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

**Remember:** `=` is used for assignment statements. `==` is used for equality comparisons.

---

# 18. Comparison Operators with Conditional Statements

Comparison operators are often used with conditional statements to make decisions.

## 18.1 Using `if`

```python
age = 20

if age >= 18:
    print("Eligible")
```

**Output:**

```text
Eligible
```

## 18.2 Using `if-else`

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Not positive")
```

**Output:**

```text
Positive
```

## 18.3 Using `if-elif-else`

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Output:**

```text
Zero
```

## 18.4 Combining Multiple Comparisons

```python
age = 25
income = 50000

if age >= 18 and income >= 25000:
    print("Both requirements satisfied.")
else:
    print("Requirements not satisfied.")
```

**Output:**

```text
Both requirements satisfied.
```

The `and` operator shown here combines comparison results. Logical operators will be covered in the next topic.

## 18.5 Why Are Comparison Operators Important in Conditions?

They help programs decide:

- Whether a student passes.
- Whether a user is eligible.
- Whether an amount is within a limit.
- Whether a number is positive.
- Whether a product is affordable.
- Whether a loop should continue.

---

# 19. Understanding the Python Program

**File Name:** `01_comparison_operators.py`

The Python program is organized into multiple sections to make learning and practice easier.

## 19.1 Module Documentation

The program starts with a module-level docstring.

It describes:

- The topic name.
- The six comparison operators.
- The purpose of the file.
- The learning sections.
- The menu options.

This documentation helps developers understand the purpose of the Python file.

## 19.2 Import Section

The program imports:

```python
import math
```

The `math` module provides mathematical functions.

This program uses `math.isfinite()` to validate floating-point input.

It rejects non-finite values such as infinity and NaN.

## 19.3 Helper Functions

The program defines four helper functions.

| Function | Purpose |
|---|---|
| `print_heading()` | Displays formatted section headings. |
| `read_int()` | Reads a valid integer. |
| `read_float()` | Reads a finite floating-point number. |
| `read_text()` | Reads non-empty text. |

### Why Are Helper Functions Useful?

They:

1. Reduce repeated code.
2. Improve readability.
3. Make input validation reusable.
4. Separate input handling from calculations.
5. Make programs easier to maintain.

## 19.4 Section 1: Twelve Examples

The first section demonstrates the following concepts:

| No. | Example | Concept |
|---:|---|---|
| 1 | Equal to | `==` |
| 2 | Not equal to | `!=` |
| 3 | Greater than | `>` |
| 4 | Less than | `<` |
| 5 | Greater than or equal to | `>=` |
| 6 | Less than or equal to | `<=` |
| 7 | Integer and float comparison | Numeric comparison |
| 8 | String equality | String comparison |
| 9 | String ordering | Lexicographical comparison |
| 10 | Chained comparison | Multiple comparisons |
| 11 | Boolean and numeric comparison | Boolean comparison |
| 12 | Comparison with conditional result | `if-else` |

## 19.5 Section 2: Twelve Solved Problems

This section contains twelve practical programs.

Each problem accepts user input when needed, performs a comparison, and displays a result.

## 19.6 `SOLVED_PROBLEMS` Dictionary

The program uses a dictionary named:

```python
SOLVED_PROBLEMS
```

It associates each problem number with:

- Its problem description.
- Its corresponding function.

This makes the solved-problem section easier to manage.

## 19.7 `show_solved_problems()`

This function displays all twelve solved problem descriptions.

It helps the user identify a problem before executing it.

## 19.8 `run_solved_problems()`

This function:

1. Displays the problem list.
2. Accepts the problem number.
3. Checks whether the selection is valid.
4. Runs the corresponding function.
5. Allows the user to return to the menu.

## 19.9 Section 3: Ten Unsolved Questions

This section displays ten questions for independent practice.

Each question also includes a small hint.

The objective is to help students practise comparison logic independently.

## 19.10 Section 4: Learning Checklist

The checklist contains important concepts from the topic.

Students can review it after practising the examples and solved questions.

## 19.11 Section 5: Main Menu

The main menu connects all the program sections.

| Option | Action |
|---:|---|
| 1 | View twelve examples |
| 2 | Practise twelve solved problems |
| 3 | View ten unsolved questions |
| 4 | View learning checklist |
| 0 | Exit |

The main menu continues until the user selects `0`.

---

# 20. Twelve Examples Explained

This section explains all twelve examples included in `01_comparison_operators.py`.

## Example 1: Equal To (`==`)

**Purpose:** Check whether two values are equal.

```python
a = 10
b = 10

print(a == b)
```

**Output:**

```text
True
```

Both values are equal.

## Example 2: Not Equal To (`!=`)

**Purpose:** Check whether two values are different.

```python
a = 10
b = 20

print(a != b)
```

**Output:**

```text
True
```

The values are different.

## Example 3: Greater Than (`>`)

**Purpose:** Check whether the first value is greater.

```python
a = 50
b = 30

print(a > b)
```

**Output:**

```text
True
```

## Example 4: Less Than (`<`)

**Purpose:** Check whether the first value is smaller.

```python
a = 15
b = 25

print(a < b)
```

**Output:**

```text
True
```

## Example 5: Greater Than or Equal To (`>=`)

**Purpose:** Check whether the first value is greater or equal.

```python
a = 100
b = 100

print(a >= b)
```

**Output:**

```text
True
```

## Example 6: Less Than or Equal To (`<=`)

**Purpose:** Check whether the first value is smaller or equal.

```python
a = 40
b = 50

print(a <= b)
```

**Output:**

```text
True
```

## Example 7: Integer and Float Comparison

**Purpose:** Understand numeric comparisons between integer and float values.

```python
a = 10
b = 10.0

print(a == b)
print(a >= b)
```

**Output:**

```text
True
True
```

## Example 8: String Equality

**Purpose:** Compare strings for exact equality.

```python
first = "Python"
second = "Python"
third = "python"

print(first == second)
print(first == third)
```

**Output:**

```text
True
False
```

## Example 9: String Lexicographical Comparison

**Purpose:** Understand string ordering.

```python
first = "Apple"
second = "Banana"

print(first < second)
```

**Output:**

```text
True
```

## Example 10: Chained Comparison

**Purpose:** Check whether a value is between two limits.

```python
number = 15

print(10 < number < 20)
print(5 < number < 10)
```

**Output:**

```text
True
False
```

## Example 11: Boolean and Numeric Comparison

**Purpose:** Understand Boolean values in numeric comparisons.

```python
print(True == 1)
print(False == 0)
print(True > False)
```

**Output:**

```text
True
True
True
```

## Example 12: Comparison and Conditional Result

**Purpose:** Use a comparison inside an `if-else` statement.

```python
marks = 75

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
```

**Output:**

```text
Result: PASS
```

---

# 21. Twelve Solved Programming Problems

The following problems correspond to the solved-problem functions in the Python file.

Each problem includes:

1. Problem statement.
2. Required operator.
3. Logic.
4. Example code.
5. Expected output.
6. Explanation.
7. Learning point.

---

## Problem 1: Check Whether Two Numbers Are Equal

**Concept:** Equal to (`==`)

### Problem Statement

Write a program that accepts two numbers and checks whether they are equal.

### Logic

1. Accept the first number.
2. Accept the second number.
3. Compare both using `==`.
4. Display the appropriate message.

### Example Code

```python
a = 10
b = 10

if a == b:
    print("Both numbers are equal.")
else:
    print("Both numbers are not equal.")
```

### Output

```text
Both numbers are equal.
```

### Explanation

Both values are `10`.

The comparison `a == b` returns `True`.

Therefore, the first message is displayed.

### Learning Point

The equality operator is useful for checking whether two values match.

---

## Problem 2: Check Whether Two Numbers Are Different

**Concept:** Not equal to (`!=`)

### Problem Statement

Accept two numbers and determine whether they are different.

### Logic

1. Accept two numbers.
2. Apply `!=`.
3. Display whether the values are different or equal.

### Example Code

```python
a = 10
b = 20

if a != b:
    print("Both numbers are different.")
else:
    print("Both numbers are equal.")
```

### Output

```text
Both numbers are different.
```

### Explanation

Since `10` and `20` are different, the comparison returns `True`.

### Learning Point

The not-equal operator is useful for identifying mismatches.

---

## Problem 3: Find the Greater Number

**Concept:** Greater than (`>`)

### Problem Statement

Accept two numbers and find which one is greater.

### Logic

1. Read two numbers.
2. Compare the first number with the second.
3. Compare the second number with the first.
4. Handle the case where both are equal.

### Example Code

```python
a = 50
b = 30

if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal.")
```

### Output

```text
Greater number: 50
```

### Dry Run

| Condition | Result |
|---|---|
| `50 > 30` | `True` |
| First branch executes | Yes |

### Learning Point

Comparison operators are useful for selecting the greater value.

---

## Problem 4: Find the Smaller Number

**Concept:** Less than (`<`)

### Problem Statement

Accept two numbers and find the smaller one.

### Example Code

```python
a = 15
b = 25

if a < b:
    print("Smaller number:", a)
elif b < a:
    print("Smaller number:", b)
else:
    print("Both numbers are equal.")
```

### Output

```text
Smaller number: 15
```

### Explanation

The expression `15 < 25` returns `True`.

Therefore, the smaller number is `15`.

### Learning Point

The less-than operator is useful for minimum-value comparisons.

---

## Problem 5: Check Voting Eligibility

**Concept:** Greater than or equal to (`>=`)

### Problem Statement

Write a program that checks whether a person is eligible to vote based on age.

For this exercise, the minimum age is `18`.

### Logic

1. Accept the person's age.
2. Compare it with `18`.
3. If age is greater than or equal to `18`, display eligible.
4. Otherwise, display not eligible.

### Example Code

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

### Learning Point

The `>=` operator includes the boundary value.

---

## Problem 6: Check Pass or Fail

**Concept:** Greater than or equal to (`>=`)

### Problem Statement

Accept student marks and check whether the student has passed.

For this exercise:

- Minimum passing marks: `40`.
- Valid marks: `0` to `100`.

### Example Code

```python
marks = 75

if 0 <= marks <= 100:
    if marks >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")
else:
    print("Invalid marks!")
```

### Output

```text
Result: PASS
```

### Dry Run

| Condition | Result |
|---|---|
| `0 <= 75 <= 100` | `True` |
| `75 >= 40` | `True` |
| Final result | PASS |

### Learning Point

Range validation and comparison are frequently used together.

---

## Problem 7: Check Whether a Number Is in a Range

**Concept:** Chained comparison

### Problem Statement

Accept a number and two limits. Check whether the number falls within the given range.

### Example Code

```python
number = 15
lower = 10
upper = 20

if lower > upper:
    print("Invalid range.")
elif lower <= number <= upper:
    print("The number is within the range.")
else:
    print("The number is outside the range.")
```

### Output

```text
The number is within the range.
```

### Explanation

The comparison is:

```python
10 <= 15 <= 20
```

Both conditions are satisfied.

### Learning Point

Chained comparison is useful for range validation.

---

## Problem 8: Check Positive, Negative or Zero

**Concept:** `>`, `<`, and equality

### Problem Statement

Accept a number and determine whether it is positive, negative, or zero.

### Example Code

```python
number = -5

if number > 0:
    print("The number is POSITIVE.")
elif number < 0:
    print("The number is NEGATIVE.")
else:
    print("The number is ZERO.")
```

### Output

```text
The number is NEGATIVE.
```

### Explanation

- If the value is greater than zero, it is positive.
- If it is less than zero, it is negative.
- Otherwise, it is zero.

### Learning Point

Multiple comparisons can classify values into different categories.

---

## Problem 9: Find the Largest of Three Numbers

**Concept:** Greater than or equal to (`>=`)

### Problem Statement

Accept three numbers and find the largest value.

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

The program checks whether each candidate is greater than or equal to the other two values.

The variable `largest` receives the selected result.

### Learning Point

Comparisons are essential for maximum and minimum problems.

---

## Problem 10: Compare Two Strings

**Concept:** String equality (`==`)

### Problem Statement

Accept two strings and check whether they are exactly equal.

### Example Code

```python
first = "Python"
second = "Python"

if first == second:
    print("Both strings are exactly equal.")
else:
    print("Both strings are different.")
```

### Output

```text
Both strings are exactly equal.
```

### Explanation

Python compares the character sequences of the strings.

The two strings match exactly, so the comparison returns `True`.

### Learning Point

String comparisons are case-sensitive by default.

---

## Problem 11: Compare the Length of Two Strings

**Concept:** Greater than (`>`) and less than (`<`)

### Problem Statement

Accept two strings and determine which string contains more characters.

### Example Code

```python
first = "Python"
second = "Java"

first_length = len(first)
second_length = len(second)

if first_length > second_length:
    print("First string is longer.")
elif first_length < second_length:
    print("Second string is longer.")
else:
    print("Both strings have equal length.")
```

### Output

```text
First string is longer.
```

### Explanation

```text
Length of Python = 6
Length of Java = 4
```

Since `6 > 4`, the first string is longer.

### Learning Point

Comparison operators can compare the results returned by functions.

---

## Problem 12: Compare Two Product Prices

**Concept:** `<` and `>`

### Problem Statement

Accept the prices of two products and identify the cheaper product.

### Example Code

```python
price_1 = 500
price_2 = 750

if price_1 < 0 or price_2 < 0:
    print("Invalid product price.")
elif price_1 < price_2:
    print("First product is cheaper.")
elif price_1 > price_2:
    print("Second product is cheaper.")
else:
    print("Both products have the same price.")
```

### Output

```text
First product is cheaper.
```

### Explanation

The first price is `500`.

The second price is `750`.

Since `500 < 750`, the first product is cheaper.

### Learning Point

Comparison operators are useful for product selection and price analysis.

---

# 22. Ten Unsolved Practice Questions

Solve the following questions independently.

Try writing the Python code before looking at any solution.

## Question 1: Check Whether Two Numbers Are Equal

**Operator:** `==`

Write a program that:

1. Accepts two numbers.
2. Compares them.
3. Displays whether they are equal.

**Hint:** Use the equality operator.

## Question 2: Check Whether Two Numbers Are Different

**Operator:** `!=`

Write a program that accepts two numbers and checks whether they are different.

**Hint:** Use the not-equal operator.

## Question 3: Find the Greater of Two Numbers

**Operator:** `>`

Write a program that accepts two numbers and displays the greater number.

Also handle the case where both values are equal.

**Hint:** Use `if-elif-else`.

## Question 4: Find the Smaller of Two Numbers

**Operator:** `<`

Write a program that accepts two numbers and finds the smaller number.

Also handle equal values.

**Hint:** Use the less-than operator.

## Question 5: Check Voting Eligibility

**Operator:** `>=`

Write a program that accepts a person's age.

Display whether the person is eligible to vote.

Use `18` as the exercise's minimum age.

**Hint:** Check whether `age >= 18`.

## Question 6: Check Student Result

**Operator:** `>=`

Write a program that accepts marks between `0` and `100`.

Display PASS if marks are at least `40`, otherwise display FAIL.

**Hint:** Validate the range before checking passing marks.

## Question 7: Check a Number Within a Range

**Concept:** Chained comparison

Accept a number, lower limit, and upper limit.

Check whether the number is within the inclusive range.

**Hint:** Use:

```python
lower <= number <= upper
```

## Question 8: Classify a Number

**Operators:** `>`, `<`, `==`

Accept a number and identify whether it is positive, negative, or zero.

**Hint:** Use three conditions.

## Question 9: Find the Largest of Three Numbers

**Operator:** `>=`

Accept three numbers and find the largest.

Handle cases where two or all three values are equal.

**Hint:** Compare each number against the other two.

## Question 10: Compare Two Strings Lexicographically

**Operators:** `<` and `>`

Accept two strings and determine which one comes first according to Python's string ordering.

Also display a message when both strings are equal.

**Hint:** Use string comparison operators.

---

# 23. Dry Run and Output Prediction

Dry running means manually tracing the execution of a program and predicting its result.

It is an important skill for practical examinations, debugging, and coding interviews.

## Question 1

Predict the output:

```python
a = 10
b = 20

print(a == b)
print(a != b)
```

### Dry Run

| Expression | Result |
|---|---|
| `10 == 20` | `False` |
| `10 != 20` | `True` |

**Answer:**

```text
False
True
```

## Question 2

Predict the output:

```python
a = 50
b = 30

print(a > b)
print(a < b)
```

**Answer:**

```text
True
False
```

## Question 3

Predict the output:

```python
number = 15

print(10 < number < 20)
print(20 < number < 30)
```

**Answer:**

```text
True
False
```

## Question 4

Predict the output:

```python
a = 10
b = 10.0

print(a == b)
print(a != b)
```

**Answer:**

```text
True
False
```

## Question 5

Predict the output:

```python
first = "Python"
second = "python"

print(first == second)
print(first != second)
```

**Answer:**

```text
False
True
```

## Question 6

Predict the output:

```python
marks = 40

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

**Answer:**

```text
PASS
```

## Question 7

Predict the output:

```python
number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Answer:**

```text
Negative
```

## Question 8

Predict the output:

```python
a = 10
b = 20
c = 30

print(a < b < c)
```

**Answer:**

```text
True
```

## Question 9

Predict the output:

```python
print(True == 1)
print(False == 0)
print(True > False)
```

**Answer:**

```text
True
True
True
```

## Question 10

Predict the output:

```python
a = 100
b = 100
c = 100

print(a >= b)
print(b <= c)
print(a != c)
```

**Answer:**

```text
True
True
False
```

---

# 24. Common Programming Mistakes

Understanding common mistakes helps you write better Python programs.

## Mistake 1: Using `=` Instead of `==`

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

`=` is assignment. `==` is equality comparison.

## Mistake 2: Forgetting the Equal Case

Incorrect:

```python
a = 10
b = 10

if a > b:
    print(a)
else:
    print(b)
```

This code does display a maximum, but it does not identify when both numbers are equal.

A clearer version:

```python
if a > b:
    print("A is greater.")
elif b > a:
    print("B is greater.")
else:
    print("Both are equal.")
```

## Mistake 3: Using Incorrect Boundary Conditions

Suppose the minimum passing mark is `40`.

Incorrect:

```python
if marks > 40:
    print("PASS")
```

This excludes a score of exactly `40`.

Correct:

```python
if marks >= 40:
    print("PASS")
```

Use the operator that matches the requirement.

## Mistake 4: Ignoring String Case

```python
print("Python" == "python")
```

Output:

```text
False
```

Use normalization if a case-insensitive comparison is required.

## Mistake 5: Comparing Incompatible Types

Incorrect:

```python
age = "22"

print(age > 18)
```

This raises a `TypeError`.

Correct:

```python
age = int("22")

print(age > 18)
```

Output:

```text
True
```

## Mistake 6: Incorrect Range Check

Incorrect:

```python
if number >= 10 or number <= 20:
    print("Within range")
```

This condition is true for almost every numeric value because either side will normally be satisfied.

Correct:

```python
if 10 <= number <= 20:
    print("Within range")
```

## Mistake 7: Floating-Point Equality Assumption

Incorrect for approximate calculations:

```python
print(0.1 + 0.2 == 0.3)
```

Output:

```text
False
```

Use `math.isclose()` when approximate equality is required.

## Mistake 8: Forgetting That Equality Is Included

Remember:

```python
10 >= 10
```

returns `True`.

Similarly:

```python
10 <= 10
```

also returns `True`.

## Mistake 9: Confusing String Length and String Value

These are different comparisons:

```python
first == second
```

checks string equality.

```python
len(first) == len(second)
```

checks whether string lengths are equal.

## Mistake 10: Reversing Comparison Direction

```python
10 > 20
```

is `False`.

```python
10 < 20
```

is `True`.

Always check which value is on the left and which is on the right.

---

# 25. Error Handling and Input Validation

Input validation ensures that a program receives acceptable data before making decisions.

## 25.1 Handling Invalid Integer Input

```python
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("Please enter a valid integer.")
```

If the user enters invalid text, Python raises a `ValueError`.

## 25.2 Validating Age

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 18:
    print("Eligible.")
else:
    print("Not eligible.")
```

## 25.3 Validating Marks

```python
marks = float(input("Enter marks: "))

if 0 <= marks <= 100:
    if marks >= 40:
        print("PASS")
    else:
        print("FAIL")
else:
    print("Invalid marks.")
```

## 25.4 Validating a Price

```python
price = float(input("Enter product price: "))

if price >= 0:
    print("Valid price.")
else:
    print("Price cannot be negative.")
```

## 25.5 Validating a Range

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

## 25.6 Why Is Validation Important?

Input validation:

- Prevents invalid application data.
- Helps avoid unexpected results.
- Improves reliability.
- Makes program behavior easier to understand.
- Helps handle user mistakes.

---

# 26. Best Practices

Follow these practices when writing programs with comparison operators.

1. Use meaningful variable names.
2. Use `==` for equality checks.
3. Use `!=` for inequality checks.
4. Choose `>=` when the boundary value must be included.
5. Choose `<=` when the maximum boundary must be included.
6. Validate user input before comparison.
7. Ensure that values have compatible data types.
8. Use chained comparisons for readable range checks.
9. Handle equal values when finding minimum or maximum numbers.
10. Remember that string comparisons are case-sensitive.
11. Use `math.isclose()` when approximate floating-point equality is required.
12. Keep conditions simple and readable.
13. Avoid unnecessary nested conditions.
14. Test boundary values.
15. Practise dry runs to understand Boolean results.

---

# 27. Real-World Applications

Comparison operators are used in almost every software application.

## 27.1 Student Result Systems

```python
marks = 75

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

Output:

```text
PASS
```

Application:

- Passing marks.
- Grade eligibility.
- Scholarship criteria.
- Exam qualification.

## 27.2 Voting Eligibility

```python
age = 20

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible.")
```

Output:

```text
Eligible to vote.
```

This is a programming exercise using an assumed minimum age of 18.

## 27.3 Shopping Applications

```python
price_1 = 500
price_2 = 700

if price_1 < price_2:
    print("First product is cheaper.")
else:
    print("First product is not cheaper.")
```

Output:

```text
First product is cheaper.
```

## 27.4 Banking Applications

```python
balance = 5000
minimum_balance = 1000

if balance >= minimum_balance:
    print("Minimum balance maintained.")
else:
    print("Balance is below minimum.")
```

Output:

```text
Minimum balance maintained.
```

## 27.5 Attendance Systems

```python
attendance = 80
required_attendance = 75

if attendance >= required_attendance:
    print("Attendance requirement satisfied.")
else:
    print("Attendance requirement not satisfied.")
```

Output:

```text
Attendance requirement satisfied.
```

## 27.6 Game Development

```python
health = 20

if health <= 0:
    print("Game Over")
else:
    print("Player is alive.")
```

Output:

```text
Player is alive.
```

## 27.7 Inventory Management

```python
stock = 5
minimum_stock = 10

if stock < minimum_stock:
    print("Restocking required.")
else:
    print("Stock is sufficient.")
```

Output:

```text
Restocking required.
```

---

# 28. Comparison Operators in DSA

Comparison operators are among the most frequently used operators in Data Structures and Algorithms.

They help determine relationships between values and control algorithm execution.

## 28.1 Finding the Maximum Element

```python
numbers = [10, 50, 20, 40]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum:", maximum)
```

**Output:**

```text
Maximum: 50
```

Comparison operators help identify the largest element.

## 28.2 Finding the Minimum Element

```python
numbers = [10, 50, 20, 40]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Minimum:", minimum)
```

**Output:**

```text
Minimum: 10
```

## 28.3 Linear Search

```python
numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for number in numbers:
    if number == target:
        found = True
        break

print(found)
```

**Output:**

```text
True
```

Equality comparison helps identify the target value.

## 28.4 Sorting

Sorting algorithms use comparisons to determine the order of elements.

Example:

```python
a = 20
b = 10

if a > b:
    a, b = b, a

print(a, b)
```

**Output:**

```text
10 20
```

## 28.5 Two-Pointer Technique

```python
left = 0
right = 5

while left < right:
    print(left, right)
    left += 1
    right -= 1
```

Comparison checks whether the two pointers have crossed.

## 28.6 Binary Search

Binary search uses comparisons to decide whether to search the left or right half of a sorted array.

The central comparison is:

```python
if target == middle_value:
    ...
elif target < middle_value:
    ...
else:
    ...
```

## 28.7 Important DSA Applications

| DSA Topic | Comparison Usage |
|---|---|
| Linear Search | Check equality |
| Binary Search | Compare target and middle |
| Bubble Sort | Compare adjacent elements |
| Selection Sort | Find minimum |
| Two Pointers | Compare pointer positions |
| Sliding Window | Compare current limits |
| Greedy Algorithms | Compare candidate values |
| Trees | Compare node values |
| Heaps | Maintain parent-child ordering |
| Dynamic Programming | Compare alternative results |

---

# 29. Time and Space Complexity

Comparison operations are generally efficient, but their cost depends on the operand type and size.

## 29.1 Numeric Comparisons

Examples:

```python
a == b
a > b
a < b
```

For ordinary fixed-size numeric reasoning, these are commonly treated as O(1).

Python integers can grow arbitrarily large, so comparisons involving extremely large integers depend on their size.

## 29.2 String Comparisons

String comparison may examine characters until it finds a difference or reaches the end of one string.

For strings of lengths `n` and `m`, the worst-case comparison time is O(min(n, m)).

Example:

```python
first = "Python"
second = "PyTorch"

print(first == second)
```

The comparison examines characters until a mismatch is found.

## 29.3 Chained Comparisons

Example:

```python
10 <= number <= 100
```

This performs two comparisons, so for ordinary numeric operands it is generally treated as O(1).

## 29.4 Finding the Largest Element

Finding the maximum in a list of `n` elements requires one scan.

Time complexity:

```text
O(n)
```

Auxiliary space complexity:

```text
O(1)
```

## 29.5 Linear Search

Searching for an element in a list of `n` values:

- Best case: O(1).
- Worst case: O(n).
- Auxiliary space: O(1) for an iterative implementation.

## 29.6 Complexity Summary

| Operation | Typical Complexity |
|---|---|
| Numeric comparison | Usually O(1) |
| String comparison | Up to O(min(n, m)) |
| Chained numeric comparison | O(1) |
| Finding maximum in a list | O(n) |
| Finding minimum in a list | O(n) |
| Linear search | O(n) worst case |
| Binary search | O(log n) |

---

# 30. Interview and Viva Questions

Prepare these questions for college practical examinations and technical interviews.

## Section A: Basic Concepts

**Q1. What are comparison operators?**

Comparison operators are used to compare two values and return a Boolean result.

**Q2. How many fundamental comparison operators are available in Python?**

Python has six fundamental comparison operators.

**Q3. Name all six comparison operators.**

`==`, `!=`, `>`, `<`, `>=`, and `<=`.

**Q4. What is the purpose of `==`?**

It checks whether two values are equal.

**Q5. What is the purpose of `!=`?**

It checks whether two values are different.

**Q6. What does the greater-than operator do?**

It checks whether the left value is strictly greater than the right value.

**Q7. What does the less-than operator do?**

It checks whether the left value is strictly smaller than the right value.

**Q8. What is the purpose of `>=`?**

It checks whether the left value is greater than or equal to the right value.

**Q9. What is the purpose of `<=`?**

It checks whether the left value is smaller than or equal to the right value.

**Q10. What type of result do comparison operators generally return?**

A Boolean result: `True` or `False`.

## Section B: Individual Operators

**Q11. What is the result of `10 == 10`?**

`True`.

**Q12. What is the result of `10 != 20`?**

`True`.

**Q13. What is the result of `20 > 10`?**

`True`.

**Q14. What is the result of `10 < 20`?**

`True`.

**Q15. What is the result of `10 >= 10`?**

`True`.

**Q16. What is the result of `10 <= 10`?**

`True`.

**Q17. Does `>` include equality?**

No.

**Q18. Does `>=` include equality?**

Yes.

**Q19. Does `<` include equality?**

No.

**Q20. Does `<=` include equality?**

Yes.

## Section C: String Comparisons

**Q21. Can strings be compared in Python?**

Yes. Python supports string equality and lexicographical comparison.

**Q22. Are string comparisons case-sensitive by default?**

Yes.

**Q23. What is the result of `"Python" == "python"`?**

`False`.

**Q24. What is lexicographical comparison?**

It compares strings according to the ordering of their characters.

**Q25. How can strings be compared without considering case?**

Normalize them using methods such as `.lower()` or `.casefold()` before comparison.

**Q26. What happens when one string is a prefix of another?**

The shorter string is considered smaller.

**Q27. What is the result of `"App" < "Apple"`?**

`True`.

**Q28. How does Python compare string characters?**

Using their Unicode code points.

**Q29. Can string equality and string length equality mean different things?**

Yes. Strings can have different contents but equal lengths.

**Q30. How do you compare the lengths of two strings?**

Use `len(first) == len(second)` or another suitable comparison.

## Section D: Chained and Boolean Comparisons

**Q31. What is chained comparison?**

It combines multiple comparisons in one expression.

**Q32. Give an example of chained comparison.**

```python
10 < number < 20
```

**Q33. How can you check whether a value lies between 0 and 100 inclusively?**

```python
0 <= number <= 100
```

**Q34. What is the result of `True == 1`?**

`True`.

**Q35. What is the result of `False == 0`?**

`True`.

**Q36. What is the numeric value of `True` in Python?**

`1`.

**Q37. What is the numeric value of `False` in Python?**

`0`.

**Q38. What is the result of `True > False`?**

`True`.

**Q39. Can comparison results be stored in variables?**

Yes. Comparison expressions return Boolean values that can be assigned to variables.

**Q40. Can comparison operators be used in conditions?**

Yes. They are commonly used with `if`, `elif`, and `while`.

## Section E: Practical and Advanced Questions

**Q41. What is the difference between `=` and `==`?**

`=` is used for assignment, while `==` checks equality.

**Q42. What error can occur when ordering an integer against a string?**

Python may raise a `TypeError`.

**Q43. Why can `0.1 + 0.2 == 0.3` return `False`?**

Because floating-point values may not be represented exactly in binary.

**Q44. What function is useful for approximate floating-point comparison?**

`math.isclose()`.

**Q45. Where are comparison operators used in DSA?**

They are used in searching, sorting, maximum and minimum calculations, and pointer conditions.

**Q46. Which operator is commonly used to check passing marks?**

`>=`.

**Q47. Which operator is useful for finding the maximum element?**

`>` or `>=`.

**Q48. Which operator checks whether a value is within an inclusive range?**

A chained comparison using `<=`.

**Q49. Which operators are commonly used in binary search?**

`==`, `<`, and `>`.

**Q50. Why should boundary values be tested?**

They help verify whether conditions correctly include or exclude the minimum and maximum permitted values.

---

# 31. Practice Test

Use this section to check your understanding.

## Part A: Predict the Output

### Question 1

```python
a = 10
b = 10

print(a == b)
```

### Question 2

```python
a = 10
b = 20

print(a != b)
```

### Question 3

```python
a = 50
b = 30

print(a > b)
```

### Question 4

```python
a = 10
b = 15

print(a < b)
```

### Question 5

```python
a = 100
b = 100

print(a >= b)
```

### Question 6

```python
a = 40
b = 50

print(a <= b)
```

### Question 7

```python
print(10 == 10.0)
```

### Question 8

```python
print("Python" == "python")
```

### Question 9

```python
number = 15

print(10 < number < 20)
```

### Question 10

```python
print(True == 1)
```

## Part B: Identify the Correct Operator

1. Check whether two numbers are equal.
2. Check whether two numbers are different.
3. Check whether the first value is greater.
4. Check whether the first value is smaller.
5. Check whether a value satisfies a minimum limit.
6. Check whether a value stays below a maximum limit.
7. Check whether a number lies inside an inclusive range.
8. Find the maximum of two values.
9. Compare two strings for exact equality.
10. Check whether a student has reached the minimum passing marks.

## Part C: Programming Challenges

1. Accept two values and check whether they are equal.
2. Find the greater of two values.
3. Find the smaller of three values.
4. Check whether a person is eligible to vote.
5. Check whether a student passes an examination.
6. Check whether a number is inside a given range.
7. Find the largest of three numbers.
8. Compare two strings.
9. Compare two string lengths.
10. Create a program that checks whether a product price is within a budget.

---

# 32. Quick Revision Notes

## Basic Comparison Operators

```python
a == b    # Equal to
a != b    # Not equal to
a > b     # Greater than
a < b     # Less than
a >= b    # Greater than or equal to
a <= b    # Less than or equal to
```

## Boolean Results

```python
10 == 10    # True
10 != 20    # True
20 > 10     # True
10 < 20     # True
10 >= 10    # True
10 <= 10    # True
```

## String Comparison

```python
"Python" == "Python"    # True
"Python" == "python"    # False
```

## Chained Comparison

```python
10 <= number <= 100
```

## Boolean and Numeric Comparison

```python
True == 1     # True
False == 0    # True
True > False  # True
```

## Assignment vs Equality

```python
x = 10       # Assignment
x == 10      # Equality comparison
```

## Important Reminders

- Comparisons normally return `True` or `False`.
- `>` and `<` do not include equality.
- `>=` and `<=` include equality.
- String comparisons are case-sensitive by default.
- Numeric values of different numeric types can compare equal.
- Chained comparisons are useful for range validation.
- Use `math.isclose()` for approximate floating-point equality.
- Comparison operators are frequently used in conditions and DSA.

---

# 33. Important Terminology

| Term | Meaning |
|---|---|
| Comparison | Checking the relationship between two values |
| Operator | Symbol that performs an operation |
| Operand | Value on which an operator works |
| Equality | A relationship in which two values compare equal |
| Inequality | A relationship in which two values compare unequal |
| Greater than | A comparison in which the left value is larger |
| Less than | A comparison in which the left value is smaller |
| Boolean | Python data type with `True` and `False` |
| Condition | An expression used to make a decision |
| Chained comparison | Multiple connected comparisons |
| Lexicographical order | Ordering based on the sequence of characters |
| Case-sensitive | Treating uppercase and lowercase characters differently |
| Unicode | Character encoding system used by Python strings |
| Boundary value | Minimum or maximum value of a permitted range |
| TypeError | Exception raised for an unsupported operation between types |
| Floating-point precision | Limitations in representing decimal values using binary floating-point numbers |
| Validation | Checking whether data satisfies specified requirements |
| Conditional statement | Statement that chooses execution based on a condition |

---

# 34. Learning Checklist

Complete this checklist after studying the topic.

## Basic Concepts

- [ ] I understand what comparison operators are.
- [ ] I know that comparison expressions return Boolean values.
- [ ] I understand the difference between assignment and comparison.
- [ ] I can predict comparison results.

## Individual Operators

- [ ] I understand equal to (`==`).
- [ ] I understand not equal to (`!=`).
- [ ] I understand greater than (`>`).
- [ ] I understand less than (`<`).
- [ ] I understand greater than or equal to (`>=`).
- [ ] I understand less than or equal to (`<=`).

## Data Type Comparisons

- [ ] I can compare integer values.
- [ ] I can compare float values.
- [ ] I understand integer and float equality.
- [ ] I can compare strings.
- [ ] I understand case-sensitive comparisons.
- [ ] I understand lexicographical ordering.
- [ ] I understand Boolean and numeric comparison.
- [ ] I know why incompatible comparisons can raise `TypeError`.

## Advanced Concepts

- [ ] I understand chained comparisons.
- [ ] I can validate inclusive ranges.
- [ ] I understand Boolean comparison results.
- [ ] I understand floating-point comparison limitations.
- [ ] I know how to use `math.isclose()`.

## Programming Practice

- [ ] I can find the greater of two numbers.
- [ ] I can find the smaller of two numbers.
- [ ] I can find the largest of three numbers.
- [ ] I can check voting eligibility.
- [ ] I can check pass or fail.
- [ ] I can check positive, negative, or zero.
- [ ] I can compare two strings.
- [ ] I can compare string lengths.
- [ ] I have practised all twelve solved problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I have completed the practice test.

---

# 35. How to Run the Python Program

Make sure Python is installed on your computer.

Open a terminal in the Comparison Operators folder.

## 35.1 Run the Program

```bash
python 01_comparison_operators.py
```

On systems where `python3` is used:

```bash
python3 01_comparison_operators.py
```

## 35.2 Expected Main Menu

The program provides the following options:

```text
1. View 12 Comparison Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

## 35.3 Recommended Usage

### Step 1: Study the Examples

Select option `1`.

Study all twelve examples and understand why each comparison returns `True` or `False`.

### Step 2: Practise Solved Problems

Select option `2`.

Choose a problem number and execute it.

Try different input values, especially values that are equal to the comparison boundaries.

### Step 3: Attempt Unsolved Questions

Select option `3`.

Read all ten questions and solve them independently.

### Step 4: Review the Learning Checklist

Select option `4`.

Check which concepts you have understood.

### Step 5: Exit

Select option `0` when you finish.

---

# 36. Recommended Learning Sequence

Follow this order to understand comparison operators properly.

| Order | Topic | What to Learn |
|---:|---|---|
| 1 | Equal To (`==`) | Check equal values |
| 2 | Not Equal To (`!=`) | Check different values |
| 3 | Greater Than (`>`) | Compare larger values |
| 4 | Less Than (`<`) | Compare smaller values |
| 5 | Greater Than or Equal (`>=`) | Understand inclusive minimum limits |
| 6 | Less Than or Equal (`<=`) | Understand inclusive maximum limits |
| 7 | Numeric Comparisons | Compare integers and floats |
| 8 | String Comparisons | Compare textual values |
| 9 | Lexicographical Comparison | Understand string ordering |
| 10 | Chained Comparison | Validate ranges |
| 11 | Boolean Comparison | Understand Boolean and numeric values |
| 12 | Practical Problems | Apply comparisons in programs |

## Before Moving to the Next Topic

Make sure that:

1. You understand all six comparison operators.
2. You can identify `True` and `False` results.
3. You understand numeric and string comparisons.
4. You can use chained comparisons.
5. You can write conditional programs.
6. You have completed the twelve solved problems.
7. You have attempted all ten unsolved questions.
8. You have revised the viva questions.

---

# 37. Topic Completion Summary

In this topic, you learned how Python compares values using comparison operators.

You covered:

- Equal to (`==`).
- Not equal to (`!=`).
- Greater than (`>`).
- Less than (`<`).
- Greater than or equal to (`>=`).
- Less than or equal to (`<=`).
- Integer and floating-point comparisons.
- String equality.
- Lexicographical comparison.
- Chained comparisons.
- Boolean and numeric comparison.
- Assignment versus equality.
- Comparisons with conditional statements.
- Input validation.
- Practical programming applications.
- DSA applications.
- Dry runs and output prediction.
- Interview and viva questions.

Comparison operators are essential for decision-making in Python.

You will use them when learning conditions, loops, functions, searching, sorting, and Data Structures and Algorithms.

Do not just memorize the six symbols. Practise writing conditions, predicting their results, and handling boundary values correctly.

**Complete the examples and programming exercises before moving to the next topic.**

---

## Navigation

**Previous Topic:** [Assignment Operators](../02-Assignment-Operators/README.md)

**Next Topic:** [Logical Operators](../04-Logical-Operators/README.md)

**Parent Section:** [Operators and Expressions](../README.md)
