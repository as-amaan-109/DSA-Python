# Hello World — Python Basics

Welcome to **Hello World**, the first topic in the Python Programming Fundamentals journey.

Every programming journey starts with a simple output statement. In Python, the `print()` function displays text, numbers, variables, and calculation results on the screen.

This topic introduces the first steps of Python programming and provides practical examples and exercises to help you understand how a Python program displays information.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 01 – Introduction
- **Topic:** Hello World
- **Level:** Beginner
- **Language:** Python
- **Practical File:** `01_hello_world.py`

### Learning Objectives

After completing this topic, you should be able to:

- Understand what a Python program is.
- Run a simple Python program.
- Use `print()` to display output.
- Display text, integers, floating-point numbers, and Boolean values.
- Display multiple values in a single statement.
- Understand the `sep` and `end` parameters of `print()`.
- Use variables and f-strings for formatted output.
- Read and understand basic Python examples.
- Solve simple output-based programming questions.
- Write your own small Python programs.

---

## 2. What Is Python?

Python is a general-purpose programming language used for a wide range of tasks, including automation, web development, data analysis, artificial intelligence, and software development.

Python is popular among beginners because its syntax is generally readable and its basic programs are easy to write.

Example:

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

This program uses Python's built-in `print()` function to display a message.

---

## 3. What Is a Python Program?

A Python program is a collection of instructions written in Python that a Python interpreter can execute.

A beginner program may contain just one statement:

```python
print("I am learning Python.")
```

Larger programs can contain variables, conditions, loops, functions, classes, and many other structures.

For now, the goal is to understand simple statements and observe how their output changes.

---

## 4. Understanding the `print()` Function

The `print()` function displays the values passed to it.

### Basic syntax

```python
print(value)
```

Examples:

```python
print("Hello, World!")
print(100)
print(3.14)
print(True)
```

Output:

```text
Hello, World!
100
3.14
True
```

### Important points

- Text is generally written inside quotation marks.
- Integer values can be printed without quotation marks.
- Decimal numbers can be printed directly.
- Boolean values are written as `True` or `False` in Python.
- Python is case-sensitive: `True` is valid, but `true` is not the Boolean literal.
- The `print()` function adds a newline at the end by default.

---

## 5. Strings and Numbers in Output

### Strings

A string represents text.

```python
print("Python")
print('Programming is fun')
```

Python permits both single and double quotes for string literals, provided the quotation marks are correctly matched.

### Integers

Integers represent whole numbers.

```python
print(10)
print(-25)
print(0)
```

### Floating-point numbers

Floating-point values represent numbers that can contain a fractional part.

```python
print(3.14)
print(99.5)
print(-12.75)
```

### Boolean values

Boolean values represent truth values.

```python
print(True)
print(False)
```

### String versus numeric value

```python
print(100)
print("100")
```

Both can appear as `100` in the output, but their data types differ: the first is an integer and the second is a string.

---

## 6. Displaying Multiple Values

The `print()` function can accept multiple positional arguments, separated by commas.

```python
name = "Amaan"
age = 22

print("Name:", name)
print("Age:", age)
```

Output:

```text
Name: Amaan
Age: 22
```

Python's default separator places a space between separate arguments.

Example:

```python
print("Learning", "Python", "Programming")
```

Output:

```text
Learning Python Programming
```

This is useful when displaying labels alongside variable values.

---

## 7. The `sep` Parameter

The `sep` parameter specifies the string inserted between multiple arguments to `print()`.

The default separator is a single space.

Example:

```python
print("Python", "Java", "JavaScript", sep=" | ")
```

Output:

```text
Python | Java | JavaScript
```

Another example:

```python
print(10, 20, 30, sep=" --> ")
```

Output:

```text
10 --> 20 --> 30
```

Use `sep` when you want a particular format between values.

---

## 8. The `end` Parameter

The `end` parameter specifies what is printed after the supplied values.

By default, `print()` ends with a newline.

Example:

```python
print("Hello", end=" ")
print("World!")
```

Output:

```text
Hello World!
```

Another example:

```python
print("Learning", end="...")
print("Python")
```

Output:

```text
Learning...Python
```

This is useful when several print statements must contribute to the same output line.

---

## 9. Displaying Variables

A variable is a named reference to a value.

Example:

```python
course = "Python Programming"
week = 1
is_beginner = True

print("Course:", course)
print("Week:", week)
print("Beginner:", is_beginner)
```

Output:

```text
Course: Python Programming
Week: 1
Beginner: True
```

Variables help programs display information without repeatedly writing the same values directly into output statements.

### Good variable naming practices

- Choose names that describe their purpose.
- Use letters, digits, and underscores where permitted.
- Do not start a variable name with a digit.
- Avoid Python reserved keywords as variable names.
- Follow a consistent naming convention, such as `student_name`.

Example:

```python
student_name = "Amaan"
```

---

## 10. Formatted Output with F-Strings

An f-string allows expressions and variable values to be inserted into a string.

Example:

```python
name = "Amaan"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Amaan and I am 22 years old.
```

The letter `f` before the opening quotation mark enables expressions inside curly braces to be evaluated.

Another example:

```python
a = 10
b = 20

print(f"The sum of {a} and {b} is {a + b}.")
```

Output:

```text
The sum of 10 and 20 is 30.
```

F-strings are useful when output combines text, variable values, and calculations.

---

## 11. Arithmetic in Output

Python can calculate expressions and display their results.

```python
a = 10
b = 20

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

Output:

```text
Addition: 30
Subtraction: -10
Multiplication: 200
Division: 0.5
```

The expression is evaluated before its result is displayed.

You can also print a calculation directly:

```python
print(5 + 3)
```

Output:

```text
8
```

---

## 12. Python Comments

Comments explain the code to the person reading it. Python ignores comments when executing a program.

A single-line comment starts with `#`.

```python
# Display a greeting
print("Hello, World!")
```

Useful comments describe a program's purpose or clarify logic that may not be obvious.

Avoid comments that simply repeat every line without adding useful information.

---

## 13. Overview of the 12 Examples

The practical file `01_hello_world.py` contains these examples:

| No. | Example | Concept |
|---:|---|---|
| 1 | Hello World | First Python output |
| 2 | Display a Simple Message | Printing text |
| 3 | Display a Name | Printing a personal message |
| 4 | Display Integers | Printing whole numbers |
| 5 | Display Float Values | Printing decimal numbers |
| 6 | Display Boolean Values | Printing `True` and `False` |
| 7 | Display Multiple Values | Multiple arguments to `print()` |
| 8 | Use the `sep` Parameter | Custom separators |
| 9 | Use the `end` Parameter | Custom line endings |
| 10 | Display Multiple Lines | Separate print statements |
| 11 | Display Variables | Printing stored values |
| 12 | Display a Calculation | Showing arithmetic results |

### How to study the examples

1. Read the comments above the example.
2. Predict its output.
3. Run only that example through the menu.
4. Compare the actual output with your prediction.
5. Change one value and observe what happens.
6. Explain the result in your own words.

---

## 14. Twelve Solved Practice Questions

The Python file also includes 12 solved exercises:

1. Print Your Full Name
2. Print Your Course
3. Display Two Messages
4. Display Five Numbers
5. Display Numbers from 1 to 5 on One Line
6. Display Subjects Separated by Commas
7. Display an Addition Equation
8. Use an F-String
9. Display a Student Profile
10. Display Arithmetic Results
11. Display Square and Cube
12. Display a Personal Introduction

These exercises reinforce basic output, variables, arithmetic, separators, and formatting.

The answers are included in the Python file so that you can run each solution independently and compare its result with your understanding.

---

## 15. Five Questions for Independent Practice

Try these five questions without looking for a solution in the code.

### Question 1: Create Your Own Introduction

Display your name, course, current learning topic, and career goal.

### Question 2: Display a Weekly Study Plan

Print the names of five subjects, each on a separate line.

### Question 3: Create an Output Card

Print a title, a decorative border, and at least three lines of information.

### Question 4: Format Arithmetic Equations

Store two numbers in variables and display their addition, subtraction, and multiplication as readable equations.

### Question 5: Create a Mini Student Report

Display a student's name, roll number, course, and favourite subject with clear labels and consistent formatting.

### Suggested approach

For each question:

1. Understand the required output.
2. Identify the values you need.
3. Decide whether to use separate `print()` calls, multiple arguments, `sep`, `end`, or an f-string.
4. Write the program.
5. Run it and verify the formatting.

The practice questions intentionally do not include completed solutions.

---

## 16. Common Beginner Mistakes

### Forgetting quotation marks around text

Incorrect:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

Without quotation marks, Python generally treats `Hello` as a variable name.

### Using the wrong Boolean capitalization

Incorrect:

```python
print(true)
```

Correct:

```python
print(True)
```

Python's Boolean literals are case-sensitive.

### Confusing `sep` with `end`

- `sep` controls the text placed between multiple arguments.
- `end` controls the text printed after the arguments.

### Expecting `print()` calls to stay on the same line

By default, each `print()` statement ends with a newline. Use `end` to change that behaviour.

### Confusing text and numbers

```python
print("10")
print(10)
```

The output looks similar, but one value is text and the other is numeric.

### Writing unclear output

Instead of:

```python
print(20)
```

Consider:

```python
print("Total:", 20)
```

Labels make results easier to understand.

---

## 17. How to Run This File

Open PowerShell or your VS Code terminal at the repository root and run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\01-Introduction\01_hello_world\01_hello_world.py"
```

The program displays a menu with three main options:

1. Run the 12 examples.
2. Run the 12 solved questions.
3. View the 5 questions without answers.

Choose a category and then select the required item. Enter `0` to return to the previous menu or exit from the main menu.

If Python is not available under the `python` command on your Windows machine, try:

```powershell
py "PYTHON\Week-1-Programming-Fundamentals\01-Introduction\01_hello_world\01_hello_world.py"
```

---

## 18. Basic Interview Questions

**Q1. What is Python?**

Python is a general-purpose programming language used for many kinds of software and automation tasks.

**Q2. What is the purpose of `print()`?**

It displays values or messages to the output stream, usually the terminal.

**Q3. What is a string?**

A string represents text, such as `"Python"`.

**Q4. What is the difference between an integer and a float?**

An integer represents a whole number. A float represents a floating-point number that may contain a fractional part.

**Q5. What is a Boolean value?**

A Boolean value represents either `True` or `False`.

**Q6. What is a variable?**

A variable is a name that refers to a value in a program.

**Q7. What does the `sep` parameter do?**

It defines the separator inserted between multiple arguments passed to `print()`.

**Q8. What does the `end` parameter do?**

It defines what is printed after the values in a `print()` call. Its default is a newline.

**Q9. What is an f-string?**

An f-string is a formatted string literal that allows expressions to be embedded inside curly braces.

**Q10. What is a comment in Python?**

A comment is text intended to explain code to readers. A single-line comment begins with `#`.

**Q11. Are `"100"` and `100` the same data type?**

No. `"100"` is a string, whereas `100` is an integer.

**Q12. Why should we test output formatting?**

Testing helps confirm that the result is readable and matches the expected layout.

---

## ✅ Completion Checklist

- [ ] Run the Hello World example.
- [ ] Understand strings, integers, floats, and Booleans.
- [ ] Display multiple values.
- [ ] Experiment with `sep` and `end`.
- [ ] Display variables and arithmetic results.
- [ ] Understand comments and f-strings.
- [ ] Complete all 12 solved questions.
- [ ] Attempt all 5 independent practice questions.
- [ ] Answer the interview questions in your own words.
- [ ] Run the entire menu without errors.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to write simple Python programs, display different kinds of values, format output, and solve beginner-level output problems.

These concepts prepare you for the next topic, **Print Statement**, where you can study printing and output formatting in greater detail.

---

## 📌 Final Note

**Do not just copy the output. Predict it, run the code, and explain why it appears that way.**

A strong programming foundation comes from understanding small concepts clearly and practising them consistently.
