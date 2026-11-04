# While Loop in Python

## 1. Introduction

The `while` loop is one of the fundamental looping statements in Python.

It is used to execute a block of code repeatedly as long as a specified condition evaluates to `True`.

Unlike a `for` loop, which commonly processes the elements of an iterable, a `while` loop is generally used when the number of repetitions depends on a condition.

For example, suppose we want to print numbers from 1 to 5.

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

The loop starts with the value 1.

Python checks whether `number <= 5`.

If the condition is true, the loop body executes.

The current number is printed and then increased by one.

This process continues until the condition becomes false.

When the number becomes 6, the condition is false and the loop terminates.

The `while` loop is useful for:

- Repeated user input.
- Input validation.
- Number-based calculations.
- Counting operations.
- Menu-driven programs.
- Sentinel-controlled repetition.
- Searching operations.
- Processing data until a condition is satisfied.
- Implementing algorithms.
- Data Structures and Algorithms.

Understanding the `while` loop is essential for learning problem-solving and programming logic.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

1. Define a `while` loop in Python.
2. Understand why a `while` loop is used.
3. Understand condition-controlled repetition.
4. Understand initialization.
5. Understand loop conditions.
6. Understand variable updates.
7. Write a basic `while` loop.
8. Print numbers in ascending order.
9. Print numbers in descending order.
10. Generate even-number sequences.
11. Generate odd-number sequences.
12. Calculate sums using a `while` loop.
13. Generate multiplication tables.
14. Iterate through a string using an index.
15. Iterate through a list using an index.
16. Count the digits of an integer.
17. Reverse the digits of a number.
18. Calculate the sum of digits.
19. Calculate factorial using a `while` loop.
20. Check whether a number is a palindrome.
21. Understand infinite loops.
22. Prevent unintended infinite loops.
23. Understand sentinel-controlled loops.
24. Use loops for input validation.
25. Understand the purpose of `break`.
26. Understand loop termination.
27. Solve number-based programming problems.
28. Analyze the complexity of a `while` loop.
29. Apply `while` loops to DSA problems.

---

## 3. What Is a While Loop?

A `while` loop is a control-flow statement that repeatedly executes a block of code while a Boolean condition remains true.

### Basic Example

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

The variable `number` is initialized with 1.

Python evaluates the condition:

```python
number <= 5
```

The condition is true, so the loop body executes.

The value is printed.

The update statement increases the variable by one.

Python evaluates the condition again.

The process continues until the condition becomes false.

### Important Points

- The `while` keyword begins the loop.
- The condition determines whether the loop continues.
- The loop body executes while the condition is true.
- The condition is checked before every iteration.
- Initialization generally happens before the loop.
- The loop variable usually changes inside the loop.
- The loop terminates when the condition becomes false or a control statement terminates it.

---

## 4. Why Do We Use While Loops?

A `while` loop is useful when a program needs to repeat an operation until a condition changes.

Consider a program that asks the user to enter a positive number.

The program should continue asking until the user enters a valid value.

This behavior can be implemented using a `while` loop.

```python
number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid number.")
    number = int(input("Enter a positive number: "))

print("Valid number:", number)
```

The loop repeats only while the entered number is zero or negative.

### Advantages of While Loops

1. Useful for condition-controlled repetition.
2. Supports repeated user input.
3. Helps implement validation.
4. Useful for number-based problems.
5. Supports sentinel-controlled programs.
6. Makes menu-driven applications possible.
7. Helps process unknown numbers of inputs.
8. Supports repeated calculations.
9. Helps implement search operations.
10. Makes condition-based algorithms easier to understand.

### Common Applications

- Login attempts.
- Password validation.
- Menu-driven applications.
- ATM applications.
- Repeated calculations.
- Number reversal.
- Digit counting.
- Game loops.
- Interactive programs.
- Data processing until a specific condition is met.

---

## 5. Syntax of a While Loop

The general syntax is:

```python
while condition:
    statement
    update
```

### Components

| Component | Explanation |
|---|---|
| `while` | Python keyword used to start the loop |
| `condition` | Boolean expression controlling repetition |
| `:` | Marks the beginning of the loop body |
| Indented statements | Code executed while the condition is true |
| `update` | Changes the control variable when required |

### Example

```python
count = 1

while count <= 3:
    print("Python")
    count += 1
```

Output:

```text
Python
Python
Python
```

### Explanation

The initial value of `count` is one.

The condition is checked before executing the loop body.

The word `Python` is printed.

The counter increases by one.

The same process continues until the condition becomes false.

---

## 6. Initialization, Condition, and Update

Three important concepts help explain the working of a basic `while` loop.

### 6.1 Initialization

Initialization means assigning the starting value to a variable before the loop begins.

Example:

```python
number = 1
```

The variable begins with the value 1.

### 6.2 Condition

A condition is a Boolean expression that decides whether the loop body should execute.

Example:

```python
while number <= 5:
```

Python evaluates the condition before executing the body.

### 6.3 Update

An update changes the value of the control variable.

Example:

```python
number += 1
```

The variable increases by one.

### Complete Example

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### General Flow

```text
Initialization
      |
      v
Check condition
      |
      v
Is condition True?
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

### Importance

If a condition-controlled loop does not update the relevant variable, it may never terminate.

Correct initialization, condition checking, and updating are essential for writing correct `while` loops.

---

## 7. How a While Loop Executes

Consider:

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

The loop executes as follows:

| Iteration | Value before printing | Condition | Value after update |
|---|---:|---|---:|
| 1 | 1 | True | 2 |
| 2 | 2 | True | 3 |
| 3 | 3 | True | 4 |
| Final check | 4 | False | Loop terminates |

Output:

```text
1
2
3
```

### Important Concept

The condition is checked before each iteration.

When the condition is false, the loop body is skipped.

A `while` loop can also execute zero times when its condition is initially false.

Example:

```python
number = 10

while number < 5:
    print(number)
```

Output:

```text
```

Nothing is printed because the condition is false at the beginning.

---

## 8. Printing Numbers in Ascending Order

A `while` loop can print numbers in increasing order by using an increment operation.

### Example

```python
number = 1

while number <= 5:
    print(number, end=" ")
    number += 1
```

Output:

```text
1 2 3 4 5
```

### Explanation

The loop starts from one.

The number is printed.

The `+= 1` operation increases the value.

The loop stops after reaching the point where the condition becomes false.

### Print Numbers from 1 to 10

```python
number = 1

while number <= 10:
    print(number, end=" ")
    number += 1
```

Output:

```text
1 2 3 4 5 6 7 8 9 10
```

### General Pattern

```python
number = start

while number <= end:
    print(number)
    number += 1
```

This pattern generates an ascending sequence with a step of one.

---

## 9. Printing Numbers in Descending Order

A descending sequence can be generated by decreasing the loop-control variable.

### Example

```python
number = 5

while number >= 1:
    print(number, end=" ")
    number -= 1
```

Output:

```text
5 4 3 2 1
```

### Explanation

The initial value is five.

The condition checks whether the number is greater than or equal to one.

The value is printed.

The `-= 1` operation decreases it by one.

### General Pattern

```python
number = start

while number >= end:
    print(number)
    number -= 1
```

### Countdown Example

```python
countdown = 10

while countdown >= 1:
    print(countdown)
    countdown -= 1

print("Countdown completed!")
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
Countdown completed!
```

---

## 10. Printing Even Numbers Using a While Loop

An even number is divisible by two.

The remainder after division by two is zero.

### Example

```python
number = 2

while number <= 10:
    print(number, end=" ")
    number += 2
```

Output:

```text
2 4 6 8 10
```

### Explanation

The loop starts at two.

The step is two.

Therefore, each generated value is even.

### Using a Condition

```python
number = 1

while number <= 10:
    if number % 2 == 0:
        print(number, end=" ")

    number += 1
```

Output:

```text
2 4 6 8 10
```

### Difference

The first approach directly generates even numbers by increasing the variable by two.

The second approach checks every number and prints only even numbers.

---

## 11. Printing Odd Numbers Using a While Loop

An odd number is not divisible by two.

Its remainder after division by two is one for positive odd integers.

### Example

```python
number = 1

while number <= 10:
    print(number, end=" ")
    number += 2
```

Output:

```text
1 3 5 7 9
```

### Using a Condition

```python
number = 1

while number <= 10:
    if number % 2 != 0:
        print(number, end=" ")

    number += 1
```

Output:

```text
1 3 5 7 9
```

### Important Point

The starting value and update determine the sequence.

Starting at one and increasing by two generates positive odd numbers.

---

## 12. Sum of Numbers Using a While Loop

An accumulator is a variable used to collect a running result.

A `while` loop can use an accumulator to calculate a sum.

### Example

Calculate the sum from one to five.

```python
number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Sum:", total)
```

Output:

```text
Sum: 15
```

### Explanation

The accumulator starts at zero.

Every number is added to `total`.

### Calculation

```text
total = 0

total = 0 + 1
total = 1 + 2
total = 3 + 3
total = 6 + 4
total = 10 + 5

Final total = 15
```

### General Pattern

```python
number = 1
total = 0

while number <= n:
    total += number
    number += 1
```

---

## 13. Multiplication Table Using a While Loop

A `while` loop can generate a multiplication table by changing the multiplier.

### Example

```python
number = 5
multiplier = 1

while multiplier <= 10:
    print(f"{number} x {multiplier} = {number * multiplier}")
    multiplier += 1
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

### Explanation

The multiplier starts at one.

The multiplication is performed.

The multiplier increases by one.

The loop continues until the multiplier becomes greater than ten.

### User-Input Version

```python
number = int(input("Enter a number: "))

multiplier = 1

while multiplier <= 10:
    print(
        f"{number} x {multiplier} = "
        f"{number * multiplier}"
    )

    multiplier += 1
```

This version accepts a number from the user.

---

## 14. Iterating Through a String Using a While Loop

A string is a sequence of characters.

A `while` loop can access each character using its index.

### Example

```python
text = "PYTHON"

index = 0

while index < len(text):
    print(text[index])
    index += 1
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

### Explanation

The index starts at zero.

Python accesses the character at the current position.

The index increases by one.

The process continues until the index reaches the string length.

### Important Functions

`len(text)` returns the number of characters in the string.

`text[index]` accesses the character at the specified index.

### Print Characters on One Line

```python
text = "PYTHON"
index = 0

while index < len(text):
    print(text[index], end=" ")
    index += 1
```

Output:

```text
P Y T H O N
```

---

## 15. Iterating Through a List Using a While Loop

A list is an ordered collection of elements.

A `while` loop can process list elements through their indexes.

### Example

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1
```

Output:

```text
Apple
Banana
Mango
Orange
```

### Explanation

The list contains four elements.

Their indexes are:

| Index | Element |
|---|---|
| 0 | Apple |
| 1 | Banana |
| 2 | Mango |
| 3 | Orange |

The loop starts at index zero.

It accesses one element during each iteration.

The index increases until the end of the list is reached.

### Calculate Sum of List Elements

```python
numbers = [10, 20, 30, 40]

index = 0
total = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print("Sum:", total)
```

Output:

```text
Sum: 100
```

---

## 16. Counting Digits Using a While Loop

A `while` loop can count digits by repeatedly removing the last digit of an integer.

The integer division operator `//` is used to remove the last digit from a non-negative integer.

### Example

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

### Explanation

The original number is 12345.

Integer division by ten removes one digit from the right side.

This operation is repeated until the remaining value becomes zero.

A counter records how many digits were removed.

### Handling Zero

Zero contains one digit.

Therefore, it requires special handling.

```python
number = 0

if number == 0:
    digit_count = 1
```

### Handling Negative Integers

Use `abs()` to obtain the non-negative magnitude before counting digits.

```python
number = -12345

temporary = abs(number)
digit_count = 0

while temporary > 0:
    temporary //= 10
    digit_count += 1

print(digit_count)
```

Output:

```text
5
```

---

## 17. Reversing a Number Using a While Loop

A number can be reversed by extracting its digits from right to left.

Two operators are especially useful:

- `%` extracts the last digit.
- `//` removes the last digit.

### Example

```python
number = 1234

temporary = number
reversed_number = 0

while temporary > 0:
    digit = temporary % 10

    reversed_number = (
        reversed_number * 10 + digit
    )

    temporary //= 10

print("Reversed number:", reversed_number)
```

Output:

```text
Reversed number: 4321
```

### Important Operations

**Extracting the last digit:**

```python
digit = temporary % 10
```

**Appending the digit:**

```python
reversed_number = reversed_number * 10 + digit
```

**Removing the last digit:**

```python
temporary //= 10
```

### Important Point

When the reversed result is stored as an integer, leading zeroes are not preserved.

For example, reversing the integer 120 produces the integer 21.

---

## 18. Infinite While Loops

An infinite loop is a loop that does not terminate normally.

It can occur when the condition always remains true.

### Example

```python
while True:
    print("Python")
```

This loop continues indefinitely unless interrupted or terminated through an appropriate control statement.

### Another Example

```python
number = 1

while number <= 5:
    print(number)
```

The value of `number` never changes.

The condition remains true.

### Correct Version

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Common Reasons for Infinite Loops

1. Forgetting to update the loop variable.
2. Updating the variable in the wrong direction.
3. Using an incorrect condition.
4. Using a condition that cannot become false.
5. Forgetting a termination condition.
6. Updating a different variable instead of the control variable.

### How to Prevent Infinite Loops

- Check the initial value.
- Check the condition carefully.
- Make sure the variable is updated.
- Verify the update direction.
- Test with small numbers.
- Include a valid exit condition where necessary.

---

## 19. Sentinel-Controlled While Loops

A sentinel is a special value used to indicate that input or processing should stop.

A sentinel-controlled loop continues until the sentinel value is received.

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

The value zero acts as the sentinel.

The loop stops when the user enters zero.

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

### Important Concepts

- Sentinel value: Special value used to terminate repetition.
- `while True`: Creates a loop with an always-true condition.
- `break`: Terminates the nearest enclosing loop.

### Applications

- Repeated numeric input.
- Menu-driven programs.
- Data entry.
- Interactive calculations.
- Processing values until an end marker is reached.

---

## 20. Input Validation Using a While Loop

Input validation checks whether user-provided data satisfies the program's requirements.

A `while` loop can repeatedly request input until valid data is supplied.

### Example: Positive Number Validation

```python
number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid input.")

    number = int(
        input("Enter a positive number: ")
    )

print("Valid number:", number)
```

### Sample Run

```text
Enter a positive number: -5
Invalid input.
Enter a positive number: 0
Invalid input.
Enter a positive number: 8
Valid number: 8
```

### Example: Fixed Range Validation

```python
marks = int(input("Enter marks between 0 and 100: "))

while marks < 0 or marks > 100:
    print("Invalid marks.")

    marks = int(
        input("Enter marks between 0 and 100: ")
    )

print("Accepted marks:", marks)
```

### Why Is Input Validation Important?

It helps:

- Prevent invalid values.
- Improve program reliability.
- Reduce incorrect calculations.
- Enforce business rules.
- Improve user experience.

### Handling Non-Numeric Input

A condition-controlled loop alone does not prevent `ValueError` when an invalid string is converted to an integer.

A `try-except` block can handle that situation.

```python
while True:
    try:
        number = int(input("Enter a positive number: "))

        if number > 0:
            print("Valid number:", number)
            break

        print("Number must be positive.")

    except ValueError:
        print("Please enter a valid integer.")
```

This example continues until the user enters a valid positive integer.

---

## 21. Difference Between For Loop and While Loop

Python provides two primary loop statements.

Both repeat code, but their common usage differs.

| Feature | For Loop | While Loop |
|---|---|---|
| Basic purpose | Process an iterable | Repeat while a condition is true |
| Common use | Iterating through collections | Condition-controlled repetition |
| Number of iterations | Often determined by iterable length | Determined by condition and updates |
| Initialization | Often handled through the iterable | Usually performed before the loop |
| Condition checking | Iteration continues while elements are available | Boolean condition is checked before each iteration |
| Update | Next iterable item is selected | Usually performed manually |
| Infinite loop risk | Less common in normal iterable processing | More common if the condition never changes |
| Common example | List traversal | Repeated user input |
| Typical use | Processing sequences | Validation and sentinel loops |

### For Loop Example

```python
for number in range(1, 6):
    print(number)
```

### While Loop Example

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Both programs print the same sequence.

Choose the loop structure based on the problem requirements.

---

## 22. Twelve Topic Examples

These examples correspond to the twelve examples in `04_while_loop.py`.

### Example 1: Basic While Loop

**Objective:** Print numbers from one to five.

```python
number = 1

while number <= 5:
    print(number, end=" ")
    number += 1
```

Output:

```text
1 2 3 4 5
```

Explanation:

The variable begins at one.

The loop prints the number and increases it after every iteration.

### Example 2: Countdown Using a While Loop

**Objective:** Print numbers from five to one.

```python
number = 5

while number >= 1:
    print(number, end=" ")
    number -= 1
```

Output:

```text
5 4 3 2 1
```

Explanation:

The loop decreases the value after every iteration.

### Example 3: Print Even Numbers

**Objective:** Print even numbers from two to ten.

```python
number = 2

while number <= 10:
    print(number, end=" ")
    number += 2
```

Output:

```text
2 4 6 8 10
```

Explanation:

The step is two, so every generated value is even.

### Example 4: Print Odd Numbers

**Objective:** Print odd numbers from one to nine.

```python
number = 1

while number <= 9:
    print(number, end=" ")
    number += 2
```

Output:

```text
1 3 5 7 9
```

Explanation:

The starting value is odd and the step is two.

### Example 5: Sum of Natural Numbers

**Objective:** Find the sum of numbers from one to five.

```python
number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Sum:", total)
```

Output:

```text
Sum: 15
```

Explanation:

Every natural number is added to the accumulator.

### Example 6: Multiplication Table

**Objective:** Display the multiplication table of five.

```python
number = 5
multiplier = 1

while multiplier <= 10:
    print(
        f"{number} x {multiplier} = "
        f"{number * multiplier}"
    )

    multiplier += 1
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

The multiplier increases from one to ten.

### Example 7: Iterate Through a String

**Objective:** Display each character of a string using indexing.

```python
text = "PYTHON"
index = 0

while index < len(text):
    print(text[index], end=" ")
    index += 1
```

Output:

```text
P Y T H O N
```

Explanation:

The index accesses each character.

### Example 8: Iterate Through a List

**Objective:** Display every element of a list.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1
```

Output:

```text
Apple
Banana
Mango
Orange
```

Explanation:

The loop accesses list elements using their indexes.

### Example 9: Count Digits in a Number

**Objective:** Count the digits in 12345.

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

Integer division removes one digit during each iteration.

### Example 10: Reverse a Number

**Objective:** Reverse the integer 1234.

```python
number = 1234
temporary = number
reversed_number = 0

while temporary > 0:
    digit = temporary % 10

    reversed_number = (
        reversed_number * 10 + digit
    )

    temporary //= 10

print("Original number:", number)
print("Reversed number:", reversed_number)
```

Output:

```text
Original number: 1234
Reversed number: 4321
```

Explanation:

The last digit is extracted and appended to the reversed number.

### Example 11: Sum Until the User Enters Zero

**Objective:** Stop the loop when the sentinel value zero is reached.

```python
values = [10, 20, 30, 0]

index = 0
total = 0

while index < len(values):
    value = values[index]

    if value == 0:
        break

    total += value
    index += 1

print("Values:", values)
print("Sum before zero:", total)
```

Output:

```text
Values: [10, 20, 30, 0]
Sum before zero: 60
```

Explanation:

The zero terminates the loop.

The preceding values are added.

### Example 12: Input Validation

**Objective:** Continue checking values until a positive number is found.

```python
sample_values = [-5, 0, 8]
index = 0

while True:
    value = sample_values[index]
    print("Checking:", value)

    if value > 0:
        print("Valid positive number:", value)
        break

    print("Invalid value. Try again.")
    index += 1
```

Output:

```text
Checking: -5
Invalid value. Try again.
Checking: 0
Invalid value. Try again.
Checking: 8
Valid positive number: 8
```

Explanation:

The loop continues until a positive value is found.

This example uses a predefined sequence to demonstrate the control flow. A real input-validation program would obtain each value from the user.

---

## 23. Twelve Solved Programming Problems

### Problem 1: Print Numbers from 1 to N

**Problem Statement:**

Write a Python program to accept a positive integer N and print all numbers from one to N using a `while` loop.

**Logic:**

1. Read N.
2. Initialize the counter with one.
3. Check whether the counter is less than or equal to N.
4. Print the counter.
5. Increase the counter.
6. Repeat until the condition becomes false.

**Code:**

```python
n = int(input("Enter the value of N: "))

number = 1

while number <= n:
    print(number, end=" ")
    number += 1

print()
```

**Sample Input:**

```text
Enter the value of N: 5
```

**Sample Output:**

```text
1 2 3 4 5
```

**Explanation:**

The counter starts at one and increases until it exceeds N.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 2: Countdown

**Problem Statement:**

Accept a positive integer and print all numbers from N down to one.

**Logic:**

1. Read the starting value.
2. Check whether it is at least one.
3. Print the current value.
4. Decrease it by one.
5. Repeat until it reaches zero.

**Code:**

```python
number = int(input("Enter the starting number: "))

while number >= 1:
    print(number, end=" ")
    number -= 1

print()
```

**Sample Input:**

```text
Enter the starting number: 5
```

**Sample Output:**

```text
5 4 3 2 1
```

**Explanation:**

The loop decreases its control variable after every iteration.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 3: Sum of Natural Numbers

**Problem Statement:**

Calculate the sum of the first N natural numbers using a `while` loop.

**Logic:**

1. Read N.
2. Initialize `number` with one.
3. Initialize `total` with zero.
4. Add the current number to total.
5. Increase the number.
6. Stop when the number exceeds N.

**Code:**

```python
n = int(input("Enter the value of N: "))

number = 1
total = 0

while number <= n:
    total += number
    number += 1

print("Sum of natural numbers:", total)
```

**Sample Input:**

```text
Enter the value of N: 5
```

**Sample Output:**

```text
Sum of natural numbers: 15
```

**Explanation:**

The loop adds all values from one through five.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 4: Sum of Even Numbers

**Problem Statement:**

Calculate the sum of even numbers from one to N.

**Logic:**

1. Read N.
2. Start the number at two.
3. Initialize the total with zero.
4. Add the current even number.
5. Increase the number by two.
6. Continue while the number does not exceed N.

**Code:**

```python
n = int(input("Enter the value of N: "))

number = 2
total = 0

while number <= n:
    total += number
    number += 2

print("Sum of even numbers:", total)
```

**Sample Input:**

```text
Enter the value of N: 10
```

**Sample Output:**

```text
Sum of even numbers: 30
```

**Explanation:**

The program adds:

```text
2 + 4 + 6 + 8 + 10 = 30
```

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 5: Multiplication Table

**Problem Statement:**

Accept a number and display its multiplication table from one to ten.

**Logic:**

1. Read a number.
2. Initialize multiplier with one.
3. Multiply the number by the current multiplier.
4. Display the result.
5. Increase the multiplier.
6. Repeat until ten.

**Code:**

```python
number = int(input("Enter a number: "))

multiplier = 1

while multiplier <= 10:
    result = number * multiplier

    print(
        f"{number} x {multiplier} = {result}"
    )

    multiplier += 1
```

**Sample Input:**

```text
Enter a number: 7
```

**Sample Output:**

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

The multiplier increases from one through ten.

**Complexity:**

- Time: O(1), because ten iterations are always performed.
- Auxiliary space: O(1).

### Problem 6: Factorial of a Number

**Problem Statement:**

Calculate the factorial of a non-negative integer using a `while` loop.

Mathematical definition:

```text
N! = N × (N - 1) × ... × 2 × 1

0! = 1
```

**Logic:**

1. Read a non-negative integer.
2. Initialize factorial with one.
3. Initialize the current value with one.
4. Multiply factorial by the current value.
5. Increase the current value.
6. Repeat until the current value exceeds N.

**Code:**

```python
number = int(input("Enter a non-negative integer: "))

factorial = 1
current = 1

while current <= number:
    factorial *= current
    current += 1

print("Factorial:", factorial)
```

**Sample Input:**

```text
Enter a non-negative integer: 5
```

**Sample Output:**

```text
Factorial: 120
```

**Explanation:**

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

When the input is zero, the condition is initially false and the factorial remains one.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1), excluding the storage required for the growing integer result.

### Problem 7: Count Digits

**Problem Statement:**

Accept an integer and count its digits.

The program should correctly handle zero and negative numbers.

**Logic:**

1. Read an integer.
2. Use `abs()` to obtain its magnitude.
3. If the value is zero, assign a digit count of one.
4. Otherwise, repeatedly divide by ten.
5. Increase the counter after each division.
6. Display the digit count.

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

**Sample Input 1:**

```text
Enter an integer: 12345
```

**Sample Output 1:**

```text
Total digits: 5
```

**Sample Input 2:**

```text
Enter an integer: -789
```

**Sample Output 2:**

```text
Total digits: 3
```

**Sample Input 3:**

```text
Enter an integer: 0
```

**Sample Output 3:**

```text
Total digits: 1
```

**Explanation:**

Integer division by ten removes the last digit from the positive magnitude.

Zero requires separate handling because it contains one digit.

**Complexity:**

- Time: O(D), where D is the number of digits.
- Auxiliary space: O(1).

### Problem 8: Reverse a Number

**Problem Statement:**

Accept a non-negative integer and reverse its digits using a `while` loop.

**Logic:**

1. Read a non-negative integer.
2. Initialize the reversed number with zero.
3. Extract the last digit using `% 10`.
4. Append the digit to the reversed number.
5. Remove the last digit using `// 10`.
6. Repeat until the temporary number becomes zero.

**Code:**

```python
number = int(input("Enter a non-negative integer: "))

temporary = number
reversed_number = 0

while temporary > 0:
    digit = temporary % 10

    reversed_number = (
        reversed_number * 10 + digit
    )

    temporary //= 10

print("Original number:", number)
print("Reversed number:", reversed_number)
```

**Sample Input:**

```text
Enter a non-negative integer: 12345
```

**Sample Output:**

```text
Original number: 12345
Reversed number: 54321
```

**Explanation:**

The last digit is extracted during every iteration.

It is then appended to the reversed number.

Leading zeroes are not preserved when the result is represented as an integer.

**Complexity:**

- Time: O(D), where D is the number of digits.
- Auxiliary space: O(1).

### Problem 9: Sum of Digits

**Problem Statement:**

Calculate the sum of all digits in an integer using a `while` loop.

**Logic:**

1. Read an integer.
2. Convert it to its non-negative magnitude using `abs()`.
3. Initialize total with zero.
4. Extract the last digit using modulo.
5. Add the digit to the total.
6. Remove the digit using integer division.
7. Repeat until the number becomes zero.

**Code:**

```python
number = int(input("Enter an integer: "))

temporary = abs(number)
total = 0

while temporary > 0:
    digit = temporary % 10
    total += digit
    temporary //= 10

print("Sum of digits:", total)
```

**Sample Input:**

```text
Enter an integer: 12345
```

**Sample Output:**

```text
Sum of digits: 15
```

**Explanation:**

```text
1 + 2 + 3 + 4 + 5 = 15
```

For an input of zero, the loop executes zero times and the total remains zero.

**Complexity:**

- Time: O(D), where D is the number of digits.
- Auxiliary space: O(1).

### Problem 10: Palindrome Number

**Problem Statement:**

Check whether a non-negative integer reads the same forward and backward.

**Logic:**

1. Read a non-negative integer.
2. Store the original number.
3. Reverse its digits.
4. Compare the reversed number with the original.
5. Display the result.

**Code:**

```python
number = int(input("Enter a non-negative integer: "))

temporary = number
reversed_number = 0

while temporary > 0:
    digit = temporary % 10

    reversed_number = (
        reversed_number * 10 + digit
    )

    temporary //= 10

if number == reversed_number:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
```

**Sample Input 1:**

```text
Enter a non-negative integer: 121
```

**Sample Output 1:**

```text
121 is a palindrome.
```

**Sample Input 2:**

```text
Enter a non-negative integer: 123
```

**Sample Output 2:**

```text
123 is not a palindrome.
```

**Explanation:**

The reverse of 121 is 121.

Since both values are equal, the number is a palindrome.

Zero is also a palindrome under this definition.

**Complexity:**

- Time: O(D), where D is the number of digits.
- Auxiliary space: O(1).

### Problem 11: Find Maximum Number

**Problem Statement:**

Accept a list of integers and find its largest element using a `while` loop.

**Logic:**

1. Read the number of elements.
2. Accept the list elements.
3. Initialize maximum with the first element.
4. Start an index at one.
5. Compare the current element with maximum.
6. Update maximum when a larger value is found.
7. Increase the index.
8. Display the maximum.

**Code:**

```python
count = int(input("How many numbers? "))

numbers = []

index = 0

while index < count:
    number = int(input("Enter a number: "))
    numbers.append(number)
    index += 1

maximum = numbers[0]
index = 1

while index < len(numbers):
    if numbers[index] > maximum:
        maximum = numbers[index]

    index += 1

print("Maximum number:", maximum)
```

**Sample Input:**

```text
How many numbers? 5
Enter a number: 12
Enter a number: 45
Enter a number: 7
Enter a number: 89
Enter a number: 31
```

**Sample Output:**

```text
Maximum number: 89
```

**Explanation:**

The first list element provides the initial maximum.

Each remaining element is compared with it.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(N) for the input list.
- Additional scanning space: O(1).

### Problem 12: Sum Until Zero

**Problem Statement:**

Accept numbers repeatedly until the user enters zero.

Calculate the sum of all numbers entered before zero.

**Logic:**

1. Initialize total with zero.
2. Start an indefinite loop.
3. Read a number.
4. Check whether the number is zero.
5. If zero, terminate the loop.
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

The `break` statement terminates the loop immediately when zero is entered.

Zero is not added to the total.

**Complexity:**

- Time: O(N), where N is the number of non-zero inputs.
- Auxiliary space: O(1).

---

## 24. Ten Unsolved Practice Questions

Solve these questions independently using `while` loops.

### Question 1: Multiples of Three

Write a program to print all multiples of three from one to N.

Example:

```text
Input:
N = 15

Expected Output:
3 6 9 12 15
```

### Question 2: Product of Natural Numbers

Write a program to calculate the product of the first N natural numbers.

Example:

```text
Input:
N = 5

Expected Output:
120
```

### Question 3: Smallest Digit

Write a program to find the smallest digit in an integer.

Example:

```text
Input:
58231

Expected Output:
1
```

### Question 4: Count Even and Odd Digits

Write a program to count the even and odd digits in an integer.

Example:

```text
Input:
123456

Expected Output:
Even digits: 3
Odd digits: 3
```

### Question 5: Fibonacci Series

Write a program to generate the first N terms of the Fibonacci series using a `while` loop.

Example:

```text
Input:
N = 7

Expected Output:
0 1 1 2 3 5 8
```

### Question 6: Prime Number

Write a program to check whether a positive integer is prime using a `while` loop.

Example:

```text
Input:
7

Expected Output:
Prime number
```

### Question 7: Average Until Zero

Write a program to accept numbers until zero is entered and calculate the average of all preceding inputs.

Example:

```text
Input:
10
20
30
0

Expected Output:
Average: 20.0
```

### Question 8: First Number Divisible by Three and Five

Write a program to find the first number greater than N that is divisible by both three and five.

Example:

```text
Input:
N = 16

Expected Output:
30
```

### Question 9: Character Occurrence

Write a program to count how many times a given character appears in a string using a `while` loop.

Example:

```text
Input:
String = banana
Character = a

Expected Output:
3
```

### Question 10: Armstrong Number

Write a program to check whether an integer is an Armstrong number using a `while` loop.

Example:

```text
Input:
153

Expected Output:
Armstrong number
```

---

## 25. Common Mistakes While Using While Loops

### Mistake 1: Forgetting the Update Statement

Incorrect:

```python
number = 1

while number <= 5:
    print(number)
```

The number never changes.

The condition remains true.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Mistake 2: Updating in the Wrong Direction

Incorrect:

```python
number = 1

while number <= 5:
    print(number)
    number -= 1
```

The number becomes smaller, so the condition remains true.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Mistake 3: Incorrect Comparison Operator

Incorrect:

```python
number = 1

while number >= 5:
    print(number)
    number += 1
```

The condition is initially false.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Mistake 4: Missing Initialization

Incorrect:

```python
while number <= 5:
    print(number)
    number += 1
```

If `number` has not been defined, Python raises a `NameError`.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Mistake 5: Incorrect Indentation

Incorrect:

```python
number = 1

while number <= 5:
print(number)
number += 1
```

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Mistake 6: Forgetting the Zero Case in Digit Counting

A program that only loops while a number is greater than zero will perform zero iterations for an input of zero.

Correct approach:

```python
number = 0

if number == 0:
    count = 1
```

### Mistake 7: Incorrect Accumulator Initialization

Incorrect:

```python
total = 1
number = 1

while number <= 5:
    total += number
    number += 1
```

This produces an incorrect sum.

Correct:

```python
total = 0
number = 1

while number <= 5:
    total += number
    number += 1
```

### Mistake 8: Incorrect Factorial Initialization

Incorrect:

```python
factorial = 0
```

Multiplication by zero keeps the result at zero.

Correct:

```python
factorial = 1
```

### Mistake 9: Accessing an Invalid List Index

Incorrect:

```python
numbers = [10, 20, 30]
index = 0

while index <= len(numbers):
    print(numbers[index])
    index += 1
```

When the index becomes three, it is outside the valid index range.

Correct:

```python
numbers = [10, 20, 30]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

### Mistake 10: Using break Before Updating Without Understanding the Logic

Consider:

```python
number = 1

while number <= 5:
    if number == 3:
        break

    print(number)
    number += 1
```

The loop stops when number becomes three.

This is intentional in this example.

However, when using a `break` statement, check that the termination condition is appropriate.

---

## 26. Best Practices for While Loops

1. Initialize loop-control variables before the loop.
2. Write clear Boolean conditions.
3. Ensure the loop can terminate when termination is intended.
4. Update the correct control variable.
5. Check the update direction.
6. Use meaningful variable names.
7. Avoid unnecessary nested loops.
8. Use `break` only when an early exit is required.
9. Use sentinel values clearly.
10. Validate input.
11. Handle zero and negative numbers where relevant.
12. Check list indexes before accessing elements.
13. Keep loop bodies readable.
14. Use consistent indentation.
15. Test small input values.
16. Test boundary conditions.
17. Consider empty collections.
18. Avoid accidental infinite loops.
19. Use `try-except` for invalid input conversion.
20. Understand the time complexity of repeated operations.

---

## 27. Debugging While Loop Programs

Debugging means identifying and correcting errors in a program.

While-loop errors frequently involve conditions, updates, and termination.

### 27.1 Print the Current Variable

```python
number = 1

while number <= 5:
    print("Current value:", number)
    number += 1
```

This helps track the changing value.

### 27.2 Check the Initial Value

Verify that the variable begins with an appropriate value.

### 27.3 Check the Condition

Ask:

- Is the comparison correct?
- Can the condition eventually become false?
- Is the correct boundary used?
- Is the variable being compared correctly?

### 27.4 Check the Update

Verify that the variable changes in the required direction.

### 27.5 Check for Infinite Loops

Ask whether the loop has a valid termination path.

### 27.6 Test Small Inputs

Use simple values such as:

```text
0
1
2
5
10
```

Small inputs help identify errors quickly.

### 27.7 Common Error Types

| Error | Possible Cause |
|---|---|
| `SyntaxError` | Incorrect Python syntax |
| `IndentationError` | Incorrect indentation |
| `NameError` | Undefined variable |
| `TypeError` | Invalid operation between types |
| `ValueError` | Invalid input conversion |
| `IndexError` | Accessing an invalid sequence index |

---

## 28. Real-Life Applications of While Loops

### 28.1 Login Systems

A program can repeat login attempts until valid credentials are provided or an attempt limit is reached.

### 28.2 ATM Applications

An ATM program can repeatedly display a menu until the user selects an exit option.

### 28.3 Input Validation

A program can continue asking for data until valid input is received.

### 28.4 Student Marks Processing

A program can accept marks until a sentinel value indicates that data entry is complete.

### 28.5 Number Games

A guessing game can continue until the correct number is guessed.

### 28.6 Banking Applications

A transaction menu can remain active until the user chooses to exit.

### 28.7 Inventory Management

Repeated inventory operations can continue until a stopping condition is reached.

### 28.8 Data Entry

A system can accept multiple records until an end marker is entered.

### 28.9 Automation

Automation scripts can continue processing until a condition indicates completion.

### 28.10 Interactive Software

Interactive programs frequently use condition-controlled repetition to keep menus and user interactions active.

---

## 29. Connection Between While Loops and DSA

The `while` loop is important in Data Structures and Algorithms because many algorithms repeat operations until a condition is satisfied.

### 29.1 Array Traversal

```python
numbers = [10, 20, 30, 40, 50]

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

Time complexity: O(N).

### 29.2 Linear Search

```python
numbers = [10, 20, 30, 40, 50]

target = 30
index = 0
found = False

while index < len(numbers):
    if numbers[index] == target:
        found = True
        break

    index += 1

if found:
    print("Element found")
else:
    print("Element not found")
```

Worst-case time complexity: O(N).

### 29.3 Finding the Maximum Element

```python
numbers = [12, 45, 7, 89, 31]

index = 1
maximum = numbers[0]

while index < len(numbers):
    if numbers[index] > maximum:
        maximum = numbers[index]

    index += 1

print(maximum)
```

Time complexity: O(N).

### 29.4 Finding the Minimum Element

```python
numbers = [12, 45, 7, 89, 31]

index = 1
minimum = numbers[0]

while index < len(numbers):
    if numbers[index] < minimum:
        minimum = numbers[index]

    index += 1

print(minimum)
```

Time complexity: O(N).

### 29.5 Reverse Traversal

```python
numbers = [10, 20, 30, 40, 50]

index = len(numbers) - 1

while index >= 0:
    print(numbers[index])
    index -= 1
```

Time complexity: O(N).

### 29.6 Two-Pointer Techniques

Two-pointer algorithms often use `while` loops to move two indexes toward each other.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

left = 0
right = len(numbers) - 1

while left < right:
    print(numbers[left], numbers[right])

    left += 1
    right -= 1
```

### 29.7 Binary Search

Binary Search uses a condition-controlled loop to reduce the search interval.

It is commonly implemented with a `while` loop.

### 29.8 Sliding Window

Some sliding-window algorithms use a `while` loop to adjust window boundaries.

### 29.9 Number-Based Algorithms

Digit extraction, number reversal, palindrome checking, and digit summation frequently use `while` loops.

### 29.10 Stack and Queue Processing

Some algorithms that process stack or queue elements use condition-controlled loops until the data structure becomes empty.

---

## 30. Time and Space Complexity

Time complexity describes how the execution time grows with input size.

Space complexity describes how memory consumption grows with input size.

A `while` loop's complexity depends on the number of iterations and the work performed during each iteration.

### 30.1 Fixed Number of Iterations

```python
number = 1

while number <= 10:
    print(number)
    number += 1
```

The loop always executes ten times.

Time complexity: O(1), because the iteration count is fixed.

### 30.2 Linear Loop

```python
number = 1

while number <= n:
    print(number)
    number += 1
```

The number of iterations grows with N.

Time complexity: O(N).

### 30.3 Decreasing by One

```python
number = n

while number > 0:
    print(number)
    number -= 1
```

The loop executes approximately N times.

Time complexity: O(N).

### 30.4 Repeated Halving

```python
number = n

while number > 1:
    number //= 2
```

The variable is divided by two during each iteration.

The iteration count grows logarithmically.

Time complexity: O(log N).

### 30.5 Nested While Loops

```python
i = 0

while i < n:
    j = 0

    while j < n:
        print(i, j)
        j += 1

    i += 1
```

The inner loop executes N times for each outer-loop iteration.

Time complexity: O(N²).

### 30.6 Two Consecutive While Loops

```python
number = 0

while number < n:
    print(number)
    number += 1

number = 0

while number < n:
    print(number)
    number += 1
```

The total number of iterations is approximately 2N.

Ignoring constant factors:

Time complexity: O(N).

### Complexity Reference

| Loop Pattern | Typical Time Complexity |
|---|---|
| Fixed number of iterations | O(1) |
| Increment by one | O(N) |
| Decrement by one | O(N) |
| Repeated halving | O(log N) |
| Two nested linear loops | O(N²) |
| Three nested linear loops | O(N³) |
| Two consecutive linear loops | O(N) |

The actual complexity depends on the operations performed inside the loop.

---

## 31. Mini Project: Number Analyzer Using While Loop

### Project Objective

Build a number-analysis program that accepts a positive integer and performs several operations using a `while` loop.

The project should:

1. Display numbers from one to N.
2. Display even numbers.
3. Display odd numbers.
4. Calculate the sum of natural numbers.
5. Count the digits.
6. Calculate the sum of digits.
7. Reverse the number.
8. Display the results.

### Project Code

```python
"""
Project: Number Analyzer Using While Loop

Description:
Analyze a positive integer using condition-controlled loops.
"""


def analyze_number(number: int) -> None:
    """
    Display properties of a positive integer.
    """
    if number <= 0:
        print("Please enter a positive integer.")
        return

    print("\nNumbers from 1 to N:")

    current = 1

    while current <= number:
        print(current, end=" ")
        current += 1

    print("\n\nEven numbers:")

    current = 2

    while current <= number:
        print(current, end=" ")
        current += 2

    print("\n\nOdd numbers:")

    current = 1

    while current <= number:
        print(current, end=" ")
        current += 2

    total = 0
    current = 1

    while current <= number:
        total += current
        current += 1

    print("\n\nSum of natural numbers:", total)

    temporary = number
    digit_count = 0
    digit_sum = 0
    reversed_number = 0

    while temporary > 0:
        digit = temporary % 10

        digit_count += 1
        digit_sum += digit

        reversed_number = (
            reversed_number * 10 + digit
        )

        temporary //= 10

    print("Number of digits:", digit_count)
    print("Sum of digits:", digit_sum)
    print("Reversed number:", reversed_number)


def main() -> None:
    """
    Accept input and execute the number analyzer.
    """
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
Sum of digits: 1
Reversed number: 1
```

### Concepts Used

- `while` loops.
- Conditions.
- Variables.
- Counters.
- Accumulators.
- Integer division.
- Modulo operator.
- Input conversion.
- Functions.
- Exception handling.

---

## 32. Fifty Viva Questions and Answers

### Basic While Loop Questions

**Q1. What is a while loop in Python?**

A `while` loop repeatedly executes its body while its condition is true.

**Q2. Why are while loops used?**

They are useful when repetition depends on a condition.

**Q3. What is the syntax of a while loop?**

```python
while condition:
    statement
```

**Q4. What is initialization?**

Initialization assigns the initial value to a loop-control variable.

**Q5. What is a loop condition?**

A Boolean expression that controls whether the loop continues.

**Q6. What is a loop update?**

An operation that changes a loop-control variable.

**Q7. What is iteration?**

One complete execution of a loop body.

**Q8. When is the while condition checked?**

It is checked before every iteration.

**Q9. What happens when the condition is initially false?**

The loop body does not execute.

**Q10. Can a while loop execute zero times?**

Yes. It executes zero times when the condition is initially false.

### Loop Control Questions

**Q11. What is an infinite loop?**

A loop that continues indefinitely without normal termination.

**Q12. What commonly causes an infinite loop?**

An unchanged control variable or a condition that never becomes false.

**Q13. How can an infinite loop be prevented?**

Use correct initialization, conditions, and updates, and provide a valid exit path.

**Q14. What does the `break` statement do?**

It immediately terminates the nearest enclosing loop.

**Q15. What is `while True`?**

It creates a loop with a condition that always evaluates to true.

**Q16. How can a while True loop terminate?**

It can use a control statement such as `break`, or another suitable termination mechanism.

**Q17. What is a sentinel value?**

A special value used to indicate that repeated input or processing should stop.

**Q18. What is a sentinel-controlled loop?**

A loop that continues until a designated sentinel value is encountered.

**Q19. What is an accumulator?**

A variable used to store a running result, such as a sum.

**Q20. What is a counter?**

A variable used to count occurrences or iterations.

### Programming Questions

**Q21. How can you print numbers from one to N using a while loop?**

Initialize a counter to one, continue while it is at most N, print it, and increment it.

**Q22. How can you print numbers in descending order?**

Start with the largest value and decrease the variable during every iteration.

**Q23. How can you print even numbers?**

Start with two and increase the number by two, or test divisibility by two.

**Q24. How can you print odd numbers?**

Start with one and increase by two, or use a modulo condition.

**Q25. How can you calculate a sum?**

Initialize an accumulator to zero and add values during every iteration.

**Q26. How can you calculate factorial?**

Initialize the result to one and repeatedly multiply it by consecutive positive integers.

**Q27. How can you count digits?**

Repeatedly perform integer division by ten and increase a counter.

**Q28. How can you reverse a number?**

Extract the last digit using `% 10`, append it to a new number, and remove it using `// 10`.

**Q29. How can you calculate the sum of digits?**

Extract each digit with modulo and add it to an accumulator.

**Q30. What is a palindrome number?**

A number that remains the same when its digits are reversed.

### Input and Data Structure Questions

**Q31. How can a while loop validate user input?**

Repeat the input operation until the supplied value satisfies the required condition.

**Q32. Why is `len()` used when iterating through a string with a while loop?**

It provides the boundary for valid string indexes.

**Q33. How can you iterate through a list using a while loop?**

Start an index at zero and continue while the index is smaller than the list length.

**Q34. What is the purpose of an index?**

It identifies the position of an element in an indexed sequence.

**Q35. What is `IndexError`?**

An exception raised when an invalid index is used for an indexed sequence.

**Q36. Why should a loop index be updated?**

It allows the loop to progress through the sequence and reach its termination condition.

**Q37. What is the difference between `break` and `continue`?**

`break` terminates the nearest loop, while `continue` skips the rest of the current iteration and moves to the next iteration.

**Q38. What is input validation?**

Checking whether the entered value satisfies the program's requirements.

**Q39. Why use `try-except` during input conversion?**

It handles exceptions such as `ValueError` when invalid text is converted into an integer.

**Q40. Can a while loop process user input until zero is entered?**

Yes. Zero can act as a sentinel value.

### DSA and Complexity Questions

**Q41. What is time complexity?**

Time complexity describes how an algorithm's running time grows with input size.

**Q42. What is the time complexity of a linear while loop?**

O(N), when the loop performs N constant-time iterations.

**Q43. What is the complexity of repeated halving?**

O(log N), when the value is reduced by a constant factor such as two.

**Q44. What is the time complexity of two nested linear while loops?**

Generally O(N²).

**Q45. What is the space complexity of a loop that uses only a few variables?**

Usually O(1) auxiliary space.

**Q46. What is array traversal?**

Visiting the elements of an array or list.

**Q47. Can a while loop implement linear search?**

Yes. It can use an index and continue until the target is found or the list ends.

**Q48. Where is a while loop used in Binary Search?**

It controls the search interval while the left and right boundaries have not crossed.

**Q49. Why are while loops useful in DSA?**

They support condition-controlled traversal, search boundaries, two-pointer algorithms, and repeated number operations.

**Q50. What should be understood before solving advanced while-loop DSA questions?**

Initialization, conditions, updates, termination, indexing, and complexity analysis should be understood.

---

## 33. Important Terminology

| Term | Meaning |
|---|---|
| While Loop | Condition-controlled looping statement |
| Initialization | Assigning the initial value |
| Condition | Boolean expression controlling repetition |
| Update | Changing the loop-control variable |
| Iteration | One execution of the loop body |
| Loop Body | Statements executed during an iteration |
| Termination | Ending of loop execution |
| Infinite Loop | Loop that does not terminate normally |
| Sentinel | Special value used to stop repetition |
| Counter | Variable used for counting |
| Accumulator | Variable used to collect a result |
| Condition-Controlled Repetition | Repetition based on a Boolean condition |
| `break` | Terminates the nearest enclosing loop |
| `continue` | Skips the rest of the current iteration |
| `pass` | Null statement that performs no action |
| `len()` | Function that returns the length of a collection |
| Index | Position of an element |
| `%` | Modulo operator |
| `//` | Integer division operator |
| Input Validation | Checking whether input is valid |
| `try-except` | Exception-handling structure |
| Two-Pointer | Technique using two positions in a sequence |
| Binary Search | Search algorithm that repeatedly reduces a search interval |
| Complexity | Measure of algorithm growth |

---

## 34. Quick Revision Notes

### Basic Syntax

```python
while condition:
    statement
    update
```

### Print Numbers

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Countdown

```python
number = 5

while number >= 1:
    print(number)
    number -= 1
```

### Even Numbers

```python
number = 2

while number <= 10:
    print(number)
    number += 2
```

### Odd Numbers

```python
number = 1

while number <= 10:
    print(number)
    number += 2
```

### Sum of Natural Numbers

```python
number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print(total)
```

### Multiplication Table

```python
number = 5
multiplier = 1

while multiplier <= 10:
    print(number * multiplier)
    multiplier += 1
```

### String Iteration

```python
text = "PYTHON"
index = 0

while index < len(text):
    print(text[index])
    index += 1
```

### List Iteration

```python
numbers = [10, 20, 30]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

### Count Digits

```python
number = 12345
count = 0

while number > 0:
    number //= 10
    count += 1

print(count)
```

### Reverse Number

```python
number = 1234
reversed_number = 0

while number > 0:
    digit = number % 10

    reversed_number = (
        reversed_number * 10 + digit
    )

    number //= 10

print(reversed_number)
```

### Sentinel Loop

```python
while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    print(number)
```

### Important Rules

- The condition is checked before every iteration.
- A false condition skips the loop body.
- Initialization should be performed before the loop when required.
- Update the correct control variable.
- Ensure the loop progresses toward termination.
- An infinite loop is possible.
- `break` terminates the nearest enclosing loop.
- `continue` skips the rest of the current iteration.
- Sentinel values can control repetition.
- Input validation can use a while loop.

### Complexity Reference

| Pattern | Typical Complexity |
|---|---|
| Fixed iterations | O(1) |
| Increment by one | O(N) |
| Decrement by one | O(N) |
| Repeated halving | O(log N) |
| Two nested linear loops | O(N²) |
| Two consecutive linear loops | O(N) |

---

## 35. Learning Checklist

### While Loop Fundamentals

- [ ] I understand what a while loop is.
- [ ] I understand why while loops are used.
- [ ] I understand condition-controlled repetition.
- [ ] I understand initialization.
- [ ] I understand loop conditions.
- [ ] I understand variable updates.
- [ ] I can write a basic while loop.

### Number Sequences

- [ ] I can print numbers in ascending order.
- [ ] I can print numbers in descending order.
- [ ] I can generate even numbers.
- [ ] I can generate odd numbers.
- [ ] I can calculate sums.
- [ ] I can generate multiplication tables.

### Strings and Collections

- [ ] I can iterate through a string using an index.
- [ ] I can iterate through a list using an index.
- [ ] I understand the role of `len()`.
- [ ] I can avoid invalid index access.

### Number-Based Programming

- [ ] I can count digits.
- [ ] I can reverse a number.
- [ ] I can calculate the sum of digits.
- [ ] I can calculate factorial.
- [ ] I can check a palindrome number.
- [ ] I can find the maximum element in a list.

### Loop Control

- [ ] I understand infinite loops.
- [ ] I can identify common causes of infinite loops.
- [ ] I understand sentinel-controlled loops.
- [ ] I can use `break`.
- [ ] I understand `continue`.
- [ ] I can validate user input.

### DSA Preparation

- [ ] I understand linear traversal.
- [ ] I understand linear search.
- [ ] I understand repeated halving.
- [ ] I understand nested loops.
- [ ] I can identify O(1) complexity.
- [ ] I can identify O(N) complexity.
- [ ] I can identify O(log N) complexity.
- [ ] I can identify O(N²) complexity.

---

## 36. How to Run the Python File

### Step 1: Open Your Repository

Open your `DSA-Python` project in VS Code.

### Step 2: Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 04-While-Loop/
            ├── README.md
            └── 04_while_loop.py
```

### Step 3: Open the Terminal

Open the integrated terminal in VS Code.

### Step 4: Execute the Python File

Run the following command from the repository root:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/04-While-Loop/04_while_loop.py
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
            └── 04-While-Loop/
                ├── README.md
                └── 04_while_loop.py
```

### File Responsibilities

**README.md**

Contains:

- Introduction.
- Learning objectives.
- While loop definition.
- Syntax and explanation.
- Initialization, condition, and update.
- Loop execution.
- Ascending and descending sequences.
- Even and odd number generation.
- Sum and multiplication table.
- String and list iteration.
- Digit counting.
- Number reversal.
- Infinite loops.
- Sentinel-controlled loops.
- Input validation.
- Twelve topic examples.
- Twelve solved programming problems.
- Ten unsolved practice questions.
- Common mistakes.
- Best practices.
- Debugging.
- Real-life applications.
- DSA connections.
- Complexity analysis.
- Mini project.
- Fifty viva questions and answers.
- Important terminology.
- Quick revision notes.
- Learning checklist.
- Execution instructions.

**04_while_loop.py**

Contains:

- Twelve executable topic examples.
- Twelve selectable solved problems.
- Ten unsolved practice questions.
- Learning checklist.
- Interactive menu.
- Input validation.

---

## 38. Final Summary

The `while` loop is an important Python control structure used for condition-controlled repetition.

It executes a block of code as long as its condition remains true.

Three important parts of a typical while loop are:

1. Initialization.
2. Condition.
3. Update.

A while loop can generate ascending and descending sequences, calculate sums, print multiplication tables, iterate through strings and lists, count digits, reverse numbers, and process repeated user input.

Sentinel-controlled loops are useful when the number of inputs is unknown.

Input validation is another important application of the `while` loop.

However, incorrect conditions or missing updates can cause infinite loops.

Understanding loop termination and complexity is important before moving to advanced DSA algorithms.

### What You Should Do Next

1. Read the complete theory.
2. Understand initialization, condition, and update.
3. Run `04_while_loop.py`.
4. Execute all twelve examples.
5. Try all twelve solved problems.
6. Attempt all ten unsolved questions independently.
7. Complete the learning checklist.
8. Revise the fifty viva questions.
9. Practise preventing infinite loops.
10. Understand the difference between `for` and `while`.

**Topic Completed: While Loop in Python**

The next topic in this repository is:

`05-Nested-Loops`

Its Python source file will be:

`05_nested_loops.py`