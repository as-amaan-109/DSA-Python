# Recursion in Python

## 1. Introduction

Recursion is a programming technique in which a function calls itself to solve a problem.

A recursive function breaks a large problem into smaller versions of the same problem until it reaches a condition where no further function calls are required.

Recursion is an important concept in Python and Data Structures and Algorithms (DSA). It is commonly used in tree traversal, graph algorithms, searching, sorting, backtracking, and mathematical problems.

### Learning Objectives

After completing this topic, you will be able to:

- Understand the meaning of recursion.
- Identify base cases and recursive cases.
- Understand how the function call stack works.
- Write recursive functions in Python.
- Solve mathematical problems using recursion.
- Apply recursion to strings and lists.
- Understand recursive searching algorithms.
- Differentiate recursion from iteration.
- Analyze time and space complexity.
- Recognize recursion depth limitations.

---

## 2. What Is Recursion?

Recursion occurs when a function calls itself directly or indirectly.

### Example: Countdown

```python
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)
```

### Output

```text
5
4
3
2
1
Done!
```

### Explanation

1. The function receives `5`.
2. It prints `5`.
3. It calls itself with `4`.
4. This continues until the number becomes `0`.
5. The base condition stops further recursive calls.

A recursive function generally contains two important parts:

### A. Base Case

The base case is the stopping condition of recursion.

Without a valid base case, a recursive function may continue calling itself until Python raises a `RecursionError`.

Example:

```python
if number == 0:
    return
```

### B. Recursive Case

The recursive case is the part where a function calls itself with a smaller or simpler problem.

Example:

```python
countdown(number - 1)
```

### Basic Structure of Recursion

```python
def recursive_function(parameters):

    # Base Case
    if stopping_condition:
        return result

    # Recursive Case
    return recursive_function(smaller_problem)
```

**Important:** Every recursive call should make progress toward the base case.

---

## 3. How the Call Stack Works

Python uses a call stack to manage function calls.

Whenever a function is called, a new stack frame is created. The frame stores information such as local variables and where execution should continue after the function returns.

When a recursive function calls itself, another stack frame is added.

When the base case is reached, the function calls start returning in reverse order.

### Example: Factorial of 4

```python
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(4))
```

### Recursive Calls

```text
factorial(4)
    4 * factorial(3)
        3 * factorial(2)
            2 * factorial(1)
                1 * factorial(0)
```

### Returning Process

```text
factorial(0) = 1
factorial(1) = 1 * 1 = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
```

### Output

```text
24
```

**Remember:** Recursive calls move toward the base case, and results return in the opposite direction.

---

## 4. Recursion vs Iteration

Iteration uses loops such as `for` and `while`, whereas recursion uses function calls.

| Feature | Recursion | Iteration |
|---|---|---|
| Technique | Function calls itself | Repeats using loops |
| Stopping condition | Base case | Loop condition |
| Memory | Uses call stack | Usually uses less extra memory |
| Code | Can be shorter for recursive structures | Often straightforward for repeated operations |
| Performance | Function-call overhead | Usually lower overhead |
| Risk | Recursion depth limit | Infinite loop if condition is incorrect |
| Common uses | Trees, backtracking, divide and conquer | Traversals, counting, repeated calculations |

### Example: Sum Using Iteration

```python
def iterative_sum(number):
    total = 0

    for value in range(1, number + 1):
        total += value

    return total


print(iterative_sum(5))
```

### Example: Sum Using Recursion

```python
def recursive_sum(number):
    if number == 0:
        return 0

    return number + recursive_sum(number - 1)


print(recursive_sum(5))
```

Both produce:

```text
15
```

---

# 5. Important Recursion Examples

The following examples cover the 12 concepts demonstrated in `09_recursion.py`.

## Example 1: Basic Recursion

```python
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)
```

**Explanation:** The function prints a number and calls itself with one less until it reaches zero.

## Example 2: Base Case and Recursive Case

```python
def sum_to_n(number):
    if number == 0:
        return 0

    return number + sum_to_n(number - 1)


print(sum_to_n(5))
```

**Output:**

```text
15
```

**Explanation:** The base case returns zero. The recursive case adds the current number to the sum of smaller numbers.

## Example 3: Factorial Call-Stack Trace

```python
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(4))
```

**Output:**

```text
24
```

**Explanation:** Factorial is calculated by multiplying a number by the factorial of the previous number.

## Example 4: Sum of Natural Numbers

```python
def sum_natural(number):
    if number == 0:
        return 0

    return number + sum_natural(number - 1)


print(sum_natural(10))
```

**Output:**

```text
55
```

## Example 5: Fibonacci Using Memoized Recursion

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


for index in range(10):
    print(fibonacci(index), end=" ")
```

**Output:**

```text
0 1 1 2 3 5 8 13 21 34
```

**Explanation:** Memoization stores previously calculated results so they can be reused instead of recalculated.

## Example 6: Naive vs Memoized Fibonacci

Naive recursive approach:

```python
def fibonacci_naive(number):
    if number <= 1:
        return number

    return fibonacci_naive(number - 1) + fibonacci_naive(number - 2)


print(fibonacci_naive(7))
```

Memoized approach:

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_memoized(number):
    if number <= 1:
        return number

    return (
        fibonacci_memoized(number - 1)
        + fibonacci_memoized(number - 2)
    )


print(fibonacci_memoized(7))
```

Both return:

```text
13
```

**Explanation:** Naive Fibonacci repeatedly calculates overlapping subproblems. Memoization stores results and improves the time complexity.

## Example 7: Recursive Power

```python
def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / power(base, -exponent)

    half = power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


print(power(2, 5))
```

**Output:**

```text
32
```

**Explanation:** Exponentiation by squaring reduces the exponent by approximately half in each recursive call.

## Example 8: Reverse a String

```python
def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print(reverse_string("Python"))
```

**Output:**

```text
nohtyP
```

**Explanation:** The function recursively reverses the remaining string and places the first character at the end.

## Example 9: Palindrome Checking

```python
def is_palindrome(text):
    text = text.lower()

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("madam"))
```

**Output:**

```text
True
```

**Explanation:** The first and last characters are compared repeatedly until the string becomes empty or a mismatch is found.

## Example 10: GCD Using Recursion

```python
def gcd(first, second):
    if second == 0:
        return abs(first)

    return gcd(second, first % second)


print(gcd(48, 18))
```

**Output:**

```text
6
```

**Explanation:** The Euclidean algorithm repeatedly replaces the pair with the second number and the remainder.

## Example 11: Recursive Binary Search

```python
def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search(numbers, target, left, middle - 1)

    return binary_search(numbers, target, middle + 1, right)


numbers = [10, 20, 30, 40, 50, 60]

print(binary_search(numbers, 40, 0, len(numbers) - 1))
```

**Output:**

```text
3
```

**Explanation:** Binary search repeatedly divides a sorted search range into two halves.

## Example 12: Flatten a Nested List

```python
def flatten_list(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


data = [1, [2, 3], [4, [5, 6]]]

print(flatten_list(data))
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

**Explanation:** The function checks whether each item is another list. Nested lists are recursively flattened.

---

# 6. Twelve Solved Recursion Problems

These problems match the solved-problem section of the Python source file.

## Problem 1: Find the Factorial of a Number

**Problem:** Write a recursive function to calculate the factorial of a non-negative integer.

**Logic:** Multiply the number by the factorial of the number minus one. The factorial of zero is one.

```python
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    print("Factorial:", factorial(number))
```

**Sample Input:**

```text
Enter a number: 5
```

**Sample Output:**

```text
Factorial: 120
```

**Complexity:** Time O(n), auxiliary call-stack space O(n).

## Problem 2: Find the Sum of Natural Numbers

**Problem:** Calculate the sum of natural numbers from 1 to n using recursion.

**Logic:** Add the current number to the sum of all smaller positive numbers.

```python
def sum_natural(number):
    if number == 0:
        return 0

    return number + sum_natural(number - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Enter a non-negative number.")
else:
    print("Sum:", sum_natural(number))
```

**Sample Input:**

```text
Enter a number: 10
```

**Sample Output:**

```text
Sum: 55
```

**Complexity:** Time O(n), auxiliary space O(n).

## Problem 3: Generate a Fibonacci Number

**Problem:** Find the Fibonacci number at a given zero-based position using memoized recursion.

**Logic:** Each Fibonacci number is the sum of the two preceding numbers.

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


position = int(input("Enter Fibonacci position: "))

if position < 0:
    print("Position must be non-negative.")
else:
    print("Fibonacci number:", fibonacci(position))
```

**Sample Input:**

```text
Enter Fibonacci position: 7
```

**Sample Output:**

```text
Fibonacci number: 13
```

**Complexity:** Time O(n), auxiliary cache and call-stack space O(n).

## Problem 4: Calculate Power Using Recursion

**Problem:** Calculate base raised to the power of exponent using exponentiation by squaring.

**Logic:** Divide the exponent by two recursively, then square the result.

```python
def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        if base == 0:
            raise ValueError("Zero cannot have a negative exponent.")

        return 1 / power(base, -exponent)

    half = power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

try:
    print("Result:", power(base, exponent))
except ValueError as error:
    print("Error:", error)
```

**Sample Input:**

```text
Enter base: 2
Enter exponent: 5
```

**Sample Output:**

```text
Result: 32.0
```

**Complexity:** Time O(log |n|), auxiliary space O(log |n|).

## Problem 5: Reverse a String Using Recursion

**Problem:** Reverse a string without using a loop for the reversal.

**Logic:** Recursively reverse the substring after the first character and append the first character.

```python
def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed string:", reverse_string(text))
```

**Sample Input:**

```text
Enter a string: Python
```

**Sample Output:**

```text
Reversed string: nohtyP
```

**Complexity:** Time O(n²) due to repeated slicing and string concatenation; auxiliary call-stack space O(n), excluding temporary string allocations.

## Problem 6: Check Whether a String Is a Palindrome

**Problem:** Check whether a string reads the same forward and backward.

**Logic:** Compare the first and last characters. If they match, recursively check the inner substring.

```python
def palindrome_check(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome_check(text[1:-1])


text = input("Enter a string: ")

print("Palindrome:", palindrome_check(text))
```

**Sample Input:**

```text
Enter a string: madam
```

**Sample Output:**

```text
Palindrome: True
```

**Complexity:** Time O(n²) for this slicing-based implementation; auxiliary call-stack space O(n).

## Problem 7: Find the GCD of Two Numbers

**Problem:** Find the Greatest Common Divisor of two integers using recursion.

**Logic:** Apply the Euclidean algorithm until the second number becomes zero.

```python
def gcd(first, second):
    if second == 0:
        return abs(first)

    return gcd(second, first % second)


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("GCD:", gcd(first, second))
```

**Sample Input:**

```text
Enter first number: 48
Enter second number: 18
```

**Sample Output:**

```text
GCD: 6
```

**Complexity:** Time O(log min(|a|, |b|)) for non-zero inputs; auxiliary space O(log min(|a|, |b|)).

## Problem 8: Search an Element Using Recursive Linear Search

**Problem:** Find the position of a target element in a list using recursion.

**Logic:** Check the current position. If the element is not found, search the next position.

```python
def linear_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return linear_search(numbers, target, index + 1)


numbers = [10, 20, 30, 40, 50]

target = int(input("Enter target element: "))

position = linear_search(numbers, target)

if position == -1:
    print("Element not found.")
else:
    print("Element found at index:", position)
```

**Sample Input:**

```text
Enter target element: 30
```

**Sample Output:**

```text
Element found at index: 2
```

**Complexity:** Time O(n), auxiliary space O(n).

## Problem 9: Search an Element Using Recursive Binary Search

**Problem:** Find the index of an element in a sorted list using recursive binary search.

**Logic:** Calculate the middle index and recursively search the appropriate half.

```python
def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search(numbers, target, left, middle - 1)

    return binary_search(numbers, target, middle + 1, right)


numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter target element: "))

position = binary_search(numbers, target, 0, len(numbers) - 1)

if position == -1:
    print("Element not found.")
else:
    print("Element found at index:", position)
```

**Sample Input:**

```text
Enter target element: 50
```

**Sample Output:**

```text
Element found at index: 4
```

**Complexity:** Time O(log n), auxiliary space O(log n). The input list must be sorted.

## Problem 10: Find the Sum of List Elements

**Problem:** Calculate the sum of all elements in a list using recursion.

**Logic:** Add the first element to the sum of the remaining elements.

```python
def recursive_list_sum(numbers, index=0):
    if index == len(numbers):
        return 0

    return numbers[index] + recursive_list_sum(numbers, index + 1)


numbers = [10, 20, 30, 40, 50]

print("List sum:", recursive_list_sum(numbers))
```

**Sample Output:**

```text
List sum: 150
```

**Complexity:** Time O(n), auxiliary space O(n).

## Problem 11: Count Occurrences of an Element

**Problem:** Count how many times a given element appears in a list.

**Logic:** Check the current element and add one when it matches the target.

```python
def count_occurrences(numbers, target, index=0):
    if index == len(numbers):
        return 0

    current_count = 1 if numbers[index] == target else 0

    return current_count + count_occurrences(
        numbers,
        target,
        index + 1
    )


numbers = [10, 20, 10, 30, 10, 40]

target = int(input("Enter target element: "))

print("Occurrences:", count_occurrences(numbers, target))
```

**Sample Input:**

```text
Enter target element: 10
```

**Sample Output:**

```text
Occurrences: 3
```

**Complexity:** Time O(n), auxiliary space O(n).

## Problem 12: Flatten a Nested List

**Problem:** Convert a nested list into a single-level list using recursion.

**Logic:** If an element is a list, recursively flatten it. Otherwise, add the element to the result.

```python
def flatten_nested_list(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)

    return result


data = [1, [2, 3], [4, [5, 6]], 7]

print("Flattened list:", flatten_nested_list(data))
```

**Sample Output:**

```text
Flattened list: [1, 2, 3, 4, 5, 6, 7]
```

**Complexity:** O(N) traversal time, where N is the total number of elements and nested-list containers visited. Output storage is O(L), where L is the number of leaf elements. Auxiliary call-stack space depends on maximum nesting depth D and is O(D).

---

# 7. Ten Unsolved Practice Questions

Try to solve these questions independently before checking other solutions.

| No. | Practice Question | Difficulty |
|---|---|---|
| 1 | Find the sum of digits of a number using recursion. | Easy |
| 2 | Find the product of digits of a number using recursion. | Easy |
| 3 | Convert a decimal number into binary using recursion. | Medium |
| 4 | Find the minimum element in a list using recursion. | Easy |
| 5 | Count uppercase characters in a string using recursion. | Easy |
| 6 | Remove spaces from a string using recursion. | Medium |
| 7 | Calculate the sum of all even numbers in a list using recursion. | Medium |
| 8 | Calculate a power using exponentiation by squaring, including negative exponents. | Medium |
| 9 | Check whether two strings are equal using recursion. | Medium |
| 10 | Flatten a nested list using recursion. | Medium |

### Practice Guidelines

For every problem:

1. Identify the input and expected output.
2. Find a suitable base case.
3. Define how the problem becomes smaller.
4. Write the recursive function.
5. Test with small inputs.
6. Analyze time and space complexity.

---

# 8. Common Mistakes in Recursion

### 1. Missing Base Case

Incorrect:

```python
def calculate(number):
    return number + calculate(number - 1)
```

This function never stops for ordinary positive input.

Correct:

```python
def calculate(number):
    if number == 0:
        return 0

    return number + calculate(number - 1)
```

### 2. Recursive Call Does Not Make Progress

Incorrect:

```python
def display(number):
    if number == 0:
        return

    display(number)
```

The input never changes, so the base case is never reached.

Correct:

```python
def display(number):
    if number == 0:
        return

    print(number)
    display(number - 1)
```

### 3. Forgetting the Return Statement

Incorrect:

```python
def factorial(number):
    if number == 0:
        return 1

    number * factorial(number - 1)
```

The recursive result is calculated but not returned.

Correct:

```python
def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)
```

### 4. Incorrect Base-Case Result

The base case must return a result that fits the problem.

For example, factorial uses `1` as its base result, while the sum of natural numbers uses `0`.

### 5. Ignoring Recursion Depth

Deep recursion can raise:

```text
RecursionError: maximum recursion depth exceeded
```

Python has a recursion-depth limit. Large inputs should be handled carefully. Iteration may be more appropriate when the recursive depth would become too large.

### 6. Using Naive Fibonacci for Large Inputs

Naive Fibonacci repeats the same calculations many times. Memoization improves execution time, but it does not eliminate recursive call depth.

---

# 9. Recursion and Time-Space Complexity

Complexity describes how an algorithm's resource requirements grow as input size increases.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Countdown | O(n) | O(n) |
| Factorial | O(n) | O(n) |
| Sum of natural numbers | O(n) | O(n) |
| Naive Fibonacci | O(2^n) upper bound | O(n) |
| Memoized Fibonacci | O(n) | O(n) |
| Recursive power | O(log n) | O(log n) |
| Reverse string using slicing | O(n²) | O(n) call stack |
| Palindrome using slicing | O(n²) | O(n) call stack |
| GCD | O(log min(a, b)) | O(log min(a, b)) |
| Linear search | O(n) | O(n) |
| Binary search | O(log n) | O(log n) |
| Recursive list sum | O(n) | O(n) |
| Count occurrences | O(n) | O(n) |
| Flatten nested list | O(N) traversal | O(D) call stack |

Here:

- `n` represents the input size.
- `N` represents all elements and nested-list containers traversed.
- `D` represents maximum nesting depth.

**Note:** Auxiliary space describes extra memory used by the algorithm. It does not include the original input. Memoization also uses memory to store cached results.

---

# 10. Real-World Applications of Recursion

Recursion is widely used in software development and computer science.

### 1. File and Folder Traversal

A folder can contain files and other folders. A recursive function can visit every nested folder.

### 2. Tree Data Structures

Recursion is commonly used to traverse binary trees and other hierarchical structures.

### 3. Graph Algorithms

Depth-First Search (DFS) can be implemented recursively.

### 4. Backtracking

Problems such as maze solving, Sudoku, and generating permutations often use recursion.

### 5. Divide and Conquer

Algorithms such as Merge Sort and Quick Sort divide problems into smaller parts.

### 6. Nested Data Processing

Nested dictionaries, lists, JSON data, and hierarchical categories can be processed recursively.

### 7. Mathematical Calculations

Factorial, Fibonacci, GCD, and power calculations are common examples.

---

# 11. Connection Between Recursion and DSA

Recursion is a foundation for several important DSA concepts.

| DSA Concept | How Recursion Is Used |
|---|---|
| Binary Trees | Traversing left and right subtrees |
| Binary Search | Repeatedly dividing a sorted search range |
| Merge Sort | Sorting smaller subarrays |
| Quick Sort | Sorting partitions recursively |
| Graph DFS | Visiting connected vertices |
| Backtracking | Exploring possible choices |
| Dynamic Programming | Solving overlapping subproblems with memoization |
| Permutations | Generating arrangements recursively |
| Combinations | Generating selected groups |
| Divide and Conquer | Breaking a problem into smaller subproblems |

### Recommended Learning Order

```text
Recursion Basics
      |
      v
Base Case and Recursive Case
      |
      v
Call Stack
      |
      v
Recursive Mathematical Problems
      |
      v
Recursion with Strings and Lists
      |
      v
Binary Search
      |
      v
Divide and Conquer
      |
      v
Backtracking
      |
      v
Trees and Graphs
      |
      v
Dynamic Programming
```

---

# 12. Mini Project: Recursive Nested List Analyzer

## Project Description

Create a program that analyzes a nested list containing integers and other nested lists.

The program should:

- Flatten the nested list.
- Calculate the sum of all integer elements.
- Count the total integer elements.
- Find the minimum and maximum values.
- Support multiple nesting levels.

### Complete Code

```python
def flatten_list(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


def analyze_nested_list(data):
    flattened = flatten_list(data)

    if not flattened:
        return {
            "count": 0,
            "sum": 0,
            "minimum": None,
            "maximum": None
        }

    if not all(isinstance(value, int) for value in flattened):
        raise ValueError("All leaf elements must be integers.")

    return {
        "count": len(flattened),
        "sum": sum(flattened),
        "minimum": min(flattened),
        "maximum": max(flattened)
    }


nested_data = [10, [20, 30], [40, [50, 60]], 70]

result = analyze_nested_list(nested_data)

print("Nested List:", nested_data)
print("Total Elements:", result["count"])
print("Sum:", result["sum"])
print("Minimum:", result["minimum"])
print("Maximum:", result["maximum"])
```

### Expected Output

```text
Nested List: [10, [20, 30], [40, [50, 60]], 70]
Total Elements: 7
Sum: 280
Minimum: 10
Maximum: 70
```

### Project Concepts Used

- Recursive function calls.
- Base cases and recursive cases.
- Nested list processing.
- List traversal.
- Data validation.
- Function return values.

### Project Extension Ideas

1. Support nested strings and integers separately.
2. Count the number of nested lists.
3. Calculate the maximum nesting depth.
4. Find a particular value inside the nested structure.
5. Build a recursive nested category explorer.

---

# 13. Fifty Recursion Viva Questions and Answers

### Basic Questions

**Q1. What is recursion?**

Recursion is a programming technique in which a function calls itself to solve a smaller version of a problem.

**Q2. What is a recursive function?**

A recursive function is a function that calls itself directly or indirectly.

**Q3. What is a base case?**

A base case is the condition that stops further recursive calls.

**Q4. What is a recursive case?**

A recursive case is the part of the function that calls itself with a smaller or simpler problem.

**Q5. Why is a base case important?**

It prevents infinite recursion and provides a stopping condition.

**Q6. What happens when recursion never reaches a base case?**

The recursive calls keep increasing until Python generally raises a `RecursionError`.

**Q7. What is the call stack?**

The call stack is a memory structure that tracks active function calls and their execution information.

**Q8. What happens when a recursive function reaches its base case?**

The function begins returning results through the pending function calls.

**Q9. Can a function call itself more than once?**

Yes. Fibonacci and tree-traversal functions are examples where a function can make multiple recursive calls.

**Q10. What is direct recursion?**

Direct recursion occurs when a function calls itself.

### Intermediate Questions

**Q11. What is indirect recursion?**

Indirect recursion occurs when one function calls another function that eventually calls the first function again.

**Q12. What is the difference between recursion and iteration?**

Recursion uses function calls, whereas iteration uses loops to repeat operations.

**Q13. What is factorial?**

Factorial of a non-negative integer n is the product of all positive integers from 1 to n. Zero factorial is one.

**Q14. What is the factorial of 5?**

120.

**Q15. What is the Fibonacci sequence?**

It is a sequence in which each number is the sum of the two previous numbers, starting with 0 and 1.

**Q16. What are the first five Fibonacci numbers?**

0, 1, 1, 2, 3.

**Q17. What is a recursive binary search?**

It is a searching algorithm that repeatedly divides a sorted list into smaller halves using recursive calls.

**Q18. Does binary search require sorted data?**

Yes. The input must be sorted for standard binary search to work correctly.

**Q19. What is linear search?**

Linear search checks elements one by one until the target is found or the list ends.

**Q20. What is the time complexity of linear search?**

O(n).

### Technical Questions

**Q21. What is the time complexity of binary search?**

O(log n).

**Q22. What is memoization?**

Memoization stores results of previously solved subproblems so they can be reused.

**Q23. Which Python module provides `lru_cache`?**

The `functools` module.

**Q24. What is the purpose of `@lru_cache`?**

It caches function results to avoid repeating calculations for the same arguments.

**Q25. What is naive Fibonacci recursion?**

It is a basic recursive Fibonacci implementation that recalculates overlapping subproblems.

**Q26. What is the approximate time complexity of naive Fibonacci?**

O(2^n) as a common upper-bound description.

**Q27. What is the time complexity of memoized Fibonacci?**

O(n) for calculating Fibonacci values from zero through n.

**Q28. What is recursion depth?**

It is the number of active recursive function calls in a call chain.

**Q29. What is `RecursionError`?**

It is an exception raised when the interpreter detects that the recursion depth limit has been exceeded.

**Q30. Does memoization remove the recursion-depth limit?**

No. It reduces repeated computations but does not remove the depth of the recursive call chain.

### Advanced Questions

**Q31. What is tail recursion?**

Tail recursion is a form of recursion in which the recursive call is the final operation of a function.

**Q32. Does Python guarantee tail-call optimization?**

No. Python does not guarantee tail-call optimization.

**Q33. What is mutual recursion?**

Mutual recursion occurs when two or more functions call each other.

**Q34. What is the time complexity of recursive factorial?**

O(n).

**Q35. What is the auxiliary space complexity of recursive factorial?**

O(n) because of the recursive call stack.

**Q36. What is the Euclidean algorithm?**

It is an efficient method for finding the GCD of two integers using repeated remainder operations.

**Q37. What is the base case for recursive GCD?**

When the second number becomes zero, the first number is the GCD in absolute value.

**Q38. What is divide and conquer?**

It is an algorithm design technique that divides a problem into smaller subproblems, solves them, and combines their results when necessary.

**Q39. Name two sorting algorithms that use recursion.**

Merge Sort and Quick Sort.

**Q40. How is recursion used in tree traversal?**

A recursive function can process a node and call itself on its child nodes.

### DSA and Practical Questions

**Q41. What is backtracking?**

Backtracking explores possible choices and reverses a choice when it cannot lead to a valid solution.

**Q42. Name two problems that use backtracking.**

Sudoku solving and maze solving.

**Q43. What is the maximum recursion depth in Python?**

It is interpreter-configurable and depends on the Python environment. It can be checked using `sys.getrecursionlimit()`.

**Q44. How can you check the recursion limit?**

```python
import sys

print(sys.getrecursionlimit())
```

**Q45. Can recursion be used with lists?**

Yes. A recursive function can process list elements, search lists, calculate sums, and flatten nested lists.

**Q46. Can recursion be used with strings?**

Yes. It can reverse strings, check palindromes, and process individual characters.

**Q47. What is the difference between a recursive function and a normal function?**

A recursive function calls itself, while a normal function does not necessarily call itself.

**Q48. Is recursion always better than iteration?**

No. Recursion can make some problems easier to express, but iteration may use less memory and avoid recursion-depth limitations.

**Q49. What is the space complexity of recursive binary search?**

O(log n) auxiliary space because of the recursive call stack.

**Q50. Why is recursion important in DSA?**

It provides a natural way to solve hierarchical, divide-and-conquer, searching, backtracking, and tree-based problems.

---

# 14. Important Recursion Terminology

| Term | Meaning |
|---|---|
| Recursion | Function calling itself |
| Recursive Function | A function that calls itself |
| Base Case | Condition that stops recursion |
| Recursive Case | Part where the function calls itself |
| Call Stack | Structure that manages active function calls |
| Stack Frame | Information associated with a function call |
| Recursion Depth | Number of active recursive calls |
| Memoization | Storing previously calculated results |
| Tail Recursion | Recursive call is the final operation |
| Direct Recursion | Function calls itself |
| Indirect Recursion | Functions call one another recursively |
| Backtracking | Exploring choices and reversing unsuccessful ones |
| Divide and Conquer | Breaking a problem into smaller subproblems |

---

# 15. Quick Revision Notes

- Recursion means a function calling itself.
- A base case stops further recursive calls.
- A recursive case reduces the problem.
- Python manages recursive calls using the call stack.
- Recursive calls return in reverse order after reaching the base case.
- Factorial and natural-number sums are basic recursion problems.
- Fibonacci demonstrates overlapping subproblems.
- Memoization avoids repeated calculations.
- Binary search requires sorted input.
- GCD can be calculated using the Euclidean algorithm.
- Recursive power can use exponentiation by squaring.
- Nested lists can be processed using recursion.
- Deep recursion can raise `RecursionError`.
- Memoization does not remove recursion-depth limitations.
- Iteration is often preferable for very deep or simple repeated operations.

---

# 16. Learning Checklist

Complete this checklist while studying the topic.

- [ ] Understand the definition of recursion.
- [ ] Understand the base case.
- [ ] Understand the recursive case.
- [ ] Understand the function call stack.
- [ ] Trace factorial calls manually.
- [ ] Write a countdown function.
- [ ] Calculate factorial recursively.
- [ ] Calculate the sum of natural numbers.
- [ ] Generate Fibonacci numbers.
- [ ] Understand naive and memoized Fibonacci.
- [ ] Calculate powers recursively.
- [ ] Reverse strings using recursion.
- [ ] Check palindromes recursively.
- [ ] Find GCD recursively.
- [ ] Implement recursive linear search.
- [ ] Implement recursive binary search.
- [ ] Calculate the sum of list elements.
- [ ] Count element occurrences.
- [ ] Flatten nested lists.
- [ ] Understand recursion depth.
- [ ] Analyze time complexity.
- [ ] Analyze auxiliary space complexity.
- [ ] Complete all 10 unsolved questions.
- [ ] Complete the mini project.
- [ ] Review all 50 viva questions.

---

# 17. File Information

**Topic:** Recursion

**Section:** Python Fundamentals → Functions

**Python File:**

```text
09_recursion.py
```

**README File:**

```text
README.md
```

**Folder Structure:**

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 09-Recursion/
            ├── README.md
            └── 09_recursion.py
```

## How to Run the Python Program

Open the terminal from your repository root and run:

```bash
python PYTHON/Python-Fundamentals/02-Functions/09-Recursion/09_recursion.py
```

## Conclusion

Recursion is one of the most important foundations of Data Structures and Algorithms. Understanding base cases, recursive cases, call-stack behavior, and complexity will prepare you for advanced topics such as binary trees, graph traversal, backtracking, divide and conquer, and dynamic programming.

**Keep practicing recursive problems and learn to trace every function call manually.**