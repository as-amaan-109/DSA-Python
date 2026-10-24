# Python String Data Type — Complete Study Notes

**Week:** 1 — Programming Fundamentals  
**Part:** Variables and Data Types  
**Topic:** String Data Type  
**File:** `03_string.py`

---

## Table of Contents

1. Introduction to Strings
2. Creating Strings
3. Single, Double and Triple Quotes
4. Escape Sequences
5. Raw Strings
6. Variables and Strings
7. String Concatenation
8. String Repetition
9. String Length
10. String Indexing
11. String Slicing
12. String Immutability
13. String Operators
14. Important String Methods
15. String Searching and Counting
16. String Splitting and Joining
17. Checking Characters and Text
18. String Formatting
19. Taking String Input from the User
20. Type Conversion with Strings
21. Comparing Strings
22. Common String Programming Patterns
23. Twelve Solved Problems with Logic
24. Five Unsolved Practice Problems
25. Common Errors and Mistakes
26. Best Practices
27. Quick Revision Table
28. Important Interview and Viva Questions
29. Final Learning Checklist

---

# 1. Introduction to Strings

## What is a string?

A **string** is a sequence of characters used to represent text in Python.

A string can contain:

- Uppercase letters: `A`, `B`, `C`
- Lowercase letters: `a`, `b`, `c`
- Numbers as text: `"12345"`
- Spaces: `"Hello World"`
- Special characters: `"@#$%"`
- Punctuation: `"Hello!"`

In Python, the data type used for strings is called `str`.

### Example

```python
name = "Amaan"
city = "Nagpur"
message = "Welcome to Python"
phone_text = "9876543210"

print(name)
print(city)
print(message)
print(phone_text)

print(type(name))
```

### Output

```text
Amaan
Nagpur
Welcome to Python
9876543210
<class 'str'>
```

Notice that `"9876543210"` is a string because it is enclosed in quotes. It is not an integer, so numeric operations cannot be performed on it directly.

### Why do we use strings?

Strings are used in many applications:

- Storing names and email addresses
- Displaying messages to users
- Processing text documents
- Searching and replacing words
- Validating usernames and passwords
- Building URLs and file paths
- Processing data received from APIs
- Creating reports and formatted output

### Important point

`str` is the name of Python's string type.

```python
text = "Hello"

print(type(text))
print(isinstance(text, str))
```

Output:

```text
<class 'str'>
True
```

---

# 2. Creating Strings

Python provides several ways to create a string.

## 2.1 Using single quotes

```python
name = 'Amaan'
print(name)
```

Output:

```text
Amaan
```

## 2.2 Using double quotes

```python
language = "Python"
print(language)
```

Output:

```text
Python
```

## 2.3 Using triple quotes

Triple single quotes or triple double quotes can represent multiline strings.

```python
message = """Welcome to Python.
Python is easy to learn.
Practice every day."""

print(message)
```

Output:

```text
Welcome to Python.
Python is easy to learn.
Practice every day.
```

You can also use triple single quotes:

```python
message = '''First line
Second line
Third line'''

print(message)
```

## 2.4 Creating an empty string

An empty string contains zero characters.

```python
text = ""

print(text)
print(len(text))
print(type(text))
```

Output:

```text
0
<class 'str'>
```

The first output line is blank because `text` contains no characters.

An empty string is different from a string containing a space.

```python
first = ""
second = " "

print(len(first))   # 0
print(len(second))  # 1
```

**Remember:** Empty strings and strings containing spaces are not the same.

---

# 3. Single, Double and Triple Quotes

Single and double quotes generally work the same way.

```python
a = 'Python'
b = "Python"

print(a == b)
```

Output:

```text
True
```

The choice depends on which quotation marks your text contains.

## Example 1: A sentence containing an apostrophe

```python
sentence = "It's a beautiful day."
print(sentence)
```

Output:

```text
It's a beautiful day.
```

## Example 2: A sentence containing double quotes

```python
sentence = 'She said, "Python is easy."'
print(sentence)
```

Output:

```text
She said, "Python is easy."
```

## Example 3: Escaping quotation marks

You may also escape quotation marks using a backslash.

```python
sentence = "She said, \"Python is easy.\""
print(sentence)
```

Output:

```text
She said, "Python is easy."
```

### When should you use triple quotes?

Use triple quotes when:

- You want to write text across multiple lines.
- You want to preserve line breaks in a string.
- You are writing a multiline string in your program.

Triple quotes can also be used for single-line strings, but ordinary quotes are usually simpler for short text.

---

# 4. Escape Sequences

An escape sequence begins with a backslash (`\`) followed by another character. It represents a special character or formatting instruction.

## Important escape sequences

| Escape sequence | Meaning | Example |
|---|---|---|
| `\n` | New line | `"Hello\nWorld"` |
| `\t` | Tab | `"Name:\tAmaan"` |
| `\\` | Literal backslash | `"C:\\Python"` |
| `\'` | Single quotation mark | `'It\'s Python'` |
| `\"` | Double quotation mark | `"Say \"Hello\""` |
| `\r` | Carriage return | `"\r"` |
| `\b` | Backspace | `"\b"` |

The visible effect of some control characters can depend on the terminal or output environment. For beginners, concentrate on `\n`, `\t`, `\\`, `\'` and `\"`.

## Example 1: New line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

The `\n` moves the following text to a new line.

## Example 2: Tab

```python
print("Name:\tAmaan")
print("Course:\tComputer Science")
```

Output resembles:

```text
Name:   Amaan
Course: Computer Science
```

The exact spacing depends on tab stops in the output environment.

## Example 3: File path with backslashes

```python
print("C:\\Python\\Programs")
```

Output:

```text
C:\Python\Programs
```

Each `\\` represents one literal backslash.

## Example 4: Quotes inside text

```python
print("She said, \"Hello!\"")
print('It\'s a Python program.')
```

Output:

```text
She said, "Hello!"
It's a Python program.
```

### Common mistake

```python
# Incorrect: the quote ends the string too early.
# text = 'It's Python'

# Correct:
text = "It's Python"

# Another correct version:
text = 'It\'s Python'

print(text)
```

---

# 5. Raw Strings

A raw string is created by placing `r` or `R` before the opening quote.

Raw strings are useful for regular expressions and Windows paths because backslashes are treated differently from ordinary escape sequences.

```python
normal_path = "C:\\Users\\Student\\Documents"
raw_path = r"C:\Users\Student\Documents"

print(normal_path)
print(raw_path)
```

Both display:

```text
C:\Users\Student\Documents
```

In the ordinary string, the backslashes were escaped. In the raw string, they are written directly.

### Important limitation

A raw string cannot end with an odd number of backslashes because the final backslash would escape its closing quote.

For example, `r"C:\Temp\"` is invalid syntax.

---

# 6. Variables and Strings

A variable can refer to a string value.

```python
name = "Amaan"
course = "Computer Science"
college_year = "Second Year"

print(name)
print(course)
print(college_year)
```

Variables can also be reassigned to different strings.

```python
language = "Java"
print(language)

language = "Python"
print(language)
```

Output:

```text
Java
Python
```

The variable now refers to a different string.

### Assigning an empty string

```python
message = ""
message = "Welcome"

print(message)
```

A variable may start with an empty string and receive text later.

---

# 7. String Concatenation

**Concatenation** means joining strings together.

The `+` operator performs string concatenation.

## Example 1: Joining two strings

```python
first_name = "Amaan"
last_name = "Syed"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Amaan Syed
```

The `" "` adds a space between the two names.

## Example 2: Concatenating more than two strings

```python
first = "Python"
second = "is"
third = "powerful"

sentence = first + " " + second + " " + third

print(sentence)
```

Output:

```text
Python is powerful
```

## Example 3: Why can't we concatenate a string and an integer directly?

```python
age = 22

# This causes a TypeError:
# print("Age: " + age)
```

Python does not automatically convert the integer to a string in this expression.

Correct approaches:

```python
age = 22

print("Age: " + str(age))
print(f"Age: {age}")
```

Output:

```text
Age: 22
Age: 22
```

**Remember:** Use `str()` for explicit conversion or an f-string for formatted output.

---

# 8. String Repetition

The `*` operator repeats a string a specified number of times.

## Example 1

```python
print("Python " * 3)
```

Output:

```text
Python Python Python
```

## Example 2: Printing a separator

```python
print("-" * 30)
print("PYTHON NOTES")
print("-" * 30)
```

Output:

```text
------------------------------
PYTHON NOTES
------------------------------
```

## Example 3: Repeating a pattern

```python
pattern = "* " * 5
print(pattern)
```

Output:

```text
* * * * *
```

A repetition count of zero or less produces an empty string.

```python
print("Hello" * 0)   # Empty output
print("Hello" * -2)  # Empty output
```

---

# 9. String Length

The built-in `len()` function returns the number of characters in a string.

## Syntax

```python
len(string)
```

## Example 1

```python
text = "Python"
print(len(text))
```

Output:

```text
6
```

## Example 2: Spaces are counted

```python
text = "Hello World"
print(len(text))
```

Output:

```text
11
```

There are five characters in `Hello`, one space, and five characters in `World`.

## Example 3: Punctuation is counted

```python
text = "Hi!"
print(len(text))
```

Output:

```text
3
```

### Important distinction

`len(text)` counts every character in the string, including spaces, tabs, newlines and punctuation.

To count characters excluding whitespace:

```python
text = "Python is easy"

count = sum(
    1
    for character in text
    if not character.isspace()
)

print(count)
```

Output:

```text
12
```

The space between the words is not counted.

---

# 10. String Indexing

Indexing allows you to retrieve a character using its position.

Python uses zero-based indexing. The first character has index `0`, not index `1`.

Consider this string:

```python
language = "Python"
```

Its positive and negative indices are:

| Character | P | y | t | h | o | n |
|---|---:|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

## Positive indexing

```python
language = "Python"

print(language[0])
print(language[1])
print(language[2])
```

Output:

```text
P
y
t
```

## Negative indexing

Negative indexing counts backward from the end.

```python
language = "Python"

print(language[-1])
print(language[-2])
print(language[-3])
```

Output:

```text
n
o
h
```

## Accessing the first and last characters

```python
text = "Programming"

print("First:", text[0])
print("Last:", text[-1])
```

Output:

```text
First: P
Last: g
```

### IndexError

An invalid index causes an `IndexError`.

```python
text = "Python"

# This raises IndexError because the last valid index is 5:
# print(text[6])
```

An empty string has no valid character index.

```python
text = ""

# This also raises IndexError:
# print(text[0])
```

You should check whether a string is empty before accessing its first or last character.

```python
text = input("Enter text: ")

if text:
    print("First:", text[0])
    print("Last:", text[-1])
else:
    print("No characters were entered.")
```

---

# 11. String Slicing

Slicing extracts a section of a string without changing the original string.

## Syntax

```python
string[start:stop:step]
```

| Parameter | Meaning |
|---|---|
| `start` | Index where extraction begins |
| `stop` | Index where extraction ends, excluded |
| `step` | Number of positions to move each time |

All three parameters are optional, depending on the slice you want.

Consider:

```python
language = "Python"
```

## Example 1: Extract a range

```python
print(language[0:3])
```

Output:

```text
Pyt
```

The slice includes positions `0`, `1` and `2`. Position `3` is excluded.

## Example 2: From an index to the end

```python
print(language[2:])
```

Output:

```text
thon
```

## Example 3: From the beginning to an index

```python
print(language[:4])
```

Output:

```text
Pyth
```

## Example 4: Copy the complete string

```python
print(language[:])
```

Output:

```text
Python
```

## Example 5: Last three characters

```python
print(language[-3:])
```

Output:

```text
hon
```

## Example 6: Skipping characters

```python
print(language[::2])
```

Output:

```text
Pto
```

The step value `2` selects every second character, beginning at index `0`.

## Example 7: Reverse a string

```python
print(language[::-1])
```

Output:

```text
nohtyP
```

A negative step moves backward through the sequence.

## Common slicing mistakes

1. The stop index is excluded.
2. A valid slice can stop before or after the actual length without raising an index error.
3. An invalid direct index and an out-of-range slice behave differently.
4. A step of zero is invalid and raises a `ValueError`.

For example:

```python
text = "Python"

print(text[0:100])  # Python

# This raises ValueError:
# print(text[::0])
```

### When is slicing useful?

Slicing is useful for:

- Reversing strings
- Extracting prefixes and suffixes
- Getting part of a username
- Processing codes and identifiers
- Selecting characters at regular intervals

---

# 12. String Immutability

A string is **immutable**, which means its characters cannot be modified in place after the string is created.

## Incorrect approach

```python
text = "python"

# This causes a TypeError:
# text[0] = "P"
```

## Correct approach: Create a new string

```python
text = "python"
updated_text = "P" + text[1:]

print(text)
print(updated_text)
```

Output:

```text
python
Python
```

The original string remains unchanged.

## Using `replace()`

```python
text = "python"
updated_text = text.replace("p", "P")

print(text)
print(updated_text)
```

Output:

```text
python
Python
```

The `replace()` method returns a new string.

### Important distinction

A variable can be reassigned even though strings are immutable.

```python
text = "python"
text = "Python"

print(text)
```

Output:

```text
Python
```

This is valid because the variable is reassigned to another string. It does not change an existing string character.

**Remember:** Immutability applies to the string object, not to the variable name that refers to it.

---

# 13. String Operators

Python supports several operators for working with strings.

| Operator | Purpose | Example |
|---|---|---|
| `+` | Concatenation | `"Py" + "thon"` |
| `*` | Repetition | `"Hi" * 3` |
| `in` | Checks membership | `"Py" in "Python"` |
| `not in` | Checks absence | `"Java" not in "Python"` |
| `==` | Checks equality | `"abc" == "abc"` |
| `!=` | Checks inequality | `"abc" != "ABC"` |
| `<`, `>` | Lexicographic comparison | `"apple" < "banana"` |

## Membership example

```python
sentence = "Python is easy to learn"

print("Python" in sentence)
print("Java" in sentence)
print("Java" not in sentence)
```

Output:

```text
True
False
True
```

## Equality example

```python
print("python" == "python")
print("python" == "Python")
print("Python" != "Java")
```

Output:

```text
True
False
True
```

String comparisons are case-sensitive.

For example, `"Python"` and `"python"` are different strings.

Lexicographic comparison uses character ordering based on Unicode code points. It is not necessarily the same as dictionary sorting in every language.

---

# 14. Important String Methods

Python provides many built-in string methods.

Methods are called using this form:

```python
string.method()
```

Some methods accept arguments.

```python
string.method(argument)
```

## 14.1 Case-conversion methods

```python
text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())
```

Output:

```text
PYTHON PROGRAMMING
python programming
Python Programming
Python programming
PYTHON PROGRAMMING
```

| Method | Purpose |
|---|---|
| `upper()` | Converts applicable letters to uppercase |
| `lower()` | Converts applicable letters to lowercase |
| `title()` | Applies title-style capitalization |
| `capitalize()` | Uppercases the first character and lowercases the rest |
| `swapcase()` | Swaps lowercase and uppercase forms |

These methods return strings; they do not modify the original string in place.

## 14.2 Whitespace-removal methods

Whitespace includes spaces, tabs and newlines.

```python
text = "   Python   "

print(repr(text))
print(repr(text.strip()))
print(repr(text.lstrip()))
print(repr(text.rstrip()))
```

Output:

```text
'   Python   '
'Python'
'Python   '
'   Python'
```

| Method | Purpose |
|---|---|
| `strip()` | Removes whitespace from both ends |
| `lstrip()` | Removes whitespace from the left |
| `rstrip()` | Removes whitespace from the right |

**Important:** These methods do not remove spaces from the middle of a string.

```python
text = "  Python Programming  "

print(text.strip())
```

Output:

```text
Python Programming
```

The space between `Python` and `Programming` remains.

## 14.3 Replacement

The `replace(old, new)` method returns a string with matching occurrences replaced.

```python
text = "I like Java"
updated = text.replace("Java", "Python")

print(updated)
```

Output:

```text
I like Python
```

You can optionally specify a maximum number of replacements:

```python
text = "apple apple apple"

print(text.replace("apple", "orange", 2))
```

Output:

```text
orange orange apple
```

## 14.4 Prefix and suffix checking

```python
filename = "notes.txt"

print(filename.startswith("notes"))
print(filename.endswith(".txt"))
print(filename.endswith(".pdf"))
```

Output:

```text
True
True
False
```

Useful for checking file extensions, prefixes and other text patterns.

## 14.5 Alignment methods

```python
text = "Python"

print(text.center(12, "-"))
print(text.ljust(12, "-"))
print(text.rjust(12, "-"))
```

Output:

```text
---Python---
Python------
------Python
```

These methods return strings padded to a specified width. If the text is already at least that wide, the original text is returned unchanged.

---

# 15. String Searching and Counting

## 15.1 `find()`

The `find()` method returns the index of the first occurrence of a substring. If the substring is not found, it returns `-1`.

```python
text = "Python programming"

print(text.find("pro"))
print(text.find("Java"))
```

Output:

```text
7
-1
```

## 15.2 `index()`

The `index()` method also finds a substring, but it raises a `ValueError` if the substring is not present.

```python
text = "Python programming"

print(text.index("Python"))
```

Output:

```text
0
```

Choose `find()` when a missing result should be represented by `-1`. Use `index()` when absence should raise an error.

## 15.3 `count()`

The `count()` method returns the number of non-overlapping occurrences of a substring.

```python
text = "banana"

print(text.count("a"))
print(text.count("na"))
```

Output:

```text
3
2
```

### Important detail

`count()` counts non-overlapping matches.

```python
print("aaaa".count("aa"))
```

Output:

```text
2
```

The string is matched in two non-overlapping pairs.

To count one character in a case-insensitive way:

```python
text = "Python PYTHON python"

print(text.lower().count("python"))
```

Output:

```text
3
```

---

# 16. String Splitting and Joining

## 16.1 `split()`

`split()` divides a string into a list of smaller strings.

```python
sentence = "Python is easy to learn"

words = sentence.split()

print(words)
print(len(words))
```

Output:

```text
['Python', 'is', 'easy', 'to', 'learn']
5
```

Without an argument, `split()` divides text on runs of whitespace and does not retain leading or trailing empty fields from whitespace.

### Split using a specific separator

```python
data = "red,green,blue"

colors = data.split(",")

print(colors)
```

Output:

```text
['red', 'green', 'blue']
```

## 16.2 `join()`

`join()` combines strings using a separator.

```python
words = ["Python", "is", "easy"]

print(" ".join(words))
print("-".join(words))
print(", ".join(words))
```

Output:

```text
Python is easy
Python-is-easy
Python, is, easy
```

The separator appears between list elements, not at the beginning or end.

### Why is `join()` useful?

It is especially useful when building a string from many pieces.

```python
characters = ["P", "y", "t", "h", "o", "n"]

result = "".join(characters)

print(result)
```

Output:

```text
Python
```

All elements provided to `join()` must be strings. Convert non-string values first if necessary.

---

# 17. Checking Characters and Text

Python provides methods for testing character types.

These methods return Boolean values: `True` or `False`.

| Method | Returns `True` when... |
|---|---|
| `isalpha()` | All characters are alphabetic and the string is non-empty |
| `isdigit()` | All characters are digits according to Python's digit classification and the string is non-empty |
| `isalnum()` | All characters are alphabetic or numeric and the string is non-empty |
| `isspace()` | All characters are whitespace and the string is non-empty |
| `islower()` | At least one cased character exists and all cased characters are lowercase |
| `isupper()` | At least one cased character exists and all cased characters are uppercase |
| `startswith()` | The string begins with the requested prefix |
| `endswith()` | The string ends with the requested suffix |

## Examples

```python
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())
print("python".islower())
print("PYTHON".isupper())
```

Output:

```text
True
True
True
True
True
True
```

### Empty-string behavior

Most of these character-classification methods return `False` for an empty string.

```python
text = ""

print(text.isalpha())
print(text.isdigit())
print(text.isspace())
```

Output:

```text
False
False
False
```

### Practical example: Validate a simple numeric string

```python
value = input("Enter a positive whole number: ")

if value.isdigit():
    print("The input contains digits.")
else:
    print("The input is not a digit-only string.")
```

This is a character check, not a complete numeric parser. For example, `"-10"` and `"3.14"` contain valid numeric values, but they are not digit-only strings.

---

# 18. String Formatting

String formatting inserts values into a text template.

## 18.1 F-strings

F-strings are a recommended way to format output in modern Python.

```python
name = "Amaan"
age = 22

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

Output:

```text
My name is Amaan.
I am 22 years old.
```

## 18.2 Expressions inside f-strings

```python
a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Product = {a * b}")
```

Output:

```text
Sum = 30
Product = 200
```

## 18.3 Formatting decimal values

```python
price = 123.45678

print(f"{price:.2f}")
```

Output:

```text
123.46
```

The `.2f` format displays two decimal places.

## 18.4 Padding and alignment

```python
name = "Amaan"

print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")
```

Output:

```text
|Amaan     |
|     Amaan|
|  Amaan   |
```

Here:

- `<` aligns text to the left.
- `>` aligns text to the right.
- `^` centers text within the field width.

## 18.5 Older formatting options

Python also supports `str.format()` and the older `%` formatting style.

```python
name = "Amaan"
marks = 95

print("{} scored {} marks.".format(name, marks))
print("%s scored %d marks." % (name, marks))
```

F-strings are generally easier to read when the variables are already available in the current scope.

---

# 19. Taking String Input from the User

The `input()` function reads a line of text entered by the user and returns it as a string.

```python
name = input("Enter your name: ")

print("Welcome,", name)
```

If the user enters `Amaan`, the output is:

```text
Welcome, Amaan
```

## Example: Read two strings

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print("Full name:", full_name)
```

## Removing leading and trailing whitespace

```python
name = input("Enter your name: ").strip()

print(f"Welcome, {name}!")
```

Use `strip()` when outer whitespace should not be retained.

**Important:** The `input()` function returns text even when the user types digits. Use explicit type conversion when numeric input is required.

---

# 20. Type Conversion with Strings

Type conversion means converting a value from one data type to another.

## 20.1 Convert an integer to a string

```python
age = 22

age_text = str(age)

print(age_text)
print(type(age_text))
```

Output:

```text
22
<class 'str'>
```

## 20.2 Convert a string to an integer

```python
number_text = "100"

number = int(number_text)

print(number + 50)
```

Output:

```text
150
```

## 20.3 Convert a string to a float

```python
price_text = "99.50"

price = float(price_text)

print(price + 0.50)
```

Output:

```text
100.0
```

## 20.4 Handle invalid numeric input

```python
value = input("Enter an integer: ")

try:
    number = int(value)
    print("Converted number:", number)
except ValueError:
    print("Invalid integer input.")
```

Converting text such as `"hello"` to an integer raises a `ValueError`.

## Common mistake: Adding strings instead of numbers

```python
first = "10"
second = "20"

print(first + second)
```

Output:

```text
1020
```

This is concatenation, not numeric addition.

For numeric addition:

```python
first = "10"
second = "20"

print(int(first) + int(second))
```

Output:

```text
30
```

---

# 21. Comparing Strings

Strings can be compared using comparison operators.

```python
first = "python"
second = "python"
third = "Python"

print(first == second)
print(first == third)
print(first != third)
```

Output:

```text
True
False
True
```

String equality compares the sequence of characters, including case and spaces.

## Case-insensitive comparison

```python
first = "Python"
second = "PYTHON"

print(first.lower() == second.lower())
```

Output:

```text
True
```

For more advanced case-insensitive comparison involving Unicode text, `casefold()` may be more appropriate than `lower()`.

```python
first = "Python"
second = "PYTHON"

print(first.casefold() == second.casefold())
```

Output:

```text
True
```

## Comparing strings with spaces

```python
first = "Python"
second = " Python"

print(first == second)
```

Output:

```text
False
```

A leading space is part of the string. Use `.strip()` before comparison only when surrounding whitespace should be ignored.

---

# 22. Common String Programming Patterns

The following patterns are used frequently in programming exercises.

## 22.1 Reverse a string

```python
text = "hello"
print(text[::-1])
```

Output: `olleh`

## 22.2 Count vowels

```python
text = "Education"
vowels = "aeiou"

count = sum(1 for ch in text.lower() if ch in vowels)

print(count)
```

Output: `5`

## 22.3 Count words

```python
sentence = "Python is easy to learn"
words = sentence.split()

print(len(words))
```

Output: `5`

## 22.4 Remove whitespace at both ends

```python
text = "   Python   "

print(text.strip())
```

Output: `Python`

## 22.5 Replace spaces with hyphens

```python
text = "learn Python today"

print(text.replace(" ", "-"))
```

Output: `learn-Python-today`

## 22.6 Check a substring

```python
text = "I am learning Python"

if "Python" in text:
    print("Python was found.")
else:
    print("Python was not found.")
```

Output: `Python was found.`

## 22.7 Count unique characters

```python
text = "banana"

unique_characters = set(text)

print(unique_characters)
print(len(unique_characters))
```

The order of characters in a printed set is not guaranteed.

The number of unique characters is `3`.

## 22.8 Build a string from a list of parts

```python
parts = ["I", "am", "learning", "Python"]

sentence = " ".join(parts)

print(sentence)
```

Output: `I am learning Python`

---

# 23. Twelve Solved String Problems with Logic

The `03_string.py` program contains these twelve solved problems in an interactive menu.

For each problem, understand three things:

1. What is the input?
2. What processing or logic is required?
3. What should the program display?

## Problem 1: Reverse a String

**Question:** Enter a string and display it in reverse order.

Example input:

```text
Python
```

Output:

```text
nohtyP
```

### Logic

1. Read the text.
2. Use slicing with `[::-1]`.
3. Display the reversed text.

```python
text = input("Enter a string: ")

reversed_text = text[::-1]

print(reversed_text)
```

**Concepts used:** Slicing and negative steps.

## Problem 2: Check a Palindrome

**Question:** Determine whether text reads the same forward and backward.

Example:

```text
Input: Madam
Output: It is a palindrome.
```

The supplied program ignores differences in case and removes characters that are not letters or numbers before checking.

### Logic

1. Read the text.
2. Convert applicable letters to lowercase.
3. Keep only alphanumeric characters.
4. Reverse the normalized text.
5. Compare the normalized text with its reverse.

```python
text = input("Enter text: ")

cleaned = "".join(
    ch.lower()
    for ch in text
    if ch.isalnum()
)

if cleaned and cleaned == cleaned[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
```

Example:

```text
Input: Never odd or even
Output: It is a palindrome.
```

The `cleaned` check makes sure that the normalized input contains at least one letter or number.

**Concepts used:** `lower()`, `isalnum()`, `join()` and slicing.

## Problem 3: Count Vowels

**Question:** Count the occurrences of `a`, `e`, `i`, `o` and `u` in a string.

Example:

```text
Input: Education
Output: 5
```

### Logic

1. Read the text.
2. Convert it to lowercase.
3. Check every character against `"aeiou"`.
4. Add one for every matching character.

```python
text = input("Enter a string: ").lower()

vowels = "aeiou"
count = sum(1 for ch in text if ch in vowels)

print("Number of vowels:", count)
```

**Concepts used:** Loops, membership operators and string normalization.

## Problem 4: Count Characters Excluding Whitespace

**Question:** Count characters excluding whitespace, then compare with the total number of characters.

Example:

```text
Input: Hi there
Characters excluding whitespace: 7
Total characters including spaces: 8
```

### Logic

1. Read a string.
2. Use `len()` to count all characters.
3. Check each character using `isspace()`.
4. Count the characters for which `isspace()` is false.

```python
text = input("Enter a string: ")

without_whitespace = sum(
    1
    for ch in text
    if not ch.isspace()
)

print("Without whitespace:", without_whitespace)
print("Total:", len(text))
```

**Concepts used:** `len()` and `isspace()`.

## Problem 5: Count Words in a Sentence

**Question:** Count the words in a sentence.

Example:

```text
Input: Python is easy to learn
Output: 5
```

### Logic

1. Read a sentence.
2. Call `split()` without an argument.
3. Count the resulting list elements using `len()`.

```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))
```

Using `split()` without an argument handles runs of whitespace more conveniently than splitting on a single space.

**Concepts used:** `split()` and `len()`.

## Problem 6: Find the First and Last Character

**Question:** Display the first and last characters of a string.

Example:

```text
Input: Programming
First character: P
Last character: g
```

### Logic

1. Read the text.
2. Check whether it is empty.
3. If non-empty, access index `0` and index `-1`.

```python
text = input("Enter a string: ")

if text:
    print("First:", text[0])
    print("Last:", text[-1])
else:
    print("The string is empty.")
```

**Concepts used:** Positive indexing, negative indexing and conditions.

## Problem 7: Generate Initials from a Full Name

**Question:** Convert a full name into initials.

Example:

```text
Input: Amaan Syed
Output: A.S.
```

### Logic

1. Split the name into words.
2. Extract the first character of every word.
3. Convert each initial to uppercase.
4. Join the initials using a period.
5. Add the final period.

```python
name = input("Enter your full name: ")

words = name.split()

initials = ".".join(word[0].upper() for word in words)

print(initials + ".")
```

**Concepts used:** `split()`, indexing, `upper()` and `join()`.

## Problem 8: Replace Spaces with Hyphens

**Question:** Replace spaces in a sentence with hyphens.

Example:

```text
Input: learn Python today
Output: learn-Python-today
```

### Logic

1. Read a sentence.
2. Normalize repeated whitespace with `" ".join(text.split())`.
3. Replace spaces with hyphens.

```python
text = input("Enter a sentence: ")

normalized = " ".join(text.split())
result = normalized.replace(" ", "-")

print(result)
```

This approach converts runs of whitespace between words to one hyphen. It also removes leading and trailing whitespace from the normalized result.

**Concepts used:** `split()`, `join()` and `replace()`.

## Problem 9: Count a Character's Occurrences

**Question:** Count how often a specified character appears in the input.

Example:

```text
String: banana
Character: a
Output: 3
```

### Logic

1. Read a string.
2. Read the target character.
3. Ensure the target contains exactly one character.
4. Use `count()` to count its occurrences.

```python
text = input("Enter a string: ")
target = input("Enter one character: ")

if len(target) != 1:
    print("Enter exactly one character.")
else:
    print(text.count(target))
```

The comparison is case-sensitive. For example, `a` and `A` are different characters.

**Concepts used:** `len()` and `count()`.

## Problem 10: Remove Duplicate Characters

**Question:** Keep only the first occurrence of each character while preserving the order.

Example:

```text
Input: banana
Output: ban
```

### Logic

1. Create an empty list for the result.
2. Create a set to remember characters already seen.
3. Visit each character in order.
4. Append a character only if it has not been seen.
5. Join the collected characters into a string.

```python
text = input("Enter a string: ")

result = []
seen = set()

for ch in text:
    if ch not in seen:
        result.append(ch)
        seen.add(ch)

print("".join(result))
```

Spaces and punctuation are also characters, so the program keeps their first occurrences.

**Concepts used:** Loops, sets, lists and `join()`.

## Problem 11: Check Whether Two Strings Are Anagrams

**Question:** Determine whether two strings contain the same letters or characters in a different order.

Example:

```text
First string: listen
Second string: silent
Output: The strings are anagrams.
```

### Logic

1. Read the two strings.
2. Convert applicable letters to lowercase.
3. Ignore characters that are not alphanumeric.
4. Sort the normalized characters.
5. Compare the sorted lists.

```python
first = input("Enter first text: ")
second = input("Enter second text: ")

first_cleaned = sorted(
    ch.lower() for ch in first if ch.isalnum()
)

second_cleaned = sorted(
    ch.lower() for ch in second if ch.isalnum()
)

if first_cleaned and first_cleaned == second_cleaned:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
```

This version ignores case, whitespace and punctuation. It preserves the frequency of each remaining character, so repeated letters must match.

**Concepts used:** `lower()`, `isalnum()` and `sorted()`.

## Problem 12: Clean and Format a Name

**Question:** Remove unnecessary whitespace and display a name in title case.

Example:

```text
Input:   amaan   syed
Output: Amaan Syed
```

### Logic

1. Read the name.
2. Split it into words.
3. Join the words with one space.
4. Apply `title()`.

```python
name = input("Enter your name: ")

cleaned_name = " ".join(name.split())
formatted_name = cleaned_name.title()

print(formatted_name)
```

**Important:** `title()` is a basic capitalization method. It may not format every real-world personal name according to an individual's preferred spelling.

**Concepts used:** `split()`, `join()` and `title()`.

---

# 24. Five Unsolved Practice Problems

First try solving these independently. Write the code inside your own practice file before checking external examples.

## Practice Problem 1: Pangram Checker

Write a program to determine whether a sentence contains all 26 letters of the English alphabet.

Example:

```text
Input: The quick brown fox jumps over the lazy dog
Output: It is a pangram.
```

Hints:

- Convert the sentence to lowercase.
- Consider the letters `a` through `z`.
- A set can help you collect unique letters.

## Practice Problem 2: Find the Longest Word

Write a program to find the longest word in a sentence.

Example:

```text
Input: Python programming is interesting
Output: programming
```

Hints:

- Use `split()` to obtain the words.
- Use `max()` with `key=len`, or write a loop to compare lengths.
- Decide how to handle a sentence containing no words.

## Practice Problem 3: Count Character Categories

Write a program to count these categories separately:

- Alphabetic characters
- Digits
- Whitespace characters
- Special characters

Example input:

```text
Python 123!
```

For this exercise, define a special character as any character that is not alphabetic, a digit or whitespace.

Hints:

- Use `isalpha()`.
- Use `isdigit()`.
- Use `isspace()`.
- Everything else belongs to the special-character category.

## Practice Problem 4: Compress Consecutive Repeated Characters

Write a program that groups consecutive repetitions of the same character.

Example:

```text
Input: aaabbc
Output: a3b2c1
```

Another example:

```text
Input: abcd
Output: a1b1c1d1
```

Hints:

- Maintain a current character and a counter.
- Increase the counter when the next character matches.
- When the character changes, record the previous character and its count.
- Remember to record the final group after the loop.

## Practice Problem 5: Find the Most Frequent Character

Write a program that displays the most frequent character in a string.

Example:

```text
Input: banana
Output: a
```

Hints:

- Use a dictionary to record character frequencies.
- Alternatively, investigate `collections.Counter`.
- Decide how to handle ties.
- Decide whether whitespace should be included in the count.

---

# 25. Common Errors and Mistakes

## Mistake 1: Forgetting quotation marks

Incorrect:

```python
# name = Amaan
```

Python treats `Amaan` as an identifier, not a string literal.

Correct:

```python
name = "Amaan"
```

## Mistake 2: Using an invalid index

Incorrect:

```python
text = "Python"

# print(text[6])
```

The last valid index is `5`.

Correct:

```python
print(text[5])
```

## Mistake 3: Confusing the index with the number of characters

The string `"Python"` has six characters, but its final positive index is `5`.

This is because indexing begins at zero.

## Mistake 4: Expecting slicing to include the stop index

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

The character at index `3` is excluded.

## Mistake 5: Trying to modify a string by index

Incorrect:

```python
text = "python"

# text[0] = "P"
```

Correct:

```python
text = "P" + text[1:]
```

## Mistake 6: Using `+` with a string and a number

Incorrect:

```python
# print("Age: " + 22)
```

Correct:

```python
print("Age: " + str(22))
print(f"Age: {22}")
```

## Mistake 7: Confusing string addition with numeric addition

```python
print("10" + "20")         # 1020
print(int("10") + int("20"))  # 30
```

The first expression concatenates strings. The second adds integers.

## Mistake 8: Forgetting that string methods return results

```python
text = "python"
text.upper()

print(text)
```

Output:

```text
python
```

The original variable still refers to the lowercase string.

Correct:

```python
text = text.upper()

print(text)
```

Output:

```text
PYTHON
```

## Mistake 9: Assuming `strip()` removes every space

```python
text = "Python Programming"

print(text.strip())
```

The internal space remains because `strip()` removes whitespace only from the ends.

## Mistake 10: Mixing up `find()` and `index()`

- `find()` returns `-1` if the substring is absent.
- `index()` raises `ValueError` if the substring is absent.

Choose the method that matches how your program should handle missing text.

---

# 26. Best Practices

1. Use descriptive variable names such as `full_name`, `email_address` and `sentence`.
2. Prefer f-strings for readable output involving variables.
3. Use `.strip()` where surrounding whitespace should be ignored.
4. Check for empty strings before accessing characters by index.
5. Use `split()` and `join()` for text processing involving words.
6. Remember that most string methods return new strings.
7. Use `find()` when a missing substring should return `-1`.
8. Convert numeric input explicitly with `int()` or `float()`.
9. Handle invalid user input with suitable validation and exceptions.
10. Practise by solving a problem first, then testing normal, empty and unusual inputs.

### Efficiency note

When combining many string fragments in a loop, repeatedly using `result += part` may create unnecessary intermediate strings.

For a sequence of string fragments, building a list and joining it at the end is often a clearer and more efficient pattern.

```python
parts = ["Learn", "Python", "every", "day"]

sentence = " ".join(parts)

print(sentence)
```

Output:

```text
Learn Python every day
```

---

# 27. Quick Revision Table

| Concept | Syntax | Purpose |
|---|---|---|
| Create a string | `text = "Hello"` | Stores text |
| Find type | `type(text)` | Checks the data type |
| Find length | `len(text)` | Counts characters |
| Concatenate | `a + b` | Joins strings |
| Repeat | `text * 3` | Repeats a string |
| Index | `text[0]` | Gets one character |
| Negative index | `text[-1]` | Gets the last character |
| Slice | `text[0:3]` | Extracts a substring |
| Reverse | `text[::-1]` | Reverses a string |
| Uppercase | `text.upper()` | Converts applicable letters to uppercase |
| Lowercase | `text.lower()` | Converts applicable letters to lowercase |
| Remove outer whitespace | `text.strip()` | Trims the ends |
| Replace | `text.replace("a", "b")` | Returns replaced text |
| Split | `text.split()` | Produces a list of words |
| Join | `" ".join(words)` | Combines strings |
| Search | `text.find("Py")` | Returns index or `-1` |
| Count | `text.count("a")` | Counts occurrences |
| Membership | `"Py" in text` | Checks whether text exists |
| Formatting | `f"Hello {name}"` | Inserts values in text |
| Convert to string | `str(value)` | Produces a string representation |
| Check letters | `text.isalpha()` | Tests alphabetic characters |
| Check digits | `text.isdigit()` | Tests digit characters |

---

# 28. Important Interview and Viva Questions

### Q1. What is a string in Python?

A string is an immutable sequence of Unicode characters represented by the `str` data type.

### Q2. How do you create a string?

Use single, double or triple quotes.

```python
a = 'Python'
b = "Python"
c = """Python"""
```

### Q3. Is a string mutable or immutable?

A string is immutable. Its characters cannot be modified in place.

### Q4. What is the difference between an empty string and a space?

An empty string has length `0`. A string containing one space has length `1`.

### Q5. What is string indexing?

Indexing retrieves a character by position. Positive indexing starts at `0`, and negative indexing starts at `-1` from the end.

### Q6. What is string slicing?

Slicing extracts part of a string using `start`, `stop` and `step`.

### Q7. What is the difference between `find()` and `index()`?

`find()` returns `-1` if the substring is absent. `index()` raises `ValueError`.

### Q8. What is the difference between `split()` and `join()`?

`split()` separates a string into a list. `join()` combines strings from an iterable into one string.

### Q9. What is the use of `strip()`?

`strip()` removes leading and trailing whitespace by default.

### Q10. What is the purpose of `replace()`?

It returns a new string in which matching occurrences of a substring are replaced.

### Q11. What is an f-string?

An f-string is a formatted string literal that allows expressions inside braces.

```python
name = "Amaan"

print(f"Hello, {name}")
```

### Q12. What does `[::-1]` do?

It returns a reversed slice of the string.

### Q13. How does `len()` work with strings?

It returns the number of characters in the string, including spaces and punctuation.

### Q14. What does `input()` return?

It returns a string containing the user's entered line, without the terminating newline.

### Q15. Can you add a string and an integer using `+`?

Not directly. Convert the integer to a string or use an f-string.

### Q16. What is the difference between `"10" + "20"` and `10 + 20`?

The first concatenates strings to produce `"1020"`. The second performs integer addition to produce `30`.

### Q17. Why should we check an empty string before indexing?

An empty string has no characters, so accessing index `0` or `-1` raises `IndexError`.

### Q18. What is the difference between `lower()` and `casefold()`?

Both help with case-insensitive processing. `casefold()` is designed for more comprehensive Unicode case-insensitive matching.

---

# 29. Final Learning Checklist

Before moving to the next topic, make sure you can:

- [ ] Explain what a string is and identify its data type.
- [ ] Create strings using single, double and triple quotes.
- [ ] Use escape sequences and raw strings.
- [ ] Concatenate and repeat strings.
- [ ] Calculate string length using `len()`.
- [ ] Access characters using positive and negative indexing.
- [ ] Extract substrings using slicing.
- [ ] Explain string immutability.
- [ ] Use case-conversion and whitespace methods.
- [ ] Search and count substrings.
- [ ] Split sentences into words and join words into sentences.
- [ ] Use character-checking methods.
- [ ] Format text using f-strings.
- [ ] Convert input strings to numeric types safely.
- [ ] Solve basic palindrome, vowel-counting and anagram problems.
- [ ] Attempt all five unsolved questions independently.

---

# 30. How to Run the Program

Open PowerShell in your `DSA-Python` repository and run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\03_string\03_string.py"
```

The program presents a menu containing:

1. Twelve string examples
2. Twelve solved string problems
3. Five unsolved practice questions
4. A learning checklist

Run the examples, test the solved problems using different inputs, and attempt the practice questions without referring to solutions.

**Final advice:** Do not only read the notes. Type the examples yourself, predict their outputs, run the program and solve the exercises. This will help you build the foundation needed for DSA and further Python programming.
