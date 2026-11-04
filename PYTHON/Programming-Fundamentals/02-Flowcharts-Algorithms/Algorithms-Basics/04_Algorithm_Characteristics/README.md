# Algorithm Characteristics

Welcome to **Algorithm Characteristics**, the fourth topic in the Algorithms Basics section of Python Programming Fundamentals.

An algorithm is more than a sequence of instructions. To be useful, its steps should be clear, it should produce the required result, it should terminate as intended, and its operations should be practical to carry out.

This topic explains the fundamental characteristics of algorithms and additional quality properties such as correctness, generality, and efficiency.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 02 – Flowcharts and Algorithms
- **Subsection:** Algorithms Basics
- **Topic:** Algorithm Characteristics
- **Level:** Beginner to Intermediate
- **Language:** Python
- **Practical File:** `04_algorithm_characteristics.py`

### Learning Objectives

After completing this topic, you should be able to:

- Define the core characteristics of an algorithm.
- Explain input and output requirements.
- Understand definiteness, finiteness, and effectiveness.
- Explain algorithm correctness and generality.
- Understand deterministic behaviour.
- Recognise the importance of input validation.
- Compare simple approaches using time and auxiliary space complexity.
- Trace and test an algorithm with appropriate test cases.
- Identify common algorithm-design mistakes.
- Evaluate algorithms using practical examples.

---

## 2. What Is an Algorithm?

An algorithm is a finite, clearly defined sequence of steps used to solve a problem or perform a task.

For example, an algorithm to add two integers could be:

1. Start.
2. Read the first integer.
3. Read the second integer.
4. Calculate their sum.
5. Display the sum.
6. Stop.

Python implementation:

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

total = a + b

print("Sum:", total)
```

The algorithm describes the solution logic. Python provides the executable implementation.

---

## 3. Core Characteristics of an Algorithm

The classic introductory characteristics commonly include input, output, definiteness, finiteness, and effectiveness.

Correctness, generality, and efficiency are also important when evaluating the quality of an algorithm.

### 3.1 Input

An algorithm should clearly define the data it requires.

For example, calculating a rectangle's area requires its length and width.

```text
INPUT LENGTH
INPUT WIDTH
```

An algorithm may also require no external input. For example, an algorithm that displays a fixed message can operate without asking the user for a value.

The number and type of inputs depend on the problem.

### 3.2 Output

An algorithm should clearly define the required result.

For the rectangle-area problem:

```text
SET AREA = LENGTH * WIDTH
DISPLAY AREA
```

The output is the calculated area.

A solution may produce one output, several outputs, or a result such as a Boolean value indicating whether a condition holds.

### 3.3 Definiteness

Definiteness means that each step should be precise and unambiguous.

Consider these instructions:

- Unclear: "Process the numbers properly."
- Clear: "Add A and B, store the result in SUM, and display SUM."

A reader should be able to determine what operation is intended at each step.

**Why it matters:** Ambiguous steps make algorithms difficult to implement, explain, and test.

### 3.4 Finiteness

Finiteness means that an algorithm should terminate after a finite number of steps for inputs within its intended scope.

An algorithm that repeats forever without achieving its goal does not satisfy this requirement for those executions.

Example of a terminating countdown:

```python
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Invalid input.")
else:
    while number > 0:
        print(number)
        number -= 1

    print("Countdown complete.")
```

The value decreases by one each iteration, so it eventually reaches zero.

For the input `3`, the output is:

```text
3
2
1
Countdown complete.
```

**Important:** A loop is not inherently incorrect. It is appropriate when repetition is part of the solution and the stopping behaviour is defined.

### 3.5 Effectiveness

Effectiveness means that the algorithm's operations should be basic, practical, and executable as specified.

For example:

```text
INPUT A
INPUT B
SET SUM = A + B
DISPLAY SUM
```

The steps use well-defined operations that can be carried out directly.

An algorithm can be written clearly but still be ineffective in practice if it relies on an unavailable operation or cannot complete the required task under its intended operating conditions.

---

## 4. Additional Quality Characteristics

### 4.1 Correctness

Correctness means that an algorithm produces the results required by the problem for all inputs within its specified scope.

Suppose the problem asks for the largest of three numbers. A correct algorithm must work regardless of which number is largest, including cases where values are equal.

Example:

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

For inputs `10`, `25`, and `15`, the result is `25`.

Testing multiple cases helps reveal errors, but a few successful tests alone do not establish correctness for every possible input. Careful reasoning about the algorithm is also needed.

### 4.2 Generality

Generality means that a solution should address the full range of inputs described by the problem rather than working only for one example.

For example, an algorithm for classifying numbers should handle positive values, negative values, and zero.

```python
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

This algorithm is not designed only for the input `5`. It defines behaviour for the three possible sign categories.

Generality depends on the stated problem requirements. A solution does not need to handle inputs that are explicitly outside the permitted scope, but its assumptions should be clear.

### 4.3 Efficiency

Efficiency describes how economically an algorithm uses computational resources, particularly time and memory.

Two algorithms may solve the same problem correctly but use different amounts of work.

For example, the sum of integers from 1 to `N` can be calculated using a loop:

```python
n = int(input("Enter N: "))

total = 0

for value in range(1, n + 1):
    total += value

print("Sum:", total)
```

It can also be calculated using a formula:

```python
n = int(input("Enter N: "))

total = n * (n + 1) // 2

print("Sum:", total)
```

Both approaches return the same sum when `N` is a non-negative integer. The loop uses O(N) iterations, whereas the formula uses O(1) arithmetic operations under the usual fixed-size operation-count model.

Efficiency should be considered alongside correctness and clarity, not instead of them.

---

## 5. Deterministic Behaviour

A deterministic algorithm follows defined rules that produce the same result for the same input and the same relevant initial conditions.

For example:

```python
a = 12
b = 8

print(a * b)
```

This displays `96` whenever the program executes those same instructions with those same values.

An algorithm that depends on random choices, changing external data, or other varying state may not produce the same result on every execution.

Deterministic behaviour is useful for reproducible tests and debugging, but it is distinct from correctness. A deterministic algorithm can consistently return the wrong answer if its logic is incorrect.

---

## 6. Input Validation and Preconditions

An algorithm is designed for a particular problem scope. Some problems permit all integer values; others require a restricted range.

A **precondition** is a requirement that should hold before an operation is carried out.

For example, division requires a non-zero divisor.

```python
numerator = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))

if denominator == 0:
    print("Division by zero is not allowed.")
else:
    print("Quotient:", numerator / denominator)
```

The program checks the divisor before performing the operation.

Validation helps the program handle invalid input, but it does not by itself prove that the algorithm is correct. The remaining calculations and conditions must also be checked.

---

## 7. Example 1 — Definiteness

### Problem

Add two integers using clearly defined steps.

### Algorithm

1. Read integer `A`.
2. Read integer `B`.
3. Calculate `SUM = A + B`.
4. Display `SUM`.

### Pseudocode

```text
START
    INPUT A
    INPUT B
    SET SUM = A + B
    DISPLAY SUM
END
```

### Python Code

```python
a = int(input("Enter A: "))
b = int(input("Enter B: "))

total = a + b

print("Sum:", total)
```

### Sample Output

```text
Enter A: 10
Enter B: 20
Sum: 30
```

The instructions explicitly identify the inputs, operation, variable assignment, and output.

---

## 8. Example 2 — Input and Output

### Problem

Calculate the perimeter of a rectangle.

### Formula

\[
\text{Perimeter}=2(\text{Length}+\text{Width})
\]

### Algorithm

1. Input length and width.
2. Reject negative dimensions.
3. Add the length and width.
4. Multiply the sum by 2.
5. Display the perimeter.

### Python Code

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Dimensions must be non-negative.")
else:
    perimeter = 2 * (length + width)
    print("Perimeter:", perimeter)
```

### Sample Output

```text
Enter length: 5
Enter width: 4
Perimeter: 18.0
```

This example has clearly defined inputs and an identifiable output.

---

## 9. Example 3 — Finiteness

### Problem

Print the integers from 1 to `N`.

### Algorithm

1. Input a non-negative integer `N`.
2. Set the counter to 1.
3. While the counter is at most `N`, display it.
4. Increase the counter by 1.
5. Stop when the condition is false.

### Python Code

```python
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("N must be non-negative.")
else:
    counter = 1

    while counter <= n:
        print(counter)
        counter += 1

    print("Finished.")
```

For `N = 3`, the output is:

```text
1
2
3
Finished.
```

The counter increases each iteration, and the loop eventually terminates. When `N = 0`, the loop performs zero iterations.

---

## 10. Example 4 — Effectiveness

### Problem

Calculate the average of three numbers using basic arithmetic operations.

### Algorithm

1. Input three values.
2. Add the values.
3. Divide the sum by 3.
4. Display the average.

### Python Code

```python
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

total = a + b + c
average = total / 3

print("Sum:", total)
print("Average:", average)
```

### Sample Output

```text
Enter A: 10
Enter B: 20
Enter C: 30
Sum: 60.0
Average: 20.0
```

The solution uses explicit calculations and a fixed number of straightforward operations.

---

## 11. Example 5 — Correctness

### Problem

Find the largest of three numbers.

### Algorithm

1. Read the three numbers.
2. Compare the first number with the other two.
3. If it is at least as large as both, select it.
4. Otherwise, compare the second number with the other two.
5. If it is at least as large as both, select it.
6. Otherwise, select the third number.
7. Display the selected value.

### Python Code

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

### Test Cases

| A | B | C | Expected result |
|---:|---:|---:|---:|
| 10 | 25 | 15 | 25 |
| 30 | 20 | 10 | 30 |
| 5 | 12 | 18 | 18 |
| 7 | 7 | 3 | 7 |
| 4 | 4 | 4 | 4 |

These cases include different largest positions and equal values.

---

## 12. Example 6 — Generality

### Problem

Classify an integer as positive, negative, or zero.

### Algorithm

1. Read an integer.
2. If it is greater than zero, display positive.
3. Otherwise, if it is less than zero, display negative.
4. Otherwise, display zero.

### Python Code

```python
number = int(input("Enter an integer: "))

if number > 0:
    result = "Positive"
elif number < 0:
    result = "Negative"
else:
    result = "Zero"

print("Classification:", result)
```

The algorithm defines all three cases rather than handling only a single example input.

---

## 13. Example 7 — Input Validation

### Problem

Safely divide a numerator by a denominator.

### Algorithm

1. Read both values.
2. Check whether the denominator is zero.
3. If it is zero, display an error.
4. Otherwise, calculate and display the quotient.

### Python Code

```python
numerator = float(input("Enter numerator: "))
denominator = float(input("Enter denominator: "))

if denominator == 0:
    print("Division by zero is not allowed.")
else:
    quotient = numerator / denominator
    print("Quotient:", quotient)
```

### Sample Output

```text
Enter numerator: 10
Enter denominator: 2
Quotient: 5.0
```

For a denominator of zero, the program reports the issue rather than performing the division.

---

## 14. Example 8 — Termination

### Problem

Display a countdown from a non-negative integer to 1.

### Python Code

```python
number = int(input("Enter starting number: "))

if number < 0:
    print("Enter a non-negative integer.")
else:
    while number > 0:
        print(number)
        number -= 1

    print("Countdown complete.")
```

For a starting value of `3`, the program displays 3, 2, 1, and then the completion message.

The decreasing variable provides a clear route to the loop's stopping condition.

---

## 15. Example 9 — Efficiency: Loop vs Formula

### Problem

Calculate the sum from 1 to `N` using two approaches.

### Approach A: Repeated addition

```python
n = int(input("Enter non-negative N: "))

if n < 0:
    print("N must be non-negative.")
else:
    total = 0

    for i in range(1, n + 1):
        total += i

    print("Sum using loop:", total)
```

### Approach B: Mathematical formula

```python
n = int(input("Enter non-negative N: "))

if n < 0:
    print("N must be non-negative.")
else:
    total = n * (n + 1) // 2
    print("Sum using formula:", total)
```

### Comparison

| Feature | Loop method | Formula method |
|---|---|---|
| Main operation | Repeated addition | Direct arithmetic calculation |
| Time complexity | O(N) | O(1) under the fixed-size operation model |
| Auxiliary space | O(1) | O(1) |
| Easy to trace each term | Yes | No repeated iterations |
| Works for non-negative integers | Yes | Yes |

The formula is an efficient alternative for this particular problem. It is still important to verify that a formula matches the problem being solved.

---

## 16. Example 10 — Deterministic Behaviour

### Problem

Multiply two integers and repeat with the same values to examine reproducibility.

### Python Code

```python
a = int(input("Enter A: "))
b = int(input("Enter B: "))

result = a * b

print("Product:", result)
print("The same inputs give the same product for this operation.")
```

For `A = 12` and `B = 8`, the output is `96`.

The multiplication operation is deterministic for the same operands under ordinary Python integer arithmetic. This does not guarantee correctness if the program implements the wrong mathematical requirement.

---

## 17. Example 11 — Linear Search

### Problem

Find the first occurrence of a target in a list.

### Algorithm

1. Read a non-empty list and target.
2. Check each element from the beginning.
3. If an element equals the target, record its index and stop.
4. If no element matches, return the not-found result.
5. Display the result.

### Python Code

```python
values = list(map(int, input("Enter integers: ").split()))
target = int(input("Enter target: "))

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

This code assumes that the user enters at least one integer. The selected index is zero-based.

The explicit result convention—first matching index or `-1`—makes the output easy to interpret.

---

## 18. Example 12 — Greatest Common Divisor

### Problem

Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

### Algorithm

1. Take the absolute values of the inputs.
2. While the second value is not zero, replace the pair with the second value and the remainder.
3. When the second value becomes zero, the first value is the GCD.
4. Display the result.

### Python Code

```python
a = abs(int(input("Enter first integer: ")))
b = abs(int(input("Enter second integer: ")))

while b != 0:
    a, b = b, a % b

print("GCD:", a)
```

For inputs `48` and `18`, the GCD is `6`.

Each non-terminal iteration reduces the remainder problem. Euclid's algorithm is substantially more efficient for large inputs than checking every candidate divisor one by one.

---

## 19. Overview of the 12 Examples

The practical file `04_algorithm_characteristics.py` includes:

| No. | Example | Characteristic or concept |
|---:|---|---|
| 1 | Definiteness | Clear, unambiguous steps |
| 2 | Input and Output | Explicit input and output |
| 3 | Finiteness | A terminating loop |
| 4 | Effectiveness | Simple executable operations |
| 5 | Correctness | Selecting the maximum value |
| 6 | Generality | Handling positive, negative, and zero |
| 7 | Input Validation | Avoiding division by zero |
| 8 | Termination | A decreasing countdown |
| 9 | Efficiency | Comparing two summation approaches |
| 10 | Deterministic Result | Reproducible calculation |
| 11 | Linear Search | Defined search result |
| 12 | GCD | Effective remainder-based algorithm |

---

## 20. Twelve Solved Practice Questions

The Python file contains the following solved questions:

1. Smallest of Three Numbers
2. Average of a List
3. Count Even and Odd Values
4. Classify Positive, Negative, and Zero
5. Factorial
6. Check Leap Year
7. Reverse an Integer
8. Sum of Digits
9. Linear Search
10. Count Target Frequency
11. Selection Sort
12. Find a Missing Number

These exercises test whether your algorithms define their inputs and outputs, handle relevant edge cases, terminate as intended, and produce the expected results.

---

## 21. Five Independent Practice Questions

These problems do not include answer code.

### Question 1: Binary Search

Search for a target in a sorted list. Explain why the sorted-input precondition matters and define the output when the target is absent.

### Question 2: Second-Largest Distinct Value

Find the second-largest distinct value in a list. Define what should happen if fewer than two distinct values exist.

### Question 3: Check an Armstrong Number

Determine whether a non-negative integer equals the sum of its digits, each raised to the power of the number of digits.

### Question 4: Merge Two Sorted Lists

Design an algorithm that combines two sorted lists into a single sorted list.

### Question 5: Compare Two Approaches

Compare a loop-based sum from 1 to `N` with the formula `N * (N + 1) // 2`. Explain correctness and efficiency.

For each question, define the inputs, output, assumptions, steps, and test cases before writing Python code.

---

## 22. Testing Algorithms Systematically

Use a test table to examine important cases.

| Test type | Purpose | Example for largest of three |
|---|---|---|
| Typical input | Check ordinary behaviour | 10, 25, 15 |
| Largest in first position | Check an alternative branch | 30, 20, 10 |
| Largest in last position | Check another branch | 5, 12, 18 |
| Equal inputs | Check ties | 7, 7, 7 |
| Invalid input | Check input restrictions | Non-numeric text for a numeric field |

Testing should reflect the problem's actual requirements. An input is not invalid merely because it is unusual; it is invalid when it violates a stated constraint or supported format.

A rigorous correctness argument is different from testing. Tests demonstrate behaviour for selected cases, whereas a proof or careful mathematical argument may establish correctness for an entire class of inputs.

---

## 23. Common Mistakes

### An ambiguous step

An instruction such as “calculate the result properly” does not define the required operation.

**Improvement:** Specify the operation and its inputs explicitly.

### An algorithm that does not terminate

A loop may repeat indefinitely if its stopping condition is never reached.

**Improvement:** Identify what changes each iteration and why it will eventually reach the stopping condition.

### Missing input or output definitions

A solution may be unclear about what it accepts or produces.

**Improvement:** Explicitly document the input and expected output.

### An incorrect algorithm that always returns a value

An algorithm can terminate and still be incorrect.

**Improvement:** Verify the logic against the problem requirements.

### A solution that works only for one test

A hard-coded result may work for a sample input but fail for others.

**Improvement:** Design a general solution and test a variety of valid inputs.

### Ignoring resource requirements

An algorithm can be correct but too slow or memory-intensive for large inputs.

**Improvement:** Compare time and auxiliary space complexity where relevant.

---

## 24. Complexity Reference

Complexity analysis describes how computational work or memory requirements grow with input size.

| Algorithm | Time complexity | Auxiliary space |
|---|---|---|
| Addition of two numbers | O(1) | O(1) |
| Largest of three numbers | O(1) | O(1) |
| Sum from 1 to N using a loop | O(N) | O(1) |
| Sum using a direct formula | O(1) under the fixed-size operation model | O(1) |
| Linear search | O(N) worst case | O(1) |
| Digit counting | O(D) | O(1) |
| GCD using the Euclidean algorithm | O(log min(A, B)) for positive inputs | O(1) |
| Selection sort | O(N²) | O(1) in the in-place version |

Here, `N` is generally the number of elements or iterations, while `D` denotes the number of decimal digits in an integer.

These are standard asymptotic estimates. For large arbitrary-precision integers, the costs of individual arithmetic operations also depend on the number of digits.

---

## 25. Interview Questions and Answers

**Q1. What are the classic characteristics of an algorithm?**

They commonly include input, output, definiteness, finiteness, and effectiveness.

**Q2. What is definiteness?**

Each instruction must be clear enough to avoid ambiguity about the required operation.

**Q3. What is finiteness?**

The algorithm must terminate after a finite number of steps for inputs within its intended scope.

**Q4. What is effectiveness?**

The operations should be sufficiently basic, practical, and executable as specified.

**Q5. What is correctness?**

Correctness means producing the required result for all inputs within the specified problem scope.

**Q6. What is generality?**

A general algorithm solves the stated class of problems rather than relying on a single hard-coded example.

**Q7. What is efficiency?**

Efficiency concerns the computational resources used by an algorithm, particularly time and memory.

**Q8. What is deterministic behaviour?**

For the same input and relevant initial conditions, a deterministic algorithm follows the same defined execution rules and produces the same result.

**Q9. Does termination guarantee correctness?**

No. An algorithm can terminate while producing an incorrect answer.

**Q10. Does testing a few inputs prove correctness?**

Not generally. Testing is useful evidence, but a proof or comprehensive reasoning may be needed to establish correctness for every input in scope.

**Q11. Why is input validation useful?**

It helps detect or reject values that violate the requirements before an unsafe or undefined operation is attempted.

**Q12. Can two correct algorithms have different efficiencies?**

Yes. Correct solutions to the same problem can require different amounts of time or memory.

---

## 26. How to Run the Python File

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\04_Algorithm_Characteristics\04_algorithm_characteristics.py"
```

The interactive menu provides three options:

1. Run the 12 examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

Select one item at a time and compare the implementation with the explanation in this README.

---

## ✅ Completion Checklist

- [ ] Understand input and output.
- [ ] Understand definiteness.
- [ ] Understand finiteness.
- [ ] Understand effectiveness.
- [ ] Understand correctness and generality.
- [ ] Understand deterministic behaviour.
- [ ] Learn the purpose of input validation.
- [ ] Compare algorithm efficiency.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved practice questions.
- [ ] Attempt the 5 independent practice questions.
- [ ] Test boundary and special cases.
- [ ] Answer the interview questions in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to evaluate a basic algorithm by considering how clearly its steps are defined, what inputs and outputs it handles, whether it terminates, whether it produces the required result, and how efficiently it operates.

These ideas will help you design better solutions as you move toward algorithm analysis and Data Structures and Algorithms.

---

## 📌 Final Note

**A good algorithm must do more than run: it should be clear, finite, effective, correct for its specified inputs, and reasonably efficient for its intended purpose.**

Practise explaining not only what your algorithm does, but also why it works and what its limitations are.
