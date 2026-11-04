# Python Explicit Type Conversion — Complete Study Notes

**Week:** 1 — Programming Fundamentals  
**Part:** Variables and Data Types  
**Topic:** Explicit Type Conversion  
**Code File:** `02_explicit_conversion.py`

---

# Table of Contents

1. Introduction to Explicit Type Conversion
2. Why Do We Need Explicit Conversion?
3. Syntax and Basic Rules
4. Integer Conversion Using `int()`
5. Float Conversion Using `float()`
6. String Conversion Using `str()`
7. Boolean Conversion Using `bool()`
8. Complex Number Conversion Using `complex()`
9. Conversion Between Collection Types
10. Converting User Input
11. Truncation, Rounding and Precision
12. Type Conversion Errors and Exception Handling
13. Conversion Compatibility Table
14. Explicit Conversion Versus Implicit Conversion
15. Twelve Detailed Examples
16. Twelve Solved Problems with Logic
17. Ten Unsolved Practice Questions
18. Common Errors and Misconceptions
19. Best Practices
20. Quick Revision Tables
21. Interview and Viva Questions
22. Final Learning Checklist

---

# 1. Introduction to Explicit Type Conversion

**Explicit type conversion** is the process in which a programmer deliberately requests a value to be converted into a particular data type.

Python provides built-in functions for this purpose, including:

- `int()` — integer conversion
- `float()` — floating-point conversion
- `str()` — string representation
- `bool()` — Boolean conversion
- `complex()` — complex-number conversion
- `list()` — list construction
- `tuple()` — tuple construction
- `set()` — set construction
- `dict()` — dictionary construction

### Example

```python
number_text = "100"

number = int(number_text)

print(number)
print(type(number))
```

Output:

```text
100
<class 'int'>
```

The original value is a string containing the characters `"100"`. The explicit call to `int()` converts it into an integer.

## Another example

```python
number = 25

text = str(number)

print(text)
print(type(text))
```

Output:

```text
25
<class 'str'>
```

The number becomes a string representation of its value.

## Important point

Explicit conversion does not mean that every conversion is possible or that every conversion preserves information.

For example:

```python
number = 9.8

print(int(number))
```

Output:

```text
9
```

The fractional part is discarded. This operation truncates toward zero; it does not round to the nearest integer.

---

# 2. Why Do We Need Explicit Conversion?

Explicit conversion is especially important when working with user input, calculations, data processing and text.

## 2.1 Converting input into a number

Python's `input()` function returns a string.

```python
first = input("Enter the first number: ")
second = input("Enter the second number: ")

print(first + second)
```

If the user enters `10` and `20`, the output is:

```text
1020
```

This happens because both values are strings. The `+` operator concatenates them.

To perform numeric addition, convert them to integers:

```python
first = input("Enter the first number: ")
second = input("Enter the second number: ")

result = int(first) + int(second)

print("Sum:", result)
```

With the same inputs:

```text
Sum: 30
```

## 2.2 Formatting messages

```python
age = 22

message = "Age: " + str(age)

print(message)
```

Output:

```text
Age: 22
```

The integer is converted to text before concatenation.

## 2.3 Converting decimal measurements

```python
temperature_text = "36.5"

temperature = float(temperature_text)

print(temperature + 1.5)
```

Output:

```text
38.0
```

The text is first converted into a floating-point value, allowing the program to perform arithmetic.

## 2.4 Handling data from external sources

Explicit conversion is useful when data comes from:

- Console input
- CSV files
- JSON documents
- Text files
- APIs
- Database fields
- Configuration files

Before performing calculations, the program should ensure the data has the expected type and format.

**Remember:** Conversion should be deliberate. A program should not assume that text containing digits is already a numeric value.

---

# 3. Syntax and Basic Rules

The general form of explicit conversion is:

```python
target_value = target_type(source_value)
```

For example:

```python
number = int("50")
price = float("99.5")
text = str(100)
flag = bool(1)
complex_number = complex(3, 4)
```

The conversion function determines the conversion rules.

## Basic syntax table

| Function | Syntax example | Result |
|---|---|---|
| `int()` | `int("50")` | `50` |
| `float()` | `float("2.5")` | `2.5` |
| `str()` | `str(100)` | `"100"` |
| `bool()` | `bool(1)` | `True` |
| `complex()` | `complex(3, 4)` | `(3+4j)` |
| `list()` | `list("ABC")` | `['A', 'B', 'C']` |
| `tuple()` | `tuple([1, 2])` | `(1, 2)` |
| `set()` | `set([1, 1, 2])` | A set containing `1` and `2` |
| `dict()` | `dict([("a", 1)])` | `{'a': 1}` |

These functions do not all behave the same way. Some parse text, some change a numeric representation, and others construct new collections.

## What if conversion fails?

A conversion may raise an exception if the supplied value is invalid or unsupported.

```python
# Raises ValueError:
# int("hello")
```

The string `"hello"` cannot be interpreted as an integer.

Another example:

```python
number = 3 + 4j

# Raises TypeError:
# float(number)
```

Python does not directly convert a complex number into a float because doing so would require choosing what happens to the imaginary component.

---

# 4. Integer Conversion Using `int()`

The `int()` function creates an integer from a compatible input.

## Syntax

```python
int(value)
```

For strings, an optional base can also be supplied:

```python
int(string, base)
```

## 4.1 String to integer

```python
number = int("250")

print(number)
print(type(number))
```

Output:

```text
250
<class 'int'>
```

The string must contain valid integer text.

## 4.2 String with leading or trailing whitespace

```python
number = int("  250  ")

print(number)
```

Output:

```text
250
```

The `int()` conversion accepts surrounding whitespace in numeric strings.

## 4.3 Negative integer string

```python
number = int("-75")

print(number)
```

Output:

```text
-75
```

A valid leading sign is permitted.

## 4.4 Float to integer

```python
number = int(9.8)

print(number)
```

Output:

```text
9
```

The fractional part is discarded.

For negative values, truncation moves toward zero:

```python
print(int(9.8))
print(int(-9.8))
```

Output:

```text
9
-9
```

This is different from floor division, which rounds downward toward negative infinity.

## 4.5 Boolean to integer

Because `bool` is a subclass of `int`, conversion is supported:

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

## 4.6 Convert a binary string to an integer

The optional `base` argument specifies the number system used to interpret the text.

```python
number = int("1010", 2)

print(number)
```

Output:

```text
10
```

The string `"1010"` represents decimal ten in base two.

Other common bases include:

- Base 2: binary
- Base 8: octal
- Base 10: decimal
- Base 16: hexadecimal

Example:

```python
print(int("10", 2))
print(int("10", 8))
print(int("10", 10))
print(int("10", 16))
```

Output:

```text
2
8
10
16
```

## 4.7 Invalid integer conversions

```python
# Raises ValueError:
# int("Python")

# Raises ValueError:
# int("3.5")
```

The second example fails because `"3.5"` is decimal text, not integer text.

When decimal text is provided, use `float()` first if that matches the required operation.

```python
number = int(float("3.5"))

print(number)
```

Output:

```text
3
```

This first parses the value as a float and then truncates it toward zero. Use this two-step approach only when that behavior is intended.

---

# 5. Float Conversion Using `float()`

The `float()` function creates a floating-point number from a compatible numeric value or numeric string.

## Syntax

```python
float(value)
```

## 5.1 Integer to float

```python
number = float(20)

print(number)
print(type(number))
```

Output:

```text
20.0
<class 'float'>
```

## 5.2 Numeric string to float

```python
number = float("3.75")

print(number)
```

Output:

```text
3.75
```

## 5.3 Negative decimal string

```python
number = float("-12.5")

print(number)
```

Output:

```text
-12.5
```

## 5.4 Scientific notation

Python accepts valid floating-point text in scientific notation.

```python
number = float("1.5e3")

print(number)
```

Output:

```text
1500.0
```

Here, `1.5e3` means \(1.5 \times 10^3\).

## 5.5 Boolean to float

```python
print(float(True))
print(float(False))
```

Output:

```text
1.0
0.0
```

## 5.6 Invalid float conversion

```python
# Raises ValueError:
# float("Python")
```

## 5.7 Non-finite floating-point values

Python can represent special floating-point values such as positive infinity, negative infinity and NaN.

```python
print(float("inf"))
print(float("-inf"))
print(float("nan"))
```

The values are commonly displayed as:

```text
inf
-inf
nan
```

These are valid floating-point values, but they are not finite real numbers.

Applications such as calculators and measurement systems may choose to reject them using `math.isfinite()` if only ordinary finite values are acceptable.

---

# 6. String Conversion Using `str()`

The `str()` function returns a string representation of a value.

## Syntax

```python
str(value)
```

## 6.1 Integer to string

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

Output:

```text
100
<class 'str'>
```

## 6.2 Float to string

```python
number = 12.5

text = str(number)

print(text)
print(type(text))
```

Output:

```text
12.5
<class 'str'>
```

## 6.3 Boolean to string

```python
value = True

text = str(value)

print(text)
print(type(text))
```

Output:

```text
True
<class 'str'>
```

The result is a string containing `"True"`. It is not the Boolean value `True`.

## 6.4 None to string

```python
value = None

text = str(value)

print(text)
print(type(text))
```

Output:

```text
None
<class 'str'>
```

Again, the printed text looks like `None`, but its type is `str`.

## 6.5 String representation versus formatted output

```python
price = 19.5

print(str(price))
print(f"{price:.2f}")
```

Output:

```text
19.5
19.50
```

`str()` creates the ordinary string representation. An f-string format specification can control how the value is displayed.

Use the correct technique depending on whether you want a standard representation or a particular display format.

## 6.6 Important limitation

Calling `str()` does not produce a universally reversible representation.

For example, `str(None)` produces the text `"None"`. Parsing that text back into a Python value requires an explicitly defined parsing rule; `str()` itself does not preserve the original data type.

---

# 7. Boolean Conversion Using `bool()`

The `bool()` function converts a value into its truth value.

## Syntax

```python
bool(value)
```

## 7.1 Numeric values

```python
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(2.5))
```

Output:

```text
False
True
True
True
```

Numeric zero is falsy. Non-zero numeric values are truthy.

## 7.2 Strings

```python
print(bool(""))
print(bool("Python"))
print(bool("False"))
print(bool("0"))
```

Output:

```text
False
True
True
True
```

The empty string is falsy. A non-empty string is truthy, even if it contains text such as `"False"` or `"0"`.

## 7.3 Collections

```python
print(bool([]))
print(bool([0]))
print(bool({}))
print(bool({"name": "Amaan"}))
```

Output:

```text
False
True
False
True
```

Empty collections are falsy. Non-empty collections are generally truthy.

## 7.4 Converting user-entered yes/no text

A program should not rely on `bool()` to interpret the meaning of words.

Instead, define accepted responses:

```python
answer = input("Do you agree? (yes/no): ").strip().lower()

if answer in ("yes", "y", "true", "1"):
    result = True
elif answer in ("no", "n", "false", "0"):
    result = False
else:
    result = None
    print("Invalid response.")

print("Parsed result:", result)
```

For input `no`, the result is:

```text
Parsed result: False
```

In this example, `None` means the text could not be interpreted as an accepted answer.

**Important distinction:** `bool()` checks truthiness. It does not parse words into their intended logical meaning.

---

# 8. Complex Number Conversion Using `complex()`

The `complex()` function creates a complex number.

## Syntax

```python
complex(real, imag)
```

Both arguments are optional, and each defaults to zero.

## 8.1 Integer to complex

```python
number = complex(5)

print(number)
```

Output:

```text
(5+0j)
```

## 8.2 Two numeric components

```python
number = complex(3, 4)

print(number)
```

Output:

```text
(3+4j)
```

The first argument is the real component. The second is the imaginary coefficient.

## 8.3 Floating-point components

```python
number = complex(2.5, 1.5)

print(number)
```

Output:

```text
(2.5+1.5j)
```

## 8.4 A complex number from text

```python
number = complex("3+4j")

print(number)
```

Output:

```text
(3+4j)
```

The text must use valid complex-number notation.

## 8.5 Complex to float

Python does not support direct conversion of a complex value into a float.

```python
number = 3 + 4j

# Raises TypeError:
# float(number)
```

The imaginary component cannot be silently discarded.

If the task genuinely requires the real component, retrieve it explicitly:

```python
number = 3 + 4j

real_value = float(number.real)

print(real_value)
```

Output:

```text
3.0
```

This operation discards the imaginary component, so it is appropriate only when the problem specifically calls for the real part.

---

# 9. Conversion Between Collection Types

Python has constructors for converting iterable values into collection types.

## 9.1 String to list

```python
text = "Python"

characters = list(text)

print(characters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

Each character becomes an item in the list.

## 9.2 List to tuple

```python
numbers = [10, 20, 30]

result = tuple(numbers)

print(result)
```

Output:

```text
(10, 20, 30)
```

The tuple is an ordered collection, like a list, but it is immutable.

## 9.3 List to set

```python
numbers = [1, 2, 2, 3, 3]

result = set(numbers)

print(sorted(result))
```

Output:

```text
[1, 2, 3]
```

A set contains unique values. It does not preserve the original list's duplicate items or guarantee their original order.

## 9.4 Tuple to list

```python
values = (10, 20, 30)

result = list(values)

print(result)
```

Output:

```text
[10, 20, 30]
```

A list can be modified after creation.

## 9.5 List of pairs to dictionary

```python
pairs = [
    ("name", "Amaan"),
    ("course", "Python")
]

profile = dict(pairs)

print(profile)
```

Output:

```text
{'name': 'Amaan', 'course': 'Python'}
```

Each pair supplies a key and a value.

For a successful conversion, the input must have an appropriate structure.

## 9.6 Common collection-conversion warning

Converting one collection to another may change its properties.

For example:

- `list()` creates a list.
- `tuple()` creates an immutable tuple.
- `set()` removes duplicate values and does not preserve list order.
- `dict()` creates key-value mappings and requires suitable dictionary input.

Always choose a conversion according to the operation you need.

---

# 10. Converting User Input

The `input()` function returns a string. Explicit conversion is normally required for numeric calculations.

## 10.1 Read an integer

```python
age = int(input("Enter your age: "))

print("Age:", age)
print("Type:", type(age).__name__)
```

If the input is `22`, the result is the integer `22`.

However, invalid input causes an error unless it is handled.

## 10.2 Read a floating-point number

```python
price = float(input("Enter the price: "))

print("Price:", price)
```

This accepts compatible decimal text such as `19.5`.

## 10.3 Handle invalid input

```python
raw_value = input("Enter an integer: ")

try:
    value = int(raw_value)
    print("Converted value:", value)
except ValueError:
    print("Please enter a valid integer.")
```

The program continues normally when the entered value cannot be converted.

## 10.4 Validate ranges after conversion

```python
raw_value = input("Enter marks: ")

try:
    marks = float(raw_value)

    if 0 <= marks <= 100:
        print("Accepted marks:", marks)
    else:
        print("Marks must be between 0 and 100.")

except ValueError:
    print("Enter a valid numeric value.")
```

Conversion checks whether the input can be interpreted as a number. Range validation checks whether that number is acceptable to the application.

These are different tasks.

---

# 11. Truncation, Rounding and Precision

Explicit conversion can change the precision or representation of a value.

## 11.1 Truncation with `int()`

```python
print(int(8.9))
print(int(-8.9))
```

Output:

```text
8
-8
```

`int()` truncates toward zero.

## 11.2 Rounding with `round()`

```python
print(round(8.9))
print(round(8.2))
```

Output:

```text
9
8
```

At exact halfway points, Python's `round()` uses ties-to-even rounding:

```python
print(round(2.5))
print(round(3.5))
```

Output:

```text
2
4
```

## 11.3 Float conversion does not guarantee exact decimal precision

```python
result = float("0.1") + float("0.2")

print(result)
```

Output:

```text
0.30000000000000004
```

This is a floating-point representation issue, not necessarily a programming error.

## 11.4 Display formatting versus conversion

```python
price = 12.5

print(str(price))
print(f"{price:.2f}")
```

Output:

```text
12.5
12.50
```

The format specification `.2f` controls the displayed text. It does not change `price` into a different numeric value.

**Remember:** Do not confuse display formatting, truncation and rounding with ordinary type conversion. They serve different purposes.

---

# 12. Type Conversion Errors and Exception Handling

Two common exceptions associated with conversion are `ValueError` and `TypeError`.

## 12.1 ValueError

`ValueError` commonly occurs when the type or operation is broadly appropriate, but the provided value cannot be interpreted as requested.

Example:

```python
int("hello")
```

This raises `ValueError`.

## 12.2 TypeError

`TypeError` commonly occurs when a conversion or operation is unsupported for the supplied type.

Example:

```python
float(3 + 4j)
```

This raises `TypeError`.

## 12.3 Safely convert an integer string

```python
def parse_integer(text):
    try:
        return int(text)
    except ValueError:
        return None


print(parse_integer("25"))
print(parse_integer("hello"))
```

Output:

```text
25
None
```

In this example, `None` represents failure to parse the input. In a larger program, you may prefer a result structure that distinguishes invalid input from a legitimate value.

## 12.4 Handle multiple conversion-related exceptions

```python
raw_value = input("Enter a number: ")

try:
    value = float(raw_value)

    if not math.isfinite(value):
        print("Please enter a finite number.")
    else:
        print("Converted:", value)

except ValueError:
    print("The text is not a valid floating-point number.")
```

Here, `math.isfinite()` checks whether the result is a finite value. It is a validation rule, not part of `float()` conversion itself.

## 12.5 Avoid unnecessarily broad exception handling

Prefer catching exceptions that you expect and can handle meaningfully.

For ordinary conversion problems, `ValueError` and `TypeError` are often more appropriate than catching every possible exception.

---

# 13. Conversion Compatibility Table

The table below summarizes common results.

| Source value | Conversion | Result | Important note |
|---|---|---|---|
| `"25"` | `int()` | `25` | Valid integer text |
| `"3.5"` | `float()` | `3.5` | Valid decimal text |
| `9.8` | `int()` | `9` | Truncation toward zero |
| `20` | `float()` | `20.0` | Numeric conversion |
| `100` | `str()` | `"100"` | Produces text |
| `False` | `int()` | `0` | Boolean is an integer subclass |
| `"False"` | `bool()` | `True` | Non-empty string |
| `None` | `bool()` | `False` | None is falsy |
| `3 + 4j` | `complex()` | `(3+4j)` | Already complex |
| `3 + 4j` | `float()` | Error | Unsupported direct conversion |
| `"Python"` | `int()` | Error | Invalid integer text |
| `[1, 2]` | `tuple()` | `(1, 2)` | Collection conversion |
| `[1, 1, 2]` | `set()` | `{1, 2}` | Duplicates removed |
| `[("a", 1)]` | `dict()` | `{"a": 1}` | Requires key-value pairs |

A conversion should be selected based on both the source value and the desired target type. Some conversions change representation, some discard information and some are invalid.

---

# 14. Explicit Conversion Versus Implicit Conversion

| Feature | Explicit conversion | Implicit conversion |
|---|---|---|
| Conversion request | Directly requested by the programmer | Handled according to an operation's rules |
| Example | `float(10)` | `10 + 2.5` |
| Control | Programmer chooses a conversion function | Python's operator behavior determines the result |
| Failure possibility | Invalid values or unsupported types can fail | Incompatible operations can fail |
| Information loss | Possible, such as `int(9.8)` | Depends on the operation and types |
| Text parsing | Can explicitly parse numeric text | Numeric-looking strings are not automatically parsed for addition |

### Example: Explicit conversion

```python
number = 10
result = float(number)

print(result)
print(type(result))
```

Output:

```text
10.0
<class 'float'>
```

### Example: Implicit numeric handling

```python
number = 10
result = number + 2.5

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

The difference is that the first example explicitly requests conversion, whereas the second performs a supported mixed numeric operation.

---

# 15. Twelve Detailed Examples

The file `02_explicit_conversion.py` provides these twelve examples.

## Example 1: String to integer

```python
value = int("250")

print(value)
print(type(value).__name__)
```

Output:

```text
250
int
```

**Explanation:** `int()` parses compatible integer text and returns an integer value.

## Example 2: Float to integer

```python
value = int(9.8)

print(value)
```

Output:

```text
9
```

**Explanation:** The fractional part is truncated toward zero.

## Example 3: Integer to float

```python
value = float(20)

print(value)
print(type(value).__name__)
```

Output:

```text
20.0
float
```

**Explanation:** The numeric value is represented using the floating-point type.

## Example 4: Scientific notation

```python
value = float("1.5e3")

print(value)
```

Output:

```text
1500.0
```

**Explanation:** The input is interpreted as \(1.5 \times 10^3\).

## Example 5: Integer to string

```python
value = str(100)

print(value)
print(type(value).__name__)
```

Output:

```text
100
str
```

**Explanation:** The result is a string representation of the integer.

## Example 6: Convert Boolean and None to strings

```python
print(str(True))
print(type(str(True)).__name__)

print(str(None))
print(type(str(None)).__name__)
```

Output:

```text
True
str
None
str
```

**Explanation:** Both calls return strings, even though the original values have different types.

## Example 7: Boolean conversion

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("False"))
```

Output:

```text
False
True
False
True
```

**Explanation:** The truth value depends on whether the object is falsy or truthy. A non-empty string is truthy.

## Example 8: Build a complex number

```python
value = complex(3, 4)

print(value)
print(type(value).__name__)
```

Output:

```text
(3+4j)
complex
```

**Explanation:** The real and imaginary components are supplied separately.

## Example 9: Convert complex text

```python
value = complex("3+4j")

print(value)
print(abs(value))
```

Output:

```text
(3+4j)
5.0
```

**Explanation:** The valid complex-number string is parsed into a complex value. Its magnitude is `5.0`.

## Example 10: String to list

```python
value = list("Python")

print(value)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

**Explanation:** Each character becomes an individual list element.

## Example 11: List to tuple

```python
value = tuple([10, 20, 30])

print(value)
```

Output:

```text
(10, 20, 30)
```

**Explanation:** The iterable is used to create an immutable tuple.

## Example 12: Invalid conversion handling

```python
try:
    int("Python")
except ValueError:
    print("Integer conversion failed.")

try:
    float(3 + 4j)
except TypeError:
    print("Float conversion of a complex value failed.")
```

Output:

```text
Integer conversion failed.
Float conversion of a complex value failed.
```

**Explanation:** `ValueError` and `TypeError` describe different reasons for failure.

---

# 16. Twelve Solved Problems with Logic

The interactive program contains twelve solved problems. Practise each problem with valid and invalid values.

## Problem 1: Convert a string to an integer

**Question:** Read integer text and convert it into an integer.

Example:

```text
Input: 250
Result: 250
Type: int
```

### Logic

1. Read text from the user.
2. Remove surrounding whitespace.
3. Call `int()`.
4. Catch `ValueError` if the text is not valid integer input.
5. Print the converted result and type.

## Problem 2: Convert a string to a float

**Question:** Convert numeric text into a finite floating-point value.

Example:

```text
Input: 12.75
Result: 12.75
Type: float
```

### Logic

Use `float()` to parse the string. Catch `ValueError`, then optionally validate the result using `math.isfinite()` if only finite numbers are accepted.

## Problem 3: Convert a float to an integer

**Question:** Convert a floating-point number to an integer.

Example:

```text
Input: 9.8
Result: 9
```

### Logic

Call `int()` and observe that truncation occurs toward zero.

## Problem 4: Compare truncation with rounding

**Question:** Display both `int(value)` and `round(value)`.

Example:

```text
Input: 8.9
int(value): 8
round(value): 9
```

### Logic

The conversion and rounding functions apply different rules. Compare their outputs rather than assuming they are equivalent.

## Problem 5: Convert a number to a string

**Question:** Convert a numeric value to text and use it in a message.

Example:

```text
Input: 25
Text: 25
Type: str
```

### Logic

Use `str()` to obtain the string representation. The resulting value is text.

## Problem 6: Parse text into a Boolean

**Question:** Accept yes/no answers and produce an actual Boolean value.

Example:

```text
Input: yes
Result: True
Type: bool
```

### Logic

1. Normalize case and surrounding whitespace.
2. Compare the text against accepted yes-style answers.
3. Compare it against accepted no-style answers.
4. Reject unrecognized answers.

Do not use `bool("False")` as a text parser.

## Problem 7: Convert components into a complex number

**Question:** Read a real component and an imaginary coefficient.

Example:

```text
Real component: 3
Imaginary coefficient: 4
Result: (3+4j)
```

### Logic

Use `complex(real_part, imaginary_part)`.

## Problem 8: Convert text into a character list

**Question:** Convert a string into a list containing its characters.

Example:

```text
Input: Code
Result: ['C', 'o', 'd', 'e']
```

### Logic

Use `list(text)`. Each character in the iterable becomes a list element.

## Problem 9: Convert a sentence into a tuple

**Question:** Convert a sentence into a tuple of words.

Example:

```text
Input: Learn Python today
Result: ('Learn', 'Python', 'today')
```

### Logic

First use `split()` to obtain the words, then use `tuple()` to construct an immutable tuple.

## Problem 10: Convert a list into a set

**Question:** Remove duplicate integer values by converting a list into a set.

Example:

```text
Input: 1,2,2,3,3
Unique values: [1, 2, 3]
Unique count: 3
```

### Logic

1. Parse each text item using `int()`.
2. Build a list of integers.
3. Convert the list to a set.
4. Sort the set for predictable display.
5. Count the unique values.

## Problem 11: Convert key-value pairs into a dictionary

**Question:** Parse text such as `name=Amaan,course=Python` into a dictionary.

Expected result:

```text
{'name': 'Amaan', 'course': 'Python'}
```

### Logic

1. Separate the pairs using commas.
2. Separate each pair into a key and value using the first `=`.
3. Trim whitespace.
4. Validate that every pair contains a key.
5. Store the results in a dictionary.

In this exercise, the dictionary's keys and values are strings.

## Problem 12: Choose and apply a conversion

**Question:** Allow the user to choose a target type and attempt a conversion.

Supported examples:

- `int`
- `float`
- `str`
- `bool`
- `complex`

### Logic

1. Read the target type.
2. Read the input value as text.
3. Select the requested conversion.
4. Validate Boolean words explicitly.
5. Catch conversion errors.
6. Display the value and its final type.

This problem combines several concepts from the chapter into one small utility.

---

# 17. Ten Unsolved Practice Questions

Solve these independently. Use separate practice files if required.

## Practice 1: Convert Binary Text

Convert the string `"1010"` into an integer using the appropriate base argument.

Expected numeric value:

```text
10
```

Also test an invalid binary string.

## Practice 2: Safe Integer Parser

Create a function that accepts a string and returns an integer if conversion succeeds. Return `None` for invalid input.

Test:

- `"25"`
- `"-10"`
- `"3.5"`
- `"Python"`

## Practice 3: Celsius to Fahrenheit

Read a temperature as text, convert it to `float`, and calculate Fahrenheit using:

\[
F=\frac{9}{5}C+32
\]

Test a normal temperature and invalid input.

## Practice 4: Boolean Text Parser

Write a function that accepts yes/no-style text and returns `True` or `False`. Reject unrecognized responses instead of automatically treating every non-empty string as `True`.

## Practice 5: Complex String Conversion

Convert a string such as `"3+4j"` into a complex number. Display its real component, imaginary coefficient and magnitude.

Handle invalid complex-number text.

## Practice 6: CSV-Style Integer List

Read comma-separated integer values, convert them into a list, and then construct a set to remove duplicates.

Handle invalid values such as `"hello"`.

## Practice 7: Convert Numeric Strings into a List

Given a sequence of comma-separated values, convert each valid integer string into an integer.

Decide whether your function should reject the entire input or report individual invalid items.

## Practice 8: Convert Inputs into a Tuple

Read three numeric strings and convert them into a tuple of floating-point values.

Example structure:

```text
(1.5, 2.5, 3.5)
```

Validate all three inputs.

## Practice 9: Key-Value Conversion

Convert text containing comma-separated `key=value` pairs into a dictionary.

Handle:

- Missing `=`
- Empty keys
- Extra spaces
- Duplicate keys

Document the behavior your program chooses for duplicate keys.

## Practice 10: Menu-Driven Converter

Create a converter that allows the user to select `int`, `float`, `str`, `bool` or `complex`.

The program should:

- Display a menu.
- Validate input.
- Catch conversion errors.
- Show the converted value and type.
- Allow repeated conversions.
- Exit cleanly when requested.

---

# 18. Common Errors and Misconceptions

## Mistake 1: Assuming `int()` rounds a float

```python
print(int(9.8))
```

Output:

```text
9
```

Use `round()` when rounding is actually required.

## Mistake 2: Converting invalid text

```python
# Raises ValueError:
# int("hello")
```

Validate input or handle the expected exception.

## Mistake 3: Using `bool()` to interpret text

```python
print(bool("False"))
```

Output:

```text
True
```

A non-empty string is truthy. Parse words into Boolean values explicitly.

## Mistake 4: Treating `str()` as a reversible conversion

```python
value = None
text = str(value)

print(type(text))
```

Output:

```text
<class 'str'>
```

Converting a value to text does not automatically preserve its original type.

## Mistake 5: Converting a complex value directly into a float

```python
number = 3 + 4j

# Raises TypeError:
# float(number)
```

Access the real component only when the calculation specifically requires it.

## Mistake 6: Confusing conversion with formatting

```python
price = 12.5

print(str(price))
print(f"{price:.2f}")
```

Output:

```text
12.5
12.50
```

The first expression produces the usual string representation. The second controls how the number is displayed.

## Mistake 7: Forgetting that set conversion removes duplicates

```python
values = [1, 1, 2, 3]

print(sorted(set(values)))
```

Output:

```text
[1, 2, 3]
```

A set is not a replacement for a list when duplicate values and original ordering matter.

## Mistake 8: Ignoring invalid numeric values

A value may be successfully parsed as a float but still be unsuitable for a particular application, such as when it is NaN or infinite.

Conversion and validation are separate steps.

---

# 19. Best Practices

1. Choose the conversion function according to the desired target type.
2. Validate user input before using it in calculations.
3. Catch expected conversion exceptions.
4. Remember that `int()` truncates floating-point values toward zero.
5. Use `round()` when the task specifically requires rounding.
6. Use `str()` or f-strings when producing text.
7. Parse Boolean words explicitly instead of relying on `bool()`.
8. Avoid discarding the imaginary component of a complex number without a clear reason.
9. Remember that collection conversion may alter ordering, uniqueness or mutability.
10. Separate conversion from range validation.
11. Do not assume that all conversions are reversible.
12. Print the type after conversion when learning or debugging.
13. Test empty values, invalid text, boundary values and negative numbers.
14. Make conversion errors understandable to the user.

---

# 20. Quick Revision Tables

## Conversion functions

| Function | Example | Purpose |
|---|---|---|
| `int()` | `int("25")` | Creates an integer |
| `float()` | `float("2.5")` | Creates a float |
| `str()` | `str(100)` | Creates a string representation |
| `bool()` | `bool(1)` | Evaluates an object's truth value |
| `complex()` | `complex(3, 4)` | Creates a complex number |
| `list()` | `list("ABC")` | Creates a list |
| `tuple()` | `tuple([1, 2])` | Creates a tuple |
| `set()` | `set([1, 1, 2])` | Creates a set of unique values |
| `dict()` | `dict([("a", 1)])` | Creates a dictionary |

## Important outcomes

| Expression | Result | Key lesson |
|---|---|---|
| `int(9.8)` | `9` | Truncation |
| `int(-9.8)` | `-9` | Truncation toward zero |
| `float(10)` | `10.0` | Integer to float |
| `str(True)` | `"True"` | Boolean to text |
| `bool("False")` | `True` | Non-empty string |
| `complex(3, 4)` | `(3+4j)` | Complex construction |
| `int("1010", 2)` | `10` | Base conversion |
| `list("ABC")` | `['A', 'B', 'C']` | String to character list |
| `tuple([1, 2])` | `(1, 2)` | List to tuple |
| `set([1, 1, 2])` | A set containing `1` and `2` | Duplicate removal |
| `float(3+4j)` | `TypeError` | Unsupported conversion |

---

# 21. Important Interview and Viva Questions

### Q1. What is explicit type conversion?

It is a conversion that the programmer deliberately requests, commonly using built-in functions such as `int()`, `float()` and `str()`.

### Q2. What does `int()` do?

It converts compatible input into an integer. When given a float, it truncates toward zero.

### Q3. What does `float()` do?

It converts compatible numeric values or numeric strings into a floating-point number.

### Q4. What is the use of `str()`?

It returns a string representation of a value.

### Q5. What does `bool()` do?

It converts an object to its truth value, `True` or `False`.

### Q6. Why does `bool("False")` return `True`?

Because the string is non-empty. `bool()` evaluates truthiness rather than parsing the word.

### Q7. How do you create a complex number?

Use a literal such as `3 + 4j` or a call such as `complex(3, 4)`.

### Q8. Can a complex number be directly converted to a float?

No. Python raises `TypeError` for direct complex-to-float conversion.

### Q9. What is the difference between `int(9.8)` and `round(9.8)`?

`int(9.8)` produces `9` by truncation, while `round(9.8)` produces `10`.

### Q10. What is the difference between `ValueError` and `TypeError`?

`ValueError` commonly indicates that a supplied value cannot be interpreted as requested. `TypeError` commonly indicates that the operation or conversion is not supported for the given type.

### Q11. What is base conversion with `int()`?

The optional base argument determines how integer text is interpreted. For example, `int("1010", 2)` returns decimal `10`.

### Q12. What does `list("Python")` return?

It returns a list containing the characters of `"Python"` as individual elements.

### Q13. What is the difference between list-to-tuple and list-to-set conversion?

Tuple conversion retains the sequence and creates an immutable tuple. Set conversion keeps unique elements without guaranteeing original ordering.

### Q14. Does converting a number to a string change the original variable's type?

No. The conversion returns a string value. The original variable keeps its original value and type unless reassigned.

### Q15. Why should conversion errors be handled?

Invalid input can cause exceptions. Handling expected conversion errors lets the program report the problem instead of terminating unexpectedly.

### Q16. What is the difference between conversion and validation?

Conversion creates or parses a value of a requested type. Validation checks whether that value meets the application's rules.

### Q17. Why should a program not use `bool()` to parse a yes/no response?

Because any non-empty string, including `"no"` and `"False"`, is truthy. The program must define and parse the accepted answers explicitly.

### Q18. Does every conversion preserve the original information?

No. For example, integer conversion from a float discards its fractional part, and set conversion removes duplicate elements.

### Q19. What is an example of explicit conversion for user input?

`int(input("Enter a number: "))` converts the returned input string into an integer if the text is valid.

### Q20. What is the benefit of using `type()` after conversion?

It helps verify which type was produced and makes debugging type-related behavior easier.

---

# 22. Final Learning Checklist

Before moving to the next topic, make sure you can:

- [ ] Explain explicit type conversion.
- [ ] Convert compatible values using `int()`.
- [ ] Convert numbers and numeric text using `float()`.
- [ ] Explain truncation versus rounding.
- [ ] Convert values into strings using `str()`.
- [ ] Understand how `bool()` handles truthy and falsy values.
- [ ] Parse yes/no text explicitly.
- [ ] Construct complex values using `complex()`.
- [ ] Convert strings and collections using `list()`, `tuple()`, `set()` and `dict()`.
- [ ] Distinguish `ValueError` from `TypeError`.
- [ ] Validate numeric inputs after conversion.
- [ ] Understand when a conversion can lose information.
- [ ] Complete the twelve solved problems.
- [ ] Attempt all ten unsolved practice questions.
- [ ] Explain the result and the resulting type for your conversions.

---

## Final Summary

Explicit type conversion gives the programmer control over how values are represented and processed.

Remember the key functions:

- `int()` for integer conversion.
- `float()` for floating-point conversion.
- `str()` for string representation.
- `bool()` for truth-value conversion.
- `complex()` for complex values.
- `list()`, `tuple()`, `set()` and `dict()` for collection construction.

The most important habit is to understand the conversion rules, validate the result when needed, handle errors appropriately and recognize when information may be lost.
