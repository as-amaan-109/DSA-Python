# Practice Flowcharts — Python

Welcome to **Practice Flowcharts**, the final topic in the Flowcharts section of Week 1: Programming Fundamentals in the DSA-Python repository.

This topic combines sequence, selection, and iteration to solve complete programming problems. The goal is to move from understanding a problem to designing a flowchart, testing the logic, and implementing a working Python solution.

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [The Three Fundamental Control Structures](#the-three-fundamental-control-structures)
4. [Problem-Solving Workflow](#problem-solving-workflow)
5. [Worked Example: Sum from 1 to N](#worked-example-sum-from-1-to-n)
6. [Worked Example: Prime Number](#worked-example-prime-number)
7. [Worked Example: Linear Search](#worked-example-linear-search)
8. [Dry Runs and Test Cases](#dry-runs-and-test-cases)
9. [Algorithm Analysis](#algorithm-analysis)
10. [Folder Structure](#folder-structure)
11. [How to Run the Program](#how-to-run-the-program)
12. [Practice Questions](#practice-questions)
13. [Common Mistakes](#common-mistakes)
14. [Interview Questions](#interview-questions)
15. [Learning Checklist](#learning-checklist)
16. [Next Learning Stage](#next-learning-stage)

---

## About This Topic

Real programming problems often require more than a single calculation. A solution may need to read multiple inputs, check conditions, repeat operations, and display a final result.

This topic combines the concepts studied in:

- Algorithm Basics.
- Algorithm Steps.
- Algorithm Examples.
- Algorithm Characteristics.
- Algorithm Analysis.
- Flowchart Basics.
- Input/Output Flowcharts.
- Decision Flowcharts.
- Loop Flowcharts.

The purpose is to practise using these concepts together rather than treating them as separate ideas.

## Learning Objectives

After completing this topic, you should be able to:

- Break down a problem into smaller steps.
- Identify required inputs, processing, decisions, and outputs.
- Combine sequence, selection, and iteration.
- Create flowcharts for complete beginner-level algorithms.
- Translate flowcharts into pseudocode.
- Implement algorithms in Python.
- Dry-run a program using a trace table.
- Test ordinary, boundary, and invalid inputs.
- Explain basic time and auxiliary-space complexity.
- Solve problems independently instead of relying entirely on worked examples.

---

## The Three Fundamental Control Structures

Most introductory flowcharts use three fundamental control structures.

### 1. Sequence

Sequence means performing operations in a defined order.

Example:

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

Sequence is suitable when the next operation follows directly from the previous one.

### 2. Selection

Selection chooses a path based on a condition.

Example:

```text
       < N % 2 == 0? >
          /       \
        Yes        No
         |          |
       [Even]      [Odd]
```

In Python, selection is commonly implemented with `if`, `elif`, and `else`.

### 3. Iteration

Iteration repeats a group of operations.

Example:

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

In Python, iteration is commonly implemented with `for` and `while`.

### Combining all three structures

A typical problem may:

1. Read data using sequence.
2. Repeat a calculation using a loop.
3. Select a result using a condition.
4. Display the output.

Learning to combine these structures is a useful foundation for DSA.

---

## Problem-Solving Workflow

Use the following process for every practice problem.

### Step 1: Understand the problem

Read the complete problem statement and identify exactly what must be calculated or determined.

### Step 2: Identify the inputs

List every value required to solve the problem.

Example: To calculate an average, the program needs the input values and their count.

### Step 3: Define the output

Specify the result or message that the program must produce.

### Step 4: Design the logic

Determine whether the solution requires calculations, conditions, loops, or a combination of them.

### Step 5: Write the algorithm

Describe the steps in order using clear language.

### Step 6: Draw the flowchart

Choose appropriate symbols and connect them with arrows. Clearly represent every condition and loop exit.

### Step 7: Write pseudocode

Use language-independent instructions to make the logic easier to review.

### Step 8: Perform a dry run

Trace the algorithm manually using sample values.

### Step 9: Write Python code

Implement the verified logic using suitable variables, conditions, and loops.

### Step 10: Test and analyze

Test normal inputs, boundary cases, and invalid values where applicable. Estimate time and auxiliary-space complexity.

---

## Worked Example: Sum from 1 to N

**Problem:** Read a positive integer N and calculate the sum of all integers from 1 through N.

### Algorithm

1. Start.
2. Read N.
3. If N is less than 1, display an error.
4. Initialize `total = 0`.
5. Repeat for numbers from 1 through N.
6. Add each number to `total`.
7. Display the final total.
8. End.

### Pseudocode

```text
START
INPUT N

IF N < 1
    OUTPUT "N must be positive"
ELSE
    total = 0

    FOR number = 1 TO N
        total = total + number
    END FOR

    OUTPUT total
END IF

END
```

### Flowchart

```text
        ( START )
            |
            v
        / Input N /
            |
            v
         < N >= 1? >
          /      \
        No        Yes
         |          |
         v          v
   [Display error] [total = 0]
                      |
                      v
               [number = 1]
                      |
                      v
               < number <= N? >
                  /       \
                Yes        No
                 |          |
                 v          v
         [total = total + n] / Display total /
                 |                  |
                 v                  v
          [number = n + 1]       ( END )
                 |
                 └────> Return to condition
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

### Dry run for N = 5

| Iteration | Number | Total before | Total after |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |
| 5 | 5 | 10 | 15 |

Expected output:

```text
Enter a positive integer: 5
Sum: 15
```

### Complexity

- Time: `O(N)` for the loop-based algorithm.
- Auxiliary space: `O(1)` because the algorithm uses a fixed number of additional variables.

---

## Worked Example: Prime Number

**Problem:** Determine whether an integer is prime.

A prime number is an integer greater than 1 that has exactly two positive divisors: 1 and itself.

### Algorithm

1. Read N.
2. If N is less than 2, report that it is not prime.
3. Start checking divisors from 2.
4. Check divisors up to the integer square root of N.
5. If any divisor divides N evenly, N is not prime.
6. If no divisor is found, N is prime.
7. Display the result.

### Pseudocode

```text
START
INPUT N

IF N < 2
    OUTPUT "Not prime"
ELSE
    divisor = 2
    is_prime = TRUE

    WHILE divisor * divisor <= N
        IF N MOD divisor = 0
            is_prime = FALSE
            BREAK
        END IF

        divisor = divisor + 1
    END WHILE

    IF is_prime
        OUTPUT "Prime"
    ELSE
        OUTPUT "Not prime"
    END IF
END IF

END
```

### Python implementation

```python
import math

n = int(input("Enter an integer: "))

if n < 2:
    print("Not prime")
else:
    is_prime = True

    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")
```

### Dry run for N = 17

- Check divisors 2, 3, and 4.
- None divides 17 evenly.
- No divisor is found up to the integer square root of 17.
- The result is `Prime`.

For N = 21, the divisor 3 is found, so the result is `Not prime`.

### Complexity

For this implementation:

- Worst-case time: `O(√N)` divisibility checks.
- Auxiliary space: `O(1)`.

---

## Worked Example: Linear Search

**Problem:** Find the position of a target value in a list by checking elements one by one.

### Algorithm

1. Read the list size and list values.
2. Read the target value.
3. Start from the first element.
4. Compare each element with the target.
5. If they match, record the position and stop searching.
6. If the end is reached without a match, report that the target was not found.

### Pseudocode

```text
START
INPUT N
INPUT N list values
INPUT TARGET

index = 0
found = FALSE

WHILE index < N
    IF LIST[index] = TARGET
        found = TRUE
        BREAK
    END IF

    index = index + 1
END WHILE

IF found
    OUTPUT index
ELSE
    OUTPUT "Not found"
END IF

END
```

### Python implementation

```python
numbers = [12, 7, 25, 4, 18]
target = int(input("Enter the value to search for: "))

found_index = -1

for index, value in enumerate(numbers):
    if value == target:
        found_index = index
        break

if found_index == -1:
    print("Value not found.")
else:
    print("Zero-based index:", found_index)
    print("Position:", found_index + 1)
```

### Dry run for target = 25

| Index | Value | Match? | Action |
|---:|---:|---|---|
| 0 | 12 | No | Continue |
| 1 | 7 | No | Continue |
| 2 | 25 | Yes | Stop and report position |

The target is at zero-based index 2, which is the third position in the list.

### Complexity

- Best-case time: `O(1)` when the first item matches.
- Worst-case time: `O(N)` when the last item matches or the target is absent.
- Auxiliary space: `O(1)` for the search itself, excluding the input list.

---

## Dry Runs and Test Cases

A dry run helps verify a solution before relying on the program output.

For every problem, test the normal path and any alternate paths created by a decision.

| Problem | Useful test cases |
|---|---|
| Even or odd | Positive even, positive odd, zero, negative integer |
| Largest of three | First largest, second largest, third largest, equal values |
| Sum from 1 to N | N = 1, N = 5, N = 0 |
| Factorial | N = 0, N = 1, N = 5, negative input |
| Prime check | N = 0, 1, 2, 9, 17 |
| Palindrome | 121, 123, 0, negative input |
| Linear search | First item, last item, missing target, repeated target |

### What should you check?

- Are variables initialized correctly?
- Does each condition represent the actual requirement?
- Does every loop have a valid stopping condition?
- Does the algorithm work for boundary inputs?
- Is the output format understandable?
- Does the code match the flowchart?

---

## Algorithm Analysis

Complexity describes how resource usage grows with input size.

| Problem | Typical time complexity | Typical auxiliary space |
|---|---:|---:|
| Add two numbers | `O(1)` | `O(1)` |
| Largest of three numbers | `O(1)` | `O(1)` |
| Sum from 1 to N using a loop | `O(N)` | `O(1)` |
| Factorial using a loop | `O(N)` multiplications | `O(1)` |
| Prime check using divisors up to √N | `O(√N)` | `O(1)` |
| Fibonacci: generate N terms iteratively | `O(N)` arithmetic steps | `O(1)` if streaming; `O(N)` if storing all terms |
| Linear search | `O(N)` worst case | `O(1)` excluding input |
| Remove duplicates using repeated list membership checks | Up to `O(N²)` | `O(N)` for the output list |

These are standard introductory analyses under a simplified operation-count model. For very large integer values, arithmetic operations may themselves require more work.

---

## Folder Structure

```text
05_Practice_FlowChart/
│
├── README.md
└── 05_practice_flowcharts.py
```

The Python file includes runnable examples, solved exercises, and unsolved practice questions. This README explains the algorithms, flowchart design process, dry runs, and complexity.

---

## How to Run the Program

Open PowerShell in the root directory of your `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\05_Practice_FlowChart\05_practice_flowcharts.py"
```

The interactive menu offers:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Select an option and follow the prompts. Choose `0` inside a sub-menu to return to the main menu.

If the `python` command is not recognized, check your Python installation. On Windows, the `py` command may be available instead.

---

## Practice Questions

The Python file contains 12 examples, 12 solved questions, and 5 unsolved questions.

### 12 Examples

1. Add two numbers.
2. Check even or odd.
3. Find the largest of three numbers.
4. Calculate the sum from 1 to N.
5. Display a multiplication table.
6. Calculate factorial.
7. Check for a prime number.
8. Generate Fibonacci terms.
9. Reverse an integer.
10. Check whether a number is a palindrome.
11. Count vowels in a text string.
12. Calculate marks, percentage, and an example grade.

### 12 Solved Questions

1. Sum of digits.
2. GCD using Euclid's algorithm.
3. LCM.
4. Minimum of N numbers.
5. Maximum of N numbers.
6. Count even and odd values.
7. Find the second-largest distinct value.
8. Check an Armstrong number.
9. Check a leap year.
10. Sum even numbers from 1 to N.
11. Linear search.
12. Remove duplicates while preserving first-occurrence order.

### 5 Unsolved Questions

1. Print all prime numbers between two bounds.
2. Convert a non-negative decimal integer to binary without using `bin()`.
3. Determine whether a number is a perfect number.
4. Find the longest run of identical adjacent values in a list.
5. Create a menu-driven calculator that repeats until the user selects Exit.

### Recommended method

For every unsolved question:

1. Write the problem in your own words.
2. Identify the inputs and outputs.
3. Design the algorithm.
4. Draw the flowchart.
5. Write pseudocode.
6. Dry-run the solution.
7. Implement the program in Python.
8. Test edge cases.
9. Explain its complexity.

---

## Common Mistakes

- Starting to code without understanding the problem.
- Missing an input or output step in the flowchart.
- Writing decision branches without clear labels.
- Forgetting loop initialization or update.
- Writing a loop condition that never becomes false.
- Failing to consider zero or negative values.
- Confusing a zero-based index with a one-based position.
- Checking only one test case.
- Using repeated operations when a simpler solution exists.
- Claiming a complexity without examining the actual implementation.
- Copying a solution without being able to explain it.

---

## Interview Questions

**1. What is a flowchart?**

A flowchart is a graphical representation of the steps and control flow of an algorithm.

**2. What are the three fundamental control structures?**

Sequence, selection, and iteration.

**3. Why do flowcharts use a decision diamond?**

It represents a condition that determines which path the algorithm follows.

**4. What is a dry run?**

A dry run manually traces the algorithm with sample input values to check its logic.

**5. What is a loop?**

A loop repeats a group of instructions according to a range or condition.

**6. What is an infinite loop?**

An infinite loop continues without reaching its intended exit condition or another stopping mechanism.

**7. What is linear search?**

Linear search checks elements one by one until the target is found or the list ends.

**8. What is a prime number?**

A prime number is an integer greater than 1 with exactly two positive divisors.

**9. What is the difference between an algorithm and a flowchart?**

An algorithm describes solution steps, while a flowchart represents those steps visually.

**10. Why should boundary values be tested?**

They help reveal errors in conditions, ranges, and stopping rules.

**11. What is time complexity?**

Time complexity describes how an algorithm's operation count grows with input size.

**12. Why is pseudocode useful?**

Pseudocode expresses solution logic without requiring the exact syntax of a programming language.

---

## Learning Checklist

- [ ] I understand sequence, selection, and iteration.
- [ ] I can identify inputs, processes, and outputs.
- [ ] I can draw a flowchart for a simple problem.
- [ ] I can represent conditions and branches clearly.
- [ ] I can represent a loop with a valid exit path.
- [ ] I can write pseudocode from a flowchart.
- [ ] I can implement the solution in Python.
- [ ] I can manually dry-run my algorithm.
- [ ] I can test normal, boundary, and invalid inputs.
- [ ] I understand basic time and auxiliary-space complexity.
- [ ] I have run all examples.
- [ ] I have reviewed all solved questions.
- [ ] I have independently attempted all five unsolved questions.

---

## Next Learning Stage

After completing Practice Flowcharts, proceed to **Pseudocode and Problem-Solving**.

The next stage focuses on writing language-independent steps, decomposing larger problems, identifying patterns, and developing structured solutions before implementing them in Python.
