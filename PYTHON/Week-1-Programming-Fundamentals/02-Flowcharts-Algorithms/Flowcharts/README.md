# Flowcharts

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Level:** Beginner  
> **Language:** Python  
> **Purpose:** Learn to represent algorithms visually using standard flowchart symbols and implement their logic in Python.

---

## 1. Introduction

A flowchart is a graphical representation of an algorithm or process. It uses standard symbols connected by arrows to show the sequence of operations, decisions, and repeated steps.

Flowcharts help us understand a problem visually before writing the actual program.

In this section, we will learn how to draw basic flowcharts, represent input and output operations, use decisions, represent loops, and solve practical problems by combining these concepts.

## 2. Learning Objectives

After completing all five topics, you should be able to:

- Understand the purpose of flowcharts.
- Identify standard flowchart symbols.
- Represent input, processing, and output operations.
- Draw decision-based flowcharts.
- Represent repeated operations using loops.
- Convert flowcharts into Python programs.
- Trace the execution of a flowchart using sample inputs.
- Identify logical mistakes and missing paths.
- Solve basic programming problems using flowcharts.
- Build a foundation for algorithm design and DSA.

---

## 3. Topics Covered

### 01. Flowchart Basics

**Folder:** `01_FlowChart_Basics/`

This topic introduces flowcharts and their standard symbols.

**What you will learn:**

- Definition and purpose of a flowchart.
- Advantages and limitations of flowcharts.
- Terminator symbol for Start and Stop.
- Process symbol for calculations.
- Input/Output symbol.
- Decision symbol.
- Flow lines and arrows.
- Connector symbols.
- Basic rules for drawing flowcharts.
- Difference between an algorithm, flowchart, and program.

**Practical examples:**

- Display a message.
- Add two numbers.
- Calculate the area of a rectangle.

**Learning outcome:** Understand the basic symbols and learn to represent simple algorithms visually.

### 02. Input/Output Flowcharts

**Folder:** `02_Input_Output_FlowChart/`

This topic focuses on representing data input, processing, and output operations.

**What you will learn:**

- Meaning of input and output.
- Input/Output flowchart symbol.
- Reading values from a user.
- Displaying results.
- Representing calculations in flowcharts.
- Python `input()` and `print()` functions.
- Type conversion using `int()` and `float()`.
- Reading multiple values.
- Dry runs for input/output problems.

**Practical examples:**

- Read a name and display a welcome message.
- Add two numbers.
- Calculate an average.
- Calculate the area of a rectangle.
- Convert Celsius to Fahrenheit.

**Learning outcome:** Represent input, processing, and output operations in a flowchart and implement them using Python.

### 03. Decision Flowcharts

**Folder:** `03_Decision_FlowChart/`

This topic explains how flowcharts represent conditions and alternative execution paths.

**What you will learn:**

- Decision symbol and branching.
- `if` statements.
- `if-else` statements.
- `if-elif-else` statements.
- Comparison operators.
- Logical operators: `and`, `or`, and `not`.
- Nested decisions.
- Testing different decision branches.
- Handling boundary and edge cases.

**Practical examples:**

- Positive, negative, or zero.
- Even or odd.
- Find the larger of two numbers.
- Find the largest of three numbers.
- Pass or fail.
- Voting-age check.
- Leap-year check.

**Learning outcome:** Draw flowcharts that represent conditional logic and implement the same logic using Python decision statements.

### 04. Loop Flowcharts

**Folder:** `04_Loop_FlowChart/`

This topic explains how flowcharts represent repeated execution.

**What you will learn:**

- Definition and purpose of loops.
- Loop conditions.
- Initialization, loop body, and updates.
- `for` loops.
- `while` loops.
- Loop-back arrows.
- Counter-controlled loops.
- Accumulators.
- Nested loops.
- `break` and `continue`.
- Infinite loops and off-by-one errors.
- Dry runs of loops.

**Practical examples:**

- Print numbers from 1 to 5.
- Calculate the sum from 1 to N.
- Display a multiplication table.
- Calculate factorial.
- Count the digits of an integer.
- Count even numbers in a list.
- Print a pattern using nested loops.

**Learning outcome:** Represent repeated operations visually and understand how loop conditions control execution.

### 05. Practice Flowcharts

**Folder:** `05_Practice_FlowChart/`

This is the final topic in the Flowcharts section. It combines the concepts learned in the previous four folders.

**What you will practise:**

- Input and output operations.
- Conditional decisions.
- Loop-based calculations.
- Combining decisions and loops.
- Writing algorithms before coding.
- Drawing flowcharts for complete problems.
- Implementing flowcharts in Python.
- Performing dry runs.
- Testing edge cases.
- Understanding basic time and auxiliary space complexity.

**Practical examples:**

- Welcome message.
- Addition of two numbers.
- Positive, negative, or zero.
- Largest of three numbers.
- Sum from 1 to N.
- Multiplication table.
- Factorial.
- Count digits.
- Linear search.
- Count even and odd numbers.
- Divisibility checks.
- Nested-loop patterns.

**Learning outcome:** Apply flowchart concepts to complete programming problems and verify the solutions using Python.

---

## 4. Recommended Learning Order

Complete the five topics in this sequence:

1. **Flowchart Basics** — Learn the standard symbols and drawing rules.
2. **Input/Output Flowcharts** — Represent data input, calculations, and output.
3. **Decision Flowcharts** — Represent conditions and branching.
4. **Loop Flowcharts** — Represent repetition and loop termination.
5. **Practice Flowcharts** — Combine all the concepts to solve problems.

Each topic builds on the previous one. Complete the examples and practice questions before moving to the next folder.

---

## 5. Standard Flowchart Symbols

The following table provides a quick reference for the symbols used throughout this section.

| Symbol | Common Shape | Purpose |
|---|---|---|
| Terminator | Oval or rounded rectangle | Start or Stop |
| Process | Rectangle | Calculation or operation |
| Input/Output | Parallelogram | Read input or display output |
| Decision | Diamond | Check a condition |
| Flow line | Arrow | Show execution direction |
| Connector | Circle or other standard connector shape | Connect separate parts of a flowchart |

Use the appropriate symbols and connect them in a logical order. Label decision branches clearly wherever applicable.

---

## 6. Repository Structure

```text
Flowcharts/
│
├── README.md
│
├── 01_FlowChart_Basics/
│   ├── 01_flowchart_basics.py
│   └── README.md
│
├── 02_Input_Output_FlowChart/
│   ├── 02_input_output_flowchart.py
│   └── README.md
│
├── 03_Decision_FlowChart/
│   ├── 03_decision_flowchart.py
│   └── README.md
│
├── 04_Loop_FlowChart/
│   ├── 04_loop_flowchart.py
│   └── README.md
│
└── 05_Practice_FlowChart/
    ├── 05_practice_flowcharts.py
    └── README.md
```

### Purpose of the Files

**Python files (`.py`)**

Contain practical examples and Python implementations that demonstrate the logic of each flowchart topic.

**README files (`.md`)**

Contain detailed theory, flowchart diagrams, explanations, algorithm steps, code examples, outputs, dry runs, interview questions, and practice problems.

The parent `README.md` provides an overview of the whole Flowcharts section. Each subfolder's `README.md` contains the detailed notes for that topic.

---

## 7. How to Study Each Topic

Follow this learning process for each folder:

1. Read the topic's `README.md`.
2. Understand the flowchart symbols and their purposes.
3. Study the algorithm steps.
4. Trace the flowchart using sample values.
5. Open the corresponding `.py` file.
6. Run the Python examples.
7. Compare the program's output with the expected result.
8. Solve the practice questions independently.
9. Test boundary cases and identify logical mistakes.

Do not memorize diagrams without understanding the execution path. Try to explain why each symbol is used and where each arrow leads.

---

## 8. Prerequisites

Before starting this section, it is helpful to understand basic Python concepts:

- The `print()` function.
- The `input()` function.
- Variables and data types.
- Arithmetic operators.
- Comparison operators.
- Type conversion.
- Conditional statements.
- `for` and `while` loops.
- Basic lists and functions.

These concepts will help you translate flowcharts into working Python programs.

---

## 9. Overall Learning Outcome

After completing all five topics, you should understand how to design and interpret flowcharts for basic programming problems.

You should be able to represent a solution using the appropriate symbols, follow its execution path, implement the same logic in Python, and test the results.

This knowledge supports further study of algorithms, problem-solving, Data Structures and Algorithms (DSA), and programming interview questions.

---

## 10. Completion Checklist

- [ ] 01 — Flowchart Basics
- [ ] 02 — Input/Output Flowcharts
- [ ] 03 — Decision Flowcharts
- [ ] 04 — Loop Flowcharts
- [ ] 05 — Practice Flowcharts

---

## Conclusion

Flowcharts provide a visual way to plan, explain, and test the logic of a program.

Start with the basic symbols, learn input and output operations, understand decisions and loops, and then combine these concepts in practical problems.

**Understand the Problem → Write the Algorithm → Draw the Flowchart → Implement in Python → Test the Solution**

Complete these five topics to build a strong foundation in flowchart design and introductory programming.
