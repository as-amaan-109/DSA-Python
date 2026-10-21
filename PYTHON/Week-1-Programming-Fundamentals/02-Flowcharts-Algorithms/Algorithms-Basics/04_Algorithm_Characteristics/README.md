# Algorithm Characteristics

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Algorithm Characteristics  
> **Level:** Beginner  
> **Goal:** Understand the fundamental properties of an algorithm and learn how to evaluate its quality.

---

## Table of Contents

1. Introduction
2. What Are Algorithm Characteristics?
3. Input
4. Output
5. Definiteness
6. Finiteness
7. Effectiveness
8. Correctness
9. Generality
10. Efficiency
11. Example: Analyze an Addition Algorithm
12. Example: Check Algorithm Correctness
13. What Makes an Algorithm Poor?
14. How to Evaluate an Algorithm
15. Algorithm Characteristics Reference Table
16. Important Terminology
17. Interview Questions
18. Practice Questions
19. Learning Checklist
20. What's Next?

---

## 1. Introduction

An algorithm is a sequence of steps designed to solve a problem.

However, simply writing a sequence of steps does not guarantee that the algorithm is good.

An algorithm should be clear, produce the expected result, finish its execution, and perform its operations effectively.

These properties are known as **algorithm characteristics**.

For example, consider an algorithm that adds two numbers.

```text
Step 1: Start.
Step 2: Read two numbers A and B.
Step 3: Calculate SUM = A + B.
Step 4: Display SUM.
Step 5: Stop.
```

This algorithm has input, produces output, uses a clearly defined operation, and finishes after a finite number of steps.

In this topic, we will learn how to identify and evaluate these characteristics.

---

## 2. What Are Algorithm Characteristics?

Algorithm characteristics are the properties used to describe and evaluate an algorithm.

Many introductory textbooks identify five fundamental characteristics:

1. Input
2. Output
3. Definiteness
4. Finiteness
5. Effectiveness

Other desirable properties commonly discussed include:

6. Correctness
7. Generality
8. Efficiency

The exact classification can differ slightly between textbooks. For this repository, we will study all eight properties.

### Why Are These Characteristics Important?

They help us determine whether an algorithm:

- Accepts the information it needs.
- Produces useful results.
- Has clear and unambiguous instructions.
- Finishes its execution.
- Performs practical operations.
- Produces correct results.
- Works for a suitable range of inputs.
- Uses time and memory efficiently.

---

## 3. Input

### Definition

**Input** is the data supplied to an algorithm so it can solve a problem.

An algorithm may accept zero or more inputs, depending on the problem.

### Example: Addition of Two Numbers

Inputs:

```text
A = 10
B = 20
```

Algorithm:

1. Start.
2. Read A and B.
3. Calculate SUM = A + B.
4. Display SUM.
5. Stop.

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

### Explanation

The values `10` and `20` are the inputs.

The algorithm uses these values to calculate the result.

### Does Every Algorithm Need Input?

No.

For example:

```python
print("Hello, Python!")
```

This program displays a fixed message without requiring any external input.

**Key point:** An algorithm can have zero or more inputs, depending on the problem it solves.

---

## 4. Output

### Definition

**Output** is the result or information produced by an algorithm.

An algorithm should produce at least one well-defined result for its intended task.

### Example

Problem: Calculate the sum of two numbers.

Inputs:

```text
A = 15
B = 5
```

Calculation:

```text
SUM = 15 + 5
SUM = 20
```

Output:

```text
Sum = 20
```

Python implementation:

```python
a = 15
b = 5

total = a + b

print("Sum:", total)
```

### Why Is Output Important?

Without a clearly defined result, it may be difficult to determine whether an algorithm has successfully completed its intended task.

Output does not always have to mean displaying text on a screen. Depending on the problem, an algorithm may return a value, generate a file, update a data structure, or produce another defined result.

**Key point:** Identify the expected result before designing the algorithm.

---

## 5. Definiteness

### Definition

**Definiteness** means that every step of an algorithm must be clear, precise, and unambiguous.

Each instruction should have a well-defined meaning.

### Example of a Clear Algorithm

Problem: Calculate the area of a rectangle.

```text
Step 1: Start.
Step 2: Set LENGTH = 5.
Step 3: Set BREADTH = 3.
Step 4: Calculate AREA = LENGTH × BREADTH.
Step 5: Display AREA.
Step 6: Stop.
```

Every instruction states exactly what needs to be done.

### Example of an Ambiguous Algorithm

```text
Step 1: Start.
Step 2: Take some numbers.
Step 3: Perform the necessary calculation.
Step 4: Display the answer.
Step 5: Stop.
```

This is unclear because:

- It does not specify how many numbers to take.
- It does not identify the required calculation.
- It does not define what answer should be displayed.

### Improved Version

```text
Step 1: Start.
Step 2: Read two numbers A and B.
Step 3: Calculate SUM = A + B.
Step 4: Display SUM.
Step 5: Stop.
```

### Why Is Definiteness Important?

Clear instructions reduce confusion and help programmers implement the algorithm consistently.

**Key point:** Every step should tell us exactly what action is required.

---

## 6. Finiteness

### Definition

**Finiteness** means that an algorithm must terminate after a finite number of steps for every valid input within its intended domain.

An algorithm should not continue executing forever when the task is expected to finish.

### Example of a Finite Algorithm

Problem: Display numbers from 1 to 5.

Algorithm:

1. Start with `number = 1`.
2. Display the number.
3. Increase the number by 1.
4. Repeat while the number is less than or equal to 5.
5. Stop when the condition becomes false.

Python implementation:

```python
number = 1

while number <= 5:
    print(number)
    number = number + 1

print("Finished")
```

Output:

```text
1
2
3
4
5
Finished
```

The variable increases on every iteration, so the loop eventually terminates.

### Example of a Potentially Infinite Loop

```python
# Do not run this example without changing its condition.
#
# number = 1
#
# while number <= 5:
#     print(number)
```

This loop never changes `number`.

Since `number` remains `1`, the condition continues to be true and the loop does not terminate normally.

### How to Avoid Infinite Loops

- Check the loop condition carefully.
- Make sure the values controlling the condition can change.
- Test the algorithm with representative inputs.
- Include an appropriate stopping condition.

### Key Point

Finiteness is about guaranteed termination for the algorithm's intended valid inputs, not simply whether the algorithm eventually stops for one example.

---

## 7. Effectiveness

### Definition

**Effectiveness** means that the operations in an algorithm should be sufficiently basic, practical, and executable in a finite amount of time.

Each step should be something that can actually be carried out.

### Example of an Effective Algorithm

Problem: Multiply two numbers.

Algorithm:

1. Start.
2. Set A = 6.
3. Set B = 7.
4. Calculate PRODUCT = A × B.
5. Display PRODUCT.
6. Stop.

Python implementation:

```python
a = 6
b = 7

product = a * b

print("Product:", product)
```

Output:

```text
Product: 42
```

The instructions are clear, and the multiplication can be performed as a practical computational operation.

### Example of an Ineffective Instruction

Consider the instruction:

```text
Find the answer without performing any calculation or using any information.
```

This does not describe a useful computational procedure.

An algorithm must specify operations that can actually be carried out.

### Definiteness vs Effectiveness

These two characteristics are related but different.

| Definiteness | Effectiveness |
|---|---|
| Steps must be clear and unambiguous. | Steps must be executable and practical. |
| Focuses on the meaning of the instructions. | Focuses on whether the operations can be carried out. |
| Example: Clearly specify `SUM = A + B`. | Example: Use an available addition operation to calculate the sum. |

**Key point:** An algorithm's instructions should be both clear and executable.

---

## 8. Correctness

### Definition

**Correctness** means that an algorithm produces the expected result for inputs that satisfy the problem's requirements.

An algorithm is not correct merely because it runs without producing an error.

The output must also be right.

### Example of a Correct Algorithm

Problem: Find the sum of two numbers.

```python
a = 15
b = 5

total = a + b

print("Sum:", total)
```

Output:

```text
Sum: 20
```

The result is correct because:

```text
15 + 5 = 20
```

### Example of an Incorrect Algorithm

```python
a = 15
b = 5

total = a - b

print("Sum:", total)
```

Output:

```text
Sum: 10
```

The program runs, but the algorithm is incorrect for the stated problem because it subtracts instead of adding.

### How to Check Correctness

1. Understand the intended result.
2. Test the algorithm using sample inputs.
3. Calculate the expected result independently.
4. Compare the actual output with the expected output.
5. Test edge cases and other relevant inputs.

### Example Test Table

| A | B | Expected Sum |
|---:|---:|---:|
| 10 | 20 | 30 |
| 0 | 5 | 5 |
| -5 | 8 | 3 |
| -4 | -6 | -10 |

An addition algorithm should produce the expected result for all these test cases.

**Important:** Testing can reveal errors, but passing a few tests does not necessarily prove an algorithm correct for every possible input.

---

## 9. Generality

### Definition

**Generality** means that an algorithm should solve a class of similar problems rather than only one fixed instance of a problem.

A general algorithm accepts different valid inputs and applies the same solution logic.

### Example of a Non-General Solution

```python
print(10 + 20)
```

This displays the sum of two fixed values.

It solves that particular calculation, but the values must be changed manually for other additions.

### A More General Solution

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

This version works for different integer inputs without rewriting the algorithm.

### Examples

For the same addition logic:

```text
10 + 20 = 30
100 + 250 = 350
-5 + 8 = 3
```

The algorithm does not need to change when the input values change.

### Why Is Generality Important?

- It makes algorithms reusable.
- It avoids hardcoding a solution for one example.
- It supports different valid inputs.
- It helps solve a wider class of problems.

**Key point:** A general solution describes a reusable method, not just one answer.

---

## 10. Efficiency

### Definition

**Efficiency** describes how much computational time and memory an algorithm uses as the problem size grows.

A more efficient algorithm generally requires fewer computational resources for the same task, although trade-offs between time, memory, and simplicity may exist.

### 10.1 Time Efficiency

Time efficiency concerns how the number of operations or execution time grows with the input size.

For example, suppose an algorithm visits every element of a list once to calculate its sum.

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for value in numbers:
    total = total + value

print("Sum:", total)
```

Output:

```text
Sum: 150
```

If the list contains `n` elements, the loop processes each element once. The work grows linearly with the number of elements.

This is commonly described as **O(n)** time complexity.

### 10.2 Space Efficiency

Space efficiency concerns how much additional memory an algorithm uses.

For example, an algorithm that calculates a running sum using a fixed number of variables can solve the problem without creating another list proportional to the input size.

### Why Is Efficiency Important?

An algorithm may be correct but take too long or consume too much memory when the input becomes large.

Efficiency becomes especially important in:

- Searching large datasets
- Sorting arrays
- Processing text
- Graph algorithms
- Competitive programming
- Technical interviews

We will study time complexity, space complexity, and Big O notation in detail in the **Algorithm Analysis** topic.

---

## 11. Example: Analyze an Addition Algorithm

Let's evaluate the algorithm for adding two numbers.

### Problem

Calculate the sum of two numbers and display the result.

### Algorithm

1. Start.
2. Read A.
3. Read B.
4. Calculate SUM = A + B.
5. Display SUM.
6. Stop.

### Python Implementation

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

### Analysis of Characteristics

| Characteristic | How the algorithm demonstrates it |
|---|---|
| Input | Receives two numbers A and B. |
| Output | Produces their sum. |
| Definiteness | Specifies the exact operation `A + B`. |
| Finiteness | Executes a fixed number of steps. |
| Effectiveness | Uses a practical arithmetic operation. |
| Correctness | Produces 30 for inputs 10 and 20. |
| Generality | The same logic works for other valid numbers. |
| Efficiency | Performs a constant number of basic operations for this fixed-size input. |

This example shows how several characteristics can be evaluated for the same algorithm.

---

## 12. Example: Check Algorithm Correctness

One way to examine correctness is to compare the expected result with the calculated result.

### Python Implementation

```python
a = 15
b = 5

calculated_sum = a + b
expected_sum = 20

print("Calculated:", calculated_sum)
print("Expected:", expected_sum)

if calculated_sum == expected_sum:
    print("Test passed")
else:
    print("Test failed")
```

Output:

```text
Calculated: 20
Expected: 20
Test passed
```

### Explanation

The program performs the addition and checks the result against the expected sum.

If the two values match, the test passes for this test case.

For a stronger verification, test multiple inputs, including zero and negative values when they are valid for the problem.

**Note:** A successful test verifies the tested case. A complete correctness argument may require reasoning about all inputs allowed by the problem.

---

## 13. What Makes an Algorithm Poor?

An algorithm may have one or more problems.

### Example 1: Unclear Instructions

```text
Step 1: Take numbers.
Step 2: Calculate something.
Step 3: Show the answer.
```

Problem: The instructions do not specify the required calculation.

Characteristic affected: Definiteness.

### Example 2: Does Not Terminate

```python
# Example only; do not run this loop.
#
# number = 1
# while number <= 5:
#     print(number)
```

Problem: The controlling variable never changes.

Characteristic affected: Finiteness.

### Example 3: Incorrect Operation

```python
a = 10
b = 20

total = a - b
print(total)
```

Problem: Subtraction is used when the task requires addition.

Characteristic affected: Correctness.

### Example 4: Only Solves One Hardcoded Case

```python
print(10 + 20)
```

Problem: The values are fixed in the statement.

Characteristic affected: Generality, if the intended task is to add arbitrary input values.

### Example 5: Excessive Work

An algorithm that repeatedly scans a large collection unnecessarily may use much more time than another algorithm solving the same problem.

Characteristic affected: Efficiency.

---

## 14. How to Evaluate an Algorithm

Use the following checklist when examining a proposed solution.

### Step 1: Check the Input

Does the algorithm obtain all the information required by the problem?

### Step 2: Check the Output

Is the expected result clearly specified?

### Step 3: Check the Instructions

Is every step precise and unambiguous?

### Step 4: Check Termination

Does the algorithm finish for all valid inputs within its intended domain?

### Step 5: Check the Operations

Can each operation be carried out?

### Step 6: Verify Correctness

Does the algorithm produce the expected result?

### Step 7: Check Generality

Does the algorithm work for the broader class of inputs it is intended to handle?

### Step 8: Consider Efficiency

How much time and memory does the algorithm require as the input grows?

### Quick Evaluation Table

| Question | Characteristic |
|---|---|
| What information is supplied? | Input |
| What result is produced? | Output |
| Are the steps clear? | Definiteness |
| Does the algorithm finish? | Finiteness |
| Are the steps executable? | Effectiveness |
| Is the result correct? | Correctness |
| Does it solve similar valid cases? | Generality |
| How much time and memory does it use? | Efficiency |

---

## 15. Algorithm Characteristics Reference Table

| Characteristic | Meaning | Simple Example |
|---|---|---|
| Input | Data supplied to the algorithm | Two numbers for addition |
| Output | Result produced | Their calculated sum |
| Definiteness | Every instruction is clear | Specify `SUM = A + B` |
| Finiteness | Execution terminates | A loop stops after a defined count |
| Effectiveness | Steps are executable | Use a defined addition operation |
| Correctness | The expected result is produced | `10 + 20 = 30` |
| Generality | Works for a class of valid inputs | Add different pairs of numbers |
| Efficiency | Uses computational resources effectively | Process a list without unnecessary repeated scans |

**Remember:** Input, output, definiteness, finiteness, and effectiveness are commonly taught as the fundamental properties. Correctness, generality, and efficiency are also important when designing and evaluating practical algorithms.

---

## 16. Important Terminology

| Term | Meaning |
|---|---|
| Algorithm | A sequence of instructions used to solve a problem |
| Input | Information supplied to the solution |
| Output | Result produced by the solution |
| Definiteness | Clarity and precision of each step |
| Finiteness | Guaranteed termination for the intended valid inputs |
| Effectiveness | Practical executability of each step |
| Correctness | Producing the expected result |
| Generality | Solving a class of similar problems |
| Efficiency | Computational time and memory requirements |
| Test case | Input with an expected result |
| Edge case | An input at a boundary or unusual part of the valid input domain |
| Time complexity | How computational work grows with input size |
| Space complexity | How memory requirements grow with input size |

---

## 17. Interview Questions

### Q1. What are algorithm characteristics?

They are properties used to describe and evaluate an algorithm, such as input, output, definiteness, finiteness, and effectiveness.

### Q2. What are the five fundamental characteristics commonly taught in introductory courses?

Input, output, definiteness, finiteness, and effectiveness.

### Q3. What is definiteness?

Definiteness means each instruction must be precise and unambiguous.

### Q4. What is finiteness?

Finiteness means an algorithm must terminate after a finite number of steps for valid inputs within its intended domain.

### Q5. What is effectiveness?

Effectiveness means the algorithm's steps must be practical and executable in a finite amount of time.

### Q6. What is correctness?

Correctness means the algorithm produces the expected result for the valid inputs covered by the problem specification.

### Q7. What is generality?

Generality means an algorithm solves a class of similar problems instead of only one fixed instance.

### Q8. What is efficiency?

Efficiency concerns the time and memory resources required by an algorithm.

### Q9. Can an algorithm be correct but inefficient?

Yes. An algorithm may produce the right result but require excessive time or memory compared with a more efficient solution.

### Q10. What is the difference between definiteness and effectiveness?

Definiteness concerns whether the steps are clearly specified. Effectiveness concerns whether those steps can actually be carried out.

### Q11. How can you test an algorithm's correctness?

Use test cases, calculate expected outputs, compare actual results, and reason about whether the algorithm satisfies the problem requirements.

### Q12. Why is generality important?

It makes an algorithm useful for many valid inputs without requiring changes to its core logic.

---

## 18. Practice Questions

Try answering these in your own words before checking the notes.

### Beginner Level

**Question 1:** Define algorithm characteristics.

**Question 2:** List the five fundamental characteristics commonly taught in introductory algorithm design.

**Question 3:** Explain input and output with an example.

**Question 4:** What is definiteness? Give an example of an ambiguous instruction.

**Question 5:** What is finiteness? Explain how an infinite loop violates this property.

### Intermediate Level

**Question 6:** Explain effectiveness and correctness. How are they different?

**Question 7:** What is generality? Compare a hardcoded addition statement with an algorithm that accepts two input values.

**Question 8:** Explain time efficiency and space efficiency.

**Question 9:** Analyze the following algorithm using at least five characteristics:

```text
1. Start.
2. Read A and B.
3. Calculate SUM = A + B.
4. Display SUM.
5. Stop.
```

**Question 10:** Identify the problem in this code:

```python
number = 1

while number <= 5:
    print(number)
```

Which characteristic does it violate, and why?

### Challenge

Design an algorithm that calculates the average of three numbers.

Then explain how it satisfies:

1. Input
2. Output
3. Definiteness
4. Finiteness
5. Effectiveness
6. Correctness
7. Generality
8. Efficiency

Finally, test the algorithm with at least three different sets of numbers.

---

## 19. Learning Checklist

- [ ] Understand algorithm characteristics.
- [ ] Explain input and output.
- [ ] Understand definiteness.
- [ ] Understand finiteness.
- [ ] Understand effectiveness.
- [ ] Understand correctness.
- [ ] Understand generality.
- [ ] Understand efficiency.
- [ ] Identify an ambiguous algorithm.
- [ ] Identify a non-terminating loop.
- [ ] Test an algorithm using sample values.
- [ ] Analyze an algorithm using the reference table.
- [ ] Answer the interview questions.
- [ ] Complete the practice questions.

---

## 20. What's Next?

Continue with the next folder:

**05 - Algorithm Analysis**

In that topic, learn how to analyze an algorithm's performance, including execution steps, time complexity, space complexity, and introductory Big O notation.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `04_algorithm_characteristics.py` | Practical demonstrations of algorithm characteristics |
| `README.md` | Detailed theory, examples, comparisons, interview questions, and practice problems |

---

## Conclusion

A good algorithm should have clear instructions, finish its execution, use practical operations, and produce the expected result.

When designing an algorithm, also consider whether it works for the required range of inputs and whether it uses time and memory appropriately.

Remember these eight concepts:

**Input → Output → Definiteness → Finiteness → Effectiveness → Correctness → Generality → Efficiency**

Understanding these properties will prepare you to analyze and improve algorithms in the next topic.