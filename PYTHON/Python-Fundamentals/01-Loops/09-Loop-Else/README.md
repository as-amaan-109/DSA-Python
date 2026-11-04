# Topic 09 – Loop Else in Python

**Part 2:** Python Fundamentals  
**Section:** 01 – Loops  
**Topic Number:** 09  
**Source File:** `09_loop_else.py`  
**Language:** Python 3.9+

---

# Table of Contents

1. Introduction to Loop Else
2. Learning Objectives
3. What Is Loop Else?
4. Syntax of Loop Else
5. How Loop Else Works
6. Else with For Loop
7. Else with While Loop
8. Relationship Between Break and Loop Else
9. Relationship Between Continue and Loop Else
10. Loop Else with Empty Iterables
11. Loop Else in Searching
12. Loop Else in Prime Number Checking
13. Loop Else in Nested Loops
14. Loop Else vs If-Else
15. Twelve Topic Examples
16. Twelve Solved Programming Problems
17. Ten Unsolved Practice Questions
18. Common Mistakes
19. Best Practices
20. Debugging Loop Else
21. Real-Life Applications
22. Connection with Data Structures and Algorithms
23. Time and Space Complexity
24. Mini Project – Student Search System
25. Fifty Python Viva Questions and Answers
26. Important Terminology
27. Quick Revision Notes
28. Learning Checklist
29. How to Run the Python File
30. Repository Structure
31. Final Summary

---

# 1. Introduction to Loop Else

Python provides an interesting feature that allows us to use an `else` block with loops.

Normally, we use `else` with conditional statements such as `if-else`.

However, Python also supports `else` with:

- `for` loops
- `while` loops

The loop's `else` block executes when the loop finishes normally without encountering a `break` statement.

This feature is especially useful when:

- Searching for an element in a list.
- Checking whether a number is prime.
- Searching for a student record.
- Checking whether a value exists in a collection.
- Validating a group of records.
- Finding whether a common element exists in two lists.

## Simple Example

```python
for number in range(1, 6):
    print(number)

else:
    print("Loop completed normally.")
```

**Output:**

```text
1
2
3
4
5
Loop completed normally.
```

The loop completes all five iterations without executing `break`.

Therefore, the `else` block executes.

## Example with Break

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)

else:
    print("Loop completed normally.")
```

**Output:**

```text
1
2
```

The `else` block does not execute because the loop terminates using `break`.

## Why Is Loop Else Useful?

Consider a searching problem.

Suppose a list contains five numbers and you want to find a particular number.

You need two possible results:

1. Target found.
2. Target not found.

Loop else gives us a convenient way to handle the second situation.

```python
numbers = [10, 20, 30, 40, 50]
target = 60

for number in numbers:

    if number == target:
        print("Target found.")
        break

else:
    print("Target not found.")
```

**Output:**

```text
Target not found.
```

If the target is found, `break` terminates the loop. Otherwise, the loop finishes normally and its `else` block executes.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand the meaning of loop else.
2. Understand the syntax of loop else.
3. Use else with a for loop.
4. Use else with a while loop.
5. Understand when loop else executes.
6. Understand why break prevents loop else execution.
7. Understand that continue does not prevent loop else execution.
8. Understand else with an empty iterable.
9. Search for elements using for-else.
10. Check prime numbers using loop else.
11. Search through lists and dictionaries.
12. Understand loop else in nested loops.
13. Validate records using loop else.
14. Apply loop else in matrix searching.
15. Differentiate between loop else and if-else.

---

# 3. What Is Loop Else?

Loop else is a Python feature that attaches an `else` block to a `for` or `while` loop.

The `else` block executes when the loop finishes normally without executing `break`.

## Important Definition

**Loop else is an additional block associated with a loop that executes when the loop completes without being terminated by a break statement.**

## Important Characteristics

| Feature | Explanation |
|---|---|
| Used with | For and while loops |
| Main purpose | Execute code after normal loop completion |
| Executes after break? | No |
| Executes after continue? | Yes, if the loop eventually completes normally |
| Executes for an empty iterable? | Yes |
| Can be used in searching? | Yes |
| Can be used in prime checking? | Yes |
| Requires indentation? | Yes |

## Example

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)

else:
    print("All elements processed.")
```

**Output:**

```text
1
2
3
All elements processed.
```

The loop processes every element and finishes without `break`.

---

# 4. Syntax of Loop Else

## 4.1 For Loop Else Syntax

```python
for variable in sequence:

    statement

else:

    else_statement
```

Explanation:

- `for` starts the loop.
- `variable` receives each value.
- `sequence` contains the values to process.
- `statement` executes during each iteration.
- `else` introduces the normal-completion block.

## 4.2 While Loop Else Syntax

```python
while condition:

    statement

else:

    else_statement
```

Explanation:

- `while` checks the condition.
- The loop body executes while the condition is true.
- When the condition becomes false, the loop completes normally.
- The `else` block executes if the loop was not terminated using `break`.

## 4.3 Search Syntax

```python
for item in collection:

    if item == target:
        print("Found")
        break

else:
    print("Not Found")
```

This is one of the most common uses of loop else.

---

# 5. How Loop Else Works

Understanding control flow is important when using loop else.

The `else` block executes only when its associated loop completes without `break`.

## Execution Flow

```text
            Start Loop
                |
                v
        Check Loop Condition
                |
          Is Condition True?
             /       \
           No         Yes
           |           |
           v           v
      Normal Exit   Execute Loop Body
           |           |
           |           v
           |       Encounter break?
           |         /       \
           |       Yes        No
           |        |          |
           |        v          |
           |    Exit Loop      |
           |        |          |
           v        v          |
       Execute Else?            |
           |                    |
           v                    |
          End <-----------------+
```

The key point is that the loop's `else` block is skipped when its associated loop is terminated by `break`.

## Example

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)

else:
    print("Loop completed.")
```

**Output:**

```text
1
2
```

Execution:

1. Number 1 is processed.
2. Number 2 is processed.
3. Number 3 is reached.
4. The break statement executes.
5. The loop terminates.
6. The loop's else block is skipped.

## Normal Completion Example

```python
for number in range(1, 4):
    print(number)

else:
    print("Normal completion.")
```

**Output:**

```text
1
2
3
Normal completion.
```

No break statement terminates the loop, so its else block executes.

---

# 6. Else with For Loop

A `for` loop is used to iterate over a sequence or iterable object.

We can attach an `else` block to it.

## Example 1 – Basic For-Else

```python
for number in range(1, 6):
    print(number)

else:
    print("For loop completed.")
```

**Output:**

```text
1
2
3
4
5
For loop completed.
```

## Example 2 – Search a Number

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:

    if number == target:
        print("Target found:", target)
        break

else:
    print("Target not found.")
```

**Output:**

```text
Target found: 30
```

## Example 3 – Search an Unavailable Number

```python
numbers = [10, 20, 30, 40, 50]
target = 100

for number in numbers:

    if number == target:
        print("Target found.")
        break

else:
    print("Target not found.")
```

**Output:**

```text
Target not found.
```

## Example 4 – Check All Values

```python
numbers = [10, 20, 30, 40]

for number in numbers:

    if number <= 0:
        print("Invalid number.")
        break

else:
    print("All numbers are positive.")
```

**Output:**

```text
All numbers are positive.
```

Here, the loop else block executes because no invalid number is found.

---

# 7. Else with While Loop

The `while` loop can also have an `else` block.

The loop else block executes when the while-loop condition becomes false naturally.

It does not execute if the loop is terminated using break.

## Example 1 – Basic While-Else

```python
count = 1

while count <= 5:
    print(count)
    count += 1

else:
    print("While loop completed.")
```

**Output:**

```text
1
2
3
4
5
While loop completed.
```

## Example 2 – While Loop with Break

```python
count = 1

while count <= 5:

    if count == 3:
        break

    print(count)
    count += 1

else:
    print("Loop completed normally.")
```

**Output:**

```text
1
2
```

The else block does not execute because the loop terminates through break.

## Example 3 – While Loop with Search

```python
numbers = [10, 20, 30, 40]
target = 30

index = 0

while index < len(numbers):

    if numbers[index] == target:
        print("Target found.")
        break

    index += 1

else:
    print("Target not found.")
```

**Output:**

```text
Target found.
```

The loop finds the target and exits using break.

---

# 8. Relationship Between Break and Loop Else

The relationship between `break` and loop else is the most important concept in this topic.

The `break` statement terminates the nearest enclosing loop.

When that loop terminates using break, its own else block does not execute.

## Example

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)

else:
    print("Else block executed.")

print("Program completed.")
```

**Output:**

```text
1
2
Program completed.
```

## Explanation

When number becomes 3, Python executes break.

The loop terminates immediately.

The loop's else block is skipped.

The statement after the complete loop still executes.

## Important Rules

1. Break terminates the nearest enclosing loop.
2. The else block belonging to that loop is skipped.
3. Statements after the loop execute normally.
4. A break in an inner loop does not automatically terminate the outer loop.

---

# 9. Relationship Between Continue and Loop Else

The `continue` statement skips the remaining statements in the current iteration.

It does not terminate the loop.

Therefore, if the loop eventually completes normally, its else block still executes.

## Example

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)

else:
    print("Loop completed without break.")
```

**Output:**

```text
1
2
4
5
Loop completed without break.
```

## Explanation

1. Numbers 1 and 2 are printed.
2. Number 3 is skipped using continue.
3. Numbers 4 and 5 are printed.
4. The loop completes normally.
5. The else block executes.

## Difference

| Statement | Effect on Loop Else |
|---|---|
| Normal completion | Executes |
| break | Does not execute |
| continue | Executes if the loop finishes normally |
| Empty iterable | Executes |

---

# 10. Loop Else with Empty Iterables

An iterable is a collection or sequence that can be traversed using a loop.

Examples:

- Lists
- Tuples
- Strings
- Sets
- Dictionaries
- Ranges

An iterable may also be empty.

When a for loop uses an empty iterable, the loop body does not execute.

However, the loop completes normally, so its else block executes.

## Example

```python
numbers = []

for number in numbers:
    print(number)

else:
    print("No elements were available.")
```

**Output:**

```text
No elements were available.
```

## Empty Tuple Example

```python
values = ()

for value in values:
    print(value)

else:
    print("Tuple is empty.")
```

**Output:**

```text
Tuple is empty.
```

## Empty String Example

```python
text = ""

for character in text:
    print(character)

else:
    print("String is empty.")
```

**Output:**

```text
String is empty.
```

## Important Point

An empty iterable does not mean the loop was terminated by break.

It means the loop had no iterations and completed normally.

---

# 11. Loop Else in Searching

Searching is one of the most common applications of loop else.

The goal is to find a particular value in a collection.

There are two possible outcomes:

1. The target is found.
2. The target is not found.

## Example – Linear Search

```python
numbers = [10, 20, 30, 40, 50]

target = 30

for number in numbers:

    if number == target:
        print("Target found:", target)
        break

else:
    print("Target not found.")
```

**Output:**

```text
Target found: 30
```

## Searching When Target Is Missing

```python
numbers = [10, 20, 30, 40, 50]

target = 100

for number in numbers:

    if number == target:
        print("Target found:", target)
        break

else:
    print("Target not found.")
```

**Output:**

```text
Target not found.
```

## Searching in a String

```python
text = "PYTHON PROGRAMMING"
target = "Z"

for character in text:

    if character == target:
        print("Character found.")
        break

else:
    print("Character not found.")
```

**Output:**

```text
Character not found.
```

## Searching in a Dictionary

```python
students = {
    101: "Amaan",
    102: "Rahul",
    103: "Sneha"
}

target = "Rahul"

for student_id, name in students.items():

    if name == target:
        print("Student ID:", student_id)
        print("Student Name:", name)
        break

else:
    print("Student not found.")
```

**Output:**

```text
Student ID: 102
Student Name: Rahul
```

---

# 12. Loop Else in Prime Number Checking

A prime number is a natural number greater than 1 that has exactly two positive divisors:

- 1
- The number itself

Loop else makes prime-number checking easier.

## Example

```python
number = 13

if number <= 1:
    print("Not a prime number.")

else:
    for divisor in range(2, number):

        if number % divisor == 0:
            print("Not a prime number.")
            break

    else:
        print("Prime number.")
```

**Output:**

```text
Prime number.
```

## Explanation

1. The number is 13.
2. The program checks possible divisors from 2 to 12.
3. No divisor divides 13 exactly.
4. The loop completes normally.
5. The else block executes.
6. The number is identified as prime.

## Optimized Prime Number Checking

We do not need to check every number up to N.

It is sufficient to check possible divisors up to the square root of N.

```python
number = 29

if number <= 1:
    print("Not prime.")

else:
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print("Not prime.")
            break

    else:
        print("Prime.")
```

**Output:**

```text
Prime.
```

## Why Use Square Root?

If a number N has a divisor greater than its square root, it must also have a corresponding divisor smaller than its square root.

Therefore, testing divisors only up to the square root is enough.

This improves the running time of basic trial-division prime checking.

---

# 13. Loop Else in Nested Loops

A nested loop means a loop inside another loop.

In nested loops, indentation determines which loop owns the `else` block.

This is extremely important.

The else block is associated with the nearest preceding loop at the same indentation level.

## Example 1 – Else with Inner Loop

```python
for row in range(1, 4):

    print("Row:", row)

    for column in range(1, 4):

        if column == 2:
            break

        print("Column:", column)

    else:
        print("Inner loop completed normally.")
```

The inner loop's else block will not execute because the inner loop always breaks at column 2.

## Example 2 – Break in Inner Loop, Else in Outer Loop

```python
for row in range(1, 4):

    print("Row:", row)

    for column in range(1, 4):

        if column == 2:
            break

        print("Column:", column)

else:
    print("Outer loop completed normally.")
```

**Output:**

```text
Row: 1
Column: 1
Row: 2
Column: 1
Row: 3
Column: 1
Outer loop completed normally.
```

The inner loop breaks during every row, but the outer loop never executes break.

Therefore, the outer loop completes normally and its else block executes.

## Example 3 – Search in a Matrix

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50
found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

else:
    print("Target not found.")
```

**Important:** In this example, the else block belongs to the outer loop. The outer break is executed after the target is found, preventing the else block from executing.

## Understanding Nested Loop Else

| Break Location | Effect |
|---|---|
| Break in inner loop | Terminates inner loop only |
| Break in outer loop | Terminates outer loop |
| Else on inner loop | Depends on whether inner loop breaks |
| Else on outer loop | Depends on whether outer loop breaks |

---

# 14. Loop Else vs If-Else

Both loop else and conditional else use the keyword `else`, but their purposes are different.

## If-Else Example

```python
number = 10

if number > 0:
    print("Positive")

else:
    print("Not positive")
```

The else block runs when the if condition is false.

## Loop Else Example

```python
for number in range(1, 4):
    print(number)

else:
    print("Loop completed.")
```

The loop else block executes when the loop completes without break.

## Comparison

| Feature | If-Else | Loop Else |
|---|---|---|
| Used with | if statement | for and while loops |
| Main purpose | Choose a conditional branch | Handle normal loop completion |
| Execution condition | If condition is false | Loop finishes without break |
| Affected by break | Not applicable directly | Yes |
| Useful for searching | With additional logic | Yes, directly useful |

---

# 15. Twelve Topic Examples

These examples correspond to the twelve examples in `09_loop_else.py`.

## Example 01 – Basic For Loop Else

**Objective:** Display numbers and print a message after normal loop completion.

```python
for number in range(1, 6):
    print(number)

else:
    print("For loop completed normally.")
```

**Output:**

```text
1
2
3
4
5
For loop completed normally.
```

**Explanation:** The loop completes all iterations without break, so its else block executes.

## Example 02 – Basic While Loop Else

**Objective:** Use else with a while loop.

```python
count = 1

while count <= 5:
    print(count)
    count += 1

else:
    print("While loop completed normally.")
```

**Output:**

```text
1
2
3
4
5
While loop completed normally.
```

**Explanation:** The while condition becomes false naturally.

## Example 03 – Search with Loop Else

**Objective:** Display a message when a target is not found.

```python
numbers = [10, 20, 30, 40, 50]
target = 60

for number in numbers:

    if number == target:
        print("Target found:", target)
        break

else:
    print("Target not found:", target)
```

**Output:**

```text
Target not found: 60
```

**Explanation:** No value matches the target, so the loop finishes normally.

## Example 04 – Break Skips Loop Else

**Objective:** Demonstrate that break prevents loop else execution.

```python
for number in range(1, 6):

    if number == 3:
        print("Break encountered.")
        break

    print(number)

else:
    print("This else block will not execute.")

print("Program continues after the loop.")
```

**Output:**

```text
1
2
Break encountered.
Program continues after the loop.
```

**Explanation:** The loop terminates using break.

## Example 05 – Prime Number Using Else

**Objective:** Check whether 13 is prime using loop else.

```python
number = 13

if number <= 1:
    print(number, "is not a prime number.")

else:
    for divisor in range(2, number):

        if number % divisor == 0:
            print(number, "is not a prime number.")
            break

    else:
        print(number, "is a prime number.")
```

**Output:**

```text
13 is a prime number.
```

**Explanation:** No divisor is found, so the loop completes normally.

## Example 06 – Continue with Loop Else

**Objective:** Demonstrate that continue does not prevent loop else execution.

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)

else:
    print("Loop completed without break.")
```

**Output:**

```text
1
2
4
5
Loop completed without break.
```

**Explanation:** Continue skips number 3, but the loop completes normally.

## Example 07 – Empty Iterable with Else

**Objective:** Use loop else with an empty list.

```python
numbers = []

for number in numbers:
    print(number)

else:
    print("Loop completed. No elements were available.")

print("Program continues.")
```

**Output:**

```text
Loop completed. No elements were available.
Program continues.
```

**Explanation:** The loop has no iterations, but it completes normally.

## Example 08 – Nested Loop Else

**Objective:** Search for a number in each row.

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50

for row_number, row in enumerate(matrix, start=1):

    for value in row:

        if value == target:
            print(f"{target} found in row {row_number}.")
            break

    else:
        print(f"{target} not found in row {row_number}.")
```

**Output:**

```text
50 not found in row 1.
50 found in row 2.
50 not found in row 3.
```

**Explanation:** The inner loop else executes for rows where the target is not found.

## Example 09 – Inner Break and Outer Else

**Objective:** Demonstrate how an inner break affects the outer loop else.

```python
for row in range(1, 4):

    print("Outer row:", row)

    for column in range(1, 4):

        if column == 2:
            print("Inner loop break.")
            break

        print("Column:", column)

else:
    print("Outer loop completed without break.")

print("Program completed.")
```

**Output:**

```text
Outer row: 1
Column: 1
Inner loop break.
Outer row: 2
Column: 1
Inner loop break.
Outer row: 3
Column: 1
Inner loop break.
Outer loop completed without break.
Program completed.
```

**Explanation:** The inner loop breaks, but the outer loop does not. Therefore, the outer loop else executes.

## Example 10 – Find First Even Number

**Objective:** Find the first even number in a list.

```python
numbers = [1, 3, 5, 7, 9, 12, 15]

for number in numbers:

    if number % 2 == 0:
        print("First even number:", number)
        break

else:
    print("No even number found.")
```

**Output:**

```text
First even number: 12
```

**Explanation:** The first even number is found, so break terminates the loop.

## Example 11 – Search in a Dictionary

**Objective:** Search for a student name in a dictionary.

```python
students = {
    101: "Amaan",
    102: "Rahul",
    103: "Sneha",
    104: "Ali"
}

target = "Sneha"

for student_id, name in students.items():

    if name == target:
        print("Student found.")
        print("Student ID:", student_id)
        print("Student Name:", name)
        break

else:
    print("Student not found.")
```

**Output:**

```text
Student found.
Student ID: 103
Student Name: Sneha
```

**Explanation:** The matching student is found and the loop terminates using break.

## Example 12 – Validate Records with Loop Else

**Objective:** Check whether every record is non-empty.

```python
records = ["Amaan", "Rahul", "Sneha", "Ali"]

for record in records:

    if not record.strip():
        print("Invalid record found.")
        break

    print("Valid record:", record)

else:
    print("All records are valid.")
```

**Output:**

```text
Valid record: Amaan
Valid record: Rahul
Valid record: Sneha
Valid record: Ali
All records are valid.
```

**Explanation:** Every record is valid, so the loop completes normally.

---

# 16. Twelve Solved Programming Problems

This section contains twelve solved problems based on loop else.

Each problem includes:

- Problem statement
- Logic
- Python code
- Sample input and output
- Explanation
- Time complexity
- Auxiliary space complexity

## Problem 01 – Search an Element in a List

**Problem Statement:**

Write a Python program to search for a target value in a list using for-else.

If the target is found, display a success message. Otherwise, display a not-found message.

**Logic:**

1. Take the number of list elements.
2. Read the elements.
3. Take the target value.
4. Traverse the list.
5. If the target matches an element, print a message and execute break.
6. If no match is found, execute the loop else block.

**Code:**

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:

    if number == target:
        print("Target found:", target)
        break

else:
    print("Target not found:", target)
```

**Sample Output:**

```text
Target found: 30
```

**Explanation:**

The target 30 is present at the third position. The program finds it and terminates the loop using break.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 02 – Check Prime Number

**Problem Statement:**

Write a program to check whether a number is prime using loop else.

**Logic:**

1. Read an integer.
2. Check whether it is less than or equal to 1.
3. If so, report that it is not prime.
4. Otherwise, check possible divisors up to the square root.
5. If a divisor is found, execute break.
6. If no divisor is found, execute loop else.

**Code:**

```python
number = 29

if number <= 1:
    print("Not a prime number.")

else:
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print("Not a prime number.")
            break

    else:
        print("Prime number.")
```

**Sample Output:**

```text
Prime number.
```

**Explanation:**

No integer divisor is found between 2 and the square root of 29. Therefore, the loop completes normally and its else block executes.

**Complexity:**

- Time Complexity: O(√N)
- Auxiliary Space Complexity: O(1)

## Problem 03 – Find a Negative Number

**Problem Statement:**

Find the first negative number in a list using for-else.

**Logic:**

1. Create a list of integers.
2. Traverse the list.
3. Check whether the current number is negative.
4. If negative, display it and execute break.
5. If the loop completes without finding a negative value, execute else.

**Code:**

```python
numbers = [10, 20, 30, -5, 40]

for number in numbers:

    if number < 0:
        print("First negative number:", number)
        break

else:
    print("No negative number found.")
```

**Sample Output:**

```text
First negative number: -5
```

**Explanation:**

The first negative number is -5. The loop terminates when it finds that value.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 04 – Find First Even Number

**Problem Statement:**

Find the first even number in a list. Display a message if the list contains no even number.

**Logic:**

1. Create a list.
2. Traverse its elements.
3. Check whether a number is divisible by 2.
4. If an even number is found, display it and break.
5. Otherwise, execute else after normal completion.

**Code:**

```python
numbers = [1, 3, 5, 7, 8, 9]

for number in numbers:

    if number % 2 == 0:
        print("First even number:", number)
        break

else:
    print("No even number found.")
```

**Sample Output:**

```text
First even number: 8
```

**Explanation:**

The first even number is 8.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 05 – Search Student Name

**Problem Statement:**

Search for a student name in a list using for-else.

The search should be case-insensitive.

**Logic:**

1. Create a list of student names.
2. Read the target name.
3. Traverse the list.
4. Compare names using casefold.
5. If a match is found, print the result and break.
6. Otherwise, display a not-found message using else.

**Code:**

```python
names = ["Amaan", "Rahul", "Sneha", "Ali"]

target = input("Enter student name: ").strip()

for name in names:

    if name.casefold() == target.casefold():
        print("Student found:", name)
        break

else:
    print("Student not found.")
```

**Sample Input:**

```text
Enter student name: sneha
```

**Sample Output:**

```text
Student found: Sneha
```

**Explanation:**

The comparison ignores differences in uppercase and lowercase letters.

**Complexity:**

- Time Complexity: O(N × L) in terms of N names and their character-comparison cost L.
- Auxiliary Space Complexity: O(1), excluding input representation.

## Problem 06 – Check Whether All Numbers Are Positive

**Problem Statement:**

Write a program to check whether every number in a list is positive.

If any number is zero or negative, display a failure message.

**Logic:**

1. Create a list of numbers.
2. Traverse the list.
3. Check whether the current number is less than or equal to zero.
4. If invalid, display a message and break.
5. If all numbers pass the condition, execute else.

**Code:**

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:

    if number <= 0:
        print("Not all numbers are positive.")
        break

else:
    print("All numbers are positive.")
```

**Sample Output:**

```text
All numbers are positive.
```

**Explanation:**

Every number is greater than zero, so the loop completes without break.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 07 – Find a Divisor

**Problem Statement:**

Find a divisor of a number other than 1 and the number itself.

If no such divisor exists for a number greater than 1, report that the number is prime.

**Logic:**

1. Read a positive integer.
2. Handle the special case of 1.
3. Check divisors from 2 to N-1.
4. If a divisor is found, display it and break.
5. If no divisor is found, execute else.

**Code:**

```python
number = 17

if number == 1:
    print("1 has no divisor other than itself.")

else:
    for divisor in range(2, number):

        if number % divisor == 0:
            print("A divisor was found:", divisor)
            break

    else:
        print("No divisor found other than 1 and itself.")
        print(number, "is prime.")
```

**Sample Output:**

```text
No divisor found other than 1 and itself.
17 is prime.
```

**Explanation:**

No integer between 2 and 16 divides 17 exactly.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 08 – Search an Allowed Password

**Problem Statement:**

Search whether an entered password matches any password in a sample allowed-password list.

**Logic:**

1. Create a list of sample passwords.
2. Read a password.
3. Traverse the list.
4. If a match is found, display success and break.
5. If no match is found, execute loop else.

**Code:**

```python
allowed_passwords = [
    "python123",
    "student456",
    "coding789"
]

entered_password = input("Enter password: ")

for password in allowed_passwords:

    if entered_password == password:
        print("Password matched.")
        break

else:
    print("Password not found in the allowed list.")
```

**Sample Input:**

```text
Enter password: python123
```

**Sample Output:**

```text
Password matched.
```

**Explanation:**

The entered string matches a value in the sample list.

**Security Note:** This is a basic programming exercise, not a secure authentication system. Real applications should use appropriate password hashing, secure storage and authentication mechanisms.

**Complexity:**

- Time Complexity: O(N × L), where N is the number of passwords and L is the comparison length.
- Auxiliary Space Complexity: O(1), excluding the supplied list and input.

## Problem 09 – Check Palindrome

**Problem Statement:**

Check whether a string is a palindrome using loop else.

For this exercise, ignore spaces, punctuation and letter case.

**Logic:**

1. Read a string.
2. Normalize it by keeping letters and digits.
3. Convert letters to a common case.
4. Compare characters from opposite ends.
5. If a mismatch is found, display not-palindrome and break.
6. Otherwise, execute else.

**Code:**

```python
text = input("Enter a string: ")

normalized = "".join(
    character.casefold()
    for character in text
    if character.isalnum()
)

for index in range(len(normalized) // 2):

    if normalized[index] != normalized[-index - 1]:
        print("Not a palindrome.")
        break

else:
    print("Palindrome.")
```

**Sample Input:**

```text
Enter a string: Madam
```

**Sample Output:**

```text
Palindrome.
```

**Explanation:**

After normalization, the string is `madam`. Its first and last characters match, as do its remaining opposing characters.

An empty or single-character normalized string is also treated as a palindrome by this implementation.

**Complexity:**

Let N be the length of the original string.

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(N) for the normalized string.

## Problem 10 – Find Common Element

**Problem Statement:**

Find the first common element between two lists using nested loops and loop else.

**Logic:**

1. Create two lists.
2. Initialize a Boolean flag to False.
3. Traverse the first list.
4. For each element, traverse the second list.
5. If a matching value is found, display it and set the flag to True.
6. Break the inner loop.
7. Check the flag and break the outer loop when a match exists.
8. If the outer loop finishes without break, execute its else block.

**Code:**

```python
first_list = [10, 20, 30, 40]
second_list = [50, 60, 30, 70]

found = False

for first_value in first_list:

    for second_value in second_list:

        if first_value == second_value:
            print("Common element:", first_value)
            found = True
            break

    if found:
        break

else:
    print("No common element found.")
```

**Sample Output:**

```text
Common element: 30
```

**Explanation:**

The value 30 is present in both lists. The inner loop stops when the match is detected, and the outer loop then stops as well.

**Complexity:**

For lists of lengths N and M:

- Time Complexity: O(N × M) in the worst case.
- Auxiliary Space Complexity: O(1).

## Problem 11 – Validate Student Marks

**Problem Statement:**

Check whether all student marks are between 0 and 100, inclusive.

**Logic:**

1. Create a list of marks.
2. Traverse each mark.
3. Check whether a mark is outside the valid range.
4. If an invalid mark is found, display it and break.
5. If the loop finishes without break, execute else.

**Code:**

```python
marks = [80, 90, 70, 60, 100]

for mark in marks:

    if mark < 0 or mark > 100:
        print("Invalid mark detected:", mark)
        break

else:
    print("All student marks are valid.")
```

**Sample Output:**

```text
All student marks are valid.
```

**Explanation:**

Every mark falls within the range 0 to 100.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 12 – Search a Number in a Matrix

**Problem Statement:**

Search for a target number in a two-dimensional matrix using nested loops.

Display its row and column position if found.

**Logic:**

1. Create a matrix.
2. Read the target value.
3. Traverse each row.
4. Traverse each element in that row.
5. If the target is found, display its location and break the inner loop.
6. Use a flag to break the outer loop.
7. If no match is found, execute the outer loop else block.

**Code:**

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50
found = False

for row_index, row in enumerate(matrix):

    for column_index, value in enumerate(row):

        if value == target:
            print("Target found.")
            print("Row:", row_index)
            print("Column:", column_index)

            found = True
            break

    if found:
        break

else:
    print("Target not found in the matrix.")
```

**Sample Output:**

```text
Target found.
Row: 1
Column: 1
```

**Explanation:**

The target 50 is located at row index 1 and column index 1 using zero-based indexing.

**Complexity:**

For a matrix with R rows and C columns:

- Time Complexity: O(R × C)
- Auxiliary Space Complexity: O(1)

---

# 17. Ten Unsolved Practice Questions

Try solving these questions independently using for-else, while-else and break.

## Question 01 – Search an Element

Write a program to check whether a number exists in a list using for-else.

Display an appropriate message when the number is not found.

## Question 02 – Find First Odd Number

Write a program to find the first odd number in a list.

Display a message if no odd number exists.

## Question 03 – Prime Number

Use a for-else loop to check whether a given number is prime.

## Question 04 – Search a Character

Write a program to search for a character in a string using loop else.

## Question 05 – Check Positive Numbers

Take a list of numbers and determine whether all values are positive using break and else.

## Question 06 – Search Student ID

Write a program to search for a student ID in a dictionary.

Display a message if the ID is not found.

## Question 07 – Detect Duplicate Values

Create a program that checks whether a list contains any duplicate values using nested loops and loop else.

## Question 08 – Validate Ages

Write a program to validate a list of ages.

Use break and else to report whether all ages are within an accepted range.

## Question 09 – Number Guessing

Create a number-guessing program where loop else displays a message when all attempts are used without success.

## Question 10 – Common Element

Write a program to find a common element between two lists using nested loops and appropriate loop-else placement.

---

# 18. Common Mistakes

Understanding common mistakes will help you use loop else correctly.

## Mistake 01 – Thinking Else Executes After Break

Incorrect understanding:

Thinking that else always executes after a loop.

Correct understanding:

The else block of a loop is skipped when that loop terminates using break.

```python
for number in range(1, 5):

    if number == 2:
        break

else:
    print("Loop completed.")
```

The message is not printed.

## Mistake 02 – Confusing Loop Else with If-Else

In an if-else statement, else executes when the if condition is false.

In a loop-else statement, else executes when the loop completes without break.

## Mistake 03 – Incorrect Indentation

Incorrect:

```python
for number in range(1, 5):
    print(number)

    else:
        print("Completed")
```

The indentation is invalid.

Correct:

```python
for number in range(1, 5):
    print(number)

else:
    print("Completed")
```

## Mistake 04 – Thinking Continue Prevents Else

Incorrect assumption:

Continue skips the loop else block.

Correct understanding:

Continue skips an iteration but does not terminate the loop. If the loop eventually finishes without break, else executes.

## Mistake 05 – Forgetting the Break After Finding a Value

Consider:

```python
numbers = [10, 20, 30]

for number in numbers:

    if number == 20:
        print("Found")
```

This program does not stop after finding the target.

For this search pattern, using break is useful:

```python
numbers = [10, 20, 30]

for number in numbers:

    if number == 20:
        print("Found")
        break

else:
    print("Not found")
```

## Mistake 06 – Incorrect Nested Loop Placement

The indentation determines which loop owns the else block.

Always check whether the else belongs to the inner or outer loop.

## Mistake 07 – Forgetting Empty Iterable Behaviour

An empty iterable causes zero loop iterations.

The loop still completes normally, so the else block executes.

## Mistake 08 – Incorrect Prime Number Logic

The numbers 0 and 1 are not prime.

Always handle values less than or equal to 1 separately before running the divisor loop.

## Mistake 09 – Incorrect While Loop Counter

A while loop requires its condition to change eventually if it is expected to terminate.

Without updating the counter, the loop may run forever and never reach its else block.

---

# 19. Best Practices

Follow these best practices when using loop else:

1. Use loop else when you need to report normal loop completion.
2. Use for-else for searching collections.
3. Use loop else for prime-number checking.
4. Use break when a required condition has been satisfied.
5. Keep the break condition easy to understand.
6. Pay attention to indentation.
7. Use flags carefully in nested loops.
8. Handle empty collections deliberately.
9. Check special values such as 0 and 1 in mathematical algorithms.
10. Keep loop conditions readable.
11. Do not use loop else when a simple conditional statement is clearer.
12. Test both found and not-found cases.
13. Test normal completion and early termination.
14. Be careful when placing else in nested loops.

## Recommended Search Pattern

```python
for item in collection:

    if item == target:
        print("Found")
        break

else:
    print("Not found")
```

This pattern is useful because it makes the found and not-found cases easy to distinguish.

---

# 20. Debugging Loop Else

Debugging is important when a loop's else block does not execute as expected.

Check the following:

- Does the loop contain break?
- Is the break condition becoming true?
- Is the else block aligned with the correct loop?
- Is the iterable empty?
- Is the while loop condition becoming false?
- Is continue being confused with break?
- Is a nested loop breaking the expected loop?

## Debugging Example

```python
for number in range(1, 6):

    print("Current number:", number)

    if number == 3:
        print("Break encountered.")
        break

else:
    print("Loop completed normally.")
```

**Output:**

```text
Current number: 1
Current number: 2
Current number: 3
Break encountered.
```

The loop else message is not displayed.

## Debugging with Continue

```python
for number in range(1, 6):

    print("Checking:", number)

    if number == 3:
        print("Skipping current iteration.")
        continue

    print("Processing:", number)

else:
    print("Loop completed normally.")
```

**Output:**

```text
Checking: 1
Processing: 1
Checking: 2
Processing: 2
Checking: 3
Skipping current iteration.
Checking: 4
Processing: 4
Checking: 5
Processing: 5
Loop completed normally.
```

---

# 21. Real-Life Applications

Loop else can be useful in multiple programming situations.

## 21.1 Student Search System

A school or college application may search for a student's ID.

```python
students = {
    101: "Amaan",
    102: "Rahul",
    103: "Sneha"
}

target_id = 105

for student_id, name in students.items():

    if student_id == target_id:
        print("Student:", name)
        break

else:
    print("Student ID not found.")
```

## 21.2 Product Search System

An online shopping application can search for a product.

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

target = "Keyboard"

for product in products:

    if product == target:
        print("Product available.")
        break

else:
    print("Product not found.")
```

## 21.3 Data Validation

A program can check whether every record satisfies a condition.

```python
ages = [18, 20, 22, 25, 30]

for age in ages:

    if age < 0 or age > 120:
        print("Invalid age detected.")
        break

else:
    print("All ages are valid.")
```

## 21.4 Inventory Search

A shop application can search its inventory for a product.

```python
inventory = {
    "Laptop": 5,
    "Mouse": 0,
    "Keyboard": 10
}

target = "Monitor"

for product in inventory:

    if product == target:
        print("Product exists.")
        break

else:
    print("Product not found in inventory.")
```

## 21.5 Prime Number Validation

A mathematical application can use for-else to check whether a number has a divisor.

```python
number = 31

if number <= 1:
    print("Not prime.")

else:
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print("Not prime.")
            break

    else:
        print("Prime.")
```

---

# 22. Connection with Data Structures and Algorithms

Loop else is particularly useful in algorithms that search or validate collections.

## 22.1 Linear Search

Linear search checks elements one by one.

```python
numbers = [10, 20, 30, 40, 50]
target = 40

for number in numbers:

    if number == target:
        print("Found.")
        break

else:
    print("Not found.")
```

Time Complexity: O(N)

## 22.2 Prime Number Checking

Trial division checks whether any possible divisor divides the number.

If no divisor is found, the loop else executes.

Time Complexity: O(√N) when testing divisors only up to the square root.

## 22.3 Duplicate Detection

Nested loops can compare pairs of elements.

```python
numbers = [10, 20, 30, 20]

duplicate_found = False

for first_index in range(len(numbers)):

    for second_index in range(first_index + 1, len(numbers)):

        if numbers[first_index] == numbers[second_index]:
            duplicate_found = True
            break

    if duplicate_found:
        break

else:
    print("No duplicate found.")
```

When a duplicate exists, the inner and then outer loops terminate using break.

## 22.4 Matrix Searching

Nested loops can search each element in a matrix.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 8
found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

else:
    print("Target not found.")
```

## 22.5 Algorithmic Importance

Loop else does not automatically improve an algorithm's time complexity.

It helps organize the logic for:

- Found versus not-found outcomes.
- Successful validation versus failure.
- Prime versus composite results.
- Normal completion versus early termination.

---

# 23. Time and Space Complexity

Complexity analysis measures how an algorithm performs as input size increases.

## 23.1 Linear Search

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:

    if number == target:
        break

else:
    print("Not found.")
```

In the worst case, every element is checked.

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## 23.2 Prime Number Checking

```python
number = 29

if number <= 1:
    print("Not prime.")

else:
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print("Not prime.")
            break

    else:
        print("Prime.")
```

The algorithm checks divisors up to the square root.

- Time Complexity: O(√N)
- Auxiliary Space Complexity: O(1)

## 23.3 Nested Loop Searching

For two lists with sizes N and M:

```python
for first_value in first_list:

    for second_value in second_list:

        if first_value == second_value:
            break
```

In the worst case, all pairs may be compared.

- Time Complexity: O(N × M)
- Auxiliary Space Complexity: O(1)

## Complexity Summary

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Basic for-else over N values | O(N) | O(1) |
| Basic while-else with N iterations | O(N) | O(1) |
| Linear search | O(N) | O(1) |
| Prime checking using square root | O(√N) | O(1) |
| Nested loop search | O(N × M) | O(1) |
| Matrix search | O(R × C) | O(1) |
| Checking all marks | O(N) | O(1) |

---

# 24. Mini Project – Student Search System

## Project Objective

Create a simple Student Search System using loop else.

The system should:

1. Store student records.
2. Display all student IDs and names.
3. Ask the user for a student ID.
4. Search for the student.
5. Display the name if found.
6. Display a not-found message if no matching ID exists.

## Project Code

```python
"""
Mini Project: Student Search System

Concepts:
- Dictionaries
- for loops
- break
- loop else
- Input validation
"""


def search_student(
    students: dict[int, str],
    target_id: int
) -> None:
    """Search for a student by ID."""
    for student_id, name in students.items():

        if student_id == target_id:
            print("\nStudent found.")
            print("Student ID:", student_id)
            print("Student Name:", name)
            break

    else:
        print("\nStudent not found.")


def display_students(students: dict[int, str]) -> None:
    """Display all available students."""
    print("\nSTUDENT RECORDS")
    print("-" * 35)

    for student_id, name in students.items():
        print(f"ID: {student_id} | Name: {name}")


def main() -> None:
    """Run the student search application."""
    students = {
        101: "Amaan",
        102: "Rahul",
        103: "Sneha",
        104: "Ali",
        105: "Arjun"
    }

    print("=" * 40)
    print("STUDENT SEARCH SYSTEM")
    print("=" * 40)

    display_students(students)

    try:
        target_id = int(input("\nEnter student ID to search: "))

    except ValueError:
        print("Invalid input! Enter a numeric student ID.")
        return

    search_student(students, target_id)


if __name__ == "__main__":
    main()
```

## Sample Input

```text
Enter student ID to search: 103
```

## Sample Output

```text
Student found.
Student ID: 103
Student Name: Sneha
```

## Example When Student Is Not Found

**Input:**

```text
Enter student ID to search: 999
```

**Output:**

```text
Student not found.
```

## Concepts Used

- Dictionaries
- Functions
- Type hints
- For loops
- Break
- Loop else
- Exception handling
- Input validation

## Possible Improvements

1. Add new students.
2. Delete student records.
3. Update student names.
4. Search by student name.
5. Store records in a file.
6. Add a menu-driven interface.
7. Add duplicate ID validation.

---

# 25. Fifty Python Viva Questions and Answers

## Basic Questions

**Q1. What is loop else in Python?**

Loop else is an additional block associated with a for or while loop that executes when that loop completes normally without break.

**Q2. Can else be used with a for loop?**

Yes.

**Q3. Can else be used with a while loop?**

Yes.

**Q4. What is the main purpose of loop else?**

It is useful for handling operations after normal loop completion, especially when searching for an element.

**Q5. Does loop else execute after break?**

No. It does not execute when its associated loop terminates through break.

**Q6. Does loop else execute after continue?**

Yes, provided the loop eventually completes normally.

**Q7. Does loop else execute for an empty list?**

Yes. The loop completes normally without any iterations.

**Q8. Is loop else similar to if-else?**

No. If-else depends on a condition, whereas loop else depends on how the loop terminates.

**Q9. Can loop else be used in nested loops?**

Yes.

**Q10. Which statement prevents a loop's else block from executing?**

The break statement.

## Conceptual Questions

**Q11. What happens when a loop completes normally?**

Its else block executes if one is present.

**Q12. What happens when a loop is terminated using break?**

The else block associated with that loop is skipped.

**Q13. What happens when continue executes?**

The remaining statements in the current iteration are skipped, and the next iteration begins.

**Q14. Does continue prevent loop else from executing?**

No. Continue does not terminate the loop.

**Q15. What happens if the iterable is empty?**

The loop performs zero iterations and its else block executes.

**Q16. Is loop else mandatory?**

No. It is optional.

**Q17. Can loop else be used with range()?**

Yes.

**Q18. Can loop else be used with a dictionary?**

Yes. It can be used while iterating over dictionary keys, values or items.

**Q19. Can loop else be used with a string?**

Yes.

**Q20. What is the biggest advantage of loop else?**

It provides a clear way to handle cases where a loop finishes without finding or encountering a specified condition.

## Programming Questions

**Q21. How can you search for a number using for-else?**

Iterate through the list, break when the number is found and use else for the not-found case.

**Q22. How can you check a prime number using loop else?**

Check divisors and break when a divisor is found. If none is found, the else block executes.

**Q23. How can you find an even number using loop else?**

Check every number and break when an even number is found.

**Q24. How can you check whether all values are positive?**

Break when a non-positive number is found; otherwise, the loop else executes.

**Q25. Can loop else help validate student marks?**

Yes. It can report that all marks are valid if the loop finds no invalid mark.

**Q26. What is linear search?**

Linear search checks elements sequentially until the target is found or the collection is exhausted.

**Q27. What is the time complexity of linear search?**

O(N) in the worst case.

**Q28. What is the time complexity of optimized trial-division prime checking?**

O(√N).

**Q29. How can loop else help with duplicate detection?**

Nested loops can search for equal pairs and use break when a duplicate is found.

**Q30. Can loop else be used for matrix searching?**

Yes. Nested loops can search each matrix element.

## Advanced Questions

**Q31. What is the difference between loop else and if-else?**

If-else selects a block based on a Boolean condition. Loop else depends on whether the associated loop terminates normally without break.

**Q32. Does a break in an inner loop prevent the outer loop else from executing?**

Not automatically. A break in the inner loop terminates only the inner loop. The outer loop can still complete normally.

**Q33. Which loop owns an else block in nested loops?**

The loop aligned with the else keyword at the same indentation level.

**Q34. Can a while loop else execute when its condition is initially false?**

Yes. The loop performs zero iterations and completes normally.

**Q35. Does the else block execute if a while loop becomes false naturally?**

Yes, if the loop was not terminated by break.

**Q36. Can a loop have both break and else?**

Yes. The else block simply does not execute if that loop is terminated using break.

**Q37. What is a flag variable?**

A Boolean or other variable used to track whether an event, such as finding a target, has occurred.

**Q38. Why are flags useful in nested-loop searching?**

They can communicate that a target was found in the inner loop so the outer loop can also terminate.

**Q39. Does loop else automatically improve time complexity?**

No. It changes control flow but does not automatically reduce the work performed.

**Q40. What happens if the loop contains multiple break statements?**

The else block is skipped if any executed break terminates that loop.

## Practical and DSA Questions

**Q41. Where is loop else commonly used?**

Searching, prime checking, validation and checking whether a value exists in a collection.

**Q42. Can loop else be used to search student records?**

Yes. The program can display a not-found message when no matching student ID exists.

**Q43. How does loop else work in a password-list search example?**

It displays a not-found message when the loop does not find a matching entry.

**Q44. What is the purpose of break in a search algorithm?**

It stops searching once the target is found.

**Q45. Why is else helpful in linear search?**

It provides a clear not-found case without requiring an additional flag.

**Q46. Can a loop else block run after a continue statement?**

Yes, if the loop eventually completes without break.

**Q47. How can loop else be used in data validation?**

It can report that all entries passed validation when no invalid entry causes break.

**Q48. What is the role of indentation in nested loop else?**

It determines which loop the else block belongs to.

**Q49. What is the auxiliary space complexity of a basic linear search?**

O(1), when no additional collection proportional to the input size is created.

**Q50. What is the most important rule to remember about loop else?**

The else block belongs to its associated loop and executes when that loop completes without executing break.

---

# 26. Important Terminology

| Term | Meaning |
|---|---|
| Loop Else | Else block associated with a loop |
| Break | Terminates the nearest enclosing loop |
| Continue | Skips current iteration |
| Iteration | One execution of a loop |
| Normal Completion | Loop finishes without break |
| Linear Search | Sequential search through elements |
| Prime Number | Number greater than 1 with exactly two positive divisors |
| Divisor | A number that divides another number exactly |
| Iterable | An object that can be iterated over |
| Empty Iterable | An iterable containing no elements |
| Nested Loop | A loop inside another loop |
| Flag Variable | Variable used to track a condition or event |
| Matrix | Two-dimensional arrangement of values |
| Validation | Checking whether data satisfies requirements |
| Time Complexity | Measure of growth in running time |
| Auxiliary Space | Additional memory used by an algorithm |

---

# 27. Quick Revision Notes

## Important Syntax

**For-Else:**

```python
for item in collection:

    statement

else:
    print("Loop completed.")
```

**While-Else:**

```python
while condition:

    statement

else:
    print("Loop completed.")
```

**Search with For-Else:**

```python
for number in numbers:

    if number == target:
        print("Found")
        break

else:
    print("Not found")
```

**Prime Number with Loop Else:**

```python
if number <= 1:
    print("Not prime.")

else:
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print("Not prime.")
            break

    else:
        print("Prime.")
```

## Important Rules

1. Loop else works with for and while loops.
2. It executes after normal completion.
3. Break prevents the associated loop's else from executing.
4. Continue does not prevent loop else.
5. An empty iterable still allows loop else to execute.
6. A break in an inner loop affects only the inner loop.
7. Indentation determines which loop owns else.
8. Loop else is useful for searching.
9. Loop else is useful for prime-number checking.
10. Loop else can be used for data validation.

## Most Important Comparison

| Situation | Does Loop Else Execute? |
|---|---|
| Normal loop completion | Yes |
| Loop terminated by break | No |
| Continue used, then normal completion | Yes |
| Empty iterable | Yes |
| Inner loop breaks but outer completes normally | Outer else executes |

---

# 28. Learning Checklist

Mark each item after understanding and practising it.

- [ ] Understand the meaning of loop else.
- [ ] Understand for-else syntax.
- [ ] Understand while-else syntax.
- [ ] Understand when loop else executes.
- [ ] Understand why break prevents loop else.
- [ ] Understand that continue does not prevent loop else.
- [ ] Understand else with an empty iterable.
- [ ] Search for elements using for-else.
- [ ] Check prime numbers using loop else.
- [ ] Search for student records.
- [ ] Search dictionary values.
- [ ] Use loop else with nested loops.
- [ ] Understand inner-loop and outer-loop else.
- [ ] Validate student marks using loop else.
- [ ] Search for common elements between lists.
- [ ] Search elements in a matrix.
- [ ] Differentiate loop else from if-else.
- [ ] Understand time and space complexity.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the Student Search System mini project.
- [ ] Prepare all fifty viva questions.

---

# 29. How to Run the Python File

## Step 1 – Open the Repository

Open your `DSA-Python` project in VS Code.

## Step 2 – Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 09-Loop-Else/
```

## Step 3 – Open the Python File

Open:

```text
09_loop_else.py
```

## Step 4 – Open the Terminal

Open the integrated terminal in VS Code.

## Step 5 – Run the Python File

From the repository root, execute:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/09-Loop-Else/09_loop_else.py
```

## Step 6 – Select an Option

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Select an option to explore the topic.

---

# 30. Repository Structure

Store both files in the following location:

```text
DSA-Python/
└── PYTHON/
    └── Python-Fundamentals/
        └── 01-Loops/
            └── 09-Loop-Else/
                ├── README.md
                └── 09_loop_else.py
```

## File Description

| File | Purpose |
|---|---|
| README.md | Detailed concepts, examples, solved problems, practice questions and viva |
| 09_loop_else.py | Executable Python examples and interactive practice menu |

## Git Commands

After adding both files, execute these commands from your repository root:

```powershell
git status
```

```powershell
git add "PYTHON/Python-Fundamentals/01-Loops/09-Loop-Else/"
```

```powershell
git commit -m "Add loop else lesson"
```

```powershell
git push origin main
```

These commands stage, commit and push the topic if each Git operation succeeds.

---

# 31. Final Summary

Loop else is an important Python feature that allows us to execute a block of code after a loop completes normally.

It is especially useful for:

- Searching elements.
- Finding missing values.
- Checking prime numbers.
- Validating records.
- Searching student information.
- Searching dictionary values.
- Matrix traversal.
- Nested-loop algorithms.

The most important rule to remember is:

**Loop else executes when its associated loop finishes without executing break.**

Remember these differences:

- `break` – Terminates the nearest enclosing loop.
- `continue` – Skips the current iteration.
- `pass` – Performs no operation.
- `loop else` – Executes after normal loop completion without break.

Before moving to the next topic:

1. Understand all twelve examples.
2. Practise the twelve solved problems.
3. Attempt the ten unsolved questions.
4. Complete the Student Search System mini project.
5. Revise the fifty viva questions.

**Topic 09 – Loop Else: Completed Study Notes.**