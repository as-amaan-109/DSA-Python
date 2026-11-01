

# Python Largest Number – Complete Learning Guide

## 1. Introduction

Finding the largest number is one of the most important beginner-level programming problems.

It teaches us how to compare values, make decisions, use conditional statements, and process multiple numbers.

In Python, we can find the largest number using:

- `if` statements.
- `if-else` statements.
- `if-elif-else` statements.
- Nested `if` statements.
- Conditional expressions.
- Loops.
- Lists.
- The built-in `max()` function.

Finding the largest number is not limited to comparing two or three values. The same logic can be used to find the maximum value in an entire list.

### What Is the Largest Number?

The largest number is the value that is greater than or equal to every other value in the given collection.

For example:

```python
a = 10
b = 20
c = 15

largest = 20
```

Here, 20 is the largest number.

Mathematically, if three numbers are \(a\), \(b\), and \(c\), their maximum is:

\[
\max(a,b,c)
\]

The maximum is the value that satisfies:

\[
maximum \geq a
\]

\[
maximum \geq b
\]

\[
maximum \geq c
\]

### Learning Objectives

After completing this topic, you should be able to:

- Understand the meaning of the largest number.
- Compare two numbers.
- Find the largest of two numbers.
- Find the largest of three numbers.
- Find the largest of four numbers.
- Find the largest among multiple numbers.
- Use nested `if` statements.
- Use `if-elif-else` statements.
- Use comparison operators.
- Use logical operators.
- Handle equal values.
- Find the largest number in a list.
- Find the largest positive number.
- Find the largest negative number.
- Find the largest even number.
- Find the largest odd number.
- Find the highest student marks.
- Find the largest absolute value.
- Find the largest digit in an integer.
- Use Python's `max()` function.
- Find the maximum using a loop without using `max()`.
- Understand maximum selection in arrays.
- Apply maximum-finding logic to DSA problems.

---

## 2. What Is the Largest Number?

The largest number is the value that has the greatest numerical value among the given numbers.

### Example 1: Two Numbers

```python
a = 10
b = 20

if a > b:
    print("A is largest")
else:
    print("B is largest")
```

**Output:**

```text
B is largest
```

**Explanation:**

Python compares `a` and `b`.

The condition:

```python
a > b
```

checks whether the first number is greater than the second.

Since 10 is not greater than 20, Python executes the `else` block.

Therefore, B is the largest.

### Example 2: Three Numbers

```python
a = 25
b = 50
c = 35

if a > b and a > c:
    print("A is largest")
elif b > a and b > c:
    print("B is largest")
else:
    print("C is largest")
```

**Output:**

```text
B is largest
```

**Explanation:**

The program checks whether A is greater than both B and C.

If that is false, it checks whether B is greater than both A and C.

Since B is 50, it is the largest value.

### Example 3: Four Numbers

```python
a = 10
b = 40
c = 25
d = 30

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

if d > largest:
    largest = d

print("Largest number:", largest)
```

**Output:**

```text
Largest number: 40
```

This approach maintains a variable containing the largest value found so far.

### Important Points

- The largest number is determined by comparison.
- A maximum value can be found among two or more numbers.
- The `>` operator checks whether one value is greater than another.
- The `>=` operator also considers equality.
- A loop can find the maximum in a collection.
- A maximum-finding algorithm does not need to sort the collection.
- Equal values must be handled according to the problem's requirements.

---

## 3. Comparison Operators Used to Find the Largest Number

Comparison operators are used to compare two or more numeric values.

| Operator | Meaning | Example |
|---|---|---|
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

### Greater Than Operator

The `>` operator checks whether the left-hand value is greater than the right-hand value.

```python
a = 20
b = 10

print(a > b)
```

**Output:**

```text
True
```

### Greater Than or Equal Operator

The `>=` operator includes equal values.

```python
a = 20
b = 20

print(a >= b)
```

**Output:**

```text
True
```

### Equality Operator

The `==` operator checks whether two values are equal.

```python
a = 20
b = 20

print(a == b)
```

**Output:**

```text
True
```

### Not Equal Operator

The `!=` operator checks whether two values are different.

```python
a = 20
b = 10

print(a != b)
```

**Output:**

```text
True
```

### Why Are Comparison Operators Important?

When finding the largest number, the program must decide which value should be selected.

For example:

```python
if a > b:
    largest = a
else:
    largest = b
```

The comparison determines the value assigned to `largest`.

---

## 4. Finding the Largest of Two Numbers

Finding the largest of two numbers is the simplest maximum-selection problem.

### Syntax

```python
if a > b:
    largest = a
else:
    largest = b
```

### Example

```python
a = 25
b = 40

if a > b:
    largest = a
else:
    largest = b

print("Largest:", largest)
```

**Output:**

```text
Largest: 40
```

### Explanation

1. The program stores two numbers.
2. It compares the first number with the second.
3. If the first is greater, it selects the first.
4. Otherwise, it selects the second.
5. It displays the selected value.

### Handling Equal Numbers

Consider:

```python
a = 50
b = 50

if a > b:
    largest = a
else:
    largest = b

print(largest)
```

**Output:**

```text
50
```

Both values are equal.

The expression still returns the correct maximum value, but it does not explicitly tell us that the values are equal.

To detect equality separately:

```python
a = 50
b = 50

if a > b:
    print("A is largest")
elif b > a:
    print("B is largest")
else:
    print("Both numbers are equal")
```

**Output:**

```text
Both numbers are equal
```

### Important Point

Finding the largest value and identifying which input position contains that value are two different tasks.

When the numbers are equal, a program may need to report all positions containing the maximum.

---

## 5. Finding the Largest of Three Numbers

Finding the largest of three numbers is a common programming exercise.

There are different ways to solve it.

### Method 1: Using If-Elif-Else

```python
a = 25
b = 50
c = 35

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

**Output:**

```text
Largest: 50
```

### Explanation

The first condition checks whether A is greater than or equal to both B and C.

If the first condition is false, Python checks whether B is greater than or equal to both A and C.

If neither of those conditions is true, C is the largest candidate.

Using `>=` allows the program to handle tied maximum values while still selecting a correct maximum value.

### Method 2: Using Nested If

```python
a = 25
b = 50
c = 35

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("Largest:", largest)
```

**Output:**

```text
Largest: 50
```

### Explanation

The program first compares A and B.

If A is greater than B, it compares A with C.

Otherwise, it compares B with C.

This reduces the problem to a second comparison.

### Method 3: Using a Conditional Expression

```python
a = 25
b = 50
c = 35

largest = a if a >= b and a >= c else (b if b >= c else c)

print("Largest:", largest)
```

**Output:**

```text
Largest: 50
```

This method uses a nested conditional expression.

It is compact, but the normal `if-elif-else` version may be easier for beginners to understand.

### Method 4: Using max()

```python
a = 25
b = 50
c = 35

largest = max(a, b, c)

print("Largest:", largest)
```

**Output:**

```text
Largest: 50
```

Python's `max()` function returns the largest argument.

### Comparison of Methods

| Method | Main Concept |
|---|---|
| If-elif-else | Multiple comparisons |
| Nested if | Dependent decisions |
| Conditional expression | Compact value selection |
| `max()` | Built-in maximum function |

---

## 6. Finding the Largest of Multiple Numbers

When more than three numbers are provided, writing separate conditions for every possible comparison becomes inconvenient.

A loop is more suitable.

### Example

```python
numbers = [10, 25, 8, 40, 15]

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print("Largest:", largest)
```

**Output:**

```text
Largest: 40
```

### Explanation

Initially:

```python
largest = numbers[0]
```

The first element is assumed to be the largest.

The program then checks the remaining elements.

Whenever a larger value is found, `largest` is updated.

At the end, the variable contains the maximum value.

### Why Use the First Element?

Consider:

```python
numbers = [-20, -10, -30]
```

If we initialize the largest value to zero, the algorithm incorrectly returns zero.

Zero is not present in the collection.

The correct largest value is `-10`.

Initializing from the first element solves this problem.

### Important Condition

The list must contain at least one element before accessing `numbers[0]`.

In the provided Python program, the input helper requires at least one number.

---

## 7. Understanding the Current Maximum Variable

A maximum-selection algorithm usually maintains a variable called `largest`.

This variable stores the largest value found so far.

### Example

```python
numbers = [10, 25, 8, 40, 15]

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print(largest)
```

### Initial Value

```python
largest = 10
```

The first value is initially treated as the maximum.

### Updating the Maximum

When the program encounters a value greater than the current maximum, the variable is updated.

```python
if number > largest:
    largest = number
```

### Why Is This Useful?

The algorithm does not need to store every comparison result.

It only needs to remember the best value found so far.

This is called maintaining a running maximum.

### Important Points

- Start with a valid value from the collection.
- Compare each remaining value.
- Update only when a larger value appears.
- Do not reset the maximum inside the loop.
- Do not initialize to zero unless the problem guarantees that all values are non-negative.

---

## 8. Finding the Largest Positive Number

Sometimes we need to find the largest number that satisfies an additional condition.

For example, we may want the largest positive number in a collection.

### Example

```python
numbers = [-10, 5, 20, -3, 15]

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

**Output:**

```text
Largest positive number: 20
```

### Explanation

The program ignores zero and negative values.

Only values greater than zero are considered.

The first positive value becomes the initial maximum.

Each later positive value is compared with the current maximum.

### Why Use None?

Initially, no positive number has been found.

Therefore:

```python
largest_positive = None
```

represents the absence of a qualifying value.

This is better than using zero because zero is not positive.

### Example Without Positive Values

```python
numbers = [-10, -5, 0]

largest_positive = None

for number in numbers:
    if number > 0:
        if largest_positive is None or number > largest_positive:
            largest_positive = number

if largest_positive is None:
    print("No positive number found")
else:
    print(largest_positive)
```

**Output:**

```text
No positive number found
```

---

## 9. Finding the Largest Negative Number

Finding the largest negative number requires careful understanding.

Consider:

```python
numbers = [-25, -10, -40, -5, -15]
```

The largest negative number is:

```text
-5
```

Why?

Because -5 is greater than -10, -15, -25, and -40.

### Important Difference

| Number | Description |
|---:|---|
| -40 | Smallest value in this collection |
| -25 | Less than -10 |
| -15 | Less than -5 |
| -10 | Less than -5 |
| -5 | Largest negative value |

The largest negative number is the negative value closest to zero.

It is not the value with the greatest absolute magnitude.

### Code

```python
numbers = [-25, -10, -40, -5, -15]

largest_negative = None

for number in numbers:
    if number < 0:
        if largest_negative is None or number > largest_negative:
            largest_negative = number

print("Largest negative number:", largest_negative)
```

**Output:**

```text
Largest negative number: -5
```

### Explanation

The program considers only negative numbers.

It selects a value when it is greater than the current largest negative number.

### Important Point

Do not use the condition:

```python
abs(number) > abs(largest_negative)
```

when finding the largest negative number.

That condition finds a negative value with a greater absolute magnitude, which is a different problem.

---

## 10. Finding the Largest Even Number

We can combine even-number checking with maximum selection.

### Example

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

### Explanation

The first condition checks whether the current value is even.

The second condition checks whether that even value should update the current maximum.

Only even values are considered.

### Important Point

Initialize the variable with `None` rather than zero if the list may contain only negative even numbers.

For example:

```python
numbers = [-8, -4, -2]
```

The largest even value is `-2`.

---

## 11. Finding the Largest Odd Number

The same maximum-selection idea works for odd numbers.

### Example

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

### Explanation

The program ignores even values.

It considers only values whose remainder after division by two is non-zero.

Every qualifying number is compared with the current maximum.

### Important Point

The algorithm works for negative odd numbers too.

For example, among `[-9, -5, -3]`, the largest odd number is `-3`.

---

## 12. Finding the Highest Student Marks

Maximum selection is commonly used in student-result programs.

### Example

```python
marks = [78, 92, 85, 67, 95]

highest_marks = marks[0]

for student_marks in marks[1:]:
    if student_marks > highest_marks:
        highest_marks = student_marks

print("Highest marks:", highest_marks)
```

**Output:**

```text
Highest marks: 95
```

### Explanation

The first marks value is used as the starting maximum.

Every remaining student's marks are compared with it.

When a higher value is found, the maximum is updated.

### Validation

When accepting marks from users, it is important to validate their values.

For a marks system with a 0–100 range:

```python
marks = float(input("Enter marks: "))

if 0 <= marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")
```

### Important Point

The rules for marks validation depend on the examination system.

For this beginner example, the accepted range is 0 to 100.

---

## 13. Finding the Largest Absolute Value

Absolute value represents the non-negative magnitude of a number.

Examples:

| Number | Absolute Value |
|---:|---:|
| 10 | 10 |
| -10 | 10 |
| 25 | 25 |
| -25 | 25 |
| 0 | 0 |

Python provides the `abs()` function.

### Example

```python
numbers = [-10, 5, -30, 20]

largest_absolute = max(abs(number) for number in numbers)

print("Largest absolute value:", largest_absolute)
```

**Output:**

```text
Largest absolute value: 30
```

### Manual Loop Approach

```python
numbers = [-10, 5, -30, 20]

largest_absolute = abs(numbers[0])

for number in numbers[1:]:
    if abs(number) > largest_absolute:
        largest_absolute = abs(number)

print("Largest absolute value:", largest_absolute)
```

**Output:**

```text
Largest absolute value: 30
```

### Important Difference

The largest absolute value is not necessarily the largest original number.

For example:

```python
numbers = [-100, 50, 20]
```

The largest original number is:

```text
50
```

The largest absolute value is:

```text
100
```

Always understand what the question actually asks.

---

## 14. Finding the Largest Digit in a Number

Finding the largest digit is a useful beginner problem.

For example:

```text
Number: 5831
Largest digit: 8
```

A number can be converted into a string so that each digit can be examined.

### Example

```python
number = 5831

digits = str(abs(number))

largest_digit = 0

for digit in digits:
    current_digit = int(digit)

    if current_digit > largest_digit:
        largest_digit = current_digit

print("Largest digit:", largest_digit)
```

**Output:**

```text
Largest digit: 8
```

### Explanation

The integer is converted into a string.

Each character is converted back into an integer.

The current maximum digit is updated whenever a larger digit is found.

### Handling Negative Integers

The `abs()` function removes the negative sign before digit processing.

For example:

```python
number = -5831

digits = str(abs(number))
```

The digit sequence becomes:

```text
5831
```

### Important Point

The largest digit is always between 0 and 9.

A number containing only zeroes has largest digit zero.

---

## 15. Python's max() Function

Python provides a built-in function called `max()`.

It returns the largest item in an iterable or the largest among multiple arguments.

### Syntax

```python
max(iterable)
```

Or:

```python
max(value1, value2, value3)
```

### Example: Two Values

```python
print(max(10, 20))
```

**Output:**

```text
20
```

### Example: Three Values

```python
print(max(10, 25, 15))
```

**Output:**

```text
25
```

### Example: List

```python
numbers = [10, 25, 8, 40, 15]

print(max(numbers))
```

**Output:**

```text
40
```

### Example: Strings

```python
names = ["Amaan", "Ali", "Zara"]

print(max(names))
```

This compares strings using their ordering rules.

It does not select a name based on the length of the string.

### Handling an Empty Collection

Calling `max()` on an empty iterable without a default value raises a `ValueError`.

One approach is to check the collection first:

```python
numbers = []

if numbers:
    print(max(numbers))
else:
    print("No values available")
```

Another approach is to use the `default` argument with an iterable:

```python
numbers = []

largest = max(numbers, default=None)

print(largest)
```

**Output:**

```text
None
```

### Why Learn the Manual Method?

Although `max()` is convenient, understanding the manual method teaches:

- Comparisons.
- Loops.
- Variable updates.
- Maximum selection.
- Array traversal.
- Algorithmic thinking.

These concepts are important in DSA.

---

## 16. Handling Equal Maximum Values

Sometimes multiple values share the maximum value.

Example:

```python
numbers = [10, 50, 20, 50, 30]
```

The maximum is 50.

However, 50 appears twice.

A question may ask only for the largest value, or it may also ask for the number of occurrences or positions.

### Finding the Maximum Value

```python
largest = max(numbers)

print(largest)
```

**Output:**

```text
50
```

### Counting Maximum Occurrences

```python
largest = max(numbers)

count = numbers.count(largest)

print("Largest:", largest)
print("Occurrences:", count)
```

**Output:**

```text
Largest: 50
Occurrences: 2
```

### Finding All Maximum Positions

```python
numbers = [10, 50, 20, 50, 30]

largest = max(numbers)

positions = []

for index in range(len(numbers)):
    if numbers[index] == largest:
        positions.append(index)

print("Largest:", largest)
print("Positions:", positions)
```

**Output:**

```text
Largest: 50
Positions: [1, 3]
```

### Important Difference

Finding the maximum value, counting its occurrences, and finding its positions are three different tasks.

Read the problem statement carefully before choosing the approach.

---

## 17. Nested If vs If-Elif-Else for Largest Number

Both structures can solve maximum-selection problems.

### Nested If

```python
a = 10
b = 20
c = 15

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print(largest)
```

### If-Elif-Else

```python
a = 10
b = 20
c = 15

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(largest)
```

### Comparison

| Feature | Nested If | If-Elif-Else |
|---|---|---|
| Main structure | Conditions inside conditions | Multiple branches |
| Decision style | Hierarchical comparison | Alternative comparisons |
| Indentation | Multiple levels | Usually one level |
| Readability | Can be harder with deeper nesting | Often clearer |
| Typical use | Dependent conditions | Multiple alternative conditions |

### Best Practice

For beginner problems involving three numbers, either approach is suitable.

Choose the approach that makes the comparison logic easiest to understand.

For larger collections, a loop is usually more practical.

---

## 18. Maximum Selection Without Sorting

One common beginner mistake is sorting the entire list just to find the largest value.

Sorting is not necessary when only the maximum value is required.

### Sorting Approach

```python
numbers = [10, 25, 8, 40, 15]

numbers.sort()

largest = numbers[-1]

print(largest)
```

**Output:**

```text
40
```

This works, but it rearranges the list and performs more work than necessary.

### Single-Traversal Approach

```python
numbers = [10, 25, 8, 40, 15]

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print(largest)
```

**Output:**

```text
40
```

### Complexity Difference

For a collection containing `n` values:

- Finding the maximum by one traversal takes \(O(n)\) time.
- Sorting generally takes \(O(n \log n)\) time.

When only the maximum is required, the single-traversal method is more efficient.

---

# SECTION 1: TWELVE PYTHON EXAMPLES

## Example 1: Largest of Two Numbers

### Objective

Find the largest of two numbers using an `if-else` statement.

### Code

```python
a = 25
b = 40

if a > b:
    largest = a
else:
    largest = b

print("A:", a)
print("B:", b)
print("Largest:", largest)
```

### Output

```text
A: 25
B: 40
Largest: 40
```

### Explanation

The program compares the first and second values.

Since 25 is smaller than 40, the `else` block assigns B to `largest`.

### Concepts Used

- If-else.
- Greater-than operator.
- Variable assignment.

---

## Example 2: Largest Using Conditional Expression

### Objective

Find the largest of two numbers using the ternary operator.

### Code

```python
a = 15
b = 35

largest = a if a > b else b

print("A:", a)
print("B:", b)
print("Largest:", largest)
```

### Output

```text
A: 15
B: 35
Largest: 35
```

### Explanation

Python checks whether A is greater than B.

The condition is false, so B is selected.

The result is assigned directly to `largest`.

### Concepts Used

- Conditional expression.
- Comparison.
- Assignment.

---

## Example 3: Largest of Three Using Nested If

### Objective

Find the largest of three numbers using nested conditions.

### Code

```python
a = 25
b = 50
c = 35

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("Largest:", largest)
```

### Output

```text
Largest: 50
```

### Explanation

The program compares A with B.

Since A is not greater than B, it compares B with C.

B is greater than C.

Therefore, B is selected.

### Concepts Used

- Nested if.
- Multiple comparisons.
- Conditional assignment.

---

## Example 4: Largest Using If-Elif-Else

### Objective

Find the largest among three numbers using `if-elif-else`.

### Code

```python
a = 70
b = 45
c = 30

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

### Output

```text
Largest: 70
```

### Explanation

The first condition checks whether A is greater than or equal to both B and C.

Both comparisons are true.

Therefore, A is the largest value.

### Concepts Used

- If-elif-else.
- Logical AND.
- Greater-than-or-equal operator.

---

## Example 5: Equal Numbers

### Objective

Find the largest number and identify whether values are equal.

### Code

```python
a = 50
b = 50
c = 30

largest = max(a, b, c)

print("Largest:", largest)

if a == b == c:
    print("All three numbers are equal")
elif a == b or b == c or a == c:
    print("At least two numbers are equal")
else:
    print("All numbers are different")
```

### Output

```text
Largest: 50
At least two numbers are equal
```

### Explanation

The program first calculates the maximum value.

It then checks whether all numbers are equal.

If not, it checks whether any pair of numbers is equal.

### Concepts Used

- `max()`.
- Equality operator.
- Logical OR.
- Chained comparison.

---

## Example 6: Largest Number in a List

### Objective

Find the largest number using a loop.

### Code

```python
numbers = [10, 25, 8, 40, 15]

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest number:", largest)
```

### Output

```text
Numbers: [10, 25, 8, 40, 15]
Largest number: 40
```

### Explanation

The first value becomes the starting maximum.

Every remaining value is compared with it.

The maximum is updated when a larger number appears.

### Concepts Used

- List.
- For loop.
- Maximum selection.
- Comparison operators.

---

## Example 7: Largest Using max() Function

### Objective

Find the largest value using Python's built-in `max()` function.

### Code

```python
numbers = [12, 45, 23, 67, 34]

largest = max(numbers)

print("Numbers:", numbers)
print("Largest number:", largest)
```

### Output

```text
Numbers: [12, 45, 23, 67, 34]
Largest number: 67
```

### Explanation

The `max()` function examines the iterable and returns its greatest value.

### Concepts Used

- Built-in functions.
- Lists.
- Maximum selection.

---

## Example 8: Largest Positive Number

### Objective

Find the largest positive number in a list.

### Code

```python
numbers = [-10, 5, 20, -3, 15]

largest = None

for number in numbers:
    if number > 0:
        if largest is None or number > largest:
            largest = number

if largest is None:
    print("No positive number found")
else:
    print("Largest positive number:", largest)
```

### Output

```text
Largest positive number: 20
```

### Explanation

Negative values and zero are ignored.

Only positive values are considered.

The maximum positive value is 20.

### Concepts Used

- Nested if.
- None.
- List traversal.
- Maximum selection.

---

## Example 9: Largest Negative Number

### Objective

Find the largest negative value.

### Code

```python
numbers = [-25, -10, -40, -5, -15]

largest = None

for number in numbers:
    if number < 0:
        if largest is None or number > largest:
            largest = number

if largest is None:
    print("No negative number found")
else:
    print("Largest negative number:", largest)
```

### Output

```text
Largest negative number: -5
```

### Explanation

The program ignores non-negative numbers.

Among negative values, the greatest numerical value is selected.

Remember that -5 is greater than -10.

### Concepts Used

- Negative number comparison.
- Nested if.
- None.
- Maximum selection.

---

## Example 10: Largest Even Number

### Objective

Find the largest even number from a list.

### Code

```python
numbers = [12, 25, 18, 31, 40, 17]

largest = None

for number in numbers:
    if number % 2 == 0:
        if largest is None or number > largest:
            largest = number

if largest is None:
    print("No even number found")
else:
    print("Largest even number:", largest)
```

### Output

```text
Largest even number: 40
```

### Explanation

Only values divisible by two are considered.

The program compares those even values to find the largest.

### Concepts Used

- Modulus operator.
- Nested if.
- Filtering.
- Maximum selection.

---

## Example 11: Largest Odd Number

### Objective

Find the largest odd number from a list.

### Code

```python
numbers = [12, 25, 18, 31, 40, 17]

largest = None

for number in numbers:
    if number % 2 != 0:
        if largest is None or number > largest:
            largest = number

if largest is None:
    print("No odd number found")
else:
    print("Largest odd number:", largest)
```

### Output

```text
Largest odd number: 31
```

### Explanation

Only odd values are considered.

The maximum among the odd values is 31.

### Concepts Used

- Modulus operator.
- Conditional statements.
- Lists.
- Maximum selection.

---

## Example 12: Highest Student Marks

### Objective

Find the highest marks among multiple students.

### Code

```python
marks = [78, 92, 85, 67, 95]

highest_marks = marks[0]

for student_marks in marks[1:]:
    if student_marks > highest_marks:
        highest_marks = student_marks

print("Student marks:", marks)
print("Highest marks:", highest_marks)
```

### Output

```text
Student marks: [78, 92, 85, 67, 95]
Highest marks: 95
```

### Explanation

The program starts with the first marks value.

Every later marks value is compared with the current maximum.

The highest value found is 95.

### Concepts Used

- List traversal.
- Maximum selection.
- Comparison operators.
- Student-result logic.

---

# SECTION 2: TWELVE SOLVED PROBLEMS

## Problem 1: Largest of Two Numbers

### Problem Statement

Write a Python program that accepts two integers and finds the largest.

Also handle the situation where both integers are equal.

### Logic

1. Accept the first integer.
2. Accept the second integer.
3. Compare the numbers.
4. Select the larger value.
5. If both are equal, display the equality message.

### Code

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

if a > b:
    largest = a
elif b > a:
    largest = b
else:
    largest = a

print("First number:", a)
print("Second number:", b)
print("Largest number:", largest)

if a == b:
    print("Both numbers are equal")
```

### Sample Input

```text
Enter first integer: 10
Enter second integer: 25
```

### Expected Output

```text
First number: 10
Second number: 25
Largest number: 25
```

### Explanation

The program compares the two values.

Because 25 is greater than 10, it becomes the maximum value.

When both values are equal, the program still reports their common value and identifies the equality.

### Concepts Used

- If-elif-else.
- Comparison operators.
- Equality checking.
- Integer input.

---

## Problem 2: Largest of Three Numbers

### Problem Statement

Accept three integers and find the largest value.

### Logic

1. Accept three integers.
2. Compare the first number with the other two.
3. If it is the largest, select it.
4. Otherwise, compare the second number with the other two.
5. If the second is the largest, select it.
6. Otherwise, select the third number.

### Code

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Numbers:", a, b, c)
print("Largest number:", largest)
```

### Sample Input

```text
Enter first integer: 25
Enter second integer: 50
Enter third integer: 35
```

### Expected Output

```text
Numbers: 25 50 35
Largest number: 50
```

### Explanation

The program uses two comparisons joined by `and`.

The first condition checks whether A is the maximum.

The second checks whether B is the maximum.

If neither is selected, C is the maximum.

The use of `>=` allows equal maximum values.

### Concepts Used

- If-elif-else.
- Logical AND.
- Comparison operators.
- Multiple values.

---

## Problem 3: Largest of Multiple Numbers

### Problem Statement

Accept multiple numbers and find the largest value using a loop.

### Logic

1. Ask how many values the user wants to enter.
2. Read the values into a list.
3. Initialize the maximum with the first value.
4. Traverse the remaining values.
5. Update the maximum when a larger value is found.
6. Display the result.

### Code

```python
count = int(input("How many numbers? "))

numbers = []

for index in range(count):
    number = float(input(f"Enter number {index + 1}: "))
    numbers.append(number)

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest number:", largest)
```

### Sample Input

```text
How many numbers? 5
Enter number 1: 10
Enter number 2: 25
Enter number 3: 8
Enter number 4: 40
Enter number 5: 15
```

### Expected Output

```text
Numbers: [10.0, 25.0, 8.0, 40.0, 15.0]
Largest number: 40.0
```

### Explanation

The first list element is selected as the initial maximum.

The remaining elements are checked one by one.

Whenever a larger value appears, the maximum is updated.

### Concepts Used

- List.
- For loop.
- Input.
- Maximum selection.

---

## Problem 4: Largest Positive Number

### Problem Statement

Accept multiple numbers and find the largest positive value.

Ignore zero and negative numbers.

### Logic

1. Accept a collection.
2. Initialize the result with `None`.
3. Check whether each value is positive.
4. Compare positive values.
5. Update the maximum.
6. Display the maximum or report that no positive value exists.

### Code

```python
numbers = [-10, 5, 20, -3, 15]

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

### Expected Output

```text
Largest positive number: 20
```

### Explanation

The program considers only values greater than zero.

The maximum among those values is 20.

### Concepts Used

- Positive-number checking.
- Nested if.
- None.
- Maximum selection.

---

## Problem 5: Largest Negative Number

### Problem Statement

Accept multiple numbers and find the largest negative value.

### Logic

1. Accept a collection of numbers.
2. Initialize the result with `None`.
3. Consider only negative values.
4. Compare each negative value with the current maximum.
5. Update the maximum.
6. Display the result.

### Code

```python
numbers = [-25, -10, -40, -5, -15]

largest_negative = None

for number in numbers:
    if number < 0:
        if largest_negative is None or number > largest_negative:
            largest_negative = number

if largest_negative is None:
    print("No negative number found")
else:
    print("Largest negative number:", largest_negative)
```

### Expected Output

```text
Largest negative number: -5
```

### Explanation

Among negative numbers, the value nearest to zero is numerically the largest.

Therefore, -5 is the result.

### Concepts Used

- Negative-number classification.
- Comparison.
- Nested conditions.
- Maximum selection.

---

## Problem 6: Largest Even Number

### Problem Statement

Find the largest even integer in a list.

### Logic

1. Accept a collection of integers.
2. Initialize the result with `None`.
3. Check whether each value is even.
4. If even, compare it with the current maximum.
5. Update the maximum.
6. Display the result.

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

Only numbers divisible by two are considered.

The even numbers are:

```text
12, 18, 40
```

The largest value is 40.

### Concepts Used

- Modulus operator.
- Nested if.
- Lists.
- Maximum selection.

---

## Problem 7: Largest Odd Number

### Problem Statement

Find the largest odd integer in a list.

### Logic

1. Accept a collection of integers.
2. Initialize the result with `None`.
3. Check whether each value is odd.
4. Compare odd values.
5. Update the maximum.
6. Display the result.

### Code

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

### Expected Output

```text
Largest odd number: 31
```

### Explanation

Only odd numbers are processed.

The odd values are:

```text
25, 31, 17
```

The largest is 31.

### Concepts Used

- Modulus operator.
- List traversal.
- Nested conditions.
- Maximum selection.

---

## Problem 8: Largest with Duplicates

### Problem Statement

Find the largest value and count how many times it occurs.

### Logic

1. Accept multiple values.
2. Find the maximum.
3. Count occurrences of that maximum.
4. Display both results.

### Code

```python
numbers = [10, 50, 20, 50, 30]

largest = max(numbers)

occurrences = numbers.count(largest)

print("Numbers:", numbers)
print("Largest number:", largest)
print("Occurrences:", occurrences)
```

### Expected Output

```text
Numbers: [10, 50, 20, 50, 30]
Largest number: 50
Occurrences: 2
```

### Explanation

The `max()` function returns 50.

The `count()` method checks how many times 50 appears in the list.

It appears twice.

### Concepts Used

- `max()`.
- `count()`.
- Lists.
- Duplicate values.

---

## Problem 9: Largest of Four Numbers

### Problem Statement

Accept four integers and determine the largest value.

### Logic

1. Accept four integers.
2. Initialize the maximum with the first number.
3. Compare the second, third, and fourth numbers.
4. Update the maximum whenever a greater number appears.
5. Display the result.

### Code

```python
numbers = []

for index in range(4):
    number = int(input(f"Enter number {index + 1}: "))
    numbers.append(number)

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest number:", largest)
```

### Sample Input

```text
Enter number 1: 10
Enter number 2: 40
Enter number 3: 25
Enter number 4: 30
```

### Expected Output

```text
Numbers: [10, 40, 25, 30]
Largest number: 40
```

### Explanation

The program processes the first value as the initial maximum.

It checks every remaining value and updates the maximum when needed.

### Concepts Used

- Lists.
- For loop.
- Maximum selection.
- Comparison.

---

## Problem 10: Highest Student Marks

### Problem Statement

Accept the marks of multiple students and find the highest marks.

For this example, marks must be between zero and 100.

### Logic

1. Accept the number of students.
2. Read marks for each student.
3. Validate every marks value.
4. Store the valid values.
5. Find the maximum.
6. Display the highest marks.

### Code

```python
count = int(input("Enter number of students: "))

marks_list = []

for index in range(count):
    marks = float(input(f"Enter marks for student {index + 1}: "))

    if 0 <= marks <= 100:
        marks_list.append(marks)
    else:
        print("Invalid marks")
        break

if len(marks_list) == count:
    highest_marks = marks_list[0]

    for marks in marks_list[1:]:
        if marks > highest_marks:
            highest_marks = marks

    print("Student marks:", marks_list)
    print("Highest marks:", highest_marks)
```

### Sample Input

```text
Enter number of students: 5
Enter marks for student 1: 78
Enter marks for student 2: 92
Enter marks for student 3: 85
Enter marks for student 4: 67
Enter marks for student 5: 95
```

### Expected Output

```text
Student marks: [78.0, 92.0, 85.0, 67.0, 95.0]
Highest marks: 95.0
```

### Explanation

The program accepts marks for every student.

Each value must satisfy the valid range.

After all valid inputs are stored, the maximum is selected.

### Concepts Used

- Input validation.
- For loop.
- Lists.
- Comparison operators.

---

## Problem 11: Largest Absolute Value

### Problem Statement

Accept multiple numbers and find the largest absolute value.

### Logic

1. Accept a collection of numbers.
2. Calculate the absolute value of the first number.
3. Compare the absolute values of remaining numbers.
4. Update the maximum magnitude.
5. Display the result.

### Code

```python
numbers = [-10, 5, -30, 20]

largest_absolute = abs(numbers[0])

for number in numbers[1:]:
    if abs(number) > largest_absolute:
        largest_absolute = abs(number)

print("Numbers:", numbers)
print("Largest absolute value:", largest_absolute)
```

### Expected Output

```text
Numbers: [-10, 5, -30, 20]
Largest absolute value: 30
```

### Explanation

The absolute values are:

```text
10, 5, 30, 20
```

The largest absolute value is 30.

The original number that produced it is -30.

### Important Point

The program returns the magnitude, not necessarily the original signed number.

### Concepts Used

- `abs()`.
- List traversal.
- Maximum selection.
- Comparison operators.

---

## Problem 12: Largest Digit in an Integer

### Problem Statement

Accept an integer and find its largest digit.

### Logic

1. Accept an integer.
2. Convert its absolute value into a string.
3. Initialize the largest digit to zero.
4. Traverse each digit.
5. Convert the character into an integer.
6. Update the largest digit when a greater digit appears.
7. Display the answer.

### Code

```python
number = int(input("Enter an integer: "))

digits = str(abs(number))

largest_digit = 0

for digit in digits:
    current_digit = int(digit)

    if current_digit > largest_digit:
        largest_digit = current_digit

print("Original number:", number)
print("Largest digit:", largest_digit)
```

### Sample Input

```text
Enter an integer: 5831
```

### Expected Output

```text
Original number: 5831
Largest digit: 8
```

### Explanation

The digits are:

```text
5, 8, 3, 1
```

The maximum digit is 8.

For a negative number, `abs()` removes the sign before the digits are processed.

### Concepts Used

- Integer-to-string conversion.
- Absolute value.
- For loop.
- Maximum selection.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving these questions independently.

Use the logic covered in this topic.

## Question 1: Smallest of Multiple Numbers

Accept multiple numbers and find the smallest value.

### Requirements

- Accept at least one number.
- Store the numbers in a list.
- Initialize the minimum correctly.
- Compare remaining values.
- Display the smallest value.

### Concepts

- Lists.
- For loop.
- Comparison.
- Minimum selection.

## Question 2: Second Largest Number

Accept a list of integers and find the second largest distinct number.

### Requirements

- Accept multiple integers.
- Identify the largest value.
- Find the next distinct largest value.
- Handle duplicate maximum values.
- Handle a collection with fewer than two distinct values.

### Concepts

- Maximum selection.
- Comparison.
- List traversal.
- Duplicate handling.

## Question 3: Largest Number Without max()

Find the largest number in a collection without using Python's built-in `max()` function.

### Requirements

- Accept multiple numbers.
- Use a loop.
- Maintain a current maximum.
- Display the final result.

### Concepts

- Loops.
- Conditional statements.
- Maximum selection.

## Question 4: Largest Number in a Matrix

Accept a two-dimensional list and find its largest value.

### Requirements

- Create a matrix.
- Traverse each row.
- Examine every element.
- Update the maximum.
- Display the result.

### Concepts

- Nested lists.
- Nested loops.
- Conditional statements.
- Matrix traversal.

## Question 5: Second Highest Marks

Accept multiple student marks and find the second highest distinct marks value.

### Requirements

- Accept marks within the valid range.
- Store all valid marks.
- Find the largest distinct value.
- Find the second largest distinct value.
- Handle ties and insufficient distinct values.

### Concepts

- Lists.
- Maximum selection.
- Duplicate handling.
- Input validation.

## Question 6: Largest Positive Even Number

Accept a collection of integers and find the largest value satisfying both conditions:

- It is positive.
- It is even.

### Requirements

- Accept integers.
- Ignore zero.
- Ignore negative values.
- Ignore odd values.
- Find the largest qualifying value.
- Handle a collection without qualifying values.

### Concepts

- Nested conditions.
- Modulus operator.
- Comparison.
- Maximum selection.

## Question 7: Largest Negative Odd Number

Accept a collection of integers and find the largest negative odd value.

### Requirements

- Consider only negative numbers.
- Consider only odd numbers.
- Compare qualifying values.
- Display the maximum negative odd value.
- Handle a collection without qualifying values.

### Concepts

- Negative-number checking.
- Odd-number checking.
- Logical conditions.
- Maximum selection.

## Question 8: Largest Digit in a Number

Accept an integer and identify its largest digit.

### Requirements

- Accept positive or negative integers.
- Ignore the negative sign.
- Examine every digit.
- Find the maximum digit.
- Display the result.

### Concepts

- Strings.
- Integer conversion.
- Loop.
- Maximum selection.

## Question 9: Largest Difference

Find the largest difference between two values in a collection.

### Requirements

- Accept multiple integers.
- Identify the smallest value.
- Identify the largest value.
- Calculate the difference between them.
- Display the result.

### Concepts

- Maximum.
- Minimum.
- Arithmetic operations.
- List traversal.

Clarify whether the question requires the difference between any two values without order or the maximum-minus-minimum range.

## Question 10: Find Largest and Its Position

Accept a collection of numbers.

Find the largest value and display every index where it occurs.

### Requirements

- Accept multiple numbers.
- Find the maximum.
- Traverse the list.
- Identify every position containing the maximum.
- Display the maximum and positions.

### Concepts

- Lists.
- Maximum selection.
- Equality comparison.
- Index tracking.

---

# SECTION 4: COMMON MISTAKES

## Mistake 1: Incorrect Comparison Operator

Incorrect:

```python
if a < b:
    largest = a
```

This selects the smaller value, not the largest.

Correct:

```python
if a > b:
    largest = a
else:
    largest = b
```

## Mistake 2: Incorrect Logical Condition

Incorrect:

```python
if a > b or a > c:
    largest = a
```

This condition only requires A to be greater than one of the other values.

It does not guarantee that A is the largest.

Correct:

```python
if a >= b and a >= c:
    largest = a
```

Both comparisons must be true.

## Mistake 3: Ignoring Equal Values

Consider:

```python
a = 50
b = 50
c = 30
```

A maximum algorithm should correctly return 50.

If the problem also asks which values are equal, handle that separately.

## Mistake 4: Initializing the Largest Value to Zero

Incorrect for general numbers:

```python
largest = 0
```

This fails when every number is negative.

Example:

```python
numbers = [-10, -5, -20]
```

The maximum is -5.

A better initialization is:

```python
largest = numbers[0]
```

## Mistake 5: Initializing a Restricted Maximum Incorrectly

For the largest positive number, zero is not a valid result.

For the largest negative number, zero is also not a valid result.

Use:

```python
largest = None
```

until a qualifying value is found.

## Mistake 6: Confusing Largest Negative with Most Negative

For:

```python
numbers = [-20, -5, -15]
```

The largest negative number is -5.

The smallest value is -20.

These are different questions.

## Mistake 7: Confusing Largest Number with Largest Absolute Value

For:

```python
numbers = [-100, 50, 20]
```

The largest number is 50.

The largest absolute value is 100.

Always understand the requested comparison.

## Mistake 8: Updating the Maximum Incorrectly

Incorrect:

```python
for number in numbers:
    if number > largest:
        largest = numbers[0]
```

This keeps assigning the first element.

Correct:

```python
for number in numbers:
    if number > largest:
        largest = number
```

## Mistake 9: Resetting the Maximum Inside the Loop

Incorrect:

```python
for number in numbers:
    largest = numbers[0]

    if number > largest:
        largest = number
```

The maximum is reset on every iteration.

Correct:

```python
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number
```

## Mistake 10: Accessing an Empty List

Incorrect:

```python
numbers = []

largest = numbers[0]
```

This produces an `IndexError`.

Check whether the list contains elements before accessing its first element.

## Mistake 11: Sorting Without Need

Sorting a collection just to find its largest value performs unnecessary work.

A single traversal is sufficient.

## Mistake 12: Returning the Wrong Result for Largest Digit

The largest digit should be between 0 and 9.

Do not accidentally compare the original multi-digit number against an individual digit.

Convert and compare individual digits correctly.

## Mistake 13: Using Invalid Input Types

A string cannot always be compared directly with a number.

Convert input using `int()` or `float()` as appropriate.

## Mistake 14: Ignoring the Tie Requirement

Some problems need only the maximum value.

Others require all positions containing that maximum.

Read the problem statement carefully.

## Mistake 15: Using `>` When `>=` Is Required

When checking whether a candidate is at least as large as other values, `>=` may be more suitable.

The correct operator depends on whether equal values should be included in the comparison.

---

# SECTION 5: BEST PRACTICES

Follow these guidelines when writing largest-number programs.

1. Understand whether the problem asks for the largest value, largest positive value, largest negative value, or largest absolute value.
2. Use meaningful variable names.
3. Use correct comparison operators.
4. Use `and` when all required conditions must be satisfied.
5. Initialize the maximum using a valid first value when the collection is non-empty.
6. Use `None` when searching for a restricted category.
7. Do not initialize a general maximum to zero.
8. Handle empty collections.
9. Handle duplicate maximum values when required.
10. Use a loop for multiple values.
11. Avoid sorting when only the maximum is required.
12. Use Python's `max()` when manual algorithm implementation is not required.
13. Learn the manual loop approach for DSA.
14. Keep the maximum update inside the correct loop.
15. Do not reset the maximum during traversal.
16. Validate numeric input.
17. Validate marks or other values according to their accepted range.
18. Use separate functions for reusable operations.
19. Keep conditions readable.
20. Test lists containing negative values.
21. Test lists containing equal values.
22. Test lists containing only one element.
23. Test lists containing only positive or only negative values.
24. Check restricted searches with no matching value.
25. Keep the return value's meaning clear.

### Good Example: Reusable Function

```python
def find_largest(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest
```

### Usage

```python
numbers = [10, 25, 8, 40, 15]

print(find_largest(numbers))
```

**Output:**

```text
40
```

The function can be reused wherever a maximum value is needed.

---

# SECTION 6: DEBUGGING

Debugging means identifying and fixing errors in a program.

Maximum-selection programs are useful for learning debugging because a small comparison mistake can produce an incorrect result.

## 1. Check the Comparison

Make sure you are selecting the larger value.

Correct:

```python
if number > largest:
    largest = number
```

## 2. Check Initialization

Initialize the maximum correctly.

For a non-empty list:

```python
largest = numbers[0]
```

For a restricted search:

```python
largest_positive = None
```

## 3. Check Loop Placement

The maximum initialization should happen before the loop.

The comparison and update should happen inside the loop.

## 4. Check the Update

When a larger candidate is found, assign that candidate to the maximum variable.

## 5. Check Negative Values

Use negative-only examples to test whether the algorithm works when all input values are below zero.

## 6. Check Equal Values

Try collections with repeated maximum values.

## 7. Check Empty Collections

If the function accepts arbitrary lists, it should handle the empty-list case.

## 8. Check Input Conversion

The input function returns a string.

Convert user input to a numeric data type before comparing values.

## 9. Common Python Errors

| Error | Meaning |
|---|---|
| `ValueError` | Invalid value during conversion |
| `TypeError` | An operation uses incompatible data types |
| `IndexError` | An invalid list index is accessed |
| `NameError` | A variable has not been defined |
| `IndentationError` | Incorrect indentation |
| `SyntaxError` | Invalid Python syntax |

## 10. Debugging Checklist

Before considering your program complete:

- Check that the correct values are being accepted.
- Check the initial maximum.
- Check that every required element is processed.
- Check that the maximum is updated correctly.
- Check the comparison operator.
- Check equal values.
- Check negative values.
- Check empty collections.
- Check whether restricted values are filtered correctly.
- Check whether the correct result is displayed.

---

# SECTION 7: REAL-LIFE APPLICATIONS

Finding the largest value is useful in many software applications.

## 1. Student Management Systems

A college application may find:

- Highest marks.
- Highest percentage.
- Highest attendance.
- Highest examination score.

Example:

```python
marks = [78, 92, 85, 67, 95]

highest_marks = max(marks)

print("Highest marks:", highest_marks)
```

## 2. Banking Applications

A banking application may identify the largest transaction in a group of transactions.

## 3. E-Commerce Applications

An online store may find the highest product price or largest order amount.

## 4. Inventory Management

An inventory application may find the product with the highest stock quantity.

## 5. Employee Management

A company may identify the highest salary or highest performance score.

## 6. Sports Applications

A sports application may identify the highest score, fastest recorded speed, or maximum performance statistic.

## 7. Data Analysis

Data analysis programs frequently find maximum values in datasets.

For example, a sales dataset may be checked for the highest daily sales amount.

## 8. Weather Applications

A weather application may identify the maximum temperature recorded during a selected period.

## 9. Financial Applications

A financial system may compare the largest transaction amount, highest return, or maximum recorded loss magnitude.

## 10. Search and Ranking Systems

Applications may compare scores or ratings to select the highest-ranked result.

## 11. Gaming Applications

A game may maintain the highest score achieved by a player.

## 12. Sensor Systems

A sensor-monitoring application may identify the maximum measurement recorded over a period.

### Important Point

The meaning of "largest" depends on what is being compared.

It might mean:

- Largest numerical value.
- Largest absolute magnitude.
- Highest score.
- Highest price.
- Highest frequency.
- Highest measurement.

Always understand the data before choosing the comparison.

---

# SECTION 8: DSA CONNECTION

Finding the largest number is an important beginner-level Data Structures and Algorithms problem.

It introduces a pattern that appears in many array and list problems.

## 1. Array Traversal

An array can contain several numbers.

To find the maximum, the algorithm visits each element.

```python
numbers = [10, 25, 8, 40, 15]

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print(largest)
```

This is a basic linear traversal.

## 2. Searching

Maximum selection is related to searching because every element is checked for whether it improves the current result.

## 3. Minimum Selection

The same approach can find the minimum.

```python
smallest = numbers[0]

for number in numbers[1:]:
    if number < smallest:
        smallest = number
```

The comparison direction changes.

## 4. Second Largest Number

Second-largest problems build on maximum selection.

They may require tracking two distinct maximum values.

## 5. Filtering

Finding the largest even number combines filtering with maximum selection.

## 6. Frequency and Duplicates

Counting how many times the maximum occurs introduces frequency counting.

## 7. Matrix Traversal

A matrix can be traversed using nested loops to find its largest element.

## 8. Sorting Algorithms

Understanding maximum selection helps when learning sorting algorithms.

Some sorting approaches repeatedly identify the maximum or minimum remaining value.

### DSA Skills Developed

- Array traversal.
- List traversal.
- Searching.
- Maximum selection.
- Minimum selection.
- Conditional comparison.
- Duplicate handling.
- Filtering.
- Frequency counting.
- Matrix traversal.
- Algorithm design.
- Complexity analysis.

### Important DSA Practice

Learn to solve the maximum problem without using `max()`.

Understand why one traversal is enough.

This idea will help you solve many array-based problems.

---

# SECTION 9: TIME AND SPACE COMPLEXITY

Time complexity describes how the number of operations grows with the input size.

Space complexity describes the additional memory used by an algorithm.

## 1. Largest of Two Numbers

Consider:

```python
a = 10
b = 20

if a > b:
    largest = a
else:
    largest = b
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

## 2. Largest of Three Numbers

A fixed number of comparisons is required.

Time complexity:

\[
O(1)
\]

Additional space complexity:

\[
O(1)
\]

## 3. Largest of Multiple Numbers

Consider:

```python
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number
```

The algorithm processes every remaining element once.

For `n` values, its time complexity is:

\[
O(n)
\]

The algorithm maintains only one maximum variable.

Its additional space complexity is:

\[
O(1)
\]

The given code uses a slice, `numbers[1:]`, which creates a new list in Python. That slice requires \(O(n)\) additional space in the worst case. A more space-efficient traversal uses indexes or an iterator without creating that slice.

## 4. Largest Positive Number

The program checks each element once and only updates the maximum for positive values.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 5. Largest Negative Number

The program also performs one traversal.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 6. Largest Even or Odd Number

Every element is examined once.

Time complexity:

\[
O(n)
\]

Additional space complexity:

\[
O(1)
\]

## 7. Largest Number Using max()

For a normal Python list, finding the maximum requires examining the values.

Time complexity:

\[
O(n)
\]

Additional space complexity for the operation is generally:

\[
O(1)
\]

## 8. Largest Digit in an Integer

If a number contains `d` decimal digits, the algorithm examines each digit.

Time complexity:

\[
O(d)
\]

The string representation of the digits also requires space proportional to the number of digits.

Additional space complexity:

\[
O(d)
\]

### Complexity Summary

| Problem | Time Complexity | Additional Space |
|---|---:|---:|
| Largest of two | \(O(1)\) | \(O(1)\) |
| Largest of three | \(O(1)\) | \(O(1)\) |
| Largest of four | \(O(1)\) | \(O(1)\) |
| Largest of `n` values | \(O(n)\) | \(O(1)\) with iterator/index traversal |
| Largest positive | \(O(n)\) | \(O(1)\) |
| Largest negative | \(O(n)\) | \(O(1)\) |
| Largest even | \(O(n)\) | \(O(1)\) |
| Largest odd | \(O(n)\) | \(O(1)\) |
| Largest using `max()` | \(O(n)\) | \(O(1)\) auxiliary space in the usual list case |
| Largest digit | \(O(d)\) | \(O(d)\) for string conversion |

### Important Point

Sorting a collection only to find the largest value is generally unnecessary.

A sorting algorithm generally requires:

\[
O(n \log n)
\]

time for common comparison-based efficient sorting algorithms.

A single traversal can find the maximum in:

\[
O(n)
\]

time.

---

# SECTION 10: MINI PROJECT – STUDENT PERFORMANCE ANALYSIS SYSTEM

## Project Overview

Create a simple student performance analysis program.

The program accepts the marks of multiple students and displays:

1. All student marks.
2. Highest marks.
3. Lowest marks.
4. Number of students.
5. Number of students who achieved the highest marks.

This project uses maximum and minimum selection.

### Example Rules

- Marks must be between 0 and 100.
- At least one student must be entered.
- The highest marks may occur more than once.

## Python Code

```python
def read_marks(prompt):
    while True:
        try:
            marks = float(input(prompt))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter valid numeric marks.")


count = int(input("Enter number of students: "))

if count < 1:
    print("At least one student is required.")

else:
    marks_list = []

    for index in range(count):
        marks = read_marks(
            f"Enter marks for student {index + 1}: "
        )

        marks_list.append(marks)

    highest_marks = marks_list[0]
    lowest_marks = marks_list[0]

    for marks in marks_list[1:]:

        if marks > highest_marks:
            highest_marks = marks

        if marks < lowest_marks:
            lowest_marks = marks

    highest_count = marks_list.count(highest_marks)

    print("\nSTUDENT PERFORMANCE REPORT")
    print("=" * 40)

    print("Student marks:", marks_list)
    print("Total students:", len(marks_list))
    print("Highest marks:", highest_marks)
    print("Lowest marks:", lowest_marks)
    print("Students with highest marks:", highest_count)
```

## Sample Input

```text
Enter number of students: 5
Enter marks for student 1: 78
Enter marks for student 2: 92
Enter marks for student 3: 85
Enter marks for student 4: 67
Enter marks for student 5: 95
```

## Expected Output

```text
STUDENT PERFORMANCE REPORT
========================================
Student marks: [78.0, 92.0, 85.0, 67.0, 95.0]
Total students: 5
Highest marks: 95.0
Lowest marks: 67.0
Students with highest marks: 1
```

## Project Explanation

The program first accepts the number of students.

It then collects valid marks.

The first student's marks initialize both the highest and lowest values.

The program traverses the remaining marks.

Whenever a value is greater than the current maximum, the maximum is updated.

Whenever a value is smaller than the current minimum, the minimum is updated.

After processing all marks, the program counts how many times the maximum occurs.

Finally, it displays the report.

## Project Improvements

After completing the basic project, try these improvements:

1. Accept student names.
2. Display the name of the highest-scoring student.
3. Display all students tied for the highest marks.
4. Display all students tied for the lowest marks.
5. Calculate the average marks.
6. Calculate the percentage.
7. Assign grades.
8. Sort marks from highest to lowest.
9. Store records in dictionaries.
10. Add a menu for different analysis operations.

---

# SECTION 11: FIFTY VIVA QUESTIONS AND ANSWERS

## Basic Questions

### 1. What is the largest number?

The largest number is the value that is greater than or equal to all other values in the given collection.

### 2. Which operator is used to compare two values?

The comparison operators include `>`, `<`, `==`, and others.

### 3. What does the greater-than operator do?

It checks whether the left-hand value is greater than the right-hand value.

### 4. What does the greater-than-or-equal operator do?

It checks whether the left-hand value is greater than or equal to the right-hand value.

### 5. How do you find the largest of two numbers?

Compare both values and select the greater one.

### 6. How do you find the largest of three numbers?

Compare the values using `if-elif-else` or nested conditions.

### 7. What is the purpose of the largest variable?

It stores the maximum value found so far.

### 8. What is the `max()` function?

It returns the largest item from an iterable or among multiple arguments.

### 9. Can negative values be the largest value in a list?

Yes. If all values are negative, the least negative value is the largest.

### 10. What happens when two values are equal?

Both values represent the same maximum if no larger value exists.

## Intermediate Questions

### 11. Why should the maximum often be initialized using the first list element?

Because it is an actual value from the collection and works even when all values are negative.

### 12. Why is initializing the maximum to zero sometimes incorrect?

It fails when all values are negative.

### 13. What is the purpose of `None` in maximum selection?

It represents that no qualifying value has been found yet.

### 14. How can you find the largest positive number?

Ignore values that are zero or negative and compare only positive values.

### 15. How can you find the largest negative number?

Consider only values below zero and select the numerically greatest value.

### 16. Is -5 greater than -10?

Yes.

### 17. What is the difference between the largest negative number and the smallest negative number?

The largest negative value is closest to zero; the smallest is the most negative.

### 18. How do you find the largest even number?

Consider only even values and maintain a maximum.

### 19. How do you find the largest odd number?

Consider only odd values and maintain a maximum.

### 20. How do you find the largest digit of an integer?

Examine its digits and select the maximum digit.

## Practical Questions

### 21. Which function finds the maximum in Python?

`max()`.

### 22. How do you get the absolute value?

Use `abs()`.

### 23. Which operator checks whether a number is even?

The modulus operator `%` with a zero remainder.

### 24. How do you handle duplicate maximum values?

Use `count()` to count them or traverse the collection to find every matching position.

### 25. How can you find the position of the largest element?

Find the maximum, then compare each list element with it while tracking indexes.

### 26. Why is sorting unnecessary for maximum selection?

A single traversal can identify the maximum without arranging all values.

### 27. What does a loop do in maximum selection?

It processes each candidate value.

### 28. When is the maximum variable updated?

When a new candidate is greater than the currently stored maximum.

### 29. How do you handle an empty list?

Check whether the collection is empty before accessing an element or use an appropriate default strategy.

### 30. What is a second-largest problem?

It asks for the second highest distinct or position-based value, depending on the problem definition.

## Advanced Questions

### 31. What is the time complexity of finding the largest value in a list?

\(O(n)\).

### 32. What is the additional space complexity of a one-pass maximum algorithm?

\(O(1)\), when no input-sized extra structure is created.

### 33. What is the time complexity of finding the largest of three numbers?

\(O(1)\).

### 34. What is the time complexity of sorting a list using a common efficient comparison sort?

Typically \(O(n \log n)\).

### 35. Why is one-pass maximum selection more efficient than sorting when only the maximum is needed?

It takes linear time instead of requiring the entire collection to be sorted.

### 36. Can a maximum algorithm handle floating-point values?

Yes, when the values are valid comparable numeric values.

### 37. What does `numbers[0]` access?

It accesses the first element of a list.

### 38. What does `numbers[1:]` return?

It returns a slice containing elements starting from index 1.

### 39. Why can `numbers[0]` produce an error?

It raises an `IndexError` when the list is empty.

### 40. What does `count()` do?

It counts how many times a value occurs in a sequence.

## Interview-Oriented Questions

### 41. How would you find the largest number without using `max()`?

Initialize a maximum from the first element and traverse the remaining elements, updating the maximum whenever a larger value appears.

### 42. How would you find the second largest distinct number?

Maintain the largest and second-largest distinct values during traversal, updating them carefully when a new value is found.

### 43. How would you find the largest even number?

Traverse the collection, filter even values, and maintain their maximum.

### 44. How would you find the largest negative number?

Consider only values below zero and select the greatest numerical value.

### 45. How would you find all indexes containing the maximum value?

Find the maximum and then traverse the collection again to collect every matching index.

### 46. Can maximum selection be performed in one traversal?

Yes. A single linear scan is sufficient.

### 47. Why should duplicate values be considered?

The problem may ask for occurrences, positions, or distinct maximum values.

### 48. How can maximum selection be used with a matrix?

Traverse every row and every element while maintaining a maximum.

### 49. Why is maximum selection important in DSA?

It teaches traversal, comparison, variable updates, and linear-time algorithms.

### 50. What is the most important rule in maximum-selection algorithms?

Initialize the maximum correctly and update it only when a larger valid candidate is found.

---

# SECTION 12: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Maximum | Largest value in a collection |
| Minimum | Smallest value in a collection |
| Comparison | Evaluating how two values relate |
| Greater than | Operator used to check whether one value is larger |
| Logical AND | Requires both conditions to be true |
| Nested if | An if statement inside another conditional block |
| Conditional branch | A possible execution path |
| Maximum selection | Process of finding the greatest value |
| Current maximum | Largest value found so far |
| Initialization | Assigning a starting value |
| Update | Changing a variable when a better value is found |
| List | Ordered and mutable collection |
| Traversal | Visiting elements of a collection |
| Duplicate | A value that occurs more than once |
| Absolute value | Non-negative magnitude of a number |
| Positive number | Number greater than zero |
| Negative number | Number smaller than zero |
| Even number | Integer divisible by two |
| Odd number | Integer not divisible by two |
| Index | Position of an element in a sequence |
| Occurrence | Number of times a value appears |
| `max()` | Built-in function that returns the largest value |
| `min()` | Built-in function that returns the smallest value |
| `None` | Special value representing the absence of a value |
| Complexity | Measure of algorithm resource usage |

---

# SECTION 13: QUICK REVISION NOTES

## Largest of Two Numbers

```python
largest = a if a > b else b
```

## Largest of Three Numbers

```python
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
```

## Largest in a List

```python
largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number
```

For a slice-free approach:

```python
largest = numbers[0]

for index in range(1, len(numbers)):
    if numbers[index] > largest:
        largest = numbers[index]
```

## Largest Positive Number

```python
largest_positive = None

for number in numbers:
    if number > 0:
        if largest_positive is None or number > largest_positive:
            largest_positive = number
```

## Largest Negative Number

```python
largest_negative = None

for number in numbers:
    if number < 0:
        if largest_negative is None or number > largest_negative:
            largest_negative = number
```

## Largest Even Number

```python
largest_even = None

for number in numbers:
    if number % 2 == 0:
        if largest_even is None or number > largest_even:
            largest_even = number
```

## Largest Odd Number

```python
largest_odd = None

for number in numbers:
    if number % 2 != 0:
        if largest_odd is None or number > largest_odd:
            largest_odd = number
```

## Highest Student Marks

```python
highest_marks = marks[0]

for value in marks[1:]:
    if value > highest_marks:
        highest_marks = value
```

## Largest Absolute Value

```python
largest_absolute = abs(numbers[0])

for number in numbers[1:]:
    if abs(number) > largest_absolute:
        largest_absolute = abs(number)
```

## Largest Digit

```python
digits = str(abs(number))
largest_digit = 0

for digit in digits:
    current_digit = int(digit)

    if current_digit > largest_digit:
        largest_digit = current_digit
```

## Using max()

```python
largest = max(numbers)
```

## Important Reminders

- Use `>` to compare numerical values.
- Use `>=` when equality must be included.
- Use `and` when multiple conditions must all be satisfied.
- Initialize the maximum with a valid first element when possible.
- Use `None` when searching for a restricted category.
- Do not initialize a general maximum to zero if negative inputs are possible.
- Do not sort a collection just to find its maximum.
- Handle empty collections.
- Consider duplicate maximum values.
- Understand whether the question asks for numerical maximum or absolute magnitude.

---

# SECTION 13: LEARNING CHECKLIST

- [ ] I understand the meaning of the largest number.
- [ ] I can compare two numbers.
- [ ] I can find the largest of two numbers.
- [ ] I can find the largest of three numbers.
- [ ] I can find the largest of four numbers.
- [ ] I can find the largest among multiple numbers.
- [ ] I can use nested if statements.
- [ ] I can use if-elif-else statements.
- [ ] I understand comparison operators.
- [ ] I understand logical AND.
- [ ] I can handle equal values.
- [ ] I can find the largest number in a list.
- [ ] I can find the maximum without using `max()`.
- [ ] I understand Python's `max()` function.
- [ ] I can find the largest positive number.
- [ ] I can find the largest negative number.
- [ ] I understand why -5 is greater than -10.
- [ ] I can find the largest even number.
- [ ] I can find the largest odd number.
- [ ] I can find the highest student marks.
- [ ] I can find the largest absolute value.
- [ ] I can find the largest digit in an integer.
- [ ] I can handle duplicate maximum values.
- [ ] I can identify the positions of maximum values.
- [ ] I can handle a collection without qualifying values.
- [ ] I understand the use of `None`.
- [ ] I understand maximum selection using a loop.
- [ ] I know the time complexity of maximum selection.
- [ ] I know the additional space complexity of maximum selection.
- [ ] I have attempted all ten unsolved questions.
- [ ] I understand the DSA connection.
- [ ] I can explain maximum selection in an interview.

---

# SECTION 14: HOW TO RUN THE PYTHON FILE

Open the terminal inside the `03-largest-number` folder.

Run:

```bash
python 03_largest_number.py
```

On Windows, you can also use:

```powershell
py 03_largest_number.py
```

The program displays an interactive menu.

## Main Menu

```text
=================================================================
                         PYTHON: LARGEST NUMBER
=================================================================

1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

## Menu Options

### Option 1 – View 12 Topic Examples

Displays twelve examples related to maximum selection.

The examples include:

1. Largest of two numbers.
2. Largest using conditional expression.
3. Largest of three using nested if.
4. Largest using if-elif-else.
5. Equal numbers.
6. Largest number in a list.
7. Largest using max().
8. Largest positive number.
9. Largest negative number.
10. Largest even number.
11. Largest odd number.
12. Highest student marks.

### Option 2 – Practice 12 Solved Problems

Displays the solved-problem menu.

You can select a problem and enter your own values.

The program calculates the result using the relevant conditional logic.

### Option 3 – View 10 Unsolved Questions

Displays ten independent practice questions.

Try solving these questions without copying the solved code.

### Option 4 – View Learning Checklist

Displays the learning checklist.

Use it to verify your understanding of the topic.

### Option 0 – Exit

Closes the program.

---

# SECTION 15: REPOSITORY STRUCTURE

```text
PYTHON/
└── Week-1-Programming-Fundamentals/
    └── 06-Conditional-Statements/
        └── 06-Practice-Problems/
            └── 03-largest-number/
                ├── README.md
                └── 03_largest_number.py
```

## File Details

| File | Purpose |
|---|---|
| `README.md` | Complete theory, syntax, examples, solved problems, unsolved questions, and revision notes |
| `03_largest_number.py` | Python program containing examples, solved problems, practice questions, checklist, and menu |

### Previous Topic

**02-even-odd**

In the previous topic, you learned how to identify even and odd numbers using the modulus operator.

You also learned how to count and filter even and odd numbers.

### Current Topic

**03-largest-number**

In this topic, you learned how to compare multiple values and find the maximum using conditional statements and loops.

### Next Topic

**04-leap-year**

In the next problem, you will learn how to determine whether a year is a leap year using conditional statements and divisibility rules.

---

# FINAL SUMMARY

Finding the largest number is an important programming concept.

It teaches you how to compare values and maintain the maximum value while processing a collection.

After completing this topic, you should be able to:

1. Find the largest of two numbers.
2. Find the largest of three numbers.
3. Find the largest of four numbers.
4. Find the largest among multiple numbers.
5. Use nested if statements.
6. Use if-elif-else statements.
7. Handle equal values.
8. Find the largest value in a list.
9. Find the maximum without using `max()`.
10. Find the largest positive number.
11. Find the largest negative number.
12. Find the largest even number.
13. Find the largest odd number.
14. Find the highest student marks.
15. Find the largest absolute value.
16. Find the largest digit in an integer.
17. Understand the use of loops.
18. Understand the maximum-selection algorithm.
19. Understand time and space complexity.
20. Apply maximum selection to DSA problems.

### Final Advice

Do not memorize only the maximum-selection code.

Understand how the current maximum is initialized and updated.

Practise with positive numbers, negative numbers, equal values, duplicate values, and lists containing different numeric categories.

Most importantly, learn to find the maximum without sorting the collection.

**One traversal is enough to find the largest value in an ordinary non-empty collection.**

Keep practising and maintain the same repository structure throughout your Python learning journey.

