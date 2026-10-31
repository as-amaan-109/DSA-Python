# Python Arithmetic Operators

**Week:** 1 — Programming Fundamentals  
**Main Section:** Operators and Expressions  
**Topic:** Arithmetic Operators  
**Language:** Python 3  
**Level:** Beginner to Intermediate  
**File:** `01_arithmetic_operators.py`  
**Purpose:** Learn how to perform mathematical calculations using Python arithmetic operators, understand their behavior, and apply them to practical programming problems.

---

# Table of Contents

1. Introduction
2. Learning Objectives
3. What Are Arithmetic Operators?
4. What Are Operands?
5. What Are Arithmetic Expressions?
6. Why Are Arithmetic Operators Important?
7. Arithmetic Operators in Python
8. Addition Operator (`+`)
9. Subtraction Operator (`-`)
10. Multiplication Operator (`*`)
11. Division Operator (`/`)
12. Floor Division Operator (`//`)
13. Modulus Operator (`%`)
14. Exponentiation Operator (`**`)
15. Unary Plus Operator (`+`)
16. Unary Minus Operator (`-`)
17. Arithmetic Operators with Negative Numbers
18. Floor Division with Negative Numbers
19. Modulus with Negative Numbers
20. Division by Zero
21. Integer Arithmetic
22. Floating-Point Arithmetic
23. Integer and Float Operations
24. Quotient and Remainder
25. The `divmod()` Function
26. Operator Precedence
27. Parentheses and Grouping
28. Operator Associativity
29. Arithmetic Expressions
30. Arithmetic Expressions with Variables
31. Arithmetic Expressions with User Input
32. Mathematical Applications
33. Section 1 — Twelve Arithmetic Operator Examples
34. Section 2 — Twelve Solved Problems
35. Understanding the Helper Functions
36. Understanding the Solved Problems Mapping
37. Section 3 — Ten Unsolved Practice Questions
38. Section 4 — Learning Checklist
39. Section 5 — Main Menu
40. How to Run the Python Program
41. Sample Program Execution
42. Common Mistakes
43. Error Handling
44. Debugging Techniques
45. Testing Strategy
46. Boundary Testing
47. Arithmetic Operators in DSA
48. Applications in Searching and Sorting
49. Applications in Number Theory
50. Best Practices
51. Code Readability
52. Mini Project Ideas
53. Frequently Asked Questions
54. Viva Questions and Answers
55. Quick Revision Tables
56. Important Terminology
57. Final Summary

---

# 1. Introduction

Arithmetic operators are one of the most important concepts in Python programming.

They are used to perform mathematical calculations on numeric values.

Almost every programming application uses arithmetic operations in some form.

Examples include:

- Adding two numbers.
- Calculating a total amount.
- Finding an average.
- Calculating percentages.
- Finding the remainder.
- Calculating squares and cubes.
- Converting seconds into hours and minutes.
- Calculating product prices.
- Performing mathematical formulas.
- Solving programming and DSA problems.

Python provides several arithmetic operators to perform these operations.

Consider the following example:

```python
first = 10
second = 20

result = first + second

print(result)
```

Output:

```text
30
```

In this program:

- `first` is a variable.
- `second` is a variable.
- `10` and `20` are integer values.
- `+` is the addition operator.
- `first + second` is an arithmetic expression.
- `result` stores the calculated value.

Python evaluates the expression and produces the result `30`.

Arithmetic operators are important because they allow a program to process numeric information.

They are also used in conditional statements, loops, functions, mathematical problems, searching algorithms, sorting algorithms, and many other programming concepts.

This topic explains arithmetic operators step by step, starting with basic calculations and moving towards negative floor division, operator precedence, parentheses, and practical programming problems.

---

# 2. Learning Objectives

After completing this topic, you should be able to understand and use Python arithmetic operators.

## 2.1 Basic Concepts

- Understand what arithmetic operators are.
- Understand what operands are.
- Understand arithmetic expressions.
- Identify operators in Python expressions.
- Identify operands in expressions.
- Understand how arithmetic expressions are evaluated.
- Use arithmetic operators with variables.
- Use arithmetic operators with numeric literals.

## 2.2 Addition

- Understand the addition operator.
- Use the `+` operator.
- Add two integers.
- Add multiple numbers.
- Add floating-point values.
- Calculate totals using addition.

## 2.3 Subtraction

- Understand the subtraction operator.
- Use the `-` operator.
- Subtract two numbers.
- Work with negative results.
- Calculate differences.
- Understand unary minus.

## 2.4 Multiplication

- Understand the multiplication operator.
- Use the `*` operator.
- Multiply two numbers.
- Multiply multiple values.
- Calculate product totals.
- Calculate squares and cubes.

## 2.5 Division

- Understand the division operator.
- Use the `/` operator.
- Divide two numbers.
- Understand floating-point division results.
- Handle division by zero.
- Use division in mathematical problems.

## 2.6 Floor Division

- Understand the `//` operator.
- Perform floor division.
- Distinguish division from floor division.
- Understand floor division with positive numbers.
- Understand floor division with negative numbers.
- Apply floor division to practical problems.

## 2.7 Modulus

- Understand the `%` operator.
- Calculate remainders.
- Check even and odd numbers.
- Find the last digit of a number.
- Find the remainder of negative numbers.
- Use modulus in DSA problems.

## 2.8 Exponentiation

- Understand the `**` operator.
- Calculate powers.
- Calculate squares.
- Calculate cubes.
- Work with positive and negative exponents.
- Understand exponentiation precedence.

## 2.9 Advanced Arithmetic Concepts

- Understand unary plus.
- Understand unary minus.
- Understand negative floor division.
- Understand negative modulus.
- Understand operator precedence.
- Use parentheses for grouping.
- Understand associativity.
- Use `divmod()` to calculate quotient and remainder.

## 2.10 Programming Skills

- Write arithmetic programs.
- Accept numeric input.
- Convert input into suitable numeric types.
- Perform calculations using variables.
- Validate divisors.
- Handle invalid input.
- Solve arithmetic problems.
- Test different numerical values.
- Apply arithmetic operators to basic DSA problems.

---

# 3. What Are Arithmetic Operators?

Arithmetic operators are symbols used to perform mathematical operations on numeric values.

They perform operations such as addition, subtraction, multiplication, and division.

Example:

```python
result = 10 + 20
```

Here:

- `10` is the first operand.
- `20` is the second operand.
- `+` is the arithmetic operator.
- `10 + 20` is the expression.
- `result` stores the evaluated value.

Output:

```text
30
```

## 3.1 Why Are Arithmetic Operators Used?

Arithmetic operators are used to:

1. Add values.
2. Subtract values.
3. Multiply values.
4. Divide values.
5. Calculate remainders.
6. Calculate powers.
7. Calculate averages.
8. Calculate percentages.
9. Perform mathematical formulas.
10. Solve numerical programming problems.

## 3.2 Arithmetic Operators Work with Numeric Values

Example:

```python
first = 10
second = 5

print(first + second)
print(first - second)
print(first * second)
```

Output:

```text
15
5
50
```

Python supports arithmetic operations on different numeric types.

However, the behavior depends on the operand types and the selected operator.

---

# 4. What Are Operands?

Operands are the values or objects on which an operator performs an operation.

Example:

```python
result = 15 + 5
```

Here:

- `15` is an operand.
- `5` is an operand.
- `+` is the operator.

## 4.1 Operands Can Be Numeric Literals

```python
result = 10 + 20
```

The operands are the numeric values `10` and `20`.

## 4.2 Operands Can Be Variables

```python
first = 10
second = 20

result = first + second
```

The operands are the variables `first` and `second`.

They refer to numeric objects.

## 4.3 Operands Can Be Expressions

```python
result = (10 + 5) * 2
```

The multiplication operator uses the result of the grouped expression as one of its operands.

## 4.4 Important Point

Whenever you see an arithmetic operator, identify the values on which it performs an operation.

Understanding operands makes it easier to read and solve expressions.

---

# 5. What Are Arithmetic Expressions?

An arithmetic expression is a combination of numeric values, variables, and arithmetic operators that produces a numerical result.

Example:

```python
10 + 20
```

Result:

```text
30
```

Another example:

```python
10 * 5 - 2
```

Result:

```text
48
```

## 5.1 Simple Arithmetic Expression

```python
result = 10 + 5
```

## 5.2 Expression with Variables

```python
first = 10
second = 5

result = first * second
```

## 5.3 Expression with Multiple Operators

```python
result = 10 + 5 * 2
```

The expression contains addition and multiplication.

Python follows operator precedence rules when evaluating it.

## 5.4 Expression with Parentheses

```python
result = (10 + 5) * 2
```

Parentheses change how the expression is grouped.

## 5.5 Expression with Floating-Point Values

```python
result = 10.5 + 5.25

print(result)
```

Output:

```text
15.75
```

Arithmetic expressions are used throughout Python programming.

---

# 6. Why Are Arithmetic Operators Important?

Arithmetic operators are used in almost every type of application.

## 6.1 Calculating Totals

```python
first = 100
second = 200
third = 300

total = first + second + third

print(total)
```

Output:

```text
600
```

## 6.2 Calculating Averages

```python
first = 80
second = 90
third = 85

average = (first + second + third) / 3

print(average)
```

## 6.3 Calculating Product Prices

```python
price = 50
quantity = 4

total = price * quantity

print(total)
```

Output:

```text
200
```

## 6.4 Finding a Remainder

```python
number = 17

print(number % 5)
```

Output:

```text
2
```

## 6.5 Checking Even and Odd Numbers

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 6.6 Applications

Arithmetic operators are used in:

- Calculators.
- Shopping applications.
- Banking systems.
- Student management systems.
- Billing software.
- Scientific applications.
- Mathematical programs.
- Searching algorithms.
- Sorting algorithms.
- Competitive programming.
- Data Structures and Algorithms.

---

# 7. Arithmetic Operators in Python

Python provides the following main arithmetic operators.

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

Python also supports unary arithmetic operators:

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Unary Plus | `+10` | `10` |
| `-` | Unary Minus | `-10` | `-10` |

## 7.1 Quick Explanation

- Addition combines values.
- Subtraction calculates the difference.
- Multiplication calculates the product.
- Division calculates the quotient.
- Floor division returns the floored quotient.
- Modulus returns the remainder.
- Exponentiation calculates a power.
- Unary plus applies a positive sign.
- Unary minus applies a negative sign.

The next sections explain each operator in detail.

---

# 8. Addition Operator (`+`)

The addition operator is represented by:

```python
+
```

It adds two or more numeric values.

## 8.1 Syntax

```python
result = first_number + second_number
```

## 8.2 Basic Example

```python
first = 10
second = 20

result = first + second

print(result)
```

Output:

```text
30
```

## 8.3 Addition of Three Numbers

```python
first = 10
second = 20
third = 30

result = first + second + third

print(result)
```

Output:

```text
60
```

## 8.4 Addition of Floating-Point Values

```python
first = 10.5
second = 5.5

result = first + second

print(result)
```

Output:

```text
16.0
```

## 8.5 Addition with Negative Numbers

```python
first = -10
second = 20

print(first + second)
```

Output:

```text
10
```

## 8.6 Addition with Variables

```python
math_marks = 80
science_marks = 90
english_marks = 85

total = math_marks + science_marks + english_marks

print("Total Marks:", total)
```

Output:

```text
Total Marks: 255
```

## 8.7 Real-Life Applications

Addition is commonly used for:

- Calculating totals.
- Adding marks.
- Calculating bill amounts.
- Adding product quantities.
- Calculating account balances.
- Combining distances.
- Calculating accumulated scores.

## 8.8 Important Note

The `+` symbol can also concatenate strings.

Example:

```python
first = "Hello"
second = "World"

print(first + second)
```

Output:

```text
HelloWorld
```

When used with strings, `+` performs concatenation rather than numeric addition.

---

# 9. Subtraction Operator (`-`)

The subtraction operator is represented by:

```python
-
```

It subtracts the second operand from the first operand.

## 9.1 Syntax

```python
result = first_number - second_number
```

## 9.2 Basic Example

```python
first = 50
second = 20

result = first - second

print(result)
```

Output:

```text
30
```

## 9.3 Subtract Three Numbers

```python
first = 100
second = 20
third = 10

result = first - second - third

print(result)
```

Output:

```text
70
```

## 9.4 Negative Result

```python
first = 10
second = 20

print(first - second)
```

Output:

```text
-10
```

## 9.5 Subtract Negative Numbers

```python
first = 10
second = -5

print(first - second)
```

Output:

```text
15
```

Subtracting a negative value is equivalent to adding its positive magnitude.

## 9.6 Real-Life Applications

Subtraction is used for:

- Finding differences.
- Calculating remaining quantities.
- Calculating discounts.
- Finding profit or loss differences.
- Updating account balances.
- Calculating distance differences.
- Computing time differences.

## 9.7 Important Point

The order of operands matters in subtraction.

```python
print(20 - 10)
print(10 - 20)
```

Output:

```text
10
-10
```

Subtraction is not commutative.

Changing the operand order can change the result.

---

# 10. Multiplication Operator (`*`)

The multiplication operator is represented by:

```python
*
```

It multiplies two or more numeric values.

## 10.1 Syntax

```python
result = first_number * second_number
```

## 10.2 Basic Example

```python
first = 10
second = 5

result = first * second

print(result)
```

Output:

```text
50
```

## 10.3 Multiply Three Numbers

```python
first = 2
second = 3
third = 4

result = first * second * third

print(result)
```

Output:

```text
24
```

## 10.4 Multiplication with Floating-Point Values

```python
first = 2.5
second = 4

print(first * second)
```

Output:

```text
10.0
```

## 10.5 Multiplication with Negative Values

```python
print(-5 * 4)
print(-5 * -4)
```

Output:

```text
-20
20
```

## 10.6 Calculate Area of a Rectangle

Formula:

\[
Area = Length \times Breadth
\]

Program:

```python
length = 10
breadth = 5

area = length * breadth

print("Area:", area)
```

Output:

```text
Area: 50
```

## 10.7 Calculate Product Total

```python
price = 50
quantity = 4

total = price * quantity

print("Total:", total)
```

Output:

```text
Total: 200
```

## 10.8 Real-Life Applications

Multiplication is used in:

- Calculating area.
- Calculating total prices.
- Calculating product quantities.
- Calculating powers through repeated multiplication.
- Scientific formulas.
- Mathematical algorithms.
- Matrix calculations.

## 10.9 Important Note

The `*` operator also supports sequence repetition.

Example:

```python
print("Python " * 3)
```

Output:

```text
Python Python Python
```

This is a sequence operation, not ordinary numeric multiplication.

---

# 11. Division Operator (`/`)

The division operator is represented by:

```python
/
```

It divides the first operand by the second operand.

## 11.1 Syntax

```python
result = first_number / second_number
```

## 11.2 Basic Example

```python
first = 20
second = 4

result = first / second

print(result)
```

Output:

```text
5.0
```

## 11.3 Division Produces a Float

For ordinary numeric division, Python's `/` operator returns a floating-point result.

Example:

```python
print(10 / 2)
```

Output:

```text
5.0
```

Even though the answer is mathematically a whole number, the result is a float.

## 11.4 Division with a Remainder

```python
print(17 / 5)
```

Output:

```text
3.4
```

## 11.5 Division with Floating-Point Values

```python
first = 10.5
second = 2.5

print(first / second)
```

Output:

```text
4.2
```

## 11.6 Negative Division

```python
print(-10 / 2)
print(10 / -2)
```

Output:

```text
-5.0
-5.0
```

## 11.7 Division by Zero

Division by zero is not allowed for ordinary numeric division.

Example:

```python
# This raises ZeroDivisionError.
# print(10 / 0)
```

A program should check the divisor before performing division.

```python
first = 10
second = 0

if second != 0:
    print(first / second)
else:
    print("Division by zero is not allowed.")
```

## 11.8 Real-Life Applications

Division is used for:

- Calculating averages.
- Dividing quantities.
- Calculating rates.
- Calculating prices per item.
- Calculating speed.
- Converting measurements.
- Solving mathematical formulas.

## 11.9 Important Difference

```python
print(10 / 3)
```

performs ordinary division.

```python
print(10 // 3)
```

performs floor division.

The two operators have different behavior.

---

# 12. Floor Division Operator (`//`)

The floor division operator is represented by:

```python
//
```

It divides two numbers and returns the quotient rounded down toward negative infinity.

## 12.1 Syntax

```python
result = first_number // second_number
```

## 12.2 Basic Example

```python
first = 17
second = 5

result = first // second

print(result)
```

Output:

```text
3
```

Explanation:

Ordinary division:

\[
17 / 5 = 3.4
\]

Floor division:

\[
17 // 5 = 3
\]

The result is the floor of the quotient.

## 12.3 Another Example

```python
print(20 // 3)
```

Output:

```text
6
```

## 12.4 Floor Division with Exact Division

```python
print(20 // 5)
```

Output:

```text
4
```

## 12.5 Floor Division with Floating-Point Values

```python
print(17.5 // 5)
```

Output:

```text
3.0
```

The result is a float because a floating-point operand is involved.

## 12.6 Floor Division with Negative Values

```python
print(-17 // 5)
```

Output:

```text
-4
```

Why?

Ordinary division gives:

\[
-17 / 5 = -3.4
\]

Floor division moves down to the next integer value:

\[
-17 // 5 = -4
\]

This is an important difference between floor division and truncation toward zero.

## 12.7 Floor Division Versus `int()`

Consider:

```python
print(int(-17 / 5))
print(-17 // 5)
```

Output:

```text
-3
-4
```

Explanation:

- `int()` truncates toward zero.
- `//` returns the floor of the quotient.

Do not treat these operations as interchangeable for negative values.

## 12.8 Real-Life Applications

Floor division is useful for:

- Dividing objects into complete groups.
- Calculating full hours.
- Calculating complete pages.
- Finding index positions.
- Converting seconds into minutes.
- Working with arrays.
- Solving numerical problems.

## 12.9 Important Rule

For ordinary built-in integer division with a nonzero divisor:

```python
a == (a // b) * b + (a % b)
```

Python's quotient and remainder follow rules that preserve this relationship.

---

# 13. Modulus Operator (`%`)

The modulus operator is represented by:

```python
%
```

It returns the remainder after division.

## 13.1 Syntax

```python
remainder = first_number % second_number
```

## 13.2 Basic Example

```python
first = 17
second = 5

result = first % second

print(result)
```

Output:

```text
2
```

Explanation:

17 divided by 5 gives:

- Quotient = 3.
- Remainder = 2.

Therefore:

```python
17 % 5
```

returns:

```text
2
```

## 13.3 Exact Division

```python
print(20 % 5)
```

Output:

```text
0
```

When one integer divides another exactly, the remainder is zero.

## 13.4 Check Even or Odd

A number is even if it is divisible by 2 without a remainder.

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

## 13.5 Check Odd Number

```python
number = 7

if number % 2 != 0:
    print("Odd")
else:
    print("Even")
```

## 13.6 Find the Last Digit

```python
number = 12345

last_digit = number % 10

print(last_digit)
```

Output:

```text
5
```

For non-negative integers, `% 10` returns the last decimal digit.

For negative numbers, use `abs()` when you specifically want the non-negative last digit.

```python
number = -12345

last_digit = abs(number) % 10

print(last_digit)
```

Output:

```text
5
```

## 13.7 Remove the Last Digit

For a non-negative integer:

```python
number = 12345

number = number // 10

print(number)
```

Output:

```text
1234
```

## 13.8 Modulus with Negative Values

```python
print(-17 % 5)
print(17 % -5)
```

Output:

```text
3
-3
```

Python's remainder has the same sign as the divisor when the remainder is nonzero.

## 13.9 Modulus by Zero

The following operation raises `ZeroDivisionError`:

```python
# print(10 % 0)
```

Always check that the divisor is not zero.

## 13.10 Real-Life Applications

Modulus is used for:

- Checking even and odd values.
- Finding the last digit.
- Divisibility checks.
- Repeating patterns.
- Circular indexing.
- Clock calculations.
- Number theory.
- DSA problems.
- Hashing-related calculations.

---

# 14. Exponentiation Operator (`**`)

The exponentiation operator is represented by:

```python
**
```

It calculates one number raised to the power of another.

## 14.1 Syntax

```python
result = base ** exponent
```

## 14.2 Basic Example

```python
base = 2
exponent = 3

result = base ** exponent

print(result)
```

Output:

```text
8
```

Explanation:

\[
2^3 = 2 \times 2 \times 2 = 8
\]

## 14.3 Calculate a Square

```python
number = 5

square = number ** 2

print(square)
```

Output:

```text
25
```

## 14.4 Calculate a Cube

```python
number = 5

cube = number ** 3

print(cube)
```

Output:

```text
125
```

## 14.5 Power of Zero

```python
print(10 ** 0)
```

Output:

```text
1
```

For a nonzero number, raising it to the power zero gives one.

## 14.6 Zero to a Positive Power

```python
print(0 ** 3)
```

Output:

```text
0
```

## 14.7 Negative Exponent

```python
print(2 ** -2)
```

Output:

```text
0.25
```

A negative exponent represents a reciprocal for a nonzero base.

\[
2^{-2} = \frac{1}{2^2} = \frac{1}{4}
\]

## 14.8 Floating-Point Exponentiation

```python
print(2.5 ** 2)
```

Output:

```text
6.25
```

## 14.9 Exponentiation with Parentheses

```python
print((-2) ** 2)
```

Output:

```text
4
```

Compare:

```python
print(-2 ** 2)
```

Output:

```text
-4
```

Exponentiation has higher precedence than unary minus in this expression.

## 14.10 Real-Life Applications

Exponentiation is used for:

- Calculating squares.
- Calculating cubes.
- Scientific formulas.
- Geometric calculations.
- Compound growth models.
- Mathematical algorithms.
- Power-related problems.

---

# 15. Unary Plus Operator (`+`)

Unary plus applies a positive sign to one operand.

It is represented by:

```python
+x
```

## 15.1 Basic Example

```python
number = 10

result = +number

print(result)
```

Output:

```text
10
```

## 15.2 Unary Plus with Negative Values

```python
number = -10

print(+number)
```

Output:

```text
-10
```

Unary plus does not change the sign of the value.

## 15.3 Unary Plus and Binary Addition

The `+` symbol has different uses.

Unary plus:

```python
number = +10
```

Binary addition:

```python
result = 10 + 20
```

The meaning depends on the position of the operator.

---

# 16. Unary Minus Operator (`-`)

Unary minus applies a negative sign to one operand.

## 16.1 Basic Example

```python
number = 10

result = -number

print(result)
```

Output:

```text
-10
```

## 16.2 Change the Sign

```python
number = -25

print(-number)
```

Output:

```text
25
```

## 16.3 Unary Minus and Binary Subtraction

Unary minus:

```python
number = -10
```

Binary subtraction:

```python
result = 20 - 10
```

The same symbol performs different operations depending on its position.

## 16.4 Practical Uses

Unary minus is useful when:

- Representing negative values.
- Reversing the sign of a value.
- Working with direction.
- Calculating negative differences.
- Manipulating signed numerical values.

---

# 17. Arithmetic Operators with Negative Numbers

Arithmetic operators also work with negative values.

However, floor division and modulus require additional care.

## 17.1 Addition

```python
print(-10 + 5)
```

Output:

```text
-5
```

## 17.2 Subtraction

```python
print(-10 - 5)
```

Output:

```text
-15
```

## 17.3 Multiplication

```python
print(-10 * 5)
```

Output:

```text
-50
```

## 17.4 Multiplication of Two Negative Numbers

```python
print(-10 * -5)
```

Output:

```text
50
```

## 17.5 Division

```python
print(-10 / 5)
```

Output:

```text
-2.0
```

## 17.6 Floor Division

```python
print(-10 // 3)
```

Output:

```text
-4
```

## 17.7 Modulus

```python
print(-10 % 3)
```

Output:

```text
2
```

Understanding negative arithmetic is essential for avoiding mistakes in mathematical programs.

---

# 18. Floor Division with Negative Numbers

Floor division is particularly important when working with negative values.

It rounds the quotient down toward negative infinity.

It does not simply remove the fractional portion.

## 18.1 Positive Division

```python
print(17 // 5)
```

Output:

```text
3
```

## 18.2 Negative Dividend

```python
print(-17 // 5)
```

Output:

```text
-4
```

## 18.3 Negative Divisor

```python
print(17 // -5)
```

Output:

```text
-4
```

## 18.4 Both Values Negative

```python
print(-17 // -5)
```

Output:

```text
3
```

## 18.5 Comparison with `int()`

```python
print(int(-17 / 5))
print(-17 // 5)
```

Output:

```text
-3
-4
```

## 18.6 Important Rule

Floor division returns the floor of the mathematical quotient.

For a negative non-integer quotient, the floor is the next smaller integer.

---

# 19. Modulus with Negative Numbers

The modulus operator returns a remainder.

Python's remainder follows the sign of the divisor when the remainder is nonzero.

## 19.1 Positive Values

```python
print(17 % 5)
```

Output:

```text
2
```

## 19.2 Negative Dividend

```python
print(-17 % 5)
```

Output:

```text
3
```

## 19.3 Negative Divisor

```python
print(17 % -5)
```

Output:

```text
-3
```

## 19.4 Both Values Negative

```python
print(-17 % -5)
```

Output:

```text
-2
```

## 19.5 Quotient and Remainder Relationship

For ordinary integer operands with a nonzero divisor:

\[
a = (a // b) \times b + (a \% b)
\]

Example:

```python
a = -17
b = 5

quotient = a // b
remainder = a % b

print(quotient)
print(remainder)

print(quotient * b + remainder)
```

Output:

```text
-4
3
-17
```

This identity is useful when understanding Python's division and remainder rules.

---

# 20. Division by Zero

Division by zero is not allowed for ordinary numeric division.

It raises:

```text
ZeroDivisionError
```

## 20.1 Ordinary Division

```python
# print(10 / 0)
```

## 20.2 Floor Division

```python
# print(10 // 0)
```

## 20.3 Modulus

```python
# print(10 % 0)
```

These expressions raise `ZeroDivisionError`.

## 20.4 Validate Before Division

```python
first = 10
second = 0

if second != 0:
    result = first / second
    print(result)
else:
    print("Division by zero is not allowed.")
```

Output:

```text
Division by zero is not allowed.
```

## 20.5 User Input Example

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if second != 0:
    result = first / second
    print("Result:", result)
else:
    print("Please enter a non-zero divisor.")
```

## 20.6 Why Is Validation Important?

A program should check the divisor before performing an operation that requires a nonzero value.

This improves reliability and gives the user a meaningful message.

---

# 21. Integer Arithmetic

Integer arithmetic uses integer operands.

Examples:

```python
first = 10
second = 5

print(first + second)
print(first - second)
print(first * second)
print(first // second)
print(first % second)
```

## 21.1 Integer Addition

```python
print(10 + 20)
```

## 21.2 Integer Subtraction

```python
print(20 - 10)
```

## 21.3 Integer Multiplication

```python
print(10 * 5)
```

## 21.4 Integer Division

```python
print(10 / 2)
```

The result is a float.

## 21.5 Integer Floor Division

```python
print(10 // 3)
```

The result is an integer when both operands are integers.

## 21.6 Integer Modulus

```python
print(10 % 3)
```

## 21.7 Integer Exponentiation

```python
print(2 ** 5)
```

Python integers support arbitrary precision, subject to available memory and practical resource limits.

---

# 22. Floating-Point Arithmetic

Floating-point arithmetic uses values represented by Python's `float` type.

Examples:

```python
first = 10.5
second = 2.5
```

## 22.1 Addition

```python
print(first + second)
```

## 22.2 Subtraction

```python
print(first - second)
```

## 22.3 Multiplication

```python
print(first * second)
```

## 22.4 Division

```python
print(first / second)
```

## 22.5 Floating-Point Precision

Binary floating-point numbers cannot represent every decimal fraction exactly.

Example:

```python
result = 0.1 + 0.2

print(result)
```

A typical output is:

```text
0.30000000000000004
```

This is a result of binary floating-point representation.

## 22.6 Formatting the Result

```python
result = 0.1 + 0.2

print(f"{result:.2f}")
```

Output:

```text
0.30
```

Formatting changes the displayed representation.

It does not make the underlying calculation exact.

## 22.7 Financial Calculations

For financial calculations requiring exact decimal arithmetic, consider Python's `decimal.Decimal` type instead of relying on binary floating-point arithmetic.

---

# 23. Integer and Float Operations

Python allows arithmetic operations between compatible numeric types.

Example:

```python
integer_value = 10
float_value = 2.5

result = integer_value + float_value

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

## 23.1 Addition

```python
print(10 + 2.5)
```

## 23.2 Subtraction

```python
print(10 - 2.5)
```

## 23.3 Multiplication

```python
print(10 * 2.5)
```

## 23.4 Division

```python
print(10 / 2)
```

## 23.5 Floor Division

```python
print(10.5 // 2)
```

Output:

```text
5.0
```

## 23.6 Important Point

The result type can depend on the operand types and the operator being used.

Use `type()` when you need to inspect the resulting type.

---

# 24. Quotient and Remainder

When one integer is divided by another nonzero integer, the result can be described using a quotient and remainder.

Example:

\[
17 = (5 \times 3) + 2
\]

Here:

- Dividend = 17.
- Divisor = 5.
- Quotient = 3.
- Remainder = 2.

## 24.1 Find the Quotient

```python
quotient = 17 // 5

print(quotient)
```

Output:

```text
3
```

## 24.2 Find the Remainder

```python
remainder = 17 % 5

print(remainder)
```

Output:

```text
2
```

## 24.3 Verify the Result

```python
dividend = 17
divisor = 5

quotient = dividend // divisor
remainder = dividend % divisor

verified = quotient * divisor + remainder

print("Verified:", verified)
```

Output:

```text
Verified: 17
```

## 24.4 Why Is This Useful?

Quotient and remainder operations are used for:

- Grouping values.
- Converting units.
- Extracting digits.
- Even and odd checks.
- Index calculations.
- Number theory.
- DSA problems.

---

# 25. The `divmod()` Function

Python provides a built-in function called `divmod()`.

It returns the quotient and remainder together.

## 25.1 Syntax

```python
divmod(dividend, divisor)
```

## 25.2 Basic Example

```python
result = divmod(17, 5)

print(result)
```

Output:

```text
(3, 2)
```

The returned value is a tuple containing:

- Quotient.
- Remainder.

## 25.3 Unpacking the Result

```python
quotient, remainder = divmod(17, 5)

print("Quotient:", quotient)
print("Remainder:", remainder)
```

Output:

```text
Quotient: 3
Remainder: 2
```

## 25.4 Compare with `//` and `%`

```python
first = 17
second = 5

quotient = first // second
remainder = first % second

print(quotient, remainder)
```

The same quotient and remainder can be obtained using:

```python
quotient, remainder = divmod(first, second)

print(quotient, remainder)
```

## 25.5 Negative Values

```python
print(divmod(-17, 5))
```

Output:

```text
(-4, 3)
```

The function follows Python's floor-division and modulus rules.

## 25.6 Invalid Divisor

```python
# This raises ZeroDivisionError:
# print(divmod(10, 0))
```

## 25.7 Applications

`divmod()` is useful for:

- Converting seconds into minutes and seconds.
- Converting minutes into hours and minutes.
- Extracting quotient and remainder together.
- Breaking values into groups.
- Solving number problems.

---

# 26. Operator Precedence

Operator precedence determines which operations are grouped first in an expression.

Consider:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication has higher precedence than addition.

The expression is grouped as:

```python
10 + (5 * 2)
```

Calculation:

```text
10 + 10 = 20
```

## 26.1 Basic Arithmetic Precedence

For the arithmetic operators covered in this topic, the simplified order is:

| Priority | Operator | Operation |
|---:|---|---|
| 1 | `**` | Exponentiation |
| 2 | `+x`, `-x` | Unary plus and unary minus |
| 3 | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| 4 | `+`, `-` | Addition and subtraction |

Parentheses are evaluated before the operators inside the grouped expression are used in the surrounding expression.

## 26.2 Multiplication Before Addition

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

## 26.3 Division Before Addition

```python
result = 10 + 20 / 5

print(result)
```

Output:

```text
14.0
```

## 26.4 Exponentiation Before Multiplication

```python
result = 2 * 3 ** 2

print(result)
```

Output:

```text
18
```

## 26.5 Why Is Precedence Important?

It helps programmers understand how Python evaluates expressions containing multiple operators.

Without understanding precedence, it is easy to calculate the wrong result.

---

# 27. Parentheses and Grouping

Parentheses are used to group parts of an expression.

They can change which operation is evaluated first.

## 27.1 Without Parentheses

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

## 27.2 With Parentheses

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

## 27.3 Nested Parentheses

```python
result = ((10 + 5) * (4 - 2))

print(result)
```

Output:

```text
30
```

## 27.4 Parentheses in Average Calculation

```python
first = 80
second = 90
third = 85

average = (first + second + third) / 3

print(average)
```

The parentheses make it clear that all three marks are added before division.

## 27.5 Why Use Parentheses?

Parentheses help to:

- Change expression grouping.
- Make calculations clearer.
- Prevent precedence-related mistakes.
- Improve readability.
- Separate complex mathematical operations.

## 27.6 Best Practice

Use parentheses when they make the intended calculation easier to understand.

---

# 28. Operator Associativity

Associativity determines how operators with the same precedence are grouped when parentheses do not specify another grouping.

## 28.1 Left Associativity

Subtraction is left-associative.

Example:

```python
result = 20 - 5 - 3

print(result)
```

Output:

```text
12
```

The expression is grouped as:

```python
(20 - 5) - 3
```

Calculation:

```text
15 - 3 = 12
```

## 28.2 Right Associativity

Exponentiation is right-associative.

Example:

```python
result = 2 ** 3 ** 2

print(result)
```

Output:

```text
512
```

The expression is grouped as:

```python
2 ** (3 ** 2)
```

Calculation:

```text
2 ** 9 = 512
```

## 28.3 Division and Multiplication

Multiplication, division, floor division, and modulus share a precedence level and are generally evaluated from left to right when they appear in the same expression.

Example:

```python
result = 20 / 5 * 2

print(result)
```

The grouping is:

```python
(20 / 5) * 2
```

Output:

```text
8.0
```

## 28.4 Important Note About Exponentiation

Exponentiation has a special relationship with unary operators.

Example:

```python
print(-2 ** 2)
```

Output:

```text
-4
```

This is interpreted as:

```python
-(2 ** 2)
```

But:

```python
print((-2) ** 2)
```

Output:

```text
4
```

Parentheses explicitly change the grouping.

---

# 29. Arithmetic Expressions

Arithmetic expressions combine arithmetic operators and operands.

## 29.1 Simple Addition

```python
result = 10 + 20
```

## 29.2 Addition and Subtraction

```python
result = 50 + 20 - 10
```

## 29.3 Multiplication and Division

```python
result = 20 * 5 / 2
```

## 29.4 Multiple Operators

```python
result = 10 + 5 * 2 - 3
```

## 29.5 Expression with Parentheses

```python
result = (10 + 5) * (8 - 3)
```

## 29.6 Expression with Powers

```python
result = 2 ** 3 + 5
```

## 29.7 Expression with Variables

```python
first = 10
second = 5
third = 2

result = first + second * third

print(result)
```

## 29.8 Why Learn Expressions?

Expressions are used in:

- Mathematical calculations.
- Program conditions.
- Algorithms.
- Loop calculations.
- Index calculations.
- Data processing.
- Scientific formulas.

---

# 30. Arithmetic Expressions with Variables

Variables make expressions reusable.

Example:

```python
first = 10
second = 20

result = first + second

print(result)
```

## 30.1 Addition with Variables

```python
first = 10
second = 20

print(first + second)
```

## 30.2 Multiplication with Variables

```python
price = 50
quantity = 4

total = price * quantity

print(total)
```

## 30.3 Average with Variables

```python
first = 80
second = 90
third = 70

average = (first + second + third) / 3

print(average)
```

## 30.4 Update a Calculation

```python
number = 10

number = number + 5

print(number)
```

## 30.5 Important Point

Variables make it possible to use the same expression with different values.

---

# 31. Arithmetic Expressions with User Input

A program can collect numeric values from the user and use them in arithmetic expressions.

Remember that `input()` returns a string.

For numeric calculations, convert the input into a suitable numeric type.

## 31.1 Read Two Integers

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

result = first + second

print("Sum:", result)
```

## 31.2 Read Two Floating-Point Values

```python
first = float(input("Enter first value: "))
second = float(input("Enter second value: "))

result = first * second

print("Product:", result)
```

## 31.3 Calculate an Average

```python
first = float(input("Enter first mark: "))
second = float(input("Enter second mark: "))
third = float(input("Enter third mark: "))

average = (first + second + third) / 3

print("Average:", average)
```

## 31.4 Handle Invalid Input

```python
try:
    number = int(input("Enter an integer: "))

    print("Square:", number ** 2)

except ValueError:
    print("Please enter a valid integer.")
```

## 31.5 Validate a Divisor

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if second != 0:
    print("Result:", first / second)
else:
    print("Divisor cannot be zero.")
```

---

# 32. Mathematical Applications

Arithmetic operators can be used to solve many mathematical problems.

## 32.1 Area of a Rectangle

Formula:

\[
Area = Length \times Breadth
\]

```python
length = 10
breadth = 5

area = length * breadth

print("Area:", area)
```

Output:

```text
Area: 50
```

## 32.2 Area of a Square

Formula:

\[
Area = Side^2
\]

```python
side = 5

area = side ** 2

print("Area:", area)
```

Output:

```text
Area: 25
```

## 32.3 Area of a Circle

Formula:

\[
Area = \pi r^2
\]

```python
pi = 3.14159
radius = 5

area = pi * radius ** 2

print("Area:", area)
```

## 32.4 Simple Interest

Formula:

\[
SI = \frac{P \times R \times T}{100}
\]

```python
principal = 10000
rate = 5
time = 2

simple_interest = (
    principal * rate * time
) / 100

print("Simple Interest:", simple_interest)
```

## 32.5 Average

Formula:

\[
Average = \frac{Sum}{Number\ of\ Values}
\]

```python
first = 10
second = 20
third = 30

average = (first + second + third) / 3

print("Average:", average)
```

## 32.6 Percentage

Formula:

\[
Percentage = \frac{Obtained}{Total} \times 100
\]

```python
obtained = 450
total = 500

percentage = (obtained / total) * 100

print("Percentage:", percentage)
```

## 32.7 Speed

Formula:

\[
Speed = \frac{Distance}{Time}
\]

```python
distance = 100
time = 2

speed = distance / time

print("Speed:", speed)
```

The examples assume the supplied values are valid and use compatible units.

---

# 33. Section 1 — Twelve Arithmetic Operator Examples

The Python file contains twelve examples.

This section explains each example separately.

## Example 1: Addition Operator

Concept:

The addition operator adds two numbers.

Code:

```python
first = 10
second = 20

result = first + second

print("Result:", result)
```

Output:

```text
Result: 30
```

Explanation:

The `+` operator combines the two integer values through addition.

The result is stored in the variable `result`.

## Example 2: Subtraction Operator

Concept:

The subtraction operator calculates the difference between two numbers.

Code:

```python
first = 50
second = 20

result = first - second

print("Result:", result)
```

Output:

```text
Result: 30
```

Explanation:

The second operand is subtracted from the first operand.

The order is important because subtraction is not commutative.

## Example 3: Multiplication Operator

Concept:

The multiplication operator multiplies two values.

Code:

```python
first = 10
second = 5

result = first * second

print("Result:", result)
```

Output:

```text
Result: 50
```

Explanation:

The `*` operator calculates the product.

## Example 4: Division Operator

Concept:

The division operator divides one number by another.

Code:

```python
first = 20
second = 4

result = first / second

print("Result:", result)
print("Type:", type(result).__name__)
```

Output:

```text
Result: 5.0
Type: float
```

Explanation:

The `/` operator performs ordinary division.

The result is a floating-point value.

## Example 5: Floor Division Operator

Concept:

Floor division returns the floored quotient.

Code:

```python
first = 17
second = 5

result = first // second

print("Result:", result)
```

Output:

```text
Result: 3
```

Explanation:

Ordinary division produces `3.4`.

Floor division returns the floor of the quotient, which is `3`.

## Example 6: Modulus Operator

Concept:

The modulus operator returns the remainder.

Code:

```python
first = 17
second = 5

result = first % second

print("Remainder:", result)
```

Output:

```text
Remainder: 2
```

Explanation:

17 divided by 5 gives quotient 3 and remainder 2.

## Example 7: Exponentiation Operator

Concept:

The exponentiation operator calculates a power.

Code:

```python
base = 2
exponent = 5

result = base ** exponent

print("Result:", result)
```

Output:

```text
Result: 32
```

Explanation:

The expression means:

\[
2^5 = 32
\]

## Example 8: Unary Operators

Concept:

Unary plus and unary minus work with one operand.

Code:

```python
number = 25

print(+number)
print(-number)
```

Output:

```text
25
-25
```

Explanation:

Unary plus preserves the sign.

Unary minus changes the sign.

## Example 9: Negative Floor Division

Concept:

Floor division with negative values rounds down toward negative infinity.

Code:

```python
first = -17
second = 5

quotient = first // second
remainder = first % second

print("Quotient:", quotient)
print("Remainder:", remainder)
```

Output:

```text
Quotient: -4
Remainder: 3
```

Explanation:

The ordinary quotient is `-3.4`.

Its floor is `-4`.

The quotient and remainder satisfy:

\[
-17 = (5 \times -4) + 3
\]

## Example 10: Operator Precedence

Concept:

Multiplication has higher precedence than addition.

Code:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Explanation:

Python evaluates multiplication first.

```text
10 + (5 * 2)
10 + 10
20
```

## Example 11: Parentheses and Grouping

Concept:

Parentheses change expression grouping.

Code:

```python
first = 10 + 5 * 2
second = (10 + 5) * 2

print(first)
print(second)
```

Output:

```text
20
30
```

Explanation:

In the first expression, multiplication is performed first.

In the second expression, addition is performed first because of the parentheses.

## Example 12: `divmod()` Function

Concept:

The `divmod()` function returns quotient and remainder together.

Code:

```python
quotient, remainder = divmod(17, 5)

print("Quotient:", quotient)
print("Remainder:", remainder)
```

Output:

```text
Quotient: 3
Remainder: 2
```

Explanation:

The returned tuple contains two values.

The first is the quotient.

The second is the remainder.

---

# 34. Section 2 — Twelve Solved Problems

The Python file includes twelve interactive solved problems.

These problems use arithmetic operators to solve practical tasks.

## Solved Problem 1: Addition of Two Numbers

Task:

Write a program to accept two integers and calculate their sum.

Code:

```python
first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))

result = first + second

print("Sum:", result)
```

Sample input:

```text
Enter first integer: 10
Enter second integer: 20
```

Output:

```text
Sum: 30
```

Explanation:

Both inputs are converted into integers.

The addition operator calculates their sum.

## Solved Problem 2: Subtraction of Two Numbers

Task:

Write a program to subtract the second number from the first number.

Code:

```python
first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))

result = first - second

print("Difference:", result)
```

Sample input:

```text
Enter first integer: 50
Enter second integer: 20
```

Output:

```text
Difference: 30
```

Explanation:

The subtraction operator calculates the difference.

The order of the operands matters.

## Solved Problem 3: Multiplication of Two Numbers

Task:

Write a program to multiply two integers.

Code:

```python
first = int(input("Enter first integer: "))
second = int(input("Enter second integer: "))

result = first * second

print("Product:", result)
```

Sample input:

```text
Enter first integer: 10
Enter second integer: 5
```

Output:

```text
Product: 50
```

Explanation:

The multiplication operator calculates the product.

## Solved Problem 4: Division of Two Numbers

Task:

Write a program to divide two numbers and handle division by zero.

Code:

```python
first = float(input("Enter dividend: "))
second = float(input("Enter divisor: "))

if second == 0:
    print("Division by zero is not allowed.")
else:
    result = first / second
    print("Quotient:", result)
```

Sample input:

```text
Enter dividend: 20
Enter divisor: 4
```

Output:

```text
Quotient: 5.0
```

Explanation:

The program validates the divisor before performing division.

If the divisor is zero, the division is not performed.

## Solved Problem 5: Floor Division

Task:

Write a program to calculate the floor quotient of two integers.

Code:

```python
first = int(input("Enter dividend: "))
second = int(input("Enter divisor: "))

if second == 0:
    print("Division by zero is not allowed.")
else:
    result = first // second
    print("Floor Quotient:", result)
```

Sample input:

```text
Enter dividend: 17
Enter divisor: 5
```

Output:

```text
Floor Quotient: 3
```

Explanation:

The `//` operator returns the floor of the quotient.

## Solved Problem 6: Find the Remainder

Task:

Write a program to find the remainder after dividing two integers.

Code:

```python
first = int(input("Enter dividend: "))
second = int(input("Enter divisor: "))

if second == 0:
    print("Modulus by zero is not allowed.")
else:
    result = first % second
    print("Remainder:", result)
```

Sample input:

```text
Enter dividend: 17
Enter divisor: 5
```

Output:

```text
Remainder: 2
```

Explanation:

The modulus operator returns the remainder.

## Solved Problem 7: Calculate Power

Task:

Write a program to calculate a number raised to a power.

Code:

```python
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

try:
    result = base ** exponent
    print("Power:", result)

except (OverflowError, ZeroDivisionError) as error:
    print("Unable to calculate the requested power.")
    print("Reason:", error)
```

Sample input:

```text
Enter base: 2
Enter exponent: 5
```

Output:

```text
Power: 32
```

Explanation:

The `**` operator calculates the exponentiation.

The program also handles the expected exceptional cases in its implementation.

## Solved Problem 8: Even or Odd Checker

Task:

Write a program to determine whether a number is even or odd.

Code:

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

Sample input:

```text
Enter an integer: 10
```

Output:

```text
Even Number
```

Explanation:

An even integer has a remainder of zero when divided by two.

An odd integer has a nonzero remainder of one or negative one, depending on its sign.

## Solved Problem 9: Find the Last Digit

Task:

Write a program to find the last decimal digit of an integer.

Code:

```python
number = int(input("Enter an integer: "))

last_digit = abs(number) % 10

print("Last Digit:", last_digit)
```

Sample input:

```text
Enter an integer: 12345
```

Output:

```text
Last Digit: 5
```

Explanation:

`abs()` obtains the non-negative magnitude.

The modulus operator extracts the last decimal digit.

## Solved Problem 10: Swap Two Numbers

Task:

Write a program to swap two numbers using Python assignment.

Code:

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("Before Swapping:")
print("First:", first)
print("Second:", second)

first, second = second, first

print("After Swapping:")
print("First:", first)
print("Second:", second)
```

Sample input:

```text
Enter first number: 10
Enter second number: 20
```

Output:

```text
Before Swapping:
First: 10
Second: 20

After Swapping:
First: 20
Second: 10
```

Explanation:

Python evaluates the right-hand side and then assigns the values to the corresponding variables.

## Solved Problem 11: Average of Three Numbers

Task:

Write a program to calculate the average of three numbers.

Code:

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))

total = first + second + third

average = total / 3

print("Total:", total)
print(f"Average: {average:.2f}")
```

Sample input:

```text
Enter first number: 80
Enter second number: 90
Enter third number: 70
```

Output:

```text
Total: 240.0
Average: 80.00
```

Explanation:

The three values are added.

The sum is divided by three.

The f-string displays the average with two decimal places.

## Solved Problem 12: Combined Arithmetic Expression

Task:

Write a program to evaluate:

\[
(a+b)\times c-d
\]

Code:

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
third = float(input("Enter third number: "))
fourth = float(input("Enter fourth number: "))

result = (first + second) * third - fourth

print("Result:", result)
```

Sample input:

```text
Enter first number: 10
Enter second number: 5
Enter third number: 2
Enter fourth number: 4
```

Output:

```text
Result: 26.0
```

Explanation:

First, the two initial values are added.

Then the result is multiplied by the third value.

Finally, the fourth value is subtracted.

---

# 35. Understanding the Helper Functions

The Python file contains helper functions that simplify input handling and output formatting.

These functions avoid unnecessary repetition.

## 35.1 `print_heading()`

Purpose:

Display a formatted heading.

Syntax:

```python
print_heading("SECTION TITLE")
```

Example output:

```text
=================================================================
                         SECTION TITLE
=================================================================
```

Why is it useful?

- Separates program sections.
- Makes the output readable.
- Provides consistent formatting.
- Avoids repeating heading-printing logic.

## 35.2 `read_int()`

Purpose:

Read a valid integer from the user.

Syntax:

```python
number = read_int("Enter an integer: ")
```

Behavior:

1. Displays the prompt.
2. Reads user input.
3. Attempts integer conversion.
4. Catches `ValueError`.
5. Displays an error message if conversion fails.
6. Requests input again.
7. Returns the valid integer.

Example interaction:

```text
Enter an integer: hello
Invalid input! Please enter a valid integer.
Enter an integer: 25
```

The function returns:

```python
25
```

## 35.3 `read_float()`

Purpose:

Read a valid finite floating-point value.

Syntax:

```python
number = read_float("Enter a number: ")
```

The helper:

- Converts the input using `float()`.
- Handles invalid numeric text.
- Rejects `NaN`.
- Rejects positive infinity.
- Rejects negative infinity.
- Repeats until a finite number is accepted.

It uses:

```python
math.isfinite(value)
```

to check whether the number is finite.

## 35.4 `read_text()`

Purpose:

Read non-empty text.

Syntax:

```python
name = read_text("Enter your name: ")
```

The helper removes surrounding whitespace using `strip()`.

It rejects an empty result.

## 35.5 Why Use Helper Functions?

Helper functions:

1. Reduce repeated code.
2. Improve readability.
3. Centralize input handling.
4. Simplify error handling.
5. Make the main program easier to understand.
6. Make programs easier to maintain.

---

# 36. Understanding the Solved Problems Mapping

The Python file contains a dictionary named:

```python
SOLVED_PROBLEMS
```

It maps problem numbers to problem titles and their corresponding functions.

Example:

```python
SOLVED_PROBLEMS = {
    1: ("Addition", problem_01_addition),
    2: ("Subtraction", problem_02_subtraction)
}
```

## 36.1 Why Use a Dictionary?

A dictionary allows related problem information to be organized using keys.

In this program:

- The key identifies the problem number.
- The first tuple item stores the title.
- The second tuple item stores the function.

## 36.2 Displaying Problems

The program uses:

```python
show_solved_problems()
```

to display the available problem titles.

## 36.3 Running Problems

The program uses:

```python
run_solved_problems()
```

to accept a problem selection and execute the corresponding function.

## 36.4 Why Separate These Functions?

Separating problem listing from problem execution makes the program more organized.

It also allows users to select an individual exercise rather than running every solved problem automatically.

---

# 37. Section 3 — Ten Unsolved Practice Questions

The Python file contains ten unsolved practice questions.

Attempt these independently.

Do not immediately look for a complete solution.

The objective is to understand how to select and use arithmetic operators.

## Question 1: Sum of Three Integers

Write a program to accept three integers and calculate their sum.

Requirements:

- Read three integer values.
- Convert the input values.
- Use the addition operator.
- Display the final sum.

## Question 2: Difference Between Two Numbers

Write a program to calculate the difference between two user-entered numbers.

Requirements:

- Accept two integers.
- Compare the values.
- Calculate the difference between the larger and smaller value.
- Display the non-negative difference.

Hint:

Think about subtraction and comparison.

## Question 3: Area of a Rectangle

Write a program to calculate the area of a rectangle.

Formula:

\[
Area = Length \times Breadth
\]

Requirements:

- Accept length.
- Accept breadth.
- Use multiplication.
- Display the area.

## Question 4: Area of a Circle

Write a program to calculate the area of a circle.

Formula:

\[
Area = \pi \times Radius^2
\]

Requirements:

- Accept the radius.
- Use a suitable value of pi.
- Use exponentiation.
- Use multiplication.
- Display the area.

## Question 5: Quotient and Remainder Without `divmod()`

Write a program to calculate the quotient and remainder of two integers without using the `divmod()` function.

Requirements:

- Accept a dividend.
- Accept a divisor.
- Use `//`.
- Use `%`.
- Handle a zero divisor.
- Display both results.

## Question 6: Find the Last Two Digits

Write a program to find the last two decimal digits of a positive integer.

Requirements:

- Read an integer.
- Use the modulus operator.
- Extract the final two digits.
- Display the result.

Hint:

Consider the base-10 modulus operation.

## Question 7: Calculate Square and Cube

Write a program to calculate the square and cube of a number.

Formulas:

\[
Square = Number^2
\]

\[
Cube = Number^3
\]

Requirements:

- Accept a number.
- Use exponentiation.
- Display the square.
- Display the cube.

## Question 8: Convert Seconds into Hours, Minutes, and Seconds

Write a program that accepts total seconds and converts them into hours, minutes, and remaining seconds.

Requirements:

- Accept a non-negative integer.
- Calculate complete hours.
- Calculate remaining minutes.
- Calculate remaining seconds.
- Use floor division.
- Use modulus.

Hint:

There are 3600 seconds in one hour and 60 seconds in one minute.

## Question 9: Calculate Total Cost After Discount

Write a program to calculate the total cost of products and apply a discount.

Requirements:

- Read product price.
- Read quantity.
- Read discount percentage.
- Calculate the original total.
- Calculate the discount amount.
- Calculate the final amount.
- Display all values.

Formula:

\[
Total = Price \times Quantity
\]

\[
Discount = \frac{Total \times DiscountPercentage}{100}
\]

\[
FinalAmount = Total - Discount
\]

## Question 10: Combined Arithmetic Expression

Write a program to evaluate a mathematical expression using at least four arithmetic operators and parentheses.

Requirements:

- Read suitable numeric values.
- Create an expression using multiple arithmetic operators.
- Use parentheses.
- Display the result.
- Explain the order of evaluation.

---

# 38. Section 4 — Learning Checklist

Use this checklist to review your understanding.

## Basic Concepts

- [ ] I understand what arithmetic operators are.
- [ ] I understand what operands are.
- [ ] I understand arithmetic expressions.
- [ ] I can identify operators in expressions.
- [ ] I can identify operands in expressions.
- [ ] I can use arithmetic operators with variables.
- [ ] I can use arithmetic operators with numeric literals.

## Addition

- [ ] I understand the addition operator.
- [ ] I can add two numbers.
- [ ] I can add multiple numbers.
- [ ] I can add floating-point values.
- [ ] I can calculate totals.

## Subtraction

- [ ] I understand the subtraction operator.
- [ ] I can subtract two numbers.
- [ ] I understand negative results.
- [ ] I can subtract negative values.
- [ ] I understand that operand order matters.

## Multiplication

- [ ] I understand the multiplication operator.
- [ ] I can multiply two numbers.
- [ ] I can multiply multiple values.
- [ ] I can calculate squares.
- [ ] I can calculate cubes.
- [ ] I can calculate product totals.

## Division

- [ ] I understand the division operator.
- [ ] I can divide two values.
- [ ] I understand why `/` commonly returns a float.
- [ ] I can handle division by zero.
- [ ] I can use division in mathematical formulas.

## Floor Division

- [ ] I understand the floor division operator.
- [ ] I can use `//`.
- [ ] I can distinguish `/` from `//`.
- [ ] I understand positive floor division.
- [ ] I understand negative floor division.
- [ ] I know that floor division rounds toward negative infinity.

## Modulus

- [ ] I understand the modulus operator.
- [ ] I can calculate remainders.
- [ ] I can check even and odd numbers.
- [ ] I can find the last digit.
- [ ] I understand negative modulus.
- [ ] I can use modulus in practical problems.

## Exponentiation

- [ ] I understand the exponentiation operator.
- [ ] I can calculate powers.
- [ ] I can calculate squares.
- [ ] I can calculate cubes.
- [ ] I understand negative exponents.
- [ ] I understand exponentiation precedence.

## Unary Operators

- [ ] I understand unary plus.
- [ ] I understand unary minus.
- [ ] I can distinguish unary minus from binary subtraction.
- [ ] I understand how signs affect numeric values.

## Expressions

- [ ] I understand operator precedence.
- [ ] I understand parentheses and grouping.
- [ ] I understand operator associativity.
- [ ] I can evaluate arithmetic expressions.
- [ ] I can use variables in expressions.
- [ ] I can explain expression evaluation step by step.

## Additional Concepts

- [ ] I can use `divmod()`.
- [ ] I can calculate quotient and remainder.
- [ ] I can validate a divisor.
- [ ] I can read integer input safely.
- [ ] I can read floating-point input safely.
- [ ] I can test boundary values.
- [ ] I can solve arithmetic programming problems.

---

# 39. Section 5 — Main Menu

The Python file provides an interactive learning menu.

The main menu contains the following options:

| Option | Purpose |
|---|---|
| `1` | View 12 arithmetic operator examples |
| `2` | Practice 12 solved problems |
| `3` | View 10 unsolved practice questions |
| `4` | View learning checklist |
| `0` | Exit the program |

## 39.1 Option 1: View Examples

This option displays all twelve arithmetic operator examples.

The examples cover:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Floor division.
- Modulus.
- Exponentiation.
- Unary operators.
- Negative floor division.
- Operator precedence.
- Parentheses.
- `divmod()`.

## 39.2 Option 2: Practice Solved Problems

This option displays twelve solved problems.

The user can select one problem at a time.

The program executes the selected problem.

## 39.3 Option 3: Unsolved Questions

This option displays ten practice questions.

These questions should be attempted independently.

## 39.4 Option 4: Learning Checklist

This option displays the checklist for reviewing arithmetic operator concepts.

## 39.5 Option 0: Exit

This option closes the program.

## 39.6 Invalid Menu Choices

If the user enters an unsupported menu choice, the program displays an error message.

The menu is displayed again.

This allows the user to continue using the program.

---

# 40. How to Run the Python Program

Make sure Python 3 is installed on your system.

Open PowerShell or the terminal.

Move to the repository root folder:

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"
```

Run the Python file:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\01-Arithmetic-Operators\01_arithmetic_operators.py"
```

If the `python` command is not recognized, try the Python launcher:

```powershell
py "PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\01-Arithmetic-Operators\01_arithmetic_operators.py"
```

The exact command depends on your Python installation.

## 40.1 Run from the Topic Folder

You can also open the topic folder directly:

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\01-Arithmetic-Operators"
```

Then execute:

```powershell
python "01_arithmetic_operators.py"
```

---

# 41. Sample Program Execution

When the program starts, it displays the main menu.

Example:

```text
=================================================================
                 WELCOME TO ARITHMETIC OPERATORS
=================================================================

Learn and practice Python arithmetic operators.
Study the examples and solve the programming problems.

=================================================================
                 PYTHON ARITHMETIC OPERATORS
=================================================================
1. View 12 Arithmetic Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
=================================================================
Enter your choice:
```

## 41.1 Select Option 1

Enter:

```text
1
```

The program displays the twelve arithmetic operator examples.

## 41.2 Select Option 2

Enter:

```text
2
```

The program displays the twelve solved problems.

Example:

```text
01. Addition of Two Numbers
02. Subtraction of Two Numbers
03. Multiplication of Two Numbers
04. Division of Two Numbers
05. Floor Division
06. Find the Remainder
07. Calculate Power
08. Even or Odd Checker
09. Find the Last Digit
10. Swap Two Numbers
11. Average of Three Numbers
12. Combined Arithmetic Expression
```

Select a problem number to execute it.

## 41.3 Select Option 3

Enter:

```text
3
```

The program displays ten unsolved practice questions.

## 41.4 Select Option 4

Enter:

```text
4
```

The program displays the learning checklist.

## 41.5 Select Option 0

Enter:

```text
0
```

The program exits.

---

# 42. Common Mistakes

Beginners frequently make mistakes while using arithmetic operators.

## Mistake 1: Confusing Division and Floor Division

Example:

```python
print(10 / 3)
print(10 // 3)
```

The first expression performs ordinary division.

The second performs floor division.

## Mistake 2: Using `^` Instead of `**`

Incorrect exponentiation:

```python
# result = 2 ^ 3
```

The `^` operator means bitwise XOR.

Correct exponentiation:

```python
result = 2 ** 3
```

## Mistake 3: Forgetting Operator Precedence

```python
result = 10 + 5 * 2
```

The result is `20`, not `30`.

Multiplication is evaluated before addition.

## Mistake 4: Forgetting Parentheses

If addition must happen before multiplication, use:

```python
result = (10 + 5) * 2
```

## Mistake 5: Ignoring Division by Zero

Incorrect:

```python
# result = 10 / 0
```

Correct:

```python
if divisor != 0:
    result = dividend / divisor
else:
    print("Divisor cannot be zero.")
```

## Mistake 6: Confusing Floor Division with Truncation

```python
print(int(-17 / 5))
print(-17 // 5)
```

Output:

```text
-3
-4
```

`int()` truncates toward zero.

`//` performs floor division.

## Mistake 7: Misunderstanding Negative Modulus

```python
print(-17 % 5)
```

Output:

```text
3
```

Python's remainder follows the sign of the divisor when the remainder is nonzero.

## Mistake 8: Forgetting to Convert User Input

Incorrect:

```python
first = input("First: ")
second = input("Second: ")

print(first + second)
```

Numeric-looking input is returned as text.

Correct:

```python
first = int(input("First: "))
second = int(input("Second: "))

print(first + second)
```

## Mistake 9: Using the Wrong Operand Order

Subtraction is not commutative.

```python
print(20 - 10)
print(10 - 20)
```

The results are different.

## Mistake 10: Assuming Every Arithmetic Operation Returns an Integer

Ordinary division generally produces a float.

Example:

```python
print(10 / 2)
```

Output:

```text
5.0
```

## Mistake 11: Forgetting to Handle Invalid Numeric Input

Direct conversion can raise `ValueError`.

Use suitable exception handling when input may be invalid.

## Mistake 12: Writing Unnecessarily Complex Expressions

Long expressions may be difficult to understand.

Use meaningful intermediate variables and parentheses when appropriate.

---

# 43. Error Handling

Arithmetic programs may encounter different errors.

Understanding these errors helps create reliable programs.

## 43.1 `ZeroDivisionError`

This exception occurs when an ordinary numeric division, floor division, or modulus operation uses a zero divisor.

Example:

```python
# print(10 / 0)
```

Handling:

```python
divisor = 0

if divisor != 0:
    print(10 / divisor)
else:
    print("Division by zero is not allowed.")
```

## 43.2 `ValueError`

This exception commonly occurs when text cannot be converted into the required numeric type.

Example:

```python
# int("hello")
```

Handling:

```python
try:
    number = int(input("Enter number: "))
    print(number)

except ValueError:
    print("Please enter a valid integer.")
```

## 43.3 `OverflowError`

Some arithmetic operations involving floating-point values can raise `OverflowError` when a result cannot be represented.

Very large integer calculations are also subject to practical resource limits, even though Python integers support arbitrary precision.

## 43.4 Why Use Exception Handling?

Exception handling helps a program:

- Handle expected failures.
- Display useful messages.
- Avoid unexpected termination for handled errors.
- Allow users to correct invalid input.
- Separate input errors from other program errors.

---

# 44. Debugging Techniques

Debugging helps identify and correct problems in arithmetic expressions.

Follow these steps when an arithmetic result is incorrect.

## Step 1: Identify the Expression

Find the expression that produces the unexpected result.

## Step 2: Identify the Operands

Write down each value involved in the expression.

## Step 3: Check Data Types

Use:

```python
print(type(first))
print(type(second))
```

## Step 4: Check the Operator

Confirm that the correct operator is being used.

Examples:

- `*` for multiplication.
- `/` for ordinary division.
- `//` for floor division.
- `%` for remainder.
- `**` for exponentiation.

## Step 5: Check Operator Precedence

Determine which operations are performed first.

## Step 6: Add Parentheses

Use parentheses to make the intended grouping clear.

## Step 7: Calculate Smaller Parts

Break a complex expression into intermediate variables.

Example:

```python
first = 10 + 5
second = 3 * 2

result = first + second

print(result)
```

## Step 8: Check Division by Zero

Verify that the divisor is not zero.

## Step 9: Test Negative Values

Negative values can reveal mistakes involving floor division and modulus.

## Step 10: Run the Program Again

After correcting the expression, test several inputs.

---

# 45. Testing Strategy

Testing verifies whether arithmetic operations produce the expected results.

A program should be tested using different values.

## 45.1 Addition Tests

| First | Second | Expected Result |
|---:|---:|---:|
| 10 | 20 | 30 |
| 0 | 10 | 10 |
| -10 | 5 | -5 |
| -10 | -5 | -15 |
| 100 | 200 | 300 |

## 45.2 Subtraction Tests

| First | Second | Expected Result |
|---:|---:|---:|
| 20 | 10 | 10 |
| 10 | 20 | -10 |
| 0 | 10 | -10 |
| -10 | -5 | -5 |
| 10 | -5 | 15 |

## 45.3 Multiplication Tests

| First | Second | Expected Result |
|---:|---:|---:|
| 10 | 5 | 50 |
| 0 | 10 | 0 |
| -5 | 4 | -20 |
| -5 | -4 | 20 |
| 2 | 10 | 20 |

## 45.4 Division Tests

| First | Second | Expected Result |
|---:|---:|---|
| 10 | 2 | `5.0` |
| 10 | 5 | `2.0` |
| 7 | 2 | `3.5` |
| -10 | 2 | `-5.0` |
| 10 | 0 | `ZeroDivisionError` if attempted |

## 45.5 Floor Division Tests

| First | Second | Expected Result |
|---:|---:|---:|
| 17 | 5 | 3 |
| 20 | 5 | 4 |
| -17 | 5 | -4 |
| 17 | -5 | -4 |
| -17 | -5 | 3 |

## 45.6 Modulus Tests

| First | Second | Expected Result |
|---:|---:|---:|
| 17 | 5 | 2 |
| 20 | 5 | 0 |
| -17 | 5 | 3 |
| 17 | -5 | -3 |
| -17 | -5 | -2 |

## 45.7 Exponentiation Tests

| Base | Exponent | Expected Result |
|---:|---:|---:|
| 2 | 3 | 8 |
| 5 | 2 | 25 |
| 3 | 3 | 27 |
| 10 | 0 | 1 |
| 2 | -2 | 0.25 |

## 45.8 Expression Tests

Test expressions with:

- Addition only.
- Subtraction only.
- Multiplication and addition.
- Division and multiplication.
- Exponentiation.
- Parentheses.
- Negative values.
- Multiple operators.

## 45.9 Error Tests

Test:

- Invalid integer text.
- Invalid float text.
- Empty numeric input.
- Zero divisor.
- Negative values.
- Very large values.
- Very small floating-point values.

---

# 46. Boundary Testing

Boundary testing checks values at or around important limits.

It is especially useful for arithmetic programs.

## 46.1 Zero

Test:

```python
number = 0
```

Zero is important for multiplication, division, modulus, and exponentiation.

## 46.2 Positive Numbers

Test:

```text
1
2
10
100
```

## 46.3 Negative Numbers

Test:

```text
-1
-2
-10
-100
```

## 46.4 Division Boundaries

Test:

```text
10 / 1
10 / 2
10 / 0
```

The zero divisor should be rejected before ordinary division is performed.

## 46.5 Modulus Boundaries

Test:

```text
10 % 1
10 % 2
10 % 10
```

## 46.6 Exponent Boundaries

Test:

```text
2 ** 0
2 ** 1
2 ** 2
2 ** -1
```

## 46.7 Why Is Boundary Testing Important?

It helps discover errors that may not appear with ordinary positive input values.

---

# 47. Arithmetic Operators in DSA

Arithmetic operators are essential for Data Structures and Algorithms.

Many DSA problems involve numerical operations and index calculations.

## 47.1 Even or Odd

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

This is one of the most common uses of modulus in basic DSA.

## 47.2 Find the Last Digit

For a non-negative integer:

```python
number = 12345

last_digit = number % 10

print(last_digit)
```

## 47.3 Remove the Last Digit

For a non-negative integer:

```python
number = 12345

number = number // 10

print(number)
```

## 47.4 Calculate a Midpoint

```python
left = 0
right = 10

middle = (left + right) // 2

print(middle)
```

Midpoint calculations are used in binary search.

The exact expression used should also account for the algorithm's range and integer-safety requirements in languages with fixed-width integers.

## 47.5 Calculate Powers

```python
number = 5

square = number ** 2
cube = number ** 3

print(square)
print(cube)
```

## 47.6 Convert Seconds

```python
total_seconds = 3675

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)
```

Output:

```text
1 1 15
```

## 47.7 DSA Importance

Arithmetic operators are used in:

- Array indexing.
- Binary search.
- Number reversal.
- Digit extraction.
- Divisibility checks.
- Mathematical algorithms.
- Sorting calculations.
- Prefix sums.
- Bitwise algorithms.
- Competitive programming.

---

# 48. Applications in Searching and Sorting

Arithmetic operators are used when working with searching and sorting algorithms.

## 48.1 Binary Search Midpoint

A binary search algorithm commonly calculates a midpoint.

```python
left = 0
right = 10

middle = (left + right) // 2

print(middle)
```

The floor division operator ensures an integer index for integer operands.

## 48.2 Array Index Calculations

Arithmetic operators can be used to calculate positions.

```python
index = 10

next_index = index + 1
previous_index = index - 1

print(next_index)
print(previous_index)
```

## 48.3 Loop Counters

```python
counter = 0

counter = counter + 1

print(counter)
```

## 48.4 Sorting Calculations

Arithmetic operations may be used when calculating partitions, midpoints, distances, or other quantities required by an algorithm.

## 48.5 Important Note

Arithmetic operators are only one part of searching and sorting.

You will study complete searching and sorting algorithms separately in the DSA sections.

---

# 49. Applications in Number Theory

Number theory is an important area of mathematics used in programming.

Arithmetic operators are used in many number theory problems.

## 49.1 Divisibility

A number is divisible by another integer when the remainder is zero.

```python
number = 20
divisor = 5

if number % divisor == 0:
    print("Divisible")
else:
    print("Not divisible")
```

## 49.2 Even and Odd

```python
number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 49.3 Extract the Last Digit

```python
number = 1234

last_digit = number % 10

print(last_digit)
```

## 49.4 Remove the Last Digit

```python
number = 1234

remaining = number // 10

print(remaining)
```

## 49.5 Sum of Digits

```python
number = 1234

total = 0

while number > 0:
    digit = number % 10

    total += digit

    number = number // 10

print(total)
```

Output:

```text
10
```

This example combines modulus, floor division, addition, and assignment.

## 49.6 Greatest Common Divisor

The Euclidean algorithm uses remainder operations.

```python
first = 48
second = 18

while second != 0:
    first, second = second, first % second

print("GCD:", first)
```

Output:

```text
GCD: 6
```

The modulus operator makes this algorithm possible.

---

# 50. Best Practices

Follow these practices while using arithmetic operators.

## 50.1 Choose the Correct Operator

Use the operator that matches the required calculation.

## 50.2 Understand Division

Know the difference between `/` and `//`.

## 50.3 Understand Negative Values

Always consider how floor division and modulus behave with negative operands.

## 50.4 Validate Divisors

Do not perform division or modulus with a zero divisor.

## 50.5 Use Parentheses for Clarity

Group complex expressions carefully.

## 50.6 Understand Precedence

Do not assume that all operations are performed from left to right.

## 50.7 Use Appropriate Numeric Types

Use integers for whole-number calculations and floating-point values when decimal values are required.

## 50.8 Handle Input Errors

Use appropriate exception handling when converting user input.

## 50.9 Test Boundary Values

Test zero, negative values, and values close to important limits.

## 50.10 Avoid Unnecessary Complexity

Use intermediate variables when a calculation becomes difficult to understand.

## 50.11 Keep Expressions Readable

Write expressions that another programmer can easily understand.

## 50.12 Practice Regularly

Arithmetic operators become easier to use through repeated problem-solving practice.

---

# 51. Code Readability

Readable code makes arithmetic programs easier to understand.

## 51.1 Use Meaningful Variable Names

Good:

```python
total_price = 500
quantity = 4
```

Less descriptive:

```python
x = 500
y = 4
```

Meaningful names communicate the purpose of a value.

## 51.2 Use Spaces Around Operators

Preferred:

```python
result = first + second
```

This improves readability.

## 51.3 Break Complex Calculations into Steps

Instead of writing an unnecessarily complicated expression, use intermediate variables.

```python
first_total = 10 + 20

second_total = 5 * 2

result = first_total + second_total

print(result)
```

## 51.4 Use Parentheses

Parentheses make grouping clear.

## 51.5 Add Comments When Needed

Comments should explain logic that may not be obvious.

Example:

```python
# Calculate the remaining quantity after full groups.
remainder = total_items % group_size
```

---

# 52. Mini Project Ideas

After completing the arithmetic operator examples and solved problems, try these projects.

## Project 1: Basic Calculator

Requirements:

- Accept two numbers.
- Perform addition.
- Perform subtraction.
- Perform multiplication.
- Perform division.
- Perform floor division.
- Calculate modulus.
- Calculate exponentiation.
- Handle division by zero.

Skills practiced:

- Arithmetic operators.
- Input conversion.
- Conditions.
- Output formatting.
- Error handling.

## Project 2: Even or Odd Checker

Requirements:

- Accept an integer.
- Use the modulus operator.
- Display whether the number is even or odd.
- Test positive, negative, and zero values.

Skills practiced:

- Modulus.
- Comparison.
- Conditional statements.

## Project 3: Student Marks Calculator

Requirements:

- Accept marks for five subjects.
- Calculate total.
- Calculate average.
- Calculate percentage when the maximum marks are known.
- Display the result.

Skills practiced:

- Addition.
- Division.
- Multiplication.
- Input conversion.
- Formatted output.

## Project 4: Shopping Bill Generator

Requirements:

- Accept product price.
- Accept product quantity.
- Calculate the total.
- Accept a discount percentage.
- Calculate the discount.
- Calculate the final amount.
- Display a formatted bill.

Skills practiced:

- Multiplication.
- Division.
- Subtraction.
- Arithmetic expressions.
- Input validation.

## Project 5: Temperature Converter

Requirements:

- Accept temperature in Celsius.
- Convert it to Fahrenheit.
- Display the result.
- Format the decimal value.

Formula:

\[
F = \frac{9}{5}C + 32
\]

## Project 6: Time Converter

Requirements:

- Accept total seconds.
- Calculate complete hours.
- Calculate remaining minutes.
- Calculate remaining seconds.
- Use floor division and modulus.

Skills practiced:

- Floor division.
- Modulus.
- Arithmetic expressions.

## Project 7: Number Analyzer

Requirements:

- Accept an integer.
- Find its square.
- Find its cube.
- Find its last digit.
- Check even or odd.
- Display the results.

Skills practiced:

- Exponentiation.
- Modulus.
- Arithmetic operators.
- Conditional statements.

## Project 8: Area Calculator

Requirements:

- Calculate the area of a rectangle.
- Calculate the area of a square.
- Calculate the area of a circle.
- Accept input values.
- Display results.

Skills practiced:

- Multiplication.
- Exponentiation.
- Floating-point arithmetic.

## Project 9: Quotient and Remainder Calculator

Requirements:

- Accept a dividend.
- Accept a divisor.
- Calculate the quotient.
- Calculate the remainder.
- Validate the divisor.
- Display results.

Skills practiced:

- Floor division.
- Modulus.
- `divmod()`.

## Project 10: Arithmetic Expression Evaluator

Requirements:

- Accept several numeric values.
- Construct an arithmetic expression.
- Use at least four operators.
- Use parentheses.
- Display the result.
- Explain expression evaluation.

Skills practiced:

- Arithmetic operators.
- Precedence.
- Parentheses.
- Associativity.

---

# 53. Frequently Asked Questions

## Q1. What are arithmetic operators?

Arithmetic operators are symbols used to perform mathematical calculations on numeric values.

## Q2. How many main arithmetic operators are covered in this topic?

Seven main binary arithmetic operators are covered:

- `+`
- `-`
- `*`
- `/`
- `//`
- `%`
- `**`

Unary plus and unary minus are also covered.

## Q3. What is the addition operator?

The `+` operator adds numeric values.

## Q4. What is the subtraction operator?

The `-` operator subtracts the second operand from the first.

## Q5. What is the multiplication operator?

The `*` operator multiplies two values.

## Q6. What is the division operator?

The `/` operator performs ordinary division.

## Q7. What is floor division?

The `//` operator returns the floor of the quotient.

## Q8. What is the modulus operator?

The `%` operator returns the remainder of division.

## Q9. What is exponentiation?

Exponentiation calculates one value raised to a power using `**`.

## Q10. What is the difference between `/` and `//`?

`/` performs ordinary division.

`//` performs floor division.

## Q11. What is the difference between `//` and `%`?

`//` returns the floor quotient.

`%` returns the remainder.

## Q12. What is the result of `10 / 2`?

The result is `5.0`.

## Q13. What is the result of `10 // 3`?

The result is `3`.

## Q14. What is the result of `10 % 3`?

The result is `1`.

## Q15. What is the result of `2 ** 3`?

The result is `8`.

## Q16. What is a unary operator?

A unary operator performs an operation using one operand.

## Q17. What is unary plus?

Unary plus applies a positive sign to one operand.

## Q18. What is unary minus?

Unary minus applies a negative sign to one operand.

## Q19. Does floor division round towards zero?

No. Floor division rounds down toward negative infinity.

## Q20. What is the result of `-17 // 5`?

The result is `-4`.

## Q21. What is the result of `-17 % 5`?

The result is `3`.

## Q22. What happens when a number is divided by zero?

An ordinary numeric division by zero raises `ZeroDivisionError`.

## Q23. What is operator precedence?

Operator precedence determines which operations are grouped first in an expression.

## Q24. What are parentheses used for?

Parentheses explicitly group expressions and can change the evaluation order.

## Q25. What is associativity?

Associativity determines how operators with the same precedence are grouped.

## Q26. What is the associativity of exponentiation?

Exponentiation is right-associative.

## Q27. What does `divmod()` do?

It returns a tuple containing the quotient and remainder.

## Q28. How can an even number be identified using modulus?

An integer is even when its remainder after division by two is zero.

## Q29. How can the last digit of a non-negative integer be found?

Use the modulus operator with 10.

## Q30. Why are arithmetic operators important in DSA?

They are used in index calculations, number theory, digit extraction, searching, sorting, and many mathematical algorithms.

---

# 54. Viva Questions and Answers

Use these questions for practical examinations, classroom revision, and basic technical interviews.

## Basic Concepts

### 1. Define arithmetic operators.

Arithmetic operators are symbols used to perform mathematical operations on numeric values.

### 2. What is an operand?

An operand is a value on which an operator performs an operation.

### 3. What is an arithmetic expression?

It is a combination of numeric operands and arithmetic operators that produces a numerical result.

### 4. Name the seven main arithmetic operators in Python.

`+`, `-`, `*`, `/`, `//`, `%`, and `**`.

### 5. What is a unary operator?

An operator that works with one operand.

### 6. What is a binary operator?

An operator that works with two operands.

## Addition, Subtraction, and Multiplication

### 7. Which symbol represents addition?

`+`.

### 8. Which symbol represents subtraction?

`-`.

### 9. Which symbol represents multiplication?

`*`.

### 10. What is the result of `10 + 20`?

`30`.

### 11. What is the result of `50 - 20`?

`30`.

### 12. What is the result of `10 * 5`?

`50`.

### 13. Is subtraction commutative?

No. Changing operand order generally changes the result.

### 14. Is multiplication commutative for ordinary numeric values?

Yes. For ordinary numeric values, changing operand order does not change the product.

## Division and Modulus

### 15. Which symbol represents ordinary division?

`/`.

### 16. Which symbol represents floor division?

`//`.

### 17. What is the result of `10 / 2`?

`5.0`.

### 18. What is the result of `10 // 3`?

`3`.

### 19. What is the result of `10 % 3`?

`1`.

### 20. What is the difference between division and floor division?

Division returns the ordinary quotient, while floor division returns the floor of the quotient.

### 21. What does the modulus operator return?

It returns the remainder.

### 22. Which exception occurs when dividing by zero?

`ZeroDivisionError`.

### 23. How can an even number be identified?

Check whether `number % 2 == 0`.

### 24. How can the last digit of a positive integer be found?

Use `number % 10`.

## Exponentiation and Unary Operators

### 25. Which symbol represents exponentiation?

`**`.

### 26. What is the result of `2 ** 3`?

`8`.

### 27. What is the result of `5 ** 2`?

`25`.

### 28. What is unary plus?

It applies a positive sign to one operand.

### 29. What is unary minus?

It applies a negative sign to one operand.

### 30. What is the result of `-10`?

It represents negative ten.

## Negative Arithmetic

### 31. What is the result of `-17 // 5`?

`-4`.

### 32. Why is the result `-4` instead of `-3`?

Because floor division rounds down toward negative infinity.

### 33. What is the result of `-17 % 5`?

`3`.

### 34. What is the relationship between quotient, divisor, and remainder?

For integer division with a nonzero divisor:

\[
a = (a // b) \times b + (a \% b)
\]

## Precedence and Expressions

### 35. What is operator precedence?

It determines which operators are grouped first.

### 36. Which operation has higher precedence: addition or multiplication?

Multiplication.

### 37. What is the purpose of parentheses?

They explicitly group expressions.

### 38. What is operator associativity?

It determines grouping for operators with the same precedence.

### 39. Is exponentiation left-associative or right-associative?

Right-associative.

### 40. What is the result of `2 ** 3 ** 2`?

`512`.

### 41. What is the result of `10 + 5 * 2`?

`20`.

### 42. What is the result of `(10 + 5) * 2`?

`30`.

## Python Functions and Applications

### 43. What does `divmod()` return?

A tuple containing quotient and remainder.

### 44. Why is `divmod()` useful?

It returns quotient and remainder together.

### 45. How can invalid integer input be handled?

Use `try` and `except ValueError`.

### 46. Why should a divisor be checked?

To prevent an invalid division or modulus operation with zero.

### 47. Why are intermediate variables useful?

They make complicated calculations easier to understand and debug.

### 48. What is the main use of modulus in DSA?

It is commonly used in divisibility checks, even/odd checks, digit extraction, and number theory.

### 49. What is the use of floor division in DSA?

It is used in integer index calculations, grouping, and numerical algorithms.

### 50. What is the main objective of this topic?

To understand and apply Python arithmetic operators in mathematical and programming problems.

---

# 55. Quick Revision Tables

## 55.1 Arithmetic Operator Table

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor Division | `10 // 3` | 3 |
| `%` | Modulus | `10 % 3` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |

## 55.2 Unary Operator Table

| Expression | Operator | Result |
|---|---|---:|
| `+10` | Unary Plus | 10 |
| `-10` | Unary Minus | -10 |

## 55.3 Division Comparison

| Expression | Result | Meaning |
|---|---:|---|
| `17 / 5` | 3.4 | Ordinary division |
| `17 // 5` | 3 | Floor division |
| `17 % 5` | 2 | Remainder |
| `divmod(17, 5)` | `(3, 2)` | Quotient and remainder |

## 55.4 Negative Division Comparison

| Expression | Result |
|---|---:|
| `-17 // 5` | -4 |
| `17 // -5` | -4 |
| `-17 // -5` | 3 |
| `-17 % 5` | 3 |
| `17 % -5` | -3 |
| `-17 % -5` | -2 |

## 55.5 Precedence Table

| Priority | Operator | Meaning |
|---:|---|---|
| Highest for these arithmetic expressions | `**` | Exponentiation |
| Next | Unary `+`, `-` | Unary plus and minus |
| Next | `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulus |
| Lowest among these groups | `+`, `-` | Addition and subtraction |

Parentheses provide explicit grouping.

## 55.6 Common Mathematical Formulas

| Calculation | Formula |
|---|---|
| Sum | `a + b` |
| Difference | `a - b` |
| Product | `a * b` |
| Quotient | `a / b` |
| Floor Quotient | `a // b` |
| Remainder | `a % b` |
| Square | `n ** 2` |
| Cube | `n ** 3` |
| Average | `sum / count` |
| Rectangle Area | `length * breadth` |
| Circle Area | `pi * radius ** 2` |
| Simple Interest | `(P * R * T) / 100` |

## 55.7 Common Exceptions

| Exception | Cause |
|---|---|
| `ZeroDivisionError` | Division, floor division, or modulus by zero |
| `ValueError` | Invalid numeric text during conversion |
| `OverflowError` | Certain calculations exceed floating-point limits |

## 55.8 Important Functions

| Function | Purpose |
|---|---|
| `int()` | Convert suitable values into integers |
| `float()` | Convert suitable values into floats |
| `abs()` | Return the absolute value |
| `round()` | Round a value according to Python's rounding rules |
| `divmod()` | Return quotient and remainder |
| `type()` | Identify an object's type |
| `math.isfinite()` | Check whether a numeric value is finite |

---

# 56. Important Terminology

**Arithmetic Operator:** A symbol used to perform a mathematical operation.

**Operand:** A value on which an operator performs an operation.

**Expression:** A combination of values and operations that evaluates to a result.

**Addition:** The operation of combining numeric values.

**Subtraction:** The operation of finding the difference between values.

**Multiplication:** The operation of calculating a product.

**Division:** The operation of dividing one value by another.

**Floor Division:** Division that returns the floor of the quotient.

**Modulus:** The operation that returns a remainder.

**Exponentiation:** The operation of raising a value to a power.

**Unary Operator:** An operator that works with one operand.

**Binary Operator:** An operator that works with two operands.

**Unary Plus:** An operator that applies a positive sign.

**Unary Minus:** An operator that applies a negative sign.

**Dividend:** The value being divided.

**Divisor:** The value by which another value is divided.

**Quotient:** The result of a division operation.

**Remainder:** The part left after division under the applicable quotient and remainder rules.

**Operator Precedence:** Rules that determine which operations are grouped first.

**Operator Associativity:** Rules that determine grouping for operators of the same precedence.

**Parentheses:** Symbols used to group expressions.

**Integer:** A whole-number value represented by Python's `int` type.

**Float:** A floating-point value represented by Python's `float` type.

**Floating-Point Precision:** The limitations that arise because many decimal fractions cannot be represented exactly in binary floating-point format.

**ZeroDivisionError:** An exception raised by ordinary numeric division, floor division, or modulus when the divisor is zero.

**Absolute Value:** The non-negative magnitude of a real number, calculated using `abs()`.

**`divmod()`:** A built-in function returning quotient and remainder together.

**Number Theory:** A branch of mathematics involving integers and their properties.

**Divisibility:** The property of one integer being divisible by another without a remainder.

**Bit Manipulation:** Working with individual bits in numeric representations.

---

# 57. Final Summary

Arithmetic operators are essential for mathematical calculations in Python.

They allow programmers to add, subtract, multiply, divide, calculate remainders, and perform exponentiation.

This topic covers seven main binary arithmetic operators:

- Addition (`+`).
- Subtraction (`-`).
- Multiplication (`*`).
- Division (`/`).
- Floor Division (`//`).
- Modulus (`%`).
- Exponentiation (`**`).

It also introduces:

- Unary plus.
- Unary minus.
- Negative floor division.
- Negative modulus.
- Operator precedence.
- Parentheses and grouping.
- Operator associativity.
- Quotient and remainder.
- `divmod()`.

## Important Points to Remember

1. Arithmetic operators perform mathematical operations.
2. Operands are the values used by operators.
3. `+` performs addition for numeric operands.
4. `-` performs subtraction for numeric operands.
5. `*` performs multiplication.
6. `/` performs ordinary division.
7. `//` performs floor division.
8. `%` returns the remainder.
9. `**` performs exponentiation.
10. Unary plus applies a positive sign.
11. Unary minus applies a negative sign.
12. Floor division rounds down toward negative infinity.
13. Modulus follows the sign of the divisor when the remainder is nonzero.
14. Division by zero raises `ZeroDivisionError`.
15. Operator precedence determines expression grouping.
16. Parentheses can change expression grouping.
17. Exponentiation is right-associative.
18. `divmod()` returns quotient and remainder together.
19. Arithmetic operators are widely used in DSA.
20. Testing positive, negative, and zero values is important.

## Recommended Practice Order

Follow this sequence:

**First:** Addition and Subtraction

Understand how values are combined and how differences are calculated.

**Second:** Multiplication and Division

Understand products, quotients, and division results.

**Third:** Floor Division and Modulus

Learn quotient and remainder operations, including negative values.

**Fourth:** Exponentiation and Unary Operators

Learn powers and sign operations.

**Fifth:** Operator Precedence and Parentheses

Understand how mathematical expressions are grouped and evaluated.

**Sixth:** `divmod()`

Learn how to calculate quotient and remainder together.

**Seventh:** Solved Problems

Complete all twelve solved problems in the Python program.

**Eighth:** Unsolved Questions

Attempt all ten practice questions independently.

**Finally:** Mini Projects

Build a calculator, number analyzer, or another arithmetic-based program.

## Final Learning Goal

After completing this topic, you should be able to:

1. Identify Python arithmetic operators.
2. Understand operands and expressions.
3. Perform basic mathematical calculations.
4. Work with integers and floating-point values.
5. Use division, floor division, and modulus correctly.
6. Perform exponentiation.
7. Handle negative numbers correctly.
8. Understand operator precedence and associativity.
9. Use parentheses to control grouping.
10. Use `divmod()` to obtain quotient and remainder.
11. Handle division-by-zero errors.
12. Write arithmetic programs independently.
13. Apply arithmetic operators to basic DSA problems.

**Addition → Subtraction → Multiplication → Division → Floor Division → Modulus → Exponentiation → Expressions → Practical Problems**

This completes the foundation of Python Arithmetic Operators.