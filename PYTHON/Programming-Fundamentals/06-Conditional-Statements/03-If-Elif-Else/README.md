# Python If-Elif-Else Statement – Complete Detailed Guide

## Week 1 – Programming Fundamentals

**Section:** 06 – Conditional Statements  
**Topic:** 03 – If-Elif-Else Statement  
**Python File:** `01_if_elif_else.py`  
**Documentation File:** `README.md`  
**Level:** Beginner to Intermediate

---

# Table of Contents

1. Introduction to Conditional Statements
2. What Is Decision-Making?
3. What Is an If-Elif-Else Statement?
4. Why Do We Need If-Elif-Else?
5. Syntax of If-Elif-Else
6. Components of If-Elif-Else
7. Understanding the If Branch
8. Understanding the Elif Branch
9. Understanding the Else Branch
10. How Python Executes If-Elif-Else
11. First-Matching-Condition Rule
12. Difference Between If, If-Else and If-Elif-Else
13. Difference Between Multiple If and Elif
14. Boolean Values and Truthiness
15. Comparison Operators
16. Logical Operators
17. Arithmetic Operators in Conditions
18. Membership and Identity Operators
19. Importance of Condition Ordering
20. Boundary Values and Range Checking
21. Multiple Elif Branches
22. Nested If-Elif-Else
23. If-Elif-Else With User Input
24. If-Elif-Else With Integer Values
25. If-Elif-Else With Floating-Point Values
26. If-Elif-Else With Strings and Characters
27. If-Elif-Else With Collections
28. If-Elif-Else With Functions
29. If-Elif-Else With Mathematical Formulas
30. If-Elif-Else in Real-World Applications
31. Explanation of 12 Topic Examples
32. Twelve Solved Programming Problems
33. Ten Unsolved Practice Questions
34. Dry Runs and Trace Tables
35. Algorithms and Flowcharts
36. Common Programming Mistakes
37. Debugging Techniques
38. Best Practices
39. If-Elif-Else and Data Structures
40. If-Elif-Else and DSA
41. Time and Space Complexity
42. Mini Project – Student Grade and Performance System
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

Python is a general-purpose programming language used for software development, web development, automation, data processing, artificial intelligence and many other applications.

A Python program contains instructions that tell the computer which operations to perform.

In a simple program, instructions commonly execute one after another. However, real-world applications often need to make decisions.

For example:

- A student receives a particular grade depending on their marks.
- A shopping application applies different discounts depending on the bill amount.
- A calculator performs an operation depending on the selected operator.
- A program identifies the name of a day using its number.
- A system calculates a ticket price according to the passenger's age.
- A program categorizes temperatures into different ranges.
- An electricity bill calculator applies different rates to different consumption slabs.

These situations involve more than two possible outcomes.

A basic `if` statement handles a condition that controls one block.

An `if-else` statement handles two alternative blocks.

When several conditions must be checked, Python provides the `if-elif-else` structure.

This structure allows a program to check multiple conditions in sequence.

## 1.1 What Is Decision-Making?

Decision-making means selecting an action according to one or more conditions.

Consider a student grade calculator.

Suppose the grading rules are:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89 | B |
| 60–74 | C |
| 40–59 | D |
| Below 40 | F |

The program needs to check several conditions to determine the grade.

Python program:

```python
marks = 85

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"

print("Grade:", grade)
```

Output:

```text
Grade: B
```

Python checks each condition from top to bottom.

The first condition is false.

The second condition is true.

Therefore, Python selects grade B and skips the remaining branches.

## 1.2 Why Are Conditional Statements Important?

Conditional statements allow a program to respond differently to different values and situations.

Without conditions, a program would not be able to select appropriate actions based on changing inputs.

For example, a calculator must choose an operation based on the selected operator.

A grade calculator must select a grade based on marks.

A delivery application must select a delivery charge based on an order amount.

A character classifier must select an output based on the character entered.

## 1.3 Benefits of Conditional Statements

1. They support decision-making.
2. They help classify values.
3. They support multiple possible outcomes.
4. They allow input-based program behavior.
5. They help implement business rules.
6. They help validate user input.
7. They make programs flexible.
8. They support algorithm development.
9. They reduce unnecessary repeated code.
10. They help develop real-world applications.

---

# 2. What Is Decision-Making?

Decision-making in programming means selecting an action based on the result of a condition.

A condition is evaluated to determine its truth value.

Example:

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

else:
    print("Other Grade")
```

Output:

```text
Grade B
```

The program checks three possible branches.

1. `marks >= 90` evaluates to false.
2. `marks >= 75` evaluates to true.
3. Python executes the second branch.
4. The remaining branches are skipped.

## 2.1 Real-World Decision-Making Examples

| Situation | Condition | Selected Action |
|---|---|---|
| Student grade | Marks >= 90 | Grade A |
| Student grade | Marks >= 75 | Grade B |
| Day selection | Day number == 1 | Monday |
| Temperature | Temperature < 15 | Cold |
| Shopping | Price >= 5000 | Higher example discount |
| Traffic light | Signal == "red" | Stop |
| Calculator | Operator == "+" | Addition |
| Triangle | All sides equal | Equilateral |
| Electricity bill | Units > 200 | Higher consumption slab |
| Ticket system | Age >= 60 | Senior ticket category |

## 2.2 Steps Involved in Decision-Making

1. Receive an input or obtain values from variables.
2. Write the first condition.
3. Evaluate that condition.
4. If it is true, execute its block.
5. Otherwise, check the next condition.
6. Continue until a matching branch is found.
7. If no condition matches, execute the `else` block when it exists.
8. Continue with the remaining program instructions.

---

# 3. What Is an If-Elif-Else Statement?

The `if-elif-else` statement is a Python control-flow structure used to select one block from several possible alternatives.

It contains:

- One initial `if` condition.
- Zero or more `elif` conditions.
- An optional `else` block.

Example:

```python
number = 0

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

Output:

```text
Zero
```

The condition `number > 0` is false.

The condition `number < 0` is also false.

Therefore, Python executes the `else` block.

## 3.1 Definition

An `if-elif-else` statement evaluates multiple conditions in sequence and executes the block belonging to the first condition that evaluates to a truthy value.

If no condition matches and an `else` block is present, that block executes.

## 3.2 Important Characteristics

1. The `if` branch starts the conditional structure.
2. `elif` means "else if".
3. Multiple `elif` branches can be used.
4. The `else` branch is optional.
5. Each `elif` contains its own condition.
6. Conditions are evaluated from top to bottom.
7. The first matching branch is selected.
8. Remaining `elif` conditions are skipped after a match.
9. The `else` block executes when all earlier conditions are falsy.
10. Indentation identifies each branch.
11. Every branch requires a colon.
12. Multiple statements can appear inside a branch.

---

# 4. Why Do We Need If-Elif-Else?

A basic `if` statement handles one condition.

An `if-else` statement handles two alternatives.

However, many real-world problems require more than two possible outcomes.

Consider classifying a student's marks.

Using only `if`:

```python
marks = 85

if marks >= 90:
    print("Grade A")
```

This does not handle lower grades.

Using `if-else`:

```python
marks = 85

if marks >= 90:
    print("Grade A")

else:
    print("Grade below A")
```

This provides only two alternatives.

Using `if-elif-else`:

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Grade F")
```

This program can classify five different grade categories.

## 4.1 Problems Solved Using If-Elif-Else

1. Grade calculation.
2. Temperature classification.
3. Day-name selection.
4. Month-name selection.
5. Calculator operations.
6. Ticket price calculation.
7. Discount categories.
8. Electricity bill calculation.
9. Character classification.
10. Triangle classification.

---

# 5. Syntax of If-Elif-Else

The general syntax is:

```python
if condition_1:
    statement_1

elif condition_2:
    statement_2

elif condition_3:
    statement_3

else:
    default_statement
```

Example:

```python
number = 15

if number < 10:
    print("Small number")

elif number < 20:
    print("Medium number")

else:
    print("Large number")
```

Output:

```text
Medium number
```

## 5.1 Components of the Syntax

| Component | Description |
|---|---|
| `if` | Begins the conditional structure |
| `condition_1` | First condition |
| `elif` | Introduces another condition |
| `condition_2` | Second condition |
| Additional `elif` | Adds more possible conditions |
| `else` | Provides the default branch |
| Indented statements | Statements belonging to each branch |

## 5.2 The If Keyword

The `if` keyword begins the conditional structure.

Example:

```python
if number > 0:
    print("Positive")
```

Only one initial `if` is used in a single `if-elif-else` chain.

## 5.3 The Elif Keyword

`elif` is a Python keyword meaning "else if".

It provides another condition to check when all earlier conditions are falsy.

Example:

```python
marks = 80

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")
```

Output:

```text
B
```

## 5.4 Multiple Elif Branches

Python allows multiple `elif` branches.

Example:

```python
number = 3

if number == 1:
    print("One")

elif number == 2:
    print("Two")

elif number == 3:
    print("Three")

elif number == 4:
    print("Four")

else:
    print("Other number")
```

Output:

```text
Three
```

## 5.5 The Else Keyword

The `else` keyword introduces the default branch.

Example:

```python
number = 10

if number < 0:
    print("Negative")

elif number > 0:
    print("Positive")

else:
    print("Zero")
```

Output:

```text
Positive
```

The `else` branch does not contain a condition.

It handles every value that reaches it after all earlier conditions are falsy.

## 5.6 Is Else Compulsory?

No.

The `else` branch is optional.

Example:

```python
marks = 85

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")
```

The program can finish without executing any branch.

This is valid Python.

---

# 6. Components of If-Elif-Else

Consider:

```python
marks = 85

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

else:
    grade = "D or F"

print(grade)
```

The components are:

**Variable assignment**

```python
marks = 85
```

Stores the input value.

**Initial condition**

```python
if marks >= 90:
```

Checks the highest grade threshold.

**First alternative condition**

```python
elif marks >= 75:
```

Checks the next threshold when the earlier condition is false.

**Second alternative condition**

```python
elif marks >= 60:
```

Checks another possible grade.

**Default branch**

```python
else:
```

Handles values not covered by earlier conditions.

**Output**

```python
print(grade)
```

Displays the selected grade.

---

# 7. Understanding the If Branch

The `if` branch is the first branch in the conditional structure.

Python checks it before checking any `elif`.

Example:

```python
age = 12

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

else:
    print("Adult")
```

Output:

```text
Child
```

The first condition is true, so Python does not check the remaining branches.

## 7.1 Important Rule

The first condition should represent the first intended case.

Its position matters because a matching condition prevents later branches from being evaluated.

---

# 8. Understanding the Elif Branch

The `elif` branch provides additional conditions.

It is evaluated only when all earlier conditions are falsy.

Example:

```python
number = 15

if number < 10:
    print("Below 10")

elif number < 20:
    print("Between 10 and 19")

else:
    print("20 or above")
```

Output:

```text
Between 10 and 19
```

The first condition is false.

The second condition is true.

Python executes the second block.

## 8.1 More Than One Elif

```python
marks = 65

if marks >= 90:
    print("Excellent")

elif marks >= 75:
    print("Very Good")

elif marks >= 60:
    print("Good")

elif marks >= 40:
    print("Pass")

else:
    print("Fail")
```

Output:

```text
Good
```

## 8.2 Elif Without a Matching Else

```python
number = 50

if number < 10:
    print("Small")

elif number < 20:
    print("Medium")

elif number < 30:
    print("Large")
```

There is no output because every condition is false.

---

# 9. Understanding the Else Branch

The `else` block is the default branch.

It executes when all preceding conditions are falsy.

Example:

```python
number = 100

if number < 10:
    print("Small")

elif number < 50:
    print("Medium")

else:
    print("Large")
```

Output:

```text
Large
```

The `else` block covers the remaining values.

## 9.1 Why Is Else Useful?

It ensures that the program handles values not matched by previous conditions.

Example:

```python
signal = "blue"

if signal == "red":
    print("Stop")

elif signal == "green":
    print("Proceed when safe")

else:
    print("Unrecognized signal")
```

Output:

```text
Unrecognized signal
```

## 9.2 Else Is Optional

Not every conditional structure needs a default action.

However, include `else` when the program must handle unmatched values explicitly.

---

# 10. How Python Executes If-Elif-Else

Python evaluates the conditions sequentially.

Consider:

```python
marks = 80

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("F")
```

Execution:

1. Assign 80 to `marks`.
2. Check whether `marks >= 90`.
3. The condition is false.
4. Check whether `marks >= 75`.
5. The condition is true.
6. Execute the B branch.
7. Skip all remaining branches.
8. Continue after the conditional structure.

Output:

```text
B
```

## 10.1 Execution Flow

```text
               START
                 |
                 v
          Evaluate If Condition
                 |
            Is True?
             /    \
           Yes     No
            |       |
            v       v
        Execute   Evaluate
        If Block   Elif 1
                      |
                  Is True?
                   /    \
                 Yes     No
                  |       |
                  v       v
              Execute   Evaluate
              Elif 1    Elif 2
                           |
                       Is True?
                        /    \
                      Yes     No
                       |       |
                       v       v
                   Execute   Evaluate
                   Elif 2    More Elif
                               |
                         No Match Remaining
                               |
                               v
                              Else
                               |
                               v
                              END
```

The diagram represents a conditional chain with multiple branches.

---

# 11. First-Matching-Condition Rule

This is the most important rule of `if-elif-else`.

Python executes the first branch whose condition evaluates to a truthy value.

After that, the remaining branches in the same chain are skipped.

Example:

```python
number = 15

if number > 0:
    print("Positive")

elif number > 10:
    print("Greater than 10")

else:
    print("Other")
```

Output:

```text
Positive
```

Both conditions are true:

```python
number > 0
```

and:

```python
number > 10
```

However, Python executes the first branch.

It does not evaluate the second `elif` after the first branch has matched.

## 11.1 First Match With Grade Calculation

```python
marks = 95

if marks >= 40:
    grade = "Pass"

elif marks >= 90:
    grade = "A"

else:
    grade = "Fail"

print(grade)
```

Output:

```text
Pass
```

This happens because the first condition matches.

The program does not reach the grade A condition.

Correct ordering:

```python
marks = 95

if marks >= 90:
    grade = "A"

elif marks >= 40:
    grade = "Pass"

else:
    grade = "Fail"

print(grade)
```

Output:

```text
A
```

This demonstrates why condition ordering is important.

---

# 12. Difference Between If, If-Else and If-Elif-Else

These structures all support conditional execution but serve different requirements.

## 12.1 If Statement

```python
marks = 30

if marks >= 40:
    print("Pass")
```

When the condition is false, the block is skipped.

## 12.2 If-Else Statement

```python
marks = 30

if marks >= 40:
    print("Pass")

else:
    print("Fail")
```

This handles two possible outcomes.

## 12.3 If-Elif-Else Statement

```python
marks = 85

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

elif marks >= 40:
    print("D")

else:
    print("F")
```

This handles several possible outcomes.

## 12.4 Comparison Table

| Feature | If | If-Else | If-Elif-Else |
|---|---|---|---|
| Number of initial if branches | One | One | One |
| Alternative branch | No | One else | Multiple elif and optional else |
| False condition | Block skipped | Else executes | Next condition checked |
| Multiple alternatives | No | Two paths | Several paths |
| Best use | Optional action | Two possible outcomes | Multiple possible outcomes |

## 12.5 Choosing the Right Structure

Use `if` when only one condition needs to control an action.

Use `if-else` when exactly two alternative actions are needed.

Use `if-elif-else` when several conditions must be checked in sequence.

---

# 13. Difference Between Multiple If and Elif

Multiple independent `if` statements are different from an `if-elif-else` chain.

## 13.1 Multiple Independent If Statements

```python
number = 15

if number > 0:
    print("Positive")

if number > 10:
    print("Greater than 10")

if number % 2 != 0:
    print("Odd")
```

Output:

```text
Positive
Greater than 10
Odd
```

Each condition is evaluated independently.

## 13.2 If-Elif-Else

```python
number = 15

if number > 0:
    print("Positive")

elif number > 10:
    print("Greater than 10")

else:
    print("Other")
```

Output:

```text
Positive
```

Only the first branch is executed.

## 13.3 Comparison Table

| Multiple If | If-Elif-Else |
|---|---|
| Each if is independent | Conditions belong to one chain |
| Several blocks can execute | At most one branch executes |
| Every if is reached separately | Later conditions are skipped after a match |
| Useful for independent checks | Useful for selecting one category |

## 13.4 When to Use Multiple If

Use independent `if` statements when multiple conditions can all be true and every matching action should execute.

## 13.5 When to Use Elif

Use `elif` when the conditions represent alternatives and only the first matching action should execute.

---

# 14. Boolean Values and Truthiness

Python has two Boolean values:

```python
True
False
```

Comparison expressions commonly produce Boolean results.

Example:

```python
number = 10

print(number > 0)
```

Output:

```text
True
```

An `if-elif-else` condition can also use non-Boolean objects directly through Python's truth-value testing.

## 14.1 Truthy Values

Examples of truthy values:

```python
1
-1
10.5
"Python"
[10, 20]
(10, 20)
{"name": "Amaan"}
{1, 2}
```

## 14.2 Falsy Values

Common falsy values include:

```python
False
None
0
0.0
0j
""
[]
()
{}
set()
range(0)
```

## 14.3 Example

```python
name = ""

if name:
    print("Name available")

elif name is None:
    print("Name not provided")

else:
    print("Empty name")
```

Output:

```text
Empty name
```

The empty string is falsy but is not `None`.

---

# 15. Comparison Operators

Comparison operators compare values and produce Boolean results.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal | `a >= b` |
| `<=` | Less than or equal | `a <= b` |

Example:

```python
marks = 85

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

else:
    print("Below B")
```

Output:

```text
B
```

## 15.1 Equality

```python
number = 10

if number == 10:
    print("Exactly 10")

elif number > 10:
    print("Greater than 10")

else:
    print("Less than 10")
```

## 15.2 Inequality

```python
number = 20

if number != 0:
    print("Non-zero number")

else:
    print("Zero")
```

## 15.3 Range Checking

```python
marks = 85

if 90 <= marks <= 100:
    print("Excellent")

elif 75 <= marks < 90:
    print("Very good")

elif 60 <= marks < 75:
    print("Good")

else:
    print("Needs improvement")
```

---

# 16. Logical Operators

Logical operators combine or reverse conditions.

Python provides:

- `and`
- `or`
- `not`

## 16.1 AND

Both operands must be truthy for the combined result to be truthy.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access allowed")

else:
    print("Access denied")
```

## 16.2 OR

At least one operand must be truthy.

```python
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount available")

else:
    print("No discount")
```

## 16.3 NOT

The `not` operator reverses truthiness.

```python
is_raining = False

if not is_raining:
    print("Not raining")

else:
    print("Raining")
```

## 16.4 Multiple Logical Conditions

```python
age = 20
marks = 80
has_id = True

if age >= 18 and marks >= 40 and has_id:
    print("All requirements satisfied")

elif age < 18:
    print("Age requirement not satisfied")

else:
    print("Other requirements not satisfied")
```

---

# 17. Arithmetic Operators in Conditions

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

Example:

```python
number = 15

if number % 2 == 0:
    print("Even")

elif number % 3 == 0:
    print("Divisible by 3")

else:
    print("Neither condition matched")
```

Output:

```text
Divisible by 3
```

The even condition is checked first.

It is false, so Python evaluates the second condition.

## 17.1 Arithmetic Conditions

```python
a = 10
b = 20

if a + b > 50:
    print("Large sum")

elif a + b > 20:
    print("Medium sum")

else:
    print("Small sum")
```

Output:

```text
Medium sum
```

---

# 18. Membership and Identity Operators

## 18.1 Membership Operators

Python provides `in` and `not in`.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

if "Apple" in fruits:
    print("Apple found")

elif "Mango" in fruits:
    print("Mango found")

else:
    print("Fruit not found")
```

Output:

```text
Apple found
```

The first matching branch executes.

## 18.2 Identity Operators

Python provides `is` and `is not`.

Example:

```python
value = None

if value is None:
    print("Value is None")

elif value is not None:
    print("Value is available")

else:
    print("Unexpected result")
```

Output:

```text
Value is None
```

Use identity operators for object identity and `None` checks.

Use `==` for ordinary value equality.

---

# 19. Importance of Condition Ordering

The order of conditions is one of the most important aspects of `if-elif-else`.

Python checks branches from top to bottom.

A branch executes when its condition is the first truthy condition.

Example of incorrect ordering:

```python
marks = 95

if marks >= 40:
    grade = "Pass"

elif marks >= 90:
    grade = "A"

else:
    grade = "Fail"

print(grade)
```

Output:

```text
Pass
```

The first condition matches, so the A condition is never checked.

Correct ordering:

```python
marks = 95

if marks >= 90:
    grade = "A"

elif marks >= 40:
    grade = "Pass"

else:
    grade = "Fail"

print(grade)
```

Output:

```text
A
```

## 19.1 General Ordering Rule for Descending Thresholds

When larger values should receive higher categories, check the higher threshold first.

Example:

```python
if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("Other")
```

## 19.2 General Ordering Rule for Increasing Ranges

When values belong to increasing ranges, checking the smallest range first can be suitable.

Example:

```python
temperature = 20

if temperature < 0:
    print("Freezing")

elif temperature < 15:
    print("Cold")

elif temperature < 25:
    print("Pleasant")

else:
    print("Warm or hot")
```

## 19.3 Unreachable Branches

A branch is unreachable when an earlier condition always matches whenever the later condition would match.

Example:

```python
number = 15

if number > 0:
    print("Positive")

elif number > 10:
    print("Greater than 10")
```

The second branch is unreachable because every number greater than 10 is already greater than zero.

This is a logical ordering mistake.

---

# 20. Boundary Values and Range Checking

Boundary values are values located at the edges of a range.

They are important when designing conditions.

Suppose the grade ranges are:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89.99 | B |
| 60–74.99 | C |
| 40–59.99 | D |
| Below 40 | F |

The conditions can be written:

```python
if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"
```

This works because the ranges are checked in descending order.

## 20.1 Important Boundary Tests

| Input | Expected Grade |
|---:|---|
| 100 | A |
| 90 | A |
| 89.99 | B |
| 75 | B |
| 74.99 | C |
| 60 | C |
| 59.99 | D |
| 40 | D |
| 39.99 | F |
| 0 | F |

## 20.2 Why Boundary Testing Matters

Many programming mistakes occur at range boundaries.

For example:

```python
if marks > 40:
    grade = "Pass"
```

This excludes exactly 40.

When the threshold includes 40, use:

```python
if marks >= 40:
    grade = "Pass"
```

---

# 21. Multiple Elif Branches

Python allows multiple `elif` branches within a conditional chain.

Example:

```python
number = 4

if number == 1:
    print("One")

elif number == 2:
    print("Two")

elif number == 3:
    print("Three")

elif number == 4:
    print("Four")

else:
    print("Other")
```

Output:

```text
Four
```

## 21.1 Day Selection

```python
day = 5

if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

else:
    print("Invalid day")
```

## 21.2 Month Selection

The same structure can map month numbers to month names.

## 21.3 When Should You Use Many Elif Branches?

Use multiple `elif` branches when:

- Several mutually exclusive categories exist.
- Conditions have a clear checking order.
- Each category requires a different action.
- The number of branches remains manageable.

For large fixed mappings, a dictionary may be a better solution.

For complex value matching, Python's `match-case` may be useful.

---

# 22. Nested If-Elif-Else

A nested conditional structure contains one conditional statement inside another.

Example:

```python
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Access allowed")

    else:
        print("ID required")

else:
    print("Age requirement not satisfied")
```

The outer condition is evaluated first.

The inner condition is evaluated only when the outer condition is true.

Nested conditions are useful when later decisions depend on earlier decisions.

A complete study of nested conditions is provided separately under:

`04-Nested-If/README.md`

---

# 23. If-Elif-Else With User Input

The `input()` function allows users to enter values.

It returns a string, so numeric input must be converted when numerical comparisons are required.

## 23.1 Integer Input

```python
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

## 23.2 Float Input

```python
temperature = float(input("Enter temperature: "))

if temperature < 0:
    print("Freezing")

elif temperature < 20:
    print("Cold")

else:
    print("Warm")
```

## 23.3 String Input

```python
signal = input("Enter signal: ").strip().lower()

if signal == "red":
    print("Stop")

elif signal == "yellow":
    print("Prepare to stop")

elif signal == "green":
    print("Proceed when safe")

else:
    print("Invalid signal")
```

## 23.4 Input Validation

```python
try:
    marks = float(input("Enter marks: "))

    if not math.isfinite(marks):
        print("Enter a finite number.")

    elif not 0 <= marks <= 100:
        print("Invalid marks.")

    elif marks >= 90:
        print("Grade A")

    elif marks >= 75:
        print("Grade B")

    elif marks >= 60:
        print("Grade C")

    elif marks >= 40:
        print("Grade D")

    else:
        print("Grade F")

except ValueError:
    print("Please enter a valid number.")
```

---

# 24. If-Elif-Else With Integer Values

## Example 1 – Positive, Negative or Zero

```python
number = -5

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

## Example 2 – Even, Odd and Zero

```python
number = 0

if number == 0:
    print("Zero")

elif number % 2 == 0:
    print("Even")

else:
    print("Odd")
```

## Example 3 – Range Classification

```python
number = 75

if number < 0:
    print("Negative")

elif number <= 10:
    print("0 to 10")

elif number <= 50:
    print("11 to 50")

elif number <= 100:
    print("51 to 100")

else:
    print("Above 100")
```

## Example 4 – Divisibility

```python
number = 30

if number % 5 == 0 and number % 3 == 0:
    print("Divisible by both")

elif number % 5 == 0:
    print("Divisible by 5")

elif number % 3 == 0:
    print("Divisible by 3")

else:
    print("Not divisible by either")
```

---

# 25. If-Elif-Else With Floating-Point Values

Floating-point values can represent decimal measurements, prices and percentages.

Example:

```python
temperature = 28.5

if temperature < 0:
    print("Freezing")

elif temperature < 15:
    print("Cold")

elif temperature < 25:
    print("Pleasant")

elif temperature < 35:
    print("Warm")

else:
    print("Hot")
```

Output:

```text
Warm
```

## 25.1 Floating-Point Comparisons

Binary floating-point numbers can represent some decimal fractions only approximately.

Example:

```python
value = 0.1 + 0.2

print(value)
```

Typical output:

```text
0.30000000000000004
```

For approximate comparisons, use:

```python
import math

if math.isclose(value, 0.3):
    print("Approximately equal")

else:
    print("Not approximately equal")
```

---

# 26. If-Elif-Else With Strings and Characters

String comparisons can be used to classify input.

## 26.1 Traffic Signal

```python
signal = "yellow"

if signal == "red":
    print("Stop")

elif signal == "yellow":
    print("Prepare to stop")

elif signal == "green":
    print("Proceed when safe")

else:
    print("Unknown signal")
```

## 26.2 Character Classification

```python
character = "A"

if character.isupper():
    print("Uppercase letter")

elif character.islower():
    print("Lowercase letter")

elif character.isdigit():
    print("Digit")

else:
    print("Other character")
```

## 26.3 Vowel and Consonant

```python
character = "e"

if character.lower() in "aeiou":
    print("Vowel")

elif character.lower().isalpha():
    print("Consonant")

else:
    print("Not an alphabet character")
```

For this example, assume a single alphabet character is entered.

## 26.4 Case-Insensitive Input

```python
answer = input("Enter yes or no: ").strip().lower()

if answer == "yes":
    print("Accepted")

elif answer == "no":
    print("Rejected")

else:
    print("Invalid answer")
```

---

# 27. If-Elif-Else With Collections

## 27.1 Lists

```python
numbers = []

if len(numbers) == 0:
    print("Empty list")

elif len(numbers) < 5:
    print("Small list")

else:
    print("Large list")
```

## 27.2 Tuples

```python
values = (10, 20, 30)

if not values:
    print("Empty tuple")

elif len(values) == 1:
    print("Single element")

else:
    print("Multiple elements")
```

## 27.3 Dictionaries

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" not in student:
    print("Marks missing")

elif student["marks"] >= 40:
    print("Pass")

else:
    print("Fail")
```

## 27.4 Sets

```python
numbers = {10, 20, 30}

if not numbers:
    print("Empty set")

elif 20 in numbers:
    print("20 exists")

else:
    print("20 does not exist")
```

---

# 28. If-Elif-Else With Functions

Functions can provide values that are used in conditions.

Example:

```python
def classify_number(number):
    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    else:
        return "Zero"


print(classify_number(-10))
```

Output:

```text
Negative
```

## 28.1 Reusable Grade Function

```python
def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


print(calculate_grade(85))
```

Output:

```text
B
```

## 28.2 Why Use Functions?

Functions:

1. Reduce repeated code.
2. Organize logic.
3. Make testing easier.
4. Support reusable conditions.
5. Improve readability.

---

# 29. If-Elif-Else With Mathematical Formulas

## 29.1 Leap Year Calculation

A Gregorian calendar year is a leap year when it is divisible by 400 or divisible by 4 but not by 100.

```python
year = 2024

if year % 400 == 0:
    print("Leap year")

elif year % 100 == 0:
    print("Not a leap year")

elif year % 4 == 0:
    print("Leap year")

else:
    print("Not a leap year")
```

## 29.2 Progressive Billing

A progressive billing rule applies different rates to different parts of consumption.

Example:

```python
units = 250

if units <= 100:
    bill = units * 1.50

elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50

else:
    bill = (
        100 * 1.50
        + 100 * 2.50
        + (units - 200) * 4.00
    )

print(bill)
```

For 250 units:

```text
First 100 units = 150
Next 100 units = 250
Remaining 50 units = 200

Total = 600
```

Output:

```text
600.0
```

These are illustrative rates, not an actual utility tariff.

---

# 30. If-Elif-Else in Real-World Applications

Conditional chains are used in many applications.

## 30.1 Student Grading

```python
if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"
```

## 30.2 Shopping Discounts

```python
if amount >= 5000:
    discount = 0.20

elif amount >= 3000:
    discount = 0.15

elif amount >= 1000:
    discount = 0.10

else:
    discount = 0
```

## 30.3 Ticket Pricing

```python
if age < 5:
    price = 0

elif age < 18:
    price = 50

elif age < 60:
    price = 100

else:
    price = 70
```

## 30.4 Traffic Signal

```python
if signal == "red":
    action = "Stop"

elif signal == "yellow":
    action = "Prepare to stop"

elif signal == "green":
    action = "Proceed when safe"

else:
    action = "Unknown signal"
```

---

# 31. Explanation of 12 Topic Examples

This section explains all twelve examples included in `01_if_elif_else.py`.

## Example 1 – Basic If-Elif-Else

Code:

```python
age = 20

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

else:
    print("Adult")
```

Output:

```text
Adult
```

Dry run:

| Step | Condition | Result |
|---|---|---|
| 1 | `20 < 13` | False |
| 2 | `20 < 20` | False |
| 3 | Else branch | Executes |
| 4 | Output | Adult |

Explanation:

The first two conditions are false.

Therefore, the `else` block executes.

## Example 2 – Positive, Negative or Zero

Code:

```python
number = -10

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

Output:

```text
Negative
```

Explanation:

1. `-10 > 0` is false.
2. `-10 < 0` is true.
3. The negative branch executes.
4. The else branch is skipped.

## Example 3 – Grade Calculator

Code:

```python
marks = 85

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"

print(grade)
```

Output:

```text
B
```

Explanation:

The first condition is false.

The second condition is true.

The grade B branch executes.

## Example 4 – Largest of Three Numbers

Code:

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

print(largest)
```

Output:

```text
50
```

Explanation:

1. The first value is not greater than both other values.
2. The second value is greater than or equal to both.
3. Therefore, the second value is selected.

## Example 5 – Day of the Week

Code:

```python
day_number = 3

if day_number == 1:
    day = "Monday"

elif day_number == 2:
    day = "Tuesday"

elif day_number == 3:
    day = "Wednesday"

elif day_number == 4:
    day = "Thursday"

elif day_number == 5:
    day = "Friday"

elif day_number == 6:
    day = "Saturday"

elif day_number == 7:
    day = "Sunday"

else:
    day = "Invalid day number"

print(day)
```

Output:

```text
Wednesday
```

Explanation:

The third condition matches.

The remaining branches are skipped.

## Example 6 – Temperature Classification

Code:

```python
temperature = 28

if temperature < 0:
    category = "Freezing"

elif temperature < 15:
    category = "Cold"

elif temperature < 25:
    category = "Pleasant"

elif temperature < 35:
    category = "Warm"

else:
    category = "Hot"

print(category)
```

Output:

```text
Warm
```

Explanation:

- 28 is not below 0.
- 28 is not below 15.
- 28 is not below 25.
- 28 is below 35.
- Therefore, Warm is selected.

## Example 7 – Traffic Light

Code:

```python
signal = "yellow"

if signal == "red":
    action = "Stop"

elif signal == "yellow":
    action = "Prepare to stop"

elif signal == "green":
    action = "Proceed when safe"

else:
    action = "Invalid signal"

print(action)
```

Output:

```text
Prepare to stop
```

Explanation:

The second condition matches.

## Example 8 – Discount Category

Code:

```python
price = 3500

if price >= 5000:
    discount_rate = 0.20

elif price >= 3000:
    discount_rate = 0.15

elif price >= 1000:
    discount_rate = 0.10

else:
    discount_rate = 0

discount = price * discount_rate
final_price = price - discount

print(final_price)
```

Output:

```text
2975.0
```

Calculation:

```text
Discount = 3500 * 0.15
Discount = 525

Final price = 3500 - 525
Final price = 2975
```

## Example 9 – Vowel, Consonant or Invalid Character

Code:

```python
character = "A"

if not ("a" <= character.lower() <= "z"):
    result = "Not an English alphabet character"

elif character.lower() in "aeiou":
    result = "Vowel"

else:
    result = "Consonant"

print(result)
```

Output:

```text
Vowel
```

The example file includes a length validation condition too, although its fixed test character is one character long.

## Example 10 – Basic Calculator

Code:

```python
a = 20
b = 10
operator = "*"

if operator == "+":
    result = a + b

elif operator == "-":
    result = a - b

elif operator == "*":
    result = a * b

elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Division by zero is not allowed."

else:
    result = "Invalid operator."

print(result)
```

Output:

```text
200
```

The multiplication condition matches.

The remaining branches are skipped.

The division branch contains a nested `if` to protect against division by zero.

## Example 11 – Triangle Classification

Code:

```python
a = 5
b = 5
c = 5

if (
    a <= 0
    or b <= 0
    or c <= 0
    or a + b <= c
    or a + c <= b
    or b + c <= a
):
    triangle_type = "Invalid triangle"

elif a == b == c:
    triangle_type = "Equilateral triangle"

elif a == b or b == c or a == c:
    triangle_type = "Isosceles triangle"

else:
    triangle_type = "Scalene triangle"

print(triangle_type)
```

Output:

```text
Equilateral triangle
```

Explanation:

1. All sides must be positive.
2. Triangle inequality must hold.
3. All sides are equal.
4. Therefore, the triangle is equilateral.

## Example 12 – Number Range Classification

Code:

```python
number = 75

if number < 0:
    category = "Negative range"

elif number <= 10:
    category = "Between 0 and 10"

elif number <= 50:
    category = "Between 11 and 50"

elif number <= 100:
    category = "Between 51 and 100"

else:
    category = "Greater than 100"

print(category)
```

Output:

```text
Between 51 and 100
```

Explanation:

The first three conditions are false.

The fourth condition is true.

Therefore, the fourth branch executes.

---

# 32. Twelve Solved Programming Problems

## Problem 1 – Positive, Negative or Zero

Objective:

Accept a number and classify it into three categories.

Code:

```python
number = float(input("Enter a number: "))

if number > 0:
    result = "Positive"

elif number < 0:
    result = "Negative"

else:
    result = "Zero"

print(result)
```

Algorithm:

1. Start.
2. Read a number.
3. Check whether it is positive.
4. If not, check whether it is negative.
5. Otherwise, classify it as zero.
6. Display the result.

Test cases:

| Input | Output |
|---:|---|
| 10 | Positive |
| -10 | Negative |
| 0 | Zero |
| 2.5 | Positive |
| -2.5 | Negative |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 2 – Even or Odd

Objective:

Accept an integer and classify it as even or odd.

Code:

```python
number = int(input("Enter an integer: "))

if number == 0:
    print("Zero is an even integer.")

elif number % 2 == 0:
    print("Even")

else:
    print("Odd")
```

Test cases:

| Input | Output |
|---:|---|
| 0 | Zero is an even integer |
| 2 | Even |
| 7 | Odd |
| -4 | Even |
| -5 | Odd |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 3 – Grade Calculator

Objective:

Assign a grade based on marks.

Example grading scale:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89.99 | B |
| 60–74.99 | C |
| 40–59.99 | D |
| Below 40 | F |

Code:

```python
marks = float(input("Enter marks: "))

if not 0 <= marks <= 100:
    print("Invalid marks.")

elif marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Grade F")
```

Test cases:

| Marks | Grade |
|---:|---|
| 95 | A |
| 80 | B |
| 65 | C |
| 50 | D |
| 30 | F |
| -1 | Invalid |
| 101 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 4 – Largest of Three Numbers

Objective:

Find the largest among three numbers.

Code:

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c

print("Largest:", largest)
```

Test cases:

| A | B | C | Largest |
|---:|---:|---:|---:|
| 10 | 20 | 30 | 30 |
| 50 | 20 | 30 | 50 |
| 10 | 50 | 30 | 50 |
| 5 | 5 | 5 | 5 |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 5 – Day of the Week

Objective:

Accept a number from 1 to 7 and display the corresponding weekday.

Code:

```python
day = int(input("Enter day number: "))

if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

else:
    print("Invalid day")
```

Test cases:

| Input | Output |
|---:|---|
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |
| 7 | Sunday |
| 8 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 6 – Month and Number of Days

Objective:

Accept a month number and year, then display the number of days in that month.

Code:

```python
month = int(input("Enter month number: "))
year = int(input("Enter year: "))

if month == 1:
    print("January - 31 days")

elif month == 2:

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("February - 29 days")

    else:
        print("February - 28 days")

elif month == 3:
    print("March - 31 days")

elif month == 4:
    print("April - 30 days")

elif month == 5:
    print("May - 31 days")

elif month == 6:
    print("June - 30 days")

elif month == 7:
    print("July - 31 days")

elif month == 8:
    print("August - 31 days")

elif month == 9:
    print("September - 30 days")

elif month == 10:
    print("October - 31 days")

elif month == 11:
    print("November - 30 days")

elif month == 12:
    print("December - 31 days")

else:
    print("Invalid month")
```

Test cases:

| Month | Year | Expected Days |
|---:|---:|---:|
| 1 | 2024 | 31 |
| 2 | 2024 | 29 |
| 2 | 2023 | 28 |
| 4 | 2024 | 30 |
| 12 | 2024 | 31 |
| 13 | 2024 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

The leap-year rule is the Gregorian calendar rule.

## Problem 7 – Basic Calculator

Objective:

Create a calculator supporting addition, subtraction, multiplication and division.

Code:

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = a + b

elif operator == "-":
    result = a - b

elif operator == "*":
    result = a * b

elif operator == "/":

    if b != 0:
        result = a / b

    else:
        result = None
        print("Division by zero is not allowed.")

else:
    result = None
    print("Invalid operator.")

if result is not None:
    print("Result:", result)
```

Test cases:

| A | B | Operator | Result |
|---:|---:|---|---:|
| 10 | 5 | `+` | 15 |
| 10 | 5 | `-` | 5 |
| 10 | 5 | `*` | 50 |
| 10 | 5 | `/` | 2 |
| 10 | 0 | `/` | Error message |
| 10 | 5 | `%` | Invalid operator |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 8 – Triangle Type Checker

Objective:

Classify a valid triangle as equilateral, isosceles or scalene.

Code:

```python
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle.")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle.")

elif a == b == c:
    print("Equilateral triangle.")

elif a == b or b == c or a == c:
    print("Isosceles triangle.")

else:
    print("Scalene triangle.")
```

Test cases:

| A | B | C | Result |
|---:|---:|---:|---|
| 5 | 5 | 5 | Equilateral |
| 5 | 5 | 8 | Isosceles |
| 3 | 4 | 5 | Scalene |
| 1 | 2 | 3 | Invalid |
| 0 | 4 | 5 | Invalid |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 9 – Character Classifier

Objective:

Classify one character as vowel, consonant, digit or other character.

Code:

```python
character = input("Enter one character: ").strip()

if len(character) != 1:
    print("Please enter exactly one character.")

elif character.isalpha() and character.isascii():

    if character.lower() in "aeiou":
        print("Vowel")

    else:
        print("Consonant")

elif character.isdigit():
    print("Digit")

else:
    print("Special or other character")
```

Test cases:

| Input | Result |
|---|---|
| A | Vowel |
| b | Consonant |
| 5 | Digit |
| @ | Special character |
| ab | Invalid length |

Complexity:

- Time: O(1) for the single-character classification.
- Auxiliary space: O(1).

## Problem 10 – Electricity Bill Calculator

Objective:

Calculate a bill using progressive unit slabs.

Example rates:

- First 100 units: 1.50 per unit.
- Next 100 units: 2.50 per unit.
- Above 200 units: 4.00 per unit.

Code:

```python
units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units.")

elif units <= 100:
    bill = units * 1.50

elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50

else:
    bill = (
        100 * 1.50
        + 100 * 2.50
        + (units - 200) * 4.00
    )

if units >= 0:
    print("Electricity bill:", round(bill, 2))
```

Test cases:

| Units | Calculation | Bill |
|---:|---|---:|
| 50 | 50 × 1.50 | 75 |
| 100 | 100 × 1.50 | 150 |
| 150 | 150 + 50 × 2.50 | 275 |
| 200 | 150 + 100 × 2.50 | 400 |
| 250 | 150 + 250 + 50 × 4 | 600 |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

These example rates do not represent an actual electricity provider's tariff.

## Problem 11 – Delivery Charge Calculator

Objective:

Calculate delivery charges according to order amount and membership.

Example rules:

- Member order of at least 1000: free delivery.
- Order of at least 500: delivery charge 30.
- Other orders: delivery charge 60.

Code:

```python
order_amount = float(input("Enter order amount: "))

is_member = input("Are you a member? (yes/no): ").strip().lower()

if is_member not in ("yes", "no"):
    print("Invalid membership input.")

elif order_amount <= 0:
    print("Invalid order amount.")

elif order_amount >= 1000 and is_member == "yes":
    delivery_charge = 0
    print("Free delivery.")

elif order_amount >= 500:
    delivery_charge = 30
    print("Reduced delivery charge.")

else:
    delivery_charge = 60
    print("Standard delivery charge.")

if is_member in ("yes", "no") and order_amount > 0:
    if (
        order_amount >= 1000 and is_member == "yes"
    ):
        total = order_amount

    elif order_amount >= 500:
        total = order_amount + 30

    else:
        total = order_amount + 60

    print("Total:", total)
```

The example in the Python file uses helper validation and directly calculates the selected delivery category.

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

## Problem 12 – Ticket Price Calculator

Objective:

Select a ticket price based on passenger age.

Example rules:

| Age | Ticket Category | Price |
|---|---|---:|
| Below 5 | Free | 0 |
| 5–17 | Child | 50 |
| 18–59 | Adult | 100 |
| 60 or above | Senior | 70 |

Code:

```python
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age.")

elif age < 5:
    print("Free entry")

elif age < 18:
    print("Child ticket - 50")

elif age < 60:
    print("Adult ticket - 100")

else:
    print("Senior ticket - 70")
```

Test cases:

| Age | Result |
|---:|---|
| 3 | Free entry |
| 5 | Child |
| 17 | Child |
| 18 | Adult |
| 59 | Adult |
| 60 | Senior |

Complexity:

- Time: O(1)
- Auxiliary space: O(1)

These prices are illustrative.

---

# 33. Ten Unsolved Practice Questions

Try solving these questions independently.

## Question 1 – Positive, Negative or Zero

Accept a number and classify it using `if-elif-else`.

## Question 2 – Grade Calculator

Accept marks and assign a grade using at least five categories.

## Question 3 – Largest of Four Numbers

Accept four numbers and find the largest using conditional branches.

## Question 4 – Month Name

Accept a number from 1 to 12 and display the corresponding month.

Display an invalid message for any other number.

## Question 5 – Days in a Month

Accept a month and year.

Display the correct number of days.

Include February leap-year logic.

## Question 6 – Advanced Calculator

Create a calculator supporting:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Modulo.

Handle division by zero and invalid operators.

## Question 7 – Triangle Classification

Accept three sides.

Validate the triangle and classify it as:

- Equilateral.
- Isosceles.
- Scalene.
- Invalid.

## Question 8 – Character Classification

Accept one character and classify it as:

- Uppercase letter.
- Lowercase letter.
- Digit.
- Special character.

## Question 9 – Progressive Electricity Bill

Create an electricity bill calculator using at least three unit slabs.

Define your own example rates.

## Question 10 – Performance Classification

Accept a student's score and classify performance into five or more named categories.

Check invalid scores too.

---

# 34. Dry Runs and Trace Tables

A dry run means manually following a program using known input values.

It helps understand which condition matches and which branch executes.

## 34.1 Grade Calculator Dry Run

Code:

```python
marks = 85

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"
```

Trace table:

| Step | Condition | Result |
|---|---|---|
| 1 | `85 >= 90` | False |
| 2 | `85 >= 75` | True |
| 3 | Selected branch | B |
| 4 | Remaining conditions | Skipped |

## 34.2 Positive, Negative or Zero

Input:

```text
-10
```

| Step | Condition | Result |
|---|---|---|
| 1 | `-10 > 0` | False |
| 2 | `-10 < 0` | True |
| 3 | Selected result | Negative |

## 34.3 Largest of Three Numbers

Input:

```text
10, 50, 30
```

| Condition | Result |
|---|---|
| `10 >= 50 and 10 >= 30` | False |
| `50 >= 10 and 50 >= 30` | True |
| Selected value | 50 |

## 34.4 Day Selection

Input:

```text
3
```

| Step | Condition | Result |
|---|---|---|
| 1 | Day == 1 | False |
| 2 | Day == 2 | False |
| 3 | Day == 3 | True |
| 4 | Selected day | Wednesday |

## 34.5 Temperature Classification

Input:

```text
28
```

| Condition | Result |
|---|---|
| `28 < 0` | False |
| `28 < 15` | False |
| `28 < 25` | False |
| `28 < 35` | True |
| Category | Warm |

---

# 35. Algorithms and Flowcharts

## 35.1 General If-Elif-Else Flowchart

```text
                 START
                   |
                   v
             Read Input
                   |
                   v
            Check Condition 1
               /       \
             Yes        No
              |          |
              v          v
          Branch 1    Condition 2
                       /      \
                     Yes       No
                      |         |
                      v         v
                  Branch 2   Condition 3
                              /     \
                            Yes      No
                             |        |
                             v        v
                         Branch 3   Else
                             \        /
                              \      /
                                END
```

## 35.2 Algorithm – Grade Calculator

1. Start.
2. Read marks.
3. Validate the marks range.
4. Check marks against the highest grade threshold.
5. If matched, assign grade A.
6. Otherwise, check the next threshold.
7. Continue for all grade categories.
8. If no condition matches, assign grade F.
9. Display the grade.
10. Stop.

## 35.3 Algorithm – Day of the Week

1. Start.
2. Read a day number.
3. Check whether it is 1.
4. If true, select Monday.
5. Otherwise, check whether it is 2.
6. Continue until day 7.
7. If no number matches, display Invalid.
8. Display the result.
9. Stop.

## 35.4 Algorithm – Basic Calculator

1. Start.
2. Read two numbers.
3. Read an operator.
4. Check the operator.
5. Perform the matching calculation.
6. If division is selected, check the denominator.
7. Handle invalid operators.
8. Display the result.
9. Stop.

---

# 36. Common Programming Mistakes

## Mistake 1 – Wrong Condition Order

Incorrect:

```python
if marks >= 40:
    print("Pass")

elif marks >= 90:
    print("A")
```

The second branch cannot be selected for a value of 90 or more because the first condition already matches.

Correct:

```python
if marks >= 90:
    print("A")

elif marks >= 40:
    print("Pass")
```

## Mistake 2 – Using Multiple If Statements Instead of Elif

When only one category should be selected, independent if statements may produce multiple outputs.

Use one `if-elif-else` chain.

## Mistake 3 – Missing Colon

Incorrect:

```python
elif marks >= 75
    print("B")
```

Correct:

```python
elif marks >= 75:
    print("B")
```

## Mistake 4 – Incorrect Indentation

Every branch must have a properly indented body.

## Mistake 5 – Using Else With a Condition

Incorrect:

```python
else marks < 40:
    print("Fail")
```

Correct:

```python
else:
    print("Fail")
```

Use `elif` when another condition is required.

## Mistake 6 – Overlapping Condition Ranges

Incorrect:

```python
if marks >= 90:
    print("A")

elif marks >= 60:
    print("B")

elif marks >= 75:
    print("C")
```

The third condition is unreachable for marks of 75 or more because the second condition catches those values.

Correct:

```python
if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")
```

## Mistake 7 – Forgetting Boundary Values

If exactly 75 belongs to grade B, use a condition that includes 75.

## Mistake 8 – Missing Default Branch

When invalid input must be handled, include an `else` branch or perform a separate validation.

## Mistake 9 – Input Type Error

Convert numeric input before comparing it with numbers.

## Mistake 10 – Uninitialized Variables

Initialize values before using them after a conditional chain.

## Mistake 11 – Division by Zero

Check the denominator before division.

## Mistake 12 – Unreachable Elif

Check that a later condition is not already covered by an earlier condition.

---

# 37. Debugging Techniques

## 37.1 Print the Input

```python
marks = 85

print("Marks:", marks)
```

## 37.2 Print Each Condition

```python
marks = 85

print(marks >= 90)
print(marks >= 75)
print(marks >= 60)
```

## 37.3 Use a Temporary Variable

```python
marks = 85

is_a = marks >= 90
is_b = marks >= 75

print("A condition:", is_a)
print("B threshold condition:", is_b)
```

## 37.4 Check Boundaries

For a threshold of 75, test:

- 74.
- 75.
- 76.

## 37.5 Check Branch Ordering

Make sure the first branch does not cover values intended for a later branch.

## 37.6 Use a Debugger

In VS Code:

1. Open the Python file.
2. Set a breakpoint on a condition.
3. Start debugging.
4. Inspect variables.
5. Step through the code.
6. Observe which branch executes.

---

# 38. Best Practices

1. Put specific conditions before broader conditions when necessary.
2. Arrange numeric ranges carefully.
3. Avoid overlapping or unreachable branches.
4. Include an else branch when unmatched values must be handled.
5. Validate user input.
6. Test boundary values.
7. Keep each branch readable.
8. Use meaningful variable names.
9. Avoid excessive nesting.
10. Use functions for reusable classification logic.
11. Use parentheses for complex logical expressions.
12. Avoid repeating expensive calculations.
13. Handle exceptional inputs.
14. Keep business rules separate from user-interface messages when appropriate.
15. Use `match-case` when it makes fixed-value matching clearer.
16. Consider dictionaries for simple fixed mappings.
17. Document example thresholds and policies.
18. Use suitable numeric types for monetary calculations.
19. Avoid exact floating-point equality when approximate comparison is needed.
20. Test every branch independently.

---

# 39. If-Elif-Else and Data Structures

Conditional statements are useful when working with lists, tuples, dictionaries, sets and other data structures.

## 39.1 Lists

```python
numbers = [10, 20, 30]

if not numbers:
    print("Empty list")

elif len(numbers) == 1:
    print("One element")

else:
    print("Multiple elements")
```

## 39.2 Stack

```python
stack = [10, 20, 30]

if not stack:
    print("Stack is empty")

elif len(stack) == 1:
    print("One item")

else:
    print("Multiple items")
```

## 39.3 Queue

```python
queue = []

if not queue:
    print("Queue is empty")

elif len(queue) < 5:
    print("Small queue")

else:
    print("Large queue")
```

## 39.4 Dictionary

```python
student = {
    "name": "Amaan",
    "marks": 85
}

if "marks" not in student:
    print("Marks unavailable")

elif student["marks"] >= 40:
    print("Pass")

else:
    print("Fail")
```

## 39.5 Sets

```python
numbers = {10, 20, 30}

if 10 in numbers:
    print("10 exists")

elif 20 in numbers:
    print("20 exists")

else:
    print("Neither value exists")
```

Remember that only the first matching branch executes.

---

# 40. If-Elif-Else and DSA

Conditional structures are important in Data Structures and Algorithms.

They are used in:

- Searching.
- Sorting.
- Traversal.
- Classification.
- Validation.
- Recursive decisions.
- Graph algorithms.
- Tree algorithms.
- Dynamic programming.
- Greedy algorithms.

## 40.1 Binary Search

Binary search uses comparisons to decide which half of a sorted sequence to search.

```python
if arr[mid] == target:
    print("Found")

elif arr[mid] < target:
    print("Search right half")

else:
    print("Search left half")
```

## 40.2 Sorting Decisions

```python
a = 10
b = 20

if a > b:
    a, b = b, a

print(a, b)
```

This condition helps place the smaller value first.

## 40.3 Finding a Category

```python
score = 85

if score >= 90:
    category = "Excellent"

elif score >= 75:
    category = "Good"

elif score >= 50:
    category = "Average"

else:
    category = "Needs improvement"
```

## 40.4 Graph Traversal

A graph algorithm may check whether a neighboring vertex has already been visited.

```python
if neighbor not in visited:
    print("Visit the neighbor")

else:
    print("Already visited")
```

## 40.5 Tree Search

A binary search tree uses comparisons to decide which child should be examined.

```python
if target == node.value:
    print("Found")

elif target < node.value:
    print("Search left")

else:
    print("Search right")
```

---

# 41. Time and Space Complexity

The complexity of an `if-elif-else` structure depends on the work performed in its conditions and branches.

## 41.1 Fixed Number of Conditions

```python
number = 10

if number < 0:
    print("Negative")

elif number == 0:
    print("Zero")

elif number < 100:
    print("Small")

else:
    print("Large")
```

When the number of conditions is fixed, the structure has constant time complexity for simple comparisons.

- Time: O(1)
- Auxiliary space: O(1)

## 41.2 Membership Conditions

```python
numbers = [10, 20, 30]

if 10 in numbers:
    print("Found")

elif 20 in numbers:
    print("Found")

else:
    print("Not found")
```

List membership is O(n) in the worst case.

The complexity depends on the search and the number of membership checks reached.

## 41.3 Repeated Expensive Conditions

Avoid repeatedly calculating the same expensive value.

Less efficient structure:

```python
if expensive_calculation() > 100:
    print("Large")

elif expensive_calculation() > 50:
    print("Medium")

else:
    print("Small")
```

Better:

```python
result = expensive_calculation()

if result > 100:
    print("Large")

elif result > 50:
    print("Medium")

else:
    print("Small")
```

The second structure calculates the value once.

## 41.4 Complexity Summary

| Operation | Complexity |
|---|---|
| Fixed integer comparison | O(1) |
| Fixed logical conditions | O(1), assuming constant-time operands |
| List membership | O(n) worst case |
| Set membership | Expected O(1) average |
| Dictionary key lookup | Expected O(1) average |
| Repeating a function call | Depends on the function |

---

# 42. Mini Project – Student Grade and Performance System

## Project Introduction

Create a student result system using `if-elif-else`.

The program accepts marks and selects a grade and performance description.

Example grading rules:

| Marks | Grade | Performance |
|---|---|---|
| 90–100 | A | Excellent |
| 75–89.99 | B | Very Good |
| 60–74.99 | C | Good |
| 40–59.99 | D | Pass |
| Below 40 | F | Needs Improvement |

## Project Requirements

1. Read student name.
2. Accept marks.
3. Validate the marks range.
4. Assign a grade.
5. Assign a performance description.
6. Display the result summary.

## Project Code

```python
print("=" * 55)
print("STUDENT GRADE AND PERFORMANCE SYSTEM")
print("=" * 55)

name = input("Enter student name: ").strip()

if not name:
    print("Student name cannot be empty.")

else:
    marks = float(input("Enter marks between 0 and 100: "))

    if not 0 <= marks <= 100:
        print("Invalid marks.")

    elif marks >= 90:
        grade = "A"
        performance = "Excellent"

    elif marks >= 75:
        grade = "B"
        performance = "Very Good"

    elif marks >= 60:
        grade = "C"
        performance = "Good"

    elif marks >= 40:
        grade = "D"
        performance = "Pass"

    else:
        grade = "F"
        performance = "Needs Improvement"

    if 0 <= marks <= 100:
        print("\n--------- RESULT SUMMARY ---------")
        print("Student:", name)
        print("Marks:", marks)
        print("Grade:", grade)
        print("Performance:", performance)
        print("----------------------------------")
```

## Sample Input

```text
Enter student name: Amaan
Enter marks between 0 and 100: 85
```

## Output

```text
--------- RESULT SUMMARY ---------
Student: Amaan
Marks: 85.0
Grade: B
Performance: Very Good
----------------------------------
```

## Project Explanation

1. Read the student's name.
2. Check whether the name is empty.
3. If the name is available, accept marks.
4. Validate the marks range.
5. Check the highest grade threshold.
6. Continue through the remaining conditions.
7. Select the corresponding grade.
8. Display the result.

## Project Challenges

1. Accept marks for five subjects.
2. Calculate the average.
3. Calculate the percentage.
4. Assign a grade based on the percentage.
5. Add a Pass or Fail result.
6. Validate every input.
7. Add a distinction category.
8. Store multiple student results.
9. Display class performance.
10. Create a reusable grade-calculation function.

---

# 43. Practice Test

Try solving these questions without looking at the answers.

## Question 1

What is the output?

```python
number = 10

if number < 0:
    print("Negative")

elif number > 0:
    print("Positive")

else:
    print("Zero")
```

## Question 2

What is the output?

```python
marks = 85

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("F")
```

## Question 3

What is the output?

```python
number = 15

if number > 0:
    print("Positive")

elif number > 10:
    print("Greater than 10")

else:
    print("Other")
```

## Question 4

What is the output?

```python
day = 7

if day == 1:
    print("Monday")

elif day == 7:
    print("Sunday")

else:
    print("Other day")
```

## Question 5

What is the output?

```python
temperature = 20

if temperature < 0:
    print("Freezing")

elif temperature < 15:
    print("Cold")

elif temperature < 25:
    print("Pleasant")

else:
    print("Hot")
```

## Question 6

What is the output?

```python
number = 0

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

## Question 7

What is the output?

```python
price = 3500

if price >= 5000:
    discount = 20

elif price >= 3000:
    discount = 15

elif price >= 1000:
    discount = 10

else:
    discount = 0

print(discount)
```

## Question 8

What is the output?

```python
signal = "blue"

if signal == "red":
    print("Stop")

elif signal == "green":
    print("Go")

else:
    print("Invalid")
```

## Question 9

What is the output?

```python
marks = 40

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

elif marks >= 40:
    print("D")

else:
    print("F")
```

## Question 10

What is the output?

```python
number = 30

if number % 5 == 0 and number % 3 == 0:
    print("Both")

elif number % 5 == 0:
    print("Five")

elif number % 3 == 0:
    print("Three")

else:
    print("Neither")
```

## Practice Test Answers

| Question | Answer |
|---|---|
| 1 | Positive |
| 2 | B |
| 3 | Positive |
| 4 | Sunday |
| 5 | Pleasant |
| 6 | Zero |
| 7 | 15 |
| 8 | Invalid |
| 9 | D |
| 10 | Both |

---

# 44. Viva and Interview Questions

## Basic Questions

**Q1. What is an if-elif-else statement?**

It is a Python conditional structure used to select one branch from multiple possible alternatives.

**Q2. What is the meaning of elif?**

`elif` means "else if".

**Q3. What is the syntax of if-elif-else?**

```python
if condition_1:
    statement_1

elif condition_2:
    statement_2

else:
    default_statement
```

**Q4. How many if branches can a single chain begin with?**

One initial `if` branch.

**Q5. Can we use multiple elif branches?**

Yes.

**Q6. Is else compulsory?**

No. The else branch is optional.

**Q7. Does elif require a condition?**

Yes.

**Q8. Does else contain a condition?**

No.

**Q9. Which branch executes when a condition matches?**

The first matching branch.

**Q10. What happens to remaining branches after a match?**

They are skipped.

## Intermediate Questions

**Q11. In which order are conditions checked?**

From top to bottom.

**Q12. Can multiple branches execute in one if-elif-else chain?**

No. Only one branch is selected.

**Q13. What happens when no condition matches and else is absent?**

No branch executes.

**Q14. What happens when no condition matches and else is present?**

The else block executes.

**Q15. What does first-match rule mean?**

Python executes the first branch whose condition is truthy.

**Q16. Why is condition ordering important?**

An earlier condition can match values intended for a later branch.

**Q17. What is an unreachable branch?**

A branch that can never be selected due to the conditions before it.

**Q18. What is the difference between if and elif?**

`if` starts the chain; `elif` adds an alternative condition.

**Q19. Can elif exist without an initial if?**

No.

**Q20. Can else exist without if?**

No.

## Programming Questions

**Q21. How do you classify positive, negative and zero?**

Use three branches to check greater than zero, less than zero and the remaining zero case.

**Q22. How do you create a grade calculator?**

Check grade thresholds in the correct order.

**Q23. How do you map numbers to weekdays?**

Compare a day number with 1 through 7.

**Q24. How do you validate a month number?**

Check whether the value lies between 1 and 12.

**Q25. How do you create a calculator using elif?**

Check the selected operator and execute the corresponding arithmetic expression.

**Q26. How do you classify a triangle?**

Validate positive side lengths and triangle inequalities before checking the side-equality categories.

**Q27. Can elif use logical operators?**

Yes.

**Q28. Can elif conditions use functions?**

Yes.

**Q29. Can if-elif-else work with strings?**

Yes.

**Q30. Can if-elif-else work with floating-point values?**

Yes.

## Advanced Questions

**Q31. What is the difference between multiple independent if statements and an if-elif chain?**

Independent if statements are evaluated separately, while an if-elif chain selects the first matching branch.

**Q32. What is the difference between elif and nested if?**

`elif` adds another branch to the same chain. Nested `if` places one conditional statement inside another block.

**Q33. Can a conditional chain have only if and elif branches?**

Yes.

**Q34. What is the purpose of an else block?**

It handles values that do not match any preceding condition.

**Q35. What is the role of indentation?**

It identifies which statements belong to each branch.

**Q36. What happens when the first condition is true?**

The first branch executes, and later branches are skipped.

**Q37. Can an elif condition be always true?**

Yes, for example `elif True:`. However, such a branch makes every later branch unreachable whenever execution reaches it.

**Q38. Can two conditions both be true in a chain?**

Yes. Python executes only the first matching branch.

**Q39. What is boundary testing?**

Testing values at the edges of ranges to detect comparison mistakes.

**Q40. When should match-case be considered?**

When matching a value against several fixed patterns makes the code clearer than an if-elif chain.

## Interview-Level Questions

**Q41. What is the output?**

```python
x = 10

if x > 5:
    print("A")

elif x > 8:
    print("B")

else:
    print("C")
```

Answer: `A`.

**Q42. Why does the second branch not execute?**

Because the first condition already matches.

**Q43. What is the output?**

```python
marks = 75

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

else:
    grade = "C"

print(grade)
```

Answer: `B`.

**Q44. What happens if conditions are written in the wrong order?**

A broader earlier condition may match before the intended specific condition.

**Q45. Can conditions contain arithmetic expressions?**

Yes.

**Q46. Can conditions contain logical expressions?**

Yes.

**Q47. Can conditions contain membership operations?**

Yes.

**Q48. What is the time complexity of a fixed number of simple conditions?**

O(1).

**Q49. Why are if-elif-else statements useful in DSA?**

They help algorithms choose actions based on comparisons and other conditions.

**Q50. What is the most important rule of if-elif-else?**

Python executes the first matching branch and skips the remaining branches in that chain.

---

# 45. Important Glossary

| Term | Meaning |
|---|---|
| Conditional Statement | Controls execution based on a condition |
| If | Starts a conditional chain |
| Elif | Adds another conditional branch |
| Else | Provides the default branch |
| Condition | Expression evaluated by Python |
| Boolean | Data type with True and False |
| Truthy | Value that evaluates to true in a Boolean context |
| Falsy | Value that evaluates to false in a Boolean context |
| Branch | One possible execution path |
| First-Match Rule | First truthy branch is selected |
| Nested If | An if statement inside another conditional block |
| Independent If | A separate conditional statement |
| Boundary Value | Value at the edge of a range |
| Unreachable Branch | Branch that cannot be selected |
| Comparison Operator | Operator that compares values |
| Logical Operator | Operator that combines or reverses conditions |
| Membership Operator | Checks whether an element belongs to a collection |
| Identity Operator | Checks object identity |
| Range Checking | Testing whether a value belongs to a specified interval |
| Validation | Checking whether input satisfies requirements |
| Dry Run | Manually tracing program execution |
| Flowchart | Visual representation of program logic |
| Algorithm | Ordered steps to solve a problem |
| Debugging | Finding and fixing errors |
| Time Complexity | Growth of running time |
| Auxiliary Space | Additional memory used by an algorithm |

---

# 46. Quick Revision Notes

1. `if-elif-else` supports multiple possible outcomes.
2. The first branch begins with `if`.
3. Additional conditions use `elif`.
4. The default branch uses `else`.
5. The else branch is optional.
6. Python checks conditions from top to bottom.
7. The first matching branch executes.
8. Remaining branches are skipped after a match.
9. Condition ordering is important.
10. Broad earlier conditions can hide specific later conditions.
11. Independent if statements are different from elif.
12. Every branch needs correct indentation.
13. Each branch header requires a colon.
14. Logical operators can combine conditions.
15. Comparison operators can define ranges.
16. Membership operators can classify collection values.
17. Boundary values should be tested.
18. Invalid input should be handled.
19. Use functions for reusable classification logic.
20. Use match-case for suitable fixed-pattern matching.
21. Use dictionaries for simple fixed mappings when appropriate.
22. Avoid unnecessarily complicated conditional chains.

### Essential Syntax

```python
if condition_1:
    statement_1

elif condition_2:
    statement_2

else:
    default_statement
```

### Grade Example

```python
if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "F"
```

### Number Classification

```python
if number > 0:
    result = "Positive"

elif number < 0:
    result = "Negative"

else:
    result = "Zero"
```

### Day Selection

```python
if day == 1:
    name = "Monday"

elif day == 2:
    name = "Tuesday"

else:
    name = "Other"
```

---

# 47. Learning Checklist

Complete this checklist after studying the topic.

- [ ] Understand conditional statements.
- [ ] Understand decision-making.
- [ ] Define if-elif-else.
- [ ] Learn the syntax.
- [ ] Understand if.
- [ ] Understand elif.
- [ ] Understand else.
- [ ] Understand first-match selection.
- [ ] Understand top-to-bottom evaluation.
- [ ] Differentiate if from if-else.
- [ ] Differentiate if-else from if-elif-else.
- [ ] Differentiate independent if from elif.
- [ ] Understand Boolean values.
- [ ] Understand truthy and falsy values.
- [ ] Use comparison operators.
- [ ] Use arithmetic operators in conditions.
- [ ] Use logical operators.
- [ ] Use membership operators.
- [ ] Use identity operators.
- [ ] Understand condition ordering.
- [ ] Identify unreachable branches.
- [ ] Understand boundary values.
- [ ] Write multiple elif branches.
- [ ] Use if-elif-else with integers.
- [ ] Use if-elif-else with floats.
- [ ] Use if-elif-else with strings.
- [ ] Use if-elif-else with lists.
- [ ] Use nested conditions.
- [ ] Use input validation.
- [ ] Build a grade calculator.
- [ ] Build a calculator.
- [ ] Build a day-selection program.
- [ ] Build a month-selection program.
- [ ] Build a triangle classifier.
- [ ] Build an electricity bill calculator.
- [ ] Debug incorrect branch selection.
- [ ] Test boundary conditions.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the mini project.
- [ ] Revise all 50 viva questions.

---

# 48. How to Run the Python Program

The Python file for this topic is:

```text
01_if_elif_else.py
```

## Step 1 – Open the Folder

Navigate to:

```text
06-Conditional-Statements/
    03-If-Elif-Else/
```

## Step 2 – Open the Terminal

Open PowerShell or the integrated terminal in VS Code.

## Step 3 – Run the Program

```powershell
python 01_if_elif_else.py
```

Alternatively:

```powershell
py 01_if_elif_else.py
```

## Step 4 – Main Menu

The program displays:

```text
======================================================================
                   PYTHON - IF-ELIF-ELSE STATEMENT
======================================================================

1. View 12 Topic Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit

Enter your choice:
```

## Step 5 – Menu Options

| Option | Action |
|---|---|
| 1 | Displays all 12 topic examples |
| 2 | Opens the 12 solved problems |
| 3 | Displays 10 unsolved questions |
| 4 | Displays the learning checklist |
| 0 | Exits the program |

---

# 49. Repository Folder Structure

The current topic folder should contain:

```text
03-If-Elif-Else/
│
├── 01_if_elif_else.py
│
└── README.md
```

The complete section structure is:

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

# 50. Previous and Next Topics

## Previous Topic

**02 – If-Else**

Folder:

```text
02-If-Else/
```

Concepts covered:

- Two alternative branches.
- True and false execution.
- If and else syntax.
- Comparison operators.
- Logical operators.
- Practical decision-making.

## Current Topic

**03 – If-Elif-Else**

Folder:

```text
03-If-Elif-Else/
```

Concepts covered:

- Multiple conditions.
- Multiple alternative branches.
- First-matching-condition rule.
- Condition ordering.
- Range checking.
- Grade calculation.
- Classification programs.
- Real-world multiple-outcome decisions.

## Next Topic

**04 – Nested If**

Folder:

```text
04-Nested-If/
```

The next topic will explain how one conditional statement can be placed inside another conditional block.

---

# 51. Final Summary

The Python `if-elif-else` statement is an important control-flow structure because it allows programs to choose between several possible outcomes.

In this topic, you studied:

- Conditional statements.
- Decision-making.
- If-elif-else syntax.
- Components of conditional chains.
- The role of if, elif and else.
- Sequential condition evaluation.
- The first-matching-condition rule.
- Differences between if, if-else and if-elif-else.
- Differences between independent if and elif.
- Boolean values.
- Truthy and falsy values.
- Comparison operators.
- Arithmetic operators.
- Logical operators.
- Membership operators.
- Identity operators.
- Condition ordering.
- Boundary values.
- Multiple elif branches.
- Nested conditions.
- User input and validation.
- Integer and floating-point conditions.
- String and character classification.
- Collection-based conditions.
- Function-based conditions.
- Mathematical calculations.
- Real-world applications.
- Dry runs and trace tables.
- Algorithms and flowcharts.
- Common programming mistakes.
- Debugging techniques.
- Best practices.
- Data structures and algorithms.
- Time and space complexity.

## Final Advice

Do not memorize only the syntax.

Understand how Python checks each condition and why the first matching branch is selected.

Practice with grade calculators, number classification, day selection, month selection, discount calculations and other real-world examples.

Pay particular attention to condition ordering and boundary values.

These concepts are important because incorrect condition ordering can produce incorrect results even when every individual condition is written correctly.

**Build a strong understanding of `if-elif-else` before moving to nested conditions and more advanced decision-making.**

---

**END OF README – TOPIC 03: IF-ELIF-ELSE STATEMENT**