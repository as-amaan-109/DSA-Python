# Loop Pseudocode — Python

Welcome to **Loop Pseudocode**, the fourth topic in the Pseudocode section of the DSA-Python repository.

This topic teaches you how to represent repetition using structured pseudocode. You will learn how to initialize variables, define loop conditions, update values, terminate loops, and translate the logic into Python.

---

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [What Is Loop Pseudocode?](#what-is-loop-pseudocode)
4. [Parts of a Loop](#parts-of-a-loop)
5. [FOR Loop](#for-loop)
6. [WHILE Loop](#while-loop)
7. [FOR vs WHILE](#for-vs-while)
8. [Worked Example: Sum from 1 to N](#worked-example-sum-from-1-to-n)
9. [Worked Example: Factorial](#worked-example-factorial)
10. [Worked Example: Sum of Digits](#worked-example-sum-of-digits)
11. [Nested Loops](#nested-loops)
12. [Sentinel-Controlled Loops](#sentinel-controlled-loops)
13. [BREAK and CONTINUE](#break-and-continue)
14. [Dry Runs and Testing](#dry-runs-and-testing)
15. [Infinite Loops and Termination](#infinite-loops-and-termination)
16. [Time and Space Complexity](#time-and-space-complexity)
17. [Folder Structure](#folder-structure)
18. [How to Run the Program](#how-to-run-the-program)
19. [Practice Questions](#practice-questions)
20. [Common Mistakes](#common-mistakes)
21. [Interview Questions](#interview-questions)
22. [Learning Checklist](#learning-checklist)

---

## About This Topic

A loop repeats a sequence of instructions. Loops are useful when a problem requires an operation to be performed multiple times.

Examples include:

- Printing numbers from 1 to N.
- Calculating the sum of a series.
- Computing factorial.
- Generating a multiplication table.
- Counting and manipulating digits.
- Generating Fibonacci numbers.
- Repeatedly reading values.
- Searching for a value.
- Producing patterns using nested loops.

Pseudocode helps describe these operations before writing the actual Python code.

## Learning Objectives

After completing this topic, you should be able to:

- Explain repetition and iteration.
- Identify initialization, condition, loop body, and update.
- Write `FOR` loop pseudocode.
- Write `WHILE` loop pseudocode.
- Choose a suitable loop structure for a problem.
- Represent counter-controlled and sentinel-controlled repetition.
- Understand nested loops.
- Use `BREAK` and `CONTINUE` in pseudocode.
- Perform loop dry runs using trace tables.
- Identify unintended infinite loops.
- Implement loop pseudocode in Python.
- Estimate basic time and auxiliary-space complexity.

---

## What Is Loop Pseudocode?

Loop pseudocode represents repeated execution using structured, language-independent instructions.

Example:

```text
START
    INPUT N
    TOTAL <- 0

    FOR NUMBER <- 1 TO N
        TOTAL <- TOTAL + NUMBER
    END FOR

    OUTPUT TOTAL
END
```

This pseudocode repeats the addition operation for each integer from 1 through N.

The keywords `FOR`, `WHILE`, `END FOR`, and `END WHILE` are conventions used in this repository. Pseudocode has no single universally enforced syntax, so consistency and clarity are more important than a specific keyword style.

---

## Parts of a Loop

A typical loop uses four main elements.

### 1. Initialization

Initialization sets the starting value.

Example:

```text
COUNT <- 1
TOTAL <- 0
```

The counter begins at 1 and the accumulated sum begins at zero.

### 2. Condition

The condition controls whether another iteration should execute.

Example:

```text
WHILE COUNT <= N
```

When the condition is false, the loop ends unless another control statement changes the execution path.

### 3. Loop body

The loop body contains the repeated operations.

Example:

```text
TOTAL <- TOTAL + COUNT
```

### 4. Update

The update changes the state of the algorithm so that it can progress.

Example:

```text
COUNT <- COUNT + 1
```

If the update is missing and the condition stays true, the loop may never terminate.

### Complete example

```text
START
    INPUT N
    COUNT <- 1
    TOTAL <- 0

    WHILE COUNT <= N
        TOTAL <- TOTAL + COUNT
        COUNT <- COUNT + 1
    END WHILE

    OUTPUT TOTAL
END
```

The loop adds the current count to the total, increments the count, and checks the condition again.

---

## FOR Loop

A `FOR` loop is useful when iterating over a known range or sequence.

### Pseudocode pattern

```text
FOR VARIABLE <- START_VALUE TO END_VALUE
    STATEMENTS
END FOR
```

In this repository's convention, the ending value is included.

Example:

```text
FOR I <- 1 TO 5
    OUTPUT I
END FOR
```

Output:

```text
1
2
3
4
5
```

### Python equivalent

```python
for i in range(1, 6):
    print(i)
```

Python's `range()` excludes the stopping value, so the equivalent Python code uses `range(1, 6)` to produce values from 1 through 5.

### FOR loop with a step

Pseudocode:

```text
FOR I <- 2 TO 10 STEP 2
    OUTPUT I
END FOR
```

Python:

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

This pattern is useful for processing even numbers or other regularly spaced values.

---

## WHILE Loop

A `WHILE` loop repeats as long as its condition is true.

### Pseudocode pattern

```text
WHILE CONDITION
    STATEMENTS
END WHILE
```

Example:

```text
START
    COUNT <- 1

    WHILE COUNT <= 5
        OUTPUT COUNT
        COUNT <- COUNT + 1
    END WHILE
END
```

### Python equivalent

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

The condition is checked before each iteration. Once `count` becomes 6, the condition is false and execution continues after the loop.

### When is WHILE useful?

A `WHILE` loop is useful when the number of iterations is not known in advance.

Examples include:

- Repeating input until a valid value is entered.
- Reading values until a sentinel is supplied.
- Continuing a search until a target is found.
- Repeating a process while a value satisfies a condition.

---

## FOR vs WHILE

| Feature | FOR | WHILE |
|---|---|---|
| Typical use | Iterate over a range or sequence | Repeat while a condition remains true |
| Iteration count | Often known or determined by an iterable | May not be known in advance |
| Progression | The loop variable receives values from the range or sequence | The algorithm commonly updates a condition-related variable |
| Common examples | Summation, tables, fixed number of inputs | Sentinel input, validation, condition-based repetition |
| Common risk | Incorrect range boundaries | Missing or incorrect update |

Both loop types can implement many of the same algorithms. Choose the structure that makes the logic easiest to understand and verify.

---

## Worked Example: Sum from 1 to N

**Problem:** Read a positive integer N and calculate the sum of integers from 1 through N.

### Algorithm

1. Read N.
2. If N is less than 1, report invalid input.
3. Initialize `TOTAL = 0`.
4. Repeat from 1 through N.
5. Add the current number to TOTAL.
6. Display TOTAL.

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

Expected output:

```text
Enter a positive integer: 4
Sum: 10
```

### Complexity

- Time: `O(N)` for the loop-based implementation.
- Auxiliary space: `O(1)` because the algorithm uses a fixed number of additional variables.

---

## Worked Example: Factorial

**Problem:** Calculate the factorial of a non-negative integer N.

Factorial is defined as:

- `0! = 1`
- `1! = 1`
- For positive N, `N! = 1 × 2 × 3 × ... × N`

### Algorithm

1. Read N.
2. Reject negative values.
3. Initialize `FACTORIAL = 1`.
4. Multiply FACTORIAL by each integer from 1 through N.
5. Display FACTORIAL.

### Pseudocode

```text
START
    INPUT N

    IF N < 0 THEN
        OUTPUT "Factorial is not defined"
    ELSE
        FACTORIAL <- 1

        FOR I <- 1 TO N
            FACTORIAL <- FACTORIAL * I
        END FOR

        OUTPUT FACTORIAL
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

| Iteration | I | FACTORIAL before | FACTORIAL after |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 2 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 6 | 24 |
| 5 | 5 | 24 | 120 |

Expected result: `5! = 120`.

For this loop-based approach, time complexity is `O(N)` multiplications and auxiliary space is `O(1)` under the usual introductory model.

---

## Worked Example: Sum of Digits

**Problem:** Calculate the sum of the decimal digits of an integer.

For example, the sum of the digits of 583 is `5 + 8 + 3 = 16`.

### Algorithm

1. Read N.
2. Take the absolute value.
3. Set TOTAL to zero.
4. Extract the last digit using the remainder after division by 10.
5. Add the extracted digit to TOTAL.
6. Remove the last digit using integer division by 10.
7. Repeat until the remaining value is zero.
8. Display TOTAL.

### Pseudocode

```text
START
    INPUT N
    TEMP <- ABS(N)
    TOTAL <- 0

    WHILE TEMP > 0
        DIGIT <- TEMP MOD 10
        TOTAL <- TOTAL + DIGIT
        TEMP <- TEMP DIV 10
    END WHILE

    OUTPUT TOTAL
END
```

### Python implementation

```python
number = int(input("Enter an integer: "))
temp = abs(number)
total = 0

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of digits:", total)
```

### Dry run for N = 583

| Iteration | TEMP before | DIGIT | TOTAL after | TEMP after |
|---:|---:|---:|---:|---:|
| 1 | 583 | 3 | 3 | 58 |
| 2 | 58 | 8 | 11 | 5 |
| 3 | 5 | 5 | 16 | 0 |

The loop stops when TEMP becomes zero. The output is `16`.

For the input zero, the algorithm performs no loop iterations and returns a digit sum of zero.

### Complexity

For an integer with D decimal digits:

- Time: `O(D)` digit-processing steps.
- Auxiliary space: `O(1)` under the usual introductory model.

---

## Nested Loops

A nested loop is a loop placed inside another loop.

Example: print a triangle of stars.

### Pseudocode

```text
START
    INPUT ROWS

    FOR ROW <- 1 TO ROWS
        FOR COLUMN <- 1 TO ROW
            OUTPUT "*" WITHOUT NEWLINE
        END FOR

        OUTPUT NEWLINE
    END FOR
END
```

### Python implementation

```python
rows = 4

for row in range(1, rows + 1):
    for column in range(row):
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

### Explanation

- The outer loop controls the row.
- The inner loop prints the stars for that row.
- The newline moves execution to the next row.

For N rows, this example prints `1 + 2 + ... + N` stars, so its total printing work is `O(N²)`. The loop counters require only `O(1)` auxiliary space.

---

## Sentinel-Controlled Loops

A sentinel is a special value that tells the algorithm when to stop accepting input.

Example: keep adding values until the user enters zero.

### Pseudocode

```text
START
    TOTAL <- 0

    WHILE TRUE
        INPUT VALUE

        IF VALUE = 0 THEN
            BREAK
        END IF

        TOTAL <- TOTAL + VALUE
    END WHILE

    OUTPUT TOTAL
END
```

### Python implementation

```python
total = 0

while True:
    value = float(input("Enter a number (0 to stop): "))

    if value == 0:
        break

    total += value

print("Total:", total)
```

Here, zero is the stopping signal and is not included in the sum.

A robust design should define the sentinel clearly so that users know how to end the input process.

---

## BREAK and CONTINUE

### BREAK

`BREAK` stops the nearest enclosing loop immediately.

Pseudocode:

```text
FOR NUMBER <- 1 TO 10
    IF NUMBER = 5 THEN
        BREAK
    END IF

    OUTPUT NUMBER
END FOR
```

Python:

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

### CONTINUE

`CONTINUE` skips the rest of the current iteration and moves to the next iteration.

Pseudocode:

```text
FOR NUMBER <- 1 TO 5
    IF NUMBER = 3 THEN
        CONTINUE
    END IF

    OUTPUT NUMBER
END FOR
```

Python:

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

Use these statements only when they make the loop logic clearer.

---

## Dry Runs and Testing

A dry run manually traces the loop using a known input.

For each iteration, record:

1. The loop variable.
2. The condition result.
3. The operation performed.
4. The updated values.
5. Whether the loop continues or exits.

### Useful test cases

| Algorithm | Suggested inputs |
|---|---|
| Print 1 to N | N = 1, N = 5, N = 0 |
| Factorial | N = 0, N = 1, N = 5, negative N |
| Count digits | 0, 7, 5832, -42 |
| Sum of digits | 0, 123, 999, -123 |
| Prime check | -1, 0, 1, 2, 9, 17 |
| Countdown | Starting value 0, 3, negative input |
| Input validation | Enter invalid values followed by a valid value |

Testing small inputs makes initialization, update, and stopping-condition errors easier to recognize.

---

## Infinite Loops and Termination

An infinite loop occurs when a loop continues indefinitely without reaching the intended stopping condition or another exit mechanism.

Incorrect example:

```python
number = 1

while number <= 5:
    print(number)
    # Missing update: number never changes.
```

The condition remains true because the value of `number` never changes.

Correct version:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### How to avoid infinite loops

- Initialize the loop variables correctly.
- Define a condition that represents the intended stopping rule.
- Update the relevant variable inside the loop.
- Ensure the variable can progress toward termination.
- Check the loop using a small sample input.
- For sentinel-controlled loops, document the stopping value.

Some software intentionally runs until an external event occurs. In beginner algorithms, however, the loop should have a clearly understood exit rule.

---

## Time and Space Complexity

The running time of a loop depends on how many iterations it performs and how much work is done during each iteration.

| Pattern | Typical time complexity |
|---|---:|
| Fixed number of iterations | `O(1)` relative to a separate input size |
| Loop through N values once | `O(N)` |
| Two nested loops over N values each | `O(N²)` |
| Repeatedly halve the search range | `O(log N)` |
| Digit-by-digit processing of a D-digit number | `O(D)` |
| Generate N Fibonacci terms iteratively | `O(N)` arithmetic steps |

Auxiliary space depends on what the algorithm stores:

- A running sum normally uses `O(1)` additional variables.
- A list storing N generated values usually uses `O(N)` additional space.
- Nested loops do not automatically imply `O(N²)` space.

These are introductory complexity estimates. The cost of arithmetic can increase when working with very large integers.

---

## Folder Structure

```text
04_Loop_Pseudocode/
│
├── README.md
└── 04_loop_pseudocode.py
```

The Python file contains runnable examples, solved questions, and unsolved practice prompts. This README explains the loop concepts and shows how to design, test, and analyse loop-based algorithms.

---

## How to Run the Program

Open PowerShell in your `DSA-Python` repository root.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\04_Loop_Pseudocode\04_loop_pseudocode.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Choose the desired option and follow the prompts. Select `0` inside a sub-menu to return to the main menu.

If `python` is not recognized, verify your Python installation. The Windows `py` command may work instead.

---

## Practice Questions

The Python file includes 12 examples, 12 solved practice questions, and 5 unsolved questions.

### 12 Examples

1. Print numbers from 1 to N.
2. Calculate the sum from 1 to N.
3. Display a multiplication table.
4. Calculate factorial.
5. Display a countdown.
6. Count digits.
7. Calculate the sum of digits.
8. Reverse an integer.
9. Generate Fibonacci terms.
10. Add values until zero is entered.
11. Check whether a number is prime.
12. Print a star triangle using nested loops.

### 12 Solved Questions

1. Sum even numbers from 1 to N.
2. Calculate the product of N entered numbers.
3. Count even and odd inputs.
4. Calculate GCD using Euclid's algorithm.
5. Calculate LCM.
6. Check a palindrome number.
7. Find the minimum of N values.
8. Find the maximum of N values.
9. Repeat input until a positive value is entered.
10. Calculate the sum of squares from 1 to N.
11. Generate Fibonacci terms and calculate their sum.
12. Check an Armstrong number.

### 5 Unsolved Questions

1. Print all prime numbers between two bounds.
2. Convert a non-negative decimal integer into binary without a built-in conversion function.
3. Determine whether a number is a perfect number.
4. Generate a sequence whose new terms are sums of the previous two terms, starting with two user-defined values.
5. Read integers until `-1` is entered, then display the minimum, maximum, and average of the preceding values. Handle the case where no values are entered.

For each question, write the initialization, condition, repeated operation, update, and stopping rule before implementing it.

---

## Common Mistakes

- Forgetting to initialize a counter or accumulator.
- Using the wrong loop range.
- Forgetting that Python's `range()` excludes the stop value.
- Forgetting to update a `WHILE` loop variable.
- Using an incorrect termination condition.
- Accidentally skipping the first or last value.
- Forgetting the special cases for zero and negative integers.
- Mixing sentinel input with ordinary data without a clear rule.
- Using `BREAK` or `CONTINUE` without understanding their effect.
- Assuming nested loops always need quadratic memory.
- Testing only one iteration.
- Writing pseudocode that does not match the Python implementation.

---

## Interview Questions

**1. What is loop pseudocode?**

It represents repeated algorithmic operations using structured instructions such as `FOR` and `WHILE`.

**2. What is initialization?**

Initialization sets the starting values used by a loop.

**3. What is a loop condition?**

It determines whether another iteration should execute.

**4. What is the difference between FOR and WHILE?**

A `FOR` loop commonly iterates over a known range or sequence, while a `WHILE` loop continues as long as a condition remains true.

**5. What is an infinite loop?**

It is a loop that does not reach its intended stopping condition or another exit mechanism.

**6. What is a nested loop?**

It is a loop inside another loop.

**7. What does BREAK do?**

It exits the nearest enclosing loop.

**8. What does CONTINUE do?**

It skips the rest of the current iteration and proceeds to the next one.

**9. What is a sentinel-controlled loop?**

It repeats until a designated value signals that the input process should stop.

**10. What is the time complexity of a loop over N elements?**

It is typically `O(N)` when each iteration performs constant-time work.

**11. Why must loop variables be updated?**

The update allows the algorithm to progress toward its stopping condition.

**12. What is a dry run?**

It is a manual trace of an algorithm using sample values to verify each iteration and the final result.

---

## Learning Checklist

- [ ] I understand iteration and repetition.
- [ ] I can write `FOR` loop pseudocode.
- [ ] I can write `WHILE` loop pseudocode.
- [ ] I understand initialization, condition, body, and update.
- [ ] I can calculate sums and factorials using loops.
- [ ] I can process the digits of an integer.
- [ ] I understand nested loops.
- [ ] I understand sentinel-controlled input.
- [ ] I understand `BREAK` and `CONTINUE`.
- [ ] I can identify an unintended infinite loop.
- [ ] I can dry-run a loop.
- [ ] I have run the examples.
- [ ] I have reviewed the solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Loop Pseudocode, review the parent `01-Pseudocode/README.md` to recap the four pseudocode topics before moving on to the next section of the repository.
