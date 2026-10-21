# Loop Flowcharts

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Loop Flowcharts  
> **Level:** Beginner  
> **Goal:** Understand repetition, loop conditions, counters, and repeated execution using flowcharts and Python.

---

## Table of Contents

1. Introduction
2. What Is a Loop?
3. What Is a Loop Flowchart?
4. Why Are Loops Needed?
5. The Loop Flow
6. Flowchart Symbols Used in Loops
7. The `while` Loop
8. The `for` Loop
9. Example 1 - Print Numbers from 1 to 5
10. Example 2 - Sum from 1 to N
11. Example 3 - Multiplication Table
12. Example 4 - Factorial
13. Example 5 - Count Digits
14. Example 6 - Count Even Numbers
15. Nested Loops
16. `break` and `continue`
17. Dry Run of a Loop
18. `for` Loop vs `while` Loop
19. Common Beginner Mistakes
20. Important Terminology
21. Interview Questions
22. Practice Questions
23. Learning Checklist
24. What's Next?

---

## 1. Introduction

In programming, we often need to repeat an operation multiple times.

For example, we may need to:

- Print numbers from 1 to 100.
- Calculate the sum of a sequence.
- Display a multiplication table.
- Calculate a factorial.
- Process every element of a list.
- Repeat an action until a condition is satisfied.

Writing the same instruction many times would make the code unnecessarily long.

**Loops allow us to repeat instructions.**

A loop flowchart shows how the execution returns to a condition and repeats a block of operations until the loop should terminate.

---

## 2. What Is a Loop?

A loop is a programming construct that repeatedly executes a block of instructions.

Python commonly provides two basic loop statements:

- `for`
- `while`

### Example Without a Loop

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

This displays five numbers using five separate statements.

### Example With a Loop

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

The loop performs the repeated operation with less code.

### Important Point

A loop must have an appropriate termination mechanism. Otherwise, it may continue running indefinitely.

---

## 3. What Is a Loop Flowchart?

A **loop flowchart** represents repeated execution using symbols and arrows.

The flowchart typically contains:

1. A start symbol.
2. An initialization step.
3. A decision symbol representing the loop condition.
4. A loop body containing the operations to repeat.
5. An update step when required.
6. An arrow returning to the condition.
7. An exit path when the condition is no longer satisfied.

### Basic Structure

```text
       ( START )
           |
           v
     [ Initialize ]
           |
           v
      < Condition? >
       /         \
     Yes          No
      |            |
      v            v
  [ Loop Body ]  ( STOP )
      |
      v
   [ Update ]
      |
      +-----------> Return to Condition
```

The Yes branch continues the loop, while the No branch exits it.

The exact order depends on the loop structure. For example, a `for` loop obtains the next item from an iterable rather than always using a numeric counter.

---

## 4. Why Are Loops Needed?

Loops help us perform repeated operations efficiently.

### 4.1 Reduce Repetition

Instead of writing 100 separate print statements, a loop can generate the same sequence.

### 4.2 Process Collections

Loops allow us to visit every element in a list, string, or other iterable.

### 4.3 Perform Repeated Calculations

A loop can accumulate a total, calculate a factorial, or generate a sequence.

### 4.4 Implement Algorithms

Loops are used in many algorithms, including searching, sorting, counting, and traversing data structures.

### 4.5 Work with Unknown Iteration Counts

A `while` loop can continue until a condition becomes false, which is useful when the number of iterations is not known in advance.

---

## 5. The Loop Flow

A typical counter-controlled loop follows these stages.

### Step 1: Initialize

Create or assign the initial counter value.

```python
counter = 1
```

### Step 2: Check the Condition

Determine whether the loop should execute.

```python
counter <= 5
```

### Step 3: Execute the Body

Perform the repeated operation.

```python
print(counter)
```

### Step 4: Update

Change the counter so that the loop can eventually terminate.

```python
counter += 1
```

### Step 5: Repeat or Exit

Return to the condition. If it is true, repeat the loop body. Otherwise, exit.

### Flowchart

```text
        ( START )
            |
            v
       [ i = 1 ]
            |
            v
        < i <= 5? >
         /       \
       Yes        No
        |          |
        v          v
     / Print i / ( STOP )
        |
        v
    [ i = i + 1 ]
        |
        +-----------> Return to Condition
```

This structure is common in counter-controlled loops.

---

## 6. Flowchart Symbols Used in Loops

| Symbol | Shape | Purpose |
|---|---|---|
| Terminator | Oval or rounded rectangle | Indicates Start or Stop |
| Process | Rectangle | Initializes a counter, updates a variable, or performs a calculation |
| Decision | Diamond | Checks whether the loop should continue |
| Input/Output | Parallelogram | Reads input or displays a result |
| Flow line | Arrow | Shows the direction of execution |

### Remember

The loop itself does not require a special new symbol.

It is represented using a combination of standard flowchart symbols and a returning flow line.

---

## 7. The `while` Loop

A `while` loop repeats its body as long as its condition evaluates to True.

### Syntax

```python
while condition:
    # Repeated statements
```

### Example

```python
counter = 1

while counter <= 5:
    print(counter)
    counter += 1
```

Output:

```text
1
2
3
4
5
```

### Flowchart

```text
       ( START )
           |
           v
      [ i = 1 ]
           |
           v
       < i <= 5? >
        /       \
      Yes        No
       |          |
       v          v
   / Print i /  ( STOP )
       |
       v
  [ i = i + 1 ]
       |
       +-----------> Back to Condition
```

### Explanation

1. The counter starts at 1.
2. Python checks whether the counter is at most 5.
3. If the condition is True, the counter is printed.
4. The counter increases by one.
5. Python checks the condition again.
6. The loop finishes when the counter becomes 6.

### When Is `while` Useful?

Use a `while` loop when repetition depends on a condition and the required number of iterations may not be known in advance.

---

## 8. The `for` Loop

A `for` loop iterates over items supplied by an iterable, such as a range, list, or string.

### Syntax

```python
for item in iterable:
    # Repeated statements
```

### Example

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

### Understanding `range(1, 6)`

In Python, the stopping value is excluded.

Therefore:

```python
range(1, 6)
```

generates these numbers:

```text
1, 2, 3, 4, 5
```

It does not generate 6.

### Flowchart Concept

A `for` loop can be represented using a decision and loop-back arrow:

```text
         ( START )
             |
             v
 / Obtain next item /
             |
             v
   < Another item available? >
          /          \
        Yes           No
         |             |
         v             v
    [ Loop Body ]    ( STOP )
         |
         +-------------> Obtain next item
```

For a numeric range, the items are generated according to the range specification.

### When Is `for` Useful?

Use `for` when iterating over a known sequence, range, collection, or other iterable.

---

## 9. Example 1 - Print Numbers from 1 to 5

### Problem

Display the numbers from 1 through 5.

### Algorithm

1. Start.
2. Initialize the counter to 1.
3. Check whether the counter is at most 5.
4. If true, display the counter.
5. Increase the counter.
6. Repeat the condition check.
7. If false, stop.

### Flowchart

```text
       ( START )
           |
           v
      [ i = 1 ]
           |
           v
       < i <= 5? >
        /       \
      Yes        No
       |          |
       v          v
    / Print i / ( STOP )
       |
       v
  [ i = i + 1 ]
       |
       +-----------> Back to Condition
```

### Python Code

```python
for number in range(1, 6):
    print(number)
```

### Output

```text
1
2
3
4
5
```

### Complexity

- Time: `O(n)` when printing a sequence of `n` numbers.
- Auxiliary space: `O(1)` for the loop's additional variables in this example.

---

## 10. Example 2 - Sum from 1 to N

### Problem

Calculate the sum of all positive integers from 1 to N.

### Formula

```text
SUM = 1 + 2 + 3 + ... + N
```

### Algorithm

1. Read N.
2. Initialize `TOTAL = 0`.
3. Initialize `COUNTER = 1`.
4. While `COUNTER <= N`, add the counter to TOTAL.
5. Increase the counter.
6. Repeat the condition check.
7. Display TOTAL.
8. Stop.

### Flowchart

```text
          ( START )
              |
              v
          / Read N /
              |
              v
    [ TOTAL = 0, i = 1 ]
              |
              v
          < i <= N? >
           /       \
         Yes        No
          |          |
          v          v
 [ TOTAL = TOTAL+i ] / Display TOTAL /
          |                |
          v                v
     [ i = i + 1 ]      ( STOP )
          |
          +---------------> Back to Condition
```

### Python Code

```python
n = int(input("Enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum:", total)
```

### Sample Input

```text
Enter a positive integer: 5
```

### Output

```text
Sum: 15
```

### Dry Run

| Counter | Previous Total | New Total |
|---:|---:|---:|
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |
| 5 | 10 | 15 |

The final answer is 15.

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(1)`.

---

## 11. Example 3 - Multiplication Table

### Problem

Display the multiplication table of a number from 1 to 10.

### Algorithm

1. Read N.
2. Set the multiplier to 1.
3. Calculate `RESULT = N × MULTIPLIER`.
4. Display the result.
5. Increase the multiplier.
6. Repeat until the multiplier exceeds 10.
7. Stop.

### Flowchart

```text
        ( START )
            |
            v
        / Read N /
            |
            v
       [ i = 1 ]
            |
            v
        < i <= 10? >
         /        \
       Yes         No
        |           |
        v           v
 [ RESULT = N*i ] ( STOP )
        |
        v
 / Display RESULT /
        |
        v
    [ i = i + 1 ]
        |
        +-----------> Back to Condition
```

### Python Code

```python
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)
```

### Sample Input

```text
Enter a number: 5
```

### Output

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Complexity

- Time: `O(1)` with a fixed table size of 10.
- More generally, if the table runs for N iterations, time is `O(N)`.
- Auxiliary space: `O(1)`.

---

## 12. Example 4 - Factorial Using a Loop

### Problem

Calculate the factorial of a non-negative integer N.

### Definition

For a positive integer:

```text
N! = N × (N - 1) × ... × 2 × 1
```

By definition:

```text
0! = 1
```

### Algorithm

1. Read N.
2. If N is negative, display an error.
3. Otherwise, initialize `FACTORIAL = 1`.
4. Multiply FACTORIAL by each integer from 1 through N.
5. Display FACTORIAL.
6. Stop.

### Flowchart

```text
        ( START )
            |
            v
        / Read N /
            |
            v
         < N < 0? >
          /      \
        Yes       No
         |         |
         v         v
 / Display Error / [ FACTORIAL = 1 ]
         |         |
         |         v
         |      [ i = 1 ]
         |         |
         |         v
         |      < i <= N? >
         |       /       \
         |     Yes        No
         |      |          |
         |      v          v
         | [ FACTORIAL =   / Display
         |   FACTORIAL*i ] FACTORIAL /
         |      |          |
         |      v          |
         |  [ i = i+1 ]    |
         |      |          |
         |      +----------> Back to Condition
         |                 |
         +-----------------+
                   |
                   v
                ( STOP )
```

### Python Code

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined here for negative integers.")
else:
    factorial = 1

    for number in range(1, n + 1):
        factorial *= number

    print("Factorial:", factorial)
```

### Sample Input

```text
Enter a non-negative integer: 5
```

### Output

```text
Factorial: 120
```

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(1)` in the basic operation-counting model.

When N is zero, the loop performs no iterations, and the result remains 1.

---

## 13. Example 5 - Count Digits

### Problem

Count the number of decimal digits in an integer, ignoring its sign.

### Algorithm

1. Read an integer.
2. Take its absolute value.
3. If the value is zero, its digit count is 1.
4. Otherwise, initialize `COUNT = 0`.
5. Repeatedly divide the number by 10 using integer division.
6. Increase COUNT after each division.
7. Stop when the remaining number becomes zero.
8. Display COUNT.

### Flowchart Concept

```text
       ( START )
           |
           v
     / Read Number /
           |
           v
 [ Number = abs(Number) ]
           |
           v
       < Number == 0? >
         /         \
       Yes          No
        |            |
        v            v
 [ COUNT = 1 ]  [ COUNT = 0 ]
        |            |
        |            v
        |        < Number > 0? >
        |          /         \
        |        Yes          No
        |         |            |
        |         v            |
        | [ Number=Number//10 ]|
        | [ COUNT = COUNT+1 ]  |
        |         |            |
        |         +------------> Back to Condition
        |                      |
        +-----------+----------+
                    |
                    v
              / Display COUNT /
                    |
                    v
                 ( STOP )
```

### Python Code

```python
number = int(input("Enter an integer: "))
remaining = abs(number)

if remaining == 0:
    digits = 1
else:
    digits = 0

    while remaining > 0:
        remaining //= 10
        digits += 1

print("Number of digits:", digits)
```

### Example

Input:

```text
Enter an integer: 4567
```

Output:

```text
Number of digits: 4
```

### Complexity

For an integer with D decimal digits:

- Time: `O(D)`.
- Auxiliary space: `O(1)` in the basic operation-counting model.

---

## 14. Example 6 - Count Even Numbers

### Problem

Count the number of even elements in a list.

### Algorithm

1. Initialize the count to zero.
2. Visit each element in the list.
3. Check whether the element is divisible by 2.
4. If it is even, increase the count.
5. Repeat until every element has been checked.
6. Display the count.

### Python Code

```python
numbers = [10, 15, 22, 31, 40, 55, 62]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("Even count:", even_count)
```

### Output

```text
Even count: 4
```

The even values are 10, 22, 40, and 62.

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(1)`.

The algorithm visits every element once and maintains a single count.

---

## 15. Nested Loops

A nested loop is a loop inside another loop.

The inner loop executes during each iteration of the outer loop, according to its own iteration rules.

### Example

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

### Output

```text
* * *
* * *
* * *
```

### Understanding the Execution

The outer loop runs 3 times.

For every outer-loop iteration, the inner loop runs 3 times.

The total number of inner-loop iterations is:

```text
3 × 3 = 9
```

### General Complexity

If both loops execute N times:

- Time complexity: `O(n²)`.
- Auxiliary space: `O(1)` for this simple example.

Nested loops do not always have quadratic complexity; analyze the actual iteration counts.

---

## 16. `break` and `continue`

Python provides two statements that change the normal flow of a loop.

### 16.1 The `break` Statement

`break` immediately terminates the nearest enclosing loop.

Example:

```python
for number in range(1, 6):
    if number == 4:
        break

    print(number)
```

Output:

```text
1
2
3
```

When the counter reaches 4, the loop ends.

### 16.2 The `continue` Statement

`continue` skips the remaining statements in the current iteration and proceeds to the next iteration.

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

The number 3 is skipped.

### Important Difference

| Statement | Effect |
|---|---|
| `break` | Terminates the nearest enclosing loop |
| `continue` | Skips the rest of the current iteration |

These statements can be represented in flowcharts by changing the path taken from a decision or condition.

---

## 17. Dry Run of a Loop

A dry run means tracing an algorithm manually to understand how its variables change during execution.

Consider:

```python
total = 0

for number in range(1, 4):
    total += number

print(total)
```

### Dry-Run Table

| Iteration | Number | Previous Total | New Total |
|---|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |

Output:

```text
6
```

The table shows that the loop adds each number to the running total.

A dry run is useful for identifying incorrect updates, wrong conditions, and errors in the sequence of steps.

---

## 18. `for` Loop vs `while` Loop

| Feature | `for` Loop | `while` Loop |
|---|---|---|
| Common use | Iterating over a range or iterable | Repeating while a condition is True |
| Iteration control | Obtains the next item from an iterable | Checks a Boolean condition |
| Manual counter update | Not always required | Often required in counter-controlled loops |
| Common risk | Incorrect range boundaries | Infinite loops when conditions do not change appropriately |
| Example | Print each item of a list | Repeat until a condition is satisfied |

### Example: `for`

```python
for number in range(1, 6):
    print(number)
```

### Example: `while`

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Both examples display the numbers from 1 to 5.

---

## 19. Common Beginner Mistakes

### Mistake 1: Forgetting to Update the Counter

A counter-controlled `while` loop may never terminate if its condition remains True.

### Mistake 2: Using the Wrong Condition

For example, changing `i <= 5` to `i < 5` changes the range of values processed.

### Mistake 3: Off-by-One Errors

An off-by-one error occurs when a loop runs one iteration too many or too few.

Remember that Python's `range()` excludes the stop value.

```python
range(1, 6)
```

generates the values 1, 2, 3, 4, and 5.

### Mistake 4: Incorrect Initialization

A sum usually starts at 0. A factorial usually starts at 1.

### Mistake 5: Incorrect Accumulation

Use an update such as:

```python
total += number
```

when adding values to a running total.

### Mistake 6: Infinite Loops

Always consider whether the condition can eventually become False.

### Mistake 7: Confusing `break` and `continue`

`break` exits the loop; `continue` skips the current iteration.

---

## 20. Important Terminology

| Term | Meaning |
|---|---|
| Loop | Repeats a block of instructions |
| Iteration | One execution of a loop body |
| Counter | Variable that tracks iterations or progress |
| Initialization | Setting the starting value |
| Condition | Boolean expression controlling repetition |
| Update | Changing a value to advance the loop |
| Loop body | Instructions repeated during execution |
| Infinite loop | Loop that does not terminate under its current behavior |
| Off-by-one error | Error involving one extra or missing iteration |
| Nested loop | A loop inside another loop |
| `break` | Terminates the nearest enclosing loop |
| `continue` | Skips the rest of the current iteration |
| Accumulator | Variable that collects a running result, such as a sum |

---

## 21. Interview Questions

### Q1. What is a loop?

A loop is a programming construct used to execute a block of instructions repeatedly.

### Q2. What is a loop flowchart?

It is a diagram showing repeated execution using a condition, loop body, and returning flow line.

### Q3. What is the difference between a `for` loop and a `while` loop?

A `for` loop iterates over an iterable. A `while` loop repeats while its condition evaluates to True.

### Q4. What causes an infinite loop?

A loop can run indefinitely when its termination condition never becomes False and no other control flow exits it.

### Q5. What is an off-by-one error?

It is a mistake where a loop processes one extra or one fewer iteration than intended.

### Q6. What is an accumulator?

An accumulator stores a result that is updated repeatedly, such as the sum of numbers.

### Q7. What is a nested loop?

A nested loop is a loop placed inside another loop.

### Q8. What is the purpose of `break`?

It terminates the nearest enclosing loop immediately.

### Q9. What is the purpose of `continue`?

It skips the remainder of the current iteration and proceeds to the next one.

### Q10. What is the time complexity of summing N elements?

`O(n)`, because every element is processed once.

### Q11. What is the time complexity of two nested loops that each execute N times?

`O(n²)`, because the inner operation runs N times for each of N outer-loop iterations.

### Q12. Why is a dry run useful when learning loops?

It shows how loop variables and accumulated results change after each iteration.

---

## 22. Practice Questions

Draw the flowchart for each problem before writing the Python code.

### Beginner Level

**Question 1:** Print numbers from 1 to 100.

**Question 2:** Print numbers from 100 down to 1.

**Question 3:** Print all even numbers from 1 to 50.

**Question 4:** Print all odd numbers from 1 to 100.

**Question 5:** Calculate the sum of the first N positive integers.

**Question 6:** Print the multiplication table of a given number.

### Intermediate Level

**Question 7:** Calculate the factorial of a non-negative integer.

**Question 8:** Count the number of digits in an integer.

**Question 9:** Calculate the sum of the digits of an integer.

**Question 10:** Count the even and odd elements of a list.

**Question 11:** Find the largest element of a non-empty list.

**Question 12:** Search for a target by scanning a list.

### Challenge

**Question 13:** Draw a flowchart that calculates the factorial using a loop and handles negative input.

**Question 14:** Draw a flowchart that keeps processing values until a sentinel value is entered.

**Question 15:** Draw a flowchart for a nested loop that prints a square pattern.

For each question:

1. Write the algorithm.
2. Draw the loop flowchart.
3. Implement the solution in Python.
4. Perform a dry run.
5. Test boundary cases.
6. State the time and auxiliary space complexities where appropriate.

---

## 23. Learning Checklist

- [ ] Understand loops and repeated execution.
- [ ] Identify the decision symbol in a loop flowchart.
- [ ] Draw the loop-back arrow correctly.
- [ ] Understand initialization, condition, body, and update.
- [ ] Use `for` loops.
- [ ] Use `while` loops.
- [ ] Calculate a sum using a loop.
- [ ] Generate a multiplication table.
- [ ] Calculate factorial using a loop.
- [ ] Count digits using repeated division.
- [ ] Understand nested loops.
- [ ] Understand `break` and `continue`.
- [ ] Perform a dry run.
- [ ] Identify off-by-one errors.
- [ ] Test for unintended infinite loops.
- [ ] Complete the practice questions.

---

## 24. What's Next?

Continue with:

**05 - Practice Flowcharts**

In the next folder, practise drawing complete flowcharts for different programming problems using input/output operations, decisions, and loops.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `04_loop_flowchart.py` | Runnable Python examples demonstrating repeated operations |
| `README.md` | Detailed theory, loop flow diagrams, code examples, dry runs, interview questions, and practice problems |

---

## Conclusion

Loops make it possible to repeat operations without writing the same instructions many times.

When designing a loop flowchart, identify the initialization, the condition, the operations to repeat, and the path back to the condition. Ensure that the loop can terminate when appropriate.

Remember:

**Initialize → Check Condition → Execute Body → Update → Repeat or Exit**

Practising these steps will help you understand loops in Python and prepare you for more advanced DSA algorithms.