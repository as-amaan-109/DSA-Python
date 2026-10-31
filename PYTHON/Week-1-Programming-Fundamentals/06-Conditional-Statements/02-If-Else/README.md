# Python If-Else Statement – Complete Detailed Guide

## Week 1 – Programming Fundamentals

**Section:** 06 – Conditional Statements  
**Topic:** 02 – If-Else Statement  
**Python File:** `01_if_else.py`  
**Documentation File:** `README.md`  
**Level:** Beginner to Intermediate

---

# Table of Contents

1. Introduction to Conditional Statements
2. What Is Decision-Making?
3. What Is an If-Else Statement?
4. Why Do We Need If-Else?
5. Syntax of If-Else
6. Components of If-Else
7. How If-Else Works
8. True and False Execution Paths
9. Difference Between If and If-Else
10. Difference Between Multiple If and If-Else
11. Boolean Values in If-Else
12. Truthy and Falsy Values
13. Comparison Operators
14. Arithmetic Operators in Conditions
15. Logical Operators in Conditions
16. Membership Operators
17. Identity Operators
18. Indentation and Code Blocks
19. The Else Clause
20. If-Else With User Input
21. If-Else With Integer Values
22. If-Else With Floating-Point Values
23. If-Else With Strings
24. If-Else With Lists and Collections
25. If-Else With Functions
26. If-Else With Nested Conditions
27. If-Else With Multiple Conditions
28. If-Else and Short-Circuit Evaluation
29. If-Else in Real-World Applications
30. Explanation of 12 Topic Examples
31. Twelve Solved Programming Problems
32. Ten Unsolved Practice Questions
33. Dry Runs and Trace Tables
34. Algorithms and Flowcharts
35. Common Programming Mistakes
36. Debugging Techniques
37. Best Practices
38. Practical Applications
39. If-Else in Data Structures
40. If-Else in Data Structures and Algorithms
41. Time and Space Complexity
42. Mini Project – Shopping Bill Calculator
43. Practice Test
44. Viva and Interview Questions
45. Important Glossary
46. Quick Revision Notes
47. Learning Checklist
48. How to Run the Python Program
49. Repository Folder Structure
50. Previous and Next Topics
51. Final Summary

---

# 1. Introduction to Conditional Statements

Python programs contain instructions that tell a computer what to do.

In a simple program, statements commonly execute one after another. However, real-world applications need to make decisions based on different conditions.

For example:

- A student should receive a Pass message when their marks meet the required threshold.
- A shopping application should apply a discount when the bill satisfies a particular condition.
- A program should display Even when a number is divisible by two and Odd otherwise.
- A user should receive an access message when their credentials are correct and an error message when they are incorrect.
- A delivery application should provide free delivery when the order value reaches a specified amount.
- A program should classify a number as positive or non-positive.

These situations require decision-making.

Python provides conditional statements to control which instructions are executed.

The main conditional structures in Python include:

1. `if`
2. `if-else`
3. `if-elif-else`
4. Nested `if`
5. Conditional expressions
6. `match-case`

In the previous topic, we studied the basic `if` statement.

In this topic, we will study the `if-else` statement.

The major difference is that an `if-else` statement provides two alternative execution paths.

When the condition is true, the `if` block executes.

When the condition is false, the `else` block executes.

## 1.1 What Is Decision-Making?

Decision-making means choosing an action based on a condition.

Consider an example:

A student passes an examination when their marks are at least 40.

The program must perform two possible actions:

- Display Pass when marks are 40 or above.
- Display Fail when marks are below 40.

Python program:

```python
marks = 65

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Pass
```

Now change the marks:

```python
marks = 25

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Fail
```

The program selects the appropriate block based on the condition.

## 1.2 Why Are Conditional Statements Important?

Conditional statements make programs flexible.

Without decision-making, a program may perform the same operation regardless of its input.

With conditional statements, a program can respond differently to different situations.

For example:

```python
age = 16

if age >= 18:
    print("You meet the example adult age requirement.")
else:
    print("You do not meet the example adult age requirement.")
```

The output depends on the user's age.

## 1.3 Benefits of Conditional Statements

1. They support decision-making.
2. They allow input-based program behavior.
3. They support validation.
4. They help implement business rules.
5. They help classify values.
6. They control application execution.
7. They make programs more flexible.
8. They support algorithm development.
9. They help prevent invalid operations.
10. They are useful in real-world applications.

---

# 2. What Is Decision-Making?

Decision-making in programming means selecting an action according to a condition.

A condition is evaluated to determine whether it is true or false in a Boolean context.

Example:

```python
number = 10

if number > 0:
    print("Positive number")
else:
    print("Zero or negative number")
```

Output:

```text
Positive number
```

The condition is:

```python
number > 0
```

Python evaluates:

```text
10 > 0
```

The result is:

```text
True
```

Therefore, the `if` branch executes.

## 2.1 Real-World Decision-Making Examples

| Situation | Condition | True Action | False Action |
|---|---|---|---|
| Student result | Marks >= 40 | Pass | Fail |
| Age checking | Age >= 18 | Adult category | Minor category |
| Shopping | Price >= 1000 | Discount | No discount |
| Number checking | Number % 2 == 0 | Even | Odd |
| Login | Credentials match | Success | Failure |
| Delivery | Order >= 500 | Free delivery | Charge delivery fee |
| Inventory | Quantity > 0 | Available | Unavailable |
| Temperature | Temperature >= 30 | Hot | Normal or cool |
| Banking | Balance >= withdrawal | Continue example transaction | Insufficient balance |
| File checking | Filename ends in `.py` | Python file | Other file type |

## 2.2 Steps Involved in Decision-Making

1. Receive input or obtain values from variables.
2. Write the condition that must be checked.
3. Evaluate the condition.
4. Determine the truth value.
5. Execute the corresponding branch.
6. Continue with the remaining statements.

---

# 3. What Is an If-Else Statement?

An `if-else` statement is a conditional control-flow statement that provides two alternative blocks.

The first block executes when the condition is truthy.

The second block executes when the condition is falsy.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Adult
```

Now consider:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

Python selects one of the two branches.

## 3.1 Definition

An `if-else` statement is a Python conditional statement that executes the `if` block when its condition evaluates to a truthy value and executes the `else` block when that condition evaluates to a falsy value.

## 3.2 Important Characteristics

- `if` is the starting keyword.
- `else` introduces the alternative branch.
- The condition is written after `if`.
- The condition is followed by a colon.
- Both blocks use indentation.
- `else` does not have its own condition.
- Both branches are part of the same conditional statement.
- Only one branch executes when the statement is evaluated normally.
- An `else` branch cannot appear by itself.
- An `if` statement can have an `else` branch.
- Each branch may contain multiple statements.
- Conditions can contain comparison operators.
- Conditions can contain logical operators.
- Functions can be called inside conditions.

---

# 4. Why Do We Need If-Else?

In the previous topic, we studied a simple `if` statement.

Consider:

```python
marks = 30

if marks >= 40:
    print("Pass")
```

Output:

```text

```

There is no output because the condition is false.

The basic `if` statement skips its body when the condition is false.

Now suppose we also need to display Fail.

We can use an `else` block:

```python
marks = 30

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Fail
```

The `else` block handles the alternative situation.

## 4.1 Problems Solved by If-Else

1. Even or odd checking.
2. Pass or fail calculation.
3. Greater or smaller number selection.
4. Positive or non-positive classification.
5. Discount or no-discount calculation.
6. Delivery charge calculation.
7. Login success or failure.
8. Product available or unavailable.
9. Valid or invalid triangle checking.
10. Leap year or non-leap year classification.

## 4.2 Why Is Else Useful?

The `else` block ensures that the program has an alternative action when the condition is false.

It makes the program suitable for situations where two outcomes must be handled.

---

# 5. Syntax of If-Else

The general syntax is:

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

Example:

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Zero or negative")
```

Output:

```text
Positive
```

## 5.1 Components of If-Else

| Component | Description |
|---|---|
| `if` | Begins the conditional statement |
| `condition` | Expression evaluated by Python |
| `:` | Marks the beginning of the block |
| `statement_if_true` | Executes when the condition is truthy |
| `else` | Introduces the alternative block |
| `statement_if_false` | Executes when the condition is falsy |

## 5.2 If Keyword

The `if` keyword begins the conditional statement.

Example:

```python
if 10 > 5:
    print("First condition is true.")
```

## 5.3 Condition

The condition decides which block executes.

Example:

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## 5.4 Colon

The colon is required after both the `if` header and the `else` header.

Correct:

```python
if number > 0:
    print("Positive")
else:
    print("Not positive")
```

Incorrect:

```python
if number > 0
    print("Positive")
else
    print("Not positive")
```

The incorrect program produces a syntax error.

## 5.5 Else Keyword

The `else` keyword introduces the alternative branch.

Example:

```python
number = -10

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

The `else` block executes because the condition is false.

## 5.6 Indented Statements

The statements inside each branch must be indented.

Correct:

```python
if True:
    print("If block")
else:
    print("Else block")
```

---

# 6. Components of an If-Else Statement

Consider this program:

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

The components are:

**Variable assignment**

```python
marks = 75
```

Stores the marks.

**Conditional keyword**

```python
if
```

Begins the condition.

**Condition**

```python
marks >= 40
```

Checks the minimum marks requirement.

**If block**

```python
print("Pass")
```

Executes when the condition is true.

**Else keyword**

```python
else
```

Begins the alternative block.

**Else block**

```python
print("Fail")
```

Executes when the condition is false.

---

# 7. How If-Else Works

Python follows a simple execution process.

Consider:

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

Execution:

1. Python assigns 10 to `number`.
2. Python evaluates `number > 0`.
3. The comparison produces `True`.
4. Python executes the `if` block.
5. Python skips the `else` block.
6. Execution continues after the conditional statement.

Output:

```text
Positive
```

Now change the number:

```python
number = -5

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

Execution:

1. Python assigns -5.
2. Python evaluates `number > 0`.
3. The condition produces `False`.
4. Python skips the `if` block.
5. Python executes the `else` block.
6. Execution continues after the statement.

Output:

```text
Non-positive
```

## 7.1 Branch Selection

| Condition | If Block | Else Block |
|---|---|---|
| True | Executes | Skipped |
| False | Skipped | Executes |

This is the basic rule of an `if-else` statement.

---

# 8. True and False Execution Paths

An `if-else` statement provides two possible execution paths.

## 8.1 True Execution Path

Example:

```python
number = 20

if number > 10:
    print("Condition is true.")
else:
    print("Condition is false.")
```

Output:

```text
Condition is true.
```

## 8.2 False Execution Path

Example:

```python
number = 5

if number > 10:
    print("Condition is true.")
else:
    print("Condition is false.")
```

Output:

```text
Condition is false.
```

## 8.3 Complete Branch Comparison

```python
number = 15

if number > 10:
    print("Greater than 10")
else:
    print("10 or below")
```

Output:

```text
Greater than 10
```

Change the value to 5:

```python
number = 5

if number > 10:
    print("Greater than 10")
else:
    print("10 or below")
```

Output:

```text
10 or below
```

## 8.4 Exactly One Branch Executes

For a normally completed `if-else` statement, exactly one of the two branches is selected.

This does not mean that the program necessarily completes successfully. An exception or another control-flow operation can affect execution.

---

# 9. Difference Between If and If-Else

Both statements are used for conditional execution, but they provide different behavior.

## 9.1 If Statement

```python
marks = 25

if marks >= 40:
    print("Pass")
```

Output:

```text

```

When the condition is false, the body is skipped.

## 9.2 If-Else Statement

```python
marks = 25

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Fail
```

The false outcome is handled by the `else` block.

## 9.3 Comparison Table

| Feature | If | If-Else |
|---|---|---|
| Purpose | Execute a block when a condition is true | Choose between two branches |
| True condition | If block executes | If block executes |
| False condition | If block is skipped | Else block executes |
| Alternative branch | Not required | Required |
| Number of branches | One conditional body | Two alternative bodies |
| Best use | Optional action | Two-outcome decision |

## 9.4 When Should You Use If?

Use a basic `if` statement when an action is required only under a particular condition.

Example:

```python
temperature = 35

if temperature > 30:
    print("High temperature.")
```

## 9.5 When Should You Use If-Else?

Use `if-else` when both possible outcomes need separate actions.

Example:

```python
temperature = 25

if temperature > 30:
    print("Hot")
else:
    print("Normal or cool")
```

---

# 10. Difference Between Multiple If and If-Else

Multiple independent `if` statements are evaluated separately.

An `if-else` statement selects one of two branches.

## 10.1 Multiple Independent If Statements

```python
number = 12

if number > 0:
    print("Positive")

if number % 2 == 0:
    print("Even")
```

Output:

```text
Positive
Even
```

Both conditions are true, so both blocks execute.

## 10.2 If-Else Statement

```python
number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

Only one branch is selected.

## 10.3 Main Differences

| Multiple If | If-Else |
|---|---|
| Each condition is checked independently | One condition selects between two branches |
| Several blocks can execute | One branch is selected |
| Conditions may be unrelated | The else belongs to its matching if |
| Useful for separate checks | Useful for alternative outcomes |

## 10.4 Important Example

```python
number = 15

if number > 0:
    print("Positive")

if number % 2 != 0:
    print("Odd")

if number > 10:
    print("Greater than 10")
```

Output:

```text
Positive
Odd
Greater than 10
```

All three conditions are evaluated independently.

---

# 11. Boolean Values in If-Else

Python has the Boolean data type `bool`.

It has two values:

```python
True
False
```

Example:

```python
is_active = True

if is_active:
    print("Active")
else:
    print("Inactive")
```

Output:

```text
Active
```

## 11.1 True Value

A true condition executes the `if` branch.

```python
condition = True

if condition:
    print("True branch")
else:
    print("False branch")
```

## 11.2 False Value

A false condition executes the `else` branch.

```python
condition = False

if condition:
    print("True branch")
else:
    print("False branch")
```

Output:

```text
False branch
```

## 11.3 Comparison Result

```python
a = 10
b = 5

if a > b:
    print("True")
else:
    print("False")
```

Output:

```text
True
```

The comparison produces a Boolean value.

---

# 12. Truthy and Falsy Values

Python allows objects other than Boolean values to be used as conditions.

An object is truthy or falsy according to its truth value.

## 12.1 Common Falsy Values

| Value | Description |
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

## 12.2 Truthy Integer

```python
value = 10

if value:
    print("Truthy")
else:
    print("Falsy")
```

Output:

```text
Truthy
```

## 12.3 Falsy Integer

```python
value = 0

if value:
    print("Truthy")
else:
    print("Falsy")
```

Output:

```text
Falsy
```

## 12.4 Truthy String

```python
name = "Python"

if name:
    print("Name available")
else:
    print("Name missing")
```

Output:

```text
Name available
```

## 12.5 Falsy String

```python
name = ""

if name:
    print("Name available")
else:
    print("Name missing")
```

Output:

```text
Name missing
```

## 12.6 Truthy List

```python
numbers = [10, 20, 30]

if numbers:
    print("List is not empty")
else:
    print("List is empty")
```

Output:

```text
List is not empty
```

## 12.7 Falsy List

```python
numbers = []

if numbers:
    print("List is not empty")
else:
    print("List is empty")
```

Output:

```text
List is empty
```

## 12.8 Checking None

```python
value = None

if value is None:
    print("No value available")
else:
    print("Value is available")
```

Output:

```text
No value available
```

Use `is None` when specifically checking whether a value is `None`.

---

# 13. Comparison Operators in If-Else

Comparison operators compare values and produce Boolean results.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

## 13.1 Equal To

```python
a = 10
b = 10

if a == b:
    print("Equal")
else:
    print("Not equal")
```

## 13.2 Not Equal To

```python
a = 10
b = 20

if a != b:
    print("Different")
else:
    print("Same")
```

## 13.3 Greater Than

```python
a = 50
b = 20

if a > b:
    print("A is greater")
else:
    print("B is greater than or equal to A")
```

## 13.4 Less Than

```python
a = 10
b = 20

if a < b:
    print("A is smaller")
else:
    print("A is not smaller")
```

## 13.5 Greater Than or Equal

```python
marks = 40

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## 13.6 Less Than or Equal

```python
age = 18

if age <= 18:
    print("Age is 18 or below")
else:
    print("Age is above 18")
```

---

# 14. Arithmetic Operators in Conditions

Arithmetic calculations can be included in conditions.

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Modulo |
| `**` | Exponentiation |

## 14.1 Addition

```python
a = 10
b = 20

if a + b > 25:
    print("Sum is greater than 25")
else:
    print("Sum is 25 or below")
```

## 14.2 Subtraction

```python
a = 50
b = 20

if a - b > 25:
    print("Difference is greater than 25")
else:
    print("Difference is 25 or below")
```

## 14.3 Multiplication

```python
a = 5
b = 4

if a * b == 20:
    print("Product is 20")
else:
    print("Product is not 20")
```

## 14.4 Division

```python
a = 20
b = 2

if b != 0 and a / b == 10:
    print("Division result is 10")
else:
    print("Division result is not 10")
```

The first condition prevents division when `b` is zero.

## 14.5 Modulo

```python
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 14.6 Exponentiation

```python
number = 2

if number ** 3 == 8:
    print("Cube is 8")
else:
    print("Cube is not 8")
```

---

# 15. Logical Operators in Conditions

Logical operators are used to combine conditions.

Python has:

- `and`
- `or`
- `not`

## 15.1 AND Operator

Both operands must be truthy for the combined condition to be truthy.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Conditions satisfied")
else:
    print("Conditions not satisfied")
```

AND truth table:

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

## 15.2 OR Operator

At least one operand must be truthy for the combined condition to be truthy.

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount condition satisfied")
else:
    print("Discount condition not satisfied")
```

OR truth table:

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

## 15.3 NOT Operator

The `not` operator reverses the truth value.

```python
is_raining = False

if not is_raining:
    print("It is not raining")
else:
    print("It is raining")
```

NOT truth table:

| A | not A |
|---|---|
| True | False |
| False | True |

## 15.4 Combined Logical Conditions

```python
age = 20
has_id = True
is_banned = False

if age >= 18 and has_id and not is_banned:
    print("Example access allowed")
else:
    print("Example access denied")
```

---

# 16. Membership Operators

Membership operators check whether an item exists in a collection.

Python provides:

- `in`
- `not in`

## 16.1 IN Operator

```python
fruits = ["Apple", "Banana", "Mango"]

if "Mango" in fruits:
    print("Fruit found")
else:
    print("Fruit not found")
```

## 16.2 NOT IN Operator

```python
fruits = ["Apple", "Banana", "Mango"]

if "Orange" not in fruits:
    print("Orange is not available")
else:
    print("Orange is available")
```

## 16.3 String Membership

```python
name = "Python Programming"

if "Python" in name:
    print("Word found")
else:
    print("Word not found")
```

## 16.4 Dictionary Membership

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" in student:
    print("Marks key exists")
else:
    print("Marks key does not exist")
```

For a dictionary, `in` checks its keys by default.

---

# 17. Identity Operators

Identity operators check whether two references point to the same object.

Python provides:

- `is`
- `is not`

## 17.1 IS Operator

```python
value = None

if value is None:
    print("Value is None")
else:
    print("Value is not None")
```

## 17.2 IS NOT Operator

```python
value = 10

if value is not None:
    print("Value is available")
else:
    print("Value is missing")
```

## 17.3 Equality Versus Identity

```python
a = [1, 2, 3]
b = [1, 2, 3]

if a == b:
    print("Values are equal")
else:
    print("Values are different")
```

Output:

```text
Values are equal
```

However, the two lists are separate objects.

```python
if a is b:
    print("Same object")
else:
    print("Different objects")
```

Output:

```text
Different objects
```

---

# 18. Indentation and Code Blocks

Indentation is the spacing at the beginning of a line.

Python uses indentation to identify code blocks.

The recommended indentation level is four spaces.

## 18.1 Correct Indentation

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

## 18.2 Incorrect Indentation

```python
if number > 0:
print("Positive")
```

This produces an `IndentationError`.

## 18.3 Indentation of Both Branches

Correct:

```python
if True:
    print("If branch")
else:
    print("Else branch")
```

## 18.4 Multiple Statements

```python
if True:
    print("First statement")
    print("Second statement")
else:
    print("Alternative first")
    print("Alternative second")
```

## 18.5 Nested Blocks

```python
if True:
    print("Outer block")

    if True:
        print("Inner block")
else:
    print("Alternative block")
```

Indentation determines which `if` an `else` belongs to.

---

# 19. The Else Clause

The `else` clause represents the alternative path of an `if` statement.

Example:

```python
number = 5

if number > 10:
    print("Greater than 10")
else:
    print("10 or below")
```

Output:

```text
10 or below
```

## 19.1 Else Does Not Have a Condition

Correct:

```python
if number > 10:
    print("Greater than 10")
else:
    print("10 or below")
```

Incorrect:

```python
else number < 10:
    print("Smaller")
```

An `else` clause does not contain its own condition.

When another condition must be checked, Python uses `elif`, which will be covered in the next topic.

## 19.2 Else Must Belong to an If

An `else` cannot appear independently.

Incorrect:

```python
else:
    print("Alternative")
```

Correct:

```python
if True:
    print("First")
else:
    print("Alternative")
```

## 19.3 Else Placement

The `else` must match its corresponding `if`.

Correct:

```python
if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

---

# 20. If-Else With User Input

The `input()` function receives information from a user.

By default, the returned value is a string.

For numerical conditions, conversion may be required.

## 20.1 Integer Input

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Sample input:

```text
Enter age: 20
```

Output:

```text
Adult
```

## 20.2 Float Input

```python
price = float(input("Enter price: "))

if price >= 1000:
    print("Discount available")
else:
    print("No discount")
```

## 20.3 String Input

```python
name = input("Enter your name: ").strip()

if name:
    print("Welcome", name)
else:
    print("Name cannot be empty")
```

## 20.4 Input Conversion Error

Incorrect:

```python
age = input("Enter age: ")

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

This may raise a `TypeError` because the value is a string and 18 is an integer.

Correct:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## 20.5 Input Validation

```python
try:
    age = int(input("Enter age: "))

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

except ValueError:
    print("Please enter a valid integer.")
```

The `try-except` block handles invalid integer input.

---

# 21. If-Else With Integer Values

Integers are commonly used in conditional calculations.

## Example 1 – Positive or Non-Positive

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Zero or negative")
```

## Example 2 – Even or Odd

```python
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Example 3 – Divisible by 5

```python
number = 25

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
```

## Example 4 – Greater Than 100

```python
number = 80

if number > 100:
    print("Greater than 100")
else:
    print("100 or below")
```

## Example 5 – Multiple of 3

```python
number = 27

if number % 3 == 0:
    print("Multiple of 3")
else:
    print("Not a multiple of 3")
```

## Example 6 – Divisible by 2 and 3

```python
number = 18

if number % 2 == 0 and number % 3 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")
```

---

# 22. If-Else With Floating-Point Values

Floating-point numbers are values that can contain decimal parts.

Example:

```python
temperature = 35.5

if temperature >= 30:
    print("Hot")
else:
    print("Normal or cool")
```

## 22.1 Positive Decimal Number

```python
number = 5.75

if number > 0:
    print("Positive")
else:
    print("Zero or negative")
```

## 22.2 Price Comparison

```python
price = 999.99

if price >= 1000:
    print("Discount available")
else:
    print("No discount")
```

## 22.3 Floating-Point Equality

Decimal floating-point values may not be represented exactly in binary.

Example:

```python
result = 0.1 + 0.2

print(result)
```

Typical output:

```text
0.30000000000000004
```

For approximate comparisons, use `math.isclose()`.

```python
import math

result = 0.1 + 0.2

if math.isclose(result, 0.3):
    print("Approximately equal")
else:
    print("Not approximately equal")
```

---

# 23. If-Else With Strings

Strings can be compared and tested using conditional statements.

## 23.1 String Equality

```python
name = "Python"

if name == "Python":
    print("Matched")
else:
    print("Not matched")
```

## 23.2 Case-Insensitive Comparison

```python
answer = "YES"

if answer.lower() == "yes":
    print("Accepted")
else:
    print("Not accepted")
```

## 23.3 Empty or Non-Empty String

```python
name = ""

if name:
    print("Name is available")
else:
    print("Name is empty")
```

## 23.4 Starts With

```python
filename = "program.py"

if filename.startswith("program"):
    print("Correct prefix")
else:
    print("Different prefix")
```

## 23.5 Ends With

```python
filename = "notes.py"

if filename.endswith(".py"):
    print("Python file")
else:
    print("Other file")
```

---

# 24. If-Else With Lists and Collections

Lists and other collections can be checked through membership and truthiness.

## 24.1 Empty or Non-Empty List

```python
numbers = [10, 20, 30]

if numbers:
    print("List is not empty")
else:
    print("List is empty")
```

## 24.2 Check Membership

```python
numbers = [10, 20, 30]

if 20 in numbers:
    print("Found")
else:
    print("Not found")
```

## 24.3 Check Length

```python
numbers = [10, 20, 30]

if len(numbers) >= 3:
    print("At least three elements")
else:
    print("Fewer than three elements")
```

## 24.4 Tuple

```python
values = (10, 20, 30)

if values:
    print("Tuple is not empty")
else:
    print("Tuple is empty")
```

## 24.5 Dictionary

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" in student:
    print("Marks key exists")
else:
    print("Marks key does not exist")
```

## 24.6 Set

```python
numbers = {10, 20, 30}

if 20 in numbers:
    print("Value exists")
else:
    print("Value does not exist")
```

---

# 25. If-Else With Functions

Functions can return values that are used in conditions.

Example:

```python
def is_even(number):
    return number % 2 == 0


number = 12

if is_even(number):
    print("Even")
else:
    print("Odd")
```

## 25.1 Function Returning True

```python
def is_valid():
    return True


if is_valid():
    print("Valid")
else:
    print("Invalid")
```

## 25.2 Function Returning False

```python
def is_valid():
    return False


if is_valid():
    print("Valid")
else:
    print("Invalid")
```

## 25.3 Why Use Functions?

Functions make conditional logic reusable.

Instead of writing the same condition in many locations, a function can perform the check and return the result.

---

# 26. If-Else With Nested Conditions

A nested condition contains another conditional statement inside a conditional block.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Age requirement not satisfied")
```

The outer condition is evaluated first.

The inner condition is evaluated only when the outer condition is true.

The complete nested-if topic will be covered separately in:

`04-Nested-If/README.md`

---

# 27. If-Else With Multiple Conditions

Multiple conditions can be combined using logical operators.

## 27.1 AND

```python
marks = 80
attendance = 85

if marks >= 40 and attendance >= 75:
    print("Both requirements satisfied")
else:
    print("At least one requirement not satisfied")
```

## 27.2 OR

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount condition satisfied")
else:
    print("Discount condition not satisfied")
```

## 27.3 NOT

```python
is_raining = False

if not is_raining:
    print("It is not raining")
else:
    print("It is raining")
```

## 27.4 Multiple Conditions With Parentheses

```python
age = 20
has_id = True
is_banned = False

if (age >= 18 and has_id) and not is_banned:
    print("Access permitted")
else:
    print("Access denied")
```

Parentheses can make complex conditions easier to understand.

---

# 28. If-Else and Short-Circuit Evaluation

Python's `and` and `or` operators use short-circuit evaluation.

For an `and` expression, Python does not need to evaluate the right operand when the left operand is falsy.

For an `or` expression, Python does not need to evaluate the right operand when the left operand is truthy.

Example:

```python
numbers = []

if numbers and numbers[0] > 10:
    print("First element is greater than 10")
else:
    print("Condition is false")
```

Output:

```text
Condition is false
```

Because the list is empty, `numbers` is falsy.

The second operand is not evaluated, so Python does not try to access `numbers[0]`.

This prevents an index error.

## 28.1 Short-Circuit With OR

```python
is_admin = True

if is_admin or 10 / 0 > 1:
    print("Access condition satisfied")
else:
    print("Access condition not satisfied")
```

Output:

```text
Access condition satisfied
```

The second operand is not evaluated because the first operand is already truthy.

## 28.2 Important Note

Short-circuit evaluation should be used carefully.

Do not hide complicated operations inside logical expressions when a clear separate statement would be easier to understand.

---

# 29. If-Else in Real-World Applications

## 29.1 Student Result System

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## 29.2 Shopping Discount

```python
price = 1500

if price >= 1000:
    print("Discount available")
else:
    print("No discount")
```

## 29.3 Inventory System

```python
quantity = 0

if quantity > 0:
    print("Product available")
else:
    print("Product unavailable")
```

## 29.4 Login System

```python
is_authenticated = False

if is_authenticated:
    print("Login successful")
else:
    print("Login required")
```

## 29.5 Banking Example

```python
balance = 5000
withdrawal = 2000

if balance >= withdrawal:
    print("Sufficient balance")
else:
    print("Insufficient balance")
```

## 29.6 File Validation

```python
filename = "program.py"

if filename.endswith(".py"):
    print("Python file")
else:
    print("Not a Python file")
```

## 29.7 Delivery Charge

```python
order_amount = 400

if order_amount >= 500:
    delivery_charge = 0
else:
    delivery_charge = 50

print(delivery_charge)
```

---

# 30. Explanation of 12 Topic Examples

This section explains all twelve examples in `01_if_else.py`.

## Example 1 – Basic If-Else

Code:

```python
age = 20

if age >= 18:
    print("You meet the example adult age condition.")
else:
    print("You do not meet the example adult age condition.")
```

Output:

```text
You meet the example adult age condition.
```

Explanation:

1. Assign 20 to the age variable.
2. Compare age with 18.
3. The condition is true.
4. Execute the `if` block.
5. Skip the `else` block.

Dry run:

| Step | Operation | Result |
|---|---|---|
| 1 | `age = 20` | 20 |
| 2 | `age >= 18` | True |
| 3 | Selected branch | If |
| 4 | Output | Adult condition satisfied |

## Example 2 – Even or Odd

Code:

```python
number = 15

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

Output:

```text
The number is odd.
```

Explanation:

```text
15 % 2 = 1

1 == 0

False
```

The `else` block executes.

## Example 3 – Positive or Non-Positive

Code:

```python
number = -10

if number > 0:
    print("The number is positive.")
else:
    print("The number is zero or negative.")
```

Output:

```text
The number is zero or negative.
```

The condition is false.

## Example 4 – Greater of Two Numbers

Code:

```python
a = 25
b = 40

if a > b:
    print("First number is greater.")
    greater = a
else:
    print("Second number is greater than or equal to the first.")
    greater = b

print("Selected value:", greater)
```

Output:

```text
Second number is greater than or equal to the first.
Selected value: 40
```

The condition `25 > 40` is false, so the else branch executes.

## Example 5 – Pass or Fail

Code:

```python
marks = 65

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
```

Output:

```text
Result: Pass
```

## Example 6 – Divisible by Five

Code:

```python
number = 25

if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")
```

Output:

```text
The number is divisible by 5.
```

Calculation:

```text
25 % 5 = 0
```

## Example 7 – Discount or No Discount

Code:

```python
price = 2000

if price >= 1000:
    discount = price * 0.10
    final_price = price - discount
    print("10 percent discount applied.")
else:
    discount = 0
    final_price = price
    print("No discount applied.")

print("Original price:", price)
print("Discount:", discount)
print("Final price:", final_price)
```

Output:

```text
10 percent discount applied.
Original price: 2000
Discount: 200.0
Final price: 1800.0
```

## Example 8 – Voting Age Condition

Code:

```python
age = 16

if age >= 18:
    print("You meet the example minimum age requirement.")
else:
    print("You do not meet the example minimum age requirement.")
```

Output:

```text
You do not meet the example minimum age requirement.
```

This is an illustrative age-threshold example.

## Example 9 – Empty or Non-Empty String

Code:

```python
name = ""

if name:
    print("Name is available:", name)
else:
    print("Name is empty.")
```

Output:

```text
Name is empty.
```

An empty string is falsy.

## Example 10 – Logical AND

Code:

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Both conditions are satisfied.")
else:
    print("At least one condition is not satisfied.")
```

Output:

```text
Both conditions are satisfied.
```

Both conditions are true.

## Example 11 – Logical OR

Code:

```python
is_member = False
has_coupon = False

if is_member or has_coupon:
    print("Discount condition is satisfied.")
else:
    print("Discount condition is not satisfied.")
```

Output:

```text
Discount condition is not satisfied.
```

Both operands are false.

## Example 12 – Empty or Non-Empty List

Code:

```python
numbers = []

if numbers:
    print("The list contains elements:", numbers)
else:
    print("The list is empty.")
```

Output:

```text
The list is empty.
```

An empty list is falsy.

---

# 31. Twelve Solved Programming Problems

The Python file contains twelve interactive solved problems.

## Problem 1 – Positive or Non-Positive

Objective:

Accept a number and classify it as positive or non-positive.

Code:

```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is zero or negative.")
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
3. Check whether it is greater than zero.
4. If true, display the positive message.
5. Otherwise, display the alternative message.
6. Stop.

Test cases:

| Input | Output |
|---:|---|
| 10 | Positive |
| -10 | Zero or negative |
| 0 | Zero or negative |
| 2.5 | Positive |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 2 – Even or Odd

Objective:

Check whether an integer is even or odd.

Code:

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Sample input:

```text
Enter an integer: 15
```

Output:

```text
Odd
```

Algorithm:

1. Read an integer.
2. Calculate the remainder after division by 2.
3. If the remainder is zero, display Even.
4. Otherwise, display Odd.

Test cases:

| Input | Output |
|---:|---|
| 2 | Even |
| 7 | Odd |
| 0 | Even |
| -4 | Even |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 3 – Voting Age Condition

Objective:

Check an example minimum-age requirement.

Code:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You meet the example minimum age requirement.")
else:
    print("You do not meet the example minimum age requirement.")
```

Test cases:

| Age | Result |
|---:|---|
| 15 | Does not meet threshold |
| 17 | Does not meet threshold |
| 18 | Meets threshold |
| 20 | Meets threshold |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

This program is not a complete legal voting eligibility checker.

## Problem 4 – Largest of Two Numbers

Code:

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    largest = a
else:
    largest = b

print("Largest:", largest)
```

Sample input:

```text
Enter first number: 25
Enter second number: 40
```

Output:

```text
Largest: 40.0
```

Test cases:

| A | B | Result |
|---:|---:|---:|
| 10 | 20 | 20 |
| 50 | 30 | 50 |
| 5 | 5 | 5 |
| -5 | -2 | -2 |

Note: This implementation returns the second input when both values are equal, but the selected maximum value is still correct.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 5 – Pass or Fail

Code:

```python
marks = float(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Test cases:

| Marks | Result |
|---:|---|
| 90 | Pass |
| 40 | Pass |
| 39 | Fail |
| 20 | Fail |

The threshold is illustrative.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 6 – Divisible by Five

Code:

```python
number = int(input("Enter number: "))

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
```

Test cases:

| Number | Result |
|---:|---|
| 25 | Divisible |
| 30 | Divisible |
| 17 | Not divisible |
| 0 | Divisible |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 7 – Leap Year Checker

Code:

```python
year = int(input("Enter year: "))

is_leap_year = (
    year % 400 == 0
    or
    (year % 4 == 0 and year % 100 != 0)
)

if is_leap_year:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

Test cases:

| Year | Result |
|---:|---|
| 2024 | Leap year |
| 2023 | Not a leap year |
| 2000 | Leap year |
| 1900 | Not a leap year |
| 2400 | Leap year |

The Gregorian calendar rule is used.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 8 – Grade Calculator

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

The program validates the marks range before calculating the grade.

The grade ranges do not overlap.

Test cases:

| Marks | Result |
|---:|---|
| 95 | A |
| 85 | B |
| 65 | C |
| 50 | D |
| 30 | F |
| -1 | Invalid |
| 101 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 9 – Delivery Charge Calculator

Code:

```python
order_amount = float(input("Enter order amount: "))

if order_amount >= 500:
    delivery_charge = 0
else:
    delivery_charge = 50

total_amount = order_amount + delivery_charge

print("Delivery charge:", delivery_charge)
print("Total amount:", total_amount)
```

Test cases:

| Order | Delivery | Total |
|---:|---:|---:|
| 300 | 50 | 350 |
| 500 | 0 | 500 |
| 750 | 0 | 750 |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

This is an example billing rule.

## Problem 10 – Basic Login Check

Code:

```python
correct_username = "student"
correct_password = "python123"

username = input("Enter username: ").strip()
password = input("Enter password: ")

if (
    username == correct_username
    and password == correct_password
):
    print("Login successful.")
else:
    print("Incorrect username or password.")
```

Sample input:

```text
Enter username: student
Enter password: python123
```

Output:

```text
Login successful.
```

Explanation:

Both comparisons must be true.

Security note:

This example is only for learning. Real authentication systems must not store plain-text passwords.

Complexity:

- Time: O(n + m) for comparing strings of lengths n and m.
- Auxiliary space: O(n + m) for input strings.

## Problem 11 – Empty or Non-Empty List

The current Python file accepts comma-separated numbers using `read_number_list()`.

Example:

```text
10, 20, 30
```

It validates that at least one finite number is entered.

Core conditional logic:

```python
if numbers:
    print("The list is not empty.")
else:
    print("The list is empty.")
```

For a general empty-list demonstration:

```python
numbers = []

if numbers:
    print("The list is not empty.")
else:
    print("The list is empty.")
```

Output:

```text
The list is empty.
```

Important implementation note:

The helper in the supplied interactive Python file requires at least one number. Therefore, its empty-list branch is not normally reachable through that helper. The separate demonstration above shows how the `else` branch works for an empty list.

## Problem 12 – Triangle Validity Checker

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
else:
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

All three sides must be positive.

The sum of any two sides must be greater than the third side.

Test cases:

| A | B | C | Result |
|---:|---:|---:|---|
| 3 | 4 | 5 | Valid |
| 5 | 5 | 5 | Valid |
| 1 | 2 | 3 | Invalid |
| 2 | 2 | 5 | Invalid |
| 0 | 4 | 5 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

---

# 32. Ten Unsolved Practice Questions

Try to solve these questions independently.

## Question 1 – Divisible by 3 and 7

Accept an integer.

Display an appropriate message based on whether it is divisible by both 3 and 7.

Hint:

```python
number % 3 == 0 and number % 7 == 0
```

## Question 2 – Smaller of Two Numbers

Accept two numbers.

Display the smaller number.

Also handle the situation when both numbers are equal.

## Question 3 – Pass or Fail

Accept marks.

Display Pass when marks are at least 50 and Fail otherwise.

## Question 4 – Child or Adult

Accept age.

Use an example threshold of 18 to classify the user as Child or Adult.

## Question 5 – Temperature Classification

Accept a temperature.

Display:

- Hot when temperature is at least 30.
- Normal or cool otherwise.

## Question 6 – Shopping Discount

Accept a bill amount.

Apply a 15% discount when the amount is at least 2000.

Otherwise, retain the original amount.

## Question 7 – Century Year

Accept a year.

Check whether it is divisible by 100.

A century year is not automatically a leap year.

## Question 8 – Vowel or Consonant

Accept one English alphabet character.

Display whether it is a vowel or consonant.

Validate that exactly one alphabet character is supplied.

## Question 9 – Equilateral Triangle

Accept three positive side lengths.

Display an appropriate message when all sides are equal.

## Question 10 – Multiple Conditions

Accept an integer.

Display separate messages when:

- The number is positive.
- The number is even.
- The number is greater than 100.

Use independent `if` statements.

---

# 33. Dry Runs and Trace Tables

A dry run means manually evaluating a program using known input values and recording each operation.

Dry runs improve understanding of conditions and branch selection.

## 33.1 Positive or Non-Positive

Code:

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

Trace:

| Step | Operation | Result |
|---|---|---|
| 1 | Assign number | 10 |
| 2 | Evaluate `10 > 0` | True |
| 3 | Selected block | If |
| 4 | Output | Positive |

## 33.2 False Condition

```python
number = -5

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

Trace:

| Step | Operation | Result |
|---|---|---|
| 1 | Assign number | -5 |
| 2 | Evaluate `-5 > 0` | False |
| 3 | Selected block | Else |
| 4 | Output | Non-positive |

## 33.3 Even or Odd

```python
number = 18

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Trace:

| Step | Expression | Result |
|---|---|---|
| 1 | `18 % 2` | 0 |
| 2 | `0 == 0` | True |
| 3 | Selected branch | If |
| 4 | Output | Even |

## 33.4 Discount Calculation

```python
price = 2000

if price >= 1000:
    final_price = price * 0.90
else:
    final_price = price
```

Trace:

| Step | Operation | Result |
|---|---|---|
| 1 | Original price | 2000 |
| 2 | Check `2000 >= 1000` | True |
| 3 | Calculate discounted price | 1800 |
| 4 | Final price | 1800 |

## 33.5 Logical AND

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Eligible")
else:
    print("Not eligible")
```

Trace:

| Condition | Result |
|---|---|
| `age >= 18` | True |
| `has_id` | True |
| AND result | True |
| Selected block | If |

## 33.6 Logical OR

```python
is_member = False
has_coupon = False

if is_member or has_coupon:
    print("Discount")
else:
    print("No discount")
```

Trace:

| Condition | Result |
|---|---|
| `is_member` | False |
| `has_coupon` | False |
| OR result | False |
| Selected block | Else |

---

# 34. Algorithms and Flowcharts

## 34.1 Basic If-Else Flowchart

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
          v          v
       If Block   Else Block
          |          |
          +-----+----+
                |
                v
               END
```

## 34.2 Algorithm – Even or Odd

1. Start.
2. Read an integer.
3. Calculate the remainder after division by two.
4. Check whether the remainder is zero.
5. If true, display Even.
6. Otherwise, display Odd.
7. Stop.

## 34.3 Algorithm – Positive or Non-Positive

1. Start.
2. Read a number.
3. Check whether the number is greater than zero.
4. If true, display Positive.
5. Otherwise, display Zero or Negative.
6. Stop.

## 34.4 Algorithm – Largest of Two Numbers

1. Start.
2. Read the first number.
3. Read the second number.
4. Compare the first number with the second.
5. If the first is greater, select the first.
6. Otherwise, select the second.
7. Display the selected maximum.
8. Stop.

## 34.5 Algorithm – Discount Calculation

1. Start.
2. Read the original price.
3. Check whether the price is at least 1000.
4. If true, calculate the discount.
5. Calculate the final price after discount.
6. Otherwise, keep the original price.
7. Display the final price.
8. Stop.

---

# 35. Common Programming Mistakes

## Mistake 1 – Missing Colon

Incorrect:

```python
if number > 0
    print("Positive")
else:
    print("Non-positive")
```

Correct:

```python
if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

## Mistake 2 – Incorrect Else Indentation

Incorrect:

```python
if number > 0:
    print("Positive")
    else:
        print("Non-positive")
```

Correct:

```python
if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

The `else` must align with its corresponding `if`.

## Mistake 3 – Assignment Instead of Comparison

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

## Mistake 4 – Missing Indentation

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

## Mistake 5 – Else Without If

Incorrect:

```python
else:
    print("Alternative")
```

Correct:

```python
if condition:
    print("First")
else:
    print("Alternative")
```

## Mistake 6 – Forgetting Input Conversion

Incorrect:

```python
age = input("Enter age: ")

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Correct:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Mistake 7 – Incorrect Comparison Boundary

Suppose marks of 40 must pass.

Incorrect:

```python
if marks > 40:
    print("Pass")
else:
    print("Fail")
```

This incorrectly classifies exactly 40 as Fail.

Correct:

```python
if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## Mistake 8 – Using OR Instead of AND

If both conditions are required, use `and`.

Incorrect:

```python
if age >= 18 or has_id:
    print("Access granted")
```

Correct for requiring both:

```python
if age >= 18 and has_id:
    print("Access granted")
```

## Mistake 9 – Incorrect Empty-List Handling

Remember that an empty list is falsy.

```python
numbers = []

if numbers:
    print("Not empty")
else:
    print("Empty")
```

## Mistake 10 – Confusing If-Else With If-Elif

An `if-else` statement handles two branches.

For multiple specific conditions, `if-elif-else` is generally more suitable.

---

# 36. Debugging Techniques

Debugging means locating and correcting problems in code.

## 36.1 Print the Condition

```python
number = 10

condition = number > 0

print("Condition:", condition)

if condition:
    print("Positive")
else:
    print("Non-positive")
```

## 36.2 Print Variable Values

```python
marks = 75

print("Marks:", marks)

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## 36.3 Inspect Data Types

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

Convert when an integer is required.

## 36.4 Test Both Branches

Test:

- A value that makes the condition true.
- A value that makes the condition false.

## 36.5 Test Boundary Values

For a threshold of 40, test:

- 39
- 40
- 41

This detects incorrect use of `>` and `>=`.

## 36.6 Use Intermediate Variables

Instead of writing:

```python
if age >= 18 and has_id and not is_banned:
    print("Allowed")
else:
    print("Denied")
```

You can write:

```python
age_ok = age >= 18
id_ok = has_id
account_ok = not is_banned

if age_ok and id_ok and account_ok:
    print("Allowed")
else:
    print("Denied")
```

This can make debugging easier.

---

# 37. Best Practices

1. Use clear variable names.
2. Use four spaces for indentation.
3. Always write the colon after `if` and `else`.
4. Align the `else` with the corresponding `if`.
5. Use `==` for equality checks.
6. Convert user input to the correct type.
7. Validate input before processing it.
8. Test both branches.
9. Test boundary values.
10. Use logical AND when all requirements must be satisfied.
11. Use logical OR when at least one requirement is sufficient.
12. Use `is None` for checking None.
13. Avoid unnecessary complex expressions.
14. Use parentheses when they improve readability.
15. Prefer `if-elif-else` when more than two alternatives must be checked.
16. Avoid storing plain-text passwords in real authentication systems.
17. Initialize variables that may be used after a conditional.
18. Keep application rules understandable.
19. Write meaningful output messages.
20. Test negative, zero and positive input values when appropriate.

---

# 38. Practical Applications

## 38.1 Student Result System

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## 38.2 Shopping Application

```python
price = 1500

if price >= 1000:
    print("Discount applied")
else:
    print("No discount")
```

## 38.3 Inventory System

```python
quantity = 5

if quantity > 0:
    print("Product available")
else:
    print("Out of stock")
```

## 38.4 Login Application

```python
is_authenticated = True

if is_authenticated:
    print("Login successful")
else:
    print("Please login")
```

## 38.5 Banking Example

```python
balance = 5000
withdrawal = 7000

if balance >= withdrawal:
    print("Transaction can proceed")
else:
    print("Insufficient balance")
```

## 38.6 Delivery Application

```python
order_amount = 300

if order_amount >= 500:
    print("Free delivery")
else:
    print("Delivery charge applies")
```

## 38.7 Data Validation

```python
age = 22

if age >= 0:
    print("Valid non-negative age value")
else:
    print("Invalid age value")
```

---

# 39. If-Else in Data Structures

Conditional statements work with many data structures.

## 39.1 Lists

```python
numbers = [10, 20, 30]

if numbers:
    print("List is not empty")
else:
    print("List is empty")
```

## 39.2 Searching in a List

```python
numbers = [10, 20, 30, 40]
target = 30

if target in numbers:
    print("Found")
else:
    print("Not found")
```

## 39.3 Stack

```python
stack = [10, 20, 30]

if stack:
    print("Stack has elements")
else:
    print("Stack is empty")
```

## 39.4 Queue

```python
queue = [10, 20, 30]

if queue:
    print("Queue has elements")
else:
    print("Queue is empty")
```

## 39.5 Dictionary

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" in student:
    print("Marks available")
else:
    print("Marks unavailable")
```

## 39.6 Set

```python
numbers = {10, 20, 30}

if 20 in numbers:
    print("Value exists")
else:
    print("Value does not exist")
```

---

# 40. If-Else in Data Structures and Algorithms

Conditions are essential in algorithm development.

## 40.1 Linear Search

```python
numbers = [10, 20, 30, 40]
target = 30

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
```

The `if` statement checks each element.

The final `if-else` selects the appropriate result.

Time complexity:

- Worst case: O(n)
- Auxiliary space: O(1)

## 40.2 Find Maximum

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

Time complexity: O(n).

Auxiliary space: O(1), excluding the input list.

## 40.3 Find Minimum

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

Time complexity: O(n).

Auxiliary space: O(1), excluding the input list.

## 40.4 Count Even Numbers

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

Time complexity: O(n).

Auxiliary space: O(1).

## 40.5 Filter Positive Numbers

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

Time complexity: O(n).

Auxiliary space: O(k), where k is the number of positive values stored in the result list.

## 40.6 Binary Search

Binary search repeatedly chooses which half of a sorted search range should be examined.

A simplified decision:

```python
if arr[mid] == target:
    print("Found")
else:
    print("Not found at this index")
```

A complete binary search uses multiple conditions to move left or right through the search range.

---

# 41. Time and Space Complexity

A simple `if-else` statement does not necessarily make a program slow.

Its complexity depends on the work done in the condition and the selected branch.

## 41.1 Simple Comparison

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

For a basic integer comparison:

- Time complexity: O(1)
- Auxiliary space: O(1)

## 41.2 Logical Conditions

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Denied")
```

For simple constant-time operands:

- Time complexity: O(1)
- Auxiliary space: O(1)

## 41.3 List Membership

```python
numbers = [10, 20, 30, 40]

if 30 in numbers:
    print("Found")
else:
    print("Not found")
```

List membership may examine every element.

- Worst-case time: O(n)
- Auxiliary space: O(1), excluding the existing list.

## 41.4 Set Membership

```python
numbers = {10, 20, 30, 40}

if 30 in numbers:
    print("Found")
else:
    print("Not found")
```

Set membership is expected O(1) on average.

## 41.5 Important Rule

The time complexity of an `if-else` structure is determined by:

- The condition.
- The selected branch.
- Function calls inside the condition.
- Operations performed inside the branch.
- Any loops or collection operations involved.

---

# 42. Mini Project – Shopping Bill Calculator

## Project Introduction

Create a basic shopping bill calculator using `if-else`.

The example policy is:

- Orders of at least 1000 receive a 10% discount.
- Smaller orders receive no discount.

This is an illustrative pricing rule.

## Project Requirements

1. Accept the original price.
2. Check whether the price is at least 1000.
3. Calculate the discount when eligible.
4. Otherwise, keep the original price.
5. Calculate the final bill.
6. Display the bill summary.

## Python Program

```python
print("=" * 50)
print("SHOPPING BILL CALCULATOR")
print("=" * 50)

price = float(input("Enter product price: "))

if price <= 0:
    print("Invalid product price.")

else:
    if price >= 1000:
        discount = price * 0.10
        print("10% discount applied.")
    else:
        discount = 0
        print("No discount applied.")

    final_price = price - discount

    print("\n--------- BILL SUMMARY ---------")
    print("Original Price:", price)
    print("Discount:", discount)
    print("Final Price:", final_price)
    print("--------------------------------")
```

## Sample Input

```text
Enter product price: 2000
```

## Output

```text
==================================================
SHOPPING BILL CALCULATOR
==================================================
10% discount applied.

--------- BILL SUMMARY ---------
Original Price: 2000.0
Discount: 200.0
Final Price: 1800.0
--------------------------------
```

## Sample Input 2

```text
Enter product price: 800
```

Output:

```text
No discount applied.

--------- BILL SUMMARY ---------
Original Price: 800.0
Discount: 0
Final Price: 800.0
--------------------------------
```

## Project Challenges

1. Accept multiple product prices.
2. Add a tax calculation.
3. Add a coupon code check.
4. Add delivery charges.
5. Display a detailed bill.
6. Validate all input values.
7. Add a repeat-order option.
8. Store completed bills in a list.

---

# 43. Practice Test

Try solving these questions without looking at the answers.

## Question 1

What is the output?

```python
number = 10

if number > 0:
    print("Positive")
else:
    print("Non-positive")
```

## Question 2

What is the output?

```python
number = -5

if number > 0:
    print("Positive")
else:
    print("Negative")
```

## Question 3

What is the output?

```python
number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Question 4

What is the output?

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## Question 5

What is the output?

```python
a = 10
b = 20

if a > b:
    print("A")
else:
    print("B")
```

## Question 6

What is the output?

```python
value = 0

if value:
    print("Truthy")
else:
    print("Falsy")
```

## Question 7

What is the output?

```python
numbers = []

if numbers:
    print("Not empty")
else:
    print("Empty")
```

## Question 8

What is the output?

```python
name = "Python"

if "P" in name:
    print("Found")
else:
    print("Not found")
```

## Question 9

What is the output?

```python
a = True
b = False

if a and b:
    print("Both true")
else:
    print("At least one is false")
```

## Question 10

What is the output?

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Practice Test Answers

| Question | Answer |
|---|---|
| 1 | Positive |
| 2 | Negative |
| 3 | Even |
| 4 | Fail |
| 5 | B |
| 6 | Falsy |
| 7 | Empty |
| 8 | Found |
| 9 | At least one is false |
| 10 | Adult |

---

# 44. Viva and Interview Questions

## Basic Questions

**Q1. What is an if-else statement?**

It is a conditional statement that selects between two alternative execution blocks.

**Q2. What is the syntax of if-else?**

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

**Q3. Why is else used?**

It provides an alternative block when the condition is false.

**Q4. Is else compulsory in an if statement?**

No. A simple `if` statement does not require `else`, but an `if-else` structure includes it.

**Q5. Does else have its own condition?**

No.

**Q6. Can an if-else statement contain multiple statements in each block?**

Yes.

**Q7. Which symbol is required after if and else headers?**

A colon `:`.

**Q8. What is indentation?**

Indentation is the spacing that defines the code block.

**Q9. What happens if the if condition is true?**

The if block executes.

**Q10. What happens if the if condition is false?**

The else block executes.

## Intermediate Questions

**Q11. How many branches are present in a basic if-else structure?**

Two branches.

**Q12. Can both if and else blocks execute in the same normal evaluation?**

No. One branch is selected.

**Q13. What is the difference between if and if-else?**

A basic `if` has one conditional block; `if-else` provides an alternative block.

**Q14. What are Boolean values?**

`True` and `False`.

**Q15. What is a truthy value?**

A value that evaluates to true in a Boolean context.

**Q16. What is a falsy value?**

A value that evaluates to false in a Boolean context.

**Q17. Is zero truthy or falsy?**

Falsy.

**Q18. Is an empty string truthy or falsy?**

Falsy.

**Q19. Is a non-empty list truthy or falsy?**

Truthy.

**Q20. Which operator checks equality?**

`==`.

## Logical Questions

**Q21. Name the logical operators in Python.**

`and`, `or` and `not`.

**Q22. When does AND return a truthy result?**

When both operands are truthy.

**Q23. When does OR return a truthy result?**

When at least one operand is truthy.

**Q24. What does NOT do?**

It reverses the truth value.

**Q25. Can if-else conditions contain multiple logical operators?**

Yes.

**Q26. What is short-circuit evaluation?**

It skips evaluating the right operand when the result of `and` or `or` is already determined by the left operand.

**Q27. Can membership operators be used in if-else?**

Yes.

**Q28. What is the difference between `==` and `is`?**

`==` compares values; `is` checks whether references point to the same object.

**Q29. How should None be checked?**

Using `is None` or `is not None`.

**Q30. Can a function be used in a condition?**

Yes.

## Intermediate Programming Questions

**Q31. How can you check whether a number is even?**

Using:

```python
number % 2 == 0
```

**Q32. How can you find the greater of two numbers?**

Compare them using `>` and select the appropriate value.

**Q33. How can you check leap years?**

Use divisibility by 400, or divisibility by 4 without divisibility by 100.

**Q34. How can you check whether a list is empty?**

Use an if-else truthiness check.

**Q35. Can if-else statements be nested?**

Yes.

**Q36. Can an else block exist without an if block?**

No.

**Q37. What error occurs if required indentation is missing?**

Usually `IndentationError`.

**Q38. What happens if a colon is missing?**

Python raises `SyntaxError`.

**Q39. What happens if a numeric string is compared directly with an integer?**

Python generally raises `TypeError`.

**Q40. What is the purpose of pass?**

It is a placeholder statement that performs no operation.

## Interview-Level Questions

**Q41. What is the output?**

```python
if 10 > 5:
    print("A")
else:
    print("B")
```

Answer: `A`.

**Q42. What is the output?**

```python
if 10 < 5:
    print("A")
else:
    print("B")
```

Answer: `B`.

**Q43. What is the output?**

```python
if []:
    print("A")
else:
    print("B")
```

Answer: `B`.

**Q44. What is the output?**

```python
if [1, 2]:
    print("A")
else:
    print("B")
```

Answer: `A`.

**Q45. What is the output?**

```python
if not None:
    print("A")
else:
    print("B")
```

Answer: `A`.

**Q46. What is the output?**

```python
a = 10
b = 10

if a > b:
    print("A")
else:
    print("B")
```

Answer: `B`.

**Q47. What is the output?**

```python
a = 10
b = 20

if a == b:
    print("Same")
else:
    print("Different")
```

Answer: `Different`.

**Q48. Can if-else return values directly?**

No. An `if-else` statement controls execution. A conditional expression is used when a value must be selected as an expression.

**Q49. When should if-elif-else be preferred over if-else?**

When more than two distinct conditions need to be checked.

**Q50. Why are if-else statements important in DSA?**

They support decision-making in searching, sorting, traversal, validation, classification and many other algorithms.

---

# 45. Important Glossary

| Term | Meaning |
|---|---|
| Conditional Statement | A statement that controls execution based on a condition |
| If Statement | Executes a block when its condition is truthy |
| If-Else Statement | Selects between two alternative blocks |
| If Block | The block executed when the condition is truthy |
| Else Block | The alternative block |
| Condition | An expression evaluated for its truth value |
| Boolean | Data type containing True and False |
| Truthy | A value that behaves as true in a Boolean context |
| Falsy | A value that behaves as false in a Boolean context |
| Comparison Operator | An operator used to compare values |
| Logical Operator | An operator used to combine or reverse conditions |
| Membership Operator | An operator that checks collection membership |
| Identity Operator | An operator that checks object identity |
| Indentation | Leading whitespace defining code blocks |
| Code Block | A group of related statements |
| Short-Circuit | Skipping an unnecessary logical operand |
| Nested If | An if statement inside another if statement |
| Debugging | Finding and correcting errors |
| Algorithm | A defined sequence of steps for solving a problem |
| Dry Run | Manual tracing of program execution |
| Time Complexity | A description of how running time grows |
| Auxiliary Space | Additional memory used by an algorithm |

---

# 46. Quick Revision Notes

Remember these points:

1. An `if-else` statement supports two alternative outcomes.
2. The `if` keyword begins the condition.
3. The condition is followed by a colon.
4. The `else` keyword introduces the alternative block.
5. The else clause does not have a condition.
6. The `if` block executes when the condition is truthy.
7. The `else` block executes when the condition is falsy.
8. Both branches use indentation.
9. Only one branch is selected in a normal evaluation.
10. Comparison operators produce Boolean results.
11. Logical operators combine conditions.
12. Membership operators can check collection contents.
13. Identity operators can check object identity.
14. Zero is falsy.
15. Empty strings are falsy.
16. Empty lists are falsy.
17. Non-empty collections are generally truthy.
18. Use `==` for value equality.
19. Use `is None` for None checks.
20. Convert user input before numeric comparison.
21. Test both branches.
22. Test boundary values.
23. Use `and` when every requirement must hold.
24. Use `or` when at least one requirement is sufficient.
25. Use `if-elif-else` for several alternatives.

### Important Syntax

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

### Important Examples

Even or odd:

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Pass or fail:

```python
if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Positive or non-positive:

```python
if number > 0:
    print("Positive")
else:
    print("Zero or negative")
```

Discount calculation:

```python
if price >= 1000:
    final_price = price * 0.90
else:
    final_price = price
```

Logical condition:

```python
if age >= 18 and has_id:
    print("Eligible")
else:
    print("Not eligible")
```

---

# 47. Learning Checklist

Complete this checklist after studying the topic.

- [ ] Understand conditional statements.
- [ ] Understand the meaning of decision-making.
- [ ] Define an if-else statement.
- [ ] Learn the complete if-else syntax.
- [ ] Identify the condition.
- [ ] Understand the if block.
- [ ] Understand the else block.
- [ ] Understand true and false execution paths.
- [ ] Differentiate if from if-else.
- [ ] Differentiate independent if statements from if-else.
- [ ] Understand Boolean values.
- [ ] Understand truthy and falsy values.
- [ ] Learn comparison operators.
- [ ] Use arithmetic operators in conditions.
- [ ] Use logical AND.
- [ ] Use logical OR.
- [ ] Use logical NOT.
- [ ] Use membership operators.
- [ ] Understand identity operators.
- [ ] Understand indentation.
- [ ] Use if-else with integer values.
- [ ] Use if-else with floating-point values.
- [ ] Use if-else with string values.
- [ ] Use if-else with lists and dictionaries.
- [ ] Use function calls in conditions.
- [ ] Understand nested conditions.
- [ ] Accept and convert user input.
- [ ] Check even and odd numbers.
- [ ] Check positive and non-positive numbers.
- [ ] Find the larger of two numbers.
- [ ] Calculate a discount.
- [ ] Calculate delivery charges.
- [ ] Check leap years.
- [ ] Validate triangle side lengths.
- [ ] Debug syntax and indentation errors.
- [ ] Test true and false branches.
- [ ] Test boundary values.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the mini project.
- [ ] Revise all 50 viva questions.

---

# 48. How to Run the Python Program

The Python file for this topic is:

```text
01_if_else.py
```

## Step 1 – Open the Folder

Navigate to:

```text
06-Conditional-Statements/
    02-If-Else/
```

## Step 2 – Open the Terminal

Open PowerShell or the VS Code terminal inside the topic folder.

## Step 3 – Run the Program

```powershell
python 01_if_else.py
```

If the `python` command is not available, try:

```powershell
py 01_if_else.py
```

## Step 4 – View the Main Menu

```text
=================================================================
                  PYTHON - IF-ELSE STATEMENT
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
| 1 | Displays all 12 topic examples |
| 2 | Opens the 12 solved problems |
| 3 | Displays 10 unsolved practice questions |
| 4 | Displays the learning checklist |
| 0 | Exits the program |

---

# 49. Repository Folder Structure

The current topic folder should contain:

```text
02-If-Else/
│
├── 01_if_else.py
│
└── README.md
```

The complete conditional statements section is organized as follows:

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
│   │
│   ├── 01-positive-negative/
│   │   ├── README.md
│   │   └── 01_positive_negative.py
│   │
│   ├── 02-even-odd/
│   │   ├── README.md
│   │   └── 02_even_odd.py
│   │
│   ├── 03-largest-number/
│   │   ├── README.md
│   │   └── 03_largest_number.py
│   │
│   ├── 04-leap-year/
│   │   ├── README.md
│   │   └── 04_leap_year.py
│   │
│   ├── 05-grade-calculator/
│   │   ├── README.md
│   │   └── 05_grade_calculator.py
│   │
│   └── 06-voting-eligibility/
│       ├── README.md
│       └── 06_voting_eligibility.py
│
└── 07-Match-Case/
    ├── README.md
    └── 01_match_case.py
```

---

# 50. Previous and Next Topics

## Previous Topic

**01 – If Statement**

Folder:

```text
01-If-Statement/
```

Concepts covered:

- Basic if syntax.
- Conditions.
- Boolean values.
- Truthy and falsy values.
- Comparison operators.
- Indentation.
- Basic decision-making.

## Current Topic

**02 – If-Else**

Folder:

```text
02-If-Else/
```

Concepts covered:

- Two alternative execution paths.
- True and false branches.
- `if` and `else`.
- Conditional calculations.
- Logical conditions.
- Practical decision-making.

## Next Topic

**03 – If-Elif-Else**

Folder:

```text
03-If-Elif-Else/
```

The next topic will explain how to handle multiple conditions and select among several possible branches.

---

# 51. Final Summary

The Python `if-else` statement is an important part of programming because it allows a program to make decisions between two possible outcomes.

In this topic, you studied:

- Conditional statements.
- Decision-making.
- If-else syntax.
- The condition.
- The if block.
- The else block.
- True and false execution paths.
- Difference between if and if-else.
- Difference between independent if statements and if-else.
- Boolean values.
- Truthy and falsy values.
- Comparison operators.
- Arithmetic operators in conditions.
- Logical operators.
- Membership operators.
- Identity operators.
- Indentation and code blocks.
- User input and conversion.
- If-else with integers.
- If-else with floating-point numbers.
- If-else with strings.
- If-else with lists and dictionaries.
- If-else with functions.
- Nested conditions.
- Short-circuit evaluation.
- Practical applications.
- Data structures and algorithms.
- Dry runs and trace tables.
- Common mistakes and debugging.
- Time and space complexity.

## Final Advice

Do not memorize only the syntax.

Understand the difference between the true and false execution paths.

Practice changing input values and predicting which block will execute.

Start with simple conditions, then move to logical conditions and real-world programming problems.

The `if-else` statement is an important foundation for learning `if-elif-else`, nested conditions and more advanced decision-making.

**Continue practicing Python and build a strong foundation for Data Structures and Algorithms.**

---

**END OF README – TOPIC 02: IF-ELSE STATEMENT**