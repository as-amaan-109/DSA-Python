# Python Programming Practice Problems

**Week:** 1 — Programming Fundamentals  
**Section:** Pseudocode and Problem Solving  
**Topic:** Practice Problems  
**Language:** Python 3  
**Level:** Beginner to Intermediate

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. Why Programming Practice Matters
4. Problem-Solving Workflow
5. How to Approach a New Problem
6. Understanding Input, Processing, and Output
7. Writing Algorithms and Pseudocode
8. Dry Runs and Trace Tables
9. Test Cases and Edge Cases
10. Python Concepts Used in This Folder
11. The 12 Guided Examples
12. The 12 Solved Practice Problems
13. Five Unsolved Practice Questions
14. Time and Space Complexity
15. Common Programming Patterns
16. Common Mistakes and Debugging
17. Recommended Practice Strategy
18. How to Run the Program
19. Interactive Menu Guide
20. Expected Folder Structure
21. Related Topics
22. Frequently Asked Questions
23. Final Revision Checklist

---

# 1. Introduction

Programming practice is the process of applying programming concepts to problems that require logical thinking, planning, implementation, and testing.

Learning the syntax of Python is only one part of becoming a programmer. You must also learn to understand unfamiliar problems, select suitable operations, design algorithms, and verify that your programs produce correct results.

This folder brings together the concepts introduced in the earlier problem-solving topics and applies them to practical exercises.

The Python program provides 12 guided examples, 12 solved problems, 5 unsolved practice questions, and an interactive menu.

### Why This Topic Matters

When you receive a programming question, you need to determine:

- What the problem requires.
- Which inputs are necessary.
- What output should be produced.
- Which operations and conditions are needed.
- Whether repetition is required.
- What happens in special cases.
- How to verify that the solution works.
- Whether the solution uses time and memory efficiently.

Practising these steps regularly helps build a foundation for Data Structures and Algorithms (DSA), competitive programming, technical interviews, and software development.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Read a problem statement and identify its objective.
2. Identify input, processing, and output.
3. Break a task into smaller logical steps.
4. Design algorithms using sequence, selection, and iteration.
5. Write pseudocode before implementing complex logic.
6. Use Python variables, operators, strings, lists, conditions, and loops.
7. Create and use functions for reusable tasks.
8. Process digits, text, and collections of numbers.
9. Search for patterns and compare values.
10. Perform manual dry runs using trace tables.
11. Test normal inputs, boundary cases, and invalid inputs.
12. Recognize common mistakes and debug incorrect results.
13. Estimate the time and auxiliary space complexity of basic algorithms.
14. Solve new questions independently instead of memorizing existing code.

---

# 3. Why Programming Practice Matters

Theory helps you understand a concept, but practice teaches you how to use that concept.

For example, knowing the purpose of a loop is different from deciding how a loop should solve a particular problem.

Consider the task of finding the sum of digits of an integer.

For the number `528`, the required calculation is:

```text
5 + 2 + 8 = 15
```

A complete solution requires several decisions:

1. How will the digits be extracted?
2. Where will the running total be stored?
3. When should the loop stop?
4. What should happen when the input is zero?
5. Should negative input be accepted?
6. How can the implementation be tested?

These are problem-solving decisions, not merely Python syntax.

### Benefits of Regular Practice

- Develops logical and analytical thinking.
- Improves understanding of conditions and loops.
- Makes algorithms easier to design.
- Helps identify edge cases.
- Strengthens debugging skills.
- Improves code readability.
- Builds confidence with unfamiliar problems.
- Prepares you for DSA and coding assessments.

**Remember:** The objective is not only to make a program work. It is to understand why it works.

---

# 4. Problem-Solving Workflow

Use a consistent workflow whenever you begin a new programming question.

## Step 1: Understand the Requirement

Read the complete problem statement and identify the result that must be produced.

Do not start coding until you understand what the program should do.

## Step 2: Identify the Inputs

Determine the data the program receives.

Examples include:

- One integer.
- Two numbers.
- A sentence.
- A list of integers.
- A matrix.
- A target value to search for.

## Step 3: Identify the Expected Output

Write down the result that should be produced for a valid input.

For a list-sum problem, the output is the sum of the list elements. For a search problem, the output may be an index or an indication that the target is absent.

## Step 4: Identify Constraints

Determine the restrictions on the input.

Examples:

- A rotation count cannot be negative.
- A binary-search list must be sorted.
- A matrix must have the required dimensions.
- A missing-number problem may require distinct values from a specified range.

## Step 5: Break the Problem into Smaller Steps

Divide the task into a logical sequence of operations.

For a word-counting problem, the stages might be reading the sentence, separating words, counting them, and displaying the result.

## Step 6: Design the Algorithm

Choose suitable conditions, loops, data structures, and calculations.

## Step 7: Write Pseudocode

Describe the algorithm in simple, language-independent steps.

## Step 8: Perform a Dry Run

Use a small input and trace the important variables manually.

## Step 9: Implement in Python

Translate each algorithmic operation into executable code.

## Step 10: Test and Debug

Compare the actual output with the expected output. Correct any errors you find.

## Step 11: Review Efficiency

Consider how the amount of work and memory usage changes as the input grows.

### Complete Workflow

```text
Understand the Problem
          |
          v
Identify Inputs and Outputs
          |
          v
Check Constraints and Edge Cases
          |
          v
Break the Task into Steps
          |
          v
Design Algorithm / Pseudocode
          |
          v
Dry Run the Algorithm
          |
          v
Implement in Python
          |
          v
Test and Debug
          |
          v
Review Time and Space Complexity
```

---

# 5. How to Approach a New Problem

Before writing code, prepare a small problem-analysis section.

Consider the following example.

### Problem: Sum the Even Numbers in a List

**Problem statement:** Given a list of integers, calculate the sum of all even values.

**Input:**

```text
1 2 3 4 6
```

**Expected output:**

```text
12
```

The even values are `2`, `4`, and `6`.

### Step 1: Define the Input and Output

- Input: A list of integers.
- Output: The sum of the even integers.
- Processing: Check each number and add it to a total when it is even.

### Step 2: Write the Algorithm

1. Read the list.
2. Initialize `total = 0`.
3. Visit each number.
4. Check whether `number % 2 == 0`.
5. If the condition is true, add the number to `total`.
6. Display `total`.

### Step 3: Write Pseudocode

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

### Step 4: Dry Run

| Number | Even? | Total after processing |
|---:|---|---:|
| 1 | No | 0 |
| 2 | Yes | 2 |
| 3 | No | 2 |
| 4 | Yes | 6 |
| 6 | Yes | 12 |

### Step 5: Implement in Python

```python
numbers = [1, 2, 3, 4, 6]
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print(total)
```

Output:

```text
12
```

This approach separates the problem's logic from its implementation.

---

# 6. Understanding Input, Processing, and Output

The Input-Process-Output (IPO) model is a useful starting point for many programming questions.

| Component | Purpose | Example |
|---|---|---|
| Input | Receive data | A list of integers |
| Processing | Apply operations | Add all even values |
| Output | Produce the result | `12` |

Some problems require additional stages such as validation, repeated processing, or multiple outputs, but the IPO model remains useful.

### Questions to Ask

**Input:** What data must be received?

**Processing:** Which rules, comparisons, or calculations are needed?

**Output:** What exact result should be displayed or returned?

Defining these three components prevents misunderstandings and helps guide the design of the algorithm.

---

# 7. Writing Algorithms and Pseudocode

An algorithm is a sequence of finite, clear instructions that solves a problem.

Pseudocode is a readable way to describe those instructions without requiring a particular programming language's syntax.

### Example: Fibonacci Sequence

The Fibonacci sequence begins with `0` and `1`. Each subsequent value is the sum of the two preceding values.

Example:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

### Algorithm

1. Read the number of required terms, `n`.
2. Reject negative input.
3. Initialize the first two numbers as `0` and `1`.
4. Repeat `n` times:
   - Add the current first value to the output sequence.
   - Update the first value to the second.
   - Update the second value to the sum of the previous two values.
5. Display the sequence.

### Pseudocode

```text
INPUT n

IF n < 0
    OUTPUT "Invalid input"
ELSE
    first = 0
    second = 1
    sequence = empty list

    REPEAT n times
        APPEND first TO sequence
        next_value = first + second
        first = second
        second = next_value
    END REPEAT

    OUTPUT sequence
END IF
```

### Why Pseudocode Is Useful

Pseudocode allows you to check the logic independently of Python syntax. It is particularly helpful for loops, conditional branches, and algorithms containing multiple steps.

---

# 8. Dry Runs and Trace Tables

A dry run is the manual execution of an algorithm using sample data.

A trace table records how important values change during execution.

### Example: Running Total

Suppose the program adds numbers from `1` through `4`.

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

Final output: `10`

### When Should You Use a Dry Run?

Use a dry run when:

- You are unfamiliar with the algorithm.
- A loop contains several updates.
- A condition has multiple branches.
- You need to understand why a result is incorrect.
- You want to verify the algorithm before coding.

A trace table does not need many columns. Include only the variables and conditions relevant to the problem.

---

# 9. Test Cases and Edge Cases

A test case specifies an input and the behavior or output expected from the program.

Testing more than one input helps reveal mistakes that a single example may not expose.

## 9.1 Example: Count Digits

Consider a program that counts the digits of an integer using its absolute value.

| Input | Expected count |
|---:|---:|
| `0` | 1 |
| `7` | 1 |
| `528` | 3 |
| `1000` | 4 |
| `-42` | 2, after taking the absolute value |

The program treats zero as a one-digit number and ignores the sign when counting digits.

## 9.2 Common Test Categories

### Normal Cases

Ordinary inputs likely to appear in regular use.

### Boundary Cases

Inputs at the limit of the stated requirements, such as the smallest valid number or a one-element list.

### Empty Inputs

Empty strings or lists, where the problem allows them.

### Invalid Inputs

Values that violate the requirements, such as an unsorted list passed to a binary-search implementation.

### Duplicate Values

Repeated values can affect maximum, minimum, searching, frequency counting, and distinct-element problems.

### Testing Principle

For every problem, ask:

1. What happens with a typical input?
2. What happens with the smallest valid input?
3. What happens with an empty input, if allowed?
4. What happens with duplicates?
5. What happens when a target does not exist?
6. What happens if the input violates a required constraint?

The relevant cases depend on the problem's specification.

---

# 10. Python Concepts Used in This Folder

## 10.1 Variables

Variables store values used by an algorithm.

```python
total = 0
count = 0
largest = 10
```

## 10.2 Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `//` | Floor division | `17 // 10` gives `1` |
| `%` | Remainder | `17 % 10` gives `7` |
| `**` | Exponentiation | `2 ** 3` gives `8` |

Modulo and floor division are especially useful when working with digits.

## 10.3 Conditions

```python
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Conditions determine which operations are performed.

## 10.4 Loops

A `for` loop is useful for iterating over a list or a known range of values.

A `while` loop is useful when repetition continues until a condition changes.

## 10.5 Strings

Strings can be inspected, split, converted to lowercase, and reversed.

Examples include counting vowels, counting words, finding the longest word, and checking text patterns.

## 10.6 Lists

Lists store ordered collections of values.

Common operations in this folder include:

- Iterating over every value.
- Finding minimum and maximum values.
- Rotating a list.
- Merging sorted lists.
- Recording matching pairs.
- Storing a generated sequence.

## 10.7 Sets

Sets store unique values and support efficient membership checks on average.

They are useful for checking whether a list contains duplicates or tracking distinct elements.

## 10.8 Functions

Functions group reusable logic into named units. This program uses functions for each example, solved problem, and menu action.

---

# 11. The 12 Guided Examples

The guided examples demonstrate core techniques before introducing more involved problems.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Input, process, and output | Basic arithmetic and IPO |
| 2 | Classify a number | Conditional branches |
| 3 | Even or odd | Modulo operator |
| 4 | Running total | Accumulator and loop |
| 5 | Multiplication table | Repetition |
| 6 | Largest of three numbers | Comparison and updates |
| 7 | Count vowels | String traversal and counter |
| 8 | Reverse a string | String slicing |
| 9 | Count digits | Integer division and loops |
| 10 | Minimum and maximum | List traversal |
| 11 | Validate age | Input validation and conditions |
| 12 | Plan test cases | Verification and test design |

### How to Study an Example

For each example:

1. Read the displayed algorithm steps.
2. Predict what should happen.
3. Enter a small sample input.
4. Compare the result with your prediction.
5. Change the input and test another case.
6. Try writing the solution yourself without looking at the code.

The objective is to learn the method, not just the output.

---

# 12. The 12 Solved Practice Problems

The solved-problems menu demonstrates a range of basic algorithms and common programming patterns.

## Problem 1: Sum of Digits

**Task:** Calculate the sum of the digits of an integer.

Example:

```text
Input: 528
Output: 15
```

**Approach:** Extract digits using `% 10`, add each digit to a total, and remove the final digit using `// 10`.

The implementation takes the absolute value, so the negative sign does not contribute to the digit sum.

**Time complexity:** `O(d)`, where `d` is the number of decimal digits.  
**Auxiliary space:** `O(1)`.

## Problem 2: Fibonacci Sequence

**Task:** Generate the first `n` Fibonacci terms, starting with `0` and `1`.

Example:

```text
Input: 7
Output: [0, 1, 1, 2, 3, 5, 8]
```

**Approach:** Maintain the previous two values and repeatedly calculate the next value.

**Time complexity:** `O(n)`.  
**Space complexity:** `O(n)` for the sequence returned by the implementation.

## Problem 3: Armstrong Number

**Task:** Determine whether a non-negative integer equals the sum of its digits raised to the power of the number of digits.

Example:

```text
153 = 1³ + 5³ + 3³
153 = 153
```

Therefore, `153` is an Armstrong number.

**Approach:** Convert the number to a string to count and iterate over its digits, calculate the required powers, and compare their sum to the original integer.

**Time complexity:** `O(d)` for `d` decimal digits, treating the digit operations as bounded-cost operations.  
**Auxiliary space:** `O(d)` for the digit string and the generator's processing context.

## Problem 4: Count Words

**Task:** Count the words in a sentence while ignoring leading, trailing, and repeated whitespace.

Example:

```text
Input: "Python is easy to learn"
Output: 5
```

**Approach:** Use `split()` without an explicit separator, then count the resulting words. Empty or whitespace-only text produces an empty word list.

**Time complexity:** `O(n)` for a sentence of length `n`.  
**Auxiliary space:** `O(n)` for the resulting word list in the general case.

## Problem 5: Find the Missing Number

**Task:** Given `n - 1` distinct integers from `1` through `n`, find the one that is missing.

Example:

```text
n = 5
List = [1, 2, 4, 5]
Output = 3
```

**Approach:** Calculate the expected sum:

```text
n * (n + 1) // 2
```

Subtract the actual list sum from the expected sum.

The implementation checks the input length, duplicate values, and allowed range before calculating the result.

**Time complexity:** `O(n)` on average for the provided validation approach.  
**Auxiliary space:** `O(n)` because it constructs a set for duplicate detection.

## Problem 6: FizzBuzz

**Task:** Print the values from `1` through `n`, with special outputs for multiples of `3` and `5`.

Rules:

- Multiples of both `3` and `5`: `FizzBuzz`
- Multiples of `3` only: `Fizz`
- Multiples of `5` only: `Buzz`
- Other values: the number itself

**Important:** Check the combined condition first. Otherwise, a multiple of `15` could be handled by an earlier divisible-by-`3` or divisible-by-`5` branch.

**Time complexity:** `O(n)`.  
**Auxiliary space:** `O(1)` apart from the current output value.

## Problem 7: Sum Even Numbers in a List

**Task:** Calculate the sum of all even elements.

Example:

```text
Input: [1, 2, 3, 4, 6]
Output: 12
```

**Approach:** Traverse the list, check each value using `% 2`, and accumulate even values in a running total.

An empty list produces a total of zero.

**Time complexity:** `O(n)`.  
**Auxiliary space:** `O(1)`.

## Problem 8: Merge Two Sorted Lists

**Task:** Combine two lists that are each sorted in ascending order, preserving sorted order in the result.

Example:

```text
First:  [1, 4, 7]
Second: [2, 3, 8]

Output: [1, 2, 3, 4, 7, 8]
```

**Approach:** Maintain two indices, compare their current values, append the smaller value, and advance the corresponding index. Append any remaining values afterward.

The implementation validates that both input lists are sorted before merging.

**Time complexity:** `O(n + m)`, where `n` and `m` are the two list lengths.  
**Auxiliary space:** `O(n + m)` for the merged result.

## Problem 9: Rotate a List Right

**Task:** Move each value `k` positions to the right, wrapping values around to the beginning.

Example:

```text
List: [1, 2, 3, 4, 5]
k = 2

Output: [4, 5, 1, 2, 3]
```

**Approach:** Reduce the rotation count with `k % len(list)`. Move the final `k` elements to the beginning.

This implementation requires a non-negative rotation count and handles an empty list separately.

**Time complexity:** `O(n)` for a list of length `n`.  
**Auxiliary space:** `O(n)` for the newly constructed list.

## Problem 10: Find Pairs with a Target Sum

**Task:** Find every pair of different list indices whose values add up to a target.

Example:

```text
List = [2, 4, 3, 5]
Target = 7

Matching value pairs:
(2, 5)
(4, 3)
```

The implementation also displays the zero-based indices of each matching pair.

**Approach:** Compare every possible index pair `(i, j)` where `i < j`.

**Time complexity:** `O(n²)` because every candidate pair is examined.  
**Auxiliary space:** `O(p)` for `p` matching pairs stored in the result; in the worst case this can be `O(n²)`.

## Problem 11: Find the Longest Word

**Task:** Find a longest whitespace-separated word in a sentence.

Example:

```text
Input: "Python makes coding enjoyable"
Output: "enjoyable"
```

**Approach:** Split the sentence into words and use `max()` with `key=len` to select a word with the greatest character count.

If multiple words share the maximum length, this implementation returns the first one among them.

**Time complexity:** `O(n)` for a sentence containing `n` characters.  
**Auxiliary space:** `O(n)` for the word list in the general case.

## Problem 12: Square-Matrix Diagonal Sums

**Task:** Find the main diagonal sum and secondary diagonal sum of a square matrix.

Example:

```text
Matrix:
1 2 3
4 5 6
7 8 9
```

Main diagonal:

```text
1 + 5 + 9 = 15
```

Secondary diagonal:

```text
3 + 5 + 7 = 15
```

Combined sum counting the centre once:

```text
15 + 15 - 5 = 25
```

**Approach:** For each row index `i`, add `matrix[i][i]` to the main diagonal and `matrix[i][n - 1 - i]` to the secondary diagonal.

For an odd-sized matrix, the centre belongs to both diagonals. Subtract it once when reporting a combined total that counts each distinct diagonal cell only once.

**Time complexity:** `O(n²)` to read the matrix of size `n × n`; the diagonal calculation itself is `O(n)`.  
**Space complexity:** `O(n²)` to store the matrix.

---

# 13. Five Unsolved Practice Questions

Solve these independently before moving on to the next section.

For each question, write the problem analysis, algorithm, pseudocode, dry run, Python solution, and test cases.

## Question 1: Collatz Sequence

Start with a positive integer `n`.

- If `n` is even, divide it by `2`.
- Otherwise, replace it with `3 * n + 1`.
- Repeat until it reaches `1`.
- Display the sequence and number of transformation steps.

Example:

```text
Start: 6
Sequence: 6, 3, 10, 5, 16, 8, 4, 2, 1
Steps: 8
```

The task is to implement the transformation and count the steps. Do not assume the program has proved that every positive starting value eventually reaches `1`.

**Hints:** Use a `while` loop, a condition, and a list to record the sequence.

## Question 2: Pangram Checker

Determine whether a sentence contains every letter from `a` through `z` at least once, ignoring case.

Example:

```text
Input: "The quick brown fox jumps over the lazy dog"
Output: Pangram
```

**Hints:** Convert the sentence to lowercase and track which English letters appear.

Decide how spaces, punctuation, and non-English characters should be treated.

## Question 3: Move Zeros to the End

Move every zero to the end of a list while preserving the relative order of the non-zero values.

Example:

```text
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

**Hints:** One approach is to collect the non-zero values first and then append the required number of zeros.

Test an all-zero list, a list with no zeros, and an empty list.

## Question 4: Longest Increasing Contiguous Run

Find the length of the longest contiguous segment in which every next value is strictly greater than the previous value.

Example:

```text
Input: [1, 2, 2, 3, 4, 1, 5]
Output length: 3
```

One longest increasing contiguous segment is `[2, 3, 4]`.

**Hints:** Track the current run length and best run length. Reset the current run when the strict-increase condition fails.

## Question 5: Matrix Row with the Largest Sum

Given a matrix, find the row with the largest sum.

Example:

```text
Matrix:
1 2 3
9 1 0
4 4 4
```

The row sums are `6`, `10`, and `12`.

Expected result: the third row, with sum `12`.

**Hints:** Calculate each row's sum and track the best result. Decide whether your program should report the first row, every tied row, or another tie-breaking rule when multiple rows have the same sum.

---

# 14. Time and Space Complexity

Complexity analysis helps compare algorithms as the size of the input grows.

## 14.1 Time Complexity

Time complexity describes how the number of operations grows with input size.

## 14.2 Space Complexity

Space complexity describes how the memory requirement grows with input size. In the descriptions below, auxiliary space refers to extra memory used by the algorithm; a stored output may require additional space.

| Complexity | Typical example | General interpretation |
|---|---|---|
| `O(1)` | Updating a counter | Constant additional work |
| `O(log n)` | Binary search | Search interval repeatedly halves |
| `O(n)` | One pass over a list | Work grows linearly |
| `O(n log n)` | Comparison sorting algorithms such as merge sort | Linearithmic growth |
| `O(n²)` | Examining all index pairs | Quadratic growth |

### Why Complexity Matters

An algorithm that works well for a list of ten values may perform poorly for a list containing millions of values.

For example, the target-sum pair solution examines all candidate index pairs, resulting in `O(n²)` time. A one-pass counting algorithm usually requires `O(n)` time.

The best solution depends on the requirements, constraints, output needed, and available memory.

---

# 15. Common Programming Patterns

The problems in this folder help build familiarity with several reusable approaches.

## 15.1 Accumulator Pattern

Use an accumulator when repeatedly combining values.

```python
total = 0

for value in numbers:
    total += value
```

Applications include list sums, digit sums, and diagonal sums.

## 15.2 Counter Pattern

Use a counter to track how often an event occurs.

```python
count = 0

for character in text:
    if character in "aeiou":
        count += 1
```

Applications include counting vowels, digits, matches, and list elements satisfying a condition.

## 15.3 Running Best Value

Use a variable that tracks the best value encountered so far.

```python
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number
```

This pattern is useful for maximum and minimum problems.

## 15.4 Two-Index Pattern

Use two indices to process two sorted lists or examine pairs.

The merge-sorted-lists solution uses one index for each input list.

The target-sum pair solution uses a nested loop to examine each index pair exactly once.

## 15.5 Digit-Processing Pattern

Use modulo and integer division to work with the digits of a number.

```python
digit = number % 10
number //= 10
```

Applications include digit sums, digit reversal, and digit counting.

## 15.6 Validation Pattern

Check required conditions before performing the main operation.

Examples include verifying list order before merging sorted lists, validating matrix row lengths, and checking constraints for a missing-number problem.

---

# 16. Common Mistakes and Debugging

## Mistake 1: Coding Before Understanding the Task

**Solution:** Identify the goal, input, output, assumptions, and constraints before implementation.

## Mistake 2: Incorrect Loop Bounds

**Solution:** Dry-run the first and last iterations, and check whether Python's `range()` stopping value is excluded.

## Mistake 3: Incorrect Variable Initialization

**Solution:** Choose initial values according to the problem. For a non-empty list maximum, the first element is a better starting point than zero when all values could be negative.

## Mistake 4: Forgetting Empty Inputs

**Solution:** Decide whether empty lists or strings are valid, then define and implement the corresponding behavior.

## Mistake 5: Ignoring Duplicate Values

**Solution:** Determine whether a problem requires distinct values, all occurrences, or unique index pairs.

## Mistake 6: Using Binary Search on Unsorted Data

**Solution:** Binary search depends on sorted input. Verify that requirement or choose an algorithm that supports the actual input.

## Mistake 7: Incorrect Condition Order

**Solution:** Check special conditions before more general conditions where necessary. FizzBuzz checks divisibility by both `3` and `5` before checking either separately.

## Mistake 8: Forgetting to Update a Loop Variable

**Solution:** Verify that every loop progresses toward its termination condition.

## Mistake 9: Testing Only One Example

**Solution:** Test ordinary, boundary, and unusual cases. Add tests for duplicates, empty inputs, missing values, and ties when relevant.

## Mistake 10: Memorizing the Solution Without Understanding It

**Solution:** Explain why each step exists and then implement the solution again without looking at the original code.

---

# 17. Recommended Practice Strategy

Use the following process for every guided example and solved problem.

### Stage 1: Understand

Read the problem and write its objective in one sentence.

### Stage 2: Analyse

Identify input, output, constraints, and important edge cases.

### Stage 3: Plan

Write the algorithm in numbered steps.

### Stage 4: Dry-Run

Use a sample input and track relevant variables.

### Stage 5: Implement

Write the Python code independently before referring to the provided implementation.

### Stage 6: Verify

Test the expected output, normal inputs, boundary cases, and invalid inputs.

### Stage 7: Explain

Explain the algorithm and its complexity in your own words.

### Suggested Practice Routine

| Session | Activity |
|---|---|
| First | Review and run the 12 guided examples |
| Second | Attempt the first six solved problems independently |
| Third | Attempt the remaining six solved problems |
| Fourth | Solve two unsolved questions without copying code |
| Fifth | Solve the remaining unsolved questions and review mistakes |

Adapt the number of sessions to your available time. Understanding and consistent practice are more important than rushing through the questions.

---

# 18. How to Run the Program

Make sure Python 3 is installed and available in your terminal.

From the repository root, execute:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\02-Problem-Solving\05_Practice_Problems\05_practice_problems.py"
```

The program presents the main menu:

```text
=================================================================
PYTHON PROGRAMMING PRACTICE PROBLEMS
=================================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View the practice checklist
0. Exit
Choose an option:
```

Enter the desired option and follow the prompts. For list inputs, separate integers with spaces.

Example:

```text
Enter integers separated by spaces: 1 2 3 4 5
```

An empty line is interpreted as an empty list wherever a list is requested.

The program retries invalid integer input in its integer-reading helper. Individual questions also validate their relevant conditions, including non-negative values, sorted input, list length, and matrix dimensions.

---

# 19. Interactive Menu Guide

The menu separates learning and practice into four sections.

### Option 1: Guided Examples

Use this section to understand common programming techniques such as:

- Input and output.
- Conditions.
- Loops and running totals.
- String processing.
- List traversal.
- Test-case planning.

### Option 2: Solved Problems

Use this section to study full solutions covering number processing, sequences, lists, searching patterns, pairs, and matrices.

### Option 3: Unsolved Questions

Use this section to review five independent practice tasks.

Attempt each problem yourself before reviewing other resources or asking for hints.

### Option 4: Practice Checklist

Use the checklist before submitting a solution or deciding that a problem is complete.

### Option 0: Exit

Ends the program normally.

---

# 20. Expected Folder Structure

The folder should contain exactly the main Python file and its documentation file:

```text
05_Practice_Problems/
│
├── 05_practice_problems.py
│
└── README.md
```

### `05_practice_problems.py`

Contains:

- Common input and display helper functions.
- Twelve guided examples.
- Twelve solved programming problems.
- Five unsolved practice questions.
- A programming practice checklist.
- Interactive navigation menus.

### `README.md`

Contains:

- Topic overview and learning objectives.
- Problem-solving techniques and workflow.
- Algorithm and pseudocode guidance.
- Dry runs and testing methods.
- Explanations of all twelve solved problems.
- Five unsolved questions and hints.
- Complexity analysis.
- Python concepts, practice strategies, and run instructions.

---

# 21. Related Topics

This folder builds on the preceding topics in the Problem-Solving section.

Once you understand the concepts here, revisit the related documentation:

- [`01_Problem_Solving_Basics`](../01_Problem_Solving_Basics/README.md)
- [`02_Problem_Breakdown`](../02_Problem_Breakdown/README.md)
- [`03_Pattern_Identification`](../03_Pattern_Identification/README.md)
- [`04_Step_By_Step_Solution`](../04_Step_By_Step_Solution/README.md)

Together, these topics cover the foundations of understanding a problem, decomposing it, recognizing patterns, designing an ordered solution, and applying those methods through practice.

---

# 22. Frequently Asked Questions

### Q1. Should I memorize the solutions?

No. First understand the logic, then try to recreate the solution without looking at the source. Practise modified versions to test your understanding.

### Q2. What should I do when I cannot solve a question?

Write down the input and output, work through a small example, break the problem into smaller steps, and develop pseudocode. If needed, ask for a hint about the next step rather than immediately copying a complete solution.

### Q3. Why are dry runs useful?

They show how variables change and help identify mistakes before or during implementation.

### Q4. How many test cases should I use?

There is no universal fixed number. Use enough tests to cover normal behavior, boundaries, special cases, and the important branches of the algorithm.

### Q5. Why does the program use helper functions?

Helper functions reduce repeated input handling and keep each example or solution organized.

### Q6. Why does binary search require sorted data?

Binary search discards half of the search range based on ordering. Without the appropriate ordering, the discarded range may contain the target.

### Q7. Do all Python programs need an interactive menu?

No. The menu is used here to organize learning examples and practice problems. A production program may use a different interface or run a particular operation directly.

### Q8. What should I study after completing this folder?

Review the entire Problem-Solving section, make sure you can solve the unsolved questions, and then continue to the next topic in your Week 1 learning path.

---

# 23. Final Revision Checklist

Before marking this folder complete, verify the following:

- [ ] I understand the difference between input, processing, and output.
- [ ] I can write a numbered algorithm before coding.
- [ ] I understand how to perform a dry run.
- [ ] I can use conditions and loops confidently.
- [ ] I can process digits and strings.
- [ ] I can traverse lists and calculate aggregate values.
- [ ] I understand the purpose of helper functions.
- [ ] I can test boundary cases and invalid inputs.
- [ ] I can explain the logic of each solved problem.
- [ ] I have attempted all five unsolved questions.
- [ ] I understand the basic complexity of the main algorithms.
- [ ] I can write at least some solutions from memory through understanding, not copying.

## Completion Goal

By completing this folder, you should be able to approach beginner programming questions systematically: understand the task, write the algorithm, implement it in Python, test the result, and explain why the solution works.

**Next step:** Review the parent `02-Problem-Solving/README.md` after completing this folder so the entire Problem-Solving section is documented and connected together.