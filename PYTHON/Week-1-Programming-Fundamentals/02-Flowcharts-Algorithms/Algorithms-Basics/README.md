# Algorithms Basics — Python

Welcome to **Algorithms Basics**, a part of the *Week 1: Programming Fundamentals* learning path in the DSA-Python repository.

This section introduces algorithms, step-by-step problem-solving, common algorithm examples, algorithm characteristics, and basic time and space complexity analysis. Each topic uses Python programs to help connect theoretical concepts with practical implementation.

---

## Table of Contents

1. [About This Section](#about-this-section)
2. [Learning Objectives](#learning-objectives)
3. [Folder Structure](#folder-structure)
4. [Topics Covered](#topics-covered)
5. [What Is an Algorithm?](#what-is-an-algorithm)
6. [Characteristics of a Good Algorithm](#characteristics-of-a-good-algorithm)
7. [Algorithm Development Process](#algorithm-development-process)
8. [Example: Find the Sum of Two Numbers](#example-find-the-sum-of-two-numbers)
9. [Algorithm Analysis](#algorithm-analysis)
10. [Time Complexity Reference](#time-complexity-reference)
11. [How to Run the Programs](#how-to-run-the-programs)
12. [Practice Structure](#practice-structure)
13. [Common Mistakes](#common-mistakes)
14. [Interview Questions](#interview-questions)
15. [Learning Checklist](#learning-checklist)

---

## About This Section

An algorithm is a finite sequence of clear instructions used to solve a problem or complete a task.

Before writing code, it is useful to understand:

- What problem needs to be solved.
- What input is required.
- What processing or calculations are needed.
- What output is expected.
- Which conditions or repetitions may be required.
- Whether the solution is correct and efficient.

Algorithms are fundamental to programming, Data Structures and Algorithms (DSA), competitive programming, and software development.

In this section, you will learn to express a solution as logical steps first and then implement it in Python.

## Learning Objectives

After completing this section, you should be able to:

- Explain the meaning and purpose of an algorithm.
- Write an algorithm using clear, ordered steps.
- Identify inputs, processing, and outputs.
- Solve basic mathematical and logical problems.
- Convert problem statements into Python programs.
- Use conditions and loops to implement algorithms.
- Understand correctness, finiteness, definiteness, and effectiveness.
- Recognize common time-complexity patterns.
- Understand basic time and auxiliary-space complexity.
- Test programs with normal, boundary, and invalid inputs.
- Practice explaining your approach before writing code.

---

## Folder Structure

```text
Algorithms-Basics/
│
├── README.md
│
├── 01_Algorithm_Basics/
│   ├── README.md
│   └── 01_algorithm_basics.py
│
├── 02_Algorithm_Steps/
│   ├── README.md
│   └── 02_algorithm_steps.py
│
├── 03_Algorithm_Examples/
│   ├── README.md
│   └── 03_algorithm_examples.py
│
├── 04_Algorithm_Characteristics/
│   ├── README.md
│   └── 04_algorithm_characteristics.py
│
├── 05_Algorithm_Analysis/
│   ├── README.md
│   └── 05_algorithm_analysis.py
│
└── 06_Practice_Algorithms/
    ├── README.md
    └── 06_practice_algorithms.py
```

*Note: Folder and filename capitalization should match the names actually used in your local repository.*

---

## Topics Covered

### 1. Algorithm Basics

**Folder:** `01_Algorithm_Basics/`

Learn what algorithms are and how they help solve programming problems.

Key concepts:

- Definition and purpose of an algorithm.
- Input, processing, and output.
- Arithmetic and comparison operations.
- Basic calculations and number classification.
- Translating a problem into logical steps.
- Testing a solution with sample inputs.

### 2. Algorithm Steps

**Folder:** `02_Algorithm_Steps/`

Learn how to break down a problem into an ordered sequence of steps.

Key concepts:

- Understanding the problem statement.
- Identifying inputs and expected outputs.
- Designing step-by-step logic.
- Writing formulas and conditions.
- Converting a solution into Python code.
- Tracing instructions manually.

### 3. Algorithm Examples

**Folder:** `03_Algorithm_Examples/`

Study common beginner-level algorithms and their implementations.

Key concepts include:

- Finding the largest of two or three numbers.
- Checking even and odd numbers.
- Working with positive, negative, and zero values.
- Calculating sums and factorials.
- Generating multiplication tables.
- Counting, summing, and reversing digits.
- Checking prime numbers and palindromes.
- Introduction to searching and other common problems.

### 4. Algorithm Characteristics

**Folder:** `04_Algorithm_Characteristics/`

Understand the properties that help determine whether an algorithm is well-designed.

Key concepts:

- **Input:** An algorithm can accept zero or more inputs.
- **Output:** It produces one or more results.
- **Definiteness:** Each instruction should be clear and unambiguous.
- **Finiteness:** The algorithm should terminate after a finite number of steps.
- **Effectiveness:** Each operation should be sufficiently basic and executable.
- **Correctness:** The algorithm should produce the expected result for valid inputs.
- **Generality:** The solution should work for the intended range of problem inputs.
- **Efficiency:** Time and memory requirements should be considered.

### 5. Algorithm Analysis

**Folder:** `05_Algorithm_Analysis/`

Learn how to reason about the efficiency of algorithms.

Key concepts:

- Time complexity.
- Auxiliary space complexity.
- Big O notation.
- Best-case, average-case, and worst-case analysis.
- Constant-time and linear-time operations.
- Nested loops and quadratic-time patterns.
- Binary search and logarithmic-time patterns.
- Comparing alternative solutions.

Complexity depends on the algorithm and how its operations scale with input size. A complexity label should be based on the actual code being analyzed.

### 6. Practice Algorithms

**Folder:** `06_Practice_Algorithms/`

Apply what you have learned through a focused collection of coding problems.

Key concepts and practice areas include:

- Basic mathematical calculations.
- Number properties and digit manipulation.
- Searching and sorting.
- Finding minimum, maximum, and second-largest values.
- Duplicate removal and frequency counting.
- GCD, LCM, and missing-number problems.
- Practicing clean logic and testing edge cases.

---

## What Is an Algorithm?

An algorithm is a sequence of finite, well-defined steps that transforms input into an expected result.

A general algorithm can be represented as:

```text
START
  |
  v
Read Input
  |
  v
Process Input
  |
  v
Produce Output
  |
  v
END
```

This is a simplified pattern. More advanced algorithms may include decisions, loops, multiple inputs, and several possible outcomes.

### Algorithm vs. Program

| Algorithm | Program |
|---|---|
| Describes the solution logic. | Implements the solution in a programming language. |
| Can be written in plain language or pseudocode. | Uses the syntax of a programming language. |
| Focuses on the steps required to solve a problem. | Must follow the language's syntax and runtime rules. |
| Can be implemented in different languages. | Is written for a specific language or environment. |

---

## Characteristics of a Good Algorithm

| Characteristic | Meaning | Simple example |
|---|---|---|
| Input | Defines the required input values. | Read `a` and `b`. |
| Output | Defines the expected result. | Display their sum. |
| Definiteness | Every step is clear. | Use `sum = a + b`. |
| Finiteness | Execution eventually ends. | Perform one addition and print the result. |
| Effectiveness | Steps are practical to execute. | Read, add, and display. |
| Correctness | The result matches the intended solution. | `4 + 5` produces `9`. |
| Generality | Works for all intended valid inputs. | Addition works with different valid numbers. |
| Efficiency | Avoids unnecessary time and memory usage. | Use a direct formula when appropriate. |

---

## Algorithm Development Process

Use this workflow when solving a new coding problem.

### Step 1: Understand the problem

Read the problem carefully and identify exactly what needs to be calculated or determined.

### Step 2: Identify inputs

Write down all values the program requires.

### Step 3: Identify outputs

Determine the information that must be displayed or returned.

### Step 4: Design the logic

Choose the required formulas, conditions, loops, or data structures.

### Step 5: Write the algorithm

Describe the solution in clear, ordered steps or pseudocode.

### Step 6: Dry-run the algorithm

Manually trace the steps using a small sample input.

### Step 7: Implement in Python

Convert the logical steps into executable Python code.

### Step 8: Test the result

Check normal values, boundary cases, and invalid inputs where applicable.

### Step 9: Analyze efficiency

Consider how the running time and additional memory usage grow as input size increases.

---

## Example: Find the Sum of Two Numbers

**Problem:** Read two numbers and display their sum.

### Algorithm

1. Start.
2. Read the first number, `a`.
3. Read the second number, `b`.
4. Calculate `total = a + b`.
5. Display `total`.
6. End.

### Pseudocode

```text
START
INPUT a
INPUT b
total ← a + b
OUTPUT total
END
```

### Python implementation

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Dry run

Suppose `a = 4` and `b = 5`.

| Step | Operation | Result |
|---|---|---|
| 1 | Read `a` | `4` |
| 2 | Read `b` | `5` |
| 3 | Calculate `a + b` | `9` |
| 4 | Display the result | `Sum: 9` |

**Expected output**

```text
Enter the first number: 4
Enter the second number: 5
Sum: 9
```

### Complexity

- **Time:** \(O(1)\), because a fixed number of arithmetic operations is performed.
- **Auxiliary space:** \(O(1)\), because the solution stores a fixed number of variables.

This analysis treats the input values as already representable by the program's numeric type.

---

## Algorithm Analysis

Algorithm analysis helps compare approaches based on the resources they use.

### 1. Time Complexity

Time complexity describes how the number of operations grows as the input size increases. It does not normally mean the exact number of seconds a program takes.

### 2. Auxiliary Space Complexity

Auxiliary space describes the additional working memory required by an algorithm, excluding the input storage under the usual convention.

### 3. Big O Notation

Big O expresses an asymptotic upper bound on growth and is commonly used to describe worst-case time complexity.

Other notations include:

- **Big Omega \(\Omega\):** Asymptotic lower bound.
- **Big Theta \(\Theta\):** Asymptotically tight bound when the upper and lower bounds match.

### Common Patterns

| Code pattern | Typical time complexity |
|---|---:|
| A fixed number of basic operations | \(O(1)\) |
| One loop over `N` items | \(O(N)\) |
| Two nested loops over `N` items each | \(O(N^2)\) |
| Repeatedly halving the search range | \(O(\log N)\) |
| Sorting algorithms | Depends on the algorithm |

These are common patterns, not automatic guarantees. Always inspect what the code actually does inside each operation or loop.

---

## Time Complexity Reference

| Complexity | Name | Example pattern |
|---|---|---|
| \(O(1)\) | Constant | Accessing an item by index in a Python list |
| \(O(\log N)\) | Logarithmic | Binary search on sorted data |
| \(O(N)\) | Linear | Traversing a list once |
| \(O(N \log N)\) | Linearithmic | Typical efficient comparison sorting |
| \(O(N^2)\) | Quadratic | Comparing every pair using two nested loops |
| \(O(2^N)\) | Exponential | Some brute-force recursive solutions |

The actual complexity of an algorithm depends on its implementation, input assumptions, and the operations being measured.

---

## How to Run the Programs

Open a terminal at the root of the `DSA-Python` repository.

For example, to run the Algorithm Basics program:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\01_Algorithm_Basics\01_algorithm_basics.py"
```

To run the other topic programs, use the corresponding folder and Python filename.

If `python` is not recognized in your terminal, check whether Python is installed and available on your PATH. On some Windows installations, the `py` command may work instead.

### Suggested learning order

1. `01_Algorithm_Basics`
2. `02_Algorithm_Steps`
3. `03_Algorithm_Examples`
4. `04_Algorithm_Characteristics`
5. `05_Algorithm_Analysis`
6. `06_Practice_Algorithms`

Read the relevant topic README before running its Python file. Try to predict the output before executing each example.

---

## Practice Structure

Each topic is designed to provide three kinds of practice:

- **12 examples:** Demonstrations of core concepts.
- **12 solved practice questions:** Questions with solution implementations to study.
- **5 unsolved practice questions:** Questions to attempt independently.

Use the solved problems to understand the logic, but try the unsolved questions before looking for help.

### Recommended approach for each question

1. Restate the problem in your own words.
2. Identify the inputs and expected output.
3. Write down the logical steps.
4. Work through a small example manually.
5. Implement the solution in Python.
6. Test boundary cases.
7. Explain the time and auxiliary-space complexity where applicable.

---

## Common Mistakes

- Starting to code before understanding the problem.
- Ignoring whether input values can be negative or zero.
- Forgetting boundary cases.
- Using a formula without checking its assumptions.
- Confusing an algorithm's steps with the programming-language syntax.
- Assuming every loop has the same time complexity.
- Forgetting to validate input when validation is required.
- Copying a solution without understanding its logic.
- Declaring a solution correct after testing only one example.
- Confusing actual runtime with asymptotic time complexity.

---

## Interview Questions

**1. What is an algorithm?**

An algorithm is a finite sequence of well-defined steps used to solve a problem.

**2. Why are algorithms important?**

They help organize problem-solving logic and provide a basis for implementing, testing, and comparing solutions.

**3. What are the key characteristics of an algorithm?**

Common characteristics include input, output, definiteness, finiteness, effectiveness, correctness, generality, and efficiency.

**4. What is the difference between an algorithm and a program?**

An algorithm describes the solution logic, while a program implements that logic in a programming language.

**5. What is a dry run?**

A dry run is a manual trace of an algorithm using specific input values to understand how each step executes.

**6. What is time complexity?**

Time complexity describes how the number of operations grows with input size.

**7. What is auxiliary space complexity?**

It measures the additional working memory used by an algorithm, separate from the input storage under the usual convention.

**8. What does \(O(1)\) mean?**

It represents constant asymptotic growth: the operation count does not increase with input size under the stated analysis.

**9. What does \(O(N)\) mean?**

It represents linear growth with input size.

**10. What is the purpose of algorithm analysis?**

It helps evaluate and compare solutions in terms of their time and memory requirements.

---

## Learning Checklist

- [ ] I understand what an algorithm is.
- [ ] I can identify inputs, processing, and outputs.
- [ ] I can write simple algorithms as ordered steps.
- [ ] I can perform a manual dry run.
- [ ] I can implement basic algorithms in Python.
- [ ] I understand the main characteristics of a good algorithm.
- [ ] I can recognize common time-complexity patterns.
- [ ] I understand the difference between time complexity and auxiliary space.
- [ ] I have attempted the solved practice questions.
- [ ] I have independently tried the unsolved questions.
- [ ] I have reviewed all six topic folders.

---

## Next Step

After completing **Algorithms Basics**, continue to the **Flowcharts** section to learn how to represent algorithm logic visually using standard symbols and flow lines.

Keep practicing, understand the logic behind every program, and build a strong foundation before moving to more advanced DSA topics.
