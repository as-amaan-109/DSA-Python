# Flowcharts — Python Programming

Welcome to the **Flowcharts** section of the DSA-Python repository.

This section focuses on representing algorithms visually using standard flowchart symbols, decision branches, and loop structures. It helps you understand program logic before translating it into pseudocode and Python code.

The goal is to develop a structured problem-solving approach that will support your future Data Structures and Algorithms (DSA) practice.

---

## Table of Contents

1. [About This Section](#about-this-section)
2. [Learning Objectives](#learning-objectives)
3. [Why Are Flowcharts Important?](#why-are-flowcharts-important)
4. [Common Flowchart Symbols](#common-flowchart-symbols)
5. [Types of Control Flow](#types-of-control-flow)
6. [Folder Structure](#folder-structure)
7. [Topics Covered](#topics-covered)
8. [How to Design a Flowchart](#how-to-design-a-flowchart)
9. [Worked Example: Sum of Two Numbers](#worked-example-sum-of-two-numbers)
10. [Flowchart to Python Conversion](#flowchart-to-python-conversion)
11. [Testing and Dry Runs](#testing-and-dry-runs)
12. [Common Mistakes](#common-mistakes)
13. [How to Run the Programs](#how-to-run-the-programs)
14. [Recommended Learning Order](#recommended-learning-order)
15. [Practice Guidelines](#practice-guidelines)
16. [Interview Questions](#interview-questions)
17. [Learning Checklist](#learning-checklist)
18. [Next Section](#next-section)

---

## About This Section

A **flowchart** is a graphical representation of an algorithm or process. It uses standard symbols connected by arrows to show the order of operations and the possible paths through a solution.

A simple flowchart may follow this pattern:

```text
        ( START )
            |
            v
       / Input Data /
            |
            v
        [ Process ]
            |
            v
      / Display Result /
            |
            v
         ( END )
```

More advanced flowcharts can include decisions and loops.

For example, a flowchart can show how a program checks whether a number is even or odd, calculates a factorial, searches for a value, or processes a series of inputs.

This section contains five topic folders, progressing from basic symbols to combined flowchart problems.

## Learning Objectives

After completing this section, you should be able to:

- Explain what a flowchart is and why it is used.
- Identify commonly used flowchart symbols.
- Represent input, processing, and output operations.
- Design flowcharts using sequence and decisions.
- Represent loops and repetition visually.
- Convert problem statements into algorithms and flowcharts.
- Translate flowchart logic into Python code.
- Perform dry runs using sample inputs.
- Identify missing steps and incorrect branches.
- Test normal cases, boundary cases, and invalid inputs.
- Explain the basic time and auxiliary-space complexity of simple algorithms.

---

## Why Are Flowcharts Important?

Flowcharts help programmers organize their thoughts before implementing a solution.

### 1. Better problem understanding

A diagram makes the sequence of operations easier to follow.

### 2. Clear decision-making

Decision symbols show how different conditions lead to different outcomes.

### 3. Easier debugging

Tracing arrows through a diagram can help reveal missing operations or incorrect branches.

### 4. Improved communication

A flowchart can explain the logic of a program to classmates, teachers, teammates, or interviewers.

### 5. Preparation for programming

Flowcharts provide an intermediate step between understanding a problem and writing code.

### 6. Stronger DSA foundations

Learning to represent loops, decisions, and repeated operations visually helps build algorithmic thinking.

---

## Common Flowchart Symbols

| Symbol | Shape | Purpose | Example |
|---|---|---|---|
| Terminal | Oval or rounded terminal | Indicates start or end | Start, End |
| Process | Rectangle | Represents an operation or calculation | `SUM = A + B` |
| Input/Output | Parallelogram | Reads or displays data | Input A, Display SUM |
| Decision | Diamond | Checks a condition and selects a path | `N % 2 == 0?` |
| Flow line | Arrow | Shows the direction of execution | Connects two steps |
| Connector | Small circle or labelled connector | Links different parts of a diagram | Continue at connector A |

### Terminal symbol

Used to identify the beginning and end of a flowchart.

### Process symbol

Represents calculations, assignments, and other processing operations.

Examples:

```text
SUM = A + B
AREA = LENGTH * WIDTH
COUNT = COUNT + 1
```

### Input/Output symbol

Represents reading input or displaying results.

Examples:

```text
INPUT A
INPUT B
OUTPUT SUM
```

### Decision symbol

Evaluates a condition and directs the flow along an appropriate branch.

Example:

```text
       < N % 2 == 0? >
          /       \
        Yes        No
         |          |
       [Even]      [Odd]
```

Every decision branch should be labelled clearly so that the flowchart can be followed without ambiguity.

---

## Types of Control Flow

Flowcharts commonly represent three fundamental control structures.

### 1. Sequence

Instructions execute one after another.

```text
Start
  |
Input A, B
  |
SUM = A + B
  |
Display SUM
  |
End
```

Typical use: addition, rectangle area, average, and unit conversions.

### 2. Selection or Decision

The next operation depends on a condition.

```text
        < Marks >= 40? >
           /       \
         Yes        No
          |          |
       [PASS]      [FAIL]
```

Typical use: even/odd checks, largest-number problems, grade calculation, and eligibility examples.

### 3. Iteration or Loop

Instructions repeat while a condition allows another iteration.

```text
       [N = 1]
           |
           v
       < N <= 5? >
         /      \
       Yes       No
        |         |
   [Display N]  [End]
        |
    [N = N + 1]
        |
        └────> Return to condition
```

Typical use: summation, factorial, multiplication tables, number sequences, and searching.

---

## Folder Structure

```text
Flowcharts/
│
├── README.md
│
├── 01_FlowChart_Basics/
│   ├── README.md
│   └── 01_flowchart_basics.py
│
├── 02_Input_Output_FlowChart/
│   ├── README.md
│   └── 02_input_output_flowchart.py
│
├── 03_Decision_FlowChart/
│   ├── README.md
│   └── 03_decision_flowchart.py
│
├── 04_Loop_FlowChart/
│   ├── README.md
│   └── 04_loop_flowchart.py
│
└── 05_Practice_FlowChart/
    ├── README.md
    └── 05_practice_flowcharts.py
```

**Note:** Folder and filename capitalization should match the actual names used in your local repository.

---

## Topics Covered

### 1. Flowchart Basics

**Folder:** `01_FlowChart_Basics/`

Learn the purpose of flowcharts and identify their main symbols.

Key concepts:

- Flowchart definition and uses.
- Terminal, process, input/output, and decision symbols.
- Flow lines and connectors.
- Sequence of operations.
- Basic flowchart design.
- Connecting algorithms with Python programs.

### 2. Input/Output Flowcharts

**Folder:** `02_Input_Output_FlowChart/`

Learn how to represent reading values, processing data, and displaying results.

Key concepts:

- Input and output operations.
- The Input–Process–Output (IPO) model.
- Reading text, integers, and decimal numbers.
- Arithmetic calculations.
- Area, averages, percentages, and conversions.
- Input validation.
- Dry runs and expected outputs.

### 3. Decision Flowcharts

**Folder:** `03_Decision_FlowChart/`

Learn how to represent conditions and alternative execution paths.

Key concepts:

- Decision diamonds.
- Yes/No and True/False branches.
- Comparison operators.
- Logical operators such as `and`, `or`, and `not`.
- `if`, `if-else`, and `if-elif-else`.
- Nested decisions.
- Number classification, grade calculation, and leap-year logic.

### 4. Loop Flowcharts

**Folder:** `04_Loop_FlowChart/`

Learn to represent repetition and termination conditions.

Key concepts:

- Initialization, condition, loop body, and update.
- `for` loops and `while` loops.
- Loop conditions and exit paths.
- Counter-controlled and sentinel-controlled loops.
- Summation and factorial.
- Fibonacci sequences.
- Digit operations.
- Nested loops.
- `break` and `continue`.
- Identifying unintended infinite loops.

### 5. Practice Flowcharts

**Folder:** `05_Practice_FlowChart/`

Apply sequence, selection, and iteration together.

Key concepts:

- Basic calculations and comparisons.
- Number properties.
- Factorial and Fibonacci.
- Prime-number checks.
- GCD and LCM.
- Searching and duplicate removal.
- Dry runs and test cases.
- Integrated problem-solving exercises.

---

## How to Design a Flowchart

Follow this process for each programming problem.

### Step 1: Understand the problem

Read the statement carefully and identify what must be solved.

### Step 2: Identify the inputs

List the values required to solve the problem.

### Step 3: Identify the outputs

Determine what result the program should produce.

### Step 4: Plan the operations

Identify formulas, assignments, comparisons, and repeated operations.

### Step 5: Write the algorithm

Describe the solution as a series of clear steps.

### Step 6: Select the symbols

Use the appropriate symbols for start/end, input/output, processing, and decisions.

### Step 7: Connect the symbols

Use arrows to show the direction of execution.

### Step 8: Include all paths

Make sure every decision branch and loop exit is clear.

### Step 9: Perform a dry run

Trace the flowchart manually using sample values.

### Step 10: Implement in Python

Translate the verified logic into code and test the program.

---

## Worked Example: Sum of Two Numbers

**Problem:** Read two integers and display their sum.

### Algorithm

1. Start.
2. Read the first integer A.
3. Read the second integer B.
4. Calculate `SUM = A + B`.
5. Display SUM.
6. End.

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

### Pseudocode

```text
START
INPUT A
INPUT B
SUM = A + B
OUTPUT SUM
END
```

### Python implementation

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

total = a + b

print("Sum:", total)
```

### Dry run

Suppose `A = 10` and `B = 15`.

| Step | Operation | Result |
|---|---|---:|
| 1 | Read A | 10 |
| 2 | Read B | 15 |
| 3 | Calculate A + B | 25 |
| 4 | Display the sum | 25 |

Expected output:

```text
Enter first integer: 10
Enter second integer: 15
Sum: 25
```

For fixed-size integer inputs, this algorithm performs a constant number of basic operations, so its time complexity is `O(1)` and its auxiliary space is `O(1)` under the usual introductory model.

---

## Flowchart to Python Conversion

| Flowchart element | Common Python equivalent |
|---|---|
| Start | Program entry |
| Input | `input()` |
| Process | Assignment or calculation |
| Output | `print()` |
| Decision | `if`, `elif`, `else` |
| Repetition | `for` or `while` |
| End | Program termination or function return |
| Flow line | Execution order |

These are conceptual equivalents. Python does not require a separate statement for every flowchart symbol.

---

## Testing and Dry Runs

A dry run manually follows the flowchart and records the values at each step.

When testing a flowchart:

- Try at least one normal input.
- Test every decision branch.
- Check important boundary values.
- Verify the loop's first and last iterations.
- Test invalid inputs where validation is required.
- Ensure the output matches the problem requirement.

For example, when testing an even/odd flowchart, use an even number, an odd number, zero, and a negative integer.

Testing multiple paths helps reveal errors that might not appear with a single sample value.

---

## Common Mistakes

- Forgetting to include a Start or End symbol.
- Using the wrong symbol for an operation.
- Leaving decision branches unlabelled.
- Connecting arrows in an unclear direction.
- Forgetting to show the exit path of a loop.
- Creating a loop without an understandable termination condition.
- Placing a calculation before the required input is available.
- Ignoring boundary and invalid inputs.
- Designing a flowchart that does not match the Python implementation.
- Testing only one possible outcome.

---

## How to Run the Programs

Open PowerShell in the root directory of the `DSA-Python` repository.

Example command for the Flowchart Basics program:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\01_FlowChart_Basics\01_flowchart_basics.py"
```

Each topic folder contains its own Python file. Run the relevant file to access its examples and practice menu.

If the `python` command is not recognized, check that Python is installed and available on your PATH. On Windows, the `py` command may work instead.

---

## Recommended Learning Order

Complete the folders in this order:

1. `01_FlowChart_Basics`
2. `02_Input_Output_FlowChart`
3. `03_Decision_FlowChart`
4. `04_Loop_FlowChart`
5. `05_Practice_FlowChart`

This progression starts with the basic symbols, moves to inputs and outputs, introduces decisions and repetition, and finishes with integrated problems.

---

## Practice Guidelines

For every problem, follow the same approach:

1. Understand the problem statement.
2. Identify inputs and outputs.
3. Write an algorithm in ordered steps.
4. Draw the flowchart.
5. Write pseudocode.
6. Perform a dry run.
7. Implement the solution in Python.
8. Test normal and boundary cases.
9. Explain the logic and complexity.

Each topic's Python file contains **12 examples, 12 solved practice questions, and 5 unsolved practice questions**. Attempt the unsolved questions independently before checking other solutions.

---

## Interview Questions

**1. What is a flowchart?**

A flowchart is a graphical representation of an algorithm or process.

**2. What are the main flowchart symbols?**

Common symbols include the terminal, process, input/output, decision, flow line, and connector.

**3. Which symbol represents input and output?**

A parallelogram is commonly used for input/output operations.

**4. Which symbol represents a decision?**

A diamond represents a decision or condition.

**5. What is the difference between sequence and selection?**

Sequence executes instructions in order, while selection chooses a path based on a condition.

**6. What is iteration?**

Iteration repeats a set of steps according to a condition or sequence.

**7. What is a dry run?**

A dry run manually traces an algorithm using sample input values.

**8. How do you convert a flowchart into Python?**

Translate input/output symbols into input and print operations, process symbols into calculations, decision symbols into conditional statements, and loops into iteration statements.

**9. Why are flowcharts useful before programming?**

They make the logical flow easier to understand and help identify missing steps before coding.

**10. Why should boundary cases be tested?**

Boundary testing can identify incorrect conditions, range errors, and loop termination issues.

---

## Learning Checklist

- [ ] I understand the purpose of flowcharts.
- [ ] I can identify common flowchart symbols.
- [ ] I can represent input, processing, and output.
- [ ] I can draw sequence-based flowcharts.
- [ ] I can represent decisions and multiple paths.
- [ ] I can draw loops with valid exit paths.
- [ ] I can convert a flowchart into pseudocode.
- [ ] I can implement the logic in Python.
- [ ] I can perform dry runs and test edge cases.
- [ ] I have completed all five topic folders.
- [ ] I have attempted the unsolved practice questions.

---

## Next Section

After completing Flowcharts, proceed to **Pseudocode and Problem-Solving**.

This section builds on visual algorithms by teaching you to express logic using structured, language-independent instructions before converting it into Python code.
