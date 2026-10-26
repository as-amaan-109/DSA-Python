# Python Type Conversion — Complete Study Notes

**Week:** 1 — Programming Fundamentals  
**Part:** Variables and Data Types  
**Section:** `03-Type-Conversion`  
**Language:** Python

---

# Table of Contents

1. Introduction to Type Conversion
2. Why Is Type Conversion Important?
3. Type Conversion vs Type Casting
4. Implicit Type Conversion
5. Numeric Promotion Rules
6. Explicit Type Conversion
7. Integer Conversion
8. Float Conversion
9. String Conversion
10. Boolean Conversion
11. Complex Number Conversion
12. Converting User Input
13. Converting Collections
14. Conversion Compatibility Table
15. Common Errors and Exceptions
16. Practical Examples
17. Type Conversion in Real Applications
18. Four-Topic Learning Roadmap
19. Complete Folder Structure
20. Practice and Revision
21. Common Interview and Viva Questions
22. Learning Checklist
23. Git Commit and Push

---

# 1. Introduction to Type Conversion

**Type conversion** is the process of converting a value from one data type to another.

In Python, variables may refer to integers, floating-point numbers, strings, Booleans, complex numbers and other data types. Sometimes an operation requires a different type from the one currently available.

For example, the `input()` function returns text. If you want to perform arithmetic on a number entered by a user, you generally need to convert that text into an appropriate numeric type.

### Example

```python
age_text = "22"

age = int(age_text)

print(age)
print(type(age))
```

Output:

```text
22
<class 'int'>
```

The original value `"22"` is a string. The `int()` function converts it into the integer `22`.

## Another example

```python
number = 10
decimal_number = float(number)

print(decimal_number)
print(type(decimal_number))
```

Output:

```text
10.0
<class 'float'>
```

Here, the integer `10` is converted into a floating-point value, `10.0`.

## Important terms

| Term | Meaning |
|---|---|
| Source type | The type of the original value |
| Target type | The type you want to obtain |
| Conversion | The process of producing a value of the target type |
| Implicit conversion | Python automatically converts compatible values in certain operations |
| Explicit conversion | The programmer requests a conversion using a function or another operation |

Understanding these concepts will help you write programs that accept input, process data and produce correct results.

---

# 2. Why Is Type Conversion Important?

Type conversion is used throughout Python programming.

## 2.1 Processing user input

```python
first = input("Enter the first number: ")
second = input("Enter the second number: ")

result = int(first) + int(second)

print("Sum:", result)
```

If the user enters `10` and `20`, the output is:

```text
Sum: 30
```

Without conversion, the values would be strings.

```python
first = "10"
second = "20"

print(first + second)
```

Output:

```text
1020
```

The `+` operator joins strings rather than performing numeric addition.

## 2.2 Calculating averages

```python
marks = [80, 75, 90]

average = sum(marks) / len(marks)

print(average)
```

Output:

```text
81.66666666666667
```

Division produces a floating-point result in this example.

## 2.3 Formatting output

```python
age = 22

message = "My age is " + str(age)

print(message)
```

Output:

```text
My age is 22
```

The `str()` function converts the integer into text so it can be joined to another string.

## 2.4 Working with different sources of data

Data can come from:

- User input
- Text files
- CSV files
- JSON documents
- APIs
- Databases
- External applications

These sources may represent values using different data types or text formats. Converting values carefully helps prepare them for calculations and other operations.

---

# 3. Type Conversion vs Type Casting

The terms *type conversion* and *type casting* are often used interchangeably in beginner Python material.

A useful way to distinguish them in this section is:

- **Implicit conversion:** Python performs a compatible conversion automatically as part of an operation.
- **Explicit conversion:** The programmer directly requests a conversion, typically using functions such as `int()`, `float()`, `str()` and `complex()`.

## Example: Implicit conversion

```python
number = 10
decimal_number = 2.5

result = number + decimal_number

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

Python handles this mixed numeric operation and returns a floating-point value.

## Example: Explicit conversion

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

The programmer explicitly called `float()`.

### Important note

Explicit conversion does not guarantee that every input can be converted successfully, nor does it guarantee that information is preserved.

For example, converting a floating-point value into an integer discards its fractional part:

```python
number = 9.8

result = int(number)

print(result)
```

Output:

```text
9
```

This is truncation toward zero, not rounding to the nearest integer.

---

# 4. Implicit Type Conversion

Implicit type conversion occurs when Python automatically handles a compatible conversion during an operation.

It is most commonly introduced through numeric operations involving integers and floating-point numbers.

## Example 1: Integer and float

```python
a = 10
b = 2.5

result = a + b

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

The result is a `float`.

## Example 2: Integer multiplication with float

```python
quantity = 4
price = 19.5

total = quantity * price

print(total)
print(type(total))
```

Output:

```text
78.0
<class 'float'>
```

## Example 3: Integer division

```python
result = 7 / 2

print(result)
print(type(result))
```

Output:

```text
3.5
<class 'float'>
```

The `/` operator produces a floating-point result for ordinary numeric operands, including when both operands are integers.

## Example 4: Division using `//`

```python
result = 7 // 2

print(result)
print(type(result))
```

Output:

```text
3
<class 'int'>
```

The result here is an integer because both operands are integers.

However, when a floating-point operand is involved, floor division can produce a float:

```python
result = 7.0 // 2

print(result)
print(type(result))
```

Output:

```text
3.0
<class 'float'>
```

## What does implicit conversion not do?

Python does not automatically convert every value into the type you might expect.

```python
number = "10"

# This raises TypeError:
# result = number + 5
```

The string `"10"` must be converted explicitly before numeric addition can be performed.

---

# 5. Numeric Promotion Rules

Python supports several numeric types, including:

- `int`
- `float`
- `complex`

In mixed numeric expressions, Python generally promotes the values to a compatible numeric type.

A simplified overview is:

| Operation | Example | Result type |
|---|---|---|
| Integer with integer using `+` | `10 + 5` | `int` |
| Integer with float using `+` | `10 + 2.5` | `float` |
| Float with float using `*` | `2.5 * 4.0` | `float` |
| Integer with complex using `+` | `10 + 2j` | `complex` |
| Float with complex using `*` | `2.5 * (1 + 2j)` | `complex` |
| Integer division using `/` | `7 / 2` | `float` |

## Example: Integer and complex

```python
integer_value = 5
complex_value = 2 + 3j

result = integer_value + complex_value

print(result)
print(type(result))
```

Output:

```text
(7+3j)
<class 'complex'>
```

## Example: Float and complex

```python
float_value = 2.5
complex_value = 1 + 2j

result = float_value * complex_value

print(result)
print(type(result))
```

Output:

```text
(2.5+5j)
<class 'complex'>
```

## Important limitation

Not every combination is compatible.

For example, adding a string and an integer directly raises a `TypeError`. Python's automatic numeric promotion rules do not mean that arbitrary types can be combined.

---

# 6. Explicit Type Conversion

Explicit type conversion occurs when a programmer asks Python to convert a value.

Common conversion functions include:

| Function | Purpose |
|---|---|
| `int()` | Converts a compatible value to an integer |
| `float()` | Converts a compatible value to a float |
| `str()` | Creates a string representation |
| `bool()` | Converts an object to its truth value |
| `complex()` | Creates a complex number |
| `list()` | Creates a list from an iterable |
| `tuple()` | Creates a tuple from an iterable |
| `set()` | Creates a set from an iterable |
| `dict()` | Constructs a dictionary from a suitable input |

The conversion depends on the input value and the rules of the requested type.

### Example

```python
integer_value = int("25")
float_value = float("3.14")
text_value = str(100)
boolean_value = bool(1)
complex_value = complex(2, 3)

print(integer_value)
print(float_value)
print(text_value)
print(boolean_value)
print(complex_value)
```

Output:

```text
25
3.14
100
True
(2+3j)
```

Some conversions can lose information, while others can fail if the input is not compatible.

---

# 7. Integer Conversion

The `int()` function converts compatible values to an integer.

## 7.1 String to integer

```python
value = int("250")

print(value)
print(type(value))
```

Output:

```text
250
<class 'int'>
```

The string must represent an integer in a format accepted by Python.

## 7.2 Float to integer

```python
value = int(9.8)

print(value)
```

Output:

```text
9
```

For floating-point values, `int()` truncates toward zero.

```python
print(int(9.8))
print(int(-9.8))
```

Output:

```text
9
-9
```

It does not perform conventional rounding.

## 7.3 Invalid string conversion

```python
# Raises ValueError:
# int("hello")
```

Python cannot interpret `"hello"` as an integer.

## 7.4 Integer conversion and rounding

Compare:

```python
print(int(9.8))
print(round(9.8))
```

Output:

```text
9
10
```

`int()` truncates toward zero, whereas `round()` performs rounding according to Python's rounding rules.

When the value is exactly halfway between two integers, Python's built-in `round()` uses ties-to-even rounding.

```python
print(round(2.5))
print(round(3.5))
```

Output:

```text
2
4
```

**Remember:** Choose `int()` or `round()` according to the result you actually need.

---

# 8. Float Conversion

The `float()` function converts compatible numeric values or numeric strings into a floating-point number.

## 8.1 Integer to float

```python
value = float(20)

print(value)
print(type(value))
```

Output:

```text
20.0
<class 'float'>
```

## 8.2 String to float

```python
value = float("3.75")

print(value)
```

Output:

```text
3.75
```

## 8.3 Scientific notation

```python
value = float("1.5e3")

print(value)
```

Output:

```text
1500.0
```

## 8.4 Invalid float conversion

```python
# Raises ValueError:
# float("Python")
```

The string does not represent an accepted numeric value.

## 8.5 Float precision

```python
result = 0.1 + 0.2

print(result)
```

Output:

```text
0.30000000000000004
```

This happens because many decimal fractions do not have exact finite representations in binary floating-point arithmetic.

For precise monetary calculations, consider an appropriate decimal-based approach instead of relying only on `float`.

---

# 9. String Conversion

The `str()` function returns a string representation of a value.

## 9.1 Integer to string

```python
age = 22

text = str(age)

print(text)
print(type(text))
```

Output:

```text
22
<class 'str'>
```

## 9.2 Float to string

```python
price = 99.5

text = str(price)

print(text)
print(type(text))
```

Output:

```text
99.5
<class 'str'>
```

## 9.3 Boolean to string

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

The result is a string containing the characters `True`, not a Boolean value.

## 9.4 None to string

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

Again, the result is text. It is not the special Python value `None`.

## 9.5 String representation versus numeric conversion

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

The numeric value is represented as text, which can be useful for constructing messages, reports and formatted output.

---

# 10. Boolean Conversion

The `bool()` function converts an object into its truth value.

## Common falsy values

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `()`
- `{}`
- `set()`

Most other ordinary non-empty values are truthy.

## Example

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([0]))
```

Output:

```text
False
True
False
True
False
True
```

Notice that `[0]` is truthy because the list is non-empty.

## Boolean conversion does not parse words

```python
print(bool("False"))
print(bool("True"))
```

Output:

```text
True
True
```

Both strings are non-empty, so both convert to `True`.

To interpret yes/no text as an answer, parse the accepted values explicitly.

```python
answer = input("Do you agree? (yes/no): ").strip().lower()

if answer in ("yes", "y", "true", "1"):
    result = True
elif answer in ("no", "n", "false", "0"):
    result = False
else:
    result = None

print(result)
```

---

# 11. Complex Number Conversion

The `complex()` function constructs a complex number from compatible values.

## 11.1 Integer to complex

```python
value = complex(5)

print(value)
```

Output:

```text
(5+0j)
```

## 11.2 Real and imaginary components

```python
value = complex(3, 4)

print(value)
```

Output:

```text
(3+4j)
```

## 11.3 String to complex

```python
value = complex("3+4j")

print(value)
```

Output:

```text
(3+4j)
```

The string must use valid Python complex-number notation.

## 11.4 Complex to integer

A direct conversion from a non-real complex number to an integer is not supported.

```python
value = 3 + 4j

# Raises TypeError:
# int(value)
```

The same restriction applies to converting a complex number directly to a float.

If a calculation genuinely requires the real component, access it explicitly:

```python
value = 3 + 4j

print(int(value.real))
```

Output:

```text
3
```

However, accessing `.real` discards the imaginary component. Do this only when that is mathematically appropriate for the problem.

---

# 12. Converting User Input

The `input()` function returns a string.

For this reason, numeric input usually needs conversion before arithmetic.

## Example: Add two integers

```python
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print("Sum:", first + second)
```

Example input:

```text
10
20
```

Output:

```text
Sum: 30
```

## Example: Calculate an average

```python
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

average = (first + second) / 2

print("Average:", average)
```

## Handling invalid input

An invalid numeric string can raise `ValueError`.

```python
value = input("Enter an integer: ")

try:
    number = int(value)
    print("Number:", number)
except ValueError:
    print("Please enter a valid integer.")
```

When designing programs, decide what invalid input should mean and respond with an appropriate message.

---

# 13. Converting Collections

Python also provides constructors for common collection types.

## 13.1 String to list

```python
text = "Python"

characters = list(text)

print(characters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

## 13.2 List to tuple

```python
numbers = [1, 2, 3]

result = tuple(numbers)

print(result)
```

Output:

```text
(1, 2, 3)
```

## 13.3 List to set

```python
numbers = [1, 2, 2, 3, 3]

result = set(numbers)

print(sorted(result))
```

Output:

```text
[1, 2, 3]
```

A set removes duplicate elements. Its elements do not have a guaranteed display order.

## 13.4 List of pairs to dictionary

```python
items = [
    ("name", "Amaan"),
    ("course", "Python")
]

profile = dict(items)

print(profile)
```

Output:

```text
{'name': 'Amaan', 'course': 'Python'}
```

Conversion into a dictionary requires an appropriate iterable of key-value pairs or another accepted dictionary input format.

---

# 14. Conversion Compatibility Table

The following table provides a general beginner's reference. Exact behavior depends on the value and its representation.

| Source value | `int()` | `float()` | `str()` | `bool()` | `complex()` |
|---|---|---|---|---|---|
| `10` | `10` | `10.0` | `"10"` | `True` | `(10+0j)` |
| `3.7` | `3` | `3.7` | `"3.7"` | `True` | `(3.7+0j)` |
| `"25"` | `25` | `25.0` | `"25"` | `True` | `(25+0j)` |
| `""` | Error | Error | `""` | `False` | Error |
| `True` | `1` | `1.0` | `"True"` | `True` | `(1+0j)` |
| `False` | `0` | `0.0` | `"False"` | `False` | `0j` |
| `None` | Error | Error | `"None"` | `False` | Error |
| `3+4j` | Error | Error | `"(3+4j)"` | `True` | `(3+4j)` |

**Important:** The table describes typical Python behavior. A row that says "Error" means that this conversion is not supported for that value through the displayed constructor in the usual way.

Complex-to-real conversions deserve particular attention: Python does not automatically discard an imaginary component when converting a complex number directly to an integer or float.

---

# 15. Common Errors and Exceptions

## 15.1 ValueError

A conversion raises `ValueError` when the value is of an acceptable general kind but its contents cannot be parsed.

```python
# Raises ValueError:
# int("hello")
```

## 15.2 TypeError

A conversion may raise `TypeError` when the input type is not supported.

```python
value = 3 + 4j

# Raises TypeError:
# float(value)
```

## 15.3 Truncation instead of rounding

```python
print(int(8.9))
print(round(8.9))
```

Output:

```text
8
9
```

Use the conversion function that matches the intended mathematical result.

## 15.4 Confusing numeric text with a number

```python
first = "10"
second = "20"

print(first + second)
```

Output:

```text
1020
```

Convert both values to integers when addition is intended.

## 15.5 Assuming bool() interprets words

```python
print(bool("no"))
```

Output:

```text
True
```

The string is non-empty. Parse textual answers explicitly.

## 15.6 Losing information through conversion

```python
value = 9.99
result = int(value)

print(result)
```

Output:

```text
9
```

The fractional component is removed. Conversion should be performed only when this behavior is acceptable.

---

# 16. Practical Examples

## Example 1: Student marks

```python
marks_text = input("Enter marks: ")

try:
    marks = float(marks_text)
    valid_marks = 0 <= marks <= 100

    print("Marks:", marks)
    print("Within the range:", valid_marks)

except ValueError:
    print("Invalid numeric input.")
```

This demonstrates text input, numeric conversion and range validation.

## Example 2: Shopping bill

```python
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total = quantity * unit_price

print(f"Total: {total:.2f}")
```

The integer quantity and floating-point unit price produce a floating-point total.

For applications requiring exact financial arithmetic, consider the `decimal.Decimal` type.

## Example 3: Formatting an integer

```python
age = 22

message = f"I am {age} years old."

print(message)
```

Output:

```text
I am 22 years old.
```

The f-string includes the numeric value in a string without requiring manual concatenation.

## Example 4: Handling optional input

```python
value = input("Enter an optional number: ").strip()

if value == "":
    number = None
else:
    try:
        number = float(value)
    except ValueError:
        number = None
        print("Input was invalid.")

print(number)
```

In a real application, consider representing blank input and invalid input separately if the program needs to distinguish those cases.

---

# 17. Four-Topic Learning Roadmap

The Type Conversion section has four subtopics. Complete them in the following order.

## Topic 1: `01_implicit_conversion`

**Main concepts:**

- What implicit conversion means
- Automatic conversion in numeric expressions
- Integer and float combinations
- Promotion to complex values
- Why Python does not automatically convert every string to a number
- Reading the result type of an expression

## Topic 2: `02_explicit_conversion`

**Main concepts:**

- The meaning of explicit conversion
- `int()`, `float()`, `str()`, `bool()` and `complex()`
- Truncation and rounding
- Valid and invalid conversions
- Handling `ValueError` and `TypeError`
- Choosing the correct conversion

## Topic 3: `03_string_conversion`

**Main concepts:**

- Converting numbers and other values into strings
- Converting numeric strings into numbers
- Why `input()` returns text
- Using `str()` and f-strings
- Handling whitespace in user input
- Parsing numbers safely
- Difference between a value and its textual representation

## Topic 4: `04_numeric_conversion`

**Main concepts:**

- Integer and float conversion
- Truncation versus rounding
- Numeric precision
- Scientific notation
- Complex-to-real conversion limitations
- Selecting suitable numeric types for calculations
- Testing edge cases

Each subtopic will have its own Python program and detailed `README.md`.

Every individual program follows the same agreed structure:

1. Module docstring and imports
2. Helper functions
3. Twelve examples
4. Twelve solved problems
5. Ten unsolved practice questions
6. Learning checklist
7. Main menu

Each individual README will include detailed explanations, code examples and outputs, solved-problem logic, common errors, best practices, revision tables, viva questions and a learning checklist.

---

# 18. Complete Folder Structure

```text
03-Type-Conversion/
├── README.md
│
├── 01_implicit_conversion/
│   ├── 01_implicit_conversion.py
│   └── README.md
│
├── 02_explicit_conversion/
│   ├── 02_explicit_conversion.py
│   └── README.md
│
├── 03_string_conversion/
│   ├── 03_string_conversion.py
│   └── README.md
│
└── 04_numeric_conversion/
    ├── 04_numeric_conversion.py
    └── README.md
```

The top-level `README.md` explains the full section, while each child README covers its individual topic.

---

# 19. Practice and Revision

After completing all four topics, make sure you can answer these questions:

1. What is implicit type conversion?
2. What is explicit type conversion?
3. What happens when an integer is added to a float?
4. Why does `input()` return a string?
5. What is the result of `int(9.8)`?
6. What is the difference between `int(9.8)` and `round(9.8)`?
7. Why does `bool("False")` return `True`?
8. What is the difference between `"10" + "20"` and `int("10") + int("20")`?
9. Why does `float(3 + 4j)` raise an error?
10. How should a program handle invalid numeric input?
11. What is the difference between a value and the string representation of that value?
12. Why is it important to test boundary cases and invalid conversions?

Use these as a quick revision set after completing the individual programs.

---

# 20. Common Interview and Viva Questions

### Q1. What is type conversion?

Type conversion changes a value from one data type to another.

### Q2. What is implicit conversion?

It is a compatible conversion that Python performs automatically during certain operations.

### Q3. What is explicit conversion?

It is a conversion requested by the programmer, commonly using functions such as `int()`, `float()` and `str()`.

### Q4. What is the difference between `int()` and `float()`?

`int()` converts a compatible value into an integer. `float()` converts a compatible value into a floating-point number.

### Q5. What happens when `int()` receives a float?

It truncates the fractional part toward zero.

### Q6. What does `str()` do?

It returns the string representation of a value.

### Q7. Why does `input()` often require conversion?

Because `input()` returns a string, even when the user types digits.

### Q8. What is the difference between `ValueError` and `TypeError` in conversion?

`ValueError` commonly means the input's contents cannot be converted as requested. `TypeError` commonly means the conversion or operation is unsupported for the supplied type.

### Q9. Does `bool("False")` return `False`?

No. It returns `True`, because the string is non-empty.

### Q10. Can a complex number be directly converted to float?

No. Python raises `TypeError` because this would require deciding what to do with the imaginary component.

### Q11. What is numeric promotion?

Numeric promotion is the selection of a compatible numeric type for an operation, such as producing a float for a mixed integer-and-float addition.

### Q12. Why should type conversion be validated?

Invalid or unexpected inputs can cause exceptions, incorrect values or silent loss of information.

---

# 21. Learning Checklist

Before completing this section, make sure you can:

- [ ] Explain implicit and explicit conversion.
- [ ] Understand numeric promotion in mixed arithmetic.
- [ ] Convert compatible values with `int()` and `float()`.
- [ ] Convert values into strings using `str()`.
- [ ] Understand the behavior of `bool()`.
- [ ] Create complex numbers using `complex()`.
- [ ] Explain common conversion errors.
- [ ] Distinguish truncation from rounding.
- [ ] Convert user input safely.
- [ ] Understand why conversion may lose information.
- [ ] Explain the difference between numeric values and text.
- [ ] Complete the four individual topic folders.
- [ ] Attempt all practice questions in each topic.

---

# Final Summary

Type conversion helps Python programs work correctly with values from different sources and of different types.

The four topics in this section move from automatic numeric promotion to explicit conversion, text conversion and numeric conversion details.

Study each child folder in order, run the associated examples, test valid and invalid values, and practise the problems independently before moving on to the next chapter.
