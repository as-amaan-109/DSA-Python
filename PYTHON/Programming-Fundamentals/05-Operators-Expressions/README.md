# Python Operators and Expressions

**Week:** 1 — Programming Fundamentals  
**Main Section:** Operators and Expressions  
**Language:** Python 3  
**Level:** Beginner to Intermediate  
**Purpose:** Understand Python operators, expressions, operator precedence, associativity, and how to construct and evaluate expressions in Python programs.

---

# Table of Contents

1. Introduction
2. About This Section
3. Learning Objectives
4. What Are Operators?
5. What Are Operands?
6. What Are Expressions?
7. Operators and Expressions in Programming
8. Why Operators Are Important
9. Complete Folder Structure
10. Overview of the Eight Main Sections
11. Section 1 — Arithmetic Operators
12. Section 2 — Assignment Operators
13. Section 3 — Comparison Operators
14. Section 4 — Logical Operators
15. Section 5 — Bitwise Operators
16. Section 6 — Membership Operators
17. Section 7 — Identity Operators
18. Section 8 — Expressions
19. Arithmetic Operators
20. Assignment Operators
21. Comparison Operators
22. Logical Operators
23. Bitwise Operators
24. Membership Operators
25. Identity Operators
26. Expressions and Their Evaluation
27. Operator Precedence
28. Operator Associativity
29. Parentheses and Grouping
30. Conditional Expressions
31. Unary and Binary Operators
32. Short-Circuit Evaluation
33. Chained Comparisons
34. Augmented Assignment
35. Walrus Operator
36. Matrix Multiplication Operator
37. Difference Between Equality and Identity
38. Difference Between Logical and Bitwise Operators
39. Difference Between Membership and Identity
40. Operator Categories at a Glance
41. Operator Precedence Reference
42. Expressions in Real Programs
43. Practical Examples
44. Solved Practical Programs
45. Applications in Data Structures and Algorithms
46. Operators in Searching and Sorting
47. Operators in Bit Manipulation
48. Operators in Conditional Logic
49. Operators in Mathematical Problems
50. Common Mistakes
51. Debugging Techniques
52. Testing Strategy
53. Boundary Testing
54. Best Practices
55. Code Readability
56. Writing Efficient Expressions
57. Real-Life Applications
58. Mini Project Ideas
59. Practice Questions
60. Practical Challenges
61. Recommended Learning Order
62. Study Strategy
63. Revision Notes
64. Quick Reference
65. Frequently Asked Questions
66. Viva Questions and Answers
67. Important Terminology
68. Learning Checklist
69. Final Summary

---

# 1. Introduction

Operators and expressions are fundamental concepts in Python programming.

Almost every program uses operators to perform calculations, compare values, make decisions, manipulate data, and evaluate conditions.

For example, consider a simple addition program:

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
- `+` is an arithmetic operator.
- `10` and `20` are operands.
- `first + second` is an expression.
- `result` stores the evaluated result.

Python provides several categories of operators.

The main categories covered in this section are:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators
8. Expressions

Each category serves a different purpose.

For example:

- Arithmetic operators perform mathematical calculations.
- Assignment operators associate values with variables.
- Comparison operators compare values.
- Logical operators combine or negate conditions.
- Bitwise operators manipulate integer bits.
- Membership operators check whether an element belongs to a collection.
- Identity operators check whether two references point to the same object.
- Expressions combine values and operators to produce results.

Understanding these concepts is important before learning conditional statements, loops, functions, data structures, and algorithms.

This section follows a structured path from basic operators to expression evaluation and practical applications.

---

# 2. About This Section

The `05-Operators-Expressions` folder is part of Week 1 — Programming Fundamentals.

It builds on the concepts learned in the previous sections:

- Variables.
- Data Types.
- Type Conversion.
- Input and Output.

After learning how to store values and understand their data types, the next step is learning how to use those values in operations.

This section explains how Python evaluates expressions and performs different operations.

The folder contains eight main sections.

| No. | Section | Main Purpose |
|---:|---|---|
| 1 | Arithmetic Operators | Perform mathematical calculations |
| 2 | Assignment Operators | Assign and update values |
| 3 | Comparison Operators | Compare values |
| 4 | Logical Operators | Combine and evaluate conditions |
| 5 | Bitwise Operators | Perform operations on integer bits |
| 6 | Membership Operators | Check whether values exist in collections |
| 7 | Identity Operators | Compare object identity |
| 8 | Expressions | Understand expression evaluation, precedence, and grouping |

The Expressions section contains five individual topics:

1. Expressions.
2. Operator Precedence.
3. Operator Associativity.
4. Parentheses and Grouping.
5. Conditional Expressions.

Each topic has a separate Python file and README file.

This parent README provides an overview of the complete section.

For detailed topic-specific explanations and coding exercises, refer to the corresponding child README files.

---

# 3. Learning Objectives

After completing this section, you should be able to understand and use the main Python operators.

## 3.1 Basic Concepts

- Define an operator.
- Define an operand.
- Explain an expression.
- Understand how Python evaluates expressions.
- Identify operators in Python code.
- Identify operands in an expression.
- Understand the difference between an operator and an expression.
- Explain why operators are used in programming.

## 3.2 Arithmetic Operators

- Use addition.
- Use subtraction.
- Use multiplication.
- Use division.
- Use floor division.
- Use modulus.
- Use exponentiation.
- Understand unary plus and unary minus.
- Perform mathematical calculations.
- Understand division by zero.

## 3.3 Assignment Operators

- Use the basic assignment operator.
- Understand augmented assignment.
- Use arithmetic assignment operators.
- Use bitwise assignment operators.
- Understand multiple assignment.
- Understand chained assignment.
- Use assignment in practical programs.
- Understand the optional assignment expression operator.

## 3.4 Comparison Operators

- Compare equal values.
- Compare unequal values.
- Compare greater and smaller values.
- Use greater-than-or-equal comparison.
- Use less-than-or-equal comparison.
- Understand chained comparisons.
- Evaluate comparison results.
- Understand Boolean comparison results.

## 3.5 Logical Operators

- Use `and`.
- Use `or`.
- Use `not`.
- Combine multiple conditions.
- Understand truthy and falsy values.
- Understand short-circuit evaluation.
- Create logical conditions.
- Use logical expressions in programs.

## 3.6 Bitwise Operators

- Understand binary representation.
- Use bitwise AND.
- Use bitwise OR.
- Use bitwise XOR.
- Use bitwise NOT.
- Use left shift.
- Use right shift.
- Understand bitwise assignment.
- Apply bitwise operations to simple problems.
- Understand their relevance to DSA.

## 3.7 Membership Operators

- Use `in`.
- Use `not in`.
- Check membership in strings.
- Check membership in lists.
- Check membership in tuples.
- Check membership in sets.
- Check membership in dictionaries.
- Understand membership testing.

## 3.8 Identity Operators

- Use `is`.
- Use `is not`.
- Understand object identity.
- Distinguish identity from equality.
- Understand reference comparisons.
- Check whether a value is `None`.
- Avoid common identity-related mistakes.

## 3.9 Expressions

- Understand expressions.
- Evaluate arithmetic expressions.
- Understand operator precedence.
- Understand operator associativity.
- Use parentheses.
- Group expressions correctly.
- Understand conditional expressions.
- Read complex expressions.
- Evaluate expressions step by step.
- Write clear and readable expressions.

## 3.10 Programming Skills

- Write programs using different operators.
- Combine multiple operators.
- Build expressions.
- Evaluate conditions.
- Perform bit manipulation.
- Debug expression-related errors.
- Solve mathematical programming problems.
- Prepare for DSA-related operator concepts.

---

# 4. What Are Operators?

An operator is a symbol or keyword that performs an operation on one or more operands.

For example:

```python
result = 10 + 20
```

Here:

- `+` is an operator.
- `10` is the first operand.
- `20` is the second operand.
- `10 + 20` is an expression.

The addition operator performs the operation.

The result is:

```text
30
```

## 4.1 Why Are Operators Used?

Operators are used to:

- Perform calculations.
- Assign values.
- Compare values.
- Evaluate conditions.
- Combine Boolean expressions.
- Manipulate binary representations.
- Check membership.
- Check object identity.
- Construct larger expressions.

## 4.2 Operators Can Have Different Numbers of Operands

Operators can be classified according to the number of operands they use.

### Unary Operator

A unary operator works with one operand.

Example:

```python
number = 10

print(-number)
```

The `-` operator is applied to one operand.

### Binary Operator

A binary operator works with two operands.

Example:

```python
result = 10 + 20
```

The `+` operator works with two operands.

### Conditional Expression

A conditional expression uses a condition and two possible result expressions.

Example:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"
```

The expression selects a result depending on the condition.

---

# 5. What Are Operands?

Operands are the values or objects on which operators perform operations.

Example:

```python
result = 15 * 5
```

Here:

- `15` is an operand.
- `5` is an operand.
- `*` is the operator.

## 5.1 Operands Can Be Literals

```python
result = 10 + 20
```

The operands are numeric literals.

## 5.2 Operands Can Be Variables

```python
first = 10
second = 20

result = first + second
```

The operands are variable names referring to values.

## 5.3 Operands Can Be Expressions

```python
result = (10 + 5) * 2
```

The multiplication operator uses the result of the grouped expression as one of its operands.

## 5.4 Important Point

Understanding operands helps you read expressions correctly.

Whenever you see an operator, identify which values or expressions it operates on.

---

# 6. What Are Expressions?

An expression is a combination of values, variables, operators, and sometimes function calls that Python evaluates to produce a value.

Example:

```python
10 + 20
```

The expression evaluates to:

```text
30
```

Another example:

```python
age >= 18
```

This expression evaluates to a Boolean result.

## 6.1 Simple Expression

```python
result = 10 + 5
```

## 6.2 Variable Expression

```python
first = 10
second = 20

result = first + second
```

## 6.3 Comparison Expression

```python
result = 10 > 5
```

Output:

```text
True
```

## 6.4 Logical Expression

```python
age = 20

result = age >= 18 and age <= 60

print(result)
```

## 6.5 Complex Expression

```python
first = 10
second = 5
third = 2

result = (first + second) * third - 4

print(result)
```

Expressions can become complex when multiple operators are combined.

Operator precedence and associativity determine how they are evaluated.

---

# 7. Operators and Expressions in Programming

Operators and expressions are used throughout a program.

Consider a student marks program:

```python
math_marks = 80
science_marks = 90
english_marks = 85

total = math_marks + science_marks + english_marks

average = total / 3

passed = average >= 40

print("Total:", total)
print("Average:", average)
print("Passed:", passed)
```

This program uses multiple categories of operators.

| Expression | Operator | Purpose |
|---|---|---|
| `math_marks + science_marks` | Arithmetic | Addition |
| `total / 3` | Arithmetic | Division |
| `average >= 40` | Comparison | Check minimum value |
| `=` | Assignment | Store calculated values |

A single program may use several operator categories together.

---

# 8. Why Operators Are Important

Operators make it possible to perform operations on data.

Without operators, programs would not be able to perform many of the calculations and decisions required by applications.

## 8.1 Mathematical Calculations

```python
total = 100 + 50
```

## 8.2 Value Updates

```python
count = 10

count += 1
```

## 8.3 Comparisons

```python
age = 20

print(age >= 18)
```

## 8.4 Logical Decisions

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

## 8.5 Bit Manipulation

```python
number = 10

print(number & 1)
```

## 8.6 Membership Checks

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

## 8.7 Identity Checks

```python
result = None

print(result is None)
```

## 8.8 Expression Evaluation

```python
result = (10 + 5) * 2
```

Operators are essential in:

- Calculators.
- Banking systems.
- Student management systems.
- Data structures.
- Sorting algorithms.
- Searching algorithms.
- Mathematical problems.
- Conditional statements.
- Loops.
- Database applications.
- Competitive programming.

---

# 9. Complete Folder Structure

The final structure of this section is:

```text
05-Operators-Expressions/
│
├── README.md
│
├── 01-Arithmetic-Operators/
│   ├── README.md
│   └── 01_arithmetic_operators.py
│
├── 02-Assignment-Operators/
│   ├── README.md
│   └── 01_assignment_operators.py
│
├── 03-Comparison-Operators/
│   ├── README.md
│   └── 01_comparison_operators.py
│
├── 04-Logical-Operators/
│   ├── README.md
│   └── 01_logical_operators.py
│
├── 05-Bitwise-Operators/
│   ├── README.md
│   └── 01_bitwise_operators.py
│
├── 06-Membership-Operators/
│   ├── README.md
│   └── 01_membership_operators.py
│
├── 07-Identity-Operators/
│   ├── README.md
│   └── 01_identity_operators.py
│
└── 08-Expressions/
    │
    ├── README.md
    │
    ├── 01-expressions/
    │   ├── 01_expressions.py
    │   └── README.md
    │
    ├── 02-operator-precedence/
    │   ├── 02_operator_precedence.py
    │   └── README.md
    │
    ├── 03-operator-associativity/
    │   ├── 03_operator_associativity.py
    │   └── README.md
    │
    ├── 04-parentheses-and-grouping/
    │   ├── 04_parentheses_and_grouping.py
    │   └── README.md
    │
    └── 05-conditional-expressions/
        ├── 05_conditional_expressions.py
        └── README.md
```

## 9.1 Main README

The current file is the main README for the complete section.

It provides an overview of all topics.

## 9.2 Section README Files

Each major folder has its own README.

These files explain the corresponding operator category or expression concepts in detail.

## 9.3 Python Source Files

Every topic has a Python source file.

The source file contains examples, solved programs, practice questions, and an interactive learning menu.

## 9.4 Topic README Files

Every topic has a separate README for theory, syntax, explanations, examples, revision, and practice.

---

# 10. Overview of the Eight Main Sections

This chapter contains eight main learning sections.

## Section 1 — Arithmetic Operators

Folder:

```text
01-Arithmetic-Operators/
```

Main purpose:

Perform mathematical calculations using Python.

Topics include:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Floor division.
- Modulus.
- Exponentiation.
- Unary plus.
- Unary minus.
- Arithmetic expressions.
- Division by zero.
- Practical mathematical problems.

Expected outcome:

You should be able to use Python arithmetic operators to solve mathematical and programming problems.

## Section 2 — Assignment Operators

Folder:

```text
02-Assignment-Operators/
```

Main purpose:

Assign values to variables and update existing values.

Topics include:

- Basic assignment.
- Multiple assignment.
- Chained assignment.
- Addition assignment.
- Subtraction assignment.
- Multiplication assignment.
- Division assignment.
- Floor division assignment.
- Modulus assignment.
- Exponentiation assignment.
- Bitwise assignment.
- Optional walrus operator.

Expected outcome:

You should be able to assign, update, and manage variable values efficiently.

## Section 3 — Comparison Operators

Folder:

```text
03-Comparison-Operators/
```

Main purpose:

Compare values and produce Boolean results.

Topics include:

- Equal to.
- Not equal to.
- Greater than.
- Less than.
- Greater than or equal to.
- Less than or equal to.
- Chained comparisons.
- Comparing numeric values.
- Comparing strings.
- Comparison expressions.

Expected outcome:

You should be able to compare values and use comparison results in program conditions.

## Section 4 — Logical Operators

Folder:

```text
04-Logical-Operators/
```

Main purpose:

Combine or negate conditions.

Topics include:

- `and`.
- `or`.
- `not`.
- Truthy values.
- Falsy values.
- Logical expressions.
- Short-circuit evaluation.
- Combining multiple conditions.
- Practical decision-making examples.

Expected outcome:

You should be able to construct logical conditions for decision-making programs.

## Section 5 — Bitwise Operators

Folder:

```text
05-Bitwise-Operators/
```

Main purpose:

Perform operations on the binary representation of integers.

Topics include:

- Binary number system.
- Bitwise AND.
- Bitwise OR.
- Bitwise XOR.
- Bitwise NOT.
- Left shift.
- Right shift.
- Bitwise assignment.
- Bit manipulation.
- Common DSA applications.

Expected outcome:

You should understand bitwise operations and apply them to basic bit-manipulation problems.

## Section 6 — Membership Operators

Folder:

```text
06-Membership-Operators/
```

Main purpose:

Check whether a value exists in a collection or sequence.

Topics include:

- `in`.
- `not in`.
- String membership.
- List membership.
- Tuple membership.
- Set membership.
- Dictionary membership.
- Membership expressions.

Expected outcome:

You should be able to test whether an element belongs to a collection or sequence.

## Section 7 — Identity Operators

Folder:

```text
07-Identity-Operators/
```

Main purpose:

Check whether two references refer to the same object.

Topics include:

- `is`.
- `is not`.
- Object identity.
- Object references.
- Equality versus identity.
- Identity with `None`.
- Common identity mistakes.

Expected outcome:

You should understand the difference between checking values and checking object identity.

## Section 8 — Expressions

Folder:

```text
08-Expressions/
```

Main purpose:

Understand how Python combines values and operators and evaluates expressions.

Topics include:

1. Expressions.
2. Operator Precedence.
3. Operator Associativity.
4. Parentheses and Grouping.
5. Conditional Expressions.

Expected outcome:

You should be able to read, construct, and evaluate Python expressions correctly.

---

# 11. Section 1 — Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

They work with numeric values such as integers and floating-point numbers.

## 11.1 Main Arithmetic Operators

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor Division | `10 // 3` | 3 |
| `%` | Modulus | `10 % 3` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |

## 11.2 Addition

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

## 11.3 Subtraction

```python
first = 20
second = 10

print(first - second)
```

Output:

```text
10
```

## 11.4 Multiplication

```python
print(10 * 5)
```

Output:

```text
50
```

## 11.5 Division

```python
print(10 / 2)
```

Output:

```text
5.0
```

The `/` operator produces a floating-point result for ordinary numeric division.

## 11.6 Floor Division

```python
print(10 // 3)
```

Output:

```text
3
```

Floor division rounds the quotient down to the nearest integer value.

For negative numbers, this distinction is important:

```python
print(-10 // 3)
```

Output:

```text
-4
```

## 11.7 Modulus

```python
print(10 % 3)
```

Output:

```text
1
```

The modulus operator returns the remainder of the division operation.

## 11.8 Exponentiation

```python
print(2 ** 3)
```

Output:

```text
8
```

This represents two raised to the power of three.

## 11.9 Unary Operators

```python
number = 10

print(+number)
print(-number)
```

The unary plus and minus operators work with one operand.

## 11.10 Division by Zero

Division and modulo operations with a zero divisor generally raise `ZeroDivisionError`.

Example:

```python
# This raises ZeroDivisionError:
# print(10 / 0)
```

A program should validate the divisor before performing the operation.

---

# 12. Section 2 — Assignment Operators

Assignment operators assign values or update variables.

## 12.1 Basic Assignment

```python
number = 10
```

## 12.2 Augmented Assignment Operators

| Operator | Equivalent operation |
|---|---|
| `+=` | Addition followed by assignment |
| `-=` | Subtraction followed by assignment |
| `*=` | Multiplication followed by assignment |
| `/=` | Division followed by assignment |
| `//=` | Floor division followed by assignment |
| `%=` | Modulus followed by assignment |
| `**=` | Exponentiation followed by assignment |
| `&=` | Bitwise AND followed by assignment |
| `|=` | Bitwise OR followed by assignment |
| `^=` | Bitwise XOR followed by assignment |
| `>>=` | Right shift followed by assignment |
| `<<=` | Left shift followed by assignment |

## 12.3 Addition Assignment

```python
number = 10

number += 5

print(number)
```

Output:

```text
15
```

## 12.4 Subtraction Assignment

```python
number = 10

number -= 3

print(number)
```

Output:

```text
7
```

## 12.5 Multiplication Assignment

```python
number = 10

number *= 2

print(number)
```

Output:

```text
20
```

## 12.6 Division Assignment

```python
number = 10

number /= 2

print(number)
```

Output:

```text
5.0
```

## 12.7 Multiple Assignment

```python
first, second = 10, 20
```

## 12.8 Chained Assignment

```python
first = second = third = 100
```

## 12.9 Important Note

Assignment statements and assignment expressions are related but different Python language constructs.

The ordinary `=` operator is used in assignment statements.

The walrus operator `:=` is an assignment expression and is covered as an optional advanced concept.

---

# 13. Section 3 — Comparison Operators

Comparison operators compare values.

They generally produce Boolean results.

## 13.1 Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `10 == 10` |
| `!=` | Not equal to | `10 != 5` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `5 <= 10` |

## 13.2 Equal To

```python
print(10 == 10)
```

Output:

```text
True
```

## 13.3 Not Equal To

```python
print(10 != 5)
```

Output:

```text
True
```

## 13.4 Greater Than

```python
print(10 > 5)
```

Output:

```text
True
```

## 13.5 Less Than

```python
print(5 < 10)
```

Output:

```text
True
```

## 13.6 Greater Than or Equal To

```python
print(10 >= 10)
```

Output:

```text
True
```

## 13.7 Less Than or Equal To

```python
print(5 <= 10)
```

Output:

```text
True
```

## 13.8 Chained Comparisons

Python allows comparisons to be chained.

```python
age = 20

print(18 <= age <= 60)
```

The expression checks both comparisons.

This is useful for range validation.

---

# 14. Section 4 — Logical Operators

Logical operators combine or negate conditions.

Python provides three main logical operators.

| Operator | Meaning |
|---|---|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

## 14.1 Logical AND

The `and` operator evaluates both operands according to Boolean truth rules.

Example:

```python
age = 20
has_id = True

result = age >= 18 and has_id

print(result)
```

Output:

```text
True
```

## 14.2 Logical OR

The `or` operator evaluates alternatives.

```python
is_weekend = True
is_holiday = False

print(is_weekend or is_holiday)
```

Output:

```text
True
```

## 14.3 Logical NOT

The `not` operator negates a truth value.

```python
is_active = True

print(not is_active)
```

Output:

```text
False
```

## 14.4 Truthy and Falsy Values

Python evaluates objects according to their truth value.

Common falsy values include:

- `False`.
- `None`.
- Numeric zero.
- Empty strings.
- Empty lists.
- Empty tuples.
- Empty dictionaries.
- Empty sets.

Most other objects are truthy.

## 14.5 Short-Circuit Evaluation

Python's logical operators can avoid evaluating the second operand when its value is no longer needed.

Example:

```python
number = 0

result = number != 0 and 10 / number > 1

print(result)
```

Output:

```text
False
```

The right-hand expression is not evaluated because the left-hand condition is false.

Short-circuit evaluation is useful for writing safe logical expressions.

---

# 15. Section 5 — Bitwise Operators

Bitwise operators perform operations on the binary representation of integers.

A binary number uses two digits:

```text
0
1
```

For example:

```text
Decimal 5 = Binary 0101
Decimal 3 = Binary 0011
```

## 15.1 Bitwise Operators

| Operator | Name |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

## 15.2 Bitwise AND

```python
print(5 & 3)
```

Binary representation:

```text
0101
0011
----
0001
```

Result:

```text
1
```

## 15.3 Bitwise OR

```python
print(5 | 3)
```

Binary representation:

```text
0101
0011
----
0111
```

Result:

```text
7
```

## 15.4 Bitwise XOR

```python
print(5 ^ 3)
```

Binary representation:

```text
0101
0011
----
0110
```

Result:

```text
6
```

## 15.5 Bitwise NOT

```python
print(~5)
```

For Python integers, bitwise NOT follows the two's-complement-style identity:

```python
~n == -(n + 1)
```

Therefore:

```text
-6
```

## 15.6 Left Shift

```python
print(5 << 1)
```

Output:

```text
10
```

The binary representation is shifted left by one position.

## 15.7 Right Shift

```python
print(5 >> 1)
```

Output:

```text
2
```

The binary representation is shifted right by one position.

## 15.8 Why Learn Bitwise Operators?

Bitwise operations are useful in:

- Bit manipulation problems.
- Flags and masks.
- Low-level programming.
- Permissions.
- Efficient integer operations.
- Competitive programming.
- DSA exercises.

---

# 16. Section 6 — Membership Operators

Membership operators check whether a value exists in a sequence or collection.

Python provides:

- `in`
- `not in`

## 16.1 The `in` Operator

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
```

Output:

```text
True
```

## 16.2 The `not in` Operator

```python
languages = ["Python", "Java", "C++"]

print("JavaScript" not in languages)
```

Output:

```text
True
```

## 16.3 String Membership

```python
text = "Python Programming"

print("Python" in text)
```

Output:

```text
True
```

## 16.4 List Membership

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

## 16.5 Tuple Membership

```python
values = (10, 20, 30)

print(10 in values)
```

## 16.6 Set Membership

```python
numbers = {10, 20, 30}

print(20 in numbers)
```

## 16.7 Dictionary Membership

For dictionaries, membership checks keys by default.

```python
student = {
    "name": "Amaan",
    "age": 20
}

print("name" in student)
```

Output:

```text
True
```

To check values, use:

```python
print("Amaan" in student.values())
```

---

# 17. Section 7 — Identity Operators

Identity operators check whether two references point to the same object.

Python provides:

- `is`
- `is not`

## 17.1 The `is` Operator

```python
first = None

print(first is None)
```

Output:

```text
True
```

## 17.2 The `is not` Operator

```python
value = 10

print(value is not None)
```

Output:

```text
True
```

## 17.3 Identity Versus Equality

Equality checks whether values compare equal.

Identity checks whether references point to the same object.

Example:

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)
print(first is second)
```

Typical output:

```text
True
False
```

The lists contain equal values but are separate objects.

## 17.4 Checking None

Prefer:

```python
if result is None:
    print("No result")
```

rather than using equality to test for the special `None` object.

## 17.5 Why Is Identity Important?

Identity checks are useful when:

- Checking for `None`.
- Understanding references.
- Understanding object identity.
- Working with mutable objects.
- Debugging reference-related behavior.

---

# 18. Section 8 — Expressions

Expressions combine values, variables, operators, and other valid Python constructs to produce results.

The Expressions section contains five individual topics.

## 18.1 Topic 1 — Expressions

Folder:

```text
08-Expressions/01-expressions/
```

This topic introduces expressions and how Python evaluates them.

You learn:

- Simple expressions.
- Arithmetic expressions.
- Comparison expressions.
- Logical expressions.
- Expressions with variables.
- Expressions with multiple operators.
- Expression evaluation.
- Expression results.

Example:

```python
first = 10
second = 5

result = first + second * 2

print(result)
```

Expected outcome:

You should understand how to create and evaluate expressions.

## 18.2 Topic 2 — Operator Precedence

Folder:

```text
08-Expressions/02-operator-precedence/
```

This topic explains which operators are evaluated first when multiple operators appear in an expression.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication has higher precedence than addition.

You learn:

- Operator precedence.
- Precedence levels.
- Expression evaluation order.
- Arithmetic precedence.
- Comparison precedence.
- Logical precedence.
- Parentheses overriding normal precedence.

Expected outcome:

You should be able to determine which operation Python evaluates first.

## 18.3 Topic 3 — Operator Associativity

Folder:

```text
08-Expressions/03-operator-associativity/
```

This topic explains how operators of the same precedence are grouped.

Example:

```python
result = 20 - 5 - 3

print(result)
```

Output:

```text
12
```

Subtraction is left-associative.

Exponentiation is right-associative:

```python
result = 2 ** 3 ** 2

print(result)
```

Output:

```text
512
```

You learn:

- Meaning of associativity.
- Left associativity.
- Right associativity.
- Arithmetic associativity.
- Exponentiation associativity.
- Expression grouping.

Expected outcome:

You should understand how expressions are grouped when operators have equal precedence.

## 18.4 Topic 4 — Parentheses and Grouping

Folder:

```text
08-Expressions/04-parentheses-and-grouping/
```

This topic explains how parentheses control expression grouping.

Example:

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

You learn:

- Parentheses.
- Grouping expressions.
- Nested parentheses.
- Overriding operator precedence.
- Improving expression readability.
- Breaking complex calculations into smaller parts.

Expected outcome:

You should be able to use parentheses to control evaluation and make expressions clearer.

## 18.5 Topic 5 — Conditional Expressions

Folder:

```text
08-Expressions/05-conditional-expressions/
```

Conditional expressions select one of two values according to a condition.

Example:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

You learn:

- Conditional expression syntax.
- Condition evaluation.
- True expression.
- False expression.
- Nested conditional expressions.
- Readability considerations.
- Practical applications.

Expected outcome:

You should be able to write short conditional value-selection expressions.

---

# 19. Arithmetic Operators

Arithmetic operators perform mathematical operations.

The principal operators are:

| Symbol | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Modulus |
| `**` | Exponentiation |
| `+x` | Unary plus |
| `-x` | Unary minus |

## 19.1 Arithmetic Expression

```python
result = 10 + 5 * 2

print(result)
```

## 19.2 Negative Numbers

```python
number = -10

print(number)
```

## 19.3 Remainder

```python
print(17 % 5)
```

Output:

```text
2
```

## 19.4 Mathematical Applications

Arithmetic operators are useful for:

- Calculating totals.
- Computing averages.
- Finding remainders.
- Calculating percentages.
- Computing powers.
- Solving mathematical problems.

## 19.5 Programming Applications

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

The modulus operator is commonly used in divisibility checks and DSA problems.

---

# 20. Assignment Operators

Assignment operators are used to assign or update values.

## 20.1 Basic Assignment

```python
count = 0
```

## 20.2 Update a Variable

```python
count = 0

count = count + 1
```

## 20.3 Use Augmented Assignment

```python
count = 0

count += 1
```

These statements express similar updating behavior for an ordinary numeric variable.

For mutable objects, augmented assignment may also modify the existing object rather than simply performing a separate rebinding operation.

## 20.4 Practical Applications

- Updating counters.
- Maintaining running totals.
- Updating scores.
- Tracking quantities.
- Accumulating values.
- Performing bitwise updates.

---

# 21. Comparison Operators

Comparison operators compare values and generally produce Boolean results.

## 21.1 Basic Example

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

## 21.2 Range Comparison

```python
marks = 85

print(0 <= marks <= 100)
```

Output:

```text
True
```

## 21.3 Multiple Conditions

```python
age = 20
has_id = True

eligible = age >= 18 and has_id

print(eligible)
```

Comparison results are often used with logical operators and conditional statements.

---

# 22. Logical Operators

Logical operators combine or negate truth values.

## 22.1 AND

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

## 22.2 OR

```python
is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)
```

## 22.3 NOT

```python
is_active = True

print(not is_active)
```

## 22.4 Truth Tables

### AND

| A | B | A and B |
|---|---|---|
| False | False | False |
| False | True | False |
| True | False | False |
| True | True | True |

### OR

| A | B | A or B |
|---|---|---|
| False | False | False |
| False | True | True |
| True | False | True |
| True | True | True |

### NOT

| A | not A |
|---|---|
| False | True |
| True | False |

## 22.5 Short-Circuit Behavior

Python evaluates logical expressions from left to right and may skip evaluating later operands when the result is already determined.

Example:

```python
number = 0

result = number != 0 and 10 / number > 1

print(result)
```

The division is skipped because the left side is false.

---

# 23. Bitwise Operators

Bitwise operators operate on integer bits.

## 23.1 Binary Representation

Example:

```python
print(bin(5))
print(bin(3))
```

Output:

```text
0b101
0b11
```

## 23.2 Bitwise AND

```python
print(5 & 3)
```

## 23.3 Bitwise OR

```python
print(5 | 3)
```

## 23.4 Bitwise XOR

```python
print(5 ^ 3)
```

## 23.5 Bitwise NOT

```python
print(~5)
```

## 23.6 Left Shift

```python
print(5 << 1)
```

## 23.7 Right Shift

```python
print(5 >> 1)
```

## 23.8 Important DSA Connection

Bitwise operators are frequently used in:

- Bit masks.
- Checking whether a number is even or odd.
- Setting specific bits.
- Clearing specific bits.
- Toggling bits.
- Checking powers of two.
- Subset and bitmask problems.

For negative integers, Python's bitwise operations follow its integer semantics rather than a fixed-width machine integer representation.

---

# 24. Membership Operators

Membership operators check whether a value appears in a collection or sequence.

## 24.1 `in`

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

## 24.2 `not in`

```python
numbers = [10, 20, 30]

print(50 not in numbers)
```

## 24.3 Strings

```python
text = "Python"

print("Py" in text)
```

## 24.4 Sets

```python
numbers = {1, 2, 3, 4}

print(3 in numbers)
```

## 24.5 Dictionaries

```python
student = {
    "name": "Amaan",
    "age": 20
}

print("age" in student)
```

For a dictionary, membership normally checks keys.

---

# 25. Identity Operators

Identity operators check object identity.

## 25.1 `is`

```python
value = None

print(value is None)
```

## 25.2 `is not`

```python
value = 10

print(value is not None)
```

## 25.3 Equality and Identity

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)
print(first is second)
```

The two lists have equal contents, but they are distinct list objects.

## 25.4 Best Practice

Use `is None` or `is not None` when checking for `None`.

Use `==` when comparing values for equality.

Do not depend on object identity for ordinary numeric or string value comparisons.

---

# 26. Expressions and Their Evaluation

An expression is evaluated according to Python's language rules.

Example:

```python
result = 10 + 5 * 2
```

Python evaluates multiplication before addition.

The result is:

```text
20
```

## 26.1 Arithmetic Expression

```python
result = 10 + 20 * 2
```

## 26.2 Comparison Expression

```python
result = 10 > 5
```

## 26.3 Logical Expression

```python
result = True and False
```

## 26.4 Mixed Expression

```python
age = 20
has_id = True

result = age >= 18 and has_id
```

## 26.5 Why Is Expression Evaluation Important?

Understanding expression evaluation prevents mistakes when multiple operators appear together.

It is especially important for:

- Mathematical calculations.
- Conditions.
- Nested expressions.
- Bitwise problems.
- DSA algorithms.
- Complex Boolean logic.

---

# 27. Operator Precedence

Operator precedence determines which operators are evaluated first in an expression.

Example:

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

## 27.1 General Precedence Order

The following table provides a simplified view of important Python operator groups, from higher to lower precedence.

| Priority | Operators or Constructs |
|---:|---|
| 1 | Parentheses, indexing, attribute access, function calls |
| 2 | Await expression |
| 3 | Exponentiation `**` |
| 4 | Unary `+`, `-`, `~` |
| 5 | Multiplication, matrix multiplication, division, floor division, modulus |
| 6 | Addition and subtraction |
| 7 | Bitwise shifts |
| 8 | Bitwise AND |
| 9 | Bitwise XOR |
| 10 | Bitwise OR |
| 11 | Comparisons, membership, identity |
| 12 | Logical `not` |
| 13 | Logical `and` |
| 14 | Logical `or` |
| 15 | Conditional expression |
| 16 | `lambda` expression |
| 17 | Assignment expression `:=` |

This is a learning summary rather than a replacement for the complete Python language reference.

## 27.2 Multiplication Before Addition

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

## 27.3 Parentheses Change the Result

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

## 27.4 Comparison Before Logical AND

```python
result = 10 > 5 and 20 > 10

print(result)
```

Output:

```text
True
```

## 27.5 Why Learn Precedence?

It helps you determine how Python evaluates expressions.

It also helps you write expressions that produce the intended result.

---

# 28. Operator Associativity

Associativity determines how operators of the same precedence are grouped when parentheses do not otherwise determine the grouping.

## 28.1 Left Associativity

Subtraction is left-associative.

Example:

```python
result = 20 - 5 - 3

print(result)
```

The expression is grouped as:

```python
(20 - 5) - 3
```

Result:

```text
12
```

## 28.2 Right Associativity

Exponentiation is right-associative.

Example:

```python
result = 2 ** 3 ** 2

print(result)
```

The expression is grouped as:

```python
2 ** (3 ** 2)
```

Result:

```text
512
```

## 28.3 Important Exception in Evaluation Rules

Exponentiation has a special interaction with unary operators.

For example:

```python
print(-2 ** 2)
```

Output:

```text
-4
```

It is interpreted as:

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

The parentheses change the grouping.

## 28.4 Why Is Associativity Important?

It helps explain why expressions containing repeated operators can produce results that may not be obvious at first glance.

---

# 29. Parentheses and Grouping

Parentheses explicitly control expression grouping.

They also make complex expressions easier to read.

## 29.1 Basic Example

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

## 29.2 Change the Grouping

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

## 29.3 Nested Parentheses

```python
result = ((10 + 5) * (4 - 2))

print(result)
```

Output:

```text
30
```

## 29.4 Use Parentheses for Readability

```python
age = 20
has_id = True

eligible = (age >= 18) and has_id

print(eligible)
```

## 29.5 Best Practice

Use parentheses when they make the intended grouping clearer.

Do not add excessive parentheses that make an expression unnecessarily difficult to read.

---

# 30. Conditional Expressions

A conditional expression chooses one of two values based on a condition.

It is sometimes called a ternary conditional expression.

## 30.1 Syntax

```python
result = value_if_true if condition else value_if_false
```

## 30.2 Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```

## 30.3 Another Example

```python
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

Output:

```text
Even
```

## 30.4 Conditional Expression Versus if-else Statement

Conditional expression:

```python
status = "Pass" if marks >= 40 else "Fail"
```

Ordinary if-else statement:

```python
if marks >= 40:
    status = "Pass"
else:
    status = "Fail"
```

Both approaches select a value.

Use a conditional expression when the logic is short and readable.

Use a normal conditional statement when the logic is more complex.

---

# 31. Unary and Binary Operators

Operators can be classified by the number of operands they use.

## 31.1 Unary Operators

Unary operators work with one operand.

Examples:

```python
number = 10

print(-number)
print(+number)
print(not True)
print(~number)
```

## 31.2 Binary Operators

Binary operators work with two operands.

Examples:

```python
print(10 + 20)
print(10 - 5)
print(10 > 5)
print(True and False)
```

## 31.3 Why Is This Classification Useful?

It helps you understand how expressions are structured.

It also helps explain why the same symbol can have different meanings depending on its position.

For example:

```python
number = -10
```

The minus sign is unary.

By contrast:

```python
result = 20 - 10
```

The minus sign is binary subtraction.

---

# 32. Short-Circuit Evaluation

Short-circuit evaluation means Python may skip evaluating the second operand of a logical expression when the result is already determined.

## 32.1 AND Example

```python
result = False and True

print(result)
```

The second operand does not need to be evaluated to determine the result.

## 32.2 OR Example

```python
result = True or False

print(result)
```

The second operand does not need to be evaluated.

## 32.3 Practical Example

```python
number = 0

if number != 0 and 10 / number > 1:
    print("Condition satisfied")
else:
    print("Condition not satisfied")
```

The division is skipped because the first condition is false.

## 32.4 Why Is Short-Circuit Evaluation Useful?

It can:

- Avoid unnecessary calculations.
- Prevent certain invalid operations.
- Improve the clarity of guarded conditions.
- Support efficient logical checks.

Remember that `and` and `or` return one of their operands rather than always converting the result into an actual Boolean object.

In conditions, Python uses the truth value of those results.

---

# 33. Chained Comparisons

Python allows multiple comparisons to be written together.

Example:

```python
age = 20

print(18 <= age <= 60)
```

This is equivalent in meaning to checking:

```python
18 <= age and age <= 60
```

## 33.1 Numeric Range

```python
marks = 85

print(0 <= marks <= 100)
```

## 33.2 Temperature Range

```python
temperature = 25

print(0 <= temperature <= 40)
```

## 33.3 Comparison Chain

```python
number = 15

print(10 < number < 20)
```

Output:

```text
True
```

## 33.4 Best Practice

Chained comparisons can make simple range checks concise.

Use them when they clearly express the intended condition.

---

# 34. Augmented Assignment

Augmented assignment combines an operation with an assignment.

Example:

```python
number = 10

number += 5

print(number)
```

Output:

```text
15
```

## 34.1 Arithmetic Augmented Assignment

```python
number = 10

number += 5
number -= 2
number *= 3
number /= 2
```

## 34.2 Bitwise Augmented Assignment

```python
number = 10

number &= 6
number |= 2
number ^= 1
```

## 34.3 Why Use Augmented Assignment?

It can make value updates shorter and easier to read.

## 34.4 Important Note

Augmented assignment is not always identical to writing a simple assignment with a binary operation.

For mutable objects, an in-place operation may be used.

The exact behavior depends on the object and operator.

---

# 35. Walrus Operator

The walrus operator is written as:

```python
:=
```

It is called the assignment expression operator.

It allows a value to be assigned as part of an expression.

## 35.1 Basic Example

```python
if (number := 10) > 5:
    print(number)
```

Output:

```text
10
```

## 35.2 Example with Input

```python
if (name := input("Enter your name: ").strip()):
    print(f"Hello, {name}")
else:
    print("Name cannot be empty.")
```

## 35.3 Why Is It Useful?

It can avoid repeating certain calculations or input operations.

## 35.4 Important Note

The walrus operator is an advanced optional concept for this beginner section.

Use it only when it improves clarity.

Do not use it merely to make code shorter.

It does not replace normal assignment in every situation.

---

# 36. Matrix Multiplication Operator

Python provides the matrix multiplication operator:

```python
@
```

It is used by types that implement matrix multiplication behavior.

## 36.1 Important Difference

The `@` operator is not ordinary numeric multiplication for built-in integers or floats.

For matrix operations, Python programs commonly use libraries such as NumPy.

## 36.2 Conceptual Example

In a suitable matrix library:

```python
# Example syntax for a matrix-capable library:
# result = matrix_a @ matrix_b
```

The exact behavior depends on the objects implementing the operation.

## 36.3 Why Is It Included?

It is useful to recognize `@` as part of Python's operator syntax.

For beginner programming, it is an optional advanced concept.

---

# 37. Difference Between Equality and Identity

Equality and identity are different concepts.

## Equality

The `==` operator compares values.

## Identity

The `is` operator checks whether two references refer to the same object.

Example:

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)
print(first is second)
```

Typical output:

```text
True
False
```

## Comparison Table

| Operator | Meaning |
|---|---|
| `==` | Values compare equal |
| `is` | References point to the same object |
| `!=` | Values compare unequal |
| `is not` | References point to different objects |

## Important Rule

Use `==` for value equality.

Use `is` for object identity, especially for comparisons with `None`.

---

# 38. Difference Between Logical and Bitwise Operators

Logical operators and bitwise operators are not interchangeable.

## Logical Operators

```python
and
or
not
```

They evaluate truth values.

## Bitwise Operators

```python
&
|
^
~
```

They operate on integer bits.

## Example

```python
first = True
second = False

print(first and second)
```

Logical result:

```text
False
```

Now consider:

```python
first = 5
second = 3

print(first & second)
```

Bitwise result:

```text
1
```

## Comparison

| Logical | Bitwise |
|---|---|
| `and` | `&` |
| `or` | `|` |
| `not` | `~` is bitwise NOT for integers |
| Works through truth-value evaluation | Works on integer bit representations |
| Supports short-circuit behavior for `and` and `or` | Does not provide logical short-circuit behavior |

---

# 39. Difference Between Membership and Identity

Membership and identity check different things.

## Membership

Checks whether a value belongs to a collection or sequence.

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

## Identity

Checks whether two references point to the same object.

```python
first = [10, 20]
second = first

print(first is second)
```

## Comparison

| Membership | Identity |
|---|---|
| `in` | `is` |
| `not in` | `is not` |
| Checks membership | Checks object identity |
| Used with sequences and collections | Used with object references |

---

# 40. Operator Categories at a Glance

| Category | Operators | Main Purpose |
|---|---|---|
| Arithmetic | `+ - * / // % **` | Mathematical operations |
| Assignment | `= += -= *= /=` and others | Assign or update values |
| Comparison | `== != > < >= <=` | Compare values |
| Logical | `and or not` | Combine or negate conditions |
| Bitwise | `& | ^ ~ << >>` | Integer bit manipulation |
| Membership | `in not in` | Check membership |
| Identity | `is is not` | Check object identity |
| Conditional Expression | `if ... else ...` | Select a value based on a condition |

---

# 41. Operator Precedence Reference

The following table summarizes common precedence groups from higher to lower.

| Group | Operators or Constructs |
|---|---|
| Grouping and access | `()`, `[]`, `.`, function calls |
| Exponentiation | `**` |
| Unary arithmetic | `+x`, `-x`, `~x` |
| Multiplication group | `*`, `@`, `/`, `//`, `%` |
| Addition group | `+`, `-` |
| Shifts | `<<`, `>>` |
| Bitwise AND | `&` |
| Bitwise XOR | `^` |
| Bitwise OR | `|` |
| Comparisons | `<`, `<=`, `>`, `>=`, `==`, `!=`, `in`, `not in`, `is`, `is not` |
| Logical NOT | `not` |
| Logical AND | `and` |
| Logical OR | `or` |
| Conditional | `if ... else` |
| Lambda | `lambda` |
| Assignment expression | `:=` |

## Important Notes

- Parentheses can override normal precedence.
- Exponentiation has right-associative grouping.
- Exponentiation has a special relationship with unary operators.
- Comparisons may be chained.
- Logical `and` and `or` short-circuit.
- Use parentheses when they make complex expressions clearer.

Always follow Python's actual evaluation rules rather than relying on memory alone.

---

# 42. Expressions in Real Programs

Expressions are used in nearly every program.

## 42.1 Calculator

```python
first = 10
second = 5

addition = first + second
subtraction = first - second
multiplication = first * second
division = first / second

print(addition)
print(subtraction)
print(multiplication)
print(division)
```

## 42.2 Student Result

```python
marks = 85

passed = marks >= 40

print(passed)
```

## 42.3 Eligibility Check

```python
age = 20
has_id = True

eligible = age >= 18 and has_id

print(eligible)
```

## 42.4 Even or Odd

```python
number = 12

is_even = number % 2 == 0

print(is_even)
```

## 42.5 Membership Check

```python
languages = ["Python", "Java", "C++"]

available = "Python" in languages

print(available)
```

## 42.6 Identity Check

```python
result = None

if result is None:
    print("Result not available.")
```

## 42.7 Conditional Expression

```python
marks = 75

result = "Pass" if marks >= 40 else "Fail"

print(result)
```

---

# 43. Practical Examples

The following examples combine multiple operator categories.

## Example 1: Addition

```python
first = 10
second = 20

print(first + second)
```

## Example 2: Subtraction

```python
first = 50
second = 20

print(first - second)
```

## Example 3: Multiplication

```python
first = 10
second = 5

print(first * second)
```

## Example 4: Division

```python
first = 20
second = 4

print(first / second)
```

## Example 5: Floor Division

```python
print(17 // 5)
```

## Example 6: Modulus

```python
print(17 % 5)
```

## Example 7: Exponentiation

```python
print(2 ** 5)
```

## Example 8: Augmented Assignment

```python
number = 10

number += 5

print(number)
```

## Example 9: Comparison

```python
print(10 > 5)
```

## Example 10: Logical Expression

```python
print(10 > 5 and 20 > 10)
```

## Example 11: Bitwise AND

```python
print(5 & 3)
```

## Example 12: Membership

```python
values = [10, 20, 30]

print(20 in values)
```

## Example 13: Identity

```python
value = None

print(value is None)
```

## Example 14: Precedence

```python
print(10 + 5 * 2)
```

## Example 15: Parentheses

```python
print((10 + 5) * 2)
```

## Example 16: Conditional Expression

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

---

# 44. Solved Practical Programs

## Solved Program 1: Simple Arithmetic Calculator

Task:

Read two numbers and display their sum, difference, product, and division.

Solution:

```python
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("Addition:", first + second)
print("Subtraction:", first - second)
print("Multiplication:", first * second)

if second != 0:
    print("Division:", first / second)
else:
    print("Division by zero is not allowed.")
```

Concepts used:

- Arithmetic operators.
- Input conversion.
- Comparison.
- Conditional statements.
- Output.

## Solved Program 2: Even or Odd

Task:

Check whether an integer is even or odd.

Solution:

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Explanation:

A number is even when its remainder after division by two is zero.

## Solved Program 3: Greater of Two Numbers

Task:

Find the greater of two values.

Solution:

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first > second:
    print("First number is greater.")
elif second > first:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")
```

Concepts used:

- Comparison operators.
- Conditional statements.

## Solved Program 4: Range Validation

Task:

Check whether a number is between 1 and 100.

Solution:

```python
number = int(input("Enter a number: "))

if 1 <= number <= 100:
    print("Number is within the range.")
else:
    print("Number is outside the range.")
```

Concepts used:

- Chained comparison.
- Range validation.

## Solved Program 5: Eligibility Check

Task:

Check whether a person satisfies an age and identity-card requirement.

Solution:

```python
age = int(input("Enter age: "))
has_id = input("Do you have an ID? ").strip().lower()

if age >= 18 and has_id in ("yes", "y"):
    print("Eligible")
else:
    print("Not eligible")
```

Concepts used:

- Comparison operators.
- Logical AND.
- Membership operators.
- String methods.

## Solved Program 6: Update a Counter

Task:

Increase a counter using augmented assignment.

Solution:

```python
counter = 0

counter += 1
counter += 1
counter += 1

print("Counter:", counter)
```

Output:

```text
Counter: 3
```

Concepts used:

- Assignment operators.
- Arithmetic operators.

## Solved Program 7: Bitwise AND

Task:

Perform bitwise AND on two integer values.

Solution:

```python
first = 5
second = 3

result = first & second

print("Result:", result)
```

Output:

```text
Result: 1
```

Concepts used:

- Bitwise AND.
- Binary representation.

## Solved Program 8: Membership Check

Task:

Check whether a programming language exists in a list.

Solution:

```python
languages = ["Python", "Java", "C++"]

language = input("Enter language: ")

if language in languages:
    print("Language is available.")
else:
    print("Language is not available.")
```

Concepts used:

- Lists.
- Membership operators.
- Conditional statements.

## Solved Program 9: Identity Check

Task:

Check whether a result is None.

Solution:

```python
result = None

if result is None:
    print("No result available.")
else:
    print("Result:", result)
```

Concepts used:

- Identity operator.
- Conditional statements.

## Solved Program 10: Evaluate Operator Precedence

Task:

Calculate the result of a mathematical expression.

Solution:

```python
result = 10 + 5 * 2 ** 2

print("Result:", result)
```

Output:

```text
30
```

Explanation:

Exponentiation is evaluated first.

Multiplication follows.

Addition is performed last.

## Solved Program 11: Conditional Expression

Task:

Determine whether a number is positive or non-positive.

Solution:

```python
number = int(input("Enter number: "))

result = "Positive" if number > 0 else "Non-positive"

print(result)
```

## Solved Program 12: Combined Operator Program

Task:

Read an integer and display information about it.

Solution:

```python
number = int(input("Enter an integer: "))

is_even = number % 2 == 0
is_positive = number > 0
is_in_range = 1 <= number <= 100

print("Even:", is_even)
print("Positive:", is_positive)
print("In range:", is_in_range)

result = "Accepted" if is_in_range else "Rejected"

print("Status:", result)
```

Concepts used:

- Arithmetic operators.
- Comparison operators.
- Logical expressions.
- Conditional expression.
- Input conversion.
- Output.

---

# 45. Applications in Data Structures and Algorithms

Operators and expressions are very important for DSA.

Many algorithm problems depend on mathematical operations, comparisons, logical conditions, and bit manipulation.

## 45.1 Arithmetic Operators in DSA

Arithmetic operators are used in:

- Calculating indexes.
- Finding remainders.
- Updating counters.
- Computing totals.
- Calculating midpoints.
- Handling numerical sequences.

Example:

```python
middle = (left + right) // 2
```

This is commonly used when calculating a midpoint in binary search, provided the index calculations are correct for the chosen algorithm.

## 45.2 Comparison Operators in DSA

Comparison operators help determine whether one value is greater, smaller, or equal to another.

They are used in:

- Sorting.
- Searching.
- Minimum and maximum calculations.
- Condition checks.
- Loop termination.

Example:

```python
if current_value > maximum:
    maximum = current_value
```

## 45.3 Logical Operators in DSA

Logical operators combine multiple algorithm conditions.

Example:

```python
if index >= 0 and index < len(numbers):
    print(numbers[index])
```

## 45.4 Bitwise Operators in DSA

Bitwise operators are used in:

- Bit manipulation.
- Masks.
- Flags.
- Checking and changing bits.
- Power-of-two problems.
- Subset enumeration.

## 45.5 Membership Operators in DSA

Membership operations can help check whether an item exists in a collection.

Example:

```python
numbers = {10, 20, 30}

print(20 in numbers)
```

Sets are especially useful for many membership-oriented problems.

## 45.6 Identity Operators in DSA

Identity is useful when checking special object references such as `None`.

Example:

```python
node = None

if node is None:
    print("Node is empty.")
```

This pattern appears in linked structures and tree-related code.

---

# 46. Operators in Searching and Sorting

Searching and sorting algorithms use operators throughout their logic.

## 46.1 Linear Search

A comparison checks whether the current element matches the target.

```python
numbers = [10, 20, 30, 40]

target = 30

for number in numbers:
    if number == target:
        print("Found")
        break
```

## 46.2 Binary Search

Comparison operators help decide which half of a sorted list should be searched.

```python
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

target = 30

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Found at index:", middle)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1
```

## 46.3 Sorting

Comparison operators determine the ordering of values.

Example:

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30]
```

Understanding comparisons and arithmetic is essential before studying sorting algorithms in detail.

---

# 47. Operators in Bit Manipulation

Bit manipulation is an important DSA topic.

It uses the binary representation of integers.

## 47.1 Check Whether a Number Is Even

```python
number = 10

if number & 1 == 0:
    print("Even")
else:
    print("Odd")
```

## 47.2 Check Whether a Number Is Odd

```python
number = 7

if number & 1:
    print("Odd")
else:
    print("Even")
```

## 47.3 Set a Bit

```python
number = 8

result = number | (1 << 1)

print(result)
```

## 47.4 Clear a Bit

```python
number = 10

result = number & ~(1 << 1)

print(result)
```

## 47.5 Toggle a Bit

```python
number = 10

result = number ^ (1 << 1)

print(result)
```

## 47.6 Check a Bit

```python
number = 10
position = 1

result = (number >> position) & 1

print(result)
```

These are introductory examples. More advanced bit manipulation will be studied with DSA.

---

# 48. Operators in Conditional Logic

Conditional logic uses comparison and logical operators.

Example:

```python
age = 20
marks = 80

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not eligible")
```

## Common Uses

- Checking eligibility.
- Checking ranges.
- Validating input.
- Deciding whether a number is positive.
- Checking even or odd numbers.
- Controlling loops.
- Selecting algorithm branches.

Understanding logical expressions is important before learning complex conditional statements.

---

# 49. Operators in Mathematical Problems

Arithmetic operators appear in numerous mathematical problems.

## 49.1 Even or Odd

```python
number = 10

print(number % 2 == 0)
```

## 49.2 Last Digit

```python
number = 12345

last_digit = number % 10

print(last_digit)
```

## 49.3 Remove Last Digit

```python
number = 12345

number = number // 10

print(number)
```

## 49.4 Calculate Square

```python
number = 5

print(number ** 2)
```

## 49.5 Calculate Cube

```python
number = 5

print(number ** 3)
```

These small operations become building blocks for larger numerical algorithms.

---

# 50. Common Mistakes

## Mistake 1: Confusing `=` and `==`

Incorrect:

```python
# if number = 10:
#     print("Matched")
```

Correct:

```python
if number == 10:
    print("Matched")
```

## Mistake 2: Confusing `/` and `//`

```python
print(10 / 3)
print(10 // 3)
```

The first performs division.

The second performs floor division.

## Mistake 3: Expecting Modulus to Return Division

```python
print(10 % 3)
```

This returns the remainder.

## Mistake 4: Forgetting Operator Precedence

```python
print(10 + 5 * 2)
```

The result is `20`, not `30`.

Use parentheses to make the intended grouping explicit.

## Mistake 5: Confusing Logical and Bitwise Operators

Logical:

```python
True and False
```

Bitwise:

```python
5 & 3
```

They perform different operations.

## Mistake 6: Using `is` Instead of `==`

Incorrect for ordinary value comparison:

```python
# first is second
```

Use:

```python
first == second
```

when checking value equality.

## Mistake 7: Assuming Membership Checks Dictionary Values

```python
student = {"name": "Amaan"}

print("Amaan" in student)
```

This checks dictionary keys, not values.

Use:

```python
print("Amaan" in student.values())
```

## Mistake 8: Ignoring Division by Zero

Before dividing, validate that the divisor is not zero.

## Mistake 9: Misunderstanding Exponentiation Grouping

```python
2 ** 3 ** 2
```

Exponentiation is right-associative.

The expression is grouped as:

```python
2 ** (3 ** 2)
```

## Mistake 10: Overusing Nested Expressions

Very long expressions may be difficult to read.

Break them into smaller parts when appropriate.

## Mistake 11: Misunderstanding `and` and `or`

These operators can return one of their operands rather than always returning a Boolean object.

Understand truth-value evaluation and short-circuit behavior.

## Mistake 12: Confusing Object Identity with Value Equality

Two separate objects can compare equal without being identical.

---

# 51. Debugging Techniques

When an expression produces an unexpected result, use a systematic debugging process.

## Step 1: Identify the Operators

List all operators used in the expression.

## Step 2: Identify the Operands

Determine the values involved.

## Step 3: Check Data Types

Use:

```python
print(type(value))
```

## Step 4: Review Operator Precedence

Check which operations are performed first.

## Step 5: Review Associativity

Check how operators with equal precedence are grouped.

## Step 6: Add Parentheses

Rewrite the expression to make grouping clearer.

## Step 7: Evaluate Smaller Parts

Break a long expression into smaller calculations.

Example:

```python
first = 10 + 5
second = 3 * 2

result = first + second

print(result)
```

## Step 8: Test Boundary Values

Try zero, negative values, equal values, and values around important limits.

## Step 9: Check Error Messages

Read the exception type and message.

## Step 10: Run Again

After correcting the problem, run the program with multiple test cases.

---

# 52. Testing Strategy

Testing ensures that operators and expressions behave as expected.

## 52.1 Arithmetic Testing

Test:

- Positive numbers.
- Negative numbers.
- Zero.
- Division.
- Floor division.
- Modulus.
- Exponentiation.
- Division by zero.

## 52.2 Assignment Testing

Test:

- Basic assignment.
- Reassignment.
- Augmented assignment.
- Multiple assignment.
- Swapping.
- Bitwise assignment.

## 52.3 Comparison Testing

Test:

- Equal values.
- Unequal values.
- Greater values.
- Smaller values.
- Equal boundary values.
- Chained comparisons.

## 52.4 Logical Testing

Test:

- True and True.
- True and False.
- False or True.
- False or False.
- Negation.
- Empty values.
- Short-circuit behavior.

## 52.5 Bitwise Testing

Test:

- Zero.
- One.
- Positive integers.
- Negative integers.
- Binary representation.
- Shifts.
- Bit masks.

## 52.6 Membership Testing

Test:

- Existing elements.
- Missing elements.
- Empty collections.
- Strings.
- Lists.
- Tuples.
- Sets.
- Dictionary keys.

## 52.7 Identity Testing

Test:

- Same reference.
- Equal but separate objects.
- `None`.
- `is not None`.

## 52.8 Expression Testing

Test:

- Simple expressions.
- Multiple operators.
- Parentheses.
- Precedence.
- Associativity.
- Conditional expressions.

---

# 53. Boundary Testing

Boundary testing checks expressions around important values.

## 53.1 Even or Odd

Test:

```text
-2
-1
0
1
2
```

## 53.2 Range Validation

Suppose a value must be between 1 and 100.

Test:

```text
0
1
2
99
100
101
```

## 53.3 Division

Test:

```text
10 / 2
10 / 1
10 / 0
```

The last case should be handled because division by zero is invalid.

## 53.4 Comparison

Test values that are:

- Smaller.
- Equal.
- Greater.

## 53.5 Membership

Test:

- Element present.
- Element absent.
- Empty collection.

Boundary testing helps identify mistakes in comparison and arithmetic expressions.

---

# 54. Best Practices

Follow these practices when using Python operators.

## 54.1 Understand the Data Types

Know which types are involved in an expression.

## 54.2 Use the Correct Operator

Choose the operator according to the intended operation.

## 54.3 Understand Precedence

Do not assume operators are evaluated from left to right in every expression.

## 54.4 Use Parentheses for Clarity

Use parentheses where they make the intended grouping clear.

## 54.5 Avoid Unnecessarily Complex Expressions

Break long expressions into meaningful parts.

## 54.6 Validate Divisors

Handle division by zero.

## 54.7 Use `==` for Value Equality

Use `is` for object identity.

## 54.8 Use Logical Operators for Conditions

Prefer `and`, `or`, and `not` for ordinary logical conditions.

## 54.9 Use Bitwise Operators for Bit Manipulation

Do not confuse bitwise operations with Boolean logic.

## 54.10 Use Membership Operators for Membership Checks

Use `in` and `not in` when checking collections and sequences.

## 54.11 Test Different Values

Try boundary values and unexpected values.

## 54.12 Keep Code Readable

Clear expressions are generally easier to debug and maintain.

---

# 55. Code Readability

Readable expressions improve program quality.

## 55.1 Use Meaningful Variable Names

Prefer:

```python
total_marks = 450
passing_marks = 40
```

over unclear names.

## 55.2 Break Long Calculations

Instead of writing one complicated expression:

```python
# A long expression may be difficult to review.
```

Use meaningful intermediate variables.

```python
total = math_marks + science_marks + english_marks

average = total / 3

passed = average >= passing_marks
```

## 55.3 Use Parentheses

Make grouping clear.

## 55.4 Follow Consistent Formatting

Use consistent spacing around operators.

Preferred style:

```python
result = first + second
```

## 55.5 Use Comments Where Needed

Explain unusual or non-obvious logic.

Do not comment every obvious operation.

---

# 56. Writing Efficient Expressions

Good expressions should be correct, readable, and appropriate for the task.

## 56.1 Avoid Repeating Calculations

Use an intermediate variable when a complex calculation is needed multiple times.

## 56.2 Use Appropriate Data Structures

For repeated membership checks, a set may be more appropriate than a list depending on the problem and ordering requirements.

## 56.3 Avoid Unnecessary Bitwise Tricks

Use bitwise operations when they solve a real bit-manipulation problem.

Do not replace readable arithmetic or logical expressions with obscure tricks without a good reason.

## 56.4 Use Short-Circuiting Carefully

Do not put side effects inside logical expressions unless the behavior is intentional and clear.

## 56.5 Prefer Readability

Code that is easy to understand is easier to test, maintain, and debug.

---

# 57. Real-Life Applications

Operators and expressions are used in many types of software.

## 57.1 Calculator Applications

Arithmetic operators perform calculations.

## 57.2 Student Result Systems

Comparison and arithmetic operators calculate totals and determine results.

## 57.3 Banking Systems

Arithmetic and comparison operators help process amounts and validate transactions.

## 57.4 Login Systems

Logical expressions combine credential and access conditions.

## 57.5 Shopping Applications

Arithmetic operators calculate bills.

Membership operators can check available product categories or supported options.

## 57.6 Inventory Management

Assignment operators update stock quantities.

Comparison operators check stock levels.

## 57.7 Data Structures

Membership checks and comparisons are used in searching and data processing.

## 57.8 Sorting Algorithms

Comparison operators help arrange values.

## 57.9 Bit Flags and Permissions

Bitwise operators can represent and manipulate groups of binary flags.

## 57.10 Mathematical Software

Arithmetic expressions evaluate formulas and numerical operations.

---

# 58. Mini Project Ideas

Complete these projects after studying the operator categories.

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

## Project 2: Even or Odd Checker

Requirements:

- Accept an integer.
- Use the modulus operator.
- Display whether it is even or odd.
- Test positive and negative values.

## Project 3: Largest of Three Numbers

Requirements:

- Accept three numbers.
- Compare the values.
- Identify the largest.
- Handle equal values.

## Project 4: Eligibility Checker

Requirements:

- Accept age.
- Ask whether an identity document is available.
- Use comparison operators.
- Use logical operators.
- Display eligibility status.

## Project 5: Range Validator

Requirements:

- Accept a number.
- Check whether it is inside a given range.
- Use chained comparisons.
- Display a suitable result.

## Project 6: Bitwise Calculator

Requirements:

- Accept two integers.
- Perform bitwise AND.
- Perform bitwise OR.
- Perform bitwise XOR.
- Display binary representations.
- Display the results.

## Project 7: Membership Checker

Requirements:

- Create a list of programming languages.
- Accept a language name.
- Check whether it exists.
- Display the result.

## Project 8: Expression Evaluator Practice

Requirements:

- Write multiple expressions.
- Calculate each result.
- Compare results with and without parentheses.
- Explain operator precedence.
- Explain associativity.

## Project 9: Conditional Expression Tool

Requirements:

- Accept a number.
- Determine whether it is positive or non-positive.
- Use a conditional expression.
- Display the result.

## Project 10: Student Result System

Requirements:

- Accept subject marks.
- Calculate total and average.
- Check the passing range.
- Use comparison operators.
- Use logical operators.
- Display a formatted report.

---

# 59. Practice Questions

Attempt the following questions after studying the eight sections.

## Basic Operator Questions

1. What is an operator?
2. What is an operand?
3. What is an expression?
4. What is the difference between an operator and an operand?
5. What is the difference between a unary and binary operator?
6. Why are operators important in programming?
7. What does expression evaluation mean?
8. Can an expression contain multiple operators?
9. Can operands be variables?
10. Can expressions be used as function arguments?

## Arithmetic Operator Questions

11. What is the addition operator?
12. What is the difference between `/` and `//`?
13. What does `%` return?
14. What does `**` perform?
15. What happens when a number is divided by zero?
16. What are unary plus and unary minus?
17. How can you check whether a number is even?
18. How can you find the last digit of a number?
19. What does floor division do with negative values?
20. What is the result of `2 ** 3`?

## Assignment Operator Questions

21. What is the assignment operator?
22. What does `+=` do?
23. What does `-=` do?
24. What is augmented assignment?
25. What is multiple assignment?
26. What is chained assignment?
27. How can two variables be swapped?
28. What are bitwise assignment operators?
29. What is the walrus operator?
30. What is the difference between assignment and an assignment expression?

## Comparison Questions

31. What does `==` do?
32. What does `!=` do?
33. What is the difference between `>` and `>=`?
34. What type of result do comparison expressions generally produce?
35. What is a chained comparison?
36. How can a range be checked using one chained comparison?
37. Are string comparisons supported?
38. Why are comparison operators useful in conditions?
39. What happens when two equal values are compared using `==`?
40. What is the result of `10 < 5`?

## Logical Questions

41. What are logical operators?
42. What does `and` do?
43. What does `or` do?
44. What does `not` do?
45. What is a truthy value?
46. What is a falsy value?
47. What is short-circuit evaluation?
48. How can two conditions be combined?
49. What is the difference between logical and bitwise AND?
50. Do `and` and `or` always return Boolean objects?

## Bitwise Questions

51. What is the binary number system?
52. What does bitwise AND do?
53. What does bitwise OR do?
54. What does bitwise XOR do?
55. What does bitwise NOT do?
56. What is a left shift?
57. What is a right shift?
58. How can bitwise operators be used to check even or odd numbers?
59. What is a bit mask?
60. Why are bitwise operators useful in DSA?

## Membership and Identity Questions

61. What does `in` do?
62. What does `not in` do?
63. How does membership work with dictionaries?
64. What does `is` do?
65. What does `is not` do?
66. What is object identity?
67. What is the difference between `==` and `is`?
68. Why should `is None` be used?
69. Can two equal lists be separate objects?
70. What is the difference between membership and identity?

## Expression Questions

71. What is operator precedence?
72. What is operator associativity?
73. What is left associativity?
74. What is right associativity?
75. Why are parentheses useful?
76. How can parentheses change an expression result?
77. What is a conditional expression?
78. What is the syntax of a conditional expression?
79. Why is precedence important?
80. How can a complex expression be made easier to read?

---

# 60. Practical Challenges

Write these programs independently.

## Challenge 1

Write a program that accepts two numbers and performs all arithmetic operations.

## Challenge 2

Write a program to check whether a number is even or odd.

## Challenge 3

Write a program to find the remainder of a number divided by another number.

## Challenge 4

Write a program to calculate a number's square and cube.

## Challenge 5

Write a program that updates a counter using augmented assignment.

## Challenge 6

Write a program to swap two values using Python assignment.

## Challenge 7

Write a program to compare two numbers.

## Challenge 8

Write a program that checks whether a number lies between 1 and 100.

## Challenge 9

Write a program to combine three conditions using logical operators.

## Challenge 10

Write a program that demonstrates truthy and falsy values.

## Challenge 11

Write a program that demonstrates short-circuit evaluation.

## Challenge 12

Write a program to perform all basic bitwise operations on two integers.

## Challenge 13

Write a program to set, clear, and toggle a particular bit.

## Challenge 14

Write a program to check whether an item exists in a list.

## Challenge 15

Write a program to check whether a dictionary contains a specific key.

## Challenge 16

Write a program to demonstrate the difference between equality and identity.

## Challenge 17

Write a program that compares two mathematical expressions with different parentheses.

## Challenge 18

Write a program demonstrating operator precedence.

## Challenge 19

Write a program demonstrating left and right associativity.

## Challenge 20

Write a program using a conditional expression to find the larger of two numbers.

---

# 61. Recommended Learning Order

Follow this exact order while studying the section.

## Stage 1 — Arithmetic Operators

Folder:

```text
01-Arithmetic-Operators/
```

Learn:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Floor division.
- Modulus.
- Exponentiation.
- Unary operators.

Goal:

Become comfortable with mathematical operations in Python.

## Stage 2 — Assignment Operators

Folder:

```text
02-Assignment-Operators/
```

Learn:

- Assignment.
- Reassignment.
- Augmented assignment.
- Multiple assignment.
- Bitwise assignment.
- Optional walrus operator.

Goal:

Understand how variable values are assigned and updated.

## Stage 3 — Comparison Operators

Folder:

```text
03-Comparison-Operators/
```

Learn:

- Equality.
- Inequality.
- Greater than.
- Less than.
- Greater than or equal.
- Less than or equal.
- Chained comparison.

Goal:

Become comfortable comparing values and producing Boolean results.

## Stage 4 — Logical Operators

Folder:

```text
04-Logical-Operators/
```

Learn:

- `and`.
- `or`.
- `not`.
- Truth tables.
- Truthy and falsy values.
- Short-circuit evaluation.

Goal:

Understand how multiple conditions are combined and evaluated.

## Stage 5 — Bitwise Operators

Folder:

```text
05-Bitwise-Operators/
```

Learn:

- Binary representation.
- AND.
- OR.
- XOR.
- NOT.
- Left shift.
- Right shift.
- Bitwise assignment.

Goal:

Build a foundation for bit manipulation in DSA.

## Stage 6 — Membership Operators

Folder:

```text
06-Membership-Operators/
```

Learn:

- `in`.
- `not in`.
- String membership.
- List membership.
- Tuple membership.
- Set membership.
- Dictionary membership.

Goal:

Understand how to check whether a value belongs to a collection.

## Stage 7 — Identity Operators

Folder:

```text
07-Identity-Operators/
```

Learn:

- `is`.
- `is not`.
- Object identity.
- Reference behavior.
- Equality versus identity.
- `None` checks.

Goal:

Understand how Python checks object identity.

## Stage 8 — Expressions

Folder:

```text
08-Expressions/
```

Study the topics in this order:

1. Expressions.
2. Operator Precedence.
3. Operator Associativity.
4. Parentheses and Grouping.
5. Conditional Expressions.

Goal:

Understand how Python combines and evaluates different operators.

## Stage 9 — Complete Revision

After studying every topic:

- Revise operator symbols.
- Practice mathematical expressions.
- Review comparison and logical conditions.
- Practice bitwise operations.
- Understand membership and identity.
- Solve expression evaluation questions.
- Complete practical challenges.
- Build a small project.

---

# 62. Study Strategy

Use the following approach while learning.

## First: Understand the Operator

Read the definition and identify the operator's purpose.

## Second: Learn the Syntax

Understand how the operator is written in Python.

## Third: Study Examples

Run the examples in the corresponding Python file.

## Fourth: Change the Values

Modify operands and observe the results.

## Fifth: Trace Expressions

Evaluate expressions manually step by step.

## Sixth: Understand Errors

Try incorrect operations and read the error messages.

## Seventh: Complete Solved Programs

Understand how each operator is applied in a practical problem.

## Eighth: Attempt Unsolved Questions

Write the solutions independently.

## Ninth: Apply the Concepts

Build small programs combining multiple operator categories.

## Tenth: Revise for DSA

Practice arithmetic, comparisons, logical expressions, and bitwise operations.

---

# 63. Revision Notes

Use these points during revision.

## Operators and Expressions

- An operator performs an operation.
- An operand is the value on which an operator works.
- An expression combines values and operators.
- Python evaluates expressions according to language rules.

## Arithmetic Operators

- `+` performs addition.
- `-` performs subtraction.
- `*` performs multiplication.
- `/` performs division.
- `//` performs floor division.
- `%` returns a remainder.
- `**` performs exponentiation.

## Assignment Operators

- `=` performs assignment.
- `+=` performs addition followed by assignment.
- `-=` performs subtraction followed by assignment.
- Other augmented operators update values using their corresponding operations.
- `:=` is the assignment expression operator.

## Comparison Operators

- `==` checks equality.
- `!=` checks inequality.
- `>` checks whether the left value is greater.
- `<` checks whether the left value is smaller.
- `>=` checks greater than or equal.
- `<=` checks less than or equal.

## Logical Operators

- `and` combines conditions.
- `or` evaluates alternatives.
- `not` negates a truth value.
- Logical operations can short-circuit.
- `and` and `or` can return operands rather than only Boolean objects.

## Bitwise Operators

- `&` performs bitwise AND.
- `|` performs bitwise OR.
- `^` performs bitwise XOR.
- `~` performs bitwise inversion.
- `<<` performs left shift.
- `>>` performs right shift.

## Membership Operators

- `in` checks membership.
- `not in` checks non-membership.
- Dictionary membership checks keys by default.

## Identity Operators

- `is` checks object identity.
- `is not` checks that references are not identical.
- Use `==` for ordinary value equality.
- Use `is None` for checking `None`.

## Expressions

- Precedence determines which operations are grouped first.
- Associativity determines grouping for operators with equal precedence.
- Parentheses can explicitly control grouping.
- Conditional expressions select one of two results.

---

# 64. Quick Reference

## Arithmetic Operators

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
```

## Assignment Operators

```python
number = 10

number += 5
number -= 2
number *= 2
number /= 2
```

## Comparison Operators

```python
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 10)
```

## Logical Operators

```python
print(True and False)
print(True or False)
print(not True)
```

## Bitwise Operators

```python
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)
```

## Membership Operators

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(40 not in numbers)
```

## Identity Operators

```python
value = None

print(value is None)
print(value is not None)
```

## Expressions

```python
result = 10 + 5 * 2

print(result)
```

## Parentheses

```python
result = (10 + 5) * 2

print(result)
```

## Conditional Expression

```python
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

---

# 65. Frequently Asked Questions

## Q1. What is an operator?

An operator is a symbol or keyword that performs an operation on one or more operands.

## Q2. What is an operand?

An operand is a value or object on which an operator performs an operation.

## Q3. What is an expression?

An expression combines values, variables, operators, or other valid Python constructs and evaluates to produce a result.

## Q4. What are arithmetic operators?

They are operators used for mathematical calculations.

## Q5. What is the difference between `/` and `//`?

`/` performs division. `//` performs floor division.

## Q6. What does `%` do?

It returns the remainder of a division operation.

## Q7. What does `**` do?

It performs exponentiation.

## Q8. What is an assignment operator?

An assignment operator associates a value with a variable or updates a variable.

## Q9. What does `+=` do?

It performs addition followed by assignment.

## Q10. What is an augmented assignment operator?

It combines an operation with assignment.

## Q11. What is the walrus operator?

It is the assignment expression operator `:=`.

## Q12. What are comparison operators?

They compare values and generally produce Boolean results.

## Q13. What does `==` do?

It checks value equality.

## Q14. What does `!=` do?

It checks whether values compare unequal.

## Q15. What are logical operators?

They combine or negate truth values.

## Q16. What does `and` do?

It evaluates two operands using truth-value rules and short-circuits when the result is determined.

## Q17. What does `or` do?

It evaluates alternatives and can short-circuit when the result is determined.

## Q18. What does `not` do?

It returns the Boolean negation of the truth value of its operand.

## Q19. What is a truthy value?

A value that evaluates as true in a Boolean context.

## Q20. What is a falsy value?

A value that evaluates as false in a Boolean context.

## Q21. What are bitwise operators?

They operate on the binary representation of integers.

## Q22. What is bitwise AND?

It performs AND operations on corresponding bits.

## Q23. What is bitwise OR?

It performs OR operations on corresponding bits.

## Q24. What is bitwise XOR?

It produces a one bit when the corresponding bits differ.

## Q25. What is a left shift?

It shifts integer bits toward the left by a specified number of positions.

## Q26. What is a right shift?

It shifts integer bits toward the right by a specified number of positions.

## Q27. What are membership operators?

They check whether an element belongs to a collection or sequence.

## Q28. What does `in` do?

It checks whether a value is present in a supported container or sequence.

## Q29. What does `not in` do?

It checks whether a value is absent from a supported container or sequence.

## Q30. What are identity operators?

They check whether references refer to the same object.

## Q31. What does `is` do?

It checks object identity.

## Q32. What does `is not` do?

It checks whether two references are not identical.

## Q33. What is the difference between `==` and `is`?

`==` compares values for equality. `is` compares object identity.

## Q34. What is operator precedence?

It determines which operators are grouped first in an expression.

## Q35. What is associativity?

It determines how operators of the same precedence are grouped.

## Q36. What is left associativity?

It means operators of the same precedence are grouped from the left, when the operator's rules specify left associativity.

## Q37. What is right associativity?

It means operators are grouped from the right, as with exponentiation.

## Q38. Why are parentheses used?

They explicitly group expressions and can change their evaluation.

## Q39. What is a conditional expression?

It selects one of two expressions based on a condition.

## Q40. Why are operators important for DSA?

They are used in calculations, comparisons, conditions, indexing, searching, sorting, and bit manipulation.

---

# 66. Viva Questions and Answers

Use these questions for practical examinations, interviews, and revision.

## Basic Concepts

### 1. Define an operator.

An operator is a symbol or keyword that performs an operation on one or more operands.

### 2. What is an operand?

An operand is a value or object used by an operator.

### 3. Define an expression.

An expression is a combination of values, operators, and other valid constructs that evaluates to a result.

### 4. What is a unary operator?

An operator that works with one operand.

### 5. What is a binary operator?

An operator that works with two operands.

## Arithmetic Operators

### 6. Which operator performs addition?

`+`.

### 7. Which operator performs subtraction?

`-`.

### 8. Which operator performs multiplication?

`*`.

### 9. Which operator performs division?

`/`.

### 10. What is the difference between `/` and `//`?

`/` performs division, while `//` performs floor division.

### 11. What does `%` return?

It returns the remainder.

### 12. Which operator performs exponentiation?

`**`.

### 13. What is unary minus?

It changes the sign of a numeric operand according to the type's rules.

### 14. What exception occurs during division by zero?

For ordinary numeric division, `ZeroDivisionError`.

## Assignment Operators

### 15. Which operator performs basic assignment?

`=`.

### 16. What does `+=` mean?

It performs addition followed by assignment.

### 17. What is augmented assignment?

It combines an operation with assignment.

### 18. What is multiple assignment?

Assigning values to multiple variables in one statement.

### 19. What is variable swapping?

Exchanging the values associated with two variables.

### 20. What is the walrus operator?

The assignment expression operator `:=`.

## Comparison Operators

### 21. Which operator checks equality?

`==`.

### 22. Which operator checks inequality?

`!=`.

### 23. Which operator checks greater than?

`>`.

### 24. Which operator checks less than?

`<`.

### 25. What is the typical result type of a comparison?

`bool`.

### 26. What is a chained comparison?

A comparison expression containing more than one comparison operation in a chain.

## Logical Operators

### 27. Name the three logical operators in Python.

`and`, `or`, and `not`.

### 28. What does AND mean?

It produces a truthy result only when both operands are truthy, and returns one of the operands according to Python's evaluation rules.

### 29. What does OR mean?

It selects an operand according to truth-value rules and short-circuits when a truthy result is found.

### 30. What is NOT?

It negates the truth value of its operand and returns a Boolean result.

### 31. What is short-circuit evaluation?

It is the behavior in which Python skips evaluating a later operand when the logical result is already determined.

## Bitwise Operators

### 32. Name the bitwise operators.

`&`, `|`, `^`, `~`, `<<`, and `>>`.

### 33. What does bitwise AND do?

It sets a result bit when both corresponding operand bits are one.

### 34. What does bitwise OR do?

It sets a result bit when at least one corresponding operand bit is one.

### 35. What does XOR do?

It sets a result bit when the corresponding operand bits differ.

### 36. What is a bitwise shift?

It moves integer bits left or right.

### 37. What is a bit mask?

A bit pattern used to select, set, clear, or inspect particular bits.

## Membership and Identity

### 38. Which operators check membership?

`in` and `not in`.

### 39. Which operators check identity?

`is` and `is not`.

### 40. What is the difference between equality and identity?

Equality compares values. Identity checks whether references point to the same object.

### 41. How should None be checked?

Use `is None` or `is not None`.

### 42. Does dictionary membership check values by default?

No. It checks dictionary keys by default.

## Expressions

### 43. Define operator precedence.

It determines which operators are grouped first in an expression.

### 44. Define associativity.

It determines how operators of the same precedence are grouped.

### 45. What is left associativity?

Grouping from the left according to the operator's rules.

### 46. What is right associativity?

Grouping from the right according to the operator's rules.

### 47. Which direction is exponentiation grouped?

Right to left.

### 48. What is the purpose of parentheses?

They explicitly group expressions and can override ordinary precedence.

### 49. What is a conditional expression?

An expression that selects one of two values based on a condition.

### 50. Why are operators important in DSA?

They are used in mathematical calculations, comparison, conditions, searching, sorting, and bit manipulation.

---

# 67. Important Terminology

**Operator:** A symbol or keyword used to perform an operation.

**Operand:** A value or object used by an operator.

**Expression:** A combination of values and operations that evaluates to a result.

**Unary Operator:** An operator that works with one operand.

**Binary Operator:** An operator that works with two operands.

**Arithmetic Operator:** An operator used for mathematical calculations.

**Assignment Operator:** An operator used to assign or update values.

**Augmented Assignment:** A form of assignment that combines an operation with updating a variable.

**Comparison Operator:** An operator used to compare values.

**Logical Operator:** An operator used to combine or negate truth values.

**Bitwise Operator:** An operator that performs operations on integer bits.

**Membership Operator:** An operator that checks whether a value belongs to a collection or sequence.

**Identity Operator:** An operator that checks whether references point to the same object.

**Expression Evaluation:** The process by which Python computes the value of an expression.

**Operator Precedence:** The rules that determine which operators are grouped first.

**Operator Associativity:** The rules that determine how operators of the same precedence are grouped.

**Short-Circuit Evaluation:** The process of skipping evaluation of a later logical operand when the result is already known.

**Truthy Value:** A value that evaluates as true in a Boolean context.

**Falsy Value:** A value that evaluates as false in a Boolean context.

**Bit Manipulation:** Working with individual bits in a number.

**Bit Mask:** A pattern of bits used to select or modify particular bits.

**Chained Comparison:** A comparison expression linking multiple comparisons.

**Conditional Expression:** An expression that chooses a result according to a condition.

**Walrus Operator:** The assignment expression operator `:=`.

**Object Identity:** The identity of an object, checked with `is` and `is not`.

**Value Equality:** Equality determined by the `==` operator.

---

# 68. Learning Checklist

Use this checklist after completing the entire section.

## Section 1 — Arithmetic Operators

- [ ] I understand what arithmetic operators are.
- [ ] I can use addition.
- [ ] I can use subtraction.
- [ ] I can use multiplication.
- [ ] I can use division.
- [ ] I can use floor division.
- [ ] I can use modulus.
- [ ] I can use exponentiation.
- [ ] I understand unary plus and minus.
- [ ] I understand division by zero.
- [ ] I can solve simple mathematical problems.

## Section 2 — Assignment Operators

- [ ] I understand basic assignment.
- [ ] I can use reassignment.
- [ ] I can use augmented assignment.
- [ ] I can use addition assignment.
- [ ] I can use subtraction assignment.
- [ ] I can use multiplication assignment.
- [ ] I can use division assignment.
- [ ] I understand bitwise assignment.
- [ ] I can perform multiple assignment.
- [ ] I can swap variable values.
- [ ] I understand the optional walrus operator.

## Section 3 — Comparison Operators

- [ ] I can use equality comparison.
- [ ] I can use inequality comparison.
- [ ] I can use greater-than comparison.
- [ ] I can use less-than comparison.
- [ ] I can use greater-than-or-equal comparison.
- [ ] I can use less-than-or-equal comparison.
- [ ] I understand Boolean results.
- [ ] I can write chained comparisons.
- [ ] I can check numeric ranges.

## Section 4 — Logical Operators

- [ ] I understand logical AND.
- [ ] I understand logical OR.
- [ ] I understand logical NOT.
- [ ] I can read logical truth tables.
- [ ] I understand truthy values.
- [ ] I understand falsy values.
- [ ] I understand short-circuit evaluation.
- [ ] I can combine multiple conditions.
- [ ] I can write logical expressions.

## Section 5 — Bitwise Operators

- [ ] I understand binary representation.
- [ ] I can use bitwise AND.
- [ ] I can use bitwise OR.
- [ ] I can use bitwise XOR.
- [ ] I understand bitwise NOT.
- [ ] I can use left shift.
- [ ] I can use right shift.
- [ ] I understand bitwise assignment.
- [ ] I can check even or odd using a bitwise expression.
- [ ] I understand basic bit masks.

## Section 6 — Membership Operators

- [ ] I understand `in`.
- [ ] I understand `not in`.
- [ ] I can check membership in strings.
- [ ] I can check membership in lists.
- [ ] I can check membership in tuples.
- [ ] I can check membership in sets.
- [ ] I can check dictionary keys.
- [ ] I understand membership testing.

## Section 7 — Identity Operators

- [ ] I understand `is`.
- [ ] I understand `is not`.
- [ ] I understand object identity.
- [ ] I understand the difference between `==` and `is`.
- [ ] I can check for `None`.
- [ ] I understand basic object reference behavior.

## Section 8 — Expressions

- [ ] I understand expressions.
- [ ] I can evaluate arithmetic expressions.
- [ ] I understand operator precedence.
- [ ] I understand operator associativity.
- [ ] I understand left associativity.
- [ ] I understand right associativity.
- [ ] I can group expressions using parentheses.
- [ ] I can evaluate nested expressions.
- [ ] I can use conditional expressions.
- [ ] I can simplify complicated expressions.

## Combined Programming

- [ ] I can combine arithmetic operators.
- [ ] I can combine comparison and logical operators.
- [ ] I can write expressions using variables.
- [ ] I can perform bitwise operations.
- [ ] I can use membership checks.
- [ ] I can use identity checks appropriately.
- [ ] I can understand expression evaluation.
- [ ] I can debug operator-related errors.
- [ ] I can write practical Python programs.
- [ ] I can solve basic DSA-related problems using operators.

---

# 69. Final Summary

Operators and Expressions are essential parts of Python programming.

Operators perform operations on values.

Operands are the values used by operators.

Expressions combine variables, values, operators, and other valid constructs to produce results.

This section contains eight main categories.

## Section 1 — Arithmetic Operators

You learned:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Floor division.
- Modulus.
- Exponentiation.
- Unary operators.

## Section 2 — Assignment Operators

You learned:

- Assignment.
- Reassignment.
- Augmented assignment.
- Multiple assignment.
- Bitwise assignment.
- Optional assignment expressions.

## Section 3 — Comparison Operators

You learned:

- Equal to.
- Not equal to.
- Greater than.
- Less than.
- Greater than or equal to.
- Less than or equal to.
- Chained comparisons.

## Section 4 — Logical Operators

You learned:

- AND.
- OR.
- NOT.
- Truth tables.
- Truthy and falsy values.
- Short-circuit evaluation.

## Section 5 — Bitwise Operators

You learned:

- Binary representation.
- AND.
- OR.
- XOR.
- NOT.
- Left shift.
- Right shift.
- Bit manipulation.

## Section 6 — Membership Operators

You learned:

- `in`.
- `not in`.
- Membership in strings.
- Membership in lists.
- Membership in tuples.
- Membership in sets.
- Membership in dictionaries.

## Section 7 — Identity Operators

You learned:

- `is`.
- `is not`.
- Object identity.
- Equality versus identity.
- Checking `None`.

## Section 8 — Expressions

You learned:

- Expression basics.
- Operator precedence.
- Operator associativity.
- Parentheses and grouping.
- Conditional expressions.

## Important Points to Remember

1. Operators perform operations.
2. Operands are the values on which operators work.
3. Expressions evaluate to produce results.
4. Arithmetic operators perform mathematical calculations.
5. Assignment operators assign or update values.
6. Comparison operators compare values.
7. Logical operators combine or negate truth values.
8. Bitwise operators manipulate integer bits.
9. Membership operators check whether values belong to collections.
10. Identity operators check object identity.
11. Equality and identity are different.
12. Operator precedence determines expression grouping.
13. Operator associativity determines grouping for operators of equal precedence.
14. Parentheses can control expression grouping.
15. Short-circuit evaluation can skip unnecessary logical operands.
16. Conditional expressions select values based on conditions.
17. Bitwise operations are useful for DSA.
18. Expressions should be written clearly and tested carefully.

## Recommended Completion Order

Follow this sequence:

**First:** `01-Arithmetic-Operators`

Learn mathematical operations and their behavior.

**Second:** `02-Assignment-Operators`

Learn how to assign and update values.

**Third:** `03-Comparison-Operators`

Learn how to compare values.

**Fourth:** `04-Logical-Operators`

Learn how to combine conditions.

**Fifth:** `05-Bitwise-Operators`

Learn binary operations and bit manipulation.

**Sixth:** `06-Membership-Operators`

Learn how to check whether values exist in collections.

**Seventh:** `07-Identity-Operators`

Learn how to compare object identity.

**Eighth:** `08-Expressions`

Learn expression evaluation, precedence, associativity, grouping, and conditional expressions.

**Finally:** Complete practical exercises and mini projects.

## Final Learning Goal

After completing this section, you should be able to:

1. Identify Python operators.
2. Understand operands.
3. Construct expressions.
4. Perform mathematical operations.
5. Assign and update variables.
6. Compare values.
7. Combine conditions.
8. Manipulate integer bits.
9. Check membership.
10. Understand object identity.
11. Evaluate complex expressions.
12. Apply operators in practical programs.
13. Use operators in basic DSA problems.

**Operators → Expressions → Precedence → Associativity → Practical Programming**

This is the foundation for using operators and expressions throughout Python programming.