## 📚 Topics Covered

### 1. Hello World

Learn the basics of writing and executing your first Python program.

Topics:

- What is Python?
- Python programming language
- First Python program
- `print()` function
- Strings
- Integers
- Floats
- Boolean values
- Comments
- Basic output
- How Python executes a program

📁 Folder:

`01_hello_world/`

---

### 2. Print Statements

Learn how Python displays information on the screen.

Topics:

- Basic `print()`
- Printing multiple values
- `sep` parameter
- `end` parameter
- Printing variables
- Printing expressions
- Combining text and values

Files:

- `02_print_statements.py`
- `02_print_statements.md`

---

### 3. Escape Sequences

Learn how to format text output using escape characters.

Topics:

- New line `\n`
- Tab `\t`
- Backslash `\\`
- Double quote `\"`
- Single quote `\'`
- Carriage return `\r`

Files:

- `03_escape_sequences.py`
- `03_escape_sequences.md`

---

## 🎯 Learning Objectives

After completing this section, you should be able to:

- Understand what Python is
- Write your first Python program
- Use the `print()` function
- Print text and numbers
- Understand basic Python values
- Use comments
- Format output
- Use escape sequences
- Understand basic Python syntax
- Run a Python program

---

## 💼 Placement Preparation

Important interview questions from this section:

1. What is Python?
2. Why is Python popular?
3. Who created Python?
4. What is the use of the `print()` function?
5. What is a string?
6. What is the difference between `"100"` and `100`?
7. What are Boolean values in Python?
8. What are comments?
9. What is an escape sequence?
10. What is the difference between `\n` and `\t`?
11. What is the use of `sep` in `print()`?
12. What is the use of `end` in `print()`?

---

## 🧪 Practice

Before moving to the next topic, practice:

- Print your name
- Print your age
- Print your college name
- Print your career goal
- Print multiple values
- Print a formatted message
- Use `\n`
- Use `\t`
- Use `sep`
- Use `end`

---

## ✅ Progress

- [ ] Hello World
- [ ] Print Statements
- [ ] Escape Sequences
- [ ] Practice Questions
- [ ] Interview Questions

---

## 🚀 Next Topic

After completing Introduction, move to:

`02-Flowcharts-Algorithms`
```

---

# 2. `01_hello_world/01_hello_world.py`

```python
# ============================================================
# File Name: 01_hello_world.py
# Topic: Hello World - First Python Program
# Week: 1 - Programming Fundamentals
# ============================================================


# ------------------------------------------------------------
# Example 1: Print Hello World
# ------------------------------------------------------------

# print() is a built-in Python function.
# It is used to display output on the screen.

print("Hello World")


# ------------------------------------------------------------
# Example 2: Print Text
# ------------------------------------------------------------

# Text is written inside quotes.

print("Hello")
print("Welcome to Python")
print("I am learning Python")


# ------------------------------------------------------------
# Example 3: Print Personal Information
# ------------------------------------------------------------

print("My name is Amaan Syed")
print("I am learning Python for placements")


# ------------------------------------------------------------
# Example 4: Print an Integer
# ------------------------------------------------------------

# An integer is a whole number.
# Numbers do not require quotes.

print(22)


# ------------------------------------------------------------
# Example 5: Print a Float
# ------------------------------------------------------------

# A float is a number containing a decimal point.

print(22.5)


# ------------------------------------------------------------
# Example 6: Print Boolean Values
# ------------------------------------------------------------

# Python has two Boolean values:
# True and False

print(True)
print(False)


# ------------------------------------------------------------
# Example 7: String vs Integer
# ------------------------------------------------------------

# "100" is a string because it is inside quotes.

print("100")

# 100 is an integer because it is not inside quotes.

print(100)


# ------------------------------------------------------------
# Example 8: Print Multiple Lines
# ------------------------------------------------------------

print("========================")
print("     PYTHON LEARNING")
print("========================")
print("Name: Amaan Syed")
print("Age: 22")
print("Goal: Software Developer")
print("========================")


# ------------------------------------------------------------
# Example 9: Comments
# ------------------------------------------------------------

# This is a single-line comment.

print("Python is easy to learn")


# ------------------------------------------------------------
# Learning Message
# ------------------------------------------------------------

print("I am learning Python")
print("I am preparing for placements")
print("I will learn Python and DSA")
```

---

# 3. `01_hello_world/README.md`

```markdown
# Hello World - First Python Program

## 1. What is Python?

Python is a high-level, general-purpose programming language.

Python is widely used for:

- Web Development
- Data Science
- Artificial Intelligence
- Machine Learning
- Automation
- Scripting
- Backend Development
- Data Analysis
- Competitive Programming
- DSA and Placement Preparation

---

# 2. First Python Program

The traditional first program in Python is:

```python
print("Hello World")
```

### Explanation

`print()` is a built-in Python function used to display output on the screen.

`"Hello World"` is a string.

The output will be:

```text
Hello World
```

---

# 3. print() Function

The `print()` function displays information on the screen.

Example:

```python
print("Hello")
print("Welcome to Python")
```

Output:

```text
Hello
Welcome to Python
```

---

# 4. Printing Text

Text is written inside quotes.

Example:

```python
print("Python")
print("Java")
print("Programming")
```

Output:

```text
Python
Java
Programming
```

Python supports:

```python
"Hello"
'Hello'
```

Both represent strings.

---

# 5. Printing Numbers

Numbers do not require quotes.

## Integer

An integer is a whole number.

```python
print(10)
print(100)
print(22)
```

## Float

A float is a number containing a decimal value.

```python
print(10.5)
print(22.5)
print(3.14)
```

---

# 6. Boolean Values

Python has two Boolean values:

```python
True
False
```

Example:

```python
print(True)
print(False)
```

Output:

```text
True
False
```

Boolean values are commonly used in conditions.

---

# 7. String vs Integer

Consider:

```python
print("100")
print(100)
```

`"100"` is a string because it is inside quotes.

`100` is an integer because it is not inside quotes.

### Important

```text
"100" → String
100   → Integer
```

This difference becomes very important when working with input and calculations.

---

# 8. Comments in Python

Comments are notes written inside the program.

Python ignores comments while executing the program.

Single-line comment:

```python
# This is a comment
```

Example:

```python
# Print the user's name
print("Amaan")
```

Comments help programmers understand code.

---

# 9. How Python Executes a Program

When we run:

```python
print("Hello World")
```

Python reads and executes the statement.

The output is displayed on the screen:

```text
Hello World
```

Python generally executes code from top to bottom.

Example:

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

---

# 10. Important Python Terms

| Term | Meaning |
|---|---|
| Python | High-level programming language |
| `print()` | Displays output |
| String | Text data |
| Integer | Whole number |
| Float | Decimal number |
| Boolean | `True` or `False` |
| Comment | Non-executable explanation |
| Syntax | Rules for writing code |
| Output | Result displayed by program |

---

# 11. Common Mistakes

## Mistake 1: Missing Quotes

Incorrect:

```python
print(Hello World)
```

Correct:

```python
print("Hello World")
```

---

## Mistake 2: Wrong Function Name

Incorrect:

```python
Print("Hello")
```

Correct:

```python
print("Hello")
```

Python is case-sensitive.

---

## Mistake 3: Missing Parentheses

Incorrect:

```python
print"Hello"
```

Correct:

```python
print("Hello")
```

---

# 12. Interview Questions

### Q1. What is Python?

Python is a high-level, general-purpose programming language known for its simple syntax and readability.

### Q2. What is the use of print()?

`print()` is used to display output on the screen.

### Q3. What is a string?

A string is a sequence of characters enclosed inside quotes.

Example:

```python
"Hello"
```

### Q4. What is an integer?

An integer is a whole number without a decimal point.

Example:

```python
100
```

### Q5. What are Boolean values?

Python has two Boolean values:

```python
True
False
```

### Q6. What is the difference between `"100"` and `100`?

`"100"` is a string while `100` is an integer.

### Q7. Are Python keywords case-sensitive?

Yes. Python is case-sensitive.

For example:

```python
print()
```

and

```python
Print()
```

are different.

---

# 13. Practice Questions

Write Python programs to:

1. Print your name.
2. Print your age.
3. Print your college name.
4. Print your city.
5. Print your career goal.
6. Print an integer.
7. Print a float.
8. Print `True`.
9. Print `False`.
10. Print your name and age.
11. Print a simple introduction.
12. Print a Python learning message.

---

# 14. Learning Outcome

After completing this topic, you should understand:

- What Python is
- How to write a Python program
- How `print()` works
- Strings
- Integers
- Floats
- Boolean values
- Comments
- Basic Python syntax
- Basic program execution

---

# 15. Progress

- First Python Program
- `print()` Function
- Printing Strings
- Printing Numbers
- Printing Boolean Values
- Basic Python Syntax
```