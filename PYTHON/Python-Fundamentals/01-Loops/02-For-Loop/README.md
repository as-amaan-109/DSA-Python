# For Loop in Python

## 1. Introduction

The `for` loop is one of the fundamental looping statements in Python.

It is used to execute a block of code once for each item in an iterable object.

An iterable is an object that can provide its elements one at a time. Examples include strings, lists, tuples, dictionaries, sets, and range objects.

For loops are useful when we want to process multiple values without writing the same instructions repeatedly.

For example, suppose we have a list containing five student names. We want to display every name.

Without a loop, we could write separate print statements for every student.

However, when the number of students increases, writing individual statements becomes difficult.

A `for` loop solves this problem by processing every item automatically.

### Example

```python
students = ["Amaan", "Rahul", "Sameer", "Arjun", "Zoya"]

for student in students:
    print(student)
```

Output:

```text
Amaan
Rahul
Sameer
Arjun
Zoya
```

The loop retrieves one name at a time and executes the print statement.

The same approach can be used for strings, numbers, tuples, dictionaries, and other iterables.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

1. Define a `for` loop in Python.
2. Understand why a `for` loop is required.
3. Understand the meaning of iteration.
4. Understand the meaning of an iterable.
5. Identify the loop variable.
6. Understand the role of the `in` keyword.
7. Write a basic `for` loop.
8. Use `range()` with a `for` loop.
9. Print numbers in ascending order.
10. Print numbers in descending order.
11. Use positive and negative step values.
12. Iterate through strings.
13. Iterate through lists.
14. Iterate through tuples.
15. Iterate through dictionaries.
16. Use `enumerate()` to access indexes and values.
17. Use `zip()` to iterate through multiple iterables.
18. Calculate sums using a `for` loop.
19. Count elements using a `for` loop.
20. Filter values using conditions.
21. Search for elements using iteration.
22. Count character frequencies.
23. Understand nested iteration.
24. Analyze basic loop time complexity.
25. Apply `for` loops to beginner-level DSA problems.

---

## 3. What Is a For Loop?

A `for` loop is a control-flow statement that iterates over an iterable and executes a block of code for each item.

### Basic Example

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

### Explanation

The statement `for number in range(1, 6)` starts the loop.

The `range()` function provides the sequence of values.

The variable `number` receives one value at a time.

The indented `print()` statement executes for every value.

After all values have been processed, the loop finishes.

### Important Points

- A `for` loop processes an iterable.
- The loop variable receives the current item.
- The loop body executes for each item.
- Indentation defines the loop body.
- A `for` loop normally finishes when there are no more items to process.
- A `for` loop does not always require `range()`.

---

## 4. Why Do We Use For Loops?

A `for` loop makes repetitive programming tasks easier.

Consider a program that prints five numbers.

### Without a For Loop

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

### With a For Loop

```python
for number in range(1, 6):
    print(number)
```

Both programs produce the same output.

However, the loop-based approach is easier to maintain and modify.

### Advantages

1. Reduces repetitive code.
2. Makes programs easier to read.
3. Simplifies iteration.
4. Helps process collections.
5. Makes calculations easier.
6. Supports searching and filtering.
7. Helps implement algorithms.
8. Makes programs easier to extend.
9. Reduces manual coding effort.
10. Improves code organization.

### Practical Applications

- Printing student records.
- Calculating marks.
- Processing product lists.
- Searching for an item.
- Counting characters.
- Processing data from files.
- Generating reports.
- Performing mathematical calculations.
- Traversing arrays.
- Implementing sorting algorithms.

---

## 5. Basic Syntax of a For Loop

```python
for variable in iterable:
    statement
```

### Components

| Component | Explanation |
|---|---|
| `for` | Python keyword used to begin the loop |
| `variable` | Receives the current item |
| `in` | Connects the variable with the iterable |
| `iterable` | Object that supplies values |
| `:` | Marks the beginning of the loop body |
| Indented statement | Code executed for each item |

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
```

### Explanation

During the first iteration, `fruit` contains `"Apple"`.

During the second iteration, it contains `"Banana"`.

During the third iteration, it contains `"Mango"`.

After the final item is processed, the loop finishes.

---

## 6. Understanding Iteration

Iteration means one complete execution of the loop body.

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

The loop executes three times.

| Iteration | Value assigned to `number` | Output |
|---|---:|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |

### Important Terms

**Iteration:** One execution of the loop body.

**Loop Variable:** The variable that receives the current item.

**Iterable:** An object from which elements can be obtained.

**Loop Body:** The indented statements that execute during each iteration.

**Termination:** The completion of loop execution after the iterable has no further elements.

---

## 7. Understanding Iterables

An iterable is an object that can return its elements one at a time.

Python supports many built-in iterable types.

### 7.1 String

```python
language = "PYTHON"

for character in language:
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

Each character is processed separately.

### 7.2 List

```python
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
```

### 7.3 Tuple

```python
colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)
```

Output:

```text
Red
Green
Blue
```

### 7.4 Set

```python
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)
```

The loop processes each element.

A set does not provide a positional indexing interface like a list. Do not rely on a particular set iteration order.

### 7.5 Dictionary

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Computer Science"
}

for key in student:
    print(key)
```

Output:

```text
name
age
course
```

By default, iterating directly over a dictionary produces its keys.

### 7.6 Range Object

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

The `range()` function produces an iterable sequence of integers.

---

## 8. Using the range() Function

The `range()` function is frequently used with `for` loops.

It represents an immutable sequence of integers.

### General Syntax

```python
range(start, stop, step)
```

It supports three arguments.

### 8.1 Start

The first value of the sequence.

The default start value is zero.

### 8.2 Stop

The sequence stops before the specified stop value.

The stop value is excluded.

### 8.3 Step

The difference between consecutive values.

The default step is one.

### Example 1: range() with One Argument

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

The values start at zero and stop before five.

### Example 2: range() with Two Arguments

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

### Example 3: range() with Three Arguments

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

### Example 4: Negative Step

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

### Example 5: Print Even Numbers

```python
for number in range(2, 11, 2):
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

### Example 6: Print Multiples of Three

```python
for number in range(3, 16, 3):
    print(number)
```

Output:

```text
3
6
9
12
15
```

### Important Rules

1. The start value is included.
2. The stop value is excluded.
3. The default start value is zero.
4. The default step value is one.
5. The step must not be zero.
6. Positive steps move forward.
7. Negative steps can move backward.
8. The direction of the step must match the start and stop values.

---

## 9. Iterating Through a String

A string is an iterable sequence of characters.

A `for` loop can process every character in a string.

### Example 1: Print Each Character

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

### Example 2: Print Characters on One Line

```python
name = "PYTHON"

for character in name:
    print(character, end=" ")
```

Output:

```text
P Y T H O N
```

### Example 3: Count Characters

```python
text = "Python Programming"

count = 0

for character in text:
    count += 1

print("Total characters:", count)
```

Output:

```text
Total characters: 18
```

Spaces are included in the character count.

### Example 4: Count Vowels

```python
text = "education"

count = 0

for character in text.lower():
    if character in "aeiou":
        count += 1

print("Vowels:", count)
```

Output:

```text
Vowels: 5
```

---

## 10. Iterating Through a List

A list stores multiple elements in a sequence.

A `for` loop can process each list element.

### Example

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

### Sum of List Elements

```python
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print("Sum:", total)
```

Output:

```text
Sum: 100
```

### Find Even Numbers

```python
numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:
    if number % 2 == 0:
        print(number)
```

Output:

```text
10
20
30
```

### Find the Maximum Element

```python
numbers = [12, 45, 7, 89, 31]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum:", maximum)
```

Output:

```text
Maximum: 89
```

---

## 11. Iterating Through a Tuple

A tuple is an ordered collection of elements.

A tuple is immutable, which means its elements cannot be changed after creation.

It is still possible to iterate through a tuple.

### Example

```python
colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)
```

Output:

```text
Red
Green
Blue
```

### Tuple of Numbers

```python
numbers = (10, 20, 30, 40)

total = 0

for number in numbers:
    total += number

print("Total:", total)
```

Output:

```text
Total: 100
```

The loop can read tuple elements without modifying the tuple.

---

## 12. Iterating Through a Dictionary

A dictionary stores data in key-value pairs.

A `for` loop can process dictionary keys, values, or key-value pairs.

### 12.1 Iterate Through Keys

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Computer Science"
}

for key in student:
    print(key)
```

Output:

```text
name
age
course
```

### 12.2 Iterate Through Values

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Computer Science"
}

for value in student.values():
    print(value)
```

Output:

```text
Amaan
22
Computer Science
```

### 12.3 Iterate Through Key-Value Pairs

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Computer Science"
}

for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Amaan
age : 22
course : Computer Science
```

### Important Dictionary Methods

| Method | Purpose |
|---|---|
| `keys()` | Provides dictionary keys |
| `values()` | Provides dictionary values |
| `items()` | Provides key-value pairs |

---

## 13. Using enumerate()

The `enumerate()` function is used when we want to access both the index and the value of an iterable item.

### Syntax

```python
enumerate(iterable, start=0)
```

The `start` argument specifies the initial index.

Its default value is zero.

### Example

```python
names = ["Amaan", "Rahul", "Sameer"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 Amaan
1 Rahul
2 Sameer
```

### Start Index from One

```python
names = ["Amaan", "Rahul", "Sameer"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

Output:

```text
1 Amaan
2 Rahul
3 Sameer
```

### Why Is enumerate() Useful?

It is useful when:

- We need an element's position.
- We want numbered output.
- We process indexed data.
- We want to avoid maintaining a separate counter.
- We need both an index and a value in one iteration.

### Comparison

Without `enumerate()`:

```python
names = ["Amaan", "Rahul", "Sameer"]

for index in range(len(names)):
    print(index, names[index])
```

With `enumerate()`:

```python
names = ["Amaan", "Rahul", "Sameer"]

for index, name in enumerate(names):
    print(index, name)
```

The second approach is often more readable.

---

## 14. Using zip()

The `zip()` function combines elements from multiple iterables.

It returns an iterator that produces tuples containing corresponding elements.

### Syntax

```python
zip(iterable1, iterable2)
```

### Example

```python
students = ["Amaan", "Rahul", "Sameer"]
marks = [85, 90, 78]

for student, mark in zip(students, marks):
    print(student, mark)
```

Output:

```text
Amaan 85
Rahul 90
Sameer 78
```

### Explanation

The first iteration combines:

```text
Amaan
85
```

The second iteration combines:

```text
Rahul
90
```

The third iteration combines:

```text
Sameer
78
```

### Important Rule

By default, `zip()` stops when the shortest input iterable is exhausted.

Example:

```python
names = ["Amaan", "Rahul", "Sameer"]
marks = [85, 90]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```text
Amaan 85
Rahul 90
```

The unmatched `"Sameer"` item is not processed.

---

## 15. Nested For Loops

A nested loop is a loop written inside another loop.

The outer loop controls one level of repetition.

The inner loop executes for each iteration of the outer loop.

### Example

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

### Explanation

The outer loop executes three times.

For every outer iteration, the inner loop executes three times.

Total inner-loop executions:

```text
3 × 3 = 9
```

### Multiplication Table Grid

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end="\t")

    print()
```

Output:

```text
1       2       3
2       4       6
3       6       9
```

### Applications of Nested Loops

- Pattern printing.
- Matrix processing.
- Comparing pairs of values.
- Generating combinations.
- Table generation.
- Basic sorting algorithms.

---

## 16. Conditional Statements Inside a For Loop

A condition can be placed inside a loop to decide which values should be processed.

### Example: Print Even Numbers

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

### Example: Print Numbers Greater Than Five

```python
numbers = [2, 8, 4, 10, 3, 7, 1]

for number in numbers:
    if number > 5:
        print(number)
```

Output:

```text
8
10
7
```

### Example: Positive, Negative, and Zero

```python
numbers = [10, -5, 0, 7, -2, 0]

for number in numbers:
    if number > 0:
        print(number, "is positive")

    elif number < 0:
        print(number, "is negative")

    else:
        print(number, "is zero")
```

Conditions help filter and classify iterable values.

---

## 17. Twelve Topic Examples

These examples correspond to the twelve examples in `02_for_loop.py`.

### Example 1: Basic For Loop Using range()

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

`range(1, 6)` generates five values.

The loop processes each value and prints it.

### Example 2: Iterate Through a String

**Objective:** Display every character in a string.

```python
language = "PYTHON"

for character in language:
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

A string is iterable, so the loop receives its characters one at a time.

### Example 3: Iterate Through a List

**Objective:** Print every element of a list.

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

The loop retrieves each list element in sequence.

### Example 4: Iterate Through a Tuple

**Objective:** Display every element in a tuple.

```python
colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)
```

Output:

```text
Red
Green
Blue
```

Explanation:

The tuple is iterable even though its elements cannot be changed.

### Example 5: Use range() with a Starting Value

**Objective:** Print numbers from 5 to 10.

```python
for number in range(5, 11):
    print(number)
```

Output:

```text
5
6
7
8
9
10
```

Explanation:

The sequence starts at 5 and stops before 11.

### Example 6: Use range() with a Step Value

**Objective:** Print even numbers from 2 to 10.

```python
for number in range(2, 11, 2):
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

The step value is 2, so every next value increases by two.

### Example 7: Print Numbers in Descending Order

**Objective:** Print numbers from 5 to 1.

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

The negative step decreases the value during each iteration.

### Example 8: Calculate Sum Using a For Loop

**Objective:** Calculate the sum of numbers from 1 to 5.

```python
total = 0

for number in range(1, 6):
    total += number

print("Total:", total)
```

Output:

```text
Total: 15
```

Explanation:

The loop adds each value to the running total.

### Example 9: Use enumerate()

**Objective:** Display the index and name of every student.

```python
names = ["Amaan", "Rahul", "Sameer"]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
```

Output:

```text
1. Amaan
2. Rahul
3. Sameer
```

Explanation:

`enumerate()` returns the index and corresponding value during every iteration.

### Example 10: Iterate Through Two Lists Using zip()

**Objective:** Display student names with their marks.

```python
students = ["Amaan", "Rahul", "Sameer"]
marks = [85, 90, 78]

for student, mark in zip(students, marks):
    print(f"{student}: {mark}")
```

Output:

```text
Amaan: 85
Rahul: 90
Sameer: 78
```

Explanation:

`zip()` combines corresponding items from the two lists.

### Example 11: Iterate Through a Dictionary

**Objective:** Display dictionary keys and values.

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Computer Science"
}

for key, value in student.items():
    print(f"{key}: {value}")
```

Output:

```text
name: Amaan
age: 22
course: Computer Science
```

Explanation:

The `items()` method provides key-value pairs.

### Example 12: Filter Numbers Using a For Loop

**Objective:** Display numbers greater than five.

```python
numbers = [2, 8, 4, 10, 3, 7, 1]

for number in numbers:
    if number > 5:
        print(number)
```

Output:

```text
8
10
7
```

Explanation:

The loop checks every number.

Only numbers satisfying the condition are printed.

---

## 18. Twelve Solved Programming Problems

### Problem 1: Print Numbers from 1 to N

**Problem Statement:**

Write a Python program to accept a positive integer N and print all natural numbers from 1 to N using a `for` loop.

**Logic:**

1. Read N.
2. Start the loop at 1.
3. Use N + 1 as the exclusive stop value.
4. Print every generated number.

**Code:**

```python
n = int(input("Enter the value of N: "))

for number in range(1, n + 1):
    print(number, end=" ")

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

The stop argument is excluded by `range()`.

Therefore, `n + 1` is used to include N.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 2: Print Numbers in Reverse

**Problem Statement:**

Accept a positive integer and print numbers from that value down to 1.

**Logic:**

1. Read the starting number.
2. Set the starting value of the range to N.
3. Use zero as the exclusive stop value.
4. Use -1 as the step.
5. Print every generated number.

**Code:**

```python
number = int(input("Enter the starting number: "))

for value in range(number, 0, -1):
    print(value, end=" ")

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

The loop moves backward by one during each iteration.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 3: Sum of Natural Numbers

**Problem Statement:**

Calculate the sum of the first N natural numbers using a `for` loop.

**Logic:**

1. Read N.
2. Initialize total with zero.
3. Iterate from 1 through N.
4. Add every number to total.
5. Display the final sum.

**Code:**

```python
n = int(input("Enter the value of N: "))

total = 0

for number in range(1, n + 1):
    total += number

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

The calculation is:

```text
1 + 2 + 3 + 4 + 5 = 15
```

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 4: Sum of Even Numbers

**Problem Statement:**

Calculate the sum of all even numbers from 1 to N.

**Logic:**

1. Accept N.
2. Initialize the total to zero.
3. Start the range at 2.
4. Increase the value by 2.
5. Add each generated value to the total.
6. Display the result.

**Code:**

```python
n = int(input("Enter the value of N: "))

total = 0

for number in range(2, n + 1, 2):
    total += number

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

The loop processes:

```text
2, 4, 6, 8, 10
```

Their sum is 30.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1).

### Problem 5: Count Vowels in a String

**Problem Statement:**

Accept a string and count the vowels using a `for` loop.

**Logic:**

1. Read a string.
2. Initialize a counter with zero.
3. Convert the string to lowercase for comparison.
4. Iterate through its characters.
5. Check whether each character belongs to `aeiou`.
6. Increase the counter when a vowel is found.
7. Display the count.

**Code:**

```python
text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print("Total vowels:", count)
```

**Sample Input:**

```text
Enter a string: Education
```

**Sample Output:**

```text
Total vowels: 5
```

**Explanation:**

The vowels are:

```text
E, u, a, i, o
```

The string is converted to lowercase so uppercase vowels are also counted.

**Complexity:**

- Time: O(N), where N is the string length.
- Auxiliary space: O(N) for the lowercase string created by `lower()`.
- The counting variables use O(1) additional space.

### Problem 6: Factorial of a Number

**Problem Statement:**

Calculate the factorial of a non-negative integer using a `for` loop.

Mathematical definition:

```text
N! = N × (N - 1) × ... × 2 × 1

0! = 1
```

**Logic:**

1. Read a non-negative integer.
2. Initialize factorial with 1.
3. Multiply factorial by each integer from 1 to N.
4. Display the result.

**Code:**

```python
number = int(input("Enter a non-negative integer: "))

factorial = 1

for value in range(1, number + 1):
    factorial *= value

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

When N is zero, the range is empty and the initialized value remains 1.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(1), excluding the storage required for the growing integer result.

### Problem 7: Multiplication Table

**Problem Statement:**

Accept a number and print its multiplication table from 1 to 10.

**Logic:**

1. Read a number.
2. Iterate through multipliers from 1 to 10.
3. Multiply the number by each multiplier.
4. Display the result.

**Code:**

```python
number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
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

The multiplier changes from 1 through 10.

**Complexity:**

- Time: O(1), because exactly ten iterations are performed.
- Auxiliary space: O(1).

### Problem 8: Count Positive Numbers, Negative Numbers, and Zeros

**Problem Statement:**

Accept a list of integers and count how many values are positive, negative, or equal to zero.

**Logic:**

1. Read the number of values.
2. Accept the values into a list.
3. Initialize three counters.
4. Iterate through the list.
5. Use conditions to classify each value.
6. Display the three counts.

**Code:**

```python
count = int(input("How many numbers do you want to enter? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

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

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
```

**Sample Input:**

```text
How many numbers do you want to enter? 6
Enter a number: 10
Enter a number: -5
Enter a number: 0
Enter a number: 7
Enter a number: -2
Enter a number: 0
```

**Sample Output:**

```text
Positive numbers: 2
Negative numbers: 2
Zeros: 2
```

**Explanation:**

Every value is checked once.

The appropriate counter is increased based on its sign.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(N) for the stored input list.
- Additional counters: O(1).

### Problem 9: Find the Maximum Number

**Problem Statement:**

Find the largest value in a list using a `for` loop.

**Logic:**

1. Read the number of elements.
2. Store the input values.
3. Initialize the maximum with the first element.
4. Iterate through the values.
5. Compare each value with the maximum.
6. Update the maximum when a larger value is found.
7. Display the maximum.

**Code:**

```python
count = int(input("How many numbers do you want to enter? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum number:", maximum)
```

**Sample Input:**

```text
How many numbers do you want to enter? 5
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

The first element is the initial maximum.

Every subsequent value is compared with it.

The variable changes only when a larger value is found.

**Complexity:**

- Time: O(N).
- Auxiliary space: O(N) for the list.
- Extra scanning space: O(1).

### Problem 10: Linear Search

**Problem Statement:**

Accept a list and a target value. Search for the target using a linear search algorithm.

**Logic:**

1. Read the number of elements.
2. Store the list elements.
3. Read the target value.
4. Iterate through the list with `enumerate()`.
5. Compare every element with the target.
6. Store its index when found.
7. Stop searching after the first match.
8. Display whether the target exists.

**Code:**

```python
count = int(input("How many numbers do you want to enter? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

target = int(input("Enter the number to search: "))

found_position = -1

for index, number in enumerate(numbers):
    if number == target:
        found_position = index
        break

if found_position != -1:
    print("Element found.")
    print("Position:", found_position + 1)
    print("Index:", found_position)
else:
    print("Element not found.")
```

**Sample Input:**

```text
How many numbers do you want to enter? 5
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 40
Enter a number: 50
Enter the number to search: 30
```

**Sample Output:**

```text
Element found.
Position: 3
Index: 2
```

**Explanation:**

Linear search examines elements one by one.

When a matching element is found, `break` terminates the loop.

The program reports the first matching occurrence.

**Complexity:**

- Best-case time: O(1).
- Worst-case time: O(N).
- Auxiliary space: O(1), excluding the input list.

### Problem 11: Character Frequency

**Problem Statement:**

Accept a string and count how many times each character appears.

**Logic:**

1. Read a string.
2. Create an empty dictionary.
3. Iterate through each character.
4. Increase its frequency if it already exists.
5. Otherwise, initialize its frequency to one.
6. Display each character and its frequency.

**Code:**

```python
text = input("Enter a string: ")

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print("\nCharacter frequencies:")

for character, count in frequency.items():
    if character == " ":
        display_character = "[space]"
    else:
        display_character = character

    print(f"{display_character}: {count}")
```

**Sample Input:**

```text
Enter a string: banana
```

**Sample Output:**

```text
Character frequencies:
b: 1
a: 3
n: 2
```

**Explanation:**

The dictionary stores each character as a key and its frequency as a value.

The `get()` method returns the existing count or zero when the key does not exist.

Spaces are also counted and displayed as `[space]`.

**Complexity:**

- Expected time: O(N), where N is the string length.
- Auxiliary space: O(K), where K is the number of distinct characters.

### Problem 12: Average of Numbers

**Problem Statement:**

Accept N numbers and calculate their average using a `for` loop.

**Logic:**

1. Read the number of elements.
2. Accept all values.
3. Initialize total with zero.
4. Iterate through the list.
5. Add every value to total.
6. Divide the total by the number of elements.
7. Display the sum and average.

**Code:**

```python
count = int(input("How many numbers do you want to enter? "))

numbers = []

for index in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)

total = 0

for number in numbers:
    total += number

average = total / count

print("Sum:", total)
print("Average:", average)
```

**Sample Input:**

```text
How many numbers do you want to enter? 3
Enter a number: 10
Enter a number: 20
Enter a number: 30
```

**Sample Output:**

```text
Sum: 60
Average: 20.0
```

**Explanation:**

The average is calculated using:

```text
Average = Sum / Number of Elements

Average = 60 / 3

Average = 20
```

**Complexity:**

- Time: O(N).
- Auxiliary space: O(N) for the list.
- Additional scanning space: O(1).

---

## 19. Ten Unsolved Practice Questions

Solve these questions independently using `for` loops.

Try to understand the logic before searching for a solution.

### Question 1: Multiples of Five

Write a program to print all multiples of 5 from 1 to N.

Example:

```text
Input:
N = 30

Expected Output:
5 10 15 20 25 30
```

### Question 2: Product of Natural Numbers

Write a program to calculate the product of all natural numbers from 1 to N.

Example:

```text
Input:
N = 5

Expected Output:
120
```

### Question 3: Find the Smallest Number

Write a program to find the smallest number in a list using a `for` loop.

Example:

```text
Input:
[12, 4, 19, 2, 8]

Expected Output:
2
```

### Question 4: Count Uppercase and Lowercase Letters

Write a program to count the uppercase and lowercase alphabetic characters in a string.

Example:

```text
Input:
"PyThOn"

Expected Output:
Uppercase: 3
Lowercase: 3
```

### Question 5: Find the Second Largest Element

Write a program to find the second largest distinct element in a list.

Example:

```text
Input:
[10, 40, 20, 30, 40]

Expected Output:
30
```

### Question 6: Check a Palindrome Word

Write a program to check whether a word is a palindrome using a `for` loop.

Example:

```text
Input:
madam

Expected Output:
Palindrome
```

### Question 7: Sum of Digits

Write a program to calculate the sum of all digits of an integer.

Example:

```text
Input:
12345

Expected Output:
15
```

### Question 8: Count Numbers Divisible by Both Three and Five

Write a program to count how many elements in a list are divisible by both 3 and 5.

Example:

```text
Input:
[15, 20, 30, 45, 50, 60]

Expected Output:
4
```

### Question 9: Merge Two Lists by Corresponding Positions

Write a program to combine corresponding elements of two lists into pairs.

Example:

```text
Input:
[1, 2, 3]
[10, 20, 30]

Expected Output:
[(1, 10), (2, 20), (3, 30)]
```

### Question 10: Find Duplicate Elements

Write a program to find all distinct values that appear more than once in a list.

Example:

```text
Input:
[1, 2, 3, 2, 4, 1, 5]

Expected Output:
1 2
```

---

## 20. Common Mistakes While Using For Loops

### Mistake 1: Forgetting That the Stop Value Is Excluded

Incorrect:

```python
for number in range(1, 5):
    print(number)
```

This prints:

```text
1
2
3
4
```

Correct:

```python
for number in range(1, 6):
    print(number)
```

### Mistake 2: Using a Zero Step

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

### Mistake 3: Incorrect Direction for a Negative Step

Incorrect:

```python
for number in range(1, 6, -1):
    print(number)
```

The sequence is empty because the starting value and step direction do not move toward the stop value.

Correct for ascending order:

```python
for number in range(1, 6, 1):
    print(number)
```

Correct for descending order:

```python
for number in range(5, 0, -1):
    print(number)
```

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

### Mistake 5: Confusing the Loop Variable

Incorrect:

```python
for number in range(1, 6):
    print(value)
```

The variable `value` has not been defined in this example.

Correct:

```python
for number in range(1, 6):
    print(number)
```

### Mistake 6: Forgetting to Initialize an Accumulator

Incorrect:

```python
for number in range(1, 6):
    total += number
```

The variable `total` must be initialized before using it.

Correct:

```python
total = 0

for number in range(1, 6):
    total += number
```

### Mistake 7: Initializing a Factorial with Zero

Incorrect:

```python
factorial = 0

for number in range(1, 6):
    factorial *= number
```

Multiplication by zero keeps the result at zero.

Correct:

```python
factorial = 1

for number in range(1, 6):
    factorial *= number
```

### Mistake 8: Forgetting That Dictionary Iteration Returns Keys

```python
student = {
    "name": "Amaan",
    "age": 22
}

for item in student:
    print(item)
```

This prints keys, not key-value pairs.

To access both:

```python
for key, value in student.items():
    print(key, value)
```

### Mistake 9: Assuming zip() Processes Every Item

When the input iterables have different lengths, regular `zip()` stops at the shortest iterable.

Always consider the length of each input.

### Mistake 10: Modifying a List During Iteration

Changing a list while iterating over it can cause elements to be skipped or produce unexpected behavior.

For filtering, consider building a new list instead.

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
```

Output:

```text
[2, 4]
```

---

## 21. Best Practices for For Loops

1. Use meaningful loop variable names.
2. Use `for` loops for iterable-based tasks.
3. Use `range()` when a numeric sequence is required.
4. Remember that the stop argument is exclusive.
5. Use `enumerate()` when both indexes and values are needed.
6. Use `zip()` when corresponding elements from multiple iterables are required.
7. Use `.items()` to access dictionary key-value pairs.
8. Use `.values()` when only dictionary values are required.
9. Keep loop bodies short and understandable.
10. Keep indentation consistent.
11. Avoid unnecessary nested loops.
12. Avoid modifying a collection unexpectedly during iteration.
13. Use conditions to filter values.
14. Initialize accumulators before the loop.
15. Initialize counters correctly.
16. Test empty iterables.
17. Test single-element collections.
18. Handle input validation where required.
19. Consider duplicate elements in search problems.
20. Analyze the complexity of repeated operations.

---

## 22. Debugging For Loop Programs

Debugging helps identify and correct errors.

### 22.1 Print the Current Item

```python
numbers = [10, 20, 30]

for number in numbers:
    print("Current item:", number)
```

This shows which value is being processed.

### 22.2 Print the Index and Value

```python
numbers = [10, 20, 30]

for index, number in enumerate(numbers):
    print("Index:", index, "Value:", number)
```

### 22.3 Test an Empty Iterable

```python
numbers = []

for number in numbers:
    print(number)

print("Loop completed.")
```

Output:

```text
Loop completed.
```

The loop body does not execute because the iterable is empty.

### 22.4 Test a Single Element

```python
numbers = [100]

for number in numbers:
    print(number)
```

Output:

```text
100
```

### 22.5 Check Loop Boundaries

For a range-based loop, verify:

- Starting value.
- Stop value.
- Step value.
- Expected number of iterations.

### 22.6 Check Accumulator Values

```python
numbers = [10, 20, 30]

total = 0

for number in numbers:
    total += number
    print("Current total:", total)
```

Output:

```text
Current total: 10
Current total: 30
Current total: 60
```

### 22.7 Common Errors

| Error | Possible reason |
|---|---|
| `SyntaxError` | Incorrect Python syntax |
| `IndentationError` | Incorrect indentation |
| `NameError` | Variable is not defined |
| `TypeError` | Incorrect operation between types |
| `ValueError` | Invalid input or argument |
| `IndexError` | Invalid sequence index |
| `KeyError` | Missing dictionary key |

---

## 23. Real-Life Applications of For Loops

### 23.1 Student Management Systems

A college management system can iterate through student records.

It can calculate marks, attendance, and results.

### 23.2 Banking Applications

A banking application can process transaction records and calculate account summaries.

### 23.3 E-Commerce Applications

Online stores can display products, calculate cart totals, and process order items.

### 23.4 Website Development

A web application can generate repeated elements such as product cards and table rows.

### 23.5 Data Analysis

Loops can process records, calculate statistics, and examine values.

### 23.6 File Processing

Programs can iterate through lines in a file and process their contents.

### 23.7 Automation

Automation scripts can process multiple files and records.

### 23.8 Games

Games can use repeated processing to update objects and game data.

### 23.9 Reporting

Programs can iterate through data and create summaries.

### 23.10 Inventory Management

Inventory systems can process product lists and calculate available stock.

---

## 24. Connection Between For Loops and DSA

The `for` loop is one of the most important foundations of Data Structures and Algorithms.

Many basic DSA operations involve visiting each element in a collection.

### 24.1 Array Traversal

Array traversal means visiting every element in an array or list.

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Time complexity: O(N).

### 24.2 Linear Search

Linear search checks each element until a matching value is found.

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

Worst-case time complexity: O(N).

### 24.3 Finding the Maximum Element

```python
numbers = [12, 45, 7, 89, 31]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
```

Time complexity: O(N).

### 24.4 Finding the Minimum Element

```python
numbers = [12, 45, 7, 89, 31]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print(minimum)
```

Time complexity: O(N).

### 24.5 Counting Frequency

```python
numbers = [1, 2, 2, 3, 1, 2]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)
```

Output:

```text
{1: 2, 2: 3, 3: 1}
```

Expected time complexity: O(N).

### 24.6 Pair Comparisons

Nested loops can compare every pair of elements.

```python
numbers = [1, 2, 3]

for first in numbers:
    for second in numbers:
        print(first, second)
```

Time complexity: O(N²).

### 24.7 Selection Sort

Selection Sort repeatedly finds the minimum element from the unsorted portion of a list.

It uses nested iteration.

### 24.8 Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them when required.

It commonly uses nested loops.

### 24.9 Two-Pointer Techniques

Two-pointer algorithms use two positions to process an array or string.

Loops often control the movement of both positions.

### 24.10 Sliding Window

Sliding window algorithms process a moving portion of an array or string.

A loop is commonly used to advance the window.

---

## 25. Time and Space Complexity

Time complexity describes how an algorithm's running time grows with input size.

Space complexity describes how memory usage grows with input size.

The number of iterations is important when analyzing a `for` loop.

### 25.1 Constant Iterations: O(1)

```python
for number in range(10):
    print(number)
```

The loop always executes ten times.

Its iteration count does not depend on N.

Time complexity: O(1).

### 25.2 Linear Iteration: O(N)

```python
for number in range(n):
    print(number)
```

The loop executes N times.

Time complexity: O(N).

### 25.3 Two Nested Loops: O(N²)

```python
for first in range(n):
    for second in range(n):
        print(first, second)
```

The inner loop executes N times for every outer-loop iteration.

Total iterations:

```text
N × N = N²
```

Time complexity: O(N²).

### 25.4 Three Nested Loops: O(N³)

```python
for first in range(n):
    for second in range(n):
        for third in range(n):
            print(first, second, third)
```

Total iterations:

```text
N × N × N = N³
```

Time complexity: O(N³).

### 25.5 Two Consecutive Loops: O(N)

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

### 25.6 Loop with Constant Work

```python
total = 0

for number in range(n):
    total += number
```

Each iteration performs constant-time work.

Time complexity: O(N).

Auxiliary space complexity: O(1), excluding the range object and the output of the program.

### Complexity Reference

| Loop Pattern | Typical Time Complexity |
|---|---|
| Fixed number of iterations | O(1) |
| One traversal of N elements | O(N) |
| Two nested loops of size N | O(N²) |
| Three nested loops of size N | O(N³) |
| Two consecutive loops of size N | O(N) |
| Outer loop N with inner logarithmic work | O(N log N) |

The actual complexity also depends on what happens inside the loop body.

---

## 26. Mini Project: Student Marks Analyzer

### Project Objective

Create a program that accepts student names and marks, then displays their results.

The project should:

1. Accept a number of students.
2. Read each student's name.
3. Read each student's marks.
4. Calculate the total marks.
5. Calculate the average marks.
6. Display each student's result.
7. Find the highest marks.
8. Find the lowest marks.

### Project Code

```python
"""
Project: Student Marks Analyzer

Description:
Accept student details and analyze their marks using
for loops and basic Python data structures.
"""


def main() -> None:
    try:
        student_count = int(input("Enter the number of students: "))

        if student_count <= 0:
            print("Enter at least one student.")
            return

        students = []

        for index in range(student_count):
            print(f"\nStudent {index + 1}")

            name = input("Enter student name: ").strip()
            marks = float(input("Enter marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            students.append({
                "name": name,
                "marks": marks
            })

        total_marks = 0
        highest = students[0]
        lowest = students[0]

        print("\nSTUDENT RESULTS")
        print("-" * 45)

        for student in students:
            print(
                f"{student['name']}: "
                f"{student['marks']}"
            )

            total_marks += student["marks"]

            if student["marks"] > highest["marks"]:
                highest = student

            if student["marks"] < lowest["marks"]:
                lowest = student

        average = total_marks / student_count

        print("\nSUMMARY")
        print("-" * 45)
        print("Total marks:", total_marks)
        print("Average marks:", average)
        print(
            "Highest marks:",
            highest["name"],
            highest["marks"]
        )
        print(
            "Lowest marks:",
            lowest["name"],
            lowest["marks"]
        )

    except ValueError:
        print("Invalid input. Enter valid numerical values.")


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter the number of students: 3

Student 1
Enter student name: Amaan
Enter marks: 85

Student 2
Enter student name: Rahul
Enter marks: 90

Student 3
Enter student name: Sameer
Enter marks: 78
```

### Sample Output

```text
STUDENT RESULTS
---------------------------------------------
Amaan: 85.0
Rahul: 90.0
Sameer: 78.0

SUMMARY
---------------------------------------------
Total marks: 253.0
Average marks: 84.33333333333333
Highest marks: Rahul 90.0
Lowest marks: Sameer 78.0
```

### Concepts Used

- `for` loop.
- Lists.
- Dictionaries.
- Input and output.
- Variables.
- Conditions.
- Accumulators.
- Maximum and minimum comparisons.
- Exception handling.
- Basic data processing.

---

## 27. Fifty Viva Questions and Answers

### Basic For Loop Questions

**Q1. What is a for loop in Python?**

A `for` loop is used to iterate over the elements of an iterable and execute a block of code for each element.

**Q2. Why do we use a for loop?**

It helps perform repetitive tasks without writing the same statements repeatedly.

**Q3. What is an iterable?**

An iterable is an object that provides its elements one at a time.

**Q4. Name some Python iterables.**

Strings, lists, tuples, sets, dictionaries, and range objects are common iterables.

**Q5. What is an iteration?**

One complete execution of the loop body is called an iteration.

**Q6. What is a loop variable?**

A loop variable receives the current item from the iterable.

**Q7. What is the purpose of the `in` keyword?**

It connects the loop variable to the iterable being processed.

**Q8. Is `range()` compulsory in a for loop?**

No. A `for` loop can directly iterate through a list, string, tuple, dictionary, or another iterable.

**Q9. What happens when the iterable is empty?**

The loop body does not execute.

**Q10. What happens when a for loop processes all iterable elements?**

The loop finishes normally.

### Range Function Questions

**Q11. What is the `range()` function?**

It creates an immutable sequence of integers.

**Q12. What is the default start value of `range()`?**

The default start value is zero.

**Q13. What is the default step value of `range()`?**

The default step value is one.

**Q14. Is the stop value included in `range()`?**

No. The stop value is excluded.

**Q15. What does `range(5)` generate?**

It represents the values 0, 1, 2, 3, and 4.

**Q16. What does `range(1, 6)` generate?**

It represents the values 1, 2, 3, 4, and 5.

**Q17. What does `range(2, 11, 2)` generate?**

It represents 2, 4, 6, 8, and 10.

**Q18. Can the step value be negative?**

Yes. A negative step can generate a descending sequence.

**Q19. Can the step value be zero?**

No. A zero step raises a `ValueError`.

**Q20. What does `range(5, 0, -1)` generate?**

It represents 5, 4, 3, 2, and 1.

### Iterable Questions

**Q21. Can a for loop iterate through a string?**

Yes. It can process every character of a string.

**Q22. Can a for loop iterate through a list?**

Yes. It can process each list element.

**Q23. Can a for loop iterate through a tuple?**

Yes. Tuples are iterable.

**Q24. How does a for loop iterate through a dictionary by default?**

It iterates through dictionary keys.

**Q25. Which dictionary method provides key-value pairs?**

The `items()` method.

**Q26. Which dictionary method provides only values?**

The `values()` method.

**Q27. Which dictionary method provides keys?**

The `keys()` method.

**Q28. What is the purpose of `enumerate()`?**

It provides both an index and an item during iteration.

**Q29. What is the default starting index of `enumerate()`?**

Zero.

**Q30. What is the purpose of `zip()`?**

It combines corresponding elements from multiple iterables into tuples.

### Problem-Solving Questions

**Q31. How can you calculate the sum of a list?**

Initialize a total to zero and add each element using a loop.

**Q32. How can you find the maximum element in a list?**

Initialize the maximum with the first element and compare every element with it.

**Q33. How can you find the minimum element in a list?**

Initialize the minimum with the first element and update it when a smaller value is found.

**Q34. How can you count vowels in a string?**

Iterate through the string and check whether each character belongs to the vowel set.

**Q35. What is linear search?**

Linear search checks elements one by one until the target is found or the collection ends.

**Q36. What is character frequency?**

Character frequency is the number of times a character appears in a string.

**Q37. How can you count positive and negative values?**

Use conditional statements inside a loop and maintain separate counters.

**Q38. How do you calculate an average?**

Divide the sum of all values by the number of values.

**Q39. What is a nested loop?**

A nested loop is a loop written inside another loop.

**Q40. What is the purpose of the `break` statement?**

It immediately terminates the nearest enclosing loop.

### DSA and Complexity Questions

**Q41. What is array traversal?**

Array traversal means visiting every element of an array or list.

**Q42. What is the time complexity of traversing N elements once?**

O(N), assuming constant work per element.

**Q43. What is the time complexity of two nested loops of size N?**

O(N²), assuming constant work inside the inner loop.

**Q44. What is the time complexity of a fixed ten-iteration loop?**

O(1), because the iteration count is constant.

**Q45. What is Big O notation?**

Big O notation describes how an algorithm's growth rate changes with input size.

**Q46. Why are loops important in DSA?**

They are used for traversal, searching, sorting, comparisons, and processing data structures.

**Q47. Which loop structure is commonly used in Bubble Sort?**

Nested `for` loops are commonly used in a basic Bubble Sort implementation.

**Q48. Can a for loop be used to perform linear search?**

Yes. It can examine each element until a matching value is found.

**Q49. What is the difference between an iterable and an iterator?**

An iterable can provide an iterator. An iterator is an object that returns values one at a time during iteration.

**Q50. Which concepts should be understood before advanced loop-based DSA problems?**

Iteration, conditions, list traversal, nested loops, searching, and time complexity should be understood.

---

## 28. Important Terminology

| Term | Meaning |
|---|---|
| For Loop | Loop that processes elements of an iterable |
| Iteration | One execution of the loop body |
| Iterable | Object that can provide elements |
| Iterator | Object that returns elements one at a time |
| Loop Variable | Variable containing the current item |
| Loop Body | Statements executed during iteration |
| `range()` | Function that creates an integer sequence |
| Start | First value in a range sequence |
| Stop | Exclusive ending value in a range sequence |
| Step | Difference between consecutive range values |
| `enumerate()` | Function that provides indexes and values |
| `zip()` | Function that combines multiple iterables |
| Dictionary | Collection of key-value pairs |
| List | Ordered, mutable collection |
| Tuple | Ordered, immutable collection |
| Set | Collection of unique elements |
| Nested Loop | A loop inside another loop |
| Accumulator | Variable used to collect a running result |
| Counter | Variable used to count occurrences |
| Linear Search | Search method that checks elements sequentially |
| Frequency | Number of occurrences of an element |
| Big O | Notation used to describe algorithm growth |
| Traversal | Visiting elements of a collection |

---

## 29. Quick Revision Notes

### For Loop Syntax

```python
for variable in iterable:
    statement
```

### Range Syntax

```python
range(start, stop, step)
```

### Print Numbers

```python
for number in range(1, 6):
    print(number)
```

### Print in Reverse

```python
for number in range(5, 0, -1):
    print(number)
```

### Iterate Through a String

```python
for character in "PYTHON":
    print(character)
```

### Iterate Through a List

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

### Iterate Through a Dictionary

```python
student = {
    "name": "Amaan",
    "age": 22
}

for key, value in student.items():
    print(key, value)
```

### Use enumerate()

```python
names = ["Amaan", "Rahul", "Sameer"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

### Use zip()

```python
names = ["Amaan", "Rahul"]
marks = [85, 90]

for name, mark in zip(names, marks):
    print(name, mark)
```

### Calculate a Sum

```python
total = 0

for number in range(1, 6):
    total += number

print(total)
```

### Find Maximum

```python
numbers = [10, 50, 20, 70]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
```

### Linear Search

```python
numbers = [10, 20, 30, 40]

target = 30

for number in numbers:
    if number == target:
        print("Found")
        break
```

### Basic Complexity

| Pattern | Complexity |
|---|---|
| Fixed iterations | O(1) |
| Single traversal | O(N) |
| Two nested loops | O(N²) |
| Three nested loops | O(N³) |
| Two consecutive linear loops | O(N) |

---

## 30. Learning Checklist

### For Loop Fundamentals

- [ ] I understand what a `for` loop is.
- [ ] I understand why for loops are used.
- [ ] I understand what an iterable is.
- [ ] I understand what an iterator is.
- [ ] I understand the meaning of iteration.
- [ ] I can identify a loop variable.
- [ ] I understand loop indentation.

### Range Function

- [ ] I can use `range()` with one argument.
- [ ] I can use `range()` with two arguments.
- [ ] I can use `range()` with three arguments.
- [ ] I understand the exclusive stop value.
- [ ] I can use a negative step.
- [ ] I can print ascending sequences.
- [ ] I can print descending sequences.

### Working with Collections

- [ ] I can iterate through a string.
- [ ] I can iterate through a list.
- [ ] I can iterate through a tuple.
- [ ] I can iterate through a dictionary.
- [ ] I understand `keys()`.
- [ ] I understand `values()`.
- [ ] I understand `items()`.
- [ ] I can use `enumerate()`.
- [ ] I can use `zip()`.

### Problem Solving

- [ ] I can calculate a sum.
- [ ] I can calculate factorial.
- [ ] I can count vowels.
- [ ] I can find the maximum element.
- [ ] I can find the minimum element.
- [ ] I can perform linear search.
- [ ] I can count character frequency.
- [ ] I can filter elements using conditions.
- [ ] I can process positive, negative, and zero values.

### DSA Preparation

- [ ] I understand array traversal.
- [ ] I understand linear search.
- [ ] I understand nested loops.
- [ ] I can identify O(1) complexity.
- [ ] I can identify O(N) complexity.
- [ ] I can identify O(N²) complexity.

---

## 31. How to Run the Python File

### Step 1: Open Your Repository

Open the `DSA-Python` project in VS Code.

### Step 2: Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 02-For-Loop/
            ├── README.md
            └── 02_for_loop.py
```

### Step 3: Open the Terminal

Open the integrated terminal in VS Code.

### Step 4: Run the Python File

Execute the following command from the repository root:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/02-For-Loop/02_for_loop.py
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

## 32. Repository Structure

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
            └── 02-For-Loop/
                ├── README.md
                └── 02_for_loop.py
```

### File Responsibilities

**README.md**

Contains:

- Introduction.
- Learning objectives.
- For loop theory.
- Syntax.
- Iterable concepts.
- Range function.
- String, list, tuple, and dictionary iteration.
- `enumerate()` and `zip()`.
- Twelve topic examples.
- Twelve solved problems.
- Ten unsolved questions.
- Common mistakes.
- Best practices.
- Debugging.
- Real-life applications.
- DSA connections.
- Complexity analysis.
- Mini project.
- Fifty viva questions and answers.
- Terminology.
- Revision notes.
- Learning checklist.
- Execution instructions.

**02_for_loop.py**

Contains:

- Twelve executable topic examples.
- Twelve selectable solved problems.
- Ten unsolved practice questions.
- Learning checklist.
- Interactive menu.
- Input validation.

---

## 33. Final Summary

The `for` loop is an important Python control structure used to iterate through iterable objects.

It helps programmers process multiple values without writing repetitive statements.

A `for` loop can work with:

- Strings.
- Lists.
- Tuples.
- Sets.
- Dictionaries.
- Range objects.

The `range()` function is frequently used for numeric iteration.

The `enumerate()` function provides indexes and values.

The `zip()` function combines corresponding elements from multiple iterables.

Conditions inside a loop allow us to filter and classify values.

Nested loops support tasks such as pattern printing and pair comparisons.

For loops are also essential for DSA because they are used in traversal, searching, sorting, and data processing.

### What You Should Do Next

1. Read the theory and understand every example.
2. Run `02_for_loop.py`.
3. Execute all twelve examples.
4. Attempt all twelve solved problems.
5. Solve the ten unsolved questions independently.
6. Complete the learning checklist.
7. Revise the viva questions.
8. Understand the complexity of each algorithm.

**Topic Completed: For Loop in Python**

The next topic in this repository is:

`03-Range-Function`

Its Python source file will be:

`03_range_function.py`
