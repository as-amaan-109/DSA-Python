# Algorithm Examples

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Algorithm Examples  
> **Level:** Beginner  
> **Goal:** Apply algorithm concepts to solve basic programming problems.

---

## Table of Contents

1. Introduction
2. How to Understand an Algorithm Example
3. Example 1 - Display a Message
4. Example 2 - Add Two Numbers
5. Example 3 - Subtract Two Numbers
6. Example 4 - Multiply Two Numbers
7. Example 5 - Calculate an Average
8. Example 6 - Area of a Rectangle
9. Example 7 - Perimeter of a Rectangle
10. Example 8 - Celsius to Fahrenheit
11. Example 9 - Swap Two Numbers
12. Example 10 - Find the Larger Number
13. Example 11 - Even or Odd
14. Example 12 - Square of a Number
15. What Is a Dry Run?
16. Common Mistakes
17. Important Terminology
18. Interview Questions
19. Practice Questions
20. Learning Checklist
21. What's Next?

---

## 1. Introduction

An algorithm is a sequence of well-defined steps used to solve a problem.

After learning the definition of an algorithm and how to write ordered steps, the next stage is to apply these concepts to actual problems.

For each problem in this topic, we will identify:

- The problem statement
- The required input
- The processing logic or formula
- The ordered algorithm steps
- The expected output
- The Python implementation

This approach helps us understand the logic before writing code.

---

## 2. How to Understand an Algorithm Example

Whenever you solve a new programming question, follow this process:

### Step 1: Understand the problem

Identify exactly what needs to be calculated or achieved.

### Step 2: Identify the input

Determine the information needed to solve the problem.

### Step 3: Determine the processing logic

Choose the formula, calculation, or comparison required.

### Step 4: Define the output

Decide what result should be produced.

### Step 5: Write the algorithm

Arrange the solution into clear, ordered steps.

### Step 6: Implement and test

Write the Python code, execute it, and compare the actual result with the expected result.

### General structure

```text
Problem
   |
   v
Input
   |
   v
Processing
   |
   v
Output
   |
   v
Test the Result
```

---

## 3. Example 1 - Display a Message

### Problem

Display the message `Welcome to Python Programming!`.

### Algorithm

1. Start.
2. Display the message.
3. Stop.

### Python Code

```python
print("Welcome to Python Programming!")
```

### Output

```text
Welcome to Python Programming!
```

### Explanation

This is a simple algorithm that displays a fixed message.

It does not require an external input or a mathematical calculation.

This example introduces the basic idea of executing an instruction and producing output.

---

## 4. Example 2 - Add Two Numbers

### Problem

Read two numbers and calculate their sum.

### Formula

```text
Sum = First Number + Second Number
```

### Algorithm

1. Start.
2. Read the first number.
3. Read the second number.
4. Calculate the sum.
5. Display the sum.
6. Stop.

### Sample Input

```text
First number = 10
Second number = 20
```

### Calculation

```text
Sum = 10 + 20
Sum = 30
```

### Expected Output

```text
Sum: 30
```

### Python Code

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Explanation

- `input()` receives text entered by the user.
- `int()` converts the input text to an integer.
- `a + b` performs addition.
- `print()` displays the result.

This is an example of an algorithm that obtains input from the user.

---

## 5. Example 3 - Subtract Two Numbers

### Problem

Find the difference between two numbers by subtracting the second number from the first.

### Formula

```text
Difference = First Number - Second Number
```

### Algorithm

1. Start.
2. Take the first number.
3. Take the second number.
4. Subtract the second number from the first.
5. Display the difference.
6. Stop.

### Sample Input

```text
First number = 25
Second number = 10
```

### Calculation

```text
Difference = 25 - 10
Difference = 15
```

### Expected Output

```text
Difference: 15
```

### Python Code

```python
a = 25
b = 10

difference = a - b

print("Difference:", difference)
```

### Explanation

The order of subtraction matters.

For the same values:

```text
25 - 10 = 15
10 - 25 = -15
```

Therefore, the algorithm must clearly specify which number is subtracted from which.

---

## 6. Example 4 - Multiply Two Numbers

### Problem

Calculate the product of two numbers.

### Formula

```text
Product = First Number × Second Number
```

### Algorithm

1. Start.
2. Take two numbers.
3. Multiply the numbers.
4. Display the product.
5. Stop.

### Sample Input

```text
First number = 6
Second number = 7
```

### Calculation

```text
Product = 6 × 7
Product = 42
```

### Python Code

```python
a = 6
b = 7

product = a * b

print("Product:", product)
```

### Output

```text
Product: 42
```

### Explanation

The multiplication operator in Python is `*`.

This example demonstrates how a mathematical operation is represented in an algorithm and then implemented in code.

---

## 7. Example 5 - Calculate an Average

### Problem

Calculate the average of three numbers.

### Formula

```text
Average = (A + B + C) / 3
```

### Algorithm

1. Start.
2. Obtain three numbers A, B, and C.
3. Add all three numbers.
4. Divide the total by 3.
5. Display the average.
6. Stop.

### Sample Input

```text
A = 10
B = 20
C = 30
```

### Calculation

```text
Total = 10 + 20 + 30
Total = 60

Average = 60 / 3
Average = 20
```

### Python Code

```python
a = 10
b = 20
c = 30

total = a + b + c
average = total / 3

print("Total:", total)
print("Average:", average)
```

### Output

```text
Total: 60
Average: 20.0
```

### Explanation

First, the algorithm calculates the total.

Next, it divides the total by the number of values.

The parentheses in the formula make it clear that the sum is calculated before division.

---

## 8. Example 6 - Area of a Rectangle

### Problem

Calculate the area of a rectangle using its length and breadth.

### Formula

```text
Area = Length × Breadth
```

### Algorithm

1. Start.
2. Take the length.
3. Take the breadth.
4. Multiply length by breadth.
5. Display the area.
6. Stop.

### Sample Input

```text
Length = 8
Breadth = 4
```

### Calculation

```text
Area = 8 × 4
Area = 32
```

### Python Code

```python
length = 8
breadth = 4

area = length * breadth

print("Area:", area)
```

### Output

```text
Area: 32
```

### Explanation

The area measures the two-dimensional surface covered by the rectangle.

The algorithm multiplies the length by the breadth to calculate the area.

If the dimensions are measured in centimetres, the area is expressed in square centimetres.

---

## 9. Example 7 - Perimeter of a Rectangle

### Problem

Calculate the perimeter of a rectangle.

### Formula

```text
Perimeter = 2 × (Length + Breadth)
```

### Algorithm

1. Start.
2. Take the length.
3. Take the breadth.
4. Add length and breadth.
5. Multiply the sum by 2.
6. Display the perimeter.
7. Stop.

### Sample Input

```text
Length = 8
Breadth = 4
```

### Calculation

```text
Perimeter = 2 × (8 + 4)
Perimeter = 2 × 12
Perimeter = 24
```

### Python Code

```python
length = 8
breadth = 4

perimeter = 2 * (length + breadth)

print("Perimeter:", perimeter)
```

### Output

```text
Perimeter: 24
```

### Explanation

The perimeter is the total distance around the boundary of a rectangle.

The formula adds the length and breadth, then multiplies the result by two.

---

## 10. Example 8 - Celsius to Fahrenheit

### Problem

Convert a temperature from Celsius to Fahrenheit.

### Formula

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

### Algorithm

1. Start.
2. Obtain the temperature in Celsius.
3. Multiply the Celsius value by 9.
4. Divide the result by 5.
5. Add 32.
6. Display the Fahrenheit value.
7. Stop.

### Sample Input

```text
Celsius = 25
```

### Calculation

```text
Fahrenheit = (25 × 9 / 5) + 32
Fahrenheit = 45 + 32
Fahrenheit = 77
```

### Python Code

```python
celsius = 25

fahrenheit = (celsius * 9 / 5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
```

### Output

```text
Celsius: 25
Fahrenheit: 77.0
```

### Explanation

The algorithm applies the standard temperature conversion formula.

The order of operations is important, so use parentheses to make the calculation clear.

---

## 11. Example 9 - Swap Two Numbers

### Problem

Exchange the values stored in two variables.

Initially:

```text
A = 10
B = 20
```

After swapping:

```text
A = 20
B = 10
```

### Algorithm Using a Temporary Variable

1. Start.
2. Store A in a temporary variable.
3. Assign B to A.
4. Assign the temporary variable to B.
5. Display A and B.
6. Stop.

### Python Code

```python
a = 10
b = 20

temp = a
a = b
b = temp

print("A:", a)
print("B:", b)
```

### Output

```text
A: 20
B: 10
```

### Dry Run

| Step | Operation | A | B | Temp |
|---|---|---:|---:|---:|
| 1 | Initial values | 10 | 20 | — |
| 2 | `temp = a` | 10 | 20 | 10 |
| 3 | `a = b` | 20 | 20 | 10 |
| 4 | `b = temp` | 20 | 10 | 10 |

### Explanation

The temporary variable preserves the original value of A before A is overwritten.

Without saving that value, the original A could be lost.

Python also supports tuple assignment for swapping, but this example demonstrates the traditional algorithm using a temporary variable.

---

## 12. Example 10 - Find the Larger of Two Numbers

### Problem

Compare two numbers and display the larger one. If they are equal, display an appropriate message.

### Algorithm

1. Start.
2. Read two numbers A and B.
3. If A is greater than B, display A.
4. Otherwise, if B is greater than A, display B.
5. Otherwise, display that both numbers are equal.
6. Stop.

### Sample Values

```text
A = 45
B = 30
```

### Expected Output

```text
Larger number: 45
```

### Python Code

```python
a = 45
b = 30

if a > b:
    print("Larger number:", a)
elif b > a:
    print("Larger number:", b)
else:
    print("Both numbers are equal.")
```

### Explanation

- `if` checks the first condition.
- `elif` checks another condition if the preceding condition is false.
- `else` handles the case in which neither number is greater.

This example introduces basic decision-making in an algorithm.

---

## 13. Example 11 - Even or Odd

### Problem

Determine whether an integer is even or odd.

### Important Concept

An even integer is divisible by 2 with a remainder of 0.

An odd integer leaves a remainder of 1 when divided by 2.

The Python modulo operator `%` gives the remainder.

### Algorithm

1. Start.
2. Obtain an integer N.
3. Calculate the remainder when N is divided by 2.
4. If the remainder is 0, display Even.
5. Otherwise, display Odd.
6. Stop.

### Sample Input

```text
N = 17
```

### Calculation

```text
17 % 2 = 1
```

Because the remainder is not zero, the number is odd.

### Python Code

```python
number = 17

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")
```

### Output

```text
17 is Odd
```

### Another Example

For `number = 24`:

```text
24 % 2 = 0
```

Output:

```text
24 is Even
```

This algorithm works for positive, zero, and negative integers.

---

## 14. Example 12 - Square of a Number

### Problem

Calculate the square of a number.

### Formula

```text
Square = Number × Number
```

### Algorithm

1. Start.
2. Obtain a number.
3. Multiply the number by itself.
4. Display the square.
5. Stop.

### Sample Input

```text
Number = 9
```

### Calculation

```text
Square = 9 × 9
Square = 81
```

### Python Code

```python
number = 9

square = number * number

print("Square:", square)
```

### Output

```text
Square: 81
```

### Explanation

Squaring a number means multiplying it by itself.

For example:

```text
5² = 5 × 5 = 25
```

---

## 15. What Is a Dry Run?

A dry run means manually tracing the steps of an algorithm using sample values.

It helps us understand how an algorithm processes data and produces its result.

For example:

```python
a = 5
b = 3
total = a + b

print(total)
```

### Dry Run Table

| Step | Operation | A | B | Total |
|---|---|---:|---:|---:|
| 1 | Assign value to A | 5 | — | — |
| 2 | Assign value to B | 5 | 3 | — |
| 3 | Calculate A + B | 5 | 3 | 8 |
| 4 | Display Total | 5 | 3 | 8 |

Output:

```text
8
```

Dry runs are especially useful when learning algorithms, loops, conditions, and data structures.

---

## 16. Common Mistakes

### Mistake 1: Using the Wrong Formula

For the rectangle perimeter, the correct formula is:

```text
Perimeter = 2 × (Length + Breadth)
```

Do not confuse this with the area formula.

### Mistake 2: Performing Operations in the Wrong Order

The average requires adding the numbers first and then dividing by the count.

```python
average = (a + b + c) / 3
```

### Mistake 3: Overwriting a Value While Swapping

Store the original value in a temporary variable before changing either variable.

### Mistake 4: Ignoring Equal Numbers

When comparing two numbers, consider whether they could be equal. Do not assume that one must always be larger.

### Mistake 5: Forgetting Operator Meaning

- `*` performs multiplication.
- `/` performs division.
- `%` calculates the remainder.
- `>` checks whether one value is greater than another.
- `==` checks equality.

### Mistake 6: Not Testing the Expected Result

Use sample values to calculate the correct result manually, then compare it with the program's output.

---

## 17. Important Terminology

| Term | Meaning |
|---|---|
| Algorithm | Ordered instructions for solving a problem |
| Input | Information supplied to the solution |
| Processing | Operations performed on the input |
| Output | The result produced by the solution |
| Formula | Mathematical relationship used for a calculation |
| Variable | Name that refers to a value |
| Temporary variable | Variable used to preserve a value during an operation |
| Condition | Expression that evaluates to true or false |
| Remainder | Amount left after division |
| Dry run | Manually tracing an algorithm with sample values |
| Implementation | Converting the algorithm into program code |

---

## 18. Interview Questions

### Q1. What is an algorithm?

An algorithm is a finite sequence of clear and ordered steps used to solve a problem.

### Q2. How do you calculate the average of three numbers?

Add the numbers and divide their sum by 3.

```text
Average = (A + B + C) / 3
```

### Q3. What is the difference between area and perimeter?

Area measures the surface enclosed by a shape. Perimeter measures the total distance around its boundary.

### Q4. How can you swap two variables using a temporary variable?

Store the first value in a temporary variable, copy the second value to the first variable, and then copy the temporary value to the second variable.

### Q5. How do you find whether a number is even or odd?

Use the modulo operator:

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Q6. How can you compare two numbers?

Use comparison operators such as `>`, `<`, and `==`.

### Q7. What is a dry run?

It is the manual tracing of an algorithm with sample values to verify its steps and expected result.

### Q8. Why should an algorithm be written before coding?

It clarifies the logic, makes the implementation easier, and helps identify mistakes before writing code.

---

## 19. Practice Questions

Try to write each algorithm before implementing it in Python.

### Beginner Level

**Question 1:** Write an algorithm to calculate the sum of three numbers.

**Question 2:** Write an algorithm to calculate the difference and product of two numbers.

**Question 3:** Write an algorithm to calculate the square and cube of a number.

**Question 4:** Write an algorithm to convert kilometres into metres.

Formula:

```text
Metres = Kilometres × 1000
```

**Question 5:** Write an algorithm to calculate the area of a square.

Formula:

```text
Area = Side × Side
```

### Intermediate Level

**Question 6:** Write an algorithm to calculate the final price after applying a discount.

State the original price and discount percentage as inputs.

**Question 7:** Write an algorithm to compare two numbers and display the smaller number or report that they are equal.

**Question 8:** Write an algorithm to calculate the average of five numbers.

**Question 9:** Write an algorithm to swap two numbers without using a third variable.

**Question 10:** Write an algorithm to check whether a number is divisible by both 3 and 5.

### Challenge

Choose three practice questions and complete all the following tasks:

1. Write the algorithm in numbered steps.
2. Identify the input, processing, and output.
3. Perform a dry run with sample values.
4. Implement the solution in Python.
5. Verify that the program produces the expected result.

---

## 20. Learning Checklist

- [ ] Understand how to approach an algorithm example.
- [ ] Identify input, processing, and output.
- [ ] Write algorithms for arithmetic operations.
- [ ] Calculate an average using a formula.
- [ ] Calculate rectangle area and perimeter.
- [ ] Convert Celsius to Fahrenheit.
- [ ] Swap two values using a temporary variable.
- [ ] Compare two numbers.
- [ ] Check whether a number is even or odd.
- [ ] Calculate the square of a number.
- [ ] Perform a dry run.
- [ ] Implement algorithms in Python.
- [ ] Solve the practice questions.

---

## 21. What's Next?

Continue with:

**04 - Algorithm Characteristics**

In the next topic, learn about the properties of a good algorithm, including clarity, finiteness, definiteness, and correctness.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `03_algorithm_examples.py` | Practical Python implementations of basic algorithms |
| `README.md` | Detailed theory, algorithm steps, formulas, dry runs, interview questions, and practice problems |

---

## Conclusion

Algorithm examples help connect theoretical problem-solving steps to practical programming.

For every problem, understand the required input, identify the correct formula or logic, write clear steps, and test the solution with sample values.

Remember:

**Problem → Algorithm → Python Implementation → Testing**

Practise these examples carefully before progressing to algorithm characteristics and analysis.