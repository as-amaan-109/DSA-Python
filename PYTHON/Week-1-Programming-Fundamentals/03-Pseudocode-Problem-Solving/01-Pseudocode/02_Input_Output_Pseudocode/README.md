# Input/Output Pseudocode — Python

Welcome to **Input/Output Pseudocode**, the second topic in the Pseudocode section of the DSA-Python repository.

This topic focuses on representing input, processing, and output operations using clear, language-independent instructions. You will learn how to plan calculations, conversions, averages, bills, and other beginner-level programs before implementing them in Python.

---

## Table of Contents

1. [About This Topic](#about-this-topic)
2. [Learning Objectives](#learning-objectives)
3. [Input, Process, Output](#input-process-output)
4. [Pseudocode Keywords](#pseudocode-keywords)
5. [The IPO Model](#the-ipo-model)
6. [Worked Example: Sum of Two Numbers](#worked-example-sum-of-two-numbers)
7. [Worked Example: Rectangle Area](#worked-example-rectangle-area)
8. [Worked Example: Simple Interest](#worked-example-simple-interest)
9. [Reading Different Types of Input](#reading-different-types-of-input)
10. [Validation and Error Handling](#validation-and-error-handling)
11. [Dry Runs and Testing](#dry-runs-and-testing)
12. [Time and Space Complexity](#time-and-space-complexity)
13. [Folder Structure](#folder-structure)
14. [How to Run the Program](#how-to-run-the-program)
15. [Practice Questions](#practice-questions)
16. [Common Mistakes](#common-mistakes)
17. [Interview Questions](#interview-questions)
18. [Learning Checklist](#learning-checklist)

---

## About This Topic

Input and output are fundamental parts of most programming solutions.

- **Input:** The data supplied to an algorithm.
- **Process:** The calculations, comparisons, or operations performed on that data.
- **Output:** The result produced by the algorithm.

Pseudocode helps represent these steps without requiring the exact syntax of Python or another programming language.

For example, to add two values:

```text
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
END
```

The Python implementation would use `input()` to read values, `+` to add them, and `print()` to display the result.

## Learning Objectives

After completing this topic, you should be able to:

- Represent input operations using pseudocode.
- Represent calculations and assignments clearly.
- Represent output operations.
- Apply the Input–Process–Output model.
- Write pseudocode for arithmetic problems.
- Express formulas for averages, percentages, conversions, and interest.
- Handle invalid values through conditions.
- Use loops when a problem requires multiple inputs.
- Convert pseudocode into Python.
- Perform dry runs and test cases.
- Recognize basic time and auxiliary-space complexity.

---

## Input, Process, Output

### 1. Input

Input represents the values required by the algorithm.

Examples:

```text
INPUT NAME
INPUT A
INPUT B
INPUT LENGTH, WIDTH
```

An algorithm may receive one value, several values, or a collection of values.

### 2. Process

Processing represents an operation, formula, or calculation.

Examples:

```text
TOTAL <- A + B
AREA <- LENGTH * WIDTH
AVERAGE <- TOTAL / COUNT
DISCOUNT <- PRICE * RATE / 100
```

The symbol `<-` represents assignment in this topic's pseudocode convention.

### 3. Output

Output communicates the result.

Examples:

```text
OUTPUT TOTAL
OUTPUT AREA
OUTPUT AVERAGE
```

An algorithm may produce multiple outputs, such as both the calculated interest and the total amount.

### Complete example

```text
START
    INPUT LENGTH
    INPUT WIDTH

    AREA <- LENGTH * WIDTH
    PERIMETER <- 2 * (LENGTH + WIDTH)

    OUTPUT AREA
    OUTPUT PERIMETER
END
```

This algorithm reads two dimensions, calculates two results, and displays both.

---

## Pseudocode Keywords

The examples in this topic use the following conventions.

| Keyword | Meaning |
|---|---|
| `START` | Begin the algorithm |
| `END` | Finish the algorithm |
| `INPUT` | Read required data |
| `OUTPUT` | Display or return a result |
| `<-` | Assign a value to a variable |
| `IF` | Evaluate a condition |
| `ELSE` | Represent an alternative path |
| `ELSE IF` | Evaluate another condition |
| `END IF` | Close a conditional structure |
| `FOR` | Repeat over a range or sequence |
| `WHILE` | Repeat while a condition remains true |
| `END FOR` | Close a `FOR` loop |
| `END WHILE` | Close a `WHILE` loop |
| `DIV` | Integer division in this convention |
| `MOD` | Remainder after division |
| `AND` | Both conditions must be true |
| `OR` | At least one condition must be true |

Pseudocode is not governed by a single universal syntax. The important requirement is to write clear, consistent steps.

---

## The IPO Model

IPO stands for **Input, Process, Output**. It is a simple technique for planning a program.

### Example: Calculate average marks

**Problem:** Read marks for three subjects and calculate the average.

| Stage | Description |
|---|---|
| Input | Marks for subjects A, B, and C |
| Process | Add the marks and divide the total by 3 |
| Output | Total marks and average marks |

### Pseudocode

```text
START
    INPUT A, B, C

    TOTAL <- A + B + C
    AVERAGE <- TOTAL / 3

    OUTPUT TOTAL
    OUTPUT AVERAGE
END
```

### Why IPO is useful

The IPO model helps you identify missing information before coding. It also makes formulas easier to review because the inputs, operations, and outputs are separated.

Before writing a solution, ask:

1. What values are required?
2. What operation must be performed?
3. What result must be produced?
4. Are there any restrictions on the input?

---

## Worked Example: Sum of Two Numbers

**Problem:** Read two numbers and display their sum.

### Algorithm

1. Start.
2. Read A and B.
3. Calculate `TOTAL = A + B`.
4. Display TOTAL.
5. End.

### Pseudocode

```text
START
    INPUT A, B
    TOTAL <- A + B
    OUTPUT TOTAL
END
```

### Python implementation

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

total = a + b

print("Sum:", total)
```

### Dry run

Suppose A is 12 and B is 8.

| Step | Operation | Result |
|---|---|---:|
| 1 | Read A | 12 |
| 2 | Read B | 8 |
| 3 | Calculate A + B | 20 |
| 4 | Display TOTAL | 20 |

Expected output:

```text
Enter first integer: 12
Enter second integer: 8
Sum: 20
```

### Complexity

For fixed-size integer inputs:

- Time: `O(1)`.
- Auxiliary space: `O(1)`.

---

## Worked Example: Rectangle Area

**Problem:** Read length and width, then calculate the area and perimeter.

### Formulas

- `AREA = LENGTH × WIDTH`
- `PERIMETER = 2 × (LENGTH + WIDTH)`

### Pseudocode

```text
START
    INPUT LENGTH, WIDTH

    IF LENGTH < 0 OR WIDTH < 0 THEN
        OUTPUT "Invalid dimensions"
    ELSE
        AREA <- LENGTH * WIDTH
        PERIMETER <- 2 * (LENGTH + WIDTH)

        OUTPUT AREA
        OUTPUT PERIMETER
    END IF
END
```

### Python implementation

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

if length < 0 or width < 0:
    print("Dimensions cannot be negative.")
else:
    area = length * width
    perimeter = 2 * (length + width)

    print("Area:", area)
    print("Perimeter:", perimeter)
```

### Dry run

Assume:

- Length = 5
- Width = 3

Calculation:

- Area = `5 × 3 = 15`
- Perimeter = `2 × (5 + 3) = 16`

Expected results are area `15` square units and perimeter `16` units.

---

## Worked Example: Simple Interest

**Problem:** Read principal, annual interest rate, and time in years. Calculate simple interest and the total amount.

### Formulas

`Simple Interest = Principal × Rate × Time / 100`

`Total Amount = Principal + Simple Interest`

### Pseudocode

```text
START
    INPUT PRINCIPAL, RATE, TIME

    IF PRINCIPAL < 0 OR RATE < 0 OR TIME < 0 THEN
        OUTPUT "Invalid values"
    ELSE
        INTEREST <- PRINCIPAL * RATE * TIME / 100
        AMOUNT <- PRINCIPAL + INTEREST

        OUTPUT INTEREST
        OUTPUT AMOUNT
    END IF
END
```

### Python implementation

```python
principal = float(input("Enter principal: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time in years: "))

if principal < 0 or rate < 0 or time < 0:
    print("Values cannot be negative.")
else:
    interest = principal * rate * time / 100
    amount = principal + interest

    print("Interest:", round(interest, 2))
    print("Total amount:", round(amount, 2))
```

### Dry run

Suppose:

- Principal = 1,000
- Rate = 5%
- Time = 2 years

`INTEREST = 1000 × 5 × 2 / 100 = 100`

`AMOUNT = 1000 + 100 = 1100`

The result is interest of `100` and a total amount of `1100`.

---

## Reading Different Types of Input

The required data type depends on the problem.

### Text input

```text
INPUT NAME
OUTPUT NAME
```

Python:

```python
name = input("Enter your name: ").strip()
print("Name:", name)
```

### Integer input

```text
INPUT AGE
```

Python:

```python
age = int(input("Enter age: "))
```

### Decimal input

```text
INPUT PRICE
```

Python:

```python
price = float(input("Enter price: "))
```

In Python, `input()` returns a string. The program converts that string into an integer or decimal value when required.

### Multiple inputs

Pseudocode:

```text
INPUT A, B, C
TOTAL <- A + B + C
OUTPUT TOTAL
```

Python:

```python
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

print("Total:", a + b + c)
```

---

## Validation and Error Handling

Input validation checks whether supplied values meet the problem's requirements.

For example, dividing by zero is not allowed in ordinary numeric division.

### Pseudocode

```text
START
    INPUT A, B

    IF B = 0 THEN
        OUTPUT "Division by zero is not allowed"
    ELSE
        RESULT <- A / B
        OUTPUT RESULT
    END IF
END
```

### Python implementation

```python
a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))

if b == 0:
    print("Division by zero is not allowed.")
else:
    print("Result:", a / b)
```

### Common validation examples

| Input | Validation rule |
|---|---|
| Rectangle dimensions | Values must not be negative |
| Percentage | Value must be between 0 and 100 |
| Quantity | Usually a non-negative integer |
| Time used as a divisor | Must be greater than zero |
| Number of inputs | Must be positive when at least one value is required |

The validation rules should reflect the requirements of the specific problem rather than being added without a reason.

---

## Dry Runs and Testing

A dry run manually follows the pseudocode using known input values.

It helps verify that the operations are performed in the correct order.

### Example: Convert seconds

Suppose the input is `3671` seconds.

| Step | Calculation | Result |
|---|---|---:|
| 1 | `3671 DIV 3600` | 1 hour |
| 2 | `3671 MOD 3600` | 71 seconds remaining |
| 3 | `71 DIV 60` | 1 minute |
| 4 | `71 MOD 60` | 11 seconds |

The output is 1 hour, 1 minute, and 11 seconds.

### Useful test cases

| Problem | Suggested tests |
|---|---|
| Addition | Positive values, zero, negative values |
| Average | Equal values, mixed values, decimal values |
| Rectangle area | Positive dimensions, zero dimensions, negative input |
| Simple interest | Zero rate, zero time, negative input |
| Quotient/remainder | Divisible values, negative integers, divisor zero |
| Temperature conversion | Celsius 0, Celsius 100, negative temperature |
| Seconds conversion | 0, 59, 60, 3600, 3671 |

Testing varied inputs helps verify that the pseudocode and its Python implementation agree.

---

## Time and Space Complexity

For fixed-size arithmetic operations, the time complexity is usually `O(1)` under the standard introductory model.

| Algorithm | Typical time complexity | Typical auxiliary space |
|---|---:|---:|
| Add two numbers | `O(1)` | `O(1)` |
| Rectangle area and perimeter | `O(1)` | `O(1)` |
| Convert a fixed numeric value | `O(1)` | `O(1)` |
| Read and sum N values | `O(N)` | `O(1)` when using a running total |
| Read and store N values | `O(N)` | `O(N)` |
| Calculate a fixed five-subject total | `O(1)` | `O(1)` |

The analysis assumes a simplified model where basic arithmetic on the numeric values is treated as constant-time. Very large values can require more computation.

---

## Folder Structure

```text
02_Input_Output_Pseudocode/
│
├── README.md
└── 02_input_output_pseudocode.py
```

The Python file contains examples and practice programs. This README provides the theory, pseudocode conventions, worked calculations, validation guidance, and testing approach.

---

## How to Run the Program

Open PowerShell in the root directory of the `DSA-Python` repository.

Run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\03-Pseudocode-Problem-Solving\01-Pseudocode\02_Input_Output_Pseudocode\02_input_output_pseudocode.py"
```

The interactive menu provides:

1. Run examples.
2. Run solved practice questions.
3. Show unsolved practice questions.
0. Exit.

Select an option and enter the requested values. Select `0` in a sub-menu to return to the main menu.

If `python` is not recognized, verify that Python is installed and available on your PATH. On Windows, the `py` command may work instead.

---

## Practice Questions

The Python file contains 12 examples, 12 solved questions, and 5 unsolved questions.

### 12 Examples

1. Read and display a name.
2. Add two numbers.
3. Perform basic arithmetic operations.
4. Calculate rectangle area.
5. Calculate the average of three numbers.
6. Calculate quotient and remainder.
7. Convert Celsius to Fahrenheit.
8. Calculate simple interest.
9. Calculate marks and percentage.
10. Convert seconds into hours, minutes, and seconds.
11. Calculate a bill with tax.
12. Calculate average speed.

### 12 Solved Questions

1. Square area and perimeter.
2. Circle area and circumference.
3. Swap two numbers.
4. Convert kilometres to miles.
5. Calculate gross salary using allowance percentages.
6. Calculate a discounted price.
7. Convert Fahrenheit to Celsius.
8. Convert minutes into hours and remaining minutes.
9. Calculate the average of N numbers.
10. Convert days into weeks and remaining days.
11. Calculate total and average marks.
12. Perform division with divisor validation.

### 5 Unsolved Questions

1. Calculate a shopping bill with quantity, discount, and tax.
2. Find the minimum, maximum, and average of N values.
3. Convert seconds into days, hours, minutes, and seconds.
4. Calculate a multi-product bill using prices and quantities.
5. Calculate a student's total, percentage, and grade for a user-defined number of subjects.

For every question, identify the inputs, describe the processing, define the output, write pseudocode, dry-run the steps, and then implement the solution.

---

## Common Mistakes

- Forgetting that Python's `input()` returns text.
- Using a formula without understanding its assumptions.
- Placing output before the relevant calculation.
- Using the wrong data type.
- Forgetting to validate inputs with restricted ranges.
- Dividing by zero.
- Confusing integer division with regular division.
- Forgetting units when interpreting results.
- Writing pseudocode that is too vague to implement.
- Testing only one input.
- Writing pseudocode and Python code that represent different logic.

---

## Interview Questions

**1. What is input in programming?**

Input is data supplied to an algorithm for processing.

**2. What is output?**

Output is the information or result produced by an algorithm.

**3. What is the IPO model?**

IPO stands for Input, Process, Output.

**4. Why is the IPO model useful?**

It helps clarify which data is needed, what operations must be performed, and what result should be produced.

**5. What does the `INPUT` keyword mean in pseudocode?**

It represents receiving data required by the algorithm.

**6. What does `<-` represent?**

It represents assignment in the pseudocode convention used in this topic.

**7. What is the difference between integer and decimal input?**

Integer input represents whole-number values, while decimal input can represent fractional values.

**8. Why is input validation necessary?**

It checks that values satisfy the problem's requirements before processing them.

**9. What is a dry run?**

A dry run manually traces an algorithm with sample values.

**10. What is the difference between pseudocode and Python?**

Pseudocode describes the algorithm's logic, while Python code follows executable Python syntax.

**11. How should division by zero be handled?**

The algorithm should check whether the denominator is zero and handle that case before attempting division.

**12. What is the purpose of time-complexity analysis?**

It helps estimate how an algorithm's work grows as the input size increases.

---

## Learning Checklist

- [ ] I understand input, processing, and output.
- [ ] I can use the IPO model.
- [ ] I understand common pseudocode keywords.
- [ ] I can write pseudocode for arithmetic calculations.
- [ ] I can represent formulas and assignments clearly.
- [ ] I can handle multiple inputs.
- [ ] I understand input validation.
- [ ] I can perform a dry run.
- [ ] I can translate pseudocode into Python.
- [ ] I have run all examples.
- [ ] I have studied all solved questions.
- [ ] I have attempted all five unsolved questions.

---

## Next Topic

After completing Input/Output Pseudocode, continue to **Conditional Pseudocode**, where you will practise expressing decisions, comparisons, and alternative outcomes using structured pseudocode.
