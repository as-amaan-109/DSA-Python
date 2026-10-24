# Float (`float`) Data Type in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Data Types  
**Topic:** Float (`float`)  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. What Is a Float?
4. Creating Float Variables
5. Integer vs Float
6. Checking Data Types
7. Arithmetic Operations
8. True Division
9. Rounding and Formatting
10. Floating-Point Precision
11. Comparing Floating-Point Values
12. Scientific Notation
13. Compound Assignment
14. Converting Text into a Float
15. Using Floats in Mathematical Formulas
16. Explanation of the 12 Guided Examples
17. Explanation of the 12 Solved Problems
18. Five Unsolved Practice Questions
19. Testing and Edge Cases
20. Time and Space Complexity
21. Common Mistakes
22. Best Practices
23. Frequently Asked Questions
24. How to Run the Program
25. Folder Structure
26. Revision Checklist

---

# 1. Introduction

Python provides the `float` data type for representing floating-point numbers.

Floating-point values are useful when a program needs to work with fractional or decimal quantities, including measurements, averages, percentages, distances, temperatures, and many mathematical calculations.

Examples:

```python
price = 99.50
temperature = 25.75
average_marks = 82.5
distance_km = 12.6
```

Floating-point numbers are different from integers. An integer represents a whole-number value, while a float represents an approximation to a real number using a finite binary representation.

This topic explains how to create float values, perform calculations, format decimal output, understand precision limitations, and solve practical problems.

# 2. Learning Objectives

After completing this topic, you should be able to:

- Explain what a floating-point number is.
- Create and display float variables.
- Distinguish `int` from `float`.
- Check types using `type()`.
- Perform arithmetic using float values.
- Understand the behavior of division.
- Round values and format decimal output.
- Explain why some decimal calculations produce surprising results.
- Compare floating-point values appropriately.
- Recognize scientific notation.
- Convert valid numeric text into a float.
- Apply float values to mathematical formulas.
- Validate inputs and handle division by zero.
- Solve beginner-level calculation problems using floats.
- Test results using suitable sample and boundary inputs.

# 3. What Is a Float?

A float is Python's built-in floating-point type, commonly used for approximate numeric calculations involving fractions.

Examples:

```python
price = 99.50
temperature = -2.5
average = 0.0
distance = 123.456
```

You can inspect its type using:

```python
number = 12.5

print(type(number))
```

Output:

```text
<class 'float'>
```

Python's standard `float` type generally uses double-precision binary floating-point representation.

This means many decimal fractions cannot be represented exactly in binary. The stored value is often the nearest representable floating-point value.

For most beginner calculations, floats are practical and convenient. However, understanding their precision limitations is important when comparing values or working with exact monetary amounts.

# 4. Creating Float Variables

A float variable can be created by assigning a floating-point literal.

```python
price = 49.99
temperature = 36.5
interest_rate = 5.25
```

A value written with a decimal point is ordinarily a float, even if its fractional part is zero.

```python
first_value = 10
second_value = 10.0

print(type(first_value).__name__)
print(type(second_value).__name__)
```

Output:

```text
int
float
```

Although these values compare equal numerically, their types differ.

### Negative Float Values

```python
temperature_change = -2.75
```

Negative floating-point values are useful when representing measurements, changes, or values below zero.

### Zero as a Float

```python
measurement = 0.0
```

The value remains a float.

### Large and Small Values

Floating-point literals may be written in ordinary decimal notation or scientific notation.

```python
large_value = 1.5e6
small_value = 2.5e-4
```

These expressions represent `1500000.0` and `0.00025`, respectively.

# 5. Integer vs Float

Python's integer and floating-point types are different.

| Feature | `int` | `float` |
|---|---|---|
| Typical use | Whole-number values | Approximate fractional values |
| Example | `25` | `25.75` |
| Negative values supported | Yes | Yes |
| Zero representation | `0` | `0.0` |
| True division result | Usually a float | Usually a float |
| Representation | Arbitrary-precision integer, subject to resources | Finite-precision floating point |

Example:

```python
integer_value = 10
float_value = 10.0

print(type(integer_value).__name__)
print(type(float_value).__name__)
print(integer_value == float_value)
```

Output:

```text
int
float
True
```

The comparison returns `True` because the numeric values are equal, even though their types are different.

### When Should You Use Each Type?

Use integers for values such as:

- Counts.
- List indices.
- Number of students.
- Number of attempts.
- Whole-number quantities.

Use floats for values such as:

- Average measurements.
- Temperatures.
- Distances.
- Percentages.
- Fractional rates.
- Mathematical results containing fractions.

The appropriate type depends on what the value represents and what the problem requires.

# 6. Checking Data Types

The built-in `type()` function reports the type of an object.

Example:

```python
price = 99.95
count = 10

print(type(price).__name__)
print(type(count).__name__)
```

Output:

```text
float
int
```

Inspecting types is useful during learning and debugging, especially when a calculation produces a value of an unexpected type.

You can also check whether a value is a float instance with `isinstance()`:

```python
value = 12.5

print(isinstance(value, float))
```

Output:

```text
True
```

For most beginner exercises, `type()` is sufficient to understand the difference between integer and floating-point values.

# 7. Arithmetic Operations

Float values support the standard arithmetic operators.

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10.5 + 2.5` | `13.0` |
| `-` | Subtraction | `10.5 - 2.5` | `8.0` |
| `*` | Multiplication | `10.5 * 2` | `21.0` |
| `/` | Division | `10.0 / 4` | `2.5` |
| `//` | Floor division | `17.0 // 5` | `3.0` |
| `%` | Modulo | `17.0 % 5` | `2.0` |
| `**` | Exponentiation | `2.0 ** 3` | `8.0` |

### Addition

```python
first_number = 12.5
second_number = 7.25

total = first_number + second_number

print(total)
```

Output:

```text
19.75
```

### Multiplication

```python
price_per_item = 35.5
quantity = 4

total_cost = price_per_item * quantity

print(total_cost)
```

Output:

```text
142.0
```

### Exponentiation

```python
radius = 3.0
square = radius ** 2

print(square)
```

Output:

```text
9.0
```

### Important Note

Arithmetic operations can produce results that are not exactly representable as binary floating-point values. This can cause small precision differences, which are discussed later in this README.

# 8. True Division

In Python, the `/` operator performs true division.

Example:

```python
result = 7 / 2

print(result)
print(type(result).__name__)
```

Output:

```text
3.5
float
```

Even if both operands are integers, ordinary true division returns a floating-point result.

Compare:

```python
print(7 / 2)
print(7 // 2)
```

Output:

```text
3.5
3
```

The first expression calculates the quotient as a floating-point result. The second performs floor division, rounding toward negative infinity.

For example:

```python
print(-7 / 2)
print(-7 // 2)
```

Output:

```text
-3.5
-4
```

Use the operator that matches the problem's requirements.

# 9. Rounding and Formatting

Python provides multiple ways to control how a floating-point result is displayed.

It is important to distinguish **rounding a numeric value** from **formatting its presentation**.

## 9.1 The `round()` Function

The `round()` function rounds a number to a specified number of decimal places.

```python
value = 12.34567

print(round(value, 1))
print(round(value, 2))
print(round(value, 3))
```

Typical output:

```text
12.3
12.35
12.346
```

Python's `round()` uses ties-to-even behavior for exact halfway cases. Floating-point representation can affect results for decimal-looking values.

For example:

```python
print(round(2.675, 2))
```

The result is commonly:

```text
2.67
```

This happens because the stored binary floating-point value is not exactly the decimal number `2.675`.

Do not assume that `round()` always behaves like rounding an exact decimal fraction on paper.

## 9.2 Formatting with f-Strings

To display a fixed number of decimal places, use an f-string.

```python
price = 12.5

print(f"{price:.2f}")
```

Output:

```text
12.50
```

More examples:

```python
value = 8.12678

print(f"{value:.1f}")
print(f"{value:.3f}")
print(f"{value:.5f}")
```

Output:

```text
8.1
8.127
8.12678
```

The format specifier controls the displayed number of decimal places.

## 9.3 Formatting Does Not Change the Original Variable

```python
price = 12.5

print(f"{price:.2f}")
print(price)
```

Output:

```text
12.50
12.5
```

The formatted output displays two decimal places, but `price` still refers to the original floating-point value.

### When Should You Use Each Method?

Use `round()` when the rounded numeric result is required for subsequent calculations.

Use formatting when the goal is to display a consistent number of decimal places.

The two operations are related but serve different purposes.

# 10. Floating-Point Precision

One of the most important float concepts is that some decimal fractions cannot be represented exactly in binary floating-point format.

Consider:

```python
first_value = 0.1
second_value = 0.2

result = first_value + second_value

print(result)
```

The displayed result is commonly:

```text
0.30000000000000004
```

This occurs because the binary floating-point representations of `0.1` and `0.2` are approximations.

The issue is not that addition is incorrect. The operands are represented using finite-precision binary values, and the arithmetic result reflects that representation.

## 10.1 Why Does This Matter?

Small precision differences can affect:

- Exact equality comparisons.
- Repeated calculations.
- Accumulated sums.
- Numerical algorithms.
- Rounding and display behavior.

Many ordinary calculations are sufficiently accurate with floats, but the limitations should be understood.

## 10.2 Compare Approximately with `math.isclose()`

For many numeric comparisons, check whether values are sufficiently close instead of requiring exact equality.

```python
import math

first_value = 0.1 + 0.2
second_value = 0.3

print(first_value == second_value)
print(math.isclose(first_value, second_value))
```

Output:

```text
False
True
```

`math.isclose()` compares values using relative and absolute tolerances. Its default tolerances are suitable for many common cases but not all numerical problems.

You should choose an appropriate tolerance for your application.

## 10.3 Absolute Tolerance

An absolute tolerance defines an allowed absolute difference between values.

```python
import math

print(math.isclose(1.000001, 1.0, rel_tol=0.0, abs_tol=0.00001))
```

Output:

```text
True
```

The absolute difference is within the specified tolerance.

## 10.4 Floats and Money

Floats are useful for learning numerical calculations, but they may not be appropriate when exact decimal arithmetic is required for financial amounts.

For production financial calculations, consider Python's `decimal.Decimal` or integer minor units, such as storing currency amounts in paise.

For example, storing `₹125.50` as `12550` paise can avoid binary floating-point representation issues in fixed-precision currency calculations.

The right representation depends on the application's rules for precision, rounding, and currency.

# 11. Scientific Notation

Scientific notation is a compact way to represent very large or very small numbers.

In Python, `e` or `E` indicates a power of ten.

Example:

```python
large_value = 1.5e6
small_value = 2.5e-4

print(large_value)
print(small_value)
```

Output:

```text
1500000.0
0.00025
```

### Explanation

```text
1.5e6 = 1.5 * 10**6
2.5e-4 = 2.5 * 10**(-4)
```

Scientific notation is useful in scientific calculations, measurements, engineering, and numerical applications.

# 12. Compound Assignment

Compound assignment operators update a variable using an operation.

Example:

```python
amount = 10.5

amount += 2.25
print(amount)

amount -= 1.5
print(amount)

amount *= 2
print(amount)

amount /= 3
print(amount)
```

These operations are equivalent in purpose to longer statements such as `amount = amount + 2.25`.

Compound assignment can be useful for updating balances, totals, counters, measurements, and intermediate results.

Remember that repeated float operations can accumulate small precision differences.

# 13. Converting Text into a Float

The `input()` function returns a string. Use `float()` to convert valid numeric text into a floating-point value.

Example:

```python
raw_value = "12.75"
number = float(raw_value)

print(number)
print(type(number).__name__)
```

Output:

```text
12.75
float
```

### Handling Invalid Input

```python
while True:
    raw_value = input("Enter a decimal number: ")

    try:
        number = float(raw_value)
        break
    except ValueError:
        print("Invalid input. Please try again.")

print(f"Value: {number}")
```

Text such as `hello` cannot be converted to a float and raises `ValueError`.

Python's `float()` also recognizes special values such as `nan` and `inf`. If the application requires an ordinary finite number, validate it using `math.isfinite()`.

The Python file provided for this topic includes a helper that rejects non-finite numeric input.

# 14. Using Floats in Mathematical Formulas

Float values are useful for formulas involving measurements and fractional results.

## Rectangle Area

```python
length = 8.5
width = 4.2

area = length * width

print(f"Area: {area:.2f}")
```

Formula:

\[
\text{Area} = \text{length} \times \text{width}
\]

## Circle Area

```python
import math

radius = 3.5
area = math.pi * radius ** 2

print(f"Area: {area:.2f}")
```

Formula:

\[
\text{Area} = \pi r^2
\]

## Simple Interest

```python
principal = 10000.0
annual_rate = 5.0
time_years = 2.0

interest = principal * annual_rate * time_years / 100

print(f"Interest: {interest:.2f}")
```

Formula:

\[
\text{Interest} = \frac{P \times R \times T}{100}
\]

## Temperature Conversion

```python
celsius = 25.0

fahrenheit = (celsius * 9 / 5) + 32

print(f"{fahrenheit:.2f}")
```

Formula:

\[
F = \frac{9}{5}C + 32
\]

These examples demonstrate how variables, formulas, floating-point calculations, and formatted output work together.

# 15. Explanation of the 12 Guided Examples

The Python program contains twelve guided examples.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Float basics | Creating and inspecting floats |
| 2 | Integer vs float | Understanding type differences |
| 3 | Float arithmetic | Performing arithmetic operations |
| 4 | True division | Understanding `/` |
| 5 | Format decimal output | Displaying fixed decimal places |
| 6 | Floating-point precision | Understanding approximate representation |
| 7 | `round()` function | Rounding a numeric value |
| 8 | Convert text to float | Converting and validating input |
| 9 | Compare floats | Using approximate equality |
| 10 | Scientific notation | Representing large and small values |
| 11 | Compound assignment | Updating float variables |
| 12 | Average of values | Combining calculations and formatting |

Run each example and inspect the result. For the precision examples, pay attention to the difference between the stored result and its formatted representation.

# 16. Explanation of the 12 Solved Problems

## Problem 1: Add Two Decimal Numbers

Reads two float values and calculates their sum.

The program formats the displayed result to four decimal places. This formatting does not change the original result variable.

## Problem 2: Average of Three Marks

Reads three marks, validates that each mark is between `0` and `100`, calculates the total, and calculates the average.

The input range is an assumption for this educational example.

## Problem 3: Rectangle Area and Perimeter

Uses length and width to calculate the area and perimeter.

\[
\text{Area} = L \times W
\]

\[
\text{Perimeter} = 2(L + W)
\]

Negative dimensions are rejected.

## Problem 4: Circle Area and Circumference

Uses `math.pi` to calculate the circle's area and circumference.

\[
\text{Area} = \pi r^2
\]

\[
\text{Circumference} = 2\pi r
\]

The program rejects a negative radius.

## Problem 5: Celsius to Fahrenheit

Converts a temperature using:

\[
F = \frac{9}{5}C + 32
\]

Negative Celsius values are permitted.

## Problem 6: Simple Interest

Calculates the interest and final amount from a principal, annual rate, and time in years.

The example requires non-negative inputs.

## Problem 7: Discount and Final Price

Calculates a discount amount and subtracts it from the original price.

The percentage is constrained to the range from `0` through `100`.

## Problem 8: Travel Distance

Calculates distance when speed is in kilometres per hour and time is in hours.

\[
\text{Distance} = \text{Speed} \times \text{Time}
\]

The program rejects negative speed and time values.

## Problem 9: Body Mass Index

Calculates BMI from weight in kilograms and height in metres.

\[
\text{BMI} = \frac{\text{weight in kg}}{(\text{height in metres})^2}
\]

Height must be greater than zero. The result is a programming example, not a medical assessment.

## Problem 10: Round a Decimal

Reads a float and a requested number of decimal places, then displays the rounded result.

The example limits the number of places to a range from `0` through `10`.

It demonstrates the distinction between a numeric result and its formatted display.

## Problem 11: Approximate Float Comparison

Compares two float values using `math.isclose()` with a user-specified absolute tolerance.

The tolerance cannot be negative. The example sets relative tolerance to zero so the comparison is controlled by the supplied absolute tolerance.

## Problem 12: Weighted Average

Calculates a weighted average using three scores and their associated weights.

\[
\text{Weighted Average}
=
\frac{\sum (\text{score} \times \text{weight})}
{\sum \text{weights}}
\]

Negative weights are rejected, and the sum of the weights must be greater than zero.

# 17. Five Unsolved Practice Questions

Attempt these independently before consulting a complete solution.

## Question 1: Compound Interest

Read the principal, annual interest rate, and time in years. Calculate the final amount using annual compounding.

Formula:

\[
A = P\left(1 + \frac{R}{100}\right)^T
\]

State your assumptions and validate the inputs.

## Question 2: Kilometres per Litre

Read distance travelled in kilometres and fuel used in litres. Calculate fuel efficiency.

Formula:

\[
\text{Efficiency} = \frac{\text{Distance in km}}{\text{Fuel in litres}}
\]

The fuel amount must be greater than zero.

## Question 3: Percentage Change

Read an original value and a new value. Calculate the percentage change.

Formula:

\[
\text{Percentage Change}
=
\frac{\text{New Value} - \text{Original Value}}
{\text{Original Value}} \times 100
\]

Define how your program handles an original value of zero.

## Question 4: Average Speed

Read distance in kilometres and travel time in hours. Calculate the average speed.

Formula:

\[
\text{Average Speed} = \frac{\text{Distance}}{\text{Time}}
\]

The time must be greater than zero.

## Question 5: Circle Sector Area

Read the circle's radius and a central angle in degrees. Calculate the sector area.

Formula:

\[
\text{Sector Area}
=
\frac{\pi r^2 \times \text{angle}}{360}
\]

Define the accepted angle range and validate the inputs.

### Practice Method

For each question:

1. Identify input and output.
2. Write the formula before coding.
3. Decide the allowed input range.
4. Implement the calculation using floats.
5. Format the output as required.
6. Test normal and boundary inputs.

# 18. Testing and Edge Cases

Floating-point programs should be tested with inputs chosen to verify the formula and the program's constraints.

| Problem | Suggested tests |
|---|---|
| Addition | Positive values, negative values, zero |
| Average | All equal values, mixed values, boundary marks |
| Rectangle | Zero length, zero width, positive dimensions, negative input |
| Circle | Zero radius, positive radius, negative input |
| Temperature | Zero Celsius, positive and negative Celsius |
| Simple interest | Zero time, zero rate, positive inputs |
| Discount | `0%`, `100%`, invalid percentage |
| Travel distance | Zero speed, zero time, positive inputs |
| BMI | Positive weight, zero height, invalid negative input |
| Rounding | Values requiring rounding up and down, several place counts |
| Approximate comparison | Equal values, small difference, negative tolerance |
| Weighted average | Zero weights, negative weight, mixed positive weights |

### Precision Testing

For values that should be approximately equal, use a suitable tolerance.

Do not assume that every arithmetic result has an exact decimal representation, and do not choose a tolerance without considering the scale and requirements of the problem.

# 19. Time and Space Complexity

For the fixed-size calculations in these exercises, the number of arithmetic operations is generally constant relative to the input values.

| Operation | Typical complexity model |
|---|---|
| Add two floating-point values | `O(1)` |
| Calculate a rectangle area | `O(1)` |
| Convert Celsius to Fahrenheit | `O(1)` |
| Calculate BMI | `O(1)` |
| Compare two floats | `O(1)` |
| Calculate a weighted average from three scores | `O(1)` |

In this table, `O(1)` describes a fixed number of arithmetic operations in a simplified operation-count model.

Actual floating-point execution costs depend on the implementation and platform. This distinction is usually not important for beginner exercises but may matter in advanced numerical computing.

# 20. Common Mistakes

## Mistake 1: Expecting Exact Decimal Results

Floating-point values are stored as finite-precision binary representations, so some decimal fractions are approximations.

**Solution:** Understand the precision limitations and compare approximate values using appropriate tolerances.

## Mistake 2: Confusing `round()` with Formatting

`round()` returns a rounded numeric value, while formatting determines how the value is displayed.

**Solution:** Use the operation that matches the requirement.

## Mistake 3: Assuming `int()` Rounds a Float

Converting a float with `int()` truncates its fractional part toward zero.

**Solution:** Use `round()` when rounding is intended, and use `int()` when truncation is intended.

## Mistake 4: Dividing by Zero

A calculation such as average speed or BMI may use a denominator that must be greater than zero.

**Solution:** Validate the denominator before calculation.

## Mistake 5: Using Floats for Exact Currency Calculations Without Considering Precision

Binary floating-point values may not represent all decimal currency amounts exactly.

**Solution:** For applications requiring exact decimal arithmetic, consider `decimal.Decimal` or integer minor units.

## Mistake 6: Treating Formatting as a Change to the Original Value

Printing `f"{price:.2f}"` does not permanently alter `price`.

**Solution:** If the rounded value itself is required, explicitly assign the result of `round()`.

# 21. Best Practices

1. Use floats when approximate fractional arithmetic is appropriate.
2. Distinguish integer values from floating-point values.
3. Use `type()` to inspect values while learning.
4. Understand the difference between `/` and `//`.
5. Use f-string formatting for readable decimal output.
6. Understand the limitations of binary floating-point representation.
7. Use `math.isclose()` where approximate comparison is appropriate.
8. Validate denominators and other important constraints.
9. Reject non-finite values when the application requires finite inputs.
10. Avoid relying on exact float equality for approximate calculations.
11. Choose appropriate rounding and tolerance rules.
12. Consider decimal or integer-based representations for exact currency calculations.
13. Test boundary inputs and inspect unexpected results carefully.

# 22. Frequently Asked Questions

### Q1. What is a float in Python?

A float is a built-in floating-point type commonly used to represent approximate fractional numeric values.

### Q2. What is the difference between `10` and `10.0`?

`10` is an integer, while `10.0` is a float. They compare equal numerically but have different types.

### Q3. What does `type()` do?

It returns the type of an object, such as `int` or `float`.

### Q4. Why can `0.1 + 0.2` produce an unexpected result?

Many decimal fractions cannot be represented exactly in binary floating-point format. The arithmetic result reflects these approximations.

### Q5. What is the difference between `round()` and formatting?

`round()` returns a rounded numeric value. Formatting controls the displayed representation of the value.

### Q6. What does `math.isclose()` do?

It checks whether two numeric values are sufficiently close under relative and absolute tolerances.

### Q7. Can a float represent a very large or small value?

Yes, within the range and precision supported by the floating-point format. Values beyond that range may overflow or underflow.

### Q8. How do I convert text to a float?

Use `float(text)` when the text represents a valid float. Invalid text raises `ValueError`.

### Q9. Should floats be used for money?

Floats are useful for educational examples, but exact financial applications often use `decimal.Decimal` or integer minor units to control representation and rounding.

### Q10. What should I learn next?

Continue with `03_string`, which introduces the string data type, text operations, indexing, slicing, and string methods.

# 23. How to Run the Program

Run the following command from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\02_float\02_float.py"
```

The main menu contains:

```text
=================================================================
FLOAT DATA TYPE IN PYTHON
=================================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View float checklist
0. Exit
Choose an option:
```

Select an option and follow the prompts. The program retries invalid integer or float input where the helper functions are used. Calculations that need specific input ranges validate those conditions separately.

# 24. Folder Structure

```text
02_float/
│
├── 02_float.py
└── README.md
```

**`02_float.py`** contains twelve guided examples, twelve solved problems, five unsolved questions, a checklist, and interactive menus.

**`README.md`** contains the theory, syntax examples, mathematical formulas, precision discussion, problem explanations, testing guidance, and revision notes.

# 25. Revision Checklist

Before moving to the next data type, make sure you can:

- [ ] Explain what a float represents.
- [ ] Distinguish `int` from `float`.
- [ ] Check types with `type()`.
- [ ] Perform arithmetic using float values.
- [ ] Understand true division.
- [ ] Round values using `round()`.
- [ ] Format a fixed number of decimal places.
- [ ] Explain why some decimal fractions are approximations.
- [ ] Compare float values using a suitable tolerance.
- [ ] Recognize scientific notation.
- [ ] Convert valid text using `float()`.
- [ ] Apply floats to common mathematical formulas.
- [ ] Validate inputs and denominators.
- [ ] Understand why exact currency calculations need care.
- [ ] Attempt all five unsolved questions.

## Completion Goal

By completing this topic, you should be able to create float variables, perform decimal calculations, format outputs, explain floating-point precision, and implement common mathematical formulas in Python.

**Next topic:** `03_string` — string creation, text operations, indexing, slicing, formatting, and common string methods.