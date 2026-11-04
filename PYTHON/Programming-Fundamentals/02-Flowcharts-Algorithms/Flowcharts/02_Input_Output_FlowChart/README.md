# Input/Output Flowcharts — Python

Welcome to **Input/Output Flowcharts**, part of Week 1: Programming Fundamentals in the DSA-Python repository.

This topic focuses on reading input, processing values, and displaying results. You will learn how to represent these operations in flowcharts and convert them into Python programs.

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is Input and Output?](#what-is-input-and-output)
4. [Input/Output Flowchart Symbols](#inputoutput-flowchart-symbols)
5. [The IPO Model](#the-ipo-model)
6. [Designing an Input/Output Flowchart](#designing-an-inputoutput-flowchart)
7. [Worked Example: Sum of Two Numbers](#worked-example-sum-of-two-numbers)
8. [Worked Example: Rectangle Area](#worked-example-rectangle-area)
9. [Worked Example: Simple Interest](#worked-example-simple-interest)
10. [Input Types and Validation](#input-types-and-validation)
11. [Dry Run and Testing](#dry-run-and-testing)
12. [Time and Space Complexity](#time-and-space-complexity)
13. [Folder Structure](#folder-structure)
14. [How to Run the Program](#how-to-run-the-program)
15. [Practice Questions](#practice-questions)
16. [Common Mistakes](#common-mistakes)
17. [Interview Questions](#interview-questions)
18. [Learning Checklist](#learning-checklist)

---

## About This Topic

Input and output are essential parts of most programs.

**Input** is the data supplied to a program. It can come from the keyboard, a file, a device, or another program.

**Processing** means performing calculations or operations on the input.

**Output** is the result produced by the program, such as a displayed message or calculated value.

For beginner flowcharts, input and output are commonly represented using a **parallelogram**.

Example:

```text
       ( START )
           |
           v
      / Input A /
           |
           v
      / Input B /
           |
           v
      [ SUM = A + B ]
           |
           v
      / Display SUM /
           |
           v
        ( END )
```

This flowchart accepts two inputs, calculates their sum, and displays the result.

## Learning Objectives

After completing this topic, you should be able to:

- Explain input, processing, and output.
- Identify the input/output symbol in a flowchart.
- Design a flowchart for simple calculations.
- Distinguish integer, decimal, and text input.
- Convert an input/output flowchart into Python code.
- Use formulas for sums, averages, percentages, and conversions.
- Validate input where necessary.
- Prevent simple errors such as division by zero.
- Perform a dry run with sample values.
- Test a program using normal and boundary inputs.

---

## What Is Input and Output?

### 1. Input

Input provides the values required to solve a problem.

Examples:

- Enter a student's name.
- Enter two numbers.
- Enter the dimensions of a rectangle.
- Enter marks for five subjects.
- Enter distance and time.

In pseudocode, input may be represented as:

```text
INPUT name
INPUT A
INPUT B
```

In Python:

```python
name = input("Enter your name: ")
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
```

### 2. Processing

Processing performs an operation on the supplied values.

Examples:

```text
SUM = A + B
AREA = LENGTH * WIDTH
AVERAGE = TOTAL / COUNT
```

Python equivalent:

```python
total = a + b
```

### 3. Output

Output communicates the result to the user.

Pseudocode:

```text
OUTPUT SUM
```

Python:

```python
print("Sum:", total)
```

---

## Input/Output Flowchart Symbols

| Symbol | Shape | Purpose | Example |
|---|---|---|---|
| Terminal | Oval or rounded terminal | Start or finish the flow | Start, End |
| Input/Output | Parallelogram | Read or display information | Input A, Display SUM |
| Process | Rectangle | Perform calculations or assignments | `SUM = A + B` |
| Flow line | Arrow | Connect steps in order | Shows direction |

### Example of a complete flow

```text
        ( START )
            |
            v
       / Input A /
            |
            v
       / Input B /
            |
            v
       [ SUM = A + B ]
            |
            v
       / Output SUM /
            |
            v
         ( END )
```

The input/output symbols collect and display the values. The rectangle performs the calculation.

---

## The IPO Model

IPO stands for **Input, Process, Output**. It is a simple method for planning a solution before drawing its flowchart or writing the code.

### Example: Calculate an average

**Problem:** Read three numbers and calculate their average.

| Stage | Description |
|---|---|
| Input | Three numbers: A, B, C |
| Process | `AVERAGE = (A + B + C) / 3` |
| Output | Display the average |

### Why use the IPO model?

The IPO model helps identify missing requirements before programming. It also makes it easier to create the required flowchart symbols in the correct order.

Before coding, write down the required inputs, operations, and expected output.

---

## Designing an Input/Output Flowchart

Follow these steps when designing a diagram.

### Step 1: Understand the problem

Determine what result is required.

### Step 2: List the inputs

Identify every value that must be supplied.

### Step 3: Define the processing

Choose the required formula or operation.

### Step 4: Decide the output

Specify what should be displayed.

### Step 5: Arrange the symbols

Begin with Start, place inputs before the calculation, place the output after processing, and finish with End.

### Step 6: Connect the steps

Use arrows to indicate the order of execution.

### Step 7: Dry-run the diagram

Use sample data and verify every calculation manually.

### Step 8: Implement in Python

Convert each input symbol into an appropriate input statement, each process into code, and each output symbol into a display statement.

---

## Worked Example: Sum of Two Numbers

**Problem:** Read two integers and display their sum.

### Algorithm

1. Start.
2. Read integer A.
3. Read integer B.
4. Calculate `SUM = A + B`.
5. Display SUM.
6. End.

### Pseudocode

```text
START
INPUT A
INPUT B
SUM = A + B
OUTPUT SUM
END
```

### Flowchart

```text
        ( START )
            |
            v
       / Input A /
            |
            v
       / Input B /
            |
            v
       [ SUM = A + B ]
            |
            v
       / Output SUM /
            |
            v
         ( END )
```

### Python implementation

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

total = a + b

print("Sum:", total)
```

### Dry run

Suppose A is `12` and B is `8`.

| Step | Operation | Result |
|---|---|---:|
| 1 | Read A | 12 |
| 2 | Read B | 8 |
| 3 | Calculate A + B | 20 |
| 4 | Display SUM | 20 |

Expected result:

```text
Enter first integer: 12
Enter second integer: 8
Sum: 20
```

### Complexity

For fixed-size integer values, the calculation uses a constant number of basic operations.

- Time complexity: `O(1)`.
- Auxiliary space: `O(1)`.

---

## Worked Example: Rectangle Area

**Problem:** Read the length and width of a rectangle and calculate its area.

### Formula

`Area = Length × Width`

### Flowchart

```text
        ( START )
            |
            v
      / Input Length /
            |
            v
       / Input Width /
            |
            v
 [ AREA = LENGTH * WIDTH ]
            |
            v
      / Display AREA /
            |
            v
         ( END )
```

### Python implementation

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Dimensions cannot be negative.")
else:
    area = length * width
    print("Area:", area)
```

### Sample calculation

If length is `5` and width is `3`:

`Area = 5 × 3 = 15`

Expected area: `15` square units.

The diagram represents the expected logical flow. When input validation is added, the flowchart should also include a decision symbol for checking whether the dimensions are valid.

---

## Worked Example: Simple Interest

**Problem:** Read principal, annual interest rate, and time in years; calculate simple interest.

### Formula

`Simple Interest = (Principal × Rate × Time) / 100`

`Total Amount = Principal + Simple Interest`

### IPO table

| Stage | Values or action |
|---|---|
| Input | Principal, annual rate, time in years |
| Process | Calculate interest and total amount |
| Output | Display interest and total amount |

### Python implementation

```python
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time in years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Values cannot be negative.")
else:
    interest = principal * rate * time / 100
    amount = principal + interest

    print("Simple interest:", round(interest, 2))
    print("Total amount:", round(amount, 2))
```

### Dry run

Assume:

- Principal = 1,000
- Annual rate = 5%
- Time = 2 years

Calculation:

`Interest = (1000 × 5 × 2) / 100 = 100`

`Total Amount = 1000 + 100 = 1100`

The output is simple interest of `100` and a total amount of `1100`.

---

## Input Types and Validation

Python's `input()` function returns text. Convert it to the required type before performing arithmetic.

| Required data | Python approach |
|---|---|
| Text | `input()` |
| Integer | `int(input(...))` |
| Decimal number | `float(input(...))` |

### Reading text

```python
name = input("Enter your name: ").strip()
print("Name:", name)
```

`.strip()` removes whitespace at the beginning and end of the input.

### Reading an integer

```python
age = int(input("Enter age: "))
print("Age:", age)
```

This code expects valid integer input. In a robust interactive program, catch `ValueError` if the user enters something other than a whole number.

### Reading a decimal

```python
price = float(input("Enter price: "))
print("Price:", price)
```

### Why validation matters

A program may receive values outside the expected range or a value that makes an operation invalid.

For example:

```python
divisor = float(input("Enter divisor: "))

if divisor == 0:
    print("Division by zero is not allowed.")
else:
    print("Result:", 10 / divisor)
```

For integer input, `int()` conversion rejects decimal strings such as `"3.5"`. Choose an input type based on the problem requirements.

---

## Dry Run and Testing

A dry run means manually following the algorithm using known sample inputs before relying on the program.

For input/output flowcharts, check that:

1. Each required input is collected.
2. The calculation uses the correct values.
3. The output is displayed after processing.
4. Division by zero is handled when division is used.
5. Inputs with restricted ranges are validated.
6. Boundary cases produce sensible results.

### Example test cases for addition

| Input A | Input B | Expected sum |
|---:|---:|---:|
| 2 | 3 | 5 |
| 0 | 8 | 8 |
| -4 | 6 | 2 |
| -3 | -7 | -10 |
| 100 | 200 | 300 |

Testing negative numbers and zero helps verify that the solution is not working only for positive inputs.

---

## Time and Space Complexity

For introductory input/output programs, complexity is often constant because the program reads a fixed number of values and performs a fixed number of operations.

| Operation | Typical complexity |
|---|---|
| Read a fixed number of values | `O(1)` for a fixed-size model |
| Add two numbers | `O(1)` for fixed-size numeric values |
| Calculate a rectangle's area | `O(1)` for fixed-size numeric values |
| Calculate a five-subject total | `O(1)` because the number of subjects is fixed |
| Read and process N values | `O(N)` time, usually `O(1)` auxiliary space if only a running total is stored |

For programs that read an input list whose size grows, the complexity depends on the number of items and how they are stored and processed.

---

## Folder Structure

```text
02_Input_Output_FlowChart/
│
├── README.md
└── 02_input_output_flowchart.py
```

The Python file contains the examples and practice programs. This README explains the concepts, formulas, flowchart patterns, and testing approach.

---

## How to Run the Program

Open PowerShell at the root of your `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\02_Input_Output_FlowChart\02_input_output_flowchart.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Choose the desired option, enter the requested values, and observe the result.

If Python is not recognized, verify your Python installation. On Windows, the `py` command may also work instead of `python`.

---

## Practice Questions

The Python file contains 12 examples, 12 solved questions, and 5 unsolved questions.

### 12 Examples

1. Read and display a name.
2. Add two numbers.
3. Perform arithmetic operations.
4. Calculate rectangle area.
5. Calculate simple interest.
6. Convert Celsius to Fahrenheit.
7. Calculate the average of three values.
8. Calculate quotient and remainder.
9. Calculate a bill with tax.
10. Calculate percentage for five subjects.
11. Convert seconds to hours, minutes, and seconds.
12. Calculate average speed.

### 12 Solved Questions

1. Calculate the area and circumference of a circle.
2. Swap two numbers.
3. Convert minutes into hours and remaining minutes.
4. Calculate gross salary using percentage-based allowances.
5. Calculate discounted price.
6. Calculate percentage and an example grade.
7. Convert kilometres to miles.
8. Find the average of N numbers.
9. Perform safe integer division.
10. Calculate an educational example electricity bill with slab rates.
11. Calculate a right triangle's hypotenuse.
12. Convert seconds into days, hours, minutes, and seconds.

The electricity rates used by that example are illustrative practice values, not official rates.

### 5 Unsolved Questions

1. Create a flowchart to calculate a multi-item bill with a user-entered tax rate.
2. Read a student's name and marks, then display a formatted result summary.
3. Convert a given number of days into weeks and remaining days.
4. Calculate a final price after applying a discount and then a separate tax.
5. Read N numbers and display their minimum, maximum, and average.

For each unsolved question:

1. Identify the inputs and outputs.
2. Write the IPO table.
3. Write the algorithm.
4. Draw the flowchart.
5. Perform a dry run.
6. Implement the solution in Python.
7. Test normal and boundary cases.

---

## Common Mistakes

- Forgetting to convert `input()` text before performing arithmetic.
- Using the wrong formula.
- Displaying the result before calculating it.
- Ignoring invalid or out-of-range inputs.
- Dividing by zero.
- Confusing integer division (`//`) with regular division (`/`).
- Forgetting units when interpreting calculated values.
- Using a flowchart that does not match the implemented logic.
- Testing only one sample input.
- Storing unnecessary intermediate values.

---

## Interview Questions

**1. What is input in programming?**

Input is the data supplied to a program for processing.

**2. What is output?**

Output is the information or result produced by a program.

**3. Which flowchart symbol represents input and output?**

A parallelogram is commonly used for input/output operations.

**4. What does IPO stand for?**

IPO stands for Input, Process, Output.

**5. Why is the IPO model useful?**

It helps identify required inputs, the operations to perform, and the output expected from a solution.

**6. What does Python's `input()` function return?**

It returns text, represented by a string.

**7. How do you convert input text into an integer?**

Use `int(input(...))` when the user is expected to enter a valid integer.

**8. What is the difference between `/` and `//` in Python?**

`/` performs true division. `//` performs floor division.

**9. Why should division by zero be checked?**

A zero divisor makes division invalid and raises an error for ordinary numeric division in Python.

**10. What is a dry run?**

A dry run manually traces an algorithm with sample input values to verify its logic.

**11. Why are test cases important?**

They help identify incorrect calculations, missing conditions, and unexpected behaviour.

**12. How are an algorithm, flowchart, and Python program related?**

An algorithm describes the logical steps, a flowchart represents them visually, and a Python program implements them in code.

---

## Learning Checklist

- [ ] I understand the difference between input, processing, and output.
- [ ] I can identify the input/output flowchart symbol.
- [ ] I can use the IPO model.
- [ ] I can draw an input/output flowchart.
- [ ] I can convert a flowchart into Python.
- [ ] I can use integer, decimal, and text input.
- [ ] I understand why input validation matters.
- [ ] I have run all examples.
- [ ] I have studied the solved questions.
- [ ] I have attempted the five unsolved questions.
- [ ] I have tested my solutions with multiple inputs.

---

## Next Topic

After completing Input/Output Flowcharts, move to **Decision Flowcharts** to learn how to represent conditions, branching paths, and multiple outcomes.
