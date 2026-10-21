# Algorithm Analysis

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Algorithm Analysis  
> **Level:** Beginner  
> **Goal:** Understand time complexity, space complexity, Big O notation, and algorithm performance.

---

## Table of Contents

1. Introduction
2. What Is Algorithm Analysis?
3. Why Is Algorithm Analysis Important?
4. Input Size: n
5. Time Complexity
6. Space Complexity
7. Big O Notation
8. Constant Time - O(1)
9. Logarithmic Time - O(log n)
10. Linear Time - O(n)
11. Linearithmic Time - O(n log n)
12. Quadratic Time - O(n²)
13. Exponential Time - O(2ⁿ)
14. Factorial Time - O(n!)
15. Complexity Comparison Table
16. Linear Search Analysis
17. Binary Search Analysis
18. Best, Average, and Worst Cases
19. Time Complexity vs Space Complexity
20. Auxiliary Space
21. How to Analyze a Loop
22. Common Beginner Mistakes
23. Important Terminology
24. Interview Questions
25. Practice Questions
26. Learning Checklist
27. What's Next?

---

## 1. Introduction

When solving a programming problem, there may be multiple ways to produce the correct answer.

For example, we might search for a number in a list using linear search or binary search.

Both algorithms can find a target, but their performance can differ significantly when the list becomes large.

Algorithm analysis helps us understand these differences.

We mainly study two resources:

1. **Time complexity:** How the amount of computational work grows with input size.
2. **Space complexity:** How memory requirements grow with input size.

Understanding these concepts is an important foundation for Data Structures and Algorithms (DSA).

---

## 2. What Is Algorithm Analysis?

Algorithm analysis is the study of the computational resources required by an algorithm.

The two most commonly discussed resources are execution time and memory.

### Example

Suppose an algorithm processes every element in a list containing `n` elements.

If it visits each element once, the amount of work generally grows proportionally to `n`.

Its time complexity is:

`O(n)`

Another algorithm that repeatedly halves the remaining problem size may have:

`O(log n)`

These notations help describe how an algorithm scales as the input grows.

### Important Point

Algorithm analysis generally focuses on how computational work changes with input size rather than measuring the execution time of one particular run.

Actual runtime also depends on the hardware, programming language, implementation, and other factors.

---

## 3. Why Is Algorithm Analysis Important?

Algorithm analysis helps us choose suitable solutions for programming problems.

### 3.1 Compare Different Algorithms

Two algorithms may produce the same result but require different amounts of work.

### 3.2 Handle Large Inputs

A method that works well for 100 elements might become impractical for millions of elements.

### 3.3 Prepare for DSA Interviews

Time and space complexity are common subjects in technical interviews.

### 3.4 Improve Code

Analysis helps identify unnecessary repeated work or excessive memory usage.

### 3.5 Understand Trade-offs

An algorithm may use additional memory to reduce its running time, or use less memory at the cost of extra computation.

---

## 4. Input Size: n

In algorithm analysis, `n` usually represents the size of the input.

The meaning of `n` depends on the problem.

Examples:

- For a list, `n` may be the number of elements.
- For a string, `n` may be the number of characters.
- For a matrix, the input size may be represented using the number of rows and columns.
- For a numeric problem, `n` may represent the magnitude or number of digits of a value, depending on the algorithm.

### Example

Consider this list:

```python
numbers = [10, 20, 30, 40, 50]
```

The list contains five elements, so:

```text
n = 5
```

If the list contains 100 elements:

```text
n = 100
```

When analyzing an algorithm, we ask how its work changes as `n` increases.

---

## 5. Time Complexity

### Definition

**Time complexity** describes how the amount of computational work performed by an algorithm grows with input size.

It is commonly expressed using asymptotic notation such as Big O.

### Example: One Operation

```python
a = 10
b = 20

total = a + b

print(total)
```

The algorithm performs a fixed number of operations, independent of the size of an external collection.

For this kind of fixed-size computation, the time complexity is:

`O(1)`

### Example: One Loop

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

The loop processes each of the `n` elements.

Its time complexity is:

`O(n)`

### Example: Nested Loops

```python
numbers = [1, 2, 3, 4]

for first in numbers:
    for second in numbers:
        print(first, second)
```

For `n` elements, the inner loop executes `n` times for each of the `n` outer-loop iterations.

The total number of pairs is:

`n × n = n²`

Its time complexity is:

`O(n²)`

**Key point:** Time complexity describes how work grows, not an exact number of seconds.

---

## 6. Space Complexity

### Definition

**Space complexity** describes how the memory requirements of an algorithm grow with input size.

When discussing space complexity, it is important to distinguish between total memory and additional memory used by the algorithm.

In many introductory DSA discussions, we focus on auxiliary space: the extra memory required beyond the input itself.

### Example: Constant Auxiliary Space

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total = total + number

print(total)
```

The algorithm uses a fixed number of additional variables, such as `total` and `number`.

The auxiliary space complexity is:

`O(1)`

The loop processes more items as the list grows, but it does not create a new list proportional to the input size.

### Example: Linear Auxiliary Space

```python
numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)
```

The new `squares` list contains one result for every input element.

For `n` input elements, the new list stores `n` results.

The auxiliary space complexity is:

`O(n)`

### Important Point

Always check whether the analysis counts the input data itself or only additional memory. State the convention when it matters.

---

## 7. Big O Notation

### Definition

**Big O notation** describes an asymptotic upper bound on how an algorithm's resource usage grows with input size.

In introductory DSA, Big O is commonly used to communicate worst-case time complexity, although Big O notation is not limited to worst-case analysis.

### Why Do We Use Big O?

Suppose one algorithm performs approximately `3n + 5` basic operations.

Another performs approximately `n² + 2n + 10`.

As `n` becomes large, the quadratic term becomes much more significant.

For these growth rates:

- `3n + 5` is `O(n)`.
- `n² + 2n + 10` is `O(n²)`.

Big O focuses on the growth rate rather than exact constants and lower-order terms.

### Example

```python
for number in numbers:
    print(number)
```

If the loop processes `n` elements once, its time complexity is `O(n)`.

### Simplifying Complexity

When deriving a Big O upper bound for common polynomial expressions, we typically focus on the dominant growth term.

Examples:

| Expression | Common Big O upper bound |
|---|---|
| `5` | `O(1)` |
| `3n + 5` | `O(n)` |
| `n² + 2n + 10` | `O(n²)` |
| `4n² + 3n + 1` | `O(n²)` |

Big O is an upper-bound notation; in algorithm analysis, we often use a tight bound such as `Θ(n)` when we want to describe growth more precisely.

---

## 8. Constant Time - O(1)

### Definition

An operation has `O(1)` time complexity when its work remains bounded independently of the input size.

### Example: List Indexing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
```

Output:

```text
10
```

Accessing a Python list element by index is an O(1) operation in the usual complexity model.

### Another Example

```python
a = 10
b = 20

total = a + b

print(total)
```

The number of arithmetic statements does not grow with the number of items in an unrelated collection.

### Common Examples of O(1)

- Reading a value from a fixed variable.
- Accessing a list element by index in the standard Python list model.
- Performing a fixed number of arithmetic operations on fixed-size numeric values.

### Important Note

O(1) does not mean that an operation literally takes zero seconds. It means its modeled work does not grow with `n`.

---

## 9. Logarithmic Time - O(log n)

### Definition

An algorithm has logarithmic time complexity when each step reduces the remaining problem size by a constant factor, such as dividing it by 2.

### Example: Repeatedly Divide by Two

```python
size = 32
steps = 0

while size > 1:
    size = size // 2
    steps = steps + 1
    print("Current size:", size)

print("Number of divisions:", steps)
```

Output:

```text
Current size: 16
Current size: 8
Current size: 4
Current size: 2
Current size: 1
Number of divisions: 5
```

The sequence is:

```text
32 → 16 → 8 → 4 → 2 → 1
```

Only five divisions are needed to reduce 32 to 1.

For a starting size `n`, the number of repeated halvings grows proportionally to `log₂(n)`.

Therefore, the time complexity is:

`O(log n)`

### Common Example

Binary search repeatedly eliminates approximately half of the remaining sorted search range.

Its worst-case time complexity is `O(log n)`.

---

## 10. Linear Time - O(n)

### Definition

An algorithm has linear time complexity when its work grows proportionally to the input size.

### Example: Sum All Elements

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total = total + number

print("Sum:", total)
```

Output:

```text
Sum: 150
```

The loop visits each element once.

If the list contains:

- 5 elements, it performs 5 loop iterations.
- 100 elements, it performs 100 loop iterations.
- `n` elements, it performs `n` loop iterations.

Time complexity:

`O(n)`

Auxiliary space complexity:

`O(1)`

The algorithm uses a running total rather than a new data structure that grows with the list.

### Common Examples of O(n)

- Finding the sum of a list.
- Scanning a list for a target using linear search.
- Finding the largest value in an unsorted list.
- Counting occurrences of a value in a list.

---

## 11. Linearithmic Time - O(n log n)

### Definition

`O(n log n)` growth combines a linear factor with a logarithmic factor.

It commonly appears in efficient comparison-based sorting algorithms.

Examples of algorithms with `O(n log n)` worst-case time bounds include merge sort and heapsort.

### Intuition

Imagine an algorithm that processes `n` items at each of approximately `log n` stages.

The total work is proportional to:

`n × log n`

Therefore, the time complexity is:

`O(n log n)`

### When Is It Useful?

This complexity is common in sorting and some divide-and-conquer algorithms.

Python's built-in sorting algorithm, Timsort, has an O(n log n) worst-case time bound, while it can perform better on certain already-structured inputs.

For this beginner topic, remember the growth pattern. Detailed sorting algorithms will be studied later.

---

## 12. Quadratic Time - O(n²)

### Definition

An algorithm has quadratic time complexity when its work grows proportionally to the square of the input size.

This commonly occurs with two nested loops, each performing `n` iterations.

### Example

```python
numbers = [1, 2, 3, 4]
pair_count = 0

for first in numbers:
    for second in numbers:
        pair_count = pair_count + 1

print("Number of pairs:", pair_count)
```

Output:

```text
Number of pairs: 16
```

### Explanation

For four elements:

- The outer loop runs 4 times.
- The inner loop runs 4 times for every outer-loop iteration.
- Total iterations = `4 × 4 = 16`.

For `n` elements, the total iterations are:

`n × n = n²`

Time complexity:

`O(n²)`

### Common Examples

- Comparing every pair of elements.
- Generating every ordered pair in a collection.
- Some simple sorting algorithms, such as bubble sort, in the worst case.

### Important Note

Not every nested loop automatically means `O(n²)`. The actual complexity depends on how many times each loop executes.

---

## 13. Exponential Time - O(2ⁿ)

### Definition

Exponential complexity occurs when the computational work grows approximately as an exponential function of the input size.

A common example is an algorithm that explores all possible combinations of `n` binary choices.

Each choice has two possibilities.

The number of combinations is:

`2ⁿ`

### Example

For three binary choices, the possibilities are:

```text
000
001
010
011
100
101
110
111
```

There are:

`2³ = 8`

possible combinations.

For 10 binary choices, there are:

`2¹⁰ = 1024`

possible combinations.

For much larger input sizes, this growth becomes very expensive.

### Where Can It Appear?

Exponential time can arise in brute-force solutions to certain combinatorial problems and in some recursive algorithms that repeatedly explore multiple branches.

**Important:** Not every recursive algorithm is exponential. The complexity depends on the recurrence and amount of repeated work.

---

## 14. Factorial Time - O(n!)

### Definition

Factorial-time growth is associated with algorithms that examine all permutations of `n` distinct items.

The number of permutations is:

`n! = n × (n - 1) × (n - 2) × ... × 1`

### Example

For three distinct items A, B, and C, the permutations are:

```text
ABC
ACB
BAC
BCA
CAB
CBA
```

There are:

`3! = 6`

permutations.

For five distinct items:

`5! = 120`

permutations.

The number of permutations grows very rapidly as `n` increases.

### Where Can It Appear?

A brute-force algorithm that examines every possible ordering may have factorial-time behavior.

Such approaches are often practical only for small input sizes unless additional optimization or pruning is used.

---

## 15. Complexity Comparison Table

The following table shows common growth rates, from generally slower growth to faster growth as the input becomes large.

| Complexity | Name | Example |
|---|---|---|
| `O(1)` | Constant | List indexing |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | Sum every element |
| `O(n log n)` | Linearithmic | Merge sort |
| `O(n²)` | Quadratic | Visit every ordered pair |
| `O(2ⁿ)` | Exponential | Enumerate all binary combinations |
| `O(n!)` | Factorial | Enumerate all permutations |

For sufficiently large inputs, these growth rates usually become increasingly expensive as we move down the table.

Actual performance also depends on constants, implementation details, and the size of the input.

---

## 16. Linear Search Analysis

Linear search checks items one at a time until it finds the target or reaches the end.

### Python Implementation

```python
def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index

    return -1


numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 10))
print(linear_search(numbers, 40))
print(linear_search(numbers, 99))
```

Output:

```text
0
3
-1
```

The function returns `-1` when the target is not found.

### Best Case

The target is the first element.

Only one comparison is required.

Time complexity:

`O(1)`

### Average Case

Under common assumptions about the target's position, a successful search may examine a number of elements proportional to `n`.

Time complexity:

`O(n)`

### Worst Case

The target is the last element, or the target does not exist.

The algorithm may examine every element.

Time complexity:

`O(n)`

### Summary

| Case | Time Complexity |
|---|---|
| Best | `O(1)` |
| Average | `O(n)` |
| Worst | `O(n)` |

Linear search works with both sorted and unsorted lists.

---

## 17. Binary Search Analysis

Binary search is an efficient search algorithm for a sorted collection.

It repeatedly compares the target with the middle element and discards the half that cannot contain the target.

### Requirement

**The list must be sorted** for the ordinary binary search algorithm to work correctly.

### Python Implementation

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


numbers = [3, 7, 11, 15, 19, 23, 27, 31, 35]

print(binary_search(numbers, 23))
print(binary_search(numbers, 7))
print(binary_search(numbers, 99))
```

Output:

```text
5
1
-1
```

### Dry Run

Find `23` in:

```text
[3, 7, 11, 15, 19, 23, 27, 31, 35]
```

**Step 1:** The middle element is `19`.

Since `23 > 19`, continue searching the right half.

```text
[23, 27, 31, 35]
```

**Step 2:** The middle of the remaining search range is `27`.

Since `23 < 27`, continue searching the left part.

```text
[23]
```

**Step 3:** The middle element is `23`.

The target is found.

### Time Complexity

- Best case: `O(1)`, when the middle element is the target.
- Worst case: `O(log n)`.
- Iterative auxiliary space: `O(1)`.

### Linear Search vs Binary Search

| Feature | Linear Search | Binary Search |
|---|---|---|
| Requires sorted input | No | Yes |
| Worst-case time | `O(n)` | `O(log n)` |
| Basic approach | Check each item | Repeatedly halve the search range |
| Extra space for iterative version | `O(1)` | `O(1)` |

Binary search is not automatically the better choice for every collection. The data must satisfy its requirements, and the cost of obtaining or maintaining sorted data may also matter.

---

## 18. Best, Average, and Worst Cases

Algorithm analysis can consider different cases depending on the input.

### Best Case

The most favorable input for the algorithm.

For linear search, the target is the first element.

### Average Case

The expected behavior under a stated or assumed distribution of inputs.

For linear search with a uniformly positioned successful target, the average number of comparisons grows proportionally to `n`.

### Worst Case

The most demanding input under the problem's assumptions.

For linear search, the target is last or missing.

### Comparison

| Case | Meaning | Linear Search Example |
|---|---|---|
| Best | Most favorable input | Target is first |
| Average | Typical expected behavior under assumptions | Target is at an average position |
| Worst | Most demanding input | Target is last or missing |

**Interview tip:** When someone asks for the complexity of an algorithm, clarify whether they want best-case, average-case, or worst-case complexity when it is relevant.

---

## 19. Time Complexity vs Space Complexity

These two concepts measure different resources.

| Time Complexity | Space Complexity |
|---|---|
| Measures growth in computational work | Measures growth in memory requirements |
| Often analyzed by counting operations | Often analyzed by counting stored elements or extra variables |
| Example: scanning a list once is `O(n)` time | Example: creating a second list of `n` values uses `O(n)` auxiliary space |
| Helps evaluate speed as input grows | Helps evaluate memory usage as input grows |

An algorithm can have linear time and constant auxiliary space.

For example, summing the elements of a list takes `O(n)` time but only `O(1)` auxiliary space when using a running total.

An algorithm can also use additional memory to achieve a desired runtime. The correct analysis depends on the implementation.

---

## 20. Auxiliary Space

Auxiliary space is the additional memory used by the algorithm, beyond the input data itself, under a stated accounting model.

### Example 1: Constant Auxiliary Space

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

The algorithm uses a fixed number of extra variables.

Auxiliary space:

`O(1)`

### Example 2: Linear Auxiliary Space

```python
def calculate_squares(numbers):
    result = []

    for number in numbers:
        result.append(number * number)

    return result
```

The result list grows with the number of input elements.

Auxiliary space:

`O(n)`

### Important Point

When comparing space complexity, specify whether you are counting only auxiliary memory or total memory, including the input.

---

## 21. How to Analyze a Loop

Counting loop iterations is one of the easiest ways to begin estimating time complexity.

### Example 1: One Loop

```python
for i in range(n):
    print(i)
```

The loop performs `n` iterations.

Time complexity:

`O(n)`

### Example 2: Two Independent Loops

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Each loop performs `n` iterations.

Total iterations:

`n + n = 2n`

The Big O time complexity is:

`O(n)`

Constant factors are ignored when expressing this upper-bound growth rate.

### Example 3: Two Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Total iterations:

`n × n = n²`

Time complexity:

`O(n²)`

### Example 4: Repeated Halving

```python
size = n

while size > 1:
    size = size // 2
```

The size decreases by a constant factor each time.

Time complexity:

`O(log n)`

### Important Warning

Do not identify complexity from indentation alone. Inspect how often each loop runs and whether the inner loop's work depends on the outer loop or on another value.

---

## 22. Common Beginner Mistakes

### Mistake 1: Thinking Big O Gives Exact Seconds

`O(n)` does not tell you the exact execution time.

It describes how the algorithm's work grows with input size.

### Mistake 2: Assuming Every Nested Loop Is O(n²)

Two nested loops often lead to quadratic time, but not always. Their actual iteration counts determine the complexity.

### Mistake 3: Confusing Time and Space Complexity

An algorithm that takes `O(n)` time may use `O(1)` auxiliary space.

These resources must be analyzed separately.

### Mistake 4: Using Binary Search on Unsorted Data

Ordinary binary search relies on sorted input.

Sorting a list may itself require time and memory, depending on the algorithm and requirements.

### Mistake 5: Assuming O(1) Means Zero Time

Constant time means the work does not grow with the input size under the analysis model. It still takes time to execute.

### Mistake 6: Confusing Big O with Worst Case

Big O is an upper-bound notation. In introductory DSA, worst-case time is often expressed using Big O, but those are not identical concepts.

### Mistake 7: Counting Only the Main Loop

Nested operations, function calls, and temporary data structures can also affect time or memory requirements.

---

## 23. Important Terminology

| Term | Meaning |
|---|---|
| Algorithm analysis | Study of computational resource usage |
| Input size | Size of the data processed by an algorithm |
| Time complexity | Growth of computational work with input size |
| Space complexity | Growth of memory requirements |
| Auxiliary space | Additional memory used by the algorithm |
| Big O | Asymptotic upper-bound notation |
| O(1) | Constant time growth |
| O(log n) | Logarithmic time growth |
| O(n) | Linear time growth |
| O(n log n) | Linearithmic time growth |
| O(n²) | Quadratic time growth |
| O(2ⁿ) | Exponential time growth |
| O(n!) | Factorial time growth |
| Linear search | Checks elements one by one |
| Binary search | Searches a sorted range by repeatedly halving it |
| Dry run | Manual tracing of an algorithm using sample data |

---

## 24. Interview Questions

### Q1. What is algorithm analysis?

It is the study of how an algorithm's computational resource usage grows with the size of its input.

### Q2. What is time complexity?

Time complexity describes how computational work grows as the input size increases.

### Q3. What is space complexity?

Space complexity describes how memory requirements grow with input size.

### Q4. What is Big O notation?

Big O describes an asymptotic upper bound on an algorithm's growth rate.

### Q5. What is O(1)?

O(1) is constant-time growth: the modeled work does not grow with input size.

### Q6. What is O(n)?

O(n) is linear growth. The amount of work grows proportionally to the input size.

### Q7. What is O(log n)?

O(log n) is logarithmic growth. It commonly appears when an algorithm repeatedly halves the remaining problem size.

### Q8. What is O(n²)?

O(n²) is quadratic growth. A common example is visiting all pairs in a collection using two loops of length `n`.

### Q9. What is the worst-case time complexity of linear search?

O(n), because the algorithm may examine every element.

### Q10. What is the worst-case time complexity of binary search?

O(log n), provided the input is sorted and the standard binary search algorithm is used.

### Q11. Why does binary search require sorted input?

It uses the ordering to determine which half cannot contain the target. Without sorted input, that decision may discard the target.

### Q12. Can an algorithm have O(n) time and O(1) auxiliary space?

Yes. Summing a list in one pass using a running total is a common example.

### Q13. What is the difference between best case and worst case?

The best case describes the most favorable input, while the worst case describes the most demanding input under the problem's assumptions.

### Q14. Is O(1) always faster than O(n) in real code?

Not necessarily for every small input and implementation. Big O describes growth as input size increases, not every constant overhead or timing detail.

### Q15. Why is algorithm analysis important in DSA?

It helps us compare solutions, select appropriate algorithms, and understand how a solution behaves as the input grows.

---

## 25. Practice Questions

Try to solve these questions before checking the examples above.

### Beginner Level

**Question 1:** What is algorithm analysis?

**Question 2:** Explain time complexity and space complexity with examples.

**Question 3:** What does `n` represent in algorithm analysis?

**Question 4:** Identify the time complexity:

```python
print("Hello")
```

**Question 5:** Identify the time complexity:

```python
for i in range(n):
    print(i)
```

### Intermediate Level

**Question 6:** Find the complexity of this code:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

**Question 7:** What is the time complexity of summing all the elements in a list?

**Question 8:** Explain why binary search is O(log n) in the worst case.

**Question 9:** Write a function that finds the largest element in a non-empty list. Explain its time complexity and auxiliary space complexity.

**Question 10:** Explain the difference between linear search and binary search.

### Challenge Questions

**Question 11:** Write code that creates a new list containing the squares of all the elements in an input list. Analyze its time and auxiliary space complexities.

**Question 12:** Compare the best and worst cases of linear search.

**Question 13:** Explain the difference between O(n) and O(n²) with example loops.

**Question 14:** Write an iterative binary search and explain why the sorted-input requirement matters.

**Question 15:** For a function that uses one loop to scan a list and a second independent loop to scan it again, determine its overall time complexity and explain your answer.

---

## 26. Learning Checklist

- [ ] Understand algorithm analysis.
- [ ] Understand input size `n`.
- [ ] Explain time complexity.
- [ ] Explain space complexity.
- [ ] Understand Big O notation.
- [ ] Recognize O(1).
- [ ] Recognize O(log n).
- [ ] Recognize O(n).
- [ ] Recognize O(n log n).
- [ ] Recognize O(n²).
- [ ] Understand exponential and factorial growth.
- [ ] Analyze single loops.
- [ ] Analyze nested loops.
- [ ] Understand linear search complexity.
- [ ] Understand binary search complexity.
- [ ] Distinguish time complexity from auxiliary space.
- [ ] Solve the practice questions.

---

## 27. What's Next?

Continue with:

**06 - Practice Algorithms**

Use the concepts from the Algorithm Basics, Algorithm Steps, Algorithm Examples, Algorithm Characteristics, and Algorithm Analysis topics to solve practice problems.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `05_algorithm_analysis.py` | Practical examples of complexity and search algorithms |
| `README.md` | Detailed notes, complexity tables, dry runs, and interview questions |

---

## Conclusion

Algorithm analysis helps us understand how a solution behaves as the size of the problem grows.

Remember the most common complexity classes:

- `O(1)` — constant
- `O(log n)` — logarithmic
- `O(n)` — linear
- `O(n log n)` — linearithmic
- `O(n²)` — quadratic
- `O(2ⁿ)` — exponential
- `O(n!)` — factorial

Also remember that time complexity and space complexity describe different resources.

**Understand the problem → Analyze the algorithm → Implement the solution → Test the result.**

These concepts form an important foundation for DSA and coding interviews.