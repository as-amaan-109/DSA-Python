# Algorithm Steps

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Algorithm Steps  
> **Level:** Beginner  
> **Goal:** Learn how to develop, arrange, trace, and implement algorithm steps.

---

## Table of Contents

1. Introduction
2. What Are Algorithm Steps?
3. Why Are Ordered Steps Important?
4. Basic Structure of an Algorithm
5. How to Write an Algorithm Step by Step
6. Input, Process, and Output
7. Example: Display a Message
8. Example: Add Two Numbers
9. Example: Area of a Rectangle
10. Example: Average of Three Numbers
11. Example: Celsius to Fahrenheit
12. What Is a Dry Run?
13. Dry Run with a Table
14. What Is Pseudocode?
15. Characteristics of Good Algorithm Steps
16. Algorithm Steps vs Python Code
17. Common Beginner Mistakes
18. Important Terminology
19. Interview Questions
20. Practice Questions
21. Learning Checklist
22. What's Next?

---

## 1. Introduction

An algorithm is a sequence of instructions used to solve a problem.

However, simply knowing what an algorithm is does not mean we can write a good one. We also need to know how to arrange its steps, identify the necessary inputs, perform the correct operations, and produce the expected output.

For example, to add two numbers, we must first obtain both numbers, then calculate their sum, and finally display the result.

The order of these actions matters.

In this topic, we will learn how to write algorithms using clear, numbered steps and how to translate those steps into Python programs.

---

## 2. What Are Algorithm Steps?

Algorithm steps are the individual instructions that make up an algorithm.

Each step describes an action required to solve the problem.

Consider the problem of calculating the sum of two numbers.

### Algorithm

1. Start.
2. Read the first number.
3. Read the second number.
4. Add the two numbers.
5. Display the sum.
6. Stop.

Every step has a specific purpose.

The input steps obtain the numbers, the processing step calculates the sum, and the output step displays the result.

### Important Point

An algorithm should describe **what needs to be done and in what order**.

It does not have to use the exact syntax of a programming language.

---

## 3. Why Are Ordered Steps Important?

Algorithm steps must be organized in a logical sequence.

Consider the addition problem.

### Correct order

1. Read the first number.
2. Read the second number.
3. Calculate their sum.
4. Display the result.

### Incorrect order

1. Calculate the sum before obtaining the numbers.
2. Read the first number.
3. Read the second number.
4. Display the result.

The second sequence is incomplete as written because it attempts to calculate the result before obtaining the required inputs.

### Benefits of Ordered Steps

- They make the solution easier to understand.
- They help identify missing instructions.
- They simplify the conversion of an algorithm into code.
- They make logical mistakes easier to find.
- They make testing and debugging easier.

---

## 4. Basic Structure of an Algorithm

A simple algorithm commonly includes a beginning, a sequence of instructions, and an ending.

```text
START

Step 1: Obtain the required input.
Step 2: Process the input.
Step 3: Display the result.

STOP
```

The number and type of steps depend on the problem.

### Common Components

| Component | Purpose |
|---|---|
| Start | Indicates the beginning |
| Input | Obtains required values |
| Processing | Performs calculations or other operations |
| Output | Produces or displays the result |
| Stop | Indicates the end |

Not every algorithm needs an external input. For example, a program that displays a fixed message can work without asking the user for anything.

---

## 5. How to Write an Algorithm Step by Step

Follow this process when solving a programming problem.

### Step 1: Understand the Problem

Read the problem carefully and identify what needs to be solved.

Example:

Find the sum of two numbers.

### Step 2: Identify the Input

Determine which values are needed.

For the addition problem:

- First number
- Second number

### Step 3: Identify the Output

Decide what the algorithm should produce.

For addition:

- The sum of the two numbers

### Step 4: Choose the Processing Logic

Determine what operation is required.

For addition:

```text
SUM = A + B
```

### Step 5: Arrange the Steps

Write every instruction in a logical order.

### Step 6: Test with Sample Values

Try values such as:

```text
A = 10
B = 20
```

The expected sum is `30`.

### Step 7: Implement the Algorithm

Translate the steps into Python or another programming language.

### Summary

```text
Understand the Problem
          |
          v
Identify Input and Output
          |
          v
Choose the Processing Logic
          |
          v
Write Ordered Steps
          |
          v
Test with Sample Values
          |
          v
Implement in Python
```

---

## 6. Input, Process, and Output

A common way to understand basic algorithms is to divide the solution into three stages.

### 6.1 Input

Input is the information required by the algorithm.

Example:

```text
A = 10
B = 20
```

### 6.2 Process

Processing means performing the required calculation or operation.

```text
SUM = A + B
SUM = 10 + 20
SUM = 30
```

### 6.3 Output

Output is the result produced by the algorithm.

```text
Sum = 30
```

### Complete Example

```text
INPUT
  A = 10
  B = 20
      |
      v
PROCESS
  SUM = A + B
      |
      v
OUTPUT
  SUM = 30
```

This structure is especially useful when beginning a new programming problem.

---

## 7. Example: Display a Message

### Problem

Display the message `Welcome to Python`.

### Algorithm

1. Start.
2. Display `Welcome to Python`.
3. Stop.

### Python Implementation

```python
print("Welcome to Python")
```

### Output

```text
Welcome to Python
```

### Explanation

This algorithm does not require any input or calculation. It simply displays a fixed message.

It demonstrates that an algorithm can be short and does not always require every component of the input-process-output pattern.

---

## 8. Example: Add Two Numbers

### Problem

Read two numbers, calculate their sum, and display the result.

### Algorithm

1. Start.
2. Read the first number A.
3. Read the second number B.
4. Calculate `SUM = A + B`.
5. Display SUM.
6. Stop.

### Sample Input

```text
A = 10
B = 20
```

### Calculation

```text
SUM = 10 + 20
SUM = 30
```

### Expected Output

```text
Sum = 30
```

### Python Implementation

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Sample Run

```text
Enter the first number: 10
Enter the second number: 20
Sum: 30
```

### Explanation

- `input()` obtains a value from the user.
- `int()` converts the entered text into an integer.
- `a + b` performs the addition.
- `print()` displays the result.

The Python code implements the same logic described by the algorithm.

---

## 9. Example: Area of a Rectangle

### Problem

Calculate the area of a rectangle using its length and breadth.

### Formula

```text
Area = Length × Breadth
```

### Algorithm

1. Start.
2. Read the length.
3. Read the breadth.
4. Calculate `AREA = LENGTH × BREADTH`.
5. Display AREA.
6. Stop.

### Sample Values

```text
Length = 5
Breadth = 3
```

### Calculation

```text
AREA = 5 × 3
AREA = 15
```

### Expected Output

```text
Area = 15
```

### Python Implementation

```python
length = 5
breadth = 3

area = length * breadth

print("Area:", area)
```

Output:

```text
Area: 15
```

### Explanation

The algorithm first obtains the dimensions, multiplies them, and displays the calculated area.

The formula is applied to the sample values to verify the result.

---

## 10. Example: Average of Three Numbers

### Problem

Calculate the average of three numbers.

### Formula

```text
Average = (A + B + C) / 3
```

### Algorithm

1. Start.
2. Read numbers A, B, and C.
3. Calculate `TOTAL = A + B + C`.
4. Calculate `AVERAGE = TOTAL / 3`.
5. Display AVERAGE.
6. Stop.

### Sample Values

```text
A = 10
B = 20
C = 30
```

### Dry Calculation

```text
TOTAL = 10 + 20 + 30
TOTAL = 60

AVERAGE = 60 / 3
AVERAGE = 20
```

### Python Implementation

```python
a = 10
b = 20
c = 30

total = a + b + c
average = total / 3

print("Total:", total)
print("Average:", average)
```

Output:

```text
Total: 60
Average: 20.0
```

Python's `/` operator returns a floating-point result for this division.

---

## 11. Example: Celsius to Fahrenheit

### Problem

Convert a temperature from Celsius into Fahrenheit.

### Formula

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

### Algorithm

1. Start.
2. Read the temperature in Celsius.
3. Calculate `FAHRENHEIT = (CELSIUS × 9 / 5) + 32`.
4. Display the Fahrenheit temperature.
5. Stop.

### Sample Input

```text
Celsius = 25
```

### Calculation

```text
Fahrenheit = (25 × 9 / 5) + 32
Fahrenheit = 45 + 32
Fahrenheit = 77
```

### Python Implementation

```python
celsius = 25

fahrenheit = (celsius * 9 / 5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
```

Output:

```text
Celsius: 25
Fahrenheit: 77.0
```

This example shows how a mathematical formula can be converted into clearly ordered instructions.

---

## 12. What Is a Dry Run?

A **dry run** is the process of tracing an algorithm manually using selected sample values.

It helps us understand how values change during execution and whether the algorithm produces the expected result.

### Example

Algorithm:

1. Set A = 5.
2. Set B = 3.
3. Calculate `SUM = A + B`.
4. Display SUM.

### Dry Run

Initially:

```text
A = 5
B = 3
```

Calculation:

```text
SUM = 5 + 3
SUM = 8
```

Expected output:

```text
8
```

### Why Perform a Dry Run?

- To verify the logic manually.
- To detect missing or incorrectly ordered steps.
- To understand how a program processes values.
- To check the expected output before running code.

---

## 13. Dry Run with a Table

A dry-run table records the values of important variables after each step.

Consider:

```python
a = 5
b = 3
total = a + b

print(total)
```

### Dry-Run Table

| Step | Operation | A | B | Total |
|---|---|---:|---:|---:|
| 1 | Assign 5 to A | 5 | — | — |
| 2 | Assign 3 to B | 5 | 3 | — |
| 3 | Calculate A + B | 5 | 3 | 8 |
| 4 | Display Total | 5 | 3 | 8 |

Output:

```text
8
```

The table makes the order of execution and variable values easier to follow.

---

## 14. What Is Pseudocode?

Pseudocode is a structured way to describe an algorithm using human-readable instructions.

It does not need to follow the exact syntax of Python or any other programming language.

### Example: Addition

```text
BEGIN

    INPUT A
    INPUT B

    SUM = A + B

    OUTPUT SUM

END
```

### Corresponding Python Code

```python
a = int(input("Enter A: "))
b = int(input("Enter B: "))

total = a + b

print(total)
```

### Why Use Pseudocode?

- It helps organize problem-solving logic.
- It is easier to modify than a complete program.
- It does not require knowledge of a specific programming language.
- It helps convert an algorithm into executable code.

Pseudocode conventions can vary. The main requirement is that the instructions are clear and logically ordered.

---

## 15. Characteristics of Good Algorithm Steps

Good algorithm steps should be written carefully.

### 15.1 Clear

Each instruction should be easy to understand.

Avoid vague steps such as `Do the calculation`.

Prefer a specific instruction such as `SUM = A + B`.

### 15.2 Ordered

Instructions should appear in the correct sequence.

Required inputs should be obtained before they are used.

### 15.3 Precise

Each step should describe a recognizable action.

### 15.4 Finite

The algorithm should finish after a finite number of steps for the intended problem.

### 15.5 Correct

The instructions should produce the expected result for valid inputs within the problem's stated requirements.

### 15.6 Testable

It should be possible to check the result using sample inputs and expected outputs.

---

## 16. Algorithm Steps vs Python Code

| Algorithm Steps | Python Code |
|---|---|
| Describe the solution in ordered instructions | Implement the instructions using Python syntax |
| Can use plain English or pseudocode | Must follow Python syntax rules |
| Focus on the solution logic | Executes the chosen implementation |
| Can be understood without running a program | Can be run by a Python interpreter |

### Example

Algorithm:

```text
1. Start.
2. Set A = 5.
3. Set B = 3.
4. Calculate SUM = A + B.
5. Display SUM.
6. Stop.
```

Python implementation:

```python
a = 5
b = 3

total = a + b

print(total)
```

Output:

```text
8
```

The algorithm and program use different representations of the same solution.

---

## 17. Common Beginner Mistakes

### Mistake 1: Ignoring the Order of Operations

Trying to calculate a result before obtaining the required values makes the solution incomplete.

**Solution:** Write the input steps first.

### Mistake 2: Missing a Required Step

An algorithm may perform the correct calculation but fail to display the result.

**Solution:** Check whether every step required by the problem is included.

### Mistake 3: Writing Vague Instructions

A step like `Process the numbers` does not explain the required operation.

**Solution:** Specify the calculation or action.

### Mistake 4: Not Testing the Algorithm

An algorithm may appear correct but produce an unexpected result.

**Solution:** Perform a dry run with sample values.

### Mistake 5: Confusing Pseudocode with Python

Pseudocode may use instructions such as `INPUT` and `OUTPUT`; they are not automatically valid Python statements.

**Solution:** Translate each pseudocode instruction into the appropriate Python syntax.

### Mistake 6: Incorrect Formula

A wrong formula leads to incorrect results even if the steps are logically ordered.

**Solution:** Verify the formula independently before implementing it.

---

## 18. Important Terminology

| Term | Meaning |
|---|---|
| Algorithm | Ordered instructions for solving a problem |
| Algorithm step | One instruction within an algorithm |
| Input | Information required by the solution |
| Processing | Operations performed on the input |
| Output | Result produced by the solution |
| Pseudocode | Human-readable description of algorithm logic |
| Dry run | Manually tracing an algorithm using sample values |
| Variable | A name referring to a value |
| Formula | A mathematical relationship used for a calculation |
| Implementation | Converting the solution into executable code |
| Test case | Input and expected result used to test a solution |

---

## 19. Interview Questions

### Q1. What are algorithm steps?

They are the individual instructions that form an algorithm and describe how to solve a problem in a logical order.

### Q2. Why must algorithm steps be ordered?

Because some operations depend on earlier steps. The required input must usually be available before it can be processed.

### Q3. What is a dry run?

A dry run is a manual trace of an algorithm using sample values to understand the execution and verify the expected result.

### Q4. What is pseudocode?

Pseudocode describes algorithm logic using structured, human-readable instructions without requiring the exact syntax of a programming language.

### Q5. What are input, processing, and output?

- Input supplies the required information.
- Processing performs the necessary operation.
- Output presents the result.

### Q6. What makes algorithm steps good?

They should be clear, logically ordered, precise, finite for the intended task, correct, and testable.

### Q7. How do you convert algorithm steps into Python code?

Identify the input, translate each processing instruction into Python operations, display the expected output, and test the program with sample values.

### Q8. Why is a dry run useful before running a program?

It helps verify the logic manually and makes mistakes in the steps or calculations easier to detect.

---

## 20. Practice Questions

Write the algorithm first for each problem. Then try to implement it in Python.

### Beginner Level

**Question 1:** Write steps to display your name.

**Question 2:** Write an algorithm to subtract two numbers.

**Question 3:** Write an algorithm to multiply two numbers.

**Question 4:** Write an algorithm to calculate the square of a number.

**Question 5:** Write an algorithm to find the average of four numbers.

### Intermediate Level

**Question 6:** Write an algorithm to calculate the perimeter of a rectangle.

Formula:

```text
Perimeter = 2 × (Length + Breadth)
```

**Question 7:** Write an algorithm to convert kilometres into metres.

Formula:

```text
Metres = Kilometres × 1000
```

**Question 8:** Write an algorithm to calculate the total price of three items.

**Question 9:** Write an algorithm to calculate the area of a triangle.

Formula:

```text
Area = (Base × Height) / 2
```

**Question 10:** Write an algorithm to calculate the final bill after adding a fixed delivery charge.

State the inputs and formula you intend to use.

### Challenge

For any two questions above:

1. Write the algorithm in numbered steps.
2. Write pseudocode.
3. Perform a dry run with sample values.
4. Implement the solution in Python.
5. Compare the actual output with the expected output.

---

## 21. Learning Checklist

- [ ] Understand what algorithm steps are.
- [ ] Write instructions in a logical order.
- [ ] Identify input, processing, and output.
- [ ] Write numbered algorithm steps.
- [ ] Convert algorithm steps into Python code.
- [ ] Understand pseudocode.
- [ ] Perform a dry run.
- [ ] Prepare a dry-run table.
- [ ] Verify formulas and calculations.
- [ ] Solve the practice questions.

---

## 22. What's Next?

Continue with:

**03 - Algorithm Examples**

In the next topic, practise applying algorithms to different problems.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `02_algorithm_steps.py` | Python examples that demonstrate algorithm steps |
| `README.md` | Detailed notes, examples, dry runs, interview questions, and practice problems |

---

## Conclusion

Writing an algorithm involves more than listing instructions. The steps must be clear, precise, correctly ordered, and suitable for solving the given problem.

Use this process whenever you approach a new coding question:

**Understand → Identify Inputs and Outputs → Write Steps → Dry Run → Implement → Test**

Practising this approach will strengthen your problem-solving skills and prepare you for more advanced algorithms and DSA.