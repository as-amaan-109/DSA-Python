# Pseudocode — Python Programming

Welcome to the **Pseudocode** section of Week 1: Programming Fundamentals in the DSA-Python repository.

This section teaches you how to express programming logic through clear, structured, language-independent instructions before implementing a solution in Python.

You will progress from basic pseudocode conventions to input/output operations, conditional logic, and loops. These concepts help you plan algorithms, explain your approach, and prepare for problem-solving and Data Structures and Algorithms (DSA).

---

## Table of Contents

1. [About This Section](#about-this-section)
2. [Learning Objectives](#learning-objectives)
3. [What Is Pseudocode?](#what-is-pseudocode)
4. [Why Is Pseudocode Important?](#why-is-pseudocode-important)
5. [Algorithm vs. Pseudocode vs. Flowchart vs. Program](#algorithm-vs-pseudocode-vs-flowchart-vs-program)
6. [Folder Structure](#folder-structure)
7. [Topics Covered](#topics-covered)
8. [Common Pseudocode Conventions](#common-pseudocode-conventions)
9. [Fundamental Programming Structures](#fundamental-programming-structures)
10. [Complete Problem-Solving Workflow](#complete-problem-solving-workflow)
11. [Worked Example: Sum of Two Numbers](#worked-example-sum-of-two-numbers)
12. [Worked Example: Even or Odd](#worked-example-even-or-odd)
13. [Worked Example: Sum from 1 to N](#worked-example-sum-from-1-to-n)
14. [Dry Runs and Testing](#dry-runs-and-testing)
15. [How to Run the Python Programs](#how-to-run-the-python-programs)
16. [Practice Guidelines](#practice-guidelines)
17. [Common Mistakes](#common-mistakes)
18. [Interview Questions](#interview-questions)
19. [Completion Checklist](#completion-checklist)
20. [Next Section](#next-section)

---

## About This Section

Pseudocode is a structured way to describe the steps of an algorithm without requiring the exact syntax of a programming language.

Instead of immediately writing Python code, you first describe:

- What input the problem requires.
- What processing or calculations must be performed.
- Which conditions determine the next action.
- Which instructions must be repeated.
- What output the solution should produce.

For example, the pseudocode for adding two numbers is:

```text
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
END
```

After understanding these steps, you can implement the same logic in Python, C++, Java, or another programming language.

The goal is to focus on the correctness of the solution before dealing with programming-language syntax.

## Learning Objectives

After completing this section, you should be able to:

- Explain pseudocode and its purpose.
- Distinguish an algorithm from pseudocode and a program.
- Use clear instructions to describe a solution.
- Represent input, processing, and output.
- Use variables and assignment.
- Express arithmetic calculations.
- Represent decisions with conditional statements.
- Represent repetition with loops.
- Use comparison and logical operators.
- Translate pseudocode into Python.
- Perform dry runs using sample values.
- Test normal, boundary, and invalid inputs.
- Explain the basic time and auxiliary-space complexity of a solution.
- Prepare structured approaches for programming and DSA problems.

---

## What Is Pseudocode?

Pseudocode is a human-readable representation of an algorithm using structured instructions.

It often resembles programming code but is not restricted to the syntax of a particular programming language.

### Example

```text
START
    INPUT LENGTH
    INPUT WIDTH

    AREA <- LENGTH * WIDTH

    OUTPUT AREA
END
```

This describes the steps required to calculate the area of a rectangle.

### Characteristics of good pseudocode

**Clarity:** Each instruction should be understandable.

**Logical order:** The steps should follow the order needed to solve the problem.

**Language independence:** The solution should not depend on a particular programming language's exact syntax.

**Completeness:** The instructions should cover the necessary inputs, processing, decisions, repetition, and output.

**Consistency:** Use the same notation for assignment, conditions, and loop structures throughout a solution.

**Testability:** The algorithm should be possible to trace manually using sample input values.

Pseudocode does not have a single universally enforced syntax. Different textbooks and development teams may use different conventions. For this repository, the examples use a consistent set of keywords documented below.

---

## Why Is Pseudocode Important?

### 1. Plan before coding

Pseudocode lets you focus on the logic of a solution before worrying about Python syntax.

### 2. Improve logical thinking

Writing the steps forces you to think carefully about the inputs, operations, conditions, and final output.

### 3. Identify errors early

A dry run can reveal missing steps, incorrect calculations, and incomplete conditions before implementation.

### 4. Communicate your approach

Pseudocode can be understood by people working in different programming languages.

### 5. Simplify debugging

When a program produces an unexpected result, you can compare its implementation with the intended algorithm.

### 6. Prepare for DSA

Pseudocode helps build the habit of designing and explaining an algorithm before coding it.

---

## Algorithm vs. Pseudocode vs. Flowchart vs. Program

| Concept | Meaning | Representation |
|---|---|---|
| Algorithm | A sequence of steps that solves a problem | Ordered instructions |
| Pseudocode | A structured description of an algorithm | Language-independent text |
| Flowchart | A visual representation of the solution's logic | Symbols, arrows, and branches |
| Program | An implementation written in a programming language | Executable code, such as Python |

These concepts support different stages of problem-solving.

For example, to find the largest of two numbers:

1. **Algorithm:** Read two numbers, compare them, and display the larger value.
2. **Pseudocode:** Express the comparison using `IF`, `ELSE IF`, and `ELSE`.
3. **Flowchart:** Draw the input steps, decision diamond, and output paths.
4. **Program:** Implement the logic using Python conditional statements.

---

## Folder Structure

```text
01-Pseudocode/
│
├── README.md
│
├── 01_Pseudocode_Basics/
│   ├── README.md
│   └── 01_pseudocode_basics.py
│
├── 02_Input_Output_Pseudocode/
│   ├── README.md
│   └── 02_input_output_pseudocode.py
│
├── 03_Conditional_Pseudocode/
│   ├── README.md
│   └── 03_conditional_pseudocode.py
│
└── 04_Loop_Pseudocode/
    ├── README.md
    └── 04_loop_pseudocode.py
```

Each topic folder contains a Python file with examples and practice questions, together with a README explaining the concepts.

Keep the folder names and filename capitalization consistent with your actual repository.

---

## Topics Covered

### 1. Pseudocode Basics

**Folder:** [`01_Pseudocode_Basics/`](01_Pseudocode_Basics/)

This topic introduces pseudocode and the conventions used to express algorithms.

Key concepts:

- Definition and purpose of pseudocode.
- Algorithm versus pseudocode.
- Input, processing, and output.
- Assignment and variables.
- Arithmetic operations.
- Basic decision structures.
- Simple repetition.
- Translating pseudocode into Python.

**Learning outcome:** Write clear, ordered instructions for a basic programming problem before implementing the solution.

### 2. Input/Output Pseudocode

**Folder:** [`02_Input_Output_Pseudocode/`](02_Input_Output_Pseudocode/)

This topic focuses on collecting values, performing calculations, and producing results.

Key concepts:

- `INPUT` and `OUTPUT`.
- The Input–Process–Output (IPO) model.
- Variable assignment.
- Basic arithmetic.
- Area and perimeter calculations.
- Averages and percentages.
- Temperature and unit conversions.
- Simple interest.
- Multiple inputs and accumulated totals.
- Input validation.

**Learning outcome:** Describe complete input/output operations using pseudocode and implement them in Python.

### 3. Conditional Pseudocode

**Folder:** [`03_Conditional_Pseudocode/`](03_Conditional_Pseudocode/)

This topic explains how an algorithm chooses between alternative actions.

Key concepts:

- `IF` statements.
- `IF-ELSE` structures.
- `ELSE IF` and multiple branches.
- Nested conditions.
- Comparison operators.
- Logical operators such as `AND`, `OR`, and `NOT`.
- Number classification.
- Largest and smallest values.
- Grade calculation.
- Divisibility and leap-year checks.
- Validation and range-based decisions.

**Learning outcome:** Write conditional pseudocode that covers the intended cases and can be translated into Python.

### 4. Loop Pseudocode

**Folder:** [`04_Loop_Pseudocode/`](04_Loop_Pseudocode/)

This topic teaches how to represent repeated operations.

Key concepts:

- `FOR` loops.
- `WHILE` loops.
- Initialization, condition, loop body, and update.
- Counting and summation.
- Factorial and Fibonacci sequences.
- Digit counting and digit sums.
- Reversing integers.
- Prime-number checks.
- Nested loops.
- Sentinel-controlled repetition.
- `BREAK` and `CONTINUE`.
- Loop termination and infinite-loop prevention.

**Learning outcome:** Design loop-based algorithms that clearly explain initialization, repetition, updates, and termination.

---

## Common Pseudocode Conventions

This repository uses the following conventions to keep examples readable and consistent.

| Keyword or notation | Meaning | Example |
|---|---|---|
| `START` | Begin an algorithm | `START` |
| `END` | Finish an algorithm | `END` |
| `INPUT` | Read data | `INPUT A, B` |
| `OUTPUT` | Display or return a result | `OUTPUT TOTAL` |
| `<-` | Assign a value | `TOTAL <- A + B` |
| `IF` | Evaluate a condition | `IF A > B THEN` |
| `ELSE` | Define an alternative path | `ELSE` |
| `ELSE IF` | Evaluate another condition | `ELSE IF N < 0 THEN` |
| `END IF` | Close a conditional structure | `END IF` |
| `FOR` | Repeat over a range or sequence | `FOR I <- 1 TO N` |
| `WHILE` | Repeat while a condition is true | `WHILE N > 0` |
| `END FOR` | Close a `FOR` loop | `END FOR` |
| `END WHILE` | Close a `WHILE` loop | `END WHILE` |
| `MOD` | Calculate a remainder | `N MOD 2` |
| `DIV` | Integer division in this convention | `N DIV 10` |
| `AND` | Both conditions must be true | `A > 0 AND B > 0` |
| `OR` | At least one condition must be true | `A = 0 OR B = 0` |
| `NOT` | Negate a condition | `NOT VALID` |
| `BREAK` | Exit the nearest loop | `BREAK` |
| `CONTINUE` | Skip to the next iteration | `CONTINUE` |

These keywords are conventions for describing algorithms. They are not Python commands and do not need to follow Python's exact syntax.

### Assignment versus comparison

Assignment gives a variable a value:

```text
TOTAL <- A + B
```

Comparison checks a relationship between values:

```text
IF A = B THEN
    OUTPUT "Equal"
END IF
```

In the examples above, `=` is used for equality comparison inside pseudocode. In Python, `=` is used for assignment and `==` is used for equality comparison.

---

## Fundamental Programming Structures

The pseudocode topics build on three common structures.

### 1. Sequence

Instructions execute one after another.

```text
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
END
```

Typical uses: addition, averages, area calculations, and conversions.

### 2. Selection

A condition determines which branch executes.

```text
INPUT N

IF N MOD 2 = 0 THEN
    OUTPUT "Even"
ELSE
    OUTPUT "Odd"
END IF
```

Typical uses: comparisons, classifications, eligibility examples, and range-based calculations.

### 3. Iteration

A collection of instructions repeats according to a rule.

```text
INPUT N
TOTAL <- 0

FOR I <- 1 TO N
    TOTAL <- TOTAL + I
END FOR

OUTPUT TOTAL
```

Typical uses: counting, summation, factorial, repeated input, and sequence generation.

These structures can be combined to solve larger problems.

---

## Complete Problem-Solving Workflow

Use this workflow when learning pseudocode and preparing to write Python programs.

### Step 1: Understand the problem

Read the problem statement carefully and identify the expected result.

### Step 2: Identify the inputs

List the values required to solve the problem.

### Step 3: Identify the outputs

Decide what the algorithm must display or return.

### Step 4: Design the logic

Determine the calculations, comparisons, or repeated operations needed.

### Step 5: Write the algorithm

Describe the required steps in plain language.

### Step 6: Write pseudocode

Represent the solution with structured instructions.

### Step 7: Perform a dry run

Manually execute the steps with sample input values.

### Step 8: Implement the solution

Translate the verified logic into Python.

### Step 9: Test the program

Test normal cases, boundary values, and invalid inputs when applicable.

### Step 10: Analyse the solution

Consider correctness, time complexity, and auxiliary-space requirements.

---

## Worked Example: Sum of Two Numbers

**Problem:** Read two numbers and display their sum.

### Algorithm

1. Start.
2. Read A and B.
3. Calculate their sum.
4. Display the total.
5. End.

### Pseudocode

```text
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
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

Assume `A = 12` and `B = 8`.

| Step | Operation | Result |
|---|---|---:|
| 1 | Read A | 12 |
| 2 | Read B | 8 |
| 3 | Calculate A + B | 20 |
| 4 | Display the total | 20 |

Expected output:

```text
Enter first integer: 12
Enter second integer: 8
Sum: 20
```

For fixed-size integer values, this algorithm performs a constant number of basic operations, so its time complexity is `O(1)` and its auxiliary space is `O(1)` under the standard introductory model.

---

## Worked Example: Even or Odd

**Problem:** Determine whether an integer is even or odd.

### Pseudocode

```text
START
    INPUT N

    IF N MOD 2 = 0 THEN
        OUTPUT "Even"
    ELSE
        OUTPUT "Odd"
    END IF
END
```

### Python implementation

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Dry run

| Input | Condition | Output |
|---:|---|---|
| 8 | Remainder is zero | Even |
| 7 | Remainder is one | Odd |
| 0 | Remainder is zero | Even |
| -4 | Remainder is zero | Even |

The algorithm uses a fixed number of operations for a fixed-size integer model, so its time complexity is `O(1)` and its auxiliary space is `O(1)`.

---

## Worked Example: Sum from 1 to N

**Problem:** Calculate the sum of integers from 1 through a positive integer N.

### Pseudocode

```text
START
    INPUT N

    IF N < 1 THEN
        OUTPUT "N must be positive"
    ELSE
        TOTAL <- 0

        FOR I <- 1 TO N
            TOTAL <- TOTAL + I
        END FOR

        OUTPUT TOTAL
    END IF
END
```

### Python implementation

```python
n = int(input("Enter a positive integer: "))

if n < 1:
    print("N must be greater than zero.")
else:
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum:", total)
```

### Dry run for N = 4

| Iteration | I | Total before | Total after |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

Expected result: `10`.

For this loop-based solution, time complexity is `O(N)` and auxiliary space is `O(1)` under the standard introductory model.

---

## Dry Runs and Testing

A **dry run** is a manual trace of an algorithm using specific input values.

During a dry run, record:

- The current instruction.
- The values of important variables.
- The result of each condition.
- The number of loop iterations.
- The final output.

### Recommended test cases

| Problem type | Useful test inputs |
|---|---|
| Addition | Positive numbers, zero, negative numbers |
| Comparison | First number larger, second number larger, equal values |
| Even/odd | Even integer, odd integer, zero, negative integer |
| Grade calculation | Values at and around the thresholds |
| Factorial | 0, 1, a small positive integer, negative input |
| Sum from 1 to N | N = 1, N = 5, N = 0 |
| Input validation | Valid values, out-of-range values, invalid text |

Testing varied inputs helps identify errors that may not appear in one simple example.

---

## Time and Space Complexity

Complexity analysis describes how the amount of work and memory used by an algorithm grows as the input size increases.

| Algorithm pattern | Typical time complexity |
|---|---:|
| Fixed number of basic operations | `O(1)` |
| One loop over N values | `O(N)` |
| Two nested loops over N values | `O(N²)` |
| Repeatedly halving a search range | `O(log N)` |
| Linear search through N values | `O(N)` worst case |

Auxiliary space describes additional working memory, excluding the input storage under the usual convention.

- A running total usually requires `O(1)` auxiliary space.
- Storing N generated values normally requires `O(N)` auxiliary space.
- Nested loops do not automatically require quadratic memory; the stored data determines the space requirement.

These are introductory estimates that use a simplified model of operation costs.

---

## How to Run the Python Programs

Open PowerShell at the root of the `DSA-Python` repository.

Example: run Pseudocode Basics.

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\01_Pseudocode_Basics\01_pseudocode_basics.py"
```

Run Input/Output Pseudocode:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\02_Input_Output_Pseudocode\02_input_output_pseudocode.py"
```

Run Conditional Pseudocode:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\03_Conditional_Pseudocode\03_conditional_pseudocode.py"
```

Run Loop Pseudocode:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\04_Loop_Pseudocode\04_loop_pseudocode.py"
```

Each program provides an interactive menu for examples, solved practice questions, and unsolved questions.

If the `python` command is not recognized, verify your Python installation. The Windows `py` command may also work.

---

## Practice Guidelines

Each topic is designed around three categories:

- **12 examples:** Demonstrate important concepts.
- **12 solved practice questions:** Provide implementations to study and understand.
- **5 unsolved questions:** Encourage independent problem-solving.

For every practice question:

1. Understand the requirement.
2. Identify input and output.
3. Write the algorithm in plain language.
4. Express it in pseudocode.
5. Perform a dry run.
6. Implement the solution in Python.
7. Test boundary cases.
8. Explain the logic and complexity.

Do not merely copy the solution. Try to explain why each variable, condition, and loop is required.

---

## Common Mistakes

- Writing pseudocode that is too vague.
- Mixing assignment and comparison.
- Forgetting to identify all required inputs.
- Writing conditions without covering the intended cases.
- Forgetting to update variables in a loop.
- Creating loops without clear termination conditions.
- Ignoring zero, negative values, or range boundaries.
- Using the wrong formula.
- Testing only one example.
- Implementing Python code that does not match the intended pseudocode.
- Memorizing a solution without understanding its logic.

---

## Interview Questions

**1. What is pseudocode?**

Pseudocode is a structured, human-readable description of an algorithm that is not tied to one programming language's exact syntax.

**2. Why is pseudocode useful?**

It helps design, communicate, review, and test logic before implementation.

**3. What is the difference between an algorithm and pseudocode?**

An algorithm describes the solution steps, while pseudocode expresses those steps in a structured, readable form.

**4. What is the difference between pseudocode and a flowchart?**

Pseudocode represents the logic in text, while a flowchart represents it graphically.

**5. What are the three fundamental programming structures?**

Sequence, selection, and iteration.

**6. What does `INPUT` mean?**

It represents receiving data required by an algorithm.

**7. What does `<-` mean in this repository's pseudocode?**

It represents assignment to a variable.

**8. What is the purpose of an IF-ELSE structure?**

It selects between alternative actions based on a condition.

**9. What is the purpose of a loop?**

It repeats operations according to a range, sequence, or condition.

**10. What is a dry run?**

A dry run manually traces an algorithm with sample values.

**11. Why should boundary cases be tested?**

They help identify mistakes in conditions, ranges, and termination rules.

**12. How does pseudocode help with DSA?**

It helps explain the steps and logic of algorithms before implementing them in a programming language.

---

## Completion Checklist

- [ ] I understand the purpose of pseudocode.
- [ ] I can distinguish algorithms, pseudocode, flowcharts, and programs.
- [ ] I understand the common pseudocode conventions.
- [ ] I can write pseudocode for basic calculations.
- [ ] I can represent input and output.
- [ ] I can express decisions using conditional structures.
- [ ] I can represent repetition with loops.
- [ ] I can convert pseudocode into Python.
- [ ] I can perform dry runs and test edge cases.
- [ ] I have completed all four pseudocode topics.
- [ ] I have studied the solved questions.
- [ ] I have attempted all unsolved practice questions.

---

## Next Section

After completing the four topics in this section, continue to **Problem-Solving**.

The next section focuses on breaking problems into manageable parts, understanding requirements, identifying patterns, and designing structured solutions before implementation.
