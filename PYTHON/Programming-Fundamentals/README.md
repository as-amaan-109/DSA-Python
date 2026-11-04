

# PYTHON PROGRAMMING FUNDAMENTALS

## Complete Learning Roadmap and Documentation

---

## 1. Introduction

Welcome to the **Programming Fundamentals** section of the DSA-Python repository.

This section establishes the foundation of programming using Python.

Before learning Data Structures and Algorithms, it is important to understand how programs work, how problems are solved, how data is stored, how operations are performed, and how a program makes decisions.

Programming Fundamentals introduces these concepts step by step.

This section is organized into six major learning areas:

1. Introduction
2. Flowcharts and Algorithms
3. Pseudocode and Problem Solving
4. Variables and Data Types
5. Operators and Expressions
6. Conditional Statements

Each folder covers a different part of the programming learning process.

The goal is not just to learn Python syntax.

The goal is to develop the ability to understand a problem, design a solution, write Python code, identify mistakes, and improve the solution.

### What You Will Learn

- What programming is.
- How programming languages work.
- How to write and execute Python programs.
- How to understand program structure.
- How to represent algorithms.
- How to create flowcharts.
- How to write pseudocode.
- How to approach programming problems.
- How variables store information.
- How Python data types work.
- How operators perform calculations.
- How expressions are evaluated.
- How conditional statements control program execution.
- How to build practical Python programs.
- How to develop problem-solving skills.

---

## 2. Purpose of This Repository Section

The purpose of Programming Fundamentals is to build a strong foundation before moving to advanced Python programming and DSA.

Programming requires more than knowing individual commands.

A programmer needs to understand:

1. The problem.
2. The required input.
3. The expected output.
4. The logic behind the solution.
5. The sequence of operations.
6. The conditions that affect execution.
7. The data involved.
8. The final result.

This section introduces these ideas through organized learning material and executable Python programs.

### Learning Approach

The learning sequence starts with basic programming concepts.

Then it moves towards algorithm design, variables, data types, operators, and conditional statements.

This order helps connect theoretical understanding with practical implementation.

### Main Learning Philosophy

**Understand → Plan → Write → Execute → Improve**

- Understand what the problem asks.
- Plan the solution using logical steps.
- Write the solution in Python.
- Execute the program.
- Review the result and improve the code.

---

## 3. Complete Folder Structure

The Programming Fundamentals section contains six main folders.

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

### Folder Overview

| No. | Folder | Main Learning Area |
|---:|---|---|
| 01 | `01-Introduction` | Introduction to programming and Python |
| 02 | `02-Flowcharts-Algorithms` | Algorithms and flowchart representation |
| 03 | `03-Pseudocode-Problem-Solving` | Pseudocode and problem-solving logic |
| 04 | `04-Variables-Data-Types` | Variables and Python data types |
| 05 | `05-Operators-Expressions` | Operators and expressions |
| 06 | `06-Conditional-Statements` | Decision-making and conditional execution |

### Recommended Learning Order

```text
PROGRAMMING FUNDAMENTALS
          |
          v
01. INTRODUCTION
          |
          v
02. FLOWCHARTS AND ALGORITHMS
          |
          v
03. PSEUDOCODE AND PROBLEM SOLVING
          |
          v
04. VARIABLES AND DATA TYPES
          |
          v
05. OPERATORS AND EXPRESSIONS
          |
          v
06. CONDITIONAL STATEMENTS
          |
          v
PYTHON PROGRAMMING PRACTICE
```

Follow this order to build your understanding gradually.

---

# PART 1: INTRODUCTION TO PROGRAMMING

## 4. Folder 01 – Introduction

**Folder:** `01-Introduction/`

This folder introduces the basic concepts of programming and Python.

Before writing complex programs, a learner must understand what a program is, what programming means, and how Python code is executed.

### 4.1 Introduction to Programming

Programming is the process of writing instructions that tell a computer how to perform specific tasks.

A computer follows instructions written using a programming language.

A program can perform activities such as:

- Performing calculations.
- Processing information.
- Displaying output.
- Accepting user input.
- Managing files.
- Automating tasks.
- Making decisions.

### 4.2 What Is Python?

Python is a high-level, general-purpose programming language.

It is known for its readable syntax and broad range of applications.

Python is used in:

- Software development.
- Web development.
- Automation.
- Data analysis.
- Artificial intelligence.
- Machine learning.
- Scientific computing.
- Scripting.
- Backend development.

### 4.3 Basic Python Program

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

The `print()` function displays information on the screen.

### 4.4 Understanding Program Execution

A basic Python program follows this process:

1. Write Python code.
2. Save the code in a `.py` file.
3. Open the terminal.
4. Execute the file.
5. Python processes the instructions.
6. The program displays the result.

### 4.5 Important Programming Concepts

| Concept | Description |
|---|---|
| Program | A collection of instructions |
| Programming | Writing instructions for a computer |
| Programming Language | Language used to write programs |
| Source Code | Human-readable program instructions |
| Python File | File containing Python code |
| Interpreter | Software that executes Python code |
| Output | Information produced by a program |
| Input | Information supplied to a program |
| Syntax | Rules for writing valid code |
| Debugging | Finding and correcting errors |

### 4.6 What You Should Understand

After completing this folder, you should understand the fundamental purpose of programming and how to write, save, and execute basic Python code.

Refer to the folder's individual README for its complete topic explanations and practical examples.

### Folder Location

```text
Programming-Fundamentals/
└── 01-Introduction/
```

---

# PART 2: FLOWCHARTS AND ALGORITHMS

## 5. Folder 02 – Flowcharts and Algorithms

**Folder:** `02-Flowcharts-Algorithms/`

This folder introduces the process of designing solutions before writing code.

Algorithms and flowcharts help organize problem-solving steps.

### 5.1 What Is an Algorithm?

An algorithm is a finite sequence of well-defined steps used to solve a problem.

An algorithm describes the logic needed to obtain a result.

### Example: Add Two Numbers

**Algorithm:**

1. Start.
2. Read the first number.
3. Read the second number.
4. Add both numbers.
5. Display the result.
6. Stop.

### Python Implementation

```python
number1 = 10
number2 = 20

result = number1 + number2

print("Sum:", result)
```

Output:

```text
Sum: 30
```

### 5.2 Characteristics of an Algorithm

A good algorithm should have:

- Clearly defined inputs.
- Clearly defined outputs.
- Definite instructions.
- Finite execution.
- Effective operations.

### 5.3 What Is a Flowchart?

A flowchart is a visual representation of an algorithm.

It represents the steps of a process using symbols connected by arrows.

Flowcharts help programmers understand the sequence of operations before implementation.

### 5.4 Common Flowchart Symbols

| Symbol | Meaning |
|---|---|
| Oval | Start or End |
| Rectangle | Process |
| Parallelogram | Input or Output |
| Diamond | Decision |
| Arrow | Flow direction |
| Connector | Connects different flowchart sections |

### 5.5 Example: Add Two Numbers Flowchart

```text
          START
            |
            v
     Input Number 1
            |
            v
     Input Number 2
            |
            v
       Sum = A + B
            |
            v
       Display Sum
            |
            v
           STOP
```

### 5.6 Algorithm vs Flowchart

| Algorithm | Flowchart |
|---|---|
| Written sequence of steps | Visual representation |
| Uses natural language or structured steps | Uses graphical symbols |
| Easy to write and modify | Easy to visualize |
| Explains solution logic | Shows execution flow |

### 5.7 Why Algorithms Are Important

Algorithms help programmers:

- Understand a problem.
- Break a problem into steps.
- Organize instructions.
- Identify possible errors.
- Improve solution efficiency.
- Prepare for coding.
- Understand DSA concepts.

### 5.8 Why Flowcharts Are Important

Flowcharts help programmers:

- Visualize program execution.
- Understand decision points.
- Identify input and output.
- Track process flow.
- Explain program logic.
- Communicate solutions clearly.

### 5.9 What You Should Understand

After completing this folder, you should be able to describe a problem using an algorithm and represent its basic execution using flowchart symbols.

Refer to the folder's README for complete explanations of its flowchart and algorithm topics.

### Folder Location

```text
Programming-Fundamentals/
└── 02-Flowcharts-Algorithms/
```

---

# PART 3: PSEUDOCODE AND PROBLEM SOLVING

## 6. Folder 03 – Pseudocode and Problem Solving

**Folder:** `03-Pseudocode-Problem-Solving/`

This folder develops the ability to design program logic in a structured and understandable way.

Before converting a problem into Python code, it is useful to describe the solution in simple steps.

Pseudocode provides this intermediate representation.

### 6.1 What Is Pseudocode?

Pseudocode is an informal, structured way of describing the logic of a program using readable statements.

It resembles programming instructions but does not follow the strict syntax of a specific programming language.

### Example: Add Two Numbers

**Pseudocode:**

```text
START

INPUT number1
INPUT number2

sum = number1 + number2

DISPLAY sum

STOP
```

### Python Implementation

```python
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

sum_value = number1 + number2

print("Sum:", sum_value)
```

### 6.2 What Is Problem Solving?

Problem solving is the process of understanding a problem and designing a logical solution.

In programming, it includes:

1. Understanding the problem statement.
2. Identifying the inputs.
3. Identifying the expected outputs.
4. Understanding the constraints.
5. Designing the algorithm.
6. Writing pseudocode.
7. Implementing the solution.
8. Evaluating the result.

### 6.3 Input, Process, and Output

A basic program can be understood through three stages.

**Input:** Information supplied to the program.

**Process:** Operations performed on the input.

**Output:** Result produced by the program.

### Example

Problem: Calculate the area of a rectangle.

Input:

```text
Length = 10
Width = 5
```

Process:

\[
Area = Length \times Width
\]

Output:

```text
Area = 50
```

### 6.4 Algorithm vs Pseudocode vs Python Code

| Algorithm | Pseudocode | Python Code |
|---|---|---|
| Describes solution steps | Represents logic in a structured form | Implements the solution |
| Focuses on the procedure | Focuses on understandable instructions | Follows Python syntax |
| Language-independent | Generally language-independent | Python-specific |

### 6.5 Important Problem-Solving Questions

Before writing code, ask:

- What is the problem asking?
- What information is provided?
- What output is required?
- What calculations are necessary?
- What conditions must be checked?
- Is repetition required?
- Which data structure is useful?
- Can the logic be divided into smaller steps?
- What happens when the input is invalid?

### 6.6 What You Should Understand

After completing this folder, you should be able to plan a solution before writing Python code.

You should be comfortable converting a simple problem into an algorithm, pseudocode, and Python implementation.

### Folder Location

```text
Programming-Fundamentals/
└── 03-Pseudocode-Problem-Solving/
```

---

# PART 4: VARIABLES AND DATA TYPES

## 7. Folder 04 – Variables and Data Types

**Folder:** `04-Variables-Data-Types/`

Variables and data types are fundamental building blocks of Python programming.

Variables store information, while data types determine the kind of information represented by a value.

### 7.1 What Is a Variable?

A variable is a named reference used to store and access a value.

### Example

```python
name = "Amaan"
age = 22
marks = 85.5
```

Here:

- `name` refers to a string value.
- `age` refers to an integer value.
- `marks` refers to a floating-point value.

### 7.2 Variable Assignment

Python uses the assignment operator `=` to assign values.

```python
number = 10

print(number)
```

Output:

```text
10
```

### 7.3 What Is a Data Type?

A data type describes the kind of value represented by an object.

Python includes several built-in data types.

### 7.4 Common Python Data Types

| Data Type | Description | Example |
|---|---|---|
| `int` | Integer | `25` |
| `float` | Floating-point number | `10.5` |
| `complex` | Complex number | `2 + 3j` |
| `str` | String | `"Python"` |
| `bool` | Boolean | `True` |
| `list` | Mutable sequence | `[10, 20, 30]` |
| `tuple` | Immutable sequence | `(10, 20, 30)` |
| `set` | Collection of unique values | `{10, 20, 30}` |
| `dict` | Key-value collection | `{"name": "Amaan"}` |
| `NoneType` | Absence of a value | `None` |

### 7.5 Checking Data Types

Python provides the `type()` function.

```python
name = "Amaan"
age = 22
marks = 85.5
is_student = True

print(type(name))
print(type(age))
print(type(marks))
print(type(is_student))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### 7.6 Type Conversion

Type conversion changes a value from one data type to another when the conversion is valid.

Common conversion functions:

| Function | Purpose |
|---|---|
| `int()` | Convert to integer |
| `float()` | Convert to floating-point |
| `str()` | Convert to string |
| `bool()` | Convert to Boolean |

### Example

```python
number = "100"

converted_number = int(number)

print(converted_number)
print(type(converted_number))
```

Output:

```text
100
<class 'int'>
```

### 7.7 Variable Naming

Python variable names should be meaningful and follow naming rules.

Good examples:

```python
student_name = "Amaan"
total_marks = 450
average_marks = 90.0
```

Avoid unclear names when meaningful names are possible.

### 7.8 What You Should Understand

After completing this folder, you should understand how to create variables, assign values, identify data types, and perform basic type conversions.

Refer to the folder's README for complete topic-specific documentation.

### Folder Location

```text
Programming-Fundamentals/
└── 04-Variables-Data-Types/
```

---

# PART 5: OPERATORS AND EXPRESSIONS

## 8. Folder 05 – Operators and Expressions

**Folder:** `05-Operators-Expressions/`

Operators are symbols or keywords used to perform operations on values.

Expressions combine values and operators to produce results.

This section develops an understanding of how Python performs calculations and evaluates expressions.

### 8.1 What Is an Operator?

An operator performs an operation on one or more operands.

Example:

```python
result = 10 + 5
```

Here:

- `10` and `5` are operands.
- `+` is an operator.
- `result` receives the calculated value.

### 8.2 Arithmetic Operators

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
```

Output:

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

### 8.3 Comparison Operators

Comparison operators compare values and produce Boolean results.

```python
a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```

### 8.4 Logical Operators

Python provides three main logical operators:

- `and`
- `or`
- `not`

Example:

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

### 8.5 Assignment Operators

Assignment operators assign values to variables.

Common examples:

| Operator | Description |
|---|---|
| `=` | Assign |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `//=` | Floor divide and assign |
| `%=` | Modulus and assign |
| `**=` | Exponentiate and assign |

### 8.6 Membership Operators

Membership operators check whether a value is present in a collection.

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(40 not in numbers)
```

Output:

```text
True
True
```

### 8.7 Identity Operators

Identity operators check whether two references point to the same object.

- `is`
- `is not`

Example:

```python
a = None

print(a is None)
```

Output:

```text
True
```

### 8.8 What Is an Expression?

An expression is a combination of values, variables, operators, and function calls that evaluates to a result.

Example:

```python
result = (10 + 5) * 2
```

The expression evaluates to 30.

### 8.9 Operator Precedence

Operator precedence determines the order in which operations are evaluated.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication is evaluated before addition.

Parentheses can be used to make the intended evaluation order clear.

### 8.10 What You Should Understand

After completing this folder, you should understand how operators work, how expressions are evaluated, and how to perform arithmetic and logical operations in Python.

### Folder Location

```text
Programming-Fundamentals/
└── 05-Operators-Expressions/
```

---

# PART 6: CONDITIONAL STATEMENTS

## 9. Folder 06 – Conditional Statements

**Folder:** `06-Conditional-Statements/`

**Documentation:** `06-Conditional-Statements/README.md`

This folder focuses on decision-making in Python.

It introduces several conditional structures and six practical programming problem categories.

### 9.1 Topics Covered

| No. | Folder | Main Concept |
|---:|---|---|
| 01 | `01-If-Statement` | Basic conditional execution |
| 02 | `02-If-Else` | Two-way decisions |
| 03 | `03-If-Elif-Else` | Multiple decision branches |
| 04 | `04-Nested-If` | Dependent conditions |
| 05 | `05-Conditional-Expressions` | Conditional expressions |
| 06 | `06-Practice-Problems` | Practical problems |
| 07 | `07-Match-Case` | Structural pattern matching |

### 9.2 If Statement

```python
number = 10

if number > 0:
    print("Positive")
```

### 9.3 If-Else

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 9.4 If-Elif-Else

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

### 9.5 Nested If

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Conditions satisfied")
    else:
        print("ID required")
else:
    print("Age condition not satisfied")
```

### 9.6 Conditional Expression

```python
number = 12

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

### 9.7 Match Case

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

### 9.8 Practical Problems Included

The practice section contains six programming topics.

| No. | Problem | Main Concept |
|---:|---|---|
| 01 | Positive and Negative | Number classification |
| 02 | Even and Odd | Divisibility |
| 03 | Largest Number | Comparison |
| 04 | Leap Year | Divisibility rules |
| 05 | Grade Calculator | Grade classification |
| 06 | Voting Eligibility | Age-based classification |

### 9.9 Standard Practice Program Format

Every practice program contains:

1. Module docstring.
2. Imports.
3. Constants where needed.
4. Helper functions.
5. Twelve topic examples.
6. Twelve solved problems.
7. Solved problem mapping.
8. Ten unsolved questions.
9. Learning checklist.
10. Interactive main menu.
11. Program execution block.

### 9.10 Common Interactive Menu

```text
=============================================================
                       PYTHON TOPIC
=============================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

### 9.11 What You Should Understand

After completing this folder, you should be able to make decisions using conditional statements and apply them to practical Python problems.

You should also understand how conditions work with loops, functions, lists, and basic problem-solving algorithms.

### Folder Location

```text
Programming-Fundamentals/
└── 06-Conditional-Statements/
```

---

# PART 7: HOW THE SIX AREAS CONNECT

## 10. Complete Programming Learning Process

The six folders are connected.

Each folder develops a particular skill required for writing programs.

### Step 1: Introduction

Understand what programming is and how Python programs execute.

### Step 2: Flowcharts and Algorithms

Learn how to design a solution and represent the steps.

### Step 3: Pseudocode and Problem Solving

Learn how to express logical instructions before implementation.

### Step 4: Variables and Data Types

Learn how to represent and store information.

### Step 5: Operators and Expressions

Learn how to perform calculations and evaluate expressions.

### Step 6: Conditional Statements

Learn how to make decisions based on conditions.

### Connected Example

Consider a problem that calculates whether a student passed or failed.

**Problem:** Accept marks and display PASS or FAIL.

**Step 1 – Understand the problem**

The program must accept marks and classify the result.

**Step 2 – Identify input**

Marks obtained by the student.

**Step 3 – Identify output**

PASS or FAIL.

**Step 4 – Design the algorithm**

1. Start.
2. Read marks.
3. Check whether marks are at least 40.
4. Display PASS if true.
5. Otherwise, display FAIL.
6. Stop.

**Step 5 – Write pseudocode**

```text
START

INPUT marks

IF marks >= 40
    DISPLAY PASS
ELSE
    DISPLAY FAIL
END IF

STOP
```

**Step 6 – Implement in Python**

```python
marks = int(input("Enter marks: "))

if marks >= 40:
    print("PASS")
else:
    print("FAIL")
```

This example connects problem understanding, algorithm design, pseudocode, variables, comparison operators, and conditional statements.

---

## 11. Important Python Concepts Reference

| Concept | Use |
|---|---|
| `print()` | Display output |
| `input()` | Accept user input |
| `type()` | Identify a value's type |
| `int()` | Convert to integer |
| `float()` | Convert to floating-point |
| `str()` | Convert to string |
| `bool()` | Convert to Boolean |
| `sum()` | Calculate sum |
| `len()` | Count elements |
| `min()` | Find minimum |
| `max()` | Find maximum |
| `range()` | Generate integer sequences |
| `append()` | Add an item to a list |
| `if` | One-way conditional decision |
| `else` | Alternative conditional block |
| `elif` | Additional conditional branch |
| `match` | Start pattern matching |
| `case` | Define a matching pattern |
| `break` | Exit a loop |
| `continue` | Skip to the next loop iteration |
| `return` | Return a value from a function |

---

## 12. Common Programming Mistakes

Beginners may encounter errors while learning programming fundamentals.

Understanding these mistakes helps improve coding skills.

### 12.1 Syntax Errors

Syntax errors occur when Python code does not follow valid language syntax.

Example:

```python
if number > 0
    print("Positive")
```

Correct:

```python
if number > 0:
    print("Positive")
```

### 12.2 Indentation Errors

Python uses indentation to define code blocks.

Incorrect indentation can cause an error or change the program's structure.

### 12.3 Incorrect Assignment

Assignment uses:

```python
number = 10
```

Comparison uses:

```python
number == 10
```

These operators have different purposes.

### 12.4 Incorrect Data Types

Some operations require compatible data types.

For example:

```python
number = "10"
```

The value is a string, not an integer.

Convert it when necessary:

```python
number = int("10")
```

### 12.5 Division by Zero

Incorrect:

```python
result = 10 / 0
```

Correct applications validate the denominator before performing division.

### 12.6 Incorrect Condition Order

When using multiple conditions, the order may affect the selected branch.

Always understand which conditions can become true first.

### 12.7 Incorrect Variable Names

Use meaningful names to make the purpose of each variable clear.

### 12.8 Missing Input Validation

Check whether user input satisfies the expected requirements before processing it.

### 12.9 Unnecessary Repeated Code

Functions can reduce repeated logic.

### 12.10 Incorrect Loop Boundaries

When working with ranges, remember that Python's `range()` excludes the ending value.

---

## 13. Best Practices

Follow these practices throughout Programming Fundamentals.

1. Understand the problem before coding.
2. Identify input and output.
3. Plan the solution first.
4. Write clear algorithms.
5. Use meaningful variable names.
6. Follow Python syntax correctly.
7. Maintain proper indentation.
8. Understand data types.
9. Choose suitable operators.
10. Use parentheses to clarify expressions.
11. Select the correct conditional structure.
12. Validate user input.
13. Avoid unnecessary repeated logic.
14. Create reusable functions.
15. Keep programs readable.
16. Use comments when they improve clarity.
17. Handle invalid inputs.
18. Use appropriate data structures.
19. Understand the reason behind each statement.
20. Review program output carefully.

---

## 14. Real-World Applications

Programming Fundamentals concepts are used throughout software development.

| Concept | Example Application |
|---|---|
| Programming Introduction | Understanding software execution |
| Algorithms | Search and sorting solutions |
| Flowcharts | Process design |
| Pseudocode | Planning software logic |
| Variables | Storing application data |
| Data Types | Representing different values |
| Arithmetic Operators | Calculations |
| Comparison Operators | Checking conditions |
| Logical Operators | Combining decisions |
| Conditional Statements | Access control and validation |
| Match Case | Command and menu processing |

These concepts appear in:

- Web applications.
- Banking systems.
- Management software.
- Student portals.
- E-commerce applications.
- Data processing.
- Automation.
- Artificial intelligence.
- Machine learning.
- Backend development.
- Mobile applications.

---

## 15. DSA Foundation

Programming Fundamentals prepares you for later Data Structures and Algorithms topics.

Before learning advanced algorithms, understand:

### 15.1 Problem Understanding

Read a problem and identify what it requires.

### 15.2 Input and Output

Understand what data enters the program and what result should be produced.

### 15.3 Logical Thinking

Develop a sequence of steps to solve the problem.

### 15.4 Variables

Store the information required by an algorithm.

### 15.5 Operators

Perform mathematical and logical operations.

### 15.6 Conditional Decisions

Select different execution paths.

### 15.7 Algorithm Analysis

Begin understanding how algorithms use time and memory.

### Important DSA Connections

| Programming Fundamental | Future DSA Connection |
|---|---|
| Variables | Data representation |
| Data Types | Data structures |
| Operators | Mathematical algorithms |
| Conditions | Algorithm decisions |
| Flowcharts | Algorithm visualization |
| Pseudocode | Algorithm design |
| Lists | Arrays and sequences |
| Functions | Problem decomposition |
| Comparisons | Searching and sorting |
| Counters | Counting algorithms |

---

## 16. Complexity Analysis Introduction

Algorithm complexity describes the resources required by an algorithm.

The two basic areas are time complexity and space complexity.

### Time Complexity

Time complexity measures how the amount of work grows as the input size increases.

Common complexity classes:

| Complexity | Name |
|---|---|
| O(1) | Constant |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(2ⁿ) | Exponential |

### Space Complexity

Space complexity describes the additional memory needed by an algorithm.

Example:

```python
number = 10
result = number * 2

print(result)
```

This example uses a fixed number of variables.

Its additional space is constant:

\[
O(1)
\]

### List Processing Example

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

The number of loop iterations depends on the list size.

For `n` elements, the traversal takes:

\[
O(n)
\]

These concepts will become more important when studying DSA.

---

## 17. Recommended Learning Workflow

Follow a consistent process for every folder.

### Step 1 – Open the Folder

Start with the README file inside the relevant folder.

### Step 2 – Read the Introduction

Understand the topic and its objectives.

### Step 3 – Understand the Theory

Learn the key concepts.

### Step 4 – Study Syntax

Understand the Python structure.

### Step 5 – Study Examples

Read the examples and understand how they work.

### Step 6 – Understand the Code

Read the Python program carefully.

### Step 7 – Execute the Program

Run the Python file using the terminal.

### Step 8 – Attempt Practice Problems

Try solving the provided problems independently.

### Step 9 – Review Mistakes

Understand common errors.

### Step 10 – Review the Learning Checklist

Confirm that you understand the topic before moving forward.

### Recommended Order

Complete the folders in this sequence:

```text
01-Introduction
       |
       v
02-Flowcharts-Algorithms
       |
       v
03-Pseudocode-Problem-Solving
       |
       v
04-Variables-Data-Types
       |
       v
05-Operators-Expressions
       |
       v
06-Conditional-Statements
```

---

## 18. Repository Naming Convention

This repository uses numbered folder names.

The numbering keeps the learning material in a consistent sequence.

### Folder Naming

```text
01-Introduction
02-Flowcharts-Algorithms
03-Pseudocode-Problem-Solving
04-Variables-Data-Types
05-Operators-Expressions
06-Conditional-Statements
```

### Documentation Naming

Each major folder has its own:

```text
README.md
```

The root README explains the complete Programming Fundamentals section.

Each child README explains its individual topic or chapter.

### Python File Naming

Python files use descriptive names and numbering where applicable.

For example:

```text
01_if.py
01_if_else.py
01_if_elif_else.py
01_nested_if.py
01_ternary_operator.py
01_match_case.py
```

For practice problems, the file name identifies the problem.

---

## 19. Complete Documentation Map

The following table shows where the individual documentation files belong.

| Location | Documentation |
|---|---|
| `Programming-Fundamentals/README.md` | Main Programming Fundamentals overview |
| `01-Introduction/README.md` | Introduction documentation |
| `02-Flowcharts-Algorithms/README.md` | Flowchart and algorithm documentation |
| `03-Pseudocode-Problem-Solving/README.md` | Pseudocode and problem-solving documentation |
| `04-Variables-Data-Types/README.md` | Variables and data types documentation |
| `05-Operators-Expressions/README.md` | Operators and expressions documentation |
| `06-Conditional-Statements/README.md` | Conditional statements chapter documentation |
| `06-Conditional-Statements/01-If-Statement/README.md` | If statement |
| `06-Conditional-Statements/02-If-Else/README.md` | If-Else |
| `06-Conditional-Statements/03-If-Elif-Else/README.md` | If-Elif-Else |
| `06-Conditional-Statements/04-Nested-If/README.md` | Nested If |
| `06-Conditional-Statements/05-Conditional-Expressions/README.md` | Conditional Expressions |
| `06-Conditional-Statements/06-Practice-Problems/README.md` | Practice Problems Overview |
| `06-Conditional-Statements/07-Match-Case/README.md` | Match Case |

---

## 20. GitHub Repository

**Repository Name:** DSA-Python

**GitHub Repository:**

https://github.com/as-amaan-109/DSA-Python

**Main Path:**

```text
PYTHON/Programming-Fundamentals/
```

This folder contains the foundational Python learning material.

The individual folders organize the topics in a sequential format.

### Working With Git

After modifying the README or adding Python programs, review the changes.

```powershell
git status
```

Stage the required files:

```powershell
git add "PYTHON/Programming-Fundamentals"
```

Review staged changes:

```powershell
git status
```

Create a commit:

```powershell
git commit -m "Add programming fundamentals documentation"
```

Push the changes:

```powershell
git push origin main
```

---

# FINAL SUMMARY

The `Programming-Fundamentals` folder is the foundation of the Python learning journey in this repository.

It contains six major learning areas:

1. Introduction.
2. Flowcharts and Algorithms.
3. Pseudocode and Problem Solving.
4. Variables and Data Types.
5. Operators and Expressions.
6. Conditional Statements.

Each area contributes to building programming knowledge and logical thinking.

### After Completing This Section

You should be able to:

- Understand the basic concepts of programming.
- Write and execute Python programs.
- Understand program structure.
- Create algorithms.
- Draw flowcharts.
- Write pseudocode.
- Analyze simple problems.
- Work with variables.
- Understand Python data types.
- Perform arithmetic operations.
- Evaluate expressions.
- Use comparison operators.
- Use logical operators.
- Make decisions through conditions.
- Write practical Python programs.
- Use basic functions and data structures.
- Understand introductory time and space complexity.

### Final Advice

Do not rush through Programming Fundamentals.

These concepts form the foundation of everything that comes next in Python and DSA.

Focus on understanding the purpose of every concept, writing your own code, and applying the logic to practical problems.

Complete the folders in their given order and use each topic's individual README for deeper explanations.

**Build your fundamentals first. Strong fundamentals make advanced programming easier to understand.**

