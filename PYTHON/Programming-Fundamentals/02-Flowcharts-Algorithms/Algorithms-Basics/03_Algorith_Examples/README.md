# Algorithm Examples

Welcome to **Algorithm Examples**, the third topic in the Algorithms Basics section of Python Programming Fundamentals.

Learning the definition of an algorithm is only the beginning. The next step is to apply algorithm design to actual problems, understand how the steps work, and translate the logic into working Python programs.

This topic covers arithmetic algorithms, comparisons, number processing, searching, and basic mathematical problems. It also introduces dry runs, test cases, and introductory complexity analysis.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 02 – Flowcharts and Algorithms
- **Subsection:** Algorithms Basics
- **Topic:** Algorithm Examples
- **Level:** Beginner to Intermediate
- **Language:** Python
- **Practical File:** `03_algorithm_examples.py`

### Learning Objectives

After completing this topic, you should be able to:

- Apply algorithms to practical programming problems.
- Identify inputs, outputs, and required operations.
- Design algorithms using ordered steps.
- Translate algorithm steps into Python.
- Use conditions and loops in algorithm implementations.
- Process individual digits of an integer.
- Search for a value in a list.
- Calculate GCD, LCM, factorial, and Fibonacci numbers.
- Perform a dry run to trace variable values.
- Test ordinary, boundary, and special cases.
- Understand the introductory time and space complexity of common algorithms.

---

## 2. What Is an Algorithm Example?

An algorithm example demonstrates how a particular sequence of steps solves a specific problem.

For example, to find the sum of two numbers:

1. Accept two input values.
2. Add them.
3. Store the result.
4. Display the result.

Python implementation:

```python
a = 10
b = 20

total = a + b

print("Sum:", total)
```

Output:

```text
Sum: 30
```

The example illustrates the relationship between a problem statement, an algorithm, and its implementation.

---

## 3. A Standard Method for Solving Algorithm Problems

Follow this process for every problem in this topic.

### Step 1: Understand the Problem

Identify the exact task. Determine whether you need to calculate a value, compare values, search a collection, or process digits.

### Step 2: Identify Inputs

Write down all required input values and their expected types.

For a largest-of-three problem, the inputs are three numbers.

### Step 3: Identify Outputs

Decide what the solution must produce.

The output may be a calculated value, a message, a sequence, or the result of a search.

### Step 4: Design the Algorithm

Write the solution as clear, ordered steps. Include decisions or repetitions when necessary.

### Step 5: Write Pseudocode

Express the solution in readable instructions without relying on exact Python syntax.

### Step 6: Implement in Python

Translate the algorithm into executable Python code.

### Step 7: Dry Run

Manually trace the program using sample values. Record variable changes and important conditions.

### Step 8: Test

Test normal inputs, boundary values, and relevant special cases.

### Step 9: Analyse

Check whether the approach is correct and whether it uses reasonable time and memory for the problem.

---

## 4. Example 1 — Addition of Two Numbers

### Problem

Accept two numbers and calculate their sum.

### Algorithm

1. Start.
2. Read `A` and `B`.
3. Calculate `SUM = A + B`.
4. Display the sum.
5. Stop.

### Pseudocode

```text
START
    INPUT A
    INPUT B
    SET SUM = A + B
    DISPLAY SUM
END
```

### Python Implementation

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

### Dry Run

For `A = 10` and `B = 20`:

| Step | Operation | Result |
|---|---|---|
| 1 | Read A | 10 |
| 2 | Read B | 20 |
| 3 | Add A and B | 30 |
| 4 | Display result | 30.0 |

### Complexity

The algorithm performs a fixed number of arithmetic operations. Under the usual fixed-size numeric model, its time and auxiliary space complexities are O(1).

---

## 5. Example 2 — Find the Largest of Two Numbers

### Problem

Compare two numbers and identify the larger value. Handle equality as well.

### Algorithm

1. Read `A` and `B`.
2. If `A > B`, choose `A`.
3. Otherwise, if `B > A`, choose `B`.
4. If neither is greater, the values are equal.
5. Display the result.

### Python Implementation

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both numbers are equal.")
```

### Test Cases

| A | B | Expected result |
|---:|---:|---|
| 10 | 20 | 20 is larger |
| 50 | 5 | 50 is larger |
| 12 | 12 | Both are equal |

The equality case is important. Without it, a solution might fail to communicate what happens when the two values are identical.

---

## 6. Example 3 — Find the Largest of Three Numbers

### Problem

Find the largest of three numbers.

### Algorithm

1. Read `A`, `B`, and `C`.
2. Check whether `A` is greater than or equal to both other values.
3. If not, check whether `B` is greater than or equal to both other values.
4. Otherwise, choose `C`.
5. Display the largest value.

### Pseudocode

```text
START
    INPUT A, B, C

    IF A >= B AND A >= C
        SET LARGEST = A
    ELSE IF B >= A AND B >= C
        SET LARGEST = B
    ELSE
        SET LARGEST = C
    END IF

    DISPLAY LARGEST
END
```

### Python Implementation

```python
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest:", largest)
```

### Dry Run

Consider `A = 10`, `B = 25`, and `C = 15`.

| Check | Result |
|---|---|
| A >= B and A >= C | False |
| B >= A and B >= C | True |
| Select B | 25 |

### Complexity

The solution performs a fixed number of comparisons, so it uses O(1) time and O(1) auxiliary space under the usual fixed-size value model.

---

## 7. Example 4 — Even or Odd

### Problem

Determine whether an integer is even or odd.

### Algorithm

1. Read an integer.
2. Calculate the remainder after division by 2.
3. If the remainder is zero, report even.
4. Otherwise, report odd.

### Python Implementation

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Explanation

The modulo operator `%` returns a remainder. For integer parity, the remainder check identifies whether the number is divisible by 2.

Examples:

| Input | Expected result |
|---:|---|
| 8 | Even |
| 11 | Odd |
| 0 | Even |
| -4 | Even |
| -7 | Odd |

The algorithm runs in O(1) time and uses O(1) auxiliary space under the standard fixed-size integer model.

---

## 8. Example 5 — Positive, Negative, or Zero

### Problem

Classify a number based on its relationship to zero.

### Algorithm

1. Read a number.
2. If it is greater than zero, classify it as positive.
3. If it is less than zero, classify it as negative.
4. Otherwise, classify it as zero.
5. Display the classification.

### Python Implementation

```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

This example introduces multiple alternative branches using `if`, `elif`, and `else`.

---

## 9. Example 6 — Sum from 1 to N

### Problem

Calculate the sum of all integers from 1 to a non-negative integer `N`.

### Algorithm

1. Read `N`.
2. Reject negative values.
3. Initialise `TOTAL = 0`.
4. For every integer from 1 through `N`, add that value to `TOTAL`.
5. Display the total.

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

### Python Implementation

```python
n = int(input("Enter N: "))

if n < 0:
    print("N must be non-negative.")
else:
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum:", total)
```

### Dry Run for N = 4

| Iteration | I | Total before | Total after |
|---|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 4 | 6 | 10 |

### Complexity

The loop executes `N` times for positive `N`. The time complexity is O(N), and the auxiliary space complexity is O(1).

For large values, the mathematical formula `N * (N + 1) // 2` can calculate the sum without iterating through every integer.

---

## 10. Example 7 — Factorial

### Problem

Calculate the factorial of a non-negative integer.

For positive `N`:

\[
N! = N \times (N-1) \times \cdots \times 2 \times 1
\]

By definition:

\[
0! = 1
\]

### Algorithm

1. Read `N`.
2. If `N` is negative, report that the factorial is not defined for negative integers.
3. Otherwise, initialise `FACTORIAL = 1`.
4. Multiply the current factorial by each integer from 1 to `N`.
5. Display the result.

### Python Implementation

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print("Factorial:", factorial)
```

### Dry Run for N = 4

| I | Factorial before | Factorial after |
|---|---:|---:|
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 6 |
| 4 | 6 | 24 |

### Complexity

The loop takes O(N) time and O(1) auxiliary space. The number of digits in the result grows with `N`, so actual computational costs for very large integers are greater than this simple operation-count model suggests.

---

## 11. Example 8 — Multiplication Table

### Problem

Display the multiplication table for a given number from 1 to 10.

### Algorithm

1. Read the number.
2. Set the counter to 1.
3. Multiply the number by the counter.
4. Display the equation and result.
5. Increase the counter.
6. Repeat until the counter exceeds 10.

### Python Implementation

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

### Sample Output

```text
Enter a number: 5
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

The loop always performs ten iterations, so its iteration count is constant and its time complexity is O(1) with respect to the input number.

---

## 12. Example 9 — Count the Digits in an Integer

### Problem

Count the digits in an integer without counting its negative sign.

### Algorithm

1. Read an integer.
2. Take its absolute value.
3. If the value is zero, set the count to 1.
4. Otherwise, repeatedly divide the number by 10 using integer division.
5. Increase the counter after every division.
6. Stop when the remaining value becomes zero.
7. Display the count.

### Python Implementation

```python
number = int(input("Enter an integer: "))
temp = abs(number)

if temp == 0:
    count = 1
else:
    count = 0

    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)
```

### Test Cases

| Input | Expected digit count |
|---:|---:|
| 7 | 1 |
| 42 | 2 |
| 12345 | 5 |
| 0 | 1 |
| -789 | 3 |

The zero case must be handled explicitly because the loop would otherwise execute zero times.

### Complexity

For a number with `D` decimal digits, the algorithm takes O(D) time and O(1) auxiliary space.

---

## 13. Example 10 — Sum of Digits

### Problem

Calculate the sum of all decimal digits in an integer.

### Algorithm

1. Read an integer.
2. Take its absolute value.
3. Initialise the sum to zero.
4. Extract the last digit using `% 10`.
5. Add that digit to the sum.
6. Remove the last digit using `// 10`.
7. Repeat until the remaining number is zero.
8. Display the sum.

### Python Implementation

```python
number = int(input("Enter an integer: "))
temp = abs(number)
total = 0

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of digits:", total)
```

### Dry Run for 352

| Current number | Last digit | Sum after addition |
|---:|---:|---:|
| 352 | 2 | 2 |
| 35 | 5 | 7 |
| 3 | 3 | 10 |

Output:

```text
Sum of digits: 10
```

Zero produces a digit sum of zero because the initial total is zero and the loop does not execute.

### Complexity

The algorithm takes O(D) time and O(1) auxiliary space, where `D` is the number of decimal digits.

---

## 14. Example 11 — Reverse an Integer

### Problem

Reverse an integer's digits while preserving its sign. Leading zeroes in the reversed magnitude are not retained as integer digits.

### Algorithm

1. Read the integer.
2. Store its sign.
3. Initialise the reversed number to zero.
4. Extract the final digit from the absolute value.
5. Append that digit to the reversed number.
6. Remove the final digit from the remaining number.
7. Repeat until no digits remain.
8. Restore the sign and display the result.

### Python Implementation

```python
number = int(input("Enter an integer: "))

sign = -1 if number < 0 else 1
temp = abs(number)
reversed_number = 0

while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

print("Reversed integer:", sign * reversed_number)
```

### Sample Results

| Input | Result |
|---:|---:|
| 1234 | 4321 |
| 560 | 65 |
| 7 | 7 |
| 0 | 0 |
| -123 | -321 |

### Complexity

The algorithm takes O(D) time and O(1) auxiliary space for a number with `D` decimal digits.

---

## 15. Example 12 — Check Whether a Number Is Prime

### Problem

Determine whether an integer is prime.

A prime number is an integer greater than 1 whose only positive divisors are 1 and itself.

### Algorithm

1. Read `N`.
2. If `N < 2`, report that it is not prime.
3. Otherwise, test divisors starting from 2.
4. Continue while the divisor squared is not greater than `N`.
5. If any divisor divides `N` exactly, report that it is not prime.
6. Otherwise, report that it is prime.

### Python Implementation

```python
n = int(input("Enter an integer: "))

if n < 2:
    print("Not prime.")
else:
    is_prime = True
    divisor = 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break

        divisor += 1

    if is_prime:
        print("Prime.")
    else:
        print("Not prime.")
```

### Why Stop at the Square Root?

If a composite number has factors greater than 1, at least one of those factors must be no greater than its square root. Therefore, checking divisors up to the square root is sufficient.

### Complexity

The algorithm takes O(√N) time and O(1) auxiliary space under the usual operation-count model.

---

## 16. Overview of the 12 Examples

The practical file `03_algorithm_examples.py` includes:

| No. | Algorithm | Main concept |
|---:|---|---|
| 1 | Addition | Arithmetic |
| 2 | Largest of Two | Comparison |
| 3 | Largest of Three | Multiple conditions |
| 4 | Even or Odd | Modulo |
| 5 | Number Classification | Conditional branching |
| 6 | Sum from 1 to N | Accumulation and loops |
| 7 | Factorial | Repeated multiplication |
| 8 | Multiplication Table | Looping over a range |
| 9 | Count Digits | Integer division |
| 10 | Sum of Digits | Digit extraction |
| 11 | Reverse an Integer | Repeated digit processing |
| 12 | Prime Check | Divisibility testing |

Each example includes a practical Python implementation and can be selected individually from the program menu.

---

## 17. Twelve Solved Practice Questions

The Python file also includes the following solved exercises:

1. Perimeter of a Rectangle
2. Area of a Square
3. Celsius to Fahrenheit
4. Percentage of Five Subjects
5. Find Minimum in a List
6. Find Maximum in a List
7. Linear Search
8. Count Even and Odd Values
9. Greatest Common Divisor
10. Least Common Multiple
11. Fibonacci Sequence
12. Palindrome Check

These exercises extend algorithm design from simple arithmetic into list processing, searching, repeated computation, and basic number theory.

### Example: Linear Search

**Problem:** Find the first index at which a target appears in a list.

**Algorithm:**

1. Read the list and target.
2. Start at the first list element.
3. Compare the current element with the target.
4. If they match, record the index and stop.
5. Otherwise, move to the next element.
6. If the list ends without a match, report that the target was not found.

Linear search takes O(N) time in the worst case for a list of `N` elements, and O(1) auxiliary space for the iterative implementation.

The practical file includes a working version of this algorithm.

---

## 18. Five Questions for Independent Practice

These questions do not include answer code.

### Question 1: Binary Search

Given a sorted list of integers and a target, design an algorithm to find the target or report that it is absent.

State why the list must be sorted for ordinary binary search.

### Question 2: Second-Largest Distinct Value

Find the second-largest distinct integer in a list. Decide how the solution behaves if there are fewer than two distinct values.

### Question 3: Selection Sort

Design an algorithm that sorts integers in ascending order by repeatedly selecting the smallest remaining value.

### Question 4: Armstrong Number

Determine whether a non-negative integer equals the sum of its digits, each raised to the power of the number of digits.

### Question 5: Missing Number

A list contains distinct integers from 1 through `N`, with exactly one number missing. Design an algorithm to find the missing value.

For every question, write the problem statement in your own words, specify inputs and outputs, design the steps, implement the code, and test boundary cases.

---

## 19. Time and Space Complexity Reference

Complexity describes how an algorithm's computational resource usage grows with input size.

| Algorithm | Time complexity | Auxiliary space |
|---|---|---|
| Add two numbers | O(1) | O(1) |
| Largest of three numbers | O(1) | O(1) |
| Sum from 1 to N using a loop | O(N) | O(1) |
| Factorial using a loop | O(N) | O(1) |
| Multiplication table of fixed size 10 | O(1) | O(1) |
| Count digits | O(D) | O(1) |
| Sum of digits | O(D) | O(1) |
| Reverse digits | O(D) | O(1) |
| Prime check up to square root | O(√N) | O(1) |
| Linear search | O(N) worst case | O(1) |
| Fibonacci generation for N terms | O(N) | O(N) for the returned list |

Here, `N` generally denotes the input size or numeric bound as appropriate, and `D` is the number of decimal digits. These are asymptotic operation-count estimates under a standard simplified model; actual runtime also depends on the implementation and size of the numbers involved.

---

## 20. Common Mistakes

### Incorrect loop boundaries

A loop may stop before processing the final required value or may perform an extra iteration.

**Improvement:** Check the first and last iteration manually.

### Missing special cases

A digit-counting algorithm may incorrectly return zero digits for the number zero.

**Improvement:** Test zero explicitly.

### Ignoring equality

A comparison algorithm may not handle equal values correctly.

**Improvement:** Include an equality branch or design comparisons that safely handle ties.

### Incorrect divisibility logic

A prime-checking algorithm may incorrectly classify 1 as prime.

**Improvement:** Check that the number is at least 2 before testing divisors.

### Not specifying assumptions

A solution might assume that a list is non-empty or that a number is within a particular range.

**Improvement:** Document input requirements and check them before processing.

### Testing only one input

A correct result for one input is not sufficient evidence for all cases.

**Improvement:** Test normal values, boundaries, and special cases.

---

## 21. Interview Questions and Answers

**Q1. What is an algorithm?**

An algorithm is a finite, well-defined sequence of steps used to solve a problem.

**Q2. Why should algorithms be tested?**

Testing helps reveal incorrect logic, missing steps, and failures on important input cases.

**Q3. What is linear search?**

Linear search checks list elements one by one until a target is found or the list ends.

**Q4. Why is binary search usually faster than linear search on sorted data?**

Binary search repeatedly halves the remaining search interval, giving O(log N) worst-case time compared with O(N) for linear search.

**Q5. What is a prime number?**

A prime number is an integer greater than 1 whose only positive divisors are 1 and itself.

**Q6. What is factorial?**

The factorial of a non-negative integer is the product of all positive integers up to that integer, with `0! = 1`.

**Q7. What is the Euclidean algorithm used for?**

It calculates the greatest common divisor of two integers using repeated remainder operations.

**Q8. What is a dry run?**

A dry run manually follows an algorithm using sample values and records how variables change.

**Q9. What is the difference between time complexity and space complexity?**

Time complexity describes computational work growth; space complexity describes memory usage growth.

**Q10. Why does prime checking stop at the square root?**

Every composite integer greater than 1 has at least one factor no larger than its square root.

**Q11. What is the worst-case time complexity of linear search?**

O(N), because the algorithm may inspect all N elements.

**Q12. What is an edge case?**

An input or situation near a boundary or special condition that can expose an error in an algorithm.

---

## 22. How to Run the Python File

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\03_Algorithm_Examples\03_algorithm_examples.py"
```

The menu offers three options:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

Select one problem at a time. Test the outputs and make sure you understand how the algorithm reaches its result.

---

## ✅ Completion Checklist

- [ ] Understand how examples demonstrate algorithm design.
- [ ] Study all 12 examples.
- [ ] Write algorithm steps before reading the implementation.
- [ ] Perform dry runs for loop-based algorithms.
- [ ] Test normal and boundary cases.
- [ ] Run all 12 solved questions.
- [ ] Attempt the 5 independent practice questions.
- [ ] Understand linear search and prime checking.
- [ ] Review the complexity table.
- [ ] Answer the interview questions in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to design, implement, and test a range of beginner algorithms. You will also begin to recognise how different approaches vary in terms of logic, correctness, and computational work.

These skills prepare you for **Algorithm Characteristics**, where you will study the properties of a good algorithm in more detail.

---

## 📌 Final Note

**Do not memorise an algorithm only by its code. Understand the problem, explain the steps, trace the variables, and verify the result.**

That is how algorithmic thinking develops.
