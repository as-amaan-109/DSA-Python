# Loop Flowcharts — Python

Welcome to **Loop Flowcharts**, part of Week 1: Programming Fundamentals in the DSA-Python repository.

This topic explains how flowcharts represent repetition, loop conditions, loop bodies, updates, and termination. You will practise converting loop-based algorithms into Python using `for` and `while` loops.

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is a Loop?](#what-is-a-loop)
4. [Loop Flowchart Structure](#loop-flowchart-structure)
5. [For Loop and While Loop](#for-loop-and-while-loop)
6. [Worked Example: Sum from 1 to N](#worked-example-sum-from-1-to-n)
7. [Worked Example: Factorial](#worked-example-factorial)
8. [Worked Example: Count Digits](#worked-example-count-digits)
9. [Nested Loops](#nested-loops)
10. [Loop Control Statements](#loop-control-statements)
11. [Dry Runs and Testing](#dry-runs-and-testing)
12. [Infinite Loops and Termination](#infinite-loops-and-termination)
13. [Time and Space Complexity](#time-and-space-complexity)
14. [Folder Structure](#folder-structure)
15. [How to Run the Program](#how-to-run-the-program)
16. [Practice Questions](#practice-questions)
17. [Common Mistakes](#common-mistakes)
18. [Interview Questions](#interview-questions)
19. [Learning Checklist](#learning-checklist)

---

## About This Topic

A **loop** repeats a set of instructions. Instead of writing the same statement many times, a loop allows a program to execute those instructions repeatedly.

For example, to display the numbers from 1 to 5, a loop can repeat the display operation while advancing the number.

Loops are commonly used for:

- Counting and summation.
- Multiplication tables.
- Factorial calculations.
- Processing collections of values.
- Searching for a value.
- Counting digits.
- Generating sequences.
- Repeating input until a condition is satisfied.
- Processing patterns using nested loops.

A loop flowchart shows how the program enters the loop, checks its condition, performs repeated operations, updates relevant values, and eventually exits.

## Learning Objectives

After completing this topic, you should be able to:

- Explain iteration and repetition.
- Identify the condition used to continue or exit a loop.
- Draw a flowchart for a `for` loop.
- Draw a flowchart for a `while` loop.
- Distinguish loop initialization, condition, body, and update.
- Use loops for counting, summation, and multiplication tables.
- Use nested loops for simple patterns.
- Understand `break` and `continue`.
- Identify the causes of infinite loops.
- Perform a dry run with a loop trace table.
- Estimate basic time and auxiliary-space complexity.

---

## What Is a Loop?

A loop repeatedly executes instructions according to a defined rule.

A loop normally contains four important elements:

1. **Initialization:** Set the starting value or state.
2. **Condition:** Decide whether another iteration should execute.
3. **Loop body:** Perform the required operations.
4. **Update:** Change the loop variable or state so that the loop can progress.

The exact arrangement depends on the loop type. A Python `for` loop gets its next value from an iterable, while a `while` loop checks a Boolean condition before every iteration.

---

## Loop Flowchart Structure

A loop flowchart commonly uses a decision diamond to check the loop condition.

```text
          ( START )
              |
              v
       [ Initialize ]
              |
              v
       < Condition? >
          /       \
        Yes        No
         |          |
         v          v
    [ Loop Body ]  [ Exit ]
         |
         v
      [ Update ]
         |
         └──────────> Return to Condition
```

### How the flow works

1. Initialize the required variables.
2. Evaluate the condition.
3. If the condition is true, execute the loop body.
4. Update the relevant values.
5. Return to the condition.
6. If the condition is false, follow the exit path.

**Important:** The condition must eventually become false, unless the loop is intentionally controlled using a statement such as `break`.

---

## For Loop and While Loop

### 1. For loop

A `for` loop is useful when iterating over a sequence or a known range of values.

Python example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

The `range(1, 6)` expression produces values from 1 through 5. Its stopping value, 6, is excluded.

Conceptual flowchart:

```text
       [ Start N at 1 ]
               |
               v
          < N <= 5? >
            /      \
          Yes       No
           |         |
           v         v
      [Display N]  [Exit]
           |
           v
       [N = N + 1]
           |
           └────> Return to condition
```

### 2. While loop

A `while` loop repeats as long as its condition is true.

Python example:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
5
```

The loop condition is evaluated before each iteration.

### Difference between `for` and `while`

| Feature | `for` loop | `while` loop |
|---|---|---|
| Common use | Iterating through a range or iterable | Repeating while a condition remains true |
| Value progression | Usually supplied by the iterable | Often updated inside the loop |
| Condition | Determined by whether the iterable has another value | Evaluated explicitly before each iteration |
| Common risk | Incorrect range limits | Forgetting to update a condition-related variable |
| Example | Print numbers from 1 to N | Repeat input until a valid value is entered |

Both loop types can implement many of the same algorithms.

---

## Worked Example: Sum from 1 to N

**Problem:** Read a positive integer `N` and calculate the sum of all integers from 1 through N.

### Algorithm

1. Start.
2. Read N.
3. Check that N is positive.
4. Set `total = 0` and `number = 1`.
5. While `number <= N`, add `number` to `total`.
6. Increase `number` by 1.
7. Repeat the condition check.
8. Display the total.
9. End.

### Pseudocode

```text
START
INPUT N

IF N < 1
    OUTPUT "Invalid input"
ELSE
    total = 0
    number = 1

    WHILE number <= N
        total = total + number
        number = number + 1
    END WHILE

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
             /       \
           No         Yes
           |            |
           v            v
      [Display error] [total = 0]
                        |
                   [number = 1]
                        |
                        v
                 < number <= N? >
                    /        \
                  Yes         No
                   |           |
                   v           v
          [total = total + n] [Display total]
                   |           |
                   v           v
             [number = n + 1] ( END )
                   |
                   └────> Return to condition
```

### Python implementation

```python
n = int(input("Enter a positive integer: "))

if n < 1:
    print("Enter a number greater than zero.")
else:
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum:", total)
```

### Dry run for N = 4

| Iteration | Number | Total before | Total after |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

After the fourth iteration, the next value would be 5. The condition `number <= 4` is false, so the loop stops.

Expected output:

```text
Enter a positive integer: 4
Sum: 10
```

### Complexity

For the loop-based solution:

- Time: `O(N)`, because the loop performs N iterations.
- Auxiliary space: `O(1)`, because a fixed number of variables is used.

A direct formula can also calculate this sum in constant time under the usual fixed-size arithmetic model:

`N × (N + 1) / 2`

The loop version is useful for learning iteration and dry-run tracing.

---

## Worked Example: Factorial

**Problem:** Calculate the factorial of a non-negative integer N.

Factorial is defined as:

- `0! = 1`
- `1! = 1`
- `N! = 1 × 2 × 3 × ... × N` for positive integers N.

### Algorithm

1. Read N.
2. Reject negative values.
3. Initialize `factorial = 1`.
4. Multiply the running result by every integer from 1 through N.
5. Display the result.

### Pseudocode

```text
START
INPUT N

IF N < 0
    OUTPUT "Factorial is not defined"
ELSE
    factorial = 1

    FOR number = 1 TO N
        factorial = factorial * number
    END FOR

    OUTPUT factorial
END IF

END
```

### Python implementation

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print("Factorial:", factorial)
```

### Dry run for N = 5

| Iteration | Number | Factorial before | Factorial after |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 6 | 24 |
| 5 | 5 | 24 | 120 |

Expected result:

`5! = 120`

### Complexity

- Time: `O(N)` multiplications.
- Auxiliary space: `O(1)` additional variables under the usual analysis.

Python integers can grow to contain many digits, so actual arithmetic cost increases for very large values.

---

## Worked Example: Count Digits

**Problem:** Count how many decimal digits an integer contains.

For example, `5832` has four digits. The sign is not counted as a digit, and zero has one digit.

### Algorithm

1. Read the integer.
2. Use its absolute value.
3. If the value is zero, the digit count is one.
4. Otherwise, repeatedly divide the value by 10 using integer division.
5. Increase the counter for every digit removed.
6. Display the count.

### Python implementation

```python
number = int(input("Enter an integer: "))
temp = abs(number)

if temp == 0:
    digit_count = 1
else:
    digit_count = 0

    while temp > 0:
        temp //= 10
        digit_count += 1

print("Number of digits:", digit_count)
```

### Dry run for 5832

| Iteration | Value before | Value after `// 10` | Counter |
|---:|---:|---:|---:|
| 1 | 5832 | 583 | 1 |
| 2 | 583 | 58 | 2 |
| 3 | 58 | 5 | 3 |
| 4 | 5 | 0 | 4 |

The loop stops when the value becomes zero. The output is `4`.

---

## Nested Loops

A nested loop is a loop inside another loop. It is often used for patterns, grids, tables, and pairwise comparisons.

Example: display a triangle of stars.

```python
rows = 4

for row in range(1, rows + 1):
    for _ in range(row):
        print("*", end="")
    print()
```

Output:

```text
*
**
***
****
```

### How it works

- The outer loop controls the row number.
- The inner loop prints the stars for the current row.
- The final `print()` moves to the next line.

For N rows, the inner loop executes 1 + 2 + ... + N times. Therefore, this particular pattern uses `O(N²)` print operations in total, while the outer and inner loop counters require `O(1)` additional variables under the usual auxiliary-space convention.

---

## Loop Control Statements

### 1. `break`

`break` exits the nearest enclosing loop immediately.

Example:

```python
for number in range(1, 11):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

The loop exits when `number == 5`.

### 2. `continue`

`continue` skips the remaining statements of the current iteration and proceeds to the next iteration.

Example:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

The value 3 is skipped.

### 3. Sentinel-controlled loops

A sentinel value is a special input that signals the end of repeated input.

Example:

```python
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Total:", total)
```

Here, entering zero ends the loop. Zero is the stopping signal and is not added to the total.

---

## Dry Runs and Testing

A dry run manually traces the loop variables, conditions, and results for each iteration.

For every loop algorithm, check:

1. The initial variable values.
2. The first condition check.
3. The loop body.
4. The variable update.
5. The next condition check.
6. The exact exit condition.

### Useful test cases

| Problem | Values worth testing |
|---|---|
| Sum from 1 to N | `N = 1`, `N = 5`, `N = 0` |
| Factorial | `N = 0`, `N = 1`, `N = 5`, negative input |
| Digit count | `0`, `7`, `5832`, `-42` |
| Countdown | Starting value `0`, `3`, negative input |
| Prime check | `-1`, `0`, `1`, `2`, `9`, `17` |
| Input validation loop | A negative number, zero, then a positive number |

Testing small inputs often makes errors in loop initialization, update logic, and stopping conditions much easier to find.

---

## Infinite Loops and Termination

An infinite loop continues without reaching its intended stopping condition.

Example of an accidental infinite loop:

```python
number = 1

while number <= 5:
    print(number)
    # Missing number += 1
```

The value remains 1, so the condition stays true.

Correct version:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### How to prevent infinite loops

- Initialize variables correctly.
- Ensure the condition reflects the intended range.
- Update the variable that affects the condition.
- Check whether the variable moves toward the stopping condition.
- Test a small input and count the expected iterations.
- In sentinel-controlled loops, ensure there is a way to enter the sentinel value.

Not every loop must terminate on its own; some programs are designed to run until an external event occurs. In beginner algorithms, however, every loop should have a clearly understood exit rule.

---

## Time and Space Complexity

The complexity of a loop depends on how many times it executes and how much work its body performs.

| Pattern | Typical time complexity |
|---|---:|
| Fixed number of iterations | `O(1)` with respect to a separate input size |
| One loop over N items | `O(N)` |
| Two full nested loops over N items | `O(N²)` |
| Repeatedly halve a value | `O(log N)` |
| N iterations with constant work each | `O(N)` |
| Pattern printing with 1 + 2 + ... + N outputs | `O(N²)` |

For auxiliary space:

- A running sum with a fixed number of variables generally uses `O(1)` auxiliary space.
- Building a list of N results generally requires `O(N)` additional space.
- The space required by a nested loop is not automatically `O(N²)`; it depends on what data the program stores.

Always analyze the body of the loop and the storage used by the complete algorithm.

---

## Folder Structure

```text
04_Loop_FlowChart/
│
├── README.md
└── 04_loop_flowchart.py
```

The Python file contains runnable examples and solved exercises. The README covers loop theory, flowchart logic, pseudocode, dry runs, complexity, and independent practice.

---

## How to Run the Program

Open PowerShell in the root directory of your `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Flowcharts\04_Loop_FlowChart\04_loop_flowchart.py"
```

The interactive menu offers:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Select an option and follow the prompts. Use `0` inside a sub-menu to return to the main menu.

If `python` is not recognized, check your Python installation. On Windows, the `py` command may be available instead.

---

## Practice Questions

The Python program provides 12 examples, 12 solved practice questions, and 5 unsolved questions.

### 12 Examples

1. Print numbers from 1 to N.
2. Display a multiplication table.
3. Calculate the sum from 1 to N.
4. Calculate factorial.
5. Display a countdown.
6. Display even numbers.
7. Count digits.
8. Reverse an integer.
9. Generate Fibonacci terms.
10. Calculate a sum until zero is entered.
11. Find the first multiple of 7 in a range.
12. Print a star triangle using nested loops.

### 12 Solved Questions

1. Sum of even numbers.
2. Product from 1 to N.
3. Count even and odd values.
4. Prime-number check.
5. GCD using Euclid's algorithm.
6. LCM.
7. Fibonacci terms and their sum.
8. Palindrome-number check.
9. Minimum of N numbers.
10. Maximum of N numbers.
11. Validate input until a positive value is entered.
12. Armstrong-number check.

### 5 Unsolved Questions

1. Print all prime numbers between two bounds.
2. Display the first N Armstrong numbers.
3. Convert a non-negative decimal integer to binary without using `bin()`.
4. Determine whether a number is a perfect number.
5. Generate the Collatz sequence until it reaches 1.

For every unsolved question:

1. Identify the initial values and loop condition.
2. Write the algorithm and pseudocode.
3. Draw the flowchart, including the exit path.
4. Perform a dry run.
5. Implement the Python code.
6. Test boundary cases.
7. State the time and auxiliary-space complexity.

---

## Common Mistakes

- Forgetting to initialize a counter or accumulator.
- Using the wrong `range()` stopping value.
- Forgetting that the stop value of `range()` is excluded.
- Forgetting to update a `while` loop variable.
- Using the wrong condition for continuing a loop.
- Accidentally skipping the first or last value.
- Misplacing an update statement.
- Using `break` when the loop should continue.
- Using `continue` without understanding which statements get skipped.
- Forgetting the special case of zero in digit-based problems.
- Assuming every nested loop requires quadratic space.
- Testing only one iteration instead of tracing the full loop.

---

## Interview Questions

**1. What is a loop?**

A loop repeats a set of instructions according to a range, sequence, or condition.

**2. What is iteration?**

Iteration means executing a loop's body repeatedly.

**3. What is the difference between a `for` loop and a `while` loop?**

A `for` loop commonly iterates over a range or iterable, while a `while` loop repeats while its condition is true.

**4. What is a loop condition?**

A Boolean expression that determines whether a loop should perform another iteration.

**5. What causes an infinite loop?**

An infinite loop may occur when its stopping condition never becomes false and there is no other way to exit.

**6. What is a nested loop?**

A nested loop is a loop inside another loop.

**7. What does `break` do?**

It terminates the nearest enclosing loop immediately.

**8. What does `continue` do?**

It skips the rest of the current iteration and proceeds to the next one.

**9. What is a sentinel-controlled loop?**

It repeats until a designated value or event signals that the input process should stop.

**10. What is the time complexity of a loop that visits N elements once?**

Typically `O(N)`, provided each iteration performs constant-time work.

**11. What is a dry run?**

A dry run manually traces an algorithm step by step using sample inputs.

**12. Why is a loop update important?**

The update helps the algorithm progress toward its intended stopping condition.

---

## Learning Checklist

- [ ] I understand the purpose of a loop.
- [ ] I can draw a loop condition using a decision diamond.
- [ ] I can identify initialization, condition, body, and update.
- [ ] I understand `for` and `while` loops.
- [ ] I can trace each iteration in a dry run.
- [ ] I can use loops for summation and factorial.
- [ ] I understand nested loops.
- [ ] I understand `break` and `continue`.
- [ ] I can recognize an unintended infinite loop.
- [ ] I have run all examples.
- [ ] I have studied all solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After Loop Flowcharts, continue to **Practice Flowcharts**, where you will combine sequence, decisions, and loops to design solutions for larger problems.
