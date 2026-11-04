# Problem Solving in Python

**Week:** 1 — Programming Fundamentals  
**Section:** Pseudocode and Problem Solving  
**Focus:** Problem Analysis, Algorithms, Logical Thinking, and Practice  
**Programming Language:** Python 3  
**Difficulty:** Beginner to Intermediate

---

## Table of Contents

1. Introduction
2. Purpose of This Section
3. Learning Objectives
4. Section Roadmap
5. Folder Structure
6. Recommended Learning Order
7. What Is Problem Solving?
8. The Problem-Solving Lifecycle
9. Input-Process-Output Model
10. Problem Decomposition
11. Algorithms and Pseudocode
12. Sequence, Selection, and Iteration
13. Dry Runs and Trace Tables
14. Input Validation and Edge Cases
15. Common Problem-Solving Patterns
16. Worked Example: Sum of Even Numbers
17. Testing and Debugging
18. Time and Space Complexity
19. How to Practise Effectively
20. Common Mistakes
21. Frequently Asked Questions
22. Completion Checklist
23. Next Steps

---

# 1. Introduction

Problem solving is one of the most important skills in programming. Learning a programming language helps you write instructions that a computer can execute, but problem-solving skills help you determine which instructions are needed in the first place.

A good programmer does not immediately start writing code for every new question. First, they understand the problem, identify the required inputs and outputs, consider the rules, design a logical solution, and verify that the approach works.

This section develops those skills through algorithms, pseudocode, step-by-step solutions, and programming practice using Python.

The topics are arranged in a progressive learning path. You will begin with the fundamentals of problem solving, learn how to break problems into smaller tasks, identify recurring patterns, design ordered solutions, and finally practise solving programming problems.

The aim is to build a foundation for Data Structures and Algorithms (DSA), technical interviews, competitive programming, and software development.

# 2. Purpose of This Section

This section connects the concepts introduced in programming fundamentals with their practical application.

By working through the topics in order, you will learn to:

- Understand what a programming problem is asking.
- Identify inputs, outputs, requirements, and constraints.
- Divide complex tasks into smaller, manageable steps.
- Design algorithms before implementation.
- Express logic using pseudocode.
- Trace an algorithm using sample data.
- Recognize common problem-solving patterns.
- Implement logical solutions in Python.
- Test and debug programs systematically.
- Understand introductory time and space complexity.

The emphasis is on understanding *why* a solution works rather than memorizing code.

# 3. Learning Objectives

After completing this section, you should be able to:

1. Explain the difference between a problem statement, an algorithm, and pseudocode.
2. Identify the input, processing, and output of a problem.
3. Break a large problem into smaller subproblems.
4. Write algorithms using clear, ordered instructions.
5. Apply conditions, loops, and functions appropriately.
6. Perform dry runs and prepare trace tables.
7. Validate inputs and account for edge cases.
8. Implement algorithms using Python.
9. Recognize common patterns such as counting, accumulation, searching, and comparison.
10. Test a solution with multiple test cases.
11. Identify and correct syntax, runtime, and logical errors.
12. Explain the basic time and space complexity of common solutions.
13. Attempt unfamiliar programming questions using a structured process.

# 4. Section Roadmap

This section contains five child folders.

<text weight="medium">01. Problem-Solving Basics</text>

Understand what problem solving means, why it matters, and how to approach a programming task.

<text weight="medium">02. Problem Breakdown</text>

Learn to divide a problem into smaller tasks and organize the solution logically.

<text weight="medium">03. Pattern Identification</text>

Learn to recognize useful patterns in problems, such as accumulation, frequency counting, searching, and two-pointer comparisons.

<text weight="medium">04. Step-by-Step Solution</text>

Practise converting a problem into an ordered sequence of instructions, performing dry runs, and implementing the resulting algorithm.

<text weight="medium">05. Practice Problems</text>

Apply the concepts through guided examples, solved problems, and independent exercises.

The recommended order is important because each folder builds on the concepts introduced earlier.

# 5. Folder Structure

The section is organized as follows:

```text
02-Problem-Solving/
│
├── README.md
│
├── 01_Problem_Solving_Basics/
│   ├── README.md
│   └── 01_problem_solving_basics.py
│
├── 02_Problem_Breakdown/
│   ├── README.md
│   └── 02_problem_breakdown.py
│
├── 03_Pattern_Identification/
│   ├── README.md
│   └── 03_pattern_identification.py
│
├── 04_Step_By_Step_Solution/
│   ├── README.md
│   └── 04_step_by_step_solution.py
│
└── 05_Practice_Problems/
    ├── README.md
    └── 05_practice_problems.py
```

Each child folder contains a Python program for practical learning and a README with the corresponding topic documentation.

This parent README provides the overall roadmap, while the individual READMEs explain each topic in greater detail.

# 6. Recommended Learning Order

Follow this sequence to build your problem-solving skills progressively.

| Order | Topic | Main goal |
|---:|---|---|
| 1 | Problem-Solving Basics | Understand how to approach a problem |
| 2 | Problem Breakdown | Divide problems into smaller tasks |
| 3 | Pattern Identification | Recognize reusable solution patterns |
| 4 | Step-by-Step Solution | Design, trace, and implement algorithms |
| 5 | Practice Problems | Apply the concepts independently |

Do not rush through the section merely to complete the folders. Make sure you can explain the reasoning behind the examples and attempt the practice questions independently.

## Topic 1: Problem-Solving Basics

**Folder:** `01_Problem_Solving_Basics/`

[Open the Problem-Solving Basics README](01_Problem_Solving_Basics/README.md)

This topic introduces the purpose of problem solving, the information contained in a problem statement, and the general stages involved in designing a solution.

Focus on understanding the problem, identifying its requirements, and deciding what a correct result should look like.

## Topic 2: Problem Breakdown

**Folder:** `02_Problem_Breakdown/`

[Open the Problem Breakdown README](02_Problem_Breakdown/README.md)

This topic teaches you how to decompose a complicated task into smaller operations.

Practise separating input collection, validation, calculations, decisions, and output into understandable steps.

## Topic 3: Pattern Identification

**Folder:** `03_Pattern_Identification/`

[Open the Pattern Identification README](03_Pattern_Identification/README.md)

This topic introduces recurring approaches that appear across different programming questions.

Examples include:

- Accumulating a running total.
- Counting occurrences.
- Finding minimum or maximum values.
- Searching for a target.
- Comparing pairs of values.
- Building prefix sums.
- Recognizing patterns in digits and sequences.

Recognizing a pattern can help you choose a suitable algorithm for a new problem.

## Topic 4: Step-by-Step Solution

**Folder:** `04_Step_By_Step_Solution/`

[Open the Step-by-Step Solution README](04_Step_By_Step_Solution/README.md)

This topic develops the skill of transforming an idea into a complete algorithm.

Focus on writing ordered steps, preparing pseudocode, performing dry runs, handling special cases, and converting the solution into Python.

## Topic 5: Practice Problems

**Folder:** `05_Practice_Problems/`

[Open the Practice Problems README](05_Practice_Problems/README.md)

This topic brings together the earlier concepts through guided examples, solved programming problems, and independent practice.

Attempt each problem before studying the provided solution. Use the test cases and complexity descriptions to understand the strengths and limitations of your approach.

# 7. What Is Problem Solving?

In programming, problem solving is the process of developing a correct and practical method for transforming given inputs into the required outputs.

Consider the task of adding two numbers.

**Input:**

```text
First number = 12
Second number = 18
```

**Processing:**

```text
sum = 12 + 18
```

**Output:**

```text
30
```

Although this problem is simple, it still involves identifying the input, selecting an operation, calculating the result, and producing the output.

More advanced problems use the same basic idea but may require conditions, repetition, collections, searching, or multiple processing stages.

## Characteristics of a Good Solution

A good solution should be:

- **Correct:** It produces the required result for valid inputs.
- **Clear:** The logic is easy to understand.
- **Finite:** The algorithm terminates for its intended valid inputs.
- **Practical:** Its operations can be carried out effectively.
- **Testable:** Its behavior can be checked using suitable test cases.
- **Appropriately efficient:** It uses reasonable time and memory for the problem's requirements.

The simplest-looking solution is not always the most efficient, and the shortest code is not necessarily the clearest or most correct.

# 8. The Problem-Solving Lifecycle

Use the following workflow when approaching a new programming question.

## Step 1: Understand the Problem

Read the complete problem statement and identify the desired outcome.

## Step 2: Identify Inputs and Outputs

Determine what data the program receives and what result it must produce.

## Step 3: Identify Constraints

Check input limits, assumptions, special rules, and any required ordering or format.

## Step 4: Break the Problem into Tasks

Divide the problem into smaller operations that can be designed and verified separately.

## Step 5: Select a Strategy

Choose a suitable approach using arithmetic, conditions, loops, strings, lists, or another appropriate structure.

## Step 6: Design the Algorithm

Write the solution in a clear sequence of steps.

## Step 7: Write Pseudocode

Express the logic independently of Python syntax.

## Step 8: Perform a Dry Run

Manually execute the algorithm using a small sample input.

## Step 9: Implement in Python

Convert the verified algorithm into executable code.

## Step 10: Test and Debug

Check normal cases, boundary cases, and invalid inputs where appropriate. Compare actual output with expected output.

## Step 11: Analyse Efficiency

Consider time complexity and auxiliary space when relevant.

### Workflow Diagram

```text
Problem Statement
        |
        v
Understand the Requirements
        |
        v
Identify Inputs and Outputs
        |
        v
Check Constraints and Edge Cases
        |
        v
Break Down the Problem
        |
        v
Design Algorithm and Pseudocode
        |
        v
Dry Run and Verify
        |
        v
Implement in Python
        |
        v
Test and Debug
        |
        v
Review Efficiency
```

# 9. Input-Process-Output Model

The Input-Process-Output (IPO) model helps organize a problem into three main components.

| Component | Meaning | Example |
|---|---|---|
| Input | Data received | Two integers |
| Process | Operation performed | Add the integers |
| Output | Result produced | Their sum |

Example:

```text
INPUT a, b
sum = a + b
OUTPUT sum
```

The IPO model is useful for basic calculations, validation tasks, and more complex programs.

For larger problems, the processing stage may contain many conditions, loops, and subtasks. The IPO model still provides a useful starting point.

# 10. Problem Decomposition

Problem decomposition means dividing a large problem into smaller, manageable subtasks.

Consider a program that calculates a student's result.

The overall task might involve:

1. Reading marks.
2. Checking whether the marks are valid.
3. Calculating the total.
4. Calculating the average.
5. Applying the result rules.
6. Displaying the result.

Each stage has a clear responsibility.

Decomposition helps you understand the solution, find errors more easily, and organize reusable operations into functions.

It is particularly useful when a problem has multiple requirements or contains several processing stages.

# 11. Algorithms and Pseudocode

An **algorithm** is a finite sequence of well-defined steps for solving a problem.

**Pseudocode** is a readable, language-independent way to describe those steps.

Example: Find the largest of three numbers.

### Algorithm

1. Read three numbers.
2. Initialize `largest` with the first number.
3. Compare the second number with `largest`; update it if necessary.
4. Compare the third number with `largest`; update it if necessary.
5. Display `largest`.

### Pseudocode

```text
START
    INPUT a, b, c
    largest = a

    IF b > largest
        largest = b
    END IF

    IF c > largest
        largest = c
    END IF

    OUTPUT largest
STOP
```

### Python

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest:", largest)
```

The algorithm describes the intended logic, pseudocode expresses that logic in a readable form, and Python implements it using executable syntax.

# 12. Sequence, Selection, and Iteration

Most beginner programming problems rely on three fundamental control structures.

## Sequence

Instructions execute in order.

```python
a = 10
b = 20
total = a + b
print(total)
```

## Selection

A condition determines which branch executes.

```python
if number > 0:
    print("Positive")
else:
    print("Zero or negative")
```

This example separates positive values from all other values. A complete positive/negative/zero classification would require an additional branch.

## Iteration

A loop repeats instructions.

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

Output:

```text
15
```

Some algorithms need only one of these structures; many practical problems combine all three.

# 13. Dry Runs and Trace Tables

A dry run is the manual execution of an algorithm using sample data. A trace table records important values as the algorithm progresses.

Consider the sum of numbers from `1` through `4`.

```text
total = 0

FOR number = 1 TO 4
    total = total + number
END FOR
```

| Iteration | Number | Previous total | New total |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

The final result is `10`.

Dry runs help reveal incorrect variable initialization, condition errors, missing updates, and mistakes in loop boundaries.

Before implementing an unfamiliar algorithm, trace at least one representative input by hand.

# 14. Input Validation and Edge Cases

Input validation ensures that values meet the requirements of the problem before the main processing takes place.

An edge case is an unusual or boundary input that deserves specific testing.

Examples include:

| Problem type | Relevant cases |
|---|---|
| Factorial | Zero, one, negative input |
| List processing | Empty list, one element, duplicates |
| Searching | Target absent, target at either end |
| Arithmetic | Zero and negative values where permitted |
| String processing | Empty text, mixed case, repeated spaces |
| Binary search | Empty list, unsorted input |
| Matrix processing | Incorrect row length, smallest permitted matrix |

Validation rules depend on the problem definition. Negative numbers are valid for some tasks and invalid for others.

Decide the requirements first, then implement validation that matches those requirements.

# 15. Common Problem-Solving Patterns

Many programming questions can be approached using a small set of recurring patterns.

| Pattern | Purpose | Example |
|---|---|---|
| Accumulator | Combine values | Calculate a sum |
| Counter | Count events | Count vowels |
| Running maximum/minimum | Track an extreme value | Find the largest number |
| Linear scan | Examine items one by one | Linear search |
| Two indices | Coordinate comparisons | Merge two sorted lists |
| Nested loops | Examine combinations | Find pairs with a target sum |
| Digit processing | Extract and process digits | Sum digits |
| Prefix sums | Reuse cumulative totals | Answer range-sum queries |
| Validation | Check required properties | Verify sorted input |
| Divide and conquer | Reduce a problem into smaller parts | Binary search |

These patterns do not replace understanding the problem. They provide reusable strategies that you can adapt to the requirements and constraints of a particular question.

# 16. Worked Example: Sum of Even Numbers

This example demonstrates how the concepts in the section work together.

**Problem:** Given a list of integers, calculate the sum of its even values.

**Input:**

```text
1 2 3 4 6
```

**Expected output:**

```text
12
```

## Step 1: Identify Input and Output

- Input: A list of integers.
- Output: The sum of all even elements.

## Step 2: Design the Algorithm

1. Read the list.
2. Initialize `total = 0`.
3. Visit each number.
4. If `number % 2 == 0`, add it to `total`.
5. Display the total.

## Step 3: Write Pseudocode

```text
INPUT numbers
total = 0

FOR each number IN numbers
    IF number MOD 2 = 0
        total = total + number
    END IF
END FOR

OUTPUT total
```

## Step 4: Perform a Dry Run

| Number | Even? | Running total |
|---:|---|---:|
| 1 | No | 0 |
| 2 | Yes | 2 |
| 3 | No | 2 |
| 4 | Yes | 6 |
| 6 | Yes | 12 |

## Step 5: Implement in Python

```python
numbers = [1, 2, 3, 4, 6]
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Sum of even numbers:", total)
```

Output:

```text
Sum of even numbers: 12
```

## Step 6: Test Additional Inputs

| Input | Expected sum |
|---|---:|
| `[2, 4, 6]` | 12 |
| `[1, 3, 5]` | 0 |
| `[-2, 3, 4]` | 2 |
| `[]` | 0 |

## Step 7: Analyse Complexity

For a list containing `n` elements, every element is inspected once.

- Time complexity: `O(n)`.
- Auxiliary space: `O(1)` for the running total and current value, excluding the input list.

This example demonstrates problem analysis, algorithm design, pseudocode, a dry run, Python implementation, testing, and complexity analysis in one workflow.

# 17. Testing and Debugging

Testing verifies whether a solution behaves as expected for selected inputs. Debugging is the process of identifying and correcting errors.

## Types of Errors

**Syntax error:** Python cannot parse the program correctly.

**Runtime error:** An error occurs while the program is executing, such as dividing by zero.

**Logical error:** The program runs but produces an incorrect result because its logic is wrong.

### Example of a Logical Error

If `total` contains the sum of three marks, the following calculation would not produce their average:

```python
average = total / 2
```

The denominator should match the number of marks:

```python
average = total / 3
```

### Recommended Testing Process

1. Choose a normal input.
2. Determine the expected result before running the code.
3. Run the program and compare results.
4. Test relevant boundary cases.
5. Test special conditions and invalid input.
6. Investigate differences and correct their cause.
7. Retest the corrected version.

Passing one test does not prove that a program is correct for every valid input. Use enough tests to cover the relevant behavior of the algorithm.

# 18. Time and Space Complexity

Complexity analysis studies how an algorithm's resource requirements grow as the input size increases.

## Common Time Complexities

| Complexity | General meaning | Common example |
|---|---|---|
| `O(1)` | Constant work | Access an element by index |
| `O(log n)` | Logarithmic growth | Binary search |
| `O(n)` | Linear growth | One complete list traversal |
| `O(n log n)` | Linearithmic growth | Merge sort |
| `O(n²)` | Quadratic growth | Compare all pairs with nested loops |

These are common patterns, and the actual complexity depends on the implemented algorithm.

### Time Complexity

Time complexity describes how the number of operations grows as the input becomes larger.

### Space Complexity

Space complexity describes how memory usage grows. Auxiliary space focuses on additional memory used by the algorithm; input and output storage may be discussed separately.

### Example Comparison

A program that scans a list once usually takes `O(n)` time.

A program that examines every pair of distinct indices usually takes `O(n²)` time.

Understanding this difference becomes increasingly important when working with large datasets and advanced DSA problems.

# 19. How to Practise Effectively

Use the following learning method throughout this section.

### Phase 1: Understand

Read the topic documentation and understand the purpose of each concept.

### Phase 2: Run

Execute the Python file and try the examples with sample inputs.

### Phase 3: Predict

Before running a program, predict the expected output and the important variable updates.

### Phase 4: Reproduce

Close or minimize the original solution and implement the same logic yourself.

### Phase 5: Modify

Change the inputs or problem requirements and adapt the solution.

### Phase 6: Test

Try normal inputs, boundary cases, and special cases.

### Phase 7: Explain

Explain why the algorithm works, what each important variable represents, and how efficient the solution is.

### Phase 8: Practise Independently

Attempt the unsolved questions without copying code. Refer to hints only after trying to formulate your own approach.

## Suggested Revision Routine

| Session | Focus |
|---|---|
| 1 | Problem-solving basics |
| 2 | Breaking problems into smaller tasks |
| 3 | Recognizing common patterns |
| 4 | Algorithms, pseudocode, and dry runs |
| 5 | Solved and unsolved practice problems |
| 6 | Testing, revision, and independent implementation |

The number of sessions is flexible. Spend more time on concepts you cannot yet explain or implement independently.

# 20. Common Mistakes

### Starting to Code Too Early

Understand the requirements and design the logic before implementation.

### Skipping Dry Runs

Trace the algorithm using small values, especially when loops and multiple variable updates are involved.

### Ignoring Edge Cases

Consider the relevant special inputs and ensure that the solution follows the stated requirements.

### Using Unclear Variable Names

Names such as `total`, `count`, `largest`, and `target` often make the purpose of a variable easier to understand.

### Using the Wrong Algorithm

Select an approach that satisfies the constraints. For example, binary search requires sorted input.

### Testing Only One Case

Use several test cases to check ordinary behavior, boundaries, and important conditional branches.

### Memorizing Without Understanding

Reimplement the solution independently and explain why its logic works.

### Ignoring Efficiency

A correct solution is the first goal. Once correctness is established, study whether the solution uses an appropriate amount of time and memory.

# 21. Frequently Asked Questions

### Q1. Why is problem solving important in programming?

It helps determine the logic and operations needed to solve a task correctly before writing the implementation.

### Q2. What is the difference between an algorithm and pseudocode?

An algorithm is the logical solution. Pseudocode is a language-independent way of representing that solution in readable steps.

### Q3. Why should I break a problem into smaller tasks?

Smaller tasks are easier to understand, test, debug, and combine into a complete solution.

### Q4. What is a dry run?

A dry run is a manual execution of an algorithm using sample data to trace the changes in variables and verify the result.

### Q5. Should I write pseudocode for every problem?

Pseudocode is particularly useful for unfamiliar or multi-step problems. For very simple problems, you may not need a full written version every time, but you should still understand the logic before coding.

### Q6. How can I improve my problem-solving ability?

Practise regularly, write algorithms before coding, test different inputs, review mistakes, and explain solutions in your own words.

### Q7. Is this section enough to complete DSA?

No. This section builds a foundation in problem-solving. DSA also requires studying data structures, algorithm design, searching, sorting, recursion, graphs, trees, and other topics.

### Q8. Why does the repository contain both `.py` and `.md` files?

The Python files contain runnable examples and solutions. The Markdown files document the concepts, algorithms, explanations, and learning instructions.

### Q9. What should I do when I cannot solve an unsolved question?

Start with a small sample, write down the expected input and output, break the problem into smaller operations, and create pseudocode. If you remain stuck, seek a hint about the next step.

### Q10. How do I know whether I have completed this section?

You should be able to explain the main concepts, implement representative solved problems without copying, test your programs, and make a genuine attempt at the unsolved questions.

# 22. Completion Checklist

Use this checklist before moving on to the next section of Week 1.

## Understanding

- [ ] I understand what problem solving means.
- [ ] I can identify input, processing, and output.
- [ ] I understand problem decomposition.
- [ ] I know the difference between an algorithm and pseudocode.
- [ ] I can use sequence, selection, and iteration.
- [ ] I understand dry runs and trace tables.

## Implementation

- [ ] I have executed the example programs.
- [ ] I can write basic conditions and loops.
- [ ] I can process numbers, digits, strings, and lists.
- [ ] I can break a problem into functions when appropriate.
- [ ] I have implemented representative problems independently.

## Testing and Analysis

- [ ] I have tested multiple inputs.
- [ ] I have considered edge cases.
- [ ] I can identify common syntax, runtime, and logical errors.
- [ ] I understand introductory time and space complexity.
- [ ] I can explain why my solutions work.

## Independent Practice

- [ ] I have attempted the unsolved questions.
- [ ] I can create an algorithm for a new beginner problem.
- [ ] I can convert that algorithm into Python.
- [ ] I can dry-run and verify my implementation.

# 23. Next Steps

After completing the five child folders:

1. Review the algorithms and concepts you found difficult.
2. Reimplement several solved problems without referring to their source code.
3. Complete the unsolved questions or revisit them with additional practice.
4. Review the related material in the Pseudocode and Flowcharts sections.
5. Continue to the next topic in your Week 1 programming roadmap.

**Final goal:** Learn to approach a programming problem systematically, design a logical solution, implement it in Python, test its correctness, and explain your reasoning clearly.