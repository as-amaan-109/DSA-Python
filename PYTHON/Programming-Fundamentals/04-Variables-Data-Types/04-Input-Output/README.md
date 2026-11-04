# Python Input and Output

## Week 1 — Programming Fundamentals

**Week:** 1  
**Main Section:** Programming Fundamentals  
**Chapter:** Variables and Data Types  
**Subsection:** Input and Output  
**Language:** Python 3  
**Level:** Beginner to Intermediate  
**Purpose:** Learn how Python programs receive information, process user input, convert data types, and display meaningful output.

---

# Table of Contents

1. Introduction
2. About This Section
3. Learning Objectives
4. What Is Input?
5. What Is Output?
6. Input and Output in Programming
7. The Input-Process-Output Cycle
8. Importance of Input and Output
9. Understanding Python Input and Output
10. Folder Structure
11. Overview of All Four Topics
12. Topic 1 — Input
13. Topic 2 — Output
14. Topic 3 — User Input
15. Topic 4 — Input Conversion
16. Understanding the `input()` Function
17. Understanding the `print()` Function
18. The Difference Between Input and Output
19. The Difference Between Input and User Input
20. Understanding Data Received from Users
21. Understanding Data Types in Input and Output
22. Working with Strings
23. Working with Integers
24. Working with Floating-Point Numbers
25. Working with Boolean Values
26. Working with Complex Numbers
27. Input Conversion
28. Type Conversion Functions
29. Integer Conversion
30. Float Conversion
31. String Conversion
32. Boolean Conversion
33. Complex Number Conversion
34. Reading Multiple Inputs
35. Splitting Input Values
36. Handling User Input
37. Input Validation
38. Error Handling
39. Exception Handling
40. Formatting Output
41. The `sep` Parameter
42. The `end` Parameter
43. Escape Sequences
44. New Line and Tab Formatting
45. F-Strings
46. String Concatenation
47. Displaying Different Data Types
48. Displaying Calculated Results
49. Input and Output Examples
50. Complete Input and Output Workflow
51. Combined Practical Examples
52. Solved Practical Programs
53. Common Mistakes
54. Debugging Techniques
55. Testing Input and Output Programs
56. Boundary Testing
57. Input Validation Test Cases
58. Output Verification
59. Best Practices
60. Code Readability
61. Naming Conventions
62. Program Structure
63. Real-Life Applications
64. Mini Project Ideas
65. Practice Questions
66. Practical Challenges
67. Learning Roadmap
68. Study Strategy
69. Revision Notes
70. Quick Reference
71. Frequently Asked Questions
72. Viva Questions and Answers
73. Important Terminology
74. Learning Checklist
75. Final Summary

---

# 1. Introduction

Input and output are fundamental concepts in every programming language.

A program generally needs information to perform a task.

It may also need to communicate its result to the user.

For example, consider a simple calculator.

The user enters two numbers.

The program adds those numbers.

The program displays their sum.

This process involves three basic activities:

1. Taking input.
2. Processing information.
3. Producing output.

Python provides simple built-in functions for these activities.

The most commonly used functions are:

- `input()`
- `print()`

The `input()` function collects information from the user.

The `print()` function displays information on the screen.

These two functions are among the first tools a Python programmer learns.

However, writing interactive programs requires more than simply calling these functions.

A good program must also understand:

- What kind of input it receives.
- How the input should be processed.
- Which data type is required.
- How to convert data when necessary.
- How to handle invalid input.
- How to display a clear result.
- How to validate user-provided information.

This section introduces these concepts step by step.

The four topic folders provide a structured learning path from basic input and output to input conversion.

---

# 2. About This Section

The `04-Input-Output` folder is part of the Variables and Data Types chapter.

Its purpose is to teach how Python programs interact with users.

Before learning advanced programming concepts, it is important to understand how information enters a program and how results are displayed.

This section contains four topic folders.

| Folder | Topic | Main Purpose |
|---|---|---|
| `01_input` | Input | Understand how to receive information |
| `02_output` | Output | Understand how to display information |
| `03_user_input` | User Input | Build programs that interact with users |
| `04_input_conversion` | Input Conversion | Convert received input into appropriate data types |

Each folder contains:

- A Python source file.
- A topic-specific README file.
- Explanations of the topic.
- Examples.
- Solved programming exercises.
- Practice questions.
- A learning checklist.

The individual topic README files provide detailed explanations of their respective subjects.

This parent README connects those topics into one complete learning section.

---

# 3. Learning Objectives

After completing this section, you should be able to understand and use input and output in Python programs.

## Basic Concepts

- Explain the meaning of input.
- Explain the meaning of output.
- Understand the input-process-output cycle.
- Identify the role of input in a program.
- Identify the role of output in a program.
- Understand how a program communicates with its user.
- Identify the difference between data collection and data display.

## Input Skills

- Use the `input()` function.
- Display a prompt before collecting information.
- Store input in variables.
- Read textual information.
- Read numeric information as text.
- Understand what happens when the user presses Enter.
- Handle empty input.
- Read multiple values.
- Use whitespace handling when required.

## Output Skills

- Use the `print()` function.
- Display strings.
- Display integers.
- Display floating-point values.
- Display Boolean values.
- Display multiple variables.
- Use separators.
- Control line endings.
- Use escape sequences.
- Format text.
- Use f-strings.

## User Interaction

- Create interactive programs.
- Ask questions using input prompts.
- Process user responses.
- Display meaningful messages.
- Build simple menu-driven programs.
- Validate user responses.
- Handle unexpected user input.

## Input Conversion

- Understand why input conversion is necessary.
- Convert text into integers.
- Convert text into floating-point values.
- Convert values into strings.
- Convert suitable text into complex numbers.
- Understand Boolean truthiness.
- Parse yes/no answers.
- Convert lists of numeric strings.
- Convert binary strings into decimal integers.

## Error Handling

- Understand `ValueError`.
- Understand `TypeError`.
- Use `try` and `except`.
- Handle invalid numeric input.
- Retry input when necessary.
- Validate ranges.
- Display helpful error messages.

## Programming Skills

- Write small interactive programs.
- Combine input, processing, and output.
- Use variables to store information.
- Apply data types correctly.
- Test programs with different inputs.
- Debug input-related errors.
- Organize reusable input-handling logic.

---

# 4. What Is Input?

Input is information supplied to a computer program.

A program receives input so that it can perform a task.

Input may come from:

- A keyboard.
- A file.
- A database.
- A web form.
- Another program.
- An external device.
- An application programming interface.

In beginner Python programs, input is commonly collected through the keyboard using the `input()` function.

Example:

```python
name = input("Enter your name: ")

print(name)
```

Sample interaction:

```text
Enter your name: Amaan
Amaan
```

The user supplies the name.

The program stores the supplied text in a variable.

The program then displays that value.

## 4.1 Characteristics of Input

Input provides information to a program.

It allows the user to control what the program processes.

Different programs require different types of input.

For example:

| Program | Possible Input |
|---|---|
| Calculator | Numbers |
| Student Management System | Student details |
| Login System | Username and password |
| Shopping Application | Product and quantity |
| Temperature Converter | Temperature |
| Attendance System | Student identification and attendance choice |
| Survey Application | Answers |
| Banking Application | Transaction information |

## 4.2 Why Is Input Important?

Without input, many programs would have to work with fixed information.

Input allows a program to work with different values each time it runs.

For example:

```python
number = 10

print(number * 2)
```

This program always uses the same number.

An interactive version is:

```python
number = int(input("Enter a number: "))

print(number * 2)
```

Now the user can provide a different number every time the program runs.

---

# 5. What Is Output?

Output is information produced by a program.

It communicates the result of a calculation, operation, or decision.

In beginner Python programs, output is commonly displayed using the `print()` function.

Example:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

## 5.1 Characteristics of Output

Output presents information to the user.

It may include:

- Text messages.
- Numbers.
- Calculation results.
- Program status.
- Error messages.
- Instructions.
- Reports.
- Menu options.

## 5.2 Why Is Output Important?

A program may successfully process information internally, but users need a way to understand its result.

Consider:

```python
first = 10
second = 20

result = first + second
```

The program calculates the answer.

However, it does not display the answer.

To communicate the result, use:

```python
print(result)
```

Output:

```text
30
```

Output makes the program's result visible.

---

# 6. Input and Output in Programming

Input and output work together.

Input supplies the information.

Processing performs the required operation.

Output communicates the result.

Consider a simple addition program.

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

result = first + second

print("Sum:", result)
```

The program performs several operations.

| Step | Operation | Purpose |
|---|---|---|
| 1 | First `input()` | Collect the first value |
| 2 | `int()` | Convert the first value |
| 3 | Second `input()` | Collect the second value |
| 4 | `int()` | Convert the second value |
| 5 | `+` | Add the numbers |
| 6 | `print()` | Display the result |

The output depends on the input supplied by the user.

This is the foundation of interactive programming.

---

# 7. The Input-Process-Output Cycle

Many programs follow a simple structure called the Input-Process-Output cycle.

It is commonly abbreviated as IPO.

The cycle has three main stages.

## 7.1 Input

The program receives information.

Example:

```python
number = int(input("Enter a number: "))
```

The user supplies a number.

## 7.2 Process

The program performs an operation on the received information.

Example:

```python
square = number * number
```

The program calculates the square.

## 7.3 Output

The program displays the result.

Example:

```python
print("Square:", square)
```

The calculated value is displayed.

## 7.4 Complete IPO Example

```python
number = int(input("Enter a number: "))

square = number * number

print("Square:", square)
```

Input:

```text
5
```

Output:

```text
Square: 25
```

## 7.5 IPO Diagram

```text
       INPUT
         |
         v
  Collect Information
         |
         v
       PROCESS
         |
         v
   Perform Operation
         |
         v
       OUTPUT
         |
         v
   Display Result
```

## 7.6 IPO in Real Applications

| Application | Input | Process | Output |
|---|---|---|---|
| Calculator | Two numbers | Addition | Sum |
| Student Result | Marks | Calculate average | Result |
| Shopping App | Price and quantity | Calculate total | Bill |
| Temperature Converter | Temperature | Apply formula | Converted temperature |
| Attendance System | Attendance information | Update record | Status |
| Login System | Credentials | Verify details | Login status |

The IPO cycle is not limited to Python.

It is a general way of understanding how programs work.

---

# 8. Importance of Input and Output

Input and output are important because they allow a program to interact with its environment.

## 8.1 User Interaction

Users can provide information to a program.

The program can respond with appropriate messages.

## 8.2 Dynamic Processing

A program can process different values without requiring changes to its source code.

## 8.3 Communication

Output allows users to understand what a program has done.

## 8.4 Reusability

The same program can work with many different input values.

## 8.5 Better User Experience

Clear prompts and well-formatted output make programs easier to use.

## 8.6 Error Communication

Output can inform users when something goes wrong.

Example:

```python
print("Invalid input. Please try again.")
```

## 8.7 Learning Programming

Input and output provide a simple way to understand:

- Variables.
- Data types.
- Functions.
- Expressions.
- Operators.
- Conditional statements.
- Loops.
- Exception handling.

They are used throughout Python programming.

---

# 9. Understanding Python Input and Output

Python includes built-in functions for basic input and output.

The most important functions in this section are:

```python
input()
```

and:

```python
print()
```

## 9.1 Input Function

The `input()` function reads a line of text.

Syntax:

```python
variable = input("Prompt message: ")
```

Example:

```python
name = input("Enter your name: ")
```

## 9.2 Output Function

The `print()` function displays values.

Syntax:

```python
print(value)
```

Example:

```python
print("Welcome to Python")
```

## 9.3 Combining Input and Output

```python
name = input("Enter your name: ")

print("Welcome,", name)
```

Input:

```text
Amaan
```

Output:

```text
Welcome, Amaan
```

## 9.4 Why Learn Both Functions Together?

Input and output are frequently used together.

A normal interactive program:

1. Displays a prompt.
2. Collects input.
3. Stores the information.
4. Processes the information.
5. Displays a result.

Understanding this flow makes it easier to build larger programs.

---

# 10. Folder Structure

The `04-Input-Output` section contains four topic folders.

```text
04-Input-Output/
│
├── 01_input/
│   ├── 01_input.py
│   └── README.md
│
├── 02_output/
│   ├── 02_output.py
│   └── README.md
│
├── 03_user_input/
│   ├── 03_user_input.py
│   └── README.md
│
├── 04_input_conversion/
│   ├── 04_input_conversion.py
│   └── README.md
│
└── README.md
```

## 10.1 Parent README

The current file is the parent README.

It explains the complete Input and Output section.

It also provides the learning order and topic overview.

## 10.2 Python Source Files

Each topic folder contains a Python source file.

The source file provides practical examples and exercises.

## 10.3 Topic README Files

Each topic folder contains its own README.

The topic README explains the concepts in more detail.

The parent README should be used as the main section overview.

The child README files should be used for topic-specific study.

---

# 11. Overview of All Four Topics

The four topic folders are arranged in a learning sequence.

## 11.1 Topic 1 — Input

Folder:

```text
01_input/
```

Main concept:

Learn how to collect information using Python's `input()` function.

Important ideas:

- Meaning of input.
- Input function.
- Input prompt.
- Reading text.
- Storing input in variables.
- Understanding returned values.
- Empty input.
- Basic input examples.

Expected outcome:

You should be able to receive information from the user and store it in variables.

## 11.2 Topic 2 — Output

Folder:

```text
02_output/
```

Main concept:

Learn how to display information using Python's `print()` function.

Important ideas:

- Meaning of output.
- Print function.
- Displaying text.
- Displaying numbers.
- Displaying variables.
- Printing multiple values.
- Separators.
- Line endings.
- Escape sequences.
- Formatted output.

Expected outcome:

You should be able to display clear and meaningful information using Python.

## 11.3 Topic 3 — User Input

Folder:

```text
03_user_input/
```

Main concept:

Learn how to create programs that interact with users.

Important ideas:

- User prompts.
- Reading user information.
- Storing values.
- Working with multiple inputs.
- Processing user responses.
- Creating interactive examples.
- Understanding the user interaction flow.
- Handling different user responses.

Expected outcome:

You should be able to create simple interactive programs.

## 11.4 Topic 4 — Input Conversion

Folder:

```text
04_input_conversion/
```

Main concept:

Learn how to convert input into suitable Python data types.

Important ideas:

- Why conversion is required.
- `int()`.
- `float()`.
- `str()`.
- `bool()`.
- `complex()`.
- List conversion.
- Multiple inputs.
- Binary conversion.
- Exception handling.
- Validation.

Expected outcome:

You should be able to convert received input into the appropriate data type and use it in calculations.

---

# 12. Topic 1 — Input

## 12.1 Introduction

Input is the information supplied to a program.

In Python, the `input()` function is commonly used to collect text from the keyboard.

Example:

```python
name = input("Enter your name: ")

print(name)
```

The program asks the user for a name.

The entered text is stored in the variable `name`.

The program displays the stored value.

## 12.2 Syntax

```python
variable = input("Prompt message")
```

## 12.3 Components

`variable` stores the received value.

`input()` reads the user's response.

The prompt message tells the user what information is required.

## 12.4 Example: Name Input

```python
name = input("Enter your name: ")

print("Name:", name)
```

Input:

```text
Amaan
```

Output:

```text
Name: Amaan
```

## 12.5 Example: City Input

```python
city = input("Enter your city: ")

print("City:", city)
```

## 12.6 Example: College Input

```python
college = input("Enter your college name: ")

print("College:", college)
```

## 12.7 Example: Course Input

```python
course = input("Enter your course: ")

print("Course:", course)
```

## 12.8 Understanding Returned Values

The `input()` function returns a string.

Even when the user enters digits, the value is initially text.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Input:

```text
20
```

Output:

```text
<class 'str'>
```

The value is a string until it is converted.

## 12.9 Input Without a Prompt

A prompt is optional.

```python
name = input()

print(name)
```

However, a helpful prompt usually makes an interactive program easier to understand.

## 12.10 Important Rule

Remember:

```python
input()
```

reads text.

It does not automatically decide whether the entered text represents an integer, float, or another data type.

This behavior is explained in Topic 4.

---

# 13. Topic 2 — Output

## 13.1 Introduction

Output is the information displayed by a program.

Python provides the `print()` function to display values.

Example:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

## 13.2 Syntax

```python
print(value)
```

The `value` can be:

- A string.
- An integer.
- A float.
- A Boolean.
- A variable.
- An expression.
- Multiple values.

## 13.3 Displaying Text

```python
print("Welcome to Python Programming")
```

## 13.4 Displaying Integers

```python
print(100)
```

## 13.5 Displaying Floating-Point Values

```python
print(10.5)
```

## 13.6 Displaying Boolean Values

```python
print(True)
print(False)
```

## 13.7 Displaying Variables

```python
name = "Amaan"
age = 20

print(name)
print(age)
```

## 13.8 Displaying Multiple Values

```python
name = "Amaan"
age = 20

print("Name:", name, "Age:", age)
```

Output:

```text
Name: Amaan Age: 20
```

## 13.9 Separating Values

The `sep` parameter controls the separator between printed values.

```python
print("Python", "Java", "C++", sep=" | ")
```

Output:

```text
Python | Java | C++
```

## 13.10 Controlling the Ending

The `end` parameter controls what is printed at the end of a `print()` call.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

## 13.11 Formatting Output

F-strings provide a convenient way to display values inside text.

```python
name = "Amaan"
age = 20

print(f"My name is {name} and my age is {age}.")
```

Output:

```text
My name is Amaan and my age is 20.
```

## 13.12 Why Is Output Formatting Important?

Good output formatting makes information easier to read.

It also improves the experience of using interactive programs.

---

# 14. Topic 3 — User Input

## 14.1 Introduction

User input refers to information provided by a person interacting with a program.

A program can ask the user questions and use the answers to perform operations.

Example:

```python
name = input("Enter your name: ")
course = input("Enter your course: ")

print("Student Name:", name)
print("Course:", course)
```

The program collects two values.

It stores them in separate variables.

It then displays the information.

## 14.2 User Interaction

An interactive program communicates with the user.

It can:

1. Display instructions.
2. Ask a question.
3. Read the response.
4. Process the response.
5. Display a result.

## 14.3 Example: Student Information

```python
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course: ")

print("Student Information")
print("--------------------")
print("Name:", name)
print("Roll Number:", roll_number)
print("Course:", course)
```

## 14.4 Example: Personal Information

```python
name = input("Enter your name: ")
city = input("Enter your city: ")
college = input("Enter your college: ")

print("Your Details")
print("Name:", name)
print("City:", city)
print("College:", college)
```

## 14.5 Example: Multiple User Inputs

```python
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name

print("Full Name:", full_name)
```

## 14.6 Processing User Responses

User input can be processed in several ways.

For example:

- A name can be displayed.
- A course can be stored.
- A number can be converted.
- A response can be checked.
- Multiple values can be combined.

## 14.7 Interactive Programs

Examples of interactive applications include:

- Calculators.
- Registration forms.
- Student information systems.
- Survey programs.
- Billing programs.
- Login interfaces.
- Command-line menus.

The `03_user_input` folder develops the basic skills needed to write these programs.

---

# 15. Topic 4 — Input Conversion

## 15.1 Introduction

Input conversion is the process of converting received input into an appropriate data type.

The `input()` function returns text.

A program may need to convert that text before performing numerical operations.

Example:

```python
first = input("Enter first number: ")
second = input("Enter second number: ")

print(first + second)
```

Input:

```text
10
20
```

Output:

```text
1020
```

The two values are strings.

The `+` operator joins their text.

To perform addition, convert them into integers.

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print(first + second)
```

Input:

```text
10
20
```

Output:

```text
30
```

## 15.2 Why Conversion Is Required

Conversion is required when the program needs to process the input using a different data type.

Examples:

- Age may need to be an integer.
- Price may need to be a float or decimal value.
- A mathematical value may need to be complex.
- A number may need to become text for display or concatenation.
- A yes/no response may need to become a Boolean value.

## 15.3 Common Conversion Functions

| Function | Purpose |
|---|---|
| `int()` | Convert suitable values to integers |
| `float()` | Convert suitable values to floating-point values |
| `str()` | Produce a string representation |
| `bool()` | Convert a value to a Boolean truth value |
| `complex()` | Convert suitable values to complex numbers |

## 15.4 Integer Conversion

```python
number = int("25")

print(number)
print(type(number))
```

Output:

```text
25
<class 'int'>
```

## 15.5 Float Conversion

```python
number = float("25.75")

print(number)
print(type(number))
```

Output:

```text
25.75
<class 'float'>
```

## 15.6 String Conversion

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

## 15.7 Boolean Conversion

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
```

Output:

```text
False
True
False
True
```

Important:

```python
bool("False")
```

returns `True` because `"False"` is a nonempty string.

Use explicit parsing for yes/no text.

## 15.8 Complex Conversion

```python
number = complex("2+3j")

print(number)
```

Output:

```text
(2+3j)
```

## 15.9 Conversion Errors

Invalid input can cause an exception.

Example:

```python
number = int("hello")
```

This raises `ValueError`.

Exception handling should be used when invalid input is possible.

## 15.10 Conversion and Validation

Conversion and validation are different.

Conversion checks whether the value can be represented as the requested type.

Validation checks whether the resulting value satisfies the application's requirements.

For example:

```python
age = int("15")
```

Conversion succeeds.

However, an application that requires an adult age may reject the value.

---

# 16. Understanding the `input()` Function

The `input()` function is one of the most important beginner functions in Python.

## 16.1 General Syntax

```python
value = input("Enter a value: ")
```

## 16.2 How It Works

When Python reaches `input()`:

1. It displays the prompt.
2. It waits for the user.
3. The user enters text.
4. The user presses Enter.
5. Python returns the entered line as a string.
6. The result can be assigned to a variable.

## 16.3 Example

```python
name = input("What is your name? ")

print("Hello,", name)
```

## 16.4 Input with No Prompt

```python
value = input()

print(value)
```

## 16.5 Empty Input

When the user presses Enter without typing anything, `input()` returns an empty string.

```python
value = input("Enter something: ")

print(repr(value))
```

The representation of empty input is:

```text
''
```

## 16.6 Input with Spaces

```python
name = input("Enter your name: ")

print(repr(name))
```

The representation makes surrounding spaces visible.

## 16.7 Removing Surrounding Spaces

```python
name = input("Enter your name: ").strip()
```

The `strip()` method removes leading and trailing whitespace.

## 16.8 Important Points

- `input()` returns a string.
- The prompt is optional.
- The user completes the input by pressing Enter.
- The result can be stored in a variable.
- Input can be converted when another data type is required.
- Invalid input must be handled appropriately.

---

# 17. Understanding the `print()` Function

The `print()` function displays information.

## 17.1 General Syntax

```python
print(*objects, sep=" ", end="\n")
```

The function supports several arguments.

The most frequently used options are:

- Objects to display.
- `sep`.
- `end`.

## 17.2 Display a String

```python
print("Hello")
```

## 17.3 Display an Integer

```python
print(100)
```

## 17.4 Display a Float

```python
print(10.5)
```

## 17.5 Display a Variable

```python
language = "Python"

print(language)
```

## 17.6 Display Multiple Variables

```python
name = "Amaan"
age = 20

print(name, age)
```

## 17.7 Display a Calculation

```python
result = 10 + 20

print(result)
```

## 17.8 Display a Message and Result

```python
result = 10 + 20

print("Sum:", result)
```

## 17.9 Use `sep`

```python
print("2026", "10", "31", sep="-")
```

Output:

```text
2026-10-31
```

## 17.10 Use `end`

```python
print("Python", end=" ")
print("Programming")
```

Output:

```text
Python Programming
```

## 17.11 Display Formatted Values

```python
name = "Amaan"
marks = 85

print(f"{name} scored {marks} marks.")
```

## 17.12 Important Points

- `print()` displays objects.
- Multiple values can be displayed.
- The default separator is a space.
- The default ending is a newline.
- `sep` changes the separator.
- `end` changes the ending.
- F-strings help create readable output.

---

# 18. Difference Between Input and Output

Input and output perform different functions.

| Basis | Input | Output |
|---|---|---|
| Meaning | Information received by a program | Information produced by a program |
| Purpose | Supply data | Display information |
| Common Python function | `input()` | `print()` |
| Direction | User or source to program | Program to user or destination |
| Example | Entering a name | Displaying a name |
| Result | A received value | Visible information |
| Common use | Reading values | Showing messages and results |

## 18.1 Input Example

```python
name = input("Enter name: ")
```

## 18.2 Output Example

```python
print("Welcome to Python")
```

## 18.3 Combined Example

```python
name = input("Enter name: ")

print("Welcome,", name)
```

Input receives the information.

Output displays the response.

---

# 19. Difference Between Input and User Input

The words input and user input are closely related.

However, they can be used in slightly different contexts.

## Input

Input is a general term for information provided to a program.

It can come from a keyboard, file, database, network, or another source.

## User Input

User input is information provided directly by a person using the program.

Example:

```python
name = input("Enter your name: ")
```

In this beginner section, the `input()` function is primarily used to demonstrate keyboard-based user input.

## Comparison

| Input | User Input |
|---|---|
| General information received by a program | Information supplied by a person |
| May come from different sources | Comes from a user interaction |
| May be automated | Usually entered or selected by a user |
| General programming concept | A specific type of interaction |

---

# 20. Understanding Data Received from Users

A program must understand the information that it receives.

The same characters can represent different kinds of information depending on how they are interpreted.

For example:

```python
value = "100"
```

This is a string.

By contrast:

```python
value = 100
```

This is an integer.

Although both values display as `100`, their data types are different.

## 20.1 Why Data Types Matter

Data types influence:

- Which operations can be performed.
- How values behave.
- How values are stored.
- How values are compared.
- How calculations work.
- How values are displayed.

## 20.2 Example

```python
first = "10"
second = "20"

print(first + second)
```

Output:

```text
1020
```

Now consider:

```python
first = 10
second = 20

print(first + second)
```

Output:

```text
30
```

The operator behaves differently because the operands have different types.

## 20.3 Verify Data Types

Python provides the `type()` function.

```python
name = "Amaan"
age = 20
price = 99.5
is_active = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_active))
```

The output identifies the data types.

Understanding `type()` is useful when debugging conversion problems.

---

# 21. Understanding Data Types in Input and Output

The main data types used in this section are:

- String.
- Integer.
- Float.
- Boolean.
- Complex.

## 21.1 String

Strings represent text.

Example:

```python
name = "Amaan"

print(name)
```

## 21.2 Integer

Integers represent whole numbers.

Example:

```python
age = 20

print(age)
```

## 21.3 Float

Floats represent floating-point numbers.

Example:

```python
price = 99.50

print(price)
```

## 21.4 Boolean

Booleans represent truth values.

Example:

```python
is_student = True

print(is_student)
```

## 21.5 Complex

Complex numbers contain real and imaginary components.

Example:

```python
number = 2 + 3j

print(number)
```

## 21.6 Why Choose the Correct Data Type?

The correct type makes processing more natural and avoids unnecessary conversions.

For example:

- A person's name should normally be stored as text.
- A count is normally stored as an integer.
- A measurement may use a float.
- A true-or-false condition can use a Boolean.

The choice should reflect the meaning and requirements of the information.

---

# 22. Working with Strings

Strings are used for textual input and output.

## 22.1 String Input

```python
name = input("Enter your name: ")
```

## 22.2 String Output

```python
print("Name:", name)
```

## 22.3 Joining Strings

```python
first_name = "Amaan"
last_name = "Syed"

full_name = first_name + " " + last_name

print(full_name)
```

## 22.4 String Methods

Useful string methods include:

| Method | Purpose |
|---|---|
| `strip()` | Remove surrounding whitespace |
| `lower()` | Convert letters to lowercase |
| `upper()` | Convert letters to uppercase |
| `title()` | Convert text to title-style capitalization |
| `replace()` | Replace specified text |
| `split()` | Divide text into parts |
| `capitalize()` | Capitalize the first character according to its rules |

## 22.5 Example

```python
name = input("Enter your name: ")

name = name.strip()

print("Welcome,", name)
```

## 22.6 Important Note

String methods are useful when preparing textual input.

They do not automatically convert arbitrary text into numeric values.

---

# 23. Working with Integers

Integers represent whole-number values.

Examples include:

```python
0
10
-10
100
```

## 23.1 Integer Input

Because `input()` returns text, use conversion when an integer is required.

```python
age = int(input("Enter age: "))
```

## 23.2 Integer Processing

```python
number = int(input("Enter a number: "))

double = number * 2

print("Double:", double)
```

## 23.3 Integer Output

```python
quantity = 5

print("Quantity:", quantity)
```

## 23.4 Common Applications

Integers are commonly used for:

- Counts.
- Quantity.
- Age in whole years.
- Number of students.
- Number of attempts.
- Whole-number calculations.

## 23.5 Important Note

An integer conversion fails when the provided text is not a valid integer representation.

Use exception handling when invalid text is possible.

---

# 24. Working with Floating-Point Numbers

Floating-point numbers represent values that may include fractional components.

Examples:

```python
10.5
99.75
-2.5
```

## 24.1 Float Input

```python
price = float(input("Enter price: "))
```

## 24.2 Float Processing

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total:", total)
```

## 24.3 Float Output

```python
average = 85.75

print("Average:", average)
```

## 24.4 Formatting Decimal Places

```python
value = 12.5678

print(f"{value:.2f}")
```

Output:

```text
12.57
```

## 24.5 Important Note

Floating-point calculations can show small representation differences.

For example:

```python
print(0.1 + 0.2)
```

The output may contain a small difference from the expected decimal expression.

For exact financial decimal arithmetic, explore Python's `decimal` module.

---

# 25. Working with Boolean Values

Boolean values represent two states:

```python
True
False
```

They are useful for decisions and conditions.

## 25.1 Boolean Output

```python
is_student = True

print(is_student)
```

## 25.2 Boolean Input

An input prompt returns text.

The program should explicitly interpret textual choices.

```python
answer = input("Are you a student? ").strip().lower()

if answer in ("yes", "y"):
    is_student = True
elif answer in ("no", "n"):
    is_student = False
else:
    is_student = None

print("Student status:", is_student)
```

## 25.3 Important Rule

Calling:

```python
bool("False")
```

returns `True`.

It checks whether the string is empty.

It does not interpret the meaning of the word.

Explicit parsing is better when the application accepts English responses.

---

# 26. Working with Complex Numbers

Python supports complex numbers.

Example:

```python
number = 2 + 3j

print(number)
```

Output:

```text
(2+3j)
```

## 26.1 Complex Input

```python
number = complex(input("Enter a complex number: "))

print(number)
```

Example input:

```text
2+3j
```

## 26.2 Accessing Components

```python
number = 2 + 3j

print(number.real)
print(number.imag)
```

## 26.3 Common Applications

Complex numbers are used in some areas of:

- Mathematics.
- Engineering.
- Signal processing.
- Electrical analysis.
- Scientific computing.

Complex-number input is included here to introduce another Python numeric type.

---

# 27. Input Conversion

Input conversion changes received input into a suitable data type.

The `input()` function returns a string.

When the program needs another type, explicit conversion may be required.

Example:

```python
age = int(input("Enter your age: "))
```

The expression first collects text and then converts it into an integer.

## 27.1 General Pattern

```python
converted_value = target_type(input("Enter value: "))
```

## 27.2 Separate Conversion

```python
raw_value = input("Enter value: ")

converted_value = int(raw_value)
```

Keeping the raw and converted values separate may make debugging easier.

## 27.3 Conversion Is Not Validation

A value can be converted successfully and still be unacceptable.

For example:

```python
age = int("-5")
```

The conversion succeeds.

An application may still reject a negative age.

---

# 28. Type Conversion Functions

The main conversion functions covered in this section are listed below.

| Function | Resulting type |
|---|---|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |
| `complex()` | Complex |

## 28.1 Integer

```python
value = int("20")
```

## 28.2 Float

```python
value = float("20.5")
```

## 28.3 String

```python
value = str(20)
```

## 28.4 Boolean

```python
value = bool(1)
```

## 28.5 Complex

```python
value = complex("2+3j")
```

## 28.6 Invalid Conversion

A conversion function may raise an exception when the provided value is not supported.

Example:

```python
int("hello")
```

This raises `ValueError`.

---

# 29. Integer Conversion

Use `int()` to convert suitable values into integers.

## Syntax

```python
int(value)
```

## Example

```python
number = int("100")

print(number)
```

Output:

```text
100
```

## Negative Number

```python
number = int("-25")

print(number)
```

Output:

```text
-25
```

## Float to Integer

```python
number = int(12.9)

print(number)
```

Output:

```text
12
```

`int()` truncates floating-point values toward zero.

It does not perform ordinary rounding.

## Invalid Text

```python
int("hello")
```

This raises `ValueError`.

---

# 30. Float Conversion

Use `float()` to convert suitable values into floating-point numbers.

## Syntax

```python
float(value)
```

## Example

```python
price = float("99.50")

print(price)
```

Output:

```text
99.5
```

## Integer Text

```python
number = float("20")

print(number)
```

Output:

```text
20.0
```

## Negative Decimal

```python
temperature = float("-5.5")

print(temperature)
```

Output:

```text
-5.5
```

## Invalid Text

```python
float("hello")
```

This raises `ValueError`.

---

# 31. String Conversion

Use `str()` to produce a string representation of a value.

## Example

```python
number = 100

text_value = str(number)

print(text_value)
print(type(text_value))
```

Output:

```text
100
<class 'str'>
```

## Use in a Message

```python
age = 20

message = "Age: " + str(age)

print(message)
```

Output:

```text
Age: 20
```

F-strings are another useful way of formatting output.

```python
print(f"Age: {age}")
```

---

# 32. Boolean Conversion

Use `bool()` to convert a value into a truth value.

## Example

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
```

Output:

```text
False
True
False
True
```

## Important Rule

Nonempty strings are truthy.

Therefore:

```python
bool("False")
```

returns:

```text
True
```

For yes/no questions, compare accepted words explicitly instead.

---

# 33. Complex Number Conversion

Use `complex()` to convert suitable values into complex numbers.

## Example

```python
number = complex("2+3j")

print(number)
```

Output:

```text
(2+3j)
```

## Components

```python
number = complex("2+3j")

print(number.real)
print(number.imag)
```

Output:

```text
2.0
3.0
```

---

# 34. Reading Multiple Inputs

A program can collect multiple values separately.

```python
first = input("Enter first value: ")
second = input("Enter second value: ")
third = input("Enter third value: ")
```

It can also collect multiple values on one line.

```python
values = input("Enter values: ").split()

print(values)
```

Input:

```text
10 20 30
```

Output:

```text
['10', '20', '30']
```

The values are still strings.

They need conversion if numeric operations are required.

---

# 35. Splitting Input Values

The `split()` method divides a string into separate parts.

## Space-Separated Input

```python
values = input("Enter numbers: ").split()
```

Input:

```text
10 20 30
```

Result:

```python
["10", "20", "30"]
```

## Comma-Separated Input

```python
values = input("Enter numbers: ").split(",")
```

Input:

```text
10,20,30
```

Result:

```python
["10", "20", "30"]
```

## Convert Values

```python
values = input("Enter numbers: ").split()

numbers = [int(value) for value in values]

print(numbers)
```

This produces a list of integers when all supplied items are valid integer text.

---

# 36. Handling User Input

A user may provide unexpected information.

A program should be designed to handle this possibility.

## 36.1 Common Input Problems

- Empty input.
- Incorrect numeric text.
- Unexpected spaces.
- Unsupported menu choices.
- Too few values.
- Too many values.
- Invalid Boolean responses.
- Numbers outside the permitted range.

## 36.2 Basic Handling

```python
value = input("Enter a value: ").strip()

if not value:
    print("Input cannot be empty.")
else:
    print("Received:", value)
```

## 36.3 Validate Before Processing

A program should check whether received information is suitable before using it.

For example, an empty name should be rejected when a name is required.

A numeric value should be converted before arithmetic.

A score should be checked against the permitted range.

---

# 37. Input Validation

Input validation checks whether received information satisfies the program's requirements.

## 37.1 Empty Input

```python
name = input("Enter name: ").strip()

if not name:
    print("Name is required.")
else:
    print("Hello,", name)
```

## 37.2 Numeric Validation

```python
try:
    age = int(input("Enter age: "))
    print("Age:", age)
except ValueError:
    print("Please enter a valid integer.")
```

## 37.3 Range Validation

```python
try:
    marks = float(input("Enter marks: "))

    if 0 <= marks <= 100:
        print("Valid marks")
    else:
        print("Marks must be between 0 and 100.")
except ValueError:
    print("Please enter a valid number.")
```

## 37.4 Validation Rules

The rules depend on the program.

A negative temperature may be valid.

A negative shopping quantity may not be valid.

Validation should reflect the application's actual requirements.

---

# 38. Error Handling

Errors can occur when a program receives or processes unexpected data.

For input and output programs, common problems include invalid conversion and incompatible operations.

## 38.1 Example of a Conversion Error

```python
number = int("hello")
```

This raises `ValueError`.

## 38.2 Example of an Incompatible Operation

```python
result = "10" + 5
```

This raises `TypeError`.

## 38.3 Why Handle Errors?

Error handling helps a program:

- Avoid abrupt failure for expected invalid input.
- Display useful messages.
- Allow users to correct mistakes.
- Maintain a predictable interaction flow.
- Separate expected input errors from unrelated programming errors.

## 38.4 Use Specific Exceptions

For integer conversion, `ValueError` is commonly the relevant exception.

```python
try:
    number = int(input("Enter integer: "))
except ValueError:
    print("Invalid integer.")
```

---

# 39. Exception Handling

Python uses `try` and `except` to handle exceptions.

## 39.1 General Structure

```python
try:
    # Code that may fail
    pass

except ValueError:
    # Handle invalid values
    pass
```

## 39.2 Example

```python
try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid integer.")
```

## 39.3 Retry Input

```python
while True:
    try:
        age = int(input("Enter age: "))
        break

    except ValueError:
        print("Invalid input. Try again.")

print("Accepted age:", age)
```

This program repeats the prompt until an integer can be converted.

## 39.4 Keep Exception Handling Specific

Catch expected errors whenever possible.

Avoid using overly broad exception handling to hide unrelated programming problems.

---

# 40. Formatting Output

Output formatting determines how information is presented.

Clear formatting can make a program easier to understand.

## 40.1 Basic Output

```python
print("Name:", "Amaan")
```

## 40.2 Multiple Lines

```python
print("Name: Amaan")
print("Course: Computer Science")
print("Language: Python")
```

## 40.3 Formatted Output

```python
name = "Amaan"
marks = 85

print(f"{name} scored {marks} marks.")
```

## 40.4 Decimal Formatting

```python
price = 99.5

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 99.50
```

## 40.5 Output Headings

```python
print("STUDENT REPORT")
print("----------------")
```

A heading can make a larger result easier to read.

---

# 41. The `sep` Parameter

The `sep` parameter controls the separator inserted between objects displayed by `print()`.

## Default Behavior

```python
print("A", "B", "C")
```

Output:

```text
A B C
```

The default separator is a space.

## Custom Separator

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

## Another Example

```python
print("2026", "10", "31", sep="/")
```

Output:

```text
2026/10/31
```

## Important Point

The separator is inserted between the printed objects.

It is not automatically appended after the final object.

---

# 42. The `end` Parameter

The `end` parameter controls what `print()` displays after the objects.

The default ending is a newline.

## Default

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

## Custom Ending

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

## Another Example

```python
print("Loading", end="...")
print("Complete")
```

Output:

```text
Loading...Complete
```

## Important Point

`end` changes the ending of a print operation.

It is useful when multiple print statements need to appear on the same line.

---

# 43. Escape Sequences

Escape sequences are special character combinations used inside strings.

They begin with a backslash.

Common escape sequences include:

| Escape sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\\` | Backslash |
| `\'` | Single quotation mark |
| `\"` | Double quotation mark |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |
| `\v` | Vertical tab |

## 43.1 New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

## 43.2 Tab

```python
print("Name\tAge")
```

Output:

```text
Name    Age
```

The exact visual spacing depends on the terminal.

## 43.3 Backslash

```python
print("C:\\Users\\Student")
```

## 43.4 Quotation Marks

```python
print("He said, \"Hello!\"")
```

## 43.5 Why Are Escape Sequences Useful?

They help organize output.

They are useful for:

- New lines.
- Simple tables.
- Messages containing quotes.
- Displaying paths.
- Formatting reports.

---

# 44. New Line and Tab Formatting

New-line and tab characters are especially useful when displaying structured information.

## 44.1 New-Line Example

```python
print("Student")
print("Marks")
print("Result")
```

## 44.2 Using `\n`

```python
print("Student\nMarks\nResult")
```

## 44.3 Using `\t`

```python
print("Name\tAge\tCourse")
print("Amaan\t20\tCSE")
```

## 44.4 Formatting a Simple Report

```python
print("STUDENT REPORT")
print("--------------------")
print("Name:\tAmaan")
print("Course:\tCSE")
print("Marks:\t85")
```

The output is easier to scan because related values are displayed in an organized format.

---

# 45. F-Strings

F-strings provide a readable way to insert values and expressions into strings.

They are written with an `f` or `F` prefix.

## 45.1 Basic Syntax

```python
f"Text {expression}"
```

## 45.2 Example

```python
name = "Amaan"

print(f"Hello, {name}")
```

Output:

```text
Hello, Amaan
```

## 45.3 Multiple Variables

```python
name = "Amaan"
age = 20
course = "CSE"

print(f"My name is {name}.")
print(f"My age is {age}.")
print(f"My course is {course}.")
```

## 45.4 Expressions Inside F-Strings

```python
first = 10
second = 20

print(f"Sum: {first + second}")
```

Output:

```text
Sum: 30
```

## 45.5 Decimal Formatting

```python
price = 99.5

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 99.50
```

## 45.6 Why Use F-Strings?

They make formatted messages easy to read.

They are often clearer than joining multiple strings with `+`.

---

# 46. String Concatenation

String concatenation means joining strings together.

The `+` operator can combine string values.

## 46.1 Basic Example

```python
first = "Hello"
second = "World"

result = first + second

print(result)
```

Output:

```text
HelloWorld
```

## 46.2 Add a Space

```python
first = "Hello"
second = "World"

result = first + " " + second

print(result)
```

Output:

```text
Hello World
```

## 46.3 Combine User Inputs

```python
first_name = input("First name: ")
last_name = input("Last name: ")

full_name = first_name + " " + last_name

print(full_name)
```

## 46.4 Concatenation Is Not Numeric Addition

```python
print("10" + "20")
```

Output:

```text
1020
```

By contrast:

```python
print(10 + 20)
```

Output:

```text
30
```

The operand types determine the behavior.

---

# 47. Displaying Different Data Types

Python's `print()` function can display values of different types.

## String

```python
name = "Amaan"

print(name)
```

## Integer

```python
age = 20

print(age)
```

## Float

```python
price = 99.5

print(price)
```

## Boolean

```python
is_student = True

print(is_student)
```

## Complex

```python
number = 2 + 3j

print(number)
```

## Multiple Types Together

```python
name = "Amaan"
age = 20
marks = 85.5
is_student = True

print(name, age, marks, is_student)
```

## Using an F-String

```python
print(
    f"Name: {name}, "
    f"Age: {age}, "
    f"Marks: {marks}, "
    f"Student: {is_student}"
)
```

---

# 48. Displaying Calculated Results

A program commonly uses input to calculate a result and output to display it.

## Addition

```python
first = int(input("First number: "))
second = int(input("Second number: "))

result = first + second

print("Sum:", result)
```

## Subtraction

```python
first = int(input("First number: "))
second = int(input("Second number: "))

result = first - second

print("Difference:", result)
```

## Multiplication

```python
first = int(input("First number: "))
second = int(input("Second number: "))

result = first * second

print("Product:", result)
```

## Division

```python
first = float(input("First number: "))
second = float(input("Second number: "))

if second != 0:
    result = first / second
    print("Result:", result)
else:
    print("Division by zero is not allowed.")
```

## Average

```python
first = float(input("First mark: "))
second = float(input("Second mark: "))
third = float(input("Third mark: "))

average = (first + second + third) / 3

print("Average:", average)
```

These examples combine input, conversion, processing, and output.

---

# 49. Input and Output Examples

This section combines basic concepts into small examples.

## Example 1: Display a Message

```python
print("Welcome to Python")
```

## Example 2: Read a Name

```python
name = input("Enter name: ")

print(name)
```

## Example 3: Read a City

```python
city = input("Enter city: ")

print("City:", city)
```

## Example 4: Read an Age

```python
age = int(input("Enter age: "))

print("Age:", age)
```

## Example 5: Read a Decimal Value

```python
price = float(input("Enter price: "))

print("Price:", price)
```

## Example 6: Display Multiple Values

```python
name = "Amaan"
age = 20

print("Name:", name, "Age:", age)
```

## Example 7: Formatted Output

```python
name = "Amaan"
course = "CSE"

print(f"{name} studies {course}.")
```

## Example 8: Add Two Numbers

```python
first = int(input("First: "))
second = int(input("Second: "))

print("Sum:", first + second)
```

## Example 9: Read Multiple Values

```python
values = input("Enter values: ").split()

print(values)
```

## Example 10: Convert Multiple Values

```python
values = input("Enter integers: ").split()

numbers = [int(value) for value in values]

print(numbers)
```

## Example 11: Display a Report

```python
name = input("Enter name: ")
course = input("Enter course: ")

print("STUDENT REPORT")
print("--------------------")
print(f"Name: {name}")
print(f"Course: {course}")
```

## Example 12: Validate an Integer

```python
try:
    number = int(input("Enter an integer: "))
    print("Accepted:", number)
except ValueError:
    print("Invalid integer.")
```

---

# 50. Complete Input and Output Workflow

The following workflow explains how to create an interactive program.

## Step 1: Understand the Requirement

Determine what information the program needs.

Example:

A program needs a student's name and marks.

## Step 2: Identify the Input

Determine which values must be collected.

```python
name
marks
```

## Step 3: Select Suitable Data Types

A name requires text.

Marks may require a numeric type.

## Step 4: Collect the Input

```python
name = input("Enter name: ")
marks_text = input("Enter marks: ")
```

## Step 5: Convert When Required

```python
marks = float(marks_text)
```

## Step 6: Validate

Check whether the marks are in the permitted range.

```python
if 0 <= marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")
```

## Step 7: Process

Perform the required operation.

## Step 8: Display the Result

```python
print(f"Student: {name}")
print(f"Marks: {marks}")
```

## Step 9: Test Different Values

Test:

- Valid text.
- Empty text.
- Valid numbers.
- Invalid numbers.
- Boundary values.
- Out-of-range values.

## Step 10: Improve the Program

Use meaningful variable names, appropriate error handling, and readable output formatting.

---

# 51. Combined Practical Examples

The following programs combine multiple topics from this section.

## Program 1: Personal Information

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nPERSONAL INFORMATION")
print("--------------------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

Concepts used:

- Input.
- Variables.
- String.
- Integer conversion.
- Output.
- F-strings.

## Program 2: Simple Calculator

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("\nCALCULATOR")
print("----------")
print("Addition:", first + second)
print("Subtraction:", first - second)
print("Multiplication:", first * second)

if second != 0:
    print("Division:", first / second)
else:
    print("Division: Not possible")
```

Concepts used:

- User input.
- Float conversion.
- Arithmetic operators.
- Conditional statement.
- Output formatting.

## Program 3: Student Marks Calculator

```python
name = input("Enter student name: ")

marks_1 = float(input("Enter subject 1 marks: "))
marks_2 = float(input("Enter subject 2 marks: "))
marks_3 = float(input("Enter subject 3 marks: "))

total = marks_1 + marks_2 + marks_3
average = total / 3

print("\nSTUDENT RESULT")
print("--------------------")
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
```

Concepts used:

- Multiple inputs.
- Float conversion.
- Arithmetic.
- Output formatting.

This example assumes valid marks. Range validation and error handling can be added as an improvement.

## Program 4: Product Bill

```python
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\nPRODUCT BILL")
print("--------------------")
print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")
```

Concepts used:

- String input.
- Numeric conversion.
- Multiplication.
- Formatted output.

## Program 5: Temperature Converter

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Fahrenheit: {fahrenheit:.2f}")
```

Concepts used:

- Float input.
- Conversion.
- Mathematical expressions.
- Output formatting.

## Program 6: Yes or No Response

```python
answer = input("Do you want to continue? ").strip().lower()

if answer in ("yes", "y"):
    print("You selected Yes.")
elif answer in ("no", "n"):
    print("You selected No.")
else:
    print("Invalid response.")
```

Concepts used:

- User input.
- String methods.
- Conditional statements.
- Explicit response parsing.

## Program 7: Multiple Number Sum

```python
raw_values = input("Enter numbers separated by spaces: ").split()

try:
    numbers = [int(value) for value in raw_values]

    if numbers:
        print("Numbers:", numbers)
        print("Sum:", sum(numbers))
    else:
        print("Please enter at least one number.")

except ValueError:
    print("One or more values are not valid integers.")
```

Concepts used:

- Multiple input.
- String splitting.
- List comprehension.
- Integer conversion.
- Exception handling.
- Output.

## Program 8: Simple Student Profile

```python
name = input("Enter name: ").strip()
course = input("Enter course: ").strip()
college = input("Enter college: ").strip()

print("\nSTUDENT PROFILE")
print("====================")
print(f"Name: {name}")
print(f"Course: {course}")
print(f"College: {college}")
print("====================")
```

Concepts used:

- Text input.
- String methods.
- Variables.
- Formatted output.

---

# 52. Solved Practical Programs

This section provides additional practical programs that combine the concepts from the four topic folders.

## Solved Program 1: Print a Welcome Message

```python
print("Welcome to Python Programming")
print("Start Learning Today")
```

Explanation:

The program displays two messages.

It uses the `print()` function.

## Solved Program 2: Read and Display a Name

```python
name = input("Enter your name: ")

print("Hello,", name)
```

Explanation:

The program receives a name and displays it.

## Solved Program 3: Read and Display an Age

```python
age = int(input("Enter your age: "))

print("Your age is:", age)
```

Explanation:

The input is converted into an integer.

## Solved Program 4: Add Two Integers

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Sum:", first + second)
```

Explanation:

Both values are converted before arithmetic.

## Solved Program 5: Calculate a Product

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Product:", first * second)
```

Explanation:

The multiplication operator calculates the product.

## Solved Program 6: Display a Student Profile

```python
name = input("Enter name: ")
roll_number = input("Enter roll number: ")
course = input("Enter course: ")

print("\nSTUDENT PROFILE")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Course: {course}")
```

Explanation:

The program collects multiple text values and displays them in an organized format.

## Solved Program 7: Calculate Average Marks

```python
mark_1 = float(input("Enter first mark: "))
mark_2 = float(input("Enter second mark: "))
mark_3 = float(input("Enter third mark: "))

average = (mark_1 + mark_2 + mark_3) / 3

print(f"Average: {average:.2f}")
```

Explanation:

The program converts marks into floating-point numbers before calculating the average.

## Solved Program 8: Display a Formatted Bill

```python
item = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\nBILL")
print("----------------")
print(f"Item: {item}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")
```

Explanation:

The program collects product details and calculates the total.

## Solved Program 9: Convert an Integer to a String

```python
number = 250

text_value = str(number)

print(text_value)
print(type(text_value))
```

Explanation:

The `str()` function produces a string representation of the integer.

## Solved Program 10: Handle Invalid Integer Input

```python
try:
    number = int(input("Enter an integer: "))
    print("Accepted:", number)

except ValueError:
    print("Please enter a valid integer.")
```

Explanation:

The program handles invalid integer input using `ValueError`.

---

# 53. Common Mistakes

Input and output are easy to learn, but several mistakes are common among beginners.

## Mistake 1: Forgetting That `input()` Returns a String

Example:

```python
age = input("Enter age: ")
```

The value is text.

Use conversion when an integer is required:

```python
age = int(input("Enter age: "))
```

## Mistake 2: Adding Strings Instead of Numbers

Example:

```python
first = input("First: ")
second = input("Second: ")

print(first + second)
```

Input:

```text
10
20
```

Output:

```text
1020
```

Correct approach:

```python
first = int(input("First: "))
second = int(input("Second: "))

print(first + second)
```

Output:

```text
30
```

## Mistake 3: Using `int()` for Decimal Text

Incorrect:

```python
number = int("12.5")
```

This raises `ValueError`.

Use `float()` when decimal input is required.

## Mistake 4: Forgetting Quotes Around Text

Incorrect:

```python
print(Hello)
```

Python treats `Hello` as an identifier.

Correct:

```python
print("Hello")
```

## Mistake 5: Forgetting Parentheses

Incorrect:

```python
print "Hello"
```

Correct in Python 3:

```python
print("Hello")
```

## Mistake 6: Incorrect String Concatenation

An integer cannot normally be concatenated directly with a string using `+`.

Incorrect:

```python
age = 20

print("Age: " + age)
```

Correct:

```python
print("Age:", age)
```

Or:

```python
print(f"Age: {age}")
```

## Mistake 7: Using `bool()` to Interpret Words

Incorrect assumption:

```python
bool("No") == False
```

The expression evaluates to `True`.

Use explicit parsing.

## Mistake 8: Ignoring Invalid Input

Direct conversion can raise an exception.

Use suitable exception handling when input may be invalid.

## Mistake 9: Forgetting Range Validation

Successful conversion does not prove that a value is acceptable.

Check application-specific limits.

## Mistake 10: Poor Output Formatting

A program should make its results understandable.

Use labels, headings, and suitable formatting.

## Mistake 11: Using Incorrect Escape Sequences

Use escape sequences carefully.

For example:

```python
print("Hello\nWorld")
```

displays two lines.

## Mistake 12: Confusing `sep` and `end`

`sep` controls the separator between objects.

`end` controls what is printed after the objects.

## Mistake 13: Forgetting to Split Multiple Inputs

A space-separated string can be divided using `split()`.

## Mistake 14: Accessing Missing Input Elements

Always check the number of supplied values before accessing positions that may not exist.

## Mistake 15: Catching Every Exception Unnecessarily

Use specific exception handlers when possible.

---

# 54. Debugging Techniques

Debugging helps identify and correct problems in a program.

Input and output programs can be debugged systematically.

## Step 1: Read the Error Message

Python often identifies the line where the error occurred.

Read the full message.

## Step 2: Check the Original Input

```python
raw_value = input("Enter value: ")

print(repr(raw_value))
```

This helps reveal empty strings and surrounding whitespace.

## Step 3: Check the Data Type

```python
print(type(raw_value))
```

This confirms the type of the stored value.

## Step 4: Test Conversion Separately

```python
number = int(raw_value)

print(number)
```

Testing conversion independently helps isolate conversion errors.

## Step 5: Check the Output

Compare the actual output with the expected output.

## Step 6: Test Different Values

Use:

- Valid text.
- Empty text.
- Positive numbers.
- Negative numbers.
- Decimal values.
- Invalid values.
- Whitespace.
- Boundary values.

## Step 7: Check Variables

Use meaningful names.

Confirm that every variable contains the expected value at the time it is used.

## Step 8: Check the Processing Logic

A program may receive and convert input correctly but still calculate an incorrect result.

Verify the arithmetic and conditions separately.

---

# 55. Testing Input and Output Programs

Testing verifies that a program behaves as expected.

It is important to test both successful and unsuccessful inputs.

## 55.1 Basic Input Tests

| Test | Input | Expected behavior |
|---|---|---|
| Name | `Amaan` | Store and display name |
| City | `Nagpur` | Store and display city |
| Course | `CSE` | Store and display course |
| Empty name | Empty line | Check required-field rule |
| Spaces | ` Amaan ` | Apply whitespace rule if intended |

## 55.2 Integer Tests

| Input | Expected behavior |
|---|---|
| `0` | Valid integer |
| `10` | Valid integer |
| `-10` | Valid integer |
| `1000` | Valid integer |
| `hello` | Conversion failure |
| `12.5` | Conversion failure with `int()` |
| Empty text | Conversion failure |

## 55.3 Float Tests

| Input | Expected behavior |
|---|---|
| `10.5` | Valid float |
| `10` | Valid float |
| `-2.5` | Valid float |
| `0.0` | Valid float |
| `hello` | Conversion failure |
| `12.3.4` | Conversion failure |
| Empty text | Conversion failure |

## 55.4 Boolean Text Tests

| Input | Expected parser result |
|---|---|
| `yes` | True |
| `YES` | True |
| `y` | True |
| `no` | False |
| `NO` | False |
| `n` | False |
| `maybe` | Invalid |
| Empty text | Invalid unless explicitly supported |

These expected results assume a parser that accepts the listed values.

## 55.5 Binary Tests

| Binary input | Decimal result |
|---|---:|
| `0` | 0 |
| `1` | 1 |
| `10` | 2 |
| `1010` | 10 |
| `1111` | 15 |
| `10000` | 16 |
| `102` | Invalid |
| Empty text | Invalid |

## 55.6 Output Tests

Check whether:

- The correct values are displayed.
- The output labels are correct.
- The spacing is appropriate.
- Newlines appear where expected.
- Decimal formatting is correct.
- No unrelated values are printed.

---

# 56. Boundary Testing

Boundary testing is the process of testing values at and around permitted limits.

For example, suppose marks must be between `0` and `100`.

The following values should be tested:

| Value | Expected result |
|---:|---|
| -1 | Reject |
| 0 | Accept |
| 1 | Accept |
| 50 | Accept |
| 99 | Accept |
| 100 | Accept |
| 101 | Reject |

Example:

```python
try:
    marks = float(input("Enter marks: "))

    if 0 <= marks <= 100:
        print("Valid marks")
    else:
        print("Marks must be between 0 and 100.")

except ValueError:
    print("Invalid number.")
```

Boundary tests help ensure that the program uses the correct comparison operators.

---

# 57. Input Validation Test Cases

Validation tests help confirm that the application handles different user responses correctly.

## Test Case 1: Valid Name

Input:

```text
Amaan
```

Expected:

The program accepts the name.

## Test Case 2: Empty Name

Input:

```text

```

Expected:

The program rejects the value if the field is required.

## Test Case 3: Valid Integer

Input:

```text
25
```

Expected:

The integer conversion succeeds.

## Test Case 4: Invalid Integer

Input:

```text
twenty
```

Expected:

The program handles the conversion error.

## Test Case 5: Valid Decimal

Input:

```text
25.5
```

Expected:

The float conversion succeeds.

## Test Case 6: Invalid Decimal

Input:

```text
25.5.5
```

Expected:

The program handles the conversion error.

## Test Case 7: Valid Yes Response

Input:

```text
yes
```

Expected:

A suitable Boolean parser returns `True`.

## Test Case 8: Valid No Response

Input:

```text
no
```

Expected:

A suitable Boolean parser returns `False`.

## Test Case 9: Unsupported Response

Input:

```text
maybe
```

Expected:

The parser rejects the response or requests another answer.

## Test Case 10: Out-of-Range Number

Input:

```text
150
```

Expected:

A program requiring a value from 0 to 100 rejects it.

---

# 58. Output Verification

Output verification checks whether the program displays the correct information.

## 58.1 Check the Displayed Value

Confirm that the displayed value matches the expected result.

## 58.2 Check the Data

Confirm that the program processes the correct variable.

## 58.3 Check Formatting

Confirm that:

- Headings are readable.
- Labels are clear.
- Spacing is appropriate.
- Decimal places match requirements.
- Newlines appear correctly.

## 58.4 Check Special Characters

When strings contain escape sequences, verify the displayed result.

## 58.5 Check Different Inputs

Use multiple test cases.

Do not verify a program using only one input value.

---

# 59. Best Practices

Follow these practices when building Python input and output programs.

## 59.1 Use Meaningful Prompts

Prefer:

```python
age = input("Enter your age: ")
```

over:

```python
age = input("Value: ")
```

The prompt should explain what the user needs to enter.

## 59.2 Use Meaningful Variable Names

Prefer:

```python
student_name
```

over:

```python
x
```

Meaningful names make programs easier to read.

## 59.3 Choose Appropriate Data Types

Use types according to the information being stored.

## 59.4 Convert Input When Necessary

Remember that `input()` returns a string.

Convert values before using operations that require another type.

## 59.5 Validate User Responses

Check whether input satisfies the program's requirements.

## 59.6 Handle Expected Errors

Use suitable exception handling for conversion operations that may fail.

## 59.7 Display Helpful Messages

A program should explain what happened.

## 59.8 Format Output Clearly

Use headings, labels, separators, and f-strings where appropriate.

## 59.9 Keep Code Organized

Separate input collection, processing, and output when doing so improves readability.

## 59.10 Avoid Unnecessary Repetition

Reusable helper functions can centralize common input-handling tasks.

## 59.11 Test Invalid Inputs

A program should be tested with more than ideal values.

## 59.12 Keep Examples Focused

Each example should have a clear learning purpose.

## 59.13 Understand Before Copying

Try to understand each statement and why it is used.

## 59.14 Practice Regularly

Write the examples yourself and experiment with different values.

---

# 60. Code Readability

Readable code is easier to understand, test, and maintain.

## 60.1 Use Indentation

Python uses indentation to define code blocks.

Example:

```python
if True:
    print("Correct indentation")
```

## 60.2 Use Blank Lines

Blank lines help visually separate logical sections.

## 60.3 Use Comments

Comments can explain the purpose of a statement.

```python
# Read the user's name
name = input("Enter your name: ")
```

## 60.4 Avoid Unclear Names

Prefer:

```python
total_marks
```

over:

```python
tm
```

when clarity is important.

## 60.5 Keep Output Consistent

Use consistent labels and formatting in related programs.

---

# 61. Naming Conventions

Python variable names should be meaningful and follow standard naming conventions.

## 61.1 Use Descriptive Names

Good examples:

```python
student_name
total_marks
product_price
user_age
```

## 61.2 Use Snake Case

Python commonly uses snake_case for variables and functions.

Example:

```python
first_name = "Amaan"
```

## 61.3 Avoid Reserved Keywords

Do not use Python keywords as variable names.

Examples of keywords include:

- `if`
- `else`
- `for`
- `while`
- `class`
- `def`
- `return`
- `True`
- `False`

## 61.4 Choose Names According to Meaning

A value storing raw text can be named:

```python
raw_age
```

A converted integer can be named:

```python
age
```

This can make conversion code easier to understand.

---

# 62. Program Structure

A clear interactive program commonly follows this structure:

1. Display instructions.
2. Collect information.
3. Convert values when required.
4. Validate input.
5. Process information.
6. Display results.

Example:

```python
# 1. Display instructions
print("Student Marks Calculator")

# 2. Collect information
name = input("Enter student name: ")

# 3. Convert values
marks = float(input("Enter marks: "))

# 4. Validate input
if 0 <= marks <= 100:

    # 5. Process information
    result = "Valid marks"

    # 6. Display result
    print(f"Student: {name}")
    print(result)

else:
    print("Marks must be between 0 and 100.")
```

A larger program can separate these operations into functions.

The exact structure should suit the size and requirements of the application.

---

# 63. Real-Life Applications

Input and output appear in almost every software application.

## 63.1 Student Management System

Input:

- Student name.
- Roll number.
- Course.
- Marks.

Processing:

- Store student details.
- Calculate totals.
- Calculate averages.
- Validate records.

Output:

- Student profile.
- Result.
- Academic report.

## 63.2 Calculator

Input:

- First number.
- Second number.
- Operation.

Processing:

- Perform arithmetic.

Output:

- Calculation result.

## 63.3 Shopping Application

Input:

- Product.
- Price.
- Quantity.

Processing:

- Calculate the bill.
- Apply any required pricing rules.

Output:

- Total amount.
- Bill summary.

## 63.4 Login System

Input:

- Username.
- Password.

Processing:

- Check credentials according to the system's authentication rules.

Output:

- Success message.
- Error message.

A real authentication system requires additional security protections beyond basic input and output.

## 63.5 Survey Application

Input:

- User responses.

Processing:

- Interpret answers.
- Count responses.
- Calculate totals.

Output:

- Survey summary.

## 63.6 Temperature Converter

Input:

- Temperature.

Processing:

- Apply the conversion formula.

Output:

- Converted temperature.

## 63.7 Attendance System

Input:

- Student details.
- Attendance response.

Processing:

- Record attendance.

Output:

- Attendance status.

## 63.8 Banking Application

Input:

- Transaction amount.
- Account selection.
- Operation.

Processing:

- Validate the transaction.
- Apply account rules.
- Update records.

Output:

- Transaction status.
- Balance information.

Real banking applications require much more than basic input validation.

---

# 64. Mini Project Ideas

Complete these projects after studying all four topic folders.

## Project 1: Personal Information Form

Requirements:

- Ask the user for a name.
- Ask for age.
- Ask for city.
- Store the information.
- Display a formatted profile.
- Validate required text fields.

Skills practiced:

- Input.
- Variables.
- Data types.
- Integer conversion.
- Output formatting.

## Project 2: Simple Calculator

Requirements:

- Ask for two numbers.
- Convert both values.
- Calculate addition.
- Calculate subtraction.
- Calculate multiplication.
- Calculate division.
- Handle division by zero.
- Display the results.

Skills practiced:

- User input.
- Numeric conversion.
- Operators.
- Conditional logic.
- Output.

## Project 3: Student Marks Calculator

Requirements:

- Ask for a student name.
- Collect marks for three subjects.
- Convert marks into numeric values.
- Validate the permitted range.
- Calculate total marks.
- Calculate average.
- Display a formatted report.

Skills practiced:

- Input.
- Conversion.
- Validation.
- Arithmetic.
- Formatted output.

## Project 4: Shopping Bill Generator

Requirements:

- Ask for the product name.
- Ask for its price.
- Ask for quantity.
- Convert the numeric input.
- Calculate the total.
- Display a bill.

Skills practiced:

- Input.
- Float conversion.
- Integer conversion.
- Multiplication.
- Output formatting.

## Project 5: Temperature Converter

Requirements:

- Ask for a temperature in Celsius.
- Convert the input into a float.
- Calculate Fahrenheit.
- Display the result.
- Format the decimal output.

Formula:

\[
F = \frac{9}{5}C + 32
\]

## Project 6: Yes/No Survey

Requirements:

- Ask a question.
- Accept yes/no responses.
- Normalize text.
- Interpret the answer.
- Reject unsupported responses.
- Display the result.

Skills practiced:

- User input.
- String methods.
- Boolean parsing.
- Conditional statements.

## Project 7: Multiple Number Calculator

Requirements:

- Read several numbers.
- Split the input.
- Convert values.
- Calculate sum.
- Calculate average.
- Handle invalid values.
- Display results.

Skills practiced:

- Multiple inputs.
- Lists.
- Conversion.
- Exception handling.

## Project 8: Student Registration Form

Requirements:

- Collect student name.
- Collect roll number.
- Collect course.
- Collect city.
- Validate required information.
- Display the submitted information.

Skills practiced:

- Interactive input.
- Strings.
- Variables.
- Validation.
- Output formatting.

---

# 65. Practice Questions

Attempt these questions after completing the four topic folders.

## Basic Input Questions

1. What is input in programming?
2. Which Python function is commonly used to receive keyboard input?
3. What does the `input()` function return?
4. How can user input be stored in a variable?
5. What happens when the user presses Enter without typing anything?
6. Can `input()` receive more than one line in a single call?
7. Why are input prompts useful?
8. What is the difference between input and user input?
9. What does the `strip()` method do?
10. How can a program read a name from the user?

## Basic Output Questions

11. What is output in programming?
12. Which function is used to display output in Python?
13. How can multiple values be displayed?
14. What is the default separator used by `print()`?
15. What is the default ending used by `print()`?
16. What is the purpose of `sep`?
17. What is the purpose of `end`?
18. What is an escape sequence?
19. What does `\n` represent?
20. What does `\t` represent?

## User Input Questions

21. What is user interaction?
22. Why are interactive programs useful?
23. How can multiple values be collected from a user?
24. Why should user input be stored in variables?
25. What is a prompt?
26. What is input validation?
27. Why should empty input sometimes be rejected?
28. What is a menu-driven program?
29. Why are clear user messages important?
30. Give two examples of programs that use user input.

## Input Conversion Questions

31. Why is input conversion necessary?
32. What does `int()` do?
33. What does `float()` do?
34. What does `str()` do?
35. What does `bool()` do?
36. What does `complex()` do?
37. Why does `int("12.5")` fail?
38. What does `int(12.9)` return?
39. Why is `bool("False")` true?
40. How can binary text be converted into an integer?

## Error Handling Questions

41. What is `ValueError`?
42. What is `TypeError`?
43. What is the purpose of `try`?
44. What is the purpose of `except`?
45. Why should invalid input be handled?
46. How can a program retry after invalid input?
47. What is the difference between conversion and validation?
48. Why should a conversion function not silently ignore invalid data?
49. What is boundary testing?
50. Why should user input be tested with different values?

---

# 66. Practical Challenges

Write the following programs independently.

## Challenge 1

Display your name, age, and course using `print()`.

## Challenge 2

Ask the user for their name and display a welcome message.

## Challenge 3

Ask the user for a city and display a formatted message.

## Challenge 4

Read two integers and display their sum.

## Challenge 5

Read two floating-point values and display their product.

## Challenge 6

Read a name and course and display them as a formatted student profile.

## Challenge 7

Read three marks and display their average.

## Challenge 8

Convert a numeric value into a string.

## Challenge 9

Read a yes/no answer and interpret it as a Boolean value.

## Challenge 10

Read comma-separated integers and convert them into a list.

## Challenge 11

Read binary text and convert it into a decimal number.

## Challenge 12

Create a program that accepts input until the user enters a valid integer.

## Challenge 13

Create a simple bill generator.

## Challenge 14

Create a formatted student report.

## Challenge 15

Create a calculator that handles division by zero and invalid numeric input.

---

# 67. Learning Roadmap

Follow this order when studying the section.

| Step | Folder | What to Learn |
|---|---|---|
| 1 | `01_input` | Understand how to receive information |
| 2 | `02_output` | Understand how to display information |
| 3 | `03_user_input` | Build interactive programs |
| 4 | `04_input_conversion` | Convert input into suitable data types |

## Step 1: Complete Input

Focus on:

- `input()`.
- Prompts.
- Variables.
- Returned strings.
- Empty input.

Practice reading names, cities, and other text.

## Step 2: Complete Output

Focus on:

- `print()`.
- Multiple values.
- `sep`.
- `end`.
- Escape sequences.
- Formatted strings.

Practice displaying information clearly.

## Step 3: Complete User Input

Focus on:

- User interaction.
- Multiple inputs.
- Storing responses.
- Combining input and output.
- Creating interactive examples.

Practice building simple forms and programs.

## Step 4: Complete Input Conversion

Focus on:

- `int()`.
- `float()`.
- `str()`.
- `bool()`.
- `complex()`.
- Lists.
- Exception handling.
- Validation.

Practice converting and processing numeric input safely.

## Step 5: Revise the Complete Section

After completing all four topics:

- Review the parent README.
- Revisit each child README.
- Run each Python file.
- Complete the solved exercises.
- Attempt the unsolved questions.
- Build at least one mini project.

---

# 68. Study Strategy

A structured approach makes learning easier.

## First Reading

Read the theory before running the code.

Understand why each function is being used.

## Code Practice

Type examples yourself.

Avoid relying only on copying and pasting.

## Experimentation

Change the input values.

Observe how the program behaves.

Try valid and invalid values.

## Debugging

When an error occurs:

1. Read the error message.
2. Identify the affected line.
3. Check the variable value.
4. Check the variable type.
5. Test the conversion separately.
6. Correct the problem.
7. Run the program again.

## Revision

After completing each topic:

- Review the important functions.
- Revise the examples.
- Explain the logic in your own words.
- Attempt the practice questions.

## Application

Combine the concepts in a small project.

Practical application improves understanding.

---

# 69. Revision Notes

Remember the following points while revising.

## Input

- Input means information received by a program.
- `input()` reads a line of text.
- `input()` returns a string.
- The result can be stored in a variable.
- A prompt helps the user understand what to enter.

## Output

- Output means information produced by a program.
- `print()` displays information.
- Multiple values can be displayed.
- `sep` controls the separator.
- `end` controls the ending.
- Escape sequences help format text.
- F-strings help display variables inside messages.

## User Input

- User input is information supplied by a person interacting with a program.
- Interactive programs use input and output together.
- Clear prompts improve usability.
- Validation checks whether values satisfy requirements.

## Input Conversion

- `int()` converts suitable values to integers.
- `float()` converts suitable values to floats.
- `str()` produces string representations.
- `bool()` produces Boolean truth values.
- `complex()` converts suitable values to complex numbers.
- `bool("False")` is `True`.
- `ValueError` commonly occurs when conversion fails.
- Conversion and validation are different operations.

## Error Handling

- `try` contains code that may raise a handled exception.
- `except` handles matching exceptions.
- Specific exception handling is usually clearer.
- Retry loops can request input again.
- Error messages should explain what the user needs to correct.

---

# 70. Quick Reference

## 70.1 Input

```python
name = input("Enter name: ")
```

## 70.2 Output

```python
print("Hello")
```

## 70.3 Input and Output

```python
name = input("Enter name: ")

print("Hello,", name)
```

## 70.4 Integer Input

```python
number = int(input("Enter integer: "))
```

## 70.5 Float Input

```python
number = float(input("Enter decimal: "))
```

## 70.6 Complex Input

```python
number = complex(input("Enter complex number: "))
```

## 70.7 String Conversion

```python
text = str(100)
```

## 70.8 Boolean Conversion

```python
result = bool(1)
```

## 70.9 Display Multiple Values

```python
print("Name:", "Amaan", "Age:", 20)
```

## 70.10 Custom Separator

```python
print("A", "B", "C", sep="-")
```

## 70.11 Custom Ending

```python
print("Hello", end=" ")
print("World")
```

## 70.12 New Line

```python
print("Hello\nWorld")
```

## 70.13 Tab

```python
print("Name\tAge")
```

## 70.14 F-String

```python
name = "Amaan"

print(f"Hello, {name}")
```

## 70.15 Safe Integer Conversion

```python
try:
    number = int(input("Enter integer: "))
    print(number)
except ValueError:
    print("Invalid integer.")
```

## 70.16 Range Validation

```python
try:
    number = int(input("Enter number: "))

    if 1 <= number <= 100:
        print("Accepted")
    else:
        print("Outside range")

except ValueError:
    print("Invalid input")
```

## 70.17 Read Multiple Integers

```python
values = input("Enter numbers: ").split()

numbers = [int(value) for value in values]

print(numbers)
```

## 70.18 Binary Conversion

```python
number = int("1010", 2)

print(number)
```

---

# 71. Frequently Asked Questions

## Q1. What is input?

Input is information supplied to a program.

## Q2. What is output?

Output is information produced by a program.

## Q3. Which function is used for input in Python?

The `input()` function.

## Q4. Which function is used for output in Python?

The `print()` function.

## Q5. What does `input()` return?

It returns a string.

## Q6. Can `input()` directly return an integer?

No. The returned value is text. Explicit conversion is required when an integer is needed.

## Q7. What is the purpose of `print()`?

It displays information.

## Q8. What does `sep` do?

It controls the separator between objects printed in a single call.

## Q9. What does `end` do?

It controls what is printed after the objects.

## Q10. What is an escape sequence?

It is a special character combination used inside strings.

## Q11. What does `\n` mean?

It represents a newline.

## Q12. What does `\t` mean?

It represents a horizontal tab.

## Q13. What is an f-string?

An f-string is a formatted string that allows expressions to be placed inside curly braces.

## Q14. Why is input conversion needed?

Because `input()` returns a string, while a program may need integers, floats, or other types for processing.

## Q15. What does `int()` do?

It converts suitable values into integers.

## Q16. What does `float()` do?

It converts suitable values into floating-point numbers.

## Q17. What does `str()` do?

It returns a string representation of a value.

## Q18. What does `bool()` do?

It converts a value into a Boolean truth value.

## Q19. Why is `bool("False")` true?

Because `"False"` is a nonempty string.

## Q20. What does `complex()` do?

It converts suitable values into complex numbers.

## Q21. What is user input?

It is information entered or supplied by a person interacting with a program.

## Q22. What is input validation?

It checks whether received information satisfies program requirements.

## Q23. What is an exception?

An exception is an event that interrupts the normal flow of execution and may be handled by the program.

## Q24. What is `ValueError`?

It is an exception that commonly occurs when a value cannot be converted or used as required.

## Q25. What is `TypeError`?

It is an exception that commonly occurs when an operation receives an incompatible type.

## Q26. Why use `try` and `except`?

They allow the program to handle expected exceptions.

## Q27. What is the IPO cycle?

It stands for Input, Process, and Output.

## Q28. Why are prompts useful?

They tell the user what information the program expects.

## Q29. What is the difference between input and conversion?

Input collects text. Conversion changes or interprets that text as another data type.

## Q30. Can a successfully converted value still be invalid?

Yes. It may not satisfy the application's range or business rules.

---

# 72. Viva Questions and Answers

Use these questions for practical examinations and oral revision.

## Basic Questions

### 1. Define input.

Input is information supplied to a computer program.

### 2. Define output.

Output is information produced by a program.

### 3. Name the Python function used for input.

`input()`.

### 4. Name the Python function used for output.

`print()`.

### 5. What is user input?

Information supplied by a person interacting with the program.

### 6. Why is input important?

It allows a program to work with different values and respond to users.

### 7. Why is output important?

It communicates information and results to users.

### 8. What does the `input()` function return?

A string.

### 9. What does the `print()` function do?

It displays values and expressions.

### 10. What is the IPO cycle?

Input, Process, and Output.

## Input Questions

### 11. What is the basic syntax of `input()`?

```python
value = input("Prompt: ")
```

### 12. Is the prompt mandatory?

No. It is optional.

### 13. What happens when the user presses Enter without typing?

An empty string is returned.

### 14. Why store input in a variable?

A variable allows the program to use the received value later.

### 15. How can surrounding spaces be removed?

Use `strip()`.

## Output Questions

### 16. What is the basic syntax of `print()`?

```python
print(value)
```

### 17. What is the default value of `sep`?

A single space.

### 18. What is the default value of `end`?

A newline character.

### 19. What does `\n` do?

It starts a new line.

### 20. What does `\t` do?

It inserts a horizontal tab.

### 21. What is string concatenation?

It joins strings together.

### 22. What is an f-string?

A formatted string that can include expressions inside braces.

### 23. Can `print()` display multiple values?

Yes.

### 24. What is the purpose of output formatting?

To display information clearly and consistently.

### 25. Can `print()` display calculated expressions?

Yes.

## Conversion Questions

### 26. Why does input conversion matter?

Because `input()` returns text, while the program may need another data type.

### 27. Which function converts suitable text to an integer?

`int()`.

### 28. Which function converts suitable text to a float?

`float()`.

### 29. Which function produces a string representation?

`str()`.

### 30. Which function converts a value to a Boolean truth value?

`bool()`.

### 31. Which function converts suitable values to complex numbers?

`complex()`.

### 32. What does `int("10")` return?

The integer `10`.

### 33. What does `float("10")` return?

The float `10.0`.

### 34. What does `int(10.9)` return?

The integer `10`.

### 35. Does `int()` round a floating-point value?

No. It truncates toward zero.

### 36. Why does `int("10.5")` fail?

Because the supplied text is not a valid integer representation for `int()`.

### 37. Why is `bool("False")` true?

Because the string is nonempty.

### 38. How can yes/no text be converted into a Boolean result?

Use explicit comparisons against supported answers.

### 39. How can multiple integer strings be converted?

Use a loop or list comprehension with `int()`.

### 40. How can binary text be converted into decimal?

Use `int(binary_text, 2)`.

## Error Handling Questions

### 41. What is `ValueError`?

An exception that commonly occurs when a value cannot be processed as required.

### 42. What is `TypeError`?

An exception that commonly indicates incompatible types in an operation.

### 43. What is the purpose of `try`?

To contain code for which specified exceptions may be handled.

### 44. What is the purpose of `except`?

To handle a matching exception.

### 45. Why should conversion errors be handled?

To prevent expected invalid input from abruptly interrupting the program.

### 46. What is a retry loop?

A loop that repeats an operation until a required condition is met.

### 47. What is validation?

Checking whether a value satisfies application requirements.

### 48. What is boundary testing?

Testing values at and around permitted limits.

### 49. Why is a specific exception better than a broad exception in many cases?

It makes the program's error-handling intention clearer and avoids hiding unrelated mistakes.

### 50. What is the main objective of this section?

To learn how a Python program receives information, processes it, converts it when necessary, and displays meaningful results.

---

# 73. Important Terminology

**Input:** Information supplied to a program.

**Output:** Information produced by a program.

**Input function:** A function used to receive information.

**Output function:** A function used to display information.

**User input:** Information supplied by a person interacting with a program.

**Prompt:** A message that tells a user what information to enter.

**Input-Process-Output:** A basic model describing how a program receives, processes, and produces information.

**Variable:** A named reference used to store or access a value.

**String:** A sequence of characters represented by Python's `str` type.

**Integer:** A whole-number value represented by Python's `int` type.

**Float:** A floating-point value represented by Python's `float` type.

**Boolean:** A logical value represented by `True` or `False`.

**Complex number:** A number containing real and imaginary components.

**Input conversion:** The process of changing or interpreting received input as another data type.

**Type conversion:** Changing a value from one data type to another.

**String concatenation:** Joining strings together.

**Escape sequence:** A special character combination used inside a string.

**Formatted string:** A string created with formatting rules, including f-strings.

**Separator:** The text inserted between objects displayed by `print()`.

**End parameter:** The parameter that controls what follows printed objects.

**Validation:** Checking whether data follows required rules.

**Exception:** An event that interrupts normal execution and can be handled.

**ValueError:** An exception commonly raised when a value is unsuitable for a requested conversion or operation.

**TypeError:** An exception commonly raised when an operation receives an incompatible type.

**Exception handling:** The process of responding to exceptions using Python constructs such as `try` and `except`.

**Boundary testing:** Testing values at or near the edge of a permitted range.

**Helper function:** A reusable function that performs a supporting task.

**Menu-driven program:** A program that presents choices for the user to select.

---

# 74. Learning Checklist

Use this checklist after completing all four topic folders.

## Topic 1 — Input

- [ ] I understand the meaning of input.
- [ ] I understand the purpose of `input()`.
- [ ] I know that `input()` returns a string.
- [ ] I can display a prompt.
- [ ] I can read a name.
- [ ] I can read a city.
- [ ] I can store input in variables.
- [ ] I can identify empty input.
- [ ] I understand how surrounding whitespace affects text.
- [ ] I can explain the purpose of an input variable.

## Topic 2 — Output

- [ ] I understand the meaning of output.
- [ ] I can use `print()`.
- [ ] I can display strings.
- [ ] I can display numbers.
- [ ] I can display variables.
- [ ] I can display multiple values.
- [ ] I understand the `sep` parameter.
- [ ] I understand the `end` parameter.
- [ ] I know common escape sequences.
- [ ] I can use newline formatting.
- [ ] I can use tab formatting.
- [ ] I can use f-strings.
- [ ] I can format decimal output.
- [ ] I can display calculation results clearly.

## Topic 3 — User Input

- [ ] I understand user interaction.
- [ ] I can create an interactive program.
- [ ] I can collect multiple inputs.
- [ ] I can store user information.
- [ ] I can combine two strings.
- [ ] I can display a formatted profile.
- [ ] I can process simple responses.
- [ ] I can write a basic menu-style interaction.
- [ ] I understand the importance of validation.
- [ ] I can explain the flow of an interactive program.

## Topic 4 — Input Conversion

- [ ] I understand why conversion is required.
- [ ] I can use `int()`.
- [ ] I can use `float()`.
- [ ] I can use `str()`.
- [ ] I can use `bool()`.
- [ ] I can use `complex()`.
- [ ] I understand Boolean truthiness.
- [ ] I can parse yes/no answers explicitly.
- [ ] I can convert a list of numeric strings.
- [ ] I can convert binary text.
- [ ] I understand `ValueError`.
- [ ] I can use `try` and `except`.
- [ ] I can validate numeric ranges.
- [ ] I understand the difference between conversion and validation.

## Combined Programming

- [ ] I can write a program that accepts two inputs.
- [ ] I can convert values before calculations.
- [ ] I can calculate and display a result.
- [ ] I can format output.
- [ ] I can handle invalid integer input.
- [ ] I can handle invalid float input.
- [ ] I can test different values.
- [ ] I can debug basic input and output errors.
- [ ] I can complete a small interactive project.
- [ ] I can explain the IPO cycle.

---

# 75. Final Summary

Input and Output are essential parts of Python programming.

They allow programs to communicate with users and process information supplied from outside the program.

The `input()` function collects a line of text.

The `print()` function displays information.

The `03_user_input` topic combines these functions to create interactive programs.

The `04_input_conversion` topic explains how to convert received text into suitable Python data types.

The complete section covers:

- Input.
- Output.
- User interaction.
- Variables.
- Data types.
- Integer conversion.
- Float conversion.
- String conversion.
- Boolean conversion.
- Complex-number conversion.
- Multiple inputs.
- List conversion.
- Output formatting.
- Escape sequences.
- Exception handling.
- Input validation.
- Practical programming.
- Debugging and testing.

## Important Points to Remember

1. Input is information received by a program.
2. Output is information produced by a program.
3. `input()` reads a line of text.
4. `input()` returns a string.
5. `print()` displays information.
6. User input should be stored in meaningful variables.
7. Convert input when another data type is required.
8. `int()` converts suitable values into integers.
9. `float()` converts suitable values into floating-point numbers.
10. `str()` produces a string representation.
11. `bool()` checks truthiness rather than interpreting English words.
12. `complex()` converts suitable values into complex numbers.
13. Use explicit parsing for yes/no responses.
14. `sep` controls separators between printed objects.
15. `end` controls the ending of printed output.
16. Escape sequences help format strings.
17. F-strings help create readable output.
18. Conversion and validation are separate operations.
19. Use exception handling for expected invalid input.
20. Test programs with different input values.

## Recommended Completion Order

Complete the folders in this order:

**First:** `01_input`

Understand how to receive information.

**Second:** `02_output`

Understand how to display information.

**Third:** `03_user_input`

Learn how to create interactive programs.

**Fourth:** `04_input_conversion`

Learn how to convert input into appropriate data types.

**Finally:** Revise all four topics and complete the practical exercises.

## Final Learning Goal

After completing this section, you should be able to create a basic interactive Python program that:

1. Displays a clear prompt.
2. Receives information from the user.
3. Stores the information in variables.
4. Converts values when necessary.
5. Validates important input.
6. Handles expected conversion errors.
7. Processes the received information.
8. Displays the final result clearly.

**Input → Process → Output**

This is the foundation of interactive programming in Python.