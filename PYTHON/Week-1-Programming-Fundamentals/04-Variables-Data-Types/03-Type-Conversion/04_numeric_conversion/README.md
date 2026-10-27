# Numeric Conversion in Python

> **Topic:** Numeric Conversion  
> **Module:** Python Programming Fundamentals  
> **Level:** Beginner  
> **Focus:** Integers, floating-point numbers, complex numbers, rounding, arithmetic operations, and safe numeric input

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. Numeric Data Types in Python
4. What Is Numeric Conversion?
5. Integer to Float Conversion
6. Float to Integer Conversion
7. Rounding Numbers Using `round()`
8. Integer and Float to Complex Conversion
9. Converting Numeric Strings
10. Normal Division, Floor Division, and Modulo
11. Comparing Integer and Float Values
12. Floating-Point Precision
13. Validating Numeric Input
14. Conversion vs. Validation
15. Twelve Examples Explained
16. Twelve Solved Problems Explained
17. Ten Unsolved Practice Questions
18. Common Mistakes
19. Viva and Interview Questions
20. Quick Revision Table
21. Learning Checklist
22. Final Summary

---

## 1. Introduction

Numeric conversion is the process of converting a numeric value from one data type into another supported data type.

Python provides three important numeric data types:

- `int` — represents integers.
- `float` — represents floating-point numbers.
- `complex` — represents complex numbers.

Numeric conversion is used in mathematical calculations, scientific programming, measurement systems, temperature conversion, percentage calculations, data processing, and user-input handling.

For example, consider an integer value:

```python
number = 10

converted_number = float(number)

print(converted_number)
print(type(converted_number))
```

**Output:**

```text
10.0
<class 'float'>
```

The integer `10` is converted into the floating-point value `10.0`.

Although both values represent the same numerical quantity, their data types are different.

Numeric conversion is particularly important when a program receives data as text but needs to perform calculations using numbers.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

- Explain the difference between `int`, `float`, and `complex`.
- Convert an integer into a floating-point number.
- Convert a floating-point number into an integer.
- Explain truncation and rounding.
- Use the `round()` function correctly.
- Convert integers and floats into complex numbers.
- Convert valid numeric strings using `int()`, `float()`, and `complex()`.
- Understand normal division, floor division, and modulo.
- Compare integer and floating-point values.
- Understand floating-point precision issues.
- Handle invalid numeric input using exception handling.
- Validate numeric values before using them in calculations.
- Write menu-driven numeric conversion programs.

---

## 3. Numeric Data Types in Python

Python supports different numeric types for representing different kinds of numbers.

### 3.1 Integer — `int`

An integer is a whole number without a fractional part.

Integers can be positive, negative, or zero.

**Examples:**

```python
age = 22
temperature = -5
quantity = 100
zero = 0

print(age)
print(temperature)
print(quantity)
print(zero)
```

**Output:**

```text
22
-5
100
0
```

To check the data type, use `type()`:

```python
number = 25

print(type(number))
```

**Output:**

```text
<class 'int'>
```

Python integers support arbitrary precision, subject to available memory.

### 3.2 Floating-Point Number — `float`

A floating-point number represents a number that may contain a fractional component.

**Examples:**

```python
price = 99.50
height = 5.8
percentage = 87.25

print(price)
print(height)
print(percentage)
```

**Output:**

```text
99.5
5.8
87.25
```

The value `99.50` is displayed as `99.5` because trailing zeros after the decimal point are not normally displayed when printing a float.

Check the data type:

```python
number = 12.5

print(type(number))
```

**Output:**

```text
<class 'float'>
```

Floating-point numbers are useful for calculations involving measurements, averages, ratios, and fractional quantities.

However, most decimal fractions cannot be represented exactly using binary floating-point arithmetic. This topic is explained later.

### 3.3 Complex Number — `complex`

A complex number has a real component and an imaginary component.

Python uses the letter `j` to represent the imaginary unit.

**Example:**

```python
number = 3 + 4j

print(number)
print(number.real)
print(number.imag)
print(type(number))
```

**Output:**

```text
(3+4j)
3.0
4.0
<class 'complex'>
```

Here:

- Real component = `3.0`
- Imaginary component = `4.0`

You can also create a complex number with the `complex()` function:

```python
number = complex(3, 4)

print(number)
```

**Output:**

```text
(3+4j)
```

### Comparison of Numeric Data Types

| Property | `int` | `float` | `complex` |
|---|---|---|---|
| Represents | Whole numbers | Floating-point numbers | Real and imaginary components |
| Example | `10` | `10.5` | `3+4j` |
| Fractional component | No | Yes | Possible in both components |
| Supports arithmetic | Yes | Yes | Yes |
| Directly accepted by `int()` | Already an integer | Yes, with truncation | No |
| Directly accepted by `float()` | Yes | Already a float | No |

---

## 4. What Is Numeric Conversion?

Numeric conversion changes a value from one supported numeric type into another.

Python provides several built-in functions for this purpose.

| Function | Purpose | Example | Result |
|---|---|---|---|
| `int()` | Converts a compatible value into an integer | `int(5.8)` | `5` |
| `float()` | Converts a compatible value into a float | `float(5)` | `5.0` |
| `complex()` | Creates a complex number | `complex(5)` | `(5+0j)` |
| `round()` | Rounds a numeric value | `round(5.7)` | `6` |
| `type()` | Identifies a value's type | `type(5.0)` | `float` |

### Example: Converting One Value into Different Numeric Types

```python
number = 10

integer_value = int(number)
float_value = float(number)
complex_value = complex(number)

print(integer_value)
print(float_value)
print(complex_value)
```

**Output:**

```text
10
10.0
(10+0j)
```

### Important Distinction

`int()`, `float()`, and `complex()` perform conversions, while `round()` applies rounding rules.

Rounding does not mean the same thing as converting a float to an integer.

```python
number = 8.7

print(int(number))
print(round(number))
```

**Output:**

```text
8
9
```

The first operation truncates the fraction. The second rounds the number.

---

## 5. Integer to Float Conversion

The `float()` function converts an integer into a floating-point number.

### Syntax

```python
float(value)
```

### Example 1: Basic Conversion

```python
number = 25

result = float(number)

print("Original value:", number)
print("Converted value:", result)
print("Original type:", type(number).__name__)
print("Converted type:", type(result).__name__)
```

**Output:**

```text
Original value: 25
Converted value: 25.0
Original type: int
Converted type: float
```

### Example 2: Positive, Negative, and Zero Values

```python
print(float(10))
print(float(-5))
print(float(0))
```

**Output:**

```text
10.0
-5.0
0.0
```

### Explanation

When an integer is converted into a float:

1. Python receives the integer.
2. `float()` creates a floating-point representation.
3. The resulting value has the `float` data type.
4. The original variable is not changed unless you assign a new value to it.

### When Is Integer-to-Float Conversion Useful?

It is useful when:

- Calculating averages.
- Performing division that requires a fractional result.
- Working with measurements.
- Calculating percentages and ratios.
- Preparing numeric values for operations that use floating-point arithmetic.

---

## 6. Float to Integer Conversion

The `int()` function converts a floating-point value into an integer.

However, it **truncates the fractional part toward zero**. It does not round the value to the nearest integer.

### Syntax

```python
int(value)
```

### Example 1: Positive Float

```python
number = 12.9

result = int(number)

print(result)
```

**Output:**

```text
12
```

The fractional part `.9` is removed.

### Example 2: Different Positive Values

```python
print(int(8.7))
print(int(8.2))
print(int(8.9))
```

**Output:**

```text
8
8
8
```

Each value is truncated toward zero.

### Example 3: Negative Float

```python
print(int(-8.7))
print(int(-8.2))
print(int(-8.9))
```

**Output:**

```text
-8
-8
-8
```

For negative numbers, truncation still moves toward zero.

### Difference Between Truncation and Rounding

| Original value | `int(value)` | `round(value)` |
|---:|---:|---:|
| `8.2` | `8` | `8` |
| `8.7` | `8` | `9` |
| `12.9` | `12` | `13` |
| `-8.7` | `-8` | `-9` |

The exact halfway cases for `round()` follow Python's ties-to-even rounding rules, which are explained in the next section.

### Important Warning

Do not use `int()` when your objective is to round a number unless truncation is actually intended.

For example, in a calculation where `8.7` should become `9`, `int(8.7)` would produce the wrong result for that requirement.

---

## 7. Rounding Numbers Using `round()`

Python provides the built-in `round()` function to round numeric values.

### Syntax

```python
round(number)
```

To specify decimal places:

```python
round(number, ndigits)
```

Here, `ndigits` specifies the number of decimal places to round to.

### Example 1: Round to an Integer

```python
print(round(4.2))
print(round(4.8))
```

**Output:**

```text
4
5
```

### Example 2: Round to Two Decimal Places

```python
number = 12.3456

result = round(number, 2)

print(result)
```

**Output:**

```text
12.35
```

### Example 3: Round to Three Decimal Places

```python
number = 3.141592

result = round(number, 3)

print(result)
```

**Output:**

```text
3.142
```

### Python's Ties-to-Even Rounding

Python uses ties-to-even rounding for exact halfway cases.

This means that when a number is exactly halfway between two integers, the even integer is selected.

```python
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))
```

**Output:**

```text
2
4
4
6
```

### Why Does `round(2.5)` Return `2`?

The value `2.5` is exactly halfway between `2` and `3`.

Since `2` is even, Python selects `2`.

Similarly, `3.5` is halfway between `3` and `4`. Since `4` is even, Python selects `4`.

### Rounding vs. Formatting

Rounding a value and displaying it with a fixed number of decimal places are related but different tasks.

```python
number = 12.5

print(round(number, 2))
print(f"{number:.2f}")
```

**Output:**

```text
12.5
12.50
```

The first expression produces a rounded numeric value. The second produces a formatted string with exactly two digits after the decimal point.

For example:

```python
number = 7.5

formatted_value = f"{number:.2f}"

print(formatted_value)
print(type(formatted_value).__name__)
```

**Output:**

```text
7.50
str
```

Remember:

- Use `round()` when you need a rounded numeric value.
- Use an f-string format specifier when you need a particular display format.
- Formatting does not change the original numeric variable.

---

## 8. Integer and Float to Complex Conversion

The `complex()` function creates a complex number.

### 8.1 Integer to Complex

```python
number = 10

result = complex(number)

print(result)
print(type(result).__name__)
```

**Output:**

```text
(10+0j)
complex
```

The integer becomes the real component. The imaginary component is zero.

### 8.2 Float to Complex

```python
number = 7.5

result = complex(number)

print(result)
```

**Output:**

```text
(7.5+0j)
```

The floating-point value becomes the real component.

### 8.3 Creating a Complex Number Using Two Arguments

The `complex()` function can also accept separate real and imaginary components.

```python
number = complex(3, 4)

print(number)
print(number.real)
print(number.imag)
```

**Output:**

```text
(3+4j)
3.0
4.0
```

### 8.4 Accessing Complex Components

The `.real` and `.imag` attributes return the real and imaginary components.

```python
number = 5 + 2j

real_part = number.real
imaginary_part = number.imag

print("Real part:", real_part)
print("Imaginary part:", imaginary_part)
```

**Output:**

```text
Real part: 5.0
Imaginary part: 2.0
```

### Important Limitation

Python does not allow a complex number to be converted directly into an integer or float.

For example:

```python
number = 3 + 4j

# int(number)    # Raises TypeError
# float(number)  # Raises TypeError
```

If the real component is required, select it explicitly:

```python
number = 3 + 4j

real_value = float(number.real)

print(real_value)
```

**Output:**

```text
3.0
```

Selecting the real component discards the imaginary component. Do this only when it is appropriate for the problem.

---

## 9. Converting Numeric Strings

Numeric data frequently arrives as text.

For example, `input()` returns a string even when the user enters digits.

```python
text = input("Enter a number: ")

print(text)
print(type(text))
```

If the user enters `25`, the output is:

```text
25
<class 'str'>
```

To perform numeric calculations, convert the text into the appropriate type.

### 9.1 String to Integer

```python
text = "25"

number = int(text)

print(number)
print(type(number).__name__)
```

**Output:**

```text
25
int
```

### 9.2 String to Float

```python
text = "12.75"

number = float(text)

print(number)
print(type(number).__name__)
```

**Output:**

```text
12.75
float
```

### 9.3 String to Complex

```python
text = "3+4j"

number = complex(text)

print(number)
print(type(number).__name__)
```

**Output:**

```text
(3+4j)
complex
```

### 9.4 Invalid Integer Text

```python
text = "12.5"

try:
    number = int(text)
    print(number)
except ValueError:
    print("Invalid integer text.")
```

**Output:**

```text
Invalid integer text.
```

The string `"12.5"` is not accepted by `int()` because it contains a decimal point.

If a floating-point value is intended, use:

```python
number = float("12.5")
print(number)
```

**Output:**

```text
12.5
```

### Quick Comparison

| Input text | `int()` | `float()` | `complex()` |
|---|---|---|---|
| `"10"` | `10` | `10.0` | `(10+0j)` |
| `"10.5"` | Raises `ValueError` | `10.5` | `(10.5+0j)` |
| `"3+4j"` | Raises `ValueError` | Raises `ValueError` | `(3+4j)` |
| `"hello"` | Raises `ValueError` | Raises `ValueError` | Raises `ValueError` |

Invalid conversions should be handled rather than allowed to terminate a program unexpectedly.

---

## 10. Normal Division, Floor Division, and Modulo

These arithmetic operations are essential when working with numeric data.

### 10.1 Normal Division — `/`

Normal division calculates the quotient.

```python
print(17 / 5)
```

**Output:**

```text
3.4
```

For integer operands, normal division returns a floating-point result.

### 10.2 Floor Division — `//`

Floor division rounds the quotient down toward negative infinity.

```python
print(17 // 5)
print(-17 // 5)
```

**Output:**

```text
3
-4
```

For negative values, floor division does not behave like truncation toward zero.

This is an important distinction between `//` and `int()`.

### 10.3 Modulo — `%`

The modulo operator returns the remainder according to Python's division rules.

```python
print(17 % 5)
print(-17 % 5)
```

**Output:**

```text
2
3
```

### 10.4 Mathematical Relationship

For a nonzero divisor, Python's floor division and modulo operators satisfy:

`a == (a // b) * b + (a % b)`

For example:

```python
a = 17
b = 5

quotient = a // b
remainder = a % b

print(a == quotient * b + remainder)
```

**Output:**

```text
True
```

### 10.5 Practical Example: Convert Seconds

Suppose a total number of seconds must be converted into hours, minutes, and remaining seconds.

```python
total_seconds = 3671

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
```

**Output:**

```text
Hours: 1
Minutes: 1
Seconds: 11
```

Floor division calculates the whole units, while modulo calculates the remainder.

**Important:** Division and modulo operations involving a zero divisor raise `ZeroDivisionError`.

---

## 11. Comparing Integer and Float Values

An integer and a float can have different data types but still represent the same numerical value.

```python
integer_value = 5
float_value = 5.0

print(integer_value == float_value)
print(type(integer_value).__name__)
print(type(float_value).__name__)
```

**Output:**

```text
True
int
float
```

The comparison returns `True` because the values are numerically equal.

However, their types remain different.

### Comparing Values and Types

```python
integer_value = 10
float_value = 10.0

print(integer_value == float_value)
print(type(integer_value) == type(float_value))
```

**Output:**

```text
True
False
```

The first comparison checks numeric equality.

The second checks whether both objects have the same type.

### When Is This Important?

Understanding this distinction is useful when:

- Comparing calculated results.
- Checking input types.
- Debugging numeric programs.
- Writing validation rules.
- Working with data that contains both integers and floats.

---

## 12. Floating-Point Precision

Floating-point numbers are represented using binary floating-point arithmetic. Many decimal fractions cannot be represented exactly in this format.

Consider this expression:

```python
print(0.1 + 0.2)
```

**Typical output:**

```text
0.30000000000000004
```

The result is close to `0.3`, but it is not exactly equal to the decimal value represented by `0.3` as a float.

This behavior arises from floating-point representation, not from a mistake in the addition operator.

### 12.1 Exact Equality Can Be Misleading

```python
result = 0.1 + 0.2

print(result == 0.3)
```

**Output:**

```text
False
```

A direct equality comparison may fail when the values differ by a tiny floating-point amount.

### 12.2 Use `math.isclose()` for Approximate Comparisons

Python provides `math.isclose()` for checking whether two numbers are sufficiently close.

```python
import math

result = 0.1 + 0.2

print(math.isclose(result, 0.3))
```

**Output:**

```text
True
```

For calculations that require a particular tolerance, pass suitable relative and absolute tolerances.

```python
import math

first = 0.1 + 0.2
second = 0.3

print(math.isclose(first, second, rel_tol=1e-9, abs_tol=0.0))
```

**Output:**

```text
True
```

Tolerance values should be chosen according to the requirements of the application.

### 12.3 When Is Floating-Point Precision Important?

It is important in:

- Scientific computations.
- Geometry and measurements.
- Simulation programs.
- Comparisons involving calculated decimals.
- Financial calculations, where an appropriate decimal arithmetic strategy may be needed.

---

## 13. Validating Numeric Input

Numeric conversion can fail when the supplied text is invalid.

For example:

```python
number = int("hello")
```

This raises a `ValueError` because the text cannot be interpreted as an integer.

Python provides `try` and `except` to handle expected errors.

### 13.1 Safe Integer Conversion

```python
text = input("Enter an integer: ")

try:
    number = int(text)
    print("Converted value:", number)

except ValueError:
    print("Invalid input. Enter a whole number.")
```

**Sample output for valid input:**

```text
Enter an integer: 25
Converted value: 25
```

**Sample output for invalid input:**

```text
Enter an integer: hello
Invalid input. Enter a whole number.
```

### 13.2 Safe Float Conversion

```python
import math

text = input("Enter a number: ")

try:
    number = float(text)

    if math.isfinite(number):
        print("Converted value:", number)
    else:
        print("The number must be finite.")

except ValueError:
    print("Invalid numeric input.")
```

This example checks two different conditions:

1. Whether the text can be converted into a float.
2. Whether the resulting float is finite.

### 13.3 Why Check `math.isfinite()`?

Python can successfully convert strings such as `"inf"` and `"nan"` into floating-point special values.

A successful conversion does not necessarily mean the result is an ordinary finite number.

`math.isfinite(value)` returns `True` for finite numeric values and `False` for infinity or NaN.

The check is useful when the program requires finite quantities.

---

## 14. Conversion vs. Validation

Conversion and validation are separate processes.

**Conversion** determines whether a value can be represented in the requested data type.

**Validation** checks whether the converted value satisfies the application's requirements.

Consider a program that accepts a positive quantity.

```python
number = int("-10")

print(number)
```

**Output:**

```text
-10
```

The conversion succeeds because `"-10"` is valid integer text.

However, the result may violate the program's requirement that the quantity must be positive.

### Example: Validate a Positive Integer

```python
text = input("Enter a positive integer: ")

try:
    number = int(text)

    if number <= 0:
        print("The number must be positive.")
    else:
        print("Accepted quantity:", number)

except ValueError:
    print("Please enter a valid integer.")
```

Here, conversion and validation perform different jobs.

- `int(text)` converts the input.
- `number <= 0` checks the application's rule.
- `except ValueError` handles invalid integer text.

This distinction is important in reliable programming.

---

## 15. Twelve Examples Explained

The Python program provides twelve numeric conversion examples.

| No. | Example | Concept Demonstrated |
|---:|---|---|
| 1 | Integer to float | Using `float()` |
| 2 | Float to integer | Truncation toward zero |
| 3 | Integer to complex | Using `complex()` |
| 4 | Float to complex | Converting floating-point values |
| 5 | Numeric text to integer | Using `int()` on strings |
| 6 | Numeric text to float | Using `float()` on strings |
| 7 | Truncation vs. rounding | Comparing `int()` and `round()` |
| 8 | Normal vs. floor division | Comparing `/` and `//` |
| 9 | Modulo operation | Calculating remainders using `%` |
| 10 | Integer and float comparison | Numerical equality vs. type equality |
| 11 | Complex components | Accessing `.real` and `.imag` |
| 12 | Safe numeric conversion | Exception handling and finite-number validation |

### What to Learn from These Examples

For each example, focus on the following:

1. What is the original value?
2. What is its original data type?
3. Which conversion or arithmetic operation is used?
4. What is the resulting value?
5. What is the resulting data type?
6. Can the operation fail for some inputs?
7. Is additional validation required?

Answering these questions helps you understand the code instead of memorizing it.

---

## 16. Twelve Solved Programming Problems Explained

The Python program contains twelve solved problems that can be selected from the interactive menu.

### Problem 1: Integer to Float

**Objective:** Convert an integer into a floating-point number.

**Main concept:** `float()`.

**Example:**

```python
number = 25
result = float(number)

print(result)
```

**Output:**

```text
25.0
```

### Problem 2: Float to Integer

**Objective:** Convert a decimal value into an integer.

**Main concept:** `int()` and truncation toward zero.

**Example:**

```python
number = 15.8

print(int(number))
```

**Output:**

```text
15
```

### Problem 3: Round a Number

**Objective:** Round a decimal value to the nearest integer according to Python's rounding rules.

**Main concept:** `round()`.

```python
number = 8.7

print(round(number))
```

**Output:**

```text
9
```

### Problem 4: Round to Two Decimal Places

**Objective:** Round a number and display two decimal places.

**Main concepts:** `round()` and formatted strings.

```python
number = 12.3456

result = round(number, 2)

print(result)
print(f"{result:.2f}")
```

**Output:**

```text
12.35
12.35
```

### Problem 5: Text to Integer

**Objective:** Convert numeric text into an integer and handle invalid input.

**Main concepts:** `int()` and `ValueError`.

```python
text = "250"

try:
    number = int(text)
    print(number)
except ValueError:
    print("Invalid integer text.")
```

**Output:**

```text
250
```

### Problem 6: Text to Float

**Objective:** Convert numeric text into a finite floating-point number.

**Main concepts:** `float()`, `math.isfinite()`, and exception handling.

```python
import math

text = "45.5"

try:
    number = float(text)

    if math.isfinite(number):
        print(number)
    else:
        print("The number must be finite.")

except ValueError:
    print("Invalid numeric text.")
```

**Output:**

```text
45.5
```

### Problem 7: Convert Seconds

**Objective:** Convert total seconds into hours, minutes, and seconds.

**Main concepts:** Floor division and modulo.

```python
total_seconds = 3671

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)
```

**Output:**

```text
1 1 11
```

### Problem 8: Calculate the Average

**Objective:** Calculate the average of three numbers.

**Formula:**

`Average = (First number + Second number + Third number) / 3`

```python
first = 10
second = 20
third = 30

average = (first + second + third) / 3

print(average)
```

**Output:**

```text
20.0
```

### Problem 9: Celsius to Fahrenheit

**Objective:** Convert a temperature from Celsius to Fahrenheit.

**Formula:**

`Fahrenheit = (Celsius * 9 / 5) + 32`

```python
celsius = 25

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)
```

**Output:**

```text
77.0
```

### Problem 10: Area of a Rectangle

**Objective:** Calculate the area using length and width.

**Formula:**

`Area = Length * Width`

```python
length = 10
width = 5

area = length * width

print(area)
```

**Output:**

```text
50
```

### Problem 11: Compare an Integer and a Float

**Objective:** Compare two numeric values and display their types.

```python
integer_value = 5
float_value = 5.0

print(integer_value == float_value)
print(type(integer_value).__name__)
print(type(float_value).__name__)
```

**Output:**

```text
True
int
float
```

### Problem 12: Numeric Converter

**Objective:** Build a converter that accepts numeric text and converts it into an integer, float, or complex number.

**Main concepts:**

- Menu-driven programming.
- `int()`, `float()`, and `complex()`.
- Input validation.
- Error handling.
- Type inspection with `type()`.

The interactive solution lets the user select a conversion type and handles invalid inputs.

### Recommended Practice Method

For all twelve problems:

1. Read the objective.
2. Write down the expected input and output.
3. Predict the result before executing the program.
4. Run the solution.
5. Test an invalid input where applicable.
6. Rewrite the solution without looking at the existing code.

---

## 17. Ten Unsolved Practice Questions

Attempt these questions independently before referring to the solved problems.

### Question 1: Integer to Float

Accept an integer from the user, convert it into a float, and display the original and converted values with their data types.

**Example:**

```text
Enter an integer: 25
Original value: 25
Converted value: 25.0
```

### Question 2: Float to Integer

Accept a decimal number and convert it into an integer.

Display both values and explain why the fractional part disappears.

### Question 3: Three Decimal Places

Accept a floating-point number and display it with exactly three digits after the decimal point.

**Example:**

```text
Enter a number: 12.34567
Formatted value: 12.346
```

### Question 4: Numeric Text to Integer

Accept numeric text, convert it into an integer, and handle invalid input with an appropriate error message.

Test both `"125"` and `"hello"`.

### Question 5: Numeric Text to Float

Accept numeric text and convert it into a finite float.

Reject invalid text, NaN, and infinity.

### Question 6: Convert Minutes

Accept the total number of minutes and convert them into hours and remaining minutes.

**Example:**

```text
Enter total minutes: 135
Hours: 2
Minutes: 15
```

### Question 7: Average of Five Numbers

Accept five numeric values and calculate their average.

Make sure the program handles invalid numeric input.

### Question 8: Fahrenheit to Celsius

Accept a temperature in Fahrenheit and convert it into Celsius.

**Formula:**

`Celsius = (Fahrenheit - 32) * 5 / 9`

### Question 9: Circle Calculations

Accept the radius of a circle and calculate its area and circumference.

**Formulas:**

`Area = pi * radius * radius`

`Circumference = 2 * pi * radius`

Reject negative radii.

### Question 10: Menu-Driven Numeric Converter

Create a menu-driven program containing these options:

1. Convert numeric text into an integer.
2. Convert numeric text into a float.
3. Convert numeric text into a complex number.
4. Exit.

Handle invalid menu choices and invalid numeric input.

---

## 18. Common Mistakes and Their Solutions

| Mistake | Why It Happens | Correct Approach |
|---|---|---|
| Assuming `int(8.9)` rounds the number | `int()` truncates toward zero | Use `round()` when rounding is intended |
| Passing `"12.5"` directly to `int()` | It is not valid integer text | Use `float("12.5")` |
| Confusing `round()` with formatting | Rounding and display formatting have different purposes | Use `round()` for rounded numeric results and f-strings for display |
| Converting a complex value directly to an integer | Complex numbers are not accepted by `int()` | Select the real component explicitly if appropriate |
| Assuming all floats are finite | Python supports NaN and infinity | Use `math.isfinite()` when finite numbers are required |
| Ignoring floating-point precision | Some decimal fractions are approximate in binary | Use appropriate comparisons such as `math.isclose()` |
| Ignoring invalid input | Conversion can raise `ValueError` | Handle expected conversion errors |
| Confusing conversion with validation | A valid number can still violate program rules | Validate the converted value separately |
| Confusing floor division with truncation | Floor division moves toward negative infinity | Test negative values and understand the difference |
| Ignoring zero division | Division by zero raises an exception | Validate the divisor where needed |
| Assuming an integer and float must compare unequal | Different data types can represent the same numeric value | Separate value comparisons from type comparisons |
| Catching every exception without a reason | Unrelated programming errors may be hidden | Catch specific expected exceptions |

---

## 19. Viva and Interview Questions

### Q1. What is numeric conversion?

Numeric conversion changes a value from one supported numeric data type into another.

### Q2. What are the main numeric data types in Python?

The main numeric types are `int`, `float`, and `complex`.

### Q3. What does `float(10)` return?

It returns `10.0`.

### Q4. What does `int(5.9)` return?

It returns `5` because the fractional part is truncated toward zero.

### Q5. What is the difference between `int()` and `round()`?

`int()` truncates a floating-point value toward zero. `round()` applies Python's rounding rules.

### Q6. What does `round(2.5)` return?

It returns `2` because Python uses ties-to-even rounding for this exact halfway case.

### Q7. What does `round(3.5)` return?

It returns `4` because `4` is the even integer in the halfway case.

### Q8. How can an integer be converted into a complex number?

Use `complex(value)`.

### Q9. Can a complex number be converted directly into a float?

No. Python raises `TypeError` for direct conversion of a complex number to a float.

### Q10. What is the difference between `/` and `//`?

`/` performs normal division. `//` performs floor division.

### Q11. What does the modulo operator do?

The `%` operator returns the remainder according to Python's division rules.

### Q12. What is floating-point precision?

It refers to the precision and representation limitations that arise when floating-point numbers are stored in binary format.

### Q13. Why can `0.1 + 0.2` differ from `0.3`?

Many decimal fractions cannot be represented exactly in binary floating-point format.

### Q14. How can two floating-point values be compared approximately?

Use `math.isclose()` with appropriate tolerance settings.

### Q15. What does `math.isfinite()` check?

It returns `True` when a number is neither infinity nor NaN.

### Q16. What is `ValueError`?

It is an exception commonly raised when a value cannot be converted into the requested format.

### Q17. What is the difference between conversion and validation?

Conversion creates or parses the desired data type. Validation checks whether the resulting value satisfies the application's rules.

### Q18. Why is exception handling useful?

It allows the program to respond to invalid input with an understandable message instead of terminating unexpectedly.

### Q19. Why should negative quantities sometimes be rejected?

Some applications require quantities to be positive or non-negative, even though negative numbers are valid integers or floats.

### Q20. How can seconds be converted into hours and minutes?

Use floor division to calculate whole units and modulo to calculate the remaining quantity.

---

## 20. Quick Revision Table

| Function or Operator | Purpose | Example |
|---|---|---|
| `int()` | Convert a compatible value to an integer | `int(5.8)` |
| `float()` | Convert a compatible value to a float | `float(5)` |
| `complex()` | Create a complex number | `complex(3, 4)` |
| `round()` | Round a numeric value | `round(3.14159, 2)` |
| `type()` | Inspect a value's data type | `type(10.0)` |
| `/` | Normal division | `17 / 5` |
| `//` | Floor division | `17 // 5` |
| `%` | Modulo operation | `17 % 5` |
| `.real` | Access a complex number's real component | `(3+4j).real` |
| `.imag` | Access a complex number's imaginary component | `(3+4j).imag` |
| `math.isfinite()` | Check whether a number is finite | `math.isfinite(12.5)` |
| `math.isclose()` | Compare approximate numeric equality | `math.isclose(0.1 + 0.2, 0.3)` |
| `try` and `except` | Handle expected errors | Safe conversion |

### Five Essential Rules

1. `float()` converts an integer into a floating-point value.
2. `int()` truncates a float toward zero rather than rounding it.
3. `round()` follows Python's rounding rules, including ties-to-even.
4. Complex numbers cannot be converted directly into integers or floats.
5. Numeric conversion and input validation are separate tasks.

---

## 21. Learning Checklist

Mark each item when you can explain and demonstrate it independently.

### Numeric Data Types

- [ ] I understand the difference between `int`, `float`, and `complex`.
- [ ] I can identify the type of a numeric value.
- [ ] I can convert integers into floats.
- [ ] I can convert integers and floats into complex numbers.

### Rounding and Arithmetic

- [ ] I understand truncation toward zero.
- [ ] I can explain the difference between `int()` and `round()`.
- [ ] I understand ties-to-even rounding.
- [ ] I can format numbers to a fixed number of decimal places.
- [ ] I can distinguish normal division and floor division.
- [ ] I can use modulo to calculate a remainder.

### Numeric Input and Validation

- [ ] I can convert valid numeric strings into integers.
- [ ] I can convert valid numeric strings into floats.
- [ ] I can parse complex-number text.
- [ ] I can handle invalid numeric input.
- [ ] I understand why finite-number validation may be necessary.
- [ ] I can distinguish conversion errors from validation errors.

### Precision and Programming Practice

- [ ] I understand floating-point representation limitations.
- [ ] I can compare floating-point numbers approximately.
- [ ] I have completed all twelve solved problems.
- [ ] I have attempted all ten unsolved practice questions.
- [ ] I can answer the viva questions in my own words.

---

## 22. Final Summary

Numeric conversion is a fundamental Python concept used in arithmetic calculations, input processing, scientific applications, and practical programming tasks.

The most important functions in this topic are `int()`, `float()`, `complex()`, and `round()`.

Remember the following:

- Integer-to-float conversion changes the data type while preserving the represented numeric value.
- Float-to-integer conversion truncates toward zero.
- Rounding follows Python's rounding rules.
- Complex numbers contain real and imaginary components.
- Numeric strings must be valid for the selected conversion function.
- Normal division, floor division, and modulo have different purposes.
- Floating-point values may contain small representation differences.
- Input conversion should be followed by validation when the application has additional requirements.
- Expected conversion errors should be handled appropriately.

**The best way to master numeric conversion is to understand each operation, predict its output, test different inputs, and solve the practice questions independently.**