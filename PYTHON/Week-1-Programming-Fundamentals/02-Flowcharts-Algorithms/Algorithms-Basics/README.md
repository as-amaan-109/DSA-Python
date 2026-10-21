# Algorithms Basics

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Level:** Beginner  
> **Language:** Python  
> **Purpose:** Understand algorithms, learn problem-solving techniques, and practise implementing basic algorithms using Python.

---

## 1. Introduction

An algorithm is a finite sequence of clear and ordered steps used to solve a problem or complete a task.

Algorithms are an important part of programming because they help us understand a problem, design a solution, and implement that solution using a programming language.

Before writing Python code, we should understand:

- What problem needs to be solved?
- What input is required?
- What operations must be performed?
- What output is expected?
- Is the solution correct and efficient?

This section introduces the fundamentals of algorithms through theory, Python examples, dry runs, complexity analysis, and practice problems.

## 2. Learning Objectives

After completing all six topics, you should be able to:

- Understand the meaning and purpose of an algorithm.
- Write algorithms using clear, ordered steps.
- Convert algorithms into Python programs.
- Solve basic mathematical and programming problems.
- Understand the characteristics of a good algorithm.
- Perform a dry run using sample inputs.
- Understand the basics of time and space complexity.
- Implement searching and other basic algorithms.
- Test solutions and handle common edge cases.
- Build a foundation for Data Structures and Algorithms (DSA).

---

## 3. Topics Covered

### 01. Algorithm Basics

**Folder:** `01_Algorithm_Basics/`

This topic introduces the fundamental concepts of algorithms.

**What you will learn:**

- Definition and purpose of an algorithm.
- Importance of algorithms in programming.
- Basic structure of an algorithm.
- Input, processing, and output.
- Difference between an algorithm and a program.
- Difference between an algorithm and a flowchart.
- Introduction to pseudocode.
- Writing simple algorithms for mathematical problems.

**Practical examples:**

- Display a message.
- Add two numbers.
- Calculate an average.
- Find the area of a rectangle.

**Learning outcome:** Understand what an algorithm is and how to describe a solution using ordered steps.

### 02. Algorithm Steps

**Folder:** `02_Algorithm_Steps/`

This topic focuses on writing algorithm instructions in the correct order.

**What you will learn:**

- How to understand a problem.
- How to identify input and expected output.
- How to decide the processing logic.
- How to write numbered algorithm steps.
- How to create pseudocode.
- How to perform a dry run.
- How to verify calculations before coding.
- How to convert steps into Python code.

**Practical examples:**

- Addition and average calculations.
- Area of a rectangle.
- Celsius-to-Fahrenheit conversion.
- Dry-run tables for simple algorithms.

**Learning outcome:** Develop a structured approach to solving programming problems before writing code.

### 03. Algorithm Examples

**Folder:** `03_Algorithm_Examples/`

This topic applies algorithm concepts to practical programming problems.

**What you will learn:**

- Writing algorithms for arithmetic operations.
- Applying mathematical formulas.
- Swapping two values using a temporary variable.
- Comparing two numbers.
- Checking whether a number is even or odd.
- Calculating the square of a number.
- Converting algorithm steps into Python programs.

**Practical examples:**

- Addition, subtraction, and multiplication.
- Average of three numbers.
- Area and perimeter of a rectangle.
- Celsius-to-Fahrenheit conversion.
- Swapping two numbers.
- Finding the larger of two numbers.
- Even-or-odd checking.

**Learning outcome:** Apply algorithm design to common mathematical and beginner programming problems.

### 04. Algorithm Characteristics

**Folder:** `04_Algorithm_Characteristics/`

This topic explains the properties used to describe and evaluate algorithms.

**What you will learn:**

- Input.
- Output.
- Definiteness.
- Finiteness.
- Effectiveness.
- Correctness.
- Generality.
- Efficiency.

You will also learn how to identify unclear instructions, non-terminating loops, incorrect calculations, and inefficient approaches.

**Practical activities:**

- Evaluate an addition algorithm.
- Check results against expected outputs.
- Understand why an algorithm must terminate.
- Compare clear and ambiguous instructions.
- Test algorithms using different inputs.

**Learning outcome:** Understand what makes an algorithm clear, executable, correct, and suitable for its intended problem.

### 05. Algorithm Analysis

**Folder:** `05_Algorithm_Analysis/`

This topic introduces the analysis of algorithm performance.

**What you will learn:**

- Meaning of algorithm analysis.
- Input size, represented by `n`.
- Time complexity.
- Space complexity.
- Auxiliary space.
- Big O notation.
- Constant time: `O(1)`.
- Logarithmic time: `O(log n)`.
- Linear time: `O(n)`.
- Linearithmic time: `O(n log n)`.
- Quadratic time: `O(n²)`.
- Exponential time: `O(2ⁿ)`.
- Factorial time: `O(n!)`.
- Best-case, average-case, and worst-case analysis.
- Linear search and binary search complexity.

**Learning outcome:** Understand how an algorithm's computational work and memory requirements grow as the input becomes larger.

### 06. Practice Algorithms

**Folder:** `06_Practice_Algorithms/`

This topic combines the concepts learned in the previous five topics through practical Python implementations.

**What you will practise:**

- Basic arithmetic algorithms.
- Average calculation.
- Area calculation.
- Temperature conversion.
- Even-or-odd checking.
- Finding the largest element.
- Linear search.
- Binary search.
- Reversing a list.
- Counting element frequencies.
- Calculating factorial.
- Testing solutions with edge cases.
- Analysing time and auxiliary space complexity.

**Learning outcome:** Apply algorithm design, implementation, testing, and complexity analysis to practical problems.

---

## 4. Recommended Learning Order

Study the six topics in the following order:

1. **Algorithm Basics** — Understand the fundamental concepts.
2. **Algorithm Steps** — Learn to arrange instructions logically.
3. **Algorithm Examples** — Apply those steps to practical problems.
4. **Algorithm Characteristics** — Understand the properties of good algorithms.
5. **Algorithm Analysis** — Learn to evaluate computational efficiency.
6. **Practice Algorithms** — Implement solutions and test your understanding.

Each topic builds on the previous one. Complete the theory and examples before moving on to the next folder.

---

## 5. Repository Structure

```text
Algorithms-Basics/
│
├── README.md
│
├── 01_Algorithm_Basics/
│   ├── 01_algorithm_basics.py
│   └── README.md
│
├── 02_Algorithm_Steps/
│   ├── 02_algorithm_steps.py
│   └── README.md
│
├── 03_Algorithm_Examples/
│   ├── 03_algorithm_examples.py
│   └── README.md
│
├── 04_Algorithm_Characteristics/
│   ├── 04_algorithm_characteristics.py
│   └── README.md
│
├── 05_Algorithm_Analysis/
│   ├── 05_algorithm_analysis.py
│   └── README.md
│
└── 06_Practice_Algorithms/
    ├── 06_practice_algorithms.py
    └── README.md
```

### Purpose of the Files

**Python files (`.py`):** Contain practical examples, implementations, and code for experimenting with algorithms.

**README files (`.md`):** Contain detailed theory, algorithm steps, explanations, outputs, dry runs, complexity analysis, interview questions, and practice exercises.

The parent `README.md` provides an overview of the complete Algorithms-Basics section. Each subfolder's README provides detailed notes for that individual topic.

---

## 6. How to Study Each Topic

Follow this approach while learning:

1. Read the topic's `README.md`.
2. Understand each concept and algorithm step.
3. Open the corresponding `.py` file.
4. Run the examples and observe their outputs.
5. Perform a dry run using sample values.
6. Solve the practice questions independently.
7. Test edge cases.
8. Identify the time and auxiliary space complexity where applicable.

Do not memorize code without understanding the logic. Try to explain why every step is required and what result it produces.

---

## 7. Prerequisites

Before starting this section, it is helpful to understand these introductory Python concepts:

- The `print()` function.
- Basic arithmetic operations.
- Variables and data types.
- Taking input using `input()`.
- Type conversion using `int()` and `float()`.
- Conditional statements.
- Loops.
- Basic lists and functions.

Some concepts will be introduced through examples, but a basic understanding of Python will make the algorithms easier to follow.

---

## 8. Overall Learning Outcome

After completing this section, you should have a foundation in algorithm design and analysis.

You should be able to move from a problem statement to an ordered algorithm, implement the solution in Python, verify its output, and estimate its computational complexity.

This knowledge prepares you for more advanced DSA topics, including arrays, strings, searching, sorting, recursion, linked lists, stacks, queues, trees, and graphs.

---

## 9. Completion Checklist

- [ ] 01 — Algorithm Basics
- [ ] 02 — Algorithm Steps
- [ ] 03 — Algorithm Examples
- [ ] 04 — Algorithm Characteristics
- [ ] 05 — Algorithm Analysis
- [ ] 06 — Practice Algorithms

---

## Conclusion

The Algorithms-Basics section establishes the foundation for systematic problem-solving.

The main goal is to learn how to understand a problem, design a clear solution, implement it in Python, test its correctness, and evaluate its efficiency.

**Understand the Problem → Design the Algorithm → Implement in Python → Test the Solution → Analyze Complexity**

Complete these six topics carefully before moving to more advanced algorithm and flowchart concepts.
