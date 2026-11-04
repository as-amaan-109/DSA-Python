# Algorithm Basics

Welcome to **Algorithm Basics**, the first topic in the Algorithms section of Python Programming Fundamentals.

An algorithm is a clear, ordered method for solving a problem or completing a task. Before writing a Python program, it is useful to design the solution as a sequence of steps, verify the logic, and then implement it in code.

This topic introduces the foundations of algorithms through practical examples, solved exercises, and independent practice questions.

---

## 1. About This Topic

- **Week:** 1 – Programming Fundamentals
- **Section:** 02 – Flowcharts and Algorithms
- **Subsection:** Algorithms Basics
- **Topic:** Algorithm Basics
- **Level:** Beginner
- **Language:** Python
- **Practical File:** `01_algorithm_basics.py`

### Learning Objectives

After completing this topic, you should be able to:

- Define an algorithm and explain its purpose.
- Identify the input, processing, and output of a problem.
- Write clear, ordered algorithm steps.
- Understand the important characteristics of a good algorithm.
- Convert an algorithm into pseudocode and Python.
- Trace the execution of an algorithm with a dry run.
- Check whether a solution produces the expected result.
- Recognize basic edge cases and invalid inputs.
- Understand introductory time and space complexity.
- Solve beginner-level programming problems systematically.

---

## 2. What Is an Algorithm?

An **algorithm** is a finite, clearly defined sequence of steps used to solve a problem or perform a computation.

Algorithms are not limited to computers. A recipe, a set of instructions for assembling an object, or a process for calculating a bill can also be described as a sequence of steps.

In programming, an algorithm provides the logic that a program implements.

### Example: Adding Two Numbers

**Problem:** Find the sum of two numbers.

**Algorithm:**

1. Start.
2. Read the first number, `A`.
3. Read the second number, `B`.
4. Calculate `SUM = A + B`.
5. Display `SUM`.
6. Stop.

**Python implementation:**

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

The algorithm describes the solution. The Python program implements it using Python syntax.

---

## 3. Why Are Algorithms Important?

Algorithms help programmers organise their reasoning before coding.

They are useful because they:

- Make problem-solving steps clear.
- Separate the logic from programming-language syntax.
- Help reveal missing operations or incorrect assumptions.
- Make solutions easier to test and explain.
- Provide a basis for comparing different approaches.
- Support debugging and maintenance.
- Prepare you for Data Structures and Algorithms (DSA).

A well-designed algorithm is not necessarily the shortest one. It must correctly solve the specified problem, and it should be clear and practical for the situation.

---

## 4. Basic Elements of an Algorithm

Many beginner algorithms can be understood using three main stages.

### Input

The information required by the solution.

Example:

```text
INPUT A
INPUT B
```

### Processing

The calculations or operations performed on the input.

Example:

```text
SET SUM = A + B
```

### Output

The result produced by the solution.

Example:

```text
DISPLAY SUM
```

These stages can be summarised as:

```text
INPUT → PROCESSING → OUTPUT
```

Not every algorithm follows exactly one input-processing-output sequence. More complex algorithms can have repeated operations, decisions, multiple outputs, and several intermediate stages.

---

## 5. Characteristics of a Good Algorithm

A good algorithm should meet the requirements of the problem and should be designed carefully.

### 1. Clearly Defined Inputs

An algorithm should make clear what information it needs.

For example, calculating the area of a rectangle requires its length and width.

### 2. Clearly Defined Outputs

The required result should be identifiable.

For a rectangle-area problem, the output is the calculated area.

### 3. Definiteness

Every step should be sufficiently clear and unambiguous for the intended task.

For example, “add the two input values” is clearer than “process the values appropriately.”

### 4. Finiteness

The algorithm should finish after a finite number of steps for inputs within its intended scope.

A loop with no reachable stopping condition may fail this requirement.

### 5. Effectiveness

The operations should be basic enough to carry out as specified and should contribute to solving the problem.

### 6. Correctness

The algorithm should produce the required results for valid inputs, including relevant boundary cases.

### 7. Generality

Where required, the solution should work for the full range of inputs described by the problem, rather than only one example.

### 8. Efficiency

The algorithm should use reasonable amounts of time and memory for its intended input sizes.

These characteristics are useful principles for analysing algorithms. The exact requirements depend on the problem being solved.

---

## 6. Algorithm vs Pseudocode vs Flowchart vs Program

These terms are related, but they describe different aspects of a solution.

| Concept | Meaning | Example |
|---|---|---|
| Algorithm | Ordered logical steps that solve a problem | Read two numbers, add them, display the sum |
| Pseudocode | A readable textual representation of the logic | `SET SUM = A + B` |
| Flowchart | A diagram representing the flow of the solution | Input symbol → process symbol → output symbol |
| Program | An implementation written in a programming language | Python code using `input()` and `print()` |

You can design an algorithm, describe it in pseudocode, represent it using a flowchart, and then implement it as a Python program.

---

## 7. Steps to Design an Algorithm

Use the following process when approaching a new programming problem.

### Step 1: Understand the Problem

Identify precisely what the problem asks you to solve.

Read the statement carefully and identify any conditions or restrictions.

### Step 2: Identify the Inputs

List the values required by the solution.

For a simple-interest calculation, the inputs are principal, annual rate, and time.

### Step 3: Identify the Outputs

Determine what the algorithm needs to produce.

For simple interest, the output might include both the interest and the final amount.

### Step 4: Identify the Required Formula or Logic

Decide which mathematical rule, condition, or sequence of actions solves the problem.

### Step 5: Write the Steps in Order

Put the operations in a logical sequence. Ensure that values are obtained before they are used.

### Step 6: Trace the Algorithm

Perform a dry run using sample input values.

Track the values of variables after each operation.

### Step 7: Implement the Algorithm

Translate the steps into Python.

### Step 8: Test the Result

Compare the actual output against the expected result. Include boundary values and special cases where relevant.

### Step 9: Review the Solution

Check whether the algorithm is clear, correct, and suitable for the problem's constraints.

---

## 8. Example 1 — Display a Greeting

### Problem

Display a welcome message.

### Algorithm

1. Start.
2. Display `Hello! Welcome to Algorithm Basics.`
3. Stop.

### Python Code

```python
print("Hello! Welcome to Algorithm Basics.")
```

### Output

```text
Hello! Welcome to Algorithm Basics.
```

### Explanation

This is a simple sequential algorithm. It performs one output operation and then finishes.

---

## 9. Example 2 — Addition of Two Numbers

### Problem

Accept two numbers and calculate their sum.

### Algorithm

1. Read `A`.
2. Read `B`.
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
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b

print("Sum:", total)
```

### Sample Output

```text
Enter first number: 10
Enter second number: 20
Sum: 30.0
```

### Dry Run

| Step | Operation | Value |
|---|---|---|
| 1 | Read first input | A = 10 |
| 2 | Read second input | B = 20 |
| 3 | Calculate the sum | SUM = 30 |
| 4 | Display the result | 30.0 |

Because the Python code uses `float()`, the result is displayed as `30.0`.

---

## 10. Example 3 — Find the Difference

### Problem

Subtract the second number from the first.

### Algorithm

1. Read `A` and `B`.
2. Calculate `DIFFERENCE = A - B`.
3. Display the difference.

### Python Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

difference = a - b

print("Difference:", difference)
```

### Sample Output

```text
Enter first number: 15
Enter second number: 5
Difference: 10.0
```

### Important Point

Subtraction is order-dependent. In general, `A - B` is not equal to `B - A`.

---

## 11. Example 4 — Multiplication of Two Numbers

### Problem

Calculate the product of two numbers.

### Algorithm

1. Read `A` and `B`.
2. Calculate `PRODUCT = A × B`.
3. Display the product.

### Python Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

product = a * b

print("Product:", product)
```

### Sample Output

```text
Enter first number: 6
Enter second number: 7
Product: 42.0
```

### Edge Case

If either input is zero, the product is zero.

---

## 12. Example 5 — Area of a Rectangle

### Problem

Calculate the area using the rectangle's length and width.

### Formula

\[
\text{Area} = \text{Length} \times \text{Width}
\]

### Algorithm

1. Read length and width.
2. Check that neither dimension is negative.
3. Multiply length by width.
4. Display the area.

### Python Code

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Dimensions must be non-negative.")
else:
    area = length * width
    print("Area:", area)
```

### Sample Output

```text
Enter length: 5
Enter width: 4
Area: 20.0
```

This example introduces a basic validation step. Zero is accepted under the illustrative non-negative dimension rule, though a physical rectangle normally has positive dimensions.

---

## 13. Example 6 — Average of Three Numbers

### Problem

Calculate the average of three values.

### Formula

\[
\text{Average} = \frac{A+B+C}{3}
\]

### Algorithm

1. Read the three values.
2. Add them.
3. Divide their sum by 3.
4. Display the average.

### Python Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average:", average)
```

### Sample Output

```text
Enter first number: 10
Enter second number: 20
Enter third number: 30
Average: 20.0
```

---

## 14. Example 7 — Check Even or Odd

### Problem

Determine whether an integer is even or odd.

### Algorithm

1. Read an integer.
2. Calculate its remainder when divided by 2.
3. If the remainder is zero, display “Even.”
4. Otherwise, display “Odd.”

### Pseudocode

```text
START
    INPUT NUMBER

    IF NUMBER MOD 2 = 0
        DISPLAY "Even"
    ELSE
        DISPLAY "Odd"
    END IF
END
```

### Python Code

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Sample Output

```text
Enter an integer: 7
Odd
```

The remainder operator in Python is `%`. For integer parity, it allows the program to distinguish even from odd numbers, including negative integers and zero.

---

## 15. Example 8 — Classify a Number

### Problem

Determine whether a number is positive, negative, or zero.

### Algorithm

1. Read a number.
2. If it is greater than zero, classify it as positive.
3. Otherwise, if it is less than zero, classify it as negative.
4. Otherwise, classify it as zero.

### Python Code

```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

### Sample Outputs

| Input | Result |
|---:|---|
| `10` | Positive number |
| `-5` | Negative number |
| `0` | Zero |

This algorithm demonstrates decision-making through multiple conditions.

---

## 16. Example 9 — Find the Larger of Two Numbers

### Problem

Compare two values and display the larger one, handling equality as well.

### Algorithm

1. Read `A` and `B`.
2. If `A > B`, select `A`.
3. Otherwise, if `B > A`, select `B`.
4. Otherwise, the values are equal.
5. Display the appropriate result.

### Python Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal.")
```

### Sample Output

```text
Enter first number: 12
Enter second number: 18
Larger number: 18.0
```

A good solution accounts for equality rather than assuming one value must always be greater than the other.

---

## 17. Example 10 — Find the Largest of Three Numbers

### Problem

Determine the largest value among three numbers.

### Algorithm

1. Read `A`, `B`, and `C`.
2. Check whether `A` is greater than or equal to both other values.
3. If not, check whether `B` is greater than or equal to both other values.
4. Otherwise, select `C`.
5. Display the largest value.

### Python Code

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)
```

### Dry Run

Suppose `A = 10`, `B = 25`, and `C = 15`.

| Step | Condition | Result |
|---|---|---|
| 1 | Is A greater than or equal to B and C? | False |
| 2 | Is B greater than or equal to A and C? | True |
| 3 | Select B | 25 |
| 4 | Display the largest number | 25 |

The use of `>=` means the logic also works when some or all input values are equal.

---

## 18. Example 11 — Swap Two Values

### Problem

Exchange the values stored in two variables.

### Algorithm

1. Read `A` and `B`.
2. Store `A` in a temporary variable.
3. Assign `B` to `A`.
4. Assign the temporary value to `B`.
5. Display the new values.

### Pseudocode

```text
START
    INPUT A, B
    SET TEMP = A
    SET A = B
    SET B = TEMP
    DISPLAY A, B
END
```

### Python Code

```python
a = 5
b = 10

temp = a
a = b
b = temp

print("A =", a)
print("B =", b)
```

Output:

```text
A = 10
B = 5
```

A temporary variable preserves the original value of `A` while the assignments take place.

Python also supports tuple assignment to swap values, but the temporary-variable approach makes the algorithm explicit for beginners.

---

## 19. Example 12 — Calculate Simple Interest

### Problem

Calculate simple interest using principal, annual rate, and time.

### Formula

\[
\text{Simple Interest}
=
\frac{\text{Principal}\times\text{Rate}\times\text{Time}}{100}
\]

### Algorithm

1. Read the principal.
2. Read the annual interest rate as a percentage.
3. Read time in years.
4. Validate that the values are non-negative.
5. Calculate simple interest.
6. Add the interest to principal to obtain the total amount.
7. Display the results.

### Python Code

```python
principal = float(input("Enter principal: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time in years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Values must be non-negative.")
else:
    interest = principal * rate * time / 100
    amount = principal + interest

    print("Simple interest:", interest)
    print("Total amount:", amount)
```

### Sample Output

```text
Enter principal: 1000
Enter annual rate (%): 5
Enter time in years: 2
Simple interest: 100.0
Total amount: 1100.0
```

This example illustrates how a mathematical formula can be translated into a sequence of program instructions.

---

## 20. Correctness and Testing

An algorithm should be checked against the problem requirements.

### Expected result

For each test, calculate the expected result independently when possible.

### Normal cases

Use common inputs to verify the main processing logic.

### Boundary cases

Test values at the limits of the allowed input range.

Examples include zero dimensions, equal numbers, or the smallest permitted input.

### Invalid inputs

Where relevant, check that invalid values are rejected or handled in a clearly defined way.

### Dry runs

A dry run manually traces the variable values and steps of an algorithm.

For the largest-of-three problem, a dry run helps verify which comparison succeeds and which value is selected.

Testing a few inputs cannot prove that every algorithm is correct, but carefully chosen cases provide useful evidence and can reveal mistakes.

---

## 21. Introductory Time and Space Complexity

Complexity analysis considers how the resources used by an algorithm grow as input size increases.

### Time complexity

Time complexity describes the growth of computational work as input size grows.

### Space complexity

Space complexity describes how memory requirements grow as input size grows.

Many single-calculation examples in this topic use a fixed number of arithmetic operations and a fixed number of variables. Under the usual model for fixed-size values, their time and auxiliary space complexity are generally described as **O(1)**.

The digit-counting solved question processes one decimal digit per loop iteration. If the integer has \(d\) digits, its time complexity is **O(d)**, and the iterative solution uses **O(1)** auxiliary space.

Complexity labels should describe how work grows with input size; they do not measure the exact number of seconds a program takes.

---

## 22. Overview of the 12 Examples

The practical file `01_algorithm_basics.py` includes:

| No. | Example | Main concept |
|---:|---|---|
| 1 | Display a Greeting | Output |
| 2 | Add Two Numbers | Arithmetic |
| 3 | Find the Difference | Subtraction |
| 4 | Multiply Two Numbers | Multiplication |
| 5 | Rectangle Area | Formula and validation |
| 6 | Average of Three Numbers | Aggregation and division |
| 7 | Even or Odd | Modulo and decision-making |
| 8 | Number Classification | Multiple conditions |
| 9 | Larger of Two Numbers | Comparison |
| 10 | Largest of Three Numbers | Combined conditions |
| 11 | Swap Two Values | Temporary variable |
| 12 | Simple Interest | Formula-based algorithm |

For each example, identify the input, the processing steps, and the expected output. Then run the example and compare your prediction with the result.

---

## 23. Twelve Solved Practice Questions

The Python file also contains these solved questions:

1. Perimeter of a Rectangle
2. Area of a Square
3. Circumference of a Circle
4. Celsius to Fahrenheit
5. Quotient and Remainder
6. Seconds to Time Components
7. Percentage of Five Subjects
8. Calculate Discount
9. Calculate Speed
10. Count Digits
11. Check Leap Year
12. Calculate Total Amount

These exercises extend the same algorithm-design principles to geometry, conversions, validation, arithmetic operations, and basic number processing.

For every problem, practise writing the algorithm yourself before inspecting the implementation.

---

## 24. Five Independent Practice Questions

The following questions do not include solution code.

### Question 1: Find the Smallest of Three Numbers

Accept three numbers and identify the smallest. Handle cases where two or more values are equal.

### Question 2: Sum of Digits

Accept an integer and calculate the sum of its digits. Decide how negative numbers should be handled.

### Question 3: Reverse an Integer

Accept an integer and display its digits in reverse order. Consider how the sign and trailing zeroes should be handled.

### Question 4: Check a Prime Number

Accept an integer and determine whether it is prime. Remember that integers below 2 are not prime.

### Question 5: Grade Classification

Accept marks out of 100 and assign a grade using a grading scale you define. Validate the marks before assigning a grade.

### Recommended solving method

1. Rewrite the problem in your own words.
2. Identify inputs and outputs.
3. Document constraints and assumptions.
4. Write the algorithm in numbered steps.
5. Convert it into pseudocode.
6. Implement it in Python.
7. Trace sample input and test boundary cases.

---

## 25. Common Algorithm-Design Mistakes

### Missing steps

**Problem:** The algorithm uses a value before it has been obtained.

**Improvement:** Check the order of input, processing, and output instructions.

### Incorrect conditions

**Problem:** A comparison does not include an equality case where one is required.

**Improvement:** Test values that are equal and values around a decision boundary.

### Incorrect formulas

**Problem:** The code runs but gives an incorrect mathematical result.

**Improvement:** Write the formula explicitly and verify it with known values.

### Ignoring invalid inputs

**Problem:** The solution assumes every possible input is permitted.

**Improvement:** Define allowed values and implement checks where required.

### Confusing an algorithm with code

**Problem:** The logic is described only through Python syntax, making it harder to reason about the solution independently.

**Improvement:** Write the steps or pseudocode first, then implement the program.

### Testing only one example

**Problem:** The algorithm works for one input but fails for another.

**Improvement:** Test ordinary values, boundary cases, and relevant special cases.

---

## 26. Interview Questions and Answers

**Q1. What is an algorithm?**

An algorithm is a finite, clearly defined sequence of steps used to solve a problem or perform a task.

**Q2. Why are algorithms important?**

They help organise logic, verify correctness, explain solutions, and compare possible approaches before implementation.

**Q3. What are the main characteristics of a good algorithm?**

Common characteristics include clearly defined inputs and outputs, definiteness, finiteness, and effective operations. Correctness, generality, and efficiency are also important design goals.

**Q4. What is the difference between an algorithm and a program?**

An algorithm describes the solution method. A program implements that method in a programming language.

**Q5. What is pseudocode?**

Pseudocode is a readable, language-independent way of expressing an algorithm's logic.

**Q6. What is a dry run?**

A dry run manually traces an algorithm using sample values to understand its execution.

**Q7. What is algorithm correctness?**

Correctness means that the algorithm produces the results required by the problem for all inputs within its specified scope.

**Q8. What is time complexity?**

Time complexity describes how an algorithm's computational work grows with input size.

**Q9. What is space complexity?**

Space complexity describes how an algorithm's memory requirements grow with input size.

**Q10. Why are edge cases important?**

They can reveal errors at the boundaries or under unusual conditions that ordinary test inputs do not expose.

**Q11. Can two algorithms solve the same problem?**

Yes. Different algorithms may solve the same problem while differing in clarity, time requirements, or memory usage.

**Q12. What is the purpose of input validation?**

It checks whether supplied values meet the problem's requirements before the program proceeds.

---

## 27. How to Run the Python File

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\02-Flowcharts-Algorithms\Algorithms-Basics\01_Algorithm_Basics\01_algorithm_basics.py"
```

The menu provides three options:

1. Run the 12 algorithm examples.
2. Run the 12 solved practice questions.
3. View the 5 questions without answers.

Select one item at a time. Enter `0` to return to the previous menu or exit from the main menu.

---

## ✅ Completion Checklist

- [ ] Understand the definition of an algorithm.
- [ ] Identify input, processing, and output.
- [ ] Learn the characteristics of a good algorithm.
- [ ] Distinguish an algorithm, pseudocode, a flowchart, and a program.
- [ ] Practise designing algorithms before coding.
- [ ] Perform dry runs.
- [ ] Test normal and boundary cases.
- [ ] Run all 12 examples.
- [ ] Complete the 12 solved questions.
- [ ] Attempt the 5 independent practice questions.
- [ ] Understand the introductory complexity notes.
- [ ] Answer the interview questions in your own words.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to describe a problem as a sequence of logical steps, implement those steps in Python, test the result, and explain the reasoning behind the solution.

These concepts form the foundation for the next topics in Algorithms Basics: algorithm steps, algorithm examples, characteristics, analysis, and practice.

---

## 📌 Final Note

**First understand the problem, then design the algorithm, and only after that write the code.**

Clear reasoning and consistent practice will make more advanced algorithm and DSA problems easier to approach.
