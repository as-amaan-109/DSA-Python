# Output in Python

> **Topic:** Output in Python
>
> **Module:** Python Programming Fundamentals
>
> **Level:** Beginner to Intermediate
>
> **Main Function:** `print()`
>
> **Core Concepts:** Printing values, separators, line endings, escape sequences, f-strings, formatting, alignment, precision, and readable reports.

---

# Table of Contents

1. Introduction
2. Learning Objectives
3. What Is Output?
4. The `print()` Function
5. Printing Strings
6. Printing Numbers
7. Printing Variables
8. Printing Multiple Values
9. The `sep` Parameter
10. The `end` Parameter
11. Newlines in Output
12. Escape Sequences
13. Quotes and Backslashes
14. Multiline Strings
15. String Concatenation in Output
16. F-Strings
17. Expressions Inside F-Strings
18. The `str.format()` Method
19. Positional and Named Placeholders
20. Formatting Numbers
21. Decimal Precision
22. Text Alignment and Field Width
23. Padding, Signs, and Separators
24. Percentages and Scientific Notation
25. Printing Tables
26. Printing Reports
27. Printing Lists and Collections
28. Understanding `repr()` and `str()`
29. Output and Data Types
30. The `print()` Function Parameters
31. Output Streams and Advanced Printing
32. Debugging Output
33. Twelve Output Examples
34. Twelve Solved Problems
35. Ten Unsolved Practice Questions
36. Extended Output Practice
37. Common Mistakes
38. Output Formatting Best Practices
39. Viva and Interview Questions
40. Quick Revision Reference
41. Learning Checklist
42. Final Summary

---

# 1. Introduction

Output is an essential part of programming.

A program often needs to display its results, explain what happened, show calculations, report an error, or present information in a readable form.

Python provides the built-in `print()` function for displaying output.

For example:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

This is the simplest example of output in Python.

The program sends the text to its standard output stream, which is usually displayed in the terminal or console.

Consider another example:

```python
name = "Amaan"

print(name)
```

Output:

```text
Amaan
```

The program displays the value stored in the `name` variable.

Output can contain text, numbers, variables, expressions, calculations, formatted tables, and reports.

```python
name = "Amaan"
age = 22
marks = 92

print(name)
print(age)
print(marks)
```

Output:

```text
Amaan
22
92
```

In this topic, you will learn how to make output clear, consistent, readable, and useful.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

- Explain the meaning of output in programming.
- Use the `print()` function correctly.
- Print strings, integers, floats, Boolean values, and other objects.
- Print multiple values in a single statement.
- Understand the default separator used by `print()`.
- Customize separators through the `sep` parameter.
- Control line endings through the `end` parameter.
- Display multiline output.
- Use escape sequences such as `\n`, `\t`, and `\\`.
- Print quotation marks inside strings.
- Use f-strings to display variables and expressions.
- Use the `str.format()` method.
- Format floating-point numbers.
- Display a fixed number of decimal places.
- Align text and numeric values in columns.
- Create simple tables, receipts, and reports.
- Display lists and other collections.
- Understand the difference between `str()` and `repr()`.
- Explain the main parameters of the `print()` function.
- Use output for debugging and troubleshooting.
- Write programs that present results in a readable format.

---

# 3. What Is Output?

Output is the information produced by a program and made available to a user or another part of a system.

For beginner Python programs, output usually means the text and values displayed in a terminal, console, or notebook.

Examples of output include:

- A greeting.
- The result of a calculation.
- A student's marks.
- A formatted receipt.
- A multiplication table.
- A status message.
- A list of values.
- An error message.
- A summary of a user's information.

## 3.1 Input, Processing, and Output

Many programs follow three basic steps:

1. Input: collect information.
2. Processing: perform calculations or operations.
3. Output: display the result.

Example:

```python
first = 10
second = 20

total = first + second

print(total)
```

Output:

```text
30
```

The variables contain the input values for this example.

The `+` operator performs the calculation.

The `print()` function displays the result.

## 3.2 Displaying a Calculation

```python
first = 15
second = 5

result = first + second

print("First number:", first)
print("Second number:", second)
print("Total:", result)
```

Output:

```text
First number: 15
Second number: 5
Total: 20
```

This output is clearer than displaying only the number `20`, because it explains the meaning of each value.

## 3.3 Why Is Output Important?

Output helps users understand what a program has done.

It can communicate:

- Successful completion.
- Calculated results.
- Information collected from the user.
- Warnings and errors.
- Program progress.
- Summaries of data.
- Information in a required format.

Well-designed output improves usability and makes a program easier to debug.

---

# 4. The `print()` Function

The `print()` function displays objects as text.

## 4.1 Basic Syntax

```python
print(value)
```

You can also supply several values:

```python
print(value1, value2, value3)
```

The general form of the built-in function is:

```python
print(*objects, sep=" ", end="\n", file=None, flush=False)
```

The asterisk in `*objects` indicates that `print()` can accept multiple positional objects.

The parameters are explained later in this README.

## 4.2 Printing a String

```python
print("Python is easy to learn.")
```

Output:

```text
Python is easy to learn.
```

The quotation marks are part of Python's source-code syntax. They are not normally shown in the printed result.

## 4.3 Printing an Integer

```python
print(100)
```

Output:

```text
100
```

## 4.4 Printing a Float

```python
print(12.75)
```

Output:

```text
12.75
```

## 4.5 Printing a Boolean Value

```python
print(True)
print(False)
```

Output:

```text
True
False
```

Python displays Boolean values with a capital first letter.

## 4.6 Printing `None`

```python
print(None)
```

Output:

```text
None
```

`None` is a special Python value that represents the absence of a value.

It is not the same as the string `"None"`.

## 4.7 Printing a Complex Number

```python
print(3 + 4j)
```

Output:

```text
(3+4j)
```

Python displays the complex number using its standard representation.

## 4.8 Printing an Expression

```python
print(10 + 5)
print(10 * 5)
print(20 / 4)
```

Output:

```text
15
50
5.0
```

The expressions are evaluated before the resulting values are displayed.

## 4.9 Printing a Variable

```python
language = "Python"

print(language)
```

Output:

```text
Python
```

Do not place a variable name inside quotation marks unless you want to display the variable name as literal text.

Compare:

```python
name = "Amaan"

print(name)
print("name")
```

Output:

```text
Amaan
name
```

The first statement displays the value stored in the variable.

The second statement displays the literal word `name`.

---

# 5. Printing Strings

A string is a sequence of characters enclosed in quotation marks.

Strings may contain names, sentences, symbols, spaces, punctuation, and many other characters.

## 5.1 Double-Quoted String

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

## 5.2 Single-Quoted String

```python
print('Hello, Python!')
```

Output:

```text
Hello, Python!
```

Both forms are valid.

## 5.3 Strings Containing Spaces

```python
print("Learning Python Programming")
```

Output:

```text
Learning Python Programming
```

Spaces inside a quoted string are retained.

## 5.4 Empty String

```python
print("")
```

Output:

```text
```

The statement prints an empty string followed by the default line ending.

The line may appear blank in the terminal.

## 5.5 Printing Symbols

```python
print("**********")
print("##########")
print("----------")
```

Output:

```text
**********
##########
----------
```

Symbols can be useful for headings, borders, and visual separators.

## 5.6 Printing a Heading

```python
print("=" * 30)
print("PYTHON PROGRAMMING")
print("=" * 30)
```

Output:

```text
==============================
PYTHON PROGRAMMING
==============================
```

Multiplying a string by an integer repeats that string.

In this example, `"=" * 30` creates thirty equals signs.

## 5.7 Printing Decorative Lines

```python
print("-" * 20)
print("STUDENT REPORT")
print("-" * 20)
```

Output:

```text
--------------------
STUDENT REPORT
--------------------
```

This technique is useful for creating simple reports.

---

# 6. Printing Numbers

Python can display different numeric types directly.

## 6.1 Integer Output

```python
print(10)
print(-25)
print(0)
```

Output:

```text
10
-25
0
```

## 6.2 Float Output

```python
print(10.5)
print(-7.25)
print(0.0)
```

Output:

```text
10.5
-7.25
0.0
```

The normal printed representation of a float does not guarantee a fixed number of decimal places.

For example:

```python
print(12.50)
```

Output:

```text
12.5
```

If the display must always include two decimal places, formatting should be used.

## 6.3 Arithmetic Output

```python
print(10 + 20)
print(50 - 15)
print(6 * 7)
print(20 / 4)
```

Output:

```text
30
35
42
5.0
```

The expressions are calculated before printing.

## 6.4 Output with Labels

```python
age = 22

print("Age:", age)
```

Output:

```text
Age: 22
```

Labels make results easier to interpret.

## 6.5 Negative Numbers

```python
temperature = -5

print("Temperature:", temperature)
```

Output:

```text
Temperature: -5
```

## 6.6 Large Integers

```python
population = 1234567890

print(population)
```

Output:

```text
1234567890
```

A numeric value can be displayed without manually inserting grouping separators. Formatting options can add separators when desired.

---

# 7. Printing Variables

A variable is a name that refers to a value.

The `print()` function can display the value referenced by a variable.

## 7.1 One Variable

```python
name = "Amaan"

print(name)
```

Output:

```text
Amaan
```

## 7.2 Multiple Variables

```python
name = "Amaan"
age = 22
city = "Nanded"

print(name, age, city)
```

Output:

```text
Amaan 22 Nanded
```

When multiple objects are printed without a custom separator, one space is inserted between their printed representations.

## 7.3 Variables with Labels

```python
name = "Amaan"
age = 22
city = "Nanded"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

Output:

```text
Name: Amaan
Age: 22
City: Nanded
```

## 7.4 Printing a Variable's Value and Type

```python
score = 95

print("Value:", score)
print("Type:", type(score))
```

Output:

```text
Value: 95
Type: <class 'int'>
```

This is useful when learning data types and debugging programs.

## 7.5 Printing Several Data Types

```python
name = "Amaan"
age = 22
percentage = 85.5
is_student = True

print(name)
print(age)
print(percentage)
print(is_student)
```

Output:

```text
Amaan
22
85.5
True
```

Each value is displayed according to its type.

## 7.6 Printing a Variable after Updating It

```python
score = 70

print(score)

score = 90

print(score)
```

Output:

```text
70
90
```

The second statement displays the updated value.

## 7.7 Printing a Computed Variable

```python
length = 10
width = 5

area = length * width

print("Area:", area)
```

Output:

```text
Area: 50
```

Separating calculations from output is useful when the same result will be reused multiple times.

---

# 8. Printing Multiple Values

The `print()` function accepts multiple positional objects.

By default, it places a space between consecutive objects.

## 8.1 Two Values

```python
print("Hello", "Python")
```

Output:

```text
Hello Python
```

## 8.2 Three Values

```python
print("Python", "Programming", "Language")
```

Output:

```text
Python Programming Language
```

## 8.3 Text and Numbers

```python
name = "Amaan"
age = 22

print("Name:", name, "Age:", age)
```

Output:

```text
Name: Amaan Age: 22
```

This is valid because `print()` accepts objects of different types.

## 8.4 Multiple Numeric Values

```python
first = 10
second = 20
third = 30

print(first, second, third)
```

Output:

```text
10 20 30
```

## 8.5 Multiple Values with an Expression

```python
first = 10
second = 20

print("First:", first, "Second:", second, "Total:", first + second)
```

Output:

```text
First: 10 Second: 20 Total: 30
```

The expression `first + second` is evaluated before its result is displayed.

## 8.6 Default Separation

```python
print("A", "B", "C")
```

Output:

```text
A B C
```

The default separator is a single space.

## 8.7 Why Multiple Arguments Are Useful

Multiple arguments allow you to:

- Display labels and values together.
- Show calculation results.
- Compare values.
- Print debugging information.
- Display several variables in one statement.

For more complex formatting, f-strings may provide greater control and readability.

---

# 9. The `sep` Parameter

The `sep` parameter determines the separator inserted between multiple objects printed by `print()`.

The default separator is one space.

## 9.1 Syntax

```python
print(value1, value2, sep="separator")
```

The separator must be a string.

## 9.2 Default Separator

```python
print("2026", "10", "27")
```

Output:

```text
2026 10 27
```

The values are separated by spaces.

## 9.3 Hyphen Separator

```python
print("2026", "10", "27", sep="-")
```

Output:

```text
2026-10-27
```

The hyphen is placed between the three values.

## 9.4 Comma Separator

```python
print("Python", "Java", "SQL", sep=", ")
```

Output:

```text
Python, Java, SQL
```

The separator contains a comma followed by a space.

## 9.5 Pipe Separator

```python
print("Name", "Age", "City", sep=" | ")
```

Output:

```text
Name | Age | City
```

A pipe separator can be useful for simple text tables.

## 9.6 Arrow Separator

```python
print("Start", "Process", "Finish", sep=" -> ")
```

Output:

```text
Start -> Process -> Finish
```

## 9.7 Empty Separator

```python
print("Py", "thon", sep="")
```

Output:

```text
Python
```

An empty separator adds no characters between the objects.

## 9.8 Slash Separator

```python
print("27", "10", "2026", sep="/")
```

Output:

```text
27/10/2026
```

The separator is a slash.

## 9.9 Custom Separator with Numbers

```python
print(10, 20, 30, sep=" + ")
```

Output:

```text
10 + 20 + 30
```

The objects are displayed as text, and the string `" + "` is inserted between them.

## 9.10 `sep` Does Not Add a Separator at the End

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

The separator appears between adjacent objects. It is not automatically added before the first object or after the last object.

## 9.11 Reusing a Separator

```python
separator = " | "

print("A", "B", "C", sep=separator)
print("1", "2", "3", sep=separator)
```

Output:

```text
A | B | C
1 | 2 | 3
```

A variable can store the separator for reuse.

## 9.12 Important Rules for `sep`

- The default value is `" "`.
- The separator must be a string.
- It is inserted only between the printed objects.
- An empty string is a valid separator.
- A multi-character separator is allowed.
- The `sep` parameter does not replace the line ending controlled by `end`.

---

# 10. The `end` Parameter

The `end` parameter controls what `print()` writes after displaying its objects.

By default, `print()` ends with a newline character.

This means the next ordinary print statement starts on a new line.

## 10.1 Default `end` Behavior

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

The default value of `end` is `"\n"`.

## 10.2 Printing on the Same Line

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

The first statement ends with a space rather than a newline.

The second statement continues on the same line.

## 10.3 Using a Hyphen as the Ending

```python
print("Python", end="-")
print("Programming")
```

Output:

```text
Python-Programming
```

## 10.4 Using an Arrow as the Ending

```python
print("Step 1", end=" -> ")
print("Step 2", end=" -> ")
print("Step 3")
```

Output:

```text
Step 1 -> Step 2 -> Step 3
```

The last statement uses the default newline.

## 10.5 Printing a Sequence on One Line

```python
for number in range(1, 6):
    print(number, end=" ")

print()
```

Output:

```text
1 2 3 4 5
```

The loop prints each number followed by a space.

The final `print()` moves to a new line.

## 10.6 Printing Dots

```python
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="\n")
print("Complete")
```

Output:

```text
Loading...
Complete
```

An empty string as `end` adds no characters between successive print statements.

## 10.7 Printing a Progress Message

```python
print("Preparing", end=" -> ")
print("Processing", end=" -> ")
print("Finished")
```

Output:

```text
Preparing -> Processing -> Finished
```

This pattern is useful for displaying simple progress stages.

## 10.8 Difference Between `sep` and `end`

Compare these examples.

With `sep`:

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

With `end`:

```python
print("A", end="-")
print("B", end="-")
print("C")
```

Output:

```text
A-B-C
```

The displayed results are the same, but the behavior is different.

- `sep` inserts a string between multiple objects in one `print()` call.
- `end` inserts a string after the objects from a `print()` call.

## 10.9 Empty Ending

```python
print("Python", end="")
print("Output")
```

Output:

```text
PythonOutput
```

No space or newline is inserted between the two strings.

## 10.10 Custom Line Ending

```python
print("First", end=" | ")
print("Second", end=" | ")
print("Third")
```

Output:

```text
First | Second | Third
```

## 10.11 Common Mistakes with `end`

A frequent mistake is expecting a new line when `end` has been changed.

```python
print("A", end="")
print("B")
```

Output:

```text
AB
```

The first statement does not end with a newline.

Another frequent mistake is forgetting the spacing in a custom ending.

```python
print("Hello", end="")
print("World")
```

Output:

```text
HelloWorld
```

If a space is required, include one explicitly:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

## 10.12 Rules to Remember

- The default ending is a newline.
- `end=""` removes the automatically added newline.
- `end=" "` ends the output with a space.
- `end="-"` ends the output with a hyphen.
- `end` must be a string.
- If you use a custom ending, remember that the next statement continues from the position where the previous output stopped.

---

# 11. Newlines in Output

A newline begins a new line of text.

Python's `print()` function automatically appends a newline by default.

You can also place newline characters inside strings.

## 11.1 Separate Print Statements

```python
print("First line")
print("Second line")
print("Third line")
```

Output:

```text
First line
Second line
Third line
```

Each call ends with a newline.

## 11.2 Newline Escape Sequence

The sequence `\n` represents a newline character in an ordinary Python string.

```python
print("First line\nSecond line")
```

Output:

```text
First line
Second line
```

Both lines come from one print statement.

## 11.3 Three Lines in One String

```python
message = "Line 1\nLine 2\nLine 3"

print(message)
```

Output:

```text
Line 1
Line 2
Line 3
```

The variable contains newline characters.

## 11.4 Blank Lines

```python
print("Heading")
print()
print("Content")
```

Output:

```text
Heading

Content
```

A call to `print()` without objects produces a blank line.

## 11.5 Multiple Blank Lines

```python
print("Start")
print()
print()
print("Finish")
```

Output:

```text
Start


Finish
```

Two empty print statements create two blank lines between the text lines.

## 11.6 A Newline at the End of a String

```python
print("Hello\n")
print("World")
```

Output:

```text
Hello

World
```

There is a newline inside the string and also the default newline added by the first `print()` call.

This produces a blank line between the two words.

## 11.7 Report with Newlines

```python
report = (
    "STUDENT REPORT\n"
    "Name: Amaan\n"
    "Subject: Python\n"
    "Status: Complete"
)

print(report)
```

Output:

```text
STUDENT REPORT
Name: Amaan
Subject: Python
Status: Complete
```

Parentheses allow adjacent string literals to be written across multiple source lines.

The strings are combined before they are printed.

## 11.8 Newlines in Address Output

```python
address = "Amaan Syed\nNanded\nMaharashtra\nIndia"

print(address)
```

Output:

```text
Amaan Syed
Nanded
Maharashtra
India
```

## 11.9 Newline Versus `end`

These statements produce two separate lines:

```python
print("A")
print("B")
```

These statements produce the same line:

```python
print("A", end="")
print("B")
```

A newline can therefore be controlled through either the content of a string or the ending parameter.

## 11.10 Important Difference

A newline character inside a string is part of that string.

The newline added by default by `print()` is part of the function's output behavior.

Both can affect the final appearance of output.

---

# 12. Escape Sequences

An escape sequence is a special sequence of characters used inside a string.

Escape sequences usually begin with a backslash.

They allow you to represent characters that are difficult to type directly or that have a special meaning in strings.

## 12.1 Common Escape Sequences

| Escape sequence | Meaning |
|---|---|
| `\n` | Newline |
| `\t` | Horizontal tab |
| `\\` | Literal backslash |
| `\'` | Single quotation mark |
| `\"` | Double quotation mark |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |
| `\v` | Vertical tab |
| `\a` | Alert character |
| `\ooo` | Character represented by an octal value |
| `\xhh` | Character represented by a hexadecimal value |
| `\uXXXX` | Unicode character using four hexadecimal digits |
| `\UXXXXXXXX` | Unicode character using eight hexadecimal digits |

The visible behavior of some control characters depends on the terminal or output environment.

## 12.2 Newline: `\n`

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

## 12.3 Tab: `\t`

```python
print("Name\tAge\tCity")
print("Amaan\t22\tNanded")
```

Typical output:

```text
Name    Age     City
Amaan   22      Nanded
```

A tab advances to a tab stop. Its visual spacing depends on the terminal.

## 12.4 Backslash: `\\`

```python
print("C:\\Users\\Amaan")
```

Output:

```text
C:\Users\Amaan
```

Each pair of backslashes represents one literal backslash in the string.

## 12.5 Single Quote: `\'`

```python
print('It\'s Python')
```

Output:

```text
It's Python
```

The escaped single quote is displayed as a literal apostrophe.

## 12.6 Double Quote: `\"`

```python
print("She said, \"Hello!\"")
```

Output:

```text
She said, "Hello!"
```

## 12.7 Carriage Return: `\r`

```python
print("Hello\rWorld")
```

The carriage return moves the output position to the beginning of the current line in environments that honor this control character.

The visible result depends on the terminal because characters after the carriage return may overwrite earlier characters.

It is often best to study `\r` separately from normal line breaks.

## 12.8 Backspace: `\b`

```python
print("AB\bC")
```

The backspace character moves the output position backward in environments that honor it.

The exact visible result may vary because terminals handle control characters differently.

## 12.9 Unicode Escape

```python
print("\u03A9")
```

Output:

```text
Ω
```

The escape sequence represents a Unicode code point.

## 12.10 Multiple Escape Sequences

```python
print("Name:\tAmaan\nCity:\tNanded")
```

Output:

```text
Name:   Amaan
City:   Nanded
```

The tab characters separate the labels and values, while the newline starts a new line.

## 12.11 Printing a Literal Backslash and `n`

Sometimes you want to display the characters `\n` rather than create a newline.

```python
print("\\n")
```

Output:

```text
\n
```

The first backslash escapes the second backslash.

The resulting string contains a literal backslash followed by the letter `n`.

## 12.12 Recognizing Escapes

Compare the following expressions:

```python
print("A\nB")
print("A\\nB")
```

Output:

```text
A
B
A\nB
```

The first expression contains a newline.

The second expression contains a literal backslash and `n`.

This difference is important when displaying paths, code examples, and debugging information.

---

# 13. Quotes and Backslashes

Quotation marks normally delimit Python string literals.

Sometimes quotation marks or apostrophes must also appear in the displayed text.

There are several ways to achieve this.

## 13.1 Single Quotes around Double Quotes

```python
print('She said, "Hello."')
```

Output:

```text
She said, "Hello."
```

The outer single quotes allow double quotes inside the string without escaping them.

## 13.2 Double Quotes around an Apostrophe

```python
print("It's a useful language.")
```

Output:

```text
It's a useful language.
```

The apostrophe does not need to be escaped because the string uses double quotes.

## 13.3 Escaping a Matching Quote

```python
print("She said, \"Hello.\"")
```

Output:

```text
She said, "Hello."
```

The double quotation marks are escaped because the string itself uses double quotes.

## 13.4 Escaping an Apostrophe

```python
print('It\'s Python.')
```

Output:

```text
It's Python.
```

## 13.5 Printing a Backslash

```python
print("\\")
```

Output:

```text
\
```

## 13.6 Printing Several Backslashes

```python
print("\\\\")
```

Output:

```text
\\
```

Each pair of backslashes produces one literal backslash.

## 13.7 Windows-Style Paths

```python
path = "C:\\Users\\Amaan\\Documents"

print(path)
```

Output:

```text
C:\Users\Amaan\Documents
```

Alternatively, a raw string can often simplify Windows-style path literals:

```python
path = r"C:\Users\Amaan\Documents"

print(path)
```

Output:

```text
C:\Users\Amaan\Documents
```

A raw string changes how backslashes are interpreted in the literal.

A raw string cannot end with a single unmatched backslash, because the final backslash would escape the closing quotation mark.

## 13.8 Printing Quoted User Text

```python
name = "Amaan"

print(f'Name: "{name}"')
```

Output:

```text
Name: "Amaan"
```

F-strings can be combined with different quote styles to create readable output.

---

# 14. Multiline Strings

A multiline string can contain line breaks within one string literal.

Python supports triple-single-quoted and triple-double-quoted strings.

## 14.1 Triple-Double-Quoted String

```python
message = """Welcome to Python.
This is the second line.
This is the third line."""

print(message)
```

Output:

```text
Welcome to Python.
This is the second line.
This is the third line.
```

## 14.2 Triple-Single-Quoted String

```python
message = '''First line
Second line
Third line'''

print(message)
```

Output:

```text
First line
Second line
Third line
```

## 14.3 Multiline Output Report

```python
report = """STUDENT REPORT
Name: Amaan
Course: Python
Status: Complete"""

print(report)
```

Output:

```text
STUDENT REPORT
Name: Amaan
Course: Python
Status: Complete
```

## 14.4 Triple Quotes versus `\n`

These two approaches can create the same visible output.

Using newline escapes:

```python
print("First line\nSecond line\nThird line")
```

Using a multiline string:

```python
print("""First line
Second line
Third line""")
```

Both produce three lines.

## 14.5 Leading and Trailing Newlines

The placement of the text after the opening triple quote matters.

```python
message = """
Python
Output
"""

print(repr(message))
```

The representation includes the newline characters created by the layout of the multiline string.

When formatting a report, make sure the opening and closing triple quotes are positioned intentionally.

## 14.6 Indentation inside Multiline Strings

```python
message = """Report
    Name: Amaan
    City: Nanded"""

print(message)
```

Output:

```text
Report
    Name: Amaan
    City: Nanded
```

The leading spaces before `Name` and `City` are part of the string.

They are not automatically removed.

## 14.7 When Are Multiline Strings Useful?

Multiline strings are useful for:

- Welcome messages.
- Help text.
- Report headings.
- Address blocks.
- Simple documentation.
- Displaying several related lines as one message.

For output that changes according to variables, f-strings may be more appropriate.

---

# 15. String Concatenation in Output

String concatenation means joining strings together.

Python uses the `+` operator for string concatenation.

## 15.1 Basic Concatenation

```python
first = "Hello"
second = "Python"

result = first + second

print(result)
```

Output:

```text
HelloPython
```

No separator is automatically inserted.

## 15.2 Concatenation with a Space

```python
first = "Hello"
second = "Python"

result = first + " " + second

print(result)
```

Output:

```text
Hello Python
```

The space must be included explicitly.

## 15.3 Three Strings

```python
first = "Learn"
second = "Python"
third = "Today"

result = first + " " + second + " " + third

print(result)
```

Output:

```text
Learn Python Today
```

## 15.4 Concatenation Does Not Automatically Convert Numbers

This code raises a `TypeError`:

```python
age = 22

# print("Age: " + age)
```

The left operand is a string, but the right operand is an integer.

Convert the integer to a string:

```python
age = 22

print("Age: " + str(age))
```

Output:

```text
Age: 22
```

For complicated output, an f-string is usually more readable than repeated concatenation.

## 15.5 Concatenation versus Multiple Print Arguments

Concatenation:

```python
print("Hello" + " " + "World")
```

Output:

```text
Hello World
```

Multiple arguments:

```python
print("Hello", "World")
```

Output:

```text
Hello World
```

The second example automatically inserts the default separator, which is a single space.

## 15.6 When Should Concatenation Be Used?

Concatenation is suitable when:

- Combining a small number of strings.
- Building a string from known text segments.
- Creating a simple result from strings.

For output containing many variables, expressions, formatting rules, or numeric values, f-strings are generally clearer.

---

# 16. F-Strings

An f-string is a formatted string literal that allows variables and expressions to be embedded inside a string.

F-strings are one of the most useful ways to create readable output in modern Python.

## 16.1 Basic Syntax

```python
name = "Amaan"

print(f"Hello, {name}!")
```

Output:

```text
Hello, Amaan!
```

The letter `f` appears immediately before the opening quotation mark.

The expression inside braces is evaluated and its result is included in the string.

## 16.2 Displaying Multiple Variables

```python
name = "Amaan"
age = 22
city = "Nanded"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
```

Output:

```text
My name is Amaan.
I am 22 years old.
I live in Nanded.
```

## 16.3 Combining Several Values

```python
name = "Amaan"
age = 22
city = "Nanded"

print(f"Name: {name}, Age: {age}, City: {city}")
```

Output:

```text
Name: Amaan, Age: 22, City: Nanded
```

## 16.4 Displaying Calculations

```python
first = 10
second = 20

print(f"Sum: {first + second}")
print(f"Product: {first * second}")
```

Output:

```text
Sum: 30
Product: 200
```

The expressions are evaluated before the final string is displayed.

## 16.5 Displaying a Variable and Its Value

```python
score = 95

print(f"Score: {score}")
```

Output:

```text
Score: 95
```

## 16.6 Displaying an Expression with Context

```python
length = 10
width = 5

print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {length * width}")
```

Output:

```text
Length: 10
Width: 5
Area: 50
```

## 16.7 Formatting a Float

```python
price = 125.6789

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 125.68
```

The format specifier `:.2f` displays the number with two digits after the decimal point.

## 16.8 Adding a Percentage Symbol

```python
percentage = 87.4567

print(f"Percentage: {percentage:.2f}%")
```

Output:

```text
Percentage: 87.46%
```

The percent sign after the closing brace is literal text.

This example assumes that `percentage` already contains a value such as `87.4567`, rather than a fraction such as `0.874567`.

## 16.9 Expressions Inside Braces

```python
first = 8
second = 4

print(f"Addition: {first + second}")
print(f"Subtraction: {first - second}")
print(f"Multiplication: {first * second}")
```

Output:

```text
Addition: 12
Subtraction: 4
Multiplication: 32
```

## 16.10 Calling Methods Inside an F-String

```python
name = "amaan syed"

print(f"Uppercase: {name.upper()}")
print(f"Title case: {name.title()}")
```

Output:

```text
Uppercase: AMAAN SYED
Title case: Amaan Syed
```

Method calls can be used inside expressions in f-strings.

## 16.11 F-String with a Conditional Expression

```python
marks = 75

print(f"Result: {'Pass' if marks >= 40 else 'Fail'}")
```

Output:

```text
Result: Pass
```

A conditional expression can select which text to display.

## 16.12 Printing Braces Literally

To display a literal opening or closing brace in an f-string, double it.

```python
name = "Amaan"

print(f"{{Name: {name}}}")
```

Output:

```text
{Name: Amaan}
```

The doubled braces are displayed as single braces.

## 16.13 F-Strings and Data Types

An f-string converts the result of an expression into text for output.

```python
number = 10

result = f"Value: {number}"

print(result)
print(type(result).__name__)
```

Output:

```text
Value: 10
str
```

The f-string produces a string.

The original variable `number` remains an integer.

## 16.14 When Should F-Strings Be Used?

F-strings are useful when:

- Displaying variables with labels.
- Combining text and numbers.
- Formatting decimal values.
- Displaying calculations.
- Producing receipts and reports.
- Controlling output alignment.
- Making output statements easier to read.

---

# 17. Expressions Inside F-Strings

An f-string can contain expressions inside braces.

The expression is evaluated at runtime, and its result is included in the displayed string.

## 17.1 Arithmetic Expressions

```python
a = 12
b = 3

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b}")
```

Output:

```text
Sum: 15
Difference: 9
Product: 36
Quotient: 4.0
```

## 17.2 Expressions with Parentheses

```python
a = 10
b = 5
c = 2

print(f"Result: {(a + b) * c}")
```

Output:

```text
Result: 30
```

Parentheses determine the order of evaluation.

## 17.3 String Expressions

```python
first = "Python"
second = "Programming"

print(f"{first} {second}")
print(f"{first.upper()} is useful.")
```

Output:

```text
Python Programming
PYTHON is useful.
```

## 17.4 Length Expressions

```python
message = "Python"

print(f"Message: {message}")
print(f"Character count: {len(message)}")
```

Output:

```text
Message: Python
Character count: 6
```

## 17.5 Expressions Using Lists

```python
numbers = [10, 20, 30]

print(f"Numbers: {numbers}")
print(f"Count: {len(numbers)}")
print(f"Total: {sum(numbers)}")
```

Output:

```text
Numbers: [10, 20, 30]
Count: 3
Total: 60
```

## 17.6 Calling a Function

```python
def square(number):
    return number * number


value = 5

print(f"Value: {value}")
print(f"Square: {square(value)}")
```

Output:

```text
Value: 5
Square: 25
```

Functions can calculate values that are then included in output.

## 17.7 Avoiding Complicated Expressions

Although expressions can be placed inside f-strings, complex calculations may be easier to understand when calculated separately.

Less readable:

```python
print(f"Average: {(10 + 20 + 30 + 40 + 50) / 5}")
```

More readable:

```python
numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

print(f"Average: {average}")
```

Both produce:

```text
Average: 30.0
```

The second version separates calculation logic from presentation.

---

# 18. The `str.format()` Method

The `str.format()` method inserts values into a string using replacement fields.

It is another approach to formatted output.

## 18.1 Basic Syntax

```python
"Some text {}".format(value)
```

The braces mark a replacement field.

## 18.2 Basic Example

```python
name = "Amaan"

print("Hello, {}!".format(name))
```

Output:

```text
Hello, Amaan!
```

## 18.3 Multiple Placeholders

```python
name = "Amaan"
age = 22

print("Name: {}, Age: {}".format(name, age))
```

Output:

```text
Name: Amaan, Age: 22
```

The values are inserted in positional order.

## 18.4 Positional Indexes

```python
print("{0} likes {1}".format("Amaan", "Python"))
```

Output:

```text
Amaan likes Python
```

The index `0` refers to the first value, and index `1` refers to the second.

## 18.5 Reusing a Positional Index

```python
print("{0} is learning {1}. {0} enjoys programming.".format("Amaan", "Python"))
```

Output:

```text
Amaan is learning Python. Amaan enjoys programming.
```

The first value is reused through the index `0`.

## 18.6 Named Placeholders

```python
print(
    "Name: {name}, City: {city}".format(
        name="Amaan",
        city="Nanded",
    )
)
```

Output:

```text
Name: Amaan, City: Nanded
```

Named placeholders can make longer formatting statements easier to understand.

## 18.7 Numeric Precision with `format()`

```python
price = 125.6789

print("Price: {:.2f}".format(price))
```

Output:

```text
Price: 125.68
```

The `:.2f` format specifier requests two digits after the decimal point.

## 18.8 Comparing F-Strings and `format()`

F-string:

```python
name = "Amaan"
age = 22

print(f"Name: {name}, Age: {age}")
```

Using `format()`:

```python
name = "Amaan"
age = 22

print("Name: {}, Age: {}".format(name, age))
```

Both display:

```text
Name: Amaan, Age: 22
```

F-strings are usually more convenient for straightforward formatting in modern Python code.

The `format()` method remains useful when the format template is stored separately from the values.

---

# 19. Positional and Named Placeholders

Replacement fields in `str.format()` can refer to values through position or name.

## 19.1 Automatic Positional Fields

```python
print("{} + {} = {}".format(10, 20, 30))
```

Output:

```text
10 + 20 = 30
```

Values fill the replacement fields in order.

## 19.2 Indexed Fields

```python
print("{2}, {0}, {1}".format("A", "B", "C"))
```

Output:

```text
C, A, B
```

The field indexes determine which argument is selected.

## 19.3 Named Fields

```python
print("{name} studies {subject}.".format(
    name="Amaan",
    subject="Python",
))
```

Output:

```text
Amaan studies Python.
```

## 19.4 Named Fields with Numeric Formatting

```python
print(
    "Price: {price:.2f}".format(price=125.6789)
)
```

Output:

```text
Price: 125.68
```

## 19.5 Mixing Placeholder Styles

In practice, use a clear and consistent placeholder style.

For beginner programs, avoid mixing indexed placeholders, automatic placeholders, and named placeholders unnecessarily.

Clear formatting makes programs easier to maintain.

---

# 20. Formatting Numbers

Numeric formatting controls how numbers appear in output.

The value used for calculation does not necessarily need to match its presentation.

For example, a float may contain several decimal places, while the output displays only two.

## 20.1 Default Float Display

```python
number = 12.5

print(number)
```

Output:

```text
12.5
```

## 20.2 Fixed Decimal Places

```python
number = 12.5

print(f"{number:.2f}")
```

Output:

```text
12.50
```

The format specifier displays two digits after the decimal point.

## 20.3 Three Decimal Places

```python
number = 3.141592

print(f"{number:.3f}")
```

Output:

```text
3.142
```

## 20.4 One Decimal Place

```python
number = 98.76

print(f"{number:.1f}")
```

Output:

```text
98.8
```

## 20.5 No Digits after the Decimal Point

```python
number = 12.8

print(f"{number:.0f}")
```

Output:

```text
13
```

The `f` format type applies rounding for display rather than simply removing the decimal digits.

## 20.6 Thousands Separator

```python
number = 1234567

print(f"{number:,}")
```

Output:

```text
1,234,567
```

The comma format option groups digits with commas.

## 20.7 Thousands Separator with Decimal Precision

```python
number = 1234567.8912

print(f"{number:,.2f}")
```

Output:

```text
1,234,567.89
```

## 20.8 Scientific Notation

```python
number = 1250000

print(f"{number:e}")
```

Output:

```text
1.250000e+06
```

Scientific notation can be useful for very large or very small values.

## 20.9 Percentage Formatting

A fraction can be displayed as a percentage using the `%` format type.

```python
ratio = 0.875

print(f"{ratio:.1%}")
```

Output:

```text
87.5%
```

The `%` format type multiplies the value by 100 for display and appends a percent sign.

## 20.10 Important Formatting Rule

Formatting controls the displayed representation.

It does not necessarily change the original value.

```python
number = 12.5678

formatted = f"{number:.2f}"

print(formatted)
print(number)
```

Output:

```text
12.57
12.5678
```

The variable `formatted` contains a string, while `number` remains a float.

---

# 21. Decimal Precision

Decimal precision determines how many digits are displayed after a decimal point when using a suitable numeric format specifier.

## 21.1 Two Decimal Places

```python
price = 99.999

print(f"{price:.2f}")
```

Output:

```text
100.00
```

The value is rounded for display to two digits after the decimal point.

## 21.2 Three Decimal Places

```python
value = 12.34567

print(f"{value:.3f}")
```

Output:

```text
12.346
```

## 21.3 Comparing Precision Settings

```python
value = 3.14159265

print(f"{value:.0f}")
print(f"{value:.1f}")
print(f"{value:.2f}")
print(f"{value:.3f}")
print(f"{value:.4f}")
```

Output:

```text
3
3.1
3.14
3.142
3.1416
```

## 21.4 Preserve a Particular Display Width

```python
value = 5.5

print(f"{value:.2f}")
print(f"{value:.4f}")
```

Output:

```text
5.50
5.5000
```

Trailing zeros are useful when a report needs consistent decimal formatting.

## 21.5 Rounding and Storage

```python
value = 5.6789

display_value = f"{value:.2f}"

print(display_value)
print(value)
```

Output:

```text
5.68
5.6789
```

The formatted string does not replace the numeric value.

## 21.6 When Does Precision Matter?

Precision matters when displaying:

- Prices.
- Percentages.
- Averages.
- Measurements.
- Scientific values.
- Scores.
- Calculated totals.

Different applications have different display and arithmetic requirements.

---

# 22. Text Alignment and Field Width

Formatting can reserve space for a value so that multiple lines align into columns.

The general pattern is:

```python
f"{value:alignment_width}"
```

Useful alignment characters include:

- `<` for left alignment.
- `>` for right alignment.
- `^` for centered alignment.

## 22.1 Left Alignment

```python
print(f"{'Python':<15}|")
print(f"{'Java':<15}|")
print(f"{'C++':<15}|")
```

Output:

```text
Python         |
Java           |
C++            |
```

Each field occupies fifteen character positions.

## 22.2 Right Alignment

```python
print(f"{'Python':>15}|")
print(f"{'Java':>15}|")
print(f"{'C++':>15}|")
```

Output:

```text
         Python|
           Java|
            C++|
```

The text is placed at the right side of the field.

## 22.3 Center Alignment

```python
print(f"{'Python':^15}|")
print(f"{'Java':^15}|")
print(f"{'C++':^15}|")
```

Output:

```text
    Python    |
      Java    |
       C++    |
```

Center alignment places the text approximately in the middle of the field.

## 22.4 Formatting a Table Header

```python
print(f"{'Name':<15}{'Language':<15}{'Score':>8}")
```

Output:

```text
Name           Language          Score
```

The first two columns are left-aligned, while the score column is right-aligned.

## 22.5 Formatting Table Rows

```python
print(f"{'Amaan':<15}{'Python':<15}{92:>8}")
print(f"{'Sara':<15}{'Java':<15}{88:>8}")
print(f"{'Ali':<15}{'SQL':<15}{85:>8}")
```

Output:

```text
Amaan          Python                92
Sara           Java                  88
Ali            SQL                   85
```

## 22.6 Width Does Not Usually Truncate Long Text

```python
print(f"{'ProgrammingLanguage':<10}|")
```

Output:

```text
ProgrammingLanguage|
```

The text may exceed the specified width.

Field width controls the minimum available width, not a maximum text length.

## 22.7 Formatting Multiple Values

```python
name = "Amaan"
score = 92

print(f"Name: {name:<15} Score: {score:>5}")
```

Output:

```text
Name: Amaan       Score:    92
```

The width specifiers improve the visual alignment.

---

# 23. Padding, Signs, and Separators

Formatting options can control how values are displayed inside a field.

They are especially useful for tables, financial summaries, progress reports, and aligned numeric columns.

## 23.1 Padding with Spaces

```python
print(f"{'Python':10}|")
print(f"{'Java':10}|")
```

Output:

```text
Python    |
Java      |
```

The default padding character is a space.

## 23.2 Padding with Zeros

```python
number = 42

print(f"{number:05d}")
print(f"{7:05d}")
print(f"{123:05d}")
```

Output:

```text
00042
00007
00123
```

The `0` option pads the integer with zeros to the requested width.

The `d` format type indicates decimal integer formatting.

## 23.3 Explicit Positive Signs

```python
print(f"{25:+d}")
print(f"{-25:+d}")
```

Output:

```text
+25
-25
```

The `+` sign requests a sign for both positive and negative values.

## 23.4 A Space for Positive Values

```python
print(f"{25: d}")
print(f"{-25: d}")
```

Output:

```text
 25
-25
```

A leading space is used for positive numbers, while a minus sign remains visible for negative numbers.

## 23.5 Thousand Separators

```python
population = 123456789

print(f"{population:,}")
```

Output:

```text
123,456,789
```

## 23.6 Zero Padding and Width

```python
for number in range(1, 6):
    print(f"Item {number:03d}")
```

Output:

```text
Item 001
Item 002
Item 003
Item 004
Item 005
```

The numbers are formatted with three digits.

## 23.7 Combining Alignment and Precision

```python
price = 125.5

print(f"{price:>12.2f}")
```

Output:

```text
      125.50
```

The value is right-aligned in a field of twelve character positions and displayed with two decimal places.

## 23.8 Combining Several Formatting Options

```python
value = 12345.6789

print(f"{value:>15,.2f}")
```

Output:

```text
      12,345.68
```

The format uses field width, grouping separators, and decimal precision.

The exact spacing is determined by the width and the formatted value.

---

# 24. Percentages and Scientific Notation

The `print()` function can display values in different numeric formats.

Percentage and scientific notation formats are especially useful when ordinary decimal output is not the clearest representation.

## 24.1 Percentage as a Fraction

```python
ratio = 0.75

print(f"{ratio:.0%}")
```

Output:

```text
75%
```

The `%` format type converts a ratio into a percentage representation.

## 24.2 Percentage with One Decimal Place

```python
ratio = 0.87456

print(f"{ratio:.1%}")
```

Output:

```text
87.5%
```

## 24.3 Percentage with Two Decimal Places

```python
ratio = 0.875678

print(f"{ratio:.2%}")
```

Output:

```text
87.57%
```

## 24.4 Percentage Values Already Expressed on a 0–100 Scale

If a variable already contains `87.5` as a percentage value, do not apply the `%` format type directly unless multiplying by 100 is intended.

```python
percentage = 87.5

print(f"{percentage:.2f}%")
```

Output:

```text
87.50%
```

The literal `%` is appended to the number without scaling it.

## 24.5 Scientific Notation

```python
number = 1500000

print(f"{number:e}")
```

Output:

```text
1.500000e+06
```

## 24.6 Scientific Notation with Precision

```python
number = 0.000012345

print(f"{number:.3e}")
```

Output:

```text
1.235e-05
```

Scientific notation is useful when displaying extremely small or very large numbers.

## 24.7 Uppercase Scientific Notation

```python
number = 1250000

print(f"{number:.2E}")
```

Output:

```text
1.25E+06
```

## 24.8 Choosing a Format

| Requirement | Example | Purpose |
|---|---|---|
| Two decimal places | `f"{value:.2f}"` | Fixed-point display |
| Percentage from a ratio | `f"{ratio:.1%}"` | Fraction-to-percentage display |
| Comma separators | `f"{number:,}"` | Group large numbers |
| Scientific notation | `f"{number:.3e}"` | Display very large or small values |
| Right alignment | `f"{value:>10}"` | Align values in a field |
| Zero padding | `f"{number:05d}"` | Display a fixed-width integer |

---

# 25. Printing Tables

A table organizes information into rows and columns.

Python's `print()` function can display simple text tables without external libraries.

Tables are useful for marks, prices, reports, item lists, and comparison results.

## 25.1 A Simple Table

```python
print("Name    Score")
print("Amaan   92")
print("Sara    88")
print("Ali     85")
```

Output:

```text
Name    Score
Amaan   92
Sara    88
Ali     85
```

The spacing is manually written.

This approach is suitable for very small examples, but it can become difficult to maintain when values have different lengths.

## 25.2 Table Using F-Strings

```python
print(f"{'Name':<15}{'Score':>8}")
print(f"{'Amaan':<15}{92:>8}")
print(f"{'Sara':<15}{88:>8}")
print(f"{'Ali':<15}{85:>8}")
```

Output:

```text
Name              Score
Amaan                92
Sara                 88
Ali                  85
```

The alignment specifiers make the columns more consistent.

## 25.3 Table with Three Columns

```python
print(f"{'Name':<12}{'Subject':<15}{'Marks':>8}")
print("-" * 35)

print(f"{'Amaan':<12}{'Python':<15}{92:>8}")
print(f"{'Sara':<12}{'Java':<15}{88:>8}")
print(f"{'Ali':<12}{'SQL':<15}{85:>8}")
```

Output:

```text
Name        Subject           Marks
-----------------------------------
Amaan       Python               92
Sara        Java                 88
Ali         SQL                  85
```

## 25.4 Table with Decimal Values

```python
print(f"{'Item':<15}{'Price':>12}")
print("-" * 27)
print(f"{'Keyboard':<15}{799.5:>12.2f}")
print(f"{'Mouse':<15}{499.0:>12.2f}")
```

Output:

```text
Item                  Price
---------------------------
Keyboard             799.50
Mouse                499.00
```

The `.2f` format ensures the price always displays two decimal places.

## 25.5 Table from a List of Tuples

```python
records = [
    ("Amaan", "Python", 92),
    ("Sara", "Java", 88),
    ("Ali", "SQL", 85),
]

print(f"{'Name':<12}{'Language':<15}{'Score':>8}")
print("-" * 35)

for name, language, score in records:
    print(f"{name:<12}{language:<15}{score:>8}")
```

Output:

```text
Name        Language          Score
-----------------------------------
Amaan       Python               92
Sara        Java                 88
Ali         SQL                  85
```

Using a loop avoids writing a separate print statement for each record.

## 25.6 Table with an Index

```python
subjects = ["Python", "Java", "SQL"]

print(f"{'No.':<6}{'Subject'}")
print("-" * 20)

for number, subject in enumerate(subjects, start=1):
    print(f"{number:<6}{subject}")
```

Output:

```text
No.   Subject
--------------------
1     Python
2     Java
3     SQL
```

## 25.7 Table with Totals

```python
prices = [100, 200, 300]

print("ITEM PRICES")
print("-" * 20)

for number, price in enumerate(prices, start=1):
    print(f"Item {number}: {price:.2f}")

print("-" * 20)
print(f"Total: {sum(prices):.2f}")
```

Output:

```text
ITEM PRICES
--------------------
Item 1: 100.00
Item 2: 200.00
Item 3: 300.00
--------------------
Total: 600.00
```

## 25.8 Table Design Tips

- Use a clear header row.
- Keep each column's width consistent.
- Use right alignment for many numeric columns.
- Use left alignment for names and descriptive text.
- Use separators only where they improve readability.
- Use loops for repeated rows.
- Use consistent numeric precision.
- Avoid unnecessary decorative symbols.
- Test long values to make sure the table remains understandable.

---

# 26. Printing Reports

Reports combine several related values into one readable output.

They are useful for displaying user information, calculations, results, receipts, and summaries.

## 26.1 Basic Report

```python
name = "Amaan"
city = "Nanded"
language = "Python"

print("=" * 35)
print("USER REPORT".center(35))
print("=" * 35)
print(f"Name: {name}")
print(f"City: {city}")
print(f"Language: {language}")
print("=" * 35)
```

Output:

```text
===================================
           USER REPORT
===================================
Name: Amaan
City: Nanded
Language: Python
===================================
```

## 26.2 Report with Calculations

```python
first = 20
second = 30

total = first + second
average = total / 2

print("CALCULATION REPORT")
print("-" * 25)
print(f"First value : {first}")
print(f"Second value: {second}")
print(f"Total       : {total}")
print(f"Average     : {average:.2f}")
```

Output:

```text
CALCULATION REPORT
-------------------------
First value : 20
Second value: 30
Total       : 50
Average     : 25.00
```

## 26.3 Student Report

```python
name = "Amaan"
marks = [90, 85, 92, 88, 95]

total = sum(marks)
average = total / len(marks)

print("=" * 35)
print("STUDENT REPORT".center(35))
print("=" * 35)
print(f"Student: {name}")
print(f"Subjects: {len(marks)}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print("=" * 35)
```

Output:

```text
===================================
         STUDENT REPORT
===================================
Student: Amaan
Subjects: 5
Total: 450
Average: 90.00
===================================
```

## 26.4 Receipt

```python
item = "Keyboard"
quantity = 2
price = 799.50

total = quantity * price

print("=" * 35)
print("RECEIPT".center(35))
print("=" * 35)
print(f"Item     : {item}")
print(f"Quantity : {quantity}")
print(f"Unit price: {price:.2f}")
print(f"Total    : {total:.2f}")
print("=" * 35)
```

Output:

```text
===================================
              RECEIPT
===================================
Item     : Keyboard
Quantity : 2
Unit price: 799.50
Total    : 1599.00
===================================
```

## 26.5 Report Formatting Checklist

Before printing a report, check:

1. Is the heading clear?
2. Are related values grouped together?
3. Does each number have an understandable label?
4. Are decimal places consistent?
5. Are columns aligned where necessary?
6. Are the units displayed?
7. Are unnecessary blank lines avoided?
8. Are the final results easy to identify?

---

# 27. Printing Lists and Collections

Python collections can be printed directly.

A collection may contain several values, but the default representation may not be the most readable way to present them.

## 27.1 Print a List Directly

```python
subjects = ["Python", "Java", "SQL"]

print(subjects)
```

Output:

```text
['Python', 'Java', 'SQL']
```

The square brackets and quotes are part of the list's printed representation.

## 27.2 Print Items Separately

```python
subjects = ["Python", "Java", "SQL"]

for subject in subjects:
    print(subject)
```

Output:

```text
Python
Java
SQL
```

This is useful when each item should appear on a separate line.

## 27.3 Print Items with Numbers

```python
subjects = ["Python", "Java", "SQL"]

for number, subject in enumerate(subjects, start=1):
    print(f"{number}. {subject}")
```

Output:

```text
1. Python
2. Java
3. SQL
```

## 27.4 Print Items on One Line

```python
subjects = ["Python", "Java", "SQL"]

print(*subjects)
```

Output:

```text
Python Java SQL
```

The asterisk unpacks the list so its elements become separate arguments to `print()`.

## 27.5 Print Items with a Custom Separator

```python
subjects = ["Python", "Java", "SQL"]

print(*subjects, sep=" | ")
```

Output:

```text
Python | Java | SQL
```

## 27.6 Print a Dictionary

```python
student = {
    "name": "Amaan",
    "age": 22,
    "city": "Nanded",
}

print(student)
```

The dictionary is displayed using Python's dictionary representation.

For a more readable presentation, print each key and value:

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Output:

```text
name: Amaan
age: 22
city: Nanded
```

## 27.7 Print a Nested Collection

```python
records = [
    ["Amaan", 92],
    ["Sara", 88],
]

for record in records:
    print(record)
```

Output:

```text
['Amaan', 92]
['Sara', 88]
```

The same information can be displayed with labels and formatting for easier reading.

## 27.8 When Should a Collection Be Printed Directly?

Direct printing is convenient during experimentation and debugging.

For user-facing output, consider whether the default representation is clear enough.

If not, use a loop, an f-string, or an appropriate formatting pattern.

---

# 28. Understanding `repr()` and `str()`

Python provides ways to obtain a textual representation of an object.

The `str()` function generally aims to provide a human-friendly representation.

The `repr()` function aims to provide a representation useful for inspection and debugging.

## 28.1 Basic String Example

```python
text = "Hello\nPython"

print(str(text))
print(repr(text))
```

Output:

```text
Hello
Python
'Hello\nPython'
```

The `str()` result displays the newline.

The `repr()` result shows the escape sequence, making it easier to inspect the string's contents.

## 28.2 Inspecting Spaces

```python
text = "  Hello  "

print(str(text))
print(repr(text))
```

Output:

```text
  Hello  
'  Hello  '
```

The quotes in the `repr()` result help make the spaces visible.

## 28.3 Numeric Values

```python
number = 25

print(str(number))
print(repr(number))
```

Output:

```text
25
25
```

For simple integer values, the results may look the same.

## 28.4 Lists

```python
values = [10, 20, 30]

print(str(values))
print(repr(values))
```

For this list, the printed representations are normally the same.

## 28.5 Using `repr()` for Debugging

Suppose a string appears to contain extra spaces.

```python
name = "   Amaan   "

print(name)
print(repr(name))
```

Output:

```text
   Amaan   
'   Amaan   '
```

The representation makes surrounding whitespace easier to notice.

## 28.6 When Should `repr()` Be Used?

Use `repr()` when inspecting:

- String whitespace.
- Escape sequences.
- Values during debugging.
- Lists and dictionaries.
- Objects whose ordinary display hides useful details.

For normal user-facing messages, `print()` and f-strings are often more suitable.

---

# 29. Output and Data Types

The displayed appearance of a value does not always reveal its data type.

Python's `print()` function displays objects, but the data type still matters to the rest of the program.

## 29.1 Integer and String

```python
number = 100
text = "100"

print(number)
print(text)

print(type(number).__name__)
print(type(text).__name__)
```

Output:

```text
100
100
int
str
```

The visible values look alike, but their types differ.

## 29.2 Float and Formatted Text

```python
price = 99.5

formatted = f"{price:.2f}"

print(formatted)
print(type(formatted).__name__)
```

Output:

```text
99.50
str
```

The formatted result is a string.

## 29.3 Boolean Values

```python
active = True

print(active)
print(type(active).__name__)
```

Output:

```text
True
bool
```

## 29.4 Printing `None`

```python
value = None

print(value)
print(type(value).__name__)
```

Output:

```text
None
NoneType
```

The string `"None"` and the special value `None` are different objects.

## 29.5 Checking a Formatted Result

```python
number = 12.3456
display_text = f"{number:.2f}"

print(display_text)
print(number)
```

Output:

```text
12.35
12.3456
```

Formatting the value does not overwrite the original numeric variable.

---

# 30. The `print()` Function Parameters

The built-in `print()` function includes several parameters that control output behavior.

The general form is:

```python
print(*objects, sep=" ", end="\n", file=None, flush=False)
```

## 30.1 `objects`

These are the values to be printed.

```python
print("Python", 10, True)
```

Output:

```text
Python 10 True
```

## 30.2 `sep`

This parameter controls the separator between objects.

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

## 30.3 `end`

This parameter controls what is written after the objects.

```python
print("Hello", end="!")
print("World")
```

Output:

```text
Hello!World
```

## 30.4 `file`

This parameter specifies a writable file-like object for the output.

When omitted, output normally goes to standard output.

A basic example is:

```python
print("Displayed in the terminal")
```

An advanced example writes output to an opened text file:

```python
with open("output_example.txt", "w", encoding="utf-8") as file:
    print("This text is written to a file.", file=file)
```

The text is written to `output_example.txt` rather than displayed by that print call in the terminal.

File handling is a separate topic, but the example demonstrates what the `file` parameter can do.

## 30.5 `flush`

This Boolean parameter controls whether the output stream is flushed after printing.

```python
print("Processing...", flush=True)
```

Flushing can be useful when output must become visible promptly.

Its exact practical effect depends on the output stream and environment.

## 30.6 Parameter Comparison

| Parameter | Purpose | Typical use |
|---|---|---|
| `objects` | Values to display | Strings, numbers, expressions |
| `sep` | Separates multiple objects | Dates, tables, readable lists |
| `end` | Specifies the ending text | Same-line printing |
| `file` | Selects the destination stream | Files or alternate streams |
| `flush` | Requests output flushing | Progress messages and interactive output |

---

# 31. Output Streams and Advanced Printing

In ordinary beginner programs, `print()` usually displays output in a terminal.

Python also supports output streams, such as standard output and standard error.

Understanding these concepts is useful when writing scripts, debugging programs, and working with command-line applications.

## 31.1 Standard Output

Standard output is commonly called `stdout`.

It is the default destination used by `print()`.

```python
print("This message goes to standard output.")
```

Typical terminal output:

```text
This message goes to standard output.
```

## 31.2 Standard Error

Standard error is commonly called `stderr`.

It is normally used for warnings and error messages.

```python
import sys

print("Normal message", file=sys.stdout)
print("Warning message", file=sys.stderr)
```

The two messages use different streams.

Their visible order can vary when output streams are captured or displayed separately by an environment.

## 31.3 Redirecting Output to a File

The `file` parameter can direct output to a writable file object.

```python
with open("report.txt", "w", encoding="utf-8") as file:
    print("Python Output Report", file=file)
    print("Status: Complete", file=file)
```

The file `report.txt` receives the two lines of output.

The `with` statement closes the file automatically when the block finishes.

## 31.4 Appending Output to a File

The file's opening mode determines whether existing contents are replaced or new contents are appended.

```python
with open("report.txt", "a", encoding="utf-8") as file:
    print("Another report entry", file=file)
```

The `"a"` mode appends output rather than replacing the existing file contents.

File-handling details are covered in a separate topic.

## 31.5 Output with `flush=True`

```python
print("Preparing output...", flush=True)
```

The `flush=True` argument requests that the output stream be flushed after printing.

Flushing can be helpful in interactive applications where visible output should not remain buffered unnecessarily.

## 31.6 When Does Standard Output Matter?

Standard output is used for:

- Displaying program results.
- Showing progress information.
- Printing help messages.
- Providing command-line output.
- Capturing output in tests.
- Piping the output of one command into another.

## 31.7 When Does Standard Error Matter?

Standard error is useful for:

- Error messages.
- Warnings.
- Diagnostic output.
- Messages that should be separated from ordinary results.

## 31.8 Keep the Main Topic in Perspective

For beginner exercises, focus first on:

- What is printed.
- Which values are printed.
- How separators are inserted.
- How the line ending works.
- How formatting changes the result.

The `file` and `flush` parameters are useful extensions, but they are not required for every small program.

---

# 32. Debugging with Output

Debugging is the process of finding and understanding errors in a program.

Printing selected values is one of the simplest debugging techniques.

## 32.1 Printing a Variable

```python
score = 90

print(score)
```

The output lets you inspect the variable's current value.

## 32.2 Printing with a Label

```python
score = 90

print("DEBUG score:", score)
```

Output:

```text
DEBUG score: 90
```

Labels make debugging messages easier to identify.

## 32.3 Printing Several Variables

```python
quantity = 3
price = 100
total = quantity * price

print("DEBUG quantity:", quantity)
print("DEBUG price:", price)
print("DEBUG total:", total)
```

Output:

```text
DEBUG quantity: 3
DEBUG price: 100
DEBUG total: 300
```

## 32.4 Using an F-String for Debugging

```python
quantity = 3
price = 100

print(f"DEBUG: quantity={quantity}, price={price}")
```

Output:

```text
DEBUG: quantity=3, price=100
```

## 32.5 Inspecting a Data Type

```python
value = "100"

print("Value:", repr(value))
print("Type:", type(value).__name__)
```

Output:

```text
Value: '100'
Type: str
```

This helps distinguish a string from a numeric value.

## 32.6 Debugging Intermediate Calculations

```python
first = 10
second = 5

total = first + second
average = total / 2

print("First:", first)
print("Second:", second)
print("Total:", total)
print("Average:", average)
```

Output:

```text
First: 10
Second: 5
Total: 15
Average: 7.5
```

Inspecting intermediate values can help locate an incorrect calculation.

## 32.7 Debugging Unexpected Whitespace

```python
text = "   Python   "

print("Normal:", text)
print("Representation:", repr(text))
```

Output:

```text
Normal:    Python
Representation: '   Python   '
```

`repr()` can reveal whitespace that is difficult to see in normal output.

## 32.8 Removing Debug Messages

Debug messages are useful during development.

Before publishing a program, review them and remove unnecessary internal messages.

Keep output that is helpful to the intended user.

## 32.9 Output Is Not a Complete Testing Strategy

Printed values help explain what a program is doing, but they do not automatically prove that every calculation is correct.

Testing should include:

- Expected normal inputs.
- Boundary values.
- Invalid inputs.
- Empty values when applicable.
- Cases that previously produced an error.

For large projects, automated tests and debugging tools are also important.

---

# 33. Twelve Core Output Examples

The Python program's first menu option demonstrates twelve core examples.

This section summarizes their purpose and provides additional exercises to deepen understanding.

## Example 1: Basic Output

```python
print("Hello, Python!")
print("Welcome to programming.")
```

Output:

```text
Hello, Python!
Welcome to programming.
```

**Concept:** The `print()` function displays text.

Additional practice:

```python
print("Good morning.")
print("Learning Python.")
print("Practice every day.")
```

Expected output:

```text
Good morning.
Learning Python.
Practice every day.
```

## Example 2: Printing Multiple Values

```python
name = "Amaan"
age = 22

print(name, age)
```

Output:

```text
Amaan 22
```

**Concept:** Multiple objects can be supplied to one `print()` call.

Additional practice:

```python
print("Python", 3, True)
print("Score", 90, "marks")
```

Output:

```text
Python 3 True
Score 90 marks
```

## Example 3: Custom Separators

```python
print("2026", "10", "27", sep="-")
print("Python", "Programming", "Output", sep=" | ")
```

Output:

```text
2026-10-27
Python | Programming | Output
```

**Concept:** The `sep` parameter customizes the text between objects.

Additional practice:

```python
print("A", "B", "C", sep=":")
print(10, 20, 30, sep=" + ")
print("Start", "End", sep=" -> ")
```

Output:

```text
A:B:C
10 + 20 + 30
Start -> End
```

## Example 4: Custom Endings

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

**Concept:** The `end` parameter controls the end of a print call.

Additional practice:

```python
print("A", end="-")
print("B", end="-")
print("C")
```

Output:

```text
A-B-C
```

## Example 5: Newline Escape Sequence

```python
print("First line\nSecond line\nThird line")
```

Output:

```text
First line
Second line
Third line
```

**Concept:** `\n` creates a line break inside the string.

## Example 6: Tab Escape Sequence

```python
print("Name\tAge\tCity")
print("Amaan\t22\tNanded")
```

Typical output:

```text
Name    Age     City
Amaan   22      Nanded
```

**Concept:** `\t` inserts a horizontal tab.

## Example 7: Quotation Marks

```python
print("She said, \"Python is useful.\"")
print('It\'s a good programming language.')
```

Output:

```text
She said, "Python is useful."
It's a good programming language.
```

**Concept:** Matching quotation marks can be escaped when needed.

## Example 8: F-Strings

```python
name = "Amaan"
language = "Python"

print(f"{name} is learning {language}.")
```

Output:

```text
Amaan is learning Python.
```

**Concept:** Variables can be inserted into a formatted string.

## Example 9: Expressions Inside F-Strings

```python
first = 10
second = 20

print(f"{first} + {second} = {first + second}")
```

Output:

```text
10 + 20 = 30
```

**Concept:** Expressions can be evaluated inside the braces of an f-string.

## Example 10: `str.format()`

```python
name = "Amaan"
score = 92

print("Name: {}, Score: {}".format(name, score))
```

Output:

```text
Name: Amaan, Score: 92
```

**Concept:** The `format()` method fills replacement fields.

## Example 11: Alignment

```python
print(f"{'Name':<12}{'Score':>8}")
print(f"{'Amaan':<12}{92:>8}")
print(f"{'Sara':<12}{88:>8}")
```

Output:

```text
Name           Score
Amaan              92
Sara               88
```

**Concept:** Field width and alignment create readable columns.

## Example 12: Numeric Precision

```python
price = 125.6789
percentage = 87.4567

print(f"Price: {price:.2f}")
print(f"Percentage: {percentage:.2f}%")
```

Output:

```text
Price: 125.68
Percentage: 87.46%
```

**Concept:** Format specifiers control numeric presentation.

---

# 34. Twelve Solved Problems Explained

The Python program includes twelve solved problems that can be selected through its interactive menu.

The following explanations describe their goals, methods, and expected behavior.

## Problem 1: Personalized Greeting

**Objective:** Accept a name and display a personalized greeting.

**Concepts:** `input()`, variables, f-strings, and `print()`.

Sample run:

```text
Enter your name: Amaan
Hello, Amaan!
Welcome to Python programming.
```

The program reads the name and includes it in the output.

The greeting is produced dynamically instead of using a fixed name in the source code.

## Problem 2: Profile Card

**Objective:** Display several user details in a structured layout.

**Concepts:** Multiple variables, labels, borders, and f-strings.

Sample run:

```text
Enter your name: Amaan
Enter your city: Nanded
Enter your favourite language: Python
```

The program then displays a formatted card:

```text
----------------------------------------
              USER PROFILE
----------------------------------------
Name     : Amaan
City     : Nanded
Language : Python
----------------------------------------
```

This example demonstrates how headings and labels improve readability.

## Problem 3: Arithmetic Report

**Objective:** Display the results of arithmetic operations.

**Concepts:** Numeric calculations, labels, and numeric formatting.

The program displays:

- Addition.
- Subtraction.
- Multiplication.
- Division when the divisor is nonzero.

Example:

```text
Enter the first number: 10
Enter the second number: 5
```

Output includes:

```text
Arithmetic Results
------------------------------
Addition       : 15.0
Subtraction    : 5.0
Multiplication : 50.0
Division       : 2.00
------------------------------
```

The input helpers return floating-point values, so calculations involving these values produce float results.

The division check prevents division by zero.

## Problem 4: Separator Demonstration

**Objective:** Display values using different separators.

**Concept:** The `sep` parameter.

Example:

```text
Enter first item: Python
Enter second item: Java
Enter third item: SQL
```

The program produces different presentations:

```text
Default separator:
Python Java SQL

Comma separator:
Python, Java, SQL

Arrow separator:
Python -> Java -> SQL

Pipe separator:
Python | Java | SQL
```

This demonstrates that the separator controls text between objects.

## Problem 5: End Parameter

**Objective:** Demonstrate how print statements can continue on the same line.

**Concept:** The `end` parameter.

Example output:

```text
First message continues on the same line.
Step 1 -> Step 2 -> Step 3
Loading...
```

The program uses different endings to demonstrate how line breaks and custom separators work.

## Problem 6: Multiline Address

**Objective:** Present an address in multiple lines.

**Concepts:** Several values, separate print statements, and report layout.

Sample run:

```text
Enter your name: Amaan
Enter house or building: House 12
Enter your city: Nanded
Enter your state: Maharashtra
Enter your country: India
```

Output:

```text
Address
------------------------------
Amaan
House 12
Nanded
Maharashtra
India
------------------------------
```

Each field appears on its own line.

## Problem 7: Formatted Receipt

**Objective:** Calculate and display a receipt.

**Concepts:** Arithmetic, f-strings, decimal precision, and labels.

Example:

```text
Enter item name: Keyboard
Enter quantity: 2
Enter unit price: 799.50
```

Output:

```text
========================================
             SALES RECEIPT
========================================
Item                 : Keyboard
Quantity             : 2
Unit price           : 799.50
Total                : 1599.00
========================================
```

The total is calculated as quantity multiplied by unit price.

The `:.2f` specifier ensures that monetary values are displayed with two decimal places.

## Problem 8: Marks Report

**Objective:** Collect marks and produce a summary.

**Concepts:** Loops, validation, arithmetic, and formatted output.

The program requires a positive number of subjects and checks that each mark is between zero and one hundred.

It then calculates:

- Total marks.
- Number of subjects.
- Average marks.
- Percentage for marks out of one hundred per subject.

If every subject uses the same maximum mark of 100, the average percentage is the average of the entered marks.

## Problem 9: Multiplication Table

**Objective:** Display the multiplication table of a number.

**Concepts:** Loops, expressions, and formatted output.

Example:

```text
Enter a number: 5
```

Output:

```text
Multiplication Table of 5
-------------------------
   5 x  1 =     5
   5 x  2 =    10
   5 x  3 =    15
   5 x  4 =    20
   5 x  5 =    25
   5 x  6 =    30
   5 x  7 =    35
   5 x  8 =    40
   5 x  9 =    45
   5 x 10 =    50
-------------------------
```

The alignment specifiers make the results easier to compare.

## Problem 10: Aligned Table

**Objective:** Display records in a set of aligned columns.

**Concepts:** Formatting, lists of tuples, loops, and field width.

The table uses consistent column widths for names, languages, and scores.

This technique can be reused when displaying many records.

## Problem 11: Escape Sequences

**Objective:** Display special characters and line control.

**Concepts:** `\n`, `\t`, `\\`, and quotation marks.

The program demonstrates:

- Multiple lines.
- Tab-separated values.
- Literal backslashes.
- Quotation marks inside output.

## Problem 12: Output Formatter

**Objective:** Let the user select how entered text should be displayed.

**Concepts:** A menu, conditionals, string methods, and alignment.

The options include:

1. Normal output.
2. Uppercase output.
3. Lowercase output.
4. Centered output.
5. Output surrounded by a border.

This problem combines input selection with different output styles.

### How to Practise the Solved Problems

For each problem:

1. Understand the objective.
2. Identify the information that must be displayed.
3. Work out the desired output before running the program.
4. Read the code and identify the role of each formatting rule.
5. Run the program with different values.
6. Test boundary cases when calculations are involved.
7. Recreate the solution without referring to the existing code.
8. Experiment with the output format without changing the calculation logic.

---

# 35. Ten Unsolved Practice Questions

Attempt each question independently before examining a solution.

## Question 1: Basic Information Output

Write a program that displays your name, age, city, and favourite programming language using separate print statements.

Requirements:

- Use meaningful labels.
- Put each field on a separate line.
- Make the output easy to read.

Expected format:

```text
Name: Amaan
Age: 22
City: Nanded
Language: Python
```

## Question 2: Formatted Profile Card

Create a profile card using f-strings.

Requirements:

- Include a heading.
- Display at least four fields.
- Use separator lines.
- Keep the output readable.

## Question 3: Custom Separators

Print three values using all of the following separators:

- A comma and a space.
- A hyphen.
- A pipe.
- An arrow.
- An empty separator.

Explain how the `sep` parameter changes the output.

## Question 4: Same-Line Output

Display three messages on a single line.

Requirements:

- Use the `end` parameter.
- Separate the messages using arrows.
- Ensure the final output ends with a newline.

## Question 5: Multiline Address

Ask for the user's name, house or building, city, state, and country.

Display the address on separate lines.

Use a heading and a border.

## Question 6: Formatted Receipt

Accept an item name, quantity, and unit price.

Calculate the total and display a receipt.

Requirements:

- Reject a non-positive quantity.
- Reject a negative unit price.
- Display prices with two decimal places.
- Label every field.
- Display a total.

## Question 7: Student Marks Report

Accept marks for several subjects.

Display each mark and calculate the total and average.

Requirements:

- Validate marks.
- Display the average to two decimal places.
- Use an aligned table.
- Explain the output format.

## Question 8: Multiplication Table

Accept a number and display its multiplication table from 1 to 10.

Requirements:

- Display a clear heading.
- Align the multiplication expressions.
- Show the final result for every row.

## Question 9: Escape-Sequence Demonstration

Create a program that demonstrates:

- Newline.
- Tab.
- Single quotation marks.
- Double quotation marks.
- Backslash.
- A literal `\n` sequence.

Explain how each escape sequence affects the displayed text.

## Question 10: Menu-Driven Output Formatter

Create a program with options to:

1. Display text normally.
2. Display text in uppercase.
3. Display text in lowercase.
4. Center the text in a field.
5. Display the text with a border.
6. Exit.

Requirements:

- Use an interactive menu.
- Validate the selected option.
- Use descriptive output.
- Keep the formatting logic organized.

---

# 36. Extended Output Practice

This section contains additional short exercises for practising output formatting independently.

Each exercise focuses on a small concept that can be tested quickly.

## 36.1 Display a Welcome Message

```python
print("Welcome to Python")
print("Start learning today")
```

Output:

```text
Welcome to Python
Start learning today
```

**Practice:** Change the text and add a third message.

## 36.2 Display a Heading with a Border

```python
print("*" * 25)
print("PYTHON OUTPUT")
print("*" * 25)
```

Output:

```text
*************************
PYTHON OUTPUT
*************************
```

**Practice:** Replace the asterisks with hyphens.

## 36.3 Print Multiple Numbers

```python
print(10, 20, 30, 40, 50)
```

Output:

```text
10 20 30 40 50
```

**Practice:** Display the numbers separated by commas.

## 36.4 Print Text with a Custom Separator

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

**Practice:** Try `sep=" | "` and `sep=" -> "`.

## 36.5 Print on One Line

```python
print("Python", end=" ")
print("Programming")
```

Output:

```text
Python Programming
```

**Practice:** Replace the ending space with a hyphen.

## 36.6 Print an Empty Line

```python
print("First")
print()
print("Second")
```

Output:

```text
First

Second
```

**Practice:** Add two blank lines between the messages.

## 36.7 Print a Date-Like String

```python
print("27", "10", "2026", sep="/")
```

Output:

```text
27/10/2026
```

**Practice:** Change the separator to a hyphen.

## 36.8 Display a Calculation

```python
first = 15
second = 25

print(first + second)
```

Output:

```text
40
```

**Practice:** Also display the subtraction and multiplication results.

## 36.9 Label the Calculation

```python
first = 15
second = 25

print("First:", first)
print("Second:", second)
print("Sum:", first + second)
```

Output:

```text
First: 15
Second: 25
Sum: 40
```

**Practice:** Use an f-string instead of multiple print arguments.

## 36.10 Format a Floating-Point Value

```python
value = 12.34567

print(f"{value:.2f}")
```

Output:

```text
12.35
```

**Practice:** Display the same number with one, three, and four decimal places.

## 36.11 Align Text to the Left

```python
print(f"{'Python':<15}|")
print(f"{'Java':<15}|")
```

Output:

```text
Python         |
Java           |
```

**Practice:** Display three programming languages with the same width.

## 36.12 Align Text to the Right

```python
print(f"{'Python':>15}|")
print(f"{'Java':>15}|")
```

Output:

```text
         Python|
           Java|
```

**Practice:** Align numeric scores to the right.

## 36.13 Center a Heading

```python
print(f"{'REPORT':^30}")
```

Output:

```text
            REPORT
```

The text is centered within a field of thirty characters.

**Practice:** Center a longer heading.

## 36.14 Display an Integer with Zero Padding

```python
number = 7

print(f"{number:03d}")
```

Output:

```text
007
```

**Practice:** Display numbers using four digits.

## 36.15 Format a Price

```python
price = 1250

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 1250.00
```

**Practice:** Add a currency label and display a total.

## 36.16 Format a Percentage

```python
ratio = 0.875

print(f"Completion: {ratio:.1%}")
```

Output:

```text
Completion: 87.5%
```

**Practice:** Test ratios such as `0.5` and `0.995`.

## 36.17 Display Several Lines from One String

```python
message = "Line 1\nLine 2\nLine 3"

print(message)
```

Output:

```text
Line 1
Line 2
Line 3
```

**Practice:** Create a four-line message.

## 36.18 Display a Tab-Separated Record

```python
print("Name\tAge\tCity")
print("Amaan\t22\tNanded")
```

The tab characters separate the values.

**Practice:** Add columns for a language and score.

## 36.19 Display Quotation Marks

```python
print('She said, "Hello!"')
print("It's Python.")
```

Output:

```text
She said, "Hello!"
It's Python.
```

**Practice:** Display a message containing both kinds of quotation marks.

## 36.20 Display a Literal Backslash

```python
print("Folder: C:\\Python")
```

Output:

```text
Folder: C:\Python
```

**Practice:** Display a Windows-style path with multiple folders.

## 36.21 Print a List on Separate Lines

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

Output:

```text
Python
Java
C++
```

**Practice:** Add five languages and number them.

## 36.22 Print a List with a Separator

```python
languages = ["Python", "Java", "C++"]

print(*languages, sep=" | ")
```

Output:

```text
Python | Java | C++
```

**Practice:** Use commas as the separator.

## 36.23 Print a Dictionary as Labels

```python
student = {
    "Name": "Amaan",
    "City": "Nanded",
    "Language": "Python",
}

for label, value in student.items():
    print(f"{label}: {value}")
```

Output:

```text
Name: Amaan
City: Nanded
Language: Python
```

**Practice:** Add two additional fields.

## 36.24 Display a Multiplication Result

```python
number = 6
multiplier = 7

print(f"{number} x {multiplier} = {number * multiplier}")
```

Output:

```text
6 x 7 = 42
```

**Practice:** Display the multiplication table from 1 to 10.

## 36.25 Display an Average

```python
marks = [80, 90, 100]

average = sum(marks) / len(marks)

print(f"Average: {average:.2f}")
```

Output:

```text
Average: 90.00
```

**Practice:** Change the marks and recalculate the average.

## 36.26 Create a Simple Status Message

```python
status = "Complete"

print(f"Status: {status}")
```

Output:

```text
Status: Complete
```

**Practice:** Display different statuses depending on a condition.

## 36.27 Display a Success Message

```python
task = "File processing"

print(f"{task}: successful")
```

Output:

```text
File processing: successful
```

**Practice:** Create a failure message with a meaningful explanation.

## 36.28 Print a Number with a Sign

```python
number = 25

print(f"{number:+d}")
```

Output:

```text
+25
```

**Practice:** Display both positive and negative values.

## 36.29 Display a Large Number

```python
number = 1234567890

print(f"{number:,}")
```

Output:

```text
1,234,567,890
```

**Practice:** Format a large total in a report.

## 36.30 Create a Small Report

```python
name = "Amaan"
score = 92
status = "Pass"

print("=" * 25)
print("RESULT REPORT".center(25))
print("=" * 25)
print(f"Name: {name}")
print(f"Score: {score}")
print(f"Result: {status}")
print("=" * 25)
```

**Practice:** Add a subject name and a percentage formatted to two decimal places.

---

# 37. Common Mistakes

Understanding common mistakes helps you write output statements correctly and avoid confusing results.

## 37.1 Forgetting Quotes Around Text

Incorrect:

```python
# print(Hello)
```

Python interprets `Hello` as a name rather than literal text.

Correct:

```python
print("Hello")
```

Output:

```text
Hello
```

## 37.2 Putting a Variable Name inside Quotes

```python
name = "Amaan"

print(name)
print("name")
```

Output:

```text
Amaan
name
```

Use quotation marks for literal text.

Use a variable name without quotation marks when displaying its value.

## 37.3 Expecting Automatic Arithmetic from Strings

```python
first = "10"
second = "20"

print(first + second)
```

Output:

```text
1020
```

The strings are joined.

If arithmetic is intended, convert the values to suitable numeric types before the calculation.

## 37.4 Forgetting Spaces in Concatenation

```python
print("Hello" + "World")
```

Output:

```text
HelloWorld
```

Add a space explicitly:

```python
print("Hello" + " " + "World")
```

Output:

```text
Hello World
```

## 37.5 Confusing `sep` with `end`

`sep` separates objects in the same print call.

`end` controls the text added after the call's objects.

Both parameters are useful, but they do different jobs.

## 37.6 Forgetting the Default Newline

```python
print("A", end="")
print("B")
```

Output:

```text
AB
```

The first call has no newline ending.

## 37.7 Incorrect F-String Syntax

An f-string uses an `f` prefix and braces around the variable or expression.

Correct:

```python
name = "Amaan"

print(f"Hello, {name}")
```

Output:

```text
Hello, Amaan
```

## 37.8 Forgetting the `f` Prefix

```python
name = "Amaan"

print("Hello, {name}")
```

Output:

```text
Hello, {name}
```

Without the `f` prefix, the braces remain literal text in this string.

## 37.9 Incorrect Braces

F-string replacement fields must use matching braces.

Correct:

```python
score = 92

print(f"Score: {score}")
```

## 37.10 Using a String Instead of a Number

```python
number = 12.5

print(f"{number:.2f}")
```

Output:

```text
12.50
```

The numeric format specifier should be applied to an appropriate numeric value.

## 37.11 Forgetting Decimal Precision

```python
price = 25

print(price)
```

Output:

```text
25
```

For a display requiring two decimal places:

```python
print(f"{price:.2f}")
```

Output:

```text
25.00
```

## 37.12 Assuming Field Width Truncates Text

A field width sets a minimum width rather than a maximum length.

Long text may extend beyond the field.

Use an explicit truncation or text-wrapping strategy when a maximum length is required.

## 37.13 Using Inconsistent Alignment

When displaying a table, inconsistent field widths can make the columns difficult to read.

Use a consistent format string for each column.

## 37.14 Forgetting to Escape Backslashes

A backslash can begin an escape sequence.

For literal backslashes, use an appropriate raw string literal or escaped backslashes.

## 37.15 Misunderstanding `repr()`

The representation returned by `repr()` may include quotes and escape sequences.

These are useful for inspection, but they are not always the best format for user-facing messages.

---

# 38. Output Formatting Best Practices

Readable output is not simply about adding decoration.

Good output communicates information accurately and makes the most important results easy to find.

## 38.1 Use Meaningful Labels

Prefer:

```python
print(f"Total: {total}")
```

Instead of only:

```python
print(total)
```

The label explains what the value represents.

## 38.2 Use Consistent Formatting

If several prices appear in one report, display them with the same number of decimal places.

```python
print(f"Item A: {19.5:.2f}")
print(f"Item B: {20:.2f}")
```

Output:

```text
Item A: 19.50
Item B: 20.00
```

## 38.3 Keep Reports Structured

Group related values together.

Use headings when useful.

Avoid inserting a decorative line after every individual value if it makes the report harder to read.

## 38.4 Align Numeric Columns

Right alignment is often effective for numeric columns.

```python
print(f"{'Score':<12}{95:>8}")
print(f"{'Percentage':<12}{92.5:>8.2f}")
```

Consistent widths make numerical differences easier to compare.

## 38.5 Separate Calculation and Presentation

Calculate a result first, then format it for display.

```python
total = 100 + 200
formatted_total = f"{total:.2f}"

print(f"Total: {formatted_total}")
```

This makes it clearer which part performs the calculation and which part controls presentation.

## 38.6 Choose Appropriate Precision

Use the level of precision required by the problem.

Examples:

- Money: often two decimal places.
- Average marks: often two decimal places.
- Whole-number counts: usually no decimal places.
- Scientific measurements: precision depends on the application.

These are common conventions, not universal rules.

## 38.7 Avoid Unnecessary Decoration

Borders can make a small report easier to scan.

However, excessive symbols and blank lines can distract from the information.

## 38.8 Do Not Expose Unnecessary Debug Information

During development, it is useful to print variable types and intermediate values.

For user-facing output, show the result and any explanation that the user actually needs.

## 38.9 Remember That Formatting Produces Text

If a formatted number will be used in later calculations, keep the original numeric value.

Use the formatted result for display rather than assuming it remains numeric.

## 38.10 Test Long Values

A report can look aligned with short names and become misaligned when a long name is displayed.

Test realistic input values before finalizing the formatting.

---

# 39. Viva and Interview Questions

## Basic Questions

**Q1. What is output in programming?**

Output is the information produced by a program and made available to a user or another system.

**Q2. Which function is commonly used to display output in Python?**

The built-in `print()` function.

**Q3. What happens when `print()` is called without arguments?**

It writes the default ending, which is a newline, producing a blank line.

**Q4. Can `print()` display different data types?**

Yes. It can display strings, numbers, Booleans, lists, dictionaries, and many other Python objects.

**Q5. Does `print()` return the displayed text?**

No. A normal call to `print()` returns `None`.

## Multiple Values and Parameters

**Q6. What is the default separator used by `print()`?**

A single space.

**Q7. What does the `sep` parameter do?**

It specifies the separator between multiple objects printed in one call.

**Q8. What does the `end` parameter do?**

It specifies the text written after the objects in a print call.

**Q9. What is the default value of `end`?**

The newline string `"\n"`.

**Q10. How can multiple print statements continue on the same line?**

Use a suitable value for `end`, such as `end=" "` or `end=""`.

## Escape Sequences

**Q11. What does `\n` represent?**

A newline character.

**Q12. What does `\t` represent?**

A horizontal tab.

**Q13. How can a literal backslash be printed?**

An ordinary string can use `\\` to represent a literal backslash.

**Q14. How can quotation marks be displayed inside a string?**

Use a suitable outer quote style or escape a matching quotation mark.

**Q15. What is a multiline string?**

A string that contains multiple lines, often created using triple quotes or newline characters.

## Formatting

**Q16. What is an f-string?**

An f-string is a formatted string literal that inserts variables and expressions into text.

**Q17. What is the purpose of `{value:.2f}`?**

It formats a floating-point value for display with two digits after the decimal point.

**Q18. Does an f-string change the original numeric variable?**

No. It creates a formatted string for output.

**Q19. What does `<` mean in a format specifier?**

It requests left alignment within a field.

**Q20. What does `>` mean in a format specifier?**

It requests right alignment within a field.

**Q21. What does `^` mean in a format specifier?**

It requests centered alignment within a field.

**Q22. What does `f"{number:,}"` do?**

It formats a number with grouping separators, using commas for the standard decimal presentation.

**Q23. What does `f"{ratio:.1%}"` do?**

It displays a ratio as a percentage with one digit after the decimal point.

**Q24. What is the difference between an f-string and `str.format()`?**

Both support formatted output. F-strings embed expressions directly in the string literal, while `str.format()` fills replacement fields in a format template.

## Practical Questions

**Q25. How can a student report be displayed neatly?**

Use headings, labels, consistent numeric precision, and aligned columns.

**Q26. How can several list items be printed on separate lines?**

Iterate over the list and print each item.

**Q27. How can list items be printed on one line with a custom separator?**

Unpack the list as arguments and pass the required `sep` value to `print()`.

**Q28. What is the difference between `str()` and `repr()`?**

`str()` aims to provide a human-friendly string representation. `repr()` aims to provide a representation useful for inspection and debugging.

**Q29. What is standard output?**

Standard output, commonly called `stdout`, is the default output stream used by `print()`.

**Q30. What is standard error?**

Standard error, commonly called `stderr`, is a stream often used for errors and diagnostic messages.

**Q31. What does `file` do in `print()`?**

It specifies a writable file-like object to receive the output.

**Q32. What does `flush=True` request?**

It requests that the output stream be flushed after printing.

**Q33. Why should calculation and display formatting be kept separate?**

Separating them makes it easier to reuse calculations and keep presentation logic clear.

**Q34. Why is consistent decimal formatting important?**

It makes numerical values easier to compare and helps reports look consistent.

**Q35. Why can columns become misaligned?**

Values may have different lengths or use inconsistent format widths.

**Q36. What should be done when output contains a literal `\n` rather than a line break?**

Use `\\n` in an ordinary string when the backslash and letter `n` should appear literally.

**Q37. Can the `sep` parameter be an empty string?**

Yes. An empty string means no separator is inserted between the objects.

**Q38. Does the field width in an f-string truncate long text?**

No. It establishes a minimum field width. Long text can exceed it.

**Q39. Why is `repr()` useful when debugging input?**

It helps reveal spaces and escape sequences that may not be obvious in normal output.

**Q40. What is the main goal of good output formatting?**

To present information accurately, clearly, consistently, and in a form that is easy to understand.

---

# 40. Quick Revision Reference

This section summarizes the most frequently used concepts from the topic.

| Feature | Syntax | Purpose |
|---|---|---|
| Basic output | `print("Hello")` | Display text |
| Multiple objects | `print(a, b)` | Display values with the default separator |
| Custom separator | `print(a, b, sep="-")` | Choose the separator between objects |
| Custom ending | `print(a, end=" ")` | Control the text added after a print call |
| Newline | `"\n"` | Start a new line inside a string |
| Tab | `"\t"` | Insert a horizontal tab |
| Literal backslash | `"\\"` | Display a backslash |
| F-string | `f"Hello {name}"` | Insert values into text |
| Two decimal places | `f"{value:.2f}"` | Display two digits after the decimal point |
| Left alignment | `f"{text:<12}"` | Align text to the left |
| Right alignment | `f"{value:>8}"` | Align text or values to the right |
| Center alignment | `f"{text:^20}"` | Center a value in a field |
| Thousands grouping | `f"{number:,}"` | Group digits with commas |
| Percentage | `f"{ratio:.2%}"` | Display a fraction as a percentage |
| Scientific notation | `f"{number:.2e}"` | Display a number in scientific notation |
| String formatting | `"Hello {}".format(name)` | Fill replacement fields |
| Inspect representation | `repr(value)` | Display a debugging-oriented representation |
| Standard error | `print(message, file=sys.stderr)` | Send output to standard error |
| File output | `print(message, file=file)` | Write to a writable file object |
| Flush output | `print(message, flush=True)` | Request that output be flushed |

## Core Rules

1. The `print()` function displays the representations of supplied objects.
2. Multiple objects are separated by one space unless `sep` is changed.
3. Every normal print call ends with a newline unless `end` is changed.
4. Escape sequences can change how strings appear.
5. F-strings can insert expressions and apply formatting rules.
6. The `str.format()` method fills replacement fields.
7. Field width and alignment can make tables easier to read.
8. Numeric format specifiers control how values are displayed.
9. Formatted strings are text and should not be mistaken for numeric values.
10. Output formatting should support clarity rather than merely decoration.

---

# 41. Learning Checklist

Mark each item after you can demonstrate it independently.

## Basic Output

- [ ] I understand the purpose of output in a program.
- [ ] I can use `print()` to display text.
- [ ] I can print integers, floats, Booleans, and variables.
- [ ] I can print multiple objects in one statement.
- [ ] I understand the default separator between objects.
- [ ] I understand why `print()` normally ends with a newline.

## Output Control

- [ ] I can customize separators using `sep`.
- [ ] I can customize endings using `end`.
- [ ] I can print multiple messages on one line.
- [ ] I can create blank lines and multiline output.
- [ ] I can use newline and tab escape sequences.
- [ ] I can display quotation marks and literal backslashes.

## Formatting

- [ ] I can use f-strings to display variables.
- [ ] I can evaluate expressions inside f-strings.
- [ ] I understand the `str.format()` method.
- [ ] I can display numbers with fixed decimal precision.
- [ ] I can format percentages and large numbers.
- [ ] I can align text and numeric columns.
- [ ] I can produce tables and formatted reports.

## Advanced Concepts

- [ ] I understand the distinction between `str()` and `repr()`.
- [ ] I can use output to inspect values while debugging.
- [ ] I understand the purpose of standard output and standard error.
- [ ] I understand what the `file` and `flush` parameters do.
- [ ] I can explain why formatting does not change the original numeric value.

## Practice

- [ ] I have run the twelve output examples.
- [ ] I have attempted all twelve solved problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I have completed the extended output practice.
- [ ] I can answer the viva questions in my own words.
- [ ] I can write a formatted report without copying an existing solution.

---

# 42. Final Summary

Output is how a Python program presents information to users and other systems.

The `print()` function provides the foundation for displaying results, while its parameters and Python's string-formatting features allow output to be organized in many different ways.

The key concepts in this topic are:

- Basic printing with `print()`.
- Displaying multiple values.
- Customizing separators using `sep`.
- Controlling line endings using `end`.
- Using newline, tab, quotation, and backslash escape sequences.
- Formatting output with f-strings and `str.format()`.
- Displaying numeric values at a chosen precision.
- Aligning columns and creating readable tables.
- Creating profiles, receipts, calculation reports, and summaries.
- Using output for debugging.
- Understanding standard output and standard error.

A strong Python program should not only calculate the correct result; it should also communicate that result clearly.

**Practise writing output statements, test different formatting options, and create your own readable reports before moving to the next topic.**