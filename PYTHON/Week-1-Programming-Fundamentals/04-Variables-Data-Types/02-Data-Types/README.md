# Python Data Types — Complete Section Guide

**Week:** 1 — Programming Fundamentals  
**Part:** Variables and Data Types  
**Section:** `02-Data-Types`  
**Language:** Python

---

# Table of Contents

1. Introduction to Data Types
2. Why Are Data Types Important?
3. Data Types Covered in This Section
4. Integer (`int`)
5. Floating-Point (`float`)
6. String (`str`)
7. Boolean (`bool`)
8. Complex (`complex`)
9. None (`NoneType`)
10. Checking Data Types with `type()`
11. Understanding Values and Variables
12. Comparison of the Six Topics
13. Common Programming Mistakes
14. Practical Examples
15. Learning Roadmap
16. Folder Structure
17. How to Run the Programs
18. Practice and Revision Checklist
19. Git Commit and Push

---

# 1. Introduction to Data Types

A **data type** defines the kind of value a variable represents and the operations that can be performed on that value.

Python supports several built-in data types. This section focuses on six important concepts:

- Integers
- Floating-point numbers
- Strings
- Booleans
- Complex numbers
- `None`

Understanding these types is essential before learning type conversion, input/output, conditional statements, loops, functions and data structures.

## Example

```python
student_name = "Amaan"
age = 22
percentage = 85.5
is_enrolled = True
complex_value = 3 + 4j
middle_name = None

print(student_name)
print(age)
print(percentage)
print(is_enrolled)
print(complex_value)
print(middle_name)
```

Output:

```text
Amaan
22
85.5
True
(3+4j)
None
```

Each variable stores a different kind of value.

---

# 2. Why Are Data Types Important?

Data types help Python determine how values behave in operations.

For example, the `+` operator can perform addition with numbers or concatenation with strings.

```python
number1 = 10
number2 = 20

print(number1 + number2)
```

Output:

```text
30
```

Now consider strings:

```python
text1 = "10"
text2 = "20"

print(text1 + text2)
```

Output:

```text
1020
```

The numeric values are added in the first example. The string values are joined in the second.

Knowing the data type helps prevent unexpected results and programming errors.

---

# 3. Data Types Covered in This Section

| No. | Topic | Python type | Main purpose |
|---:|---|---|---|
| 1 | Integer | `int` | Whole numbers |
| 2 | Floating-point | `float` | Numbers with fractional values |
| 3 | String | `str` | Text and character sequences |
| 4 | Boolean | `bool` | Logical truth values |
| 5 | Complex | `complex` | Numbers with real and imaginary components |
| 6 | None | `NoneType` | Represents an absent value or result |

Each topic has its own folder, Python program and `README.md` documentation.

---

# 4. Integer (`int`)

An integer is a whole number without a fractional component.

Examples:

```python
age = 22
temperature = -5
quantity = 0

print(type(age))
print(type(temperature))
print(type(quantity))
```

Output:

```text
<class 'int'>
<class 'int'>
<class 'int'>
```

Integers support operations such as addition, subtraction, multiplication, integer division and modulo.

```python
a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
```

Output:

```text
22
12
85
3
2
```

**Topics to practise:** Integer operations, arithmetic expressions, digit manipulation, even/odd checks and common number problems.

Folder: `01_int`

---

# 5. Floating-Point (`float`)

A floating-point number represents a numeric value that can contain a fractional component.

Examples:

```python
price = 99.50
temperature = -2.75
percentage = 85.5

print(type(price))
print(type(temperature))
print(type(percentage))
```

Output:

```text
<class 'float'>
<class 'float'>
<class 'float'>
```

Floating-point values are useful in measurements, averages, percentages and many scientific calculations.

```python
price = 99.50
discount = 10.0

final_price = price - discount

print(final_price)
```

Output:

```text
89.5
```

Floating-point representation can introduce small rounding differences. Financial applications may require decimal arithmetic rather than ordinary binary floating-point arithmetic.

**Topics to practise:** Decimal values, rounding, formatting, precision and mathematical calculations.

Folder: `02_float`

---

# 6. String (`str`)

A string represents text. It can contain letters, numbers, spaces and special characters.

```python
name = "Amaan"
language = "Python"
message = "Learning Python is useful"

print(type(name))
print(language)
print(message)
```

Output:

```text
<class 'str'>
Python
Learning Python is useful
```

Strings support indexing, slicing, concatenation, searching and many built-in methods.

```python
language = "Python"

print(language[0])
print(language[-1])
print(language.upper())
print(language[::-1])
```

Output:

```text
P
n
PYTHON
nohtyP
```

Strings are immutable, which means their characters cannot be altered in place.

**Topics to practise:** Indexing, slicing, string methods, immutability, formatting and string-based programming problems.

Folder: `03_string`

---

# 7. Boolean (`bool`)

A Boolean represents one of two truth values:

```python
True
False
```

Boolean values are used for comparisons, conditions and decision-making.

```python
age = 20

print(age >= 18)
print(age < 18)
```

Output:

```text
True
False
```

Logical operators allow conditions to be combined.

```python
age = 20
has_id = True

eligible = age >= 18 and has_id

print(eligible)
```

Output:

```text
True
```

**Topics to practise:** Comparison operators, `and`, `or`, `not`, truthy/falsy values, short-circuit evaluation and conditional expressions.

Folder: `04_boolean`

---

# 8. Complex (`complex`)

A complex number contains a real component and an imaginary component.

Python uses `j` for the imaginary unit.

```python
number = 3 + 4j

print(number)
print(number.real)
print(number.imag)
print(type(number))
```

Output:

```text
(3+4j)
3.0
4.0
<class 'complex'>
```

Python supports complex arithmetic and provides the `cmath` module for complex mathematical functions.

```python
number = 3 + 4j

print(abs(number))
print(number.conjugate())
```

Output:

```text
5.0
(3-4j)
```

**Topics to practise:** Complex arithmetic, components, magnitude, conjugate and polar representation.

Folder: `05_complex`

---

# 9. None (`NoneType`)

`None` is a special value used to represent an absent value or the absence of a meaningful result.

```python
middle_name = None

print(middle_name)
print(type(middle_name))
```

Output:

```text
None
<class 'NoneType'>
```

Check for it using `is None` or `is not None`.

```python
value = None

if value is None:
    print("No value is available.")
else:
    print("Value:", value)
```

Output:

```text
No value is available.
```

Do not confuse `None` with zero, `False` or an empty string. They can all be falsy in a Boolean context, but they represent different values.

**Topics to practise:** Optional values, function return values, dictionaries, missing data and safe defaults.

Folder: `06_none`

---

# 10. Checking Data Types with `type()`

Python provides the built-in `type()` function to identify the type of a value.

```python
print(type(100))
print(type(25.5))
print(type("Hello"))
print(type(True))
print(type(3 + 4j))
print(type(None))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'complex'>
<class 'NoneType'>
```

The `isinstance()` function is also useful when checking whether a value is an instance of a particular type.

```python
value = "Python"

print(isinstance(value, str))
print(isinstance(value, int))
```

Output:

```text
True
False
```

### Important distinction

`type()` reports an object's type. `isinstance()` checks whether an object belongs to a type or one of its subclasses.

For normal beginner exercises, both are valuable tools for understanding variables and their data types.

---

# 11. Understanding Values and Variables

A variable is a name that refers to a value. The type belongs to the value, not permanently to the variable name.

```python
value = 100
print(value, type(value))

value = "Python"
print(value, type(value))
```

Output:

```text
100 <class 'int'>
Python <class 'str'>
```

The same variable is first assigned an integer and later assigned a string.

Python is dynamically typed, so an assignment can change what value a variable refers to. This does not mean every operation is allowed: operators still have rules about which types they support.

For example:

```python
value = "Python"

# This would raise a TypeError:
# result = value + 10
```

Understanding types helps you use operators correctly and recognize when conversion is required.

---

# 12. Comparison of the Six Topics

| Property | `int` | `float` | `str` | `bool` | `complex` | `NoneType` |
|---|---|---|---|---|---|---|
| Represents | Whole numbers | Floating-point numbers | Text | Truth values | Complex numbers | Absence of a value |
| Example | `10` | `10.5` | `"Python"` | `True` | `3+4j` | `None` |
| Addition | Yes | Yes | Concatenation | Numeric behavior is supported | Yes | Not directly supported |
| Ordering comparisons | Yes | Yes | Lexicographic | Boolean/numeric behavior | `<` and `>` unsupported | Not generally supported |
| Indexing | No | No | Yes | No | No | No |
| Mutable | No | No | No | No | No | No |

This table gives a high-level comparison. The meaning of an operation depends on the particular operands and operator.

### Important points

- Strings are sequences; integers and floating-point numbers are numeric scalar values.
- Booleans are used primarily for logical conditions.
- Complex numbers support arithmetic but not ordinary ordering comparisons.
- `None` is not a numeric zero or Boolean false.
- These built-in values are immutable.

---

# 13. Common Programming Mistakes

## Mistake 1: Treating numeric text as a number

```python
value = "100"

print(type(value))
```

Output:

```text
<class 'str'>
```

The value is text, even though the characters look numeric.

## Mistake 2: Confusing a float with an integer

```python
a = 10
b = 10.0

print(type(a))
print(type(b))
```

Output:

```text
<class 'int'>
<class 'float'>
```

They may have equal numerical values, but their types differ.

## Mistake 3: Using `bool()` to parse `"False"`

```python
print(bool("False"))
```

Output:

```text
True
```

A non-empty string is truthy. Parse textual Boolean answers explicitly when required.

## Mistake 4: Trying to modify a string directly

```python
text = "Python"

# This causes a TypeError:
# text[0] = "J"
```

Create a new string instead.

## Mistake 5: Comparing complex values with `<`

```python
first = 3 + 4j
second = 2 + 1j

# This causes a TypeError:
# print(first < second)
```

Compare magnitudes using `abs()` if that is the intended mathematical comparison.

## Mistake 6: Confusing None with zero

```python
print(None == 0)
```

Output:

```text
False
```

`None` represents an absent value, while zero is a valid numeric value.

---

# 14. Practical Examples

## Example 1: Student information

```python
name = "Amaan"
age = 22
percentage = 85.5
is_enrolled = True
middle_name = None

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}")
print(f"Enrolled: {is_enrolled}")
print(f"Middle name: {middle_name}")
```

This example combines strings, integers, floats, Booleans and `None` in one simple student record.

## Example 2: Inspecting data types

```python
values = [100, 25.5, "Python", True, 3 + 4j, None]

for value in values:
    print(repr(value), "->", type(value).__name__)
```

Output:

```text
100 -> int
25.5 -> float
'Python' -> str
True -> bool
(3+4j) -> complex
None -> NoneType
```

## Example 3: Selecting operations based on type

```python
value = "Python"

if isinstance(value, str):
    print("This value contains text.")
elif isinstance(value, (int, float)):
    print("This value is numeric.")
else:
    print("This example uses another data type.")
```

Output:

```text
This value contains text.
```

This example shows how type checking can be used to select different operations.

---

# 15. Learning Roadmap

Study these folders in order:

1. `01_int` — Understand whole numbers and integer operations.
2. `02_float` — Learn fractional values, precision and rounding.
3. `03_string` — Learn how text is stored and processed.
4. `04_boolean` — Learn true/false values and logical conditions.
5. `05_complex` — Learn real and imaginary components.
6. `06_none` — Learn how to represent absent values and results.

For each topic:

1. Read the theory in `README.md`.
2. Run the examples in the Python program.
3. Trace the output manually.
4. Attempt every solved problem using different inputs.
5. Complete the unsolved practice questions provided in that topic.
6. Review common errors and the final checklist.
7. Commit the topic files to Git once they have been tested.

After completing this section, move to `03-Type-Conversion` to study how Python converts values between types.

---

# 16. Folder Structure

```text
02-Data-Types/
├── README.md
│
├── 01_int/
│   ├── 01_int.py
│   └── README.md
│
├── 02_float/
│   ├── 02_float.py
│   └── README.md
│
├── 03_string/
│   ├── 03_string.py
│   └── README.md
│
├── 04_boolean/
│   ├── 04_boolean.py
│   └── README.md
│
├── 05_complex/
│   ├── 05_complex.py
│   └── README.md
│
└── 06_none/
    ├── 06_none.py
    └── README.md
```

Every topic folder has a Python practice file and a `README.md` file containing its detailed documentation.

The parent `README.md` explains the overall section and links the concepts together.

---

# 17. How to Run the Programs

Open PowerShell in your repository root.

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"
```

Run individual topic files with Python.

### Integer

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\01_int\01_int.py"
```

### Float

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\02_float\02_float.py"
```

### String

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\03_string\03_string.py"
```

### Boolean

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\04_boolean\04_boolean.py"
```

### Complex

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\05_complex\05_complex.py"
```

### None

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\06_none\06_none.py"
```

Run only one topic file at a time. Each script has its own interactive menu.

---

# 18. Practice and Revision Checklist

Before considering this section complete, make sure you can:

- [ ] Explain the six data types covered here.
- [ ] Check types using `type()` and `isinstance()`.
- [ ] Perform basic integer operations.
- [ ] Work with floating-point values and understand rounding.
- [ ] Create, index and slice strings.
- [ ] Use common string methods.
- [ ] Evaluate Boolean expressions.
- [ ] Combine conditions using logical operators.
- [ ] Create and manipulate complex numbers.
- [ ] Calculate a complex number's magnitude and conjugate.
- [ ] Explain the purpose of `None`.
- [ ] Distinguish None from zero, False and empty strings.
- [ ] Run all six topic programs successfully.
- [ ] Attempt the practice questions in each topic.
- [ ] Understand when type conversion is required.

---

# 19. Git Commit and Push

After saving and reviewing the parent README, run these commands from the repository root:

```powershell
git status

git add "PYTHON/Week-1-Programming-Fundamentals/04-Variables-Data-Types/02-Data-Types/README.md"

git status

git commit -m "Add Python data types section documentation"

git push origin main
```

Review the `git status` output before committing so that you know exactly which files will be included.

---

## Final Summary

Python data types determine the kinds of values that variables represent and the operations that are supported.

The six topics in this section form the foundation for later programming work:

- `int` for whole numbers.
- `float` for floating-point calculations.
- `str` for text.
- `bool` for logical conditions.
- `complex` for real and imaginary components.
- `None` for absent values or results.

Understand these concepts thoroughly before moving on to type conversion, input/output, control flow and data structures.
