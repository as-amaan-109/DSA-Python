# Input and Output Flowcharts

> **Week:** 01 - Programming Fundamentals  
> **Section:** Algorithms and Flowcharts  
> **Topic:** Input and Output Flowcharts  
> **Level:** Beginner  
> **Goal:** Understand how input, processing, and output operations are represented using flowcharts and implemented in Python.

---

## Table of Contents

1. Introduction
2. What Is Input?
3. What Is Output?
4. The Input/Output Flowchart Symbol
5. Understanding Input, Process, and Output
6. Example 1 - Display a Message
7. Example 2 - Take a Name as Input
8. Example 3 - Double a Number
9. Example 4 - Add Two Numbers
10. Example 5 - Read Multiple Values
11. Example 6 - Calculate an Average
12. Example 7 - Area of a Rectangle
13. Example 8 - Celsius to Fahrenheit
14. Python `input()` and `print()`
15. Type Conversion
16. Dry Run
17. Rules for Input/Output Flowcharts
18. Common Beginner Mistakes
19. Important Terminology
20. Interview Questions
21. Practice Questions
22. Learning Checklist
23. What's Next?

---

## 1. Introduction

Input and output are fundamental operations in programming.

**Input** provides data to a program, while **output** presents the result produced by the program.

A flowchart helps us represent these operations visually using standard symbols.

For example, a program that adds two numbers needs to:

1. Read the first number.
2. Read the second number.
3. Calculate their sum.
4. Display the result.

The corresponding flowchart connects these steps in the correct order.

---

## 2. What Is Input?

Input is the information supplied to a program or algorithm.

Input may come from:

- A user entering information through a keyboard.
- A file.
- A database.
- Another program or service.
- A sensor or other device.

In beginner Python programs, input is often provided through the `input()` function.

### Example

```python
name = input("Enter your name: ")
```

If the user enters:

```text
Amaan
```

The variable `name` stores the text `"Amaan"`.

### Flowchart Representation

An input operation is commonly represented using a parallelogram.

```text
     ( START )
         |
         v
    / Read Name /
         |
         v
      ( STOP )
```

This simple flowchart represents a program that receives a name.

---

## 3. What Is Output?

Output is the information produced by a program or algorithm.

Examples include:

- Displaying a message.
- Showing the result of a calculation.
- Printing a student's details.
- Writing information to a file.

In Python, the `print()` function is commonly used to display output.

### Example

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

### Flowchart Representation

Output is also commonly represented using a parallelogram.

```text
     ( START )
         |
         v
 / Display Hello /
         |
         v
      ( STOP )
```

**Important:** Input and output commonly use the same flowchart symbol, although the instruction inside the symbol identifies the operation.

---

## 4. The Input/Output Flowchart Symbol

### Shape

Parallelogram.

### Purpose

The parallelogram represents an input or output operation.

### Input examples

```text
Read A
```

```text
Read Name
```

```text
Read Length and Breadth
```

### Output examples

```text
Display SUM
```

```text
Print Area
```

```text
Display Student Details
```

### Example: Addition

```text
       ( START )
           |
           v
    / Read A and B /
           |
           v
     [ SUM = A + B ]
           |
           v
      / Display SUM /
           |
           v
        ( STOP )
```

In this diagram:

- `START` uses a terminator.
- Reading A and B uses an input/output symbol.
- Calculating SUM uses a process rectangle.
- Displaying SUM uses an input/output symbol.
- `STOP` uses a terminator.

---

## 5. Understanding Input, Process, and Output

A basic computational problem can often be divided into three parts.

### 5.1 Input

Receive the values required for the task.

Example:

```text
A = 10
B = 20
```

### 5.2 Process

Perform the required operation.

Example:

```text
SUM = A + B
SUM = 10 + 20
SUM = 30
```

### 5.3 Output

Display or return the result.

Example:

```text
Sum = 30
```

### Combined Flowchart

```text
       ( START )
           |
           v
    / Read A and B /
           |
           v
      [ SUM = A + B ]
           |
           v
      / Display SUM /
           |
           v
        ( STOP )
```

### Why Is This Structure Important?

It helps us separate the data a problem needs, the operation performed on that data, and the result produced.

This makes programs easier to design and understand.

---

## 6. Example 1 - Display a Message

### Problem

Display the message `Hello, Python!`.

### Algorithm

1. Start.
2. Display `Hello, Python!`.
3. Stop.

### Flowchart

```text
       ( START )
           |
           v
 / Display Hello, Python! /
           |
           v
        ( STOP )
```

### Python Code

```python
print("Hello, Python!")
```

### Output

```text
Hello, Python!
```

### Explanation

No external input is required because the message is already specified in the program.

The output operation displays the message.

---

## 7. Example 2 - Take a Name as Input

### Problem

Ask the user for a name and display a welcome message.

### Algorithm

1. Start.
2. Read the name.
3. Display a welcome message containing the name.
4. Stop.

### Flowchart

```text
       ( START )
           |
           v
     / Read Name /
           |
           v
 / Display Welcome Message /
           |
           v
        ( STOP )
```

### Python Code

```python
name = input("Enter your name: ")

print("Welcome,", name)
```

### Sample Input

```text
Enter your name: Amaan
```

### Output

```text
Welcome, Amaan
```

### Explanation

The `input()` function reads the text entered by the user.

The value is stored in the variable `name`.

The `print()` function then displays the welcome message.

---

## 8. Example 3 - Double a Number

### Problem

Read an integer and display twice its value.

### Formula

```text
Double = Number × 2
```

### Algorithm

1. Start.
2. Read an integer N.
3. Calculate `DOUBLE = N × 2`.
4. Display DOUBLE.
5. Stop.

### Flowchart

```text
       ( START )
           |
           v
      / Read N /
           |
           v
    [ DOUBLE = N * 2 ]
           |
           v
    / Display DOUBLE /
           |
           v
        ( STOP )
```

### Python Code

```python
number = int(input("Enter an integer: "))

double = number * 2

print("Double:", double)
```

### Sample Input

```text
Enter an integer: 7
```

### Output

```text
Double: 14
```

### Explanation

`input()` initially returns a string, so `int()` converts the value into an integer before multiplication.

---

## 9. Example 4 - Add Two Numbers

### Problem

Read two integers and display their sum.

### Algorithm

1. Start.
2. Read A.
3. Read B.
4. Calculate `SUM = A + B`.
5. Display SUM.
6. Stop.

### Flowchart

```text
        ( START )
            |
            v
     / Read A and B /
            |
            v
       [ SUM = A + B ]
            |
            v
       / Display SUM /
            |
            v
         ( STOP )
```

### Python Code

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Sample Input

```text
Enter the first number: 10
Enter the second number: 20
```

### Output

```text
Sum: 30
```

### Dry Run

| Step | Operation | A | B | SUM |
|---|---|---:|---:|---:|
| 1 | Read A | 10 | — | — |
| 2 | Read B | 10 | 20 | — |
| 3 | Calculate A + B | 10 | 20 | 30 |
| 4 | Display SUM | 10 | 20 | 30 |

---

## 10. Example 5 - Read Multiple Values

Sometimes we want a user to enter several values in a single line.

Python's `split()` method separates a string into parts using whitespace by default.

### Example

```python
a, b, c = map(
    int,
    input("Enter three integers: ").split()
)

total = a + b + c

print("Total:", total)
```

### Sample Input

```text
Enter three integers: 10 20 30
```

### Output

```text
Total: 60
```

### Explanation

The statement performs three operations:

1. `input()` reads a line of text.
2. `split()` separates the text into parts.
3. `map(int, ...)` converts the parts into integers.

The values are assigned to `a`, `b`, and `c`.

### Flowchart

```text
        ( START )
            |
            v
    / Read A, B, and C /
            |
            v
    [ TOTAL = A + B + C ]
            |
            v
      / Display TOTAL /
            |
            v
         ( STOP )
```

**Note:** The user must enter the expected number of valid integers. More advanced input validation can be added later.

---

## 11. Example 6 - Calculate an Average

### Problem

Read three numbers and calculate their average.

### Formula

```text
Average = (A + B + C) / 3
```

### Algorithm

1. Start.
2. Read A, B, and C.
3. Calculate `TOTAL = A + B + C`.
4. Calculate `AVERAGE = TOTAL / 3`.
5. Display AVERAGE.
6. Stop.

### Flowchart

```text
         ( START )
             |
             v
     / Read A, B, C /
             |
             v
    [ AVG = (A+B+C)/3 ]
             |
             v
       / Display AVG /
             |
             v
          ( STOP )
```

### Python Code

```python
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

average = (a + b + c) / 3

print("Average:", average)
```

### Sample Input

```text
Enter the first number: 10
Enter the second number: 20
Enter the third number: 30
```

### Output

```text
Average: 20.0
```

### Explanation

`float()` allows the program to accept integers as well as decimal values.

The calculation is completed before the average is displayed.

---

## 12. Example 7 - Area of a Rectangle

### Problem

Read the length and breadth of a rectangle and display the area.

### Formula

```text
Area = Length × Breadth
```

### Algorithm

1. Start.
2. Read LENGTH.
3. Read BREADTH.
4. Calculate `AREA = LENGTH × BREADTH`.
5. Display AREA.
6. Stop.

### Flowchart

```text
              ( START )
                  |
                  v
     / Read Length and Breadth /
                  |
                  v
     [ AREA = LENGTH * BREADTH ]
                  |
                  v
            / Display AREA /
                  |
                  v
               ( STOP )
```

### Python Code

```python
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

area = length * breadth

print("Area:", area)
```

### Sample Input

```text
Enter the length: 8
Enter the breadth: 4
```

### Output

```text
Area: 32.0
```

---

## 13. Example 8 - Celsius to Fahrenheit

### Problem

Read a temperature in Celsius and convert it into Fahrenheit.

### Formula

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

### Algorithm

1. Start.
2. Read the Celsius temperature.
3. Apply the conversion formula.
4. Display the Fahrenheit value.
5. Stop.

### Flowchart

```text
         ( START )
             |
             v
     / Read Celsius /
             |
             v
 [ F = (C * 9 / 5) + 32 ]
             |
             v
    / Display Fahrenheit /
             |
             v
          ( STOP )
```

### Python Code

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)
```

### Sample Input

```text
Enter temperature in Celsius: 25
```

### Output

```text
Fahrenheit: 77.0
```

---

## 14. Python `input()` and `print()`

### The `input()` Function

`input()` reads a line of text from the user.

Example:

```python
name = input("Enter your name: ")
```

The optional prompt is displayed before Python waits for input.

### The `print()` Function

`print()` displays values.

Example:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

### Important Difference

`input()` receives information, while `print()` displays information.

| Function | Purpose |
|---|---|
| `input()` | Reads user input as text |
| `print()` | Displays values or messages |
| `int()` | Converts suitable input text into an integer |
| `float()` | Converts suitable input text into a floating-point number |
| `split()` | Separates a string into parts |

---

## 15. Type Conversion

### What Is Type Conversion?

Type conversion means converting a value from one data type into another.

This is important because `input()` returns a string.

### Example: Without Conversion

```python
a = input("Enter the first number: ")
b = input("Enter the second number: ")

print(a + b)
```

If the user enters `10` and `20`, the output is:

```text
1020
```

Python concatenates the two strings instead of performing numeric addition.

### Correct Addition Using `int()`

```python
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(a + b)
```

For the same input, the output is:

```text
30
```

### When to Use `int()` and `float()`

- Use `int()` when the input must be an integer.
- Use `float()` when decimal values may be supplied.

The input must contain text that can be converted to the requested type. Otherwise, Python raises a `ValueError`.

---

## 16. Dry Run

A dry run means tracing an algorithm manually with sample values.

Consider the addition example.

Input:

```text
A = 10
B = 20
```

### Dry-Run Table

| Step | Operation | A | B | SUM |
|---|---|---:|---:|---:|
| 1 | Read A | 10 | — | — |
| 2 | Read B | 10 | 20 | — |
| 3 | Calculate SUM | 10 | 20 | 30 |
| 4 | Display SUM | 10 | 20 | 30 |

Expected output:

```text
Sum: 30
```

A dry run helps us verify that the sequence of input, processing, and output operations is correct.

---

## 17. Rules for Input/Output Flowcharts

1. Use a terminator to represent the start and end of the process.
2. Use a parallelogram for input operations.
3. Use a parallelogram for output operations.
4. Use a rectangle for calculations and assignments.
5. Connect the symbols using arrows.
6. Arrange operations in a logical sequence.
7. Label each operation clearly.
8. Ensure that all required inputs are collected before they are processed.
9. Display or return the intended result.
10. Test the flowchart using sample values.

For example, an addition flowchart should read both numbers before calculating their sum.

---

## 18. Common Beginner Mistakes

### Mistake 1: Forgetting That Input Is Text

Incorrect:

```python
a = input("Enter a number: ")
```

If a calculation requires a numeric value, convert the input appropriately.

Correct:

```python
a = int(input("Enter a number: "))
```

### Mistake 2: Using the Wrong Flowchart Symbol

Use a parallelogram for input/output and a rectangle for processing.

### Mistake 3: Missing a Processing Step

A flowchart that reads two values but never specifies their addition is incomplete for a sum problem.

### Mistake 4: Incorrect Formula

Always verify the formula before writing the corresponding process symbol.

### Mistake 5: Entering Values in the Wrong Format

If a program expects three space-separated integers, enter:

```text
10 20 30
```

rather than a single number or an unexpected format.

### Mistake 6: Confusing Output with Input

The instruction `Read A` represents input, whereas `Display A` represents output.

---

## 19. Important Terminology

| Term | Meaning |
|---|---|
| Input | Data provided to an algorithm |
| Output | Information produced by an algorithm |
| Process | A calculation or operation |
| Parallelogram | Common input/output flowchart symbol |
| Terminator | Symbol representing start or stop |
| Flow line | Arrow showing the direction of execution |
| `input()` | Python function used to read a line of text |
| `print()` | Python function used to display values |
| Type conversion | Converting a value into another data type |
| Dry run | Manually tracing an algorithm |
| `split()` | Separating a string into parts |
| `int()` | Converting suitable input text into an integer |
| `float()` | Converting suitable input text into a floating-point value |

---

## 20. Interview Questions

### Q1. What is an input/output flowchart?

It is a flowchart that represents how a process receives data and produces results using standard symbols.

### Q2. Which shape represents input and output?

A parallelogram is commonly used.

### Q3. What is the difference between input and output?

Input supplies information to a process. Output presents the result of that process.

### Q4. Which Python function reads user input?

The `input()` function.

### Q5. Which Python function displays output?

The `print()` function.

### Q6. What does `input()` return?

It returns a string containing the line entered by the user, without the trailing newline character.

### Q7. Why is `int()` used with `input()`?

Because arithmetic operations may require an integer, while `input()` returns a string.

### Q8. What is the purpose of a process symbol?

A rectangle represents an operation, calculation, or assignment.

### Q9. What are input, processing, and output?

They are the three stages of many computational tasks: receiving data, transforming it, and producing a result.

### Q10. Why is a dry run useful?

It helps verify the expected behavior and identify missing or incorrectly ordered steps before executing a program.

---

## 21. Practice Questions

Try drawing the flowchart first, then write the Python program.

### Beginner Level

**Question 1:** Take a name as input and display a welcome message.

**Question 2:** Take two integers and display their sum.

**Question 3:** Take two numbers and display their difference.

**Question 4:** Take a number and display its double.

**Question 5:** Take a number and display its square.

### Intermediate Level

**Question 6:** Take three numbers and calculate their average.

**Question 7:** Take the length and breadth of a rectangle and calculate its area.

**Question 8:** Take a Celsius temperature and convert it into Fahrenheit.

**Question 9:** Take three integers on one line and calculate their sum.

**Question 10:** Take a product's price and quantity and calculate the total price.

### Challenge

Choose any two questions and complete these tasks:

1. Write the algorithm.
2. Draw the input/output flowchart.
3. Implement the algorithm in Python.
4. Test the program with sample values.
5. Compare the output against a manually calculated result.

---

## 22. Learning Checklist

- [ ] Understand what input means.
- [ ] Understand what output means.
- [ ] Identify the input/output symbol.
- [ ] Identify the process symbol.
- [ ] Use `input()` to receive data.
- [ ] Use `print()` to display results.
- [ ] Convert input into numeric types.
- [ ] Read multiple values on one line.
- [ ] Write flowcharts for simple calculations.
- [ ] Perform a dry run.
- [ ] Identify common input/output mistakes.
- [ ] Solve the practice questions.

---

## 23. What's Next?

Continue with:

**03 - Decision Flowchart**

The next topic will explain how a flowchart represents conditions and different execution paths.

---

## Files in This Folder

| File | Purpose |
|---|---|
| `02_input_output_flowchart.py` | Practical input/output programs with corresponding flowchart steps |
| `README.md` | Detailed theory, diagrams, code examples, dry runs, interview questions, and practice problems |

---

## Conclusion

Input and output are essential components of most beginner programming problems.

Flowcharts help represent when data is received, how it is processed, and how the result is produced.

Remember:

**Start → Input → Process → Output → Stop**

Learn the symbols, practise drawing the diagrams, and implement each example in Python to strengthen your understanding.