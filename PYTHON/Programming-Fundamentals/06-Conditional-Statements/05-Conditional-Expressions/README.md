

# Python Conditional Expressions – Complete Learning Guide

## 1. Introduction

Conditional expressions are an important part of Python programming.

They allow a program to choose between two values based on a condition.

A conditional expression is also commonly called the **ternary operator**.

It is useful when you want to write a simple `if-else` decision in a single expression.

For example, imagine a program that checks whether a student has passed an examination.

The program can choose:

- `"Pass"` when marks are at least 40.
- `"Fail"` when marks are below 40.

Using a normal `if-else` statement:

```python
marks = 75

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print(result)
```

The same decision can be written using a conditional expression:

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

### Output

```text
Pass
```

Both programs produce the same result.

The second version is shorter because it uses a conditional expression.

However, shorter code is not always better code. Conditional expressions should be used when the decision is simple and easy to understand.

### Learning Objectives

After completing this topic, you should be able to:

- Understand what a conditional expression is.
- Understand why it is called the ternary operator.
- Write the correct conditional expression syntax.
- Identify the condition, true value, and false value.
- Convert simple `if-else` statements into conditional expressions.
- Use conditional expressions with integers and floating-point numbers.
- Use conditional expressions with strings.
- Use conditional expressions with Boolean values.
- Use conditional expressions inside print statements.
- Assign conditional expression results to variables.
- Understand nested conditional expressions.
- Understand chained conditional expressions.
- Use conditional expressions with comparison operators.
- Use conditional expressions with logical operators.
- Apply conditional expressions to programming problems.
- Identify when a normal `if-else` statement is a better choice.

---

## 2. What Is a Conditional Expression?

A conditional expression is an expression that returns one of two values depending on whether a condition is true or false.

It is called a ternary operator because it involves three main parts:

1. A value or expression when the condition is true.
2. A condition that is evaluated.
3. A value or expression when the condition is false.

### Definition

A conditional expression is a one-line expression that evaluates a condition and returns one value when the condition is `True` or another value when the condition is `False`.

### Simple Example

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

### Output

```text
Adult
```

### Explanation

The expression contains three main parts.

```python
"Adult" if age >= 18 else "Minor"
```

| Part | Value | Purpose |
|---|---|---|
| True expression | `"Adult"` | Returned when the condition is true |
| Condition | `age >= 18` | Decides which value is selected |
| False expression | `"Minor"` | Returned when the condition is false |

The variable `age` contains `20`.

Python checks:

```python
age >= 18
```

The condition is true.

Therefore, Python selects:

```python
"Adult"
```

The selected value is assigned to `result`.

The final output is:

```text
Adult
```

### Important Points

- A conditional expression returns a value.
- It uses the keywords `if` and `else`.
- It is useful for simple two-way decisions.
- It can be used directly in assignments.
- It can be used inside function arguments.
- It can be used inside print statements.
- It can return strings, numbers, Boolean values, and other Python objects.
- It does not replace every normal `if-else` statement.
- A complex decision is often easier to understand with normal conditional blocks.

---

## 3. Syntax of a Conditional Expression

The syntax of a conditional expression is:

```python
value_if_true if condition else value_if_false
```

### Understanding Each Part

**1. `value_if_true`**

This value is selected when the condition evaluates to true.

**2. `if`**

The keyword separates the true expression from the condition.

**3. `condition`**

This is the condition Python evaluates.

It should produce a truth value.

**4. `else`**

The keyword separates the condition from the alternative expression.

**5. `value_if_false`**

This value is selected when the condition evaluates to false.

### General Example

```python
number = 10

result = "Positive" if number > 0 else "Not positive"

print(result)
```

### Output

```text
Positive
```

### Another Example

```python
temperature = 15

message = "Warm" if temperature >= 25 else "Cool"

print(message)
```

### Output

```text
Cool
```

The condition is false, so Python selects `"Cool"`.

### Syntax Comparison

| Normal If-Else | Conditional Expression |
|---|---|
| Uses multiple statements | Usually written as one expression |
| Uses an indented block | Uses an inline expression |
| Can contain several statements | Each selected branch produces an expression value |
| Suitable for complex logic | Suitable for simple choices |
| Can perform multiple actions | Best used when selecting a value |

### General Form

```python
variable = true_value if condition else false_value
```

### Example

```python
marks = 85

grade = "Pass" if marks >= 40 else "Fail"

print(grade)
```

### Output

```text
Pass
```

---

## 4. Understanding How Conditional Expressions Work

Python evaluates the condition before selecting the result.

The general execution process is:

1. Python evaluates the condition.
2. Python checks whether the result is truthy or falsy.
3. If the condition is true, Python evaluates and returns the true expression.
4. If the condition is false, Python evaluates and returns the false expression.
5. The selected value is used by the surrounding expression or statement.

### Example

```python
number = 8

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

### Explanation

First, Python evaluates:

```python
number % 2 == 0
```

The value of `number` is `8`.

The remainder after dividing 8 by 2 is zero.

Therefore, the condition is true.

Python selects:

```python
"Even"
```

The result is stored in the variable.

### Important Behaviour

Only the selected branch expression is evaluated.

Consider:

```python
condition = True

result = "Selected" if condition else 10 / 0

print(result)
```

### Output

```text
Selected
```

Python does not evaluate the false expression because the condition is true.

Therefore, the division by zero expression is not executed.

This behaviour is useful when the unselected expression should not be evaluated.

However, it should not be used to hide complicated logic inside a conditional expression.

---

## 5. Conditional Expression vs Normal If-Else

A conditional expression is not exactly the same syntactic structure as a normal `if-else` statement.

Both can make decisions, but they are written differently.

### Normal If-Else

```python
age = 19

if age >= 18:
    result = "Eligible"
else:
    result = "Not eligible"

print(result)
```

### Conditional Expression

```python
age = 19

result = "Eligible" if age >= 18 else "Not eligible"

print(result)
```

### Comparison

| Feature | If-Else Statement | Conditional Expression |
|---|---|---|
| Form | Statement | Expression |
| Syntax | Multiple blocks | Inline expression |
| Result | Executes statements | Produces a value |
| Number of statements | Can contain many statements | Each branch is an expression |
| Readability | Better for complex logic | Better for simple choices |
| Nested decisions | Often easier to understand | Can become difficult to read |
| Assignment | Can assign values inside blocks | Can assign the selected value directly |

### When to Use a Conditional Expression

Use it when:

- You need to choose between two values.
- The condition is simple.
- The result is short and understandable.
- You want to assign one of two values.
- You want to pass a selected value to a function.
- You want to display one of two short messages.

### When to Use a Normal If-Else

Use a normal `if-else` statement when:

- Each branch contains multiple statements.
- The logic requires multiple calculations.
- The condition is difficult to understand.
- There are several actions to perform.
- You need multiple independent operations.
- The expression becomes too long.
- Readability would be reduced by putting everything on one line.

### Important Rule

Do not convert every `if-else` statement into a conditional expression just to reduce the number of lines.

Readable code is more important than short code.

---

## 6. Conditional Expressions with Numbers

Conditional expressions can return numeric values.

They are useful for selecting a minimum, maximum, absolute value, or another numeric result.

### Example: Largest of Two Numbers

```python
a = 25
b = 40

largest = a if a > b else b

print(largest)
```

### Output

```text
40
```

### Explanation

Python checks whether `a` is greater than `b`.

Since 25 is not greater than 40, the false expression is selected.

The selected value is `b`.

### Example: Minimum of Two Numbers

```python
a = 15
b = 8

minimum = a if a < b else b

print(minimum)
```

### Output

```text
8
```

### Example: Absolute Value

```python
number = -20

absolute = number if number >= 0 else -number

print(absolute)
```

### Output

```text
20
```

The condition checks whether the number is non-negative.

If it is, Python keeps the original number.

Otherwise, Python selects its negative.

### Important Points

- Conditional expressions can return integers.
- They can return floating-point values.
- They can select a minimum or maximum.
- They can perform a small calculation in either branch.
- Use meaningful variable names for the selected value.

---

## 7. Conditional Expressions with Strings

Conditional expressions can return string values.

This is particularly useful when selecting messages or categories.

### Example: Pass or Fail

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

### Output

```text
Pass
```

### Example: Adult or Minor

```python
age = 16

category = "Adult" if age >= 18 else "Minor"

print(category)
```

### Output

```text
Minor
```

### Example: Available or Unavailable

```python
stock = 10

status = "Available" if stock > 0 else "Out of stock"

print(status)
```

### Output

```text
Available
```

### Important Points

- The true expression may return a string.
- The false expression may return another string.
- Both branches do not have to return the same text.
- The selected string can be stored in a variable.
- The selected string can be printed directly.

---

## 8. Conditional Expressions with Boolean Values

A conditional expression can return `True` or `False`.

However, when the condition itself already produces the required Boolean value, you usually do not need a conditional expression.

### Example

```python
age = 20

is_adult = age >= 18

print(is_adult)
```

### Output

```text
True
```

The comparison directly returns a Boolean value.

This is simpler than writing:

```python
is_adult = True if age >= 18 else False
```

Both produce the same Boolean result, but the direct comparison is clearer.

### Another Example

```python
stock = 0

is_available = stock > 0

print(is_available)
```

### Output

```text
False
```

### Important Best Practice

Avoid unnecessary expressions such as:

```python
is_valid = True if marks >= 40 else False
```

Prefer:

```python
is_valid = marks >= 40
```

Use a conditional expression when you need to select between different values, not when a Boolean condition already provides exactly the required result.

---

## 9. Conditional Expressions with Print Statements

A conditional expression can be used directly inside a `print()` statement.

### Example

```python
age = 22

print("Adult" if age >= 18 else "Minor")
```

### Output

```text
Adult
```

The selected value is passed directly to `print()`.

### Example: Even or Odd

```python
number = 17

print("Even" if number % 2 == 0 else "Odd")
```

### Output

```text
Odd
```

### Example: Positive or Negative

```python
number = -10

print("Positive" if number > 0 else "Not positive")
```

### Output

```text
Not positive
```

### When This Style Is Useful

- When displaying a short result.
- When the result does not need to be reused.
- When the expression is easy to understand.
- When the condition is simple.

### When to Avoid It

Avoid placing long nested expressions directly inside a print statement.

For complicated logic, assign the result to a clearly named variable first.

---

## 10. Conditional Expressions with Variables

One of the most common uses of conditional expressions is assigning a selected value to a variable.

### Syntax

```python
result = value_if_true if condition else value_if_false
```

### Example

```python
marks = 82

grade = "Pass" if marks >= 40 else "Fail"

print("Grade:", grade)
```

### Output

```text
Grade: Pass
```

### Explanation

The expression selects the value `"Pass"` because the condition is true.

That value is assigned to `grade`.

The variable can then be used elsewhere in the program.

### Example with Numbers

```python
a = 10
b = 20

maximum = a if a > b else b

print("Maximum:", maximum)
```

### Output

```text
Maximum: 20
```

### Benefits of Assigning the Result

- The selected value can be reused.
- The program becomes easier to read.
- The expression can be tested independently.
- The selected value can be passed to another function.
- The variable name can explain the purpose of the result.

---

## 11. Nested Conditional Expressions

A nested conditional expression contains another conditional expression inside one of its result branches.

It is useful when you need to select from more than two values.

### Syntax

```python
result = (
    value1 if condition1
    else value2 if condition2
    else value3
)
```

The expression is interpreted as:

```python
result = (
    value1 if condition1
    else (
        value2 if condition2
        else value3
    )
)
```

### Example: Positive, Negative, or Zero

```python
number = -5

result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

print(result)
```

### Output

```text
Negative
```

### Explanation

1. Python checks whether the number is greater than zero.
2. The condition is false.
3. Python checks whether the number is less than zero.
4. The condition is true.
5. Python selects `"Negative"`.

### Example: Grade Calculator

```python
marks = 85

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print(grade)
```

### Output

```text
B
```

### Understanding the Structure

The grade expression contains several conditional choices.

The first condition is checked first.

If it is false, Python moves to the next conditional expression.

This continues until a condition is true or the final fallback value is reached.

### Important Note

Nested conditional expressions can become difficult to understand.

When many conditions are required, a normal `if-elif-else` statement is usually clearer.

---

## 12. Chained Conditional Expressions

A chained conditional expression uses multiple conditional expressions to select among multiple alternatives.

It is also commonly called a nested ternary expression.

### Example

```python
marks = 65

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print(grade)
```

### Output

```text
C
```

### Explanation

The conditions are checked in order.

- `marks >= 90` is false.
- `marks >= 75` is false.
- `marks >= 60` is true.

Python selects `"C"`.

### Parentheses

Parentheses can make nested expressions easier to read.

For example:

```python
result = (
    "High"
    if number > 100
    else (
        "Medium"
        if number >= 50
        else "Low"
    )
)
```

This format makes the nested relationship more visible.

### Best Practice

Use chained conditional expressions only when the result remains easy to understand.

For long grading systems, menus, or business rules, prefer ordinary conditional statements.

---

## 13. Conditional Expressions with Logical Operators

Conditional expressions can contain logical operators such as:

- `and`
- `or`
- `not`

These operators allow multiple conditions to be evaluated together.

### Example Using `and`

```python
age = 20
has_id = True

result = "Allowed" if age >= 18 and has_id else "Not allowed"

print(result)
```

### Output

```text
Allowed
```

### Explanation

Both conditions must be true:

- Age must be at least 18.
- ID must be available.

Because both conditions are satisfied, Python selects `"Allowed"`.

### Example Using `or`

```python
is_student = False
has_coupon = True

result = "Discount available" if is_student or has_coupon else "No discount"

print(result)
```

### Output

```text
Discount available
```

At least one condition is true, so the first value is selected.

### Example Using `not`

```python
is_blocked = False

result = "Access allowed" if not is_blocked else "Access denied"

print(result)
```

### Output

```text
Access allowed
```

### Important Points

- `and` requires both conditions to be true.
- `or` requires at least one condition to be true.
- `not` reverses a Boolean result.
- Parentheses can make complicated conditions clearer.
- Do not combine too many conditions into one unreadable expression.

---

## 14. Conditional Expressions with Comparison Operators

Comparison operators are commonly used inside conditional expressions.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

### Example: Equality

```python
a = 10
b = 10

result = "Equal" if a == b else "Not equal"

print(result)
```

### Output

```text
Equal
```

### Example: Greater Than

```python
number = 50

result = "Large" if number > 25 else "Small"

print(result)
```

### Output

```text
Large
```

### Example: Not Equal

```python
password = "python"

result = "Accepted" if password != "" else "Empty password"

print(result)
```

### Output

```text
Accepted
```

### Important Rule

Use the correct comparison operator.

For example:

```python
marks >= 40
```

includes marks equal to 40.

But:

```python
marks > 40
```

does not include marks equal to 40.

---

## 15. Conditional Expressions and Data Types

The selected result may be of different Python data types.

### Integer Result

```python
number = -10

result = number if number >= 0 else 0

print(result)
```

### Output

```text
0
```

### Float Result

```python
price = 100.0

final_price = price if price >= 50 else 50.0

print(final_price)
```

### Output

```text
100.0
```

### String Result

```python
age = 17

category = "Adult" if age >= 18 else "Minor"

print(category)
```

### Output

```text
Minor
```

### Boolean Result

```python
marks = 80

eligible = True if marks >= 40 else False

print(eligible)
```

### Output

```text
True
```

The Boolean example can be simplified:

```python
eligible = marks >= 40
```

### List Result

```python
has_items = True

items = ["apple", "banana"] if has_items else []

print(items)
```

### Output

```text
['apple', 'banana']
```

### Tuple Result

```python
available = False

result = ("Available", 10) if available else ("Unavailable", 0)

print(result)
```

### Output

```text
('Unavailable', 0)
```

### Important Point

A conditional expression can return almost any Python object.

The important requirement is that the selected branch must produce a valid expression result.

---

## 16. Conditional Expressions with Functions

A conditional expression can select a value that is passed to a function.

### Example

```python
age = 20

print("Adult" if age >= 18 else "Minor")
```

The selected string is passed to `print()`.

### Example with `round()`

```python
price = 99.876

result = round(price, 2) if price > 0 else 0

print(result)
```

### Output

```text
99.88
```

### Example with `abs()`

```python
number = -25

result = abs(number) if number < 0 else number

print(result)
```

### Output

```text
25
```

### Important Point

You can use function calls in either branch.

Only the selected branch is evaluated.

Keep the function calls simple so that the expression remains readable.

---

## 17. Python Conditional Expression Evaluation

Understanding evaluation is important when expressions become longer.

Consider:

```python
a = 10
b = 20

result = a if a > b else b
```

Python evaluates the condition:

```python
a > b
```

Since the condition is false, Python selects `b`.

The final result is `20`.

### Parentheses and Readability

Consider:

```python
result = (
    "A" if condition1
    else "B" if condition2
    else "C"
)
```

This is interpreted as:

```python
result = (
    "A" if condition1
    else (
        "B" if condition2
        else "C"
    )
)
```

### Avoid Ambiguous Expressions

Do not write long expressions without considering how Python groups them.

Use parentheses to make the intended structure clear.

### Important Concepts

- Python evaluates the condition before selecting a result.
- Only the selected branch expression is evaluated.
- Nested expressions can appear inside another expression.
- Parentheses can improve readability.
- Chained conditional expressions should be used carefully.

---

## 18. Limitations of Conditional Expressions

Conditional expressions are useful, but they are not suitable for every situation.

### Limitation 1: Readability

A very long conditional expression can become difficult to read.

### Limitation 2: Multiple Actions

A conditional expression is designed to produce a value.

It is not a replacement for a block of multiple statements.

### Limitation 3: Complex Validation

Several stages of input validation are usually clearer with normal `if-else` blocks.

### Limitation 4: Difficult Debugging

Long nested expressions may be harder to debug because several decisions are written together.

### Limitation 5: Multiple Alternatives

When many alternatives are required, `if-elif-else` may be easier to understand.

### Example of an Overcomplicated Expression

```python
result = (
    "Excellent" if marks >= 90
    else "Very Good" if marks >= 80
    else "Good" if marks >= 70
    else "Average" if marks >= 60
    else "Below Average" if marks >= 50
    else "Fail"
)
```

Although this is valid, a normal `if-elif-else` structure may be more readable when the grading rules grow.

### Better Alternative

```python
if marks >= 90:
    result = "Excellent"
elif marks >= 80:
    result = "Very Good"
elif marks >= 70:
    result = "Good"
elif marks >= 60:
    result = "Average"
elif marks >= 50:
    result = "Below Average"
else:
    result = "Fail"
```

The best solution is the one that clearly communicates the logic.

---

# SECTION 2: TWELVE PYTHON CONDITIONAL EXPRESSION EXAMPLES

## Example 1: Basic Conditional Expression

### Objective

Use a conditional expression to classify a person as an adult or minor.

### Code

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print("Age:", age)
print("Result:", result)
```

### Output

```text
Age: 20
Result: Adult
```

### Explanation

The variable `age` stores 20.

The condition is:

```python
age >= 18
```

It evaluates to `True`.

Therefore, the expression selects `"Adult"`.

### Concepts Used

- Conditional expression
- Comparison operator
- String assignment

---

## Example 2: Even or Odd

### Objective

Check whether a number is even or odd.

### Code

```python
number = 15

result = "Even" if number % 2 == 0 else "Odd"

print("Number:", number)
print("Result:", result)
```

### Output

```text
Number: 15
Result: Odd
```

### Explanation

The modulus operator finds the remainder.

For an even number, the remainder after division by two is zero.

For 15, the remainder is one.

Therefore, the condition is false and Python selects `"Odd"`.

### Concepts Used

- Modulus operator
- Conditional expression
- Integer comparison

---

## Example 3: Positive or Negative

### Objective

Check whether a number is positive or not positive.

### Code

```python
number = -12

result = "Positive" if number > 0 else "Not positive"

print("Number:", number)
print("Result:", result)
```

### Output

```text
Number: -12
Result: Not positive
```

### Explanation

The expression checks whether the number is greater than zero.

Since `-12` is not greater than zero, Python selects `"Not positive"`.

This example groups negative numbers and zero into the same result.

If you want to identify all three categories separately, use a chained conditional expression.

---

## Example 4: Largest of Two Numbers

### Objective

Find the largest of two numbers.

### Code

```python
a = 25
b = 40

largest = a if a > b else b

print("A:", a)
print("B:", b)
print("Largest:", largest)
```

### Output

```text
A: 25
B: 40
Largest: 40
```

### Explanation

Python checks:

```python
a > b
```

The condition is false.

Therefore, it selects `b`.

The selected value is assigned to `largest`.

### Important Point

If the numbers are equal, this expression selects `b`.

Both values still represent the same largest numeric value.

---

## Example 5: Pass or Fail

### Objective

Check whether a student has passed.

### Code

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"

print("Marks:", marks)
print("Result:", result)
```

### Output

```text
Marks: 75
Result: Pass
```

### Explanation

The condition checks whether marks are at least 40.

Since the condition is true, the expression selects `"Pass"`.

The passing threshold is an illustrative programming rule.

---

## Example 6: Absolute Value

### Objective

Find the absolute value of a number using a conditional expression.

### Code

```python
number = -25

absolute = number if number >= 0 else -number

print("Original number:", number)
print("Absolute value:", absolute)
```

### Output

```text
Original number: -25
Absolute value: 25
```

### Explanation

The condition checks whether the number is greater than or equal to zero.

If true, the original number is selected.

Otherwise, the negative of the number is selected.

---

## Example 7: Minimum of Two Numbers

### Objective

Find the smaller of two numbers.

### Code

```python
a = 18
b = 12

minimum = a if a < b else b

print("A:", a)
print("B:", b)
print("Minimum:", minimum)
```

### Output

```text
A: 18
B: 12
Minimum: 12
```

### Explanation

Python checks whether `a` is smaller than `b`.

The condition is false.

Therefore, it selects `b`.

---

## Example 8: Voting Eligibility

### Objective

Check whether a person is eligible to vote based on an age threshold.

### Code

```python
age = 19

result = "Eligible to vote" if age >= 18 else "Not eligible to vote"

print("Age:", age)
print("Result:", result)
```

### Output

```text
Age: 19
Result: Eligible to vote
```

### Explanation

The condition checks whether the person's age is at least 18.

Since the condition is true, Python selects the eligibility message.

---

## Example 9: Largest of Three Numbers

### Objective

Find the largest among three numbers using nested conditional expressions.

### Code

```python
a = 25
b = 50
c = 35

largest = a if a >= b and a >= c else (b if b >= c else c)

print("A:", a)
print("B:", b)
print("C:", c)
print("Largest:", largest)
```

### Output

```text
A: 25
B: 50
C: 35
Largest: 50
```

### Explanation

The outer expression checks whether `a` is greater than or equal to both `b` and `c`.

If true, `a` is selected.

Otherwise, Python evaluates:

```python
b if b >= c else c
```

This selects the larger value between `b` and `c`.

For the given values, the result is 50.

### Important Point

Parentheses help show the nested expression clearly.

---

## Example 10: Grade Calculator

### Objective

Calculate a grade using chained conditional expressions.

### Example Rules

| Marks | Grade |
|---|---|
| 90 or above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

### Code

```python
marks = 86

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print("Marks:", marks)
print("Grade:", grade)
```

### Output

```text
Marks: 86
Grade: B
```

### Explanation

Python evaluates the conditions in sequence.

The first condition is false.

The second condition is true.

Therefore, Python selects grade `"B"`.

The thresholds are illustrative.

---

## Example 11: Leap Year

### Objective

Check whether a year is a leap year using a conditional expression.

### Code

```python
year = 2024

result = (
    "Leap year"
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    else "Not a leap year"
)

print("Year:", year)
print("Result:", result)
```

### Output

```text
Year: 2024
Result: Leap year
```

### Explanation

A year is a leap year when:

- It is divisible by 400, or
- It is divisible by 4 and not divisible by 100.

The expression uses both `or` and `and`.

Parentheses make the intended grouping clear.

---

## Example 12: Discount Calculator

### Objective

Calculate a purchase discount using a conditional expression.

### Example Rule

- Purchase amount of at least 5000 receives a 20% discount.
- Purchase amount below 5000 receives no discount.

### Code

```python
purchase_amount = 6000

discount_rate = 20 if purchase_amount >= 5000 else 0

discount_amount = purchase_amount * discount_rate / 100
final_amount = purchase_amount - discount_amount

print("Purchase amount:", purchase_amount)
print("Discount rate:", discount_rate, "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)
```

### Output

```text
Purchase amount: 6000
Discount rate: 20 %
Discount amount: 1200.0
Final amount: 4800.0
```

### Explanation

Python first checks whether the purchase amount is at least 5000.

Since the condition is true, the discount rate becomes 20.

The program then calculates the discount amount.

Finally, it subtracts the discount from the purchase amount.

The discount rule is an illustrative programming example.

---

# SECTION 3: TWELVE SOLVED PROBLEMS

## Problem 1: Even or Odd

### Problem Statement

Write a Python program that accepts an integer and determines whether the number is even or odd using a conditional expression.

### Logic

1. Accept an integer.
2. Divide the number by two using the modulus operator.
3. If the remainder is zero, select `"Even"`.
4. Otherwise, select `"Odd"`.
5. Display the result.

### Code

```python
number = int(input("Enter a number: "))

result = "Even" if number % 2 == 0 else "Odd"

print("Result:", result)
```

### Sample Input

```text
Enter a number: 14
```

### Expected Output

```text
Result: Even
```

### Explanation

The expression is:

```python
"Even" if number % 2 == 0 else "Odd"
```

The condition evaluates to true for 14.

Therefore, `"Even"` is selected.

### Concepts Used

- Conditional expression
- Modulus operator
- Integer input
- Comparison operator

---

## Problem 2: Positive, Negative or Zero

### Problem Statement

Accept a number and classify it as positive, negative, or zero.

Use chained conditional expressions.

### Logic

1. Accept a number.
2. Check whether it is greater than zero.
3. If not, check whether it is less than zero.
4. Otherwise, classify it as zero.

### Code

```python
number = float(input("Enter a number: "))

result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

print("Result:", result)
```

### Sample Input

```text
Enter a number: -8
```

### Expected Output

```text
Result: Negative
```

### Explanation

The first condition is false because `-8` is not greater than zero.

The second condition is true because `-8` is less than zero.

Therefore, `"Negative"` is selected.

### Concepts Used

- Chained conditional expression
- Comparison operators
- Floating-point input

---

## Problem 3: Voting Eligibility

### Problem Statement

Accept a person's age and check voting eligibility using a conditional expression.

Use 18 as the example age threshold.

### Logic

1. Accept age.
2. Compare age with 18.
3. Select the appropriate message.
4. Display the result.

### Code

```python
age = int(input("Enter your age: "))

result = "Eligible to vote" if age >= 18 else "Not eligible to vote"

print("Result:", result)
```

### Sample Input

```text
Enter your age: 20
```

### Expected Output

```text
Result: Eligible to vote
```

### Explanation

The condition checks whether age is at least 18.

Since 20 is greater than 18, the expression selects the first message.

### Concepts Used

- Conditional expression
- Integer input
- Comparison operator

---

## Problem 4: Largest of Two Numbers

### Problem Statement

Accept two numbers and determine the larger value.

Handle equality separately.

### Logic

1. Accept the first number.
2. Accept the second number.
3. Check whether both numbers are equal.
4. Otherwise, compare the numbers.
5. Display the result.

### Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = (
    "Both numbers are equal" if a == b
    else f"Largest number: {a}" if a > b
    else f"Largest number: {b}"
)

print(result)
```

### Sample Input

```text
Enter first number: 10
Enter second number: 25
```

### Expected Output

```text
Largest number: 25.0
```

### Explanation

The program first checks equality.

The numbers are not equal.

Next, it checks whether `a` is greater than `b`.

That condition is false.

Therefore, the final expression selects the message containing `b`.

### Concepts Used

- Nested conditional expression
- Equality comparison
- String formatting
- Numeric input

---

## Problem 5: Pass or Fail

### Problem Statement

Accept marks between 0 and 100.

Classify the student as pass or fail.

Use 40 as the illustrative passing threshold.

### Logic

1. Accept marks.
2. Validate that the marks are between 0 and 100.
3. If valid, check the passing condition.
4. Display pass or fail.

### Code

```python
marks = float(input("Enter marks: "))

result = (
    "Invalid marks" if marks < 0 or marks > 100
    else "Pass" if marks >= 40
    else "Fail"
)

print("Result:", result)
```

### Sample Input

```text
Enter marks: 75
```

### Expected Output

```text
Result: Pass
```

### Explanation

The first expression checks whether marks are outside the valid range.

Since 75 is within the range, Python continues to the next conditional expression.

The passing condition is true.

Therefore, `"Pass"` is selected.

### Concepts Used

- Chained conditional expressions
- Input validation
- Logical operators
- Comparison operators

---

## Problem 6: Minimum of Two Numbers

### Problem Statement

Accept two values and find the smaller value using a conditional expression.

### Logic

1. Accept two numbers.
2. Compare the numbers.
3. Select the smaller number.
4. Display the result.

### Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

minimum = a if a <= b else b

print("Minimum:", minimum)
```

### Sample Input

```text
Enter first number: 18
Enter second number: 12
```

### Expected Output

```text
Minimum: 12.0
```

### Explanation

The condition checks whether `a` is less than or equal to `b`.

Since 18 is not less than or equal to 12, Python selects `b`.

### Concepts Used

- Conditional expression
- Numeric comparison
- Minimum selection

---

## Problem 7: Largest of Three Numbers

### Problem Statement

Accept three numbers and find the largest value using nested conditional expressions.

### Logic

1. Accept three numbers.
2. Check whether the first number is greater than or equal to both other numbers.
3. If true, select the first number.
4. Otherwise, compare the second and third numbers.
5. Select the larger value.

### Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = a if a >= b and a >= c else (b if b >= c else c)

print("Largest:", largest)
```

### Sample Input

```text
Enter first number: 25
Enter second number: 50
Enter third number: 35
```

### Expected Output

```text
Largest: 50.0
```

### Explanation

The first comparison checks whether `a` is the largest.

Since that condition is false, Python evaluates the nested expression.

It compares `b` and `c`.

Because 50 is greater than 35, it selects `b`.

### Concepts Used

- Nested conditional expression
- Logical `and`
- Comparison operators

---

## Problem 8: Absolute Value

### Problem Statement

Accept a number and find its absolute value using a conditional expression.

### Logic

1. Accept a number.
2. Check whether it is greater than or equal to zero.
3. If true, select the original value.
4. Otherwise, select its negative.
5. Display the result.

### Code

```python
number = float(input("Enter a number: "))

absolute = number if number >= 0 else -number

print("Absolute value:", absolute)
```

### Sample Input

```text
Enter a number: -25
```

### Expected Output

```text
Absolute value: 25.0
```

### Explanation

The condition is false because the number is negative.

Therefore, Python selects `-number`.

The result is 25.

### Concepts Used

- Conditional expression
- Comparison operator
- Unary minus operator

---

## Problem 9: Divisibility by Five

### Problem Statement

Accept an integer and check whether it is divisible by five.

### Logic

1. Accept an integer.
2. Calculate the remainder after division by five.
3. If the remainder is zero, select the divisible message.
4. Otherwise, select the non-divisible message.

### Code

```python
number = int(input("Enter an integer: "))

result = "Divisible by 5" if number % 5 == 0 else "Not divisible by 5"

print("Result:", result)
```

### Sample Input

```text
Enter an integer: 45
```

### Expected Output

```text
Result: Divisible by 5
```

### Explanation

The value 45 leaves no remainder when divided by five.

Therefore, the condition is true.

### Concepts Used

- Modulus operator
- Conditional expression
- Integer input

---

## Problem 10: Grade Calculator

### Problem Statement

Accept marks and calculate a grade using chained conditional expressions.

### Example Rules

| Marks | Grade |
|---|---|
| 90 to 100 | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

### Code

```python
marks = float(input("Enter marks: "))

grade = (
    "Invalid marks" if marks < 0 or marks > 100
    else "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print("Grade:", grade)
```

### Sample Input

```text
Enter marks: 86
```

### Expected Output

```text
Grade: B
```

### Explanation

The first expression validates the marks.

Since 86 is valid, Python checks the grade conditions.

The conditions for A are false.

The condition for B is true.

Therefore, the expression selects grade B.

### Concepts Used

- Chained conditional expressions
- Input validation
- Numeric comparison

---

## Problem 11: Discount Calculator

### Problem Statement

Accept purchase amount and membership status.

Calculate the discount using conditional expressions.

### Example Rules

- A member purchasing at least 5000 receives a 20% discount.
- A non-member purchasing at least 5000 receives a 10% discount.
- A purchase below 5000 receives no discount.

### Code

```python
purchase_amount = float(input("Enter purchase amount: "))

is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"

discount_rate = (
    20 if purchase_amount >= 5000 and is_member
    else 10 if purchase_amount >= 5000
    else 0
)

discount_amount = purchase_amount * discount_rate / 100
final_amount = purchase_amount - discount_amount

print("Purchase amount:", purchase_amount)
print("Discount rate:", discount_rate, "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)
```

### Sample Input

```text
Enter purchase amount: 6000
Are you a member? (yes/no): yes
```

### Expected Output

```text
Purchase amount: 6000.0
Discount rate: 20 %
Discount amount: 1200.0
Final amount: 4800.0
```

### Explanation

The first condition checks whether the purchase amount is at least 5000 and the customer is a member.

Both conditions are true.

Therefore, the discount rate is 20%.

The program then calculates the discount amount and final price.

### Concepts Used

- Nested conditional expression
- Logical `and`
- Percentage calculation
- String input

---

## Problem 12: Login Check

### Problem Statement

Create a simple login-check demonstration using a conditional expression.

Check:

- Username.
- Password.
- Account status.

### Demonstration Credentials

```text
Username: amaan
Password: python123
```

### Code

```python
correct_username = "amaan"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")
account_active = input("Is the account active? (yes/no): ").strip().lower() == "yes"

result = (
    "Incorrect username" if username != correct_username
    else "Incorrect password" if password != correct_password
    else "Account is inactive" if not account_active
    else "Login successful"
)

print("Login result:", result)
```

### Sample Input

```text
Enter username: amaan
Enter password: python123
Is the account active? (yes/no): yes
```

### Expected Output

```text
Login result: Login successful
```

### Explanation

The expression checks conditions in a sequence.

First, it checks whether the username is incorrect.

If the username is correct, it checks whether the password is incorrect.

If both credentials are correct, it checks account status.

When all required conditions are satisfied, the final value is `"Login successful"`.

### Important Security Note

This is a beginner learning exercise using dummy credentials.

It is not a secure authentication system.

Real applications should not store plain-text passwords.

They should use appropriate password hashing, authentication controls, and secure session handling.

### Concepts Used

- Chained conditional expressions
- String comparison
- Boolean conditions
- Logical `not`

---

# SECTION 4: TEN UNSOLVED PRACTICE QUESTIONS

Try to solve these questions yourself.

Use conditional expressions where they make the solution easier to read.

Do not force a conditional expression into a problem when a normal `if-else` statement would be clearer.

## Question 1: Smallest of Three Numbers

Accept three numbers and find the smallest using conditional expressions.

### Requirements

- Accept three numeric values.
- Compare the values.
- Select the smallest.
- Display the result.

### Concepts

- Conditional expression.
- Nested conditional expressions.
- Comparison operators.

---

## Question 2: Temperature Classification

Accept a temperature and classify it into three categories.

### Example Rules

- Below 15: Cold.
- From 15 to below 30: Moderate.
- 30 or above: Hot.

### Requirements

- Accept temperature.
- Validate that the input is a finite number.
- Select the appropriate category.
- Display the result.

### Concepts

- Chained conditional expression.
- Numeric comparison.
- Boundary conditions.

---

## Question 3: Vowel or Consonant

Accept one alphabet character.

Classify it as a vowel or consonant.

### Requirements

- Accept one character.
- Convert it to lowercase.
- Check whether it is an alphabet.
- If alphabetic, check vowel membership.
- Display the result.

### Concepts

- Conditional expression.
- String methods.
- Membership operator.

---

## Question 4: Leap Year

Accept a year and check whether it is a leap year.

### Requirements

- Accept an integer year.
- Validate that the year is positive.
- Apply the leap-year rules.
- Display the result.

### Concepts

- Conditional expression.
- Modulus operator.
- Logical operators.

---

## Question 5: Taxi Fare Calculator

Create a simple taxi fare calculator.

### Example Rules

- Minimum fare: 50.
- If distance is greater than a selected threshold, calculate an additional amount.
- Otherwise, apply the minimum fare.

### Requirements

- Accept distance.
- Validate distance.
- Calculate the example fare.
- Display the final fare.

### Concepts

- Conditional expression.
- Arithmetic operators.
- Numeric validation.

Use clearly documented sample fare rates.

---

## Question 6: Shipping Fee Calculator

Create a shipping fee calculator based on order amount.

### Example Rules

- Orders of at least 1000 receive free shipping.
- Orders below 1000 have a shipping fee of 50.

### Requirements

- Accept order amount.
- Validate the amount.
- Select the shipping fee.
- Calculate the total amount.

### Concepts

- Conditional expression.
- Comparison operator.
- Arithmetic operations.

---

## Question 7: Scholarship Eligibility

Create a scholarship eligibility demonstration.

### Example Rules

- Marks must be at least 75.
- Family income must not exceed 200000.

### Requirements

- Accept marks.
- Accept family income.
- Validate both inputs.
- Check eligibility.
- Display the result.

### Concepts

- Nested conditional expression.
- Logical `and`.
- Numeric comparison.

Use illustrative thresholds only.

---

## Question 8: Simple Calculator

Create a simple calculator using two numbers and an operator.

### Requirements

- Accept the first number.
- Accept the second number.
- Accept an arithmetic operator.
- Support addition, subtraction, multiplication, and division.
- Handle division by zero.
- Display the calculated result.

### Concepts

- Conditional expressions.
- Arithmetic operators.
- String comparison.
- Error handling.

A normal `if-elif-else` structure may be more readable for this problem because there are several operations.

---

## Question 9: Ticket Price Calculator

Create a ticket category or price calculator based on age.

### Example Rules

- Children below 12 receive a child ticket.
- People aged 12 to 59 receive a regular ticket.
- People aged 60 or above receive a senior ticket.

### Requirements

- Accept age.
- Validate the age.
- Select the category.
- Display the result.

### Concepts

- Chained conditional expression.
- Numeric comparison.
- Boundary values.

Use illustrative ticket prices if you decide to calculate an amount.

---

## Question 10: Student Result

Create a student result program using multiple subject marks.

### Requirements

- Accept marks in multiple subjects.
- Validate marks.
- Check whether all required passing conditions are met.
- Display an overall result.

### Concepts

- Conditional expressions.
- Comparison operators.
- Logical operators.
- Multiple conditions.

A normal conditional structure may be preferable if the result logic becomes complicated.

---

# SECTION 5: COMMON MISTAKES

## Mistake 1: Writing the Expression in the Wrong Order

Incorrect:

```python
result = if age >= 18 "Adult" else "Minor"
```

Correct:

```python
result = "Adult" if age >= 18 else "Minor"
```

The true value comes before `if`.

The condition comes between `if` and `else`.

The false value comes after `else`.

## Mistake 2: Forgetting Else

Incorrect:

```python
result = "Adult" if age >= 18
```

Correct:

```python
result = "Adult" if age >= 18 else "Minor"
```

A conditional expression requires both alternatives.

## Mistake 3: Using Assignment Instead of Comparison

Incorrect:

```python
result = "Equal" if a = b else "Different"
```

Correct:

```python
result = "Equal" if a == b else "Different"
```

`=` is assignment.

`==` is comparison.

## Mistake 4: Using a Normal If Block Where an Expression Is Required

Incorrect:

```python
result = if age >= 18:
    "Adult"
else:
    "Minor"
```

Correct:

```python
result = "Adult" if age >= 18 else "Minor"
```

A conditional expression has its own syntax.

It is not a shortened way of writing the full block syntax character by character.

## Mistake 5: Forgetting Operator Precedence

Consider:

```python
result = "Eligible" if age >= 18 and has_id else "Not eligible"
```

The condition contains two checks joined by `and`.

Both checks must be true to select `"Eligible"`.

If the logic is complicated, use parentheses to make the condition clearer.

## Mistake 6: Writing an Unreadable Nested Expression

Avoid extremely long expressions.

Incorrect style:

```python
result = "A" if a else "B" if b else "C" if c else "D" if d else "E"
```

This may be difficult to maintain.

A normal `if-elif-else` structure can be clearer.

## Mistake 7: Not Validating Input

A user may enter invalid values.

For example, marks should generally be validated before a grade is selected.

Incorrect:

```python
grade = "Pass" if marks >= 40 else "Fail"
```

This expression does not reject marks above 100 or below zero.

A better expression is:

```python
grade = (
    "Invalid marks" if marks < 0 or marks > 100
    else "Pass" if marks >= 40
    else "Fail"
)
```

## Mistake 8: Confusing Positive and Non-Negative

Consider:

```python
result = "Positive" if number > 0 else "Negative"
```

This expression classifies zero as `"Negative"`.

That is logically incorrect if the intention is to distinguish all three categories.

Use a chained expression:

```python
result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)
```

## Mistake 9: Using a Conditional Expression for Multiple Actions

A conditional expression returns a value.

It is not designed to replace a group of independent statements.

Use normal conditional blocks when multiple actions are required.

## Mistake 10: Choosing Unclear Variable Names

Avoid:

```python
x = "Pass" if marks >= 40 else "Fail"
```

Prefer:

```python
result = "Pass" if marks >= 40 else "Fail"
```

A meaningful variable name helps explain the purpose of the result.

## Mistake 11: Ignoring Equal Values

Consider:

```python
largest = a if a > b else b
```

When `a` and `b` are equal, the expression selects `b`.

This is acceptable when only the largest value is required.

If equality needs a separate message, check equality explicitly.

## Mistake 12: Assuming Every Short Expression Is Readable

A one-line expression may still be difficult to understand.

The goal is not merely to reduce the number of lines.

The goal is clear and maintainable code.

---

# SECTION 6: BEST PRACTICES

Follow these guidelines when using conditional expressions.

1. Use conditional expressions for simple decisions.
2. Keep the condition short and understandable.
3. Use meaningful variable names.
4. Validate input before applying business rules.
5. Use parentheses to clarify nested expressions.
6. Avoid unnecessary nested expressions.
7. Do not write long business logic in one line.
8. Prefer `if-elif-else` for several complex alternatives.
9. Use normal conditional blocks when multiple actions are required.
10. Use conditional expressions when selecting one value.
11. Keep true and false branches easy to understand.
12. Use clear comparison operators.
13. Check boundary values carefully.
14. Avoid hiding complicated function calls inside expressions.
15. Do not use a conditional expression merely to make code shorter.
16. Prefer direct Boolean expressions when they already provide the required result.
17. Keep formatting consistent.
18. Use comments when the selected value may not be obvious.
19. Consider maintainability before reducing line count.
20. Follow the conventions of the existing project.

### Good Example

```python
age = 20

category = "Adult" if age >= 18 else "Minor"

print(category)
```

The expression is short and understandable.

### Less Readable Example

```python
result = ("Adult" if age >= 18 else ("Minor" if age < 18 else "Unknown"))
```

The additional condition may be unnecessary because `age >= 18` and `age < 18` already cover the ordinary numeric cases.

### Better Alternative

```python
category = "Adult" if age >= 18 else "Minor"
```

Choose the simplest expression that correctly represents the intended decision.

---

# SECTION 7: DEBUGGING CONDITIONAL EXPRESSIONS

Debugging means identifying and correcting errors in a program.

Conditional expressions can be harder to debug when their conditions or nested branches become complicated.

## 1. Check the Syntax

Confirm that the expression follows this order:

```python
true_value if condition else false_value
```

## 2. Check the Condition

Make sure the comparison is correct.

For example:

```python
marks >= 40
```

is different from:

```python
marks > 40
```

The first includes 40.

The second excludes 40.

## 3. Check Both Result Branches

Confirm that:

- The true value is correct.
- The false value is correct.
- The expression returns the intended type.
- The selected value is used correctly.

## 4. Check Input Types

The `input()` function returns text.

Incorrect:

```python
age = input("Enter age: ")

result = "Adult" if age >= 18 else "Minor"
```

The comparison attempts to compare a string with an integer.

Correct:

```python
age = int(input("Enter age: "))

result = "Adult" if age >= 18 else "Minor"
```

## 5. Check Numeric Validation

For numeric calculations, ensure that input values are valid.

For example, a percentage calculation should handle an invalid purchase amount before performing the calculation.

## 6. Check Nested Expressions

When a conditional expression contains another conditional expression, add parentheses where necessary to show the intended structure.

## 7. Use Intermediate Variables

If an expression is difficult to understand, separate the condition into smaller parts.

Instead of:

```python
result = "Eligible" if age >= 18 and marks >= 40 and has_id else "Not eligible"
```

You can write:

```python
age_valid = age >= 18
marks_valid = marks >= 40
documents_available = has_id

is_eligible = age_valid and marks_valid and documents_available

result = "Eligible" if is_eligible else "Not eligible"
```

The second version makes the logic easier to understand.

## 8. Common Errors

| Error | Possible Reason |
|---|---|
| `SyntaxError` | Incorrect conditional expression syntax |
| `NameError` | Variable was not defined |
| `TypeError` | Incompatible data types |
| `ValueError` | Invalid value supplied to a conversion |
| `ZeroDivisionError` | Division by zero in an evaluated branch |

Remember that an error in an unselected branch may not occur because that branch is not evaluated.

---

# SECTION 8: REAL-WORLD APPLICATIONS

Conditional expressions are useful in many applications where a simple value must be selected based on a condition.

## 1. Student Result Systems

A student result system may select a result:

```python
result = "Pass" if marks >= 40 else "Fail"
```

The expression chooses a message according to the marks.

## 2. E-Commerce Applications

An online store may select a shipping message:

```python
shipping = "Free" if order_amount >= 1000 else "Paid"
```

The expression chooses one shipping category.

## 3. Shopping Discounts

A shopping application may select a discount rate:

```python
discount = 20 if purchase_amount >= 5000 else 0
```

The selected discount is then used for a calculation.

## 4. Login Interfaces

A simple interface may choose a message based on login status:

```python
message = "Welcome" if is_logged_in else "Please log in"
```

Real authentication and security decisions require more than a simple message selection.

## 5. Ticket Booking

A ticket system may select a ticket category:

```python
category = "Child" if age < 12 else "Regular"
```

For multiple age categories, a normal conditional structure may be easier to maintain.

## 6. Inventory Management

An inventory application may display:

```python
status = "Available" if stock > 0 else "Out of stock"
```

The expression selects a stock status.

## 7. Banking Interfaces

A banking interface may display an account message:

```python
status = "Active" if account_active else "Inactive"
```

Actual account operations require validation and authorization beyond this simple expression.

## 8. Weather Applications

A weather application may display a temperature category:

```python
message = "Hot" if temperature >= 30 else "Moderate"
```

A more complete weather classification may require several conditions.

## 9. Employee Management

An employee management system may select a basic eligibility label:

```python
status = "Eligible" if years_of_service >= 2 else "Not eligible"
```

The real eligibility rules depend on the organization's policy.

## 10. Delivery Applications

A delivery system may select a fee:

```python
delivery_fee = 0 if order_amount >= 1000 else 50
```

The fee values are illustrative.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Conditional expressions are evaluated as part of normal Python expressions.

Their complexity depends on the operations contained in the condition and selected result branches.

## Time Complexity of a Simple Conditional Expression

Consider:

```python
number = 10

result = "Even" if number % 2 == 0 else "Odd"
```

The expression performs:

- A modulus operation.
- A comparison.
- A selection between two constant values.

For ordinary integer values, these operations are treated as constant time in introductory complexity analysis.

Therefore, the time complexity is:

\[
O(1)
\]

## Nested Conditional Expressions

Consider:

```python
result = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "F"
)
```

The program evaluates a fixed number of conditions.

When the number of conditions is fixed, the total time complexity is generally:

\[
O(1)
\]

If the number of conditions grows with the input size, or if a condition performs a more expensive operation, the complexity can be different.

## Conditional Expression with List Membership

Consider:

```python
numbers = [10, 20, 30, 40]
target = 30

result = "Found" if target in numbers else "Not found"
```

The membership check in a Python list may inspect each element.

For a list of `n` elements, the worst-case time complexity is:

\[
O(n)
\]

The conditional expression itself does not make the list search constant time.

## Space Complexity

A simple conditional expression usually uses constant additional space.

Therefore:

\[
O(1)
\]

This assumes the selected expressions do not create additional collections whose sizes grow with the input.

### Important Points

- A simple conditional expression generally takes constant time.
- A fixed number of nested conditional checks generally takes constant time.
- Expensive operations inside a condition affect the overall complexity.
- List membership can take linear time.
- Simple conditional expressions generally use constant additional space.

---

# SECTION 10: MINI PROJECT – STUDENT GRADE AND RESULT SYSTEM

## Project Overview

Create a simple student grade and result system using conditional expressions.

The program should:

1. Accept student marks.
2. Validate the marks.
3. Select a grade.
4. Select a pass or fail result.
5. Display the result.

### Example Grade Rules

| Marks | Grade |
|---|---|
| 90 to 100 | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 40 to below 60 | D |
| Below 40 | F |

The thresholds are illustrative.

## Python Code

```python
marks = float(input("Enter student marks: "))

grade = (
    "Invalid marks" if marks < 0 or marks > 100
    else "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

result = (
    "Invalid result" if marks < 0 or marks > 100
    else "Pass" if marks >= 40
    else "Fail"
)

print("\nSTUDENT RESULT")
print("-------------------------")
print("Marks:", marks)
print("Grade:", grade)
print("Result:", result)
```

## Sample Output 1

```text
Enter student marks: 95

STUDENT RESULT
-------------------------
Marks: 95.0
Grade: A
Result: Pass
```

## Sample Output 2

```text
Enter student marks: 65

STUDENT RESULT
-------------------------
Marks: 65.0
Grade: C
Result: Pass
```

## Sample Output 3

```text
Enter student marks: 25

STUDENT RESULT
-------------------------
Marks: 25.0
Grade: F
Result: Fail
```

## Sample Output 4

```text
Enter student marks: 110

STUDENT RESULT
-------------------------
Marks: 110.0
Grade: Invalid marks
Result: Invalid result
```

## Project Explanation

The program first reads marks from the user.

The grade expression checks whether the marks are outside the accepted range.

If the marks are valid, it checks the grade conditions in order.

The result expression independently checks the passing condition.

Finally, the program displays the marks, grade, and result.

## Project Improvements

After completing the basic version, try these improvements:

1. Accept a student name.
2. Accept marks for multiple subjects.
3. Validate marks for each subject.
4. Calculate the total marks.
5. Calculate the average.
6. Calculate the final grade.
7. Display the student's name with the result.
8. Store student information in a dictionary.
9. Use functions for validation and grade calculation.
10. Use a loop to process multiple students.

### Skills Practiced

- Conditional expressions.
- Chained conditional expressions.
- Numeric validation.
- Arithmetic operations.
- String formatting.
- Variable assignment.
- Program organization.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is a conditional expression?

A conditional expression returns one value when a condition is true and another value when it is false.

### 2. What is another name for a conditional expression?

It is commonly called the ternary operator.

### 3. Why is it called a ternary operator?

Because it contains three main parts: a true expression, a condition, and a false expression.

### 4. What is the basic syntax?

```python
value_if_true if condition else value_if_false
```

### 5. Which keywords are used?

The keywords are `if` and `else`.

### 6. Does a conditional expression return a value?

Yes. It evaluates to the selected expression value.

### 7. Can it be used in variable assignment?

Yes.

Example:

```python
result = "Pass" if marks >= 40 else "Fail"
```

### 8. Can it be used inside print?

Yes.

Example:

```python
print("Adult" if age >= 18 else "Minor")
```

### 9. Does it support only strings?

No. It can return strings, numbers, Boolean values, lists, and other Python objects.

### 10. Does it require an else expression?

Yes. A conditional expression requires both alternatives.

## Intermediate Questions

### 11. What happens when the condition is true?

Python selects and evaluates the true expression.

### 12. What happens when the condition is false?

Python selects and evaluates the false expression.

### 13. Does Python evaluate both branches?

No. Only the selected branch expression is evaluated.

### 14. Can conditional expressions be nested?

Yes. A conditional expression can contain another conditional expression.

### 15. What is a chained conditional expression?

It is a sequence of nested conditional expressions used to select among multiple alternatives.

### 16. Can a conditional expression return an integer?

Yes.

### 17. Can a conditional expression return a Boolean?

Yes.

### 18. Can a conditional expression use logical operators?

Yes. Conditions can contain `and`, `or`, and `not`.

### 19. Can it use comparison operators?

Yes. Operators such as `==`, `!=`, `>`, `<`, `>=`, and `<=` can be used.

### 20. Can it be used with a function call?

Yes. The selected value or function result can be passed to or returned from a function.

## Practical Questions

### 21. How do you check even or odd?

```python
result = "Even" if number % 2 == 0 else "Odd"
```

### 22. How do you check pass or fail?

```python
result = "Pass" if marks >= 40 else "Fail"
```

### 23. How do you find the largest of two numbers?

```python
largest = a if a > b else b
```

### 24. How do you find the minimum of two numbers?

```python
minimum = a if a < b else b
```

### 25. How do you calculate an absolute value?

```python
absolute = number if number >= 0 else -number
```

### 26. How do you classify a number as positive, negative, or zero?

Use a chained conditional expression with two conditions and a final fallback value.

### 27. Can conditional expressions be used for grades?

Yes. They can be used to select a grade based on marks.

### 28. Can conditional expressions calculate discounts?

Yes. They can select a discount rate based on a condition.

### 29. Why are parentheses useful in nested expressions?

They make the grouping and intended structure easier to understand.

### 30. What happens if a comparison condition is false?

The false expression is selected.

## Advanced Questions

### 31. What is the difference between an if statement and a conditional expression?

An `if` statement controls execution of statement blocks, while a conditional expression produces a value.

### 32. Can a conditional expression replace every if-else statement?

No. It is best suited to simple value selection.

### 33. Why should long conditional expressions be avoided?

They can reduce readability and make the code harder to maintain.

### 34. What is a nested conditional expression?

A conditional expression placed inside another conditional expression.

### 35. Can a conditional expression use `and`?

Yes.

### 36. Can a conditional expression use `or`?

Yes.

### 37. Can a conditional expression use `not`?

Yes.

### 38. Can conditional expressions be used with strings?

Yes.

### 39. Can they be used with lists?

Yes. A conditional expression can select a list.

### 40. What is short-circuit evaluation?

Python may stop evaluating a logical expression when the final result is already determined.

## Interview-Oriented Questions

### 41. When should you use a conditional expression?

Use it when selecting between two simple values based on a condition.

### 42. When should you avoid a conditional expression?

Avoid it when the condition or branches become long, complicated, or difficult to read.

### 43. What does a conditional expression return?

It returns the value of the selected branch.

### 44. Is a conditional expression a statement or an expression?

It is an expression.

### 45. What is the time complexity of a simple conditional expression?

Generally `O(1)` when it contains only a fixed number of constant-time operations.

### 46. What is the space complexity of a simple conditional expression?

Generally `O(1)` additional space.

### 47. Can a conditional expression cause a TypeError?

Yes. An evaluated branch or condition can perform an invalid operation.

### 48. Can the unselected branch cause a runtime error?

An error in an unselected branch is generally not triggered because that branch is not evaluated.

### 49. How can nested conditional expressions become clearer?

Use parentheses, line breaks, meaningful names, or normal `if-elif-else` blocks.

### 50. What is the most important best practice?

Use conditional expressions only when they make the logic shorter without reducing readability.

---

# SECTION 12: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Conditional expression | Expression that selects a value based on a condition |
| Ternary operator | Common name for a conditional expression |
| Condition | An expression that determines which branch is selected |
| True expression | Value or expression selected when the condition is true |
| False expression | Value or expression selected when the condition is false |
| Expression | A piece of code that evaluates to a value |
| Statement | An instruction executed by Python |
| Nested expression | An expression contained inside another expression |
| Chained expression | Multiple conditional choices connected through nesting |
| Boolean | A value that is either `True` or `False` |
| Comparison operator | Operator used to compare values |
| Logical operator | Operator used to combine or reverse conditions |
| Assignment | Storing a value in a variable |
| Evaluation | Processing an expression to determine its value |
| Truthy | A value treated as true in a Boolean context |
| Falsy | A value treated as false in a Boolean context |
| Short-circuit evaluation | Stopping evaluation when the final logical result is known |
| TypeError | Error caused by an operation on incompatible types |
| ValueError | Error caused by an invalid value for an operation |
| Readability | How easily a person can understand code |

---

# SECTION 13: QUICK REVISION NOTES

## Main Definition

A conditional expression selects one of two values based on a condition.

## Important Syntax

```python
value_if_true if condition else value_if_false
```

## Basic Example

```python
age = 20

result = "Adult" if age >= 18 else "Minor"
```

## Important Rules

- The true value appears before `if`.
- The condition appears between `if` and `else`.
- The false value appears after `else`.
- Both alternatives are required.
- The expression returns the selected value.
- Only the selected branch is evaluated.
- A conditional expression can be assigned to a variable.
- It can be used inside a function call.
- It can return different data types.
- It can be nested.
- It can be chained for more alternatives.
- Parentheses can make nested expressions clearer.
- Long expressions should generally be avoided.
- Normal `if-elif-else` is better for complicated decisions.

## Important Examples

### Even or Odd

```python
result = "Even" if number % 2 == 0 else "Odd"
```

### Pass or Fail

```python
result = "Pass" if marks >= 40 else "Fail"
```

### Largest of Two

```python
largest = a if a > b else b
```

### Minimum of Two

```python
minimum = a if a < b else b
```

### Absolute Value

```python
absolute = number if number >= 0 else -number
```

### Positive, Negative or Zero

```python
result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)
```

### Grade Selection

```python
grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)
```

## Conditional Expression vs If-Else

| Conditional Expression | If-Else |
|---|---|
| Produces a value | Controls statement execution |
| Suitable for simple choices | Suitable for complex decisions |
| Usually one expression | Can contain multiple statements |
| Compact | Often easier for several actions |

---

# SECTION 14: LEARNING CHECKLIST

Use this checklist after completing the topic.

- [ ] I understand what a conditional expression is.
- [ ] I know why it is called the ternary operator.
- [ ] I understand the basic syntax.
- [ ] I can identify the true expression.
- [ ] I can identify the condition.
- [ ] I can identify the false expression.
- [ ] I understand how Python selects a result.
- [ ] I can use conditional expressions with integers.
- [ ] I can use conditional expressions with floating-point numbers.
- [ ] I can use conditional expressions with strings.
- [ ] I can use conditional expressions with Boolean values.
- [ ] I can use conditional expressions in print statements.
- [ ] I can assign conditional expression results to variables.
- [ ] I can find the largest of two numbers.
- [ ] I can find the minimum of two numbers.
- [ ] I can calculate an absolute value.
- [ ] I can check whether a number is even or odd.
- [ ] I can check whether marks represent pass or fail.
- [ ] I understand nested conditional expressions.
- [ ] I understand chained conditional expressions.
- [ ] I can use logical operators inside conditions.
- [ ] I can use comparison operators inside conditions.
- [ ] I understand the difference between an expression and a statement.
- [ ] I can choose between a conditional expression and if-else.
- [ ] I understand common mistakes.
- [ ] I can debug simple conditional expressions.
- [ ] I understand their real-world applications.
- [ ] I understand their DSA connection.
- [ ] I have attempted all ten unsolved questions.
- [ ] I can explain the topic in an interview.

---

# SECTION 15: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `05-Conditional-Expressions` folder.

Run:

```bash
python 01_ternary_operator.py
```

On Windows, you can also use:

```powershell
py 01_ternary_operator.py
```

The program displays an interactive menu.

## Main Menu

```text
=============================================================
                 PYTHON CONDITIONAL EXPRESSIONS
=============================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

Displays the twelve examples related to conditional expressions.

The examples include:

1. Basic conditional expression.
2. Even or odd.
3. Positive or negative.
4. Largest of two.
5. Pass or fail.
6. Absolute value.
7. Minimum of two.
8. Voting eligibility.
9. Largest of three.
10. Grade calculator.
11. Leap year.
12. Discount calculator.

### Option 2 – Practice 12 Solved Problems

Displays the available solved-problem menu.

You can choose a problem and enter your own values.

The program then evaluates the conditional expression and displays the result.

### Option 3 – View 10 Unsolved Questions

Displays ten questions for independent practice.

Try to solve the questions before looking for help.

### Option 4 – View Learning Checklist

Displays the learning checklist.

Use it to review which concepts you have understood.

### Option 0 – Exit

Closes the program.

---

# SECTION 16: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 05-Conditional-Expressions/
            ├── README.md
            └── 01_ternary_operator.py
```

## File Details

| File | Purpose |
|---|---|
| `README.md` | Complete theory, syntax, examples, solved problems, unsolved questions, and revision notes |
| `01_ternary_operator.py` | Python program containing examples, solved problems, practice questions, checklist, and menu |

## Previous Topic

**04-Nested-If**

In the previous topic, you learned how to place one conditional statement inside another.

You learned dependent decision-making using nested `if` statements.

## Current Topic

**05-Conditional-Expressions**

In this topic, you learned how to select between values using a conditional expression.

You also learned how to write simple nested and chained conditional expressions.

## Next Learning Direction

After completing conditional expressions, continue with the next folder in your approved roadmap.

Do not change the existing folder structure unless you decide to update the roadmap.

---

# FINAL SUMMARY

Conditional expressions are a useful feature of Python.

They allow a program to choose between values based on a condition.

The main syntax is:

```python
value_if_true if condition else value_if_false
```

You should now understand:

1. What conditional expressions are.
2. Why they are called ternary operators.
3. Their syntax and evaluation.
4. How to use them with numbers.
5. How to use them with strings.
6. How to use them with Boolean values.
7. How to use them inside print statements.
8. How to assign their results to variables.
9. How to write nested conditional expressions.
10. How to write chained conditional expressions.
11. How to combine conditions with logical operators.
12. How to choose between conditional expressions and normal if-else statements.
13. How to apply them to programming problems.
14. How they connect with DSA and interview questions.

### Final Advice

Do not use conditional expressions everywhere.

Use them when they make a simple decision easier to read.

When a decision contains several actions or complicated conditions, use normal conditional statements.

The objective is not to write the shortest possible code.

The objective is to write code that is correct, readable, and easy to maintain.

**Keep practising, understand the logic, and maintain the same repository structure throughout your Python learning journey.**

