# Print Statements in Python

> **Week:** 01 - Programming Fundamentals  
> **Topic:** Print Statements  
> **Level:** Beginner  
> **Purpose:** Learn how to display text, numbers, multiple values, and formatted output using Python's `print()` function.

---

## Table of Contents

1. Introduction
2. What Is the `print()` Function?
3. Syntax of `print()`
4. Printing Text
5. Printing Numbers
6. Printing Multiple Values
7. The `sep` Parameter
8. The `end` Parameter
9. Printing a Blank Line
10. Printing Variables
11. Printing Different Data Types
12. Printing Mathematical Expressions
13. Formatted Output Using f-Strings
14. Practical Examples
15. Common Beginner Mistakes
16. Important Terms
17. Interview Questions
18. Practice Questions
19. Learning Checklist
20. What's Next?

---

## 1. Introduction

In Python, the `print()` function is used to display information on the screen.

It is one of the first functions every Python programmer learns because output helps us understand what a program is doing.

For example:

```python
print("Hello, Python!")
```

### Output

```text
Hello, Python!
```

The `print()` function can display:

- Text and strings
- Integers and decimal numbers
- Boolean values
- Multiple values
- Results of mathematical expressions
- Values stored in variables
- Formatted messages

Understanding `print()` properly will help you debug programs, solve coding questions, and display results clearly.

---

## 2. What Is the `print()` Function?

`print()` is a built-in Python function that displays the values supplied to it.

A built-in function is a function provided by Python, so we can use it without defining it ourselves.

### Example

```python
print("Welcome to Python")
print(100)
print(True)
```

### Output

```text
Welcome to Python
100
True
```

### Explanation

In the first statement, Python displays a string.

In the second statement, Python displays an integer.

In the third statement, Python displays a Boolean value.

The same function can display different kinds of values.

---

## 3. Syntax of `print()`

The general syntax is:

```python
print(*objects, sep=' ', end='\n')
```

For beginners, the most important parts are:

| Part | Meaning |
|---|---|
| `print` | Name of the built-in function |
| `()` | Parentheses used to call the function |
| `objects` | Values we want to display |
| `sep` | Separator between multiple values |
| `end` | Text printed after the values |

The `sep` and `end` parameters have default values. You only need to specify them when you want different behavior.

### Simple example

```python
print("Hello World")
```

### Output

```text
Hello World
```

---

## 4. Printing Text

Text is represented by the string data type in Python.

A string is written using matching single or double quotation marks.

### Example 1: Double quotes

```python
print("Hello World")
print("Learning Python")
```

### Output

```text
Hello World
Learning Python
```

### Example 2: Single quotes

```python
print('Hello World')
print('Learning Python')
```

### Output

```text
Hello World
Learning Python
```

Both quotation styles are valid.

### Important point

Python treats each `print()` call as a separate output operation. By default, each call ends with a newline, so the next output appears on the next line.

---

## 5. Printing Numbers

The `print()` function can display numbers directly.

### 5.1 Printing integers

An integer is a whole number without a decimal point.

```python
print(10)
print(100)
print(500)
print(-25)
```

### Output

```text
10
100
500
-25
```

### 5.2 Printing floating-point numbers

Floating-point numbers represent decimal values.

```python
print(3.14)
print(10.5)
print(-2.75)
```

### Output

```text
3.14
10.5
-2.75
```

### String versus number

Compare:

```python
print("100")
print(100)
```

Output:

```text
100
100
```

Although the displayed output looks identical, `"100"` is a string and `100` is an integer.

Quotation marks change how Python interprets the value.

---

## 6. Printing Multiple Values

You can pass multiple values to `print()` by separating them with commas.

### Example

```python
print("Name:", "Amaan")
print("Age:", 21)
print("Language:", "Python")
```

### Output

```text
Name: Amaan
Age: 21
Language: Python
```

By default, Python puts a single space between the values passed to one `print()` call.

### Another example

```python
print("Python", "Java", "C++")
```

### Output

```text
Python Java C++
```

### Why use commas?

Commas let you display different values together without manually combining them into one string.

For example:

```python
age = 21
print("Age:", age)
```

Output:

```text
Age: 21
```

The variable `age` is passed as a value to `print()`.

---

## 7. The `sep` Parameter

The `sep` parameter means **separator**.

It controls what appears between multiple values passed to the same `print()` call.

The default separator is one space.

### Example 1: Default separator

```python
print("Python", "DSA", "Placement")
```

Output:

```text
Python DSA Placement
```

### Example 2: Hyphen separator

```python
print("2026", "10", "16", sep="-")
```

Output:

```text
2026-10-16
```

### Example 3: Comma separator

```python
print("10", "20", "30", sep=",")
```

Output:

```text
10,20,30
```

### Example 4: Custom separator

```python
print("Python", "DSA", "Placement", sep=" | ")
```

Output:

```text
Python | DSA | Placement
```

### How does `sep` work?

Consider:

```python
print("A", "B", "C", sep="*")
```

Python places `*` between the values.

Output:

```text
A*B*C
```

**Remember:** `sep` separates values within a single `print()` call. It does not add a separator between separate calls to `print()`.

---

## 8. The `end` Parameter

The `end` parameter controls what Python prints after the values in a `print()` call.

By default, `end` is a newline. This is why separate print statements normally display their results on separate lines.

### Example 1: Default behavior

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

### Example 2: Using a space as `end`

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

The first statement ends with a space instead of a newline. The second statement continues on the same line.

### Example 3: Using a custom ending

```python
print("Loading", end="...")
print("Done")
```

Output:

```text
Loading...Done
```

### Example 4: Ending with a hyphen

```python
print("Python", end="-")
print("Programming")
```

Output:

```text
Python-Programming
```

### Difference between `sep` and `end`

| Parameter | Purpose | Example |
|---|---|---|
| `sep` | Separates multiple values in one call | `print("A", "B", sep="-")` |
| `end` | Controls what is printed at the end of a call | `print("A", end="-")` |

**Easy way to remember:**

- `sep` works between values.
- `end` works after the output of a call.

---

## 9. Printing a Blank Line

Calling `print()` without any values displays a blank line.

### Example

```python
print("First Section")
print()
print("Second Section")
```

### Output

```text
First Section

Second Section
```

This is useful for separating headings, sections, and results.

---

## 10. Printing Variables

A variable is a name that refers to a value.

Variables are useful because they allow a program to store and reuse information.

### Example

```python
name = "Amaan"
age = 21

print(name)
print(age)
```

### Output

```text
Amaan
21
```

You can also combine labels with variable values:

```python
name = "Amaan"
age = 21

print("Name:", name)
print("Age:", age)
```

### Output

```text
Name: Amaan
Age: 21
```

Variables will be studied in more detail in a later topic.

---

## 11. Printing Different Data Types

Python supports several data types, and `print()` can display their values.

```python
print("Python")
print(25)
print(8.5)
print(True)
```

### Output

```text
Python
25
8.5
True
```

| Value | Data type | Description |
|---|---|---|
| `"Python"` | `str` | String or text |
| `25` | `int` | Integer |
| `8.5` | `float` | Floating-point number |
| `True` | `bool` | Boolean value |

Python displays the value, not its type name. You can inspect a value's type using the `type()` function.

Example:

```python
print(type("Python"))
print(type(25))
```

Output:

```text
<class 'str'>
<class 'int'>
```

---

## 12. Printing Mathematical Expressions

The `print()` function can display the result of an expression.

An expression is a combination of values and operators that Python evaluates.

### Example

```python
print(10 + 5)
print(20 - 4)
print(6 * 7)
print(15 / 3)
```

### Output

```text
15
16
42
5.0
```

Python calculates each expression before displaying its result.

### More examples

```python
print(10 + 20 + 30)
print(5 * 5)
print(100 - 25)
```

Output:

```text
60
25
75
```

This is useful for displaying the answers to arithmetic problems.

---

## 13. Formatted Output Using f-Strings

An f-string is a way to insert values into a string.

An f-string starts with the letter `f` immediately before the opening quotation mark. Expressions or variable names can be placed inside curly braces.

### Example

```python
name = "Amaan"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

### Output

```text
My name is Amaan and I am 21 years old.
```

### Explanation

- `f` marks the string as an f-string.
- `{name}` is replaced with the value of `name`.
- `{age}` is replaced with the value of `age`.

### Another example

```python
a = 10
b = 20

print(f"The sum of {a} and {b} is {a + b}.")
```

Output:

```text
The sum of 10 and 20 is 30.
```

F-strings are especially useful when displaying formatted results.

---

## 14. Practical Examples

### Example 1: Student information

```python
print("Student Information")
print("Name:", "Amaan")
print("Course:", "B.Tech Computer Science")
print("Language:", "Python")
print("Goal:", "Software Developer")
```

Output:

```text
Student Information
Name: Amaan
Course: B.Tech Computer Science
Language: Python
Goal: Software Developer
```

### Example 2: Learning profile

```python
name = "Amaan"

print("==============================")
print("       LEARNING PROFILE")
print("==============================")
print("Name:", name)
print("Language:", "Python")
print("Current Topic:", "Print Statements")
print("Goal:", "Software Developer")
print("==============================")
```

Output:

```text
==============================
       LEARNING PROFILE
==============================
Name: Amaan
Language: Python
Current Topic: Print Statements
Goal: Software Developer
==============================
```

### Example 3: Displaying a calculation

```python
first_number = 125
second_number = 375

print("First number:", first_number)
print("Second number:", second_number)
print("Sum:", first_number + second_number)
```

Output:

```text
First number: 125
Second number: 375
Sum: 500
```

---

## 15. Common Beginner Mistakes

### Mistake 1: Incorrect capitalization

Incorrect:

```python
Print("Hello")
```

Correct:

```python
print("Hello")
```

Python is case-sensitive. The function name is `print`, not `Print`.

### Mistake 2: Missing quotation marks

Incorrect:

```python
print(Hello World)
```

Correct:

```python
print("Hello World")
```

Text should be written as a string using matching quotation marks.

### Mistake 3: Missing closing parenthesis

Incorrect:

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

### Mistake 4: Confusing `sep` and `end`

To separate values in one call, use `sep`:

```python
print("A", "B", sep="-")
```

Output:

```text
A-B
```

To control what appears after a call, use `end`:

```python
print("A", end="-")
print("B")
```

Output:

```text
A-B
```

The outputs may look similar, but the parameters control different parts of the output.

### Mistake 5: Expecting separate calls to share a custom separator

Incorrect expectation:

```python
print("A")
print("B", sep="-")
```

Output:

```text
A
B
```

The `sep` parameter only separates values passed to the same call. It does not connect separate calls.

---

## 16. Important Terms

| Term | Meaning |
|---|---|
| Function | A reusable operation that can be called |
| `print()` | Built-in function that displays output |
| Argument | A value supplied to a function |
| String | Text represented as a sequence of characters |
| Integer | Whole number without a decimal point |
| Float | Floating-point number |
| Boolean | Value that is either `True` or `False` |
| `sep` | Parameter controlling the separator between values |
| `end` | Parameter controlling what follows the output |
| Variable | A name referring to a value |
| Expression | Code that Python evaluates to produce a value |
| f-string | String format that supports inserting values using `{}` |

---

## 17. Interview Questions

### Q1. What is the purpose of `print()` in Python?

`print()` is a built-in function used to display values and messages.

### Q2. What is the default separator in `print()`?

The default separator is a single space.

```python
print("A", "B")
```

Output:

```text
A B
```

### Q3. What is the purpose of the `sep` parameter?

It controls the separator placed between multiple values passed to the same `print()` call.

### Q4. What is the purpose of the `end` parameter?

It controls what is printed at the end of a `print()` call. By default, it is a newline.

### Q5. How can two outputs be displayed on the same line?

You can change the `end` parameter.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

### Q6. Can `print()` display numbers?

Yes. For example:

```python
print(100)
print(3.14)
```

### Q7. Can `print()` display the result of a calculation?

Yes.

```python
print(10 + 20)
```

Output:

```text
30
```

### Q8. What is an f-string?

An f-string is a string format that allows values or expressions to be inserted inside curly braces.

```python
name = "Amaan"
print(f"Hello, {name}")
```

Output:

```text
Hello, Amaan
```

---

## 18. Practice Questions

Try solving these questions yourself before looking back at the examples.

### Beginner Level

**Question 1:** Print your name, college, and course using separate statements.

**Question 2:** Print the following numbers: `10`, `25`, `100`, and `3.14`.

**Question 3:** Print three words in one line using a single `print()` call.

**Question 4:** Print `Python`, `DSA`, and `Placement` separated by hyphens.

**Question 5:** Print two words on the same line using the `end` parameter.

### Intermediate Level

**Question 6:** Display your name, age, and career goal using multiple values in `print()`.

**Question 7:** Use `sep` to print `01`, `02`, and `03` separated by a colon.

**Question 8:** Display the result of `125 + 375`.

**Question 9:** Create two variables and display their sum using `print()`.

**Question 10:** Use an f-string to display a name and age.

### Challenge

Create a program that displays this output:

```text
==============================
       LEARNING PROFILE
==============================
Name: Amaan
Language: Python
Topic: Print Statements
Goal: Software Developer
==============================
```

Try to write the program without copying the practical example.

---

## 19. Learning Checklist

- [ ] Understand the purpose of `print()`.
- [ ] Print strings and numbers.
- [ ] Print multiple values in one call.
- [ ] Understand the default separator.
- [ ] Use the `sep` parameter.
- [ ] Use the `end` parameter.
- [ ] Print blank lines.
- [ ] Display variables.
- [ ] Display the result of expressions.
- [ ] Use f-strings for formatted output.
- [ ] Identify common syntax mistakes.
- [ ] Solve the practice questions.

---

## 20. What's Next?

After completing Print Statements, continue with:

**03 - Escape Sequences**

In the next topic, learn how special characters can be represented inside strings, including newline and tab characters.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `02_print_statements.py` | Python examples and practice prompts |
| `README.MD` | Detailed notes, explanations, outputs, and interview questions |

---

## Conclusion

The `print()` function is a fundamental part of Python programming.

It allows us to display values, inspect calculations, and communicate program results clearly.

Remember these three important patterns:

```python
# Display a value
print("Hello World")

# Separate multiple values
print("Python", "DSA", sep="-")

# Continue output on the same line
print("Hello", end=" ")
print("World")
```

Mastering these basics will make it easier to understand variables, input/output operations, and more advanced Python programs.
