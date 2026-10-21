# Practice Flowcharts

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Practice Flowcharts  
> **Level:** Beginner  
> **Goal:** Combine input/output, decisions, and loops to design and implement complete solutions.

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. How to Solve a Flowchart Problem
4. Example 1 - Welcome Message
5. Example 2 - Addition
6. Example 3 - Positive, Negative, or Zero
7. Example 4 - Largest of Three Numbers
8. Example 5 - Sum from 1 to N
9. Example 6 - Multiplication Table
10. Example 7 - Factorial
11. Example 8 - Count Digits
12. Example 9 - Linear Search
13. Example 10 - Count Even and Odd Numbers
14. Example 11 - Divisibility Check
15. Example 12 - Nested Loop Pattern
16. How to Test a Flowchart
17. Common Beginner Mistakes
18. Important Terminology
19. Interview Questions
20. Practice Questions
21. Learning Checklist
22. Final Review

---

## 1. Introduction

A flowchart represents an algorithm visually using standard symbols connected by arrows.

So far, we have studied:

- Basic flowchart symbols.
- Input and output operations.
- Decision-making.
- Loops and repeated execution.

This topic combines these concepts to solve complete programming problems.

For each example, we will identify the problem, write the algorithm steps, represent the logic using a flowchart, implement it in Python, and check its output.

The goal is to understand how different flowchart concepts work together rather than treating them as separate topics.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

- Convert a problem statement into ordered steps.
- Identify the input, processing, and output.
- Use decision symbols to represent conditions.
- Use loops to represent repeated operations.
- Combine decisions and loops in one solution.
- Implement flowchart logic using Python.
- Perform dry runs.
- Test solutions with different input values.
- Recognize common logical errors.
- Explain the time and auxiliary space complexity of basic algorithms.

---

## 3. How to Solve a Flowchart Problem

Use this workflow for each programming problem.

### Step 1: Understand the Problem

Identify exactly what the program needs to do.

### Step 2: Identify the Input

Determine the values the algorithm needs.

### Step 3: Identify the Output

Decide what the final result should be.

### Step 4: Write the Algorithm

Arrange the instructions in a logical sequence.

### Step 5: Draw the Flowchart

Use the appropriate symbols:

| Symbol | Purpose |
|---|---|
| Oval or rounded rectangle | Start or Stop |
| Parallelogram | Input or Output |
| Rectangle | Calculation or assignment |
| Diamond | Decision or condition |
| Arrow | Direction of execution |

### Step 6: Implement in Python

Convert the flowchart steps into working code.

### Step 7: Test the Solution

Use normal inputs, boundary cases, and other relevant test cases.

### General Workflow

```text
Understand the Problem
          |
          v
Identify Input and Output
          |
          v
Write Algorithm Steps
          |
          v
Draw the Flowchart
          |
          v
Implement in Python
          |
          v
Test the Result
```

---

## 4. Example 1 - Welcome Message

### Problem

Ask the user for a name and display a welcome message.

### Algorithm

1. Start.
2. Read the name.
3. Display a welcome message.
4. Stop.

### Flowchart

```text
       ( START )
           |
           v
     / Read Name /
           |
           v
  / Display Welcome /
           |
           v
        ( STOP )
```

### Python Code

```python
name = input("Enter your name: ")
print("Welcome to Python,", name)
```

### Sample Input

```text
Enter your name: Amaan
```

### Output

```text
Welcome to Python, Amaan
```

### Explanation

This example demonstrates a basic sequence of input and output operations.

No calculation or decision is required.

### Complexity

The program uses a fixed number of input/output statements. In the usual instructional model, it performs a constant number of operations, excluding costs that depend on the length of the input text.

---

## 5. Example 2 - Addition

### Problem

Read two integers and display their sum.

### Algorithm

1. Start.
2. Read A and B.
3. Calculate `SUM = A + B`.
4. Display SUM.
5. Stop.

### Flowchart

```text
        ( START )
            |
            v
     / Read A and B /
            |
            v
       [ SUM = A + B ]
            |
            v
       / Display SUM /
            |
            v
         ( STOP )
```

### Python Code

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Sample Input

```text
Enter the first number: 10
Enter the second number: 20
```

### Output

```text
Sum: 30
```

### Explanation

The program receives two values, performs addition, and displays the result.

The process rectangle represents the addition operation.

### Complexity

- Time: `O(1)` for fixed-size integer inputs.
- Auxiliary space: `O(1)` under the usual basic analysis model.

---

## 6. Example 3 - Positive, Negative, or Zero

### Problem

Determine whether an integer is positive, negative, or zero.

### Algorithm

1. Start.
2. Read N.
3. If N is greater than zero, display Positive.
4. Otherwise, if N is less than zero, display Negative.
5. Otherwise, display Zero.
6. Stop.

### Flowchart

```text
       ( START )
           |
           v
       / Read N /
           |
           v
       < N > 0? >
       /       \
     Yes        No
      |          |
      v          v
 / Positive /  < N < 0? >
               /       \
             Yes        No
              |          |
              v          v
         / Negative /  / Zero /
              |          |
              +----+-----+
                   |
                   v
                ( STOP )
```

### Python Code

```python
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Example Results

| Input | Output |
|---:|---|
| 10 | Positive |
| -5 | Negative |
| 0 | Zero |

### Explanation

The diamond-shaped symbols represent decisions.

The program follows a different branch depending on the conditions.

### Complexity

- Time: `O(1)`.
- Auxiliary space: `O(1)`.

---

## 7. Example 4 - Largest of Three Numbers

### Problem

Find a largest value among three integers.

### Algorithm

1. Start.
2. Read A, B, and C.
3. If A is greater than or equal to both B and C, choose A.
4. Otherwise, if B is greater than or equal to both A and C, choose B.
5. Otherwise, choose C.
6. Display the largest value.
7. Stop.

### Flowchart

```text
          ( START )
              |
              v
     / Read A, B, C /
              |
              v
     < A >= B and A >= C? >
            /         \
          Yes          No
           |            |
           v            v
      [ LARGEST=A ]  < B >= A and B >= C? >
                         /             \
                       Yes              No
                        |                |
                        v                v
                  [ LARGEST=B ]    [ LARGEST=C ]
                        |                |
                        +-------+--------+
                                |
                                v
                        / Display LARGEST /
                                |
                                v
                             ( STOP )
```

### Python Code

```python
a, b, c = map(
    int,
    input("Enter three integers: ").split()
)

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

### Sample Input

```text
Enter three integers: 12 45 30
```

### Output

```text
Largest: 45
```

### Explanation

The flowchart compares values through decisions and chooses a value that is at least as large as the others.

### Complexity

- Time: `O(1)` for a fixed number of inputs.
- Auxiliary space: `O(1)`.

---

## 8. Example 5 - Sum from 1 to N

### Problem

Calculate the sum of positive integers from 1 through N.

### Formula

```text
SUM = 1 + 2 + 3 + ... + N
```

### Algorithm

1. Read N.
2. If N is less than 1, display an error.
3. Otherwise, initialize TOTAL = 0.
4. Repeat for each integer from 1 through N.
5. Add the current integer to TOTAL.
6. Display TOTAL.
7. Stop.

### Flowchart

```text
          ( START )
              |
              v
          / Read N /
              |
              v
           < N < 1? >
            /      \
          Yes       No
           |         |
           v         v
    / Display Error / [ TOTAL = 0, i = 1 ]
           |                   |
           |                   v
           |               < i <= N? >
           |                /       \
           |              Yes        No
           |               |          |
           |               v          v
           |       [ TOTAL=TOTAL+i ] / Display TOTAL /
           |               |          |
           |               v          |
           |          [ i = i+1 ]     |
           |               |          |
           |               +----------> Back to Condition
           |                          |
           +-------------+------------+
                         |
                         v
                      ( STOP )
```

### Python Code

```python
n = int(input("Enter a positive integer: "))

if n < 1:
    print("Invalid input")
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

| Number | Previous Total | New Total |
|---:|---:|---:|
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |
| 5 | 10 | 15 |

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(1)`.

The loop processes each number from 1 to N.

---

## 9. Example 6 - Multiplication Table

### Problem

Display the multiplication table of a given number from 1 to 10.

### Algorithm

1. Read N.
2. Set the multiplier to 1.
3. Check whether the multiplier is at most 10.
4. Calculate N multiplied by the multiplier.
5. Display the result.
6. Increase the multiplier.
7. Repeat the condition check.
8. Stop when the condition becomes false.

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
     [ i = i+1 ]
        |
        +-----------> Back to Condition
```

### Python Code

```python
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    print(
        number,
        "x",
        multiplier,
        "=",
        number * multiplier
    )
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

The table has a fixed size of 10, so this particular implementation performs a constant number of iterations.

If the number of iterations is generalized to N, the time complexity is `O(n)`.

---

## 10. Example 7 - Factorial

### Problem

Calculate the factorial of a non-negative integer.

### Definition

```text
N! = N × (N-1) × ... × 2 × 1
```

By definition:

```text
0! = 1
```

### Algorithm

1. Read N.
2. If N is negative, display an error.
3. Otherwise, initialize FACTORIAL = 1.
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
          | [ FACTORIAL=   / Display /
          |   FACTORIAL*i ] FACTORIAL
          |      |          |
          |      v          |
          |   [ i = i+1 ]   |
          |      |          |
          |      +----------> Back to Condition
          |                 |
          +--------+--------+
                   |
                   v
                ( STOP )
```

### Python Code

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Invalid input")
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

The initial value of 1 ensures that the algorithm also returns the correct result for `0!`.

---

## 11. Example 8 - Count Digits

### Problem

Count the decimal digits in an integer, ignoring its sign.

### Algorithm

1. Read an integer.
2. Take its absolute value.
3. If the value is zero, set the count to 1.
4. Otherwise, repeatedly divide by 10 using integer division.
5. Increase the count after each division.
6. Stop when the value becomes zero.
7. Display the digit count.

### Flowchart

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
        /          \
      Yes           No
       |             |
       v             v
 [ COUNT = 1 ]   [ COUNT = 0 ]
       |             |
       |             v
       |       < Number > 0? >
       |        /          \
       |      Yes           No
       |       |             |
       |       v             |
       | [ Number=Number//10 ]
       | [ COUNT = COUNT+1 ]
       |       |
       |       +-------------> Back to Condition
       |                     |
       +----------+----------+
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

## 12. Example 9 - Linear Search

### Problem

Find the position of a target value in a list.

### Algorithm

1. Start.
2. Read the target value.
3. Initialize the result to Not Found.
4. Visit each list element.
5. If an element matches the target, record its index and stop searching.
6. If no match exists, display Not Found.
7. Stop.

### Flowchart

```text
         ( START )
             |
             v
      / Read Target /
             |
             v
       [ index = 0 ]
             |
             v
     < More elements? >
         /         \
       Yes          No
        |            |
        v            v
   < Element ==     / Display
      Target? >    Not Found /
     /       \          |
   Yes        No         |
    |          |         |
    v          v         |
/ Display / [ index=     |
 Found    /  index+1 ]   |
    |          |         |
    |          +---------> Back to Condition
    |                    |
    +---------+----------+
              |
              v
           ( STOP )
```

### Python Code

```python
numbers = [10, 20, 30, 40, 50]
target = int(input("Enter the target: "))

found_index = -1

for index, value in enumerate(numbers):
    if value == target:
        found_index = index
        break

if found_index != -1:
    print("Found at index:", found_index)
else:
    print("Not Found")
```

### Complexity

- Worst-case time: `O(n)`.
- Auxiliary space: `O(1)`.

Linear search can work on unsorted data.

---

## 13. Example 10 - Count Even and Odd Numbers

### Problem

Count the even and odd integers in a list.

### Algorithm

1. Initialize EVEN_COUNT = 0 and ODD_COUNT = 0.
2. Visit each element in the list.
3. If the number is divisible by 2, increase EVEN_COUNT.
4. Otherwise, increase ODD_COUNT.
5. Continue until all elements have been checked.
6. Display both counts.
7. Stop.

### Python Code

```python
numbers = [10, 15, 22, 31, 40, 55, 62]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)
```

### Output

```text
Even count: 4
Odd count: 3
```

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(1)`.

The algorithm visits every element once.

---

## 14. Example 11 - Divisibility by 3 and 5

### Problem

Determine whether an integer is divisible by both 3 and 5.

### Algorithm

1. Start.
2. Read a number N.
3. Check `N % 3 == 0 and N % 5 == 0`.
4. If True, display that the number is divisible by both.
5. Otherwise, display that it is not divisible by both.
6. Stop.

### Python Code

```python
number = int(input("Enter an integer: "))

if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")
```

### Sample Input

```text
Enter an integer: 30
```

### Output

```text
Divisible by both 3 and 5
```

### Explanation

The condition uses the logical operator `and`.

Both divisibility conditions must be True for the first branch to execute.

Zero is divisible by both 3 and 5 mathematically because `0 % 3 == 0` and `0 % 5 == 0`.

---

## 15. Example 12 - Nested Loop Pattern

### Problem

Display a square pattern containing three rows and three stars per row.

### Algorithm

1. Start.
2. Set the outer loop to repeat for three rows.
3. For every row, execute an inner loop three times.
4. Print a star during every inner-loop iteration.
5. Move to a new line after each row.
6. Repeat until all rows are complete.
7. Stop.

### Flowchart Concept

```text
        ( START )
            |
            v
        [ row = 1 ]
            |
            v
        < row <= 3? >
         /         \
       Yes          No
        |            |
        v            v
    [ col = 1 ]    ( STOP )
        |
        v
     < col <= 3? >
      /         \
    Yes          No
     |            |
     v            v
 / Print * /  / New Line /
     |            |
     v            v
 [ col=col+1 ] [ row=row+1 ]
     |            |
     +-> Inner    +-> Outer
         Condition    Condition
```

### Python Code

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

### Complexity

With three rows and three columns, the loop size is fixed.

For a generalized N-by-N pattern:

- Time: `O(n²)`.
- Auxiliary space: `O(1)` excluding output storage.

---

## 16. How to Test a Flowchart

A flowchart should be checked before relying on its implementation.

### Step 1: Check the Starting Point

Ensure the process has a clear start.

### Step 2: Follow the Arrows

Trace the instructions in their specified order.

### Step 3: Check Decisions

Verify that all relevant outcomes are covered.

### Step 4: Check Loop Termination

Ensure the loop has a suitable stopping condition.

### Step 5: Try Sample Inputs

Manually work through the algorithm using selected values.

### Step 6: Compare with Python Output

The program's behavior should match the logic represented in the flowchart.

### Step 7: Test Edge Cases

Examples include:

- Zero.
- Negative numbers.
- Equal values.
- Empty collections.
- Boundary values.
- Targets that are not present.

---

## 17. Common Beginner Mistakes

### Mistake 1: Missing a Decision Branch

A conditional flowchart may be incomplete if one possible outcome has no appropriate path.

### Mistake 2: Incorrect Loop Condition

An incorrect boundary may produce one extra or one fewer iteration.

### Mistake 3: Infinite Loops

A loop may fail to terminate if its controlling condition never becomes False.

### Mistake 4: Using the Wrong Formula

A flowchart can be logically arranged but still produce an incorrect answer if its calculation is wrong.

### Mistake 5: Forgetting to Update a Variable

Many loops depend on updating a counter or other variable.

### Mistake 6: Not Testing Edge Cases

A solution may work for one normal example but fail for zero, negative values, or other valid boundary cases.

### Mistake 7: Confusing a Value with an Index

Linear search in Python usually returns a zero-based index, not the value itself.

---

## 18. Important Terminology

| Term | Meaning |
|---|---|
| Flowchart | Visual representation of an algorithm |
| Input | Information provided to a solution |
| Output | Result produced by a solution |
| Process | Calculation or operation |
| Decision | Condition that selects a path |
| Loop | Repeated execution of instructions |
| Iteration | One execution of a loop body |
| Counter | Variable used to track progress |
| Accumulator | Variable used to collect a result |
| Linear search | Checks elements one by one |
| Dry run | Manually tracing an algorithm |
| Edge case | Boundary or unusual valid input |
| Time complexity | Growth in computational work |
| Auxiliary space | Additional memory used by an algorithm |

---

## 19. Interview Questions

### Q1. What is the purpose of a flowchart?

A flowchart represents the logic and execution order of a process visually.

### Q2. Which symbol represents a decision?

A diamond.

### Q3. Which symbol represents a calculation?

A rectangle.

### Q4. What is the purpose of a loop?

A loop repeats a block of instructions according to its iteration rules or condition.

### Q5. What is the difference between a decision and a loop?

A decision selects a path based on a condition. A loop repeats operations until the required termination condition is met or its iterable is exhausted.

### Q6. What is a dry run?

A dry run is the manual tracing of an algorithm using sample values to verify its behavior.

### Q7. How can a flowchart be tested?

Trace its paths using sample inputs, check each condition and loop, and verify the expected output.

### Q8. What is an off-by-one error?

It is an error where an algorithm executes one more or one fewer iteration than intended.

### Q9. What is the time complexity of linear search in the worst case?

`O(n)` because the algorithm may inspect every element.

### Q10. Why should every loop be checked for termination?

A loop that never terminates can prevent the algorithm from completing its task.

### Q11. Why are edge cases important?

They help determine whether the solution handles boundary and unusual inputs correctly.

### Q12. How do flowcharts help before coding?

They help organize the logic and identify missing steps or incorrect branches before implementation.

---

## 20. Practice Questions

Draw the flowchart first, then implement it in Python.

### Beginner Level

**Question 1:** Display a welcome message containing the user's name.

**Question 2:** Add two input numbers.

**Question 3:** Determine whether a number is positive, negative, or zero.

**Question 4:** Check whether an integer is even or odd.

**Question 5:** Find the largest of three numbers.

### Intermediate Level

**Question 6:** Calculate the sum of integers from 1 through N.

**Question 7:** Display the multiplication table of a number.

**Question 8:** Calculate the factorial of a non-negative integer.

**Question 9:** Count the digits of an integer.

**Question 10:** Find a target in a list using linear search.

**Question 11:** Count the even and odd elements in a list.

**Question 12:** Determine whether a number is divisible by both 3 and 5.

### Challenge

**Question 13:** Draw a flowchart to find the smallest of three numbers.

**Question 14:** Draw a flowchart to calculate the sum of digits of an integer.

**Question 15:** Draw a flowchart to reverse an integer.

**Question 16:** Draw a flowchart to find the largest value in a list.

**Question 17:** Draw a flowchart that processes numbers until a sentinel value is entered.

**Question 18:** Draw a flowchart using nested loops to print a square pattern.

For each challenge:

1. Identify the input and expected output.
2. Write the algorithm.
3. Draw the flowchart.
4. Implement the logic in Python.
5. Test multiple inputs.
6. Record time and auxiliary space complexity where appropriate.

---

## 21. Learning Checklist

- [ ] Understand input and output flowcharts.
- [ ] Use process symbols correctly.
- [ ] Create decision-based flowcharts.
- [ ] Create loop-based flowcharts.
- [ ] Combine decisions and loops.
- [ ] Write algorithms before coding.
- [ ] Implement flowchart logic in Python.
- [ ] Perform a dry run.
- [ ] Test edge cases.
- [ ] Recognize common logical mistakes.
- [ ] Explain basic time complexity.
- [ ] Solve the practice questions.

---

## 22. Final Review

The Practice Flowcharts topic combines the concepts learned throughout the Flowcharts section.

You should now be able to create a flowchart for a basic problem, implement it in Python, and verify that both use the same logic.

Remember the core approach:

**Understand → Plan → Draw → Implement → Test**

---

## Files in This Folder

| File | Purpose |
|---|---|
| `05_practice_flowcharts.py` | Practical examples combining input/output, decisions, and loops |
| `README.md` | Detailed notes, diagrams, algorithms, explanations, interview questions, and practice problems |

---

## Conclusion

Flowcharts are most useful when you apply them to complete problems.

Practise writing algorithms, drawing the correct symbols, tracing the arrows, implementing the logic in Python, and testing different inputs.

Completing these exercises will establish a foundation for more advanced programming and Data Structures and Algorithms.