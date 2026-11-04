# Pseudocode Basics — Python

Welcome to **Pseudocode Basics**, the first topic in the Pseudocode section of the DSA-Python repository.

This topic introduces pseudocode as a way to describe algorithm logic using simple, structured, language-independent instructions before implementing a solution in Python.

The goal is to understand the problem and design its solution before focusing on programming-language syntax.

---

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is Pseudocode?](#what-is-pseudocode)
4. [Why Is Pseudocode Useful?](#why-is-pseudocode-useful)
5. [Algorithm, Pseudocode, and Program](#algorithm-pseudocode-and-program)
6. [Common Pseudocode Conventions](#common-pseudocode-conventions)
7. [Basic Structure of Pseudocode](#basic-structure-of-pseudocode)
8. [Worked Example: Sum of Two Numbers](#worked-example-sum-of-two-numbers)
9. [Worked Example: Even or Odd](#worked-example-even-or-odd)
10. [Worked Example: Sum from 1 to N](#worked-example-sum-from-1-to-n)
11. [Assignment and Conditions](#assignment-and-conditions)
12. [Dry Runs and Testing](#dry-runs-and-testing)
13. [Time and Space Complexity](#time-and-space-complexity)
14. [Folder Structure](#folder-structure)
15. [How to Run the Program](#how-to-run-the-program)
16. [Practice Questions](#practice-questions)
17. [Common Mistakes](#common-mistakes)
18. [Interview Questions](#interview-questions)
19. [Learning Checklist](#learning-checklist)

---

## About This Topic

**Pseudocode** describes the logical steps of an algorithm in a structured, human-readable form. It uses programming-like instructions without requiring the exact syntax of a particular programming language.

For example:

```text
START
    INPUT A, B
    SUM <- A + B
    OUTPUT SUM
END
```

This describes a solution for adding two numbers.

The same logic can later be implemented in Python:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

Pseudocode focuses on what the solution should do rather than the exact syntax needed to execute it.

## Learning Objectives

After completing this topic, you should be able to:

- Define pseudocode and explain its purpose.
- Distinguish pseudocode from an algorithm and a Python program.
- Identify inputs, processing, and outputs.
- Represent assignment, calculations, and decisions.
- Understand common pseudocode keywords.
- Write algorithms in a clear and structured format.
- Use pseudocode to plan a Python solution.
- Perform a dry run using sample values.
- Test normal, boundary, and invalid inputs.
- Explain your problem-solving logic before writing code.

---

## What Is Pseudocode?

Pseudocode is a way of representing the logic of a solution using informal but structured instructions.

It is useful because a problem can be understood and reviewed without worrying about the exact syntax of Python, Java, C++, or another programming language.

### Characteristics of good pseudocode

Good pseudocode should be:

- **Clear:** Every instruction should be understandable.
- **Structured:** Steps should follow a logical order.
- **Language-independent:** It should not depend on one programming language's exact syntax.
- **Unambiguous:** Conditions and operations should have clear meanings.
- **Complete:** It should describe the required input, processing, and output.
- **Testable:** It should be possible to trace the steps using example values.

Pseudocode does not have one universally enforced syntax. Different textbooks, instructors, and teams may use different conventions.

---

## Why Is Pseudocode Useful?

### 1. Plan before coding

You can design the solution without becoming distracted by language syntax.

### 2. Communicate logic

Other people can understand the intended steps even if they use a different programming language.

### 3. Identify logic errors

Missing inputs, incorrect calculations, and incomplete conditions can be found before implementation.

### 4. Simplify debugging

A dry run of pseudocode can reveal unexpected results before any code is executed.

### 5. Prepare for interviews

Explaining the approach and algorithm before coding is an important problem-solving habit.

### 6. Support DSA learning

Pseudocode helps focus on the reasoning behind searching, sorting, loops, and data-structure operations.

---

## Algorithm, Pseudocode, and Program

| Concept | Meaning | Example |
|---|---|---|
| Algorithm | A sequence of steps to solve a problem | Read two values, add them, and display the result |
| Pseudocode | A structured description of those steps | `SUM <- A + B` |
| Flowchart | A visual representation of the steps | Input symbol → Process symbol → Output symbol |
| Program | Executable implementation in a programming language | Python code using `input()` and `print()` |

These concepts work together. An algorithm defines the logic, pseudocode expresses the steps in a readable structure, a flowchart visualizes the execution, and a program implements the solution.

---

## Common Pseudocode Conventions

The following conventions are used throughout this topic. They are illustrative rather than a universal language specification.

| Keyword or notation | Meaning | Example |
|---|---|---|
| `START` | Begin the algorithm | `START` |
| `END` | Finish the algorithm | `END` |
| `INPUT` | Read a value | `INPUT AGE` |
| `OUTPUT` | Display or return information | `OUTPUT TOTAL` |
| `<-` | Assign a value to a variable | `TOTAL <- A + B` |
| `IF` | Check a condition | `IF AGE >= 18 THEN` |
| `ELSE` | Specify an alternative branch | `ELSE` |
| `ELSE IF` | Check another condition | `ELSE IF N < 0 THEN` |
| `END IF` | Finish a conditional structure | `END IF` |
| `FOR` | Repeat over a range or sequence | `FOR I <- 1 TO N` |
| `WHILE` | Repeat while a condition is true | `WHILE N > 0` |
| `END FOR` | Finish a `FOR` structure | `END FOR` |
| `END WHILE` | Finish a `WHILE` structure | `END WHILE` |
| `MOD` | Calculate a remainder | `N MOD 2` |
| `AND` | Require both conditions to be true | `A > 0 AND B > 0` |
| `OR` | Require at least one condition to be true | `A = 0 OR B = 0` |
| `NOT` | Negate a condition | `NOT VALID` |

### Assignment using `<-`

An assignment places a value into a variable.

Example:

```text
A <- 10
B <- 20
TOTAL <- A + B
```

After these steps, `TOTAL` is 30.

The arrow `<-` is used here to distinguish assignment from comparison. Other pseudocode styles may use different notation.

### Comparison

A comparison checks whether a relationship between values is true or false.

Examples:

```text
A = B
A > B
A < B
N MOD 2 = 0
```

Be clear about whether an expression is assigning a value or testing a condition.

---

## Basic Structure of Pseudocode

A simple algorithm often follows this pattern:

```text
START
    INPUT required_values
    PROCESS the_values
    OUTPUT result
END
```

Not every algorithm has exactly one input or one output. Some algorithms do not require input, and others may produce multiple results or use decisions and repetition.

### Example: Calculate a rectangle's area

```text
START
    INPUT LENGTH
    INPUT WIDTH

    AREA <- LENGTH * WIDTH

    OUTPUT AREA
END
```

The instructions follow a sequential order: input, calculation, output.

---

## Worked Example: Sum of Two Numbers

**Problem:** Read two numbers and display their sum.

### Algorithm

1. Start.
2. Read A and B.
3. Calculate their sum.
4. Display the sum.
5. End.

### Pseudocode

```text
START
    INPUT A, B
    SUM <- A + B
    OUTPUT SUM
END
```

### Python implementation

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

### Dry run

Suppose A is 12 and B is 8.

| Step | Operation | Value |
|---|---|---:|
| 1 | Read A | 12 |
| 2 | Read B | 8 |
| 3 | Calculate A + B | 20 |
| 4 | Display SUM | 20 |

Expected output:

```text
Enter first number: 12
Enter second number: 8
Sum: 20
```

### Complexity

For fixed-size integer values:

- Time complexity: `O(1)`.
- Auxiliary space: `O(1)`.

The solution performs a fixed number of basic operations and uses a fixed number of variables.

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

For `N = 7`:

1. Calculate `7 MOD 2`.
2. The remainder is 1.
3. The condition `N MOD 2 = 0` is false.
4. Follow the `ELSE` branch.
5. Output `Odd`.

For `N = 8`, the remainder is zero, so the algorithm outputs `Even`.

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

        FOR NUMBER <- 1 TO N
            TOTAL <- TOTAL + NUMBER
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

| Iteration | NUMBER | TOTAL before | TOTAL after |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

Expected result: `10`.

### Complexity

- Time: `O(N)` for the loop-based algorithm.
- Auxiliary space: `O(1)` because a fixed number of variables is used.

---

## Assignment and Conditions

### Assignment example

```text
A <- 5
B <- 10
C <- A + B
OUTPUT C
```

The value assigned to C is 15.

### Conditional example

```text
INPUT MARKS

IF MARKS >= 40 THEN
    OUTPUT "PASS"
ELSE
    OUTPUT "FAIL"
END IF
```

This example uses an illustrative pass threshold of 40. Actual grading rules may differ.

### Multiple conditions

```text
INPUT MARKS

IF MARKS >= 90 THEN
    OUTPUT "A"
ELSE IF MARKS >= 75 THEN
    OUTPUT "B"
ELSE IF MARKS >= 60 THEN
    OUTPUT "C"
ELSE IF MARKS >= 40 THEN
    OUTPUT "D"
ELSE
    OUTPUT "F"
END IF
```

When using multiple conditions, write them in an order that matches the intended ranges. Test values at each boundary.

---

## Dry Runs and Testing

A dry run manually executes the pseudocode with sample values.

During a dry run, record:

- The current instruction.
- The values of important variables.
- The result of each condition.
- The number of loop iterations.
- The final output.

### Example test cases

| Problem | Test inputs |
|---|---|
| Sum of two numbers | 2 and 3; 0 and 5; -4 and 7 |
| Even or odd | 8; 7; 0; -3 |
| Largest of three | 8, 4, 2; 2, 8, 4; 3, 3, 3 |
| Sum from 1 to N | N = 1; N = 4; N = 0 |
| Factorial | N = 0; N = 1; N = 5; negative N |

Test cases help confirm that the written steps match the problem requirements.

---

## Time and Space Complexity

Pseudocode itself is not a particular executable language, but its operations can still be analysed using the intended algorithm.

| Algorithm pattern | Typical time complexity |
|---|---:|
| Fixed number of arithmetic operations | `O(1)` |
| Single loop from 1 to N | `O(N)` |
| Two nested loops over N values | `O(N²)` |
| Repeatedly halving a search range | `O(log N)` |
| Linear search through N items | `O(N)` worst case |

Auxiliary-space analysis considers the extra working memory required by the algorithm, excluding input storage under the usual convention.

For example, a loop that calculates a running total generally uses `O(1)` auxiliary space, while an algorithm that stores N generated values typically requires `O(N)` additional space.

---

## Folder Structure

```text
01_Pseudocode_Basics/
│
├── README.md
└── 01_pseudocode_basics.py
```

The Python file contains the interactive examples and practice questions. This README provides the theory, conventions, worked examples, testing guidance, and interview questions.

---

## How to Run the Program

Open PowerShell from your `DSA-Python` repository root.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\01_Pseudocode_Basics\01_pseudocode_basics.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Choose an option and follow the input prompts. Inside a sub-menu, select `0` to return to the main menu.

If Python is not recognized, verify that it is installed and available on your PATH. On Windows, the `py` command may also work.

---

## Practice Questions

The Python file includes 12 examples, 12 solved practice questions, and 5 unsolved questions.

### 12 Examples

1. Understand the meaning of pseudocode.
2. Compare an algorithm with pseudocode.
3. Represent sequential instructions.
4. Demonstrate input and output.
5. Understand assignment.
6. Express arithmetic operations.
7. Compare two numbers.
8. Check even or odd.
9. Classify a number.
10. Calculate rectangle area.
11. Calculate the sum from 1 to N.
12. Review pseudocode conventions.

### 12 Solved Practice Questions

1. Calculate the area of a square.
2. Calculate the average of three numbers.
3. Swap two values.
4. Convert Celsius to Fahrenheit.
5. Calculate simple interest.
6. Calculate integer quotient and remainder.
7. Find the largest of three numbers.
8. Check an illustrative voting-age threshold.
9. Determine pass or fail using an example threshold.
10. Check a leap year.
11. Calculate factorial.
12. Find the sum of the digits of an integer.

### 5 Unsolved Practice Questions

1. Check whether a number is prime.
2. Check whether a non-negative integer is a palindrome.
3. Calculate a percentage and assign a grade using stated thresholds.
4. Calculate the GCD of two integers using Euclid's algorithm.
5. Calculate a final bill after applying a discount and a separate tax percentage.

For each problem:

1. Identify inputs and outputs.
2. Write logical steps.
3. Convert the steps into pseudocode.
4. Dry-run the algorithm manually.
5. Implement it in Python.
6. Test boundary cases.
7. Explain the result and complexity.

---

## Common Mistakes

- Writing pseudocode that is too vague to follow.
- Mixing the algorithm's logic with unnecessary Python syntax.
- Forgetting to define an important input.
- Using a variable before assigning a value to it.
- Writing a condition without covering the intended alternative cases.
- Forgetting an `END IF` or loop-ending statement when the chosen convention uses one.
- Writing loops without a clear stopping condition.
- Ignoring invalid or boundary inputs.
- Using assignment notation and comparison notation inconsistently.
- Copying an algorithm without performing a dry run.
- Assuming pseudocode has one universal syntax.

---

## Interview Questions

**1. What is pseudocode?**

Pseudocode is a structured, human-readable description of an algorithm that is not tied to one programming language's exact syntax.

**2. Why is pseudocode useful?**

It helps plan, explain, review, and test solution logic before implementation.

**3. Is pseudocode executable?**

Ordinary pseudocode is not directly executable because it does not follow a single formal programming-language syntax.

**4. What is the difference between pseudocode and a flowchart?**

Pseudocode describes steps in text, while a flowchart represents the steps graphically.

**5. What does `INPUT` mean?**

It represents receiving the data required by the algorithm.

**6. What does `OUTPUT` mean?**

It represents displaying or returning information.

**7. What does `<-` represent in this topic?**

It represents assigning a value to a variable.

**8. What does `MOD` represent?**

It represents the remainder after division.

**9. How can pseudocode represent a decision?**

Using conditional structures such as `IF`, `ELSE IF`, and `ELSE`.

**10. How can pseudocode represent repetition?**

Using loop structures such as `FOR` and `WHILE`.

**11. What is a dry run?**

It is a manual trace of an algorithm using example input values.

**12. Why should pseudocode be written before code?**

It makes it easier to check the logic independently from programming-language syntax.

---

## Learning Checklist

- [ ] I understand what pseudocode is.
- [ ] I can distinguish an algorithm, pseudocode, a flowchart, and a program.
- [ ] I can write pseudocode for basic calculations.
- [ ] I understand input, output, and assignment.
- [ ] I can write pseudocode for decisions.
- [ ] I can represent a loop using structured steps.
- [ ] I can dry-run an algorithm.
- [ ] I can translate simple pseudocode into Python.
- [ ] I have run the examples.
- [ ] I have studied the solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Pseudocode Basics, proceed to **Input/Output Pseudocode**, where you will practise expressing input, calculations, and output using structured, language-independent steps.
