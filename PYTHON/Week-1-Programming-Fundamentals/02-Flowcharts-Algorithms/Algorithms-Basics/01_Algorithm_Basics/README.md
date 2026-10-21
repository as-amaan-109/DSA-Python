# Algorithm Basics

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Algorithm Basics  
> **Level:** Beginner  
> **Goal:** Understand algorithms and learn how to describe a solution step by step.

---

## Table of Contents

1. Introduction
2. What Is an Algorithm?
3. Why Do We Need Algorithms?
4. Real-Life Example of an Algorithm
5. Basic Structure of an Algorithm
6. Input, Process, and Output
7. Algorithm vs Program
8. Algorithm vs Flowchart
9. How to Write an Algorithm
10. Example: Add Two Numbers
11. Example: Calculate an Average
12. Example: Area of a Rectangle
13. What Is Pseudocode?
14. Algorithm and Python Implementation
15. Common Beginner Mistakes
16. Important Terminology
17. Interview Questions
18. Practice Questions
19. Learning Checklist
20. What's Next?

---

## 1. Introduction

Before writing code, we need to understand the problem and decide how to solve it.

In programming, this step-by-step problem-solving approach is represented using an **algorithm**.

An algorithm describes the instructions required to solve a problem in a logical order.

For example, if we want to add two numbers, we need to:

1. Get the first number.
2. Get the second number.
3. Add the numbers.
4. Display the result.

Once we understand these steps, we can convert the solution into Python code.

**Important concept:**

Understand the problem first, design the algorithm next, and then write the program.

---

## 2. What Is an Algorithm?

An **algorithm** is a finite sequence of clear and ordered steps used to solve a problem or complete a task.

Algorithms describe the logic of a solution without requiring a specific programming language.

For example, an algorithm for adding two numbers can be written in simple English, pseudocode, or implemented in Python.

### Example

Problem: Add two numbers.

Algorithm:

1. Start.
2. Read the first number.
3. Read the second number.
4. Calculate their sum.
5. Display the sum.
6. Stop.

The algorithm explains how to solve the problem without depending on Python syntax.

### In simple words

An algorithm is a step-by-step plan for solving a problem.

---

## 3. Why Do We Need Algorithms?

Algorithms help us organize our thinking before writing code.

### 3.1 Clear Problem-Solving Logic

Breaking a problem into smaller steps makes it easier to understand.

### 3.2 Easier Implementation

Once the steps are clear, converting them into a programming language becomes easier.

### 3.3 Easier Debugging

When a program produces an incorrect result, we can review the algorithm to find a logical mistake.

### 3.4 Language Independence

The same algorithm can often be implemented in different programming languages.

For example, the steps for adding two numbers remain the same whether the solution is implemented in Python, Java, C, or C++.

### 3.5 Preparation for DSA

Data Structures and Algorithms involve designing and analyzing solutions to computational problems.

Learning basic algorithms builds a foundation for:

- Arrays
- Searching
- Sorting
- Strings
- Recursion
- Linked lists
- Stacks and queues
- Trees and graphs
- Problem-solving and coding interviews

---

## 4. Real-Life Example of an Algorithm

We use step-by-step procedures in daily life without necessarily calling them algorithms.

### Example: Making a Cup of Tea

Algorithm:

1. Start.
2. Take a saucepan.
3. Add water.
4. Heat the water.
5. Add tea leaves and other desired ingredients.
6. Allow the tea to brew.
7. Strain the tea into a cup.
8. Serve the tea.
9. Stop.

Each step describes an action in a logical sequence.

### Programming Connection

A computer program also follows instructions to perform tasks.

The difference is that programming instructions must be expressed in a form the computer can execute.

---

## 5. Basic Structure of an Algorithm

A simple algorithm can be represented using the following structure:

```text
START

Step 1: Receive the required input.
Step 2: Process the input.
Step 3: Produce the result.

STOP
```

The exact steps depend on the problem being solved.

### Common elements

| Element | Meaning |
|---|---|
| Start | Marks the beginning of the procedure |
| Input | Information required to solve the problem |
| Processing | Operations performed on the input |
| Output | Result produced by the procedure |
| Stop | Marks the end of the procedure |

Not every algorithm requires external input. For example, an algorithm that displays a fixed message may not need any input.

---

## 6. Input, Process, and Output

Many beginner programming problems can be understood using three stages.

### 6.1 Input

Input is the information supplied to the algorithm.

Example:

```text
First number = 10
Second number = 20
```

### 6.2 Process

Processing means performing the operation required to solve the problem.

Example:

```text
10 + 20 = 30
```

### 6.3 Output

Output is the result produced by the algorithm.

Example:

```text
Sum = 30
```

### Complete representation

```text
Input
  |
  v
Process
  |
  v
Output
```

### Why is this important?

Understanding input, processing, and output helps us identify what a problem requires before writing code.

---

## 7. Algorithm vs Program

An algorithm and a program are related, but they are not the same thing.

| Algorithm | Program |
|---|---|
| Describes the steps to solve a problem | Implements instructions in a programming language |
| Focuses on solution logic | Focuses on executable code |
| Can be written in plain language or pseudocode | Must follow the syntax of its programming language |
| Does not require a specific programming language | Uses a particular programming language or execution environment |

### Example: Algorithm

Problem: Add two numbers.

```text
1. Start.
2. Read A and B.
3. Calculate SUM = A + B.
4. Display SUM.
5. Stop.
```

### Example: Python Program

```python
a = 10
b = 20

total = a + b

print("Sum:", total)
```

Output:

```text
Sum: 30
```

The algorithm describes the solution, while the Python program implements it.

---

## 8. Algorithm vs Flowchart

An algorithm and a flowchart can represent the logic of the same solution in different ways.

| Algorithm | Flowchart |
|---|---|
| Represents steps using written instructions | Represents steps using a visual diagram |
| Easy to write as a numbered list | Uses standardized shapes and arrows |
| Focuses on the ordered steps | Shows the flow between steps |
| Can be written without drawing | Requires a diagram to show the process visually |

### Example

Algorithm for adding two numbers:

1. Start.
2. Input A and B.
3. Calculate A + B.
4. Display the result.
5. Stop.

A flowchart would represent these stages using appropriate symbols and arrows.

**Note:** Flowcharts will be studied in a separate section of this repository.

---

## 9. How to Write an Algorithm

Follow these steps when designing an algorithm for a programming problem.

### Step 1: Understand the Problem

Identify exactly what needs to be calculated or achieved.

### Step 2: Identify the Input

Determine what values or information the solution needs.

### Step 3: Identify the Output

Determine what result should be produced.

### Step 4: Decide the Processing Logic

Choose the operations required to transform the input into the output.

### Step 5: Write the Steps in Order

Use numbered instructions and make sure the sequence is logical.

### Step 6: Test the Algorithm

Try sample inputs and manually verify the expected result.

### Step 7: Implement the Algorithm

Convert the steps into Python code or another programming language.

---

## 10. Example: Add Two Numbers

### Problem

Write an algorithm to add two numbers and display the result.

### Input

```text
A = 10
B = 20
```

### Algorithm

1. Start.
2. Read the first number A.
3. Read the second number B.
4. Calculate SUM = A + B.
5. Display SUM.
6. Stop.

### Processing

```text
SUM = A + B
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

- `input()` receives information from the user.
- `int()` converts the entered text into an integer.
- `a + b` calculates the sum.
- `print()` displays the result.

This example connects the written algorithm to an actual Python implementation.

---

## 11. Example: Calculate an Average

### Problem

Calculate the average of two numbers.

### Algorithm

1. Start.
2. Read the first number A.
3. Read the second number B.
4. Calculate SUM = A + B.
5. Calculate AVERAGE = SUM / 2.
6. Display AVERAGE.
7. Stop.

### Example Input

```text
A = 10
B = 20
```

### Calculation

```text
SUM = 10 + 20
SUM = 30

AVERAGE = 30 / 2
AVERAGE = 15
```

### Output

```text
Average = 15
```

### Python Implementation

```python
a = 10
b = 20

average = (a + b) / 2

print("Average:", average)
```

Output:

```text
Average: 15.0
```

Python's `/` operator produces a floating-point result for this division.

---

## 12. Example: Calculate the Area of a Rectangle

### Problem

Find the area of a rectangle using its length and breadth.

### Formula

```text
Area = Length × Breadth
```

### Algorithm

1. Start.
2. Read the length.
3. Read the breadth.
4. Calculate AREA = LENGTH × BREADTH.
5. Display AREA.
6. Stop.

### Example Input

```text
Length = 5
Breadth = 3
```

### Calculation

```text
AREA = 5 × 3
AREA = 15
```

### Output

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

This example demonstrates how a mathematical formula can be converted into an algorithm and then into code.

---

## 13. What Is Pseudocode?

Pseudocode is a way of describing the logic of an algorithm using simple, structured, language-independent instructions.

It resembles programming code but does not need to follow the exact syntax of a programming language.

### Example: Add Two Numbers

```text
BEGIN

    INPUT A
    INPUT B

    SUM = A + B

    OUTPUT SUM

END
```

The instructions describe the logic without using Python-specific syntax.

### Pseudocode vs Python

Pseudocode:

```text
INPUT A
INPUT B
SUM = A + B
OUTPUT SUM
```

Python:

```python
a = int(input("Enter A: "))
b = int(input("Enter B: "))

total = a + b

print(total)
```

### Why Use Pseudocode?

- It helps organize the solution logic.
- It is easier to revise than a full program.
- It can be understood without knowing a specific programming language.
- It helps prepare for implementation.

Pseudocode conventions vary. The important thing is that the steps remain clear and understandable.

---

## 14. Algorithm and Python Implementation

The same problem can be expressed in three stages.

### Stage 1: Problem

Find the sum of two numbers.

### Stage 2: Algorithm

```text
1. Start.
2. Read A and B.
3. Calculate SUM = A + B.
4. Display SUM.
5. Stop.
```

### Stage 3: Python Code

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

### Complete Learning Process

```text
Understand the Problem
         |
         v
Design the Algorithm
         |
         v
Write Pseudocode
         |
         v
Implement in Python
         |
         v
Test the Result
```

This process helps avoid writing code before understanding the solution.

---

## 15. Common Beginner Mistakes

### Mistake 1: Writing Steps in the Wrong Order

For example, trying to calculate a sum before obtaining the required numbers.

**Solution:** Identify the inputs before deciding how to process them.

### Mistake 2: Forgetting the Output

An algorithm may calculate the correct result but fail to state how that result will be presented.

**Solution:** Include an output step when the problem requires a displayed result.

### Mistake 3: Writing Unclear Steps

A step such as "do the calculation" does not specify what calculation is needed.

**Solution:** Write precise instructions, such as `SUM = A + B`.

### Mistake 4: Confusing an Algorithm with Code

Algorithms do not need to use Python syntax. A Python program is an implementation of the solution.

**Solution:** Write the logical steps first, then translate them into code.

### Mistake 5: Not Testing the Algorithm

A solution may appear correct but fail for some inputs.

**Solution:** Try sample values and verify each step manually.

---

## 16. Important Terminology

| Term | Meaning |
|---|---|
| Algorithm | Ordered steps used to solve a problem |
| Input | Information supplied to a solution |
| Process | Operations performed on the input |
| Output | Result produced by a solution |
| Program | Instructions implemented in a programming language |
| Pseudocode | Structured description of an algorithm |
| Implementation | Converting a solution into executable code |
| Debugging | Finding and correcting problems in a program |
| Test case | Input and expected result used to test a solution |

---

## 17. Interview Questions

### Q1. What is an algorithm?

An algorithm is a finite sequence of clear and ordered steps used to solve a problem or complete a task.

### Q2. Why are algorithms important?

They help us organize problem-solving logic, implement solutions, test correctness, and prepare for more advanced programming concepts.

### Q3. What is the difference between an algorithm and a program?

An algorithm describes the steps needed to solve a problem. A program implements those steps using a programming language.

### Q4. What is pseudocode?

Pseudocode describes algorithm logic using structured, human-readable instructions without requiring the exact syntax of a programming language.

### Q5. What are input, processing, and output?

- Input is the information required by the solution.
- Processing is the operation performed on that information.
- Output is the resulting information produced by the solution.

### Q6. Can one algorithm be implemented in different languages?

Yes. The same solution logic can often be implemented in Python, Java, C, C++, or other languages.

### Q7. What should you do before writing an algorithm?

Understand the problem, identify the inputs and expected outputs, and determine the necessary processing steps.

### Q8. What is the difference between an algorithm and a flowchart?

An algorithm presents the solution as ordered steps. A flowchart presents the solution visually using symbols and arrows.

---

## 18. Practice Questions

Try to write the algorithm first. After that, implement it in Python.

### Beginner Level

**Question 1:** Write an algorithm to display your name.

**Question 2:** Write an algorithm to add two numbers.

**Question 3:** Write an algorithm to calculate the difference between two numbers.

**Question 4:** Write an algorithm to calculate the product of two numbers.

**Question 5:** Write an algorithm to calculate the average of three numbers.

### Intermediate Level

**Question 6:** Write an algorithm to calculate the area of a rectangle.

**Question 7:** Write an algorithm to convert Celsius into Fahrenheit using:

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

**Question 8:** Write an algorithm to calculate the square of a number.

**Question 9:** Write pseudocode to calculate the total price of three items.

**Question 10:** Choose any one of the above questions and implement its algorithm in Python.

### Challenge

Choose a daily activity, such as preparing for college, and write a clear algorithm for it. Make sure each step is in a logical order and the procedure has a clear beginning and end.

---

## 19. Learning Checklist

- [ ] Understand the definition of an algorithm.
- [ ] Understand why algorithms are useful.
- [ ] Identify input, processing, and output.
- [ ] Write steps in a logical order.
- [ ] Distinguish algorithms from programs.
- [ ] Understand how algorithms differ from flowcharts.
- [ ] Write basic pseudocode.
- [ ] Convert an algorithm into Python code.
- [ ] Test an algorithm with sample values.
- [ ] Solve the practice questions.

---

## 20. What's Next?

Continue with the next subtopic:

**02 - Algorithm Steps**

In that folder, practise writing algorithms in a structured sequence and learn how to express problem-solving steps clearly.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `01_algorithm_basics.py` | Practical examples of basic algorithms |
| `README.md` | Detailed concepts, examples, theory, interview questions, and practice |

---

## Conclusion

Algorithms are a foundation of programming and problem-solving.

Before writing code, understand the problem, identify the input and output, design clear steps, and test the result.

Remember the main idea:

**Problem → Algorithm → Implementation → Testing**

Practising this approach will help you build a stronger foundation for Python programming and Data Structures and Algorithms.