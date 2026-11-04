# Integer (`int`) Data Type in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Data Types  
**Topic:** Integer (`int`)  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. What Is an Integer?
4. Creating Integer Variables
5. Positive Integers, Negative Integers, and Zero
6. Checking the Data Type with `type()`
7. Arithmetic Operators
8. Division, Floor Division, and Modulo
9. Integer Exponentiation
10. Updating Integers with Assignment Operators
11. Converting Values to Integers
12. Boolean Values and Integers
13. Large Integers in Python
14. Integer Comparisons
15. Extracting Digits from an Integer
16. Dry Run: Sum of Digits
17. Explanation of the 12 Guided Examples
18. Explanation of the 12 Solved Problems
19. Five Unsolved Practice Questions
20. Testing and Edge Cases
21. Time and Space Complexity
22. Common Mistakes
23. Best Practices
24. Frequently Asked Questions
25. How to Run the Program
26. Folder Structure
27. Revision Checklist

---

# 1. Introduction

Python provides several built-in data types for representing different kinds of information. The integer type, written as `int`, is used to represent whole numbers.

Examples include:

```python
age = 20
temperature = -5
student_count = 0
total_marks = 450
```

Integers are useful for counting, indexing, arithmetic calculations, digit processing, number comparisons, and many algorithmic problems.

The `int` type is one of the first data types to learn because it appears throughout beginner programming and Data Structures and Algorithms (DSA).

This topic introduces integer values, arithmetic operators, floor division, modulo, conversions, digit manipulation, and practical problems.

# 2. Learning Objectives

After completing this topic, you should be able to:

- Explain what an integer is.
- Create positive, negative, and zero-valued integers.
- Check a value's data type using `type()`.
- Perform integer arithmetic.
- Understand division, floor division, and modulo.
- Calculate integer powers.
- Update an integer variable using compound assignment.
- Convert valid input text into an integer.
- Recognize the relationship between Boolean values and integers.
- Understand Python's support for large integers.
- Extract and process integer digits.
- Solve basic number-related problems.
- Test algorithms using normal and boundary cases.
- Identify common integer-related programming errors.

# 3. What Is an Integer?

An integer is a whole number without a fractional component.

Examples:

```text
0
1
25
-7
1000
-250
```

In Python, these values have the built-in type `int`.

```python
first_number = 10
second_number = -25
third_number = 0

print(type(first_number))
print(type(second_number))
print(type(third_number))
```

Output:

```text
<class 'int'>
<class 'int'>
<class 'int'>
```

Unlike a floating-point value such as `10.5`, an integer represents a whole-number value.

### Important Distinction

```python
whole_number = 10
decimal_number = 10.0

print(type(whole_number).__name__)
print(type(decimal_number).__name__)
```

Output:

```text
int
float
```

Although both values are numerically equal, they have different data types.

The integer type is suitable when a problem works with whole numbers, such as counts, indices, or integer arithmetic.

# 4. Creating Integer Variables

You can create an integer by assigning an integer literal to a variable.

```python
age = 20
marks = 85
balance_change = -100
count = 0
```

Python determines the type from the value assigned.

### Using Integer Values in Calculations

```python
first_number = 12
second_number = 8

total = first_number + second_number
difference = first_number - second_number
product = first_number * second_number

print(total)
print(difference)
print(product)
```

Output:

```text
20
4
96
```

### Integer Values from User Input

The `input()` function returns text. Use `int()` to convert suitable text to an integer.

```python
age = int(input("Enter your age: "))
print(age)
```

If the user enters `20`, the conversion produces the integer `20`.

If the user enters text that does not represent a valid integer, such as `hello` or `12.5`, `int()` raises a `ValueError`.

Input validation is therefore important when programs accept user-entered values.

# 5. Positive Integers, Negative Integers, and Zero

Python integers can be positive, negative, or zero.

## Positive Integers

Positive integers are greater than zero.

Examples:

```python
age = 20
count = 5
temperature_change = 12
```

## Negative Integers

Negative integers are less than zero.

Examples:

```python
temperature_change = -5
balance_adjustment = -200
movement = -10
```

## Zero

Zero is neither positive nor negative.

Example:

```python
number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Output:

```text
Zero
```

### Why Does This Matter?

Algorithms that classify numbers, process digits, or calculate absolute values often need to handle all three cases.

Do not assume that every integer input is positive unless the problem specifically states that restriction.

# 6. Checking the Data Type with `type()`

Python's built-in `type()` function reports the type of an object.

Example:

```python
first_number = 25
second_number = -8

print(type(first_number))
print(type(second_number))
```

Output:

```text
<class 'int'>
<class 'int'>
```

To display only the type name:

```python
number = 100

print(type(number).__name__)
```

Output:

```text
int
```

### Comparing Integer and Float Types

```python
a = 10
b = 10.0

print(type(a).__name__)
print(type(b).__name__)
```

Output:

```text
int
float
```

Checking types is helpful when learning Python and debugging unexpected calculations.

For general numeric input, remember that integers and floating-point values behave differently in operations such as division.

# 7. Arithmetic Operators

Python supports standard arithmetic operators for integers.

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor division | `17 // 5` | 3 |
| `%` | Modulo or remainder | `17 % 5` | 2 |
| `**` | Exponentiation | `2 ** 5` | 32 |

### Addition

```python
a = 10
b = 5

total = a + b
print(total)
```

Output:

```text
15
```

### Subtraction

```python
difference = 10 - 5
print(difference)
```

Output:

```text
5
```

### Multiplication

```python
product = 10 * 5
print(product)
```

Output:

```text
50
```

### Division

```python
result = 10 / 4

print(result)
print(type(result).__name__)
```

Output:

```text
2.5
float
```

The `/` operator returns a floating-point result for ordinary numeric division, including when both operands are integers.

### Exponentiation

```python
result = 2 ** 5
print(result)
```

Output:

```text
32
```

The `**` operator raises the left operand to the power of the right operand.

# 8. Division, Floor Division, and Modulo

These three operators are particularly important for integer-based algorithms.

## 8.1 True Division `/`

True division calculates a quotient.

```python
print(17 / 5)
```

Output:

```text
3.4
```

The result is a floating-point value.

## 8.2 Floor Division `//`

Floor division rounds the quotient down toward negative infinity.

```python
print(17 // 5)
print(-17 // 5)
```

Output:

```text
3
-4
```

Notice that `-17 // 5` produces `-4`, not `-3`. This is because floor division rounds toward negative infinity.

For non-negative integers, floor division by a positive integer is useful for calculating whole units.

## 8.3 Modulo `%`

The modulo operator returns a remainder consistent with Python's floor-division rules.

```python
print(17 % 5)
print(-17 % 5)
```

Output:

```text
2
3
```

The quotient and remainder satisfy the relationship:

\[
a = (a // b) \times b + (a \% b)
\]

for a non-zero divisor \(b\).

### Example: Even or Odd

```python
number = 14

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

If an integer's remainder after division by `2` is zero, it is even. Otherwise, it is odd.

### Example: Extract the Last Digit

```python
number = 528

last_digit = number % 10

print(last_digit)
```

Output:

```text
8
```

Modulo and floor division are frequently used in digit-processing algorithms.

# 9. Integer Exponentiation

Exponentiation uses the `**` operator.

```python
base = 3
exponent = 4

result = base ** exponent

print(result)
```

Output:

```text
81
```

The calculation is:

\[
3^4 = 3 \times 3 \times 3 \times 3 = 81
\]

### Common Uses

- Calculating squares and cubes.
- Working with mathematical formulas.
- Generating powers in algorithms.
- Calculating compound interest.
- Solving number-related programming problems.

### Square and Cube

```python
number = 5

square = number ** 2
cube = number ** 3

print(square)
print(cube)
```

Output:

```text
25
125
```

### Important Note

A negative exponent can produce a floating-point result.

```python
print(2 ** -1)
```

Output:

```text
0.5
```

When a problem explicitly requires integer results, check that the operands and the exponent are appropriate for that requirement.

# 10. Updating Integers with Assignment Operators

Compound assignment operators combine an operation with assignment.

| Operator | Equivalent form |
|---|---|
| `+=` | `number = number + value` |
| `-=` | `number = number - value` |
| `*=` | `number = number * value` |
| `//=` | `number = number // value` |
| `%=` | `number = number % value` |
| `**=` | `number = number ** value` |

Example:

```python
number = 10

number += 5
print(number)

number *= 2
print(number)

number -= 4
print(number)
```

Output:

```text
15
30
26
```

These operators are useful when updating counters, totals, balances, and intermediate results.

# 11. Converting Values to Integers

The built-in `int()` function creates an integer from a compatible value or text representation.

## 11.1 Converting Integer Text

```python
text_number = "125"
number = int(text_number)

print(number)
print(type(number).__name__)
```

Output:

```text
125
int
```

## 11.2 Converting a Float

```python
number = int(12.9)

print(number)
```

Output:

```text
12
```

When converting a finite floating-point value to an integer, `int()` truncates the fractional part toward zero. It does not round to the nearest integer.

For example:

```python
print(int(12.9))
print(int(-12.9))
```

Output:

```text
12
-12
```

## 11.3 Invalid Numeric Text

```python
number = int("hello")
```

This raises `ValueError`.

A program that accepts user input should handle invalid input when appropriate.

```python
while True:
    raw_value = input("Enter an integer: ")

    try:
        number = int(raw_value)
        break
    except ValueError:
        print("Invalid input. Try again.")

print(f"Accepted integer: {number}")
```

This approach is used by the input helper in the Python practice program.

# 12. Boolean Values and Integers

Python's `bool` type is a subclass of `int`.

Consequently:

```python
print(int(True))
print(int(False))
```

Output:

```text
1
0
```

A Boolean value can therefore be explicitly converted to an integer.

However, it is usually clearer to use `True` and `False` when representing logical states, and integer values when representing counts, indices, or numeric quantities.

This topic introduces the relationship; the dedicated Boolean data-type section will cover logical values more thoroughly.

# 13. Large Integers in Python

Python integers can represent values larger than the fixed-width integers commonly encountered in some other programming languages.

Example:

```python
large_number = 2 ** 100

print(large_number)
print(type(large_number).__name__)
```

The result is still an `int`.

Python does not normally restrict integer values to a fixed 32-bit or 64-bit range. In practice, calculations are limited by available memory and computation time.

### Why Is This Useful?

Large integers can be used in:

- Factorial calculations.
- Exponentiation.
- Combinatorial calculations.
- Number theory.
- Certain cryptographic and mathematical algorithms.

A mathematically valid calculation can still require too much time or memory if the values grow extremely large.

# 14. Integer Comparisons

Python supports comparison operators for integers.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
first_number = 10
second_number = 20

print(first_number == second_number)
print(first_number != second_number)
print(first_number < second_number)
print(first_number >= second_number)
```

Output:

```text
False
True
True
False
```

Comparison operations produce Boolean values, which can be used in conditions.

Example:

```python
number = 15

if number > 10:
    print("The number is greater than 10.")
```

Output:

```text
The number is greater than 10.
```

# 15. Extracting Digits from an Integer

Modulo and floor division make it possible to process digits individually.

Consider the integer `528`.

### Extract the Last Digit

```python
number = 528

last_digit = number % 10

print(last_digit)
```

Output:

```text
8
```

### Remove the Last Digit

```python
number = 528

remaining_number = number // 10

print(remaining_number)
```

Output:

```text
52
```

### Repeated Digit Extraction

A loop can repeatedly extract the last digit until the number becomes zero.

This technique is used in:

- Sum of digits.
- Count digits.
- Reverse an integer.
- Numeric palindrome checks.
- Some number classification problems.

### Handling Zero

The integer `0` contains one decimal digit. Therefore, a digit-counting algorithm must handle zero separately if its main loop only runs while the remaining number is greater than zero.

### Handling Negative Integers

For simple digit-processing exercises, a common convention is to use the absolute value before extracting digits.

For example, `-528` has the digits `5`, `2`, and `8`, while the negative sign is not itself a digit.

The exact behavior should match the problem statement.

# 16. Dry Run: Sum of Digits

Consider the integer `528`.

The objective is to calculate:

```text
5 + 2 + 8 = 15
```

### Algorithm

1. Read an integer.
2. Use its absolute value.
3. Initialize `total = 0`.
4. Extract the final digit using `% 10`.
5. Add the digit to `total`.
6. Remove the final digit using `// 10`.
7. Repeat until the remaining number is zero.
8. Display the total.

### Pseudocode

```text
INPUT number
number = ABS(number)
total = 0

WHILE number > 0
    digit = number MOD 10
    total = total + digit
    number = number DIV 10
END WHILE

OUTPUT total
```

### Trace Table

| Iteration | Number before | Extracted digit | Total after addition | Number after |
|---:|---:|---:|---:|---:|
| 1 | 528 | 8 | 8 | 52 |
| 2 | 52 | 2 | 10 | 5 |
| 3 | 5 | 5 | 15 | 0 |

Final output:

```text
Sum of digits: 15
```

### Python Implementation

```python
number = abs(int(input("Enter an integer: ")))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)
```

For input `0`, this implementation correctly returns `0`.

# 17. Explanation of the 12 Guided Examples

The Python file provides twelve interactive examples.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Integer basics | Creating and displaying `int` values |
| 2 | Positive, negative, or zero | Classifying integers with conditions |
| 3 | Integer arithmetic | Addition, subtraction, multiplication, and division |
| 4 | Floor division | Understanding `//` |
| 5 | Remainder operator | Understanding `%` and divisibility |
| 6 | Integer exponentiation | Using the `**` operator |
| 7 | Compound assignment | Updating integer variables |
| 8 | Integer digit extraction | Using modulo and floor division |
| 9 | Convert text to integer | Using `int()` and handling invalid text |
| 10 | Boolean to integer | Understanding `int(True)` and `int(False)` |
| 11 | Large integers | Working with large integer values |
| 12 | Integer comparisons | Comparing two numeric values |

Run these examples to understand how integer values behave in different situations.

# 18. Explanation of the 12 Solved Problems

## Problem 1: Add Two Integers

Reads two integers and calculates their sum.

Formula:

```text
Total = First Number + Second Number
```

This demonstrates basic arithmetic and integer input.

## Problem 2: Even or Odd

Uses the remainder after division by two.

If `number % 2 == 0`, the number is even; otherwise, it is odd.

Zero and negative integers are handled by the same rule.

## Problem 3: Sum of Digits

Extracts digits using `% 10`, accumulates them, and removes the final digit using `// 10`.

The solution handles zero and negative input by taking the absolute value.

## Problem 4: Reverse an Integer

Rebuilds a number from its digits in reverse order.

For example:

```text
Input:  472
Output: 274
```

The implementation preserves the sign of a negative input. Leading zeros in the reversed representation are not preserved because the result is an integer.

## Problem 5: Count Digits

Repeatedly removes the last digit using integer division.

The number `0` is treated as a one-digit number.

## Problem 6: Quotient and Remainder

Uses floor division and modulo to calculate the quotient and remainder.

The divisor must not be zero.

For negative values, the result follows Python's floor-division rules rather than truncation toward zero.

## Problem 7: Swap Two Integers

Uses tuple assignment to exchange two values:

```python
first_number, second_number = second_number, first_number
```

## Problem 8: Convert Seconds into Hours, Minutes, and Seconds

Splits a non-negative integer number of seconds into hours, minutes, and remaining seconds using `//` and `%`.

For `3665` seconds, the formatted result is:

```text
01:01:05
```

## Problem 9: Sum Integers from 1 Through n

Uses the arithmetic-series formula:

```text
Sum = n * (n + 1) // 2
```

This calculates the sum without iterating over every integer.

## Problem 10: Factorial

Multiplies the integers from `1` through `n`.

For example:

```text
5! = 5 * 4 * 3 * 2 * 1 = 120
```

The implementation rejects negative input and returns `1` for `0!`.

## Problem 11: Prime-Number Check

A prime number is an integer greater than `1` with exactly two positive divisors.

The program tests possible divisors up to the square root of the number, using the equivalent condition `divisor * divisor <= number`.

## Problem 12: Find Minimum and Maximum

Reads a list of integers and uses `min()` and `max()` to find its smallest and largest values.

The program checks for an empty list before applying those operations.

# 19. Five Unsolved Practice Questions

Try to solve these questions independently after completing the guided examples and solved problems.

## Question 1: Armstrong Number

Determine whether a non-negative integer is an Armstrong number.

For a number with `d` digits, add each digit raised to the power `d`. The number is an Armstrong number when that sum equals the original number.

Example:

```text
153 = 1³ + 5³ + 3³ = 153
```

## Question 2: Greatest Common Divisor

Read two integers and calculate their greatest common divisor (GCD) using the Euclidean algorithm.

**Hint:** Repeatedly replace the pair `(a, b)` with `(b, a % b)` until the second value becomes zero. Consider the inputs `(0, 0)` and other zero-input cases explicitly.

## Question 3: Least Common Multiple

Read two integers and calculate their least common multiple (LCM).

For two non-zero integers:

```text
LCM(a, b) = abs(a * b) // GCD(a, b)
```

Define how the program handles zero inputs and test the cases where one or both values are zero.

## Question 4: Palindrome Integer

Determine whether a non-negative integer reads the same forward and backward.

Examples:

```text
121  -> Palindrome
1331 -> Palindrome
123  -> Not a palindrome
```

**Hint:** Reverse the digits and compare the reversed integer with the original.

## Question 5: Nth Power Calculator

Read an integer base and a non-negative integer exponent. Calculate the base raised to that exponent.

Example:

```text
Base: 3
Exponent: 4
Result: 81
```

Use the `**` operator and validate the exponent.

### Practice Method

For every question:

1. Identify the input and output.
2. Write an algorithm.
3. Convert the algorithm into pseudocode.
4. Dry-run the solution with small values.
5. Implement it in Python.
6. Test relevant boundary cases.

# 20. Testing and Edge Cases

Integer algorithms should be tested with more than one input.

| Problem | Suggested test cases |
|---|---|
| Number classification | Positive, negative, and zero |
| Even or odd | Positive even, positive odd, zero, negative integer |
| Sum of digits | `0`, `123`, `-456` |
| Reverse integer | `0`, `120`, `-123` |
| Count digits | `0`, `7`, `1000`, negative value |
| Quotient and remainder | Positive values, negative values, zero divisor |
| Factorial | `0`, `1`, positive value, negative input |
| Prime check | Values below `2`, a prime, a composite number |
| Minimum and maximum | Empty list, one value, duplicates, negative numbers |

### Important Edge Cases

- Zero may require special handling in digit loops.
- Negative inputs may require their own rules.
- A division operation must not use a zero divisor.
- Invalid text cannot always be converted using `int()`.
- A mathematically correct integer calculation can still be too expensive for extremely large values.

Correctness depends on the input rules established by the problem.

# 21. Time and Space Complexity

Complexity analysis describes how resource requirements grow as the input becomes larger.

| Algorithm | Typical time complexity | Auxiliary space |
|---|---|---|
| Add two integers | `O(1)` for a fixed-width operation model | `O(1)` |
| Classify an integer | `O(1)` for the shown comparisons | `O(1)` |
| Sum digits | `O(d)` | `O(1)` |
| Count digits | `O(d)` | `O(1)` |
| Reverse digits | `O(d)` | `O(1)` |
| Factorial by loop | `O(n)` loop iterations, excluding large-integer arithmetic costs | `O(1)` variables, excluding the growing result's representation |
| Prime check up to square root | `O(√n)` trial checks in the usual operation-count model | `O(1)` |

Here, `d` is the number of decimal digits and `n` is the relevant input value or loop limit.

Python integers can grow to arbitrary precision subject to available resources. For very large operands, arithmetic operations are not necessarily constant-time, so practical runtime can grow beyond these simplified operation-count models.

# 22. Common Mistakes

## Mistake 1: Confusing `int` and `float`

`10` is an integer, while `10.0` is a floating-point value.

**Solution:** Use `type()` while learning and select the type appropriate for the problem.

## Mistake 2: Assuming `/` Always Produces an Integer

In Python, `/` performs true division and ordinarily returns a float.

**Solution:** Use `//` when floor division is required.

## Mistake 3: Assuming Floor Division Truncates Toward Zero

For example:

```python
print(-17 // 5)
```

The result is `-4`, because floor division rounds down toward negative infinity.

## Mistake 4: Forgetting That `input()` Returns Text

A number entered by a user initially arrives as a string.

**Solution:** Convert it with `int()` where an integer is required, and handle invalid input.

## Mistake 5: Incorrect Digit Extraction

The last digit is obtained with `% 10`, and removing the last digit uses `// 10`.

Reversing these operations or updating the number incorrectly can produce an incorrect result.

## Mistake 6: Ignoring Zero in Digit Counting

A loop that executes only while the number is greater than zero does not count any digits when the input is zero.

**Solution:** Handle `0` as a special one-digit value.

## Mistake 7: Dividing by Zero

Integer division and modulo are not defined for a zero divisor in Python.

**Solution:** Validate the divisor before division.

# 23. Best Practices

1. Use `int` for values that should represent whole numbers.
2. Choose descriptive variable names.
3. Use `type()` to inspect types while learning.
4. Distinguish true division from floor division.
5. Understand Python's modulo rules for negative values.
6. Validate numeric input when required.
7. Handle zero explicitly in digit-processing algorithms.
8. Avoid division by zero.
9. Test both positive and negative inputs where relevant.
10. Consider time and memory requirements when processing very large integers.
11. Use the simplest correct algorithm for the stated constraints.
12. Write pseudocode and perform dry runs for unfamiliar problems.

# 24. Frequently Asked Questions

### Q1. What is the `int` data type?

It is Python's built-in type for integer values, such as `10`, `0`, and `-25`.

### Q2. Can an integer be negative?

Yes. Python integers may be positive, negative, or zero.

### Q3. How can I check the type of a value?

Use `type(value)`.

### Q4. What is the difference between `/` and `//`?

`/` performs true division, while `//` performs floor division.

### Q5. What does `%` do?

It returns the remainder according to Python's modulo and floor-division rules.

### Q6. How do I convert text into an integer?

Use `int(text)` when the text represents a valid integer. Invalid input raises `ValueError`.

### Q7. Does `int(12.9)` return `13`?

No. It truncates toward zero and returns `12`.

### Q8. Can Python handle very large integers?

Yes, subject to available memory and computation time.

### Q9. Why is modulo useful for even/odd checks?

An even integer has a remainder of zero when divided by `2`. An odd integer does not.

### Q10. How do I extract the last digit of a positive integer?

Use `number % 10`.

### Q11. How do I remove the last digit?

Use `number // 10` for a non-negative integer.

### Q12. What should I study next?

Continue to `02_float`, which introduces floating-point numbers and decimal calculations in Python.

# 25. How to Run the Program

Run the following command from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\01_int\01_int.py"
```

The main menu contains:

```text
=================================================================
INTEGER (int) DATA TYPE IN PYTHON
=================================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View integer checklist
0. Exit
Choose an option:
```

Select the required option and follow the prompts. Enter integer values where requested. If you enter invalid integer text, the helper function asks you to try again.

# 26. Folder Structure

```text
01_int/
│
├── 01_int.py
└── README.md
```

**`01_int.py`** contains the runnable examples, solved problems, unsolved questions, checklist, and interactive menus.

**`README.md`** contains the theory, operator explanations, algorithms, dry-run tables, practice questions, complexity notes, run command, and revision checklist.

# 27. Revision Checklist

Before moving to the next data type, confirm that you can:

- [ ] Explain the integer data type.
- [ ] Create positive and negative integers.
- [ ] Recognize zero as an integer.
- [ ] Inspect a data type with `type()`.
- [ ] Use arithmetic operators.
- [ ] Distinguish `/`, `//`, and `%`.
- [ ] Calculate powers using `**`.
- [ ] Convert suitable text to an integer.
- [ ] Understand how `int()` converts floating-point values.
- [ ] Extract digits using modulo and floor division.
- [ ] Reverse an integer.
- [ ] Sum the digits of an integer.
- [ ] Count integer digits correctly, including zero.
- [ ] Test prime-number and factorial algorithms.
- [ ] Attempt all five unsolved questions.

## Completion Goal

By completing this topic, you should understand how Python represents integers, how integer operators work, how to convert valid input into integers, and how to solve common integer-based programming problems.

**Next topic:** `02_float` — floating-point values, decimal calculations, rounding, formatting, and numeric precision.