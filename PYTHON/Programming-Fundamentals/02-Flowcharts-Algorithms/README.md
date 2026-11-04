# Algorithms and Flowcharts — Python

Welcome to **Algorithms and Flowcharts**, the second section of Week 1: Programming Fundamentals in the DSA-Python repository.

This section builds the foundation of algorithmic thinking. Before writing more complex Python programs, you will learn to design step-by-step solutions, represent them visually using flowcharts, analyse their logic, and implement them in Python.

The section is divided into two main parts:

1. **Algorithms Basics** — understand algorithms, logical steps, common examples, characteristics, and complexity analysis.
2. **Flowcharts** — represent algorithm logic visually using standard symbols, decisions, and loops.

Both parts help prepare you for pseudocode, problem-solving, and Data Structures and Algorithms (DSA).

---

## Table of Contents

1. [About This Section](#about-this-section)
2. [Learning Objectives](#learning-objectives)
3. [Why Algorithms and Flowcharts Matter](#why-algorithms-and-flowcharts-matter)
4. [Section Structure](#section-structure)
5. [Part 1: Algorithms Basics](#part-1-algorithms-basics)
6. [Part 2: Flowcharts](#part-2-flowcharts)
7. [Algorithm vs. Flowchart vs. Program](#algorithm-vs-flowchart-vs-program)
8. [Problem-Solving Workflow](#problem-solving-workflow)
9. [Worked Example: Find the Largest Number](#worked-example-find-the-largest-number)
10. [Running the Python Programs](#running-the-python-programs)
11. [Practice Guidelines](#practice-guidelines)
12. [Common Mistakes](#common-mistakes)
13. [Interview Questions](#interview-questions)
14. [Completion Checklist](#completion-checklist)
15. [Next Section](#next-section)

---

## About This Section

An **algorithm** is a finite sequence of well-defined steps used to solve a problem or perform a task.

A **flowchart** is a graphical representation of the steps and control flow of an algorithm.

Together, they help you plan a solution before writing code.

For example, a program that adds two numbers can be planned as:

**Input → Process → Output**

A program that checks whether a number is even or odd requires a decision. A program that calculates a factorial requires repetition.

By studying these patterns separately and then combining them, you can develop a systematic approach to programming problems.

## Learning Objectives

After completing this section, you should be able to:

- Explain what an algorithm is and why it is useful.
- Break a problem into clear, ordered instructions.
- Identify inputs, processing operations, and expected outputs.
- Understand the important characteristics of a good algorithm.
- Identify common flowchart symbols.
- Represent sequence, selection, and iteration.
- Translate algorithms into flowcharts and Python code.
- Perform dry runs using sample inputs.
- Test normal, boundary, and invalid cases.
- Recognize common time-complexity patterns.
- Understand basic auxiliary-space analysis.
- Explain your problem-solving approach clearly.
- Build a foundation for pseudocode and DSA practice.

---

## Why Algorithms and Flowcharts Matter

### 1. Structured problem-solving

Algorithms help you organize the solution into understandable steps rather than writing code randomly.

### 2. Clear program logic

Flowcharts make the order of operations, decisions, and repetition visible.

### 3. Easier testing

A step-by-step algorithm can be checked manually before implementation.

### 4. Better debugging

A missing calculation, incorrect condition, or infinite loop can often be identified by tracing the logic.

### 5. Language-independent thinking

The same algorithm can usually be implemented in different programming languages.

### 6. DSA preparation

Searching, sorting, recursion, data structures, and advanced algorithms all benefit from strong logical reasoning.

---

## Section Structure

```text
02-Flowcharts-Algorithms/
│
├── README.md
│
├── Algorithms-Basics/
│   ├── README.md
│   │
│   ├── 01_Algorithm_Basics/
│   │   ├── README.md
│   │   └── 01_algorithm_basics.py
│   │
│   ├── 02_Algorithm_Steps/
│   │   ├── README.md
│   │   └── 02_algorithm_steps.py
│   │
│   ├── 03_Algorithm_Examples/
│   │   ├── README.md
│   │   └── 03_algorithm_examples.py
│   │
│   ├── 04_Algorithm_Characteristics/
│   │   ├── README.md
│   │   └── 04_algorithm_characteristics.py
│   │
│   ├── 05_Algorithm_Analysis/
│   │   ├── README.md
│   │   └── 05_algorithm_analysis.py
│   │
│   └── 06_Practice_Algorithms/
│       ├── README.md
│       └── 06_practice_algorithms.py
│
└── Flowcharts/
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

*Note: This is the intended structure. Keep your folder names and capitalization consistent with your actual repository.*

---

## Part 1: Algorithms Basics

**Folder:** [`Algorithms-Basics/`](Algorithms-Basics/README.md)

This part teaches you to understand and design algorithms before focusing on their visual representation.

### Topics covered

| No. | Topic | Main focus |
|---|---|---|
| 1 | Algorithm Basics | Definition, purpose, inputs, outputs, and basic logic |
| 2 | Algorithm Steps | Breaking a problem into ordered instructions |
| 3 | Algorithm Examples | Arithmetic, number problems, searching, and other beginner algorithms |
| 4 | Algorithm Characteristics | Finiteness, definiteness, correctness, effectiveness, and efficiency |
| 5 | Algorithm Analysis | Time complexity, auxiliary space, and growth patterns |
| 6 | Practice Algorithms | Applying the concepts to coding problems |

### What you will learn

- How to identify the problem and expected result.
- How to design a solution before writing code.
- How to translate mathematical formulas into instructions.
- How to use conditions and loops.
- How to recognize common algorithm characteristics.
- How to estimate the efficiency of simple solutions.
- How to test and explain your programs.

Start with `Algorithms-Basics/README.md`, then complete its six topic folders in order.

---

## Part 2: Flowcharts

**Folder:** [`Flowcharts/`](Flowcharts/README.md)

This part teaches you to represent algorithm logic visually.

### Topics covered

| No. | Topic | Main focus |
|---|---|---|
| 1 | Flowchart Basics | Symbols, connectors, and the direction of execution |
| 2 | Input/Output Flowcharts | Reading values, calculations, and displaying results |
| 3 | Decision Flowcharts | Conditions, branches, and alternative outcomes |
| 4 | Loop Flowcharts | Repetition, loop conditions, updates, and exit paths |
| 5 | Practice Flowcharts | Combining sequences, decisions, and loops |

### What you will learn

- How to select an appropriate symbol for an operation.
- How to represent input, processing, and output.
- How to represent a decision using labelled branches.
- How to represent loop conditions and termination.
- How to check a flowchart using a dry run.
- How to convert the diagram into Python code.

Start with `Flowcharts/README.md`, then complete all five topic folders in order.

---

## Algorithm vs. Flowchart vs. Program

| Concept | Meaning | Typical representation |
|---|---|---|
| Algorithm | Describes the logical steps used to solve a problem | Ordered instructions |
| Flowchart | Represents those steps visually | Symbols, arrows, and branches |
| Pseudocode | Expresses the solution in structured, language-independent text | `INPUT`, `IF`, `WHILE`, `OUTPUT` |
| Program | Implements the logic in a programming language | Python statements and functions |

These representations support different stages of problem-solving. You can use an algorithm to plan the solution, a flowchart to visualize it, pseudocode to refine the steps, and Python to implement and test it.

---

## Problem-Solving Workflow

Use this workflow throughout the section.

### Step 1: Understand the problem

Read the statement and identify what needs to be calculated or decided.

### Step 2: Identify input and output

List the data required and the result expected.

### Step 3: Develop the algorithm

Break the solution into small, clear steps.

### Step 4: Identify control flow

Decide whether the problem requires a simple sequence, branching conditions, repetition, or a combination.

### Step 5: Draw the flowchart

Use the appropriate symbols and connect them in execution order.

### Step 6: Write pseudocode

Express the logic in concise steps before coding.

### Step 7: Perform a dry run

Manually trace the solution using a small set of sample values.

### Step 8: Implement in Python

Convert the verified logic into working code.

### Step 9: Test the implementation

Try ordinary inputs, boundary cases, and invalid values where applicable.

### Step 10: Analyse the solution

Consider its correctness, time complexity, and auxiliary-space requirements.

---

## Worked Example: Find the Largest Number

**Problem:** Read two numbers and display the larger value.

### Algorithm

1. Start.
2. Read numbers A and B.
3. Compare A with B.
4. If A is greater than B, display A.
5. If B is greater than A, display B.
6. Otherwise, display that both values are equal.
7. End.

### Flowchart

```text
         ( START )
             |
             v
        / Input A, B /
             |
             v
         < A > B? >
          /      \
        Yes       No
         |         |
         v         v
    [Display A] < B > A? >
                   /     \
                 Yes      No
                  |        |
                  v        v
            [Display B] [Display equal]
                  \        /
                   \      /
                      v
                    ( END )
```

### Python implementation

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both numbers are equal.")
```

### Dry run

| A | B | Decision | Output |
|---:|---:|---|---|
| 10 | 7 | A > B | 10 |
| 4 | 9 | B > A | 9 |
| 5 | 5 | Values are equal | Both numbers are equal |

### Complexity

For fixed-size numeric inputs, this solution performs a constant number of comparisons:

- Time complexity: `O(1)`.
- Auxiliary space: `O(1)`.

---

## Running the Python Programs

Open PowerShell in the root folder of your `DSA-Python` repository.

For example, to run the first Algorithms Basics program:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\01_Algorithm_Basics\01_algorithm_basics.py"
```

To run Flowchart Basics:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\01_FlowChart_Basics\01_flowchart_basics.py"
```

Each topic has its own Python program and interactive menu. Use the corresponding command to open a different topic.

If your local folder structure differs, update the command to match the actual path. On Windows, `py` may also work when `python` is not recognized.

---

## Practice Guidelines

Each topic is designed to provide:

- **12 examples** to demonstrate important concepts.
- **12 solved practice questions** to help you understand implementations.
- **5 unsolved practice questions** to encourage independent problem-solving.

For every question:

1. Write down the input and expected output.
2. Develop the algorithm.
3. Draw a flowchart when relevant.
4. Write pseudocode.
5. Perform a dry run.
6. Implement the solution in Python.
7. Test boundary cases.
8. Explain the result and complexity.

Do not only copy the code. Make sure you can explain why every important condition and loop exists.

---

## Common Mistakes

- Coding before understanding the complete problem.
- Skipping the algorithm design stage.
- Drawing a flowchart that does not match the implementation.
- Forgetting to represent one of the decision branches.
- Creating loops without a clear exit condition.
- Ignoring invalid inputs and boundary cases.
- Testing only one input.
- Declaring an algorithm efficient without examining its operations.
- Memorizing answers without understanding the underlying logic.

---

## Interview Questions

**1. What is an algorithm?**

An algorithm is a finite sequence of well-defined steps used to solve a problem.

**2. What is a flowchart?**

A flowchart represents the steps and control flow of an algorithm using symbols and arrows.

**3. What is the difference between an algorithm and a program?**

An algorithm describes the solution logic, while a program implements that logic in a programming language.

**4. What are the three fundamental control structures?**

Sequence, selection, and iteration.

**5. Why are flowcharts useful?**

They make program logic visible and can help identify missing operations or incorrect branches before implementation.

**6. What is a dry run?**

A dry run manually traces the algorithm using sample values.

**7. What is time complexity?**

Time complexity describes how an algorithm's operation count grows with input size.

**8. What is auxiliary space complexity?**

It describes the additional working memory an algorithm uses, excluding input storage under the usual convention.

**9. Why should an algorithm be tested with boundary cases?**

Boundary tests help reveal errors in conditions, range limits, and stopping rules.

**10. How are algorithms and flowcharts useful for DSA?**

They help develop structured logic, which is essential when designing and understanding data-structure operations and algorithms.

---

## Completion Checklist

- [ ] I understand the purpose of algorithms.
- [ ] I can write steps to solve a basic problem.
- [ ] I understand the characteristics of a good algorithm.
- [ ] I can recognize common time-complexity patterns.
- [ ] I can identify flowchart symbols.
- [ ] I can draw a flowchart for input/output operations.
- [ ] I can represent decisions and loops.
- [ ] I can convert a flowchart into Python code.
- [ ] I can manually dry-run an algorithm.
- [ ] I have completed all six Algorithms Basics topics.
- [ ] I have completed all five Flowcharts topics.
- [ ] I have attempted the unsolved practice questions.

---

## Next Section

After completing Algorithms and Flowcharts, continue to **Pseudocode and Problem-Solving**.

This next section develops your ability to express logic in structured, language-independent instructions, break larger problems into smaller parts, identify patterns, and design solutions before coding them in Python.

Keep practising and focus on understanding the logic behind each solution.
