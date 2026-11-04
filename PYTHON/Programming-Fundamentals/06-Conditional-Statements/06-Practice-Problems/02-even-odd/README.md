

# Python Even and Odd Numbers – Complete Learning Guide

## 1. Introduction

Even and odd numbers are basic mathematical concepts that are frequently used in programming.

In Python, we can identify whether an integer is even or odd using the modulus operator `%`.

An even number is divisible by 2 without leaving any remainder.

An odd number is not divisible by 2 without leaving a remainder.

For example:

**Even numbers:**

```python
2
4
6
8
10
12
14
16
18
20
```

**Odd numbers:**

```python
1
3
5
7
9
11
13
15
17
19
```

Zero is also an even number because it is divisible by 2 without any remainder.

Negative integers can also be even or odd.

For example:

- `-2` is even.
- `-4` is even.
- `-3` is odd.
- `-7` is odd.

### Learning Objectives

After completing this topic, you should be able to:

- Understand even numbers.
- Understand odd numbers.
- Identify zero as an even number.
- Understand the modulus operator.
- Check whether an integer is divisible by two.
- Identify positive even and odd numbers.
- Identify negative even and odd numbers.
- Count even and odd numbers in a collection.
- Calculate the sum of even numbers.
- Calculate the sum of odd numbers.
- Filter even numbers from a list.
- Filter odd numbers from a list.
- Find the first even number in a list.
- Find the largest even number.
- Check divisibility by six.
- Use loops with conditional statements.
- Use lists to solve number problems.
- Apply even-odd logic to DSA problems.

---

## 2. What Is an Even Number?

An even number is an integer that is completely divisible by 2.

When an even number is divided by 2, the remainder is zero.

### Mathematical Representation

\[
n \bmod 2 = 0
\]

### Python Condition

```python
number % 2 == 0
```

If this condition is true, the integer is even.

### Example 1

```python
number = 10

if number % 2 == 0:
    print("Even number")
```

**Output:**

```text
Even number
```

**Explanation:**

The number is 10.

When divided by 2:

\[
10 \div 2 = 5
\]

The remainder is zero.

Therefore, 10 is even.

### Example 2

```python
number = 24

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**Output:**

```text
Even number
```

### Properties of Even Numbers

- Even integers are divisible by 2.
- Their remainder after division by 2 is zero.
- Zero is even.
- Negative even integers are possible.
- Adding two even integers produces an even integer.
- Multiplying an even integer by any integer produces an even integer.

### Examples

| Number | Remainder after division by 2 | Classification |
|---:|---:|---|
| 2 | 0 | Even |
| 4 | 0 | Even |
| 6 | 0 | Even |
| 8 | 0 | Even |
| 10 | 0 | Even |
| 0 | 0 | Even |
| -2 | 0 | Even |
| -4 | 0 | Even |

---

## 3. What Is an Odd Number?

An odd number is an integer that is not completely divisible by 2.

When an odd integer is divided by 2, the remainder is non-zero.

For integers, the remainder in Python's modulo operation is `1` for positive odd values and `-1` for negative odd values when the divisor is positive 2.

The most reliable general condition is:

```python
number % 2 != 0
```

### Mathematical Representation

An odd integer can be represented as:

\[
n = 2k + 1
\]

where \(k\) is an integer.

### Example 1

```python
number = 7

if number % 2 != 0:
    print("Odd number")
```

**Output:**

```text
Odd number
```

### Example 2

```python
number = 15

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**Output:**

```text
Odd number
```

### Properties of Odd Numbers

- Odd integers are not divisible by 2.
- Their remainder is non-zero.
- Negative odd integers are possible.
- Adding two odd integers produces an even integer.
- Adding an even integer and an odd integer produces an odd integer.
- Multiplying two odd integers produces an odd integer.

### Examples

| Number | Classification |
|---:|---|
| 1 | Odd |
| 3 | Odd |
| 5 | Odd |
| 7 | Odd |
| 9 | Odd |
| 11 | Odd |
| -1 | Odd |
| -3 | Odd |
| -5 | Odd |

---

## 4. Understanding the Modulus Operator

The modulus operator `%` is used to calculate the remainder after division.

It is one of the most important operators for solving even-odd problems.

### Syntax

```python
a % b
```

Here:

- `a` is the dividend.
- `b` is the divisor.
- The result is the remainder according to Python's modulo operation.

### Example 1

```python
print(10 % 2)
```

**Output:**

```text
0
```

10 is completely divisible by 2.

### Example 2

```python
print(7 % 2)
```

**Output:**

```text
1
```

7 leaves a remainder of 1.

### Example 3

```python
print(14 % 2)
```

**Output:**

```text
0
```

14 is even.

### Example 4

```python
print(15 % 2)
```

**Output:**

```text
1
```

15 is odd.

### Modulus Table

| Expression | Result |
|---|---:|
| `2 % 2` | 0 |
| `3 % 2` | 1 |
| `4 % 2` | 0 |
| `5 % 2` | 1 |
| `6 % 2` | 0 |
| `7 % 2` | 1 |
| `8 % 2` | 0 |
| `9 % 2` | 1 |
| `10 % 2` | 0 |
| `11 % 2` | 1 |

### Important Python Detail

For negative integers, Python's modulo result follows the sign of the divisor.

For example:

```python
print(-7 % 2)
print(-8 % 2)
```

**Output:**

```text
1
0
```

Therefore, the following conditions work for positive and negative integers:

```python
number % 2 == 0
```

and:

```python
number % 2 != 0
```

Do not assume that every negative odd number produces a remainder of `-1` in Python.

---

## 5. Basic Syntax to Check Even and Odd Numbers

### Using If-Else

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Explanation

The program first calculates:

```python
number % 2
```

Then it compares the remainder with zero.

If the remainder is zero, the number is even.

Otherwise, the number is odd.

### Using a Conditional Expression

```python
result = "Even" if number % 2 == 0 else "Odd"
```

### Using a Function

```python
def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0
```

### Example

```python
number = 12

print(is_even(number))
print(is_odd(number))
```

**Output:**

```text
True
False
```

### Choosing the Correct Method

| Method | Purpose |
|---|---|
| `if-else` | Display different results |
| Conditional expression | Select between two values |
| Function | Reuse even-odd logic |
| Loop with if | Process multiple values |

---

## 6. Is Zero Even or Odd?

Zero is an even number.

This is an important concept because beginners sometimes think zero is neither even nor odd.

An integer is even when it can be written as:

\[
n = 2k
\]

where \(k\) is an integer.

For zero:

\[
0 = 2 \times 0
\]

Therefore, zero satisfies the definition of an even number.

### Python Example

```python
number = 0

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**Output:**

```text
Even number
```

### More Examples

```python
print(0 % 2)
print(-2 % 2)
print(-4 % 2)
```

**Output:**

```text
0
0
0
```

All three values are even.

### Important Points

- Zero is even.
- Zero is not odd.
- Zero is neither positive nor negative.
- Zero passes the even-number condition.
- Zero does not pass the positive-number condition.

---

## 7. Positive and Negative Even-Odd Numbers

Even and odd classification applies to negative integers as well.

The sign of the integer does not determine whether it is even or odd.

The remainder after division by two determines the classification.

### Positive Even Number

```python
number = 12

if number > 0 and number % 2 == 0:
    print("Positive even number")
```

**Output:**

```text
Positive even number
```

### Positive Odd Number

```python
number = 15

if number > 0 and number % 2 != 0:
    print("Positive odd number")
```

**Output:**

```text
Positive odd number
```

### Negative Even Number

```python
number = -12

if number < 0 and number % 2 == 0:
    print("Negative even number")
```

**Output:**

```text
Negative even number
```

### Negative Odd Number

```python
number = -15

if number < 0 and number % 2 != 0:
    print("Negative odd number")
```

**Output:**

```text
Negative odd number
```

### Classification Table

| Number | Sign | Parity |
|---:|---|---|
| 10 | Positive | Even |
| 15 | Positive | Odd |
| 0 | Neither | Even |
| -10 | Negative | Even |
| -15 | Negative | Odd |

### Important Rule

Do not confuse two separate concepts:

- Positive and negative describe a number's sign.
- Even and odd describe an integer's divisibility by two.

A number can be negative and even, or negative and odd.

---

## 8. Even and Odd Numbers Using Loops

Loops are useful when we need to process multiple numbers.

Instead of writing a separate condition for every number, a loop can process all values.

### Using a For Loop

```python
for number in range(1, 11):
    if number % 2 == 0:
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

### Explanation

The `range(1, 11)` function generates integers from 1 to 10.

The loop checks each number.

Only numbers satisfying the even condition are printed.

### Printing Odd Numbers

```python
for number in range(1, 11):
    if number % 2 != 0:
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

### Using a While Loop

```python
number = 1

while number <= 10:
    if number % 2 == 0:
        print(number)

    number += 1
```

**Output:**

```text
2
4
6
8
10
```

### Important Points

- A `for` loop is useful when the iteration range is known.
- A `while` loop is useful when repetition depends on a condition.
- The modulus operator identifies even and odd values.
- A condition inside a loop can filter the numbers.

---

## 9. Counting Even and Odd Numbers

Counting is a common beginner programming problem.

We use two counter variables:

- `even_count`
- `odd_count`

Both start at zero.

### Example

```python
numbers = [10, 15, 20, 25, 30]

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

**Output:**

```text
Even count: 3
Odd count: 2
```

### Explanation

The list contains:

```text
10, 15, 20, 25, 30
```

Even values:

```text
10, 20, 30
```

Odd values:

```text
15, 25
```

Therefore:

- Even count = 3.
- Odd count = 2.

### Important Point

A counter stores how many times a specific condition is satisfied.

The statement:

```python
even_count += 1
```

is equivalent to:

```python
even_count = even_count + 1
```

---

## 10. Sum of Even and Odd Numbers

An accumulator is a variable that stores a running total.

We can use an accumulator to calculate the sum of even or odd values.

### Sum of Even Numbers

```python
numbers = [2, 5, 8, 11, 14]

even_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number

print("Even sum:", even_sum)
```

**Output:**

```text
Even sum: 24
```

The even values are 2, 8, and 14.

Their sum is:

\[
2 + 8 + 14 = 24
\]

### Sum of Odd Numbers

```python
numbers = [1, 4, 7, 10, 13]

odd_sum = 0

for number in numbers:
    if number % 2 != 0:
        odd_sum += number

print("Odd sum:", odd_sum)
```

**Output:**

```text
Odd sum: 21
```

The odd values are 1, 7, and 13.

Their sum is:

\[
1 + 7 + 13 = 21
\]

### Important Difference

A counter increases by one.

An accumulator adds the actual value.

Counter:

```python
count += 1
```

Accumulator:

```python
total += number
```

---

## 11. Filtering Even and Odd Numbers

Filtering means selecting only the elements that satisfy a particular condition.

### Filter Even Numbers

```python
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
```

**Output:**

```text
[10, 20, 30]
```

### Filter Odd Numbers

```python
numbers = [10, 15, 20, 25, 30, 35]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)
```

**Output:**

```text
[15, 25, 35]
```

### Explanation

A new empty list is created.

The loop examines every element in the original list.

Matching values are added to the new list using `append()`.

The original list remains unchanged.

### Using List Comprehension

Even numbers:

```python
even_numbers = [number for number in numbers if number % 2 == 0]
```

Odd numbers:

```python
odd_numbers = [number for number in numbers if number % 2 != 0]
```

List comprehensions are useful when the filtering condition is simple.

---

## 12. Finding Even and Odd Numbers in a List

Searching means finding an element that satisfies a condition.

### First Even Number

```python
numbers = [7, 9, 11, 14, 17, 20]

first_even = None

for number in numbers:
    if number % 2 == 0:
        first_even = number
        break

print(first_even)
```

**Output:**

```text
14
```

### First Odd Number

```python
numbers = [10, 12, 14, 15, 17]

first_odd = None

for number in numbers:
    if number % 2 != 0:
        first_odd = number
        break

print(first_odd)
```

**Output:**

```text
15
```

### Why Use None?

The variable can start with `None` to indicate that no matching number has been found.

If the loop finishes and the variable is still `None`, no matching value exists.

### Why Use Break?

The `break` statement terminates the loop once the first matching value is found.

This avoids unnecessary iterations.

---

## 13. Finding the Largest Even or Odd Number

Finding the largest value is a common array and list problem.

We can combine maximum-value logic with a parity condition.

### Largest Even Number

```python
numbers = [12, 25, 18, 31, 40, 17]

largest_even = None

for number in numbers:
    if number % 2 == 0:
        if largest_even is None or number > largest_even:
            largest_even = number

if largest_even is None:
    print("No even number found")
else:
    print("Largest even number:", largest_even)
```

**Output:**

```text
Largest even number: 40
```

### Largest Odd Number

```python
numbers = [12, 25, 18, 31, 40, 17]

largest_odd = None

for number in numbers:
    if number % 2 != 0:
        if largest_odd is None or number > largest_odd:
            largest_odd = number

if largest_odd is None:
    print("No odd number found")
else:
    print("Largest odd number:", largest_odd)
```

**Output:**

```text
Largest odd number: 31
```

### Important Point

Do not initialize `largest_even` to zero if negative even numbers are possible.

For a list containing only negative even numbers, zero would not be a valid result.

Using `None` avoids that problem.

---

## 14. Divisibility by Two and Six

Even-odd logic is related to divisibility problems.

### Divisibility by Two

An integer is divisible by two when:

```python
number % 2 == 0
```

### Divisibility by Six

An integer is divisible by six when:

```python
number % 6 == 0
```

### Divisible by Both Two and Three

An integer divisible by both 2 and 3 is divisible by 6.

```python
number = 18

if number % 2 == 0 and number % 3 == 0:
    print("Divisible by both 2 and 3")
else:
    print("Not divisible by both")
```

**Output:**

```text
Divisible by both 2 and 3
```

### Divisibility Comparison

| Number | Divisible by 2 | Divisible by 3 | Divisible by 6 |
|---:|---|---|---|
| 6 | Yes | Yes | Yes |
| 8 | Yes | No | No |
| 9 | No | Yes | No |
| 12 | Yes | Yes | Yes |
| 15 | No | Yes | No |
| 18 | Yes | Yes | Yes |

---

## 15. Important Python Methods and Functions

The even-odd problem can be solved using a few useful Python features.

### 15.1 input()

Accepts input from the user.

```python
number = input("Enter number: ")
```

The returned value is a string.

### 15.2 int()

Converts valid integer text into an integer.

```python
number = int(input("Enter number: "))
```

### 15.3 range()

Generates a sequence of integers.

```python
for number in range(1, 11):
    print(number)
```

### 15.4 append()

Adds an item to the end of a list.

```python
even_numbers = []

even_numbers.append(2)
even_numbers.append(4)

print(even_numbers)
```

Output:

```text
[2, 4]
```

### 15.5 len()

Returns the number of items in a collection.

```python
numbers = [2, 4, 6, 8]

print(len(numbers))
```

Output:

```text
4
```

### 15.6 sum()

Calculates the sum of values in an iterable.

```python
numbers = [2, 4, 6]

print(sum(numbers))
```

Output:

```text
12
```

### 15.7 min()

Returns the smallest value.

```python
numbers = [4, 2, 8]

print(min(numbers))
```

Output:

```text
2
```

### 15.8 max()

Returns the largest value.

```python
numbers = [4, 2, 8]

print(max(numbers))
```

Output:

```text
8
```

### Important Note

Built-in functions can simplify some solutions, but it is important to understand the loop and conditional logic first.

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Basic Even Number

### Objective

Check whether an integer is even.

### Code

```python
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Output

```text
Even number
```

### Explanation

The modulus operator calculates the remainder after division by two.

For 10, the remainder is zero.

Therefore, the condition is true and the number is even.

### Concepts Used

- Modulus operator.
- If-else.
- Integer comparison.

---

## Example 2: Basic Odd Number

### Objective

Check whether an integer is odd.

### Code

```python
number = 15

if number % 2 != 0:
    print("Odd number")
else:
    print("Even number")
```

### Output

```text
Odd number
```

### Explanation

The value 15 leaves a remainder of one when divided by two.

Therefore, the condition `number % 2 != 0` is true.

The program displays the odd-number message.

### Concepts Used

- Modulus operator.
- Not-equal operator.
- If-else.

---

## Example 3: Zero Is Even

### Objective

Demonstrate that zero is an even number.

### Code

```python
number = 0

if number % 2 == 0:
    print("Zero is an even number")
else:
    print("Odd number")
```

### Output

```text
Zero is an even number
```

### Explanation

Zero divided by two leaves a remainder of zero.

Therefore, zero is even.

### Concepts Used

- Modulus operator.
- Zero.
- Equality comparison.

---

## Example 4: Positive Even Number

### Objective

Check whether a number is positive and even.

### Code

```python
number = 24

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

The first condition verifies that the number is positive.

The inner condition checks divisibility by two.

Both conditions are satisfied.

### Concepts Used

- Nested if.
- Modulus operator.
- Comparison operators.

---

## Example 5: Negative Odd Number

### Objective

Check whether a negative integer is odd.

### Code

```python
number = -15

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

The outer condition identifies a negative integer.

The inner condition checks whether the remainder after division by two is zero.

For -15, the remainder is non-zero.

Therefore, the number is odd.

### Concepts Used

- Nested if.
- Modulus operator.
- Negative integer classification.

---

## Example 6: Negative Even Number

### Objective

Check whether a negative integer is even.

### Code

```python
number = -20

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
Negative even number
```

### Explanation

-20 is less than zero.

It is also divisible by two.

Therefore, it is a negative even number.

### Concepts Used

- Nested if.
- Comparison operators.
- Modulus operator.

---

## Example 7: Even Numbers in a Range

### Objective

Display even numbers between 1 and 20.

### Code

```python
start = 1
end = 20

for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)
```

### Output

```text
2
4
6
8
10
12
14
16
18
20
```

### Explanation

The loop processes all integers from 1 through 20.

The conditional statement prints only numbers whose remainder after division by two is zero.

### Concepts Used

- For loop.
- Range.
- Modulus operator.
- Filtering.

---

## Example 8: Count Even and Odd Numbers

### Objective

Count even and odd integers in a list.

### Code

```python
numbers = [10, 15, 20, 25, 30, 35]

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
Even count: 3
Odd count: 3
```

### Explanation

The program visits every element in the list.

Each element increases either the even counter or the odd counter.

Both counters are displayed after the loop finishes.

### Concepts Used

- List traversal.
- For loop.
- Counter variables.
- If-else.

---

## Example 9: Sum of Even Numbers

### Objective

Calculate the sum of even values in a list.

### Code

```python
numbers = [2, 5, 8, 11, 14, 17]

even_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number

print("Even sum:", even_sum)
```

### Output

```text
Even sum: 24
```

### Explanation

The even values are 2, 8, and 14.

The program adds these values to the accumulator.

The final sum is 24.

### Concepts Used

- List.
- Loop.
- Accumulator.
- Conditional statement.

---

## Example 10: Sum of Odd Numbers

### Objective

Calculate the sum of odd values in a list.

### Code

```python
numbers = [1, 4, 7, 10, 13, 16]

odd_sum = 0

for number in numbers:
    if number % 2 != 0:
        odd_sum += number

print("Odd sum:", odd_sum)
```

### Output

```text
Odd sum: 21
```

### Explanation

The odd values are 1, 7, and 13.

Their sum is 21.

Even values are ignored.

### Concepts Used

- Modulus operator.
- Accumulator.
- List traversal.

---

## Example 11: First Even Number

### Objective

Find the first even number in a list.

### Code

```python
numbers = [7, 9, 11, 14, 17, 20]

first_even = None

for number in numbers:
    if number % 2 == 0:
        first_even = number
        break

if first_even is not None:
    print("First even number:", first_even)
else:
    print("No even number found")
```

### Output

```text
First even number: 14
```

### Explanation

The program checks the elements in their existing order.

The first matching value is 14.

The `break` statement stops the loop.

### Concepts Used

- Searching.
- List traversal.
- Break statement.
- Conditional statement.

---

## Example 12: Largest Even Number

### Objective

Find the largest even value in a list.

### Code

```python
numbers = [12, 25, 18, 31, 40, 17]

largest_even = None

for number in numbers:
    if number % 2 == 0:
        if largest_even is None or number > largest_even:
            largest_even = number

if largest_even is not None:
    print("Largest even number:", largest_even)
else:
    print("No even number found")
```

### Output

```text
Largest even number: 40
```

### Explanation

The program checks whether each value is even.

If it is even, the value is compared with the currently stored maximum.

The largest value is updated when a larger even number is found.

### Concepts Used

- Nested if.
- List traversal.
- Maximum selection.
- `None`.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Even or Odd

### Problem Statement

Accept an integer and determine whether it is even or odd.

### Logic

1. Accept an integer.
2. Calculate its remainder after division by two.
3. Check whether the remainder is zero.
4. Display the result.

### Code

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Sample Input

```text
Enter an integer: 14
```

### Expected Output

```text
Even number
```

### Explanation

The condition is:

```python
number % 2 == 0
```

For 14, the result is zero.

Therefore, the number is even.

### Concepts Used

- Integer input.
- Modulus operator.
- If-else.
- Comparison.

---

## Problem 2: Negative Even or Odd

### Problem Statement

Accept a negative integer and classify it as even or odd.

### Logic

1. Accept a negative integer.
2. Check divisibility by two.
3. Display the parity.

### Code

```python
number = int(input("Enter a negative integer: "))

if number >= 0:
    print("Please enter a negative integer")
elif number % 2 == 0:
    print("Negative even number")
else:
    print("Negative odd number")
```

### Sample Input

```text
Enter a negative integer: -15
```

### Expected Output

```text
Negative odd number
```

### Explanation

The program first checks whether the number is negative.

Then it checks divisibility by two.

-15 is negative and is not divisible by two without a remainder.

Therefore, the result is a negative odd number.

### Concepts Used

- If-elif-else.
- Modulus operator.
- Negative number validation.

---

## Problem 3: Zero Parity

### Problem Statement

Demonstrate whether zero is even or odd.

### Logic

1. Set the number to zero.
2. Check whether the remainder after division by two is zero.
3. Display the result.

### Code

```python
number = 0

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Expected Output

```text
Even number
```

### Explanation

Zero can be written as two multiplied by zero.

Therefore, zero is divisible by two and is even.

### Concepts Used

- Modulus operator.
- Equality comparison.
- Zero.

---

## Problem 4: Even or Odd in a Range

### Problem Statement

Accept an integer between 1 and 100 and classify it as even or odd.

### Logic

1. Accept an integer.
2. Validate its allowed range.
3. Check divisibility by two.
4. Display the result.

### Code

```python
number = int(input("Enter an integer between 1 and 100: "))

if 1 <= number <= 100:
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Number is outside the valid range")
```

### Sample Input

```text
Enter an integer between 1 and 100: 50
```

### Expected Output

```text
Even number
```

### Explanation

The first condition checks whether the number belongs to the accepted range.

Only valid numbers are classified as even or odd.

### Concepts Used

- Range validation.
- Nested if.
- Modulus operator.

---

## Problem 5: Count Even and Odd Numbers

### Problem Statement

Accept multiple integers and count even and odd values.

### Logic

1. Accept the number of integers.
2. Initialize both counters to zero.
3. Read each integer.
4. Classify it as even or odd.
5. Increase the appropriate counter.
6. Display the counts.

### Code

```python
count = int(input("How many integers? "))

even_count = 0
odd_count = 0

for index in range(count):
    number = int(input(f"Enter integer {index + 1}: "))

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)
```

### Sample Input

```text
How many integers? 5
Enter integer 1: 10
Enter integer 2: 15
Enter integer 3: 20
Enter integer 4: 25
Enter integer 5: 30
```

### Expected Output

```text
Even count: 3
Odd count: 2
```

### Explanation

Three values are even.

Two values are odd.

The program processes every input once.

### Concepts Used

- For loop.
- Counter variables.
- If-else.
- User input.

---

## Problem 6: Sum of Even Numbers

### Problem Statement

Accept multiple integers and calculate the sum of all even numbers.

### Logic

1. Accept a collection of integers.
2. Initialize `even_sum` to zero.
3. Visit each integer.
4. If the number is even, add it to the sum.
5. Display the final sum.

### Code

```python
count = int(input("How many integers? "))

even_sum = 0

for index in range(count):
    number = int(input(f"Enter integer {index + 1}: "))

    if number % 2 == 0:
        even_sum += number

print("Sum of even numbers:", even_sum)
```

### Sample Input

```text
How many integers? 5
Enter integer 1: 2
Enter integer 2: 5
Enter integer 3: 8
Enter integer 4: 11
Enter integer 5: 14
```

### Expected Output

```text
Sum of even numbers: 24
```

### Explanation

The even values are 2, 8, and 14.

Their sum is:

\[
2 + 8 + 14 = 24
\]

### Concepts Used

- For loop.
- Accumulator.
- Modulus operator.
- If condition.

---

## Problem 7: Sum of Odd Numbers

### Problem Statement

Accept multiple integers and calculate the sum of odd values.

### Logic

1. Accept the number of values.
2. Initialize the odd sum to zero.
3. Read all numbers.
4. Check which values are odd.
5. Add odd values to the accumulator.
6. Display the sum.

### Code

```python
count = int(input("How many integers? "))

odd_sum = 0

for index in range(count):
    number = int(input(f"Enter integer {index + 1}: "))

    if number % 2 != 0:
        odd_sum += number

print("Sum of odd numbers:", odd_sum)
```

### Sample Input

```text
How many integers? 5
Enter integer 1: 1
Enter integer 2: 4
Enter integer 3: 7
Enter integer 4: 10
Enter integer 5: 13
```

### Expected Output

```text
Sum of odd numbers: 21
```

### Explanation

The odd values are 1, 7, and 13.

Their sum is:

\[
1 + 7 + 13 = 21
\]

### Concepts Used

- For loop.
- Modulus operator.
- Accumulator.
- Conditional statement.

---

## Problem 8: Filter Even Numbers

### Problem Statement

Accept multiple integers and store only even numbers in a new list.

### Logic

1. Accept integers.
2. Create an empty list.
3. Check each value.
4. Append even values to the new list.
5. Display the result.

### Code

```python
numbers = [10, 15, 20, 25, 30, 35]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
```

### Expected Output

```text
Original list: [10, 15, 20, 25, 30, 35]
Even numbers: [10, 20, 30]
```

### Explanation

The loop checks every list element.

Only the values divisible by two are added to `even_numbers`.

### Concepts Used

- Lists.
- For loop.
- Append method.
- Filtering.
- Conditional statements.

---

## Problem 9: Filter Odd Numbers

### Problem Statement

Accept multiple integers and create a new list containing only odd values.

### Logic

1. Accept a list of integers.
2. Create an empty list.
3. Check every value.
4. Append odd values.
5. Display the filtered list.

### Code

```python
numbers = [10, 15, 20, 25, 30, 35]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print("Original list:", numbers)
print("Odd numbers:", odd_numbers)
```

### Expected Output

```text
Original list: [10, 15, 20, 25, 30, 35]
Odd numbers: [15, 25, 35]
```

### Explanation

The expression `number % 2 != 0` identifies odd integers.

Every matching value is appended to the new list.

### Concepts Used

- Lists.
- Conditional statements.
- For loop.
- Append method.

---

## Problem 10: Find the First Even Number

### Problem Statement

Accept multiple integers and find the first even value.

### Logic

1. Read a collection of integers.
2. Initialize the result with `None`.
3. Traverse the values.
4. Check whether each number is even.
5. Store the first even number.
6. Stop the loop.
7. Display the result.

### Code

```python
numbers = [7, 9, 11, 14, 17, 20]

first_even = None

for number in numbers:
    if number % 2 == 0:
        first_even = number
        break

if first_even is None:
    print("No even number found")
else:
    print("First even number:", first_even)
```

### Expected Output

```text
First even number: 14
```

### Explanation

The first three values are odd.

The fourth value is 14, which is even.

The program stores it and uses `break` to stop searching.

### Concepts Used

- List traversal.
- Searching.
- Break statement.
- None.

---

## Problem 11: Largest Even Number

### Problem Statement

Find the largest even integer in a collection.

### Logic

1. Accept integers.
2. Initialize the largest-even value with `None`.
3. Check each integer.
4. Ignore odd values.
5. Compare even values.
6. Update the maximum when a larger even value is found.
7. Display the final result.

### Code

```python
numbers = [12, 25, 18, 31, 40, 17]

largest_even = None

for number in numbers:
    if number % 2 == 0:
        if largest_even is None or number > largest_even:
            largest_even = number

if largest_even is None:
    print("No even number found")
else:
    print("Largest even number:", largest_even)
```

### Expected Output

```text
Largest even number: 40
```

### Explanation

The program examines every integer.

It ignores odd values.

Even numbers are compared with the current maximum.

The final maximum is 40.

### Concepts Used

- Nested if.
- Maximum selection.
- List traversal.
- Comparison operators.

---

## Problem 12: Divisibility by Six

### Problem Statement

Accept an integer and check whether it is divisible by six.

### Logic

A number is divisible by six when it is divisible by both two and three.

Check:

```python
number % 2 == 0
```

and:

```python
number % 3 == 0
```

Both conditions must be true.

### Code

```python
number = int(input("Enter an integer: "))

if number % 2 == 0 and number % 3 == 0:
    print("Divisible by 6")
else:
    print("Not divisible by 6")
```

### Sample Input

```text
Enter an integer: 18
```

### Expected Output

```text
Divisible by 6
```

### Explanation

18 is divisible by two.

18 is also divisible by three.

Therefore, it is divisible by six.

### Concepts Used

- Modulus operator.
- Logical AND.
- Conditional statements.
- Divisibility.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try to solve all ten questions independently.

Use the modulus operator and conditional statements where appropriate.

## Question 1: Smallest Even Number

Accept a list of integers and find the smallest even number.

Requirements:

- Accept multiple integers.
- Identify even values.
- Compare even values.
- Display the smallest even value.
- Handle a list containing no even numbers.

Concepts:

- Lists.
- For loop.
- Conditional statements.
- Minimum selection.

## Question 2: Largest Odd Number

Accept a list of integers and find the largest odd number.

Requirements:

- Accept multiple integers.
- Identify odd values.
- Compare odd values.
- Display the largest odd number.
- Handle a list containing no odd numbers.

Concepts:

- Lists.
- Modulus operator.
- Maximum selection.

## Question 3: Count Positive Even and Odd Numbers

Accept multiple integers and count:

- Positive even numbers.
- Positive odd numbers.

Requirements:

- Ignore zero.
- Ignore negative values.
- Count positive even numbers separately.
- Count positive odd numbers separately.
- Display both counters.

Concepts:

- Nested if.
- Counter variables.
- Logical conditions.

## Question 4: Average of Even Numbers

Accept multiple integers and calculate the average of even values.

Requirements:

- Read the values.
- Add only even values.
- Count even values.
- Divide the sum by the count.
- Handle the case where no even values exist.

Concepts:

- Accumulator.
- Counter.
- Conditional statement.
- Arithmetic operators.

## Question 5: First Odd Number and Position

Accept a list of integers.

Find the first odd number and display its index.

Requirements:

- Traverse the list.
- Check each number.
- Find the first odd value.
- Display its index.
- Handle the case where no odd value exists.

Concepts:

- List indexing.
- Searching.
- For loop.
- Break statement.

## Question 6: Even Numbers in a Given Range

Accept two integers representing the starting and ending values.

Display all even numbers within the range.

Requirements:

- Accept the starting value.
- Accept the ending value.
- Validate the range.
- Generate the integers.
- Display even values.

Concepts:

- Range.
- For loop.
- Modulus operator.

## Question 7: Divisible by Two and Three

Accept a collection of integers.

Find values divisible by both two and three.

Requirements:

- Accept multiple integers.
- Check divisibility by two.
- Check divisibility by three.
- Display matching values.

Concepts:

- Modulus operator.
- Logical AND.
- List filtering.

## Question 8: Compare Even and Odd Counts

Accept multiple integers.

Determine whether even numbers or odd numbers occur more frequently.

Requirements:

- Count even numbers.
- Count odd numbers.
- Compare both counts.
- Display which category has more values.
- Display a tie message when both counts are equal.

Concepts:

- Counters.
- If-elif-else.
- Comparisons.

## Question 9: Separate Even and Odd Lists

Accept multiple integers and create two separate lists.

Requirements:

- Create an empty even list.
- Create an empty odd list.
- Check every number.
- Append even values to one list.
- Append odd values to the other list.
- Display both lists.

Concepts:

- Lists.
- Append.
- Conditional statements.
- Loop.

## Question 10: Parity Classification of Multiple Numbers

Accept multiple integers and classify each as even or odd.

Requirements:

- Accept the number of integers.
- Read each integer.
- Determine its parity.
- Display the classification for every value.

Concepts:

- Input.
- Loop.
- Modulus operator.
- If-else.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Forgetting the Modulus Operator

Incorrect:

```python
if number / 2 == 0:
    print("Even")
```

Correct:

```python
if number % 2 == 0:
    print("Even")
```

The `/` operator performs division.

The `%` operator calculates the remainder.

## Mistake 2: Using Incorrect Comparison

Incorrect:

```python
if number % 2 = 0:
    print("Even")
```

Correct:

```python
if number % 2 == 0:
    print("Even")
```

Use `==` for comparison.

## Mistake 3: Thinking Zero Is Odd

Zero is even because:

\[
0 \bmod 2 = 0
\]

Correct:

```python
number = 0

if number % 2 == 0:
    print("Even")
```

## Mistake 4: Thinking Negative Numbers Cannot Be Even

Negative integers can be even.

Example:

```python
number = -10

print(number % 2 == 0)
```

Output:

```text
True
```

## Mistake 5: Using Wrong Odd Condition

For general integer inputs, use:

```python
number % 2 != 0
```

Do not rely on checking whether the remainder equals exactly 1, especially when negative integers are allowed.

## Mistake 6: Forgetting Counter Initialization

Incorrect:

```python
even_count += 1
```

This produces a `NameError` if the variable has not already been defined.

Correct:

```python
even_count = 0
even_count += 1
```

## Mistake 7: Replacing a Counter Instead of Updating It

Incorrect:

```python
if number % 2 == 0:
    even_count = 1
```

Correct:

```python
if number % 2 == 0:
    even_count += 1
```

The second version counts every matching value.

## Mistake 8: Using the Wrong Initial Maximum

If negative even numbers are possible, avoid starting the largest-even search at zero.

For example, consider:

```python
numbers = [-8, -4, -2]
```

The largest even value is `-2`, not zero.

Use `None` initially and update it when the first even number appears.

## Mistake 9: Forgetting to Handle No Matching Value

If a list contains only odd numbers, a search for an even number must handle that case.

## Mistake 10: Forgetting Break

When finding the first even number, use `break` after a match if no later values are needed.

Do not use `break` when the program needs to examine every value.

## Mistake 11: Incorrect Range

Remember that:

```python
range(1, 10)
```

generates values from 1 through 9.

It does not include 10.

## Mistake 12: Using Float Values for Integer Parity Problems

Even-odd classification is normally defined for integers.

If the input can contain decimal values, decide whether to reject them, convert them only under an explicit rule, or solve a different divisibility problem.

Do not silently truncate decimal input and change the intended value.

---

# SECTION 5: BEST PRACTICES

Follow these guidelines when solving even-odd problems.

1. Use `% 2 == 0` to check even integers.
2. Use `% 2 != 0` to check odd integers.
3. Remember that zero is even.
4. Remember that negative integers can be even or odd.
5. Use meaningful variable names.
6. Initialize counters before using them.
7. Initialize accumulators to the correct starting value.
8. Use loops to process multiple numbers.
9. Use `break` when a search is complete.
10. Use `None` when no qualifying result has been found.
11. Handle empty or non-matching collections.
12. Avoid unnecessary nested conditions.
13. Validate input types.
14. Use lists when multiple values need to be stored.
15. Use functions when logic is repeated.
16. Do not use sorting when one traversal is sufficient.
17. Consider boundary values.
18. Keep the output understandable.
19. Test negative even and odd values.
20. Keep code readable.

### Reusable Even Function

```python
def is_even(number: int) -> bool:
    return number % 2 == 0
```

### Reusable Odd Function

```python
def is_odd(number: int) -> bool:
    return number % 2 != 0
```

### Example Usage

```python
numbers = [2, 5, 8, 11, 14]

for number in numbers:
    if is_even(number):
        print(number, "is even")
    else:
        print(number, "is odd")
```

Output:

```text
2 is even
5 is odd
8 is even
11 is odd
14 is even
```

---

# SECTION 6: DEBUGGING

Debugging is the process of finding and correcting errors in a program.

Even-odd problems are useful for learning debugging because incorrect operators can produce incorrect results.

## 1. Check the Modulus Expression

Verify that you are checking the remainder.

Correct:

```python
number % 2 == 0
```

## 2. Check the Input Type

The `input()` function returns a string.

Convert it to an integer before using the remainder operator for integer classification.

```python
number = int(input("Enter an integer: "))
```

## 3. Check Negative Values

Test values such as:

```text
-2
-3
-4
-5
```

The even-odd condition should work with both positive and negative integers.

## 4. Check Zero

Always test zero.

A correct even-odd program should classify zero as even.

## 5. Check Counter Variables

Before using counters, initialize them.

```python
even_count = 0
odd_count = 0
```

## 6. Check Accumulators

Before calculating sums, initialize the total.

```python
even_sum = 0
odd_sum = 0
```

## 7. Check Loop Behaviour

Make sure every value is processed when counting or summing.

Use `break` only when a search is intentionally stopped after the first match.

## 8. Check Missing Results

When searching for an even or odd value, consider whether the collection might not contain a matching element.

## 9. Common Python Errors

| Error | Meaning |
|---|---|
| `ValueError` | Invalid value during conversion |
| `TypeError` | Incompatible operation |
| `NameError` | Variable has not been defined |
| `IndexError` | Invalid list index |
| `IndentationError` | Incorrect indentation |
| `SyntaxError` | Invalid Python syntax |

## 10. Debugging Checklist

Before considering the program complete:

- Check that numeric input is valid.
- Check that integer conversion is used correctly.
- Check the modulus condition.
- Check zero.
- Check positive even values.
- Check positive odd values.
- Check negative even values.
- Check negative odd values.
- Check counter initialization.
- Check accumulator initialization.
- Check the loop range.
- Check whether the search handles missing results.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Even-odd classification is used in many computing situations.

## 1. Number Classification Programs

A basic mathematical program can identify whether a number is even or odd.

## 2. Array Indexing

Python list indexes start from zero.

An index can be classified as even or odd.

Example:

```python
items = ["A", "B", "C", "D", "E"]

for index in range(len(items)):
    if index % 2 == 0:
        print("Even index:", index, items[index])
```

Output:

```text
Even index: 0 A
Even index: 2 C
Even index: 4 E
```

This is useful when processing alternating positions.

## 3. Alternating Patterns

A program can use parity to alternate between two behaviours.

Example:

```python
for number in range(1, 7):
    if number % 2 == 0:
        print(number, "Second pattern")
    else:
        print(number, "First pattern")
```

## 4. Seating Systems

A seating application may use alternating row or seat numbers for certain patterns.

## 5. Scheduling Systems

A simple schedule may assign alternating tasks to even and odd numbered days or slots.

## 6. Data Processing

Data-processing programs may separate values according to divisibility rules.

## 7. Mathematics Applications

Even-odd classification is used in arithmetic problems, number theory, and mathematical calculations.

## 8. Game Programming

A game may use even and odd numbers to alternate turns, phases, or visual patterns.

## 9. Inventory and IDs

Systems may classify numbered records by parity to create simple grouping rules.

## 10. DSA Problems

Even-odd conditions appear in array traversal, filtering, searching, partitioning, and counting problems.

---

# SECTION 7: DSA CONNECTION

Even-odd problems introduce several important concepts used in Data Structures and Algorithms.

## 1. Array Traversal

An array or list can be traversed to inspect each element.

```python
numbers = [2, 5, 8, 11, 14]

for number in numbers:
    if number % 2 == 0:
        print(number)
```

This is the foundation of filtering and classification problems.

## 2. Searching

Finding the first even number is a searching problem.

The algorithm examines values until it finds a match.

## 3. Filtering

Creating a new list containing only even numbers is a filtering problem.

## 4. Counting

Counting even and odd values is a frequency-counting problem.

## 5. Accumulation

Calculating the sum of even numbers introduces accumulator logic.

## 6. Maximum and Minimum

Finding the largest even or smallest odd value introduces conditional maximum and minimum selection.

## 7. Two-Pointer and Partitioning Ideas

Even-odd classification can also be used in partitioning problems.

For example, you may need to rearrange an array so that even values appear before odd values.

That is a separate algorithmic problem involving array manipulation.

### DSA Skills Developed

- Array traversal.
- Searching.
- Filtering.
- Counting.
- Summation.
- Maximum selection.
- Minimum selection.
- Conditional logic.
- Index handling.
- Problem decomposition.

### Important Practice Advice

Do not memorize the code only.

Understand:

- Why the modulus operator is used.
- Why a counter is initialized to zero.
- Why an accumulator stores a running total.
- Why a search may use `break`.
- Why a maximum variable must be updated.
- Why a list is sometimes created for filtered results.

These ideas appear repeatedly in beginner and intermediate DSA problems.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

Time complexity describes how the number of operations grows with input size.

Space complexity describes how much additional memory an algorithm requires.

## 1. Checking One Number

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

The program performs a fixed number of operations.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 2. Printing Even Numbers in a Range

```python
for number in range(1, n + 1):
    if number % 2 == 0:
        print(number)
```

The loop examines all numbers in the range.

Time complexity:

\[
O(n)
\]

The loop uses a constant amount of additional memory.

Additional space complexity:

\[
O(1)
\]

This assumes output is streamed directly rather than stored in an input-sized list.

## 3. Counting Even and Odd Numbers

```python
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
```

The algorithm visits every element once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 4. Sum of Even Numbers

The algorithm also examines every input value once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 5. Filtering Even Numbers

```python
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
```

The program examines all elements.

Time complexity:

\[
O(n)
\]

In the worst case, all values may be even, so the new list can contain `n` elements.

Additional space complexity:

\[
O(n)
\]

## 6. Finding the First Even Number

The best case occurs when the first element is even.

Best-case time complexity:

\[
O(1)
\]

The worst case occurs when the last element is even or no even value exists.

Worst-case time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 7. Finding the Largest Even Number

The algorithm checks every element to ensure the maximum is correct.

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
| Check one integer | \(O(1)\) | \(O(1)\) |
| Print even numbers in a range | \(O(n)\) | \(O(1)\) |
| Count even and odd values | \(O(n)\) | \(O(1)\) |
| Sum even values | \(O(n)\) | \(O(1)\) |
| Filter even values | \(O(n)\) | \(O(n)\) |
| Find first even value | Best \(O(1)\), worst \(O(n)\) | \(O(1)\) |
| Find largest even value | \(O(n)\) | \(O(1)\) |

---

# SECTION 9: MINI PROJECT – EVEN AND ODD NUMBER ANALYSIS SYSTEM

## Project Overview

Create a number-analysis program that accepts multiple integers and produces an even-odd report.

The program should:

1. Accept multiple integers.
2. Separate even and odd values.
3. Count even numbers.
4. Count odd numbers.
5. Calculate the sum of even values.
6. Calculate the sum of odd values.
7. Find the largest even number.
8. Find the largest odd number.

This project combines the main concepts from this topic.

## Python Code

```python
numbers = []

count = int(input("How many integers do you want to enter? "))

for index in range(count):
    number = int(input(f"Enter integer {index + 1}: "))
    numbers.append(number)

even_numbers = []
odd_numbers = []

even_sum = 0
odd_sum = 0

largest_even = None
largest_odd = None

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)
        even_sum += number

        if largest_even is None or number > largest_even:
            largest_even = number

    else:
        odd_numbers.append(number)
        odd_sum += number

        if largest_odd is None or number > largest_odd:
            largest_odd = number

print("\nEVEN AND ODD ANALYSIS REPORT")
print("=" * 40)

print("Original numbers:", numbers)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

print("Even count:", len(even_numbers))
print("Odd count:", len(odd_numbers))

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

if largest_even is None:
    print("Largest even number: Not found")
else:
    print("Largest even number:", largest_even)

if largest_odd is None:
    print("Largest odd number: Not found")
else:
    print("Largest odd number:", largest_odd)
```

## Sample Input

```text
How many integers do you want to enter? 6

Enter integer 1: 10
Enter integer 2: 15
Enter integer 3: 20
Enter integer 4: 25
Enter integer 5: 30
Enter integer 6: 35
```

## Expected Output

```text
EVEN AND ODD ANALYSIS REPORT
========================================
Original numbers: [10, 15, 20, 25, 30, 35]

Even numbers: [10, 20, 30]
Odd numbers: [15, 25, 35]

Even count: 3
Odd count: 3

Even sum: 60
Odd sum: 75

Largest even number: 30
Largest odd number: 35
```

## Project Explanation

The program first accepts a collection of integers.

It creates two new lists:

- `even_numbers`
- `odd_numbers`

Each integer is checked using the modulus operator.

If the remainder after division by two is zero, the value is even.

Otherwise, it is odd.

The program stores each value in the correct list.

It also maintains separate sums and maximum values.

Finally, it displays the complete analysis report.

## Project Improvements

After completing the basic project, try these improvements:

1. Add an option to process another list.
2. Display positive even numbers separately.
3. Display negative even numbers separately.
4. Display positive odd numbers separately.
5. Display negative odd numbers separately.
6. Find the smallest even number.
7. Find the smallest odd number.
8. Calculate the average of even numbers.
9. Calculate the average of odd numbers.
10. Create functions for every major operation.
11. Add input validation.
12. Add an interactive menu.

---

# SECTION 10: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is an even number?

An even integer is completely divisible by 2.

### 2. What is an odd number?

An odd integer is not completely divisible by 2.

### 3. Which operator checks even and odd numbers in Python?

The modulus operator `%`.

### 4. What is the condition for an even number?

`number % 2 == 0`.

### 5. What is the condition for an odd number?

`number % 2 != 0`.

### 6. Is zero even or odd?

Zero is even.

### 7. Can negative numbers be even?

Yes. For example, `-4` is even.

### 8. Can negative numbers be odd?

Yes. For example, `-7` is odd.

### 9. What is the remainder of 10 divided by 2?

Zero.

### 10. What is the remainder of 7 divided by 2?

One.

## Intermediate Questions

### 11. What is the modulus operator?

It returns the remainder after division according to Python's modulo rules.

### 12. What is the difference between `/` and `%`?

`/` performs division, while `%` returns the remainder.

### 13. What is the output of `12 % 2`?

Zero.

### 14. What is the output of `15 % 2`?

One.

### 15. Why is zero considered even?

Because zero is divisible by two without a remainder.

### 16. Which statement is used to check even or odd values?

An `if-else` statement is commonly used.

### 17. Can a conditional expression check even or odd values?

Yes.

### 18. What is a counter variable?

A variable used to count how many times a condition is satisfied.

### 19. What is an accumulator?

A variable used to maintain a running total.

### 20. What does `break` do?

It terminates the nearest enclosing loop.

## Practical Questions

### 21. How do you check whether 20 is even?

Use `20 % 2 == 0`.

### 22. How do you check whether 21 is odd?

Use `21 % 2 != 0`.

### 23. How do you count even numbers in a list?

Traverse the list and increase a counter whenever the number is divisible by two.

### 24. How do you count odd numbers?

Traverse the list and increase a counter whenever the number is not divisible by two.

### 25. How do you calculate the sum of even numbers?

Add only numbers satisfying `number % 2 == 0`.

### 26. How do you calculate the sum of odd numbers?

Add only numbers satisfying `number % 2 != 0`.

### 27. How do you find the first even number?

Traverse the collection and stop at the first number satisfying the even condition.

### 28. How do you find the largest even number?

Maintain a maximum value and update it whenever a larger even number is found.

### 29. How do you filter odd numbers?

Create a new list and append values satisfying the odd condition.

### 30. How do you check whether a number is divisible by six?

Check whether it is divisible by both two and three.

## Advanced Questions

### 31. What is the time complexity of checking one integer?

Generally `O(1)`.

### 32. What is the time complexity of counting even values in a list?

`O(n)`.

### 33. What is the time complexity of filtering even values?

`O(n)`.

### 34. What is the additional space complexity of filtering values into a new list?

`O(n)` in the worst case.

### 35. What is the additional space complexity of a simple counting algorithm?

`O(1)`.

### 36. Can negative integers be classified using `% 2`?

Yes. The condition `number % 2 == 0` correctly checks negative even integers as well.

### 37. What is the purpose of `append()`?

It adds an element to the end of a list.

### 38. What is the purpose of `len()`?

It returns the number of elements in a collection.

### 39. Why initialize the sum variable to zero?

Zero is the neutral starting value for addition.

### 40. Why use `None` when finding the largest even number?

It represents that no even number has been found yet.

## Interview-Oriented Questions

### 41. How would you separate even and odd numbers from an array?

Traverse the array and append each value to the appropriate list based on its remainder after division by two.

### 42. How would you count even and odd values in one traversal?

Use two counters and update one counter for each element.

### 43. How can you find the first even number efficiently?

Use a linear search and stop when the first even number is found.

### 44. What is the advantage of using a single loop for counting?

It examines each element only once.

### 45. Can sorting be avoided when finding the largest even number?

Yes. A single traversal is sufficient.

### 46. What happens when a list contains no even numbers?

The program should report that no even value was found.

### 47. Why should zero be included in even-number logic?

Because zero is mathematically even.

### 48. What is parity?

Parity refers to whether an integer is even or odd.

### 49. What is the difference between an even number and a positive number?

Evenness is based on divisibility by two; positivity is based on being greater than zero.

### 50. Why is even-odd classification important in DSA?

It builds the foundation for array traversal, filtering, counting, searching, and mathematical algorithms.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Even number | Integer divisible by 2 |
| Odd number | Integer not divisible by 2 |
| Parity | Classification of an integer as even or odd |
| Modulus | Remainder after division |
| Counter | Variable used to count matching values |
| Accumulator | Variable used to store a running total |
| List | Ordered, mutable collection of values |
| Traversal | Visiting elements of a collection |
| Filtering | Selecting values that satisfy a condition |
| Searching | Finding an element that satisfies a condition |
| Maximum | Largest value |
| Minimum | Smallest value |
| Break | Statement that terminates the nearest loop |
| Append | Operation that adds an item to a list |
| Index | Position of an element in a sequence |
| Range | Sequence of integer values generated by `range()` |
| Integer | Whole-number type in Python |
| Conditional statement | Statement that executes based on a condition |
| Boolean | Value that is either `True` or `False` |
| Complexity | Measure of an algorithm's time or space usage |

---

# SECTION 12: QUICK REVISION NOTES

## Main Definitions

Even number:

An integer divisible by 2 without a remainder.

Odd number:

An integer that is not divisible by 2 without a remainder.

Zero:

An even number.

## Important Conditions

Even:

```python
number % 2 == 0
```

Odd:

```python
number % 2 != 0
```

Divisible by 6:

```python
number % 6 == 0
```

Divisible by both 2 and 3:

```python
number % 2 == 0 and number % 3 == 0
```

## Count Even Numbers

```python
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
```

## Count Odd Numbers

```python
odd_count = 0

for number in numbers:
    if number % 2 != 0:
        odd_count += 1
```

## Sum of Even Numbers

```python
even_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number
```

## Sum of Odd Numbers

```python
odd_sum = 0

for number in numbers:
    if number % 2 != 0:
        odd_sum += number
```

## Filter Even Numbers

```python
even_numbers = [
    number for number in numbers
    if number % 2 == 0
]
```

## Filter Odd Numbers

```python
odd_numbers = [
    number for number in numbers
    if number % 2 != 0
]
```

## First Even Number

```python
first_even = None

for number in numbers:
    if number % 2 == 0:
        first_even = number
        break
```

## Important Operators

| Operator | Meaning |
|---|---|
| `%` | Modulus |
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `and` | Both conditions true |
| `+=` | Add and assign |

## Important Concepts

- Zero is even.
- Negative integers can be even or odd.
- Use `% 2 == 0` for even.
- Use `% 2 != 0` for odd.
- Use counters for frequency.
- Use accumulators for sums.
- Use lists to store filtered values.
- Use loops to examine multiple numbers.
- Use `break` to stop at the first matching value.
- Use `None` when no qualifying value has been found.
- Avoid sorting when a single traversal is sufficient.

---

# SECTION 13: LEARNING CHECKLIST

Use this checklist after completing the topic.

- [ ] I understand what an even number is.
- [ ] I understand what an odd number is.
- [ ] I know that zero is even.
- [ ] I understand the modulus operator.
- [ ] I can check whether a number is even.
- [ ] I can check whether a number is odd.
- [ ] I can classify positive even numbers.
- [ ] I can classify positive odd numbers.
- [ ] I can classify negative even numbers.
- [ ] I can classify negative odd numbers.
- [ ] I can display even numbers within a range.
- [ ] I can display odd numbers within a range.
- [ ] I can count even numbers.
- [ ] I can count odd numbers.
- [ ] I can calculate the sum of even numbers.
- [ ] I can calculate the sum of odd numbers.
- [ ] I can filter even values from a list.
- [ ] I can filter odd values from a list.
- [ ] I can find the first even number.
- [ ] I can find the first odd number.
- [ ] I can find the largest even number.
- [ ] I can check divisibility by six.
- [ ] I can use loops with conditions.
- [ ] I can use counters and accumulators.
- [ ] I understand basic time complexity.
- [ ] I understand basic space complexity.
- [ ] I can handle lists without matching values.
- [ ] I have attempted all ten unsolved questions.
- [ ] I understand the DSA connection.
- [ ] I can explain even-odd classification in an interview.

---

# SECTION 14: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `02-even-odd` folder.

Run:

```bash
python 02_even_odd.py
```

On Windows, you can also use:

```powershell
py 02_even_odd.py
```

The Python program provides an interactive menu.

## Main Menu

```text
=================================================================
                    PYTHON: EVEN AND ODD NUMBERS
=================================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

Displays the twelve examples:

1. Basic even number.
2. Basic odd number.
3. Zero is even.
4. Positive even number.
5. Negative odd number.
6. Negative even number.
7. Even numbers in a range.
8. Count even and odd numbers.
9. Sum of even numbers.
10. Sum of odd numbers.
11. First even number.
12. Largest even number.

### Option 2 – Practice 12 Solved Problems

Displays the solved-problem selection menu.

Select a problem number to run it.

The program accepts input and displays the result.

### Option 3 – View 10 Unsolved Questions

Displays ten independent problems for practice.

Attempt these problems without copying the solved code.

### Option 4 – View Learning Checklist

Displays the topic checklist.

Use it to confirm that the required concepts have been understood.

### Option 0 – Exit

Closes the program.

---

# SECTION 15: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 06-Practice-Problems/
            └── 02-even-odd/
                ├── README.md
                └── 02_even_odd.py
```

### File Details

| File | Purpose |
|---|---|
| `README.md` | Complete theory, syntax, twelve examples, twelve solved problems, ten unsolved questions, and revision notes |
| `02_even_odd.py` | Python program containing examples, solved problems, unsolved questions, checklist, and interactive menu |

### Previous Topic

**01-positive-negative**

In the previous problem, you learned how to classify numbers as positive, negative, and zero.

### Current Topic

**02-even-odd**

In this problem, you learned how to classify integers as even and odd using the modulus operator.

### Next Topic

**03-largest-number**

In the next problem, you will learn how to compare numbers and find the largest value using conditional statements.

---

# FINAL SUMMARY

Even and odd number classification is one of the most important beginner-level programming problems.

It helps you understand the modulus operator, comparison operators, loops, and conditions.

After completing this topic, you should be able to:

1. Understand even numbers.
2. Understand odd numbers.
3. Identify zero as an even number.
4. Classify positive and negative integers.
5. Use the modulus operator.
6. Check whether numbers are divisible by two.
7. Count even and odd numbers.
8. Calculate sums of even and odd numbers.
9. Filter values from lists.
10. Find the first even or odd number.
11. Find the largest even number.
12. Solve basic divisibility problems.
13. Apply loops and conditional statements.
14. Understand the connection with DSA.
15. Explain the topic in an interview.

### Final Advice

Do not memorize the condition only.

Understand why `% 2 == 0` identifies an even integer and why `% 2 != 0` identifies an odd integer.

Practice with positive numbers, negative numbers, zero, and collections containing different values.

After understanding even and odd classification, you will be better prepared for array traversal, filtering, counting, searching, and other beginner-level DSA problems.

**Keep practising and maintain the same repository structure throughout your Python learning journey.**

