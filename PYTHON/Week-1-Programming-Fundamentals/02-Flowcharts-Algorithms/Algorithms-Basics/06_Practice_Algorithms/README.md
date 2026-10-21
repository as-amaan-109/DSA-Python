# Practice Algorithms

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Practice Algorithms  
> **Level:** Beginner  
> **Goal:** Apply algorithm steps, correctness, dry runs, and complexity analysis to practical problems.

---

## Table of Contents

1. Introduction
2. How to Approach a Problem
3. Addition of Two Numbers
4. Subtraction and Multiplication
5. Average of a List
6. Area of a Rectangle
7. Celsius to Fahrenheit
8. Square of a Number
9. Even or Odd
10. Find the Largest Number
11. Linear Search
12. Binary Search
13. Reverse a List
14. Count Element Frequencies
15. Factorial
16. Time and Space Complexity Summary
17. Testing and Edge Cases
18. Common Beginner Mistakes
19. Interview Questions
20. Practice Questions
21. Learning Checklist
22. What's Next?

---

## 1. Introduction

Learning an algorithm's definition is only the first step. To develop problem-solving skills, we must practise converting problem statements into logical steps and working Python programs.

This topic combines the concepts covered in the previous folders:

- Algorithm Basics
- Algorithm Steps
- Algorithm Examples
- Algorithm Characteristics
- Algorithm Analysis

For each problem, identify the inputs, write the algorithm, implement it in Python, test the result, and understand its complexity.

---

## 2. How to Approach a Problem

Follow this method whenever you receive a coding question.

### Step 1: Understand the Problem

Read the question carefully and identify the required result.

### Step 2: Identify Inputs and Outputs

Determine which values the algorithm needs and what it must produce.

### Step 3: Design the Logic

Write the mathematical formula or ordered steps.

### Step 4: Implement the Solution

Convert the algorithm into Python code.

### Step 5: Test the Solution

Try normal values, edge cases, and invalid inputs where relevant.

### Step 6: Analyze Complexity

Estimate the algorithm's time and auxiliary space complexity.

The general workflow is:

```text
Problem
   |
   v
Understand Inputs and Outputs
   |
   v
Write Algorithm Steps
   |
   v
Implement in Python
   |
   v
Test the Result
   |
   v
Analyze Complexity
```

---

## 3. Addition of Two Numbers

### Problem

Calculate the sum of two numbers.

### Formula

```text
Sum = A + B
```

### Algorithm

1. Start.
2. Obtain A and B.
3. Calculate `SUM = A + B`.
4. Display SUM.
5. Stop.

### Python Code

```python
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 20))
```

### Output

```text
30
```

### Complexity

- Time: `O(1)`
- Auxiliary space: `O(1)`

This assumes a fixed number of operations on fixed-size numeric values.

### Practice

Test the function with positive values, negative values, and zero.

---

## 4. Subtraction and Multiplication

### Subtraction

Formula:

```text
Difference = A - B
```

```python
def subtract_numbers(a, b):
    return a - b

print(subtract_numbers(25, 10))
```

Output:

```text
15
```

**Important:** The order matters. `25 - 10` is not the same as `10 - 25`.

### Multiplication

Formula:

```text
Product = A * B
```

```python
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(6, 7))
```

Output:

```text
42
```

### Complexity

Both examples use a fixed number of operations, so their time and auxiliary space complexities are `O(1)` under the usual fixed-size numeric model.

---

## 5. Average of a List

### Problem

Calculate the average of a list of numbers.

### Formula

```text
Average = Sum of all values / Number of values
```

### Algorithm

1. Check that the list contains at least one element.
2. Initialize a total to zero.
3. Visit every number and add it to the total.
4. Divide the total by the number of elements.
5. Return the average.

### Python Code

```python
def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list must not be empty.")

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

print(calculate_average([10, 20, 30]))
```

### Output

```text
20.0
```

### Dry Run

| Step | Operation | Total |
|---|---|---:|
| 1 | Initialize total | 0 |
| 2 | Add 10 | 10 |
| 3 | Add 20 | 30 |
| 4 | Add 30 | 60 |
| 5 | Divide by 3 | 20.0 |

### Complexity

- Time: `O(n)`, because every element is processed once.
- Auxiliary space: `O(1)`, because only a running total and a fixed number of other variables are used.

Here, `n` is the number of elements.

### Edge Case

An empty list has no average under this definition. The implementation raises `ValueError` rather than dividing by zero.

---

## 6. Area of a Rectangle

### Problem

Calculate the area of a rectangle from its length and breadth.

### Formula

```text
Area = Length × Breadth
```

### Algorithm

1. Obtain length and breadth.
2. Multiply the two values.
3. Return or display the area.

### Python Code

```python
def rectangle_area(length, breadth):
    return length * breadth

print(rectangle_area(8, 4))
```

### Output

```text
32
```

If length and breadth are measured in centimetres, the area is measured in square centimetres.

### Complexity

- Time: `O(1)`
- Auxiliary space: `O(1)`

This example performs a fixed number of arithmetic operations.

---

## 7. Celsius to Fahrenheit

### Problem

Convert a temperature in Celsius to Fahrenheit.

### Formula

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

### Algorithm

1. Obtain the Celsius temperature.
2. Multiply it by 9.
3. Divide the result by 5.
4. Add 32.
5. Return the Fahrenheit result.

### Python Code

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(celsius_to_fahrenheit(25))
```

### Output

```text
77.0
```

### Complexity

- Time: `O(1)`
- Auxiliary space: `O(1)`

---

## 8. Square of a Number

### Problem

Calculate the square of a number.

### Formula

```text
Square = Number × Number
```

### Python Code

```python
def square_number(number):
    return number * number

print(square_number(9))
```

### Output

```text
81
```

### Complexity

- Time: `O(1)`
- Auxiliary space: `O(1)`

For fixed-size numeric values, calculating the square uses a constant number of operations.

---

## 9. Even or Odd

### Problem

Determine whether an integer is even or odd.

### Concept

The modulo operator `%` calculates a remainder.

If an integer divided by 2 has remainder zero, it is even. Otherwise, it is odd.

### Algorithm

1. Obtain an integer.
2. Calculate `number % 2`.
3. If the remainder is zero, return that the number is even.
4. Otherwise, return that it is odd.

### Python Code

```python
def is_even(number):
    return number % 2 == 0

print(is_even(12))
print(is_even(17))
```

### Output

```text
True
False
```

The first result means 12 is even. The second means 17 is odd.

### Complexity

- Time: `O(1)`
- Auxiliary space: `O(1)`

### Practice

Test with zero, a negative integer, and a positive integer.

---

## 10. Find the Largest Number

### Problem

Find the largest number in a list.

### Algorithm

1. Check that the list is not empty.
2. Assume the first element is the largest.
3. Visit every remaining element.
4. If the current element is larger, update the largest value.
5. Return the final largest value.

### Python Code

```python
def find_largest(numbers):
    if not numbers:
        raise ValueError("The list must not be empty.")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest

numbers = [34, 67, 89, 12, 60]

print(find_largest(numbers))
```

### Output

```text
89
```

### Dry Run

| Current number | Largest value |
|---:|---:|
| 34 | 34 |
| 67 | 67 |
| 89 | 89 |
| 12 | 89 |
| 60 | 89 |

### Complexity

- Time: `O(n)`, because the algorithm examines every element.
- Auxiliary space: `O(1)`, using a fixed number of variables.

The slice `numbers[1:]` shown in this implementation creates a copy in Python. If strict constant auxiliary space is required, use an index-based loop instead:

```python
for index in range(1, len(numbers)):
    if numbers[index] > largest:
        largest = numbers[index]
```

That avoids creating the slice.

---

## 11. Linear Search

### Problem

Find the index of a target value in a list.

### Algorithm

1. Start at the first element.
2. Compare each element with the target.
3. Return the index when a match is found.
4. If no match is found, return `-1`.

### Python Code

```python
def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index

    return -1

numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 40))
print(linear_search(numbers, 99))
```

### Output

```text
3
-1
```

The target `40` is at index 3. The target `99` is absent, so the function returns `-1`.

### Complexity

| Case | Time Complexity |
|---|---|
| Best case | `O(1)` |
| Average case | `O(n)` under common assumptions |
| Worst case | `O(n)` |

Auxiliary space: `O(1)`.

### Important Point

Linear search does not require the list to be sorted.

---

## 12. Binary Search

### Problem

Find a target value in a sorted list.

### Important Requirement

**Binary search requires sorted input.** The implementation in this section assumes ascending order.

### Algorithm

1. Set pointers to the beginning and end of the list.
2. Find the middle index.
3. If the middle value equals the target, return the index.
4. If the target is larger, search the right half.
5. Otherwise, search the left half.
6. Repeat until the target is found or the range becomes empty.

### Python Code

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

numbers = [3, 7, 11, 15, 19, 23, 27, 31]

print(binary_search(numbers, 23))
print(binary_search(numbers, 8))
```

### Output

```text
5
-1
```

### Complexity

- Best-case time: `O(1)`.
- Worst-case time: `O(log n)`.
- Auxiliary space: `O(1)` for this iterative implementation.

### Why Is Binary Search Efficient?

After each unsuccessful comparison, it discards roughly half of the remaining search range.

This is why its number of comparisons grows logarithmically with input size.

---

## 13. Reverse a List

### Problem

Return a new list containing the same values in reverse order.

### Example

Input:

```text
[1, 2, 3, 4, 5]
```

Output:

```text
[5, 4, 3, 2, 1]
```

### Algorithm

1. Create a copy of the input list.
2. Set a left pointer to the first index and a right pointer to the last index.
3. Swap the values at those positions.
4. Move the left pointer forward and the right pointer backward.
5. Continue until the pointers meet or cross.
6. Return the reversed list.

### Python Code

```python
def reverse_list(numbers):
    reversed_numbers = numbers.copy()

    left = 0
    right = len(reversed_numbers) - 1

    while left < right:
        reversed_numbers[left], reversed_numbers[right] = (
            reversed_numbers[right],
            reversed_numbers[left]
        )
        left += 1
        right -= 1

    return reversed_numbers

print(reverse_list([1, 2, 3, 4, 5]))
```

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(n)`, because a copy of the input is created.

This implementation preserves the original list.

---

## 14. Count Element Frequencies

### Problem

Count how many times each value occurs in a list.

### Example

Input:

```text
[1, 2, 2, 3, 1, 4, 2]
```

Output:

```text
{1: 2, 2: 3, 3: 1, 4: 1}
```

### Algorithm

1. Create an empty dictionary.
2. Visit each element.
3. If the element exists in the dictionary, increase its count.
4. Otherwise, add it with a count of 1.
5. Return the dictionary.

### Python Code

```python
def count_frequency(numbers):
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return counts

numbers = [1, 2, 2, 3, 1, 4, 2]

print(count_frequency(numbers))
```

### Complexity

Let:

- `n` be the total number of elements.
- `k` be the number of distinct values.

With ordinary dictionary operations, the average time complexity is `O(n)`.

The auxiliary space complexity is `O(k)` because the dictionary stores one entry for each distinct value.

In the worst case, `k` can equal `n`.

---

## 15. Factorial

### Problem

Calculate the factorial of a non-negative integer.

### Definition

For a positive integer:

```text
n! = n × (n - 1) × (n - 2) × ... × 2 × 1
```

By definition:

```text
0! = 1
```

### Example

```text
5! = 5 × 4 × 3 × 2 × 1
5! = 120
```

### Algorithm

1. Check that the input is a non-negative integer.
2. Initialize the result to 1.
3. Multiply the result by each integer from 2 through n.
4. Return the result.

### Python Code

```python
def factorial(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("The number must be an integer.")

    if number < 0:
        raise ValueError("Factorial is not defined here for negatives.")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result

print(factorial(5))
print(factorial(0))
```

### Output

```text
120
1
```

### Complexity

- Time: `O(n)`.
- Auxiliary space: `O(1)` in the basic operation-counting model.

The number of iterations grows with the input `n`.

---

## 16. Time and Space Complexity Summary

| Problem | Time Complexity | Auxiliary Space | Important Note |
|---|---|---|---|
| Add two numbers | `O(1)` | `O(1)` | Fixed number of operations |
| Subtract two numbers | `O(1)` | `O(1)` | Fixed number of operations |
| Multiply two numbers | `O(1)` | `O(1)` | Fixed-size numeric model |
| Average of a list | `O(n)` | `O(1)` | Every element is visited once |
| Rectangle area | `O(1)` | `O(1)` | Single calculation |
| Celsius conversion | `O(1)` | `O(1)` | Fixed number of calculations |
| Check even or odd | `O(1)` | `O(1)` | One remainder operation |
| Find largest element | `O(n)` | `O(1)` | Every element must be considered |
| Linear search | `O(n)` worst case | `O(1)` | Does not require sorted data |
| Binary search | `O(log n)` worst case | `O(1)` | Requires sorted data |
| Reverse a list | `O(n)` | `O(n)` | A copy is created |
| Count frequencies | `O(n)` average | `O(k)` | Dictionary stores distinct values |
| Factorial | `O(n)` | `O(1)` | Iterative calculation |

These complexities describe growth under the usual introductory analysis model. Exact runtime also depends on input types, implementation details, and the execution environment.

---

## 17. Testing and Edge Cases

A good solution should be checked using more than one example.

### What Is an Edge Case?

An edge case is an input at a boundary or an unusual part of the valid input domain that is important to test.

### Examples

**Addition**
- Two positive numbers.
- A negative number and a positive number.
- Zero as an input.

**Largest element**
- A list containing one element.
- All elements are negative.
- Multiple elements share the largest value.
- An empty list, which should be handled according to the problem specification.

**Linear search**
- Target at the first index.
- Target at the last index.
- Target missing from the list.
- An empty list.

**Binary search**
- Target equals the middle element.
- Target is smaller than all elements.
- Target is greater than all elements.
- Target is absent.
- An empty sorted list.

**Factorial**
- `0`.
- `1`.
- A positive integer.
- A negative or non-integer input.

Testing these cases helps identify errors that ordinary examples might not reveal.

---

## 18. Common Beginner Mistakes

### Mistake 1: Ignoring Empty Inputs

An empty list has no average or largest element under the definitions used in this topic.

**Solution:** Check whether the input is valid before processing it.

### Mistake 2: Using Binary Search on an Unsorted List

Binary search relies on sorted data.

**Solution:** Ensure the list is sorted, or choose linear search when the input is not sorted.

### Mistake 3: Forgetting That Indexing Starts at Zero

In Python, the first element is at index 0.

For example:

```python
numbers = [10, 20, 30]
print(numbers[0])
```

Output:

```text
10
```

### Mistake 4: Confusing a Value with Its Index

In linear and binary search, returning `3` means index 3, not necessarily that the target value is 3.

### Mistake 5: Ignoring Auxiliary Space

Creating a new list uses additional memory.

**Solution:** Analyze the data structures the algorithm creates, not just its loop count.

### Mistake 6: Returning the Wrong Result

A search algorithm should return a consistent result when the target is missing.

This topic uses `-1` to mean "not found".

---

## 19. Interview Questions

### Q1. What is an algorithm?

An algorithm is a finite sequence of clear and ordered steps used to solve a problem.

### Q2. What is the difference between linear search and binary search?

Linear search checks elements one by one and works on unsorted data. Binary search repeatedly halves a search range and requires sorted data.

### Q3. What is the worst-case time complexity of linear search?

`O(n)`, because it may need to check every element.

### Q4. What is the worst-case time complexity of binary search?

`O(log n)`, when the input is sorted and the standard binary search algorithm is used.

### Q5. How do you find the largest element in a list?

Start with the first element as the current largest and compare every remaining element. Update the largest value whenever a greater value is found.

### Q6. Why should an empty list be checked before calculating an average?

Because the average requires dividing the sum by the number of elements, and an empty list has a count of zero.

### Q7. What is the time complexity of finding the largest element?

`O(n)`, because every list element must be considered in the general case.

### Q8. What is the difference between time complexity and auxiliary space complexity?

Time complexity describes the growth of computational work. Auxiliary space complexity describes additional memory usage.

### Q9. What is factorial?

For a non-negative integer n, its factorial is the product of all positive integers from 1 to n, with `0! = 1`.

### Q10. How can you count element frequencies efficiently?

Use a dictionary to store each distinct value and its count. This usually takes average `O(n)` time for `n` elements.

---

## 20. Practice Questions

Try to write the algorithm and Python implementation for each question.

### Beginner Level

**Question 1:** Write a function to calculate the sum of three numbers.

**Question 2:** Write a function to calculate the cube of a number.

**Question 3:** Write a function to convert kilometres into metres.

**Question 4:** Write a function to calculate the perimeter of a rectangle.

**Question 5:** Write a function to determine whether an integer is positive, negative, or zero.

### Intermediate Level

**Question 6:** Write a function that returns the smallest element in a non-empty list.

**Question 7:** Write a function that counts how many even numbers occur in a list.

**Question 8:** Write a function that returns the index of the first occurrence of a target.

**Question 9:** Write a function that returns a reversed copy of a list.

**Question 10:** Write a function that counts the frequency of each element in a list.

### Challenge

**Question 11:** Write an iterative binary search and test it with a sorted list.

**Question 12:** Write a function that calculates factorial iteratively.

**Question 13:** Explain the time and auxiliary space complexities of your largest-element solution.

**Question 14:** Create test cases for linear search when the target is found, missing, or searched for in an empty list.

**Question 15:** Compare linear search and binary search and explain which one is appropriate for a given input.

For each problem:

1. Write the algorithm steps.
2. Implement the solution in Python.
3. Test normal cases and edge cases.
4. Record time and auxiliary space complexity.

---

## 21. Learning Checklist

- [ ] Implement basic arithmetic algorithms.
- [ ] Calculate averages and rectangle areas.
- [ ] Convert Celsius to Fahrenheit.
- [ ] Check even or odd.
- [ ] Find the largest element.
- [ ] Implement linear search.
- [ ] Implement binary search.
- [ ] Reverse a list.
- [ ] Count element frequencies.
- [ ] Calculate factorial.
- [ ] Handle empty inputs where appropriate.
- [ ] Test edge cases.
- [ ] Explain time complexity.
- [ ] Explain auxiliary space complexity.
- [ ] Solve the practice questions independently.

---

## 22. What's Next?

You have now completed the planned six folders under **Algorithms-Basics**.

The next step is to review the concepts and then continue with the Flowcharts section using its own folder structure.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `06_practice_algorithms.py` | Runnable implementations of basic algorithms |
| `README.md` | Detailed notes, algorithm steps, complexity analysis, testing guidance, and practice questions |

---

## Conclusion

Practice is what turns algorithm theory into problem-solving ability.

For every new question, understand the requirements, write the steps, implement the logic, test multiple inputs, and analyze the resources used.

**Understand → Design → Implement → Test → Analyze**

Repeat this process for every practice problem to develop a strong foundation for Data Structures and Algorithms.