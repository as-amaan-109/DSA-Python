

# PYTHON PROGRAMMING FUNDAMENTALS

# Complete Programming Learning Guide

**Repository:** DSA-Python  
**Main Directory:** `PYTHON/Programming-Fundamentals/`  
**Language:** Python  
**Learning Level:** Beginner to Programming Fundamentals  
**Purpose:** Build a strong foundation for Python programming and Data Structures and Algorithms.

---

# TABLE OF CONTENTS

1. Introduction to Programming Fundamentals
2. Purpose of This Repository Section
3. Programming Fundamentals Learning Roadmap
4. Complete Repository Structure
5. Folder 01 – Introduction
6. Folder 02 – Flowcharts and Algorithms
7. Folder 03 – Pseudocode and Problem Solving
8. Folder 04 – Variables and Data Types
9. Folder 05 – Operators and Expressions
10. Folder 06 – Conditional Statements
11. Connection Between All Six Folders
12. Understanding the Python Program Execution Process
13. Input, Processing, and Output
14. Programming Logic and Decision-Making
15. Python Syntax and Indentation
16. Variables and Memory Concepts
17. Data Representation
18. Operator Reference
19. Expression Evaluation
20. Boolean Logic
21. Conditional Execution
22. Problem-Solving Methodology
23. Algorithm Design
24. Flowchart Design
25. Pseudocode Design
26. Python Implementation Process
27. Practical Programming Problems
28. Standard Python File Structure
29. Documentation Structure
30. Common Programming Errors
31. Debugging Fundamentals
32. Input Validation
33. Code Quality and Best Practices
34. Functions and Reusability
35. Basic Data Structures
36. DSA Foundation
37. Time Complexity Introduction
38. Space Complexity Introduction
39. Real-World Applications
40. Recommended Learning Sequence
41. How to Study Every Topic
42. How to Run Python Programs
43. GitHub Repository Workflow
44. File Naming Convention
45. Documentation Map
46. Programming Fundamentals Revision
47. Complete Learning Checklist
48. Chapter Completion Summary
49. Final Learning Guidance

---

# 1. INTRODUCTION TO PROGRAMMING FUNDAMENTALS

Programming Fundamentals is the foundation of software development.

Before learning advanced programming, a student needs to understand how a computer receives instructions, processes information, makes decisions, and produces results.

Programming Fundamentals introduces the basic concepts required to write computer programs.

It focuses on developing logical thinking and understanding how programming instructions work.

Python is used throughout this repository because it has readable syntax and supports a wide range of programming applications.

## 1.1 What Is Programming?

Programming is the process of writing instructions that tell a computer how to perform a particular task.

A computer follows instructions provided by a program.

A program can perform operations such as:

- Calculating mathematical values.
- Accepting user information.
- Displaying messages.
- Comparing values.
- Processing data.
- Managing information.
- Performing repetitive operations.
- Making decisions.
- Automating tasks.
- Producing reports.

### Example

```python
print("Welcome to Python Programming")
```

Output:

```text
Welcome to Python Programming
```

In this example, the program instructs Python to display a message.

## 1.2 What Is a Programming Language?

A programming language is a language used to write instructions that a computer can execute.

Different programming languages have different syntax, features, and applications.

Examples include:

- Python.
- C.
- C++.
- Java.
- JavaScript.
- C#.
- Go.
- Rust.

This repository uses Python for learning programming fundamentals.

## 1.3 What Is Python?

Python is a high-level, general-purpose programming language.

It is commonly used for:

- Software development.
- Web development.
- Backend development.
- Automation.
- Scripting.
- Data analysis.
- Artificial intelligence.
- Machine learning.
- Scientific computing.
- Educational programming.

## 1.4 Why Learn Python?

Python is useful for beginners because its syntax is relatively readable.

Example:

```python
number1 = 10
number2 = 20

result = number1 + number2

print(result)
```

Output:

```text
30
```

The code is easy to understand because the operations are expressed clearly.

## 1.5 What Is Source Code?

Source code is the human-readable set of instructions written in a programming language.

Example:

```python
name = "Amaan"

print("Hello", name)
```

This Python code is source code.

## 1.6 What Is a Program?

A program is a collection of instructions that performs a task.

Example:

```python
first_number = 10
second_number = 20

total = first_number + second_number

print("Total:", total)
```

This program calculates the sum of two numbers.

## 1.7 What Is an Interpreter?

An interpreter is software that executes a programming language.

Python programs are commonly executed using the Python interpreter.

Example:

```powershell
python main.py
```

The command asks Python to execute the file named `main.py`.

## 1.8 What Is Syntax?

Syntax means the rules that define how code must be written.

Incorrect syntax:

```python
if number > 0
    print("Positive")
```

Correct syntax:

```python
if number > 0:
    print("Positive")
```

The colon is required after the condition.

## 1.9 What Is Output?

Output is the information produced by a program.

Example:

```python
print("Hello")
```

Output:

```text
Hello
```

## 1.10 What Is Input?

Input is the information supplied to a program.

Example:

```python
name = input("Enter your name: ")

print("Welcome", name)
```

The program accepts a name and displays it.

## 1.11 Input, Process, and Output

Most beginner programs can be understood using three main stages.

**Input**

Information enters the program.

**Process**

The program performs operations on the information.

**Output**

The program displays or returns the result.

Example:

Problem: Add two numbers.

Input:

```text
10
20
```

Process:

```text
10 + 20
```

Output:

```text
30
```

## 1.12 Learning Outcome

After completing the Introduction folder, you should understand:

- What programming means.
- What a programming language is.
- What Python is.
- How source code works.
- How Python executes a program.
- How input and output work.
- How to write basic Python statements.
- How to identify basic syntax errors.

---

# 2. PURPOSE OF THIS REPOSITORY SECTION

The Programming Fundamentals directory is designed to organize the first stage of the Python learning journey.

It contains six major learning areas.

Each area introduces concepts required by the next area.

## 2.1 Learning Area 01 – Introduction

Understand programming and Python basics.

## 2.2 Learning Area 02 – Flowcharts and Algorithms

Understand how to design solutions before writing code.

## 2.3 Learning Area 03 – Pseudocode and Problem Solving

Understand how to express program logic using structured instructions.

## 2.4 Learning Area 04 – Variables and Data Types

Understand how information is represented and stored.

## 2.5 Learning Area 05 – Operators and Expressions

Understand how values are manipulated and expressions are evaluated.

## 2.6 Learning Area 06 – Conditional Statements

Understand how programs make decisions.

## 2.7 Overall Learning Goal

The overall goal is to develop the ability to:

1. Understand a programming problem.
2. Identify inputs.
3. Identify expected outputs.
4. Design a logical solution.
5. Write an algorithm.
6. Represent the algorithm using pseudocode.
7. Implement the logic in Python.
8. Execute the program.
9. Identify errors.
10. Improve the solution.

---

# 3. PROGRAMMING FUNDAMENTALS LEARNING ROADMAP

The roadmap follows six major stages.

## Stage 01 – Introduction

Learn:

- Programming basics.
- Python introduction.
- Python installation.
- Running Python programs.
- Print statements.
- Basic syntax.
- Comments.
- Escape sequences.
- Basic input and output.

## Stage 02 – Flowcharts and Algorithms

Learn:

- Algorithm meaning.
- Algorithm characteristics.
- Algorithm steps.
- Flowchart basics.
- Flowchart symbols.
- Flowchart construction.
- Process representation.
- Input/output representation.
- Decision representation.

## Stage 03 – Pseudocode and Problem Solving

Learn:

- Pseudocode meaning.
- Pseudocode structure.
- Input identification.
- Output identification.
- Problem decomposition.
- Algorithm planning.
- Logical steps.
- Solution representation.

## Stage 04 – Variables and Data Types

Learn:

- Variables.
- Variable assignment.
- Naming rules.
- Integers.
- Floating-point numbers.
- Complex numbers.
- Strings.
- Booleans.
- Lists.
- Tuples.
- Sets.
- Dictionaries.
- Type checking.
- Type conversion.

## Stage 05 – Operators and Expressions

Learn:

- Arithmetic operators.
- Comparison operators.
- Logical operators.
- Assignment operators.
- Membership operators.
- Identity operators.
- Bitwise operators.
- Expressions.
- Operator precedence.
- Expression evaluation.

## Stage 06 – Conditional Statements

Learn:

- If statement.
- If-else.
- If-elif-else.
- Nested if.
- Conditional expressions.
- Match case.
- Practical decision-making problems.

## 3.1 Learning Roadmap Diagram

```text
                 PYTHON
                    |
                    v
          PROGRAMMING FUNDAMENTALS
                    |
       +------------+-------------+
       |            |             |
       v            v             v
  INTRODUCTION  ALGORITHMS   PSEUDOCODE
       |            |             |
       +------------+-------------+
                    |
                    v
           VARIABLES AND TYPES
                    |
                    v
          OPERATORS AND EXPRESSIONS
                    |
                    v
          CONDITIONAL STATEMENTS
                    |
                    v
           PROGRAMMING PRACTICE
                    |
                    v
             DSA FOUNDATION
```

---

# 4. COMPLETE REPOSITORY STRUCTURE

The current Programming Fundamentals directory contains six main folders.

```text
PYTHON/
└── Programming-Fundamentals/
    │
    ├── README.md
    │
    ├── 01-Introduction/
    │
    ├── 02-Flowcharts-Algorithms/
    │
    ├── 03-Pseudocode-Problem-Solving/
    │
    ├── 04-Variables-Data-Types/
    │
    ├── 05-Operators-Expressions/
    │
    └── 06-Conditional-Statements/
```

## 4.1 Folder Descriptions

| Folder | Main Purpose |
|---|---|
| `01-Introduction` | Understand Python and programming basics |
| `02-Flowcharts-Algorithms` | Understand algorithms and flowcharts |
| `03-Pseudocode-Problem-Solving` | Develop problem-solving logic |
| `04-Variables-Data-Types` | Learn data storage and data types |
| `05-Operators-Expressions` | Learn calculations and expressions |
| `06-Conditional-Statements` | Learn decision-making |

## 4.2 Why Use Numbered Folders?

Numbered folders maintain a clear learning sequence.

They make it easier to:

- Identify the next topic.
- Maintain repository organization.
- Navigate through GitHub.
- Locate documentation.
- Track learning progress.
- Keep the learning structure consistent.

## 4.3 Purpose of the Parent README

This README is the main documentation file for the entire Programming Fundamentals directory.

It provides:

- Overall learning roadmap.
- Folder descriptions.
- Concept connections.
- Topic navigation.
- Programming workflow.
- Common references.
- Learning guidance.
- Repository structure.

Individual folders maintain their own READMEs for detailed topic-level documentation.

---

# 5. FOLDER 01 – INTRODUCTION

**Directory:** `01-Introduction/`

This folder introduces Python and the basic concepts required to begin programming.

It is the starting point of the Programming Fundamentals section.

## 5.1 Learning Purpose

The purpose of this folder is to understand how to write a basic Python program and how to execute it.

Before learning calculations, conditions, and algorithms, you should know how Python code is written.

## 5.2 Introduction to Python

Python is a high-level language.

Its syntax allows programmers to express instructions using readable statements.

Example:

```python
print("Hello World")
```

The `print()` function displays output.

## 5.3 Hello World Program

The Hello World program is traditionally used as the first example when learning a programming language.

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

## 5.4 Understanding Print Statements

The `print()` function displays information.

Example:

```python
print("Python")
print("Programming")
print(100)
print(10.5)
```

Output:

```text
Python
Programming
100
10.5
```

## 5.5 Printing Multiple Values

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

## 5.6 Understanding Escape Sequences

Escape sequences represent special characters inside strings.

Common examples:

| Escape Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Horizontal tab |
| `\\` | Backslash |
| `\'` | Single quotation mark |
| `\"` | Double quotation mark |

Example:

```python
print("Hello\nPython")
```

Output:

```text
Hello
Python
```

## 5.7 Comments in Python

Comments explain code and are ignored during normal execution.

Single-line comment:

```python
# This is a comment

print("Hello")
```

Comments improve readability when used appropriately.

## 5.8 Python File Extension

Python files generally use the `.py` extension.

Example:

```text
main.py
hello_world.py
program.py
```

## 5.9 Running a Python File

Open a terminal in the correct directory.

Execute:

```powershell
python filename.py
```

Example:

```powershell
python hello_world.py
```

## 5.10 Important Concepts

- Programming language.
- Python.
- Source code.
- Interpreter.
- Python file.
- Print function.
- Comments.
- Escape sequences.
- Output.
- Syntax.

## 5.11 Practical Applications

The concepts in this folder are used in every Python application.

The `print()` function is used for displaying information.

Comments explain the purpose of code.

Escape sequences help format output.

Python files store executable source code.

## 5.12 Folder Completion Goals

After completing Introduction, you should be able to:

- Write a Hello World program.
- Use print statements.
- Print multiple values.
- Use strings and numbers in output.
- Understand escape sequences.
- Add comments.
- Save code in a Python file.
- Execute a Python file.
- Recognize basic syntax mistakes.

## 5.13 Folder Structure

```text
Programming-Fundamentals/
└── 01-Introduction/
```

Refer to `01-Introduction/README.md` for the complete topic documentation and the available Python examples.

---

# 6. FOLDER 02 – FLOWCHARTS AND ALGORITHMS

**Directory:** `02-Flowcharts-Algorithms/`

This folder introduces algorithm design and flowchart representation.

An algorithm describes how a problem can be solved.

A flowchart visually represents the steps of the algorithm.

## 6.1 What Is an Algorithm?

An algorithm is a finite sequence of instructions designed to solve a problem.

An algorithm must clearly explain what needs to happen and in which order.

### Example: Addition of Two Numbers

Algorithm:

1. Start.
2. Input the first number.
3. Input the second number.
4. Calculate their sum.
5. Display the sum.
6. Stop.

### Python Implementation

```python
a = 10
b = 20

total = a + b

print(total)
```

Output:

```text
30
```

## 6.2 Characteristics of an Algorithm

### Input

An algorithm may accept zero or more inputs.

### Output

An algorithm should produce the required result.

### Definiteness

Every step must be clearly specified.

### Finiteness

The algorithm must terminate after a finite number of steps.

### Effectiveness

The instructions should be practical and executable.

## 6.3 What Is a Flowchart?

A flowchart is a graphical representation of an algorithm.

It uses standard symbols to represent the steps of a process.

## 6.4 Flowchart Symbols

| Symbol | Meaning |
|---|---|
| Oval | Start or Stop |
| Rectangle | Process |
| Parallelogram | Input or Output |
| Diamond | Decision |
| Arrow | Flow direction |
| Connector | Connects sections |

## 6.5 Start and Stop Symbol

The oval represents the beginning or ending of a process.

Example:

```text
      START
        |
        v
       STOP
```

## 6.6 Process Symbol

A rectangle represents an operation or calculation.

Example:

```text
     +-------------+
     | Sum = A + B |
     +-------------+
```

## 6.7 Input and Output Symbol

A parallelogram represents accepting input or displaying output.

Example:

```text
    /----------------\
   /  Input Number A  /
   \----------------/
```

## 6.8 Decision Symbol

A diamond represents a condition.

Example:

```text
       +-----------+
       | A > B ?   |
       +-----------+
         /       \
       Yes       No
```

## 6.9 Example: Positive Number Flowchart

```text
          START
            |
            v
       Input Number
            |
            v
       Number > 0 ?
         /     \
       Yes      No
        |        |
        v        v
   Display     Display
   Positive   Not Positive
        |        |
        +---+----+
            |
            v
           STOP
```

## 6.10 Example: Even and Odd Algorithm

Algorithm:

1. Start.
2. Input a number.
3. Calculate the remainder after division by two.
4. If the remainder equals zero, display Even.
5. Otherwise, display Odd.
6. Stop.

Python implementation:

```python
number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 6.11 Algorithm vs Flowchart

| Algorithm | Flowchart |
|---|---|
| Written instructions | Visual symbols |
| Describes steps | Represents process flow |
| Easy to write | Easy to visualize |
| Uses a sequence of operations | Uses arrows and shapes |
| Useful in planning | Useful in explaining logic |

## 6.12 When to Use Algorithms

Algorithms are useful when:

- A problem has multiple steps.
- A solution requires mathematical operations.
- A program includes decisions.
- A task involves repeated processing.
- A problem needs to be optimized.
- A solution must be explained clearly.

## 6.13 When to Use Flowcharts

Flowcharts are useful when:

- Visualizing program logic.
- Understanding decision branches.
- Explaining a process.
- Teaching problem-solving.
- Reviewing the execution sequence.
- Communicating a solution.

## 6.14 Folder Completion Goals

After completing this folder, you should be able to:

- Explain what an algorithm is.
- Identify algorithm characteristics.
- Write simple algorithms.
- Understand flowchart symbols.
- Draw basic flowcharts.
- Represent input and output.
- Represent processes.
- Represent decisions.
- Convert a simple flowchart into Python code.

## 6.15 Folder Structure

```text
Programming-Fundamentals/
└── 02-Flowcharts-Algorithms/
```

Refer to `02-Flowcharts-Algorithms/README.md` for the complete detailed documentation.

---

# 7. FOLDER 03 – PSEUDOCODE AND PROBLEM SOLVING

**Directory:** `03-Pseudocode-Problem-Solving/`

This folder develops logical thinking and structured problem solving.

It explains how a programmer can describe a solution before implementing it in Python.

## 7.1 What Is Pseudocode?

Pseudocode is a readable, structured representation of a program's logic.

It is not restricted to a particular programming language.

It helps programmers express the solution without worrying about programming syntax.

### Example

Problem: Add two numbers.

Pseudocode:

```text
START

INPUT A
INPUT B

SUM = A + B

DISPLAY SUM

STOP
```

## 7.2 Why Use Pseudocode?

Pseudocode helps programmers:

- Understand the problem.
- Plan the logic.
- Organize instructions.
- Identify missing steps.
- Explain solutions.
- Convert logic into Python.
- Avoid unnecessary coding mistakes.

## 7.3 What Is Problem Solving?

Problem solving is the process of understanding a task and designing a solution.

A programming problem usually provides some information and asks for a particular result.

A programmer must identify how that result can be obtained.

## 7.4 Problem-Solving Steps

### Step 1 – Understand the Problem

Read the statement carefully.

Identify what is required.

### Step 2 – Identify Inputs

Determine what information is provided.

### Step 3 – Identify Outputs

Determine what the program must display or return.

### Step 4 – Identify Operations

Find the calculations or logical checks required.

### Step 5 – Design an Algorithm

Write the solution as an ordered sequence of steps.

### Step 6 – Write Pseudocode

Express the algorithm using structured instructions.

### Step 7 – Implement in Python

Convert the pseudocode into executable Python code.

### Step 8 – Review the Result

Check whether the program produces the expected output.

## 7.5 Input, Process, and Output

Every simple problem can be examined using three components.

**Input:** Information provided to the program.

**Process:** Instructions performed using that information.

**Output:** Result produced by the program.

### Example: Area of a Rectangle

Input:

```text
Length = 10
Width = 5
```

Process:

```text
Area = Length * Width
```

Output:

```text
Area = 50
```

Python implementation:

```python
length = 10
width = 5

area = length * width

print("Area:", area)
```

## 7.6 Problem Decomposition

Problem decomposition means dividing a large problem into smaller tasks.

For example, a student result management program can be divided into:

1. Accept student details.
2. Accept subject marks.
3. Calculate total.
4. Calculate percentage.
5. Calculate average.
6. Assign grade.
7. Determine result.
8. Display report.

Each part can be implemented and reviewed separately.

## 7.7 Pseudocode for a Decision Problem

Problem: Check whether a number is positive or negative.

```text
START

INPUT NUMBER

IF NUMBER > 0
    DISPLAY "POSITIVE"

ELSE IF NUMBER < 0
    DISPLAY "NEGATIVE"

ELSE
    DISPLAY "ZERO"

END IF

STOP
```

Python implementation:

```python
number = int(input("Enter number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## 7.8 Algorithm vs Pseudocode vs Source Code

| Feature | Algorithm | Pseudocode | Source Code |
|---|---|---|---|
| Purpose | Describe solution steps | Structure solution logic | Execute solution |
| Syntax | Informal | Structured but flexible | Strict language syntax |
| Language dependency | Independent | Generally independent | Language-specific |
| Visual appearance | Numbered steps | Instruction-like | Actual program |
| Execution | Not directly executable | Not directly executable | Executable by an appropriate runtime |

## 7.9 Folder Completion Goals

After completing this folder, you should be able to:

- Understand a problem statement.
- Identify inputs and outputs.
- Describe a solution.
- Write pseudocode.
- Develop step-by-step algorithms.
- Break larger problems into smaller parts.
- Convert pseudocode into Python.
- Explain why a solution works.

## 7.10 Folder Structure

```text
Programming-Fundamentals/
└── 03-Pseudocode-Problem-Solving/
```

Refer to the folder's README for its complete topic-wise explanations.

---

# 8. FOLDER 04 – VARIABLES AND DATA TYPES

**Directory:** `04-Variables-Data-Types/`

This folder explains how Python represents and stores information.

Variables and data types are required in almost every program.

## 8.1 What Is a Variable?

A variable is a name used to refer to a value.

Example:

```python
name = "Amaan"
age = 22
marks = 85.5
```

Variables allow the program to work with values using meaningful names.

## 8.2 Variable Assignment

The `=` operator assigns a value.

```python
number = 100

print(number)
```

Output:

```text
100
```

## 8.3 Variable Naming Rules

Python identifiers follow naming rules.

Examples of valid names:

```python
student_name = "Amaan"
total_marks = 450
age = 22
number1 = 10
```

Variable names should:

- Begin with a letter or underscore.
- Not begin with a digit.
- Avoid spaces.
- Avoid reserved keywords.
- Use meaningful names.
- Follow consistent naming conventions.

## 8.4 Python Naming Convention

Snake case is commonly used for Python variable and function names.

Example:

```python
first_name = "Amaan"
total_amount = 5000
average_marks = 85.5
```

## 8.5 What Is a Data Type?

A data type identifies the category of a value.

It helps Python determine how that value can be used.

## 8.6 Numeric Data Types

### Integer

Represents whole numbers.

```python
age = 22

print(type(age))
```

Output:

```text
<class 'int'>
```

### Float

Represents decimal numbers.

```python
marks = 85.5

print(type(marks))
```

Output:

```text
<class 'float'>
```

### Complex

Represents complex numbers.

```python
number = 2 + 3j

print(type(number))
```

Output:

```text
<class 'complex'>
```

## 8.7 String

A string represents text.

```python
name = "Amaan"

print(type(name))
```

Output:

```text
<class 'str'>
```

## 8.8 Boolean

A Boolean represents one of two values:

```python
True
False
```

Example:

```python
is_student = True

print(type(is_student))
```

Output:

```text
<class 'bool'>
```

## 8.9 List

A list is an ordered and mutable collection.

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

## 8.10 Tuple

A tuple is an ordered and immutable collection.

```python
numbers = (10, 20, 30)

print(numbers)
```

## 8.11 Set

A set stores unique elements.

```python
numbers = {10, 20, 30}

print(numbers)
```

## 8.12 Dictionary

A dictionary stores key-value pairs.

```python
student = {
    "name": "Amaan",
    "age": 22,
    "marks": 85
}

print(student["name"])
```

## 8.13 None

`None` represents the absence of a value.

```python
result = None

print(result)
```

## 8.14 Checking Data Types

The `type()` function identifies the type of an object.

```python
values = [
    10,
    10.5,
    2 + 3j,
    "Python",
    True,
    [1, 2],
    (1, 2),
    {1, 2},
    {"name": "Amaan"},
    None
]

for value in values:
    print(value, type(value))
```

## 8.15 Type Conversion

Python supports converting values between compatible types.

Integer conversion:

```python
number = int("100")
```

Float conversion:

```python
number = float("10.5")
```

String conversion:

```python
number = str(100)
```

Boolean conversion:

```python
result = bool(1)
```

## 8.16 Input and Data Types

The `input()` function returns a string.

Example:

```python
age = input("Enter age: ")

print(type(age))
```

To perform integer operations:

```python
age = int(input("Enter age: "))

print(age + 1)
```

## 8.17 Folder Completion Goals

You should be able to:

- Create variables.
- Assign values.
- Choose meaningful names.
- Identify Python data types.
- Use `type()`.
- Convert compatible values.
- Understand collections.
- Accept typed user input.
- Use variables in calculations.

## 8.18 Folder Structure

```text
Programming-Fundamentals/
└── 04-Variables-Data-Types/
```

Refer to the folder's README for the complete topic-wise notes.

---

# 9. FOLDER 05 – OPERATORS AND EXPRESSIONS

**Directory:** `05-Operators-Expressions/`

This folder introduces the symbols and operations used to manipulate values.

Operators are essential in calculations, comparisons, and logical decision-making.

## 9.1 What Is an Operator?

An operator performs an operation on one or more operands.

Example:

```python
result = 10 + 20
```

- `10` is an operand.
- `20` is an operand.
- `+` is an operator.

## 9.2 Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor division | `10 // 3` |
| `%` | Modulus | `10 % 3` |
| `**` | Exponentiation | `2 ** 3` |

### Example

```python
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // 3)
print("Modulus:", a % 3)
print("Exponent:", 2 ** 3)
```

## 9.3 Comparison Operators

Comparison operators compare values.

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `==` | Equal to |
| `!=` | Not equal to |

Example:

```python
a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```

## 9.4 Logical Operators

Python includes:

- `and`
- `or`
- `not`

Example:

```python
age = 20
has_id = True

result = age >= 18 and has_id

print(result)
```

## 9.5 Assignment Operators

Assignment operators modify or assign values.

| Operator | Example |
|---|---|
| `=` | `x = 10` |
| `+=` | `x += 5` |
| `-=` | `x -= 5` |
| `*=` | `x *= 2` |
| `/=` | `x /= 2` |
| `//=` | `x //= 2` |
| `%=` | `x %= 2` |
| `**=` | `x **= 2` |

## 9.6 Membership Operators

Membership operators check whether an item belongs to a collection.

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(40 not in numbers)
```

## 9.7 Identity Operators

Identity operators compare object identity.

- `is`
- `is not`

Example:

```python
value = None

if value is None:
    print("No value assigned")
```

## 9.8 Bitwise Operators

Bitwise operators work on integer bits.

| Operator | Name |
|---|---|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left shift |
| `>>` | Right shift |

Example:

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
```

## 9.9 What Is an Expression?

An expression combines values, variables, operators, and other operations to produce a result.

Example:

```python
result = (10 + 5) * 2
```

The expression produces 30.

## 9.10 Operator Precedence

Operator precedence determines which operations are evaluated first.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication is performed before addition.

## 9.11 Parentheses

Parentheses help control the order of evaluation.

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

## 9.12 Expressions in Practical Problems

Expressions can calculate:

- Total marks.
- Percentage.
- Average.
- Area.
- Perimeter.
- Distance.
- Profit.
- Loss.
- Discounts.
- Divisibility.
- Comparisons.

## 9.13 Folder Completion Goals

You should be able to:

- Understand operators and operands.
- Use arithmetic operators.
- Use comparison operators.
- Use logical operators.
- Use assignment operators.
- Use membership operators.
- Use identity operators.
- Use bitwise operators.
- Evaluate expressions.
- Understand precedence.
- Use expressions in practical calculations.

## 9.14 Folder Structure

```text
Programming-Fundamentals/
└── 05-Operators-Expressions/
```

Refer to `05-Operators-Expressions/README.md` for the full notes and examples.

---

# 10. FOLDER 06 – CONDITIONAL STATEMENTS

**Directory:** `06-Conditional-Statements/`

This folder introduces decision-making structures in Python.

It contains individual conditional statement topics and a practical problem-solving section.

## 10.1 Introduction

A conditional statement allows a program to select different instructions depending on a condition.

Example:

```python
age = 20

if age >= 18:
    print("Condition satisfied")
else:
    print("Condition not satisfied")
```

## 10.2 Topics Inside This Folder

| No. | Folder | Main Concept |
|---:|---|---|
| 01 | `01-If-Statement` | Basic if |
| 02 | `02-If-Else` | Two-way decision |
| 03 | `03-If-Elif-Else` | Multiple decisions |
| 04 | `04-Nested-If` | Dependent decisions |
| 05 | `05-Conditional-Expressions` | Ternary conditional expression |
| 06 | `06-Practice-Problems` | Six practical problem topics |
| 07 | `07-Match-Case` | Structural pattern matching |

## 10.3 If Statement

The if statement executes a code block when a condition evaluates to true.

```python
number = 10

if number > 0:
    print("Positive")
```

## 10.4 If-Else Statement

The if-else statement provides two execution alternatives.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 10.5 If-Elif-Else Statement

The if-elif-else structure checks multiple conditions.

```python
marks = 85

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Other grade")
```

## 10.6 Nested If

A nested if is placed inside another conditional block.

```python
age = 20
has_id = True

if age >= 18:

    if has_id:
        print("Both conditions satisfied")

    else:
        print("ID required")

else:
    print("Age condition not satisfied")
```

## 10.7 Conditional Expressions

A conditional expression selects one value based on a condition.

```python
number = 10

result = "Positive" if number > 0 else "Not Positive"

print(result)
```

## 10.8 Match Case

Match case performs structural pattern matching.

It requires Python 3.10 or newer.

```python
choice = 2

match choice:

    case 1:
        print("Home")

    case 2:
        print("Profile")

    case 3:
        print("Settings")

    case _:
        print("Invalid choice")
```

## 10.9 Practical Problems

The folder contains six practical programming topics.

| No. | Problem | Main Concept |
|---:|---|---|
| 01 | Positive and Negative | Number classification |
| 02 | Even and Odd | Divisibility |
| 03 | Largest Number | Number comparison |
| 04 | Leap Year | Calendar conditions |
| 05 | Grade Calculator | Marks classification |
| 06 | Voting Eligibility | Age-based classification |

### Practice Problem 01 – Positive and Negative

```python
number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Practice Problem 02 – Even and Odd

```python
number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Practice Problem 03 – Largest Number

```python
a = 10
b = 20
c = 15

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
```

### Practice Problem 04 – Leap Year

```python
year = 2024

if year % 400 == 0 or (
    year % 4 == 0 and year % 100 != 0
):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

### Practice Problem 05 – Grade Calculator

```python
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)
```

### Practice Problem 06 – Voting Eligibility

```python
age = 20

if age >= 18:
    print("Eligible by age")
else:
    print("Not eligible by age")
```

**Important:** The voting exercise is an age-based programming example, not a complete legal eligibility determination.

## 10.10 Practice Program Standard

Each of the six practice programs follows a consistent layout.

```text
Python File
│
├── Module Docstring
├── Imports
├── Constants
├── HELPER FUNCTIONS
├── SECTION 1: TWELVE TOPIC EXAMPLES
├── SECTION 2: TWELVE SOLVED PROBLEMS
├── SOLVED_PROBLEMS
├── SECTION 3: TEN UNSOLVED QUESTIONS
├── SECTION 4: LEARNING CHECKLIST
├── SECTION 5: MAIN MENU
└── PROGRAM EXECUTION
```

## 10.11 Standard Main Menu

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## 10.12 Learning Outcome

After completing this folder, you should be able to implement decision-making logic using several conditional structures.

You should also be able to apply conditions to practical numerical, academic, and classification problems.

---

# 11. CONNECTION BETWEEN ALL SIX FOLDERS

The six folders are connected through the process of creating a program.

Consider this problem:

**Write a program to calculate the area of a rectangle and classify the result as zero, positive, or invalid.**

This problem uses concepts from several folders.

## 11.1 Introduction Connection

Understand how to write a Python program.

## 11.2 Algorithm Connection

Create an algorithm describing the calculation.

## 11.3 Pseudocode Connection

Write structured steps.

## 11.4 Variables and Data Types Connection

Store length, width, and area.

## 11.5 Operators Connection

Use multiplication.

## 11.6 Conditional Statements Connection

Classify the calculated area.

### Complete Problem

Input:

```text
Length = 10
Width = 5
```

Formula:

\[
Area = Length \times Width
\]

Expected result:

```text
Area = 50
```

### Algorithm

1. Start.
2. Input length.
3. Input width.
4. Check whether either value is negative.
5. If invalid, display an error.
6. Otherwise, calculate the area.
7. Display the area.
8. Stop.

### Pseudocode

```text
START

INPUT length
INPUT width

IF length < 0 OR width < 0
    DISPLAY "Invalid dimensions"
ELSE
    area = length * width
    DISPLAY area
END IF

STOP
```

### Python Implementation

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Invalid dimensions")
else:
    area = length * width
    print("Area:", area)
```

This example combines all six learning areas.

---

# 12. UNDERSTANDING THE PYTHON PROGRAM EXECUTION PROCESS

A Python program follows a series of steps from writing code to receiving output.

## 12.1 Write the Program

Create a Python source file.

Example:

```text
main.py
```

## 12.2 Write Instructions

```python
print("Hello Python")
```

## 12.3 Save the File

Save the code with a `.py` extension.

## 12.4 Open a Terminal

Open the terminal in the folder containing the program.

## 12.5 Execute the File

```powershell
python main.py
```

## 12.6 Observe the Output

```text
Hello Python
```

## 12.7 Review the Result

Compare the actual output with the expected output.

If the output is incorrect, identify and correct the problem.

## 12.8 Execution Workflow

```text
WRITE CODE
    |
    v
SAVE FILE
    |
    v
OPEN TERMINAL
    |
    v
RUN PYTHON FILE
    |
    v
PYTHON PROCESSES CODE
    |
    v
DISPLAY OUTPUT
    |
    v
REVIEW RESULT
```

---

# 13. INPUT, PROCESSING, AND OUTPUT

Input, processing, and output are basic components of programming.

## 13.1 Input

Input is the information supplied to a program.

Example:

```python
number = input("Enter a number: ")
```

## 13.2 Processing

Processing means performing operations using the input.

Example:

```python
number = int(input("Enter a number: "))

result = number * 2
```

## 13.3 Output

Output is the result produced by the program.

Example:

```python
print("Result:", result)
```

## 13.4 Complete Example

```python
number = int(input("Enter a number: "))

result = number * 2

print("Result:", result)
```

Sample input:

```text
Enter a number: 5
```

Output:

```text
Result: 10
```

---

# 14. PROGRAMMING LOGIC AND DECISION-MAKING

Programming logic describes how a solution is organized and how instructions are executed.

A programmer needs to understand the sequence and relationship between operations.

## 14.1 Sequential Execution

Sequential execution means statements are executed in order.

```python
a = 10
b = 20

total = a + b

print(total)
```

## 14.2 Decision-Making

Decision-making selects an execution path.

```python
number = 10

if number > 0:
    print("Positive")
```

## 14.3 Repetition

Repetition executes instructions multiple times.

Example:

```python
for number in range(1, 6):
    print(number)
```

## 14.4 Three Basic Programming Control Structures

| Structure | Purpose |
|---|---|
| Sequence | Execute instructions in order |
| Selection | Choose a path based on a condition |
| Iteration | Repeat instructions |

These are foundational concepts in structured programming.

---

# 15. PYTHON SYNTAX AND INDENTATION

Python uses indentation to define code blocks.

Indentation is not simply visual formatting.

It is part of Python syntax.

## 15.1 Correct Indentation

```python
if number > 0:
    print("Positive")
```

## 15.2 Incorrect Indentation

```python
if number > 0:
print("Positive")
```

The second example causes an indentation error.

## 15.3 Consistent Indentation

Use consistent indentation throughout the program.

Four spaces are the standard convention for Python code blocks.

## 15.4 Colon Usage

A colon is used after statements that begin a block.

Examples:

```python
if condition:
    statement
```

```python
for item in items:
    print(item)
```

```python
def function_name():
    print("Hello")
```

## 15.5 Important Syntax Rules

- Use correct spelling for Python keywords.
- Use colons where required.
- Maintain indentation.
- Use matching brackets.
- Use quotation marks for string literals.
- Use valid variable names.
- Use parentheses where required.
- Write expressions according to Python syntax.

---

# 16. VARIABLES AND MEMORY CONCEPTS

Variables allow programs to refer to information.

In Python, names are bound to objects.

## 16.1 Assigning Values

```python
number = 10
```

## 16.2 Reassigning Values

```python
number = 10
number = 20

print(number)
```

Output:

```text
20
```

## 16.3 Multiple Variables

```python
first_name = "Amaan"
last_name = "Syed"
age = 22
```

## 16.4 Multiple Assignment

```python
a, b, c = 10, 20, 30
```

## 16.5 Same Value Assignment

```python
x = y = z = 100
```

## 16.6 Variable Use in Expressions

```python
price = 100
quantity = 5

total = price * quantity

print(total)
```

Output:

```text
500
```

## 16.7 Meaningful Names

Good variable names explain the purpose of their values.

Prefer:

```python
total_marks = 450
average_marks = 90
student_name = "Amaan"
```

Avoid using unclear variable names when a descriptive name improves readability.

---

# 17. DATA REPRESENTATION

Programs process different kinds of information.

Python provides built-in types that represent numbers, text, Boolean values, and collections.

## 17.1 Numeric Data

```python
age = 22
marks = 90.5
complex_number = 2 + 3j
```

## 17.2 Text Data

```python
name = "Python"
```

## 17.3 Boolean Data

```python
is_active = True
```

## 17.4 Collection Data

```python
numbers = [10, 20, 30]
coordinates = (10, 20)
unique_values = {10, 20, 30}

student = {
    "name": "Amaan",
    "age": 22
}
```

## 17.5 Choosing a Suitable Type

Choose the data type according to the kind of information.

| Requirement | Suitable Type |
|---|---|
| Whole number | `int` |
| Decimal value | `float` |
| Text | `str` |
| True/False | `bool` |
| Ordered mutable collection | `list` |
| Ordered immutable collection | `tuple` |
| Unique values | `set` |
| Key-value information | `dict` |
| Missing value | `None` |

---

# 18. OPERATOR REFERENCE

## 18.1 Arithmetic

```python
a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

## 18.2 Comparison

```python
a = 10
b = 20

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
```

## 18.3 Logical

```python
x = 10

print(x > 5 and x < 20)
print(x < 5 or x == 10)
print(not x == 10)
```

## 18.4 Assignment

```python
x = 10

x += 5
x -= 2
x *= 2

print(x)
```

## 18.5 Membership

```python
numbers = [10, 20, 30]

print(10 in numbers)
print(40 not in numbers)
```

## 18.6 Identity

```python
value = None

print(value is None)
print(value is not None)
```

## 18.7 Bitwise

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
```

---

# 19. EXPRESSION EVALUATION

An expression is evaluated according to Python's operator rules.

## 19.1 Arithmetic Expression

```python
result = 10 + 5
```

## 19.2 Combined Expression

```python
result = 10 + 5 * 2
```

## 19.3 Parenthesized Expression

```python
result = (10 + 5) * 2
```

## 19.4 Comparison Expression

```python
result = 10 > 5
```

## 19.5 Logical Expression

```python
result = 10 > 5 and 20 > 10
```

## 19.6 Expression as a Condition

```python
number = 12

if number % 2 == 0:
    print("Even")
```

## 19.7 Importance of Operator Precedence

Operator precedence determines which operations take priority.

Parentheses make complex expressions easier to read.

Do not rely on memorization when an expression can be made clearer using parentheses.

---

# 20. BOOLEAN LOGIC

Boolean logic is fundamental to conditions.

Python uses two Boolean values.

```python
True
False
```

## 20.1 Comparison Results

```python
print(5 > 2)
print(5 < 2)
print(5 == 5)
```

## 20.2 AND

Both conditions must be true.

```python
age = 20
marks = 80

if age >= 18 and marks >= 40:
    print("Conditions satisfied")
```

## 20.3 OR

At least one condition must be true.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

## 20.4 NOT

Reverses a Boolean value.

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

## 20.5 Truth Tables

### AND

| A | B | A and B |
|---|---|---|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

### OR

| A | B | A or B |
|---|---|---|
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

### NOT

| A | not A |
|---|---|
| False | True |
| True | False |

---

# 21. CONDITIONAL EXECUTION

Conditional execution allows a program to choose instructions based on a condition.

## 21.1 Basic If

```python
if condition:
    statement
```

## 21.2 If-Else

```python
if condition:
    statement1
else:
    statement2
```

## 21.3 If-Elif-Else

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

## 21.4 Nested If

```python
if condition1:
    if condition2:
        statement
```

## 21.5 Conditional Expression

```python
result = value1 if condition else value2
```

## 21.6 Match Case

```python
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
```

---

# 22. PROBLEM-SOLVING METHODOLOGY

A strong programmer does not immediately begin typing code after reading a problem.

The problem should first be understood.

## 22.1 Understand the Problem

Read the complete problem statement.

Identify the required result.

## 22.2 Identify the Inputs

Determine what values are provided.

## 22.3 Identify the Outputs

Determine what the program must return or display.

## 22.4 Identify Constraints

Find the valid ranges and restrictions.

## 22.5 Select the Logic

Choose the required operations and conditions.

## 22.6 Write the Algorithm

Represent the solution as steps.

## 22.7 Write Pseudocode

Describe the logic in a readable format.

## 22.8 Implement in Python

Convert the designed solution into code.

## 22.9 Review the Result

Check whether the output matches the requirement.

## 22.10 Improve the Solution

Improve clarity, validation, and organization.

### Problem-Solving Template

```text
Problem Name:

Problem Statement:

Input:

Output:

Constraints:

Logic:

Algorithm:

Pseudocode:

Python Implementation:

Explanation:
```

This template is a planning aid for understanding a problem. It is not an additional worksheet requirement for individual README files.

---

# 23. ALGORITHM DESIGN

Algorithm design means creating a logical procedure for solving a problem.

## 23.1 Algorithm Example – Even or Odd

1. Start.
2. Read number.
3. Calculate number modulo 2.
4. If remainder is zero, display Even.
5. Otherwise, display Odd.
6. Stop.

## 23.2 Algorithm Example – Largest of Two

1. Start.
2. Read A.
3. Read B.
4. Compare A and B.
5. If A is greater, display A.
6. Otherwise, display B.
7. Stop.

## 23.3 Algorithm Example – Percentage

1. Start.
2. Read obtained marks.
3. Read maximum marks.
4. Validate maximum marks.
5. Calculate percentage.
6. Display percentage.
7. Stop.

## 23.4 Algorithm Quality

An algorithm should be:

- Correct.
- Clear.
- Finite.
- Effective.
- Unambiguous.

---

# 24. FLOWCHART DESIGN

Flowcharts provide a visual explanation of program logic.

## 24.1 Basic Flowchart

```text
      START
        |
        v
       INPUT
        |
        v
      PROCESS
        |
        v
      OUTPUT
        |
        v
       STOP
```

## 24.2 Decision Flowchart

```text
         START
           |
           v
       Input Number
           |
           v
       Number > 0 ?
         /      \
       Yes      No
        |        |
        v        v
    Positive   Other
        |        |
        +---+----+
            |
            v
           STOP
```

## 24.3 Flowchart Design Guidelines

1. Use a clear Start symbol.
2. Use a clear End symbol.
3. Represent input and output correctly.
4. Use decision diamonds for conditions.
5. Label decision branches.
6. Connect steps with arrows.
7. Avoid unnecessary crossing lines.
8. Keep the process readable.
9. Ensure every path is understandable.
10. Verify that every path reaches an appropriate ending.

---

# 25. PSEUDOCODE DESIGN

Pseudocode allows programmers to describe a solution independently of Python syntax.

## 25.1 Sequential Pseudocode

```text
START

INPUT A
INPUT B

SUM = A + B

DISPLAY SUM

STOP
```

## 25.2 Conditional Pseudocode

```text
START

INPUT NUMBER

IF NUMBER > 0
    DISPLAY "POSITIVE"
ELSE
    DISPLAY "NOT POSITIVE"
END IF

STOP
```

## 25.3 Multiple Conditions

```text
START

INPUT MARKS

IF MARKS >= 90
    DISPLAY "A+"

ELSE IF MARKS >= 80
    DISPLAY "A"

ELSE IF MARKS >= 70
    DISPLAY "B"

ELSE
    DISPLAY "OTHER"

END IF

STOP
```

## 25.4 Pseudocode Best Practices

- Use descriptive variable names.
- Use clear instructions.
- Keep steps in logical order.
- Indent conditional blocks.
- Separate input, processing, and output.
- Avoid unnecessary details.
- Make the logic understandable before coding.

---

# 26. PYTHON IMPLEMENTATION PROCESS

An algorithm becomes a program through implementation.

## 26.1 Convert Inputs

Identify the expected input types.

```python
number = int(input("Enter a number: "))
```

## 26.2 Perform Operations

```python
result = number * 2
```

## 26.3 Apply Conditions

```python
if result > 0:
    print("Positive result")
else:
    print("Zero or negative result")
```

## 26.4 Organize Logic

Use functions to divide a program into smaller reusable units.

```python
def double_number(number):
    return number * 2


value = double_number(10)

print(value)
```

## 26.5 Review the Code

Check syntax, indentation, data types, and calculations.

---

# 27. PRACTICAL PROGRAMMING PROBLEMS

Practical programming problems help convert theoretical concepts into usable code.

The current Conditional Statements folder provides six practical problem categories.

## 27.1 Positive and Negative

Main concept:

Classify numbers based on their relationship with zero.

## 27.2 Even and Odd

Main concept:

Use the modulus operator to check divisibility by two.

## 27.3 Largest Number

Main concept:

Compare values and find the maximum.

## 27.4 Leap Year

Main concept:

Apply Gregorian calendar divisibility rules.

## 27.5 Grade Calculator

Main concept:

Classify marks and calculate student performance.

## 27.6 Voting Eligibility

Main concept:

Check whether an age satisfies a specified threshold.

### Important Learning Point

Each of these problems can be solved in different ways.

For example, the largest number problem can use:

- If-else.
- Nested if.
- If-elif-else.
- Conditional expressions.
- Lists.
- Built-in maximum functions.

Understanding multiple approaches improves programming flexibility.

---

# 28. STANDARD PYTHON FILE STRUCTURE

The Python practice programs in the Conditional Statements chapter use a consistent organization.

```text
PYTHON FILE
│
├── MODULE DOCSTRING
│
├── IMPORTS
│
├── CONSTANTS
│
├── HELPER FUNCTIONS
│
├── SECTION 1:
│   TWELVE TOPIC EXAMPLES
│
├── SECTION 2:
│   TWELVE SOLVED PROBLEMS
│
│   ├── Problem Functions
│   ├── SOLVED_PROBLEMS Mapping
│   ├── show_solved_problems()
│   └── run_solved_problems()
│
├── SECTION 3:
│   TEN UNSOLVED PRACTICE QUESTIONS
│
├── SECTION 4:
│   LEARNING CHECKLIST
│
├── SECTION 5:
│   MAIN MENU
│
└── PROGRAM EXECUTION
    │
    └── main()
```

## 28.1 Module Docstring

Describes the topic and file purpose.

## 28.2 Imports

Provides required Python functionality.

## 28.3 Constants

Stores fixed values used throughout the program.

## 28.4 Helper Functions

Contains reusable operations.

## 28.5 Topic Examples

Demonstrates the subject's basic concepts.

## 28.6 Solved Problems

Provides runnable problem implementations.

## 28.7 Mapping

Connects problem numbers and titles to their functions.

## 28.8 Unsolved Questions

Provides independent practice questions.

## 28.9 Learning Checklist

Lists the skills to review.

## 28.10 Main Menu

Provides navigation.

## 28.11 Program Execution

The standard Python entry-point structure is:

```python
if __name__ == "__main__":
    main()
```

---

# 29. DOCUMENTATION STRUCTURE

Each major learning folder has its own README.

The README should explain its own topic and provide the necessary learning material.

The parent README provides the overall navigation and chapter context.

## 29.1 Parent README

This README explains the complete Programming Fundamentals directory.

## 29.2 Folder README

Each child folder's README explains its subject.

## 29.3 Program Documentation

Python source files include module docstrings and comments where appropriate.

## 29.4 Documentation Naming

Use:

```text
README.md
```

## 29.5 Python File Naming

Use meaningful `.py` names.

Examples:

```text
01_if.py
01_if_else.py
01_nested_if.py
01_match_case.py
```

## 29.6 Markdown Formatting

Markdown can represent:

- Headings.
- Subheadings.
- Tables.
- Lists.
- Code blocks.
- Mathematical formulas.
- Links.
- Checklists.

## 29.7 Documentation Quality

Good documentation should:

- Explain concepts correctly.
- Use clear examples.
- Maintain consistent terminology.
- Follow the repository structure.
- Avoid unnecessary repetition.
- Explain code outputs.
- Include practical applications.
- Connect concepts to later topics.

---

# 30. COMMON PROGRAMMING ERRORS

Beginners may encounter different types of errors while writing Python programs.

## 30.1 SyntaxError

Occurs when code violates Python syntax.

Example:

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

## 30.2 IndentationError

Occurs when code blocks are not indented correctly.

Example:

```python
if number > 0:
print("Positive")
```

Correct:

```python
if number > 0:
    print("Positive")
```

## 30.3 NameError

Occurs when a name is not defined.

Example:

```python
print(total)
```

If `total` has not been defined, Python raises a `NameError`.

## 30.4 TypeError

Occurs when an operation is not supported for the involved types.

## 30.5 ValueError

Occurs when a value is inappropriate for an operation.

Example:

```python
number = int("hello")
```

## 30.6 ZeroDivisionError

Occurs when a number is divided by zero.

Example:

```python
result = 10 / 0
```

## 30.7 IndexError

Occurs when an invalid sequence index is accessed.

Example:

```python
numbers = [10, 20]

print(numbers[5])
```

## 30.8 KeyError

Occurs when a required dictionary key does not exist.

## 30.9 Debugging Approach

When an error occurs:

1. Read the error message.
2. Identify the file and line.
3. Check the operation.
4. Check variable values.
5. Check data types.
6. Check syntax.
7. Correct the problem.
8. Run the code again.

---

# 31. DEBUGGING FUNDAMENTALS

Debugging is part of programming.

A programmer should understand how to identify incorrect behaviour.

## 31.1 Syntax Problems

Check:

- Missing colons.
- Missing brackets.
- Incorrect quotation marks.
- Incorrect indentation.
- Misspelled keywords.

## 31.2 Logical Problems

A program may execute but produce an incorrect result.

Examples:

- Incorrect formula.
- Incorrect comparison.
- Incorrect condition order.
- Incorrect loop boundary.
- Incorrect variable used in calculation.

## 31.3 Data Type Problems

Check whether values are represented using suitable data types.

## 31.4 Input Problems

Check:

- Empty input.
- Invalid integer input.
- Invalid decimal input.
- Values outside expected ranges.

## 31.5 Debugging Example

Incorrect:

```python
marks = 85

if marks > 90:
    print("A+")
elif marks > 80:
    print("A")
```

For marks of 90, the first condition is false.

This example does not implement the intended inclusive boundary.

Correct:

```python
marks = 90

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
```

The comparison operator must reflect the required rules.

---

# 32. INPUT VALIDATION

Input validation checks whether information is acceptable before it is processed.

## 32.1 Integer Validation

```python
while True:
    try:
        age = int(input("Enter age: "))
        break

    except ValueError:
        print("Please enter a valid integer")
```

## 32.2 Non-Negative Validation

```python
while True:
    age = int(input("Enter age: "))

    if age >= 0:
        break

    print("Age cannot be negative")
```

## 32.3 Marks Validation

```python
marks = float(input("Enter marks: "))

if 0 <= marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")
```

## 32.4 Division Validation

```python
number1 = 10
number2 = 0

if number2 != 0:
    print(number1 / number2)
else:
    print("Cannot divide by zero")
```

## 32.5 Why Validation Matters

Validation improves:

- Program reliability.
- User experience.
- Data correctness.
- Calculation safety.
- Error handling.

---

# 33. CODE QUALITY AND BEST PRACTICES

Readable code is easier to understand and maintain.

## 33.1 Meaningful Variable Names

Prefer:

```python
student_name = "Amaan"
total_marks = 450
```

## 33.2 Consistent Indentation

Use consistent indentation throughout the file.

## 33.3 Functions

Separate reusable logic into functions.

## 33.4 Comments

Explain logic where it is not immediately clear.

## 33.5 Input Validation

Validate input before calculations.

## 33.6 Avoid Unnecessary Repetition

Use functions instead of repeating the same operation.

## 33.7 Keep Functions Focused

A function should generally perform one clearly defined task.

## 33.8 Avoid Unnecessary Complexity

Use a straightforward approach whenever it solves the problem correctly.

## 33.9 Use Appropriate Data Types

Choose a type based on the information being stored.

## 33.10 Write Readable Output

Use labels and formatting.

Example:

```python
print(f"Percentage: {percentage:.2f}%")
```

---

# 34. FUNCTIONS AND REUSABILITY

Functions help organize larger programs into smaller units.

## 34.1 Function Definition

```python
def greet():
    print("Hello Python")
```

## 34.2 Function Call

```python
greet()
```

## 34.3 Function With Parameters

```python
def greet(name):
    print("Hello", name)


greet("Amaan")
```

## 34.4 Return Values

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

## 34.5 Why Functions Matter

Functions help:

- Reduce repetition.
- Organize code.
- Improve readability.
- Simplify debugging.
- Support reusable algorithms.
- Divide large tasks into smaller tasks.

---

# 35. BASIC DATA STRUCTURES

Programming Fundamentals introduces collections that are useful in later DSA topics.

## 35.1 List

A list stores an ordered collection of values.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
```

## 35.2 Tuple

A tuple stores an ordered immutable collection.

```python
point = (10, 20)

print(point)
```

## 35.3 Set

A set stores unique elements.

```python
values = {10, 20, 10, 30}

print(values)
```

## 35.4 Dictionary

A dictionary stores key-value pairs.

```python
student = {
    "name": "Amaan",
    "marks": 85
}
```

## 35.5 Why Learn These Structures?

They are used for:

- Storing multiple values.
- Organizing records.
- Processing collections.
- Searching.
- Counting.
- Filtering.
- Representing relationships.

---

# 36. DSA FOUNDATION

Programming Fundamentals provides the knowledge needed to begin learning DSA.

## 36.1 What Is DSA?

DSA stands for Data Structures and Algorithms.

**Data Structures** organize and store information.

**Algorithms** define procedures used to solve problems.

## 36.2 Why Learn DSA?

DSA helps programmers understand:

- How data is stored.
- How data is accessed.
- How values are searched.
- How values are arranged.
- How algorithms are designed.
- How solutions are analyzed.
- How program performance can be improved.

## 36.3 Foundation Provided by This Repository

| Fundamental Concept | DSA Connection |
|---|---|
| Variables | Data representation |
| Data Types | Data organization |
| Operators | Mathematical operations |
| Conditions | Algorithm decisions |
| Algorithms | DSA procedures |
| Flowcharts | Algorithm visualization |
| Pseudocode | Algorithm planning |
| Lists | Array and sequence operations |
| Functions | Algorithm decomposition |

## 36.4 Important Beginner Algorithms

### Linear Traversal

Visit every element.

### Linear Search

Find a target value by checking elements one by one.

### Counting

Count items satisfying a condition.

### Filtering

Select matching values.

### Minimum Selection

Find the smallest value.

### Maximum Selection

Find the largest value.

## 36.5 Linear Search Example

```python
numbers = [10, 20, 30, 40, 50]

target = 30

found = False

for number in numbers:

    if number == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")
```

## 36.6 Counting Example

```python
numbers = [10, 15, 20, 25, 30]

count = 0

for number in numbers:

    if number % 2 == 0:
        count += 1

print("Even count:", count)
```

## 36.7 Filtering Example

```python
numbers = [10, -5, 20, -3, 30]

positive_numbers = []

for number in numbers:

    if number > 0:
        positive_numbers.append(number)

print(positive_numbers)
```

---

# 37. TIME COMPLEXITY INTRODUCTION

Time complexity describes how an algorithm's execution work grows as input size grows.

## 37.1 Constant Time – O(1)

A fixed number of operations.

```python
number = 10

result = number + 5

print(result)
```

## 37.2 Linear Time – O(n)

Work grows with input size.

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

## 37.3 Quadratic Time – O(n²)

A nested loop may process combinations of elements.

```python
numbers = [1, 2, 3]

for first in numbers:
    for second in numbers:
        print(first, second)
```

## 37.4 Logarithmic Time – O(log n)

Some algorithms reduce the problem size repeatedly.

Binary search is a common example when applied to a sorted collection.

## 37.5 Common Complexity Classes

| Complexity | General Meaning |
|---|---|
| O(1) | Constant |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(2ⁿ) | Exponential |

---

# 38. SPACE COMPLEXITY INTRODUCTION

Space complexity describes the memory required by a program or algorithm.

## 38.1 Constant Space

```python
number = 10
result = number * 2
```

A fixed number of variables is used.

## 38.2 Linear Space

```python
numbers = []

for number in range(100):
    numbers.append(number)
```

The list grows with the number of stored values.

## 38.3 Important Distinction

Input storage and additional memory should be considered separately when analyzing algorithms.

For example, traversing an existing list does not necessarily require another list.

Creating a filtered list requires additional memory.

---

# 39. REAL-WORLD APPLICATIONS

Programming Fundamentals is used across many software applications.

## 39.1 Web Development

Applications use variables, conditions, and operators to process user input.

## 39.2 Backend Development

Backend systems validate information, process requests, and generate responses.

## 39.3 Banking Systems

Banking applications perform calculations, validate balances, and make decisions.

## 39.4 Student Management Systems

Academic software calculates marks, percentages, averages, and results.

## 39.5 E-Commerce Applications

Shopping software calculates prices, discounts, taxes, and order totals.

## 39.6 Data Processing

Data programs use variables, data types, expressions, and conditional statements.

## 39.7 Automation

Python programs automate repetitive tasks.

## 39.8 Artificial Intelligence

AI applications rely on programming fundamentals for data processing and implementation.

## 39.9 Machine Learning

Machine learning programs use variables, calculations, logical operations, and algorithms.

## 39.10 Software Development

All software development relies on programming logic and structured problem solving.

---

# 40. RECOMMENDED LEARNING SEQUENCE

Follow this order without skipping the foundational topics.

| Sequence | Folder | Focus |
|---:|---|---|
| 01 | Introduction | Understand Python |
| 02 | Flowcharts and Algorithms | Design solutions |
| 03 | Pseudocode and Problem Solving | Express logic |
| 04 | Variables and Data Types | Represent data |
| 05 | Operators and Expressions | Perform operations |
| 06 | Conditional Statements | Make decisions |

## 40.1 Study Introduction First

Learn to write and execute basic Python programs.

## 40.2 Understand Algorithms

Learn to describe solutions before coding.

## 40.3 Learn Pseudocode

Convert problem logic into structured instructions.

## 40.4 Learn Variables and Data Types

Understand how information is stored and represented.

## 40.5 Learn Operators

Understand how calculations and comparisons work.

## 40.6 Learn Conditional Statements

Apply decision-making logic to practical problems.

## 40.7 Complete the Full Sequence

Review all six folders after completing them.

---

# 41. HOW TO STUDY EVERY TOPIC

Use the same learning method throughout the repository.

## Step 1 – Read the README

Start by reading the topic introduction.

## Step 2 – Understand the Concept

Learn the meaning and purpose of the topic.

## Step 3 – Learn the Syntax

Understand how the Python statement is written.

## Step 4 – Study the Examples

Read the examples and identify the underlying logic.

## Step 5 – Understand the Python File

Study the executable program.

## Step 6 – Run the Program

Execute the Python file.

## Step 7 – Understand the Solved Problems

Study the problem statement, logic, and implementation.

## Step 8 – Attempt the Unsolved Questions

Try solving the questions independently.

## Step 9 – Review Mistakes

Understand common syntax and logical mistakes.

## Step 10 – Review the DSA Connection

Identify which problem-solving concepts are introduced.

## Step 11 – Review Complexity

Understand the time and space requirements.

## Step 12 – Complete the Learning Checklist

Review the concepts before moving ahead.

---

# 42. HOW TO RUN PYTHON PROGRAMS

Python files are executed through the Python interpreter.

## 42.1 Check Python Version

```powershell
python --version
```

Alternatively:

```powershell
py --version
```

## 42.2 Navigate to the Project

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"
```

## 42.3 Navigate to a Topic Folder

Example:

```powershell
cd "PYTHON\Programming-Fundamentals\01-Introduction"
```

## 42.4 Run a Python Program

```powershell
python filename.py
```

## 42.5 Run Using the Windows Launcher

```powershell
py filename.py
```

## 42.6 Navigate Between Folders

Move to the parent directory:

```powershell
cd ..
```

Navigate into another folder:

```powershell
cd "04-Variables-Data-Types"
```

## 42.7 Important Terminal Commands

| Command | Purpose |
|---|---|
| `cd` | Change directory |
| `dir` | Display directory contents |
| `cd ..` | Move to parent directory |
| `cls` | Clear Windows terminal |
| `python --version` | Check Python version |
| `python file.py` | Execute Python file |

---

# 43. GITHUB REPOSITORY WORKFLOW

The DSA-Python repository is maintained using Git and GitHub.

Git helps track project changes.

GitHub provides a remote location for storing the repository.

## 43.1 Repository Details

**Repository Name:** DSA-Python

**Repository URL:**

https://github.com/as-amaan-109/DSA-Python

**Programming Fundamentals Directory:**

```text
PYTHON/Programming-Fundamentals/
```

## 43.2 Check Repository Status

```powershell
git status
```

## 43.3 Stage a Specific Folder

```powershell
git add "PYTHON/Programming-Fundamentals"
```

## 43.4 Review Staged Changes

```powershell
git status
```

## 43.5 Commit Changes

```powershell
git commit -m "Update programming fundamentals documentation"
```

## 43.6 Push to GitHub

```powershell
git push origin main
```

## 43.7 Recommended Workflow

```text
MAKE CHANGES
     |
     v
CHECK STATUS
     |
     v
STAGE FILES
     |
     v
REVIEW CHANGES
     |
     v
CREATE COMMIT
     |
     v
PUSH TO GITHUB
```

## 43.8 Important Git Commands

| Command | Purpose |
|---|---|
| `git status` | View repository status |
| `git add` | Stage changes |
| `git commit -m` | Create a commit |
| `git push` | Push changes |
| `git pull` | Fetch and integrate remote changes |
| `git log` | View commit history |
| `git diff` | Review unstaged differences |

---

# 44. FILE NAMING CONVENTION

The repository follows numbered and descriptive folder names.

## 44.1 Main Folders

```text
01-Introduction
02-Flowcharts-Algorithms
03-Pseudocode-Problem-Solving
04-Variables-Data-Types
05-Operators-Expressions
06-Conditional-Statements
```

## 44.2 Documentation Files

Each folder contains a README where applicable.

```text
README.md
```

## 44.3 Python Files

Python files use descriptive filenames.

Examples:

```text
01_if.py
01_if_else.py
01_if_elif_else.py
01_nested_if.py
01_ternary_operator.py
01_match_case.py
```

## 44.4 Why Consistent Naming Matters

Consistent naming helps:

- Locate source code.
- Identify topics.
- Organize GitHub folders.
- Maintain documentation.
- Understand program purpose.
- Avoid confusing filenames.

---

# 45. DOCUMENTATION MAP

The Programming Fundamentals parent README is the main navigation page.

The following table identifies the expected documentation locations based on the current folder structure.

| Path | Purpose |
|---|---|
| `README.md` | Programming Fundamentals overview |
| `01-Introduction/README.md` | Introduction to programming |
| `02-Flowcharts-Algorithms/README.md` | Algorithms and flowcharts |
| `03-Pseudocode-Problem-Solving/README.md` | Pseudocode and problem solving |
| `04-Variables-Data-Types/README.md` | Variables and types |
| `05-Operators-Expressions/README.md` | Operators and expressions |
| `06-Conditional-Statements/README.md` | Conditional Statements chapter |
| `06-Conditional-Statements/01-If-Statement/README.md` | If statement |
| `06-Conditional-Statements/02-If-Else/README.md` | If-Else |
| `06-Conditional-Statements/03-If-Elif-Else/README.md` | If-Elif-Else |
| `06-Conditional-Statements/04-Nested-If/README.md` | Nested If |
| `06-Conditional-Statements/05-Conditional-Expressions/README.md` | Conditional expressions |
| `06-Conditional-Statements/06-Practice-Problems/README.md` | Practice problems overview |
| `06-Conditional-Statements/07-Match-Case/README.md` | Match Case |

The six main folder names are based on the current repository structure. Individual subtopic organization should continue to follow the files actually present in each folder.

---

# 46. PROGRAMMING FUNDAMENTALS REVISION

This section summarizes the most important concepts from the six learning areas.

## 46.1 Programming

Programming means creating instructions for a computer.

## 46.2 Python

Python is a high-level, general-purpose programming language.

## 46.3 Algorithm

An algorithm is a finite sequence of steps used to solve a problem.

## 46.4 Flowchart

A flowchart is a visual representation of a process.

## 46.5 Pseudocode

Pseudocode describes program logic in readable structured instructions.

## 46.6 Variable

A variable is a name that refers to a value.

## 46.7 Data Type

A data type represents the category of a value.

## 46.8 Operator

An operator performs an operation.

## 46.9 Expression

An expression evaluates to a value.

## 46.10 Condition

A condition evaluates to a Boolean result.

## 46.11 If Statement

Executes a block when a condition is true.

## 46.12 If-Else

Provides two execution alternatives.

## 46.13 If-Elif-Else

Provides multiple conditional branches.

## 46.14 Nested If

Places a condition inside another conditional block.

## 46.15 Conditional Expression

Selects one value based on a condition.

## 46.16 Match Case

Matches values and structures against patterns.

---

# 47. COMPLETE LEARNING CHECKLIST

Use this checklist to review the complete Programming Fundamentals section.

## 47.1 Introduction

- [ ] I understand what programming is.
- [ ] I understand what Python is.
- [ ] I understand programming languages.
- [ ] I understand source code.
- [ ] I understand the role of an interpreter.
- [ ] I can write a Hello World program.
- [ ] I can use `print()`.
- [ ] I can use comments.
- [ ] I can use escape sequences.
- [ ] I can save Python files.
- [ ] I can execute Python files.
- [ ] I can identify basic syntax errors.

## 47.2 Flowcharts and Algorithms

- [ ] I understand the meaning of an algorithm.
- [ ] I understand algorithm characteristics.
- [ ] I can write simple algorithms.
- [ ] I understand flowchart symbols.
- [ ] I can identify the Start and End symbols.
- [ ] I can identify Process symbols.
- [ ] I can identify Input and Output symbols.
- [ ] I can identify Decision symbols.
- [ ] I can draw a simple flowchart.
- [ ] I understand algorithm representation.

## 47.3 Pseudocode and Problem Solving

- [ ] I understand pseudocode.
- [ ] I can identify input values.
- [ ] I can identify expected output.
- [ ] I can understand a problem statement.
- [ ] I can divide a problem into smaller steps.
- [ ] I can write an algorithm.
- [ ] I can write pseudocode.
- [ ] I can convert pseudocode into Python.
- [ ] I understand input, process, and output.

## 47.4 Variables and Data Types

- [ ] I understand variables.
- [ ] I can assign values.
- [ ] I understand variable naming.
- [ ] I understand integers.
- [ ] I understand floats.
- [ ] I understand complex numbers.
- [ ] I understand strings.
- [ ] I understand Booleans.
- [ ] I understand lists.
- [ ] I understand tuples.
- [ ] I understand sets.
- [ ] I understand dictionaries.
- [ ] I understand None.
- [ ] I can use `type()`.
- [ ] I can perform type conversion.
- [ ] I can accept typed input.

## 47.5 Operators and Expressions

- [ ] I understand arithmetic operators.
- [ ] I understand comparison operators.
- [ ] I understand logical operators.
- [ ] I understand assignment operators.
- [ ] I understand membership operators.
- [ ] I understand identity operators.
- [ ] I understand bitwise operators.
- [ ] I understand operands.
- [ ] I understand expressions.
- [ ] I understand operator precedence.
- [ ] I can evaluate arithmetic expressions.
- [ ] I can evaluate logical expressions.

## 47.6 Conditional Statements

- [ ] I understand the if statement.
- [ ] I can use if-else.
- [ ] I can use if-elif-else.
- [ ] I can write nested if statements.
- [ ] I can use conditional expressions.
- [ ] I can use match-case.
- [ ] I understand literal patterns.
- [ ] I understand wildcard patterns.
- [ ] I understand OR patterns.
- [ ] I understand guard conditions.
- [ ] I understand tuple patterns.
- [ ] I understand list patterns.

## 47.7 Practical Programming

- [ ] I can classify positive and negative numbers.
- [ ] I can identify even and odd numbers.
- [ ] I can find the largest number.
- [ ] I can check leap years.
- [ ] I can calculate grades.
- [ ] I can calculate percentages.
- [ ] I can check age-based eligibility.
- [ ] I can write reusable functions.
- [ ] I can validate input.
- [ ] I can generate formatted output.

## 47.8 DSA Foundation

- [ ] I understand basic algorithm design.
- [ ] I understand sequential processing.
- [ ] I understand conditional processing.
- [ ] I understand list traversal.
- [ ] I understand counting.
- [ ] I understand filtering.
- [ ] I understand linear search.
- [ ] I understand minimum and maximum selection.
- [ ] I understand basic time complexity.
- [ ] I understand basic space complexity.

---

# 48. CHAPTER COMPLETION SUMMARY

Programming Fundamentals is the starting point of the DSA-Python repository.

It introduces the knowledge required to understand and write Python programs.

The six major folders are:

**01 – Introduction**

Introduces programming, Python, syntax, print statements, comments, and basic execution.

**02 – Flowcharts and Algorithms**

Introduces algorithm design, flowchart symbols, and visual representation of solutions.

**03 – Pseudocode and Problem Solving**

Develops structured problem-solving logic before actual implementation.

**04 – Variables and Data Types**

Explains how Python represents and stores different types of information.

**05 – Operators and Expressions**

Explains calculations, comparisons, logical operations, and expression evaluation.

**06 – Conditional Statements**

Explains decision-making using if, if-else, if-elif-else, nested if, conditional expressions, match-case, and practical problems.

### Skills Developed

After completing this section, you should be able to:

- Understand programming concepts.
- Understand Python syntax.
- Design simple algorithms.
- Draw basic flowcharts.
- Write pseudocode.
- Identify input and output.
- Use variables.
- Work with data types.
- Convert data types.
- Use operators.
- Evaluate expressions.
- Understand Boolean logic.
- Write conditional statements.
- Solve beginner programming problems.
- Organize Python programs.
- Debug basic errors.
- Understand introductory DSA concepts.

---

# 49. FINAL LEARNING GUIDANCE

Programming Fundamentals should be studied carefully.

Every advanced programming topic depends on the ability to understand basic instructions, data, operations, and logic.

Do not skip the early topics because they appear simple.

The purpose of learning these concepts is to build a strong foundation that supports future Python programming and DSA.

### Remember This Learning Process

```text
UNDERSTAND THE CONCEPT
          |
          v
STUDY THE THEORY
          |
          v
LEARN THE SYNTAX
          |
          v
UNDERSTAND THE LOGIC
          |
          v
WRITE PYTHON CODE
          |
          v
EXECUTE THE PROGRAM
          |
          v
REVIEW THE RESULT
          |
          v
IMPROVE YOUR SOLUTION
```

### Final Advice

Focus on understanding why each statement is used.

Do not memorize code without understanding its purpose.

Learn how to convert a problem into logical steps, how to represent those steps through algorithms and pseudocode, and how to implement them using Python.

Maintain the folder structure and documentation consistently.

Use the individual README files as detailed study guides and this parent README as the main reference for the entire Programming Fundamentals section.

**Strong programming fundamentals are the first step towards becoming a good software developer and solving Data Structures and Algorithms problems confidently.**

**Build your logic first. Build your Python skills next. Build your DSA foundation step by step.**

