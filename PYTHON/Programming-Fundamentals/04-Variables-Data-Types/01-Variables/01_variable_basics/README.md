# Variable Basics in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Topic:** Variables  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. Introduction to Variables
2. Learning Objectives
3. What Is a Variable?
4. Why Are Variables Important?
5. Creating and Assigning Variables
6. Reading and Updating Variable Values
7. Assignment Operator vs Comparison Operator
8. Variables in Arithmetic Expressions
9. Multiple Variables
10. Compound Assignment Operators
11. Constants and Naming Conventions
12. Displaying Variables with `print()` and f-Strings
13. Variable Tracing and Dry Runs
14. Practical Applications
15. Explanation of the 12 Guided Examples
16. Explanation of the 12 Solved Problems
17. Five Unsolved Practice Questions
18. Common Errors and Debugging
19. Best Practices
20. Frequently Asked Questions
21. How to Run the Program
22. Folder Structure
23. Revision Checklist

---

# 1. Introduction to Variables

Variables are one of the first concepts to learn when starting Python programming.

A program frequently needs to remember information, perform calculations, update results, and display values. Variables provide names that allow a program to refer to those values.

For example, a program that calculates the total price of items may use variables for the item price, quantity, and total cost.

```python
price = 35
quantity = 4

total_cost = price * quantity

print(total_cost)
```

Output:

```text
140
```

In this program:

- `price` refers to the value `35`.
- `quantity` refers to the value `4`.
- `total_cost` refers to the calculated result `140`.

Instead of repeating literal numbers throughout the program, we use meaningful names that make the calculation easier to understand.

# 2. Learning Objectives

After completing this topic, you should be able to:

- Define a variable in Python.
- Create variables using assignment statements.
- Understand variable reassignment.
- Use variables in arithmetic expressions.
- Store and update calculation results.
- Use compound assignment operators.
- Display variables using `print()`.
- Format output using f-strings.
- Distinguish assignment from comparison.
- Trace variable values step by step.
- Use meaningful variable names.
- Apply variables to beginner-level programming problems.

# 3. What Is a Variable?

A variable is a name that refers to an object in a Python program.

For beginners, it is helpful to think of a variable as a named place for information. In Python, however, the name refers to an object rather than acting as a permanently typed storage box.

Example:

```python
student_name = "Amaan"
age = 20
marks = 85.5
```

Here, the names refer to different values.

| Variable | Example value | Purpose |
|---|---|---|
| `student_name` | `"Amaan"` | Stores a student's name |
| `age` | `20` | Represents age in years |
| `marks` | `85.5` | Represents a marks value |

The actual meaning depends on how the variable is used in the program.

### Important Terms

**Variable name:** The name used to refer to a value, such as `age`.

**Assignment:** The operation of binding a name to a value or object.

**Value:** The information represented by an object, such as `20` or `"Amaan"`.

**Expression:** A combination of values, variables, and operators that produces a result.

Example:

```python
age = 20
next_year_age = age + 1
```

The expression `age + 1` is evaluated, and its result is assigned to `next_year_age`.

# 4. Why Are Variables Important?

Variables make programs useful because calculations can work with named values instead of only fixed numbers.

## 4.1 Store Information

```python
name = "Amaan"
city = "Nagpur"
```

## 4.2 Perform Calculations

```python
length = 10
width = 5

area = length * width
```

## 4.3 Reuse Values

The same variable can participate in multiple calculations.

```python
price = 100

discount = price * 0.10
final_price = price - discount
```

## 4.4 Update Results

```python
score = 50
score = score + 10

print(score)
```

Output:

```text
60
```

## 4.5 Improve Readability

Compare:

```python
total = 35 * 4
```

with:

```python
price_per_item = 35
quantity = 4
total_cost = price_per_item * quantity
```

Both expressions calculate the same amount, but the second version makes the purpose of each value clearer.

# 5. Creating and Assigning Variables

Python uses the assignment operator `=` to assign a value to a variable.

### Basic Syntax

```python
variable_name = value
```

Examples:

```python
name = "Amaan"
age = 20
price = 99.50
is_student = True
```

The name on the left refers to the object produced by the expression on the right.

### Assignment with an Expression

```python
a = 10
b = 20
total = a + b

print(total)
```

Output:

```text
30
```

Python evaluates the right-hand expression and then assigns the result to the variable.

### Assigning a Value to a New Name

```python
number = 25
another_number = number

print(number)
print(another_number)
```

Both names initially refer to the integer value `25`.

If you later reassign one name to a different object, the other name does not automatically change.

```python
number = 50

print(number)
print(another_number)
```

Output:

```text
50
25
```

This is important when learning how variable assignment works in Python.

# 6. Reading and Updating Variable Values

A variable can be reassigned during program execution.

Example:

```python
score = 40
print(score)

score = 65
print(score)

score = 90
print(score)
```

Output:

```text
40
65
90
```

Each assignment binds the name `score` to a new value.

### Updating Based on the Existing Value

```python
balance = 1000
balance = balance + 500

print(balance)
```

Output:

```text
1500
```

The statement is evaluated in this order:

1. Read the current value of `balance`.
2. Add `500`.
3. Assign the result back to `balance`.

The value changes from `1000` to `1500`.

### Important Difference

```python
score = 10
score = score + 5
```

This is valid because the second statement reads the current value of `score` before assigning the calculated result back to the same name.

By contrast, using a name before assigning it a value can result in a `NameError`.

# 7. Assignment Operator vs Comparison Operator

The assignment operator `=` and equality comparison operator `==` have different purposes.

| Operator | Purpose | Example |
|---|---|---|
| `=` | Assign a value | `age = 20` |
| `==` | Check equality | `age == 20` |
| `!=` | Check inequality | `age != 20` |

### Assignment Example

```python
number = 10
```

This assigns `10` to `number`.

### Comparison Example

```python
number = 10
result = number == 10

print(result)
```

Output:

```text
True
```

The expression `number == 10` evaluates to a Boolean value. The result is then assigned to `result`.

### Common Mistake

Incorrect:

```python
if age = 18:
    print("Age is 18")
```

Correct:

```python
if age == 18:
    print("Age is 18")
```

Assignment is not used as the equality test in this conditional expression.

# 8. Variables in Arithmetic Expressions

Variables can be used with arithmetic operators to perform calculations.

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `//` | Floor division | `a // b` |
| `%` | Remainder | `a % b` |
| `**` | Exponentiation | `a ** b` |

Example:

```python
a = 17
b = 5

print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4
print(a // b)  # 3
print(a % b)   # 2
print(a ** 2)  # 289
```

### Using Variables in Formulas

**Rectangle area:**

```python
length = 8
width = 5

area = length * width
```

**Rectangle perimeter:**

```python
perimeter = 2 * (length + width)
```

**Simple interest:**

```python
principal = 10000
rate = 5
time = 2

interest = principal * rate * time / 100
```

Using variables makes it easier to update input values without rewriting the formulas.

# 9. Multiple Variables

Python allows multiple assignments in a single statement.

### Separate Assignments

```python
name = "Amaan"
age = 20
city = "Nagpur"
```

Each statement assigns a value to one name.

### Multiple Assignment

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

The number of variable names must match the number of values being unpacked.

### Assign the Same Value to Multiple Names

```python
x = y = z = 0

print(x, y, z)
```

Output:

```text
0 0 0
```

All three names refer to the assigned integer object.

This form is convenient for initializing several counters to zero. Be more careful with mutable objects such as lists, because assigning the same mutable object to several names does not create separate lists.

The dedicated Multiple Variables topic will explore these concepts in greater detail.

# 10. Compound Assignment Operators

Compound assignment combines an operation with assignment.

| Operator | Equivalent expression |
|---|---|
| `+=` | `x = x + value` |
| `-=` | `x = x - value` |
| `*=` | `x = x * value` |
| `/=` | `x = x / value` |
| `//=` | `x = x // value` |
| `%=` | `x = x % value` |
| `**=` | `x = x ** value` |

Example:

```python
count = 10

count += 5
print(count)  # 15

count -= 3
print(count)  # 12

count *= 2
print(count)  # 24
```

These operators are particularly useful for updating counters, accumulators, balances, and calculation results.

# 11. Constants and Naming Conventions

A constant is a value intended to remain unchanged throughout a program.

Python does not enforce ordinary variable immutability merely because a name is intended to represent a constant. By convention, uppercase names are used to communicate that the value should not be reassigned.

Example:

```python
PI = 3.14159
SECONDS_PER_MINUTE = 60
DAYS_PER_WEEK = 7
```

The convention makes the intended role of each name clearer.

## Variable Naming Rules

Python identifiers generally follow these rules:

1. A name may contain letters, digits, and underscores.
2. A name cannot begin with a digit.
3. A name cannot be a reserved Python keyword.
4. Names are case-sensitive.
5. Spaces are not allowed inside identifiers.

Examples:

| Name | Valid? | Reason |
|---|---|---|
| `student_name` | Yes | Uses letters and underscore |
| `age2` | Yes | Does not begin with a digit |
| `_count` | Yes | May start with underscore |
| `2age` | No | Begins with a digit |
| `student name` | No | Contains a space |
| `class` | No | Reserved keyword |

## Recommended Naming Style

For ordinary variables, Python commonly uses `snake_case`.

```python
first_name = "Amaan"
total_marks = 250
average_marks = 83.33
```

Avoid confusing names such as `x1`, `a2`, or `z` when a meaningful name is practical.

The dedicated Variable Naming topic will explore these rules further.

# 12. Displaying Variables with `print()` and f-Strings

The `print()` function displays information in the output.

Example:

```python
name = "Amaan"
age = 20

print(name)
print(age)
```

You can display multiple values together:

```python
print("Name:", name, "Age:", age)
```

Output:

```text
Name: Amaan Age: 20
```

## Using f-Strings

An f-string lets you include expressions inside a string using braces.

```python
name = "Amaan"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Amaan and I am 20 years old.
```

### Formatting Decimal Values

```python
price = 35.5

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 35.50
```

The `.2f` format displays the value with two digits after the decimal point. It changes how the number is displayed; it does not convert the variable into a string permanently.

# 13. Variable Tracing and Dry Runs

Variable tracing means following each assignment and recording how the values change.

Consider:

```python
x = 5
x = x + 3
x = x * 2
x = x - 4

print(x)
```

### Trace Table

| Step | Statement | Value of `x` |
|---:|---|---:|
| 1 | `x = 5` | 5 |
| 2 | `x = x + 3` | 8 |
| 3 | `x = x * 2` | 16 |
| 4 | `x = x - 4` | 12 |

Output:

```text
12
```

### Why Is Tracing Useful?

Tracing helps you:

- Understand the order of evaluation.
- Identify unexpected variable updates.
- Debug incorrect calculations.
- Check algorithms before implementing them.
- Understand compound assignment.
- Build confidence with loops and conditions.

When debugging, create a trace table for the variables involved rather than guessing how the program reached its result.

# 14. Practical Applications

Variables are used in nearly every practical program.

## Student Result

```python
marks1 = 75
marks2 = 82
marks3 = 91

total = marks1 + marks2 + marks3
average = total / 3
```

## Shopping Calculation

```python
price = 100
quantity = 4

total_cost = price * quantity
```

## Distance Calculation

```python
speed = 60
time = 2

distance = speed * time
```

The units used in the inputs determine the corresponding units of the output. If speed is measured in kilometres per hour and time is in hours, the resulting distance is in kilometres.

## Balance Update

```python
balance = 1000
deposit = 500
withdrawal = 200

balance += deposit
balance -= withdrawal
```

The final balance is `1300`.

These examples show how descriptive variable names make calculations easier to read and modify.

# 15. Explanation of the 12 Guided Examples

The Python program contains an interactive menu with twelve guided examples.

| No. | Example | Concept |
|---:|---|---|
| 1 | Variable assignment | Creating names and assigning values |
| 2 | Reassign a variable | Updating a variable's value |
| 3 | Variables in calculations | Using names in expressions |
| 4 | Area and perimeter | Applying mathematical formulas |
| 5 | Arithmetic operators | Performing mathematical operations |
| 6 | Compound assignment | Updating variables efficiently |
| 7 | Average of marks | Using variables for multiple values |
| 8 | Temperature conversion | Applying a conversion formula |
| 9 | Update a balance | Tracking a changing value |
| 10 | Counter variable | Using a variable to count repeated actions |
| 11 | Formatted output | Displaying values with f-strings |
| 12 | Variable trace | Tracking changes step by step |

Study each example by predicting its output, running it, and explaining the purpose of its variables.

# 16. Explanation of the 12 Solved Problems

The solved-problems menu demonstrates the practical application of variables.

## 1. Personal Profile

Stores a name, age, and city in separate variables. It illustrates collecting information and displaying a formatted summary.

The example rejects a negative age.

## 2. Sum and Product

Stores two numbers and calculates their sum and product.

Formulas:

```text
Sum = a + b
Product = a * b
```

## 3. Rectangle Area and Perimeter

Uses the length and width variables to calculate two geometric measurements.

```text
Area = length * width
Perimeter = 2 * (length + width)
```

Negative dimensions are rejected by the implementation.

## 4. Simple Interest

Uses principal, annual interest rate, and time in years.

```text
Interest = Principal * Rate * Time / 100
Total Amount = Principal + Interest
```

## 5. Celsius to Fahrenheit

Converts a temperature using:

```text
Fahrenheit = (Celsius * 9 / 5) + 32
```

## 6. Shopping Total

Multiplies the price per item by the quantity.

```text
Total Cost = Price Per Item * Quantity
```

The program checks that price and quantity are non-negative.

## 7. Salary with Bonus

Calculates a bonus from a base salary and a percentage, then adds it to the base salary.

```text
Bonus = Salary * Bonus Percentage / 100
Final Salary = Salary + Bonus
```

## 8. Average of Four Numbers

Calculates the sum of four numbers and divides by four.

```text
Average = Total / 4
```

## 9. Seconds into Minutes and Seconds

Uses integer division and the remainder operator to split a total number of seconds into whole minutes and leftover seconds.

```text
Minutes = Total Seconds // 60
Remaining Seconds = Total Seconds % 60
```

## 10. Distance Calculation

Calculates distance when speed and time are supplied in compatible units.

```text
Distance = Speed * Time
```

With speed in kilometres per hour and time in hours, the result is in kilometres.

## 11. Discount Calculation

Calculates a discount amount and subtracts it from the original price.

```text
Discount = Original Price * Discount Percentage / 100
Final Price = Original Price - Discount
```

The program validates that the discount percentage lies between `0` and `100`.

## 12. Seconds into Hours, Minutes, and Seconds

Separates the total into hours, leftover minutes, and leftover seconds using floor division and modulo.

The program also displays a formatted time representation such as `02:05:09`.

# 17. Five Unsolved Practice Questions

Attempt each problem before searching for a complete solution.

## Question 1: Compound Interest

Read principal, annual interest rate, and number of years. Calculate the final amount using annual compounding.

For an annual rate expressed as a percentage:

```text
Amount = Principal * (1 + Rate / 100) ** Time
```

Make sure your explanation states the assumption of annual compounding and non-negative input values.

## Question 2: Electricity Bill

Read the units consumed and the price per unit. Calculate the bill before additional charges.

```text
Bill = Units Consumed * Price Per Unit
```

For this exercise, use a single fixed rate rather than a multi-slab tariff.

## Question 3: Profit or Loss

Read cost price and selling price. Determine whether the transaction produces a profit, loss, or neither.

```text
Difference = Selling Price - Cost Price
```

If the cost price is positive, calculate the percentage relative to cost price.

## Question 4: Convert Kilometres

Read a non-negative distance in kilometres and convert it into metres and centimetres.

```text
Metres = Kilometres * 1000
Centimetres = Kilometres * 100000
```

## Question 5: Student Percentage

Read marks obtained and maximum possible marks for several subjects. Calculate total marks and percentage after checking that each mark lies in its valid range.

```text
Percentage = Total Marks Obtained / Maximum Total Marks * 100
```

Define how invalid marks or a zero maximum total should be handled.

# 18. Common Errors and Debugging

## Error 1: Using a Variable Before Assignment

```python
print(total)
```

If `total` has not been defined in the current scope, Python raises a `NameError`.

**Solution:** Assign a value before reading the variable.

## Error 2: Confusing `=` and `==`

Use `=` for assignment and `==` to test equality.

## Error 3: Unexpected Reassignment

A later assignment can change what a variable name refers to.

**Solution:** Trace assignments in execution order and choose descriptive variable names.

## Error 4: Using Unclear Names

Names such as `a`, `b`, and `c` are fine for short mathematical examples, but descriptive names often make longer programs easier to understand.

## Error 5: Assuming Values Have the Right Meaning

A variable name does not automatically enforce a unit, range, or semantic rule.

**Solution:** Validate inputs and document the intended meaning of each value.

## Error 6: Incorrect Formula

A program may run successfully but produce the wrong calculation.

**Solution:** Write the formula independently, test it with known values, and compare the expected result with the actual output.

# 19. Best Practices

1. Use meaningful variable names.
2. Follow `snake_case` for ordinary Python variable names.
3. Initialize variables before using them.
4. Make the intended units and meanings clear.
5. Avoid unnecessary reassignment when separate names improve readability.
6. Use constants by convention for values intended to remain fixed.
7. Use f-strings for clear formatted output.
8. Check relevant input constraints.
9. Test calculations with known sample values.
10. Trace unexpected results instead of guessing.
11. Keep each calculation easy to understand.
12. Explain the purpose of important variables.

# 20. Frequently Asked Questions

### Q1. What is a variable?

A variable is a name that refers to an object in Python.

### Q2. How do I create a variable?

Use an assignment statement such as `age = 20`.

### Q3. Can I change the value of a variable?

Yes. Reassigning the name can make it refer to a different object.

### Q4. Is `=` the same as `==`?

No. `=` assigns a value, while `==` checks equality.

### Q5. What happens if I use a variable before defining it?

If the name is not defined in the current scope, Python raises a `NameError`.

### Q6. Can multiple variables have the same value?

Yes. For example, `x = y = z = 0` assigns the value `0` to each name.

### Q7. What is a compound assignment operator?

It combines an operation with assignment, such as `count += 1`.

### Q8. Are uppercase names automatically constants in Python?

No. Uppercase names are a convention used to indicate that a value is intended to remain constant.

### Q9. What is an f-string?

An f-string is a string literal that can contain expressions inside braces, making formatted output easier to write.

### Q10. What should I study next?

Continue with Variable Naming, followed by Multiple Variables and Variable Swapping. Then study Data Types, Type Conversion, and Input-Output in the order defined by your folder structure.

# 21. How to Run the Program

Make sure Python 3 is installed and available in your terminal.

Run the following command from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\01_variable_basics\01_variable_basics.py"
```

The program displays the following main menu:

```text
============================================================
VARIABLE BASICS IN PYTHON
============================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View variable basics checklist
0. Exit
Choose an option:
```

Enter the option number and follow the prompts. Enter an integer or valid numeric value when requested.

The program retries when integer or floating-point input cannot be parsed. Individual exercises also validate their relevant input requirements.

# 22. Folder Structure

This topic contains two files:

```text
01_variable_basics/
│
├── 01_variable_basics.py
└── 01_variable_basics.md
```

**`01_variable_basics.py`** contains the runnable examples, solved problems, unsolved question list, and interactive menu.

**`01_variable_basics.md`** contains the detailed theory, explanations, formulas, practice guidance, run instructions, and revision notes.

# 23. Revision Checklist

Before moving to the next topic, make sure you can:

- [ ] Explain what a variable represents in Python.
- [ ] Create variables using assignment statements.
- [ ] Explain how reassignment changes a variable's binding.
- [ ] Use variables in mathematical expressions.
- [ ] Distinguish `=` from `==`.
- [ ] Use arithmetic and compound assignment operators.
- [ ] Follow naming conventions.
- [ ] Display variables using `print()` and f-strings.
- [ ] Trace variable updates manually.
- [ ] Implement simple formulas with meaningful variable names.
- [ ] Validate relevant inputs.
- [ ] Complete the five unsolved practice questions.

## Completion Goal

You should be able to create and update variables, use them in calculations, produce readable output, and explain how their values change during a program's execution.

**Next topic:** `02_variable_naming` — rules, conventions, keywords, and meaningful variable names.