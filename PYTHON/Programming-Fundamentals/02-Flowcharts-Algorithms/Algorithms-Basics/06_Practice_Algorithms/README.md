# Practice Algorithms

Welcome to **Practice Algorithms**, the sixth and final topic in the Algorithms Basics section of Python Programming Fundamentals.

This topic brings together the concepts learned in algorithm fundamentals, step-by-step design, examples, characteristics, and analysis. The focus is on implementing algorithms, tracing their execution, testing edge cases, and improving problem-solving skills.

Practice is essential because understanding an algorithm's explanation is different from being able to implement it independently.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 02 – Flowcharts and Algorithms
- **Subsection:** Algorithms Basics
- **Topic:** Practice Algorithms
- **Level:** Beginner to Intermediate
- **Language:** Python
- **Practical File:** `06_practice_algorithms.py`

### Learning Objectives

After completing this topic, you should be able to:

- Convert problem statements into algorithms.
- Write pseudocode before implementation.
- Solve arithmetic and number-based problems.
- Use conditions and loops effectively.
- Understand digit-processing algorithms.
- Implement searching and sorting techniques.
- Apply the Euclidean algorithm to calculate GCD.
- Understand basic list processing.
- Test solutions with normal and edge cases.
- Estimate time and auxiliary space complexity.
- Explain and debug your own code.
- Practise independent problem solving.

---

## 2. How to Approach a Practice Problem

For every problem, follow the same systematic method.

### Step 1: Understand the Problem

Read the problem statement and describe the required result in your own words.

### Step 2: Identify Inputs and Outputs

Record the information the program receives and the result it must return or display.

### Step 3: Define Constraints

Determine allowed input values, whether a list can be empty, whether values may repeat, and how special cases should be handled.

### Step 4: Design the Algorithm

Write the solution as ordered steps. Identify which operations require decisions or repetition.

### Step 5: Write Pseudocode

Represent the logic without depending on exact Python syntax.

### Step 6: Implement in Python

Translate the planned steps into code using appropriate variables, conditions, and loops.

### Step 7: Perform a Dry Run

Trace your variables with a small example before relying on the program output.

### Step 8: Test the Solution

Try ordinary inputs, boundary cases, and relevant unusual inputs.

### Step 9: Analyse the Algorithm

Estimate how computational work and additional memory grow with the input size.

### Step 10: Review and Improve

Check the correctness, readability, and assumptions of the solution.

---

## 3. Common Algorithms in This Topic

The practical file includes examples of several important beginner algorithms.

| Algorithm | Purpose | Typical complexity |
|---|---|---|
| Sum from 1 to N | Accumulate a sequence of numbers | O(N) with a loop |
| Factorial | Multiply positive integers up to N | O(N) time |
| Prime check | Test whether a number has a divisor other than 1 and itself | O(√N) time with trial division |
| Fibonacci sequence | Generate terms of a numeric sequence | O(N) time for N terms |
| Sum of digits | Add the decimal digits of an integer | O(D) time |
| Reverse an integer | Reverse the order of digits | O(D) time |
| Linear search | Find an element in a list | O(N) worst-case time |
| Binary search | Search a sorted list by repeatedly halving the range | O(log N) search time |
| Bubble sort | Sort values by exchanging adjacent out-of-order elements | O(N²) worst-case time |
| GCD | Find the greatest common divisor of two integers | O(log min(A, B)) for positive inputs |

Here, `D` is the number of decimal digits. Complexity estimates use the usual introductory operation-count model and exclude unrelated input/output costs. The precise interpretation depends on the algorithm and what memory is counted.

---

## 4. Example 1 — Sum from 1 to N

### Problem

Calculate the sum of all integers from 1 through a non-negative integer N.

### Algorithm

1. Read N.
2. Reject N if it is negative.
3. Initialise the total to zero.
4. Add each value from 1 through N.
5. Display the sum.

### Pseudocode

```text
START
    INPUT N

    IF N < 0
        DISPLAY "Invalid input"
    ELSE
        SET TOTAL = 0

        FOR I = 1 TO N
            SET TOTAL = TOTAL + I
        END FOR

        DISPLAY TOTAL
    END IF
END
```

### Python Code

```python
n = int(input("Enter N: "))

if n < 0:
    print("N must be non-negative.")
else:
    total = 0

    for value in range(1, n + 1):
        total += value

    print("Sum:", total)
```

### Dry Run for N = 4

| Iteration | Value | Total before | Total after |
|---|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

Output:

```text
Sum: 10
```

### Complexity

- Time: O(N)
- Auxiliary space: O(1)

The loop visits each integer in the requested range once.

---

## 5. Example 2 — Factorial

### Problem

Calculate the factorial of a non-negative integer.

For N greater than zero:

\[
N! = 1 \times 2 \times 3 \times \cdots \times N
\]

By definition:

\[
0! = 1
\]

### Python Code

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    result = 1

    for value in range(1, n + 1):
        result *= value

    print("Factorial:", result)
```

### Sample Output

```text
Enter a non-negative integer: 5
Factorial: 120
```

For N = 0, the loop does not execute and the initial value remains 1.

### Complexity

- Time: O(N) loop iterations
- Auxiliary space: O(1)

For extremely large integers, the actual cost of arithmetic grows with the size of the values.

---

## 6. Example 3 — Prime Number Check

### Problem

Determine whether an integer is prime.

A prime number is an integer greater than 1 whose only positive divisors are 1 and itself.

### Algorithm

1. Read N.
2. If N is less than 2, report that it is not prime.
3. Test candidate divisors starting at 2.
4. Continue while the divisor squared is at most N.
5. If a divisor divides N exactly, report that N is not prime.
6. Otherwise, report that N is prime.

### Python Code

```python
n = int(input("Enter an integer: "))

if n < 2:
    print("Not prime.")
else:
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            print("Not prime.")
            break

        divisor += 1
    else:
        print("Prime.")
```

### Why Stop at the Square Root?

For a composite number, at least one non-trivial factor must be no greater than its square root. If no divisor is found by that point, the number is prime.

### Complexity

- Time: O(√N) for N ≥ 2
- Auxiliary space: O(1)

---

## 7. Example 4 — Fibonacci Sequence

The Fibonacci sequence starts with 0 and 1. Each subsequent term is the sum of the previous two terms.

Example sequence:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

### Python Code

```python
n = int(input("How many terms? "))

if n < 0:
    print("Number of terms must be non-negative.")
else:
    first, second = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second

    print("Fibonacci sequence:", sequence)
```

### Complexity

- Time: O(N) iterations
- Auxiliary space: O(N) for the returned list

If terms are printed directly without storing them in a list, auxiliary space can be O(1), excluding the output stream.

---

## 8. Example 5 — Sum of Digits

### Problem

Calculate the sum of an integer's decimal digits. For this example, use the absolute value, so a negative sign is not counted as a digit.

### Python Code

```python
number = abs(int(input("Enter an integer: ")))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)
```

For input `352`, the algorithm processes the digits 2, 5, and 3, giving a sum of 10.

For zero, the total remains zero.

### Complexity

- Time: O(D)
- Auxiliary space: O(1)

Here D is the number of decimal digits.

---

## 9. Example 6 — Reverse an Integer

### Problem

Reverse the decimal digits of an integer while preserving the original sign.

### Algorithm

1. Save the sign.
2. Work with the absolute value.
3. Extract the last digit using modulo 10.
4. Append the digit to the reversed number.
5. Remove the processed digit using integer division by 10.
6. Repeat until the remaining value becomes zero.
7. Restore the sign and display the result.

### Python Code

```python
number = int(input("Enter an integer: "))

sign = -1 if number < 0 else 1
remaining = abs(number)
reversed_number = 0

while remaining > 0:
    digit = remaining % 10
    reversed_number = reversed_number * 10 + digit
    remaining //= 10

print("Reversed integer:", sign * reversed_number)
```

Examples:

| Input | Output |
|---:|---:|
| 1234 | 4321 |
| 560 | 65 |
| -123 | -321 |
| 0 | 0 |

Leading zeroes disappear because the result is an integer.

### Complexity

- Time: O(D)
- Auxiliary space: O(1)

---

## 10. Example 7 — Palindrome Check

### Problem

Determine whether a non-negative integer reads the same forward and backward.

Examples include 121, 1331, and 7.

### Python Code

```python
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Enter a non-negative integer.")
else:
    original = number
    remaining = number
    reversed_number = 0

    while remaining > 0:
        digit = remaining % 10
        reversed_number = reversed_number * 10 + digit
        remaining //= 10

    if original == reversed_number:
        print("Palindrome.")
    else:
        print("Not a palindrome.")
```

Zero is a palindrome under this definition because its reversed value is also zero.

### Complexity

- Time: O(D)
- Auxiliary space: O(1)

---

## 11. Example 8 — Linear Search

### Problem

Find the first occurrence of a target value in a list.

### Python Code

```python
values = [10, 20, 30, 40, 50]
target = 40

position = -1

for index, value in enumerate(values):
    if value == target:
        position = index
        break

if position == -1:
    print("Target not found.")
else:
    print("Target found at index:", position)
```

Output:

```text
Target found at index: 3
```

The returned position is zero-based. The first item has index 0.

### Complexity

- Best-case time: O(1)
- Worst-case time: O(N)
- Auxiliary space: O(1)

The algorithm may inspect every item when the target is absent or appears at the end.

---

## 12. Example 9 — Bubble Sort

Bubble sort compares adjacent values and swaps them when they are out of order.

### Python Code

```python
values = [5, 1, 4, 2, 8]
n = len(values)

for i in range(n):
    swapped = False

    for j in range(0, n - i - 1):
        if values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            swapped = True

    if not swapped:
        break

print("Sorted list:", values)
```

Output:

```text
Sorted list: [1, 2, 4, 5, 8]
```

The `swapped` flag lets this version stop early if a complete pass makes no changes.

### Complexity

- Best case: O(N) for already sorted input with this early-exit implementation
- Average case: O(N²)
- Worst case: O(N²)
- Auxiliary space: O(1)

---

## 13. Example 10 — Greatest Common Divisor

The greatest common divisor (GCD) of two integers is the largest positive integer that divides both, when at least one input is non-zero.

The Euclidean algorithm uses repeated remainder operations.

### Python Code

```python
a = abs(int(input("Enter first integer: ")))
b = abs(int(input("Enter second integer: ")))

while b != 0:
    a, b = b, a % b

print("GCD:", a)
```

For `48` and `18`, the GCD is 6.

When both inputs are zero, this implementation returns zero as a computational convention, though the positive-divisor definition of GCD does not define a unique positive GCD for that pair.

### Complexity

For positive inputs, the Euclidean algorithm takes O(log min(A, B)) iterations in the standard asymptotic analysis, with O(1) auxiliary space.

---

## 14. Example 11 — Binary Search

Binary search repeatedly divides the remaining search interval approximately in half.

**Precondition:** The input list must be sorted in ascending order for the following implementation.

### Python Code

```python
values = [10, 20, 30, 40, 50, 60, 70]
target = 50

left = 0
right = len(values) - 1
position = -1

while left <= right:
    mid = (left + right) // 2

    if values[mid] == target:
        position = mid
        break
    elif target < values[mid]:
        right = mid - 1
    else:
        left = mid + 1

if position == -1:
    print("Target not found.")
else:
    print("Index:", position)
```

### Complexity

- Search time: O(log N)
- Auxiliary space: O(1) for this iterative implementation

If your program first validates that the input is sorted, the validation itself takes O(N) time. The O(log N) complexity refers to binary search when the sorted-input requirement is already satisfied.

---

## 15. Example 12 — Count Even and Odd Values

### Problem

Count how many values in a list are even and how many are odd.

### Python Code

```python
values = [10, 15, 22, 7, 8]

even_count = 0
odd_count = 0

for value in values:
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)
```

Output:

```text
Even count: 3
Odd count: 2
```

### Complexity

- Time: O(N)
- Auxiliary space: O(1)

The algorithm examines every list element once and maintains two counters.

---

## 16. Overview of the 12 Python Examples

The practical file `06_practice_algorithms.py` includes these examples:

| No. | Example | Main concept |
|---:|---|---|
| 1 | Sum from 1 to N | Accumulation |
| 2 | Multiplication Table | Loops and arithmetic |
| 3 | Factorial | Repeated multiplication |
| 4 | Prime Number Check | Divisibility |
| 5 | Fibonacci Sequence | Sequence generation |
| 6 | Sum of Digits | Modulo and integer division |
| 7 | Reverse an Integer | Digit processing |
| 8 | Palindrome Check | Comparing original and reversed values |
| 9 | Greatest Common Divisor | Euclidean algorithm |
| 10 | Linear Search | Sequential searching |
| 11 | Bubble Sort | Adjacent comparisons and swaps |
| 12 | Count Even and Odd Values | List traversal and counting |

Each example can be run individually from the menu.

---

## 17. Twelve Solved Practice Questions

The same Python file includes the following solved questions:

1. Minimum and Maximum
2. Second-Largest Distinct Value
3. Leap Year
4. Armstrong Number
5. Binary Search
6. Remove Duplicates
7. Frequency Count
8. Merge Two Sorted Lists
9. Selection Sort
10. Greatest Common Divisor
11. Least Common Multiple
12. Missing Number

These exercises broaden your practice from arithmetic and number processing to collection manipulation, search, and sorting.

### Important assumptions

- Binary search requires an ascending-sorted input list.
- Removing duplicates preserves the order of first occurrences.
- The missing-number problem assumes exactly one missing value from the range 1 through N and distinct, in-range inputs.
- The second-largest problem asks for the second-largest **distinct** value.
- GCD and LCM behaviour for zero inputs is handled explicitly in the code.

Read these assumptions before running an exercise. Understanding the problem specification is part of algorithm design.

---

## 18. Five Questions for Independent Practice

These questions are displayed by the program menu without providing their solutions.

### Question 1: Two Sum

Given a list of integers and a target, find two distinct elements whose sum equals the target.

Define what should happen if no valid pair exists.

### Question 2: Insertion Sort

Implement insertion sort to arrange a list in ascending order. Count comparisons or shifts and explain its complexity.

### Question 3: Anagram Check

Accept two strings and determine whether they contain the same characters with the same frequencies.

Decide how uppercase/lowercase differences and spaces should be handled.

### Question 4: Rotate a List

Given a list and a non-negative rotation count K, rotate the list to the right by K positions.

Handle empty lists and K values larger than the list length.

### Question 5: Maximum Subarray Sum

Given a non-empty list of integers, find the contiguous subarray with the greatest sum.

Test lists containing negative values and explain how your approach handles them.

### Suggested method

For each question:

1. Rewrite the problem in your own words.
2. Identify the inputs and expected output.
3. Define the assumptions and edge cases.
4. Design the algorithm and pseudocode.
5. Implement the solution in Python.
6. Test the result with several inputs.
7. Explain the time and auxiliary space complexity.

---

## 19. How to Choose Test Cases

Testing should include a range of cases, not just the first example that comes to mind.

| Test category | Example for a factorial algorithm |
|---|---|
| Typical value | N = 5 |
| Boundary value | N = 0 |
| Invalid value | N = -2 |
| Smallest non-zero input | N = 1 |
| Larger value | N = 15, subject to practical limits |

For searching algorithms, test a target at the beginning, middle, and end, as well as a target that is absent.

For sorting algorithms, test a list that is already sorted, reverse-sorted, contains duplicate values, and contains only one element.

A test case is useful when it checks a specific aspect of the solution's behaviour.

---

## 20. Common Mistakes

### Coding before understanding the problem

**Issue:** The program solves a slightly different task from the one requested.

**Improvement:** Define the inputs, output, constraints, and special cases before choosing the algorithm.

### Forgetting zero and negative values

**Issue:** Number-based algorithms may return incorrect results for zero or mishandle a negative sign.

**Improvement:** Define whether the problem accepts negative values and test zero explicitly.

### Using binary search on unsorted data

**Issue:** Binary search depends on sorted order when deciding which half to discard.

**Improvement:** Ensure the input is sorted or use an algorithm suited to unsorted data.

### Not handling duplicates

**Issue:** Problems involving the second-largest value or unique elements may produce unexpected answers.

**Improvement:** Decide whether the output refers to distinct values or permits repeated values.

### Incorrect loop boundaries

**Issue:** An algorithm skips a required value or performs an extra iteration.

**Improvement:** Trace the first and final iterations manually.

### Trusting only one test

**Issue:** A program can succeed for a normal input while failing on an edge case.

**Improvement:** Create a small test table before declaring the algorithm complete.

---

## 21. Interview Questions and Answers

**Q1. What is algorithm practice?**

It is the process of applying algorithm design and implementation concepts to programming problems and checking the results.

**Q2. What is the difference between linear search and binary search?**

Linear search examines elements sequentially. Binary search reduces the search range by half at each step and requires sorted data.

**Q3. What is bubble sort?**

Bubble sort repeatedly compares adjacent values and swaps out-of-order pairs to sort a list.

**Q4. What is a palindrome number?**

It is a number that reads the same forward and backward under the chosen representation.

**Q5. What is an Armstrong number?**

For an integer with D decimal digits, it is a non-negative integer that equals the sum of each digit raised to the power D.

**Q6. What is the Euclidean algorithm?**

It calculates the greatest common divisor using repeated remainder operations.

**Q7. What is the purpose of dry running an algorithm?**

It helps trace variable values and conditions manually so that the program's logic becomes easier to verify.

**Q8. Why are edge cases important?**

They can reveal errors that ordinary input values do not expose.

**Q9. What is time complexity?**

It describes how an algorithm's computational work grows with input size.

**Q10. What is auxiliary space?**

It is the additional working memory an algorithm uses, excluding input storage according to the chosen analysis convention.

**Q11. Why is duplicate handling important?**

The problem may require distinct values or may require preserving repeated values. The algorithm must match that requirement.

**Q12. When should an algorithm be improved?**

When there is a clear need to improve correctness, readability, resource usage, or suitability for the stated constraints.

---

## 22. How to Run the Python File

From the repository root, execute:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\06_Practice_Algorithms\06_practice_algorithms.py"
```

The menu offers:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 unsolved questions.

Select one task at a time. This makes it easier to focus on a single algorithm and understand how it behaves for different inputs.

---

## ✅ Completion Checklist

- [ ] Understand the purpose of algorithm practice.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved practice questions.
- [ ] Attempt all 5 independent questions.
- [ ] Use pseudocode before implementing new solutions.
- [ ] Test normal, boundary, and special cases.
- [ ] Trace loop-based algorithms with dry runs.
- [ ] Understand the assumptions of each algorithm.
- [ ] Review time and auxiliary space complexity.
- [ ] Explain your solutions in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to apply the core algorithm concepts from this section to a wide range of beginner programming tasks.

You will have practised arithmetic algorithms, conditionals, loops, digit processing, searching, sorting, and mathematical algorithms while learning to test and explain your solutions.

This completes the **Algorithms Basics** subsection of Week 1.

---

## 📌 Final Note

**The goal of practice is not merely to obtain the right output. It is to understand why the algorithm works, which inputs it supports, and how to test it reliably.**

Practise consistently, write solutions independently, and review your mistakes as part of the learning process.
