

# Python Match Case – Complete Learning Guide

## 1. Introduction

Python provides conditional statements that allow a program to make decisions based on different conditions.

The `match-case` statement is another decision-making structure introduced in Python 3.10.

It is used for structural pattern matching. A value or data structure is compared against different patterns, and the first matching case is selected.

It is particularly useful when a program needs to handle:

- Multiple menu options.
- Different commands.
- Integer values.
- String values.
- Multiple alternative patterns.
- Grade categories.
- Calculator operations.
- Tuple patterns.
- List patterns.
- Type patterns.
- Conditional guard expressions.

Before Python 3.10, programmers commonly used `if-elif-else` statements for multi-option decisions.

Python 3.10 introduced `match-case`, providing another readable way to implement these decisions.

### Basic Example

```python
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")
```

**Output:**

```text
Two
```

### Explanation

The `match` statement evaluates the subject `number`.

Python checks the patterns one by one.

When the value matches `case 2`, that case executes.

The `_` pattern acts as a wildcard and matches any value that has not matched an earlier case.

### Python Version Requirement

`match-case` requires Python 3.10 or newer.

Check your installed Python version:

```bash
python --version
```

On Windows:

```powershell
py --version
```

### Learning Objectives

After completing this topic, you should be able to:

- Understand the purpose of `match-case`.
- Understand structural pattern matching.
- Understand the difference between `match-case` and `if-elif-else`.
- Write basic `match-case` statements.
- Match integer values.
- Match string values.
- Use multiple patterns with `|`.
- Understand the wildcard pattern `_`.
- Understand literal patterns.
- Use guard conditions.
- Implement menu-driven programs.
- Create arithmetic calculators using `match-case`.
- Match weekday and month numbers.
- Classify grade percentages.
- Classify status codes.
- Understand tuple patterns.
- Understand list patterns.
- Understand simple type patterns.
- Use functions with `match-case`.
- Handle invalid inputs.
- Understand pattern order.
- Build reusable command handlers.
- Analyze time and space complexity.
- Apply pattern matching to practical programming problems.

---

## 2. What Is Match Case?

The `match-case` statement is a Python control-flow statement that performs structural pattern matching.

It compares a subject against a sequence of patterns.

The first matching case is selected.

### Basic Syntax

```python
match subject:
    case pattern1:
        statement1

    case pattern2:
        statement2

    case pattern3:
        statement3

    case _:
        default_statement
```

### Main Components

| Component | Purpose |
|---|---|
| `match` | Starts a pattern-matching statement |
| Subject | Value or object being examined |
| `case` | Defines a pattern to match |
| Pattern | Describes the value or structure to match |
| Guard | Adds an additional condition to a pattern |
| `_` | Wildcard pattern that matches anything |
| Case block | Statements executed when the case matches |

### Example

```python
command = "start"

match command:
    case "start":
        print("Program started")

    case "stop":
        print("Program stopped")

    case _:
        print("Unknown command")
```

**Output:**

```text
Program started
```

### Explanation

The variable `command` contains the string `"start"`.

Python checks each case:

1. Does it match `"start"`? Yes.
2. The first case executes.
3. The remaining cases are not executed.

### Important Point

Unlike a traditional switch statement in some other programming languages, Python's `match-case` does not automatically fall through to the next case.

Only the selected case block executes.

---

## 3. Why Use Match Case?

Consider a program that displays a message according to a menu choice.

Using `if-elif-else`:

```python
choice = 2

if choice == 1:
    print("Home")
elif choice == 2:
    print("Profile")
elif choice == 3:
    print("Settings")
elif choice == 4:
    print("Help")
else:
    print("Invalid choice")
```

The same logic can be written using `match-case`.

```python
choice = 2

match choice:
    case 1:
        print("Home")

    case 2:
        print("Profile")

    case 3:
        print("Settings")

    case 4:
        print("Help")

    case _:
        print("Invalid choice")
```

**Output:**

```text
Profile
```

Both approaches work.

However, `match-case` provides a pattern-oriented structure that can be particularly helpful when working with more complex values and data structures.

### Advantages of Match Case

1. Makes multiple alternatives easier to organize.
2. Provides a readable structure for menu-based programs.
3. Supports literal patterns.
4. Supports multiple alternative patterns.
5. Supports wildcard matching.
6. Supports guard conditions.
7. Supports tuple and list patterns.
8. Supports mapping and class patterns.
9. Supports structural pattern matching.
10. Helps organize command-processing logic.

### When to Use Match Case

It is useful when:

- A value must be compared against several possible patterns.
- A program has multiple menu choices.
- A command handler processes different commands.
- Different data structures must be identified.
- Several values must be grouped into patterns.
- A program must identify the structure of a sequence.

### When If-Elif-Else May Be Better

Use `if-elif-else` when:

- Conditions are simple comparisons.
- The logic depends on complicated Boolean expressions.
- Conditions involve calculations that are easier to express directly.
- Pattern matching would make a simple problem unnecessarily complicated.

Both structures are useful.

Choose the one that makes the program easiest to understand.

---

## 4. Understanding Literal Patterns

A literal pattern matches a specific value.

Common literal patterns include:

- Integers.
- Strings.
- Floating-point values.
- Boolean values.
- `None`.

### Integer Literal Pattern

```python
number = 10

match number:
    case 5:
        print("Five")

    case 10:
        print("Ten")

    case 15:
        print("Fifteen")

    case _:
        print("Other")
```

**Output:**

```text
Ten
```

### String Literal Pattern

```python
command = "login"

match command:
    case "login":
        print("Login selected")

    case "logout":
        print("Logout selected")

    case "register":
        print("Register selected")

    case _:
        print("Unknown command")
```

**Output:**

```text
Login selected
```

### Boolean Pattern

```python
status = True

match status:
    case True:
        print("Active")

    case False:
        print("Inactive")

    case _:
        print("Unknown status")
```

**Output:**

```text
Active
```

### None Pattern

```python
value = None

match value:
    case None:
        print("No value available")

    case _:
        print("Value exists")
```

**Output:**

```text
No value available
```

### Important Point

Literal patterns are suitable for exact-value matching.

They are useful for menu selections, commands, status values, and fixed categories.

---

## 5. Understanding Multiple Patterns

Sometimes different values should execute the same block.

The `|` operator allows multiple alternative patterns in one case.

### Syntax

```python
match value:
    case pattern1 | pattern2 | pattern3:
        statement
```

### Example

```python
number = 2

match number:
    case 1 | 2 | 3:
        print("Number belongs to group one")

    case 4 | 5 | 6:
        print("Number belongs to group two")

    case _:
        print("Other number")
```

**Output:**

```text
Number belongs to group one
```

### Explanation

The first case matches numbers 1, 2, or 3.

Since the value is 2, that case executes.

### Example: Vowels

```python
letter = "a"

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")

    case _:
        print("Not a vowel")
```

**Output:**

```text
Vowel
```

### Example: Weekdays and Weekends

```python
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")

    case 6 | 7:
        print("Weekend")

    case _:
        print("Invalid day")
```

**Output:**

```text
Weekend
```

### Important Rule

When using OR patterns, every alternative must bind the same set of variable names.

For example, patterns that capture different names in their alternatives are not valid.

For beginner-level problems, matching literal alternatives is a straightforward use of `|`.

---

## 6. Understanding the Wildcard Pattern

The underscore `_` is called a wildcard pattern.

It matches any value that has not matched an earlier case.

It is commonly used as the default case.

### Syntax

```python
match value:
    case pattern1:
        statement1

    case _:
        default_statement
```

### Example

```python
choice = 10

match choice:
    case 1:
        print("Home")

    case 2:
        print("Profile")

    case 3:
        print("Settings")

    case _:
        print("Invalid choice")
```

**Output:**

```text
Invalid choice
```

### Explanation

The value 10 does not match any of the first three patterns.

Therefore, the wildcard pattern executes.

### Important Points

- `_` matches any value.
- It is commonly used as a default.
- It should normally be placed last.
- It does not create or store a variable.
- It can be used when the exact value is not important.

### Incorrect Ordering

```python
match choice:
    case _:
        print("Default")

    case 1:
        print("One")
```

This is invalid because the unconditional wildcard pattern already matches every possible subject. The later case cannot be reached.

### Correct Ordering

```python
match choice:
    case 1:
        print("One")

    case _:
        print("Default")
```

---

## 7. Understanding Guard Conditions

A guard is an additional Boolean condition written after a pattern.

The guard begins with the `if` keyword.

A pattern must match first, and then its guard must evaluate to true for the case to be selected.

### Syntax

```python
match value:
    case pattern if condition:
        statement

    case _:
        default_statement
```

### Example

```python
marks = 85

match marks:
    case value if value >= 90:
        print("Grade A+")

    case value if value >= 80:
        print("Grade A")

    case value if value >= 70:
        print("Grade B")

    case _:
        print("Other grade")
```

**Output:**

```text
Grade A
```

### Explanation

The pattern:

```python
case value if value >= 90:
```

captures the subject into the name `value`.

The guard then checks whether the captured value is at least 90.

The same process occurs for the next case.

### Guard Conditions for Grade Calculation

```python
def get_grade(percentage):

    match percentage:

        case value if 90 <= value <= 100:
            return "A+"

        case value if 80 <= value < 90:
            return "A"

        case value if 70 <= value < 80:
            return "B"

        case value if 60 <= value < 70:
            return "C"

        case value if 50 <= value < 60:
            return "D"

        case value if 40 <= value < 50:
            return "E"

        case value if 0 <= value < 40:
            return "F"

        case _:
            return "Invalid percentage"
```

### Important Points

- A guard is written after a pattern.
- The guard uses an ordinary Boolean expression.
- The pattern must match before the guard is evaluated.
- Guard conditions are useful for numerical ranges.
- The order of guarded cases matters.

---

## 8. Match Case for Day Names

A day number can be mapped to a weekday name.

### Number Mapping

| Number | Day |
|---:|---|
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |
| 7 | Sunday |

### Example

```python
day_number = 3

match day_number:
    case 1:
        day = "Monday"

    case 2:
        day = "Tuesday"

    case 3:
        day = "Wednesday"

    case 4:
        day = "Thursday"

    case 5:
        day = "Friday"

    case 6:
        day = "Saturday"

    case 7:
        day = "Sunday"

    case _:
        day = "Invalid day number"

print(day)
```

**Output:**

```text
Wednesday
```

### Explanation

The program matches the number 3.

The matching case returns Wednesday.

### Reusable Function

```python
def get_day_name(day_number):

    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"
```

### Important Point

Validate that the input is a number between 1 and 7 when the program requires a valid weekday.

---

## 9. Match Case for Month Names

A month number can be converted into the corresponding month name.

### Number Mapping

| Number | Month |
|---:|---|
| 1 | January |
| 2 | February |
| 3 | March |
| 4 | April |
| 5 | May |
| 6 | June |
| 7 | July |
| 8 | August |
| 9 | September |
| 10 | October |
| 11 | November |
| 12 | December |

### Example

```python
month_number = 4

match month_number:
    case 1:
        print("January")

    case 2:
        print("February")

    case 3:
        print("March")

    case 4:
        print("April")

    case 5:
        print("May")

    case 6:
        print("June")

    case 7:
        print("July")

    case 8:
        print("August")

    case 9:
        print("September")

    case 10:
        print("October")

    case 11:
        print("November")

    case 12:
        print("December")

    case _:
        print("Invalid month")
```

**Output:**

```text
April
```

### Learning Point

This is a common use of `match-case`: converting one fixed value into a corresponding label.

---

## 10. Match Case for Arithmetic Operations

A calculator can use `match-case` to select an arithmetic operation.

### Arithmetic Operators

| Operator | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Remainder |

### Example

```python
number1 = 20
number2 = 5
operator = "+"

match operator:

    case "+":
        result = number1 + number2

    case "-":
        result = number1 - number2

    case "*":
        result = number1 * number2

    case "/":
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            result = number1 / number2

    case "%":
        if number2 == 0:
            print("Cannot calculate remainder with zero")
        else:
            result = number1 % number2

    case _:
        print("Invalid operator")

if operator in {"+", "-", "*"} or (
    operator in {"/", "%"} and number2 != 0
):
    print("Result:", result)
```

**Output:**

```text
Result: 25
```

### Explanation

The `match` statement examines the operator.

When the operator is `+`, addition is performed.

When the operator is `-`, subtraction is performed.

The division and remainder cases also check for zero before calculation.

### Important Point

A calculator needs input validation.

Division by zero should be handled explicitly.

---

## 11. Tuple Patterns

A tuple pattern matches the structure and values of a sequence.

Tuple patterns are useful when multiple related values must be checked together.

### Example

```python
point = (0, 0)

match point:

    case (0, 0):
        print("Origin")

    case (0, y):
        print("Y-axis:", y)

    case (x, 0):
        print("X-axis:", x)

    case (x, y):
        print("Other point:", x, y)
```

**Output:**

```text
Origin
```

### Explanation

The tuple contains two values:

```python
(0, 0)
```

The first pattern matches both coordinates being zero.

Therefore, the program prints Origin.

### Example: Different Coordinates

```python
point = (0, 5)

match point:

    case (0, 0):
        print("Origin")

    case (0, y):
        print("Y-axis:", y)

    case (x, 0):
        print("X-axis:", x)

    case (x, y):
        print("Other point:", x, y)
```

**Output:**

```text
Y-axis: 5
```

### Coordinate Classification

A point can be classified using its X and Y coordinates.

| Condition | Position |
|---|---|
| X = 0 and Y = 0 | Origin |
| X = 0 and Y is not 0 | Y-axis |
| Y = 0 and X is not 0 | X-axis |
| X greater than 0 and Y greater than 0 | First quadrant |
| X less than 0 and Y greater than 0 | Second quadrant |
| X less than 0 and Y less than 0 | Third quadrant |
| X greater than 0 and Y less than 0 | Fourth quadrant |

### Important Point

More specific tuple patterns should appear before general capture patterns.

---

## 12. List Patterns

List patterns are useful when the program needs to identify the number or arrangement of elements in a sequence.

### Empty List

```python
values = []

match values:

    case []:
        print("Empty list")

    case _:
        print("List contains values")
```

**Output:**

```text
Empty list
```

### Single Element

```python
values = [10]

match values:

    case []:
        print("Empty list")

    case [only]:
        print("One element:", only)

    case _:
        print("Multiple elements")
```

**Output:**

```text
One element: 10
```

### Two Elements

```python
values = [10, 20]

match values:

    case []:
        print("Empty list")

    case [only]:
        print("One element")

    case [first, second]:
        print("Two elements:", first, second)

    case _:
        print("Multiple elements")
```

**Output:**

```text
Two elements: 10 20
```

### Multiple Elements

```python
values = [10, 20, 30, 40]

match values:

    case []:
        print("Empty list")

    case [only]:
        print("One element")

    case [first, second]:
        print("Two elements")

    case [first, second, *remaining]:
        print("Multiple elements")
        print("First:", first)
        print("Second:", second)
        print("Remaining:", remaining)
```

**Output:**

```text
Multiple elements
First: 10
Second: 20
Remaining: [30, 40]
```

### Understanding the Star Pattern

In:

```python
case [first, second, *remaining]:
```

- The first value is captured by `first`.
- The second value is captured by `second`.
- All remaining values are captured by `remaining`.

The star pattern can collect zero or more remaining elements.

### Important Point

Place more specific sequence patterns before more general patterns.

---

## 13. Type Patterns

A class pattern can check whether the subject matches a particular class or type.

The following syntax uses built-in types:

```python
match value:

    case int():
        print("Integer")

    case float():
        print("Float")

    case str():
        print("String")

    case list():
        print("List")

    case None:
        print("No value")

    case _:
        print("Other type")
```

### Example

```python
value = "Python"

match value:

    case int():
        print("Integer value")

    case float():
        print("Float value")

    case str():
        print("String value")

    case list():
        print("List value")

    case None:
        print("No value")

    case _:
        print("Other data type")
```

**Output:**

```text
String value
```

### Explanation

The subject is a string.

The `str()` class pattern matches it.

Therefore, the string case executes.

### Important Point About Boolean and Integer Types

In Python, `bool` is a subclass of `int`.

Therefore, a Boolean value can also match an `int()` class pattern.

When a program must distinguish Booleans from integers, place the Boolean case before the integer case.

Example:

```python
value = True

match value:

    case bool():
        print("Boolean")

    case int():
        print("Integer")

    case _:
        print("Other type")
```

Output:

```text
Boolean
```

---

## 14. Pattern Order and Matching Behaviour

Python checks cases in the order in which they are written.

The first matching case whose guard is true is selected.

### Example

```python
number = 5

match number:

    case 1:
        print("One")

    case 5:
        print("Five")

    case 10:
        print("Ten")

    case _:
        print("Other")
```

**Output:**

```text
Five
```

### Specific Pattern Before General Pattern

Consider:

```python
values = [10, 20]

match values:

    case []:
        print("Empty")

    case [first, second]:
        print("Two elements")

    case [first, second, *remaining]:
        print("Two or more elements")
```

The two-element pattern is selected for `[10, 20]`.

### Important Rules

1. Patterns are checked from top to bottom.
2. The first successful case is selected.
3. A guard must also be true for its case to execute.
4. `_` matches anything.
5. Unconditional wildcard cases should be placed last.
6. More specific patterns should generally appear before general patterns.
7. A capture pattern such as `case value:` matches anything and binds the subject to the name.
8. Match-case does not automatically execute later case blocks.

---

## 15. Capture Patterns and Constant Values

One important detail in structural pattern matching is that a bare name is generally interpreted as a capture pattern.

### Capture Pattern

```python
value = 10

match value:

    case number:
        print("Captured:", number)
```

**Output:**

```text
Captured: 10
```

The name `number` captures the subject value.

It does not check whether the subject is equal to a previously defined variable called `number`.

### Why This Matters

Consider:

```python
TARGET = 10
value = 5

match value:
    case TARGET:
        print("Matched")
```

This is not an equality check against the variable `TARGET`.

A bare name in a pattern captures the subject.

To match a constant stored in an attribute, use a qualified name, such as:

```python
import math

value = math.pi

match value:
    case math.pi:
        print("Matched pi")
    case _:
        print("Other value")
```

### Important Point

Use literal patterns for fixed values and guard conditions for comparisons against variables or ranges.

---

## 16. Match Case With Functions

A function can contain a `match-case` statement and return the result.

### Example: Day Name

```python
def get_day_name(day_number):

    match day_number:

        case 1:
            return "Monday"

        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"

        case 4:
            return "Thursday"

        case 5:
            return "Friday"

        case 6:
            return "Saturday"

        case 7:
            return "Sunday"

        case _:
            return "Invalid day number"


print(get_day_name(3))
```

**Output:**

```text
Wednesday
```

### Advantages

- Reusable logic.
- Clear separation of responsibilities.
- Easier testing.
- Less repeated code.
- Better organization.

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Basic Match Case

### Objective

Write a program that matches an integer against several literal patterns.

### Code

```python
number = 2

match number:

    case 1:
        print("One")

    case 2:
        print("Two")

    case 3:
        print("Three")

    case _:
        print("Other number")
```

### Output

```text
Two
```

### Explanation

The number is 2.

The second case matches the subject.

### Concepts Used

- `match`.
- `case`.
- Integer patterns.
- Wildcard.

---

## Example 2: Multiple Patterns

### Objective

Use multiple alternative patterns in a single case.

### Code

```python
number = 3

match number:

    case 1 | 2 | 3:
        print("Number is between 1 and 3")

    case 4 | 5 | 6:
        print("Number is between 4 and 6")

    case _:
        print("Number is outside the selected groups")
```

### Output

```text
Number is between 1 and 3
```

### Explanation

The value 3 matches one of the alternatives in the first case.

### Concepts Used

- OR patterns.
- Multiple literals.
- Wildcard.

---

## Example 3: Wildcard Pattern

### Objective

Use `_` as the default matching case.

### Code

```python
command = "start"

match command:

    case "start":
        print("Program started")

    case "stop":
        print("Program stopped")

    case _:
        print("Unknown command")
```

### Output

```text
Program started
```

### Explanation

The subject matches the first case.

The wildcard is only used when earlier patterns do not match.

### Concepts Used

- String patterns.
- Wildcard.
- Default handling.

---

## Example 4: Day Name

### Objective

Display the weekday name according to a number.

### Code

```python
day_number = 3

match day_number:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Invalid day")
```

### Output

```text
Wednesday
```

### Explanation

The number 3 corresponds to Wednesday.

### Concepts Used

- Integer patterns.
- Multiple cases.
- Wildcard.

---

## Example 5: Menu Choices

### Objective

Display different messages according to a menu choice.

### Code

```python
choice = 2

match choice:

    case 1:
        print("Home")

    case 2:
        print("Profile")

    case 3:
        print("Settings")

    case 4:
        print("Help")

    case _:
        print("Invalid menu choice")
```

### Output

```text
Profile
```

### Explanation

The value 2 matches the Profile option.

### Concepts Used

- Menu handling.
- Integer matching.
- Default case.

---

## Example 6: String Commands

### Objective

Process different commands using string patterns.

### Code

```python
command = "login"

match command:

    case "login":
        print("Login selected")

    case "logout":
        print("Logout selected")

    case "register":
        print("Registration selected")

    case _:
        print("Unknown command")
```

### Output

```text
Login selected
```

### Explanation

The subject is compared with three string literals.

The matching case executes.

### Concepts Used

- String matching.
- Literal patterns.
- Wildcard.

---

## Example 7: Grade Using Guards

### Objective

Calculate a grade using guarded patterns.

### Code

```python
percentage = 85

match percentage:

    case value if 90 <= value <= 100:
        print("Grade A+")

    case value if 80 <= value < 90:
        print("Grade A")

    case value if 70 <= value < 80:
        print("Grade B")

    case value if 60 <= value < 70:
        print("Grade C")

    case value if 50 <= value < 60:
        print("Grade D")

    case value if 40 <= value < 50:
        print("Grade E")

    case value if 0 <= value < 40:
        print("Grade F")

    case _:
        print("Invalid percentage")
```

### Output

```text
Grade A
```

### Explanation

The value 85 does not match the first range.

It matches the second range.

Therefore, the grade is A.

### Concepts Used

- Guard conditions.
- Capture patterns.
- Range comparison.
- Grade classification.

---

## Example 8: Simple Calculator

### Objective

Perform arithmetic operations using `match-case`.

### Code

```python
number1 = 20
number2 = 5
operator = "+"

match operator:

    case "+":
        result = number1 + number2

    case "-":
        result = number1 - number2

    case "*":
        result = number1 * number2

    case "/":
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            result = number1 / number2

    case _:
        print("Invalid operator")

if operator in {"+", "-", "*"} or (
    operator == "/" and number2 != 0
):
    print("Result:", result)
```

### Output

```text
Result: 25
```

### Explanation

The operator is `+`.

Therefore, the program performs addition.

### Concepts Used

- String patterns.
- Arithmetic operators.
- Conditional validation.
- Match-case.

---

## Example 9: Tuple Pattern

### Objective

Classify a two-dimensional coordinate using tuple patterns.

### Code

```python
point = (0, 0)

match point:

    case (0, 0):
        print("Origin")

    case (0, y):
        print("Y-axis:", y)

    case (x, 0):
        print("X-axis:", x)

    case (x, y):
        print("Other point:", x, y)
```

### Output

```text
Origin
```

### Explanation

The point contains two zero coordinates.

Therefore, it matches the origin pattern.

### Concepts Used

- Tuple patterns.
- Sequence matching.
- Capture patterns.

---

## Example 10: List Pattern

### Objective

Identify the structure of a list using pattern matching.

### Code

```python
values = [10, 20]

match values:

    case []:
        print("Empty list")

    case [only]:
        print("One element:", only)

    case [first, second]:
        print("Two elements:", first, second)

    case [first, second, *remaining]:
        print("Multiple elements:", first, second, remaining)
```

### Output

```text
Two elements: 10 20
```

### Explanation

The list contains exactly two elements.

The two-element pattern matches.

### Concepts Used

- List patterns.
- Sequence matching.
- Wildcard sequence capture.

---

## Example 11: Status Code Classification

### Objective

Classify an illustrative numeric status code using guard conditions.

### Code

```python
status_code = 200

match status_code:

    case value if 100 <= value < 200:
        print("Informational")

    case value if 200 <= value < 300:
        print("Success")

    case value if 300 <= value < 400:
        print("Redirection")

    case value if 400 <= value < 500:
        print("Client Error")

    case value if 500 <= value < 600:
        print("Server Error")

    case _:
        print("Unknown Status Code")
```

### Output

```text
Success
```

### Explanation

200 belongs to the range from 200 to below 300.

Therefore, the result is Success.

### Concepts Used

- Guard conditions.
- Numeric ranges.
- Conditional classification.

---

## Example 12: Type Patterns

### Objective

Identify a value according to its data type using class patterns.

### Code

```python
value = "Python"

match value:

    case int():
        print("Integer value")

    case float():
        print("Float value")

    case str():
        print("String value")

    case list():
        print("List value")

    case None:
        print("No value")

    case _:
        print("Other data type")
```

### Output

```text
String value
```

### Explanation

The value is a string.

Therefore, the `str()` class pattern matches.

### Concepts Used

- Class patterns.
- Type identification.
- Wildcard.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Day Name

### Problem Statement

Accept a number between 1 and 7 and display the corresponding weekday name using `match-case`.

### Logic

1. Accept a day number.
2. Validate that it is from 1 to 7.
3. Match the number.
4. Display its day name.

### Code

```python
day = int(input("Enter day number (1-7): "))

match day:

    case 1:
        name = "Monday"

    case 2:
        name = "Tuesday"

    case 3:
        name = "Wednesday"

    case 4:
        name = "Thursday"

    case 5:
        name = "Friday"

    case 6:
        name = "Saturday"

    case 7:
        name = "Sunday"

    case _:
        name = "Invalid day number"

print("Day:", name)
```

### Sample Input

```text
Enter day number (1-7): 3
```

### Expected Output

```text
Day: Wednesday
```

### Explanation

The value 3 matches the Wednesday case.

### Concepts Used

- Integer patterns.
- Match-case.
- Case mapping.

---

## Problem 2: Month Name

### Problem Statement

Accept a month number from 1 to 12 and display the corresponding month name.

### Logic

1. Accept a month number.
2. Match the number.
3. Display the month.
4. Handle an invalid number.

### Code

```python
month = int(input("Enter month number (1-12): "))

match month:

    case 1:
        name = "January"

    case 2:
        name = "February"

    case 3:
        name = "March"

    case 4:
        name = "April"

    case 5:
        name = "May"

    case 6:
        name = "June"

    case 7:
        name = "July"

    case 8:
        name = "August"

    case 9:
        name = "September"

    case 10:
        name = "October"

    case 11:
        name = "November"

    case 12:
        name = "December"

    case _:
        name = "Invalid month number"

print("Month:", name)
```

### Sample Input

```text
Enter month number (1-12): 4
```

### Expected Output

```text
Month: April
```

### Explanation

The number 4 matches the April case.

### Concepts Used

- Integer patterns.
- Literal matching.
- Wildcard.

---

## Problem 3: Simple Calculator

### Problem Statement

Create a calculator using `match-case`.

The program must support:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Remainder.

### Logic

1. Accept the first number.
2. Accept an operator.
3. Accept the second number.
4. Match the operator.
5. Perform the appropriate calculation.
6. Handle division by zero.
7. Display the result.

### Code

```python
number1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
number2 = float(input("Enter second number: "))

match operator:

    case "+":
        result = number1 + number2

    case "-":
        result = number1 - number2

    case "*":
        result = number1 * number2

    case "/":
        if number2 == 0:
            result = "Cannot divide by zero"
        else:
            result = number1 / number2

    case "%":
        if number2 == 0:
            result = "Cannot calculate remainder with zero"
        else:
            result = number1 % number2

    case _:
        result = "Invalid operator"

print("Result:", result)
```

### Sample Input

```text
Enter first number: 20
Enter operator (+, -, *, /, %): +
Enter second number: 5
```

### Expected Output

```text
Result: 25.0
```

### Explanation

The operator is `+`.

The program selects the addition case and calculates 20 + 5.

### Concepts Used

- String patterns.
- Arithmetic operators.
- Match-case.
- Error handling.

---

## Problem 4: Menu Selection

### Problem Statement

Create a menu-driven program that displays a message according to the selected option.

### Menu

```text
1. Home
2. Profile
3. Settings
4. Help
```

### Logic

1. Display the menu.
2. Accept the user's choice.
3. Match the choice.
4. Display the selected option.

### Code

```python
print("1. Home")
print("2. Profile")
print("3. Settings")
print("4. Help")

choice = int(input("Enter choice: "))

match choice:

    case 1:
        print("You selected Home.")

    case 2:
        print("You selected Profile.")

    case 3:
        print("You selected Settings.")

    case 4:
        print("You selected Help.")

    case _:
        print("Invalid menu choice.")
```

### Sample Input

```text
Enter choice: 2
```

### Expected Output

```text
You selected Profile.
```

### Explanation

The number 2 corresponds to Profile.

### Concepts Used

- Match-case.
- Menu handling.
- Integer patterns.

---

## Problem 5: Weekday or Weekend

### Problem Statement

Accept a day number and classify it as a weekday or weekend.

Use:

- 1–5 for weekdays.
- 6–7 for weekends.

### Logic

1. Accept a day number.
2. Match the number against multiple patterns.
3. Display Weekday or Weekend.
4. Handle invalid values.

### Code

```python
day = int(input("Enter day number (1-7): "))

match day:

    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")

    case 6 | 7:
        print("Weekend")

    case _:
        print("Invalid day")
```

### Sample Input

```text
Enter day number (1-7): 6
```

### Expected Output

```text
Weekend
```

### Explanation

6 matches the second alternative pattern.

### Concepts Used

- OR patterns.
- Multiple literals.
- Wildcard.

---

## Problem 6: Grade Using Guards

### Problem Statement

Accept a percentage and calculate the corresponding grade using `match-case` guard conditions.

### Grading Scale

| Percentage | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| 0–39.99 | F |

### Logic

1. Accept a percentage.
2. Validate it between 0 and 100.
3. Match the subject.
4. Evaluate the appropriate guard.
5. Return the grade.

### Code

```python
percentage = float(input("Enter percentage: "))

match percentage:

    case value if 90 <= value <= 100:
        grade = "A+"

    case value if 80 <= value < 90:
        grade = "A"

    case value if 70 <= value < 80:
        grade = "B"

    case value if 60 <= value < 70:
        grade = "C"

    case value if 50 <= value < 60:
        grade = "D"

    case value if 40 <= value < 50:
        grade = "E"

    case value if 0 <= value < 40:
        grade = "F"

    case _:
        grade = "Invalid percentage"

print("Grade:", grade)
```

### Sample Input

```text
Enter percentage: 85
```

### Expected Output

```text
Grade: A
```

### Explanation

85 falls within the range 80 to below 90.

Therefore, the result is grade A.

### Concepts Used

- Guards.
- Conditional matching.
- Range checks.

---

## Problem 7: Command Handler

### Problem Statement

Create a program that accepts a text command and performs the corresponding action.

Supported commands:

- `start`
- `stop`
- `pause`
- `restart`

### Logic

1. Accept a command.
2. Convert it to lowercase.
3. Match the command.
4. Display the corresponding message.
5. Handle unknown commands.

### Code

```python
command = input(
    "Enter command (start/stop/pause/restart): "
).strip().lower()

match command:

    case "start":
        print("Starting program...")

    case "stop":
        print("Stopping program...")

    case "pause":
        print("Program paused.")

    case "restart":
        print("Restarting program...")

    case _:
        print("Unknown command.")
```

### Sample Input

```text
Enter command (start/stop/pause/restart): pause
```

### Expected Output

```text
Program paused.
```

### Explanation

The command is converted to lowercase and matched against the supported options.

### Concepts Used

- String patterns.
- String methods.
- Command processing.
- Wildcard.

---

## Problem 8: Status Code Category

### Problem Statement

Accept a numeric status code and classify it according to its numeric range.

### Categories

| Range | Classification |
|---|---|
| 100–199 | Informational |
| 200–299 | Success |
| 300–399 | Redirection |
| 400–499 | Client Error |
| 500–599 | Server Error |
| Other values | Unknown |

These are illustrative HTTP-style status-code categories.

### Logic

1. Accept a numeric status code.
2. Match the value.
3. Check the numerical range using guards.
4. Display the classification.

### Code

```python
code = int(input("Enter status code: "))

match code:

    case value if 100 <= value < 200:
        print("Informational")

    case value if 200 <= value < 300:
        print("Success")

    case value if 300 <= value < 400:
        print("Redirection")

    case value if 400 <= value < 500:
        print("Client Error")

    case value if 500 <= value < 600:
        print("Server Error")

    case _:
        print("Unknown Status Code")
```

### Sample Input

```text
Enter status code: 200
```

### Expected Output

```text
Success
```

### Explanation

200 is within the range from 200 to below 300.

Therefore, the classification is Success.

### Concepts Used

- Guards.
- Numeric ranges.
- Conditional matching.

---

## Problem 9: Coordinate Classification

### Problem Statement

Accept two coordinates, X and Y, and classify the point.

### Logic

1. Accept X coordinate.
2. Accept Y coordinate.
3. Create a tuple.
4. Match the tuple pattern.
5. Use guards for quadrant classification.
6. Display the result.

### Code

```python
x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

point = (x, y)

match point:

    case (0, 0):
        print("Point is at the origin.")

    case (0, y):
        print("Point is on the Y-axis.")

    case (x, 0):
        print("Point is on the X-axis.")

    case (x, y) if x > 0 and y > 0:
        print("Point is in the first quadrant.")

    case (x, y) if x < 0 and y > 0:
        print("Point is in the second quadrant.")

    case (x, y) if x < 0 and y < 0:
        print("Point is in the third quadrant.")

    case (x, y) if x > 0 and y < 0:
        print("Point is in the fourth quadrant.")
```

### Sample Input

```text
Enter X coordinate: 5
Enter Y coordinate: 7
```

### Expected Output

```text
Point is in the first quadrant.
```

### Explanation

Both coordinates are positive.

Therefore, the point belongs to the first quadrant.

### Concepts Used

- Tuple patterns.
- Guard conditions.
- Logical operators.
- Pattern matching.

---

## Problem 10: List Pattern

### Problem Statement

Accept a list of integers and identify whether it is empty, contains one value, two values, or multiple values.

### Logic

1. Accept the number of elements.
2. Read the values.
3. Store them in a list.
4. Match the list structure.
5. Display the matching category.

### Code

```python
count = int(input("How many numbers? "))

values = []

for index in range(count):
    number = int(input(f"Enter number {index + 1}: "))
    values.append(number)

match values:

    case []:
        print("Empty list")

    case [only]:
        print("List contains one element:", only)

    case [first, second]:
        print("List contains two elements:", first, second)

    case [first, second, *remaining]:
        print("List contains multiple elements.")
        print("First:", first)
        print("Second:", second)
        print("Remaining:", remaining)
```

### Sample Input

```text
How many numbers? 4
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
```

### Expected Output

```text
List contains multiple elements.
First: 10
Second: 20
Remaining: [30, 40]
```

### Explanation

The list contains more than two elements.

The first two elements are captured separately.

The remaining elements are collected in the `remaining` list.

### Concepts Used

- Lists.
- Sequence patterns.
- Star patterns.
- Match-case.

---

## Problem 11: Unit Converter

### Problem Statement

Create a unit converter using `match-case`.

Support:

1. Kilometres to miles.
2. Miles to kilometres.

### Conversion Formulas

\[
Miles = Kilometres \times 0.621371
\]

\[
Kilometres = Miles \times 1.609344
\]

### Logic

1. Display the conversion menu.
2. Accept the choice.
3. Accept the distance.
4. Match the choice.
5. Apply the correct formula.
6. Display the converted value.

### Code

```python
print("1. Kilometres to Miles")
print("2. Miles to Kilometres")

choice = int(input("Enter choice: "))

value = float(input("Enter distance: "))

match choice:

    case 1:
        converted = value * 0.621371
        print(f"{value:.2f} km = {converted:.2f} miles")

    case 2:
        converted = value * 1.609344
        print(f"{value:.2f} miles = {converted:.2f} km")

    case _:
        print("Invalid choice")
```

### Sample Input

```text
1. Kilometres to Miles
2. Miles to Kilometres
Enter choice: 1
Enter distance: 10
```

### Expected Output

```text
10.00 km = 6.21 miles
```

### Explanation

The choice is 1, so the program converts kilometres into miles.

### Concepts Used

- Match-case.
- Arithmetic.
- Menu selection.
- Floating-point values.

---

## Problem 12: Calculator Menu

### Problem Statement

Build a calculator menu using `match-case`.

### Menu

```text
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Remainder
```

### Logic

1. Display the calculator menu.
2. Accept the choice.
3. Select an arithmetic operator.
4. Accept two numbers.
5. Execute the operation.
6. Handle division by zero.
7. Display the result.

### Code

```python
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")

choice = int(input("Enter choice: "))

match choice:

    case 1:
        operator = "+"

    case 2:
        operator = "-"

    case 3:
        operator = "*"

    case 4:
        operator = "/"

    case 5:
        operator = "%"

    case _:
        operator = None

if operator is None:
    print("Invalid choice")

else:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    match operator:

        case "+":
            result = number1 + number2

        case "-":
            result = number1 - number2

        case "*":
            result = number1 * number2

        case "/":
            if number2 == 0:
                result = "Cannot divide by zero"
            else:
                result = number1 / number2

        case "%":
            if number2 == 0:
                result = "Cannot calculate remainder with zero"
            else:
                result = number1 % number2

    print("Result:", result)
```

### Sample Input

```text
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Remainder
Enter choice: 1
Enter first number: 20
Enter second number: 5
```

### Expected Output

```text
Result: 25.0
```

### Explanation

The menu choice 1 maps to addition.

The selected operator is `+`.

The calculator performs addition.

### Concepts Used

- Nested match-case logic.
- Menu selection.
- Arithmetic.
- Error handling.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these problems independently using Python 3.10 or newer.

## Question 1: Day Name

Accept a number from 1 to 7 and display the corresponding weekday name using `match-case`.

### Requirements

- Accept a day number.
- Match all seven weekday values.
- Display the correct day name.
- Handle an invalid number.

### Concepts

- Integer patterns.
- Wildcard.
- Match-case.

## Question 2: Month Name

Accept a month number from 1 to 12 and display its name.

### Requirements

- Accept month number.
- Match all twelve months.
- Display the matching month.
- Handle invalid input.

### Concepts

- Literal patterns.
- Match-case.
- Integer mapping.

## Question 3: Calculator Using Match Case

Create a calculator that performs five arithmetic operations.

### Requirements

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Remainder.
- Invalid operator handling.
- Division-by-zero handling.

### Concepts

- String matching.
- Arithmetic.
- Conditional logic.

## Question 4: Menu-Driven Program

Create a menu-based program with the following choices:

1. Home.
2. Profile.
3. Settings.
4. Help.

### Requirements

- Display menu choices.
- Accept a choice.
- Match the selected option.
- Display the corresponding message.
- Handle invalid choices.

### Concepts

- Match-case.
- Integer matching.
- Menu handling.

## Question 5: Weekday or Weekend

Accept a day number and classify it as a weekday or weekend.

### Requirements

- 1–5 represent weekdays.
- 6–7 represent weekends.
- Use multiple patterns.
- Handle invalid numbers.

### Concepts

- OR patterns.
- Multiple literal patterns.
- Wildcard.

## Question 6: Grade Using Guards

Accept a percentage and assign a grade using `match-case` guards.

### Requirements

- Validate percentage between 0 and 100.
- Use all seven grade categories.
- Display the grade.
- Handle invalid input.

### Concepts

- Guard conditions.
- Comparison.
- Range classification.

## Question 7: Command Handler

Create a text command processor.

Supported commands:

- start.
- stop.
- pause.
- resume.
- restart.

### Requirements

- Accept a command.
- Convert it to lowercase.
- Match the command.
- Display an appropriate response.
- Handle unknown commands.

### Concepts

- String patterns.
- Match-case.
- Command processing.

## Question 8: Status Code Classification

Accept a numeric status code and classify it into the appropriate range.

### Requirements

- 100–199: Informational.
- 200–299: Success.
- 300–399: Redirection.
- 400–499: Client Error.
- 500–599: Server Error.
- Other values: Unknown.

### Concepts

- Guard conditions.
- Numeric comparisons.
- Pattern matching.

## Question 9: Coordinate Classification

Accept two coordinates and classify the point as:

- Origin.
- X-axis.
- Y-axis.
- First quadrant.
- Second quadrant.
- Third quadrant.
- Fourth quadrant.

### Requirements

- Accept X and Y.
- Store values in a tuple.
- Use tuple patterns.
- Use guards.
- Display the correct position.

### Concepts

- Tuple patterns.
- Guards.
- Logical operators.

## Question 10: List Pattern Matching

Accept a list of integers and identify its structure.

### Requirements

- Empty list.
- One element.
- Two elements.
- Multiple elements.
- Display the captured values.

### Concepts

- List patterns.
- Sequence matching.
- Star patterns.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Using the Wrong Python Version

`match-case` is available from Python 3.10.

Using an older Python version causes a syntax error.

Check your version:

```bash
python --version
```

## Mistake 2: Incorrect Indentation

Incorrect:

```python
match number:
case 1:
    print("One")
```

Correct:

```python
match number:
    case 1:
        print("One")
```

## Mistake 3: Forgetting the Colon

Incorrect:

```python
match number
```

Correct:

```python
match number:
```

Every case pattern also needs a colon.

## Mistake 4: Missing Default Case

Incorrect:

```python
match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
```

This does not define how unrecognized values should be handled.

Correct when a default action is required:

```python
match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other value")
```

## Mistake 5: Placing Wildcard First

Incorrect:

```python
match number:
    case _:
        print("Default")
    case 1:
        print("One")
```

The unconditional wildcard case matches everything, making the later case unreachable.

Correct:

```python
match number:
    case 1:
        print("One")
    case _:
        print("Default")
```

## Mistake 6: Confusing Match Case With If-Elif-Else

`match-case` uses patterns.

`if-elif-else` directly evaluates Boolean expressions.

A numerical range condition is often written using a guard in `match-case`.

## Mistake 7: Incorrect Use of OR Patterns

Incorrect:

```python
match number:
    case 1 or 2 or 3:
        print("Group")
```

The `or` keyword is not used to define alternatives inside a pattern.

Correct:

```python
match number:
    case 1 | 2 | 3:
        print("Group")
```

## Mistake 8: Incorrect Guard Syntax

Incorrect:

```python
match number:
    case value:
        if value > 10:
            print("Greater")
```

This does not express a guarded pattern.

Correct:

```python
match number:
    case value if value > 10:
        print("Greater")
```

## Mistake 9: Treating a Capture Pattern as Equality

Incorrect:

```python
TARGET = 10

match number:
    case TARGET:
        print("Matched")
```

A bare name is a capture pattern, not a check against the existing variable.

Use a literal pattern or an appropriate guard.

## Mistake 10: Incorrect Pattern Order

A broad pattern can match before a more specific pattern.

Place specific cases before general cases.

## Mistake 11: Forgetting Guard Conditions

A captured value does not automatically satisfy the guard.

Both the pattern and the guard must succeed.

## Mistake 12: Not Handling Invalid Input

A menu-based program should handle invalid menu choices.

## Mistake 13: Division by Zero

A calculator should check the second operand before division or remainder operations.

## Mistake 14: Confusing First Match and All Matches

A `match-case` statement selects one case.

It does not automatically execute all matching case blocks.

## Mistake 15: Using a Case That Can Never Match

An unconditional case such as `case value:` captures every subject.

Placing it before specific patterns makes later cases unreachable.

## Mistake 16: Confusing Pattern Matching With Assignment

A pattern may bind names, but the purpose of `match-case` is to match the structure and values of the subject.

## Mistake 17: Incorrect Tuple Length

A pattern such as:

```python
case (x, y):
```

expects a sequence with exactly two matching elements.

A sequence with three elements does not match this two-element pattern.

## Mistake 18: Incorrect List Pattern Order

Place exact patterns before more general star patterns when their results should be different.

## Mistake 19: Forgetting None Handling

Use:

```python
case None:
```

when checking for the absence of a value.

## Mistake 20: Ignoring Type Pattern Behaviour

Python class patterns follow the language's type relationships.

For example, `bool` is a subclass of `int`.

---

# SECTION 5: BEST PRACTICES

Follow these practices when writing `match-case` programs.

1. Use Python 3.10 or newer.
2. Understand the subject before defining patterns.
3. Use meaningful case labels.
4. Use literal patterns for fixed values.
5. Use `|` for alternative patterns.
6. Use `_` for the default case.
7. Place wildcard cases last.
8. Use guards for ranges and extra conditions.
9. Use specific patterns before general patterns.
10. Understand capture patterns.
11. Use tuple patterns for related values.
12. Use list patterns to identify sequence structure.
13. Use class patterns for type-based matching.
14. Validate user input before processing it.
15. Handle unexpected values.
16. Avoid unnecessarily complicated patterns.
17. Use functions to keep code reusable.
18. Use clear variable names.
19. Keep menu options organized.
20. Handle division by zero.
21. Add comments for complex patterns.
22. Use consistent indentation.
23. Separate input handling from calculations when appropriate.
24. Keep the main menu simple.
25. Use `if-elif-else` when it is clearer than pattern matching.

### Recommended Calculator Function

```python
def perform_calculation(number1, number2, operator):

    match operator:

        case "+":
            return number1 + number2

        case "-":
            return number1 - number2

        case "*":
            return number1 * number2

        case "/":
            if number2 == 0:
                raise ZeroDivisionError(
                    "Cannot divide by zero."
                )

            return number1 / number2

        case "%":
            if number2 == 0:
                raise ZeroDivisionError(
                    "Cannot calculate remainder with zero."
                )

            return number1 % number2

        case _:
            raise ValueError("Invalid operator")
```

### Recommended Day Function

```python
def get_day_name(day_number):

    match day_number:

        case 1:
            return "Monday"

        case 2:
            return "Tuesday"

        case 3:
            return "Wednesday"

        case 4:
            return "Thursday"

        case 5:
            return "Friday"

        case 6:
            return "Saturday"

        case 7:
            return "Sunday"

        case _:
            return "Invalid day"
```

---

# SECTION 6: DEBUGGING

Debugging is the process of identifying and correcting errors in a program.

Match-case problems can contain errors related to pattern syntax, pattern order, data types, guards, and input handling.

## 1. Check Python Version

Ensure Python 3.10 or newer is installed.

## 2. Check Match Syntax

Correct structure:

```python
match subject:
    case pattern:
        statement
```

## 3. Check Case Indentation

Every case must be indented under the match statement.

The statements inside each case must be indented further.

## 4. Check Pattern Order

Ensure specific patterns appear before general patterns.

## 5. Check Wildcard Placement

Place `case _` last.

## 6. Check Guard Conditions

Verify that the guard evaluates to the intended Boolean result.

## 7. Check Capture Patterns

Remember that bare names capture the subject.

They do not compare against previously defined variables.

## 8. Check Input Types

The `input()` function returns text.

Use integer or floating-point conversion when required.

## 9. Check Calculator Operations

Handle zero before performing division or remainder.

## 10. Check Sequence Patterns

Verify that tuple or list shapes match the expected number of elements.

### Common Python Errors

| Error | Meaning |
|---|---|
| `SyntaxError` | Invalid Python syntax |
| `IndentationError` | Incorrect indentation |
| `ValueError` | Invalid input conversion |
| `TypeError` | Invalid operation involving data types |
| `NameError` | Variable or function is undefined |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | Invalid sequence index |
| `AttributeError` | Invalid attribute access |

### Debugging Checklist

Before considering your program complete:

- Check the Python version.
- Check the `match` statement.
- Check each `case`.
- Check indentation.
- Check pattern order.
- Check the wildcard.
- Check guard conditions.
- Check captured variables.
- Check string and integer types.
- Check list and tuple structures.
- Check invalid inputs.
- Check arithmetic calculations.
- Check division by zero.
- Check the output.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Structural pattern matching is useful in applications where a program must respond differently to different commands, values, or data structures.

## 1. Menu-Driven Applications

A program can perform different tasks according to the user's menu choice.

## 2. Calculator Applications

An arithmetic calculator can select an operation based on an operator.

## 3. Command-Line Tools

Command processors can respond to commands such as start, stop, pause, and restart.

## 4. Calendar Applications

Weekday and month numbers can be converted into readable names.

## 5. Educational Applications

Marks and percentages can be classified into different grade categories.

## 6. Data Processing

Programs can identify different data structures and process them accordingly.

## 7. API Response Handling

Numeric status codes can be classified into groups.

## 8. Coordinate Processing

Tuple patterns can classify points according to coordinate structure.

## 9. Workflow Systems

Different commands or states can be handled through separate cases.

## 10. Configuration Processing

Programs can match recognized configuration values and handle defaults.

### Real-Life Example: Command Handler

```python
command = input("Enter command: ").strip().lower()

match command:

    case "start":
        print("Application started.")

    case "stop":
        print("Application stopped.")

    case "pause":
        print("Application paused.")

    case "restart":
        print("Application restarting.")

    case _:
        print("Unknown command.")
```

This approach provides a clean way to process recognized commands.

---

# SECTION 8: DSA CONNECTION

The `match-case` topic introduces concepts that support future problem-solving and algorithm design.

Although `match-case` itself is a control-flow feature rather than a data structure or searching algorithm, it helps organize decision-making logic.

## 1. Decision-Making

A program selects an action based on a matching pattern.

## 2. Classification

Different values can be classified into categories.

## 3. Searching for a Matching Pattern

Python examines patterns in order until a matching case is selected.

## 4. Sequence Processing

Tuple and list patterns introduce structural matching.

## 5. Data Type Identification

Class patterns help identify objects of specific types.

## 6. Command Processing

Different commands can be handled using separate branches.

## 7. Function Design

Pattern matching can be placed inside reusable functions.

## 8. Guard Conditions

Guards combine pattern matching with additional Boolean conditions.

### DSA Skills Developed

- Conditional decision-making.
- Value classification.
- Sequence recognition.
- Pattern matching.
- Function design.
- Control-flow organization.
- Data type handling.
- Input validation.
- Basic complexity analysis.

### Example: Matching a Value in a List

```python
values = [10, 20, 30]

for value in values:

    match value:

        case 10:
            print("Ten")

        case 20:
            print("Twenty")

        case 30:
            print("Thirty")

        case _:
            print("Other")
```

**Output:**

```text
Ten
Twenty
Thirty
```

The loop processes every list element.

The `match-case` statement selects the appropriate action for each value.

### Example: Classifying a Tuple

```python
point = (5, 0)

match point:

    case (0, 0):
        print("Origin")

    case (0, y):
        print("Y-axis")

    case (x, 0):
        print("X-axis")

    case (x, y):
        print("General point")
```

**Output:**

```text
X-axis
```

This demonstrates how structural matching can be used to recognize data arrangements.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Time complexity describes how an algorithm's running time changes as input size increases.

Space complexity describes how much additional memory an algorithm requires.

## 1. Matching One Integer

Consider:

```python
number = 2

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
```

For a fixed number of cases, the program performs a bounded number of matching attempts.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 2. Matching a String

Consider:

```python
command = "start"

match command:
    case "start":
        print("Started")
    case "stop":
        print("Stopped")
    case _:
        print("Unknown")
```

For a fixed number of cases and bounded-length strings, this is treated as constant-time classification for basic complexity analysis.

Additional space complexity:

\[
O(1)
\]

For arbitrary string lengths, string comparison itself may require time proportional to the compared string length.

## 3. Matching a Day Number

The program matches one number against a fixed set of weekday patterns.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 4. Calculator Operation Selection

Selecting one operation among a fixed number of arithmetic choices requires a bounded number of pattern checks.

Time complexity:

\[
O(1)
\]

The arithmetic operation also uses constant additional space.

## 5. Guard-Based Grade Calculation

A fixed number of grade ranges is checked.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 6. Tuple Pattern Matching

A tuple with a fixed number of elements is matched against a fixed set of patterns.

For the simple coordinate examples:

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 7. List Pattern Matching

A list pattern may need to examine its sequence structure.

For a list with `n` elements, structural checks and sequence matching may require work proportional to the number of elements, depending on the pattern.

A reasonable general upper-bound analysis for sequence matching is:

Time complexity:

\[
O(n)
\]

Additional space depends on captures and the pattern.

A star capture such as:

```python
case [first, second, *remaining]:
```

creates a new list for the remaining elements.

Its captured data may require:

\[
O(n)
\]

additional space.

## 8. Processing Multiple Values

Consider:

```python
values = [1, 2, 3, 4, 5]

for value in values:

    match value:
        case 1:
            print("One")
        case 2:
            print("Two")
        case _:
            print("Other")
```

If the number of cases is fixed, each list element requires bounded matching work.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

excluding the input list.

## Complexity Summary

| Operation | Time Complexity | Additional Space |
|---|---:|---:|
| Match one integer | \(O(1)\) | \(O(1)\) |
| Match one fixed command | \(O(1)\) | \(O(1)\) |
| Match weekday number | \(O(1)\) | \(O(1)\) |
| Calculator operation selection | \(O(1)\) | \(O(1)\) |
| Grade classification with fixed guards | \(O(1)\) | \(O(1)\) |
| Match fixed-size coordinate tuple | \(O(1)\) | \(O(1)\) |
| Inspect a sequence of n elements | Up to \(O(n)\), pattern-dependent | Pattern-dependent |
| Capture remaining sequence elements | \(O(n)\) | \(O(n)\) |
| Process n values using fixed cases | \(O(n)\) | \(O(1)\) additional |

### Important Point

The presence of `match-case` does not automatically make a program faster than `if-elif-else`.

Choose the construct based on readability and the problem structure.

---

# SECTION 10: MINI PROJECT – MENU-DRIVEN COMMAND MANAGEMENT SYSTEM

## Project Overview

Create a menu-driven command management application using `match-case`.

The program supports:

1. Start.
2. Stop.
3. Pause.
4. Resume.
5. Restart.
6. Display help.
7. Exit.

This project combines string patterns, integer patterns, functions, loops, input validation, and wildcard handling.

### Project Features

- Interactive menu.
- Command selection.
- Match-case operation handling.
- Multiple alternative command patterns.
- Guard conditions.
- Invalid command handling.
- Reusable functions.
- Continuous menu until exit.

### Python Code

```python
def start_program():
    print("Program started.")


def stop_program():
    print("Program stopped.")


def pause_program():
    print("Program paused.")


def resume_program():
    print("Program resumed.")


def restart_program():
    print("Program restarted.")


def show_help():
    print("Available commands:")
    print("start")
    print("stop")
    print("pause")
    print("resume")
    print("restart")
    print("help")
    print("exit")


def process_command(command):

    match command:

        case "start" | "run":
            start_program()

        case "stop" | "close":
            stop_program()

        case "pause":
            pause_program()

        case "resume":
            resume_program()

        case "restart" | "reset":
            restart_program()

        case "help":
            show_help()

        case "exit" | "quit":
            return False

        case value if value == "":
            print("Empty command.")

        case _:
            print("Unknown command.")

    return True


def main():

    print("COMMAND MANAGEMENT SYSTEM")

    while True:

        print("\nAvailable Options")
        print("1. Start")
        print("2. Stop")
        print("3. Pause")
        print("4. Resume")
        print("5. Restart")
        print("6. Help")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        match choice:

            case "1":
                command = "start"

            case "2":
                command = "stop"

            case "3":
                command = "pause"

            case "4":
                command = "resume"

            case "5":
                command = "restart"

            case "6":
                command = "help"

            case "0":
                command = "exit"

            case _:
                print("Invalid menu choice.")
                continue

        if not process_command(command):
            print("Exiting application...")
            break


if __name__ == "__main__":
    main()
```

### Sample Input

```text
COMMAND MANAGEMENT SYSTEM

Available Options
1. Start
2. Stop
3. Pause
4. Resume
5. Restart
6. Help
0. Exit

Enter choice: 1
```

### Expected Output

```text
Program started.
```

### Explanation

The main menu uses integer-like string patterns.

The selected option is converted into a command.

The `process_command()` function uses string patterns to select the operation.

### Project Improvements

After completing the basic project, try these improvements:

1. Add more commands.
2. Add command aliases.
3. Add a command history list.
4. Store application states.
5. Use tuples to process command arguments.
6. Add a status display.
7. Add an error log.
8. Add command validation.
9. Add file-based settings.
10. Build a command-line utility using structural pattern matching.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is match-case in Python?

It is a statement used for structural pattern matching.

### 2. In which Python version was match-case introduced?

Python 3.10.

### 3. What is the main purpose of match-case?

To select an appropriate block based on a matching pattern.

### 4. What is the syntax of match-case?

```python
match subject:
    case pattern:
        statement
```

### 5. What is the role of the match keyword?

It begins the pattern-matching statement.

### 6. What is the role of the case keyword?

It defines a pattern to match against the subject.

### 7. What is a pattern?

A pattern describes the structure or value that should match a subject.

### 8. What is a wildcard pattern?

The `_` pattern, which matches any value.

### 9. What does the `|` symbol do in an OR pattern?

It allows multiple alternative patterns in one case.

### 10. Does match-case support string matching?

Yes.

## Intermediate Questions

### 11. What is a literal pattern?

A pattern that matches a specific literal value.

### 12. What is a guard condition?

An additional Boolean condition written after a pattern using `if`.

### 13. What is a capture pattern?

A pattern that binds the subject value to a name.

### 14. Does a bare variable name compare values in a case pattern?

No. A bare name is generally a capture pattern.

### 15. What is the purpose of `case _`?

It handles values that did not match earlier cases.

### 16. Does match-case automatically execute the next case?

No. It selects one matching case.

### 17. Can match-case be used for a menu-driven application?

Yes.

### 18. Can match-case be used with integers?

Yes.

### 19. Can match-case be used with strings?

Yes.

### 20. Can match-case be used with Boolean values?

Yes.

## Practical Questions

### 21. What is a tuple pattern?

A pattern that matches a tuple-like sequence structure.

### 22. What is a list pattern?

A pattern that matches a sequence structure.

### 23. What is the use of `*remaining` in a sequence pattern?

It captures the remaining sequence elements.

### 24. What is a class pattern?

A pattern that matches an object using a specified class.

### 25. How do you classify a grade with match-case?

Use guard conditions for percentage ranges.

### 26. How do you build a calculator using match-case?

Match the operator and perform its corresponding arithmetic operation.

### 27. How do you display the month name using match-case?

Match a number from 1 to 12 with the month patterns.

### 28. How do you classify a weekday or weekend?

Use OR patterns to group weekday and weekend numbers.

### 29. What is the purpose of `return`?

It returns a value from a function.

### 30. Can a match-case statement be inside a function?

Yes.

## Advanced Questions

### 31. What is structural pattern matching?

It is a language feature that matches the shape and content of data structures.

### 32. Why is pattern order important?

Python checks cases in order and selects the first successful match.

### 33. Where should the wildcard case normally appear?

At the end.

### 34. What happens when a guard is false?

That case is not selected, and pattern matching continues with subsequent cases.

### 35. Can a match-case statement contain tuple patterns?

Yes.

### 36. Can a match-case statement contain list patterns?

Yes.

### 37. Can match-case contain nested patterns?

Yes.

### 38. Does match-case automatically fall through?

No.

### 39. What is the time complexity of matching one fixed integer against a fixed number of cases?

\(O(1)\) for the usual fixed-case problem.

### 40. What is the time complexity of processing n values with a fixed match statement?

\(O(n)\).

## Interview-Oriented Questions

### 41. What is the difference between match-case and if-elif-else?

`if-elif-else` evaluates Boolean conditions, while `match-case` uses patterns and supports structural matching.

### 42. What is the advantage of OR patterns?

They allow multiple alternatives to share the same case block.

### 43. Why use guards?

They add conditions to patterns, such as checking numerical ranges.

### 44. Why should the wildcard case be placed last?

An unconditional wildcard captures every subject, so later cases would be unreachable.

### 45. Does a bare name in a pattern refer to an existing variable?

No. It normally creates a capture binding.

### 46. What is the difference between a literal pattern and a capture pattern?

A literal pattern checks a specific value, while a capture pattern binds the subject to a name.

### 47. Can match-case identify object types?

Yes, using class patterns.

### 48. What should be used to handle division by zero in a calculator?

Check whether the second operand is zero before division or remainder calculation.

### 49. Why is Python 3.10 required?

Because structural pattern matching was introduced in Python 3.10.

### 50. Which applications can use match-case?

Menu systems, calculators, command handlers, data processing programs, and pattern-based classification systems.

---

# SECTION 12: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Match-case | Python structural pattern matching statement |
| Structural pattern matching | Matching values and data structures against patterns |
| Subject | Value or object being matched |
| Pattern | Description of the expected value or structure |
| Case | A branch containing a pattern |
| Literal pattern | Pattern that matches a specific value |
| Wildcard | `_`, a pattern matching anything |
| OR pattern | Pattern containing alternative matches |
| Guard | Additional Boolean condition after a pattern |
| Capture pattern | Pattern that binds a subject to a variable |
| Sequence pattern | Pattern matching a sequence structure |
| Tuple pattern | Pattern matching tuple-like data |
| List pattern | Pattern matching a list-like sequence |
| Star pattern | Pattern capturing remaining sequence values |
| Class pattern | Pattern matching an object by class |
| Mapping pattern | Pattern matching a mapping's keys and values |
| Subject | Expression evaluated by the match statement |
| Boolean | Value that is either true or false |
| Conditional expression | Compact form of conditional value selection |
| Control flow | Order in which program statements execute |
| Menu-driven program | Program controlled through user menu choices |
| Command handler | Function or system that processes commands |
| Pattern order | Order in which patterns are evaluated |
| Type matching | Matching an object using its class |
| Default case | Fallback case, commonly written using `_` |
| Function | Reusable block of code |
| Return | Sends a value back from a function |
| Validation | Checking whether input is acceptable |
| Time complexity | Growth of algorithm execution time |
| Space complexity | Growth of algorithm memory requirements |

---

# SECTION 13: QUICK REVISION NOTES

## Basic Match-Case

```python
match value:
    case 1:
        print("One")

    case 2:
        print("Two")

    case _:
        print("Other")
```

## Multiple Patterns

```python
match value:
    case 1 | 2 | 3:
        print("Group one")

    case 4 | 5 | 6:
        print("Group two")

    case _:
        print("Other")
```

## Wildcard Pattern

```python
match value:
    case _:
        print("Default")
```

## String Matching

```python
match command:
    case "start":
        print("Started")

    case "stop":
        print("Stopped")

    case _:
        print("Unknown")
```

## Guard Condition

```python
match percentage:
    case value if value >= 90:
        print("A+")

    case value if value >= 80:
        print("A")

    case _:
        print("Other")
```

## Tuple Pattern

```python
point = (0, 0)

match point:
    case (0, 0):
        print("Origin")

    case (0, y):
        print("Y-axis")

    case (x, 0):
        print("X-axis")

    case (x, y):
        print("General point")
```

## List Pattern

```python
values = [10, 20]

match values:
    case []:
        print("Empty")

    case [only]:
        print("One element")

    case [first, second]:
        print("Two elements")

    case [first, second, *remaining]:
        print("Multiple elements")
```

## Type Pattern

```python
match value:
    case int():
        print("Integer")

    case str():
        print("String")

    case list():
        print("List")

    case _:
        print("Other")
```

## Day Name Function

```python
def get_day_name(day):

    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"
```

## Calculator

```python
match operator:
    case "+":
        result = a + b

    case "-":
        result = a - b

    case "*":
        result = a * b

    case "/":
        result = a / b

    case _:
        print("Invalid operator")
```

## Important Reminders

- Match-case requires Python 3.10 or newer.
- `match` identifies the subject.
- `case` defines a pattern.
- `_` is a wildcard.
- `|` represents alternative patterns.
- Guards add Boolean conditions.
- Bare names create capture patterns.
- Tuple and list patterns recognize sequence structures.
- Class patterns can match types.
- Pattern order matters.
- Match-case does not fall through.
- Place the default wildcard last.
- Handle invalid input.
- Use functions for reusable logic.

---

# SECTION 14: LEARNING CHECKLIST

- [ ] I understand the purpose of match-case.
- [ ] I know that match-case was introduced in Python 3.10.
- [ ] I understand the basic syntax.
- [ ] I can match integer values.
- [ ] I can match string values.
- [ ] I can use literal patterns.
- [ ] I can use multiple patterns with `|`.
- [ ] I understand the wildcard `_`.
- [ ] I can write a menu-driven program.
- [ ] I can handle commands using string patterns.
- [ ] I understand guard conditions.
- [ ] I can classify grades using guards.
- [ ] I can perform calculator operations using match-case.
- [ ] I can match weekday numbers.
- [ ] I can match month numbers.
- [ ] I understand capture patterns.
- [ ] I can match tuple patterns.
- [ ] I can match list patterns.
- [ ] I understand star patterns.
- [ ] I understand class patterns.
- [ ] I can classify status codes using guards.
- [ ] I can classify coordinates using tuple patterns.
- [ ] I understand pattern order.
- [ ] I can use functions with match-case.
- [ ] I can handle invalid choices.
- [ ] I can handle division by zero.
- [ ] I understand the difference between match-case and if-elif-else.
- [ ] I understand time complexity.
- [ ] I understand space complexity.
- [ ] I have attempted all ten unsolved questions.

---

# SECTION 15: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `07-Match-Case` folder.

### Check Python Version

```powershell
python --version
```

The installed version should be Python 3.10 or newer.

### Run the File

```powershell
python 01_match_case.py
```

On Windows, you can also use:

```powershell
py 01_match_case.py
```

### Main Menu

```text
=================================================================
                       PYTHON: MATCH CASE
=================================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

### Option 1 – View 12 Topic Examples

Displays the twelve examples:

1. Basic Match-Case.
2. Multiple Patterns.
3. Wildcard Pattern.
4. Day Name.
5. Menu Choices.
6. String Commands.
7. Grade Using Guards.
8. Simple Calculator.
9. Tuple Pattern.
10. List Pattern.
11. Status Code Classification.
12. Type Patterns.

### Option 2 – Practice 12 Solved Problems

Displays the twelve solved problem options.

Select a problem number to execute it.

### Option 3 – View 10 Unsolved Questions

Displays ten independent problems for practice.

### Option 4 – View Learning Checklist

Displays the topic checklist.

### Option 0 – Exit

Closes the program.

---

# SECTION 16: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        ├── README.md
        │
        ├── 01-If-Statement/
        ├── 02-If-Else/
        ├── 03-If-Elif-Else/
        ├── 04-Nested-If/
        ├── 05-Conditional-Expressions/
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

### File Details

| File | Purpose |
|---|---|
| `README.md` | Complete Match Case theory, patterns, syntax, examples, solved problems, and revision notes |
| `01_match_case.py` | Executable Python program containing 12 examples, 12 solved problems, 10 unsolved questions, helper functions, learning checklist, and interactive menu |

### Current Topic

**07 – Match Case**

You have learned how Python matches values and structures against different patterns.

### Previous Folder

**06 – Practice Problems**

You completed six practical problems applying conditional statements:

1. Positive and Negative.
2. Even and Odd.
3. Largest Number.
4. Leap Year.
5. Grade Calculator.
6. Voting Eligibility.

### Next Learning Step

After completing Match Case, continue with the next topic or section in your repository's learning sequence.

---

# FINAL SUMMARY

The Match Case topic introduces structural pattern matching in Python.

It provides a readable way to match values, commands, and data structures against different patterns.

After completing this topic, you should be able to:

1. Explain the meaning of match-case.
2. Understand its Python version requirement.
3. Write basic match-case statements.
4. Match integer values.
5. Match string values.
6. Use multiple patterns.
7. Use wildcard patterns.
8. Use guard conditions.
9. Build menu-based applications.
10. Build calculator programs.
11. Match weekday numbers.
12. Match month numbers.
13. Classify percentages.
14. Classify status codes.
15. Understand tuple patterns.
16. Understand list patterns.
17. Understand star patterns.
18. Use class patterns.
19. Understand capture patterns.
20. Organize code using reusable functions.

### Final Advice

Do not memorize only the syntax of `match-case`.

Understand how Python checks patterns, why case order matters, how wildcard patterns work, and how guard conditions add extra decision-making logic.

Practise simple literal matching first.

Then move to OR patterns, guards, tuple patterns, list patterns, and class patterns.

Once you understand these concepts, you will be able to use structural pattern matching in menu-driven programs, calculators, command processors, and more complex Python applications.

**Keep practising, keep improving, and maintain the same repository structure throughout your Python learning journey.**

