# Input/Output Pseudocode

Welcome to **Input/Output Pseudocode**, the second topic in the Pseudocode section of Python Programming Fundamentals.

Input and output are fundamental parts of almost every program. A program accepts data, performs operations on that data, and displays the result.

In this topic, you will learn how to represent input, processing, and output in pseudocode and translate that logic into Python.

---

## 📌 About This Topic

- **Section:** Pseudocode and Problem Solving
- **Subsection:** Pseudocode
- **Topic:** Input/Output Pseudocode
- **Level:** Beginner
- **Programming Language:** Python

---

## 🎯 Learning Objectives

After completing this topic, you will be able to:

- Understand input, processing, and output.
- Write pseudocode for accepting data.
- Represent calculations and display results.
- Understand Python's `input()` and `print()` functions.
- Convert string input into numeric values.
- Accept multiple values in a single line.
- Translate input/output pseudocode into Python code.

---

## 1. What Is Input/Output?

**Input** is the information a program receives.

**Processing** means performing operations on the input, such as calculations or comparisons.

**Output** is the information displayed by the program.

### Basic Process

```text
INPUT → PROCESSING → OUTPUT
```

For example, when adding two numbers:

1. Accept the first number.
2. Accept the second number.
3. Calculate their sum.
4. Display the sum.

---

## 2. Basic Input/Output Instructions

| Pseudocode instruction | Purpose |
|---|---|
| `INPUT A` | Accept a value and store it in A |
| `SET SUM = A + B` | Calculate and store a result |
| `DISPLAY SUM` | Display the value of SUM |
| `START` | Mark the beginning of the solution |
| `END` | Mark the end of the solution |

These are conventions used in this repository. Pseudocode does not have one universally fixed syntax.

---

## 3. Input and Output in Python

### The `input()` function

Python's `input()` function reads a line of text entered by the user.

```python
name = input("Enter your name: ")
```

The entered value is stored in the variable `name` as a string.

### The `print()` function

Python's `print()` function displays information.

```python
print("Hello, Python!")
print("Your name is:", name)
```

### Type conversion

By default, `input()` returns a string. To perform numeric calculations, convert the input into an appropriate numeric type.

| Function | Purpose | Example |
|---|---|---|
| `int()` | Converts suitable input into an integer | `int(input())` |
| `float()` | Converts suitable input into a decimal number | `float(input())` |
| `str()` | Converts a value into a string | `str(100)` |

Example:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

Enter valid values in the expected format when running these beginner examples.

---

## 4. Example 1 — Input a Name and Display a Greeting

### Problem

Accept a person's name and display a greeting.

### Pseudocode

```text
START
    INPUT NAME
    DISPLAY "Hello", NAME
END
```

### Python Code

```python
name = input("Enter your name: ")
print("Hello,", name)
```

### Sample Output

```text
Enter your name: Amaan
Hello, Amaan
```

### Explanation

The program accepts a name and stores it in `name`. It then displays the greeting using the entered value.

---

## 5. Example 2 — Add Two Numbers

### Problem

Accept two integers and display their sum.

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
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

total = a + b

print("Sum:", total)
```

### Sample Output

```text
Enter the first number: 10
Enter the second number: 20
Sum: 30
```

### Dry Run

| Step | Operation | Result |
|---|---|---|
| 1 | Input A | A = 10 |
| 2 | Input B | B = 20 |
| 3 | Calculate A + B | 30 |
| 4 | Display the sum | 30 |

---

## 6. Example 3 — Average of Three Numbers

### Problem

Accept three numbers and calculate their average.

### Formula

Average = (A + B + C) / 3

### Pseudocode

```text
START
    INPUT A, B, C
    SET AVERAGE = (A + B + C) / 3
    DISPLAY AVERAGE
END
```

### Python Code

```python
a, b, c = map(
    float,
    input("Enter three numbers separated by spaces: ").split()
)

average = (a + b + c) / 3

print("Average:", average)
```

### Sample Output

```text
Enter three numbers separated by spaces: 10 20 30
Average: 20.0
```

### Understanding `split()` and `map()`

- `input()` reads the entire line.
- `.split()` separates the line into parts using whitespace by default.
- `map(float, ...)` converts each part into a floating-point number.
- The three converted values are assigned to `a`, `b`, and `c`.

Enter exactly three numbers separated by spaces for this example.

---

## 7. Example 4 — Area of a Rectangle

### Formula

Area = Length × Width

### Pseudocode

```text
START
    INPUT LENGTH
    INPUT WIDTH
    SET AREA = LENGTH * WIDTH
    DISPLAY AREA
END
```

### Python Code

```python
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of rectangle:", area)
```

### Sample Output

```text
Enter the length: 5
Enter the width: 4
Area of rectangle: 20.0
```

### Explanation

The program accepts the length and width, multiplies them, and displays the calculated area.

---

## 8. Example 5 — Celsius to Fahrenheit

### Formula

Fahrenheit = (Celsius × 9 / 5) + 32

### Pseudocode

```text
START
    INPUT CELSIUS
    SET FAHRENHEIT = (CELSIUS * 9 / 5) + 32
    DISPLAY FAHRENHEIT
END
```

### Python Code

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
```

### Sample Output

```text
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.0
```

---

## 9. Pseudocode vs Python Input/Output

| Task | Pseudocode | Python |
|---|---|---|
| Accept a value | `INPUT A` | `a = input()` |
| Display a value | `DISPLAY A` | `print(a)` |
| Calculate a sum | `SET SUM = A + B` | `total = a + b` |
| Accept an integer | `INPUT AGE` | `age = int(input())` |
| Accept a decimal | `INPUT PRICE` | `price = float(input())` |

Pseudocode describes the intended operations. Python implements them using valid Python syntax.

---

## 10. Common Mistakes

- Forgetting that `input()` returns a string.
- Performing arithmetic without converting suitable numeric input.
- Entering fewer or more values than an example expects.
- Using `*` incorrectly instead of `+` or another intended operator.
- Confusing the variable storing input with the value displayed as output.
- Writing the output step before calculating the result.
- Entering text where the program expects a number.

---

## 11. Practice Problems

For each question, first write pseudocode and then implement it in Python.

1. Accept a person's name and print a welcome message.
2. Accept two numbers and display their sum and difference.
3. Accept two integers and display their product.
4. Accept three numbers and calculate their average.
5. Accept the length and width of a rectangle and calculate its area.
6. Accept the side of a square and calculate its area.
7. Accept a temperature in Celsius and convert it to Fahrenheit.
8. Accept a distance in kilometres and convert it to metres.
9. Accept the prices of three products and calculate their total.
10. Accept a student's marks in five subjects and calculate the average.

---

## 12. Interview Questions

**Q1. What is input in programming?**  
Input is data received by a program for processing.

**Q2. What is output?**  
Output is the information produced or displayed by a program.

**Q3. What does Python's `input()` return?**  
It returns the entered line as a string.

**Q4. Why do we use `int()` or `float()` with input?**  
They convert suitable input strings into numeric values for calculations.

**Q5. What is the purpose of `print()`?**  
It displays values or messages.

**Q6. What are the three basic stages of many programs?**  
Input, processing, and output.

**Q7. What does `.split()` do?**  
It separates a string into parts, using whitespace by default.

**Q8. What is the purpose of `map()` in the multiple-input example?**  
It applies a conversion function to each separated input value.

---

## ✅ Completion Checklist

- [ ] Understand input, processing, and output.
- [ ] Learn the pseudocode instructions for input and output.
- [ ] Use `input()` and `print()` in Python.
- [ ] Understand `int()` and `float()`.
- [ ] Practise accepting multiple values in one line.
- [ ] Complete all five program examples.
- [ ] Solve the practice problems.
- [ ] Write pseudocode before implementing each solution.

---

## 🚀 Learning Outcome

After completing this topic, you should be able to design and implement basic input/output operations using pseudocode and Python.

You are now ready to move on to **Conditional Pseudocode**, where programs make decisions based on conditions.

**Remember: accept the input, process it correctly, and display the result.**
