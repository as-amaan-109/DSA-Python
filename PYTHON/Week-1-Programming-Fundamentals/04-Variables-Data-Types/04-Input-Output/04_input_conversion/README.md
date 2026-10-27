# Python Input Conversion

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Input and Output  
**Topic:** Input Conversion  
**Folder:** `04_input_conversion`  
**Language:** Python 3  
**Level:** Beginner to Intermediate  
**Purpose:** Learn how to convert values received from user input into appropriate Python data types.

---

# Table of Contents

1. Introduction
2. Learning Objectives
3. What Is Input Conversion?
4. Why Input Conversion Is Needed
5. Understanding the `input()` Function
6. Return Type of `input()`
7. Difference Between Input and Conversion
8. Python Data Types Used in This Topic
9. The `int()` Function
10. The `float()` Function
11. The `complex()` Function
12. The `str()` Function
13. The `bool()` Function
14. Why `bool("False")` Is True
15. Converting Text into Boolean Values
16. Converting Lists
17. Converting Multiple Inputs
18. Converting Binary Strings
19. Numeric Conversion Rules
20. Type Conversion and Type Casting
21. Implicit and Explicit Conversion
22. Safe Input Conversion
23. The `ValueError` Exception
24. The `TypeError` Exception
25. Using `try` and `except`
26. Repeated Input Until Valid
27. Input Validation
28. Range Validation
29. Empty Input Validation
30. Whitespace Handling
31. Decimal and Integer Input
32. Floating-Point Precision
33. Truncation and Rounding
34. Complex Number Conversion
35. List Conversion
36. Common Input Conversion Patterns
37. Helper Functions Used in This Project
38. Section 1 — Twelve Examples
39. Section 2 — Twelve Solved Problems
40. Understanding `SOLVED_PROBLEMS`
41. Section 3 — Ten Unsolved Questions
42. Section 4 — Learning Checklist
43. Section 5 — Main Menu
44. How to Run the Program
45. Sample Program Execution
46. Common Mistakes
47. Debugging Strategies
48. Testing Strategy
49. Boundary Testing
50. Best Practices
51. Real-Life Applications
52. Mini Project Ideas
53. Frequently Asked Questions
54. Viva Questions and Answers
55. Quick Revision Tables
56. Important Terms
57. Final Summary

---

# 1. Introduction

Input conversion is an important concept in Python programming.

Programs frequently receive information from users.

Examples of user-provided information include:

- Name
- Age
- Marks
- Price
- Quantity
- Temperature
- Distance
- Weight
- Boolean choices
- Lists of numbers
- Complex numbers

A program must understand the kind of information it receives before using it in calculations.

For example, consider this program:

```python
age = input("Enter your age: ")

print(age)
```

If the user enters:

```text
20
```

Python receives the characters representing the value `20` as a string.

The variable `age` therefore contains:

```python
"20"
```

It does not automatically contain the integer:

```python
20
```

This distinction becomes important when performing arithmetic.

Consider the following program:

```python
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

print(first_number + second_number)
```

Suppose the user enters:

```text
10
20
```

The output is:

```text
1020
```

Why?

Because both variables contain strings.

The `+` operator joins strings together rather than adding the numeric values.

To perform arithmetic, the inputs must be converted into numbers.

```python
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(first_number + second_number)
```

Input:

```text
10
20
```

Output:

```text
30
```

This is the basic purpose of input conversion.

Input conversion means changing a value from one data type into another appropriate data type.

Python provides built-in functions such as:

- `int()`
- `float()`
- `complex()`
- `str()`
- `bool()`

These functions help programs convert values when the conversion is valid.

Input conversion must also be combined with validation.

A user may enter invalid text, an empty value, a negative number, or a number outside the permitted range.

A reliable program should handle these situations carefully.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Explain what input conversion means.
2. Understand why `input()` returns a string.
3. Convert numeric strings into integers.
4. Convert numeric strings into floating-point numbers.
5. Convert valid strings into complex numbers.
6. Convert numbers into strings.
7. Explain the difference between numeric and textual values.
8. Understand the behavior of `bool()`.
9. Explain why `bool("False")` evaluates to `True`.
10. Convert textual yes/no answers into Boolean values.
11. Convert a collection of numeric strings into numeric values.
12. Convert binary text into an integer using base `2`.
13. Understand the difference between conversion and validation.
14. Handle invalid numeric input with exception handling.
15. Use `try` and `except` safely.
16. Validate whether a number is inside an acceptable range.
17. Understand integer truncation.
18. Distinguish integer conversion from rounding.
19. Use helper functions to simplify input handling.
20. Read and understand a menu-driven Python program.
21. Test input conversion with valid and invalid values.
22. Recognize common conversion errors.
23. Design simple programs that accept and process user input.
24. Practice writing programs that handle unexpected input.

---

# 3. What Is Input Conversion?

Input conversion is the process of changing received input into a different data type.

Suppose a user enters the following value:

```text
25
```

The value may initially be represented as a string:

```python
"25"
```

To use it as an integer, convert it:

```python
age = int("25")

print(age)
print(type(age))
```

Output:

```text
25
<class 'int'>
```

The result is an integer.

The conversion function is:

```python
int()
```

Another example:

```python
price = float("99.50")

print(price)
print(type(price))
```

Output:

```text
99.5
<class 'float'>
```

The string has been converted into a floating-point number.

## 3.1 General Syntax

The general syntax of explicit conversion is:

```python
converted_value = target_type(original_value)
```

Here:

- `converted_value` stores the conversion result.
- `target_type` identifies the desired data type.
- `original_value` is the value to convert.

Examples:

```python
number = int("100")
price = float("45.75")
message = str(500)
complex_value = complex("2+3j")
```

## 3.2 Important Rule

Not every value can be converted into every data type.

For example:

```python
number = int("hello")
```

This statement raises a `ValueError`.

The string `"hello"` does not represent a valid integer.

A correct program must either reject the input or handle the error.

---

# 4. Why Input Conversion Is Needed

Input conversion is necessary because the data type of a value determines which operations make sense.

## 4.1 Numeric Calculations

Suppose a program receives two numbers.

```python
first = input("Enter first number: ")
second = input("Enter second number: ")
```

When the user enters `4` and `6`, the variables contain strings.

Therefore:

```python
print(first + second)
```

produces:

```text
46
```

If the program needs arithmetic addition, the inputs should be converted:

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print(first + second)
```

Output:

```text
10
```

## 4.2 Comparing Numbers

Text and numbers can behave differently during comparison.

For example:

```python
print("20" == 20)
```

Output:

```text
False
```

The values have different types.

A numeric comparison should use numeric values:

```python
age = int("20")

print(age == 20)
```

Output:

```text
True
```

## 4.3 Calculating an Average

Average marks require arithmetic.

```python
marks_1 = float(input("Enter first mark: "))
marks_2 = float(input("Enter second mark: "))

average = (marks_1 + marks_2) / 2

print("Average:", average)
```

Input:

```text
80
90
```

Output:

```text
Average: 85.0
```

## 4.4 Processing Prices

Prices frequently contain decimal values.

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total:", total)
```

Input:

```text
49.50
3
```

Output:

```text
Total: 148.5
```

For financial applications, Python's `decimal.Decimal` may be more suitable than binary floating-point arithmetic. That subject is beyond the basic scope of this module.

## 4.5 Data Processing

A program that reads numeric information from text files, forms, or command-line input may need to convert text into numbers before processing it.

The same principle applies to:

- Student marks
- Product quantities
- Measurements
- Survey responses
- Scientific values
- Configuration values
- User-selected options

---

# 5. Understanding the `input()` Function

The `input()` function reads a line of text from the user.

Basic syntax:

```python
value = input("Enter something: ")
```

The string supplied as the argument becomes the prompt displayed to the user.

Example:

```python
name = input("Enter your name: ")

print("Hello,", name)
```

Example interaction:

```text
Enter your name: Amaan
Hello, Amaan
```

The returned value is a string.

## 5.1 Reading a Value

```python
value = input("Enter a value: ")
```

If the user enters:

```text
Python
```

Then:

```python
value == "Python"
```

## 5.2 Reading a Number

```python
number = input("Enter a number: ")
```

If the user enters:

```text
100
```

The variable contains:

```python
"100"
```

The type can be verified:

```python
print(type(number))
```

Output:

```text
<class 'str'>
```

## 5.3 Input Followed by Conversion

```python
number = int(input("Enter an integer: "))
```

Python evaluates the expression from the inside out.

First:

```python
input("Enter an integer: ")
```

collects text.

Then:

```python
int(...)
```

converts the returned string into an integer.

Finally, the resulting integer is assigned to `number`.

This is called nested function usage.

## 5.4 Separate Input and Conversion

The conversion can also be written on a separate line.

```python
raw_value = input("Enter an integer: ")

number = int(raw_value)

print(number)
```

This form can be easier to debug because the original input and converted value are stored separately.

---

# 6. Return Type of `input()`

The `input()` function returns a string when the operation completes successfully.

Examples:

| User enters | Result returned by `input()` |
|---|---|
| `25` | `"25"` |
| `3.14` | `"3.14"` |
| `hello` | `"hello"` |
| `True` | `"True"` |
| `1+2j` | `"1+2j"` |
| `007` | `"007"` |
| `-10` | `"-10"` |
| Empty line | `""` |

The quotes shown in the table indicate string values.

They are not normally displayed as part of the returned value.

## 6.1 Numeric-Looking Text Is Still Text

```python
value = input("Enter a value: ")
```

If the user enters `50`, Python does not automatically infer that it should be an integer.

The program must request that conversion explicitly.

```python
value = int(input("Enter a value: "))
```

## 6.2 Empty Input

If a user presses Enter without entering text, `input()` returns an empty string.

```python
value = input("Enter text: ")

print(repr(value))
```

If the user immediately presses Enter, the output is:

```text
''
```

Attempting this conversion is invalid:

```python
int("")
```

The conversion raises `ValueError`.

A reliable program should check for empty input or catch the conversion error.

---

# 7. Difference Between Input and Conversion

Input and conversion are two separate operations.

**Input** collects a value from the user.

**Conversion** changes the data type of that value.

| Operation | Function | Purpose |
|---|---|---|
| Read text | `input()` | Collect a line of text |
| Convert to integer | `int()` | Produce an integer |
| Convert to decimal number | `float()` | Produce a floating-point number |
| Convert to complex number | `complex()` | Produce a complex number |
| Convert to string | `str()` | Produce a string representation |
| Interpret truth value | `bool()` | Produce a Boolean value |

Example:

```python
raw_age = input("Enter age: ")

age = int(raw_age)

print(age)
```

The first assignment stores the raw input.

The second assignment stores the converted value.

These steps should be understood separately, even when they appear on one line.

---

# 8. Python Data Types Used in This Topic

The following data types appear frequently in input conversion.

## 8.1 `str`

A string represents text.

```python
name = "Amaan"
number_text = "100"
```

Both variables contain strings.

The string `"100"` can be converted into an integer because its contents represent a valid integer.

## 8.2 `int`

An integer represents a whole number without a fractional component.

```python
age = 20
quantity = 4
temperature_difference = -8
```

Integers may be positive, negative, or zero.

## 8.3 `float`

A floating-point number represents a real-number approximation.

```python
price = 99.50
average = 82.75
temperature = -2.5
```

Python generally displays `99.50` as `99.5`.

The stored numeric value does not preserve the original number of trailing zeros as formatting information.

## 8.4 `complex`

A complex number contains real and imaginary components.

```python
value = 2 + 3j
```

In Python, `j` represents the imaginary unit.

Example:

```python
value = complex("2+3j")

print(value)
```

Output:

```text
(2+3j)
```

## 8.5 `bool`

A Boolean value is either:

```python
True
```

or:

```python
False
```

Boolean values must be capitalized exactly as shown.

Examples:

```python
is_valid = True
is_empty = False
```

A string such as `"True"` is not the same as the Boolean value `True`.

---

# 9. The `int()` Function

The `int()` function converts suitable values into integers.

## 9.1 Basic Syntax

```python
integer_value = int(value)
```

## 9.2 Convert a Numeric String

```python
number = int("125")

print(number)
print(type(number))
```

Output:

```text
125
<class 'int'>
```

## 9.3 Convert a Negative Integer String

```python
number = int("-25")

print(number)
```

Output:

```text
-25
```

## 9.4 Convert a String Containing Surrounding Spaces

```python
number = int(" 45 ")

print(number)
```

Output:

```text
45
```

Whitespace around the integer text is accepted.

## 9.5 Convert an Integer-Like Decimal String

```python
number = int("12")
```

This conversion succeeds.

However:

```python
number = int("12.5")
```

raises `ValueError`.

The string contains a decimal point and is not a valid integer literal for this conversion.

A possible approach is:

```python
number = int(float("12.5"))

print(number)
```

Output:

```text
12
```

This first converts the text into a floating-point number and then converts the result into an integer.

The decimal portion is discarded.

This behavior should not be confused with rounding.

## 9.6 Convert a Floating-Point Number to an Integer

```python
print(int(9.8))
print(int(9.2))
print(int(-9.8))
```

Output:

```text
9
9
-9
```

For floating-point inputs, `int()` truncates toward zero.

It does not always round down.

## 9.7 Convert a Boolean to an Integer

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

This conversion is valid in Python because `bool` is a subclass of `int`.

In beginner-facing applications, it is usually clearer to handle Boolean input explicitly rather than relying on this relationship.

## 9.8 Convert Binary Text

The second argument to `int()` specifies the base.

```python
number = int("1010", 2)

print(number)
```

Output:

```text
10
```

The text `"1010"` is interpreted as a base-2 number.

The second argument is not a request to display the answer in binary.

It tells Python how to interpret the input text.

## 9.9 Invalid Integer Input

```python
int("hello")
```

This raises:

```text
ValueError
```

Other invalid examples include:

```python
int("12.5")
int("")
int("ten")
```

## 9.10 Reading an Integer from the User

```python
age = int(input("Enter your age: "))

print("Age:", age)
```

Input:

```text
20
```

Output:

```text
Age: 20
```

This approach works only when the entered text is a valid integer.

For reusable programs, it is safer to use an exception-handling helper function.

---

# 10. The `float()` Function

The `float()` function converts appropriate values into floating-point numbers.

## 10.1 Basic Syntax

```python
float_value = float(value)
```

## 10.2 Convert a Decimal String

```python
price = float("99.50")

print(price)
print(type(price))
```

Output:

```text
99.5
<class 'float'>
```

## 10.3 Convert an Integer String

```python
number = float("25")

print(number)
```

Output:

```text
25.0
```

## 10.4 Convert a Negative Decimal String

```python
temperature = float("-4.75")

print(temperature)
```

Output:

```text
-4.75
```

## 10.5 Convert an Integer

```python
number = float(10)

print(number)
```

Output:

```text
10.0
```

## 10.6 Scientific Notation

Python supports scientific notation.

```python
value = float("1.5e3")

print(value)
```

Output:

```text
1500.0
```

The text represents:

\[
1.5 \times 10^3
\]

Another example:

```python
value = float("2.5e-2")

print(value)
```

Output:

```text
0.025
```

## 10.7 Invalid Float Input

```python
float("hello")
```

This raises `ValueError`.

The following is also invalid:

```python
float("12.5.7")
```

A string cannot contain multiple decimal points in this numeric format.

## 10.8 Float Conversion and Precision

Floating-point numbers use a binary representation.

Some decimal fractions cannot be represented exactly in binary floating-point format.

Example:

```python
value = 0.1 + 0.2

print(value)
```

A typical output is:

```text
0.30000000000000004
```

This is a representation limitation, not necessarily a programming mistake.

When comparing floating-point results, consider whether a tolerance is appropriate.

For financial calculations that require exact decimal behavior, consider the `decimal` module.

## 10.9 Reading a Float from the User

```python
price = float(input("Enter price: "))

print("Price:", price)
```

Input:

```text
49.75
```

Output:

```text
Price: 49.75
```

---

# 11. The `complex()` Function

Python supports complex numbers.

A complex number has a real part and an imaginary part.

Example:

```python
value = 2 + 3j
```

The real part is `2`.

The imaginary coefficient is `3`.

## 11.1 Basic Syntax

```python
complex_value = complex(value)
```

The `complex()` function can also receive separate real and imaginary components:

```python
complex_value = complex(real, imaginary)
```

## 11.2 Convert a Complex String

```python
value = complex("2+3j")

print(value)
```

Output:

```text
(2+3j)
```

## 11.3 Convert an Integer

```python
value = complex(5)

print(value)
```

Output:

```text
(5+0j)
```

## 11.4 Convert a Float

```python
value = complex(2.5)

print(value)
```

Output:

```text
(2.5+0j)
```

## 11.5 Provide Real and Imaginary Components

```python
value = complex(4, 6)

print(value)
```

Output:

```text
(4+6j)
```

## 11.6 Access Complex Components

```python
value = complex("2+3j")

print(value.real)
print(value.imag)
```

Output:

```text
2.0
3.0
```

The `.real` and `.imag` attributes return the respective components as floating-point values.

## 11.7 Invalid Complex Input

```python
complex("hello")
```

This raises `ValueError`.

## 11.8 Reading a Complex Number

```python
value = complex(input("Enter a complex number: "))

print(value)
```

Example input:

```text
2+3j
```

Output:

```text
(2+3j)
```

The complex-number syntax must be valid for Python.

---

# 12. The `str()` Function

The `str()` function converts many values into their string representation.

## 12.1 Convert an Integer to a String

```python
value = str(100)

print(value)
print(type(value))
```

Output:

```text
100
<class 'str'>
```

## 12.2 Convert a Float to a String

```python
price = str(49.5)

print(price)
```

Output:

```text
49.5
```

## 12.3 Convert a Boolean to a String

```python
value = str(True)

print(value)
print(type(value))
```

Output:

```text
True
<class 'str'>
```

The result is the string `"True"`, not the Boolean value `True`.

## 12.4 Use a String in a Message

```python
age = 20

message = "Age: " + str(age)

print(message)
```

Output:

```text
Age: 20
```

An often clearer alternative is an f-string:

```python
age = 20

print(f"Age: {age}")
```

Both approaches display the integer inside a message.

## 12.5 Conversion Does Not Preserve Every Formatting Choice

```python
value = str(10.0)

print(value)
```

Output:

```text
10.0
```

String conversion represents the numeric value according to Python's string conversion rules.

It does not automatically apply every display format an application may require.

For a fixed number of decimal places, formatted strings can be used:

```python
price = 10.5

print(f"{price:.2f}")
```

Output:

```text
10.50
```

---

# 13. The `bool()` Function

The `bool()` function converts a value into its truth value.

## 13.1 Convert Zero

```python
print(bool(0))
```

Output:

```text
False
```

## 13.2 Convert a Nonzero Integer

```python
print(bool(1))
print(bool(-1))
print(bool(100))
```

Output:

```text
True
True
True
```

## 13.3 Convert an Empty String

```python
print(bool(""))
```

Output:

```text
False
```

## 13.4 Convert a Nonempty String

```python
print(bool("Python"))
```

Output:

```text
True
```

## 13.5 Convert an Empty List

```python
print(bool([]))
```

Output:

```text
False
```

## 13.6 Convert a Nonempty List

```python
print(bool([1, 2, 3]))
```

Output:

```text
True
```

## 13.7 Truthiness Rule

Common false values include:

- `False`
- `None`
- Numeric zero
- Empty strings
- Empty lists
- Empty tuples
- Empty dictionaries
- Empty sets

Most other objects are truthy.

The exact behavior depends on the object's truth-value rules.

## 13.8 Important Warning

This statement:

```python
bool("False")
```

returns:

```text
True
```

The string contains characters.

It is not an empty string.

The Boolean conversion does not read the English meaning of the text.

This distinction is especially important when collecting yes/no answers from a user.

---

# 14. Why `bool("False")` Is True

Consider:

```python
answer = "False"

print(bool(answer))
```

Output:

```text
True
```

The variable `answer` contains a nonempty string.

Python evaluates whether the string is empty, not whether its text spells the word `False`.

Compare the following:

```python
print(bool(""))
print(bool("False"))
print(bool("True"))
print(bool("No"))
print(bool("Yes"))
```

Output:

```text
False
True
True
True
True
```

Every string in this example except the empty string is truthy.

## 14.1 Why This Matters

Suppose a program asks:

```python
answer = input("Continue? ")
```

The user enters:

```text
no
```

If the program then uses:

```python
if bool(answer):
    print("Continuing")
```

the branch runs because `"no"` is a nonempty string.

This is probably not the intended application behavior.

## 14.2 Better Approach

Normalize the string and compare it with known answers.

```python
answer = input("Continue? ").strip().lower()

if answer in ("yes", "y"):
    print("Continuing")
elif answer in ("no", "n"):
    print("Stopping")
else:
    print("Invalid answer")
```

This program checks the text explicitly.

It handles uppercase and lowercase input because `lower()` normalizes the answer.

The use of `strip()` removes whitespace from the beginning and end of the response.

---

# 15. Converting Text into Boolean Values

A program sometimes needs to accept textual answers and convert them into Boolean values.

Examples include:

- Yes or no
- True or false
- Y or N
- Enabled or disabled

Python does not automatically interpret every nonempty string as an English Boolean value.

A custom parsing function can define which answers are accepted.

## 15.1 Basic Boolean Parser

```python
def parse_boolean(value):
    value = value.strip().lower()

    if value in ("true", "yes", "y", "1"):
        return True

    if value in ("false", "no", "n", "0"):
        return False

    raise ValueError("Invalid Boolean value")
```

Example:

```python
print(parse_boolean("yes"))
print(parse_boolean("NO"))
print(parse_boolean("True"))
print(parse_boolean("0"))
```

Output:

```text
True
False
True
False
```

## 15.2 Invalid Answer

```python
parse_boolean("maybe")
```

The function raises `ValueError`.

This is better than silently treating an unknown answer as true or false.

## 15.3 Why Normalize Input?

The following strings differ in capitalization:

```text
YES
Yes
yes
YeS
```

Using:

```python
value.strip().lower()
```

normalizes them into:

```text
yes
```

This makes comparison simpler.

## 15.4 Boolean Conversion Design

A Boolean parser should define:

1. Accepted true values.
2. Accepted false values.
3. Treatment of whitespace.
4. Treatment of capitalization.
5. Expected behavior for invalid input.
6. Whether the application should retry.
7. Whether the application should terminate after repeated invalid input.

Different applications may choose different rules.

The parser must follow the requirements of the program.

---

# 16. Converting Lists

A list is a collection of values.

Sometimes user input arrives as text containing several values.

For example:

```text
10,20,30
```

The program may need to split the text into individual items and convert each item.

## 16.1 Split a Comma-Separated String

```python
raw_values = "10,20,30"

values = raw_values.split(",")

print(values)
```

Output:

```text
['10', '20', '30']
```

The resulting items are strings.

## 16.2 Convert the Items to Integers

```python
raw_values = "10,20,30"

values = [int(item) for item in raw_values.split(",")]

print(values)
```

Output:

```text
[10, 20, 30]
```

The list now contains integers.

## 16.3 Convert to Floating-Point Values

```python
raw_values = "10.5,20.25,30.75"

values = [float(item) for item in raw_values.split(",")]

print(values)
```

Output:

```text
[10.5, 20.25, 30.75]
```

## 16.4 Handle Spaces

```python
raw_values = "10, 20, 30"

values = [int(item.strip()) for item in raw_values.split(",")]

print(values)
```

Output:

```text
[10, 20, 30]
```

In this example, `strip()` removes whitespace around each individual item.

## 16.5 Invalid List Item

Consider:

```python
raw_values = "10,twenty,30"

values = [int(item) for item in raw_values.split(",")]
```

The conversion fails because `"twenty"` is not a valid integer string.

A robust implementation should decide how to handle invalid list items.

Possible approaches include:

- Reject the entire list.
- Report the invalid item.
- Ask the user to enter the list again.
- Skip invalid values only when the application requirements explicitly allow it.

Silently skipping bad data can hide mistakes.

---

# 17. Converting Multiple Inputs

A program may need multiple values from a single input line.

For example:

```text
10 20
```

Whitespace-separated values can be collected using `split()`.

## 17.1 Read Two Integer Values

```python
raw_values = input("Enter two integers: ").split()

first = int(raw_values[0])
second = int(raw_values[1])

print(first + second)
```

Input:

```text
10 20
```

Output:

```text
30
```

This basic example assumes that exactly two valid integer values are provided.

## 17.2 Read Multiple Integers

```python
raw_values = input("Enter integers separated by spaces: ").split()

numbers = [int(value) for value in raw_values]

print(numbers)
```

Input:

```text
10 20 30 40
```

Output:

```text
[10, 20, 30, 40]
```

## 17.3 Calculate the Sum

```python
raw_values = input("Enter integers: ").split()

numbers = [int(value) for value in raw_values]

print("Sum:", sum(numbers))
```

Input:

```text
10 20 30
```

Output:

```text
Sum: 60
```

The `sum()` function calculates the total of the numbers in the list.

## 17.4 Validate the Number of Inputs

A program that needs exactly two values should check the count before accessing list elements.

```python
raw_values = input("Enter two numbers: ").split()

if len(raw_values) != 2:
    print("Please enter exactly two values.")
else:
    first = int(raw_values[0])
    second = int(raw_values[1])

    print(first + second)
```

This protects against missing or additional values.

However, it does not yet handle invalid integer text. Exception handling is still needed when conversion errors are possible.

---

# 18. Converting Binary Strings

Binary is a number system that uses only two digits:

```text
0
1
```

Python can interpret binary text using the `int()` function with base `2`.

## 18.1 Basic Conversion

```python
number = int("1010", 2)

print(number)
```

Output:

```text
10
```

The binary number `1010` equals decimal ten.

## 18.2 Another Example

```python
number = int("1111", 2)

print(number)
```

Output:

```text
15
```

## 18.3 A Single Binary Digit

```python
print(int("0", 2))
print(int("1", 2))
```

Output:

```text
0
1
```

## 18.4 Invalid Binary Text

```python
int("102", 2)
```

This raises `ValueError`.

The digit `2` is invalid in base `2`.

## 18.5 Binary Input from the User

```python
binary_text = input("Enter a binary number: ")

decimal_value = int(binary_text, 2)

print("Decimal value:", decimal_value)
```

Input:

```text
1010
```

Output:

```text
Decimal value: 10
```

A production-quality version should catch invalid binary input.

## 18.6 Understand the Base Argument

In:

```python
int("1010", 2)
```

the first argument is the text.

The second argument says that the text represents a number in base `2`.

This differs from:

```python
int("1010")
```

which interprets the text as a decimal integer by default.

The second form produces:

```text
1010
```

The first form produces:

```text
10
```

---

# 19. Numeric Conversion Rules

Input conversion follows rules defined by Python.

Understanding these rules helps prevent unexpected results.

## 19.1 String to Integer

```python
int("50")
```

Result:

```text
50
```

## 19.2 String to Float

```python
float("50.5")
```

Result:

```text
50.5
```

## 19.3 Float to Integer

```python
int(50.9)
```

Result:

```text
50
```

The fractional portion is discarded.

## 19.4 Integer to Float

```python
float(50)
```

Result:

```text
50.0
```

## 19.5 Integer to String

```python
str(50)
```

Result:

```text
'50'
```

## 19.6 String to Complex

```python
complex("2+3j")
```

Result:

```text
(2+3j)
```

## 19.7 Invalid Conversion

```python
int("five")
```

Result:

```text
ValueError
```

## 19.8 Conversion Does Not Mean Validation

This statement can successfully convert a value:

```python
age = int("0")
```

But whether age `0` is acceptable depends on the application's rules.

Conversion checks whether the representation can be interpreted as an integer.

Validation checks whether that integer satisfies the application's requirements.

---

# 20. Type Conversion and Type Casting

The terms *type conversion* and *type casting* are often used similarly in beginner Python lessons.

The important distinction is between automatically occurring conversion and explicitly requested conversion.

## 20.1 Explicit Conversion

A programmer calls a conversion function.

```python
number = int("20")
```

The programmer explicitly requests an integer.

## 20.2 Automatic Numeric Behavior

Python sometimes performs operations between compatible numeric types.

```python
result = 5 + 2.5

print(result)
```

Output:

```text
7.5
```

The result is a floating-point value.

This is numeric promotion during an arithmetic operation.

It does not mean that `input()` automatically converts user-entered strings to numbers.

## 20.3 Assignment Does Not Convert Automatically

```python
number = "10"
```

The variable refers to a string.

Writing:

```python
number = "10"
```

does not produce an integer.

The programmer must request conversion:

```python
number = int("10")
```

## 20.4 Naming Variables Carefully

These variable names suggest different intentions:

```python
raw_age = input("Age: ")
age = int(raw_age)
```

`raw_age` indicates the original textual value.

`age` indicates the converted integer.

Clear variable names make input-processing code easier to understand.

---

# 21. Implicit and Explicit Conversion

## 21.1 Implicit Conversion

Implicit conversion happens as part of certain Python operations without an explicit conversion function call.

Example:

```python
result = 10 + 2.5

print(result)
```

Output:

```text
12.5
```

## 21.2 Explicit Conversion

Explicit conversion is directly requested.

```python
result = int("10")

print(result)
```

Output:

```text
10
```

## 21.3 Important Difference

A common beginner mistake is assuming that the presence of numeric text is enough for arithmetic.

It is not.

```python
"10" + "20"
```

produces:

```text
1020
```

By contrast:

```python
int("10") + int("20")
```

produces:

```text
30
```

## 21.4 Practical Rule

When receiving a value from `input()`:

1. Identify the required data type.
2. Convert the input appropriately.
3. Handle conversion failures.
4. Validate the converted value.
5. Process the value.
6. Display the result.

---

# 22. Safe Input Conversion

Direct conversion is convenient:

```python
age = int(input("Enter age: "))
```

However, it assumes the input is valid.

If the user enters:

```text
twenty
```

the program raises an exception.

Safe input conversion handles invalid values without abruptly terminating the entire application.

## 22.1 Basic Safe Conversion

```python
try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid integer.")
```

If valid input is supplied, the program continues normally.

If invalid integer text is supplied, the exception handler displays a message.

## 22.2 Safe Float Conversion

```python
try:
    price = float(input("Enter price: "))
    print("Price:", price)
except ValueError:
    print("Please enter a valid number.")
```

## 22.3 Safe Complex Conversion

```python
try:
    value = complex(input("Enter a complex number: "))
    print("Value:", value)
except ValueError:
    print("Please enter a valid complex number.")
```

## 22.4 Why Safe Conversion Matters

Users do not always enter the expected value.

For example, an integer prompt may receive:

```text
abc
```

or:

```text
12.5
```

or an empty line.

The program should explain what went wrong and, when appropriate, allow another attempt.

---

# 23. The `ValueError` Exception

A `ValueError` commonly occurs when a value has the expected general type but an inappropriate value for an operation.

For input conversion, an example is:

```python
int("hello")
```

The function receives a string, but its contents do not represent a valid integer.

## 23.1 Example

```python
try:
    number = int("hello")
except ValueError:
    print("Conversion failed.")
```

Output:

```text
Conversion failed.
```

## 23.2 Invalid Integer Examples

```python
int("abc")
int("")
int("12.5")
int("ten")
```

Each expression raises `ValueError`.

## 23.3 Invalid Float Examples

```python
float("abc")
float("")
float("12.3.4")
```

Each expression raises `ValueError`.

## 23.4 Handle the Error at the Appropriate Level

A reusable helper should communicate a clear error or retry.

The rest of the program should not need to duplicate the same conversion logic everywhere.

The project's input helpers are intended to centralize this behavior.

---

# 24. The `TypeError` Exception

A `TypeError` often occurs when an operation receives an object of an unsupported type.

For example:

```python
result = "10" + 5
```

This raises `TypeError`.

Python does not automatically choose between string concatenation and numeric addition for this mixed operation.

## 24.1 Correct by Converting to Integer

```python
result = int("10") + 5

print(result)
```

Output:

```text
15
```

## 24.2 Correct by Converting to String

```python
result = "10" + str(5)

print(result)
```

Output:

```text
105
```

These two programs perform different operations.

The correct choice depends on whether the program needs arithmetic or text construction.

## 24.3 Difference Between Common Errors

| Exception | Common input-conversion cause |
|---|---|
| `ValueError` | Text cannot be interpreted as the requested value |
| `TypeError` | An operation receives an incompatible type |
| `EOFError` | Input reaches end-of-file unexpectedly in some execution contexts |

The exact exception depends on the operation performed.

---

# 25. Using `try` and `except`

Python exception handling allows a program to respond to certain errors.

## 25.1 Basic Structure

```python
try:
    # Operation that may raise an exception
    pass
except ValueError:
    # Handling for invalid values
    pass
```

The `try` block contains the operation that may fail.

The `except` block handles the specified exception.

## 25.2 Input Conversion Example

```python
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer.")
```

## 25.3 Print the Converted Value

```python
try:
    number = int(input("Enter an integer: "))
    print("Converted value:", number)
except ValueError:
    print("Invalid integer.")
```

## 25.4 Avoid Unnecessarily Broad Exception Handling

This is often too broad:

```python
try:
    number = int(input("Enter an integer: "))
except Exception:
    print("Something went wrong.")
```

A specific exception is clearer when the expected failure is known.

Prefer:

```python
except ValueError:
```

when invalid textual conversion is the expected error.

Broad exception handling can hide unrelated programming mistakes.

## 25.5 Keep the Protected Block Small

Place the operation that may fail inside the `try` block.

```python
raw_value = input("Enter an integer: ")

try:
    number = int(raw_value)
except ValueError:
    print("Invalid integer.")
else:
    print("Valid integer:", number)
```

The `else` block runs only when the `try` block completes without the handled exception.

This can make a program easier to reason about.

---

# 26. Repeated Input Until Valid

A reliable interactive program may repeatedly request input until it can convert the value successfully.

## 26.1 Integer Input Loop

```python
while True:
    try:
        age = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Try again.")

print("Accepted:", age)
```

## 26.2 What Happens?

1. The loop starts.
2. Python requests input.
3. Python attempts conversion.
4. If conversion succeeds, `break` exits the loop.
5. If conversion fails, the error message appears.
6. The loop requests input again.
7. The program continues once valid input is accepted.

## 26.3 Why This Is Useful

The user may make an accidental typing mistake.

Retrying lets the user correct the input without restarting the whole program.

## 26.4 Avoid Infinite Retry Without Feedback

A program should explain why the input was rejected.

For example:

```text
Invalid input. Please enter a whole number.
```

This message is more useful than:

```text
Error.
```

The feedback should identify the expected format.

---

# 27. Input Validation

Input validation determines whether data satisfies requirements.

Conversion and validation are related but different.

## 27.1 Conversion Example

```python
age = int("15")
```

The conversion succeeds.

## 27.2 Validation Example

```python
age = int("15")

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

The first statement converts the text.

The conditional statement applies the application's rule.

## 27.3 Validation Questions

When validating input, ask:

- Is the value present?
- Can it be converted?
- Is the value in the permitted range?
- Is a negative value allowed?
- Does the value make sense for the application?
- Should leading or trailing spaces be accepted?
- Should invalid input be rejected or retried?
- Is the input required to be a whole number?
- Is a decimal number acceptable?
- Are special values allowed?

## 27.4 Validation Is Application-Specific

For example, a negative number may be valid for temperature but invalid for a product quantity.

A value of zero may be valid for a temperature or balance, but not for a quantity that must be strictly positive.

The requirements determine which values are acceptable.

---

# 28. Range Validation

Range validation checks whether a number falls inside permitted boundaries.

For example, a program may require a percentage between `0` and `100`.

## 28.1 Inclusive Range

```python
percentage = float(input("Enter percentage: "))

if 0 <= percentage <= 100:
    print("Accepted")
else:
    print("Percentage must be between 0 and 100.")
```

Both boundaries are allowed.

## 28.2 Exclusive Lower Boundary

A positive quantity may be required:

```python
quantity = int(input("Enter quantity: "))

if quantity > 0:
    print("Accepted")
else:
    print("Quantity must be greater than zero.")
```

## 28.3 Inclusive Integer Range

Suppose a rating must be an integer from `1` through `5`.

```python
rating = int(input("Enter rating: "))

if 1 <= rating <= 5:
    print("Valid rating")
else:
    print("Rating must be between 1 and 5.")
```

## 28.4 Range Validation Must Follow Conversion

The program needs a numeric value before numeric range comparisons can be applied.

A robust program should first convert the input and then validate the result.

## 28.5 Both Checks Are Needed

An input may be:

- Convertible but outside the allowed range.
- Inside the intended range when interpreted numerically.
- Not convertible at all.

For example:

| Input text | Conversion to integer | Range check |
|---|---|---|
| `"5"` | Successful | May pass |
| `"500"` | Successful | May fail |
| `"hello"` | Fails | Cannot proceed normally |
| `""` | Fails | Cannot proceed normally |

---

# 29. Empty Input Validation

Empty input often indicates that the user has skipped a required field.

Example:

```python
name = input("Enter name: ")
```

If the user presses Enter immediately, `name` is an empty string.

## 29.1 Check for Empty Text

```python
name = input("Enter name: ").strip()

if not name:
    print("Name cannot be empty.")
else:
    print("Name:", name)
```

## 29.2 Why Use `strip()`?

A user might enter only spaces:

```text

```

Without trimming, the string is nonempty.

Using:

```python
.strip()
```

removes leading and trailing whitespace.

The resulting string becomes empty.

## 29.3 Empty Numeric Input

This statement fails:

```python
int("")
```

A numeric input helper should handle that failure and request a valid value or return an appropriate error result.

The expected response depends on the design of the application.

---

# 30. Whitespace Handling

Whitespace includes spaces and other spacing characters.

Input values sometimes contain unnecessary whitespace around the useful text.

## 30.1 Remove Surrounding Whitespace

```python
value = "  123  "

print(value.strip())
```

Output:

```text
123
```

## 30.2 Normalize Text Before Comparing

```python
answer = input("Continue? ").strip().lower()
```

The answer becomes easier to compare consistently.

## 30.3 Do Not Confuse Trimming with Full Validation

Whitespace removal only addresses surrounding whitespace.

It does not make arbitrary text numeric.

For example:

```python
"  hello  ".strip()
```

produces:

```text
hello
```

It does not produce an integer.

## 30.4 Keep Original Text When Needed

Sometimes the program needs the exact original input.

For that reason, it can be useful to store the raw value first:

```python
raw_value = input("Enter value: ")

normalized_value = raw_value.strip()
```

This approach preserves the original string while creating a normalized version for validation.

---

# 31. Decimal and Integer Input

One common question is whether all numeric values should be converted using `int()`.

The answer depends on what kind of value the program needs.

## 31.1 Whole-Number Input

Use integer conversion when the application expects a whole number:

```python
quantity = int(input("Enter quantity: "))
```

Examples of quantities that are often whole numbers include:

- Number of students
- Number of items
- Number of pages
- Number of attempts

## 31.2 Decimal Input

Use float conversion when the application accepts decimal values:

```python
price = float(input("Enter price: "))
```

Examples include:

- Measurements
- Temperatures
- Average values
- Approximate scientific values

## 31.3 A Decimal String Cannot Be Passed Directly to `int()`

```python
int("8.75")
```

This raises `ValueError`.

By contrast:

```python
float("8.75")
```

succeeds.

## 31.4 Do Not Convert Every Number to Float Automatically

Use the type that matches the problem.

A count of students is normally represented as an integer.

A measured temperature may require a floating-point value.

The goal is to represent the information appropriately.

---

# 32. Floating-Point Precision

Floating-point numbers are useful for many measurements and calculations.

However, their binary representation can produce small rounding differences.

## 32.1 Example

```python
value = 0.1 + 0.2

print(value)
```

A typical output is:

```text
0.30000000000000004
```

The displayed result may differ slightly from the expected decimal expression.

## 32.2 Formatting the Result

```python
value = 0.1 + 0.2

print(f"{value:.2f}")
```

Output:

```text
0.30
```

Formatting controls how a number is displayed.

It does not change the underlying floating-point value into an exact decimal representation.

## 32.3 Approximate Comparison

When comparing computed floating-point values, consider a tolerance.

```python
value = 0.1 + 0.2

print(abs(value - 0.3) < 1e-9)
```

Output:

```text
True
```

This example checks whether the difference is sufficiently small.

The appropriate tolerance depends on the scale and requirements of the calculation.

---

# 33. Truncation and Rounding

`int()` truncates floating-point values toward zero.

It does not round to the nearest integer.

## 33.1 Positive Example

```python
print(int(7.9))
```

Output:

```text
7
```

## 33.2 Negative Example

```python
print(int(-7.9))
```

Output:

```text
-7
```

## 33.3 Using `round()`

```python
print(round(7.9))
```

Output:

```text
8
```

Python's `round()` uses rounding behavior that includes ties-to-even for exact halfway cases.

For example:

```python
print(round(2.5))
print(round(3.5))
```

Output:

```text
2
4
```

## 33.4 Comparison Table

| Expression | Result | Meaning |
|---|---:|---|
| `int(7.9)` | `7` | Truncation toward zero |
| `int(-7.9)` | `-7` | Truncation toward zero |
| `round(7.9)` | `8` | Nearest integer |
| `round(2.5)` | `2` | Ties-to-even behavior |
| `round(3.5)` | `4` | Ties-to-even behavior |

Use the conversion or rounding operation that matches the problem requirement.

Do not use `int()` when the task specifically requires rounding.

---

# 34. Complex Number Conversion

Complex numbers are less common in basic input exercises, but understanding them is part of Python's numeric type system.

## 34.1 Input Format

A complex number may be represented as:

```text
2+3j
```

The imaginary unit is written using `j` in Python.

## 34.2 Convert Text into a Complex Value

```python
value = complex(input("Enter a complex number: "))
```

Valid examples can include:

```text
2+3j
```

```text
4-2j
```

```text
5j
```

```text
7
```

The exact accepted syntax follows Python's complex-number parsing rules.

## 34.3 Read the Components

```python
value = complex("4-2j")

print(value.real)
print(value.imag)
```

Output:

```text
4.0
-2.0
```

## 34.4 Addition

```python
first = complex("2+3j")
second = complex("4+5j")

print(first + second)
```

Output:

```text
(6+8j)
```

## 34.5 Conversion Failure

A string such as:

```text
hello
```

does not represent a valid complex number.

The conversion should be handled with `try` and `except` if the value comes from an untrusted input source.

---

# 35. List Conversion

When input contains multiple items, a program may need to convert each item separately.

## 35.1 Convert a Single Value

```python
number = int("10")
```

## 35.2 Convert Several Values

```python
raw_values = ["10", "20", "30"]

numbers = [int(value) for value in raw_values]

print(numbers)
```

Output:

```text
[10, 20, 30]
```

## 35.3 Use a Loop Instead

```python
raw_values = ["10", "20", "30"]

numbers = []

for value in raw_values:
    numbers.append(int(value))

print(numbers)
```

Output:

```text
[10, 20, 30]
```

Both approaches produce a list of integers.

The list-comprehension approach is compact.

The loop approach may be easier to understand when first learning collections.

## 35.4 Validate Each Element

If one element cannot be converted, list construction using `int()` raises an exception.

A robust implementation should decide whether the list is all-or-nothing or whether individual invalid items should be reported separately.

For most beginner exercises, rejecting invalid input is the safest default.

---

# 36. Common Input Conversion Patterns

## Pattern 1: Read and Convert an Integer

```python
number = int(input("Enter integer: "))
```

## Pattern 2: Read and Convert a Float

```python
number = float(input("Enter decimal value: "))
```

## Pattern 3: Read and Convert a Complex Number

```python
number = complex(input("Enter complex value: "))
```

## Pattern 4: Read Text and Then Convert

```python
raw_value = input("Enter value: ")

number = int(raw_value)
```

## Pattern 5: Handle Invalid Integer Text

```python
try:
    number = int(input("Enter integer: "))
except ValueError:
    print("Invalid integer.")
```

## Pattern 6: Read a Yes/No Answer

```python
answer = input("Continue? ").strip().lower()

if answer in ("yes", "y"):
    print("Yes selected")
elif answer in ("no", "n"):
    print("No selected")
else:
    print("Invalid answer")
```

## Pattern 7: Read Multiple Numbers

```python
values = input("Enter numbers: ").split()

numbers = [int(value) for value in values]
```

## Pattern 8: Convert a Binary String

```python
number = int(input("Enter binary: "), 2)
```

## Pattern 9: Validate an Integer Range

```python
number = int(input("Enter number: "))

if 1 <= number <= 10:
    print("Accepted")
else:
    print("Outside allowed range")
```

## Pattern 10: Convert and Display a String

```python
number = 25

text_value = str(number)

print(text_value)
```

---

# 37. Helper Functions Used in This Project

The Python file uses helper functions to make the examples and interactive menu easier to read.

The helpers centralize recurring tasks instead of repeating the same code throughout the module.

## 37.1 `print_heading()`

This function displays a heading for a section.

It helps separate the different parts of program output.

A clear heading makes it easier to understand which example or problem is currently running.

## 37.2 `read_int()`

This helper is used when the program needs an integer from the user.

It can centralize integer conversion and error handling.

The intended input is a whole number, such as:

```text
10
```

Invalid text should be handled according to the helper's implementation.

## 37.3 `read_float()`

This helper is used when the program needs a floating-point value.

Examples include:

```text
10.5
```

and:

```text
-2.75
```

It provides one consistent place for float conversion.

## 37.4 `read_text()`

This helper is used when the program expects text.

Examples include:

- Names
- Labels
- Descriptions
- Other textual values

Text should not be converted to a number unless a numeric value is actually required.

## 37.5 `read_complex_number()`

This helper is intended for input that should represent a complex number.

Examples include:

```text
2+3j
```

and:

```text
4-5j
```

The helper keeps complex-number input handling separate from the rest of the program.

## 37.6 Boolean Parsing

Boolean parsing requires additional care because a nonempty string is truthy even when the string says `"False"` or `"No"`.

A parser should explicitly recognize the textual values allowed by the application.

## 37.7 Why Use Helpers?

Helpers provide several advantages:

1. Reduce duplicated code.
2. Make the main program easier to read.
3. Keep input-handling behavior consistent.
4. Make error handling easier to maintain.
5. Let different sections reuse the same logic.
6. Make it easier to test input handling independently.
7. Improve the separation between input and processing.

---

# 38. Section 1 — Twelve Examples

The Python program includes twelve demonstrations related to input conversion.

This section explains the principal ideas those demonstrations are intended to teach.

## Example 1: Convert a String to an Integer

```python
raw_value = "25"

number = int(raw_value)

print(number)
print(type(number))
```

Output:

```text
25
<class 'int'>
```

Explanation:

The input is a string.

The `int()` function converts it into an integer.

The resulting variable can be used for integer arithmetic.

## Example 2: Convert a String to a Float

```python
raw_value = "25.75"

number = float(raw_value)

print(number)
print(type(number))
```

Output:

```text
25.75
<class 'float'>
```

Explanation:

The string represents a decimal value.

The `float()` function produces a floating-point result.

## Example 3: Convert an Integer to a Float

```python
number = 25

converted_value = float(number)

print(converted_value)
```

Output:

```text
25.0
```

Explanation:

The numeric value is converted from an integer to a floating-point number.

## Example 4: Convert a Float to an Integer

```python
number = 25.75

converted_value = int(number)

print(converted_value)
```

Output:

```text
25
```

Explanation:

The fractional portion is discarded because `int()` truncates toward zero.

## Example 5: Convert an Integer to a String

```python
number = 250

converted_value = str(number)

print(converted_value)
print(type(converted_value))
```

Output:

```text
250
<class 'str'>
```

Explanation:

The value becomes text.

The distinction matters when concatenating strings or formatting a message.

## Example 6: Convert a String to a Complex Number

```python
raw_value = "2+3j"

number = complex(raw_value)

print(number)
```

Output:

```text
(2+3j)
```

Explanation:

Python recognizes the complex-number representation.

## Example 7: Interpret Text as a Boolean Answer

```python
answer = "yes".strip().lower()

if answer in ("yes", "y", "true", "1"):
    result = True
elif answer in ("no", "n", "false", "0"):
    result = False
else:
    raise ValueError("Invalid Boolean text")

print(result)
```

Output:

```text
True
```

Explanation:

The text is normalized before being compared with explicitly accepted values.

This is different from calling `bool()` on an arbitrary string.

## Example 8: Convert a List of Numeric Strings

```python
raw_values = ["10", "20", "30"]

numbers = [int(value) for value in raw_values]

print(numbers)
```

Output:

```text
[10, 20, 30]
```

Explanation:

Each list item is converted separately.

The result is a list of integers.

## Example 9: Convert Comma-Separated Values

```python
raw_values = "10,20,30"

numbers = [int(value) for value in raw_values.split(",")]

print(numbers)
```

Output:

```text
[10, 20, 30]
```

Explanation:

The string is split into individual values.

Each item is then converted to an integer.

## Example 10: Convert Binary Text to Decimal

```python
binary_text = "1010"

decimal_value = int(binary_text, 2)

print(decimal_value)
```

Output:

```text
10
```

Explanation:

The second argument indicates that the original text is in base `2`.

## Example 11: Convert Multiple Numeric Inputs

```python
raw_values = "10 20 30"

numbers = [int(value) for value in raw_values.split()]

print(numbers)
print(sum(numbers))
```

Output:

```text
[10, 20, 30]
60
```

Explanation:

The text is divided into separate values.

Each item is converted and stored in a list.

The `sum()` function then calculates the total.

## Example 12: Convert and Validate a Number

```python
raw_value = "75"

number = int(raw_value)

if 0 <= number <= 100:
    print("Valid value")
else:
    print("Value outside range")
```

Output:

```text
Valid value
```

Explanation:

Conversion determines whether the text can become an integer.

Range validation determines whether the converted number satisfies the program's requirement.

These are separate steps.

---

# 39. Section 2 — Twelve Solved Problems

The solved-problem section of the Python program provides practice with conversion and simple processing.

The following worked problems explain the core techniques involved.

## Solved Problem 1: Add Two Integer Inputs

Task:

Read two integer values and display their sum.

Solution:

```python
first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))

total = first + second

print("Sum:", total)
```

Sample input:

```text
10
20
```

Output:

```text
Sum: 30
```

Explanation:

Both inputs are converted before addition.

Without conversion, string concatenation could occur instead of numeric addition.

## Solved Problem 2: Add Two Decimal Inputs

Task:

Read two decimal values and calculate their sum.

Solution:

```python
first = float(input("Enter first decimal: "))
second = float(input("Enter second decimal: "))

total = first + second

print("Sum:", total)
```

Sample input:

```text
10.5
2.5
```

Output:

```text
Sum: 13.0
```

Explanation:

The `float()` function allows decimal input.

## Solved Problem 3: Calculate an Average

Task:

Read two numeric values and calculate the average.

Solution:

```python
first = float(input("Enter first value: "))
second = float(input("Enter second value: "))

average = (first + second) / 2

print("Average:", average)
```

Sample input:

```text
80
90
```

Output:

```text
Average: 85.0
```

Explanation:

The values are converted to numbers before arithmetic.

The average is calculated by dividing the total by the count.

## Solved Problem 4: Convert a Number to Text

Task:

Convert a numeric value into a string.

Solution:

```python
number = 100

text_value = str(number)

print(text_value)
print(type(text_value))
```

Output:

```text
100
<class 'str'>
```

Explanation:

`str()` returns a string representation of the number.

## Solved Problem 5: Convert Decimal Text to Float

Task:

Read a decimal number from input.

Solution:

```python
raw_value = input("Enter a decimal value: ")

number = float(raw_value)

print("Converted value:", number)
```

Sample input:

```text
12.75
```

Output:

```text
Converted value: 12.75
```

Explanation:

The input function returns text.

The float conversion makes the value usable in decimal arithmetic.

## Solved Problem 6: Convert Float Text to an Integer

Task:

Read a floating-point value and convert the result to an integer.

Solution:

```python
raw_value = input("Enter a decimal value: ")

number = float(raw_value)

integer_value = int(number)

print(integer_value)
```

Sample input:

```text
18.9
```

Output:

```text
18
```

Explanation:

The program first interprets the value as a float.

It then truncates the result using `int()`.

It does not round to the nearest integer.

## Solved Problem 7: Convert a Complex Number

Task:

Read a complex number and display its components.

Solution:

```python
value = complex(input("Enter a complex number: "))

print("Complex value:", value)
print("Real part:", value.real)
print("Imaginary part:", value.imag)
```

Sample input:

```text
2+3j
```

Output:

```text
Complex value: (2+3j)
Real part: 2.0
Imaginary part: 3.0
```

Explanation:

The `complex()` function parses the input.

The `.real` and `.imag` attributes expose its components.

## Solved Problem 8: Convert Text into a Boolean Answer

Task:

Interpret yes/no text as a Boolean value.

Solution:

```python
answer = input("Enter yes or no: ").strip().lower()

if answer in ("yes", "y"):
    result = True
elif answer in ("no", "n"):
    result = False
else:
    result = None

print("Result:", result)
```

Sample input:

```text
yes
```

Output:

```text
Result: True
```

Explanation:

The program explicitly checks the accepted words.

This avoids incorrectly interpreting `"no"` as true merely because it is a nonempty string.

The `None` value indicates that this simple example did not recognize the response.

A stricter application can reject invalid input or retry.

## Solved Problem 9: Convert a List of Integers

Task:

Convert comma-separated integer text into a list.

Solution:

```python
raw_values = input("Enter integers separated by commas: ")

numbers = [int(value.strip()) for value in raw_values.split(",")]

print(numbers)
```

Sample input:

```text
10, 20, 30
```

Output:

```text
[10, 20, 30]
```

Explanation:

`split(",")` separates the input.

`strip()` removes surrounding spaces from each item.

`int()` converts each item into an integer.

## Solved Problem 10: Convert a Binary Number

Task:

Convert binary text into a decimal integer.

Solution:

```python
binary_text = input("Enter binary number: ")

decimal_value = int(binary_text, 2)

print("Decimal value:", decimal_value)
```

Sample input:

```text
1011
```

Output:

```text
Decimal value: 11
```

Explanation:

The second argument of `int()` specifies base `2`.

The output is the corresponding integer value.

## Solved Problem 11: Calculate a Total from Multiple Inputs

Task:

Read several integers and display their total.

Solution:

```python
raw_values = input("Enter integers separated by spaces: ")

numbers = [int(value) for value in raw_values.split()]

total = sum(numbers)

print("Total:", total)
```

Sample input:

```text
5 10 15
```

Output:

```text
Total: 30
```

Explanation:

The input is split into individual strings.

Each item is converted into an integer.

The sum is then calculated.

This basic example assumes all items are valid integers.

## Solved Problem 12: Validate an Integer Range

Task:

Convert an integer input and verify that the value is between `1` and `100`, inclusive.

Solution:

```python
raw_value = input("Enter an integer from 1 to 100: ")

try:
    number = int(raw_value)

    if 1 <= number <= 100:
        print("Accepted")
    else:
        print("Outside the allowed range")
except ValueError:
    print("Enter a valid integer")
```

Sample input:

```text
75
```

Output:

```text
Accepted
```

Explanation:

The program converts the text.

It handles invalid integer text.

It checks the range only after successful conversion.

This structure separates conversion errors from range errors.

---

# 40. Understanding `SOLVED_PROBLEMS`

The Python module uses a mapping named `SOLVED_PROBLEMS`.

A mapping associates keys with corresponding values.

In Python, dictionaries provide this behavior.

Simple example:

```python
SOLVED_PROBLEMS = {
    "example_one": "Description of the first problem",
    "example_two": "Description of the second problem",
}
```

A dictionary allows related information to be organized under names.

## 40.1 Why Use a Mapping?

A mapping helps group problem-related information in one place.

It can also make it easier to display the available items or select an item for execution.

## 40.2 Viewing the Available Problems

A program can display the keys:

```python
for name in SOLVED_PROBLEMS:
    print(name)
```

The actual project uses its own display function to present the available solved problems.

## 40.3 Selecting a Problem

A menu-driven program can ask the user to select a number.

It then validates the choice and dispatches the associated behavior.

The exact implementation details should be read directly from the Python file.

## 40.4 Why Separate Listing and Execution?

Listing available problems and executing them are different responsibilities.

Separating them helps keep the program organized.

A user can inspect the available exercises before choosing one.

## 40.5 Important Note

The README explains the intended design pattern.

The Python file remains the source of truth for the exact problem names and execution logic.

---

# 41. Section 3 — Ten Unsolved Questions

Attempt the following questions without looking up a complete solution immediately.

The goal is to practice the concepts covered in input conversion.

## Question 1: Integer Conversion

Write a program that accepts an integer as text and converts it into an integer.

Display the converted value and its type.

Requirements:

- Read user input.
- Use `int()`.
- Display the resulting value.
- Display its type.
- Consider what should happen when the input is invalid.

## Question 2: Float Conversion

Write a program that accepts a decimal value and converts it into a float.

Requirements:

- Read the value using `input()`.
- Convert it using `float()`.
- Display the converted value.
- Display the type.
- Handle invalid input.

## Question 3: Sum of Two Values

Write a program that accepts two whole numbers.

Convert both values into integers.

Display their sum.

Your program should not concatenate the original strings.

## Question 4: Average of Three Numbers

Read three numeric values.

Convert them into suitable numeric types.

Calculate the average.

Display the result.

Consider whether integer or floating-point division is more appropriate.

## Question 5: Number to String

Convert an integer into a string.

Display the result and its data type.

Then use the string inside a message.

Compare string concatenation with an f-string.

## Question 6: Boolean Text Parsing

Read a yes/no response.

Convert the textual response into an appropriate Boolean value.

Requirements:

- Accept uppercase and lowercase responses.
- Ignore surrounding spaces.
- Recognize both yes and no.
- Reject unknown answers or ask again.
- Do not rely on `bool()` alone for interpreting English words.

## Question 7: List Conversion

Ask the user to enter several integers separated by commas.

Split the input.

Convert every element into an integer.

Display the resulting list.

Also display the sum of the numbers.

Consider how the program should handle an invalid element.

## Question 8: Binary Conversion

Read a binary number as text.

Convert the text into a decimal integer.

Display the result.

Test the program with:

```text
1010
```

Then test it with invalid binary text containing the digit `2`.

Explain the result.

## Question 9: Range Validation

Ask the user for a numeric score.

Convert the value into an appropriate numeric type.

Accept the value only when it is between `0` and `100`, inclusive.

Display a suitable message for values outside the range.

Handle invalid numeric text separately.

## Question 10: Safe Input Function

Write a reusable function that repeatedly asks for an integer until the user enters valid integer text.

Requirements:

- Use a loop.
- Use `try` and `except`.
- Catch `ValueError`.
- Display a helpful error message.
- Return the accepted integer.
- Test the helper with valid and invalid entries.

---

# 42. Section 4 — Learning Checklist

Use this checklist to review your progress.

## Basic Input

- [ ] I understand the purpose of `input()`.
- [ ] I know that `input()` returns a string.
- [ ] I can explain why `"10"` and `10` are different values.
- [ ] I can read input into a variable.
- [ ] I can display the type of a variable.
- [ ] I understand the difference between input and conversion.

## Integer Conversion

- [ ] I can use `int()` to convert valid integer text.
- [ ] I understand why `int("12.5")` fails.
- [ ] I understand how negative integers behave.
- [ ] I understand that `int()` truncates floating-point values toward zero.
- [ ] I can identify invalid integer input.

## Float Conversion

- [ ] I can use `float()` to convert numeric text.
- [ ] I can process decimal values.
- [ ] I understand that floating-point calculations may have small precision differences.
- [ ] I can format floating-point output.
- [ ] I can explain why a decimal string may be invalid for `int()`.

## Complex Conversion

- [ ] I can use `complex()` to convert suitable input.
- [ ] I understand the role of `j`.
- [ ] I can access `.real`.
- [ ] I can access `.imag`.
- [ ] I can recognize invalid complex-number text.

## String Conversion

- [ ] I can use `str()` to produce text.
- [ ] I understand that string conversion changes the resulting type.
- [ ] I can build a message containing a number.
- [ ] I understand the difference between numeric addition and string concatenation.

## Boolean Conversion

- [ ] I understand that an empty string is falsey.
- [ ] I understand that a nonempty string is truthy.
- [ ] I know why `bool("False")` is `True`.
- [ ] I can parse yes/no text explicitly.
- [ ] I can reject unsupported Boolean responses.

## Collections

- [ ] I can split a string into individual values.
- [ ] I can convert a list of numeric strings.
- [ ] I can use list comprehension for conversions.
- [ ] I can handle surrounding spaces.
- [ ] I know how invalid items affect list conversion.

## Error Handling

- [ ] I can use `try`.
- [ ] I can use `except ValueError`.
- [ ] I can display useful error messages.
- [ ] I understand why conversion errors should be handled.
- [ ] I can write a retry loop.
- [ ] I understand the difference between invalid input and a programming error.

## Validation

- [ ] I understand the difference between conversion and validation.
- [ ] I can check for empty input.
- [ ] I can remove surrounding whitespace.
- [ ] I can validate numeric ranges.
- [ ] I can check the number of values supplied.
- [ ] I can distinguish range errors from conversion errors.

## Program Structure

- [ ] I can understand helper functions.
- [ ] I can read a dictionary mapping.
- [ ] I can navigate a menu-driven program.
- [ ] I can run the Python file.
- [ ] I can test all menu options.
- [ ] I can explain the logic of the examples.

---

# 43. Section 5 — Main Menu

The Python file provides an interactive menu.

Its main options are:

| Option | Purpose |
|---|---|
| `1` | View twelve input-conversion examples |
| `2` | Practice twelve solved problems |
| `3` | View ten unsolved practice questions |
| `4` | View the learning checklist |
| `0` | Exit the program |

## 43.1 Why Use a Menu?

A menu lets the user explore a topic without executing every example in sequence.

The user can select a specific learning activity.

The separation also makes it easier to revisit earlier material.

## 43.2 Menu Input

Menu choices are normally collected as text.

The program then needs to interpret the choice and decide what to do.

For example:

```python
choice = input("Enter your choice: ").strip()
```

In some designs, the program can compare the textual choice directly.

In others, the choice may be converted into an integer:

```python
choice = int(input("Enter your choice: "))
```

If integer conversion is used, invalid menu text needs to be handled.

The project's own main-menu implementation determines the exact behavior.

## 43.3 Invalid Menu Choice

A well-designed menu should display a helpful message when the user enters an unsupported choice.

Example:

```text
Invalid choice. Please select an available option.
```

It should not silently perform an unrelated action.

## 43.4 Exiting

The user can select the exit option to leave the program.

The intended exit behavior is controlled by the main-menu function.

---

# 44. How to Run the Program

Make sure Python 3 is installed.

Open PowerShell or a terminal.

Move to the repository folder:

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"
```

Run the Python file:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\04-Input-Output\04_input_conversion\04_input_conversion.py"
```

If the `python` command is not recognized, check your Python installation and PATH configuration.

On many Windows installations, the following launcher command may also work:

```powershell
py "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\04-Input-Output\04_input_conversion\04_input_conversion.py"
```

The exact command depends on the local environment.

## 44.1 Running the Program from Its Folder

You can also move directly into the topic folder:

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\04-Input-Output\04_input_conversion"
```

Then execute:

```powershell
python "04_input_conversion.py"
```

## 44.2 What Happens When the Program Starts?

The script's main entry point calls the menu function.

The user can select an option and inspect the corresponding content.

The learning examples are organized into sections so that the material can be reviewed repeatedly.

---

# 45. Sample Program Execution

The following examples show the expected behavior of common input-conversion operations.

They are illustrative examples for understanding Python conversion rules.

## 45.1 Integer Conversion

Program:

```python
value = int(input("Enter integer: "))

print(value)
```

Input:

```text
25
```

Output:

```text
25
```

## 45.2 Invalid Integer

Program:

```python
try:
    value = int(input("Enter integer: "))
    print(value)
except ValueError:
    print("Invalid integer.")
```

Input:

```text
hello
```

Output:

```text
Invalid integer.
```

## 45.3 Float Conversion

Program:

```python
value = float(input("Enter decimal: "))

print(value)
```

Input:

```text
12.5
```

Output:

```text
12.5
```

## 45.4 Complex Conversion

Program:

```python
value = complex(input("Enter complex value: "))

print(value)
```

Input:

```text
2+3j
```

Output:

```text
(2+3j)
```

## 45.5 Boolean Text Parsing

Program:

```python
answer = input("Enter yes or no: ").strip().lower()

if answer in ("yes", "y"):
    print(True)
elif answer in ("no", "n"):
    print(False)
else:
    print("Invalid answer")
```

Input:

```text
NO
```

Output:

```text
False
```

## 45.6 Binary Conversion

Program:

```python
number = int(input("Enter binary: "), 2)

print(number)
```

Input:

```text
1111
```

Output:

```text
15
```

## 45.7 Conversion Followed by Range Validation

Program:

```python
try:
    score = int(input("Enter score: "))

    if 0 <= score <= 100:
        print("Valid score")
    else:
        print("Invalid range")
except ValueError:
    print("Invalid integer")
```

Input:

```text
85
```

Output:

```text
Valid score
```

---

# 46. Common Mistakes

This section describes mistakes that frequently appear in beginner Python programs.

## Mistake 1: Assuming `input()` Returns an Integer

Incorrect assumption:

```python
age = input("Enter age: ")
```

The value is text.

Correct conversion:

```python
age = int(input("Enter age: "))
```

The conversion must be appropriate for the actual input.

## Mistake 2: Adding Strings Instead of Numbers

Incorrect for numeric addition:

```python
first = "10"
second = "20"

print(first + second)
```

Output:

```text
1020
```

Correct for numeric addition:

```python
first = int("10")
second = int("20")

print(first + second)
```

Output:

```text
30
```

## Mistake 3: Passing Decimal Text Directly to `int()`

Incorrect:

```python
number = int("10.5")
```

This raises `ValueError`.

When decimal input is intended, use:

```python
number = float("10.5")
```

If an integer result is required after processing, decide explicitly whether truncation or rounding is appropriate.

## Mistake 4: Treating `bool()` as an English Parser

Incorrect assumption:

```python
bool("False") == False
```

The expression actually evaluates to `True`.

Use explicit comparison when interpreting words such as yes, no, true, and false.

## Mistake 5: Ignoring Invalid Values

A statement such as:

```python
number = int(input("Enter number: "))
```

may raise `ValueError`.

Use exception handling when invalid input is a realistic possibility.

## Mistake 6: Forgetting Whitespace

A textual answer may contain surrounding spaces.

Normalize it when that behavior is appropriate:

```python
answer = input("Answer: ").strip().lower()
```

## Mistake 7: Confusing Conversion with Validation

A converted integer may still be outside the permitted range.

Use an additional condition when the application has numeric constraints.

## Mistake 8: Converting Before Checking Input Count

A program expecting three space-separated values should verify that three values were provided before accessing all three positions.

## Mistake 9: Losing the Original Input

Sometimes it is useful to preserve the raw string.

Use separate variables when both the original text and converted result are relevant.

## Mistake 10: Catching Every Exception Without a Reason

Catching every possible exception may hide programming errors.

Handle the expected exception as specifically as practical.

## Mistake 11: Using `int()` When Rounding Is Required

`int(8.9)` produces `8`.

It does not produce `9`.

Use an appropriate rounding operation when required by the problem statement.

## Mistake 12: Assuming a Successful Conversion Means Valid Data

An integer can be successfully converted and still violate the application's requirements.

Validation must follow conversion when constraints exist.

---

# 47. Debugging Strategies

When input conversion does not behave as expected, work through the following steps.

## Step 1: Inspect the Original Input

```python
raw_value = input("Enter value: ")

print(repr(raw_value))
```

`repr()` helps make whitespace and empty strings easier to identify.

## Step 2: Check the Type

```python
print(type(raw_value))
```

This confirms that the original input is a string.

## Step 3: Test Conversion Separately

```python
number = int(raw_value)

print(number)
```

Testing conversion separately can make it easier to identify the source of a failure.

## Step 4: Add Exception Handling

```python
try:
    number = int(raw_value)
except ValueError:
    print("The input cannot be converted to an integer.")
```

## Step 5: Test Boundary Values

Try:

```text
0
1
-1
```

Also try invalid values:

```text
hello
```

```text
12.5
```

```text
```

## Step 6: Test Unexpected Spaces

Try:

```text
 25
```

and:

```text
25 
```

Consider whether the input should accept these formats.

## Step 7: Separate Conversion and Validation

First determine whether conversion succeeds.

Then determine whether the result satisfies the application rules.

This makes debugging easier because the two operations have different purposes.

## Step 8: Read the Full Error Message

Python error messages often identify the operation that failed.

Use the message to locate the likely source of the problem.

Do not remove exception handling simply to hide errors.

---

# 48. Testing Strategy

Testing is essential for input-conversion programs because users can provide values in many different formats.

A program that works for one valid value may still fail for other common inputs.

## 48.1 Test Valid Input

For integer conversion, test:

```text
0
```

```text
10
```

```text
-10
```

For float conversion, test:

```text
0.0
```

```text
12.5
```

```text
-3.75
```

For complex conversion, test several valid complex-number representations.

## 48.2 Test Invalid Input

For integer conversion, test:

```text
hello
```

```text
12.5
```

```text
```

For float conversion, test:

```text
abc
```

```text
12.3.4
```

For binary conversion, test a value containing a digit outside the binary digit set.

## 48.3 Test Whitespace

Consider:

```text
  25
```

```text
25
```

and a string containing only spaces.

Decide which values should be accepted.

## 48.4 Test Boundaries

Suppose an input must be between `0` and `100`.

Test:

```text
0
```

```text
100
```

```text
-1
```

```text
101
```

Boundary tests help identify incorrect comparison operators.

## 48.5 Test Menu Choices

Test:

- Every valid menu choice
- The exit choice
- An unsupported choice
- Alphabetic text where a number is expected
- An empty response where applicable

## 48.6 Test Repeated Input

When a helper retries invalid input, test an interaction containing both invalid and valid attempts.

Example:

```text
hello
25
```

The program should handle the invalid attempt and then accept the valid integer if the helper is designed to retry.

## 48.7 Record Results

A simple testing table can help.

| Test | Input | Expected behavior |
|---|---|---|
| Integer | `25` | Successful conversion |
| Integer | `hello` | Conversion error handled |
| Float | `12.5` | Successful conversion |
| Float | `abc` | Conversion error handled |
| Boolean | `yes` | True according to parser rules |
| Boolean | `no` | False according to parser rules |
| Binary | `1010` | Decimal result `10` |
| Range | `50` | Accepted for the range 0–100 |
| Range | `150` | Rejected for the range 0–100 |
| Empty input | Empty string | Rejected for required numeric input |

The expected behavior depends on how the particular helper and exercise are implemented.

---

# 49. Boundary Testing

Boundary testing checks values at and around a permitted limit.

It is useful whenever the program applies a rule such as:

```python
0 <= number <= 100
```

## 49.1 Inclusive Lower Boundary

If zero is allowed, test zero.

```python
number = 0

print(0 <= number <= 100)
```

Output:

```text
True
```

## 49.2 Inclusive Upper Boundary

If one hundred is allowed, test one hundred.

```python
number = 100

print(0 <= number <= 100)
```

Output:

```text
True
```

## 49.3 Below the Lower Boundary

```python
number = -1

print(0 <= number <= 100)
```

Output:

```text
False
```

## 49.4 Above the Upper Boundary

```python
number = 101

print(0 <= number <= 100)
```

Output:

```text
False
```

## 49.5 Why Boundaries Matter

A condition such as:

```python
number < 100
```

does not include `100`.

A condition such as:

```python
number <= 100
```

does include it.

The correct operator must match the requirement.

---

# 50. Best Practices

Use these principles when writing input-conversion programs.

## 50.1 Choose the Appropriate Type

Do not convert a value to an integer if it genuinely needs a decimal component.

Do not use floating-point arithmetic merely because it is available when the problem requires an integer count.

## 50.2 Use Clear Variable Names

Prefer:

```python
raw_age = input("Enter age: ")
age = int(raw_age)
```

over variable names that do not communicate their purpose.

## 50.3 Handle Expected Conversion Errors

Use `try` and `except` when the input can reasonably be invalid.

## 50.4 Give Helpful Feedback

Explain the expected input format.

For example:

```text
Please enter a whole number.
```

is better than a generic error message.

## 50.5 Normalize Text When Appropriate

Use `strip()` and `lower()` when comparing textual responses and when those transformations match the application's requirements.

## 50.6 Separate Conversion from Validation

The conversion step produces a value of a target type.

The validation step checks whether the value is acceptable.

Keeping these steps distinct improves clarity.

## 50.7 Avoid Duplicating Input Logic

If multiple exercises need the same safe input behavior, use a helper function.

## 50.8 Avoid Silent Data Loss

When processing a list, do not silently skip invalid entries unless the application explicitly requires that behavior.

## 50.9 Test Failure Cases

Test invalid values as carefully as valid values.

## 50.10 Keep Examples Focused

A learning example should demonstrate one principal concept at a time.

Once a concept is understood, combine multiple concepts in a larger exercise.

---

# 51. Real-Life Applications

Input conversion appears in many types of programs.

## 51.1 Student Marks

A program receives marks as text.

The program converts them into numbers before calculating a total or average.

It may then validate whether the marks are inside the permitted range.

## 51.2 Online Shopping

A purchase form receives quantities and prices.

Quantities normally require integer conversion.

Prices may require decimal-aware handling.

The program validates the values before calculating the order total.

## 51.3 Temperature Conversion

A user enters a temperature.

The program converts it to a floating-point value.

It then applies the appropriate temperature-conversion formula.

## 51.4 Survey Application

A user selects yes or no.

The application converts the selected response into a Boolean value using explicit parsing rules.

## 51.5 Command-Line Tools

A command-line program may receive numeric options as text.

The application converts and validates those values before performing the requested task.

## 51.6 Scientific Programs

A scientific application may require integers, floating-point values, or complex numbers.

The input format should match the numerical operation that follows.

## 51.7 Data Import

A file may contain numeric values stored as strings.

The program converts the fields before numerical analysis.

## 51.8 Configuration

A configuration file may store textual values that represent timeouts, counts, thresholds, or Boolean options.

A program must interpret those values according to the application's rules.

---

# 52. Mini Project Ideas

Try these projects after you understand the basic exercises.

## Project 1: Student Marks Calculator

Requirements:

- Read three marks.
- Convert them into suitable numeric values.
- Validate the permitted mark range.
- Calculate the total.
- Calculate the average.
- Display the results.
- Handle invalid numeric input.

## Project 2: Simple Shopping Calculator

Requirements:

- Read the price of an item.
- Read the quantity.
- Convert each value into an appropriate type.
- Validate the values.
- Calculate the total.
- Display the result.
- Decide how decimal values should be represented.

## Project 3: Boolean Survey

Requirements:

- Ask a yes/no question.
- Accept uppercase and lowercase answers.
- Accept the supported short forms if required.
- Convert the text into a Boolean value.
- Reject invalid responses.
- Display the interpreted result.

## Project 4: Binary Converter

Requirements:

- Read binary text.
- Convert it using `int(text, 2)`.
- Handle invalid binary input.
- Display the decimal value.
- Test zero, one, and multi-digit binary values.

## Project 5: Multi-Number Calculator

Requirements:

- Read multiple integers on one line.
- Split the text into individual values.
- Convert each value.
- Calculate the total.
- Calculate the average.
- Handle an empty list.
- Handle invalid values.

## Project 6: Safe Integer Reader

Requirements:

- Write a helper function for integer input.
- Catch `ValueError`.
- Retry after invalid input.
- Return the accepted integer.
- Reuse the function in two or more exercises.

## Project 7: Range-Validated Input

Requirements:

- Request a value.
- Convert it into an integer or float as appropriate.
- Validate a defined range.
- Display useful messages.
- Distinguish conversion errors from range errors.

## Project 8: Complex Number Inspector

Requirements:

- Read a complex number.
- Convert the text into a complex value.
- Display the real component.
- Display the imaginary component.
- Handle invalid input.

---

# 53. Frequently Asked Questions

## Q1. What is input conversion?

Input conversion changes an input value from one data type into another appropriate type.

For example, `int("10")` converts the string `"10"` into the integer `10`.

## Q2. Why does `input()` return a string?

The `input()` function reads a line of text. The program must explicitly interpret that text as an integer, float, complex number, Boolean response, or another required value.

## Q3. What does `int()` do?

It converts appropriate values into integers.

For floating-point input, it truncates toward zero.

## Q4. What does `float()` do?

It converts appropriate values into floating-point numbers.

## Q5. What does `complex()` do?

It converts appropriate values into complex numbers.

## Q6. What does `str()` do?

It produces a string representation of a value.

## Q7. What does `bool()` do?

It converts a value into a Boolean truth value.

## Q8. Why is `bool("False")` true?

The string `"False"` is nonempty. Nonempty strings are truthy regardless of their English meaning.

## Q9. Can `int("12.5")` work?

No. The string `"12.5"` is not a valid integer representation for `int()`.

## Q10. Can `float("12")` work?

Yes. It produces the floating-point value `12.0`.

## Q11. What happens when conversion fails?

The conversion typically raises `ValueError` when the provided value cannot be interpreted as the requested type.

## Q12. How can the program handle invalid input?

Use exception handling, validation, or a retry loop, depending on the requirements.

## Q13. What is `ValueError`?

It is an exception raised when an operation receives a value of an appropriate general type but cannot use that value as required.

## Q14. What is `TypeError`?

It is an exception that commonly indicates an operation received an incompatible type.

## Q15. What is the difference between conversion and validation?

Conversion changes or interprets a value's type.

Validation determines whether the value satisfies application requirements.

## Q16. Why use `strip()`?

It removes leading and trailing whitespace from a string.

## Q17. Why use `lower()`?

It converts letters to lowercase so that textual comparison is consistent.

## Q18. How can multiple inputs be read from one line?

Use `split()` to divide the text into separate values, then convert each value as required.

## Q19. How can a list of numeric strings be converted?

Convert each item individually, often using a loop or list comprehension.

## Q20. How can binary text be converted into a decimal integer?

Use `int(binary_text, 2)`.

## Q21. Does `int()` round a float?

No. It truncates the fractional component toward zero.

## Q22. How is rounding different from truncation?

Rounding selects a nearby value according to the rounding rule. Truncation discards the fractional component toward zero.

## Q23. Can a converted integer still be invalid for a program?

Yes. The integer may be outside the required range or fail another application-specific condition.

## Q24. Why are helper functions useful?

They centralize common behavior, reduce duplicated code, and make programs easier to understand and maintain.

## Q25. Should every conversion use `try` and `except`?

Not necessarily. Exception handling is especially important when the value may be invalid or comes from an external input source.

## Q26. Why should invalid input produce a clear message?

The message helps the user understand the expected format and correct the mistake.

## Q27. Can a string containing only spaces be treated as empty?

After calling `strip()`, a string containing only surrounding whitespace becomes an empty string.

## Q28. Why can decimal calculations show unexpected digits?

Binary floating-point representation cannot exactly represent every decimal fraction.

## Q29. Should all numeric input use `float()`?

No. Choose the numeric type that matches the requirements.

## Q30. What is the main lesson of this topic?

Read input, convert it appropriately, handle invalid data, validate application rules, and then process the value.

---

# 54. Viva Questions and Answers

Use these questions to prepare for classroom discussion, practical examinations, and interviews.

## Basic Questions

### 1. What is the purpose of `input()`?

It collects a line of text from the user and returns it as a string.

### 2. Which function converts text to an integer?

`int()`.

### 3. Which function converts suitable text to a floating-point number?

`float()`.

### 4. Which function converts suitable text to a complex number?

`complex()`.

### 5. Which function produces a string representation of a value?

`str()`.

### 6. Which function converts a value to a Boolean truth value?

`bool()`.

### 7. What is a string?

A string is a sequence of characters represented by the `str` type.

### 8. What is an integer?

An integer is a whole-number value represented by the `int` type.

### 9. What is a floating-point value?

It is a numeric value represented using Python's `float` type.

### 10. What is a Boolean value?

A Boolean value is either `True` or `False`.

## Conversion Questions

### 11. What does `int("10")` return?

It returns the integer `10`.

### 12. What does `float("10")` return?

It returns `10.0`.

### 13. What does `str(25)` return?

It returns the string `"25"`.

### 14. What happens when `int("hello")` is evaluated?

It raises `ValueError`.

### 15. What happens when `float("abc")` is evaluated?

It raises `ValueError`.

### 16. Why does `int("12.5")` fail?

The string contains a decimal representation rather than a valid integer representation for `int()`.

### 17. What does `int(12.9)` return?

It returns `12`.

### 18. What does `int(-12.9)` return?

It returns `-12`.

### 19. Does `int()` round numbers?

No. When converting a float, it truncates toward zero.

### 20. What does `complex("2+3j")` return?

It returns the complex number `(2+3j)`.

## Boolean Questions

### 21. Why is `bool("False")` true?

Because `"False"` is a nonempty string.

### 22. Is `bool("")` true or false?

It is false.

### 23. Is `bool(0)` true or false?

It is false.

### 24. Is `bool(1)` true or false?

It is true.

### 25. How should a program interpret yes/no text?

It should compare normalized text against explicitly accepted true and false values.

## Exception Questions

### 26. What is `ValueError`?

It is an exception used when an operation receives a value that it cannot process as required.

### 27. Why use `try` and `except`?

They allow a program to handle expected exceptions instead of letting the program terminate unexpectedly at that operation.

### 28. Which exception commonly occurs when `int("hello")` is evaluated?

`ValueError`.

### 29. Which exception can occur when adding a string and an integer?

`TypeError`.

### 30. Should a program catch every possible exception?

Not automatically. Specific exception handling is usually clearer when the likely failure is known.

## Validation Questions

### 31. What is input validation?

It checks whether data satisfies application requirements.

### 32. Can a value be converted successfully but still be invalid?

Yes. For example, an integer can be outside the permitted range.

### 33. Why should the program check a range?

A range check enforces requirements such as permitted ages, scores, ratings, or quantities.

### 34. What does `strip()` do?

It removes leading and trailing whitespace.

### 35. What does `lower()` do?

It converts text to lowercase.

## Collection Questions

### 36. What does `split()` do?

It separates a string into parts and returns a list of strings.

### 37. How can a list of numeric strings be converted?

Convert each element with a suitable conversion function.

### 38. What happens if one list item cannot be converted?

The conversion raises an exception unless the program catches and handles the invalid item.

### 39. What does `int("1010", 2)` return?

It returns the integer `10`.

### 40. What does the second argument of `int()` represent?

It specifies the base used to interpret the supplied integer text.

## Program Design Questions

### 41. Why use helper functions?

They reduce duplication and centralize behavior.

### 42. Why preserve the original input?

It can be useful for debugging, reporting errors, or comparing the original text with a normalized version.

### 43. Why separate conversion and validation?

They solve different problems and produce clearer code.

### 44. What is a retry loop?

It repeatedly requests input until the specified stopping condition is met.

### 45. Why test invalid input?

It verifies that the program responds safely to unexpected or incorrectly formatted data.

### 46. What is boundary testing?

It tests values at and around the edges of an allowed range.

### 47. How can an empty required input be rejected?

Check whether the normalized string is empty before processing it.

### 48. Why is a useful error message important?

It explains what went wrong and how the user can correct the input.

### 49. What is the purpose of a menu?

A menu allows the user to choose an available action.

### 50. What is the most important principle in input conversion?

Convert input to the appropriate type, handle expected failures, and validate the resulting value before relying on it.

---

# 55. Quick Revision Tables

## 55.1 Conversion Functions

| Function | Purpose | Example |
|---|---|---|
| `int()` | Convert to integer | `int("10")` |
| `float()` | Convert to float | `float("10.5")` |
| `complex()` | Convert to complex number | `complex("2+3j")` |
| `str()` | Convert to string representation | `str(10)` |
| `bool()` | Convert to truth value | `bool("")` |

## 55.2 Input Examples

| Expression | Typical result |
|---|---|
| `int("10")` | `10` |
| `float("10")` | `10.0` |
| `complex("2+3j")` | `(2+3j)` |
| `str(10)` | `"10"` |
| `bool("")` | `False` |
| `bool("False")` | `True` |
| `int("1010", 2)` | `10` |

## 55.3 Common Exceptions

| Exception | Example | Reason |
|---|---|---|
| `ValueError` | `int("hello")` | Invalid integer text |
| `ValueError` | `float("12.3.4")` | Invalid float text |
| `ValueError` | `complex("hello")` | Invalid complex text |
| `TypeError` | `"10" + 5` | Incompatible operand types |

## 55.4 Input Processing Pipeline

| Step | Action | Example |
|---|---|---|
| 1 | Read input | `input()` |
| 2 | Normalize text when appropriate | `.strip()` |
| 3 | Convert value | `int()` |
| 4 | Handle conversion failure | `try` / `except` |
| 5 | Validate requirements | Conditional checks |
| 6 | Process data | Arithmetic or other operations |
| 7 | Display the result | `print()` |

## 55.5 Integer and Float Selection

| Requirement | Typical choice |
|---|---|
| Number of students | `int` |
| Number of items | `int` |
| Whole-number count | `int` |
| Decimal measurement | `float` |
| Temperature with fractional part | `float` |
| Average value | Often `float` |
| Complex mathematical quantity | `complex` |

The exact representation should match the application requirements.

## 55.6 Validation Checklist

| Question | Purpose |
|---|---|
| Can the value be converted? | Conversion validation |
| Is the result in the allowed range? | Range validation |
| Is the input empty? | Required-field validation |
| Are there the correct number of values? | Input-count validation |
| Are textual choices recognized? | Choice validation |
| Does the value meet the application's requirements? | Business-rule validation |

---

# 56. Important Terms

**Input:** Information supplied to a program.

**Conversion:** Changing a value into a different data type.

**Type casting:** A commonly used term for explicitly changing a value's type.

**String:** A sequence of characters represented by `str`.

**Integer:** A whole-number value represented by `int`.

**Float:** A floating-point value represented by `float`.

**Complex number:** A number containing real and imaginary components.

**Boolean:** A value that is either `True` or `False`.

**Truthiness:** The behavior Python uses to interpret a value as true or false in a Boolean context.

**Parser:** Code that interprets structured input text according to defined rules.

**Validation:** Checking whether input satisfies the requirements of an application.

**Exception:** An event that interrupts ordinary execution and may be handled by the program.

**`ValueError`:** An exception that commonly occurs when a value cannot be used in the requested way.

**`TypeError`:** An exception that commonly occurs when an operation receives an incompatible type.

**`try`:** The block containing code whose specified exceptions may be handled.

**`except`:** The block that handles a matching exception.

**`strip()`:** A string method that removes leading and trailing whitespace.

**`lower()`:** A string method that returns a lowercase version of the text.

**`split()`:** A string method that separates text into parts.

**List comprehension:** A concise syntax for constructing a list from an iterable.

**Range validation:** Checking whether a value falls inside defined boundaries.

**Boundary testing:** Testing values at and near the edges of a permitted range.

**Truncation:** Discarding the fractional part of a number according to the relevant rule; `int()` truncates floats toward zero.

**Rounding:** Selecting a rounded result according to a rounding rule.

**Binary:** A base-2 number system using the digits `0` and `1`.

**Base:** The number system used to interpret a numeric representation.

**Helper function:** A reusable function that performs a specific supporting task.

**Menu-driven program:** A program that offers available actions and lets the user choose among them.

---

# 57. Final Summary

Input conversion is a core Python skill.

The `input()` function returns text.

When a program needs a numeric value, the text must be converted using an appropriate function.

The main conversion functions covered in this topic are:

- `int()`
- `float()`
- `complex()`
- `str()`
- `bool()`

The topic also covers list conversion, binary input, helper functions, exception handling, validation, range checks, and interactive menus.

Remember these key points:

1. `input()` returns a string.
2. Convert user input before performing operations that require a different type.
3. `int()` does not directly convert decimal text such as `"12.5"`.
4. `float()` supports suitable decimal text.
5. `complex()` supports valid complex-number representations.
6. `str()` creates a string representation.
7. `bool("False")` is `True` because the string is nonempty.
8. Interpret yes/no answers using explicit parsing rules.
9. `ValueError` commonly occurs when text cannot be converted as requested.
10. Use exception handling when invalid user input is possible.
11. Conversion and validation are separate operations.
12. Validate ranges according to the application's requirements.
13. Test both valid and invalid inputs.
14. Use helper functions to reduce repeated input-handling logic.
15. Keep variable names and error messages clear.

## Recommended Practice Order

1. Understand the return type of `input()`.
2. Practice integer conversion.
3. Practice float conversion.
4. Understand truncation and rounding.
5. Practice string conversion.
6. Learn complex-number conversion.
7. Understand Boolean truthiness.
8. Build a Boolean text parser.
9. Convert lists of numeric strings.
10. Practice binary conversion.
11. Add exception handling.
12. Add range validation.
13. Complete the twelve solved problems.
14. Attempt the ten unsolved questions.
15. Run the interactive program and review the learning checklist.

**Final learning goal:** Be able to collect user input, convert it to the correct data type, handle invalid values, validate application requirements, and process the resulting data safely.