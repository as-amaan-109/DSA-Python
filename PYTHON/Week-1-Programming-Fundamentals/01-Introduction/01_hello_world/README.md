# Python - Hello World

> **Topic:** Python Programming Fundamentals  
> **Level:** Beginner  
> **Goal:** Understand your first Python program, `print()`, basic output, comments, and Python syntax.


## Table of Contents

- [1. Introduction](#1-introduction)
- [2. What is Python?](#2-what-is-python)
- [3. Why Learn Python?](#3-why-learn-python)
- [4. Your First Python Program](#4-your-first-python-program)
- [5. Understanding `print()`](#5-understanding-print)
- [6. What is a Function?](#6-what-is-a-function)
- [7. Printing Text](#7-printing-text)
- [8. What is a String?](#8-what-is-a-string)
- [9. Printing Numbers](#9-printing-numbers)
- [10. String vs Integer](#10-string-vs-integer)
- [11. Printing Boolean Values](#11-printing-boolean-values)
- [12. Printing Multiple Values](#12-printing-multiple-values)
- [13. Printing Personal Information](#13-printing-personal-information)
- [14. How Python Executes the Program](#14-how-python-executes-the-program)
- [15. Comments in Python](#15-comments-in-python)
- [16. Why Use Comments?](#16-why-use-comments)
- [17. Python is Case-Sensitive](#17-python-is-case-sensitive)
- [18. Basic Python Syntax](#18-basic-python-syntax)
- [19. Parentheses `()`](#19-parentheses)
- [20. Quotation Marks](#20-quotation-marks)
- [21. Single Quotes vs Double Quotes](#21-single-quotes-vs-double-quotes)
- [22. Multiple `print()` Statements](#22-multiple-print-statements)
- [23. Basic Data Types Used in This Topic](#23-basic-data-types-used-in-this-topic)
- [24. Checking Data Type with `type()`](#24-checking-data-type-with-type)
- [25. Example: Complete Beginner Program](#25-example-complete-beginner-program)
- [26. Common Beginner Mistakes](#26-common-beginner-mistakes)
- [27. Real-World Example](#27-real-world-example)
- [28. Hello World Program Breakdown](#28-hello-world-program-breakdown)
- [29. Important Terms](#29-important-terms)
- [30. Interview Questions](#30-interview-questions)
- [31. Practice Questions](#31-practice-questions)
- [32. Mini Practice Program](#32-mini-practice-program)
- [33. Key Takeaways](#33-key-takeaways)
- [34. Learning Checklist](#34-learning-checklist)
- [35. What's Next?](#35-whats-next)
- [36. Folder Structure](#36-folder-structure)

---

## 1. Introduction

When learning any programming language, the first step is to understand how to write and execute a basic program.

In Python, one of the simplest programs is:

```python
print("Hello World")
```

Output:

```text
Hello World
```

This simple program introduces us to one of the most important concepts in programming:

> **Taking an instruction from the programmer and producing an output.**

Before moving toward advanced topics like variables, loops, functions, OOP, and DSA, it is important to understand these basic Python concepts properly.

---

## 2. What is Python?

Python is a high-level, interpreted, general-purpose programming language.

It was created by **Guido van Rossum** and was first released in **1991**.

Python is designed with a simple and readable syntax, which makes it beginner-friendly.

### Python is used in:

- Web Development
- Backend Development
- Data Science
- Artificial Intelligence
- Machine Learning
- Automation
- Scripting
- Cybersecurity
- Software Development
- Data Analysis
- Competitive Programming
- DSA and Problem Solving

---

## 3. Why Learn Python?

Python is one of the most popular programming languages because its syntax is relatively simple and readable.

For example, printing something in Python requires only:

```python
print("Hello World")
```

Compared with many programming languages, Python requires less boilerplate code for simple tasks.

### Important advantages of Python

####### 1. Simple Syntax

Python code is generally easy to read and understand.

####### 2. Beginner Friendly

Python is commonly recommended for beginners because the syntax is relatively straightforward.

####### 3. Large Ecosystem

Python has a large collection of libraries and frameworks.

####### 4. Multiple Applications

Python can be used in many different areas such as:

```text
Web Development
       ↓
Data Science
       ↓
Artificial Intelligence
       ↓
Machine Learning
       ↓
Automation
       ↓
Software Development
```

---

## 4. Your First Python Program

The traditional first program is:

```python
print("Hello World")
```

Output:

```text
Hello World
```

Let's understand this statement carefully.

---

## 5. Understanding `print()`

`print()` is a built-in Python function used to display information on the screen.

####### Syntax

```python
print(value)
```

Here:

- `print` → function name
- `()` → parentheses used to call the function
- `value` → information that we want to display

Example:

```python
print("Hello")
```

Output:

```text
Hello
```

---

## 6. What is a Function?

A function is a reusable block of code designed to perform a particular task.

Python provides many built-in functions.

Examples:

```python
print()
len()
type()
input()
```

For this topic, we are mainly focusing on:

```python
print()
```

The `print()` function is used to display output.

---

## 7. Printing Text

Text in Python is represented using a string.

Strings can be written using:

- Double quotes `" "`
- Single quotes `' '`

Example:

```python
print("Hello World")
```

We can also write:

```python
print('Hello World')
```

Both are valid.

Output:

```text
Hello World
```

---

## 8. What is a String?

A string is a sequence of characters.

Examples:

```python
"Hello"
"Python"
"Amaan"
"Hello World"
```

A string is usually written inside quotation marks.

Example:

```python
name = "Amaan"
```

Here:

```text
name       → variable
"Amaan"    → string value
```

For now, remember:

> **Text written inside quotation marks is treated as a string.**

---

## 9. Printing Numbers

Python can also print numbers.

### Integer

An integer is a whole number without a decimal point.

Example:

```python
print(10)
print(100)
print(500)
print(1000)
```

Output:

```text
10
100
500
1000
```

### Floating-Point Number

A number containing a decimal point is generally represented as a floating-point value.

Example:

```python
print(10.5)
print(99.99)
print(3.14)
```

Output:

```text
10.5
99.99
3.14
```

---

## 10. String vs Integer

This is an important beginner concept.

Consider:

```python
print("100")
```

and:

```python
print(100)
```

They may look similar when displayed:

```text
100
```

But Python treats them differently.

### `"100"`

This is a string.

```python
"100"
```

### `100`

This is an integer.

```python
100
```

The quotation marks make the difference.

####### Example

```python
print("100")
print(100)
```

Output:

```text
100
100
```

Although the output looks the same, their data types are different.

---

## 11. Printing Boolean Values

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

Boolean values are commonly used when working with conditions and decision-making.

Remember:

```python
True
False
```

are Boolean values.

Whereas:

```python
"True"
"False"
```

are strings.

---

## 12. Printing Multiple Values

The `print()` function can display multiple values.

We can separate values using commas.

Example:

```python
print("Name:", "Amaan")
print("Age:", 21)
print("Student:", True)
```

Output:

```text
Name: Amaan
Age: 21
Student: True
```

Another example:

```python
print("Python", "Java", "C++")
```

Output:

```text
Python Java C++
```

---

## 13. Printing Personal Information

We can use multiple `print()` statements to display information.

Example:

```python
print("Name: Amaan")
print("Course: B.Tech Computer Science")
print("Learning: Python")
print("Goal: Software Developer")
```

Output:

```text
Name: Amaan
Course: B.Tech Computer Science
Learning: Python
Goal: Software Developer
```

This is a simple example of how multiple instructions are executed one after another.

---

## 14. How Python Executes the Program

Consider:

```python
print("Hello")
print("Python")
print("DSA")
```

Python executes the statements sequentially.

Conceptually:

```text
Start
  ↓
print("Hello")
  ↓
print("Python")
  ↓
print("DSA")
  ↓
End
```

Output:

```text
Hello
Python
DSA
```

This introduces the idea of program execution.

Later, we will learn how conditions and loops can change the normal flow of execution.

---

## 15. Comments in Python

Comments are used to write explanations inside the source code.

Python ignores comments during normal execution.

A single-line comment starts with:

```python
#
```

Example:

```python
# This is my first Python program

print("Hello World")
```

Output:

```text
Hello World
```

The comment is not displayed as output.

---

## 16. Why Use Comments?

Comments help programmers:

- Explain code
- Document logic
- Remember important information
- Make code easier to understand
- Help other developers understand the program

Example:

```python
# Display welcome message
print("Welcome to Python")
```

The comment explains what the next statement does.

---

## 17. Python is Case-Sensitive

Python is case-sensitive.

This means uppercase and lowercase letters are treated differently.

Correct:

```python
print("Hello World")
```

Incorrect:

```python
Print("Hello World")
```

The function name is:

```python
print()
```

not:

```python
Print()
```

Similarly:

```python
True
```

and:

```python
true
```

are not the same in Python.

---

## 18. Basic Python Syntax

Syntax means the rules used to write valid code.

For example:

```python
print("Hello World")
```

is valid Python syntax.

But:

```python
print("Hello World"
```

is incomplete because the closing parenthesis is missing.

Correct:

```python
print("Hello World")
```

---

## 19. Parentheses `()`

The `print()` function uses parentheses.

Example:

```python
print("Hello")
```

Here:

```text
print → function
()    → function call
"Hello" → argument/value
```

The parentheses are important.

Incorrect:

```python
print"Hello"
```

Correct:

```python
print("Hello")
```

---

## 20. Quotation Marks

Strings require quotation marks.

Correct:

```python
print("Hello World")
```

Also correct:

```python
print('Hello World')
```

Incorrect:

```python
print(Hello World)
```

The last example is invalid because Python does not recognize `Hello World` as a string.

---

## 21. Single Quotes vs Double Quotes

Both are commonly used for strings.

```python
print("Hello")
```

and:

```python
print('Hello')
```

Both produce:

```text
Hello
```

The important thing is to use matching quotation marks.

Correct:

```python
"Hello"
```

Correct:

```python
'Hello'
```

Incorrect:

```python
"Hello'
```

---

## 22. Multiple `print()` Statements

We can use multiple print statements in one program.

Example:

```python
print("Hello World")
print("Welcome to Python")
print("I am learning programming")
print("I am learning DSA")
```

Output:

```text
Hello World
Welcome to Python
I am learning programming
I am learning DSA
```

Each statement produces output on a separate line by default.

---

## 23. Basic Data Types Used in This Topic

At this stage, we have already seen some basic Python data types.

| Data Type | Example | Description |
|---|---|---|
| `str` | `"Hello"` | Text |
| `int` | `100` | Whole number |
| `float` | `10.5` | Decimal number |
| `bool` | `True` | Boolean value |

Example:

```python
print("Python")
print(100)
print(10.5)
print(True)
```

---

## 24. Checking Data Type with `type()`

Python provides the `type()` function to check the type of a value.

Example:

```python
print(type("Hello"))
print(type(100))
print(type(10.5))
print(type(True))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

This is useful when learning how Python handles different types of data.

---

## 25. Example: Complete Beginner Program

```python
# My first Python program

print("Hello World")
print("Welcome to Python")
print("I am learning Python")
print("I am learning DSA")
print("My goal is to become a Software Developer")
```

Output:

```text
Hello World
Welcome to Python
I am learning Python
I am learning DSA
My goal is to become a Software Developer
```

---

## 26. Common Beginner Mistakes

### Mistake 1: Incorrect Function Name

Incorrect:

```python
Print("Hello")
```

Correct:

```python
print("Hello")
```

---

### Mistake 2: Missing Parenthesis

Incorrect:

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

---

### Mistake 3: Missing Quotation Marks

Incorrect:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

---

### Mistake 4: Mismatched Quotes

Incorrect:

```python
print("Hello')
```

Correct:

```python
print("Hello")
```

---

### Mistake 5: Confusing String and Number

```python
print("100")
```

Here `100` is a string.

```python
print(100)
```

Here `100` is an integer.

---

## 27. Real-World Example

Suppose we want to display information about a student.

```python
print("Student Information")
print("Name: Amaan")
print("Course: B.Tech CSE")
print("Language: Python")
print("Topic: DSA")
```

Output:

```text
Student Information
Name: Amaan
Course: B.Tech CSE
Language: Python
Topic: DSA
```

This is a very basic example, but later we will replace fixed values with variables.

For example:

```python
name = "Amaan"
```

and then use:

```python
print(name)
```

Variables will be covered in a later topic.

---

## 28. Hello World Program Breakdown

Let's break down:

```python
print("Hello World")
```

 `print`

A built-in Python function used to display output.

 `(`

Opening parenthesis for the function call.

 `"Hello World"`

A string value.

 `)`

Closing parenthesis.

So the complete statement means:

> Call the `print()` function and display the string `"Hello World"`.

---

## 29. Important Terms

| Term | Meaning |
|---|---|
| Python | Programming language |
| Program | Set of instructions |
| Function | Reusable block of code |
| `print()` | Function used to display output |
| String | Sequence of characters |
| Integer | Whole number |
| Float | Decimal number |
| Boolean | `True` or `False` |
| Comment | Non-executed explanation in source code |
| Syntax | Rules for writing valid code |
| Output | Result produced by a program |

---

## 30. Interview Questions

### Q1. What is Python?

Python is a high-level, interpreted, general-purpose programming language known for its readable syntax and wide range of applications.

---

### Q2. Who created Python?

Python was created by **Guido van Rossum**.

---

### Q3. When was Python first released?

Python was first released in **1991**.

---

### Q4. What is `print()` in Python?

`print()` is a built-in Python function used to display information on the output screen.

---

### Q5. How do you print Hello World in Python?

```python
print("Hello World")
```

---

### Q6. What is a string?

A string is a sequence of characters, generally represented using quotation marks.

Example:

```python
"Hello Python"
```

---

### Q7. What is the difference between `"10"` and `10`?

```python
"10"
```

is a string, while:

```python
10
```

is an integer.

---

### Q8. Is Python case-sensitive?

Yes. Python is case-sensitive.

For example:

```python
print()
```

and:

```python
Print()
```

are different.

---

### Q9. How do you write a comment in Python?

A single-line comment is written using `#`.

Example:

```python
# This is a comment
```

---

### Q10. What are Boolean values in Python?

Python has two Boolean values:

```python
True
False
```

---

## 31. Practice Questions

Try solving these yourself before checking any solution.

# Beginner Level

# Question 1

Print:

```text
Hello Python
```

---

# Question 2

Print your:

- Name
- Age
- College
- Course

---

# Question 3

Print the following:

```text
I am learning Python
I am learning DSA
I want to become a Software Developer
```

---

# Question 4

Print:

- An integer
- A float
- A Boolean
- A string

---

# Question 5

Write a Python program containing three comments and three print statements.

---

## 32. Mini Practice Program

Create a program that displays your learning information.

Expected output:

```text
========================
My Learning Profile
========================
Name: Amaan
Language: Python
Topic: Programming Fundamentals
Next Topic: Print Statements
Goal: Software Developer
========================
```

Try writing this program yourself using only `print()`.

---

## 33. Key Takeaways

After completing this topic, you should remember:

1. Python is a high-level, interpreted, general-purpose programming language.
2. `print()` is used to display output.
3. Strings are written inside quotation marks.
4. Integers are whole numbers.
5. Floating-point numbers contain decimal values.
6. Boolean values are `True` and `False`.
7. Python is case-sensitive.
8. Comments start with `#`.
9. Correct syntax is important.
10. `type()` can be used to check the data type of a value.

---

## 34. Learning Checklist

- [x] Understand what Python is
- [x] Write the first Python program
- [x] Understand `print()`
- [x] Print strings
- [x] Print integers
- [x] Print floating-point values
- [x] Print Boolean values
- [x] Print multiple values
- [x] Understand string vs integer
- [x] Understand comments
- [x] Understand basic syntax
- [x] Understand Python case sensitivity
- [x] Check data types using `type()`
- [x] Solve basic practice questions

---

## 35. What's Next?

Now that we understand the basic `print()` function and how Python displays output, the next topic is:

### Print Statements

In the next topic, we will learn more about:

- Different ways of using `print()`
- Printing multiple values
- Separators
- End parameter
- Formatting output
- New lines
- Combining values
- Practical examples

---

## 36. Folder Structure

Current folder:

```text
01_hello_world/
│
├── 01_hello_world.py
└── README.md
```

# `01_hello_world.py`

Contains the practical Python programs and examples.

# `README.md`

Contains detailed study notes, explanations, examples, interview questions, and practice problems for the Hello World topic.

---

# Conclusion

The `Hello World` program may look very simple, but it is the foundation of understanding how a programming language works.

We learned how to:

```text
Write Code
   ↓
Execute Code
   ↓
Python Processes the Instruction
   ↓
Output is Displayed
```

The most important statement from this topic is:

```python
print("Hello World")
```

This is our first step toward learning Python programming, problem solving, and eventually Data Structures and Algorithms.
```
