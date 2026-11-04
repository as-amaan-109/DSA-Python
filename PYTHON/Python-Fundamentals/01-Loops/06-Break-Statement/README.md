# Break Statement in Python

## 1. Introduction

The `break` statement is a loop-control statement in Python.

It is used to terminate the nearest enclosing loop immediately when a particular condition is satisfied.

When Python executes `break`, it stops the current loop and moves execution to the first statement after that loop.

The `break` statement can be used inside:

- `for` loops.
- `while` loops.
- Nested loops.

For example, suppose we want to print numbers from 1 to 10 but stop when the number becomes 6.

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

When the value becomes 6, the condition becomes true.

Python executes `break` and immediately terminates the loop.

The numbers after 6 are not processed.

The `break` statement is useful in searching, input processing, validation, menu-driven applications, games, and algorithm implementation.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

1. Define the `break` statement.
2. Understand why `break` is used.
3. Understand how `break` terminates a loop.
4. Use `break` inside a `for` loop.
5. Use `break` inside a `while` loop.
6. Understand the nearest-enclosing-loop rule.
7. Stop a loop when a condition is satisfied.
8. Search for an element using `break`.
9. Find the first matching element in a collection.
10. Find the first even number in a list.
11. Find the first vowel in a string.
12. Use sentinel values to terminate repetition.
13. Stop processing when a negative number is found.
14. Use `break` in number-based algorithms.
15. Understand `break` in nested loops.
16. Stop an outer loop using a flag.
17. Use `break` in input-controlled programs.
18. Stop repeated attempts after success.
19. Understand the relationship between `break` and algorithm efficiency.
20. Compare `break` with `continue` and `pass`.
21. Understand the interaction between `break` and loop `else`.
22. Apply early termination in basic DSA problems.

---

## 3. What Is the Break Statement?

The `break` statement is used to terminate the nearest enclosing `for` or `while` loop.

It is normally placed inside a conditional statement.

### Syntax

```python
break
```

### Basic Example

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

### Explanation

The loop starts from one.

The condition checks whether the current number is equal to five.

When the number becomes five, Python executes `break`.

The loop terminates immediately.

The print statement is not executed for five because `break` is encountered first.

### Important Points

- `break` terminates the nearest enclosing loop.
- It works with `for` loops.
- It works with `while` loops.
- It can be used inside nested loops.
- It does not terminate the entire Python program.
- It does not automatically terminate every enclosing loop.
- The statements after the loop execute normally.
- A loop's `else` block is skipped when the loop terminates through `break`.

---

## 4. Why Do We Use the Break Statement?

The `break` statement is useful when continuing a loop is no longer necessary.

For example, suppose a program searches for a number in a list.

Once the target is found, the program does not need to check the remaining elements when only the first occurrence is required.

### Without Break

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print("Element found:", number)
```

The loop continues checking the remaining values even after finding the target.

### With Break

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print("Element found:", number)
        break
```

Once the target is found, the loop stops.

### Advantages

1. Terminates unnecessary loop iterations.
2. Makes searching more efficient when a match is found early.
3. Helps stop repeated input.
4. Supports sentinel-controlled processing.
5. Makes early exit conditions easier to implement.
6. Prevents unnecessary calculations.
7. Helps control nested loops.
8. Supports interactive programs.
9. Helps implement guessing games.
10. Makes certain algorithms easier to understand.

### Common Applications

- Linear search.
- Finding the first matching element.
- Finding the first vowel.
- Finding a divisor.
- Number guessing games.
- Input processing.
- Sentinel-controlled loops.
- Matrix searching.
- Prime-number checking.
- Stopping a calculation after reaching a limit.

---

## 5. Basic Syntax of Break in a For Loop

The `break` statement can be placed inside a `for` loop.

### Syntax

```python
for variable in iterable:
    if condition:
        break

    statement
```

### Example

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

### Explanation

The `for` loop processes values from one to ten.

The condition checks whether the current value is six.

When the condition becomes true, `break` terminates the loop.

### Important Rule

The placement of `break` matters.

In this example, the value six is not printed because the `break` statement executes before `print()`.

---

## 6. Basic Syntax of Break in a While Loop

The `break` statement can also terminate a `while` loop.

### Syntax

```python
while condition:
    if another_condition:
        break

    statement
```

### Example

```python
number = 1

while number <= 10:
    if number == 6:
        break

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

The loop starts with one.

The condition `number <= 10` controls the normal repetition.

The inner condition checks whether the number is six.

When it becomes six, `break` terminates the loop immediately.

### Important Point

The `break` statement can terminate a `while True` loop even though its normal condition is always true.

Example:

```python
while True:
    command = input("Enter exit to stop: ")

    if command == "exit":
        break

    print("You entered:", command)
```

---

## 7. How the Break Statement Executes

Consider:

```python
for number in range(1, 8):
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

### Execution Explanation

| Iteration | Current Number | Condition `number == 4` | Action |
|---|---:|---|---|
| 1 | 1 | False | Print 1 |
| 2 | 2 | False | Print 2 |
| 3 | 3 | False | Print 3 |
| 4 | 4 | True | Execute break |
| Remaining | 5, 6, 7 | Not checked | Loop already terminated |

### Execution Flow

```text
Start loop
    |
    v
Get next value
    |
    v
Check break condition
    |
    v
Is condition True?
    |
  Yes|       No
    |        |
    v        v
  Break    Execute
    |      loop body
    |        |
    v        v
Statement  Next iteration
after loop
```

### Important Concept

Once the `break` statement executes, the nearest enclosing loop is terminated.

The remaining iterations of that loop are skipped.

---

## 8. Break with a For Loop

A `for` loop commonly processes an iterable.

The `break` statement can stop iteration when a required item or condition is encountered.

### Example: Stop at a Specific Value

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        break

    print(number)
```

Output:

```text
10
20
```

### Example: Find a Particular Word

```python
names = ["Amaan", "Rahul", "Sameer", "Arjun"]

for name in names:
    if name == "Sameer":
        print("Name found:", name)
        break
```

Output:

```text
Name found: Sameer
```

### Example: Stop When the Number Becomes Greater Than 20

```python
numbers = [5, 10, 15, 25, 30, 35]

for number in numbers:
    if number > 20:
        break

    print(number)
```

Output:

```text
5
10
15
```

### Applications

- Searching in lists.
- Processing names.
- Finding the first matching value.
- Stopping at an invalid record.
- Avoiding unnecessary iteration.

---

## 9. Break with a While Loop

A `while` loop can use `break` to terminate repetition before its normal condition becomes false.

### Example

```python
number = 1

while number <= 10:
    if number == 5:
        break

    print(number)
    number += 1
```

Output:

```text
1
2
3
4
```

### Example: Stop a Countdown

```python
countdown = 10

while countdown > 0:
    if countdown == 5:
        break

    print(countdown)
    countdown -= 1
```

Output:

```text
10
9
8
7
6
```

### Example: User-Controlled Loop

```python
while True:
    command = input("Enter a command: ")

    if command == "quit":
        print("Exiting program.")
        break

    print("Command received:", command)
```

The loop continues accepting commands until the user enters `quit`.

### Important Point

A `while` loop often uses `break` when the number of repetitions is not known in advance.

---

## 10. Finding the First Matching Element

One of the most common uses of `break` is searching for the first occurrence of an element.

### Example

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print("Element found:", number)
        break
```

Output:

```text
Element found: 30
```

### Explanation

The loop checks each element in order.

When it finds the target, it displays the result and stops.

### Why Use Break?

Without `break`, the program might continue checking elements that do not need to be processed.

### Finding the First Index

```python
numbers = [10, 20, 30, 40, 50]
target = 30

found_index = -1

for index, number in enumerate(numbers):
    if number == target:
        found_index = index
        break

if found_index != -1:
    print("Found at index:", found_index)
else:
    print("Element not found.")
```

Output:

```text
Found at index: 2
```

### Important Point

This method reports the first occurrence of the target.

If duplicate values exist, the loop stops at the first match.

---

## 11. Finding the First Even Number

The `break` statement can stop iteration as soon as an even number is found.

### Example

```python
numbers = [1, 3, 5, 8, 9, 12]

for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        break
```

Output:

```text
First even number: 8
```

### Explanation

The loop checks one number at a time.

The first five is odd.

The next number, eight, is even.

The loop stops immediately after finding eight.

### Important Point

The program does not check 9 or 12.

This is an example of early termination.

---

## 12. Finding the First Vowel in a String

A `break` statement can stop character iteration when the first vowel is found.

### Example

```python
text = "PYTHON PROGRAMMING"
vowels = "aeiou"

for character in text.lower():
    if character in vowels:
        print("First vowel:", character)
        break
```

Output:

```text
First vowel: o
```

### Explanation

The string is converted to lowercase.

The loop processes every character.

When a vowel is found, `break` terminates the loop.

### Another Example

```python
text = "BCDFGHELLO"

for character in text.lower():
    if character in "aeiou":
        print("Vowel found:", character)
        break
```

Output:

```text
Vowel found: e
```

### Applications

- Searching text.
- Finding the first matching character.
- Basic validation.
- Character processing.

---

## 13. Stopping at a Negative Number

A loop can stop when it encounters the first negative number.

### Example

```python
numbers = [10, 20, 30, -5, 40, 50]

for number in numbers:
    if number < 0:
        print("Negative number encountered:", number)
        break

    print(number)
```

Output:

```text
10
20
30
Negative number encountered: -5
```

### Explanation

The loop processes the positive values.

When it reaches negative five, the condition becomes true.

The loop terminates immediately.

The remaining values are not processed.

### Practical Use

This logic is useful when:

- A negative value indicates invalid data.
- A sequence has an end marker.
- Processing must stop at the first error.
- A particular boundary condition is reached.

---

## 14. Sentinel-Controlled Loops Using Break

A sentinel is a special value used to indicate that repetition should stop.

The sentinel value is different from ordinary data values.

For example, zero can be used to stop accepting numbers.

### Example

```python
total = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    total += number

print("Final sum:", total)
```

### Sample Input

```text
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 0
```

### Sample Output

```text
Final sum: 60
```

### Explanation

The program repeatedly accepts numbers.

If the user enters zero, the loop terminates.

Otherwise, the value is added to the total.

### Common Sentinel Values

| Sentinel | Possible Meaning |
|---|---|
| `0` | Stop numeric input |
| `-1` | End data entry |
| `"exit"` | Exit a command loop |
| `"quit"` | Stop an interactive program |
| `"done"` | Finish a data-entry operation |

A sentinel must be selected carefully so that it does not conflict with valid input.

---

## 15. Break in Nested Loops

A nested loop contains one loop inside another.

When `break` is executed inside a nested loop, it terminates only the nearest enclosing loop.

It does not automatically terminate the outer loop.

### Example

```python
for row in range(1, 4):
    print("Row:", row)

    for column in range(1, 5):
        if column == 3:
            break

        print(column, end=" ")

    print()
```

Output:

```text
Row: 1
1 2
Row: 2
1 2
Row: 3
1 2
```

### Explanation

The outer loop controls rows.

The inner loop controls columns.

When the column becomes three, `break` terminates the inner loop.

The outer loop continues with the next row.

Therefore, the same inner-loop behaviour occurs for all three rows.

### Important Rule

A `break` statement terminates only the nearest enclosing loop.

This rule is especially important when working with nested loops.

---

## 16. How to Stop Both Loops

Sometimes a program must stop both the inner and outer loops after finding a result.

A single `break` inside the inner loop does not stop the outer loop.

One common solution is to use a Boolean flag.

### Example: Search a Matrix

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == target:
            print("Found at:", row, column)
            found = True
            break

    if found:
        break
```

Output:

```text
Found at: 1 1
```

### Explanation

1. The outer loop selects a row.
2. The inner loop checks the elements.
3. When the target is found, `found` becomes `True`.
4. The inner loop terminates.
5. The outer loop checks the flag.
6. The outer loop also terminates.

### Alternative: Return from a Function

If the search is inside a function, `return` can terminate the function and therefore stop all its loops.

```python
def search_matrix(matrix, target):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == target:
                return row, column

    return None


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(search_matrix(matrix, 5))
```

Output:

```text
(1, 1)
```

### Important Point

Use a flag when the surrounding code needs to continue after the loop.

Use `return` when the function should finish as soon as the result is found.

---

## 17. Break in a Number Guessing Game

A guessing game can use `break` to stop when the correct number is guessed.

### Example

```python
secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct guess!")
        break

    print("Incorrect guess. Try again.")
```

### Sample Run

```text
Guess the number: 4
Incorrect guess. Try again.

Guess the number: 9
Incorrect guess. Try again.

Guess the number: 7
Correct guess!
```

### Explanation

The loop continues until the correct number is entered.

When the correct guess is received, `break` terminates the loop.

### Applications

- Number guessing games.
- Password-entry exercises.
- Interactive menus.
- Quiz applications.
- Repeated user attempts.

---

## 18. Break After a Limit Is Reached

A running calculation can use `break` to stop when a particular limit is exceeded.

### Example

```python
numbers = [5, 7, 4, 8, 10]

total = 0

for number in numbers:
    total += number

    print("Current total:", total)

    if total > 20:
        print("Limit exceeded.")
        break
```

Output:

```text
Current total: 5
Current total: 12
Current total: 16
Current total: 24
Limit exceeded.
```

### Explanation

The total increases after each iteration.

When it becomes greater than 20, the loop terminates.

The remaining number is not processed.

### Practical Applications

- Processing until a budget limit is reached.
- Stopping when a threshold is exceeded.
- Ending repeated calculations.
- Terminating a simulation when a boundary is reached.

---

## 19. Break in Prime Number Checking

Prime-number checking can use `break` to stop divisor testing as soon as a factor is found.

A prime number is a positive integer greater than one that has exactly two positive divisors: one and itself.

### Example

```python
number = 15

if number < 2:
    print("Not prime.")

else:
    divisor = 2
    is_prime = True

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            print("Divisor found:", divisor)
            break

        divisor += 1

    if is_prime:
        print("Prime number")
    else:
        print("Not prime")
```

Output:

```text
Divisor found: 3
Not prime
```

### Explanation

The loop tests possible divisors starting from two.

When a divisor is found, the number cannot be prime.

There is no need to test the remaining candidate divisors.

The `break` statement stops the search.

### Why Test Only Up to the Square Root?

If a number has a divisor greater than its square root, it must also have a corresponding divisor smaller than its square root.

Therefore, checking while `divisor * divisor <= number` is sufficient.

### Complexity

- Worst-case time: O(√N).
- Auxiliary space: O(1).

---

## 20. Break with Loop Else

Python supports an `else` block with both `for` and `while` loops.

The loop's `else` block executes when the loop finishes normally without encountering `break`.

When `break` terminates the loop, the loop's `else` block is skipped.

### Example Without Break

```python
for number in range(1, 4):
    print(number)

else:
    print("Loop completed normally.")
```

Output:

```text
1
2
3
Loop completed normally.
```

### Example With Break

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)

else:
    print("Loop completed normally.")
```

Output:

```text
1
2
```

The `else` block does not execute.

### Practical Search Example

```python
numbers = [10, 20, 30, 40]
target = 50

for number in numbers:
    if number == target:
        print("Element found.")
        break

else:
    print("Element not found.")
```

Output:

```text
Element not found.
```

### Explanation

If the target is found, `break` terminates the loop.

If the loop finishes without finding the target, the `else` block executes.

### Important Rules

- Loop `else` is not the same as an `if-else`.
- It runs when the loop completes normally.
- It is skipped when the loop exits through `break`.
- It is useful for search problems.
- It can reduce the need for a separate Boolean flag in simple cases.

---

## 21. Difference Between Break, Continue, and Pass

Python provides three important statements that affect program flow.

They have different purposes.

### 21.1 Break

The `break` statement terminates the nearest enclosing loop.

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)
```

Output:

```text
1
2
```

### 21.2 Continue

The `continue` statement skips the remaining statements in the current iteration and moves to the next iteration.

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

### 21.3 Pass

The `pass` statement performs no operation.

It is used as a placeholder when a statement is syntactically required but no action is needed yet.

```python
for number in range(1, 6):
    if number == 3:
        pass

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

### Comparison Table

| Feature | Break | Continue | Pass |
|---|---|---|---|
| Main purpose | Terminate the nearest loop | Skip the current iteration | Do nothing |
| Stops loop? | Yes | No | No |
| Skips remaining statements in the current iteration? | Yes, by leaving the loop | Yes | No |
| Starts next iteration? | No | Yes | Normal execution continues |
| Common use | Early termination | Skipping unwanted values | Placeholder |
| Works inside loops | Yes | Yes | Yes, but it is not a loop-control operation |

### Important Point

Do not confuse these statements.

`break` ends the nearest enclosing loop.

`continue` skips the rest of the current iteration.

`pass` does nothing and does not change the loop's control flow.

---

## 22. Twelve Topic Examples

These examples correspond to the twelve examples in `06_break_statement.py`.

### Example 1: Stop a For Loop at a Specific Value

**Objective:** Print numbers until the value becomes six.

```python
for number in range(1, 11):
    if number == 6:
        break

    print(number, end=" ")
```

Output:

```text
1 2 3 4 5
```

Explanation:

When the value becomes six, the loop terminates.

### Example 2: Search for an Element in a List

**Objective:** Find the target value and stop searching.

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print("Target found:", number)
        break

    print("Checking:", number)
```

Output:

```text
Checking: 10
Checking: 20
Target found: 30
```

Explanation:

The remaining list elements are not checked after the target is found.

### Example 3: Stop at the First Negative Number

**Objective:** Stop processing a list when a negative value appears.

```python
values = [10, 20, 30, -5, 40, 50]

for value in values:
    if value < 0:
        print("Negative number encountered:", value)
        break

    print(value, end=" ")
```

Output:

```text
10 20 30 Negative number encountered: -5
```

Explanation:

The loop processes positive values until it reaches negative five.

### Example 4: Sentinel Value Using Break

**Objective:** Stop processing at zero.

```python
values = [5, 10, 15, 0, 20, 25]

for value in values:
    if value == 0:
        print("Sentinel value detected.")
        break

    print(value, end=" ")
```

Output:

```text
5 10 15 Sentinel value detected.
```

Explanation:

Zero acts as the terminating value.

### Example 5: Find the First Even Number

**Objective:** Find the first even number in a list.

```python
numbers = [1, 3, 5, 8, 9, 12]

for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        break
```

Output:

```text
First even number: 8
```

Explanation:

The loop stops at the first even number.

### Example 6: Find the First Vowel

**Objective:** Find the first vowel in a string.

```python
text = "PYTHON PROGRAMMING"
vowels = "aeiou"

for character in text.lower():
    if character in vowels:
        print("First vowel:", character)
        break
```

Output:

```text
First vowel: o
```

Explanation:

The string is processed character by character until a vowel is found.

### Example 7: Break Only the Inner Loop

**Objective:** Stop the inner loop when the column reaches three.

```python
for row in range(1, 4):
    print("Row:", row)

    for column in range(1, 5):
        if column == 3:
            break

        print(column, end=" ")

    print()
```

Output:

```text
Row: 1
1 2
Row: 2
1 2
Row: 3
1 2
```

Explanation:

The inner loop terminates, but the outer loop continues.

### Example 8: Stop the Outer Loop Using a Flag

**Objective:** Stop both loops when a target position is reached.

```python
found = False

for row in range(1, 5):
    print("Checking row:", row)

    for column in range(1, 5):
        if row == 3 and column == 2:
            print("Target position reached.")
            found = True
            break

    if found:
        break
```

Output:

```text
Checking row: 1
Checking row: 2
Checking row: 3
Target position reached.
```

Explanation:

The flag communicates the result of the inner loop to the outer loop.

### Example 9: Stop After a Successful Attempt

**Objective:** Stop repeated attempts when the correct result is obtained.

```python
attempts = ["wrong", "wrong", "correct", "wrong"]

for attempt_number, result in enumerate(attempts, start=1):
    print(f"Attempt {attempt_number}: {result}")

    if result == "correct":
        print("Successful attempt!")
        break
```

Output:

```text
Attempt 1: wrong
Attempt 2: wrong
Attempt 3: correct
Successful attempt!
```

Explanation:

The loop stops after the successful third attempt.

### Example 10: Stop When a Running Sum Exceeds a Limit

**Objective:** Stop calculating when the total exceeds 20.

```python
numbers = [5, 7, 4, 8, 10]

total = 0

for number in numbers:
    total += number

    print("Current total:", total)

    if total > 20:
        print("Limit exceeded.")
        break
```

Output:

```text
Current total: 5
Current total: 12
Current total: 16
Current total: 24
Limit exceeded.
```

Explanation:

The program stops as soon as the running total becomes greater than 20.

### Example 11: Stop After Finding a Divisor

**Objective:** Find a divisor of a number and stop checking.

```python
number = 15
divisor = 2

while divisor < number:
    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}")
        break

    divisor += 1
```

Output:

```text
15 is divisible by 3
```

Explanation:

The loop stops when it finds the first divisor.

### Example 12: Stop at a Non-Alphabetic Character

**Objective:** Print letters until a non-alphabetic character appears.

```python
text = "PYTHON123PROGRAMMING"

for character in text:
    if not character.isalpha():
        print("Non-alphabetic character found:", character)
        break

    print(character, end="")
```

Output:

```text
PYTHONNon-alphabetic character found: 1
```

Explanation:

The program processes alphabetic characters.

When it encounters the digit one, it terminates the loop.

---

## 23. Twelve Solved Programming Problems

### Problem 1: Stop Printing at a Target

**Problem Statement:**

Accept a positive integer N and a target number.

Print numbers from one to N, but stop when the target value is reached.

**Logic:**

1. Read N.
2. Read the target value.
3. Validate that the target is within the range.
4. Start a loop from one to N.
5. Check whether the current number equals the target.
6. Execute `break` when the target is reached.
7. Otherwise, print the current number.

**Code:**

```python
n = int(input("Enter the value of N: "))
target = int(input("Enter the number at which to stop: "))

if target < 1 or target > n:
    print("Target must be between 1 and N.")

else:
    for number in range(1, n + 1):
        if number == target:
            print("Target reached:", target)
            break

        print(number, end=" ")

    print()
```

**Sample Input:**

```text
Enter the value of N: 10
Enter the number at which to stop: 6
```

**Sample Output:**

```text
1 2 3 4 5
Target reached: 6
```

**Explanation:**

The loop stops before printing six.

This demonstrates how the placement of `break` affects the output.

**Complexity:**

- Time: O(N) in the worst case.
- Best-case time for a target at the beginning: O(1).
- Auxiliary space: O(1).

### Problem 2: Linear Search

**Problem Statement:**

Accept a list of integers and search for a target value.

Stop searching at the first occurrence.

**Logic:**

1. Read the number of elements.
2. Accept the list values.
3. Read the target.
4. Traverse the list using `enumerate()`.
5. Compare each element with the target.
6. Store the index when a match is found.
7. Execute `break`.
8. Display the result.

**Code:**

```python
count = int(input("How many numbers do you want? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

target = int(input("Enter the target value: "))

found_index = -1

for index, number in enumerate(numbers):
    if number == target:
        found_index = index
        break

if found_index != -1:
    print("Element found.")
    print("Index:", found_index)
    print("Position:", found_index + 1)

else:
    print("Element not found.")
```

**Sample Input:**

```text
How many numbers do you want? 5
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 40
Enter a number: 50
Enter the target value: 30
```

**Sample Output:**

```text
Element found.
Index: 2
Position: 3
```

**Explanation:**

Linear search examines the values sequentially.

Once 30 is found, the loop stops.

**Complexity:**

- Best-case time: O(1).
- Worst-case time: O(N).
- Auxiliary space: O(1), excluding the input list.

### Problem 3: Find the First Even Number

**Problem Statement:**

Accept a list and find the first even number.

Stop searching after the first matching value.

**Logic:**

1. Read the number of elements.
2. Accept the list values.
3. Initialize a Boolean flag.
4. Traverse the list.
5. Check whether the current number is even.
6. Display the number and execute `break`.
7. Display a message when no even number exists.

**Code:**

```python
count = int(input("How many numbers do you want? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

found = False

for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        found = True
        break

if not found:
    print("No even number found.")
```

**Sample Input:**

```text
How many numbers do you want? 5
Enter a number: 1
Enter a number: 3
Enter a number: 7
Enter a number: 8
Enter a number: 10
```

**Sample Output:**

```text
First even number: 8
```

**Explanation:**

The loop stops at eight.

The number ten is not checked.

**Complexity:**

- Best-case time: O(1).
- Worst-case time: O(N).
- Auxiliary space: O(1), excluding the input list.

### Problem 4: Find the First Vowel

**Problem Statement:**

Accept a string and find its first vowel.

**Logic:**

1. Read a string.
2. Define the vowel collection.
3. Convert the string to lowercase during iteration.
4. Check each character.
5. If a vowel is found, display it and execute `break`.
6. Otherwise, display that no vowel was found.

**Code:**

```python
text = input("Enter a string: ")

vowels = "aeiou"
found = False

for character in text.lower():
    if character in vowels:
        print("First vowel:", character)
        found = True
        break

if not found:
    print("No vowel found.")
```

**Sample Input:**

```text
Enter a string: PYTHON
```

**Sample Output:**

```text
First vowel: o
```

**Explanation:**

The loop processes each character until it finds the first vowel.

**Complexity:**

- Best-case time: O(1) after preprocessing.
- Worst-case time: O(N).
- Auxiliary space: O(N) for the lowercase string produced by `lower()`.

### Problem 5: Sum Until Zero

**Problem Statement:**

Accept numbers continuously until zero is entered.

Calculate the sum of all preceding values.

**Logic:**

1. Initialize total with zero.
2. Start a `while True` loop.
3. Accept a number.
4. Check whether it is zero.
5. If zero, terminate using `break`.
6. Otherwise, add it to total.
7. Display the final sum.

**Code:**

```python
total = 0

print("Enter numbers to calculate their sum.")
print("Enter 0 to stop.")

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    total += number

print("Final sum:", total)
```

**Sample Input:**

```text
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 0
```

**Sample Output:**

```text
Final sum: 60
```

**Explanation:**

Zero is the sentinel value.

The loop stops when zero is received.

**Complexity:**

- Time: O(N), where N is the number of non-zero inputs.
- Auxiliary space: O(1).

### Problem 6: Sum Until a Negative Number

**Problem Statement:**

Accept a list of integers and calculate the sum until the first negative value is encountered.

**Logic:**

1. Read the number of elements.
2. Accept the values into a list.
3. Initialize the total with zero.
4. Iterate through the list.
5. If a value is negative, stop using `break`.
6. Otherwise, add the value to total.
7. Display the sum.

**Code:**

```python
count = int(input("How many numbers do you want? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

total = 0

for number in numbers:
    if number < 0:
        print("Negative number encountered:", number)
        break

    total += number

print("Sum before the negative number:", total)
```

**Sample Input:**

```text
How many numbers do you want? 5
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: -5
Enter a number: 40
```

**Sample Output:**

```text
Negative number encountered: -5
Sum before the negative number: 60
```

**Explanation:**

The values 10, 20, and 30 are added.

When negative five is encountered, the loop terminates.

**Complexity:**

- Time: O(N) in the worst case.
- Auxiliary space: O(N) for the input list.
- Additional processing space: O(1).

### Problem 7: Find the First Multiple

**Problem Statement:**

Accept a starting value, ending value, and positive divisor.

Find the first number in the inclusive interval that is divisible by the divisor.

**Logic:**

1. Read the interval boundaries.
2. Read a positive divisor.
3. Validate the boundaries.
4. Start iterating through the interval.
5. Check divisibility using `%`.
6. Print the first matching value.
7. Stop with `break`.
8. Report when no matching value exists.

**Code:**

```python
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
divisor = int(input("Enter a positive divisor: "))

if start > end:
    print("Starting value must not exceed ending value.")

elif divisor <= 0:
    print("Divisor must be positive.")

else:
    found = False

    for number in range(start, end + 1):
        if number % divisor == 0:
            print("First multiple found:", number)
            found = True
            break

    if not found:
        print("No multiple found in this interval.")
```

**Sample Input:**

```text
Enter the starting value: 1
Enter the ending value: 20
Enter a positive divisor: 5
```

**Sample Output:**

```text
First multiple found: 5
```

**Explanation:**

Five is the first number in the interval divisible by five.

The loop terminates immediately after finding it.

**Complexity:**

- Best-case time: O(1).
- Worst-case time: O(N), where N is the interval size.
- Auxiliary space: O(1).

### Problem 8: Check Prime Number

**Problem Statement:**

Accept a positive integer and check whether it is prime.

Stop divisor testing once a factor is found.

**Logic:**

1. Read the number.
2. Check whether it is one.
3. Initialize the divisor with two.
4. Check divisors while the square of the divisor does not exceed the number.
5. If the remainder is zero, mark the number as non-prime.
6. Execute `break`.
7. Otherwise, increase the divisor.
8. Display the result.

**Code:**

```python
number = int(input("Enter a positive integer: "))

if number < 2:
    print("Not a prime number.")

else:
    divisor = 2
    is_prime = True

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            print("Divisor found:", divisor)
            break

        divisor += 1

    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
```

**Sample Input:**

```text
Enter a positive integer: 15
```

**Sample Output:**

```text
Divisor found: 3
15 is not a prime number.
```

**Explanation:**

The number 15 is divisible by three.

Once a divisor is found, further divisor checks are unnecessary.

**Complexity:**

- Worst-case time: O(√N).
- Auxiliary space: O(1).

### Problem 9: Number Guessing Game

**Problem Statement:**

Create a simple number guessing game with a maximum of three attempts.

Stop when the correct number is guessed.

**Logic:**

1. Define the demonstration number.
2. Set the maximum attempts.
3. Start the attempt counter at one.
4. Accept a guess.
5. Compare it with the secret number.
6. If correct, display success and execute `break`.
7. Otherwise, provide a hint.
8. Repeat until success or the attempts are exhausted.

**Code:**

```python
secret_number = 7

maximum_attempts = 3
attempt = 1

while attempt <= maximum_attempts:
    guess = int(
        input(
            f"Attempt {attempt}/{maximum_attempts}: "
            "Guess the number: "
        )
    )

    if guess == secret_number:
        print("Correct guess!")
        break

    print("Incorrect guess.")

    if guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

    attempt += 1

if attempt > maximum_attempts:
    print("No attempts remaining.")
    print("The demonstration number was:", secret_number)
```

**Sample Run:**

```text
Attempt 1/3: Guess the number: 4
Incorrect guess.
Try a higher number.

Attempt 2/3: Guess the number: 9
Incorrect guess.
Try a lower number.

Attempt 3/3: Guess the number: 7
Correct guess!
```

**Explanation:**

The loop stops immediately after a correct guess.

The attempt counter increases only after an incorrect guess.

**Complexity:**

- Time: O(A), where A is the maximum number of attempts.
- Auxiliary space: O(1).

### Problem 10: Factorial Limit

**Problem Statement:**

Accept a positive limit and find the first factorial value that exceeds it.

**Logic:**

1. Read a positive limit.
2. Initialize factorial with one.
3. Initialize the number with one.
4. Multiply the current factorial by the number.
5. Check whether it exceeds the limit.
6. If it does, display the result and execute `break`.
7. Otherwise, increase the number and continue.

**Code:**

```python
limit = int(input("Enter a positive limit: "))

if limit <= 0:
    print("Enter a positive limit.")

else:
    factorial = 1
    number = 1

    while True:
        factorial *= number

        if factorial > limit:
            print("First factorial exceeding the limit:")
            print(f"{number}! =", factorial)
            break

        number += 1
```

**Sample Input:**

```text
Enter a positive limit: 100
```

**Sample Output:**

```text
First factorial exceeding the limit:
5! = 120
```

**Explanation:**

The factorial values are:

```text
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

The first value greater than 100 is 120.

**Complexity:**

- Time: O(K), where K is the first integer whose factorial exceeds the limit.
- Auxiliary space: O(1), excluding the storage required for the growing integer result.

### Problem 11: Matrix Search

**Problem Statement:**

Accept a matrix and a target value.

Search for the target and stop both loops after finding its first occurrence.

**Logic:**

1. Read matrix dimensions.
2. Accept all matrix elements.
3. Read the target value.
4. Initialize a Boolean flag.
5. Use the outer loop to process rows.
6. Use the inner loop to process columns.
7. When the target is found, record its position.
8. Break the inner loop.
9. Check the flag and break the outer loop.
10. Display the result.

**Code:**

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        value = int(input("Enter element: "))
        current_row.append(value)

    matrix.append(current_row)

target = int(input("Enter the value to search: "))

found = False
found_row = -1
found_column = -1

for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == target:
            found = True
            found_row = row
            found_column = column
            break

    if found:
        break

if found:
    print("Element found.")
    print("Row index:", found_row)
    print("Column index:", found_column)
    print(
        "Position:",
        found_row + 1,
        found_column + 1
    )

else:
    print("Element not found in the matrix.")
```

**Sample Input:**

```text
Enter the number of rows: 2
Enter the number of columns: 3
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Enter element: 6
Enter the value to search: 5
```

**Sample Output:**

```text
Element found.
Row index: 1
Column index: 1
Position: 2 2
```

**Explanation:**

The nested loops search every matrix element.

When the value five is found, the flag becomes true.

The inner and outer loops both terminate.

**Complexity:**

- Best-case time: O(1).
- Worst-case time: O(R × C).
- Auxiliary space: O(R × C) for the input matrix.
- Additional search space: O(1).

### Problem 12: First Value Above Threshold

**Problem Statement:**

Accept a list and a threshold.

Find the first element greater than the threshold.

**Logic:**

1. Read the number of elements.
2. Accept the list values.
3. Read the threshold.
4. Traverse the list with indexes.
5. Check whether each value is greater than the threshold.
6. Display the first match and execute `break`.
7. Report when no matching value exists.

**Code:**

```python
count = int(input("How many numbers do you want? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

threshold = int(input("Enter the threshold: "))

found = False

for index, number in enumerate(numbers):
    if number > threshold:
        print("First value above threshold:", number)
        print("Index:", index)
        found = True
        break

if not found:
    print("No value greater than the threshold was found.")
```

**Sample Input:**

```text
How many numbers do you want? 5
Enter a number: 4
Enter a number: 7
Enter a number: 12
Enter a number: 20
Enter a number: 30
Enter the threshold: 10
```

**Sample Output:**

```text
First value above threshold: 12
Index: 2
```

**Explanation:**

The first two values are not greater than ten.

Twelve is the first value that satisfies the condition.

The loop stops immediately after finding it.

**Complexity:**

- Best-case time: O(1).
- Worst-case time: O(N).
- Auxiliary space: O(1), excluding the input list.

---

## 24. Ten Unsolved Practice Questions

Attempt these questions independently.

Use `break` only when the problem requires early termination.

### Question 1: Stop at a Multiple of Seven

Write a program to print numbers from one to N and stop when the first number divisible by seven is encountered.

Example:

```text
Input:
N = 20

Expected Output:
1 2 3 4 5 6
Stopped at: 7
```

### Question 2: Search for an Element

Write a program to search for a target element in a list.

Stop at the first occurrence.

Example:

```text
Input:
Numbers = [10, 20, 30, 40, 50]
Target = 30

Expected Output:
Element found at index 2
```

### Question 3: Find the First Negative Number

Write a program to find the first negative number in a list.

Example:

```text
Input:
[10, 20, -5, 30, -8]

Expected Output:
First negative number: -5
```

### Question 4: Password Attempts

Write a program that accepts password attempts and stops when the correct password is entered.

Allow a maximum of five attempts.

Example:

```text
Correct Password:
python123

Expected Behaviour:
Stop immediately when python123 is entered.
```

### Question 5: First Prime Number

Write a program to find the first prime number in a list.

Example:

```text
Input:
[4, 6, 8, 11, 15]

Expected Output:
First prime number: 11
```

### Question 6: Running Sum Limit

Write a program to calculate a running sum and stop when it exceeds a specified limit.

Example:

```text
Numbers:
[5, 7, 8, 10]

Limit:
15

Expected Output:
First total exceeding limit: 20
```

### Question 7: First Repeated Character

Write a program to find the first character whose occurrence count becomes two while scanning a string from left to right.

Example:

```text
Input:
programming

Expected Output:
First repeated character: r
```

### Question 8: Matrix Search

Write a program to search for a target in a matrix.

Stop both nested loops after the first occurrence.

Example:

```text
Matrix:
1 2 3
4 5 6

Target:
5

Expected Output:
Found at row 2, column 2
```

### Question 9: Factorial Limit

Write a program to find the first factorial value that exceeds a user-provided limit.

Example:

```text
Input:
Limit = 50

Expected Output:
5! = 120
```

### Question 10: Sentinel-Controlled List Processing

Write a program that processes numbers from a list until a sentinel value is encountered.

Example:

```text
Input:
[10, 20, 30, 0, 40, 50]

Sentinel:
0

Expected Output:
Sum before sentinel: 60
```

---

## 25. Common Mistakes While Using Break

### Mistake 1: Using Break Outside a Loop

Incorrect:

```python
if True:
    break
```

This causes a `SyntaxError` because `break` must be inside a `for` or `while` loop.

Correct:

```python
for number in range(5):
    if number == 2:
        break

    print(number)
```

### Mistake 2: Expecting Break to Stop All Nested Loops

Incorrect assumption:

A `break` statement inside an inner loop automatically terminates every enclosing loop.

Example:

```python
for row in range(3):
    for column in range(3):
        if column == 1:
            break

    print("Outer loop continues.")
```

The inner loop stops, but the outer loop continues.

### Mistake 3: Placing Break Before the Required Output

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)
```

Output:

```text
1
2
```

Three is not printed because `break` executes before `print()`.

If the target must also be displayed, place the print statement before `break`.

```python
for number in range(1, 6):
    print(number)

    if number == 3:
        break
```

Output:

```text
1
2
3
```

### Mistake 4: Forgetting the Found Flag in Nested Loops

A `break` inside an inner loop does not tell the outer loop to stop.

Use a flag or return from a function when both loops must terminate.

### Mistake 5: Incorrect Sentinel Condition

If a program should stop at zero, it must check zero correctly.

Incorrect:

```python
if number == 1:
    break
```

Correct:

```python
if number == 0:
    break
```

### Mistake 6: Forgetting That Break Skips the Loop Else

The loop's `else` block does not execute after `break`.

Incorrect assumption:

The `else` block always runs after the loop.

Correct understanding:

It runs only when the loop finishes normally.

### Mistake 7: Using Break When Continue Is Required

If the goal is to skip one unwanted value but continue processing remaining values, use `continue`.

`break` would terminate the entire nearest loop.

### Mistake 8: Stopping Too Early

Check the break condition carefully.

For example, `number >= 5` and `number == 5` represent different stopping rules.

### Mistake 9: Forgetting to Handle Not Found

A search program should handle both outcomes:

- The target is found.
- The target is not found.

Use a flag, result variable, or loop `else`.

### Mistake 10: Assuming Break Terminates the Program

`break` only exits the nearest enclosing loop.

The statements after the loop still execute.

---

## 26. Best Practices for Using Break

1. Use `break` when continuing the current loop is unnecessary.
2. Keep the break condition clear.
3. Place `break` near the condition that causes termination.
4. Use `break` in search algorithms when only the first match is required.
5. Use a flag when both inner and outer loops must stop.
6. Use `return` when an entire function should finish early.
7. Select sentinel values that do not conflict with valid data.
8. Handle cases where no matching value exists.
9. Understand the nearest-enclosing-loop rule.
10. Avoid unnecessary `break` statements.
11. Do not use `break` when `continue` is the required behaviour.
12. Test the first-match scenario.
13. Test the not-found scenario.
14. Check the placement of output statements around `break`.
15. Understand how `break` affects the loop `else` block.
16. Use input validation in interactive programs.
17. Keep nested-loop termination logic readable.
18. Analyze the best and worst cases of early termination.
19. Do not assume that an early exit always improves worst-case complexity.
20. Use functions to make complex search logic easier to maintain.

---

## 27. Debugging Break Statement Programs

Debugging helps identify incorrect termination conditions and unexpected loop behaviour.

### 27.1 Print the Current Value

```python
for number in range(1, 10):
    print("Checking:", number)

    if number == 5:
        print("Break condition reached.")
        break
```

Output:

```text
Checking: 1
Checking: 2
Checking: 3
Checking: 4
Checking: 5
Break condition reached.
```

### 27.2 Check the Break Condition

Verify that the condition matches the intended stopping point.

### 27.3 Check Statement Order

Compare the positions of:

- The condition.
- The print statement.
- The update statement.
- The `break` statement.

A different order can produce different output.

### 27.4 Check Nested Loop Behaviour

Use separate prints to identify which loop has terminated.

```python
for row in range(1, 4):
    print("Outer:", row)

    for column in range(1, 4):
        print("Inner:", column)

        if column == 2:
            break

    print("Outer loop continues.")
```

### 27.5 Check Search Results

Always test:

- Target present at the beginning.
- Target present in the middle.
- Target present at the end.
- Target absent.
- Target repeated multiple times.

### 27.6 Check Sentinel Values

Confirm that the sentinel is detected before the value is added or processed.

### 27.7 Common Errors

| Error | Possible Cause |
|---|---|
| `SyntaxError` | `break` used outside a loop |
| `IndentationError` | Incorrect placement inside nested blocks |
| `NameError` | Undefined condition variable |
| `ValueError` | Invalid user input |
| Unexpected output | Incorrect statement order |
| Outer loop continues | Break only terminated the inner loop |

---

## 28. Real-Life Applications of Break

### 28.1 Search Systems

A search program can stop after finding the required record.

### 28.2 Login Applications

A login program can stop asking for input after successful authentication.

### 28.3 ATM Applications

An interactive menu can stop processing after the user chooses an exit option.

### 28.4 Number Guessing Games

A guessing game can stop when the correct answer is entered.

### 28.5 Data Validation

A program can stop processing when an invalid record is detected.

### 28.6 Banking Applications

A transaction loop can stop when a cancellation or exit condition occurs.

### 28.7 Data Processing

A file-processing operation may stop when an end marker or error condition is found.

### 28.8 Inventory Systems

A search operation can stop once a particular product is located.

### 28.9 Monitoring Systems

A repeated check can terminate when a specified threshold or event occurs.

### 28.10 Games

A game loop may stop when the player wins, loses, or chooses to exit.

---

## 29. Connection Between Break and DSA

The `break` statement is closely related to early termination in algorithms.

Early termination means stopping an algorithm as soon as the required result has been obtained or continuing is unnecessary.

### 29.1 Linear Search

```python
numbers = [10, 20, 30, 40, 50]
target = 30

for index, number in enumerate(numbers):
    if number == target:
        print("Found at index:", index)
        break
```

Best-case time: O(1).

Worst-case time: O(N).

### 29.2 Finding the First Matching Value

```python
numbers = [4, 8, 12, 15, 20]

for number in numbers:
    if number > 10:
        print("First number above 10:", number)
        break
```

The loop stops when it finds the first qualifying value.

### 29.3 Prime Number Checking

```python
number = 29
divisor = 2
is_prime = True

while divisor * divisor <= number:
    if number % divisor == 0:
        is_prime = False
        break

    divisor += 1

print(is_prime)
```

The loop stops when a divisor is found.

### 29.4 Matrix Search

Nested loops can stop both levels after finding the target by using a flag.

### 29.5 Finding the First Duplicate Pair

```python
numbers = [1, 2, 3, 2, 4]

found = False

for first in range(len(numbers)):
    for second in range(first + 1, len(numbers)):
        if numbers[first] == numbers[second]:
            print("Duplicate:", numbers[first])
            found = True
            break

    if found:
        break
```

The search stops when the first duplicate pair is found.

### 29.6 Binary Search

Binary Search uses a different approach to reduce a search interval.

Although it does not require `break` in every implementation, early termination can be used when a matching value is found.

### 29.7 Two-Pointer Algorithms

Some two-pointer problems stop processing once the pointer conditions are no longer satisfied.

### 29.8 Brute-Force Algorithms

A brute-force search can stop when it finds a valid answer if only one result is required.

### 29.9 Search in Collections

Searching algorithms can use `break` to avoid checking unnecessary remaining elements.

### 29.10 Early Termination and Complexity

Early termination can improve performance for particular inputs.

However, it does not necessarily change the worst-case Big O complexity.

---

## 30. Time and Space Complexity

Time complexity describes how algorithm execution time grows with input size.

Space complexity describes how memory requirements grow with input size.

The `break` statement can reduce the number of executed iterations.

However, complexity analysis must consider the input cases and the algorithm structure.

### 30.1 Fixed Loop with Early Break

```python
for number in range(1, 11):
    if number == 3:
        break

    print(number)
```

The loop stops after a fixed number of iterations.

Time complexity: O(1).

### 30.2 Linear Search with Break

```python
for number in numbers:
    if number == target:
        break
```

Best case:

The target is the first element.

Time complexity: O(1).

Worst case:

The target is the final element or is absent.

Time complexity: O(N).

### 30.3 Search in a Matrix

```python
for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == target:
            break
```

This version stops the inner loop at a match, but the outer loop can continue.

Its worst-case complexity is O(R × C).

### 30.4 Matrix Search with Two-Level Termination

A flag can stop both the inner and outer loops.

Best-case time: O(1).

Worst-case time: O(R × C).

### 30.5 Prime Checking with Early Break

```python
divisor = 2

while divisor * divisor <= number:
    if number % divisor == 0:
        break

    divisor += 1
```

The algorithm checks at most approximately the square root of the number.

Worst-case time: O(√N).

### 30.6 Fixed Maximum Attempts

```python
attempt = 1

while attempt <= 3:
    if success:
        break

    attempt += 1
```

The loop has at most three iterations.

Time complexity: O(1).

### Complexity Reference

| Problem Pattern | Best-Case Time | Worst-Case Time |
|---|---|---|
| Linear search | O(1) | O(N) |
| First matching element | O(1) | O(N) |
| Search in R-by-C matrix | O(1) | O(R × C) |
| Prime checking up to square root | O(1) for very small inputs | O(√N) |
| Fixed number of attempts | O(1) | O(1) |
| Fixed-size loop | O(1) | O(1) |
| Pair search with nested loops | Depends on match position | O(N²) |

### Important Note

`break` can reduce the number of iterations for some inputs.

It does not guarantee that the worst-case complexity becomes smaller.

For example, linear search remains O(N) in the worst case even when it uses `break`.

---

## 31. Mini Project: Smart Number Search

### Project Objective

Create an interactive number-search program that accepts a list and allows the user to search for values.

The program should:

1. Accept the number of elements.
2. Read all list values.
3. Accept a search target.
4. Search using a `for` loop.
5. Stop at the first matching element.
6. Display its index and position.
7. Allow repeated searches.
8. Stop the search menu when the user chooses to exit.

### Project Code

```python
"""
Project: Smart Number Search

Description:
Search for values in a list using linear search and break.
"""


def read_numbers() -> list[int]:
    """
    Read a list of integers from the user.
    """
    while True:
        try:
            count = int(
                input("How many numbers do you want to enter? ")
            )

            if count <= 0:
                print("Enter at least one number.")
                continue

            break

        except ValueError:
            print("Please enter a valid integer.")

    numbers = []

    for index in range(count):
        while True:
            try:
                number = int(
                    input(f"Enter number {index + 1}: ")
                )

                numbers.append(number)
                break

            except ValueError:
                print("Please enter a valid integer.")

    return numbers


def linear_search(
    numbers: list[int],
    target: int
) -> int:
    """
    Search for the first occurrence of a target value.

    Returns:
        The index of the first match, or -1 if absent.
    """
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


def main() -> None:
    """
    Display a repeated search menu.
    """
    numbers = read_numbers()

    print("\nStored numbers:", numbers)

    while True:
        print("\n" + "=" * 45)
        print("          SMART NUMBER SEARCH")
        print("=" * 45)

        print("1. Search for a number")
        print("2. Display the list")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid menu option.")
            continue

        if choice == 1:
            try:
                target = int(input("Enter the target: "))

            except ValueError:
                print("Please enter a valid integer.")
                continue

            result = linear_search(numbers, target)

            if result != -1:
                print("Element found.")
                print("Index:", result)
                print("Position:", result + 1)

            else:
                print("Element not found.")

        elif choice == 2:
            print("Stored numbers:", numbers)

        elif choice == 0:
            print("Exiting Smart Number Search.")
            break

        else:
            print("Invalid choice. Select 0, 1, or 2.")


if __name__ == "__main__":
    main()
```

### Sample Input

```text
How many numbers do you want to enter? 5
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
Enter number 5: 50
```

### Sample Run

```text
Stored numbers: [10, 20, 30, 40, 50]

=============================================
          SMART NUMBER SEARCH
=============================================
1. Search for a number
2. Display the list
0. Exit
Enter your choice: 1
Enter the target: 30
Element found.
Index: 2
Position: 3
```

### Concepts Used

- `for` loops.
- `while` loops.
- `break`.
- Linear search.
- Lists.
- Functions.
- Indexes.
- Input validation.
- Conditional statements.
- Early termination.

---

## 32. Fifty Viva Questions and Answers

### Basic Questions

**Q1. What is the break statement in Python?**

The `break` statement terminates the nearest enclosing loop immediately.

**Q2. Why is break used?**

It is used when a loop should stop before completing all its iterations.

**Q3. Can break be used inside a for loop?**

Yes. It can terminate a `for` loop.

**Q4. Can break be used inside a while loop?**

Yes. It can terminate a `while` loop.

**Q5. What happens after break executes?**

Execution moves to the first statement after the nearest enclosing loop.

**Q6. Does break terminate the entire Python program?**

No. It terminates only the nearest enclosing loop.

**Q7. Can break be used outside a loop?**

No. Using it outside a loop causes a syntax error.

**Q8. What is early termination?**

Early termination means stopping an operation as soon as a required condition is satisfied.

**Q9. Does break skip the remaining iterations of its loop?**

Yes. The remaining iterations of the nearest enclosing loop are skipped.

**Q10. What is the nearest enclosing loop?**

It is the closest loop surrounding the location of the `break` statement.

### Loop Control Questions

**Q11. Can break terminate both nested loops?**

A single break terminates only the nearest enclosing loop.

**Q12. How can both nested loops be stopped?**

Use a Boolean flag or return from the containing function.

**Q13. Can break be used with a while True loop?**

Yes. It is commonly used to provide an exit condition.

**Q14. What is a sentinel value?**

A special value used to indicate that repeated processing should stop.

**Q15. Give an example of a sentinel value.**

Zero can be used to stop repeated numeric input.

**Q16. What happens if break is executed inside a while loop?**

The nearest enclosing while loop terminates immediately.

**Q17. Can break be used inside an if statement?**

Yes, provided that the if statement is inside a loop.

**Q18. Does break stop the outer loop when it is inside an inner loop?**

No. It stops only the inner loop.

**Q19. What is the purpose of a Boolean flag in nested loops?**

It communicates a condition, such as a successful search, to the outer loop.

**Q20. Does break execute the statements after the loop?**

Yes. Normal execution continues after the loop.

### Break, Continue, and Pass

**Q21. What is the difference between break and continue?**

`break` terminates the nearest loop, while `continue` skips the current iteration and proceeds to the next one.

**Q22. What is the purpose of pass?**

`pass` performs no operation and acts as a placeholder.

**Q23. Does continue terminate a loop?**

No. It skips the remainder of the current iteration.

**Q24. Does pass change loop execution?**

No. It does not alter normal loop execution.

**Q25. Which statement is used to stop a loop immediately?**

`break`.

**Q26. Which statement skips the current iteration?**

`continue`.

**Q27. Which statement performs no operation?**

`pass`.

**Q28. What happens to a loop's else block when break executes?**

The loop's `else` block is skipped.

**Q29. When does a loop's else block execute?**

It executes when the loop completes normally without `break`.

**Q30. Is loop else the same as an if-else statement?**

No. It is associated with normal completion of a loop.

### Programming Questions

**Q31. How can you find the first occurrence of an element?**

Traverse the collection, check each element, and execute `break` when a match is found.

**Q32. How can you find the first even number?**

Check every number using `number % 2 == 0` and break after the first match.

**Q33. How can you find the first vowel in a string?**

Iterate through its characters, check vowel membership, and break when a vowel is found.

**Q34. How can break be used in a number guessing game?**

Break the loop when the correct number is guessed.

**Q35. How can break be used in input processing?**

Use a sentinel value or condition to stop accepting input.

**Q36. How can break stop a matrix search?**

Use break for the inner loop and a flag to terminate the outer loop.

**Q37. How does break help in prime checking?**

It stops divisor testing as soon as a factor is found.

**Q38. What is linear search?**

Linear search examines elements sequentially until a match is found or the collection is exhausted.

**Q39. What does a search program display when no target is found?**

It should display a not-found result after the loop finishes without a match.

**Q40. Why is break useful in threshold-based calculations?**

It stops repeated calculations as soon as the required threshold condition is reached.

### DSA and Complexity Questions

**Q41. What is time complexity?**

Time complexity describes how an algorithm's running time grows with input size.

**Q42. What is the best-case time complexity of linear search?**

O(1), when the target is the first element.

**Q43. What is the worst-case time complexity of linear search?**

O(N).

**Q44. Does break always improve worst-case complexity?**

No. It can reduce iterations for some inputs without changing the worst-case complexity.

**Q45. What is early exit in an algorithm?**

It is terminating an algorithm before processing all possible inputs once its result is known.

**Q46. Can break be used in nested matrix searches?**

Yes. It can stop the inner loop, and an additional mechanism can stop the outer loop.

**Q47. What is a brute-force search?**

A direct approach that checks possible candidates systematically.

**Q48. What is a Boolean flag?**

A variable that stores a true or false state.

**Q49. When is return preferable to break?**

When a function should terminate completely and return a result immediately.

**Q50. Which concepts should be understood before using break in advanced DSA problems?**

Loop termination, nested loops, searching, Boolean flags, sentinel values, and complexity analysis.

---

## 33. Important Terminology

| Term | Meaning |
|---|---|
| `break` | Terminates the nearest enclosing loop |
| Early Termination | Stopping before all iterations are completed |
| Loop Control | Statements that change normal loop flow |
| Nearest Enclosing Loop | The closest loop containing the break statement |
| Sentinel | Special value used to stop repetition |
| Linear Search | Sequential search through collection elements |
| First Occurrence | Earliest matching element in traversal order |
| Boolean Flag | Variable storing True or False |
| Inner Loop | Loop placed inside another loop |
| Outer Loop | Loop containing another loop |
| `continue` | Skips the rest of the current iteration |
| `pass` | Null statement that performs no operation |
| Loop Else | Block executed when a loop completes normally |
| Threshold | Boundary value used in a condition |
| Accumulator | Variable storing a running result |
| Counter | Variable used for counting |
| Prime Number | Integer greater than one with exactly two positive divisors |
| Divisor | Integer that divides another integer without a remainder |
| Matrix Search | Searching for a value inside a matrix |
| Input Validation | Checking whether provided data is acceptable |
| Worst Case | Input requiring the maximum amount of work |
| Best Case | Input requiring the minimum amount of work |
| Time Complexity | Growth of execution time |
| Auxiliary Space | Additional memory used by an algorithm |

---

## 34. Quick Revision Notes

### Basic Syntax

```python
for item in iterable:
    if condition:
        break
```

### Break with For Loop

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

### Break with While Loop

```python
number = 1

while number <= 10:
    if number == 5:
        break

    print(number)
    number += 1
```

### Linear Search

```python
numbers = [10, 20, 30, 40]

target = 30

for index, number in enumerate(numbers):
    if number == target:
        print("Found:", index)
        break
```

### First Even Number

```python
numbers = [1, 3, 5, 8, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)
        break
```

### Sentinel Loop

```python
while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    print(number)
```

### Break in Nested Loops

```python
for row in range(3):
    for column in range(3):
        if column == 2:
            break

        print(row, column)
```

### Stop Both Nested Loops

```python
found = False

for row in range(3):
    for column in range(3):
        if row == 1 and column == 1:
            found = True
            break

    if found:
        break
```

### Loop Else

```python
for number in range(5):
    if number == 3:
        break
else:
    print("Loop completed normally.")
```

The `else` block is skipped because the loop exits through `break`.

### Important Rules

- Break terminates the nearest enclosing loop.
- It works inside both `for` and `while` loops.
- It must be used within a loop.
- It skips the remaining iterations of that loop.
- A break inside an inner loop does not automatically stop the outer loop.
- Use a flag or `return` when both loops must terminate.
- A sentinel can control when a loop stops.
- A loop's `else` block is skipped when `break` executes.

### Complexity Reference

| Algorithm | Best Case | Worst Case |
|---|---|---|
| Linear Search | O(1) | O(N) |
| First matching value | O(1) | O(N) |
| Matrix Search | O(1) | O(R × C) |
| Prime checking up to square root | O(1) for suitable small inputs | O(√N) |
| Fixed attempts | O(1) | O(1) |

---

## 35. Learning Checklist

### Break Fundamentals

- [ ] I understand what the break statement is.
- [ ] I understand why break is used.
- [ ] I can use break inside a for loop.
- [ ] I can use break inside a while loop.
- [ ] I understand the nearest-enclosing-loop rule.
- [ ] I know that break does not terminate the whole program.
- [ ] I understand how break affects normal loop execution.

### Searching and Conditions

- [ ] I can find the first matching element.
- [ ] I can find the first even number.
- [ ] I can find the first vowel.
- [ ] I can stop when a negative number is found.
- [ ] I can stop when a threshold is exceeded.
- [ ] I can use break in prime-number checking.

### Nested Loops

- [ ] I understand break in an inner loop.
- [ ] I understand why the outer loop may continue.
- [ ] I can use a flag to stop both loops.
- [ ] I understand when `return` is preferable.

### Input and Loop Control

- [ ] I understand sentinel values.
- [ ] I can use break with `while True`.
- [ ] I can stop repeated attempts after success.
- [ ] I understand break versus continue.
- [ ] I understand the purpose of pass.
- [ ] I understand loop else behaviour.

### DSA Preparation

- [ ] I understand early termination.
- [ ] I can implement linear search.
- [ ] I can identify best-case complexity.
- [ ] I can identify worst-case complexity.
- [ ] I understand why break does not always change worst-case Big O.
- [ ] I can apply break to matrix searching.

---

## 36. How to Run the Python File

### Step 1: Open Your Repository

Open the `DSA-Python` repository in VS Code.

### Step 2: Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 06-Break-Statement/
            ├── README.md
            └── 06_break_statement.py
```

### Step 3: Open the Terminal

Open the integrated terminal in VS Code.

### Step 4: Run the Python File

Execute this command from the repository root:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/06-Break-Statement/06_break_statement.py
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

Enter the option you want to execute.

---

## 37. Repository Structure

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
            ├── 01-Introduction-to-Loops/
            │   ├── README.md
            │   └── 01_introduction_to_loops.py
            │
            ├── 02-For-Loop/
            │   ├── README.md
            │   └── 02_for_loop.py
            │
            ├── 03-Range-Function/
            │   ├── README.md
            │   └── 03_range_function.py
            │
            ├── 04-While-Loop/
            │   ├── README.md
            │   └── 04_while_loop.py
            │
            ├── 05-Nested-Loops/
            │   ├── README.md
            │   └── 05_nested_loops.py
            │
            └── 06-Break-Statement/
                ├── README.md
                └── 06_break_statement.py
```

### File Responsibilities

**README.md**

Contains:

- Introduction.
- Learning objectives.
- Break statement definition.
- Syntax and execution.
- Break in for loops.
- Break in while loops.
- Finding matching elements.
- Finding the first even number.
- Finding the first vowel.
- Sentinel-controlled loops.
- Break in nested loops.
- Stopping both loops.
- Number guessing.
- Threshold-based termination.
- Prime-number checking.
- Loop else behaviour.
- Break versus continue versus pass.
- Twelve topic examples.
- Twelve solved problems.
- Ten unsolved practice questions.
- Common mistakes.
- Best practices.
- Debugging.
- Real-life applications.
- DSA connections.
- Complexity analysis.
- Mini project.
- Fifty viva questions and answers.
- Terminology.
- Quick revision.
- Learning checklist.
- Execution instructions.

**06_break_statement.py**

Contains:

- Twelve executable topic examples.
- Twelve selectable solved problems.
- Ten unsolved practice questions.
- Learning checklist.
- Interactive menu.
- Input validation.
- Matrix search example.
- Early termination examples.

---

## 38. Final Summary

The `break` statement is an important Python loop-control statement.

It terminates the nearest enclosing loop immediately when a specified condition is satisfied.

It can be used with both `for` and `while` loops.

The statement is particularly useful when:

- A target value is found.
- The first matching element is identified.
- A sentinel value is received.
- An invalid value is encountered.
- A threshold is exceeded.
- A user completes a task successfully.
- Further iterations are unnecessary.

In nested loops, `break` stops only the nearest enclosing loop.

A flag or `return` can be used when both the inner and outer loops need to terminate.

The difference between `break`, `continue`, and `pass` should also be understood carefully.

In DSA, early termination is useful in searching, divisor checking, and other algorithms.

Although `break` can reduce the number of operations for particular inputs, it does not necessarily improve worst-case time complexity.

### What You Should Do Next

1. Understand the meaning of break.
2. Practise break in a `for` loop.
3. Practise break in a `while` loop.
4. Understand how it behaves in nested loops.
5. Learn sentinel-controlled termination.
6. Understand the difference between break, continue, and pass.
7. Run `06_break_statement.py`.
8. Execute all twelve examples.
9. Attempt all twelve solved problems.
10. Solve the ten unsolved questions.
11. Complete the learning checklist.
12. Revise the fifty viva questions.

**Topic Completed: Break Statement in Python**

The next topic in this repository is:

`07-Continue-Statement`

Its Python source file will be:

`07_continue_statement.py`