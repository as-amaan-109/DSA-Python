

# Python Positive and Negative Numbers – Complete Guide

## 1. Introduction

Positive and negative numbers are among the most basic concepts in mathematics and programming.

In Python, we use conditional statements to identify whether a number is positive, negative, or zero.

This problem is useful for understanding how a program makes decisions based on numeric values.

Every real number belongs to one of three categories:

1. Positive numbers.
2. Negative numbers.
3. Zero.

A positive number is greater than zero.

A negative number is less than zero.

Zero is neither positive nor negative.

### Examples of Positive Numbers

```python
10
25
100
1
0.5
12.75
```

All these numbers are greater than zero.

### Examples of Negative Numbers

```python
-10
-25
-100
-1
-0.5
-12.75
```

All these numbers are less than zero.

### Example of Zero

```python
0
0.0
-0.0
```

All these values represent zero.

### Learning Objectives

After completing this topic, you should be able to:

- Understand positive numbers.
- Understand negative numbers.
- Understand zero.
- Identify whether an integer is positive or negative.
- Identify whether a decimal number is positive or negative.
- Classify numbers into positive, negative, and zero.
- Use `if`, `elif`, and `else`.
- Use comparison operators.
- Understand the difference between positive and non-negative numbers.
- Check whether a positive number is even or odd.
- Check whether a negative number is even or odd.
- Count positive and negative values in a collection.
- Calculate the sum of positive numbers.
- Find the first positive number in a list.
- Filter positive values from a list.
- Find the largest positive number.
- Validate positive input.
- Apply number classification to practical programming problems.
- Understand how number classification is used in DSA.

---

## 2. Understanding Positive, Negative and Zero

### 2.1 Positive Numbers

A positive number is any number greater than zero.

Mathematically:

\[
n > 0
\]

Examples:

```python
number = 10

if number > 0:
    print("Positive number")
```

Output:

```text
Positive number
```

The condition `number > 0` checks whether the value is greater than zero.

Because `10` is greater than zero, the condition is true.

### 2.2 Negative Numbers

A negative number is any number smaller than zero.

Mathematically:

\[
n < 0
\]

Example:

```python
number = -10

if number < 0:
    print("Negative number")
```

Output:

```text
Negative number
```

The condition is true because `-10` is smaller than zero.

### 2.3 Zero

Zero is neither positive nor negative.

Mathematically:

\[
n = 0
\]

Example:

```python
number = 0

if number == 0:
    print("Number is zero")
```

Output:

```text
Number is zero
```

The equality operator `==` checks whether the value is equal to zero.

### 2.4 Number Classification

A number can be classified using three conditions.

```python
number = -15

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

Output:

```text
Negative number
```

### Explanation

The program checks the conditions in order.

First:

```python
number > 0
```

The condition is false.

Next:

```python
number < 0
```

The condition is true.

Therefore, Python executes the `elif` block.

The final `else` block executes only when both previous conditions are false.

For an ordinary numeric value, that means the number is zero.

### 2.5 Number Classification Table

| Number | Classification | Reason |
|---:|---|---|
| 25 | Positive | Greater than zero |
| 10 | Positive | Greater than zero |
| 1 | Positive | Greater than zero |
| 0.5 | Positive | Greater than zero |
| 0 | Zero | Equal to zero |
| -0.5 | Negative | Less than zero |
| -1 | Negative | Less than zero |
| -10 | Negative | Less than zero |
| -25 | Negative | Less than zero |

### 2.6 Important Mathematical Rules

| Rule | Meaning |
|---|---|
| `number > 0` | Positive |
| `number < 0` | Negative |
| `number == 0` | Zero |
| `number >= 0` | Non-negative |
| `number <= 0` | Non-positive |

These conditions are different and should not be confused.

---

## 3. Python Syntax and Explanation

### 3.1 Basic If Statement

Syntax:

```python
if condition:
    statement
```

Example:

```python
number = 20

if number > 0:
    print("Positive number")
```

Explanation:

- `if` starts the conditional statement.
- `number > 0` is the condition.
- The condition produces a Boolean result.
- If the result is `True`, Python executes the indented statement.

### 3.2 If-Else Statement

Syntax:

```python
if condition:
    statement1
else:
    statement2
```

Example:

```python
number = -20

if number > 0:
    print("Positive number")
else:
    print("Not positive")
```

Output:

```text
Not positive
```

Explanation:

If the number is greater than zero, the first block executes.

Otherwise, the `else` block executes.

This example groups negative numbers and zero together.

### 3.3 If-Elif-Else Statement

Syntax:

```python
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
```

Example:

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Output:

```text
Zero
```

### 3.4 Why Use Elif?

We need three different categories:

- Positive.
- Negative.
- Zero.

A single `if-else` can select only between two branches.

An `if-elif-else` structure is more suitable when there are three alternatives.

### 3.5 Comparison Operators

Comparison operators are used to compare values.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `number == 0` |
| `!=` | Not equal to | `number != 0` |
| `>` | Greater than | `number > 0` |
| `<` | Less than | `number < 0` |
| `>=` | Greater than or equal | `number >= 0` |
| `<=` | Less than or equal | `number <= 0` |

### Example Using Comparison Operators

```python
number = 10

print(number > 0)
print(number < 0)
print(number == 0)
print(number != 0)
```

Output:

```text
True
False
False
True
```

### 3.6 Positive vs Non-Negative

A positive number is strictly greater than zero.

A non-negative number is greater than or equal to zero.

| Value | Positive? | Non-negative? |
|---:|---|---|
| 10 | Yes | Yes |
| 1 | Yes | Yes |
| 0 | No | Yes |
| -1 | No | No |
| -10 | No | No |

Python examples:

```python
number = 0

print(number > 0)
print(number >= 0)
```

Output:

```text
False
True
```

### 3.7 Negative vs Non-Positive

A negative number is strictly less than zero.

A non-positive number is less than or equal to zero.

| Value | Negative? | Non-positive? |
|---:|---|---|
| 10 | No | No |
| 1 | No | No |
| 0 | No | Yes |
| -1 | Yes | Yes |
| -10 | Yes | Yes |

Python examples:

```python
number = 0

print(number < 0)
print(number <= 0)
```

Output:

```text
False
True
```

### 3.8 Integer Input

The `input()` function returns a string.

Use `int()` when an integer is required.

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### 3.9 Decimal Input

Use `float()` when decimal values are accepted.

```python
number = float(input("Enter a decimal number: "))

if number > 0:
    print("Positive decimal")
elif number < 0:
    print("Negative decimal")
else:
    print("Zero")
```

### 3.10 Handling Invalid Numeric Input

An invalid input can cause a `ValueError`.

For example:

```python
number = int("hello")
```

This does not produce a valid integer.

A safe approach is to use `try-except`.

```python
try:
    number = float(input("Enter a number: "))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

except ValueError:
    print("Please enter a valid number")
```

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Positive Number

### Objective

Write a Python program to check whether a number is positive.

### Code

```python
number = 25

if number > 0:
    print("Positive number")
else:
    print("Not a positive number")
```

### Output

```text
Positive number
```

### Explanation

The variable `number` stores 25.

Python checks:

```python
number > 0
```

Since 25 is greater than zero, the condition is true.

Therefore, the program prints:

```text
Positive number
```

### Concepts Used

- If statement.
- Comparison operator.
- Positive-number classification.

---

## Example 2: Negative Number

### Objective

Check whether a number is negative.

### Code

```python
number = -15

if number < 0:
    print("Negative number")
else:
    print("Not a negative number")
```

### Output

```text
Negative number
```

### Explanation

The condition is:

```python
number < 0
```

The value is `-15`.

Because `-15` is less than zero, the condition is true.

Python executes the first block.

### Concepts Used

- If statement.
- Less-than operator.
- Negative-number classification.

---

## Example 3: Zero Check

### Objective

Check whether a number is exactly zero.

### Code

```python
number = 0

if number == 0:
    print("The number is zero")
else:
    print("The number is not zero")
```

### Output

```text
The number is zero
```

### Explanation

The equality operator compares the number with zero.

Since both values are equal, Python executes the first block.

### Concepts Used

- Equality operator.
- If-else.
- Zero classification.

---

## Example 4: Positive, Negative or Zero

### Objective

Classify a number into one of three categories.

### Code

```python
number = -20

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

### Output

```text
Negative number
```

### Explanation

The first condition checks whether the number is positive.

It is false.

The second condition checks whether the number is negative.

It is true.

Therefore, Python executes the `elif` block.

### Concepts Used

- If-elif-else.
- Three-way classification.
- Comparison operators.

---

## Example 5: Positive or Non-Positive

### Objective

Check whether a number is positive or non-positive.

### Code

```python
number = 0

result = "Positive" if number > 0 else "Non-positive"

print("Number:", number)
print("Result:", result)
```

### Output

```text
Number: 0
Result: Non-positive
```

### Explanation

A non-positive value is either zero or negative.

Since zero is not greater than zero, the false expression is selected.

### Concepts Used

- Conditional expression.
- Greater-than operator.
- Positive and non-positive classification.

---

## Example 6: Non-Negative Number

### Objective

Check whether a number is non-negative.

### Code

```python
number = 10

if number >= 0:
    print("Non-negative number")
else:
    print("Negative number")
```

### Output

```text
Non-negative number
```

### Explanation

The condition `number >= 0` includes zero and all positive values.

Since 10 is greater than zero, it is non-negative.

### Concepts Used

- Greater-than-or-equal operator.
- If-else.
- Non-negative classification.

---

## Example 7: Positive Even or Odd

### Objective

Check whether a positive integer is even or odd.

### Code

```python
number = 12

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")
```

### Output

```text
Positive even number
```

### Explanation

First, Python checks whether the number is positive.

Then it checks whether the number is divisible by two.

The expression:

```python
number % 2 == 0
```

is true for even integers.

### Concepts Used

- Nested if.
- Modulus operator.
- Even and odd classification.

---

## Example 8: Negative Even or Odd

### Objective

Check whether a negative integer is even or odd.

### Code

```python
number = -7

if number < 0:
    if number % 2 == 0:
        print("Negative even number")
    else:
        print("Negative odd number")
else:
    print("Number is not negative")
```

### Output

```text
Negative odd number
```

### Explanation

The first condition checks whether the number is negative.

Since `-7` is negative, Python enters the inner condition.

The remainder of `-7 % 2` is non-zero.

Therefore, the number is odd.

### Concepts Used

- Nested if.
- Modulus operator.
- Negative-number classification.

### Important Note

In Python, negative integers can also be classified as even or odd.

For example:

```python
-8 % 2 == 0
```

evaluates to `True`.

---

## Example 9: Count Positive, Negative and Zero Values

### Objective

Count positive, negative, and zero values in a list.

### Code

```python
numbers = [10, -5, 0, 20, -8, 0, 15]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Numbers:", numbers)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
```

### Output

```text
Numbers: [10, -5, 0, 20, -8, 0, 15]
Positive numbers: 3
Negative numbers: 2
Zeros: 2
```

### Explanation

The program initializes three counters.

Each number is checked.

- Positive values increase `positive_count`.
- Negative values increase `negative_count`.
- Zero values increase `zero_count`.

The loop processes every element exactly once.

### Concepts Used

- For loop.
- If-elif-else.
- Lists.
- Counter variables.

---

## Example 10: Sum of Positive Numbers

### Objective

Calculate the sum of only the positive values in a list.

### Code

```python
numbers = [10, -5, 20, -8, 15]

positive_sum = 0

for number in numbers:
    if number > 0:
        positive_sum += number

print("Numbers:", numbers)
print("Sum of positive numbers:", positive_sum)
```

### Output

```text
Numbers: [10, -5, 20, -8, 15]
Sum of positive numbers: 45
```

### Explanation

Only values greater than zero are added.

The positive values are:

```text
10, 20, 15
```

Their sum is:

```text
10 + 20 + 15 = 45
```

Negative values are ignored.

### Concepts Used

- For loop.
- If statement.
- Accumulator variable.
- List traversal.

---

## Example 11: Find the First Positive Number

### Objective

Find the first positive number in a list.

### Code

```python
numbers = [-5, -2, 0, 8, 10]

first_positive = None

for number in numbers:
    if number > 0:
        first_positive = number
        break

print("Numbers:", numbers)

if first_positive is not None:
    print("First positive number:", first_positive)
else:
    print("No positive number found")
```

### Output

```text
Numbers: [-5, -2, 0, 8, 10]
First positive number: 8
```

### Explanation

The loop checks the numbers from left to right.

The first three values are not positive.

When Python reaches 8, the condition becomes true.

The value is stored in `first_positive`.

The `break` statement stops the loop.

### Concepts Used

- For loop.
- If statement.
- `break`.
- `None`.
- Searching.

---

## Example 12: Decimal Number Classification

### Objective

Classify a floating-point number as positive, negative, or zero.

### Code

```python
number = -12.75

if number > 0:
    print("Positive decimal number")
elif number < 0:
    print("Negative decimal number")
else:
    print("Decimal value is zero")
```

### Output

```text
Negative decimal number
```

### Explanation

A floating-point number can also be positive, negative, or zero.

The same comparison rules apply.

Because `-12.75` is less than zero, Python prints the negative classification.

### Concepts Used

- Float data type.
- If-elif-else.
- Comparison operators.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Classify an Integer

### Problem Statement

Write a program that accepts an integer and determines whether it is positive, negative, or zero.

### Logic

1. Accept an integer from the user.
2. Check whether the number is greater than zero.
3. If true, classify it as positive.
4. Otherwise, check whether the number is smaller than zero.
5. If true, classify it as negative.
6. Otherwise, classify it as zero.

### Code

```python
number = int(input("Enter an integer: "))

if number > 0:
    result = "Positive"
elif number < 0:
    result = "Negative"
else:
    result = "Zero"

print("Number:", number)
print("Classification:", result)
```

### Sample Input 1

```text
Enter an integer: 25
```

### Expected Output 1

```text
Number: 25
Classification: Positive
```

### Sample Input 2

```text
Enter an integer: -15
```

### Expected Output 2

```text
Number: -15
Classification: Negative
```

### Sample Input 3

```text
Enter an integer: 0
```

### Expected Output 3

```text
Number: 0
Classification: Zero
```

### Explanation

This is the basic number-classification problem.

The conditions are mutually exclusive:

- A number cannot be both greater than zero and less than zero.
- Zero satisfies neither strict comparison.

Therefore, the final `else` handles zero.

### Concepts Used

- Integer input.
- If-elif-else.
- Comparison operators.

---

## Problem 2: Classify a Decimal Number

### Problem Statement

Accept a decimal number and classify it as positive, negative, or zero.

### Logic

1. Accept a floating-point value.
2. Compare it with zero.
3. Display the appropriate classification.

### Code

```python
number = float(input("Enter a decimal number: "))

if number > 0:
    result = "Positive"
elif number < 0:
    result = "Negative"
else:
    result = "Zero"

print("Number:", number)
print("Classification:", result)
```

### Sample Input

```text
Enter a decimal number: -12.75
```

### Expected Output

```text
Number: -12.75
Classification: Negative
```

### Explanation

The `float()` function converts the input into a floating-point value.

The comparison operators work with floating-point numbers as well as integers.

Since the number is smaller than zero, it is classified as negative.

### Concepts Used

- Float conversion.
- Comparison operators.
- If-elif-else.

---

## Problem 3: Check Zero

### Problem Statement

Accept a number and check whether it is zero or not.

### Logic

1. Read a number.
2. Compare it with zero using `==`.
3. Display the result.

### Code

```python
number = float(input("Enter a number: "))

if number == 0:
    result = "Zero"
else:
    result = "Not zero"

print("Result:", result)
```

### Sample Input

```text
Enter a number: 0
```

### Expected Output

```text
Result: Zero
```

### Explanation

The equality operator checks whether the number is exactly equal to zero.

A value other than zero enters the `else` block.

### Concepts Used

- Equality comparison.
- If-else.
- Numeric input.

---

## Problem 4: Positive or Non-Positive

### Problem Statement

Accept a number and classify it as positive or non-positive.

A non-positive number is either zero or negative.

### Logic

1. Accept a number.
2. Check whether it is greater than zero.
3. If true, classify it as positive.
4. Otherwise, classify it as non-positive.

### Code

```python
number = float(input("Enter a number: "))

result = "Positive" if number > 0 else "Non-positive"

print("Number:", number)
print("Result:", result)
```

### Sample Input

```text
Enter a number: 0
```

### Expected Output

```text
Number: 0.0
Result: Non-positive
```

### Explanation

Zero is not positive.

Therefore, zero belongs to the non-positive category.

This problem demonstrates how the same condition can be used with a different classification rule.

### Concepts Used

- Conditional expression.
- Greater-than operator.
- Non-positive classification.

---

## Problem 5: Positive Even or Odd

### Problem Statement

Accept an integer.

First check whether it is positive.

If positive, determine whether it is even or odd.

### Logic

1. Accept an integer.
2. Check whether it is greater than zero.
3. If positive, check the remainder after division by two.
4. Display even or odd.
5. If the number is not positive, display an appropriate message.

### Code

```python
number = int(input("Enter an integer: "))

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")
```

### Sample Input 1

```text
Enter an integer: 12
```

### Expected Output 1

```text
Positive even number
```

### Sample Input 2

```text
Enter an integer: 15
```

### Expected Output 2

```text
Positive odd number
```

### Explanation

The outer condition checks whether the number is positive.

The inner condition checks whether it is even.

This is an example of dependent decision-making.

### Concepts Used

- Nested if.
- Modulus operator.
- Even and odd classification.

---

## Problem 6: Count Positive, Negative and Zero Values

### Problem Statement

Accept multiple numbers and count:

- Positive numbers.
- Negative numbers.
- Zero values.

### Logic

1. Accept the number of values.
2. Read each number.
3. Initialize three counters.
4. Use a loop to process each value.
5. Increase the appropriate counter.
6. Display the counts.

### Code

```python
count = int(input("How many numbers? "))

positive_count = 0
negative_count = 0
zero_count = 0

for index in range(count):
    number = float(input(f"Enter number {index + 1}: "))

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
```

### Sample Input

```text
How many numbers? 5
Enter number 1: 10
Enter number 2: -5
Enter number 3: 0
Enter number 4: 20
Enter number 5: -8
```

### Expected Output

```text
Positive numbers: 2
Negative numbers: 2
Zeros: 1
```

### Explanation

The program reads five numbers.

It processes each number using the three conditions.

The final counters represent the frequency of each category.

### Concepts Used

- For loop.
- If-elif-else.
- Counter variables.
- Numeric input.

---

## Problem 7: Sum of Positive Numbers

### Problem Statement

Accept multiple numbers and calculate the sum of only the positive numbers.

### Logic

1. Read the total number of inputs.
2. Initialize the sum to zero.
3. Read each number.
4. Check whether it is positive.
5. Add only positive values.
6. Display the sum.

### Code

```python
count = int(input("How many numbers? "))

positive_sum = 0

for index in range(count):
    number = float(input(f"Enter number {index + 1}: "))

    if number > 0:
        positive_sum += number

print("Sum of positive numbers:", positive_sum)
```

### Sample Input

```text
How many numbers? 5
Enter number 1: 10
Enter number 2: -5
Enter number 3: 20
Enter number 4: -8
Enter number 5: 15
```

### Expected Output

```text
Sum of positive numbers: 45.0
```

### Explanation

The positive values are:

```text
10, 20, 15
```

The negative values are ignored.

Calculation:

\[
10 + 20 + 15 = 45
\]

### Concepts Used

- For loop.
- If condition.
- Accumulator variable.
- Addition.

---

## Problem 8: Find the First Positive Number

### Problem Statement

Accept multiple numbers and find the first positive number.

### Logic

1. Accept a collection of numbers.
2. Initialize a variable with `None`.
3. Examine each number in order.
4. If a positive number is found, store it.
5. Stop the loop using `break`.
6. Display the first positive value.

### Code

```python
numbers = [ -5, -2, 0, 8, 10 ]

first_positive = None

for number in numbers:
    if number > 0:
        first_positive = number
        break

if first_positive is None:
    print("No positive number found")
else:
    print("First positive number:", first_positive)
```

### Output

```text
First positive number: 8
```

### Explanation

The program examines the list from left to right.

The values `-5`, `-2`, and `0` are not positive.

The value `8` is the first positive number.

The `break` statement stops further searching.

### Concepts Used

- Lists.
- For loop.
- If statement.
- `break`.
- `None`.

---

## Problem 9: Filter Positive Numbers

### Problem Statement

Accept multiple numbers and create a new list containing only positive numbers.

### Logic

1. Accept numbers.
2. Create an empty list.
3. Traverse the original list.
4. Check whether each value is positive.
5. Append positive values to the new list.
6. Display the new list.

### Code

```python
numbers = [10, -5, 0, 20, -8, 15]

positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print("Original list:", numbers)
print("Positive numbers:", positive_numbers)
```

### Output

```text
Original list: [10, -5, 0, 20, -8, 15]
Positive numbers: [10, 20, 15]
```

### Explanation

The original list contains positive values, negative values, and zero.

The program creates a second list.

Only values greater than zero are appended.

The original list remains unchanged.

### Concepts Used

- Lists.
- For loop.
- If condition.
- `append()` method.
- Filtering.

---

## Problem 10: Largest Positive Number

### Problem Statement

Find the largest positive number in a collection.

If no positive number exists, display an appropriate message.

### Logic

1. Accept multiple numbers.
2. Initialize the largest positive value as `None`.
3. Traverse the collection.
4. Ignore values that are zero or negative.
5. If a positive value is found, compare it with the current largest value.
6. Update the largest value when necessary.
7. Display the answer.

### Code

```python
numbers = [-10, 5, -3, 20, 8, 0]

largest_positive = None

for number in numbers:
    if number > 0:
        if largest_positive is None or number > largest_positive:
            largest_positive = number

if largest_positive is None:
    print("No positive number found")
else:
    print("Largest positive number:", largest_positive)
```

### Output

```text
Largest positive number: 20
```

### Explanation

The program ignores negative numbers and zero.

It compares every positive value with the currently stored maximum.

When a larger positive number appears, the variable is updated.

### Concepts Used

- Nested if.
- List traversal.
- Comparison operators.
- Maximum selection.
- `None`.

---

## Problem 11: Positive Input Validation

### Problem Statement

Write a program that keeps asking the user for a number until a positive number is entered.

### Logic

1. Start an infinite loop.
2. Accept a number.
3. Check whether it is greater than zero.
4. If positive, display it and stop the loop.
5. Otherwise, display an error message and ask again.

### Code

```python
while True:
    number = float(input("Enter a positive number: "))

    if number > 0:
        print("Valid positive number:", number)
        break
    else:
        print("Invalid input. Enter a number greater than zero.")
```

### Sample Input

```text
Enter a positive number: -5
Invalid input. Enter a number greater than zero.

Enter a positive number: 0
Invalid input. Enter a number greater than zero.

Enter a positive number: 12
Valid positive number: 12.0
```

### Explanation

The loop continues until the user enters a value greater than zero.

Zero is rejected because it is not positive.

The `break` statement ends the loop when valid input is received.

### Concepts Used

- While loop.
- If-else.
- Input validation.
- Break statement.

---

## Problem 12: Compare Number Signs

### Problem Statement

Accept two numbers and compare their sign categories.

Classify each number as positive, negative, or zero.

Then determine whether both numbers belong to the same category.

### Logic

1. Accept the first number.
2. Accept the second number.
3. Classify both numbers.
4. Compare the classification results.
5. Display whether the categories match.

### Code

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if first > 0:
    first_sign = "Positive"
elif first < 0:
    first_sign = "Negative"
else:
    first_sign = "Zero"

if second > 0:
    second_sign = "Positive"
elif second < 0:
    second_sign = "Negative"
else:
    second_sign = "Zero"

print("First number:", first_sign)
print("Second number:", second_sign)

if first_sign == second_sign:
    print("Both numbers have the same sign category")
else:
    print("The numbers have different sign categories")
```

### Sample Input

```text
Enter first number: -10
Enter second number: -25
```

### Expected Output

```text
First number: Negative
Second number: Negative
Both numbers have the same sign category
```

### Explanation

The program classifies each value separately.

Then it compares the two classification strings.

Both values are negative, so their categories match.

### Concepts Used

- If-elif-else.
- String comparison.
- Multiple conditions.
- Numeric classification.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try to solve these problems yourself.

Use the concepts learned in this topic.

Do not directly copy the solved programs.

## Question 1: Classify Multiple Numbers

### Problem Statement

Accept multiple numbers from the user.

Classify each number as:

- Positive.
- Negative.
- Zero.

### Requirements

- Ask how many numbers the user wants to enter.
- Read each value.
- Check each value.
- Display the classification.

### Concepts to Use

- For loop.
- If-elif-else.
- Input.
- Comparison operators.

---

## Question 2: Count Positive and Negative Numbers

### Problem Statement

Accept a collection of numbers and count positive and negative values separately.

### Requirements

- Accept multiple numbers.
- Initialize positive and negative counters.
- Check each value.
- Increase the appropriate counter.
- Display the counts.

### Concepts to Use

- Lists.
- Loops.
- Counter variables.
- Conditional statements.

---

## Question 3: Average of Positive Numbers

### Problem Statement

Calculate the average of positive numbers in a collection.

### Requirements

- Accept multiple numbers.
- Add only positive values.
- Count the positive values.
- Calculate the average.
- Handle the case where no positive values exist.

### Concepts to Use

- For loop.
- If statement.
- Accumulator.
- Counter.
- Division.

---

## Question 4: Smallest Negative Number

### Problem Statement

Find the smallest negative number in a collection.

### Requirements

- Accept multiple values.
- Ignore positive values.
- Ignore zero.
- Compare negative values.
- Find the smallest negative value.
- Display an appropriate message if there are no negative numbers.

### Concepts to Use

- Lists.
- Conditional statements.
- Comparison operators.
- Minimum selection.

---

## Question 5: Positive Even Numbers

### Problem Statement

Display only positive even integers from a collection.

### Requirements

- Accept a list of integers.
- Check whether each number is positive.
- Check whether it is even.
- Display all values satisfying both conditions.

### Concepts to Use

- Lists.
- For loop.
- Nested if.
- Modulus operator.

---

## Question 6: Negative Odd Numbers

### Problem Statement

Display all negative odd integers in a collection.

### Requirements

- Accept a list of integers.
- Check whether a number is negative.
- Check whether it is odd.
- Display the selected values.

### Concepts to Use

- If statements.
- Nested conditions.
- Modulus operator.
- Lists.

---

## Question 7: First Negative Number

### Problem Statement

Find the first negative value in a collection.

Also display its position.

### Requirements

- Accept multiple numbers.
- Traverse the collection from beginning to end.
- Check for a negative value.
- Store its position.
- Stop searching after finding the first negative number.

### Concepts to Use

- Lists.
- Loop.
- If statement.
- `break`.
- Index tracking.

---

## Question 8: Count Zeros

### Problem Statement

Accept multiple numbers and count how many values are exactly zero.

### Requirements

- Accept the number of values.
- Read each value.
- Check whether it equals zero.
- Increase the zero counter.
- Display the final count.

### Concepts to Use

- Equality operator.
- For loop.
- Counter variable.

---

## Question 9: Positive Range Check

### Problem Statement

Accept a number and check whether it is positive and within a specified range.

### Requirements

- Accept a numeric value.
- Check whether the value is greater than zero.
- Check whether it belongs to the selected range.
- Display the result.

### Concepts to Use

- Comparison operators.
- Logical operators.
- Nested if.
- Range checking.

---

## Question 10: Compare Signs

### Problem Statement

Accept three numbers.

Count how many are positive, negative, and zero.

### Requirements

- Accept three numbers.
- Initialize three counters.
- Classify all three values.
- Display positive count.
- Display negative count.
- Display zero count.

### Concepts to Use

- If-elif-else.
- Comparison operators.
- Counter variables.
- Multiple input values.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Treating Zero as Positive

Incorrect:

```python
number = 0

if number >= 0:
    print("Positive")
```

The condition is true for zero.

However, zero is not a positive number.

Correct:

```python
if number > 0:
    print("Positive")
```

If you want to classify positive, negative, and zero values, use:

```python
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## Mistake 2: Using `>` Instead of `>=`

These conditions are different:

```python
number > 0
number >= 0
```

The first excludes zero.

The second includes zero.

Choose the operator according to the required classification.

## Mistake 3: Using Assignment Instead of Equality

Incorrect:

```python
if number = 0:
    print("Zero")
```

Correct:

```python
if number == 0:
    print("Zero")
```

The equality operator is `==`.

## Mistake 4: Forgetting Negative Values

A program should handle both positive and negative inputs.

Do not test a program using only positive numbers.

## Mistake 5: Ignoring Zero

Zero is an important special case.

A number-classification program should handle zero separately whenever all three categories are required.

## Mistake 6: Confusing Positive and Non-Negative

Positive:

```python
number > 0
```

Non-negative:

```python
number >= 0
```

Zero belongs to the non-negative category but not to the positive category.

## Mistake 7: Incorrect Even-Odd Logic

Correct even condition:

```python
number % 2 == 0
```

Correct odd condition:

```python
number % 2 != 0
```

Do not use division `/` when the goal is to check the remainder.

## Mistake 8: Ignoring Negative Even and Odd Numbers

Negative integers can also be even or odd.

Examples:

- `-2` is even.
- `-4` is even.
- `-3` is odd.
- `-7` is odd.

## Mistake 9: Incorrect Counter Initialization

A counter should normally start at zero.

Correct:

```python
positive_count = 0
negative_count = 0
zero_count = 0
```

## Mistake 10: Not Updating the Counter

Incorrect:

```python
if number > 0:
    positive_count = 1
```

This does not correctly count multiple positive numbers because the variable is repeatedly set to one.

Correct:

```python
if number > 0:
    positive_count += 1
```

## Mistake 11: Forgetting to Handle an Empty Result

A program searching for a positive number should handle the case where no positive number exists.

## Mistake 12: Incorrect Largest-Value Logic

When searching for the largest positive number, negative values and zero should not become the selected result.

Use an appropriate initial value or a separate found-value indicator.

## Mistake 13: Using the Wrong Data Type

The `input()` function returns text.

Convert it to an integer or float before numeric comparisons.

## Mistake 14: Not Validating User Input

Invalid text cannot be directly converted into a number.

Use `try-except` where needed.

## Mistake 15: Forgetting That Floating-Point Values Exist

Classification should work for decimal numbers as well as integers.

For example:

```python
-0.25
0.0
0.25
```

These should be classified as negative, zero, and positive respectively.

---

# SECTION 5: BEST PRACTICES

Follow these guidelines when solving positive and negative number problems.

1. Use meaningful variable names.
2. Choose comparison operators carefully.
3. Treat zero as a separate category when required.
4. Use `if-elif-else` for three-way classification.
5. Use `>` for strictly positive values.
6. Use `<` for strictly negative values.
7. Use `>=` for non-negative values.
8. Use `<=` for non-positive values.
9. Validate user input.
10. Convert input to the correct numeric type.
11. Test both positive and negative values.
12. Test zero explicitly.
13. Test decimal values when required.
14. Use separate counters for different categories.
15. Initialize counters to zero.
16. Use accumulator variables for sums.
17. Use `None` when no valid result has been found yet.
18. Use `break` when a search should stop at the first match.
19. Avoid repeating classification logic unnecessarily.
20. Use functions for reusable logic.
21. Keep nested conditions readable.
22. Handle cases where no qualifying value exists.
23. Do not confuse positive with non-negative.
24. Do not confuse negative with non-positive.
25. Keep the program output clear.

### Good Example

```python
number = -15

if number > 0:
    result = "Positive"
elif number < 0:
    result = "Negative"
else:
    result = "Zero"

print("Classification:", result)
```

### Reusable Function

```python
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


print(classify_number(15))
print(classify_number(-5))
print(classify_number(0))
```

Output:

```text
Positive
Negative
Zero
```

A reusable function is helpful when the same classification logic is needed in multiple parts of a program.

---

# SECTION 6: DEBUGGING

Debugging means identifying and correcting errors in a program.

Number-classification programs are useful for learning debugging because small mistakes in comparison operators can produce incorrect results.

## 1. Check the Comparison Operator

If zero is printed as positive, check whether the program uses:

```python
number >= 0
```

when it should use:

```python
number > 0
```

## 2. Check the Input Conversion

Incorrect:

```python
number = input("Enter number: ")

if number > 0:
    print("Positive")
```

The input is a string.

Correct:

```python
number = float(input("Enter number: "))

if number > 0:
    print("Positive")
```

## 3. Check Zero Handling

Make sure the program contains an appropriate zero condition.

## 4. Check Counter Updates

For counting values, use:

```python
count += 1
```

when a matching value is found.

## 5. Check the Initial Value

When finding the largest positive number, make sure negative values cannot become the initial result.

A suitable approach is:

```python
largest_positive = None
```

Then update it only when a positive number is found.

## 6. Check Loop Conditions

When processing a list, make sure the loop examines every element.

## 7. Check Break Statements

Use `break` only when the required search is complete.

For example, when finding the first positive number, stopping after the first match is correct.

When counting every positive number, stopping after the first match would be incorrect.

## 8. Common Python Errors

| Error | Meaning |
|---|---|
| `ValueError` | Input cannot be converted to the requested numeric type |
| `TypeError` | An operation uses incompatible types |
| `NameError` | A variable name is not defined |
| `IndentationError` | Incorrect indentation |
| `SyntaxError` | Invalid Python syntax |

## 9. Debugging Checklist

Before deciding that a program is correct, confirm:

- The input is numeric.
- The input conversion is correct.
- The correct comparison operator is used.
- Zero is handled.
- Negative values are handled.
- Decimal values are handled when required.
- Counters are initialized correctly.
- Accumulators are updated correctly.
- Search operations handle missing values.
- All required collection elements are processed.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Positive and negative number classification is used in many real-world software systems.

## 1. Banking Applications

A banking application may use positive and negative values to represent account transactions.

For example:

- Positive amount: Money credited.
- Negative amount: Money debited.
- Zero: No transaction amount.

Example:

```python
transaction = -500

if transaction > 0:
    print("Money credited")
elif transaction < 0:
    print("Money debited")
else:
    print("No transaction")
```

## 2. Shopping Applications

An online shopping system may use numeric values to calculate profit or loss.

Example:

```python
profit = -200

if profit > 0:
    print("Profit")
elif profit < 0:
    print("Loss")
else:
    print("No profit or loss")
```

## 3. Temperature Applications

Temperature measurements can be positive, negative, or zero.

Example:

```python
temperature = -5

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    print("Below zero")
else:
    print("Exactly zero")
```

## 4. Inventory Management

A stock-adjustment system may use positive and negative quantities.

- Positive adjustment: Stock increased.
- Negative adjustment: Stock decreased.
- Zero adjustment: No change.

## 5. Employee Salary Systems

A payroll system may calculate salary differences.

- Positive difference: Salary increased.
- Negative difference: Salary decreased.
- Zero difference: No change.

## 6. Student Result Systems

A student management application may compare marks, scores, or performance differences.

Positive values can represent an increase in marks.

Negative values can represent a decrease.

## 7. Data Analysis

Data analysts frequently classify numerical values according to whether they are above or below a reference point.

For example, a change in monthly sales can be positive or negative.

## 8. Financial Applications

Financial software can use sign classification to identify gains and losses.

## 9. Sensor Applications

Sensors may return measurements that are positive, negative, or zero relative to a reference level.

## 10. Scientific Applications

Scientific calculations frequently use negative and positive values for position, displacement, and measurements.

---

# SECTION 8: DSA CONNECTION

Positive and negative number problems help build the logical thinking required for Data Structures and Algorithms.

The concepts used in this topic appear in searching, sorting, arrays, lists, and mathematical problems.

## 1. Arrays

An array can contain positive numbers, negative numbers, and zero.

Example:

```python
numbers = [10, -5, 0, 20, -8]
```

You can traverse the array and classify each element.

## 2. Searching

A search algorithm may look for the first positive number.

Example:

```python
numbers = [-5, -2, 0, 8, 10]

for number in numbers:
    if number > 0:
        print("Found:", number)
        break
```

## 3. Filtering

Filtering means selecting elements that satisfy a condition.

For example, selecting positive values:

```python
numbers = [10, -5, 0, 20, -8]

positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print(positive_numbers)
```

## 4. Counting

Counting positive and negative values is a basic array traversal problem.

## 5. Maximum and Minimum

Finding the largest positive value introduces the concept of maintaining a current maximum.

## 6. Accumulator Problems

Calculating the sum of positive numbers is an example of an accumulator-based problem.

## 7. Conditional Logic

Every loop-based DSA problem uses conditions to decide what operation should be performed.

### DSA Skills Developed

- Array traversal.
- List traversal.
- Searching.
- Filtering.
- Counting.
- Summation.
- Maximum and minimum selection.
- Conditional logic.
- Input validation.
- Problem decomposition.

### Important Practice

When learning DSA, do not only memorize the Python code.

Understand:

- Why the condition exists.
- When the condition becomes true.
- Why a variable is updated.
- Why a loop stops.
- How every input value is processed.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Time and space complexity help measure the efficiency of a program.

## 1. Classifying One Number

Consider:

```python
number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

The program checks a fixed number of conditions.

Therefore, its time complexity is:

\[
O(1)
\]

The program uses a constant amount of additional memory.

Its additional space complexity is:

\[
O(1)
\]

## 2. Counting Positive and Negative Values

Consider:

```python
numbers = [10, -5, 0, 20, -8]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1
```

The loop visits every element once.

For `n` values, the time complexity is:

\[
O(n)
\]

The program uses a fixed number of counters.

Its additional space complexity is:

\[
O(1)
\]

## 3. Sum of Positive Numbers

The sum program also examines every element.

Its time complexity is:

\[
O(n)
\]

Its additional space complexity is:

\[
O(1)
\]

## 4. Find First Positive Number

In the best case, the first element is positive.

In the worst case, the algorithm checks every element.

Best-case time complexity:

\[
O(1)
\]

Worst-case time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 5. Filter Positive Numbers

The filtering program checks every element and may create a new list containing positive values.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(n)
\]

The new list may contain all elements in the worst case.

## 6. Largest Positive Number

The largest-positive-number program examines all elements.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

### Complexity Summary

| Problem | Time Complexity | Additional Space |
|---|---:|---:|
| Classify one number | \(O(1)\) | \(O(1)\) |
| Count number categories | \(O(n)\) | \(O(1)\) |
| Sum positive numbers | \(O(n)\) | \(O(1)\) |
| Find first positive | Best \(O(1)\), worst \(O(n)\) | \(O(1)\) |
| Filter positive numbers | \(O(n)\) | \(O(n)\) |
| Find largest positive | \(O(n)\) | \(O(1)\) |

---

# SECTION 10: MINI PROJECT – NUMBER CLASSIFICATION SYSTEM

## Project Overview

Create a simple number-classification program.

The program accepts multiple numbers and displays:

1. Positive numbers.
2. Negative numbers.
3. Zero values.
4. Count of positive numbers.
5. Count of negative numbers.
6. Count of zero values.
7. Sum of positive numbers.
8. Largest positive number.

This project combines the main concepts from this topic.

## Python Code

```python
numbers = []

count = int(input("How many numbers do you want to enter? "))

for index in range(count):
    number = float(input(f"Enter number {index + 1}: "))
    numbers.append(number)

positive_numbers = []
negative_numbers = []
zero_numbers = []

positive_sum = 0
largest_positive = None

for number in numbers:

    if number > 0:
        positive_numbers.append(number)
        positive_sum += number

        if largest_positive is None or number > largest_positive:
            largest_positive = number

    elif number < 0:
        negative_numbers.append(number)

    else:
        zero_numbers.append(number)

print("\nNUMBER CLASSIFICATION REPORT")
print("=" * 40)

print("Original numbers:", numbers)

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Zero values:", zero_numbers)

print("Positive count:", len(positive_numbers))
print("Negative count:", len(negative_numbers))
print("Zero count:", len(zero_numbers))

print("Sum of positive numbers:", positive_sum)

if largest_positive is None:
    print("Largest positive number: Not found")
else:
    print("Largest positive number:", largest_positive)
```

## Sample Output

```text
How many numbers do you want to enter? 6

Enter number 1: 10
Enter number 2: -5
Enter number 3: 0
Enter number 4: 20
Enter number 5: -8
Enter number 6: 15

NUMBER CLASSIFICATION REPORT
========================================
Original numbers: [10.0, -5.0, 0.0, 20.0, -8.0, 15.0]

Positive numbers: [10.0, 20.0, 15.0]
Negative numbers: [-5.0, -8.0]
Zero values: [0.0]

Positive count: 3
Negative count: 2
Zero count: 1

Sum of positive numbers: 45.0
Largest positive number: 20.0
```

## Project Explanation

The program first accepts a collection of numbers.

It creates three lists:

- `positive_numbers`
- `negative_numbers`
- `zero_numbers`

Each value is classified using an `if-elif-else` structure.

Positive values are stored and added to the positive sum.

Negative values are stored in the negative list.

Zero values are stored separately.

The program also maintains the largest positive value.

Finally, it displays a classification report.

## Project Improvements

After completing the basic project, try these improvements:

1. Add an option to classify another collection.
2. Display positive even numbers.
3. Display negative odd numbers.
4. Calculate the sum of negative values.
5. Calculate the average of positive values.
6. Find the smallest negative value.
7. Sort positive values.
8. Sort negative values.
9. Create functions for each operation.
10. Add an interactive menu.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is a positive number?

A number greater than zero.

### 2. What is a negative number?

A number less than zero.

### 3. What is zero?

Zero is neither positive nor negative.

### 4. Which operator checks whether a number is positive?

The greater-than operator `>`.

### 5. Which condition checks whether a number is negative?

`number < 0`.

### 6. How do you check whether a number is zero?

Use `number == 0`.

### 7. What is a non-negative number?

A number greater than or equal to zero.

### 8. What is a non-positive number?

A number less than or equal to zero.

### 9. Is zero positive?

No.

### 10. Is zero negative?

No.

## Intermediate Questions

### 11. Which conditional structure is suitable for classifying positive, negative, and zero values?

`if-elif-else`.

### 12. What is the difference between `>` and `>=`?

`>` excludes equality, while `>=` includes equality.

### 13. Can decimal numbers be positive or negative?

Yes.

### 14. Can negative integers be even?

Yes. For example, `-4` is even.

### 15. Can negative integers be odd?

Yes. For example, `-7` is odd.

### 16. How do you check whether a number is even?

Use `number % 2 == 0`.

### 17. How do you check whether a number is odd?

Use `number % 2 != 0`.

### 18. What is the modulus operator?

It returns the remainder after division.

### 19. Which function can convert input to an integer?

`int()`.

### 20. Which function can convert input to a floating-point number?

`float()`.

## Practical Questions

### 21. How do you count positive numbers in a list?

Use a loop and increase a counter whenever a number is greater than zero.

### 22. How do you count negative numbers?

Increase a counter whenever a number is less than zero.

### 23. How do you count zeros?

Increase a counter whenever a number is equal to zero.

### 24. How do you find the sum of positive numbers?

Initialize a sum variable and add only values greater than zero.

### 25. How do you find the first positive number?

Traverse the collection and stop when a positive number is found.

### 26. What does `break` do?

It immediately terminates the nearest enclosing loop.

### 27. What is `None` in Python?

It is a special value representing the absence of a value.

### 28. How can you filter positive numbers?

Create a new list and append values that are greater than zero.

### 29. How do you find the largest positive number?

Maintain a current maximum and update it whenever a larger positive value is found.

### 30. Why should zero be checked separately?

Because zero is neither positive nor negative.

## Advanced Questions

### 31. What is the time complexity of classifying one number?

`O(1)`.

### 32. What is the time complexity of counting positive numbers in a list?

`O(n)`.

### 33. What is the time complexity of summing positive numbers?

`O(n)`.

### 34. What is the time complexity of filtering positive values?

`O(n)`.

### 35. What is the additional space complexity of filtering positive values?

`O(n)` in the worst case because a new list may contain all values.

### 36. What is the additional space complexity of counting values?

`O(1)`.

### 37. Why is a largest-value variable sometimes initialized as `None`?

It represents that no qualifying positive value has been found yet.

### 38. What is input validation?

Checking whether input satisfies the required rules before using it.

### 39. What error can occur when invalid text is converted to an integer?

`ValueError`.

### 40. Why should floating-point inputs be checked for finiteness?

Because values such as infinity and NaN are not ordinary finite numeric values and can behave unexpectedly in comparisons.

## Interview-Oriented Questions

### 41. How would you classify a number as positive, negative, or zero?

Use `if-elif-else` with comparisons against zero.

### 42. How would you count positive and negative values in one loop?

Use separate counters and classify each value during a single traversal.

### 43. How would you find the first negative element in an array?

Traverse the array and stop when the first negative value is found.

### 44. How would you find the largest positive number without sorting?

Maintain a current maximum and update it while traversing the collection.

### 45. Why is sorting unnecessary for finding the largest positive value?

A single traversal can identify the maximum in linear time.

### 46. What happens when a list contains no positive values?

A largest-positive search should report that no qualifying value exists.

### 47. How can you avoid confusing zero with negative values?

Use three separate conditions: greater than zero, less than zero, and otherwise zero.

### 48. Why is the condition `number >= 0` not a positive-number check?

Because it also includes zero.

### 49. What is the benefit of writing a classification function?

It allows the same logic to be reused throughout the program.

### 50. Why is positive and negative number classification important for DSA?

It builds experience with conditions, comparisons, arrays, searching, filtering, and counting.

---

# SECTION 12: QUICK REVISION NOTES

## Main Rules

Positive:

\[
n > 0
\]

Negative:

\[
n < 0
\]

Zero:

\[
n = 0
\]

Non-negative:

\[
n \geq 0
\]

Non-positive:

\[
n \leq 0
\]

## Important Python Conditions

```python
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

## Positive or Non-Positive

```python
result = "Positive" if number > 0 else "Non-positive"
```

## Non-Negative Check

```python
result = "Non-negative" if number >= 0 else "Negative"
```

## Even or Odd

```python
result = "Even" if number % 2 == 0 else "Odd"
```

## Count Positive Numbers

```python
positive_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
```

## Sum Positive Numbers

```python
positive_sum = 0

for number in numbers:
    if number > 0:
        positive_sum += number
```

## Find First Positive Number

```python
first_positive = None

for number in numbers:
    if number > 0:
        first_positive = number
        break
```

## Important Operators

| Operator | Purpose |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `==` | Equal to |
| `!=` | Not equal to |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `%` | Modulus |
| `+=` | Add and assign |

## Important Concepts

- Zero is neither positive nor negative.
- Negative integers can be even or odd.
- A decimal value can also be positive or negative.
- Use `if-elif-else` for three-way classification.
- Use counters to count values.
- Use accumulators to calculate sums.
- Use `break` to stop searching after finding a required value.
- Use `None` when no qualifying result has been found.
- Use loops when processing multiple values.
- Use functions when the same logic is needed repeatedly.

---

# SECTION 13: LEARNING CHECKLIST

- [ ] I understand what positive numbers are.
- [ ] I understand what negative numbers are.
- [ ] I understand that zero is neither positive nor negative.
- [ ] I can identify positive integers.
- [ ] I can identify negative integers.
- [ ] I can identify zero.
- [ ] I can classify positive, negative, and zero values.
- [ ] I understand the difference between positive and non-negative.
- [ ] I understand the difference between negative and non-positive.
- [ ] I can use greater-than and less-than operators.
- [ ] I can use the equality operator.
- [ ] I can classify decimal numbers.
- [ ] I can check whether positive numbers are even or odd.
- [ ] I can check whether negative numbers are even or odd.
- [ ] I can count positive values in a list.
- [ ] I can count negative values in a list.
- [ ] I can count zeros in a list.
- [ ] I can calculate the sum of positive numbers.
- [ ] I can find the first positive number.
- [ ] I can filter positive values.
- [ ] I can find the largest positive number.
- [ ] I can validate positive input.
- [ ] I can compare number-sign categories.
- [ ] I can work with loops and lists.
- [ ] I understand the time complexity of basic problems.
- [ ] I understand the space complexity of basic problems.
- [ ] I can explain the topic in an interview.
- [ ] I have attempted all ten unsolved questions.
- [ ] I understand the connection with DSA.

---

# SECTION 14: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `01-positive-negative` folder.

Run:

```bash
python 01_positive_negative.py
```

On Windows, you can also run:

```powershell
py 01_positive_negative.py
```

The program displays an interactive menu.

## Main Menu

```text
=================================================================
                  PYTHON: POSITIVE AND NEGATIVE NUMBERS
=================================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

This option displays all twelve examples.

The examples include:

1. Positive number.
2. Negative number.
3. Zero check.
4. Positive, negative, or zero.
5. Positive or non-positive.
6. Non-negative number.
7. Positive even or odd.
8. Negative even or odd.
9. Count number categories.
10. Sum positive numbers.
11. Find first positive.
12. Decimal number classification.

### Option 2 – Practice 12 Solved Problems

This option displays a list of solved problems.

Choose a problem number to execute it.

The program accepts input and displays the result.

### Option 3 – View 10 Unsolved Questions

This option displays ten independent practice problems.

Attempt them yourself.

### Option 4 – Learning Checklist

This option displays the learning checklist.

Use it to check whether you understand each concept.

### Option 0 – Exit

This option closes the program.

---

# SECTION 15: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 06-Practice-Problems/
            └── 01-positive-negative/
                ├── README.md
                └── 01_positive_negative.py
```

### File Details

| File | Purpose |
|---|---|
| `README.md` | Complete topic explanation, examples, solved problems, unsolved questions, and revision notes |
| `01_positive_negative.py` | Python program containing examples, solved problems, practice questions, checklist, and menu |

### Previous Topic

**05-Conditional-Expressions**

In the previous topic, you learned how to use conditional expressions to select values based on conditions.

### Current Topic

**01-positive-negative**

In this topic, you are applying conditional statements to number-classification problems.

### Next Topic

**02-even-odd**

In the next problem, you will work on even and odd number classification in greater detail.

---

# FINAL SUMMARY

Positive and negative number classification is a basic but important programming concept.

It helps you understand how a program makes decisions based on numerical comparisons.

After completing this topic, you should be able to:

1. Identify positive numbers.
2. Identify negative numbers.
3. Identify zero.
4. Classify integers and decimal numbers.
5. Understand positive and non-negative values.
6. Understand negative and non-positive values.
7. Check positive and negative even-odd numbers.
8. Count positive, negative, and zero values.
9. Calculate the sum of positive values.
10. Find the first positive value.
11. Filter positive values from a list.
12. Find the largest positive number.
13. Validate positive input.
14. Apply number classification in practical programs.
15. Understand the connection with arrays, searching, and DSA.

### Final Advice

Do not memorize the classification code only.

Understand why a number greater than zero is positive, why a number less than zero is negative, and why zero must be handled separately.

Practise using integers, decimal values, lists, and user input.

Once you understand this problem, you will find it easier to solve even-odd problems, number filtering problems, counting problems, and many beginner-level DSA questions.

**Keep practising and maintain the same folder structure throughout your Python learning journey.**

