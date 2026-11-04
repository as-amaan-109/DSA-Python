# Topic 07 – Continue Statement in Python

**Part 2:** Python Fundamentals  
**Section:** 01 – Loops  
**Topic Number:** 07  
**Source File:** `07_continue_statement.py`  
**Language:** Python 3.9+

---

# Table of Contents

1. Introduction to Continue Statement
2. Learning Objectives
3. What Is the Continue Statement?
4. Syntax of Continue
5. How Continue Works
6. Continue with for Loop
7. Continue with while Loop
8. Continue with Conditional Statements
9. Continue with Lists
10. Continue with Strings
11. Continue with Nested Loops
12. Continue vs Break vs Pass
13. Continue and Loop Else
14. Twelve Topic Examples
15. Twelve Solved Programming Problems
16. Ten Unsolved Practice Questions
17. Common Mistakes
18. Best Practices
19. Debugging Continue Statement
20. Real-Life Applications
21. Connection with Data Structures and Algorithms
22. Time and Space Complexity
23. Mini Project – Data Filtering System
24. Fifty Python Viva Questions and Answers
25. Important Terminology
26. Quick Revision Notes
27. Learning Checklist
28. How to Run the Python File
29. Repository Structure
30. Final Summary

---

# 1. Introduction to Continue Statement

The `continue` statement is a loop control statement in Python.

It is used when we want to skip the remaining statements in the current iteration of a loop and move directly to the next iteration.

Sometimes, while processing data, we do not want to perform an operation on every item.

For example:

- Print numbers from 1 to 20 but skip multiples of 3.
- Display only odd numbers.
- Ignore empty strings from a list.
- Skip invalid student marks.
- Ignore zero values while calculating an average.
- Process only records that satisfy a condition.

We can use conditional statements to decide which iterations should be skipped.

The `continue` statement makes this process easier and more readable.

## Simple Example

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

**Output:**

```text
1
2
4
5
```

The number `3` is not printed because the `continue` statement skips the remaining part of that iteration.

## Explanation

| Iteration | Number | Condition | Result |
|---|---:|---|---|
| 1 | 1 | False | Print 1 |
| 2 | 2 | False | Print 2 |
| 3 | 3 | True | Skip printing |
| 4 | 4 | False | Print 4 |
| 5 | 5 | False | Print 5 |

The loop does not terminate when it encounters `continue`. It simply moves to the next iteration.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand the purpose of the `continue` statement.
2. Understand the syntax of `continue`.
3. Use `continue` inside a `for` loop.
4. Use `continue` inside a `while` loop.
5. Skip selected numbers during iteration.
6. Print only odd numbers using `continue`.
7. Print only even numbers using `continue`.
8. Skip specific elements from lists.
9. Skip characters while processing strings.
10. Ignore empty or invalid records.
11. Use `continue` in mathematical calculations.
12. Understand `continue` in nested loops.
13. Differentiate between `break`, `continue`, and `pass`.
14. Avoid infinite loops when using `continue`.
15. Apply loop filtering in practical programming problems.

---

# 3. What Is the Continue Statement?

The `continue` statement skips the remaining statements in the current iteration of a loop.

It does not stop the complete loop.

It transfers control to the next iteration.

## Important Points

- `continue` is a Python keyword.
- It is used inside loops.
- It works with `for` loops.
- It works with `while` loops.
- It skips the current iteration's remaining statements.
- It does not permanently terminate the loop.
- It can be used with `if` conditions.
- It is useful for filtering values.
- In nested loops, it affects only the nearest enclosing loop.
- In a `while` loop, the loop condition and counter updates must be handled carefully.

## Example

```python
for number in range(1, 8):

    if number == 4:
        continue

    print("Current number:", number)

print("Loop completed.")
```

**Output:**

```text
Current number: 1
Current number: 2
Current number: 3
Current number: 5
Current number: 6
Current number: 7
Loop completed.
```

Here, the loop skips only the iteration where `number` is 4.

The remaining iterations execute normally.

---

# 4. Syntax of Continue

The basic syntax is:

```python
for variable in sequence:

    if condition:
        continue

    statement
```

For a `while` loop:

```python
while condition:

    if skip_condition:
        continue

    statement
```

## Understanding the Syntax

| Component | Meaning |
|---|---|
| `for` | Starts a for loop |
| `while` | Starts a while loop |
| `if` | Checks a condition |
| `condition` | Determines whether an iteration should be skipped |
| `continue` | Skips the remaining statements in the current iteration |
| `statement` | Executes when the continue condition is false |

## Example

```python
for number in range(1, 6):

    if number == 2:
        continue

    print(number)

    print("Processing completed")
```

**Output:**

```text
1
Processing completed
3
Processing completed
4
Processing completed
5
Processing completed
```

When the number is 2, both print statements after `continue` are skipped.

---

# 5. How Continue Works

The `continue` statement changes the normal flow of a loop.

Without `continue`, the statements inside the loop execute normally.

When Python encounters `continue`, it skips the remaining statements in the current iteration.

## Execution Flow

```text
          Start Loop
              |
              v
        Check Loop Condition
              |
          Is True?
           /    \
         No      Yes
         |        |
         v        v
     End Loop   Execute Statements
                    |
                    v
             Check Continue Condition
                    |
                Is True?
                 /    \
               Yes     No
                |       |
                v       v
         Skip Remaining  Execute Remaining
         Statements      Statements
                |            |
                |            |
                v            |
          Next Iteration <---+
```

## Example

```python
for number in range(1, 6):

    print("Before condition:", number)

    if number == 3:
        continue

    print("After condition:", number)
```

**Output:**

```text
Before condition: 1
After condition: 1
Before condition: 2
After condition: 2
Before condition: 3
Before condition: 4
After condition: 4
Before condition: 5
After condition: 5
```

The statement after `continue` is not executed when the number is 3.

## Important Understanding

`continue` does not mean:

- Stop the complete loop.
- Exit the program.
- Skip all future iterations.
- Restart the program.

It means only:

**Skip the rest of the current iteration and move to the next iteration.**

---

# 6. Continue with for Loop

A `for` loop is commonly used when we want to iterate through a sequence or a range.

The `continue` statement can skip specific values during iteration.

## Example 1: Skip Number 5

```python
for number in range(1, 11):

    if number == 5:
        continue

    print(number)
```

**Output:**

```text
1
2
3
4
6
7
8
9
10
```

## Example 2: Skip Even Numbers

```python
for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)
```

**Output:**

```text
1
3
5
7
9
```

Explanation:

- `%` is the modulus operator.
- `number % 2 == 0` identifies even numbers.
- `continue` skips even numbers.
- The remaining odd numbers are printed.

## Example 3: Skip Odd Numbers

```python
for number in range(1, 11):

    if number % 2 != 0:
        continue

    print(number)
```

**Output:**

```text
2
4
6
8
10
```

Explanation:

- Odd numbers have a remainder of 1 when divided by 2.
- The condition skips those numbers.
- Only even numbers are printed.

## Example 4: Skip Multiples of 3

```python
for number in range(1, 16):

    if number % 3 == 0:
        continue

    print(number)
```

**Output:**

```text
1
2
4
5
7
8
10
11
13
14
```

## Applications

Using `continue` with a `for` loop is useful for:

- Filtering numbers.
- Processing lists.
- Searching through collections.
- Ignoring unwanted values.
- Validating data.
- Processing records.

---

# 7. Continue with while Loop

A `while` loop repeatedly executes statements while its condition remains true.

The `continue` statement can also be used inside a `while` loop.

However, extra care is required.

The programmer must ensure that the loop variable is updated even when an iteration is skipped.

## Example 1: Skip Even Numbers

```python
number = 0

while number < 10:

    number += 1

    if number % 2 == 0:
        continue

    print(number)
```

**Output:**

```text
1
3
5
7
9
```

Explanation:

1. The counter starts at 0.
2. The counter increases by 1.
3. Python checks whether the number is even.
4. If the number is even, the current iteration is skipped.
5. Otherwise, the number is printed.

## Example 2: Skip Number 4

```python
number = 0

while number < 7:

    number += 1

    if number == 4:
        continue

    print(number)
```

**Output:**

```text
1
2
3
5
6
7
```

## Important Warning: Infinite Loop

Consider this incorrect program:

```python
number = 0

while number < 5:

    if number == 2:
        continue

    number += 1

    print(number)
```

This program can create an infinite loop.

Why?

When `number` becomes 2:

1. The condition becomes true.
2. Python executes `continue`.
3. The increment statement is skipped.
4. The number remains 2.
5. The condition remains true.
6. The same iteration pattern repeats.

## Correct Program

```python
number = 0

while number < 5:

    number += 1

    if number == 2:
        continue

    print(number)
```

**Output:**

```text
1
3
4
5
```

**Remember:** In a `while` loop, place necessary counter updates before a possible `continue`, or use another structure that guarantees progress.

---

# 8. Continue with Conditional Statements

The `continue` statement is frequently used with `if` and `if-else` conditions.

It helps decide which values should be processed.

## Example: Display Passing Marks

```python
marks = [30, 45, 78, 20, 90, 35, 66]

for mark in marks:

    if mark < 40:
        continue

    print("Pass:", mark)
```

**Output:**

```text
Pass: 45
Pass: 78
Pass: 90
Pass: 66
```

Explanation:

- Marks below 40 are skipped.
- Marks equal to or above 40 are printed.

## Example: Skip Negative Numbers

```python
numbers = [10, -5, 20, -3, 30, 0, 40]

for number in numbers:

    if number < 0:
        continue

    print(number)
```

**Output:**

```text
10
20
30
0
40
```

Only negative numbers are skipped.

## Example: Skip Invalid Ages

```python
ages = [18, 25, -2, 30, 150, 22]

for age in ages:

    if age < 0 or age > 120:
        continue

    print("Valid age:", age)
```

**Output:**

```text
Valid age: 18
Valid age: 25
Valid age: 30
Valid age: 22
```

---

# 9. Continue with Lists

A list stores multiple values in a single variable.

We can use a loop to access every list element.

The `continue` statement allows us to skip selected elements.

## Example 1: Skip Mango

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:

    if fruit == "Mango":
        continue

    print(fruit)
```

**Output:**

```text
Apple
Banana
Orange
```

## Example 2: Skip Zero Values

```python
numbers = [10, 0, 20, 0, 30, 40]

for number in numbers:

    if number == 0:
        continue

    print(number)
```

**Output:**

```text
10
20
30
40
```

## Example 3: Skip Empty List Elements

```python
names = ["Amaan", "", "Rahul", "", "Ali"]

for name in names:

    if name == "":
        continue

    print(name)
```

**Output:**

```text
Amaan
Rahul
Ali
```

## Example 4: Sum Only Positive Numbers

```python
numbers = [10, -5, 20, -2, 30]

total = 0

for number in numbers:

    if number <= 0:
        continue

    total += number

print("Total:", total)
```

**Output:**

```text
Total: 60
```

## Important Point

The `continue` statement does not modify the list.

It only changes which elements are processed during the loop.

---

# 10. Continue with Strings

Strings are sequences of characters.

We can iterate through a string using a loop.

The `continue` statement can skip selected characters.

## Example 1: Skip Spaces

```python
text = "PYTHON PROGRAMMING"

for character in text:

    if character == " ":
        continue

    print(character, end="")
```

**Output:**

```text
PYTHONPROGRAMMING
```

## Example 2: Skip Vowels

```python
text = "PROGRAMMING"
vowels = "AEIOU"

for character in text:

    if character in vowels:
        continue

    print(character, end="")
```

**Output:**

```text
PRGRMMNG
```

## Example 3: Skip Digits

```python
text = "PYTHON123PROGRAMMING"

for character in text:

    if character.isdigit():
        continue

    print(character, end="")
```

**Output:**

```text
PYTHONPROGRAMMING
```

## Example 4: Skip Special Characters

```python
text = "Hello@123 World!"

for character in text:

    if not character.isalnum() and not character.isspace():
        continue

    print(character, end="")
```

**Output:**

```text
Hello123 World
```

---

# 11. Continue with Nested Loops

A nested loop means a loop inside another loop.

The `continue` statement affects only the nearest enclosing loop in which it appears.

This is an important concept.

## Example

```python
for row in range(1, 4):

    print("Row:", row)

    for column in range(1, 6):

        if column == 3:
            continue

        print(column, end=" ")

    print()
```

**Output:**

```text
Row: 1
1 2 4 5
Row: 2
1 2 4 5
Row: 3
1 2 4 5
```

Explanation:

- The outer loop controls rows.
- The inner loop controls columns.
- When the column is 3, only that inner-loop iteration is skipped.
- The outer loop continues normally.

## Important Point

A `continue` statement inside the inner loop does not automatically skip the outer loop.

## Example: Multiplication Table

```python
for number in range(1, 4):

    for multiplier in range(1, 6):

        if multiplier == 3:
            continue

        print(f"{number} x {multiplier} = {number * multiplier}")

    print()
```

The multiplication expressions using 3 are skipped, but all other inner iterations execute.

---

# 12. Continue vs Break vs Pass

Python provides three statements that are often discussed together:

- `break`
- `continue`
- `pass`

They have different purposes.

## Comparison Table

| Feature | break | continue | pass |
|---|---|---|---|
| Purpose | Terminates the nearest loop | Skips current iteration | Performs no operation |
| Loop continues? | No | Yes | Yes |
| Skips remaining statements in current iteration? | Yes, by exiting loop | Yes | No |
| Used inside loops? | Yes | Yes | Yes |
| Used in function/class placeholders? | Not as an exit mechanism | No | Yes |
| Typical application | Stop searching | Skip unwanted data | Temporary placeholder |

## Example 1: break

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)
```

**Output:**

```text
1
2
```

The loop terminates when the number reaches 3.

## Example 2: continue

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

**Output:**

```text
1
2
4
5
```

The loop skips 3 and continues.

## Example 3: pass

```python
for number in range(1, 6):

    if number == 3:
        pass

    print(number)
```

**Output:**

```text
1
2
3
4
5
```

`pass` does nothing, so the print statement still executes.

## Remember

- `break` means stop the nearest loop.
- `continue` means skip the current iteration.
- `pass` means do nothing.

---

# 13. Continue and Loop Else

Python supports an `else` clause with `for` and `while` loops.

The loop's `else` clause executes when the loop finishes normally.

A loop's `else` clause is skipped when that loop is terminated by `break`.

**Important:** A `continue` statement does not prevent the loop's `else` clause from executing.

## Example: Continue with Loop Else

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)

else:
    print("Loop completed normally.")
```

**Output:**

```text
1
2
4
5
Loop completed normally.
```

The loop was not terminated by `break`. Therefore, its `else` clause executes.

## Comparison

| Situation | Loop else executes? |
|---|---|
| Loop completes normally | Yes |
| Loop uses continue and finishes normally | Yes |
| Loop terminates with break | No |

---

# 14. Twelve Topic Examples

The following examples correspond to the twelve examples in `07_continue_statement.py`.

## Example 01 – Skip a Specific Number

**Objective:** Print numbers from 1 to 10 but skip 5.

```python
for number in range(1, 11):

    if number == 5:
        continue

    print(number, end=" ")
```

**Output:**

```text
1 2 3 4 6 7 8 9 10
```

**Concept:** Conditional skipping in a for loop.

## Example 02 – Print Only Odd Numbers

**Objective:** Skip all even numbers.

```python
for number in range(1, 16):

    if number % 2 == 0:
        continue

    print(number, end=" ")
```

**Output:**

```text
1 3 5 7 9 11 13 15
```

**Concept:** Modulus operator with continue.

## Example 03 – Print Only Even Numbers

**Objective:** Skip all odd numbers.

```python
for number in range(1, 16):

    if number % 2 != 0:
        continue

    print(number, end=" ")
```

**Output:**

```text
2 4 6 8 10 12 14
```

**Concept:** Conditional filtering.

## Example 04 – Skip a List Element

**Objective:** Skip Mango from a list of fruits.

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

for fruit in fruits:

    if fruit == "Mango":
        continue

    print(fruit)
```

**Output:**

```text
Apple
Banana
Orange
Grapes
```

**Concept:** List iteration.

## Example 05 – Skip a Character in a String

**Objective:** Skip the character O.

```python
message = "PYTHON PROGRAMMING"

for character in message:

    if character == "O":
        continue

    print(character, end="")
```

**Output:**

```text
PYTHN PRGRAMMING
```

**Concept:** String iteration.

## Example 06 – Skip Empty Strings

**Objective:** Ignore empty elements from a list.

```python
names = ["Amaan", "", "Rahul", "", "Sneha", "Ali"]

for name in names:

    if name == "":
        continue

    print(name)
```

**Output:**

```text
Amaan
Rahul
Sneha
Ali
```

**Concept:** Empty value filtering.

## Example 07 – Continue in a while Loop

**Objective:** Print odd numbers using a while loop.

```python
number = 0

while number < 10:

    number += 1

    if number % 2 == 0:
        continue

    print(number, end=" ")
```

**Output:**

```text
1 3 5 7 9
```

**Concept:** Continue with while loop and counter updates.

## Example 08 – Skip Zero and Negative Numbers

**Objective:** Calculate the sum of positive numbers only.

```python
numbers = [10, -5, 20, 0, -3, 30, 40]

total = 0

for number in numbers:

    if number <= 0:
        continue

    total += number

print(total)
```

**Output:**

```text
100
```

**Concept:** Conditional summation.

## Example 09 – Skip Multiples of Three

**Objective:** Print numbers from 1 to 20 except multiples of 3.

```python
for number in range(1, 21):

    if number % 3 == 0:
        continue

    print(number, end=" ")
```

**Output:**

```text
1 2 4 5 7 8 10 11 13 14 16 17 19 20
```

**Concept:** Multiple filtering.

## Example 10 – Continue in Nested Loops

**Objective:** Skip column 3 in every row.

```python
for row in range(1, 4):

    print(f"Row {row}:")

    for column in range(1, 6):

        if column == 3:
            continue

        print(column, end=" ")

    print()
```

**Output:**

```text
Row 1:
1 2 4 5
Row 2:
1 2 4 5
Row 3:
1 2 4 5
```

**Concept:** Continue in nested loops.

## Example 11 – Filter Values Using Conditions

**Objective:** Display marks greater than or equal to 40.

```python
marks = [45, 78, 32, 90, 55, 20, 88]

for mark in marks:

    if mark < 40:
        continue

    print(f"Qualified marks: {mark}")
```

**Output:**

```text
Qualified marks: 45
Qualified marks: 78
Qualified marks: 90
Qualified marks: 55
Qualified marks: 88
```

**Concept:** Data filtering.

## Example 12 – Ignore Invalid Records

**Objective:** Ignore empty and whitespace-only records.

```python
records = [
    "Amaan",
    "",
    "Rahul",
    "   ",
    "Sneha",
    "",
    "Ali"
]

valid_records = []

for record in records:

    if not record.strip():
        continue

    valid_records.append(record.strip())

print(valid_records)
```

**Output:**

```text
['Amaan', 'Rahul', 'Sneha', 'Ali']
```

**Concept:** Record validation and filtering.

---

# 15. Twelve Solved Programming Problems

This section contains twelve solved problems based on the continue statement.

Each problem includes:

- Problem statement
- Logic
- Python code
- Sample input and output
- Explanation
- Time complexity
- Space complexity

## Problem 01 – Skip Multiples of Three

**Problem Statement:**

Write a Python program to print numbers from 1 to N. Skip all multiples of 3 using the `continue` statement.

**Logic:**

1. Take the value of N.
2. Iterate from 1 to N.
3. Check whether the current number is divisible by 3.
4. If it is divisible by 3, skip it.
5. Otherwise, print the number.

**Code:**

```python
n = int(input("Enter N: "))

for number in range(1, n + 1):

    if number % 3 == 0:
        continue

    print(number, end=" ")
```

**Sample Input:**

```text
Enter N: 12
```

**Sample Output:**

```text
1 2 4 5 7 8 10 11
```

**Explanation:**

Multiples of 3 are 3, 6, 9 and 12. These numbers are skipped.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 02 – Sum Positive Numbers

**Problem Statement:**

Write a program to calculate the sum of positive numbers from a list. Ignore zero and negative values using `continue`.

**Logic:**

1. Create a list of integers.
2. Initialize total to zero.
3. Traverse the list.
4. Skip values less than or equal to zero.
5. Add positive values to total.
6. Print the result.

**Code:**

```python
numbers = [10, -5, 20, 0, -3, 30]

total = 0

for number in numbers:

    if number <= 0:
        continue

    total += number

print("Sum:", total)
```

**Sample Output:**

```text
Sum: 60
```

**Explanation:**

Only 10, 20 and 30 are included.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 03 – Count Non-Zero Numbers

**Problem Statement:**

Count the number of non-zero elements in a list using `continue`.

**Logic:**

1. Create a list.
2. Initialize a counter to zero.
3. Traverse the list.
4. Skip an element if it equals zero.
5. Increase the counter for every non-zero value.
6. Display the counter.

**Code:**

```python
numbers = [10, 0, 20, 30, 0, 40, 0]

count = 0

for number in numbers:

    if number == 0:
        continue

    count += 1

print("Non-zero count:", count)
```

**Sample Output:**

```text
Non-zero count: 4
```

**Explanation:**

There are four non-zero values: 10, 20, 30 and 40.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 04 – Display Odd Numbers

**Problem Statement:**

Take a list of integers and display only odd numbers using `continue`.

**Logic:**

1. Create a list of numbers.
2. Traverse the list.
3. If a number is divisible by 2, skip it.
4. Print the remaining numbers.

**Code:**

```python
numbers = [10, 15, 22, 33, 40, 51, 64]

for number in numbers:

    if number % 2 == 0:
        continue

    print(number, end=" ")
```

**Sample Output:**

```text
15 33 51
```

**Explanation:**

Even numbers are skipped. Only odd numbers are displayed.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 05 – Remove Spaces from a String

**Problem Statement:**

Write a program to remove all spaces from a string using `continue`.

**Logic:**

1. Take a string from the user.
2. Create an empty result string.
3. Iterate through every character.
4. Skip the character if it is a space.
5. Add other characters to the result.
6. Print the result.

**Code:**

```python
text = input("Enter a sentence: ")

result = ""

for character in text:

    if character == " ":
        continue

    result += character

print("Original:", text)
print("Without spaces:", result)
```

**Sample Input:**

```text
Enter a sentence: Python is easy
```

**Sample Output:**

```text
Original: Python is easy
Without spaces: Pythoniseasy
```

**Explanation:**

Each space is skipped. All other characters are added to the result.

**Complexity:**

Let N be the number of characters in the input string.

- Time Complexity: O(N) under the usual character-processing model for this example.
- Space Complexity: O(N) for the resulting string.

Note: Repeated string concatenation can involve additional copying in Python. A list of characters followed by `"".join(...)` is preferable for larger strings.

## Problem 06 – Count Vowels

**Problem Statement:**

Write a program to count vowels in a string using `continue`.

**Logic:**

1. Read a string.
2. Store the vowels in a string.
3. Initialize a counter to zero.
4. Iterate through each character.
5. Skip characters that are not vowels.
6. Increase the counter for vowels.
7. Print the total.

**Code:**

```python
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for character in text:

    if character not in vowels:
        continue

    count += 1

print("Total vowels:", count)
```

**Sample Input:**

```text
Enter a string: Programming
```

**Sample Output:**

```text
Total vowels: 3
```

**Explanation:**

The vowels are o, a and i. Other characters are skipped.

**Complexity:**

Let N be the string length.

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1), because the vowel collection has a fixed size.

## Problem 07 – Average of Valid Marks

**Problem Statement:**

Calculate the average of valid student marks. A valid mark must be between 0 and 100, inclusive. Skip invalid marks using `continue`.

**Logic:**

1. Create a list of marks.
2. Initialize total and valid count to zero.
3. Traverse every mark.
4. Skip marks below 0 or above 100.
5. Add valid marks to total.
6. Increase the valid count.
7. Calculate the average if at least one valid mark exists.

**Code:**

```python
marks = [80, 90, -5, 70, 120, 60]

total = 0
valid_count = 0

for mark in marks:

    if mark < 0 or mark > 100:
        continue

    total += mark
    valid_count += 1

if valid_count > 0:
    average = total / valid_count
    print("Average:", average)
else:
    print("No valid marks.")
```

**Sample Output:**

```text
Average: 75.0
```

**Explanation:**

Valid marks are 80, 90, 70 and 60.

Their sum is 300 and their count is 4.

Average = 300 / 4 = 75.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 08 – Skip Multiples of a Divisor

**Problem Statement:**

Given a list and a positive divisor, display all numbers that are not divisible by the divisor.

**Logic:**

1. Create a list of numbers.
2. Take a positive divisor.
3. Iterate through the list.
4. If the remainder is zero, skip the number.
5. Otherwise, display it.

**Code:**

```python
numbers = [10, 12, 15, 20, 23, 25, 30]

divisor = int(input("Enter divisor: "))

if divisor <= 0:
    print("Divisor must be positive.")

else:
    for number in numbers:

        if number % divisor == 0:
            continue

        print(number, end=" ")
```

**Sample Input:**

```text
Enter divisor: 5
```

**Sample Output:**

```text
12 23
```

**Explanation:**

10, 15, 20, 25 and 30 are divisible by 5, so they are skipped.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 09 – Display Non-Zero Matrix Values

**Problem Statement:**

Write a program to display only non-zero values from a matrix using nested loops and `continue`.

**Logic:**

1. Create a matrix.
2. Traverse each row.
3. Traverse every value in the current row.
4. Skip values equal to zero.
5. Display the remaining values.

**Code:**

```python
matrix = [
    [1, 0, 3],
    [0, 5, 6],
    [7, 8, 0]
]

for row in matrix:

    for value in row:

        if value == 0:
            continue

        print(value, end=" ")
```

**Sample Output:**

```text
1 3 5 6 7 8
```

**Explanation:**

The zero values are skipped. All other matrix elements are displayed.

**Complexity:**

For a matrix with R rows and C columns:

- Time Complexity: O(R × C)
- Auxiliary Space Complexity: O(1)

## Problem 10 – Count Valid Scores

**Problem Statement:**

Count valid student scores. A score is valid if it lies between 0 and 100, inclusive.

**Logic:**

1. Create a list of scores.
2. Initialize valid and invalid counters.
3. Traverse the list.
4. If a score is invalid, increase invalid count and continue.
5. Otherwise, increase valid count.
6. Print both counts.

**Code:**

```python
scores = [85, 90, -10, 70, 110, 65, 50]

valid_count = 0
invalid_count = 0

for score in scores:

    if score < 0 or score > 100:
        invalid_count += 1
        continue

    valid_count += 1

print("Valid scores:", valid_count)
print("Invalid scores:", invalid_count)
```

**Sample Output:**

```text
Valid scores: 5
Invalid scores: 2
```

**Explanation:**

The values -10 and 110 are invalid. The remaining five values are valid.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

## Problem 11 – Filter Words by Length

**Problem Statement:**

Display words that contain at least a specified number of characters.

**Logic:**

1. Read words separated by spaces.
2. Take the minimum length.
3. Iterate through the words.
4. Skip any word shorter than the minimum length.
5. Print all matching words.

**Code:**

```python
words = input("Enter words: ").split()

minimum_length = int(input("Minimum length: "))

for word in words:

    if len(word) < minimum_length:
        continue

    print(word)
```

**Sample Input:**

```text
Enter words: cat apple banana hi orange
Minimum length: 4
```

**Sample Output:**

```text
apple
banana
orange
```

**Explanation:**

The words cat and hi are shorter than four characters, so they are skipped.

**Complexity:**

Let N be the number of words and L be the total number of characters processed.

- Time Complexity: O(L) for checking all word lengths.
- Auxiliary Space Complexity: O(1), excluding the input representation and output.

## Problem 12 – Process Valid Positive Numbers

**Problem Statement:**

Calculate the sum and average of positive numbers from a list. Ignore zero and negative values.

**Logic:**

1. Create a list.
2. Initialize total and count.
3. Traverse the list.
4. Skip zero and negative values.
5. Add positive values to total.
6. Increase the count.
7. Calculate the average if at least one positive number exists.

**Code:**

```python
numbers = [10, -5, 20, 0, 30, -2, 40]

total = 0
count = 0

for number in numbers:

    if number <= 0:
        continue

    total += number
    count += 1

if count == 0:
    print("No positive numbers.")

else:
    average = total / count

    print("Sum:", total)
    print("Count:", count)
    print("Average:", average)
```

**Sample Output:**

```text
Sum: 100
Count: 4
Average: 25.0
```

**Explanation:**

The positive values are 10, 20, 30 and 40.

Their sum is 100 and their average is 25.

**Complexity:**

- Time Complexity: O(N)
- Auxiliary Space Complexity: O(1)

---

# 16. Ten Unsolved Practice Questions

Try solving these questions independently using the `continue` statement.

Do not directly look for a solution before attempting the problem.

## Question 01 – Skip Multiples of Five

Write a program to print numbers from 1 to N while skipping all multiples of 5.

## Question 02 – Display Negative Numbers

Take a list of integers and display only negative numbers using `continue`.

## Question 03 – Count Consonants

Write a program to count consonants in a string by skipping vowels and spaces.

## Question 04 – Passing Marks

Take a list of student marks and display only marks greater than or equal to 40.

## Question 05 – Remove Digits

Write a program to remove all digits from a string using `continue`.

## Question 06 – Sum Numbers Not Divisible by Four

Take 10 numbers as input and calculate the sum of numbers that are not divisible by 4.

## Question 07 – Skip Special Symbols

Write a program to display all characters except special symbols from a string.

## Question 08 – Nested Loop Filtering

Create a nested loop program that skips column number 2 in every row.

## Question 09 – Filter Short Words

Take a list of words and skip words that contain fewer than three characters.

## Question 10 – Positive Even Numbers

Write a program that reads a fixed number of values and calculates the average of valid positive even numbers.

---

# 17. Common Mistakes

Understanding common mistakes helps prevent errors while writing programs.

## Mistake 01 – Using Continue Outside a Loop

Incorrect:

```python
if True:
    continue
```

This causes a SyntaxError because `continue` must be inside a loop.

Correct:

```python
for number in range(5):

    if number == 2:
        continue

    print(number)
```

## Mistake 02 – Forgetting to Update a while Loop Counter

Incorrect:

```python
number = 0

while number < 5:

    if number == 2:
        continue

    number += 1
```

The counter never changes when it reaches 2.

This creates an infinite loop.

Correct:

```python
number = 0

while number < 5:

    number += 1

    if number == 2:
        continue

    print(number)
```

## Mistake 03 – Confusing Continue with Break

Incorrect understanding:

- Thinking that `continue` stops the complete loop.

Correct understanding:

- `continue` skips only the current iteration.
- `break` terminates the nearest enclosing loop.

## Mistake 04 – Incorrect Condition

Incorrect:

```python
for number in range(1, 11):

    if number % 2 == 1:
        continue

    print(number)
```

This prints even numbers, not odd numbers.

Correct understanding:

The condition determines which values get skipped. Always check the condition carefully.

## Mistake 05 – Placing Continue After the Statement

```python
for number in range(1, 6):

    print(number)

    if number == 3:
        continue
```

This still prints 3 because the print statement executes before `continue`.

To skip printing 3:

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

## Mistake 06 – Incorrect Indentation

Incorrect:

```python
for number in range(1, 6):

    if number == 3:
        continue

        print(number)
```

The print statement is unreachable because it is placed after `continue` inside the same block.

Correct:

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

## Mistake 07 – Assuming Continue Skips the Outer Loop

Inside nested loops, `continue` affects only the nearest enclosing loop.

Do not assume it automatically skips the outer loop.

## Mistake 08 – Forgetting to Check Empty Data

When calculating averages, always check whether the valid-value count is zero before dividing.

---

# 18. Best Practices

Follow these practices when using `continue`:

1. Use `continue` when an iteration should be skipped.
2. Keep the condition easy to understand.
3. Use meaningful variable names.
4. Avoid unnecessary nested conditions.
5. Update `while` loop counters before a possible `continue` when required.
6. Validate input data before processing it.
7. Check for division by zero when calculating averages.
8. Use appropriate data structures.
9. Avoid excessive use of `continue` when a simpler condition would be clearer.
10. Add comments when the skip condition is not obvious.
11. Remember that nested-loop `continue` affects only the nearest loop.
12. Test normal, boundary and invalid inputs.

## Good Example

```python
numbers = [10, 0, -5, 20, 30]

for number in numbers:

    if number <= 0:
        continue

    print("Positive number:", number)
```

This code is clear because the skip condition is checked before the useful operation.

---

# 19. Debugging Continue Statement

Debugging helps identify where a program is not behaving as expected.

When working with `continue`, check:

- Whether the condition is correct.
- Whether the statement is in the correct indentation block.
- Whether statements after `continue` are being skipped as intended.
- Whether a `while` loop counter is updated.
- Whether a nested loop is being controlled correctly.
- Whether the loop terminates normally.

## Debugging Example

```python
for number in range(1, 6):

    print("Current value:", number)

    if number == 3:
        print("Skipping this iteration")
        continue

    print("Processing:", number)
```

**Output:**

```text
Current value: 1
Processing: 1
Current value: 2
Processing: 2
Current value: 3
Skipping this iteration
Current value: 4
Processing: 4
Current value: 5
Processing: 5
```

The debugging message shows when `continue` is executed.

---

# 20. Real-Life Applications

The `continue` statement is useful in many real-world programming situations.

## 20.1 Data Cleaning

A dataset may contain missing or empty values.

A program can skip those entries while processing the remaining data.

```python
names = ["Amaan", "", "Rahul", "Ali"]

for name in names:

    if not name.strip():
        continue

    print(name)
```

## 20.2 Student Result Processing

A program can skip invalid marks.

```python
marks = [80, 90, -5, 70, 120]

for mark in marks:

    if mark < 0 or mark > 100:
        continue

    print("Valid mark:", mark)
```

## 20.3 Log File Processing

While reading log entries, a program may ignore blank lines.

```python
logs = [
    "INFO: Started",
    "",
    "ERROR: Failed",
    "WARNING: Retry"
]

for log in logs:

    if not log.strip():
        continue

    print(log)
```

## 20.4 Filtering Product Records

An online store can skip unavailable products.

```python
products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 0},
    {"name": "Keyboard", "stock": 8}
]

for product in products:

    if product["stock"] == 0:
        continue

    print(product["name"])
```

## 20.5 Validating User Data

A program can skip records that do not satisfy basic validation rules.

```python
ages = [18, 25, -1, 35, 150]

for age in ages:

    if age < 0 or age > 120:
        continue

    print("Valid age:", age)
```

---

# 21. Connection with Data Structures and Algorithms

The `continue` statement is useful when implementing algorithms that process collections of data.

## 21.1 Array and List Traversal

When traversing an array or list, we may want to process only selected values.

Example:

```python
numbers = [5, 10, 15, 20, 25, 30]

for number in numbers:

    if number % 2 == 0:
        continue

    print(number)
```

This processes only odd values.

## 21.2 Linear Search

Linear search examines elements one by one.

`continue` can be used to ignore candidates that do not match a filtering condition.

```python
numbers = [10, -5, 20, 30, -2, 40]
target = 30

for number in numbers:

    if number < 0:
        continue

    if number == target:
        print("Found:", number)
```

The algorithm skips negative values and checks the remaining values.

## 21.3 Filtering Data

Filtering means selecting values that satisfy a specific condition.

Example:

```python
numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:

    if number < 20:
        continue

    print(number)
```

Only numbers greater than or equal to 20 are displayed.

## 21.4 Matrix Traversal

Nested loops can be used to traverse matrix elements.

```python
matrix = [
    [1, 0, 3],
    [4, 5, 0],
    [7, 8, 9]
]

for row in matrix:

    for value in row:

        if value == 0:
            continue

        print(value)
```

Zero values are ignored.

## 21.5 Algorithmic Importance

The `continue` statement does not automatically make an algorithm faster.

It changes the control flow.

The total time complexity still depends on how many elements the algorithm visits and what work it performs for each element.

---

# 22. Time and Space Complexity

Complexity analysis helps us understand how an algorithm performs when its input size increases.

## 22.1 Time Complexity

Consider:

```python
for number in range(1, n + 1):

    if number % 2 == 0:
        continue

    print(number)
```

The loop visits all N numbers.

Therefore:

**Time Complexity: O(N)**

Even though some iterations are skipped, the loop still checks every number.

## 22.2 Space Complexity

The program uses only a fixed number of variables.

It does not create another collection.

**Auxiliary Space Complexity: O(1)**

## 22.3 Common Complexity Examples

| Operation | Time Complexity |
|---|---|
| Skip a specific value while traversing N items | O(N) |
| Print only odd numbers from N values | O(N) |
| Count non-zero elements in a list | O(N) |
| Sum positive elements in a list | O(N) |
| Traverse an R × C matrix | O(R × C) |
| Process every character in a string | O(N) |

Remember that `continue` changes which operations execute, but it generally does not remove the cost of visiting each element.

---

# 23. Mini Project – Data Filtering System

## Project Objective

Create a simple data filtering program using the `continue` statement.

The program receives a list of values and processes only valid positive integers.

It should:

1. Accept a collection of integers.
2. Skip zero values.
3. Skip negative values.
4. Count the positive values.
5. Calculate their sum.
6. Calculate their average.
7. Display the valid values.

## Project Code

```python
"""
Mini Project: Data Filtering System

Concepts:
- Lists
- Loops
- Continue statement
- Conditional statements
- Sum and average
"""


def filter_positive_numbers(numbers: list[int]) -> list[int]:
    """Return only positive numbers."""
    valid_numbers = []

    for number in numbers:

        if number <= 0:
            continue

        valid_numbers.append(number)

    return valid_numbers


def calculate_statistics(numbers: list[int]) -> None:
    """Display statistics for positive numbers."""
    valid_numbers = filter_positive_numbers(numbers)

    if not valid_numbers:
        print("No valid positive values found.")
        return

    total = sum(valid_numbers)
    count = len(valid_numbers)
    average = total / count

    print("\nDATA FILTERING REPORT")
    print("-" * 35)

    print("Original data:", numbers)
    print("Valid data:", valid_numbers)
    print("Total valid values:", count)
    print("Sum:", total)
    print("Average:", average)


def main() -> None:
    """Run the data filtering project."""
    print("DATA FILTERING SYSTEM")

    raw_values = input(
        "Enter integers separated by spaces: "
    ).split()

    try:
        numbers = [int(value) for value in raw_values]
    except ValueError:
        print("Invalid input! Enter integers only.")
        return

    calculate_statistics(numbers)


if __name__ == "__main__":
    main()
```

## Sample Input

```text
Enter integers separated by spaces: 10 -5 20 0 30 -2 40
```

## Sample Output

```text
DATA FILTERING REPORT
-----------------------------------
Original data: [10, -5, 20, 0, 30, -2, 40]
Valid data: [10, 20, 30, 40]
Total valid values: 4
Sum: 100
Average: 25.0
```

## Project Concepts Used

- Functions
- Lists
- Type hints
- Exception handling
- For loops
- Conditional statements
- Continue statement
- Average calculation

## Possible Improvements

1. Allow decimal values.
2. Add minimum and maximum value filters.
3. Count skipped values.
4. Calculate the minimum and maximum valid values.
5. Export the results to a text file.

---

# 24. Fifty Python Viva Questions and Answers

## Basic Questions

**Q1. What is the continue statement in Python?**

The `continue` statement skips the remaining statements in the current loop iteration and moves to the next iteration.

**Q2. Why is continue used?**

It is used to ignore selected iterations based on a condition.

**Q3. Is continue a keyword in Python?**

Yes. `continue` is a reserved Python keyword.

**Q4. Can continue be used with a for loop?**

Yes. It can be used inside a `for` loop.

**Q5. Can continue be used with a while loop?**

Yes. It can be used inside a `while` loop.

**Q6. Does continue terminate a loop?**

No. It skips the current iteration and allows the loop to continue.

**Q7. What happens after continue executes?**

Python proceeds to the next iteration of the nearest enclosing loop.

**Q8. Can continue be used outside a loop?**

No. Using it outside a loop causes a SyntaxError.

**Q9. Is continue a replacement for break?**

No. They perform different operations.

**Q10. What is the main purpose of continue?**

To skip unwanted iterations without stopping the complete loop.

## Conceptual Questions

**Q11. What is the difference between break and continue?**

`break` terminates the nearest enclosing loop, whereas `continue` skips only the current iteration.

**Q12. What is the difference between continue and pass?**

`continue` changes loop execution by skipping the rest of the current iteration. `pass` does nothing.

**Q13. Can continue be used inside an if statement?**

Yes. It is commonly placed inside an `if` block.

**Q14. Can continue be used inside nested loops?**

Yes. It affects only the nearest enclosing loop.

**Q15. Does continue skip the next iteration?**

No. It skips the remaining statements in the current iteration and proceeds to the next one.

**Q16. Does continue work with lists?**

Yes. It can skip selected list elements during iteration.

**Q17. Can continue be used with strings?**

Yes. It can skip selected characters during string iteration.

**Q18. Can continue be used for filtering data?**

Yes. It is useful for skipping unwanted or invalid values.

**Q19. Does continue modify the original list?**

No. It does not change the list by itself.

**Q20. What is the most common use of continue?**

Skipping values that do not satisfy a required condition.

## Programming Questions

**Q21. How can you print only odd numbers using continue?**

Skip numbers for which `number % 2 == 0`.

**Q22. How can you print only even numbers using continue?**

Skip numbers for which `number % 2 != 0`.

**Q23. How can you skip multiples of 5?**

Use `if number % 5 == 0:` followed by `continue`.

**Q24. How can you skip negative numbers?**

Use `if number < 0:` followed by `continue`.

**Q25. How can you skip empty strings?**

Use `if not text.strip():` followed by `continue`.

**Q26. How can you remove spaces while processing a string?**

Skip characters equal to a space.

**Q27. How can you skip zeros from a list?**

Use `if number == 0:` followed by `continue`.

**Q28. How can continue help calculate a positive-number sum?**

Skip zero and negative values and add only positive values to the total.

**Q29. How can you count valid marks?**

Skip marks outside the 0 to 100 range and count the remaining values.

**Q30. Why should we use input validation?**

It prevents invalid data from being processed as though it were valid.

## Advanced Questions

**Q31. What happens if continue is placed before a print statement?**

The print statement is skipped when the continue condition is true.

**Q32. What happens if print is placed before continue?**

The print statement executes before the iteration is skipped.

**Q33. Can continue cause an infinite loop?**

Yes. In a `while` loop, it can cause an infinite loop if the loop condition never changes on a skipped iteration.

**Q34. How can an infinite loop caused by continue be avoided?**

Ensure the counter or relevant loop state is updated before a possible continue, or otherwise guarantee progress.

**Q35. Does continue skip the loop's else clause?**

No. If the loop finishes normally, its `else` clause can still execute.

**Q36. When does a loop's else clause not execute?**

When the loop is terminated by `break`.

**Q37. What does continue do in a nested loop?**

It skips the current iteration of the nearest enclosing loop.

**Q38. Can continue be used with a while True loop?**

Yes. It can be used, but the loop must have a suitable termination condition or exit mechanism.

**Q39. Does continue reduce time complexity?**

Not automatically. The loop may still visit all N elements.

**Q40. What is the complexity of traversing a list of N elements with continue?**

Usually O(N), because each element is visited.

## Practical and DSA Questions

**Q41. How is continue useful in data cleaning?**

It can ignore empty or invalid records before processing.

**Q42. How is continue useful in student result processing?**

It can skip invalid marks and process only valid results.

**Q43. Can continue be used during matrix traversal?**

Yes. It can skip selected matrix elements inside nested loops.

**Q44. What is the difference between skipping a value and removing it?**

Skipping a value leaves the original collection unchanged. Removing a value modifies a collection or creates a filtered collection.

**Q45. Is continue useful in linear search?**

Yes. It can skip candidates that do not meet a preliminary condition.

**Q46. What is the role of modulus in continue examples?**

The modulus operator helps identify divisibility and filter values.

**Q47. What happens if the continue condition is always true?**

Every iteration skips the statements after `continue`. The loop may still continue until its normal termination condition is reached.

**Q48. Can multiple continue statements appear in one loop?**

Yes. A loop can contain multiple conditional continue statements.

**Q49. Why is indentation important with continue?**

Indentation determines which statements belong to the condition and which statements execute after the continue check.

**Q50. What is the most important rule to remember about continue?**

It skips the remaining statements in the current iteration and moves to the next iteration of the nearest enclosing loop.

---

# 25. Important Terminology

| Term | Meaning |
|---|---|
| Continue | Skips the current iteration |
| Iteration | One execution of a loop |
| Loop | A structure used to repeat statements |
| Condition | An expression that evaluates to True or False |
| Filtering | Selecting values that satisfy a condition |
| Validation | Checking whether input data is acceptable |
| Nested Loop | A loop inside another loop |
| Modulus | Operator that returns the remainder |
| Infinite Loop | A loop that does not terminate normally |
| Counter | A variable used to track a count |
| Accumulator | A variable used to collect a running result |
| Sequence | An ordered collection of values |
| Traversal | Visiting elements of a collection |
| Time Complexity | Measure of how running time grows with input size |
| Space Complexity | Measure of how memory usage grows with input size |

---

# 26. Quick Revision Notes

## Important Syntax

```python
for value in sequence:

    if condition:
        continue

    statement
```

## Important Rules

1. Continue is used inside loops.
2. It skips the current iteration.
3. It does not terminate the complete loop.
4. It works with for and while loops.
5. It skips statements placed after it in the same iteration.
6. In nested loops, it affects only the nearest enclosing loop.
7. A while loop must still make progress.
8. Continue does not modify the original collection.
9. Continue does not prevent a normally completed loop's else clause.
10. Continue and break are different.

## Important Code Patterns

**Skip even numbers:**

```python
if number % 2 == 0:
    continue
```

**Skip odd numbers:**

```python
if number % 2 != 0:
    continue
```

**Skip negative numbers:**

```python
if number < 0:
    continue
```

**Skip zeros:**

```python
if number == 0:
    continue
```

**Skip empty strings:**

```python
if not text.strip():
    continue
```

**Skip multiples of a number:**

```python
if number % divisor == 0:
    continue
```

## One-Line Difference

- `break` – Stop the nearest loop.
- `continue` – Skip the current iteration.
- `pass` – Do nothing.

---

# 27. Learning Checklist

Mark each item after understanding and practising it.

- [ ] Understand the purpose of continue.
- [ ] Understand the syntax of continue.
- [ ] Use continue inside a for loop.
- [ ] Use continue inside a while loop.
- [ ] Skip a specific number.
- [ ] Print only odd numbers.
- [ ] Print only even numbers.
- [ ] Skip selected list elements.
- [ ] Skip characters in strings.
- [ ] Ignore empty strings.
- [ ] Skip zero and negative numbers.
- [ ] Calculate sums using continue.
- [ ] Calculate averages using continue.
- [ ] Filter valid marks.
- [ ] Skip multiples using modulus.
- [ ] Use continue inside nested loops.
- [ ] Understand continue with loop else.
- [ ] Differentiate break, continue and pass.
- [ ] Avoid infinite while loops.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the data filtering mini project.
- [ ] Prepare for the viva questions.

---

# 28. How to Run the Python File

## Step 1 – Open the Repository

Open your `DSA-Python` project in VS Code.

## Step 2 – Open the Topic Folder

Navigate to:

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 07-Continue-Statement/
```

## Step 3 – Open the Python File

Open:

```text
07_continue_statement.py
```

## Step 4 – Open Terminal

In VS Code, open the integrated terminal.

## Step 5 – Run the File

From the repository root, execute:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/07-Continue-Statement/07_continue_statement.py
```

## Step 6 – Select a Menu Option

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Select an option to explore the topic.

---

# 29. Repository Structure

The topic should be stored in the following location:

```text
DSA-Python/
└── PYTHON/
    └── Python-Fundamentals/
        └── 01-Loops/
            └── 07-Continue-Statement/
                ├── README.md
                └── 07_continue_statement.py
```

## File Description

| File | Purpose |
|---|---|
| README.md | Detailed theory, examples, solved questions and revision |
| 07_continue_statement.py | Executable Python examples and interactive practice menu |

## Git Commands

After adding both files, use these commands from the repository root:

```powershell
git status
```

```powershell
git add "PYTHON/Python-Fundamentals/01-Loops/07-Continue-Statement/"
```

```powershell
git commit -m "Add continue statement lesson"
```

```powershell
git push origin main
```

These commands stage, commit and push the topic to your GitHub repository when executed successfully.

---

# 30. Final Summary

The `continue` statement is an important loop control statement in Python.

It allows a programmer to skip unwanted iterations without terminating the complete loop.

It is particularly helpful when working with:

- Number filtering
- List processing
- String manipulation
- Data validation
- Student result processing
- Matrix traversal
- Data cleaning
- DSA problems

The most important difference to remember is:

**break:** Terminates the nearest enclosing loop.

**continue:** Skips the remaining statements in the current iteration.

**pass:** Does nothing.

Practise all twelve solved problems, attempt the ten unsolved questions and complete the mini project before moving to the next topic.

**Topic 07 – Continue Statement: Completed Study Notes.**