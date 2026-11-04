# Step-by-Step Solution Methods in Python

**Week:** 1 — Programming Fundamentals  
**Section:** Pseudocode and Problem Solving  
**Topic:** Step-by-Step Solution Methods  
**Language:** Python 3  
**Difficulty:** Beginner to Intermediate

---

## Table of Contents

1. Introduction to Step-by-Step Problem Solving
2. Learning Objectives
3. What Is a Problem?
4. Important Terms and Definitions
5. The Complete Problem-Solving Lifecycle
6. Input-Process-Output (IPO) Model
7. Problem Decomposition
8. Designing an Algorithm
9. Converting an Algorithm into Pseudocode
10. Sequence, Selection, and Iteration
11. Dry Run and Trace Tables
12. Input Validation and Edge Cases
13. Translating Logic into Python
14. Functions and Modular Problem Solving
15. Testing and Debugging
16. Time and Space Complexity
17. Detailed Explanation of the 12 Examples
18. Detailed Explanation of the 12 Solved Problems
19. Five Unsolved Practice Questions
20. Step-by-Step Problem-Solving Checklist
21. Common Mistakes and Their Solutions
22. Best Practices for Writing Algorithms
23. Frequently Asked Questions
24. How to Run the Python Program
25. Expected Folder Structure
26. Final Revision Notes

---

# 1. Introduction to Step-by-Step Problem Solving

Step-by-step problem solving is a systematic method of solving a problem by dividing it into small, logical, and manageable operations.

Instead of immediately writing Python code, we first understand the problem, identify the required inputs and outputs, plan the processing steps, and determine the correct sequence of operations.

Once the logic is clear, we convert it into an algorithm or pseudocode and finally implement it in Python.

This process is useful for both beginner-level programming and advanced subjects such as Data Structures and Algorithms (DSA).

### Why Is It Important?

Suppose we have to calculate the average of three students' marks.

A beginner may immediately start writing code without planning the calculation. A structured approach first identifies the following tasks:

1. Receive three marks as input.
2. Add the marks.
3. Divide the total by three.
4. Display the average.

After these steps are clear, writing the code becomes much easier.

### Main Benefits

- Improves logical thinking and analytical skills.
- Makes complex problems easier to understand.
- Reduces programming and logical errors.
- Makes code easier to test and debug.
- Helps identify missing conditions and special cases.
- Makes algorithms easier to explain during exams and interviews.
- Builds a strong foundation for DSA and competitive programming.

**Key idea:** Understand the logic first; write the code second.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

- Understand a problem statement and identify its goal.
- Determine the input, processing, and output of a problem.
- Identify constraints, conditions, and special cases.
- Break a large problem into smaller subproblems.
- Design an algorithm using clear, ordered instructions.
- Express logic using pseudocode.
- Use conditions, loops, and functions appropriately.
- Perform dry runs using sample inputs.
- Create trace tables to observe changes in variables.
- Convert an algorithm into executable Python code.
- Test programs with normal, boundary, and invalid inputs.
- Understand basic time and space complexity.
- Explain your solution clearly to another person.

---

# 3. What Is a Problem?

In programming, a problem is a task that requires a specific result from given inputs, according to a defined set of rules.

A problem statement usually describes what needs to be calculated, checked, searched, transformed, or displayed.

### Example: Find the Sum of Two Numbers

**Problem statement:** Write a program that accepts two numbers and displays their sum.

**Input:**

```text
First number: 15
Second number: 25
```

**Expected output:**

```text
Sum = 40
```

**Processing operation:**

```text
sum = first_number + second_number
```

### Understanding the Problem

Before writing code, answer these questions:

| Question | Answer for this example |
|---|---|
| What is the goal? | Add two numbers. |
| What are the inputs? | Two numbers. |
| What operation is required? | Addition. |
| What is the output? | The sum. |
| Is repetition required? | No. |
| Is a decision required? | No. |
| Is any special case relevant? | Negative values and zero are valid for addition. |

This preliminary analysis helps prevent unnecessary complexity.

---

# 4. Important Terms and Definitions

### 4.1 Problem Statement

A written description of the task that must be solved.

### 4.2 Input

The information supplied to a program.

Examples include numbers, strings, lists, and user choices.

### 4.3 Processing

The calculations, comparisons, transformations, or other operations performed on the input.

### 4.4 Output

The final result produced by the program.

### 4.5 Algorithm

A finite sequence of well-defined instructions for solving a problem.

### 4.6 Pseudocode

A language-independent representation of an algorithm using readable, structured instructions.

### 4.7 Dry Run

A manual execution of an algorithm using sample input to understand how variables and operations change.

### 4.8 Trace Table

A table used during a dry run to record variable values at important stages of execution.

### 4.9 Decomposition

Breaking a complex problem into smaller subproblems that are easier to design, solve, and test.

### 4.10 Condition

A Boolean expression that evaluates to either `True` or `False` and can control program flow.

### 4.11 Iteration

Repeating a group of instructions using a loop.

### 4.12 Debugging

Finding, understanding, and correcting errors in a program.

### 4.13 Edge Case

An input at a boundary or unusual situation that may reveal a weakness in a solution.

Examples include an empty list, zero, negative values, a single-element list, or a missing search target.

---

# 5. The Complete Problem-Solving Lifecycle

A reliable approach to solving programming problems consists of the following stages.

## Step 1: Understand the Problem

Read the problem carefully. Identify exactly what is required.

Do not assume that the expected output or rules are obvious.

## Step 2: Identify the Inputs

Determine the values the program must receive.

For example, finding the largest of three numbers requires three numeric inputs.

## Step 3: Identify the Expected Output

Decide what the program must display or return.

A sorting problem, for example, requires the values in the requested order.

## Step 4: Identify Constraints

Constraints define the valid inputs and any special rules.

Examples:

- A number must be non-negative.
- A list may be empty.
- Search input must be sorted before binary search.
- A percentage must be between 0 and 100.

## Step 5: Break the Problem into Tasks

Divide the problem into smaller operations that can be completed individually.

## Step 6: Design the Algorithm

Write a clear sequence of instructions using the required logic.

## Step 7: Write Pseudocode

Express the algorithm using simple, language-independent steps.

## Step 8: Perform a Dry Run

Use a small sample input and verify the expected variable updates and output.

## Step 9: Implement the Solution

Translate the algorithm into Python using variables, operators, conditions, loops, and functions.

## Step 10: Test the Program

Test normal inputs, boundary cases, and invalid inputs.

## Step 11: Debug Errors

Compare actual output with expected output and correct any mistakes.

## Step 12: Review Efficiency

Consider how much work and memory the algorithm requires as the input grows.

### Workflow Summary

```text
Problem Statement
       |
       v
Understand Requirements
       |
       v
Identify Input and Output
       |
       v
Check Constraints and Edge Cases
       |
       v
Break into Smaller Tasks
       |
       v
Design Algorithm
       |
       v
Write Pseudocode
       |
       v
Dry Run and Verify Logic
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

---

# 6. Input-Process-Output (IPO) Model

The Input-Process-Output model is a simple way to organize the main components of a solution.

## 6.1 Input

The data supplied to the program.

## 6.2 Process

The operations performed on the input.

## 6.3 Output

The resulting information displayed or returned by the program.

### Example: Calculate a Rectangle's Area

**Input:**

```text
length = 8
width = 4
```

**Process:**

```text
area = length * width
area = 8 * 4
area = 32
```

**Output:**

```text
Area = 32
```

### Algorithm

1. Start.
2. Read length and width.
3. Check whether either measurement is negative.
4. If either is negative, report invalid measurements.
5. Otherwise, calculate `area = length * width`.
6. Display the area.
7. Stop.

### Pseudocode

```text
START

    INPUT length
    INPUT width

    IF length < 0 OR width < 0 THEN
        OUTPUT "Invalid measurements"
    ELSE
        area = length * width
        OUTPUT area
    END IF

STOP
```

### Python Implementation

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Invalid measurements")
else:
    area = length * width
    print("Area =", area)
```

**Important:** IPO is a planning model. It can be used for small calculations as well as more complicated applications.

---

# 7. Problem Decomposition

Problem decomposition means dividing a large problem into small, connected tasks.

Each task handles one specific part of the complete solution.

### Example: Student Result Calculator

Suppose the task is to calculate a student's total, average, and result.

Instead of writing everything together, decompose it into the following tasks:

1. Read the marks.
2. Validate the marks.
3. Calculate the total.
4. Calculate the average.
5. Determine the result according to the given rules.
6. Display the results.

The decomposition separates input handling, calculation, decision-making, and output.

### Another Example: Simple Calculator

A calculator can be divided into:

- Read the first operand.
- Read the operator.
- Read the second operand.
- Validate the operator.
- Perform the requested arithmetic operation.
- Handle division by zero.
- Display the result.

### Advantages of Decomposition

1. **Clarity:** Each task has a defined purpose.
2. **Simplicity:** A large task becomes easier to understand.
3. **Testing:** Individual parts can be checked independently.
4. **Reusability:** Common operations can be placed in functions.
5. **Maintenance:** Problems can be corrected with less disruption.
6. **Collaboration:** Different people can work on separate parts.

### Top-Down Approach

The top-down approach begins with the overall task and gradually divides it into smaller subtasks.

```text
Student Result
    |
    +-- Read Marks
    |
    +-- Validate Marks
    |
    +-- Calculate Total
    |
    +-- Calculate Average
    |
    +-- Determine Result
    |
    +-- Display Results
```

Start with the overall objective, then design each component.

---

# 8. Designing an Algorithm

An algorithm is a finite sequence of clear instructions used to solve a problem.

A well-designed algorithm should satisfy the following properties.

### 8.1 Input

An algorithm may accept zero or more inputs.

### 8.2 Output

It should produce at least one meaningful result.

### 8.3 Definiteness

Every step should have a clear interpretation.

### 8.4 Finiteness

The algorithm should terminate after a finite number of steps for the intended valid inputs.

### 8.5 Effectiveness

Each instruction should be practical to execute.

### 8.6 Correctness

The algorithm should produce the required output for inputs within its specified requirements.

### Example: Find the Largest of Three Numbers

**Problem:** Find the greatest among three integers, `a`, `b`, and `c`.

**Algorithm:**

1. Read `a`, `b`, and `c`.
2. Set `largest = a`.
3. If `b > largest`, update `largest = b`.
4. If `c > largest`, update `largest = c`.
5. Display `largest`.
6. Stop.

### Pseudocode

```text
START

    INPUT a, b, c
    largest = a

    IF b > largest THEN
        largest = b
    END IF

    IF c > largest THEN
        largest = c
    END IF

    OUTPUT largest

STOP
```

### Dry Run

Input:

```text
a = 15
b = 28
c = 20
```

| Step | Operation | `largest` |
|---:|---|---:|
| 1 | Initialize with `a` | 15 |
| 2 | Compare `b` with 15 | 28 |
| 3 | Compare `c` with 28 | 28 |
| 4 | Display result | 28 |

Expected output:

```text
Largest number = 28
```

The algorithm works with equal values as well. For example, if all three inputs are `10`, the largest remains `10`.

---

# 9. Converting an Algorithm into Pseudocode

Pseudocode helps us develop and verify logic before choosing a programming language.

It describes what needs to happen without requiring strict Python syntax.

### Example: Calculate Factorial

The factorial of a non-negative integer `n` is the product of all positive integers from `1` through `n`. By definition, `0! = 1`.

For example:

```text
4! = 4 * 3 * 2 * 1 = 24
```

### Algorithm

1. Read `n`.
2. Reject negative values.
3. Initialize `factorial = 1`.
4. Repeat from `1` through `n`.
5. Multiply the current factorial by the current number.
6. Display the result.

### Pseudocode

```text
START

    INPUT n

    IF n < 0 THEN
        OUTPUT "Invalid input"
    ELSE
        factorial = 1

        FOR number = 1 TO n
            factorial = factorial * number
        END FOR

        OUTPUT factorial
    END IF

STOP
```

### Python

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Invalid input")
else:
    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print(factorial)
```

### Why Start with Pseudocode?

Pseudocode allows you to concentrate on the algorithm rather than syntax.

It can be reviewed, discussed, and converted to different programming languages. It is especially helpful when solving unfamiliar problems.

---

# 10. Sequence, Selection, and Iteration

Most beginner programs use three fundamental control structures.

## 10.1 Sequence

Sequence means executing instructions in their specified order.

Example:

```python
a = 10
b = 20
total = a + b
print(total)
```

The program reads the assignments in order, calculates the total, and prints the result.

## 10.2 Selection

Selection means choosing between alternative actions based on a condition.

Example:

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

The selected branch depends on the condition that evaluates to `True`.

## 10.3 Iteration

Iteration means repeating instructions.

Example:

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

### Dry Run of the Loop

| Iteration | Number | Previous total | New total |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |
| 5 | 5 | 10 | 15 |

### When Should Each Structure Be Used?

| Structure | Use it when |
|---|---|
| Sequence | Operations must occur in order. |
| Selection | The solution depends on a condition. |
| Iteration | Operations must be repeated. |

Many real programming problems combine all three.

---

# 11. Dry Run and Trace Tables

A dry run means manually executing the steps of an algorithm without running the program.

A trace table records the values of variables during the execution process.

### Example: Find the Sum of Digits

Consider the number `352`.

Expected calculation:

```text
3 + 5 + 2 = 10
```

One way to calculate the digit sum is to repeatedly extract the final digit.

### Algorithm

1. Read the integer.
2. Work with its absolute value if negative inputs are allowed.
3. Initialize `total = 0`.
4. Extract the last digit using `% 10`.
5. Add the digit to `total`.
6. Remove the last digit using `// 10`.
7. Repeat until no digits remain.
8. Display the total.

### Pseudocode

```text
INPUT number
number = ABS(number)
total = 0

WHILE number > 0
    digit = number MOD 10
    total = total + digit
    number = number DIV 10
END WHILE

OUTPUT total
```

### Trace Table for 352

| Iteration | Number before | Extracted digit | Total after addition | Number after |
|---:|---:|---:|---:|---:|
| 1 | 352 | 2 | 2 | 35 |
| 2 | 35 | 5 | 7 | 3 |
| 3 | 3 | 3 | 10 | 0 |

Final output:

```text
Digit sum = 10
```

### Benefits of Dry Running

- Reveals incorrect variable initialization.
- Helps identify loop-boundary errors.
- Makes complex conditions easier to understand.
- Exposes missing updates.
- Builds confidence before implementation.
- Helps explain an algorithm during exams and interviews.

### Common Trace Table Columns

A trace table often includes:

- Step or iteration number.
- Input or current value.
- Important variable values.
- Condition result.
- Action performed.
- Output or final state.

Include only the columns relevant to the algorithm.

---

# 12. Input Validation and Edge Cases

Input validation checks that a value satisfies the requirements needed by the program.

An edge case is an unusual or boundary input that deserves specific testing.

## 12.1 Example: Discount Calculator

Suppose a discount calculator accepts an original price and a percentage.

Valid requirements for this example:

- The price must be non-negative.
- The discount percentage must be between `0` and `100`.

### Algorithm

1. Read the price.
2. Read the percentage.
3. Reject a negative price.
4. Reject a percentage outside the valid range.
5. Calculate the discount amount.
6. Subtract the discount from the original price.
7. Display the final price.

### Formula

```text
discount_amount = price * percentage / 100
final_price = price - discount_amount
```

### Example

For a price of `1000` and a discount of `20%`:

```text
Discount amount = 1000 * 20 / 100
Discount amount = 200

Final price = 1000 - 200
Final price = 800
```

## 12.2 Important Edge Cases

| Problem | Cases to consider |
|---|---|
| Factorial | `0`, `1`, negative input |
| Search | Empty list, absent target, duplicate values |
| Largest number | Negative values, duplicates, single value |
| Division | Zero denominator |
| Binary search | Empty list and unsorted input |
| String processing | Empty text, mixed case, spaces |
| Numeric algorithms | Zero and negative values |
| List processing | One element, all duplicates, empty list |

The correct handling depends on the problem's specification.

### Valid Input vs. Invalid Input

Do not assume all problems share the same rules. For example, addition generally allows negative numbers, while a factorial program commonly accepts only non-negative integers.

The algorithm should define its input requirements explicitly.

---

# 13. Translating Logic into Python

Once the algorithm has been designed and verified, translate each operation into Python.

### Common Translations

| Pseudocode | Python |
|---|---|
| `INPUT n` | `n = int(input(...))` |
| `OUTPUT result` | `print(result)` |
| `IF condition` | `if condition:` |
| `ELSE` | `else:` |
| `WHILE condition` | `while condition:` |
| `FOR each item` | `for item in collection:` |
| `total = total + value` | `total += value` |
| `number MOD 10` | `number % 10` |
| Integer division | `number // 10` |

### Example: Even or Odd

**Problem:** Determine whether a number is even or odd.

**Step 1 — Input:**

```python
number = int(input("Enter an integer: "))
```

**Step 2 — Apply the condition:**

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Step 3 — Test sample inputs:**

| Input | Remainder after division by 2 | Output |
|---:|---:|---|
| 8 | 0 | Even |
| 7 | 1 | Odd |
| 0 | 0 | Even |
| -4 | 0 | Even |

### Important Rule

Do not confuse a syntactically valid Python program with a correct algorithm. Code can run successfully and still produce incorrect results.

Always compare the implementation with the intended steps and test cases.

---

# 14. Functions and Modular Problem Solving

A function is a named, reusable block of code that performs a specific task.

Functions help divide a larger solution into smaller components.

### Example

```python
def calculate_area(length, width):
    return length * width


result = calculate_area(8, 4)
print(result)
```

Output:

```text
32
```

### Explanation

- `def` defines the function.
- `length` and `width` are parameters.
- `return` sends the calculated result back to the caller.
- `calculate_area(8, 4)` calls the function with two arguments.

### Benefits of Functions

1. Reduce unnecessary repetition.
2. Separate distinct responsibilities.
3. Improve readability.
4. Allow independent testing.
5. Make code easier to maintain.
6. Encourage reuse.

### Decomposing a Calculator Using Functions

A calculator might use separate functions for:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Input collection.
- Output display.

For smaller beginner programs, a single function may be sufficient. For larger programs, modular design can be more maintainable.

---

# 15. Testing and Debugging

Testing checks whether a program produces the expected result for selected inputs.

Debugging is the process of finding the cause of incorrect behavior and correcting it.

## 15.1 Types of Errors

### Syntax Error

An error caused by invalid Python syntax.

Example:

```python
if number > 0
    print("Positive")
```

The missing colon causes a syntax error.

### Runtime Error

An error that occurs while a program is executing.

Example:

```python
result = 10 / 0
```

This causes `ZeroDivisionError`.

### Logical Error

The program runs but produces the wrong result.

Example:

```python
average = total / 2
```

If `total` represents the sum of three marks, dividing by two is logically incorrect.

## 15.2 Testing Strategy

A useful testing sequence is:

1. Test a normal input.
2. Test the smallest valid input.
3. Test the largest or a boundary input when relevant.
4. Test zero and negative values if permitted.
5. Test invalid input.
6. Test an empty or minimal collection where relevant.
7. Compare actual output with expected output.

### Example Test Cases for Factorial

| Input | Expected output or behavior |
|---:|---|
| `0` | `1` |
| `1` | `1` |
| `5` | `120` |
| `-1` | Reject as a negative input |
| `abc` | Ask again for a valid integer in the supplied program |

### Debugging Questions

When a test fails, ask:

- Is the input being read correctly?
- Is a variable initialized to the correct value?
- Are the conditions correct?
- Does the loop stop at the right time?
- Are variables updated in the proper order?
- Is a special case missing?
- Does the implementation match the algorithm?

---

# 16. Time and Space Complexity

Complexity analysis estimates how an algorithm's resource requirements grow with the size of its input.

## 16.1 Time Complexity

Time complexity describes how the number of computational operations grows as the input size increases.

It does not directly give the exact number of seconds a program takes.

## 16.2 Space Complexity

Space complexity describes how the memory requirements grow with input size.

The analysis may consider auxiliary storage used by the algorithm, depending on the convention being applied.

## 16.3 Common Complexity Classes

| Complexity | Name | Common example |
|---|---|---|
| `O(1)` | Constant | Accessing a list item by index |
| `O(log n)` | Logarithmic | Binary search on sorted data |
| `O(n)` | Linear | Scanning a list once |
| `O(n log n)` | Linearithmic | Merge sort |
| `O(n²)` | Quadratic | Comparing every pair with nested loops |

These are common patterns rather than universal classifications for every implementation.

## 16.4 Example: Linear Search

In linear search, the algorithm examines elements until it finds a target or reaches the end.

- Best case: `O(1)` when the first element matches.
- Worst case: `O(n)` when the target is last or absent.
- Auxiliary space: `O(1)` for the iterative search itself.

## 16.5 Example: Binary Search

Binary search repeatedly divides a sorted search range approximately in half.

- Best case: `O(1)` when the middle element matches immediately.
- Worst case: `O(log n)` search time.
- Auxiliary space: `O(1)` for the iterative implementation.

**Important:** Binary search requires sorted input. It is not a correct general replacement for searching an unsorted list.

## 16.6 Example: Counting Nested-Loop Operations

Consider two independent loops, each performing `n` iterations:

```python
for i in range(n):
    for j in range(n):
        pass
```

The inner operation executes `n * n` times.

The resulting growth is quadratic, or `O(n²)`.

By contrast, a single loop performing `n` iterations generally has linear growth, or `O(n)`.

The example in this folder illustrates the operation counts `n` and `n²`; the exact runtime also depends on the programming environment and the operations being performed.

---

# 17. Detailed Explanation of the 12 Examples

The file `04_step_by_step_solution.py` contains an interactive examples menu. Each example displays a solution plan before demonstrating the corresponding logic.

## Example 1 — Problem-Solving Workflow

**Concept:** A repeatable process for designing a solution.

It demonstrates the sequence of understanding the problem, identifying inputs and outputs, planning the algorithm, checking it, implementing it, and testing it.

**Goal:** Establish a reliable method to use for future programming exercises.

## Example 2 — Input-Process-Output

**Concept:** Organizing a calculation around input, processing, and output.

The program reads two numbers, adds them, and displays the result.

**Goal:** Learn how to distinguish the information provided, the operation performed, and the final result.

## Example 3 — Decomposing an Average Calculation

**Concept:** Dividing a calculation into smaller tasks.

The program reads three marks, calculates their total, and divides that total by three.

**Goal:** Understand how a multi-step mathematical problem becomes a simple algorithm.

## Example 4 — Rectangle Area

**Concept:** Translating a formula into an algorithm with validation.

The program checks that the dimensions are not negative before calculating the area.

Formula:

```text
Area = length * width
```

**Goal:** Apply arithmetic, conditions, and input requirements.

## Example 5 — Input Validation

**Concept:** Using mutually exclusive branches to classify a value.

The program checks whether the number is positive, negative, or zero.

**Goal:** Understand how conditions control program flow.

## Example 6 — Dry Run of a Running Total

**Concept:** Tracking a variable across repeated operations.

The program calculates the sum from `1` through `n` and shows the updated total at each iteration.

**Goal:** Understand initialization, accumulation, and loop execution.

## Example 7 — Discount Calculation

**Concept:** Combining arithmetic with validation.

The program validates the original price and discount percentage, calculates the discount amount, and subtracts it from the price.

Formulas:

```text
Discount = Price * Percentage / 100

Final Price = Price - Discount
```

**Goal:** Apply the IPO model to a practical calculation.

## Example 8 — Leap-Year Decision

**Concept:** Designing ordered conditions.

The program checks divisibility by `400`, `100`, and `4` according to the leap-year rule.

**Goal:** Learn why the order of conditions matters.

## Example 9 — Count Vowels

**Concept:** Traversing a string and maintaining a counter.

The program converts characters to lowercase for comparison and counts occurrences of the vowels `a`, `e`, `i`, `o`, and `u`.

**Goal:** Practise loops, strings, conditional checks, and counters.

## Example 10 — Trace the Largest Number

**Concept:** Maintaining the largest value seen so far.

The program initializes the largest value using the first element and updates it whenever it encounters a greater number.

**Goal:** Learn the comparison-and-update pattern.

## Example 11 — Modular Calculator

**Concept:** Breaking a calculation into a sequence of input, operation selection, computation, and output.

The program supports addition, subtraction, multiplication, and division. It also prevents division by zero.

**Goal:** Practise branching and handling invalid operations.

## Example 12 — Estimate Algorithm Work

**Concept:** Comparing linear and quadratic iteration counts.

For an input size `n`, the program prints `n` for one loop and `n²` for nested loops of size `n`.

**Goal:** Build an introductory understanding of algorithm growth and complexity.

---

# 18. Detailed Explanation of the 12 Solved Problems

The solved-problems menu demonstrates how to turn a clearly defined algorithm into working Python code.

## Solved Problem 1 — Largest of Three Numbers

**Approach:** Keep a variable containing the largest value seen so far.

Steps:

1. Read three integers.
2. Start with the first integer as the largest.
3. Compare the second integer and update if necessary.
4. Compare the third integer and update if necessary.
5. Display the largest value.

**Concepts:** Comparisons, variables, `if` statements.

**Time complexity:** `O(1)` because the number of comparisons is fixed.

## Solved Problem 2 — Factorial

**Approach:** Repeated multiplication.

For example:

```text
5! = 5 * 4 * 3 * 2 * 1 = 120
```

The program starts with `factorial = 1` and multiplies it by each integer from `1` through `n`.

The code rejects negative integers. For `n = 0`, the loop performs no iterations, so the result remains `1`.

**Concepts:** Loops, accumulators, input validation.

**Time complexity:** `O(n)`.

## Solved Problem 3 — Prime-Number Check

**Approach:** Check for divisors.

A prime number is an integer greater than `1` with exactly two positive divisors: `1` and itself.

The algorithm rejects numbers smaller than `2`. It then checks possible divisors from `2` while the square of the divisor does not exceed the number.

If any divisor divides the number evenly, the number is not prime.

**Concepts:** Modulo, conditions, loops, early termination.

**Time complexity:** `O(√n)` for positive `n`, as the number of candidate divisors is bounded by the square root of `n`.

## Solved Problem 4 — Reverse the Digits

**Approach:** Extract and append digits.

For example:

```text
Input: 472
Output: 274
```

The program extracts the final digit using `% 10`, appends it to the reversed number, and removes the digit with integer division by `10`.

It handles the sign separately so that negative inputs retain their sign.

**Concepts:** Modulo, integer division, loops, arithmetic.

**Time complexity:** `O(d)`, where `d` is the number of digits.

## Solved Problem 5 — Numeric Palindrome

A numeric palindrome reads the same forward and backward.

Examples:

```text
121  -> Palindrome
1331 -> Palindrome
123  -> Not a palindrome
```

The solution reverses the digits and compares the result with the original value. Negative integers are rejected as palindromes by this program's stated convention.

**Concepts:** Digit manipulation, comparisons, loops.

**Time complexity:** `O(d)`.

## Solved Problem 6 — Greatest Common Divisor (GCD)

The GCD is the largest positive integer that divides both input integers, with the special convention that `gcd(0, 0)` is `0` in this implementation.

The program uses the Euclidean algorithm:

```text
WHILE b is not zero
    remainder = a MOD b
    a = b
    b = remainder

RETURN a
```

The values are converted to their absolute values before the algorithm runs.

**Concepts:** Modulo, tuple assignment, iterative algorithms.

**Time complexity:** `O(log(min(a, b)))` for positive inputs, with the zero-input cases handled separately by the loop.

## Solved Problem 7 — Least Common Multiple (LCM)

The LCM is the smallest positive common multiple of two non-zero integers.

For non-zero integers:

```text
LCM(a, b) = abs(a * b) / GCD(a, b)
```

The program uses integer division after calculating the GCD. If either input is zero, it returns `0`.

**Concepts:** Reusing an algorithm, arithmetic, special cases.

The Euclidean algorithm is logarithmic in the usual positive-input analysis; this problem also performs constant additional arithmetic operations.

## Solved Problem 8 — Second-Largest Distinct Number

The problem is to find the second-largest **distinct** value, not merely the second element after sorting.

Example:

```text
Input:  10 20 20 8 15
Output: 15
```

The solution removes duplicate values, sorts the distinct values in descending order, and selects the second value.

If fewer than two distinct values exist, it reports that the input is insufficient.

**Concepts:** Lists, sets, sorting, edge cases.

**Typical time complexity:** `O(n log n)` due to sorting, plus the work of creating the set.

## Solved Problem 9 — Linear Search

Linear search checks each element until it finds the target or reaches the end of the list.

Example:

```text
List:   [4, 8, 12, 16]
Target: 12
Index:  2
```

The program reports a zero-based index when a match is found. Otherwise, it reports that the target was not found.

**Concepts:** Iteration, comparison, list indexing, early termination.

**Time complexity:** Best case `O(1)`; worst case `O(n)`.

## Solved Problem 10 — Count Even and Odd Numbers

An integer is even if its remainder after division by `2` is zero. Otherwise, it is odd.

The solution maintains two counters and increments the appropriate one for each element.

Example:

```text
Input:  1 2 3 4 6
Even:   3
Odd:    2
```

**Concepts:** Modulo, loops, counters.

**Time complexity:** `O(n)`.

## Solved Problem 11 — Remove Duplicates While Preserving Order

The solution retains the first occurrence of each number and ignores later occurrences.

Example:

```text
Input:  3 5 3 7 5 9
Output: [3, 5, 7, 9]
```

A set tracks which values have already appeared. A separate list preserves the original order of first occurrences.

**Concepts:** Lists, sets, membership checks, order preservation.

**Typical time complexity:** `O(n)` on average for hash-set membership operations. Auxiliary storage grows with the number of distinct values.

## Solved Problem 12 — Binary Search

Binary search is a searching algorithm for sorted data.

The algorithm maintains a search interval, examines its middle element, and discards half of the remaining interval according to the comparison.

Example:

```text
Sorted list: [10, 20, 30, 40, 50]
Target:      40
Index:       3
```

The implementation checks that the input list is sorted in ascending order before searching.

**Concepts:** Search intervals, midpoint calculation, comparisons, loop conditions.

**Time complexity:** Worst case `O(log n)`. The iterative implementation uses `O(1)` auxiliary space.

---

# 19. Five Unsolved Practice Questions

Attempt these problems independently before searching for a solution.

For each question, first identify input and output, then write the algorithm, pseudocode, dry run, and Python implementation.

## Question 1 — Sum of Digits

**Problem:** Given an integer, calculate the sum of its digits.

Example:

```text
Input:  528
Output: 15
```

Because:

```text
5 + 2 + 8 = 15
```

**Hints:**

- Use `% 10` to obtain a final digit.
- Use `// 10` to remove the final digit.
- Repeat until the remaining number is zero.
- Decide how negative integers should be handled.

## Question 2 — Fibonacci Sequence

**Problem:** Read `n` and display the first `n` Fibonacci numbers, using the starting sequence `0, 1`.

Example:

```text
Input: 7
Output: 0 1 1 2 3 5 8
```

**Hints:**

- Track the previous two numbers.
- Generate the next value using their sum.
- Handle small values of `n`.
- Define how invalid negative input should be handled.

## Question 3 — Armstrong Number

**Problem:** Determine whether a non-negative integer is an Armstrong number.

For a number with `d` digits, add each digit raised to the power `d`. The number is an Armstrong number when the total equals the original number.

Example:

```text
153 = 1³ + 5³ + 3³
153 = 153
```

**Hints:**

- Count the digits.
- Extract each digit.
- Raise each digit to the required power.
- Add the values and compare the sum with the original number.

## Question 4 — Count Words in a Sentence

**Problem:** Count the words in a sentence while handling extra spaces sensibly.

Example:

```text
Input:  "Python is easy to learn"
Output: 5
```

Also test an empty sentence and a sentence containing multiple spaces.

**Hints:**

- Consider string methods such as `split()`.
- Decide whether punctuation affects word counting.
- Define the behavior for empty input.

## Question 5 — Find the Missing Number

**Problem:** A list contains distinct integers from `1` through `n`, but one number is missing. Find the missing number.

Example:

```text
n = 5
List = [1, 2, 4, 5]
Output = 3
```

**Hints:**

- Calculate the expected sum from `1` through `n`.
- Calculate the actual sum of the list.
- Subtract the actual sum from the expected sum.
- Verify the input assumptions.

---

# 20. Step-by-Step Problem-Solving Checklist

Use this checklist whenever you begin a new programming question.

### Understanding

- [ ] I have read the problem statement carefully.
- [ ] I know exactly what needs to be solved.
- [ ] I have identified the inputs.
- [ ] I have identified the expected output.
- [ ] I understand the restrictions and assumptions.

### Designing

- [ ] I have broken the task into smaller steps.
- [ ] I know which calculations are required.
- [ ] I know which conditions are required.
- [ ] I know whether a loop is required.
- [ ] I have written an algorithm or pseudocode.

### Verifying

- [ ] I have performed a dry run.
- [ ] I have checked the loop boundaries.
- [ ] I have verified important variable updates.
- [ ] I have tested at least one normal case.
- [ ] I have considered edge cases.

### Implementing

- [ ] I have written readable Python code.
- [ ] I have used suitable variable names.
- [ ] I have handled expected invalid inputs.
- [ ] I have tested the actual implementation.
- [ ] I have reviewed the result against the problem requirements.

### Reviewing

- [ ] I understand why the solution works.
- [ ] I can explain the algorithm.
- [ ] I have considered time complexity.
- [ ] I have considered auxiliary space when relevant.
- [ ] I have kept the solution as simple as reasonably possible.

---

# 21. Common Mistakes and Their Solutions

## Mistake 1: Writing Code Before Understanding the Problem

**Problem:** You may miss a condition or misunderstanding of the expected output.

**Solution:** Write down the goal, inputs, outputs, and constraints first.

## Mistake 2: Skipping Pseudocode

**Problem:** Coding without a plan often creates unnecessary conditions and tangled logic.

**Solution:** Write a short algorithm before implementation, especially for unfamiliar problems.

## Mistake 3: Incorrect Initialization

**Problem:** Starting an accumulator or maximum variable with an unsuitable value can produce incorrect results.

**Solution:** Choose initial values based on the problem. For a non-empty list's maximum, initializing from the first element is safer than always using zero because the list may contain only negative numbers.

## Mistake 4: Wrong Loop Boundaries

**Problem:** A loop may run one time too many or too few.

**Solution:** Dry-run the first and last iterations and understand the difference between inclusive mathematical ranges and Python's exclusive stopping value in `range()`.

## Mistake 5: Forgetting Special Cases

**Problem:** A solution that works for regular inputs may fail for zero, empty lists, negative numbers, or missing values.

**Solution:** List relevant edge cases before coding.

## Mistake 6: Incorrect Condition Order

**Problem:** More general conditions may prevent special conditions from being checked correctly.

**Solution:** Arrange branches according to the problem's rules. The leap-year example demonstrates why the divisibility rules must be applied in the correct order.

## Mistake 7: Ignoring Input Requirements

**Problem:** An algorithm that assumes a sorted list can produce incorrect results on unsorted data.

**Solution:** Validate required properties or state them clearly.

## Mistake 8: Testing Only One Example

**Problem:** Passing a single test does not establish that an algorithm handles all relevant cases.

**Solution:** Test ordinary, boundary, invalid, and unusual inputs.

## Mistake 9: Using Unclear Variable Names

**Problem:** Names such as `x1`, `x2`, and `z` can make a program difficult to understand when used without context.

**Solution:** Prefer meaningful names such as `total`, `largest`, `discount`, and `found_index`.

## Mistake 10: Memorizing Without Understanding

**Problem:** Memorized code may not transfer to a similar but different problem.

**Solution:** Explain every important step in your own words, then modify the inputs or requirements and solve the changed problem.

---

# 22. Best Practices for Writing Algorithms

1. Use simple, ordered steps.
2. Keep each step focused on one task.
3. Use meaningful variable names.
4. Make inputs and outputs explicit.
5. State assumptions and constraints.
6. Choose conditions that cover the relevant cases.
7. Ensure loops make progress toward termination.
8. Use functions when a task can be separated cleanly.
9. Dry-run the algorithm before implementation.
10. Test both typical and unusual inputs.
11. Avoid unnecessary operations.
12. Explain the reasoning behind the solution.

**For DSA practice:** Correctness comes first. Once you understand why the solution works, study whether it can be made more efficient.

---

# 23. Frequently Asked Questions

### Q1. What is a step-by-step solution?

It is a method of solving a problem by performing clearly defined operations in an appropriate order.

### Q2. Why should I design an algorithm before coding?

An algorithm helps you validate the logic independently of programming syntax. It can expose missing steps before you begin implementation.

### Q3. What is the difference between an algorithm and pseudocode?

An algorithm is the logical solution. Pseudocode is one way to represent that solution in a readable, language-independent format.

### Q4. What is a dry run?

A dry run is the manual tracing of an algorithm with sample data to observe variable updates and verify the expected result.

### Q5. What is problem decomposition?

It is the process of breaking a larger task into smaller subproblems.

### Q6. Why is input validation important?

Validation helps ensure that the program processes values that meet the problem's requirements and handles invalid inputs appropriately.

### Q7. What is debugging?

Debugging is the process of identifying, understanding, and correcting errors.

### Q8. Is a program correct simply because it runs?

No. A program may run successfully but still produce an incorrect answer. Test the output against the requirements.

### Q9. When should I use a loop?

Use a loop when an operation must be repeated, for example when processing a list or calculating a running total.

### Q10. When should I use a function?

Use a function when a task can be expressed as a reusable, logically separate unit or when separating responsibilities makes the program easier to maintain.

### Q11. What is the difference between linear search and binary search?

Linear search checks elements sequentially and can work on an unsorted list. Binary search repeatedly halves the search range and requires sorted data.

### Q12. How is complexity useful?

Complexity analysis helps compare algorithms by how their computational work and memory requirements grow with input size.

### Q13. How can I improve problem-solving skills?

Practise writing algorithms, performing dry runs, solving small problems independently, testing edge cases, and explaining your reasoning.

### Q14. What should I do when my solution fails a test?

Compare the actual output with the expected output. Check the conditions, loop boundaries, variable initialization, updates, and any unhandled edge cases.

### Q15. Is this topic useful for DSA?

Yes. DSA requires the same fundamentals: understanding a problem, choosing a strategy, implementing the algorithm, verifying correctness, and analysing efficiency.

---

# 24. How to Run the Python Program

Make sure Python 3 is installed and available in your terminal.

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\02-Problem-Solving\04_Step_By_Step_Solution\04_step_by_step_solution.py"
```

### Main Menu

The program displays the following options:

```text
============================================================
STEP-BY-STEP SOLUTION METHODS
============================================================
1. Explore 12 examples
2. Practice 12 solved problems
3. View 5 unsolved questions
4. View solution checklist
0. Exit
Choose an option:
```

### Menu Instructions

- Enter `1` to explore the examples.
- Enter `2` to practise the solved problems.
- Enter `3` to view the unsolved questions.
- Enter `4` to review the solution checklist.
- Enter `0` to exit.
- Use the displayed submenu numbers to choose individual examples or solved problems.
- Press Enter when prompted to return to the previous menu.

The program validates integer menu choices and retries if the input is not a valid integer.

---

# 25. Expected Folder Structure

Your folder should contain these two files:

```text
04_Step_By_Step_Solution/
│
├── 04_step_by_step_solution.py
│
└── README.md
```

### `04_step_by_step_solution.py`

Contains:

- Input helper functions.
- Twelve interactive examples.
- Twelve solved programming problems.
- Five unsolved practice questions.
- A step-by-step solution checklist.
- Interactive menus for navigation.

### `README.md`

Contains:

- Topic theory and definitions.
- Algorithms and pseudocode.
- IPO and decomposition explanations.
- Dry-run examples and trace tables.
- Validation, testing, and debugging guidance.
- Complexity analysis.
- Explanations of the program's examples and solved problems.
- Practice exercises.
- Instructions for running the Python file.

---

# 26. Final Revision Notes

Before moving to the next topic, revise these essential concepts:

- A problem statement defines what needs to be solved.
- Inputs are the data supplied to a program.
- Processing describes the operations performed.
- Outputs are the results produced.
- An algorithm defines an ordered, finite set of instructions.
- Pseudocode expresses algorithmic logic in readable steps.
- Problem decomposition breaks a complex task into smaller units.
- Sequence executes operations in order.
- Selection chooses an action based on a condition.
- Iteration repeats instructions.
- A dry run helps trace an algorithm manually.
- A trace table records changes in important variables.
- Input validation checks whether values meet the problem's requirements.
- Testing verifies program behavior against expected results.
- Debugging identifies and fixes errors.
- Complexity analysis studies how resource usage grows as the input size increases.

## Completion Goal

By the end of this topic, you should be able to take a beginner programming problem, explain its input and output, write a numbered algorithm, express it in pseudocode, dry-run it, implement it in Python, test it, and explain why the solution works.

**Next topic:** Practice Problems — apply these problem-solving methods to independent exercises and build confidence in algorithm design.