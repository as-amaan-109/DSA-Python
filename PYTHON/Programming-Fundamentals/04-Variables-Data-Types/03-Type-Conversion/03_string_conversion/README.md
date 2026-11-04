# String Conversion in Python

## 1. Introduction

String conversion is an important concept in Python programming. It involves converting values into strings or converting text into other data types such as integers, floating-point numbers, complex numbers, and Boolean values.

In Python, the `input()` function always returns the entered value as a string. Therefore, whenever a program needs to perform mathematical calculations using user input, the text usually needs to be converted into an appropriate numeric type.

For example:

```python
age = input("Enter your age: ")

print(age)
print(type(age))
```

**Sample output:**

```text
Enter your age: 22
22
<class 'str'>
```

Even though the user entered `22`, Python stores it as the string `"22"`.

To use it as an integer, we can convert it:

```python
age = input("Enter your age: ")
age = int(age)

print(age)
print(type(age))
```

**Sample output:**

```text
Enter your age: 22
22
<class 'int'>
```

This topic covers string conversion, numeric parsing, text formatting, Boolean parsing, text normalization, and error handling.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

- Understand the meaning and importance of string conversion.
- Differentiate between a string and a numeric value.
- Convert integers, floats, Booleans, complex numbers, and `None` into strings.
- Convert valid numeric strings into integers and floating-point numbers.
- Convert binary, octal, and hexadecimal text into integers.
- Understand the use of `str()`, `int()`, `float()`, and `complex()`.
- Use `strip()`, `split()`, `join()`, `lower()`, and `upper()` for text processing.
- Correctly interpret Boolean text such as `"True"`, `"False"`, `"yes"`, and `"no"`.
- Understand the difference between `str()`, `repr()`, and f-strings.
- Handle invalid input with `try` and `except`.
- Write reliable conversion programs that validate user input.

---

## 3. What Is a String in Python?

A string is a sequence of characters enclosed in quotation marks.

Python supports single quotes, double quotes, and triple quotes for writing strings.

### Examples

```python
name = "Amaan"
city = 'Nanded'
message = """I am learning Python."""

print(name)
print(city)
print(message)
```

**Output:**

```text
Amaan
Nanded
I am learning Python.
```

### Checking the Data Type

Python provides the built-in `type()` function to identify the data type of a value.

```python
name = "Amaan"
age = 22
percentage = 85.5

print(type(name))
print(type(age))
print(type(percentage))
```

**Output:**

```text
<class 'str'>
<class 'int'>
<class 'float'>
```

The three variables have different data types:

| Variable | Value | Data type |
|---|---|---|
| `name` | `"Amaan"` | `str` |
| `age` | `22` | `int` |
| `percentage` | `85.5` | `float` |

### Important Point

The text `"100"` and the integer `100` are not the same.

```python
first = "100"
second = 100

print(first, type(first))
print(second, type(second))
```

**Output:**

```text
100 <class 'str'>
100 <class 'int'>
```

Although they look similar when printed, their data types are different.

---

## 4. What Is String Conversion?

String conversion refers to converting a value into a string representation or parsing a string into another supported data type.

There are two primary directions.

### A. Converting a Value into a String

Use `str()` to convert a value into a string representation.

```python
number = 100
text = str(number)

print(text)
print(type(text))
```

**Output:**

```text
100
<class 'str'>
```

### B. Converting a String into Another Data Type

Use an appropriate conversion function to parse valid text.

```python
text = "100"
number = int(text)

print(number)
print(type(number))
```

**Output:**

```text
100
<class 'int'>
```

### Conversion Reference Table

| Conversion | Function | Example | Result |
|---|---|---|---|
| Integer to string | `str()` | `str(25)` | `"25"` |
| Float to string | `str()` | `str(3.5)` | `"3.5"` |
| Boolean to string | `str()` | `str(True)` | `"True"` |
| Integer text to integer | `int()` | `int("25")` | `25` |
| Decimal text to float | `float()` | `float("3.5")` | `3.5` |
| Complex text to complex | `complex()` | `complex("2+3j")` | `(2+3j)` |
| Binary text to integer | `int(text, 2)` | `int("1010", 2)` | `10` |
| Hexadecimal text to integer | `int(text, 16)` | `int("FF", 16)` | `255` |

**Remember:** A conversion succeeds only when the input is acceptable to the conversion function.

---

## 5. The `str()` Function

The `str()` function creates a string representation of a value.

### Syntax

```python
str(value)
```

Here, `value` can be an integer, float, Boolean, complex number, `None`, or another supported object.

### Example 1: Integer to String

```python
number = 250
result = str(number)

print(result)
print(type(result))
```

**Output:**

```text
250
<class 'str'>
```

### Example 2: Float to String

```python
price = 99.75
price_text = str(price)

print(price_text)
print(type(price_text))
```

**Output:**

```text
99.75
<class 'str'>
```

### Example 3: Boolean to String

```python
is_student = True

result = str(is_student)

print(result)
print(type(result))
```

**Output:**

```text
True
<class 'str'>
```

Notice that `str(True)` produces the text `"True"`. It does not produce the Boolean value `True`.

### Example 4: `None` to String

```python
value = None

result = str(value)

print(result)
print(type(result))
```

**Output:**

```text
None
<class 'str'>
```

The result is the string `"None"`, not the special Python value `None`.

### Example 5: Complex Number to String

```python
number = 3 + 4j

result = str(number)

print(result)
print(type(result))
```

**Output:**

```text
(3+4j)
<class 'str'>
```

### When Is `str()` Useful?

The `str()` function is useful when:

- A number must be combined with text using concatenation.
- A value needs to be displayed or stored as text.
- Numeric values must be converted before joining them into a string.
- A program needs a string representation of a value.

---

## 6. Converting Strings to Integers Using `int()`

The `int()` function converts a valid integer value or valid integer text into an integer.

### Syntax

```python
int(value)
```

For text written in another number system, an optional base can be supplied:

```python
int(string, base)
```

### Example 1: Positive Integer Text

```python
text = "125"
number = int(text)

print(number)
print(type(number))
```

**Output:**

```text
125
<class 'int'>
```

### Example 2: Negative Integer Text

```python
text = "-45"
number = int(text)

print(number)
```

**Output:**

```text
-45
```

### Example 3: Integer Text with Surrounding Whitespace

```python
text = "   250   "
number = int(text)

print(number)
```

**Output:**

```text
250
```

Python's integer parser accepts surrounding whitespace.

However, using `strip()` explicitly can be useful when normalizing input before additional validation.

### Example 4: Decimal-Point Text

```python
# This raises ValueError:
# number = int("12.5")

number = int(float("12.5"))

print(number)
```

**Output:**

```text
12
```

The direct conversion `int("12.5")` fails because `"12.5"` is not valid integer text.

The second example first converts the text to a float and then to an integer. The fractional part is truncated toward zero.

Be careful: truncation is not the same as rounding.

```python
print(int(8.9))
print(int(-8.9))
```

**Output:**

```text
8
-8
```

### Example 5: Invalid Integer Text

```python
text = "hello"

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

The `ValueError` is raised because `"hello"` cannot be interpreted as an integer.

---

## 7. Converting Strings to Floats Using `float()`

The `float()` function converts a valid numeric value or numeric string into a floating-point number.

### Syntax

```python
float(value)
```

### Example 1: Decimal Text

```python
text = "12.75"
number = float(text)

print(number)
print(type(number))
```

**Output:**

```text
12.75
<class 'float'>
```

### Example 2: Integer-Looking Text

```python
text = "25"
number = float(text)

print(number)
```

**Output:**

```text
25.0
```

### Example 3: Negative Floating-Point Text

```python
text = "-4.5"
number = float(text)

print(number)
```

**Output:**

```text
-4.5
```

### Example 4: Scientific Notation

```python
text = "1.5e3"
number = float(text)

print(number)
```

**Output:**

```text
1500.0
```

Here, `e3` means multiplication by \(10^3\).

### Example 5: Invalid Floating-Point Text

```python
text = "twelve"

try:
    number = float(text)
    print(number)
except ValueError:
    print("Invalid floating-point text.")
```

**Output:**

```text
Invalid floating-point text.
```

### Checking Whether a Float Is Finite

Python supports values such as `inf` and `nan`. A conversion may succeed even when the result is not a finite number.

For applications that require finite values, use `math.isfinite()`.

```python
import math

text = "125.5"

try:
    number = float(text)

    if math.isfinite(number):
        print("Valid finite number:", number)
    else:
        print("The value must be finite.")

except ValueError:
    print("Invalid numeric text.")
```

**Output:**

```text
Valid finite number: 125.5
```

---

## 8. Converting Text to Complex Numbers

A complex number has a real component and an imaginary component.

Python uses `j` to represent the imaginary unit.

### Syntax

```python
complex(string)
```

### Example 1: Complex Number from Text

```python
text = "3+4j"
number = complex(text)

print(number)
print(type(number))
```

**Output:**

```text
(3+4j)
<class 'complex'>
```

### Example 2: Real Component and Imaginary Component

```python
number = complex("5+2j")

print(number.real)
print(number.imag)
```

**Output:**

```text
5.0
2.0
```

### Example 3: Purely Imaginary Number

```python
number = complex("4j")

print(number)
```

**Output:**

```text
4j
```

### Example 4: Invalid Complex Text

```python
text = "hello"

try:
    number = complex(text)
    print(number)
except ValueError:
    print("Invalid complex-number text.")
```

**Output:**

```text
Invalid complex-number text.
```

---

## 9. Converting Binary, Octal, and Hexadecimal Text

The `int()` function can interpret a string according to a specified number-system base.

A base determines the symbols used to represent numbers.

| Number system | Base | Valid digits |
|---|---:|---|
| Binary | 2 | `0`, `1` |
| Octal | 8 | `0` to `7` |
| Decimal | 10 | `0` to `9` |
| Hexadecimal | 16 | `0` to `9`, `A` to `F` |

### Binary Text to Decimal Integer

```python
binary_text = "1010"

number = int(binary_text, 2)

print(number)
```

**Output:**

```text
10
```

### Octal Text to Decimal Integer

```python
octal_text = "17"

number = int(octal_text, 8)

print(number)
```

**Output:**

```text
15
```

### Hexadecimal Text to Decimal Integer

```python
hex_text = "FF"

number = int(hex_text, 16)

print(number)
```

**Output:**

```text
255
```

### Important Rule

The supplied base must match the text.

```python
# Valid binary:
print(int("1010", 2))

# Invalid binary:
# print(int("102", 2))
```

The second conversion raises `ValueError` because the digit `2` is not valid in base 2.

---

## 10. Boolean String Conversion

Boolean conversion requires special attention because Python distinguishes between a string's truthiness and its written meaning.

### Example 1: Converting a Boolean to Text

```python
value = True
text = str(value)

print(text)
print(type(text))
```

**Output:**

```text
True
<class 'str'>
```

### Example 2: The `bool()` Function

```python
print(bool(""))
print(bool("Python"))
print(bool("False"))
print(bool("0"))
```

**Output:**

```text
False
True
True
True
```

Why does `bool("False")` return `True`?

Because `"False"` is a non-empty string. Python does not interpret the word `"False"` as a Boolean keyword when it is inside quotation marks.

### Correctly Parsing Boolean Text

To interpret words as Boolean values, define the accepted inputs explicitly.

```python
def parse_boolean(text):
    value = text.strip().lower()

    if value in {"true", "t", "yes", "y", "1", "on"}:
        return True

    if value in {"false", "f", "no", "n", "0", "off"}:
        return False

    raise ValueError("Enter a valid Boolean value.")


print(parse_boolean("True"))
print(parse_boolean(" FALSE "))
print(parse_boolean("yes"))
print(parse_boolean("no"))
```

**Output:**

```text
True
False
True
False
```

This approach is useful when collecting settings, choices, and yes-or-no answers from users.

Unrecognized words should be rejected rather than automatically interpreted as `True`.

---

## 11. Removing Unnecessary Whitespace with `strip()`

Sometimes users enter spaces before or after text.

The `strip()` method removes whitespace from both ends of a string.

### Example

```python
text = "   Python   "

print(repr(text))
print(repr(text.strip()))
```

**Output:**

```text
'   Python   '
'Python'
```

The `repr()` function is useful here because it makes surrounding spaces visible.

### Related Methods

| Method | Purpose | Example |
|---|---|---|
| `strip()` | Removes surrounding whitespace on both sides | `"  hi  ".strip()` |
| `lstrip()` | Removes whitespace from the left | `"  hi  ".lstrip()` |
| `rstrip()` | Removes whitespace from the right | `"  hi  ".rstrip()` |
| `lower()` | Converts letters to lowercase | `"PYTHON".lower()` |
| `upper()` | Converts letters to uppercase | `"python".upper()` |
| `capitalize()` | Capitalizes the first character and lowercases the remaining letters | `"pYTHON".capitalize()` |

### Example: Cleaning and Parsing a Number

```python
text = "   450   "
cleaned_text = text.strip()
number = int(cleaned_text)

print(cleaned_text)
print(number)
```

**Output:**

```text
450
450
```

`strip()` cleans the text, while `int()` performs the numeric conversion. These are different operations.

---

## 12. Using `split()` to Process Strings

The `split()` method separates a string into a list of strings.

### Syntax

```python
string.split(separator)
```

The separator is optional. Without one, Python separates the string at whitespace and ignores repeated whitespace between words.

### Example 1: Splitting a Sentence

```python
sentence = "Python is easy to learn"

words = sentence.split()

print(words)
```

**Output:**

```text
['Python', 'is', 'easy', 'to', 'learn']
```

### Example 2: Splitting Comma-Separated Numbers

```python
text = "10,20,30,40"

parts = text.split(",")

print(parts)
```

**Output:**

```text
['10', '20', '30', '40']
```

The elements are still strings.

### Converting Each Element to an Integer

```python
text = "10,20,30,40"

numbers = [int(part.strip()) for part in text.split(",")]

print(numbers)
print(type(numbers[0]))
```

**Output:**

```text
[10, 20, 30, 40]
<class 'int'>
```

The list comprehension converts every separated text item into an integer.

### Calculating the Total

```python
text = "10,20,30,40"

numbers = [int(part.strip()) for part in text.split(",")]

print(sum(numbers))
```

**Output:**

```text
100
```

If any item contains invalid integer text, the conversion raises `ValueError`. A robust program should handle that possibility.

---

## 13. Using `join()` to Combine Strings

The `join()` method combines strings into a single string, using the chosen separator.

### Syntax

```python
separator.join(iterable_of_strings)
```

### Example 1: Joining Words

```python
words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)
```

**Output:**

```text
Python is powerful
```

### Example 2: Joining with a Comma

```python
names = ["Amaan", "Ali", "Sara"]

result = ", ".join(names)

print(result)
```

**Output:**

```text
Amaan, Ali, Sara
```

### Example 3: Joining Numbers After Conversion

The `join()` method requires strings. It cannot join integers directly.

```python
numbers = [10, 20, 30]

result = ", ".join(str(number) for number in numbers)

print(result)
```

**Output:**

```text
10, 20, 30
```

The expression `str(number)` converts each number into text before joining.

---

## 14. Difference Between `str()`, `repr()`, and F-Strings

These tools can all produce strings, but their purposes differ.

### `str()`

Creates a human-friendly string representation.

```python
number = 100
print(str(number))
```

**Output:**

```text
100
```

### `repr()`

Creates a representation useful for debugging and inspection.

```python
text = "Hello\nPython"

print(repr(text))
```

**Output:**

```text
'Hello\nPython'
```

The backslash and `n` make the newline escape sequence visible.

### F-Strings

F-strings insert expressions into a string and support formatting.

```python
name = "Amaan"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```text
My name is Amaan and I am 22 years old.
```

### Formatting Decimal Places

```python
price = 125.6789

print(f"{price:.2f}")
```

**Output:**

```text
125.68
```

The format specifier `:.2f` displays the value with two digits after the decimal point.

The formatted result is a string. The original variable `price` remains a float.

### Comparison Table

| Feature | `str()` | `repr()` | F-string |
|---|---|---|---|
| Main purpose | Human-friendly representation | Inspection and debugging | Interpolation and formatting |
| Accepts expressions inside text | No | No | Yes |
| Supports decimal-place formatting directly | No | No | Yes |
| Returns a string | Yes | Yes | Yes |
| Best known use | Converting values to text | Debugging values | Creating readable output |

---

## 15. Handling Conversion Errors

User input cannot always be trusted. The user may type letters where a number is required or enter data in an unexpected format.

Python provides exception handling to manage such situations.

### Understanding `ValueError`

A `ValueError` commonly occurs when the input type is suitable for a conversion but its contents are invalid for that conversion.

For example:

```python
number = int("hello")
```

This raises `ValueError`.

### Example: Safe Integer Conversion

```python
text = input("Enter an integer: ")

try:
    number = int(text)
    print("Converted number:", number)

except ValueError:
    print("Invalid input. Please enter a whole number.")
```

**Sample output for valid input:**

```text
Enter an integer: 25
Converted number: 25
```

**Sample output for invalid input:**

```text
Enter an integer: hello
Invalid input. Please enter a whole number.
```

### Example: Safe Floating-Point Conversion

```python
text = input("Enter a decimal number: ")

try:
    number = float(text)
    print("Converted value:", number)

except ValueError:
    print("Please enter a valid numeric value.")
```

### Understanding `TypeError`

A `TypeError` commonly occurs when an operation is performed using an inappropriate type.

For example, joining integers directly into a string causes a `TypeError`.

```python
numbers = [10, 20, 30]

# This raises TypeError:
# print(", ".join(numbers))

result = ", ".join(str(number) for number in numbers)
print(result)
```

**Output:**

```text
10, 20, 30
```

### `ValueError` vs. `TypeError`

| Exception | Typical cause | Example |
|---|---|---|
| `ValueError` | The value cannot be parsed as requested | `int("hello")` |
| `TypeError` | An operation receives an incompatible type | `", ".join([1, 2])` |

Good error handling catches expected exceptions and gives a clear explanation without hiding unrelated programming errors.

---

## 16. Recommended Pattern for Safe Conversion

A reliable conversion program generally follows these steps:

1. Read the input.
2. Remove unnecessary surrounding whitespace if appropriate.
3. Validate the input's format.
4. Attempt the conversion.
5. Handle expected conversion errors.
6. Validate the converted value against the program's requirements.
7. Use the value only after validation succeeds.

### Example

```python
def parse_positive_integer(text):
    cleaned_text = text.strip()

    try:
        number = int(cleaned_text)
    except ValueError as error:
        raise ValueError("Enter a valid integer.") from error

    if number <= 0:
        raise ValueError("The number must be positive.")

    return number


try:
    value = parse_positive_integer(" 25 ")
    print("Accepted value:", value)
except ValueError as error:
    print("Error:", error)
```

**Output:**

```text
Accepted value: 25
```

Notice that conversion and validation are separate. A negative number can be a valid integer but still be invalid for a program that requires a positive quantity.

---

## 17. Twelve Examples Covered in This Topic

The Python program demonstrates the following concepts.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Integer to string | `str()` |
| 2 | Boolean to string | Boolean representation |
| 3 | `None` to string | Converting a special value to text |
| 4 | `str()` vs. formatting | Difference between conversion and formatted output |
| 5 | Cleaning integer text | Whitespace and `int()` |
| 6 | Parsing floating-point text | `float()` |
| 7 | Splitting comma-separated numbers | `split()` and integer parsing |
| 8 | Joining words | `join()` |
| 9 | Parsing binary and hexadecimal text | `int()` with a base |
| 10 | Parsing Boolean words | Explicit Boolean validation |
| 11 | Comparing `str()` and `repr()` | Human-readable vs. debugging representation |
| 12 | Parsing complex-number text | `complex()` and error handling |

These examples introduce the fundamental operations used in everyday Python programs.

---

## 18. Twelve Solved Programming Problems

The Python program contains twelve solved problems. Each problem is available through the interactive menu.

| No. | Problem | Main approach |
|---:|---|---|
| 1 | Convert text into an integer | Apply `int()` with error handling |
| 2 | Convert text into a finite float | Apply `float()` and check finiteness |
| 3 | Convert a number into text | Use `str()` and inspect its type |
| 4 | Format a float to two decimal places | Use an f-string format specifier |
| 5 | Parse Boolean words | Normalize text and use explicit accepted values |
| 6 | Convert comma-separated text into integers | Use `split()`, `strip()`, and `int()` |
| 7 | Clean text before conversion | Normalize whitespace |
| 8 | Convert binary text into an integer | Use `int(text, 2)` |
| 9 | Convert hexadecimal text into an integer | Handle the optional prefix and parse using base 16 |
| 10 | Parse complex-number text | Use `complex()` and inspect its components |
| 11 | Normalize a sentence | Use `split()` and `join()` |
| 12 | Build a conversion summary | Attempt supported conversions and handle failures |

### How to Study the Solved Problems

For every problem:

1. Read the problem statement.
2. Identify the input and expected output.
3. Predict the output before running the code.
4. Run the solution.
5. Test at least one invalid input.
6. Explain the conversion and error-handling steps in your own words.

Understanding the logic is more useful than simply memorizing the code.

---

## 19. Ten Unsolved Practice Questions

Try to solve these questions independently before checking other solutions.

### Question 1: String to Integer

Ask the user to enter an integer as text. Convert it into an integer and handle invalid input.

**Example:**

```text
Enter an integer: 45
Converted value: 45
```

### Question 2: String to Finite Float

Accept a numeric string, convert it to a float, and reject invalid or non-finite results.

**Concepts:** `float()`, `math.isfinite()`, `try`, and `except`.

### Question 3: Number to String

Ask the user for their name and age. Display a sentence that includes both values.

**Example:**

```text
My name is Amaan and I am 22 years old.
```

Use string conversion or an f-string.

### Question 4: Decimal Formatting

Ask the user for a floating-point number and display it with exactly three digits after the decimal point.

**Example:**

```text
Original value: 12.34567
Formatted value: 12.346
```

### Question 5: Boolean Text Parser

Write a function that accepts values such as `true`, `false`, `yes`, `no`, `1`, and `0`.

The function should ignore surrounding whitespace and letter case. Unsupported values must be rejected.

### Question 6: Comma-Separated Integer List

Ask the user to enter several integers separated by commas. Convert them into a list and calculate the average.

**Example:**

```text
Enter numbers: 10,20,30
Numbers: [10, 20, 30]
Average: 20.0
```

Handle empty input and invalid list elements.

### Question 7: Binary to Decimal

Accept binary text and convert it into a decimal integer.

**Example:**

```text
Binary: 1011
Decimal: 11
```

Reject digits that are not valid in a binary number.

### Question 8: Hexadecimal to Decimal

Accept a hexadecimal string with or without the `0x` prefix and convert it into a decimal integer.

**Example:**

```text
Hexadecimal: FF
Decimal: 255
```

### Question 9: Normalize a Sentence

Accept a sentence containing unnecessary spaces. Split the sentence into words and join them again using a single space.

**Example:**

```text
Original:  Python    is    easy
Normalized: Python is easy
```

### Question 10: Menu-Driven String Converter

Create a program with options to:

1. Convert numeric text to an integer.
2. Convert numeric text to a float.
3. Parse Boolean text.
4. Convert text into a complex number.
5. Exit the program.

Validate the input and display understandable error messages.

---

## 20. Common Mistakes and Their Solutions

| Mistake | Why it happens | Correct approach |
|---|---|---|
| Assuming `input()` returns an integer | Input is always returned as text | Convert using `int()` where required |
| Writing `int("3.5")` | Decimal-point text is not integer text | Use `float("3.5")` when a decimal is intended |
| Expecting `int(3.9)` to round | `int()` truncates toward zero | Use `round()` when rounding is intended |
| Assuming `bool("False")` is false | Non-empty strings are truthy | Implement an explicit Boolean parser |
| Forgetting to trim input | Unnecessary whitespace may interfere with validation | Use `strip()` when appropriate |
| Assuming `split()` returns integers | `split()` produces strings | Convert each item separately |
| Joining integers directly | `join()` requires strings | Apply `str()` to the items |
| Ignoring invalid conversion errors | Unexpected input may interrupt the program | Handle expected exceptions |
| Treating formatted output as a number | Formatting produces text | Preserve the original numeric variable |
| Accepting every non-empty Boolean word as true | Truthiness is not the same as word interpretation | Define accepted true and false values |
| Ignoring number-system bases | Digits have different meanings in different bases | Use the correct base with `int()` |
| Catching every exception indiscriminately | Unrelated bugs can be hidden | Catch specific expected exceptions |

---

## 21. Important Viva and Interview Questions

### Q1. What is string conversion?

String conversion is the process of creating text representations of values or parsing text into supported data types.

### Q2. What is the use of `str()`?

`str()` creates a string representation of a value.

### Q3. What is the return type of `input()`?

The `input()` function returns a string.

### Q4. What is the difference between `"100"` and `100`?

`"100"` is a string, while `100` is an integer.

### Q5. Why does `int("12.5")` raise `ValueError`?

Because `"12.5"` is not a valid integer string. It can be parsed using `float()`.

### Q6. Does `int(12.9)` round the number?

No. It truncates the fractional part toward zero.

### Q7. Why does `bool("False")` return `True`?

Because `"False"` is a non-empty string. The `bool()` function does not interpret its written meaning.

### Q8. How can Boolean words be parsed correctly?

Normalize the text and check it against explicitly defined true and false values.

### Q9. What is the use of `strip()`?

It removes whitespace from both ends of a string.

### Q10. What is the difference between `split()` and `join()`?

`split()` divides a string into a list of strings. `join()` combines strings into one string.

### Q11. Why can't `join()` directly join a list of integers?

Because the elements must be strings. Convert the integers first.

### Q12. What is `ValueError`?

It is an exception commonly raised when a value cannot be converted into the requested format.

### Q13. What is `TypeError`?

It commonly occurs when an operation receives an inappropriate type.

### Q14. What is the difference between `str()` and `repr()`?

`str()` aims for a human-friendly representation, while `repr()` aims for a useful representation for inspection and debugging.

### Q15. What is an f-string?

An f-string allows expressions and variables to be embedded inside a string using braces.

### Q16. Does an f-string change the original value?

No. It produces a formatted string.

### Q17. How do you convert binary text into an integer?

Use `int(binary_text, 2)`.

### Q18. How do you convert hexadecimal text into an integer?

Use `int(hex_text, 16)`.

### Q19. Why should programs validate input after conversion?

A value can be a valid integer or float but still violate the program's requirements, such as requiring a positive value.

### Q20. Why is exception handling important in conversion programs?

It allows programs to respond to invalid input with understandable messages instead of terminating unexpectedly.

---

## 22. Quick Revision Sheet

| Function or method | Purpose | Example |
|---|---|---|
| `str()` | Convert a value to text | `str(100)` |
| `int()` | Parse integer text | `int("100")` |
| `float()` | Parse floating-point text | `float("10.5")` |
| `complex()` | Parse complex-number text | `complex("2+3j")` |
| `bool()` | Determine truthiness | `bool("Python")` |
| `type()` | Check an object's type | `type("Hello")` |
| `repr()` | Obtain a representation for inspection | `repr("Hello\n")` |
| `strip()` | Remove surrounding whitespace | `"  hi  ".strip()` |
| `split()` | Split text into a list | `"a,b".split(",")` |
| `join()` | Combine strings | `"-".join(["a", "b"])` |
| `lower()` | Convert letters to lowercase | `"YES".lower()` |
| `upper()` | Convert letters to uppercase | `"yes".upper()` |
| `round()` | Round a numeric value | `round(3.14159, 2)` |
| `math.isfinite()` | Check whether a number is finite | `math.isfinite(12.5)` |

### Five Rules to Remember

1. `input()` always returns a string.
2. `str()` creates text; `int()`, `float()`, and `complex()` parse supported numeric text.
3. `bool("False")` returns `True` because the string is non-empty.
4. `split()` returns strings, and `join()` requires strings.
5. Invalid conversion input should be handled deliberately.

---

## 23. Learning Checklist

Mark each item after you understand it and can demonstrate it without copying a solution.

- [ ] I understand the meaning of string conversion.
- [ ] I can explain the difference between strings and numeric values.
- [ ] I can use `str()` with integers, floats, Booleans, and `None`.
- [ ] I can convert valid integer strings using `int()`.
- [ ] I can convert valid decimal strings using `float()`.
- [ ] I can parse complex-number strings using `complex()`.
- [ ] I can convert binary, octal, and hexadecimal text using the correct base.
- [ ] I understand why `bool("False")` returns `True`.
- [ ] I can write a Boolean text parser.
- [ ] I can clean strings using `strip()`.
- [ ] I can split text and convert its elements into numbers.
- [ ] I can join strings using `join()`.
- [ ] I understand the difference between `str()`, `repr()`, and f-strings.
- [ ] I can handle `ValueError` during conversion.
- [ ] I can distinguish a conversion error from a validation error.
- [ ] I have attempted all twelve solved problems.
- [ ] I have attempted all ten unsolved practice questions.
- [ ] I can explain the topic's viva questions in my own words.

---

## 24. Final Summary

String conversion connects text-based input with Python's numeric and logical operations. It is essential for command-line programs, data processing, file handling, forms, and many real-world applications.

The most important functions are `str()`, `int()`, `float()`, and `complex()`. Text-processing methods such as `strip()`, `split()`, and `join()` help prepare data for conversion, while `try` and `except` make conversion programs more reliable.

The best way to master this topic is to practice with valid inputs, invalid inputs, boundary cases, and small programs that combine multiple conversion techniques.

**Practice consistently, understand the reason behind each conversion, and write your own solutions before referring to the completed examples.**