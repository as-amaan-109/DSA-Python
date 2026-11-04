# Conditional Expressions in Python

## Topic 08.5 – Python Operators and Expressions

**File Name:** `05_conditional_expressions.py`  
**Week:** Week 1 – Programming Fundamentals  
**Section:** 05 – Operators and Expressions  
**Subtopic:** 08 – Expressions

---

# 1. Introduction

Conditional expressions are used in Python to select one of two values based on a condition.

They provide a shorter way to write simple `if-else` decisions inside an expression.

For example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

**Output:**

```text
Adult
```

Python checks whether `age >= 18`.

- If the condition is `True`, it selects `"Adult"`.
- If the condition is `False`, it selects `"Minor"`.

Conditional expressions are also known as **ternary conditional expressions** because they contain three parts:

1. A value or expression for the true case.
2. A condition.
3. A value or expression for the false case.

They are useful when a simple decision needs to produce a value.

---

# 2. What Is a Conditional Expression?

A conditional expression is an expression that evaluates a condition and returns one of two possible values.

Example:

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

**Output:**

```text
Pass
```

Explanation:

- The condition is `marks >= 40`.
- Since `75 >= 40` is `True`, Python selects `"Pass"`.
- The selected string is assigned to `result`.

Another example:

```python
number = 8

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

**Output:**

```text
Even
```

The conditional expression selects a value depending on whether the number is divisible by 2.

---

# 3. Syntax of a Conditional Expression

The general syntax is:

```python
value_if_true if condition else value_if_false
```

There are three important parts.

| Part | Meaning |
|---|---|
| `value_if_true` | Value selected when the condition is True |
| `condition` | Expression evaluated to determine which value to select |
| `value_if_false` | Value selected when the condition is False |

### Example

```python
age = 20

category = "Adult" if age >= 18 else "Minor"
```

Here:

- `"Adult"` is the true-case value.
- `age >= 18` is the condition.
- `"Minor"` is the false-case value.

**Output:**

```text
Adult
```

### Important

The `else` part is compulsory in a conditional expression.

Incorrect:

```python
result = "Pass" if marks >= 40
```

Correct:

```python
result = "Pass" if marks >= 40 else "Fail"
```

A conditional expression must provide a value for both possible outcomes.

---

# 4. How Does a Conditional Expression Work?

Python follows a simple evaluation process.

Consider:

```python
age = 16

result = "Adult" if age >= 18 else "Minor"

print(result)
```

**Output:**

```text
Minor
```

### Step-by-step execution

**Step 1:** Python evaluates the condition.

```python
age >= 18
```

**Step 2:** The values are substituted.

```text
16 >= 18
```

**Step 3:** The condition evaluates to:

```text
False
```

**Step 4:** Python selects the false-case value.

```python
"Minor"
```

**Step 5:** The selected value is assigned to `result`.

Final output:

```text
Minor
```

Only the selected value expression is evaluated.

---

# 5. Conditional Expression Flow

A conditional expression can be represented using a simple decision flow.

```text
          Start
            |
            v
      Evaluate Condition
            |
       Is it True?
        /       \
      Yes        No
       |          |
       v          v
  Select True   Select False
     Value         Value
       |            |
       +-----+------+
             |
             v
        Return Result
```

This flow represents the two possible outcomes of a conditional expression.

---

# 6. Conditional Expression vs If-Else Statement

Both conditional expressions and `if-else` statements are used to make decisions. However, they are used differently.

### Using an if-else statement

```python
marks = 75

if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print(result)
```

**Output:**

```text
Pass
```

### Using a conditional expression

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

**Output:**

```text
Pass
```

Both programs produce the same result.

### Main differences

| Feature | If-Else Statement | Conditional Expression |
|---|---|---|
| Purpose | Controls program execution | Produces a selected value |
| Syntax | Uses separate blocks | Written as one expression |
| `else` | Required for a complete if-else | Compulsory |
| Multiple statements | Supports multiple statements in each block | Each branch is an expression |
| Readability | Better for complex logic | Better for simple decisions |
| Assignment | Usually assigns inside a branch | Can directly assign the result |
| Best use | Complex decision-making | Short value selection |

### Important rule

Use `if-else` statements when the logic is complex or when multiple statements must run in each branch.

Use conditional expressions when a simple condition selects one value.

---

# 7. Basic Conditional Expression Example

Program:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print("Age:", age)
print("Category:", result)
```

**Output:**

```text
Age: 20
Category: Adult
```

Explanation:

1. The age is 20.
2. Python checks whether the age is at least 18.
3. The condition is true.
4. `"Adult"` is selected.
5. The result is printed.

---

# 8. Conditional Expression With Even and Odd Numbers

The modulo operator `%` returns the remainder after division.

A number is even when it is divisible by 2 without a remainder.

Program:

```python
number = 15

result = "Even" if number % 2 == 0 else "Odd"

print("Number:", number)
print("Result:", result)
```

**Output:**

```text
Number: 15
Result: Odd
```

### Dry run

```text
number = 15

15 % 2 == 0

1 == 0

False
```

Since the condition is false, Python selects `"Odd"`.

### Try another value

```python
number = 12

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

**Output:**

```text
Even
```

---

# 9. Conditional Expression With Positive and Negative Numbers

A conditional expression can also classify numbers.

Program:

```python
number = -10

result = "Positive" if number > 0 else "Negative or Zero"

print(result)
```

**Output:**

```text
Negative or Zero
```

This example has only two possible outcomes:

- Positive when the number is greater than zero.
- Negative or Zero otherwise.

To classify positive, negative and zero separately, use a nested conditional expression.

```python
number = 0

result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

print(result)
```

**Output:**

```text
Zero
```

---

# 10. Conditional Expression With Comparison Operators

Comparison operators return Boolean values: `True` or `False`.

Common comparison operators:

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
a = 25
b = 40

result = a if a > b else b

print("Greater number:", result)
```

**Output:**

```text
Greater number: 40
```

Python checks `a > b`.

Since 25 is not greater than 40, the false-case value `b` is selected.

Another example:

```python
a = 15
b = 8

result = a if a < b else b

print("Smaller number:", result)
```

**Output:**

```text
Smaller number: 8
```

---

# 11. Find the Greater of Two Numbers

One practical use of conditional expressions is finding the greater of two numbers.

Program:

```python
a = 25
b = 40

greater = a if a > b else b

print("First number:", a)
print("Second number:", b)
print("Greater number:", greater)
```

**Output:**

```text
First number: 25
Second number: 40
Greater number: 40
```

### Dry run

| Step | Operation | Result |
|---|---|---|
| 1 | `a = 25` | 25 |
| 2 | `b = 40` | 40 |
| 3 | `a > b` | False |
| 4 | Select false-case value | `b` |
| 5 | Final result | 40 |

### Important

When both values are equal, the expression selects `b` because the condition `a > b` is false.

If you want a particular tie-handling rule, choose the comparison operator accordingly.

---

# 12. Find the Smaller of Two Numbers

The same technique can find the smaller value.

Program:

```python
a = 15
b = 8

smaller = a if a < b else b

print("Smaller number:", smaller)
```

**Output:**

```text
Smaller number: 8
```

Explanation:

- Python checks whether `a < b`.
- The condition is false.
- Therefore, it selects `b`.

---

# 13. Conditional Expression With Pass or Fail

Conditional expressions are useful in student result programs.

Program:

```python
marks = 65

result = "Pass" if marks >= 40 else "Fail"

print("Marks:", marks)
print("Result:", result)
```

**Output:**

```text
Marks: 65
Result: Pass
```

### Condition

```python
marks >= 40
```

If marks are 40 or above, the result is `"Pass"`.

Otherwise, it is `"Fail"`.

### More test cases

| Marks | Condition | Result |
|---:|---|---|
| 85 | True | Pass |
| 60 | True | Pass |
| 40 | True | Pass |
| 39 | False | Fail |
| 20 | False | Fail |

This example uses a simple pass threshold. Actual academic grading rules may differ.

---

# 14. Conditional Expression for Absolute Value

Absolute value represents the non-negative magnitude of a number.

Examples:

```text
Absolute value of 10 = 10
Absolute value of -10 = 10
Absolute value of 0 = 0
```

Python program:

```python
number = -25

absolute_value = number if number >= 0 else -number

print("Original number:", number)
print("Absolute value:", absolute_value)
```

**Output:**

```text
Original number: -25
Absolute value: 25
```

### Explanation

- If the number is zero or positive, select the number itself.
- Otherwise, select its negation.

Python also provides the built-in `abs()` function:

```python
number = -25

print(abs(number))
```

**Output:**

```text
25
```

The conditional expression example helps demonstrate how a value can be selected based on a condition.

---

# 15. Conditional Expression for Discount Calculation

Conditional expressions can select a price depending on whether a discount applies.

Suppose a shop offers a 10% discount when the price is at least 1000.

Program:

```python
price = 2000

final_price = price * 0.90 if price >= 1000 else price

print("Original price:", price)
print("Final price:", final_price)
```

**Output:**

```text
Original price: 2000
Final price: 1800.0
```

### Explanation

The condition is:

```python
price >= 1000
```

Since the price is 2000, the condition is true.

The selected expression is:

```python
price * 0.90
```

Calculation:

```text
2000 * 0.90 = 1800
```

If the price were 800, the original price would be selected.

---

# 16. Nested Conditional Expressions

A nested conditional expression is a conditional expression placed inside another conditional expression.

It is useful when more than two possible values must be selected.

Syntax:

```python
result = (
    value_1 if condition_1
    else value_2 if condition_2
    else value_3
)
```

Example:

```python
marks = 85

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print("Grade:", grade)
```

**Output:**

```text
Grade: B
```

### Explanation

Python checks conditions in order:

1. Is marks at least 90? No.
2. Is marks at least 75? Yes.
3. Select `"B"`.

The remaining branches are not evaluated.

---

# 17. Grade Calculation Using Nested Conditional Expressions

Consider these grade criteria:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89 | B |
| 60–74 | C |
| 40–59 | D |
| Below 40 | F |

Program:

```python
marks = 85

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

**Output:**

```text
Marks: 85
Grade: B
```

### Dry run

| Step | Condition | Result |
|---|---|---|
| 1 | `marks >= 90` | False |
| 2 | `marks >= 75` | True |
| 3 | Select grade | B |

### Important

Conditions should be arranged carefully.

For example, checking `marks >= 40` first would cause every mark of 40 or above to receive grade D, even when a higher grade is appropriate.

---

# 18. Conditional Expression With Logical Operators

Logical operators can be used inside the condition.

Python has three main logical operators:

| Operator | Meaning |
|---|---|
| `and` | True when both conditions are true |
| `or` | True when at least one condition is true |
| `not` | Reverses the truth value |

Example:

```python
age = 20
has_id = True

result = (
    "Allowed"
    if age >= 18 and has_id
    else "Not Allowed"
)

print(result)
```

**Output:**

```text
Allowed
```

Explanation:

- `age >= 18` is `True`.
- `has_id` is `True`.
- The combined `and` condition is `True`.
- Therefore, `"Allowed"` is selected.

---

# 19. Conditional Expression With Multiple Conditions

Example:

```python
marks = 80
attendance = 85

result = (
    "Eligible"
    if marks >= 40 and attendance >= 75
    else "Not Eligible"
)

print(result)
```

**Output:**

```text
Eligible
```

Both conditions must be true.

Another example using `or`:

```python
is_member = False
has_coupon = True

discount_available = (
    "Yes" if is_member or has_coupon else "No"
)

print(discount_available)
```

**Output:**

```text
Yes
```

At least one condition must be true for the `or` expression to be true.

---

# 20. Conditional Expression Inside print()

A conditional expression can be used directly inside a function call.

Example:

```python
temperature = 35

print(
    "Weather:",
    "Hot" if temperature >= 30 else "Normal"
)
```

**Output:**

```text
Weather: Hot
```

Python evaluates the conditional expression before passing its selected value to `print()`.

Another example:

```python
number = 12

print("Result:", "Even" if number % 2 == 0 else "Odd")
```

**Output:**

```text
Result: Even
```

This is useful when a selected value only needs to be displayed.

---

# 21. Conditional Expression Inside a Function Argument

Conditional expressions can be passed as arguments to functions.

Example:

```python
number = -15

print(abs(number) if number < 0 else number)
```

**Output:**

```text
15
```

The conditional expression selects a value first, and the selected value is passed to `print()`.

Another example:

```python
marks = 75

print("Grade:", "Pass" if marks >= 40 else "Fail")
```

**Output:**

```text
Grade: Pass
```

---

# 22. Conditional Expression With String Values

Strings can also be selected based on conditions.

Example:

```python
name = ""

display_name = name if name else "Guest"

print(display_name)
```

**Output:**

```text
Guest
```

An empty string is considered false in a Boolean context.

Another example:

```python
name = "Amaan"

display_name = name if name else "Guest"

print(display_name)
```

**Output:**

```text
Amaan
```

A non-empty string is truthy, so the original name is selected.

### Important

The condition does not always have to be a comparison.

Python can test the truth value of many objects directly.

---

# 23. Truthy and Falsy Values

Python treats certain values as false when they are tested in a condition.

Common falsy values include:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Most other values are truthy.

Example:

```python
name = ""

result = name if name else "Guest"

print(result)
```

**Output:**

```text
Guest
```

Another example:

```python
name = "Python"

result = name if name else "Guest"

print(result)
```

**Output:**

```text
Python
```

### Practical use

This is helpful when selecting default values.

```python
username = ""

display_name = username if username else "Anonymous"
```

However, be careful when zero or an empty collection is a valid value in your program. In that situation, test the exact condition you need rather than relying on truthiness.

---

# 24. Conditional Expression and None

Sometimes a variable may contain `None`.

Example:

```python
username = None

display_name = username if username is not None else "Guest"

print(display_name)
```

**Output:**

```text
Guest
```

This example checks specifically for `None`.

Another example:

```python
value = 0

result = value if value is not None else 100

print(result)
```

**Output:**

```text
0
```

Here, zero is preserved because the condition checks whether the value is `None`, not whether it is truthy.

### Important difference

Compare:

```python
value = 0

result_1 = value if value else 100
result_2 = value if value is not None else 100

print(result_1)
print(result_2)
```

**Output:**

```text
100
0
```

Choose the condition according to the actual requirement.

---

# 25. Conditional Expression in List Comprehension

A conditional expression can be used inside a list comprehension to select a value for every element.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(labels)
```

**Output:**

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
```

### Explanation

For every number:

- Python checks whether it is divisible by 2.
- It selects `"Even"` or `"Odd"`.
- The selected value is added to the new list.

### Important distinction

A conditional expression selects a value for each item.

A comprehension filter decides whether an item should be included.

Conditional expression:

```python
result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]
```

Comprehension with a filter:

```python
result = [
    number
    for number in numbers
    if number % 2 == 0
]
```

These two expressions perform different tasks.

---

# 26. Conditional Expression in Dictionary Values

A conditional expression can also select dictionary values.

Example:

```python
marks = 85

student = {
    "name": "Amaan",
    "marks": marks,
    "result": "Pass" if marks >= 40 else "Fail"
}

print(student)
```

**Output:**

```text
{'name': 'Amaan', 'marks': 85, 'result': 'Pass'}
```

This is useful when creating structured data based on conditions.

---

# 27. Conditional Expression in a Leap Year Check

A leap year follows these rules:

1. A year divisible by 400 is a leap year.
2. Otherwise, a year divisible by 100 is not a leap year.
3. Otherwise, a year divisible by 4 is a leap year.
4. All other years are not leap years.

The Boolean condition is:

```python
(year % 400 == 0) or (
    year % 4 == 0 and year % 100 != 0
)
```

Program:

```python
year = 2024

is_leap_year = (
    (year % 400 == 0)
    or
    (year % 4 == 0 and year % 100 != 0)
)

result = "Leap Year" if is_leap_year else "Not a Leap Year"

print(result)
```

**Output:**

```text
Leap Year
```

This example combines:

- Arithmetic operators.
- Comparison operators.
- Logical operators.
- A conditional expression.

---

# 28. Conditional Expression for Delivery Charges

Suppose an online shop provides free delivery for orders of 500 or more.

Otherwise, the delivery charge is 50.

Program:

```python
order_amount = 350

delivery_charge = 0 if order_amount >= 500 else 50

total_amount = order_amount + delivery_charge

print("Order amount:", order_amount)
print("Delivery charge:", delivery_charge)
print("Total amount:", total_amount)
```

**Output:**

```text
Order amount: 350
Delivery charge: 50
Total amount: 400
```

If the order amount is 600, the delivery charge becomes zero.

Conditional expressions are useful for selecting small values in billing applications.

---

# 29. Conditional Expression for User Input

Conditional expressions can work with values entered by the user.

Example:

```python
age = int(input("Enter your age: "))

category = "Adult" if age >= 18 else "Minor"

print("Category:", category)
```

### Sample Input

```text
Enter your age: 22
```

### Output

```text
Category: Adult
```

Another example:

```python
number = int(input("Enter a number: "))

result = "Positive" if number > 0 else "Not Positive"

print(result)
```

The selected value depends on the user's input.

---

# 30. Evaluation Order and Short-Circuit Behavior

A conditional expression evaluates its condition first and then evaluates only the selected branch.

Example:

```python
condition = True

result = "Selected" if condition else 10 / 0

print(result)
```

**Output:**

```text
Selected
```

No `ZeroDivisionError` occurs because the false-case expression is not evaluated.

Now consider:

```python
condition = False

result = "Selected" if condition else 10 / 0
```

This time, Python attempts to evaluate `10 / 0`, resulting in:

```text
ZeroDivisionError
```

### Important

Only one of the two result expressions is evaluated.

This behavior is useful when one branch contains an operation that should only run under a particular condition.

---

# 31. Nested Conditional Expressions: Evaluation Order

Consider:

```python
marks = 55

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print(grade)
```

**Output:**

```text
D
```

Python interprets the expression as a chain of conditional expressions:

```python
grade = (
    "A" if marks >= 90
    else (
        "B" if marks >= 75
        else (
            "C" if marks >= 60
            else (
                "D" if marks >= 40
                else "F"
            )
        )
    )
)
```

### Dry run

| Step | Condition | Result |
|---|---|---|
| 1 | `55 >= 90` | False |
| 2 | `55 >= 75` | False |
| 3 | `55 >= 60` | False |
| 4 | `55 >= 40` | True |
| 5 | Selected value | D |

Nested conditional expressions are valid, but too many levels can make code difficult to read.

---

# 32. Conditional Expression vs Logical AND and OR

Conditional expressions and logical operators are not interchangeable.

Consider:

```python
condition = True

result = "Yes" if condition else "No"

print(result)
```

**Output:**

```text
Yes
```

Now consider:

```python
condition = True

result = condition and "Yes"

print(result)
```

**Output:**

```text
Yes
```

These examples happen to produce the same displayed value, but their behavior is different.

The `and` and `or` operators return one of their operands, while a conditional expression selects one of two branches based on its condition.

Example:

```python
value = 0

result_1 = value or 100
result_2 = value if value is not None else 100

print(result_1)
print(result_2)
```

**Output:**

```text
100
0
```

Understanding this difference prevents bugs involving zero, empty strings and other falsy values.

---

# 33. Common Mistakes in Conditional Expressions

### Mistake 1: Forgetting else

Incorrect:

```python
result = "Pass" if marks >= 40
```

Correct:

```python
result = "Pass" if marks >= 40 else "Fail"
```

### Mistake 2: Writing the syntax in the wrong order

Incorrect:

```python
result = if marks >= 40 "Pass" else "Fail"
```

Correct:

```python
result = "Pass" if marks >= 40 else "Fail"
```

### Mistake 3: Using assignment instead of comparison

Incorrect when checking equality:

```python
result = "Equal" if a = b else "Not Equal"
```

Correct:

```python
result = "Equal" if a == b else "Not Equal"
```

### Mistake 4: Incorrect nested condition order

Incorrect for the intended descending grade thresholds:

```python
grade = (
    "D" if marks >= 40
    else "A" if marks >= 90
    else "F"
)
```

Correct:

```python
grade = (
    "A" if marks >= 90
    else "D" if marks >= 40
    else "F"
)
```

### Mistake 5: Making the expression unnecessarily complicated

Difficult to read:

```python
result = "A" if a > b else "B" if b > c else "C" if c > d else "D"
```

A normal `if-elif-else` statement may be clearer when there are many conditions.

### Mistake 6: Not handling equal values

Example:

```python
a = 10
b = 10

result = a if a > b else b

print(result)
```

**Output:**

```text
10
```

The expression still returns a value, but it does not explicitly identify that both values are equal.

When equality matters, handle it separately or use a suitable comparison.

---

# 34. Best Practices

Follow these practices while writing conditional expressions:

1. Use conditional expressions for simple decisions.
2. Always include the `else` branch.
3. Keep both selected expressions easy to understand.
4. Use meaningful variable names.
5. Arrange nested conditions in the correct order.
6. Avoid unnecessary nested conditional expressions.
7. Use ordinary `if-else` statements for complex logic.
8. Test both true and false outcomes.
9. Handle edge cases such as zero and empty strings.
10. Use parentheses when they improve readability.
11. Understand the difference between truthiness and checking for `None`.
12. Do not use conditional expressions merely to shorten code when doing so reduces clarity.

### Good example

```python
marks = 85

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

This is simple, clear and easy to understand.

---

# 35. Debugging Conditional Expressions

Common errors include:

| Error | Possible Reason |
|---|---|
| `SyntaxError` | Incorrect conditional expression syntax |
| `NameError` | Variable used before being defined |
| `TypeError` | Incompatible comparison or operation |
| Incorrect result | Wrong condition or branch order |
| Unexpected default value | Truthiness used when a specific check was needed |

### Debugging example

```python
marks = 75

condition = marks >= 40

print("Marks:", marks)
print("Condition:", condition)

result = "Pass" if condition else "Fail"

print("Final Result:", result)
```

**Output:**

```text
Marks: 75
Condition: True
Final Result: Pass
```

### Debugging technique

Break a complicated expression into smaller parts.

Instead of:

```python
result = "Eligible" if age >= 18 and marks >= 40 and has_id else "Not Eligible"
```

You can write:

```python
age_condition = age >= 18
marks_condition = marks >= 40

overall_condition = age_condition and marks_condition and has_id

result = "Eligible" if overall_condition else "Not Eligible"
```

This makes it easier to inspect each condition.

---

# 36. Step-by-Step Dry Run

Consider:

```python
number = 12

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

**Output:**

```text
Even
```

### Dry run table

| Step | Operation | Result |
|---|---|---|
| 1 | `number = 12` | 12 |
| 2 | `number % 2` | 0 |
| 3 | `0 == 0` | True |
| 4 | Select true-case value | Even |
| 5 | Print result | Even |

### Another dry run

Expression:

```python
marks = 55

result = (
    "Excellent" if marks >= 90
    else "Good" if marks >= 60
    else "Needs Improvement"
)
```

| Step | Condition | Result |
|---|---|---|
| 1 | `55 >= 90` | False |
| 2 | `55 >= 60` | False |
| 3 | Select final else value | Needs Improvement |

Final result:

```text
Needs Improvement
```

---

# 37. Practical Applications

Conditional expressions are useful in different programming applications.

### 1. Student result systems

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"
```

### 2. Shopping applications

```python
price = 1500

discount = 150 if price >= 1000 else 0
```

### 3. Online delivery systems

```python
order_amount = 750

delivery_charge = 0 if order_amount >= 500 else 50
```

### 4. Login systems

```python
is_logged_in = True

message = "Welcome" if is_logged_in else "Please Login"
```

### 5. Number classification

```python
number = -5

result = "Negative" if number < 0 else "Non-negative"
```

### 6. Default values

```python
username = ""

display_name = username if username else "Guest"
```

### 7. Data processing

```python
numbers = [1, 2, 3, 4]

labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
```

---

# 38. Conditional Expressions and DSA

Conditional expressions are useful in Data Structures and Algorithms because algorithms frequently need to select values based on conditions.

### 1. Binary Search

```python
left = 0
right = 9

mid = left + ((right - left) // 2) if left <= right else -1

print(mid)
```

**Output:**

```text
4
```

The expression selects the middle index when the search range is valid. Otherwise, it selects `-1`.

### 2. Finding the Maximum

```python
a = 10
b = 20

maximum = a if a > b else b

print(maximum)
```

### 3. Even and Odd Classification

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(result)
```

### 4. Selecting a Valid Index

```python
index = 3
size = 10

valid_index = index if 0 <= index < size else -1

print(valid_index)
```

### 5. Choosing a Result Based on a Condition

```python
score = 85

status = "Success" if score >= 50 else "Retry"

print(status)
```

Conditional expressions support concise value selection inside algorithmic logic.

---

# 39. Mini Project – Student Result and Grade Calculator

Create a small program that accepts student marks and calculates a result and grade.

### Project requirements

1. Accept marks from the user.
2. Validate the marks between 0 and 100.
3. Select Pass or Fail.
4. Calculate a grade using nested conditional expressions.
5. Display the final result.

### Python Program

```python
print("STUDENT RESULT AND GRADE CALCULATOR")

marks = float(input("Enter marks between 0 and 100: "))

if not 0 <= marks <= 100:
    print("Invalid marks! Enter a value from 0 to 100.")

else:
    result = "Pass" if marks >= 40 else "Fail"

    grade = (
        "A" if marks >= 90
        else "B" if marks >= 75
        else "C" if marks >= 60
        else "D" if marks >= 40
        else "F"
    )

    print("\n----- STUDENT RESULT -----")
    print("Marks:", marks)
    print("Result:", result)
    print("Grade:", grade)

    print("-------------------------")
```

### Sample Input

```text
STUDENT RESULT AND GRADE CALCULATOR

Enter marks between 0 and 100: 85
```

### Output

```text
----- STUDENT RESULT -----
Marks: 85.0
Result: Pass
Grade: B
-------------------------
```

### Project concepts

- User input
- Type conversion
- Comparison operators
- Conditional expressions
- Nested conditional expressions
- Input validation
- Displaying results

**Challenge:** Extend the project to accept marks for multiple subjects and calculate the average before assigning the grade.

---

# 40. Practice Test

Try answering these questions without checking the answers.

### Question 1

What is the output?

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

### Question 2

What is the output?

```python
number = 15

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

### Question 3

What is the output?

```python
a = 10
b = 20

result = a if a > b else b

print(result)
```

### Question 4

What is the output?

```python
marks = 35

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

### Question 5

What is the output?

```python
number = -10

result = "Positive" if number > 0 else "Negative or Zero"

print(result)
```

### Question 6

What is the output?

```python
value = 0

result = value or 100

print(result)
```

### Question 7

What is the output?

```python
value = 0

result = value if value is not None else 100

print(result)
```

### Question 8

What is the output?

```python
marks = 85

grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"

print(grade)
```

### Question 9

What is the output?

```python
is_logged_in = False

message = "Welcome" if is_logged_in else "Please Login"

print(message)
```

### Question 10

What is the output?

```python
numbers = [1, 2, 3, 4]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)
```

## Practice Test Answers

| Question | Answer |
|---|---|
| 1 | `Adult` |
| 2 | `Odd` |
| 3 | `20` |
| 4 | `Fail` |
| 5 | `Negative or Zero` |
| 6 | `100` |
| 7 | `0` |
| 8 | `B` |
| 9 | `Please Login` |
| 10 | `['Odd', 'Even', 'Odd', 'Even']` |

---

# 41. Viva Questions and Answers

## Basic Questions

**Q1. What is a conditional expression in Python?**

A conditional expression selects one of two values based on a condition.

**Q2. What is another name for a conditional expression?**

Ternary conditional expression.

**Q3. Why is it called a ternary expression?**

Because it contains three parts: a true-case expression, a condition and a false-case expression.

**Q4. What is the syntax of a conditional expression?**

```python
value_if_true if condition else value_if_false
```

**Q5. Which keyword is compulsory in a conditional expression?**

`else`.

**Q6. Can a conditional expression be used in an assignment?**

Yes.

**Q7. Can a conditional expression return a string?**

Yes.

**Q8. Can it return an integer?**

Yes.

**Q9. Can it return a Boolean value?**

Yes.

**Q10. Can it return a floating-point value?**

Yes.

## Intermediate Questions

**Q11. What happens when the condition is True?**

Python evaluates and returns the true-case expression.

**Q12. What happens when the condition is False?**

Python evaluates and returns the false-case expression.

**Q13. Does Python evaluate both result branches?**

No. Only the selected branch is evaluated.

**Q14. What is the difference between an if-else statement and a conditional expression?**

An if-else statement controls execution blocks, while a conditional expression produces a value.

**Q15. Can conditional expressions be nested?**

Yes.

**Q16. What is a nested conditional expression?**

A conditional expression placed inside another conditional expression.

**Q17. Can comparison operators be used in conditional expressions?**

Yes.

**Q18. Can logical operators be used in the condition?**

Yes.

**Q19. Can conditional expressions be used inside print()?**

Yes.

**Q20. Can they be used in list comprehensions?**

Yes.

## Logical and Practical Questions

**Q21. What are the three main logical operators in Python?**

`and`, `or` and `not`.

**Q22. What does the `and` operator do?**

It returns a truthy or falsy operand according to whether the left operand is truthy; it evaluates the right operand only when necessary.

**Q23. What does the `or` operator do?**

It returns a truthy or falsy operand according to whether the left operand is truthy; it evaluates the right operand only when necessary.

**Q24. What is a truthy value?**

A value that evaluates to True in a Boolean context.

**Q25. What is a falsy value?**

A value that evaluates to False in a Boolean context.

**Q26. Give examples of falsy values.**

`False`, `None`, `0`, `0.0`, `""`, `[]`, `{}` and `()`.

**Q27. How can a conditional expression select a default name?**

```python
name = name if name else "Guest"
```

**Q28. How do you select a value only when it is not None?**

```python
value = value if value is not None else default
```

**Q29. Can a conditional expression check even and odd numbers?**

Yes, using the modulo operator.

**Q30. Can it find the larger of two numbers?**

Yes.

## Advanced Questions

**Q31. What happens if else is missing from a conditional expression?**

Python reports a syntax error.

**Q32. Can functions be called inside conditional expressions?**

Yes.

**Q33. Can conditional expressions be passed as function arguments?**

Yes.

**Q34. Can conditional expressions be used in dictionary values?**

Yes.

**Q35. How are multiple outcomes handled using conditional expressions?**

By nesting conditional expressions.

**Q36. Why should complex nested expressions be avoided?**

They can reduce readability and make debugging difficult.

**Q37. What is the difference between a conditional expression and the `or` operator?**

A conditional expression selects one of two explicit branches, while `or` returns one of its operands based on truthiness.

**Q38. What is the difference between a conditional expression and a list comprehension filter?**

A conditional expression selects a value; a filter controls whether an item is included.

**Q39. What is short-circuit behavior in a conditional expression?**

Only the selected result expression is evaluated.

**Q40. Can a conditional expression cause a ZeroDivisionError?**

Yes, if the selected branch attempts division by zero.

## Interview-Level Questions

**Q41. Write a conditional expression to check whether a number is even or odd.**

```python
result = "Even" if number % 2 == 0 else "Odd"
```

**Q42. Write a conditional expression to find the greater of two numbers.**

```python
greater = a if a > b else b
```

**Q43. Write a conditional expression to check whether marks are at least 40.**

```python
result = "Pass" if marks >= 40 else "Fail"
```

**Q44. Write a nested conditional expression to classify positive, negative and zero.**

```python
result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)
```

**Q45. What is the output of `10 if True else 20`?**

`10`.

**Q46. What is the output of `10 if False else 20`?**

`20`.

**Q47. Can a conditional expression return a list?**

Yes, either branch can evaluate to a list.

**Q48. What is the advantage of conditional expressions in DSA?**

They allow concise value selection in algorithms and data-processing expressions.

**Q49. When should an ordinary if-else statement be preferred?**

When the decision involves multiple statements, complex logic or several operations in each branch.

**Q50. What is the most important rule when using conditional expressions?**

Keep the condition and both possible outcomes clear, correct and easy to understand.

---

# 42. Important Glossary

| Term | Meaning |
|---|---|
| Conditional Expression | An expression that selects a value based on a condition |
| Ternary Expression | Another name for a conditional expression |
| Condition | An expression that determines which value is selected |
| True Branch | The expression selected when the condition is True |
| False Branch | The expression selected when the condition is False |
| Nested Conditional | A conditional expression inside another conditional expression |
| Boolean | A data type with the values `True` and `False` |
| Truthy | A value that behaves as True in a Boolean context |
| Falsy | A value that behaves as False in a Boolean context |
| Comparison Operator | An operator that compares two values |
| Logical Operator | An operator used to combine or reverse conditions |
| Short-Circuit Evaluation | Evaluating only the necessary part of an expression |
| List Comprehension | A concise way to create a list from an iterable |
| Default Value | A fallback value selected when a preferred value is unavailable |

---

# 43. Quick Revision Notes

Remember these important points:

1. Conditional expressions select values based on conditions.
2. They are also called ternary conditional expressions.
3. The `else` part is compulsory.
4. The true-case expression is evaluated when the condition is true.
5. The false-case expression is evaluated when the condition is false.
6. Only the selected result expression is evaluated.
7. They can be used in assignments.
8. They can be used inside function calls.
9. They can be used in list comprehensions.
10. Nested conditional expressions can handle multiple outcomes.
11. Truthy and falsy values can be used directly as conditions.
12. `None` checks are different from truthiness checks.
13. Conditional expressions are useful for simple decisions.
14. Use ordinary `if-else` statements for complex logic.
15. Always test both outcomes.

### Important Syntax

```python
result = value_if_true if condition else value_if_false
```

### Important Examples

```python
# Even or Odd
result = "Even" if number % 2 == 0 else "Odd"

# Adult or Minor
result = "Adult" if age >= 18 else "Minor"

# Pass or Fail
result = "Pass" if marks >= 40 else "Fail"

# Greater of Two Numbers
result = a if a > b else b

# Positive, Negative or Zero
result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

# Default Name
result = name if name else "Guest"

# Check for None
result = value if value is not None else default
```

---

# 44. Learning Checklist

Complete the checklist after studying the topic.

- [ ] Understand the meaning of a conditional expression.
- [ ] Learn its complete syntax.
- [ ] Understand the three parts of the expression.
- [ ] Understand how the condition is evaluated.
- [ ] Understand true-case and false-case values.
- [ ] Differentiate conditional expressions from if-else statements.
- [ ] Use conditional expressions with integers.
- [ ] Use conditional expressions with strings.
- [ ] Use comparison operators in conditions.
- [ ] Use logical operators in conditions.
- [ ] Check even and odd numbers.
- [ ] Find the greater and smaller of two numbers.
- [ ] Classify positive, negative and zero values.
- [ ] Calculate pass or fail results.
- [ ] Apply conditional expressions in discount calculations.
- [ ] Understand nested conditional expressions.
- [ ] Use conditional expressions for grade calculation.
- [ ] Understand truthy and falsy values.
- [ ] Understand the difference between truthiness and `None`.
- [ ] Use conditional expressions in list comprehensions.
- [ ] Understand short-circuit evaluation.
- [ ] Identify common mistakes.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved practice questions.
- [ ] Complete the mini project.
- [ ] Revise all 50 viva questions.

---

# 45. How to Run the Python File

Open the terminal in the `05-conditional-expressions` folder.

Run:

```bash
python 05_conditional_expressions.py
```

The program displays the following menu:

```text
=============================================================
              PYTHON - CONDITIONAL EXPRESSIONS
=============================================================

1. View 12 Topic Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit

Enter your choice:
```

### Menu Details

| Option | Function |
|---|---|
| 1 | Displays all 12 examples |
| 2 | Opens the 12 solved problems |
| 3 | Displays 10 unsolved questions |
| 4 | Displays the learning checklist |
| 0 | Exits the program |

---

# 46. Folder Structure

The current topic folder should look like this:

```text
05-conditional-expressions/
│
├── 05_conditional_expressions.py
│
└── README.md
```

### File Responsibilities

**05_conditional_expressions.py**

Contains:

- 12 conditional expression examples.
- 12 solved programming problems.
- 10 unsolved practice questions.
- Learning checklist.
- Interactive main menu.
- Input validation and helper functions.

**README.md**

Contains:

- Complete topic introduction.
- Conditional expression syntax.
- Theory and explanations.
- Code examples with outputs.
- Step-by-step dry runs.
- Nested conditional expressions.
- Truthy and falsy values.
- Common mistakes and debugging.
- Practical applications.
- DSA relevance.
- Mini project.
- Practice test.
- 50 viva and interview questions.
- Learning checklist.
- Execution instructions.

---

# 47. Previous and Next Topics

### Previous Topic

**08.4 – Parentheses and Grouping**

Folder:

```text
04-parentheses-and-grouping/
```

### Current Topic

**08.5 – Conditional Expressions**

Folder:

```text
05-conditional-expressions/
```

### Section Completion

This is the final subtopic under:

**08 – Expressions**

The complete `08-Expressions` section contains:

```text
08-Expressions/
│
├── README.md
│
├── 01-expressions/
│
├── 02-operator-precedence/
│
├── 03-operator-associativity/
│
├── 04-parentheses-and-grouping/
│
└── 05-conditional-expressions/
```

---

# 48. Final Summary

Conditional expressions are an important part of Python because they allow programmers to select values using conditions.

In this topic, you studied:

- Meaning and syntax of conditional expressions.
- Difference between conditional expressions and if-else statements.
- Working and evaluation order.
- Comparison and logical operators.
- Even and odd checking.
- Positive, negative and zero classification.
- Greater and smaller number selection.
- Pass and fail calculations.
- Discount calculations.
- Nested conditional expressions.
- Truthy and falsy values.
- Default values and `None`.
- Conditional expressions in list comprehensions.
- Short-circuit behavior.
- Common mistakes and debugging.
- Practical applications and DSA relevance.

### Final Advice

Do not use conditional expressions only to write shorter code. Understand how the condition works, which branch is selected, and why Python returns that value.

Practice simple conditions first, then move to nested conditional expressions and real-world problems.

**With this topic, you have completed all five subtopics under 08 – Expressions. Keep practicing and continue building your Python and DSA foundation.**