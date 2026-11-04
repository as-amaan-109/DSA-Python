# Introduction to Loops in Python

## 1. Introduction

Loops are one of the most important concepts in Python programming.

A loop allows a programmer to execute a block of code repeatedly while a particular condition is satisfied or while there are elements available in a sequence.

Without loops, programmers would need to write the same instructions multiple times whenever a task requires repetition.

For example, suppose you want to print the numbers from 1 to 100.

One approach would be to write 100 separate print statements.

However, this approach is inefficient, difficult to maintain, and unnecessarily increases the size of the program.

Loops solve this problem by allowing us to write a single block of code that executes repeatedly.

Python provides two primary looping statements:

1. `for` loop
2. `while` loop

Both loops help execute repeated instructions, but their usage depends on the problem being solved.

Loops are widely used in:
- Calculations.
- Number-based programs.
- Data processing.
- Searching and sorting.
- Pattern printing.
- List and string operations.
- File processing.
- Data Structures and Algorithms.
- Automation.
- Software development.

Understanding loops is essential before learning nested loops, functions, lists, searching, sorting, and other DSA topics.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

1. Define a loop in Python.
2. Explain why loops are required.
3. Understand the meaning of iteration.
4. Identify repetitive tasks.
5. Understand the basic working of a `for` loop.
6. Understand the basic working of a `while` loop.
7. Identify loop initialization.
8. Identify loop conditions.
9. Understand loop updates.
10. Use `range()` with a loop.
11. Print numbers in ascending order.
12. Print numbers in descending order.
13. Display even and odd numbers.
14. Calculate sums using loops.
15. Generate multiplication tables.
16. Iterate through strings.
17. Iterate through lists.
18. Understand the basic concept of nested loops.
19. Understand the purpose of the `break` statement.
20. Identify infinite loops.
21. Avoid common looping mistakes.
22. Solve beginner-level programming problems using loops.

---

## 3. What Is a Loop?

A loop is a programming control structure that executes a block of statements repeatedly.

The statements inside a loop are called the loop body.

Each execution of the loop body is known as an iteration.

A loop generally works through three important components:

1. Initialization.
2. Condition.
3. Update.

These components are particularly visible in a `while` loop.

### Example

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

### Explanation

The variable `number` is initialized with the value `1`.

Python checks whether `number <= 5`.

If the condition is true, the loop body executes.

The value is printed.

The statement `number += 1` increases the value by one.

The condition is checked again.

This process continues until the condition becomes false.

When `number` becomes `6`, the condition `number <= 5` is false and the loop terminates.

---

## 4. Why Are Loops Required?

Loops are required whenever a program needs to repeat a particular operation.

Consider this program without a loop:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Output:

```text
1
2
3
4
5
```

Now consider the same task using a loop:

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

Both programs produce the same output.

However, the second approach is shorter and easier to modify.

### Advantages of loops

- Reduce code duplication.
- Improve readability.
- Simplify repetitive operations.
- Reduce maintenance effort.
- Help process collections of data.
- Make mathematical calculations easier.
- Support algorithm implementation.
- Make programs more flexible.

### Practical example

Suppose a college application needs to calculate the marks of 100 students.

Instead of writing separate calculation statements for every student, a loop can process each student's marks.

This makes the program easier to maintain and extend.

---

## 5. Important Loop Terminology

### 5.1 Loop

A control structure that repeats a block of instructions.

### 5.2 Iteration

One complete execution of the loop body.

### 5.3 Loop Body

The indented statements executed during each iteration.

### 5.4 Initialization

The starting value assigned to a loop-control variable.

### 5.5 Condition

An expression that determines whether a loop should continue.

### 5.6 Update

A change made to a variable that controls loop execution.

### 5.7 Loop Termination

The point at which the loop stops executing.

### 5.8 Infinite Loop

A loop that continues indefinitely because its termination condition is never reached.

### 5.9 Nested Loop

A loop written inside another loop.

### 5.10 Control Variable

A variable used to control the execution of a loop.

---

## 6. Types of Loops in Python

Python provides two primary loop statements.

### 6.1 For Loop

A `for` loop is used to iterate over the elements of an iterable object.

Common iterable objects include:

- Strings.
- Lists.
- Tuples.
- Sets.
- Dictionaries.
- Range objects.

Example:

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

The loop takes each value generated by `range()` and assigns it to `number`.

The loop body executes once for each generated value.

### 6.2 While Loop

A `while` loop repeatedly executes its body as long as its condition remains true.

Example:

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

The condition is checked before each iteration.

When the condition becomes false, the loop stops.

---

## 7. Difference Between For Loop and While Loop

| Feature | For Loop | While Loop |
|---|---|---|
| Basic purpose | Iteration over an iterable | Repetition based on a condition |
| Common use | Processing a sequence | Repeating until a condition changes |
| Initialization | Often handled by the iterable | Usually written before the loop |
| Condition | Iteration availability | Boolean condition |
| Update | Next iterable item is selected | Usually updated manually |
| Common examples | Lists, strings, ranges | Input validation, condition-based repetition |
| Risk of infinite loop | Less common in normal iteration | More common if the condition never changes |

### For loop example

```python
for number in range(1, 6):
    print(number)
```

### While loop example

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Both programs print the same sequence.

The choice depends on the requirements of the problem.

---

## 8. Basic Syntax of a For Loop

```python
for variable in iterable:
    statement
```

### Explanation

- `for` is the Python loop keyword.
- `variable` receives an item from the iterable.
- `in` connects the variable with the iterable.
- `iterable` supplies the values.
- `:` marks the beginning of the loop body.
- Indented statements form the loop body.

Example:

```python
for letter in "PYTHON":
    print(letter)
```

Output:

```text
P
Y
T
H
O
N
```

Each character is assigned to `letter` during one iteration.

---

## 9. Basic Syntax of a While Loop

```python
while condition:
    statement
    update
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Explanation

- `while` is the loop keyword.
- `condition` is evaluated before each iteration.
- If the condition is true, the body executes.
- If the condition is false, the loop terminates.
- The update changes the condition-control variable.

The update is important whenever the loop depends on a changing variable.

---

## 10. Understanding Loop Initialization, Condition, and Update

Consider this program:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Initialization

```python
number = 1
```

The variable receives its initial value.

### Condition

```python
number <= 5
```

Python checks whether the current value is less than or equal to five.

### Loop Body

```python
print(number)
```

The current value is printed.

### Update

```python
number += 1
```

The variable increases by one.

### General structure

```text
Initialization
      |
      v
Check condition
      |
      v
Is condition true?
      |
   Yes|       No
      |        |
      v        v
 Execute     Terminate
 loop body    loop
      |
      v
    Update
      |
      |
      └------> Check condition again
```

This structure is useful for understanding how condition-controlled repetition works.

---

## 11. Understanding Iteration

Iteration means one complete execution of a loop body.

Consider:

```python
for number in range(1, 4):
    print(number)
```

Output:

```text
1
2
3
```

The loop performs three iterations.

| Iteration | Value of number | Output |
|---|---:|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |

After the third iteration, there are no more values generated by the range.

Therefore, the loop finishes.

### Important point

The number of iterations depends on the iterable or on the number of times the loop condition remains true.

---

## 12. Understanding the range() Function

The `range()` function creates an immutable sequence of integers.

It is frequently used with `for` loops.

It supports three arguments:

```python
range(start, stop, step)
```

### 12.1 Start

The first value in the sequence.

The default start value is `0`.

### 12.2 Stop

The sequence stops before this value.

The stop value is excluded.

### 12.3 Step

The difference between consecutive values.

The default step value is `1`.

### Example 1: One argument

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

### Example 2: Two arguments

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

### Example 3: Three arguments

```python
for number in range(1, 11, 2):
    print(number)
```

Output:

```text
1
3
5
7
9
```

### Example 4: Negative step

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

### Important range() rules

1. The start value is included.
2. The stop value is excluded.
3. The step determines the interval.
4. The default start value is zero.
5. The default step value is one.
6. A negative step supports descending sequences.
7. A zero step is invalid.
8. `range()` produces an iterable range object.

---

## 13. Positive and Negative Conditions in Loops

A loop condition is a Boolean expression.

It evaluates to either `True` or `False`.

Example:

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

The condition is true while `number` is 1, 2, or 3.

When `number` becomes 4, the condition becomes false.

### Common comparison operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `number == 5` |
| `!=` | Not equal to | `number != 5` |
| `>` | Greater than | `number > 5` |
| `<` | Less than | `number < 5` |
| `>=` | Greater than or equal to | `number >= 5` |
| `<=` | Less than or equal to | `number <= 5` |

### Example

```python
number = 10

while number > 0:
    print(number)
    number -= 2
```

Output:

```text
10
8
6
4
2
```

---

## 14. The Loop Body and Indentation

Python uses indentation to identify the statements belonging to a loop.

Correct example:

```python
for number in range(1, 4):
    print(number)
    print("Loop is running")
```

Both statements are inside the loop.

Output:

```text
1
Loop is running
2
Loop is running
3
Loop is running
```

Incorrect example:

```python
for number in range(1, 4):
print(number)
```

This produces an `IndentationError`.

### Important indentation rules

- Use consistent indentation.
- Four spaces are the standard indentation convention.
- Keep loop-body statements aligned.
- Nested blocks need another indentation level.
- Do not mix indentation styles unnecessarily.

---

## 15. Twelve Topic Examples

This section covers the same twelve examples available in the Python source file.

### Example 1: Print Numbers Using a For Loop

**Objective:** Print numbers from 1 to 5.

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

Explanation:

The `range(1, 6)` expression generates values from 1 through 5.

The loop prints each value.

### Example 2: Print Numbers Using a While Loop

**Objective:** Print numbers from 1 to 5 using a condition-controlled loop.

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

Explanation:

The variable starts at 1.

The loop continues while its value is at most 5.

The update increases it after every iteration.

### Example 3: Print Numbers in Reverse Order

**Objective:** Print numbers from 5 down to 1.

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

Explanation:

The starting value is 5.

The stop value is 0 and is excluded.

The step is -1, so the sequence decreases.

### Example 4: Print Even Numbers

**Objective:** Display even numbers from 1 to 10.

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
```

Output:

```text
2
4
6
8
10
```

Explanation:

An even number is divisible by 2.

The modulo operator `%` returns the remainder.

If the remainder is zero, the number is even.

### Example 5: Print Odd Numbers

**Objective:** Display odd numbers from 1 to 10.

```python
for number in range(1, 11):
    if number % 2 != 0:
        print(number)
```

Output:

```text
1
3
5
7
9
```

Explanation:

An odd number leaves a remainder of 1 when divided by 2.

The condition checks whether the remainder is not zero.

### Example 6: Calculate the Sum Using a Loop

**Objective:** Calculate the sum of numbers from 1 to 5.

```python
total = 0

for number in range(1, 6):
    total += number

print("Sum:", total)
```

Output:

```text
Sum: 15
```

Explanation:

The variable `total` stores the running sum.

Every number is added to it.

At the end, the sum is 15.

### Example 7: Display a Multiplication Table

**Objective:** Display the multiplication table of 5.

```python
for number in range(1, 11):
    print(f"5 x {number} = {5 * number}")
```

Output:

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

Explanation:

The multiplier changes from 1 to 10.

Each iteration calculates the product.

### Example 8: Count Digits Using a While Loop

**Objective:** Count the digits in the number 12345.

```python
number = 12345
temporary = number
digit_count = 0

while temporary > 0:
    temporary //= 10
    digit_count += 1

print("Total digits:", digit_count)
```

Output:

```text
Total digits: 5
```

Explanation:

Integer division by 10 removes the last digit.

The counter increases once for every removed digit.

The loop stops when the remaining number becomes zero.

For zero and negative numbers, additional handling is required. The solved problem later in this README covers those cases.

### Example 9: Iterate Through a String

**Objective:** Display each character of a string.

```python
name = "PYTHON"

for character in name:
    print(character)
```

Output:

```text
P
Y
T
H
O
N
```

Explanation:

A string is iterable.

The loop retrieves one character at a time.

### Example 10: Iterate Through a List

**Objective:** Display each element of a list.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
Orange
```

Explanation:

The loop accesses each list element in sequence.

### Example 11: Using Nested Loops

**Objective:** Display a square pattern with three rows and three columns.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

Explanation:

The outer loop controls the rows.

The inner loop controls the columns.

The inner loop completes its iterations for each outer-loop iteration.

### Example 12: Stop a Loop Using Break

**Objective:** Stop printing when the value becomes 6.

```python
for number in range(1, 11):
    if number == 6:
        break

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

Explanation:

When `number` becomes 6, the `break` statement immediately terminates the loop.

The remaining values are not printed.

---

## 16. Twelve Solved Programming Problems

The following problems correspond to the twelve selectable solutions in the Python source file.

### Problem 1: Print Numbers from 1 to N

**Problem statement:**

Write a Python program to accept an integer N and print all natural numbers from 1 to N.

**Logic:**

1. Read the value of N.
2. Create a loop from 1 through N.
3. Print each number.
4. Stop after reaching N.

**Code:**

```python
n = int(input("Enter the value of N: "))

for number in range(1, n + 1):
    print(number, end=" ")
```

**Sample input:**

```text
Enter the value of N: 5
```

**Sample output:**

```text
1 2 3 4 5
```

**Explanation:**

The stop argument is `n + 1` because the stop value of `range()` is excluded.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 2: Print Numbers in Reverse

**Problem statement:**

Accept a positive integer and display all numbers from that integer down to 1.

**Logic:**

1. Read the starting number.
2. Continue while the number is at least 1.
3. Print the current number.
4. Decrease the number by one.

**Code:**

```python
number = int(input("Enter the starting number: "))

while number >= 1:
    print(number, end=" ")
    number -= 1
```

**Sample input:**

```text
Enter the starting number: 5
```

**Sample output:**

```text
5 4 3 2 1
```

**Explanation:**

The loop starts from the entered number and moves backwards.

The update decreases the value after each iteration.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 3: Sum of Natural Numbers

**Problem statement:**

Calculate the sum of the first N natural numbers.

**Logic:**

1. Accept N.
2. Initialize `total` with zero.
3. Iterate from 1 to N.
4. Add each value to `total`.
5. Display the result.

**Code:**

```python
n = int(input("Enter the value of N: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum:", total)
```

**Sample input:**

```text
Enter the value of N: 5
```

**Sample output:**

```text
Sum: 15
```

**Explanation:**

The calculation is:

```text
1 + 2 + 3 + 4 + 5 = 15
```

The variable `total` stores the running result.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 4: Sum of Even Numbers

**Problem statement:**

Calculate the sum of even numbers from 1 to N.

**Logic:**

1. Read N.
2. Initialize the sum to zero.
3. Start the loop at 2.
4. Increase the loop value by 2.
5. Add each even number to the total.
6. Print the total.

**Code:**

```python
n = int(input("Enter the value of N: "))

total = 0

for number in range(2, n + 1, 2):
    total += number

print("Sum of even numbers:", total)
```

**Sample input:**

```text
Enter the value of N: 10
```

**Sample output:**

```text
Sum of even numbers: 30
```

**Explanation:**

The even numbers are 2, 4, 6, 8, and 10.

Their sum is 30.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 5: Count Odd Numbers

**Problem statement:**

Count the odd numbers between 1 and N.

**Logic:**

1. Read N.
2. Initialize the counter with zero.
3. Iterate through the numbers.
4. Check whether the remainder after division by 2 is not zero.
5. Increase the counter when the condition is true.
6. Print the counter.

**Code:**

```python
n = int(input("Enter the value of N: "))

count = 0

for number in range(1, n + 1):
    if number % 2 != 0:
        count += 1

print("Total odd numbers:", count)
```

**Sample input:**

```text
Enter the value of N: 10
```

**Sample output:**

```text
Total odd numbers: 5
```

**Explanation:**

The odd numbers are 1, 3, 5, 7, and 9.

There are five odd numbers.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 6: Multiplication Table

**Problem statement:**

Accept a number and display its multiplication table from 1 to 10.

**Logic:**

1. Read the number.
2. Start a loop from 1 to 10.
3. Multiply the number by the current multiplier.
4. Display the result.

**Code:**

```python
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
```

**Sample input:**

```text
Enter a number: 7
```

**Sample output:**

```text
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

**Explanation:**

The multiplier changes during every iteration.

The multiplication is performed using the current value.

**Complexity:**

- Time: O(1), because the table always contains ten rows.
- Auxiliary space: O(1).

### Problem 7: Factorial of a Number

**Problem statement:**

Calculate the factorial of a non-negative integer.

The factorial of a positive integer N is the product of all positive integers from 1 to N.

Mathematically:

```text
N! = N × (N - 1) × (N - 2) × ... × 1
```

By definition:

```text
0! = 1
```

**Logic:**

1. Read a non-negative integer.
2. Initialize factorial with 1.
3. Multiply it by every integer from 1 to N.
4. Display the result.

**Code:**

```python
number = int(input("Enter a non-negative number: "))

factorial = 1

for value in range(1, number + 1):
    factorial *= value

print("Factorial:", factorial)
```

**Sample input:**

```text
Enter a non-negative number: 5
```

**Sample output:**

```text
Factorial: 120
```

**Explanation:**

The calculation is:

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

The initial value must be 1 because multiplying by zero would make the result zero.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 8: Count Digits

**Problem statement:**

Write a program to count the number of digits in an integer.

The program should correctly handle zero and negative integers.

**Logic:**

1. Read an integer.
2. Use `abs()` to obtain its non-negative magnitude.
3. If the number is zero, the digit count is one.
4. Otherwise, repeatedly perform integer division by 10.
5. Increase the count after each division.
6. Display the count.

**Code:**

```python
number = int(input("Enter an integer: "))

temporary = abs(number)
count = 0

if temporary == 0:
    count = 1
else:
    while temporary > 0:
        temporary //= 10
        count += 1

print("Total digits:", count)
```

**Sample input 1:**

```text
Enter an integer: 12345
```

**Sample output 1:**

```text
Total digits: 5
```

**Sample input 2:**

```text
Enter an integer: -789
```

**Sample output 2:**

```text
Total digits: 3
```

**Sample input 3:**

```text
Enter an integer: 0
```

**Sample output 3:**

```text
Total digits: 1
```

**Explanation:**

Integer division by ten removes the rightmost digit.

The number of divisions required to reach zero gives the number of digits for a positive integer.

**Complexity:**

- Time: O(D), where D is the number of digits.
- Auxiliary space: O(1).

### Problem 9: Reverse a Number

**Problem statement:**

Accept a non-negative integer and reverse its digits.

**Logic:**

1. Read the number.
2. Initialize `reversed_number` with zero.
3. Extract the last digit using `% 10`.
4. Append the digit to the reversed number.
5. Remove the last digit using `// 10`.
6. Repeat until the original temporary value becomes zero.

**Code:**

```python
number = int(input("Enter a non-negative number: "))

temporary = number
reversed_number = 0

while temporary > 0:
    digit = temporary % 10
    reversed_number = reversed_number * 10 + digit
    temporary //= 10

print("Reversed number:", reversed_number)
```

**Sample input:**

```text
Enter a non-negative number: 12345
```

**Sample output:**

```text
Reversed number: 54321
```

**Explanation:**

The last digit is extracted in each iteration.

That digit is appended to the new number.

Leading zeroes in the reversed result are not preserved because the result is an integer.

**Complexity:**

- Time: O(D), where D is the number of digits.
- Auxiliary space: O(1).

### Problem 10: Calculate Power

**Problem statement:**

Calculate a base raised to a non-negative integer exponent using repeated multiplication.

**Logic:**

1. Read the base.
2. Read a non-negative exponent.
3. Initialize result with 1.
4. Multiply the result by the base for every exponent iteration.
5. Display the answer.

**Code:**

```python
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

for _ in range(exponent):
    result *= base

print("Result:", result)
```

**Sample input:**

```text
Enter the base: 2
Enter the exponent: 4
```

**Sample output:**

```text
Result: 16
```

**Explanation:**

The calculation is:

```text
2 × 2 × 2 × 2 = 16
```

When the exponent is zero, the loop executes zero times and the result remains 1.

**Complexity:**

- Time: O(E), where E is the exponent.
- Auxiliary space: O(1).

### Problem 11: Find the Maximum Number

**Problem statement:**

Accept a list of integers and find its largest value using a loop.

**Logic:**

1. Read the number of elements.
2. Accept all elements.
3. Initialize the maximum with the first element.
4. Compare each element with the current maximum.
5. Update the maximum when a larger element is found.
6. Display the final maximum.

**Code:**

```python
count = int(input("How many numbers? "))

numbers = []

for index in range(count):
    value = int(input("Enter a number: "))
    numbers.append(value)

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Largest number:", maximum)
```

**Sample input:**

```text
How many numbers? 5
Enter a number: 12
Enter a number: 45
Enter a number: 7
Enter a number: 89
Enter a number: 31
```

**Sample output:**

```text
Largest number: 89
```

**Explanation:**

The first list element is used as the initial maximum.

Every remaining element is compared with it.

The maximum changes only when a larger element is found.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(N) for the input list.
- Extra scanning space: O(1).

### Problem 12: Sum Until Zero

**Problem statement:**

Accept numbers repeatedly from the user until zero is entered.

Calculate the sum of all entered numbers except the terminating zero.

**Logic:**

1. Initialize total with zero.
2. Start an indefinite `while` loop.
3. Accept a number.
4. If the number is zero, terminate the loop.
5. Otherwise, add the number to total.
6. Display the final sum.

**Code:**

```python
total = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    total += number

print("Final sum:", total)
```

**Sample input:**

```text
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 0
```

**Sample output:**

```text
Final sum: 60
```

**Explanation:**

The loop continues until the user enters zero.

The `break` statement terminates the loop immediately.

Zero is not added to the sum.

**Complexity:**

- Time: O(N), where N is the number of non-zero inputs.
- Auxiliary space: O(1).

---

## 17. Ten Unsolved Practice Questions

Attempt these questions independently before checking solutions elsewhere.

### Question 1: Multiples of Three

Write a program to print all multiples of 3 from 1 to N.

Example:

```text
Input:
N = 15

Expected output:
3 6 9 12 15
```

### Question 2: Sum of Digits

Write a program to calculate the sum of all digits of a number.

Example:

```text
Input:
1234

Expected output:
10
```

### Question 3: Palindrome Number

Write a program to check whether a number is a palindrome.

Example:

```text
Input:
121

Expected output:
Palindrome
```

### Question 4: Prime Number

Write a program to check whether a number is prime.

Example:

```text
Input:
7

Expected output:
Prime number
```

### Question 5: Fibonacci Series

Write a program to print the Fibonacci series up to N terms.

Example:

```text
Input:
N = 7

Expected output:
0 1 1 2 3 5 8
```

### Question 6: Count Vowels

Write a program to count the number of vowels in a string using a loop.

Example:

```text
Input:
"education"

Expected output:
5
```

### Question 7: Find the Smallest Number

Write a program to find the smallest number in a list using a loop.

Example:

```text
Input:
[12, 4, 19, 2, 8]

Expected output:
2
```

### Question 8: Average of N Numbers

Write a program to accept N numbers and calculate their average.

Example:

```text
Input:
10, 20, 30

Expected output:
20.0
```

### Question 9: Factors of a Number

Write a program to print all factors of a given positive integer.

Example:

```text
Input:
12

Expected output:
1 2 3 4 6 12
```

### Question 10: Armstrong Number

Write a program to check whether a number is an Armstrong number.

Example:

```text
Input:
153

Expected output:
Armstrong number
```

---

## 18. Common Mistakes While Using Loops

### Mistake 1: Forgetting to Update the While Loop Variable

Incorrect:

```python
number = 1

while number <= 5:
    print(number)
```

Problem:

The value of `number` never changes.

The condition remains true indefinitely.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Mistake 2: Incorrect Range Stop Value

Incorrect:

```python
for number in range(1, 5):
    print(number)
```

This prints only 1, 2, 3, and 4.

Correct:

```python
for number in range(1, 6):
    print(number)
```

The stop value must be 6 to include 5.

### Mistake 3: Using a Wrong Step Value

Incorrect:

```python
for number in range(1, 10, 0):
    print(number)
```

This raises a `ValueError`.

Correct:

```python
for number in range(1, 10, 1):
    print(number)
```

The step must not be zero.

### Mistake 4: Incorrect Indentation

Incorrect:

```python
for number in range(5):
print(number)
```

Correct:

```python
for number in range(5):
    print(number)
```

### Mistake 5: Infinite While Loop

Incorrect:

```python
number = 10

while number > 0:
    print(number)
    number += 1
```

The value keeps increasing, so the condition remains true.

Correct:

```python
number = 10

while number > 0:
    print(number)
    number -= 1
```

### Mistake 6: Incorrect Loop Boundary

Incorrect:

```python
for number in range(1, 11):
    if number > 10:
        print(number)
```

The condition never becomes true.

Correct:

```python
for number in range(1, 11):
    print(number)
```

### Mistake 7: Initializing a Sum with the Wrong Value

Incorrect:

```python
total = 1

for number in range(1, 6):
    total += number
```

This produces an incorrect sum for the intended task.

Correct:

```python
total = 0

for number in range(1, 6):
    total += number
```

### Mistake 8: Forgetting the Zero Case in Digit Counting

A loop such as:

```python
number = 0
count = 0

while number > 0:
    count += 1
    number //= 10
```

does not execute for zero.

Zero must be handled separately because it contains one digit.

### Mistake 9: Incorrectly Using a Negative Step

Incorrect:

```python
for number in range(1, 6, -1):
    print(number)
```

The starting value and step direction do not produce the intended ascending sequence.

Correct ascending sequence:

```python
for number in range(1, 6, 1):
    print(number)
```

Correct descending sequence:

```python
for number in range(5, 0, -1):
    print(number)
```

### Mistake 10: Confusing Assignment and Comparison

Assignment:

```python
number = 5
```

Comparison:

```python
number == 5
```

A loop condition generally uses comparison or another Boolean expression.

---

## 19. Best Practices for Writing Loops

1. Choose the loop type based on the task.
2. Use a `for` loop when iterating over a known iterable.
3. Use a `while` loop when repetition depends on a condition.
4. Initialize control variables correctly.
5. Ensure that condition-controlled loops can terminate.
6. Use meaningful variable names.
7. Keep loop bodies readable.
8. Avoid unnecessary nested loops.
9. Avoid repeating calculations unnecessarily.
10. Use `range()` carefully.
11. Remember that the stop value is excluded.
12. Use appropriate input validation.
13. Avoid changing a collection unexpectedly while iterating over it.
14. Keep indentation consistent.
15. Test boundary values.
16. Consider zero and negative inputs.
17. Use comments when the logic is not immediately clear.
18. Avoid unnecessary variables.
19. Break large problems into smaller steps.
20. Analyze the time complexity of repeated operations.

---

## 20. Debugging Loop Problems

Debugging means finding and correcting errors in a program.

Loop errors can be difficult to identify when the loop repeats many times.

The following techniques can help.

### 20.1 Print the Control Variable

```python
number = 1

while number <= 5:
    print("Current value:", number)
    number += 1
```

This shows the changing value during execution.

### 20.2 Check the Condition

Ask these questions:

- Is the condition correct?
- Can it become false?
- Is the correct comparison operator used?
- Is the loop boundary correct?

### 20.3 Check the Update

Confirm that the control variable changes in the required direction.

### 20.4 Test Small Inputs

Start with simple values such as:

```text
0
1
2
5
10
```

Small inputs make incorrect behavior easier to identify.

### 20.5 Test Boundary Conditions

For number-based problems, test:

- Zero.
- One.
- A negative number where supported.
- The smallest valid input.
- The largest practical input.

### 20.6 Read Error Messages

Common errors include:

| Error | Possible reason |
|---|---|
| `SyntaxError` | Invalid Python syntax |
| `IndentationError` | Incorrect indentation |
| `ValueError` | Invalid conversion or argument |
| `NameError` | Variable not defined |
| `TypeError` | Unsupported operation between types |

---

## 21. Real-Life Applications of Loops

Loops are used in many everyday applications.

### 21.1 Student Marks Processing

A college management system can use loops to process the marks of multiple students.

### 21.2 Attendance Management

A program can iterate through student records to calculate attendance percentages.

### 21.3 Banking Applications

A program can process multiple transactions or account records.

### 21.4 E-Commerce Applications

An online shopping application can iterate through product lists and cart items.

### 21.5 Data Processing

Loops can process records from files and datasets.

### 21.6 Automation

Scripts can repeat routine tasks such as renaming files or processing records.

### 21.7 Web Applications

Loops can generate repeated elements such as product cards and table rows.

### 21.8 Games

Loops can repeatedly update game states and process events.

### 21.9 Pattern Printing

Nested loops can generate star patterns, number patterns, and grids.

### 21.10 Data Analysis

Loops can process values and calculate statistics.

---

## 22. Connection Between Loops and Data Structures and Algorithms

Loops form the foundation of many Data Structures and Algorithms concepts.

Before learning DSA, a programmer should understand iteration properly.

### 22.1 Array Traversal

An array or list can be traversed using a loop.

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

### 22.2 Finding the Maximum Element

```python
numbers = [12, 45, 7, 89, 31]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
```

### 22.3 Linear Search

Linear search checks elements one by one.

```python
numbers = [10, 20, 30, 40, 50]

target = 30
found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
```

### 22.4 Sum of Array Elements

```python
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)
```

### 22.5 Nested Loops and Pair Comparisons

Nested loops can be used to examine pairs of elements.

```python
numbers = [1, 2, 3]

for first in numbers:
    for second in numbers:
        print(first, second)
```

This produces every ordered pair.

### 22.6 Searching Algorithms

Many searching algorithms use loops to examine elements or update search boundaries.

### 22.7 Sorting Algorithms

Algorithms such as Bubble Sort and Selection Sort use repeated comparisons and loop iterations.

### 22.8 Two-Pointer Techniques

Some array and string problems use loops with two indices moving through a sequence.

### 22.9 Sliding Window

Sliding window algorithms use loops to move a window across an array or string.

### 22.10 Complexity Analysis

The number of loop iterations is an important factor in determining time complexity.

Understanding loop behavior is therefore essential for DSA interviews and coding assessments.

---

## 23. Introduction to Time and Space Complexity

Time complexity describes how the running time of an algorithm grows as the input size increases.

Space complexity describes how memory usage grows as the input size increases.

Loops are frequently used when estimating time complexity.

### 23.1 Constant Number of Iterations

```python
for number in range(10):
    print(number)
```

The loop always executes ten times.

Time complexity: O(1).

### 23.2 Linear Loop

```python
for number in range(n):
    print(number)
```

The number of iterations grows with N.

Time complexity: O(N).

### 23.3 Nested Loop

```python
for first in range(n):
    for second in range(n):
        print(first, second)
```

The inner loop executes N times for each outer-loop iteration.

Total iterations:

```text
N × N = N²
```

Time complexity: O(N²).

### 23.4 Consecutive Loops

```python
for number in range(n):
    print(number)

for number in range(n):
    print(number)
```

Total iterations:

```text
N + N = 2N
```

Ignoring constant factors:

Time complexity: O(N).

### 23.5 Logarithmic Loop

```python
number = n

while number > 1:
    number //= 2
```

The value is reduced approximately by half during each iteration.

For positive N greater than one, the number of iterations grows logarithmically.

Time complexity: O(log N).

### Complexity reference

| Loop pattern | Time complexity |
|---|---|
| Fixed number of iterations | O(1) |
| One loop through N elements | O(N) |
| Two nested loops of size N | O(N²) |
| Three nested loops of size N | O(N³) |
| Repeated halving | O(log N) |
| Outer linear loop with logarithmic inner work | O(N log N) |

### Important note

These complexities describe common loop structures.

The exact complexity depends on the number of iterations and the work performed inside the loop body.

A single loop does not automatically mean O(N). Its actual behavior depends on its iteration count.

---

## 24. Mini Project: Number Analysis Program

### Project Objective

Create a simple program that accepts a positive integer and displays different properties using loops.

The program should:

1. Print numbers from 1 to N.
2. Display even numbers.
3. Display odd numbers.
4. Calculate the sum of natural numbers.
5. Count the digits.
6. Display the reverse of the number.

### Project Code

```python
"""
Project: Number Analysis Program

Description:
Analyze a positive integer using basic Python loops.
"""


def analyze_number(number: int) -> None:
    if number <= 0:
        print("Please enter a positive integer.")
        return

    print("\nNumbers from 1 to N:")

    for value in range(1, number + 1):
        print(value, end=" ")

    print("\n\nEven numbers:")

    for value in range(1, number + 1):
        if value % 2 == 0:
            print(value, end=" ")

    print("\n\nOdd numbers:")

    for value in range(1, number + 1):
        if value % 2 != 0:
            print(value, end=" ")

    total = 0

    for value in range(1, number + 1):
        total += value

    print("\n\nSum of natural numbers:", total)

    temporary = number
    digit_count = 0
    reversed_number = 0

    while temporary > 0:
        digit = temporary % 10
        reversed_number = reversed_number * 10 + digit
        temporary //= 10
        digit_count += 1

    print("Number of digits:", digit_count)
    print("Reversed number:", reversed_number)


def main() -> None:
    try:
        number = int(input("Enter a positive integer: "))
        analyze_number(number)

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter a positive integer: 10
```

### Sample Output

```text
Numbers from 1 to N:
1 2 3 4 5 6 7 8 9 10

Even numbers:
2 4 6 8 10

Odd numbers:
1 3 5 7 9

Sum of natural numbers: 55
Number of digits: 2
Reversed number: 1
```

### Project Concepts Used

- Input and output.
- Integer conversion.
- `for` loops.
- `while` loops.
- Conditions.
- Modulo operator.
- Integer division.
- Variables.
- Functions.
- Basic exception handling.

### Possible Improvements

1. Add a multiplication-table option.
2. Add factorial calculation.
3. Add prime-number checking.
4. Add palindrome checking.
5. Add a menu for selecting individual operations.
6. Add more input validation.

---

## 25. Fifty Viva Questions and Answers

### Basic Questions

**Q1. What is a loop in Python?**

A loop is a control structure that executes a block of code repeatedly.

**Q2. Why are loops used?**

Loops reduce code repetition and make repetitive operations easier to implement.

**Q3. What are the two primary types of loops in Python?**

The two primary types are `for` loops and `while` loops.

**Q4. What is iteration?**

Iteration is one complete execution of a loop body.

**Q5. What is a loop body?**

The loop body contains the statements that execute during each iteration.

**Q6. What is a loop condition?**

A loop condition is a Boolean expression that determines whether a condition-controlled loop should continue.

**Q7. What is initialization?**

Initialization means assigning the initial value to a variable before using it in a loop.

**Q8. What is a loop update?**

An update changes a loop-control variable during execution.

**Q9. What is an infinite loop?**

An infinite loop is a loop that continues without reaching its termination condition.

**Q10. What is a nested loop?**

A nested loop is a loop written inside another loop.

### For Loop Questions

**Q11. What is a `for` loop?**

A `for` loop iterates over the elements of an iterable.

**Q12. What is an iterable?**

An iterable is an object from which elements can be obtained one at a time.

**Q13. Name some Python iterables.**

Strings, lists, tuples, sets, dictionaries, and range objects are common iterables.

**Q14. What is the purpose of the `in` keyword in a `for` loop?**

It connects the loop variable with the iterable.

**Q15. Can a `for` loop iterate through a string?**

Yes. A string provides its characters one at a time.

**Q16. Can a `for` loop iterate through a list?**

Yes. It can process every element in a list.

**Q17. What happens when an iterable has no elements?**

The loop body does not execute.

**Q18. Does a `for` loop always need `range()`?**

No. It can directly iterate over an iterable such as a list or string.

**Q19. What is the advantage of a `for` loop?**

It provides a convenient way to process elements of an iterable.

**Q20. Can a `for` loop be used with a tuple?**

Yes. Tuples are iterable.

### While Loop Questions

**Q21. What is a `while` loop?**

A `while` loop executes its body while its condition evaluates to true.

**Q22. When is a `while` loop useful?**

It is useful when repetition depends on a condition rather than simply processing an iterable.

**Q23. Is the condition checked before every iteration?**

Yes. Python evaluates the condition before executing each iteration.

**Q24. What happens if a `while` condition is initially false?**

The loop body does not execute.

**Q25. Why is updating the loop variable important?**

An appropriate update can move the program toward the termination condition.

**Q26. Can a `while` loop run forever?**

Yes, if it never reaches a false condition or is not otherwise terminated.

**Q27. What is `while True`?**

It creates a loop with a condition that is always true. It generally needs a suitable exit mechanism.

**Q28. Can a `while` loop process user input repeatedly?**

Yes. It is commonly used for repeated input and validation.

**Q29. What is the difference between `while` and `if`?**

An `if` statement checks a condition and executes its block when true. A `while` statement repeats its block while the condition remains true.

**Q30. What is one common mistake in a `while` loop?**

Forgetting to update a variable that controls the loop condition.

### Range Function Questions

**Q31. What is the `range()` function?**

It creates an immutable sequence of integers.

**Q32. What is the default start value of `range()`?**

The default start value is 0.

**Q33. Is the stop value included in `range()`?**

No. The stop value is excluded.

**Q34. What is the default step value?**

The default step value is 1.

**Q35. Can `range()` generate descending numbers?**

Yes. A negative step can generate descending values.

**Q36. Can the step value be zero?**

No. A zero step raises a `ValueError`.

**Q37. What does `range(5)` generate?**

It represents the values 0, 1, 2, 3, and 4.

**Q38. What does `range(1, 6)` generate?**

It represents the values 1, 2, 3, 4, and 5.

**Q39. What does `range(2, 11, 2)` generate?**

It represents the even numbers 2, 4, 6, 8, and 10.

**Q40. What does `range(5, 0, -1)` generate?**

It represents the values 5, 4, 3, 2, and 1.

### Programming and DSA Questions

**Q41. What is the purpose of the `break` statement?**

It terminates the nearest enclosing loop immediately.

**Q42. Which operator can be used to check whether a number is even?**

The modulo operator `%` can be used. A number is even when `number % 2 == 0`.

**Q43. How can you calculate the sum of numbers using a loop?**

Initialize a total to zero and add each number to it during iteration.

**Q44. How can you count the digits of a positive integer using a loop?**

Repeatedly divide the number by 10 using integer division and increment a counter.

**Q45. How can a multiplication table be generated using loops?**

Iterate through the required multipliers and multiply each one by the given number.

**Q46. What is time complexity?**

Time complexity describes how an algorithm's running time grows with its input size.

**Q47. What is the time complexity of a loop that executes N times?**

Its time complexity is generally O(N) when each iteration performs constant-time work.

**Q48. What is the time complexity of two nested loops that each execute N times?**

It is generally O(N²) when the inner work is constant time.

**Q49. Why are loops important in DSA?**

They are used to traverse data structures, perform comparisons, search for elements, sort data, and implement algorithms.

**Q50. What should you understand before learning advanced loop-based DSA problems?**

You should understand iteration, conditions, updates, loop termination, nested loops, and complexity analysis.

---

## 26. Important Terminology for Revision

| Term | Meaning |
|---|---|
| Loop | Repeated execution of statements |
| Iteration | One execution of a loop body |
| Loop Body | Statements executed inside a loop |
| Initialization | Starting value assignment |
| Condition | Expression controlling repetition |
| Update | Modification of a control variable |
| Termination | Ending of loop execution |
| Infinite Loop | Loop that does not terminate normally |
| Nested Loop | Loop inside another loop |
| Iterable | Object that provides elements for iteration |
| Iterator | Object that represents iteration over an iterable |
| `for` | Iterable-based loop statement |
| `while` | Condition-controlled loop statement |
| `range()` | Function that produces a sequence of integers |
| `break` | Statement that terminates the nearest loop |
| `continue` | Statement that skips to the next loop iteration |
| `pass` | Null statement that performs no action |
| Counter | Variable used to count occurrences or iterations |
| Accumulator | Variable used to collect a running result |
| Modulo | Operator that returns a remainder |
| Integer Division | Division using `//` |
| Complexity | Measure of algorithm growth |

---

## 27. Quick Revision Notes

### Loop Fundamentals

- A loop repeats a block of code.
- One complete execution is an iteration.
- Python has `for` and `while` loop statements.
- Loops reduce code duplication.
- Loop bodies are identified by indentation.

### For Loop

```python
for value in iterable:
    statement
```

Use it to process elements of an iterable.

### While Loop

```python
while condition:
    statement
```

Use it to repeat operations while a condition remains true.

### Range Function

```python
range(start, stop, step)
```

Remember:

- Start is included.
- Stop is excluded.
- Step controls the interval.
- The default start is 0.
- The default step is 1.
- Step cannot be zero.

### Important Operators

| Operator | Use |
|---|---|
| `%` | Find the remainder |
| `//` | Integer division |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `==` | Compare equality |
| `!=` | Compare inequality |

### Common Loop Patterns

Print numbers:

```python
for number in range(1, 6):
    print(number)
```

Calculate a sum:

```python
total = 0

for number in range(1, 6):
    total += number
```

Count iterations:

```python
count = 0

for number in range(1, 6):
    count += 1
```

Reverse a sequence:

```python
for number in range(5, 0, -1):
    print(number)
```

Condition-controlled repetition:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

---

## 28. Learning Checklist

Use this checklist to assess your understanding.

### Fundamentals

- [ ] I understand what a loop is.
- [ ] I understand why loops are needed.
- [ ] I understand the meaning of iteration.
- [ ] I can identify a loop body.
- [ ] I understand initialization.
- [ ] I understand conditions and updates.

### For Loops

- [ ] I can write a basic `for` loop.
- [ ] I can iterate through a string.
- [ ] I can iterate through a list.
- [ ] I understand how `range()` works.
- [ ] I can print numbers in ascending order.
- [ ] I can print numbers in descending order.

### While Loops

- [ ] I can write a basic `while` loop.
- [ ] I can write a correct loop condition.
- [ ] I can update a loop-control variable.
- [ ] I can recognize an infinite loop.
- [ ] I can make a loop terminate correctly.

### Problem Solving

- [ ] I can calculate the sum of natural numbers.
- [ ] I can display even numbers.
- [ ] I can display odd numbers.
- [ ] I can count digits.
- [ ] I can reverse a number.
- [ ] I can calculate factorial.
- [ ] I can find the maximum element in a list.
- [ ] I can use `break` to terminate a loop.

### DSA Preparation

- [ ] I understand linear iteration.
- [ ] I understand basic nested loops.
- [ ] I can estimate the complexity of a simple loop.
- [ ] I understand why loops are important in DSA.

---

## 29. How to Run the Python File

### Step 1: Open the Repository

Open your `DSA-Python` repository in VS Code.

### Step 2: Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 01-Introduction-to-Loops/
            ├── README.md
            └── 01_introduction_to_loops.py
```

### Step 3: Open the Terminal

Open the VS Code integrated terminal.

### Step 4: Run the Python File

From the repository root, execute:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/01-Introduction-to-Loops/01_introduction_to_loops.py
```

### Step 5: Select a Menu Option

The program displays:

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Enter the option you want to explore.

---

## 30. Repository Structure

```text
DSA-Python/
│
└── PYTHON/
    │
    └── Python-Fundamentals/
        │
        └── 01-Loops/
            │
            ├── README.md
            │
            └── 01-Introduction-to-Loops/
                │
                ├── README.md
                │
                └── 01_introduction_to_loops.py
```

### File Responsibilities

**README.md**

This document contains:

- Topic introduction.
- Learning objectives.
- Loop concepts and syntax.
- Twelve topic examples.
- Twelve solved problems.
- Ten unsolved practice questions.
- Common mistakes.
- Best practices.
- Debugging guidance.
- Real-life applications.
- DSA connections.
- Complexity analysis.
- Mini project.
- Fifty viva questions and answers.
- Revision notes.
- Learning checklist.
- Execution instructions.

**01_introduction_to_loops.py**

This Python file contains:

- Twelve executable topic examples.
- Twelve selectable solved problems.
- Ten unsolved practice questions.
- Learning checklist.
- Interactive menu.
- Input validation.

---

## 31. Final Summary

Loops are fundamental control structures in Python.

They allow programmers to repeat instructions without writing the same code multiple times.

Python provides two primary loop statements:

- `for` loop.
- `while` loop.

A `for` loop is commonly used to iterate through an iterable.

A `while` loop is commonly used when repetition depends on a condition.

The `range()` function helps generate integer sequences for iteration.

Understanding initialization, conditions, updates, iteration, and termination is important for writing correct loops.

Loops are also essential for learning Data Structures and Algorithms because many algorithms depend on repeated traversal, comparison, searching, and processing.

### What You Should Do Next

1. Understand the difference between `for` and `while`.
2. Run the Python source file.
3. Execute all twelve topic examples.
4. Try every solved problem.
5. Attempt all ten unsolved practice questions independently.
6. Complete the learning checklist.
7. Revise the fifty viva questions.
8. Make sure you can explain the logic behind each program.

**Topic Completed: Introduction to Loops**

The next topic in this repository is:

`02-For-Loop`

Its Python source file will be:

`02_for_loop.py`
