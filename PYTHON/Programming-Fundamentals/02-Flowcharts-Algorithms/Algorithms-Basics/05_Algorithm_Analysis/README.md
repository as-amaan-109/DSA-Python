# Algorithm Analysis

Welcome to **Algorithm Analysis**, the fifth topic in the Algorithms Basics section of Python Programming Fundamentals.

Algorithm analysis helps us understand how much computational work and memory an algorithm requires as the input size grows. It also helps us compare different solutions to the same problem.

In this topic, you will learn time complexity, space complexity, asymptotic notation, operation counting, and the analysis of common algorithms such as linear search, binary search, and selection sort.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 02 – Flowcharts and Algorithms
- **Subsection:** Algorithms Basics
- **Topic:** Algorithm Analysis
- **Level:** Beginner to Intermediate
- **Language:** Python
- **Practical File:** `05_algorithm_analysis.py`

### Learning Objectives

After completing this topic, you should be able to:

- Explain why algorithms are analysed.
- Distinguish time complexity from space complexity.
- Understand the purpose of Big O notation.
- Understand Big Omega and Big Theta notation.
- Recognise constant, logarithmic, linear, and quadratic growth.
- Compare best, average, and worst cases.
- Count basic operations in loops.
- Analyse linear search, binary search, and selection sort.
- Understand auxiliary space.
- Compare different approaches to the same problem.
- Perform a dry run and verify operation counts.
- Interpret complexity estimates without confusing them with exact execution time.

---

## 2. What Is Algorithm Analysis?

Algorithm analysis is the study of an algorithm's resource requirements, especially computational work and memory.

Suppose two algorithms solve the same task. One might perform a single calculation, while another processes every element in a large collection. Both may be correct, but their performance can differ greatly as the input grows.

Algorithm analysis helps answer questions such as:

- How does the amount of work change when the input doubles?
- Does the algorithm need to examine every element?
- How many comparisons does it perform?
- Does it create a new collection proportional to the input size?
- Is there a more efficient algorithm for the same problem?

The goal is to understand growth and trade-offs, not just the time taken by a single run.

---

## 3. What Is Input Size?

Complexity is generally expressed as a function of an input-size parameter.

The parameter depends on the problem:

| Problem | Possible input-size parameter |
|---|---|
| Search a list | Number of list elements, `N` |
| Sort a list | Number of elements, `N` |
| Process an integer's digits | Number of digits, `D` |
| Print numbers up to a limit | Numeric limit, `N` |
| Multiply two large integers | Number of digits in the operands |

It is important to distinguish the size of an input from its numerical value. For example, a large integer has many digits, but the number of digits grows approximately with the logarithm of its value.

The appropriate size parameter should reflect what controls the algorithm's work.

---

## 4. Time Complexity

Time complexity describes how an algorithm's computational work grows as the input size grows.

In introductory analysis, we usually count important operations rather than measuring actual seconds. This avoids depending too heavily on a particular computer, operating system, or programming-language runtime.

### Example: Constant number of operations

```python
a = 10
b = 20

total = a + b
print(total)
```

For this fixed sequence of operations, the amount of algorithmic work does not grow with an input collection.

Its time complexity is O(1) under the usual fixed-size operation-count model.

### Example: Loop over N elements

```python
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print(total)
```

The loop body executes N times for a non-negative N. The number of iterations grows proportionally with N.

Its time complexity is O(N).

**Important:** Complexity describes the growth of computational work. It does not mean O(1) always takes one second, or that O(N) always takes N seconds.

---

## 5. Space Complexity

Space complexity describes how memory requirements grow as the input size grows.

When comparing algorithms, it is useful to distinguish auxiliary space from the memory needed to hold the input itself.

### Auxiliary space

Auxiliary space refers to additional working memory used by the algorithm, beyond its input storage and any exclusions specified by the analysis convention.

### Example: Constant auxiliary space

```python
values = [10, 20, 30, 40]

total = 0

for value in values:
    total += value

print(total)
```

The algorithm uses a running total and a loop variable rather than creating another collection that grows with the input.

Its auxiliary space is O(1), excluding the input list and fixed runtime overhead.

### Example: Additional list

```python
values = [10, 20, 30, 40]

doubled = [value * 2 for value in values]

print(doubled)
```

The new list contains one result for each input element. Its additional space grows with N, giving O(N) auxiliary space.

### Time vs space complexity

| Feature | Time complexity | Space complexity |
|---|---|---|
| Measures | Growth in computational work | Growth in memory requirements |
| Typical unit | Operation count | Memory units or stored items |
| Main question | How does work grow? | How does memory grow? |
| Example | Linear search takes O(N) worst-case time | Copying a list requires O(N) additional space |

An algorithm can be efficient in time but require more memory, or use little extra memory while performing more work.

---

## 6. Asymptotic Notation

Asymptotic notation describes growth rates as input size becomes large.

It deliberately ignores many details, including constant factors and lower-order terms.

### 6.1 Big O — O(f(N))

Big O gives an asymptotic upper bound on growth.

For example, if an algorithm's work grows proportionally with N, it is O(N).

In beginner courses, Big O is often used to describe worst-case complexity, but the notation itself is not limited to worst-case analysis. It describes an upper bound on whichever function or case is being analysed.

### 6.2 Big Omega — Ω(f(N))

Big Omega gives an asymptotic lower bound on growth.

For example, an algorithm that always performs at least a number of operations proportional to N has an Ω(N) lower bound.

### 6.3 Big Theta — Θ(f(N))

Big Theta describes a tight asymptotic bound: the growth is bounded both above and below by constant multiples of the same function for sufficiently large inputs.

For example, a loop that performs exactly N iterations with constant work per iteration is Θ(N).

### Example

The following loop performs N increments:

```python
n = int(input("Enter N: "))
count = 0

for _ in range(n):
    count += 1

print(count)
```

Under a standard operation-count model, the loop work is Θ(N) for non-negative N, and therefore it is also O(N) and Ω(N).

### Summary

| Notation | Main interpretation |
|---|---|
| O(f(N)) | Asymptotic upper bound |
| Ω(f(N)) | Asymptotic lower bound |
| Θ(f(N)) | Asymptotically tight bound |

These notations describe mathematical growth. They are not exact execution-time measurements.

---

## 7. Common Time Complexity Classes

The following classes are commonly encountered in introductory algorithm analysis.

| Complexity | Name | Common example |
|---|---|---|
| O(1) | Constant | Accessing an element by index in a list |
| O(log N) | Logarithmic | Binary search on sorted data |
| O(N) | Linear | Linear search |
| O(N log N) | Linearithmic | Merge sort |
| O(N²) | Quadratic | Selection sort, nested pair comparisons |
| O(N³) | Cubic | Three nested loops each growing with N |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci time growth |
| O(N!) | Factorial | Generating every permutation in a brute-force approach |

These are typical classifications, not guarantees for every algorithm in a category. The actual analysis depends on the code and its input conditions.

---

## 8. Understanding Constant Time — O(1)

An algorithm has constant-time complexity when its computational work is bounded independently of the input size under the chosen operation-count model.

Example:

```python
a = 5
b = 8

print(a + b)
```

The number of stated arithmetic operations does not grow with an input collection.

However, operations on arbitrary-precision integers may themselves require more work as the operands gain digits. O(1) claims in beginner analysis generally assume fixed-size values or treat individual arithmetic operations as constant cost.

---

## 9. Understanding Linear Time — O(N)

Linear-time algorithms perform work proportional to the number of elements or iterations.

Example:

```python
values = [10, 20, 30, 40, 50]

for value in values:
    print(value)
```

The loop processes each element once.

For N elements, it performs N iterations, giving Θ(N) time for the iteration work.

If the input size doubles, the iteration count also doubles.

Common linear-time algorithms include:

- Traversing a list.
- Counting matching items.
- Finding a minimum or maximum in one pass.
- Linear search in the worst case.

---

## 10. Understanding Quadratic Time — O(N²)

Quadratic-time algorithms often contain two nested loops that each grow with the input size.

Example:

```python
n = 4

for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop runs N times, and for each outer iteration the inner loop runs N times.

Total inner operations:

\[
N \times N = N^2
\]

For N = 4, the inner operation executes 16 times.

A loop containing another loop is not automatically quadratic. The loop bounds and their relationship to the input size determine the complexity.

---

## 11. Understanding Logarithmic Time — O(log N)

Logarithmic growth occurs when the problem size is repeatedly reduced by a constant factor, such as dividing it by two.

Example:

```python
n = int(input("Enter a positive integer: "))
iterations = 0

while n > 1:
    n //= 2
    iterations += 1

print("Iterations:", iterations)
```

At each step, the value becomes approximately half of its previous value.

After k halvings, the value is approximately N / 2ᵏ. The loop stops when this quantity reaches at most 1, requiring a number of iterations proportional to log₂ N.

This gives O(log N) time.

Binary search uses the same broad principle: each unsuccessful comparison discards roughly half of the remaining search range.

---

## 12. Best, Average, and Worst Cases

The number of operations can differ depending on the input, even for the same algorithm.

### Best case

The minimum work required among inputs of a given size.

### Average case

The expected work under a specified distribution of inputs. An average-case statement is meaningful only when the input distribution or probability assumptions are defined.

### Worst case

The maximum work required among inputs of a given size.

### Example: Linear Search

Linear search checks items one by one until it finds the target or reaches the end.

| Case | Example | Comparisons |
|---|---|---:|
| Best | Target at the first index | 1 |
| Average | Target at a typical interior position under an assumed distribution | Proportional to N |
| Worst | Target is last or absent | Up to N |

For N elements, linear search has O(N) worst-case time complexity.

Its best-case running time is Θ(1), because it can stop after a single comparison. If we account for the entire implementation's fixed setup and list storage conventions, we should state clearly which operations are included in the analysis.

---

## 13. Example: Linear Search

### Problem

Find the index of a target value in a list.

### Algorithm

1. Start from the first element.
2. Compare the current element with the target.
3. If they match, return the index.
4. Otherwise, move to the next element.
5. If the list ends without a match, report not found.

### Python Implementation

```python
values = [10, 20, 30, 40, 50]
target = 40

position = -1
comparisons = 0

for index, value in enumerate(values):
    comparisons += 1

    if value == target:
        position = index
        break

print("Index:", position)
print("Comparisons:", comparisons)
```

Output:

```text
Index: 3
Comparisons: 4
```

### Complexity

- Best-case time: Θ(1).
- Worst-case time: Θ(N).
- Auxiliary space: O(1).

The index is zero-based, so the first element has index 0.

---

## 14. Example: Binary Search

Binary search requires a sorted collection.

### Algorithm

1. Set the left and right boundaries.
2. Find the middle index.
3. Compare the middle element with the target.
4. If they match, return the index.
5. If the target is smaller, continue in the left half.
6. Otherwise, continue in the right half.
7. Repeat until found or the range becomes empty.

### Python Implementation

```python
values = [10, 20, 30, 40, 50, 60, 70]
target = 50

left = 0
right = len(values) - 1

while left <= right:
    mid = (left + right) // 2

    if values[mid] == target:
        print("Index:", mid)
        break
    elif target < values[mid]:
        right = mid - 1
    else:
        left = mid + 1
else:
    print("Target not found.")
```

### Complexity

- Worst-case time: O(log N).
- Auxiliary space: O(1) for the iterative version.
- Precondition: the collection is sorted according to the search order.

Checking whether the list is sorted before searching takes O(N) time. Therefore, a program that performs this validation every time has O(N) total time for validation plus binary search. The O(log N) search bound refers to the binary-search operation itself when its sorted-input precondition already holds.

---

## 15. Example: Selection Sort

Selection sort repeatedly selects the smallest element from the unsorted suffix and places it at the next position.

### Algorithm

1. Set the current position to the beginning of the list.
2. Find the smallest element from the current position to the end.
3. Swap it with the element at the current position.
4. Advance to the next position.
5. Repeat until the list has been processed.

### Python Implementation

```python
values = [64, 25, 12, 22, 11]
n = len(values)
comparisons = 0

for i in range(n):
    smallest_index = i

    for j in range(i + 1, n):
        comparisons += 1

        if values[j] < values[smallest_index]:
            smallest_index = j

    values[i], values[smallest_index] = (
        values[smallest_index],
        values[i],
    )

print("Sorted list:", values)
print("Comparisons:", comparisons)
```

Output:

```text
Sorted list: [11, 12, 22, 25, 64]
Comparisons: 10
```

### Complexity

- Best-case time: Θ(N²).
- Average-case time: Θ(N²).
- Worst-case time: Θ(N²).
- Auxiliary space: O(1) for the in-place version.

Selection sort performs N(N − 1) / 2 element comparisons regardless of the input ordering, though the specific swap behaviour can differ.

---

## 16. Counting Operations

Counting operations is a useful way to derive complexity.

### One loop

```python
count = 0

for _ in range(n):
    count += 1
```

The body executes N times, so its repeated work is Θ(N).

### Two nested loops

```python
count = 0

for _ in range(n):
    for _ in range(n):
        count += 1
```

The increment occurs N² times, so the repeated work is Θ(N²).

### Triangular nested loop

```python
count = 0

for i in range(n):
    for _ in range(i):
        count += 1
```

The inner loop executes:

\[
0 + 1 + 2 + \cdots + (N-1)
\]

Its total is:

\[
\frac{N(N-1)}{2}
\]

The growth is Θ(N²).

### Important note

When describing an algorithm's complexity, count how the work grows rather than just counting the lines of source code. A single line inside a loop can execute thousands of times.

---

## 17. Comparing Algorithms

Two algorithms can solve the same problem but have different growth rates.

Consider the sum of integers from 1 to N.

### Loop-based approach

```python
total = 0

for value in range(1, n + 1):
    total += value
```

The loop performs N iterations. The time complexity is Θ(N), and the auxiliary space is O(1).

### Formula-based approach

```python
total = n * (n + 1) // 2
```

It performs a fixed number of arithmetic operations. Under the standard fixed-size operation-count model, this approach takes O(1) time and O(1) auxiliary space.

The formula is valid for non-negative integers when the sum is defined from 1 through N. For large arbitrary-precision integers, actual arithmetic costs grow with the number of digits, so the simplified constant-time label is a model rather than a statement about exact machine work.

### Comparison table

| Factor | Loop | Formula |
|---|---|---|
| Logic | Repeated addition | Direct calculation |
| Iterations | N | No input-dependent loop |
| Simplified time complexity | Θ(N) | O(1) |
| Auxiliary space | O(1) | O(1) |
| Best use | Understanding accumulation | Computing the sum efficiently |

---

## 18. Understanding Space Complexity with Lists

Suppose an algorithm processes a list with N elements.

### In-place processing

A loop that updates a fixed number of variables uses O(1) auxiliary space, excluding the original input.

### Creating a second list

A list comprehension such as:

```python
doubled = [value * 2 for value in values]
```

creates a new collection with one element per input element. The additional storage grows proportionally with N, so its auxiliary space is O(N).

### Recursive calls

Recursive algorithms may use call-stack memory proportional to their recursion depth. For example, a recursive algorithm with depth N generally requires O(N) stack space, even if it does not build a separate list.

Space analysis should state what is counted, especially whether input storage and returned output are included.

---

## 19. Overview of the 12 Examples

The Python file `05_algorithm_analysis.py` includes:

| No. | Example | Main concept |
|---:|---|---|
| 1 | Constant-Time Operations | O(1) |
| 2 | Linear-Time Loop | O(N) |
| 3 | Quadratic Nested Loops | O(N²) |
| 4 | Logarithmic Halving Loop | O(log N) |
| 5 | Linear Search | Best and worst cases |
| 6 | Binary Search | Logarithmic search |
| 7 | Selection Sort | Quadratic sorting |
| 8 | Minimum and Maximum | One-pass analysis |
| 9 | Triangular Nested Loop | Counting operations |
| 10 | Auxiliary Space with a New List | O(N) additional memory |
| 11 | Loop versus Formula | Comparing approaches |
| 12 | Fibonacci with Constant Auxiliary Space | Time and auxiliary space |

For every example, predict the number of operations, run the code, and compare the observed count with the expected formula.

---

## 20. Twelve Solved Practice Questions

The Python file also contains these solved exercises:

1. Constant-Time Calculation
2. Count Linear Iterations
3. Count N-Squared Operations
4. Count Triangular Operations
5. Count Logarithmic Halvings
6. Linear Search Comparisons
7. Binary Search Comparisons
8. Selection Sort Comparisons
9. Minimum Search Comparisons
10. Count Positive Values
11. Compare Two Sum Methods
12. Copy a List

These exercises help connect operation counts and memory allocation with asymptotic complexity.

---

## 21. Five Independent Practice Questions

The following questions do not include solution code.

### Question 1: Analyse Bubble Sort

Implement bubble sort, count comparisons and swaps, and describe best-case and worst-case time complexity for your chosen implementation.

### Question 2: Compare Linear and Binary Search

Test both algorithms on suitable data. Count comparisons and explain why binary search requires sorted input.

### Question 3: Compare Two Two-Sum Approaches

Compare a nested-loop approach to finding two values that sum to a target with an approach that uses a set. Explain expected time and additional-space trade-offs.

### Question 4: Analyse List-Copy Space

Create lists of different lengths and reason about how additional space changes as the input grows. Distinguish element count from the exact number of bytes used by the runtime.

### Question 5: Compare Fibonacci Algorithms

Compare naive recursive Fibonacci with an iterative version. Explain their time and space complexity and test small N.

For each task, state your assumptions, estimate the complexity, implement the algorithm, and use test cases to verify its behaviour.

---

## 22. Common Complexity Mistakes

### Mistake 1: Confusing Big O with exact runtime

O(N) does not mean exactly N seconds or N instructions.

**Improvement:** Explain the growth in the relevant operation count.

### Mistake 2: Counting only the number of code lines

A short statement inside nested loops may execute far more times than several statements outside the loops.

**Improvement:** Count iterations and operations based on the loop bounds.

### Mistake 3: Assuming every nested loop is O(N²)

The inner loop may run a fixed number of times, or its bound may depend on the outer loop.

**Improvement:** Analyse the actual number of executions.

### Mistake 4: Ignoring input validation overhead

A validation pass may increase the total runtime even when the core algorithm is faster.

**Improvement:** State whether you are analysing just the algorithmic operation or the entire program, including validation.

### Mistake 5: Ignoring auxiliary space

Creating new lists or using recursive calls can increase memory requirements.

**Improvement:** Identify all storage that grows with input size.

### Mistake 6: Treating Big O as always worst-case complexity

Big O is an upper-bound notation. It can describe worst-case, average-case, or another specified growth function.

**Improvement:** State the case being analysed as well as the notation.

---

## 23. Interview Questions and Answers

**Q1. What is algorithm analysis?**

It is the study of an algorithm's resource requirements, especially computational work and memory, as input size grows.

**Q2. What is time complexity?**

It describes how an algorithm's computational work grows with input size.

**Q3. What is space complexity?**

It describes how an algorithm's memory requirements grow with input size.

**Q4. What does O(1) mean?**

It means the quantity being analysed is bounded independently of the input size under the chosen operation-count model.

**Q5. What does O(N) mean?**

It means the amount of work has an asymptotic upper bound proportional to N.

**Q6. What is O(N²)?**

It is a quadratic growth class. It commonly appears when two loops each scale with the input size.

**Q7. What is O(log N)?**

It is logarithmic growth, often arising when the problem size is repeatedly reduced by a constant factor.

**Q8. What is the difference between Big O, Big Omega, and Big Theta?**

Big O gives an asymptotic upper bound, Big Omega a lower bound, and Big Theta a tight bound.

**Q9. What is worst-case complexity?**

It describes the maximum work over inputs of a given size.

**Q10. What is average-case complexity?**

It describes expected work under a specified input distribution or probability model.

**Q11. What is the worst-case time complexity of linear search?**

O(N), because all elements may need to be checked.

**Q12. What is the worst-case time complexity of binary search?**

O(log N) for the search operation on already-sorted data.

**Q13. What is the time complexity of selection sort?**

Θ(N²) for its comparisons in best, average, and worst cases.

**Q14. What is auxiliary space?**

It is the additional working memory used by an algorithm beyond the inputs, subject to the chosen analysis convention.

**Q15. Why is complexity analysis useful?**

It helps compare algorithmic growth rates and reason about how solutions behave as their inputs grow.

---

## 24. How to Run the Python File

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\05_Algorithm_Analysis\05_algorithm_analysis.py"
```

The menu provides three options:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

For searching and sorting exercises, use different input sizes and input arrangements. Note the number of comparisons or iterations reported by the program.

---

## ✅ Completion Checklist

- [ ] Understand time complexity.
- [ ] Understand space and auxiliary space.
- [ ] Understand Big O, Big Omega, and Big Theta.
- [ ] Identify O(1), O(log N), O(N), and O(N²) patterns.
- [ ] Distinguish best, average, and worst cases.
- [ ] Count loop iterations and comparisons.
- [ ] Analyse linear and binary search.
- [ ] Analyse selection sort.
- [ ] Compare a loop with a formula.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved practice questions.
- [ ] Attempt all 5 independent practice questions.
- [ ] Explain the complexity of each solution in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to estimate how an algorithm's computational work and memory use grow with input size. You should also be able to explain common complexity classes and compare alternative solutions to the same problem.

These skills will be important when studying data structures, sorting algorithms, searching strategies, and interview-style DSA problems.

---

## 📌 Final Note

**Do not judge an algorithm only by how quickly it runs on one small input. Analyse how its work and memory requirements grow as the input becomes larger.**

Understand the assumptions, count the operations, and compare algorithms on the same problem.
