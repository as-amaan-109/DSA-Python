# Python Operator Associativity

**Week:** 01 – Programming Fundamentals  
**Main Topic:** Operators and Expressions  
**Subtopic:** Operator Associativity  
**Folder:** `03-operator-associativity`  
**Python File:** `03_operator_associativity.py`  
**Level:** Beginner to Intermediate

---

# 1. Introduction to Operator Associativity

Operator associativity is an important concept in Python programming.

When an expression contains multiple operators that have the same precedence, Python needs rules to determine how those operators are grouped.

These rules are called **operator associativity**.

In simple words:

**Operator associativity determines how operators with the same precedence are grouped in an expression.**

There are two commonly discussed directions:

1. Left-to-right associativity.
2. Right-to-left associativity.

### Example 1: Left-to-Right Associativity

```python
result = 20 - 5 - 2

print(result)
```

**Output:**

```text
13
```

Subtraction is grouped from left to right.

```text
20 - 5 - 2
(20 - 5) - 2
15 - 2
13
```

### Example 2: Right-to-Left Associativity

```python
result = 2 ** 3 ** 2

print(result)
```

**Output:**

```text
512
```

Exponentiation is grouped from right to left.

```text
2 ** 3 ** 2
2 ** (3 ** 2)
2 ** 9
512
```

### Why Is Operator Associativity Important?

Associativity helps Python determine the grouping of expressions when multiple operators have the same precedence.

It is important when working with:

- Arithmetic calculations.
- Mathematical expressions.
- Exponentiation.
- Multiplication and division.
- Addition and subtraction.
- Bitwise operations.
- Logical expressions.
- Comparison expressions.
- Conditional expressions.
- Complex programming conditions.
- Data Structures and Algorithms.

Understanding associativity helps prevent unexpected results while evaluating expressions.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand operator associativity.
2. Explain the meaning of left-to-right associativity.
3. Explain the meaning of right-to-left associativity.
4. Understand the difference between precedence and associativity.
5. Understand subtraction associativity.
6. Understand addition associativity.
7. Understand division associativity.
8. Understand multiplication and division grouping.
9. Understand modulus and floor division grouping.
10. Understand exponentiation associativity.
11. Understand unary operators and exponentiation.
12. Understand shift operator associativity.
13. Understand bitwise operator grouping.
14. Understand logical AND associativity.
15. Understand logical OR associativity.
16. Understand short-circuit evaluation.
17. Understand chained comparisons.
18. Understand nested conditional expressions.
19. Use parentheses to change expression grouping.
20. Evaluate complicated expressions step by step.
21. Identify common associativity mistakes.
22. Apply associativity to mathematical problems.
23. Apply associativity to logical conditions.
24. Apply associativity to DSA expressions.
25. Complete all 12 solved problems.
26. Attempt all 10 unsolved practice questions.

---

# 3. Prerequisites

Before learning operator associativity, you should understand the following Python concepts.

| Concept | Why It Is Required |
|---|---|
| Variables | To store values used in expressions |
| Arithmetic Operators | To understand arithmetic grouping |
| Comparison Operators | To understand comparison expressions |
| Logical Operators | To understand `and`, `or`, and `not` |
| Bitwise Operators | To understand bitwise associativity |
| Expressions | To understand expression evaluation |
| Operator Precedence | To understand operator priority |
| Parentheses | To understand expression grouping |
| Conditional Statements | To understand conditions and decisions |
| Functions | To understand interactive programming examples |

### Recommended Revision

Before starting this topic, revise:

- `01-Arithmetic-Operators`
- `03-Comparison-Operators`
- `04-Logical-Operators`
- `05-Bitwise-Operators`
- `08-Expressions/01-expressions`
- `08-Expressions/02-operator-precedence`

---

# 4. What Is Operator Associativity?

Operator associativity determines the grouping direction of operators that have the same precedence, subject to Python's special expression rules.

Consider:

```python
result = 20 - 5 - 2
```

Both subtraction operators have the same precedence.

Python groups them from left to right.

Therefore:

```text
20 - 5 - 2
(20 - 5) - 2
15 - 2
13
```

The result is `13`.

### Another Example

```python
result = 100 / 10 / 2

print(result)
```

**Output:**

```text
5.0
```

Grouping:

```text
(100 / 10) / 2
10.0 / 2
5.0
```

Division groups from left to right.

### Important Point

Associativity and precedence are different concepts.

- Precedence determines which operator has priority.
- Associativity determines how equal-precedence operators are grouped.
- Parentheses can explicitly change grouping.
- Some operators, such as comparisons, have special chaining behavior.

---

# 5. Types of Operator Associativity

Two common associativity directions are discussed in programming.

## 5.1 Left-to-Right Associativity

Left-to-right associativity means that operators of the same precedence are grouped starting from the left side.

### Example

```python
result = 20 - 5 - 2

print(result)
```

**Output:**

```text
13
```

Grouping:

```text
(20 - 5) - 2
15 - 2
13
```

### Another Example

```python
result = 100 / 10 / 2

print(result)
```

**Output:**

```text
5.0
```

Grouping:

```text
(100 / 10) / 2
10.0 / 2
5.0
```

### Common Left-Associative Operators

Many Python binary operators group from left to right, including:

- Addition.
- Subtraction.
- Multiplication.
- Division.
- Floor division.
- Modulus.
- Bitwise AND.
- Bitwise OR.
- Bitwise XOR.
- Bitwise shifts.
- Logical AND.
- Logical OR.

However, logical operators use short-circuit evaluation, and some operators have special behavior. The exact grouping and evaluation rules should always be understood for the operator involved.

## 5.2 Right-to-Left Associativity

Right-to-left associativity means that operators are grouped starting from the right side.

### Example

```python
result = 2 ** 3 ** 2

print(result)
```

**Output:**

```text
512
```

Grouping:

```text
2 ** (3 ** 2)
2 ** 9
512
```

### Important Operator

Python exponentiation is right-associative.

### Another Example

```python
result = 3 ** 2 ** 2

print(result)
```

**Output:**

```text
81
```

Grouping:

```text
3 ** (2 ** 2)
3 ** 4
81
```

### Important Note

Python also has other special grouping behavior, particularly for comparison chaining and conditional expressions.

Therefore, it is not correct to assume that every Python expression follows only two simple left-to-right or right-to-left rules.

---

# 6. Difference Between Operator Precedence and Associativity

Operator precedence and operator associativity are related, but they are not the same.

## 6.1 Operator Precedence

Precedence determines which operator has higher priority.

Example:

```python
result = 10 + 5 * 2

print(result)
```

**Output:**

```text
20
```

Multiplication has higher precedence than addition.

Grouping:

```text
10 + (5 * 2)
10 + 10
20
```

## 6.2 Operator Associativity

Associativity determines how operators with equal precedence are grouped.

Example:

```python
result = 20 - 5 - 2

print(result)
```

**Output:**

```text
13
```

Grouping:

```text
(20 - 5) - 2
15 - 2
13
```

## 6.3 Complete Difference

| Operator Precedence | Operator Associativity |
|---|---|
| Determines operator priority | Determines grouping for equal-precedence operators |
| Decides which group binds more tightly | Decides how operators in the same group associate |
| Example: `+` and `*` | Example: `-` and `+` |
| Multiplication before addition | Subtraction before the next addition in a left-grouped expression |
| Explains different priority levels | Explains grouping direction |

### Remember

Precedence answers:

**Which operator has higher priority?**

Associativity answers:

**How are operators of the same precedence grouped?**

---

# 7. Left-to-Right Associativity with Subtraction

Subtraction is a left-associative binary operator.

When multiple subtraction operators appear at the same precedence level, Python groups them from left to right.

### Example 1

```python
result = 20 - 5 - 2

print(result)
```

**Output:**

```text
13
```

### Step-by-Step Evaluation

Original expression:

```text
20 - 5 - 2
```

Grouping:

```text
(20 - 5) - 2
```

First subtraction:

```text
20 - 5 = 15
```

Second subtraction:

```text
15 - 2 = 13
```

Final result:

```text
13
```

### Example 2

```python
result = 50 - 10 - 5 - 2

print(result)
```

**Output:**

```text
33
```

Grouping:

```text
(((50 - 10) - 5) - 2)
```

Evaluation:

```text
50 - 10 = 40
40 - 5 = 35
35 - 2 = 33
```

### Example 3: Parentheses Change Grouping

```python
result = 20 - (5 - 2)

print(result)
```

**Output:**

```text
17
```

Evaluation:

```text
20 - (5 - 2)
20 - 3
17
```

Without parentheses, the result would be `13`.

### Practical Application

Subtraction expressions are useful for:

- Calculating remaining balance.
- Finding price differences.
- Calculating remaining stock.
- Calculating remaining time.
- Calculating differences between measurements.

---

# 8. Left-to-Right Associativity with Division

Division is a left-associative binary operator.

When multiple division operators occur with the same precedence, they group from left to right.

### Example 1

```python
result = 100 / 10 / 2

print(result)
```

**Output:**

```text
5.0
```

### Evaluation

```text
100 / 10 / 2
(100 / 10) / 2
10.0 / 2
5.0
```

### Example 2

```python
result = 120 / 10 / 3

print(result)
```

**Output:**

```text
4.0
```

Evaluation:

```text
(120 / 10) / 3
12.0 / 3
4.0
```

### Example 3: Parentheses Change Grouping

```python
result = 100 / (10 / 2)

print(result)
```

**Output:**

```text
20.0
```

Evaluation:

```text
100 / (10 / 2)
100 / 5
20.0
```

### Important Difference

```python
print(100 / 10 / 2)
print(100 / (10 / 2))
```

**Output:**

```text
5.0
20.0
```

The results differ because parentheses change the grouping.

### Important Rule

Division by zero raises `ZeroDivisionError`.

Always validate divisors when using user input.

---

# 9. Multiplication and Division Associativity

Multiplication and division have the same precedence.

When they appear together without parentheses, they group from left to right.

### Example 1

```python
result = 100 / 10 * 2

print(result)
```

**Output:**

```text
20.0
```

Grouping:

```text
(100 / 10) * 2
10.0 * 2
20.0
```

### Example 2

```python
result = 5 * 4 / 2

print(result)
```

**Output:**

```text
10.0
```

Grouping:

```text
(5 * 4) / 2
20 / 2
10.0
```

### Example 3

```python
result = 100 * 2 / 10

print(result)
```

**Output:**

```text
20.0
```

Grouping:

```text
(100 * 2) / 10
200 / 10
20.0
```

### Important Note

Although multiplication is mathematically associative in many ordinary cases, multiplication and division are not interchangeable.

Compare:

```python
print(100 / 10 * 2)
print(100 * 10 / 2)
```

**Output:**

```text
20.0
500.0
```

The grouping is important.

### Practical Applications

- Calculating unit prices.
- Calculating average cost.
- Converting measurements.
- Calculating speed.
- Calculating financial values.

---

# 10. Addition and Subtraction Associativity

Addition and subtraction have equal precedence.

They normally group from left to right.

### Example 1

```python
result = 20 + 5 - 3 + 2

print(result)
```

**Output:**

```text
24
```

Grouping:

```text
(((20 + 5) - 3) + 2)
```

Evaluation:

```text
20 + 5 = 25
25 - 3 = 22
22 + 2 = 24
```

### Example 2

```python
result = 50 + 10 - 5 + 2

print(result)
```

**Output:**

```text
57
```

Grouping:

```text
(((50 + 10) - 5) + 2)
```

Evaluation:

```text
50 + 10 = 60
60 - 5 = 55
55 + 2 = 57
```

### Example 3: Using Parentheses

```python
result = 20 + (5 - 3 + 2)

print(result)
```

**Output:**

```text
24
```

Grouping:

```text
20 + ((5 - 3) + 2)
20 + (2 + 2)
20 + 4
24
```

### Practical Applications

Addition and subtraction are used in:

- Bank balance calculations.
- Inventory tracking.
- Marks calculations.
- Profit and loss calculations.
- Distance calculations.

---

# 11. Exponentiation Associativity

Exponentiation is a special case in Python.

The `**` operator is right-associative.

This means that an unparenthesized chain of exponentiation is grouped from right to left.

### Syntax

```python
base ** exponent
```

### Example 1

```python
result = 2 ** 3 ** 2

print(result)
```

**Output:**

```text
512
```

### Grouping

```text
2 ** 3 ** 2
2 ** (3 ** 2)
2 ** 9
512
```

### Example 2

```python
result = 3 ** 2 ** 2

print(result)
```

**Output:**

```text
81
```

Grouping:

```text
3 ** (2 ** 2)
3 ** 4
81
```

### Example 3

```python
result = 2 ** 2 ** 3

print(result)
```

**Output:**

```text
256
```

Grouping:

```text
2 ** (2 ** 3)
2 ** 8
256
```

### Why Is This Important?

A beginner might calculate:

```text
(2 ** 3) ** 2
8 ** 2
64
```

But Python evaluates:

```text
2 ** (3 ** 2)
2 ** 9
512
```

### Important Rule

When exponentiation is chained, group it from right to left.

Use parentheses whenever you want a different grouping.

---

# 12. Exponentiation with Parentheses

Parentheses can change the grouping of exponentiation.

### Example 1: Right Grouping

```python
result = 2 ** (3 ** 2)

print(result)
```

**Output:**

```text
512
```

Evaluation:

```text
3 ** 2 = 9
2 ** 9 = 512
```

### Example 2: Left Grouping

```python
result = (2 ** 3) ** 2

print(result)
```

**Output:**

```text
64
```

Evaluation:

```text
2 ** 3 = 8
8 ** 2 = 64
```

### Comparison

| Expression | Grouping | Result |
|---|---|---:|
| `2 ** 3 ** 2` | `2 ** (3 ** 2)` | 512 |
| `(2 ** 3) ** 2` | Left grouped | 64 |
| `2 ** (3 ** 2)` | Right grouped | 512 |

### Another Example

```python
a = 3

result1 = a ** 2 ** 2
result2 = (a ** 2) ** 2

print(result1)
print(result2)
```

**Output:**

```text
81
81
```

Here, both produce the same numerical result because of the selected values.

This is a useful reminder that different groupings do not always produce different answers.

### Best Practice

Use parentheses to communicate the intended mathematical grouping rather than relying on readers to remember the associativity rule.

---

# 13. Unary Operators and Exponentiation

Unary operators operate on one operand.

Examples include:

- Unary plus `+x`.
- Unary minus `-x`.
- Bitwise NOT `~x`.

Unary minus and exponentiation have a special relationship in Python.

### Example 1

```python
result = -2 ** 2

print(result)
```

**Output:**

```text
-4
```

Grouping:

```text
-(2 ** 2)
-4
```

### Example 2

```python
result = (-2) ** 2

print(result)
```

**Output:**

```text
4
```

Grouping:

```text
(-2) ** 2
(-2) * (-2)
4
```

### Example 3: Negative Exponent

```python
result = 2 ** -2

print(result)
```

**Output:**

```text
0.25
```

Python allows a unary expression on the right side of exponentiation.

The expression is interpreted as:

```python
2 ** (-2)
```

### Important Difference

| Expression | Result |
|---|---:|
| `-2 ** 2` | -4 |
| `(-2) ** 2` | 4 |
| `-(2 ** 2)` | -4 |
| `2 ** -2` | 0.25 |

### Remember

Exponentiation groups from right to left, but its interaction with unary operators is not a simple rule that every symbol is always grouped in the same direction.

---

# 14. Shift Operator Associativity

Python provides two bitwise shift operators:

- `<<` — Left shift.
- `>>` — Right shift.

These operators share the same precedence and group from left to right.

### Example 1: Right Shift

```python
result = 64 >> 1 >> 1

print(result)
```

**Output:**

```text
16
```

Grouping:

```text
(64 >> 1) >> 1
32 >> 1
16
```

### Example 2: Left Shift

```python
result = 2 << 2 << 1

print(result)
```

**Output:**

```text
16
```

Grouping:

```text
(2 << 2) << 1
8 << 1
16
```

### Example 3: Parentheses

```python
result = 64 >> (1 >> 1)

print(result)
```

**Output:**

```text
64
```

Evaluation:

```text
1 >> 1 = 0
64 >> 0 = 64
```

### Important Point

Left and right shift operations are different bitwise operations.

For more details about their binary behavior, refer to:

`../../05-Bitwise-Operators/README.md`

---

# 15. Bitwise Operator Associativity

Python provides three main bitwise binary operators:

- `&` — Bitwise AND.
- `^` — Bitwise XOR.
- `|` — Bitwise OR.

These operators have different precedence levels:

```text
Bitwise AND &
      |
      v
Bitwise XOR ^
      |
      v
Bitwise OR |
```

When multiple operators of the same precedence occur, they generally group from left to right.

### Example 1: Bitwise AND

```python
result = 15 & 7 & 3

print(result)
```

**Output:**

```text
3
```

Grouping:

```text
(15 & 7) & 3
7 & 3
3
```

### Example 2: Bitwise OR

```python
result = 1 | 2 | 4

print(result)
```

**Output:**

```text
7
```

Grouping:

```text
(1 | 2) | 4
3 | 4
7
```

### Example 3: Bitwise XOR

```python
result = 7 ^ 3 ^ 1

print(result)
```

**Output:**

```text
5
```

Grouping:

```text
(7 ^ 3) ^ 1
4 ^ 1
5
```

### Important Note

The operators `&`, `^`, and `|` have different precedence levels.

Therefore, when combining them, precedence determines the grouping before associativity becomes relevant.

---

# 16. Logical AND Associativity

The logical AND operator is written as:

```python
and
```

It returns a result based on the truthiness of its operands.

Logical AND has left-to-right grouping.

### Example 1

```python
result = True and False and True

print(result)
```

**Output:**

```text
False
```

Grouping:

```text
(True and False) and True
False and True
False
```

### Example 2

```python
result = True and True and True

print(result)
```

**Output:**

```text
True
```

### Example 3

```python
result = False and True and True

print(result)
```

**Output:**

```text
False
```

### Short-Circuit Evaluation

Logical AND also uses short-circuit evaluation.

If the first operand is falsy, Python does not need to evaluate the remaining operands.

Example:

```python
result = False and print("This will not execute")

print(result)
```

**Output:**

```text
False
```

The `print()` call is skipped because the first operand is already falsy.

### Important Technical Point

Python's `and` operator does not always return a Boolean.

It returns one of its operands.

Example:

```python
result = 10 and 20

print(result)
```

**Output:**

```text
20
```

Both operands are truthy, so the final operand is returned.

---

# 17. Logical OR Associativity

The logical OR operator is written as:

```python
or
```

It returns a truthy operand when one is found; otherwise, it returns the final falsy operand.

Logical OR has left-to-right grouping.

### Example 1

```python
result = False or False or True

print(result)
```

**Output:**

```text
True
```

Grouping:

```text
(False or False) or True
False or True
True
```

### Example 2

```python
result = True or False or False

print(result)
```

**Output:**

```text
True
```

### Example 3

```python
result = False or False or False

print(result)
```

**Output:**

```text
False
```

### Short-Circuit Evaluation

If the first operand is truthy, Python does not need to evaluate the remaining operands.

Example:

```python
result = True or print("This will not execute")

print(result)
```

**Output:**

```text
True
```

The `print()` call is skipped.

### Important Technical Point

Python's `or` operator can return an operand rather than a Boolean.

Example:

```python
result = 0 or 50

print(result)
```

**Output:**

```text
50
```

Zero is falsy, so Python evaluates and returns the second operand.

---

# 18. Associativity of Comparison Operators

Comparison operators include:

- `<`
- `<=`
- `>`
- `>=`
- `==`
- `!=`

These operators share one precedence level.

However, comparison operators have special chaining behavior in Python.

### Example 1: Chained Comparison

```python
number = 5

result = 1 < number < 10

print(result)
```

**Output:**

```text
True
```

Python checks both conditions:

```python
1 < number
number < 10
```

Both conditions must be true.

### Equivalent Logical Form

```python
result = 1 < number and number < 10
```

For these ordinary comparisons, both forms have the same result.

### Example 2: Range Validation

```python
marks = 85

result = 0 <= marks <= 100

print(result)
```

**Output:**

```text
True
```

### Example 3: Failed Comparison

```python
marks = 120

result = 0 <= marks <= 100

print(result)
```

**Output:**

```text
False
```

### Important Difference

A chained comparison is not exactly the same as simply grouping comparison operators left to right.

Python treats it as a chain of comparisons.

For example:

```python
1 < 5 < 10
```

means:

```python
1 < 5 and 5 < 10
```

The middle expression is evaluated only once.

### Example with a Function

```python
def get_number():
    print("Function executed")
    return 5

result = 1 < get_number() < 10

print(result)
```

**Output:**

```text
Function executed
True
```

`get_number()` is called only once.

---

# 19. Conditional Expression Associativity

A conditional expression allows Python to choose one value based on a condition.

### Syntax

```python
value_if_true if condition else value_if_false
```

Conditional expressions group from right to left when nested.

### Example 1: Basic Conditional Expression

```python
marks = 75

result = "PASS" if marks >= 40 else "FAIL"

print(result)
```

**Output:**

```text
PASS
```

### Example 2: Nested Conditional Expression

```python
condition1 = True
condition2 = False

result = (
    "A" if condition1
    else "B" if condition2
    else "C"
)

print(result)
```

**Output:**

```text
A
```

### Grouping

The nested expression is interpreted as:

```python
"A" if condition1 else ("B" if condition2 else "C")
```

### Example 3: Multiple Grade Conditions

```python
marks = 82

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print(grade)
```

**Output:**

```text
B
```

### Important Point

Nested conditional expressions can become difficult to read.

For long conditions, a normal `if-elif-else` statement is often clearer.

---

# 20. Associativity and Parentheses

Parentheses can explicitly control grouping.

Even when an operator has a default associativity, parentheses can change the calculation.

### Example 1: Subtraction

```python
result1 = 20 - 5 - 2

result2 = 20 - (5 - 2)

print(result1)
print(result2)
```

**Output:**

```text
13
17
```

### Example 2: Division

```python
result1 = 100 / 10 / 2

result2 = 100 / (10 / 2)

print(result1)
print(result2)
```

**Output:**

```text
5.0
20.0
```

### Example 3: Exponentiation

```python
result1 = 2 ** 3 ** 2

result2 = (2 ** 3) ** 2

print(result1)
print(result2)
```

**Output:**

```text
512
64
```

### Comparison Table

| Expression | Default Grouping or Explicit Grouping | Result |
|---|---|---:|
| `20 - 5 - 2` | `(20 - 5) - 2` | 13 |
| `20 - (5 - 2)` | Explicit right grouping | 17 |
| `100 / 10 / 2` | `(100 / 10) / 2` | 5.0 |
| `100 / (10 / 2)` | Explicit right grouping | 20.0 |
| `2 ** 3 ** 2` | `2 ** (3 ** 2)` | 512 |
| `(2 ** 3) ** 2` | Explicit left grouping | 64 |

### Best Practice

Use parentheses whenever you want to make your intended grouping clear.

---

# 21. Precedence and Associativity Together

Precedence and associativity are often used together when evaluating expressions.

Consider:

```python
result = 10 + 20 * 3 / 2
```

### Step 1: Identify the Operators

- Addition.
- Multiplication.
- Division.

### Step 2: Apply Precedence

Multiplication and division have higher precedence than addition.

### Step 3: Apply Associativity

Multiplication and division share the same precedence and group from left to right.

### Step 4: Evaluate

```text
10 + 20 * 3 / 2
10 + (20 * 3) / 2
10 + 60 / 2
10 + 30.0
40.0
```

**Output:**

```text
40.0
```

### Another Example

```python
result = 2 + 3 ** 2 ** 2 * 2

print(result)
```

**Output:**

```text
164
```

Evaluation:

```text
2 + 3 ** 2 ** 2 * 2
2 + 3 ** (2 ** 2) * 2
2 + 3 ** 4 * 2
2 + 81 * 2
2 + 162
164
```

This example combines:

- Exponentiation precedence.
- Right-to-left exponentiation grouping.
- Multiplication precedence.
- Addition precedence.

---

# 22. Complete Associativity Reference Table

The following table summarizes important grouping behavior.

| Operator or Expression | Grouping Behavior |
|---|---|
| `a + b + c` | Left to right |
| `a - b - c` | Left to right |
| `a * b * c` | Left to right |
| `a / b / c` | Left to right |
| `a // b // c` | Left to right |
| `a % b % c` | Left to right |
| `a / b * c` | Left to right |
| `a + b - c` | Left to right |
| `a << b << c` | Left to right |
| `a >> b >> c` | Left to right |
| `a & b & c` | Left to right |
| `a ^ b ^ c` | Left to right |
| `a \| b \| c` | Left to right |
| `a and b and c` | Left to right grouping, with short-circuit behavior |
| `a or b or c` | Left to right grouping, with short-circuit behavior |
| `a ** b ** c` | Right to left |
| `a if c1 else b if c2 else c` | Right-nested conditional expression |
| `a < b < c` | Special chained comparison behavior |

### Important Note

The table is a learning reference, not a replacement for Python's complete grammar.

Comparison chaining is not ordinary left-associative binary grouping.

Logical operators use short-circuit evaluation.

Conditional expressions have their own right-nested behavior.

---

# 23. Difference Between Associativity and Evaluation Order

Associativity describes expression grouping.

Evaluation order describes when the parts of an expression are evaluated.

These concepts are related but not identical.

### Example: Function Calls

```python
def first():
    print("First function")
    return 10

def second():
    print("Second function")
    return 20

result = first() - second()

print(result)
```

**Output:**

```text
First function
Second function
-10
```

Python evaluates the function call operands from left to right in this expression.

The subtraction groups as:

```python
first() - second()
```

However, associativity itself is not a general rule for evaluating every side effect.

### Example: Logical Short-Circuiting

```python
result = False and print("Hello")

print(result)
```

**Output:**

```text
False
```

The second operand is not evaluated because the result is already known.

### Important Lesson

Do not confuse:

- Operator grouping.
- Operand evaluation order.
- Short-circuit behavior.

All three can affect the behavior of a Python expression.

---

# 24. Common Real-World Applications

Operator associativity is useful in many practical programs.

## 24.1 Financial Calculations

```python
balance = 10000

balance = balance - 1000 - 500

print(balance)
```

Output:

```text
8500
```

Each subtraction is applied from left to right.

## 24.2 Calculating Total Cost

```python
cost = 100 * 2 / 5

print(cost)
```

The expression is evaluated left to right for multiplication and division.

Output:

```text
40.0
```

## 24.3 Calculating Exponential Growth

```python
result = 2 ** 3 ** 2

print(result)
```

Output:

```text
512
```

Exponentiation grouping matters.

## 24.4 Student Eligibility

```python
marks = 75
attendance = 80
has_documents = True

eligible = (
    marks >= 40
    and attendance >= 75
    and has_documents
)

print(eligible)
```

Output:

```text
True
```

## 24.5 Validating a Number Range

```python
number = 50

valid = 10 <= number <= 100

print(valid)
```

Output:

```text
True
```

## 24.6 Grade Assignment

```python
marks = 82

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C"
)

print(grade)
```

Output:

```text
B
```

---

# 25. Twelve Examples Explained

The Python file `03_operator_associativity.py` contains twelve examples.

Each example demonstrates a particular grouping rule or special expression behavior.

## Example 1: Subtraction Left to Right

```python
result = 20 - 5 - 2

print(result)
```

**Output:**

```text
13
```

**Explanation:**

Subtraction is left-associative.

Grouping:

```text
(20 - 5) - 2
15 - 2
13
```

**Concept:** Left-to-right arithmetic grouping.

## Example 2: Division Left to Right

```python
result = 100 / 10 / 2

print(result)
```

**Output:**

```text
5.0
```

**Explanation:**

Division groups from left to right.

```text
(100 / 10) / 2
10.0 / 2
5.0
```

**Concept:** Division associativity.

## Example 3: Multiplication and Division

```python
result = 100 / 10 * 2

print(result)
```

**Output:**

```text
20.0
```

**Explanation:**

Multiplication and division share precedence.

They group from left to right.

**Concept:** Equal-precedence arithmetic operators.

## Example 4: Addition and Subtraction

```python
result = 20 + 5 - 3 + 2

print(result)
```

**Output:**

```text
24
```

**Explanation:**

The operations are grouped from the left.

```text
(((20 + 5) - 3) + 2)
24
```

**Concept:** Addition and subtraction grouping.

## Example 5: Exponentiation Right to Left

```python
result = 2 ** 3 ** 2

print(result)
```

**Output:**

```text
512
```

**Explanation:**

```text
2 ** (3 ** 2)
2 ** 9
512
```

**Concept:** Right-associative exponentiation.

## Example 6: Exponentiation with Parentheses

```python
result1 = (2 ** 3) ** 2

result2 = 2 ** (3 ** 2)

print(result1)
print(result2)
```

**Output:**

```text
64
512
```

**Explanation:**

Parentheses explicitly control the grouping.

**Concept:** Grouping and exponentiation.

## Example 7: Shift Operators Left to Right

```python
result = 64 >> 1 >> 1

print(result)
```

**Output:**

```text
16
```

**Explanation:**

```text
(64 >> 1) >> 1
32 >> 1
16
```

**Concept:** Shift associativity.

## Example 8: Bitwise AND Left to Right

```python
result = 15 & 7 & 3

print(result)
```

**Output:**

```text
3
```

**Explanation:**

```text
(15 & 7) & 3
7 & 3
3
```

**Concept:** Bitwise AND grouping.

## Example 9: Logical AND Associativity

```python
result = True and False and True

print(result)
```

**Output:**

```text
False
```

**Explanation:**

The left-to-right expression reaches a falsy value.

The result remains false.

**Concept:** Logical AND and short-circuit behavior.

## Example 10: Logical OR Associativity

```python
result = False or False or True

print(result)
```

**Output:**

```text
True
```

**Explanation:**

The final operand is truthy.

Therefore, the result is truthy.

**Concept:** Logical OR and short-circuit behavior.

## Example 11: Chained Comparison

```python
number = 5

result = 1 < number < 10

print(result)
```

**Output:**

```text
True
```

**Explanation:**

The expression checks both relationships:

```text
1 < 5
5 < 10
```

Both are true.

**Concept:** Python chained comparisons.

## Example 12: Nested Conditional Expressions

```python
condition1 = True

condition2 = False

result = (
    "A" if condition1
    else "B" if condition2
    else "C"
)

print(result)
```

**Output:**

```text
A
```

**Explanation:**

The expression is grouped as:

```python
"A" if condition1 else ("B" if condition2 else "C")
```

The first condition is true, so `"A"` is selected.

**Concept:** Right-nested conditional expressions.

---

# 26. Twelve Solved Problems

The Python file contains twelve interactive solved problems.

Every problem demonstrates a practical use of operator grouping or associativity.

## Problem 1: Subtraction Associativity

**Problem Statement:**

Take three numbers and evaluate the expression `a - b - c`.

### Logic

1. Read three numbers.
2. Subtract the second from the first.
3. Subtract the third from the result.
4. Display the final value.

### Code

```python
a = 20
b = 5
c = 2

result = a - b - c

print(result)
```

**Output:**

```text
13
```

### Dry Run

```text
20 - 5 - 2
(20 - 5) - 2
15 - 2
13
```

**Concept:** Subtraction groups from left to right.

---

## Problem 2: Division Associativity

**Problem Statement:**

Take a numerator and two divisors. Evaluate division from left to right.

### Code

```python
a = 120
b = 10
c = 3

result = a / b / c

print(result)
```

**Output:**

```text
4.0
```

### Dry Run

```text
120 / 10 / 3
(120 / 10) / 3
12.0 / 3
4.0
```

### Important Point

Both divisors must be non-zero.

**Concept:** Division associativity.

---

## Problem 3: Multiplication and Division Associativity

**Problem Statement:**

Take three numbers and evaluate an expression containing division followed by multiplication.

### Code

```python
a = 100
b = 10
c = 2

result = a / b * c

print(result)
```

**Output:**

```text
20.0
```

### Dry Run

```text
100 / 10 * 2
(100 / 10) * 2
10.0 * 2
20.0
```

**Concept:** Equal-precedence arithmetic operators.

---

## Problem 4: Addition and Subtraction Associativity

**Problem Statement:**

Take four numbers and evaluate an expression containing addition and subtraction.

### Code

```python
a = 20
b = 5
c = 3
d = 2

result = a + b - c + d

print(result)
```

**Output:**

```text
24
```

### Dry Run

```text
20 + 5 - 3 + 2
((20 + 5) - 3) + 2
25 - 3 + 2
22 + 2
24
```

**Concept:** Left-to-right grouping for addition and subtraction.

---

## Problem 5: Exponentiation Associativity

**Problem Statement:**

Take a base and two exponent values. Evaluate chained exponentiation.

### Code

```python
base = 2

first_exponent = 3

second_exponent = 2

result = base ** first_exponent ** second_exponent

print(result)
```

**Output:**

```text
512
```

### Dry Run

```text
2 ** 3 ** 2
2 ** (3 ** 2)
2 ** 9
512
```

**Concept:** Right-to-left exponentiation.

---

## Problem 6: Compare Exponentiation Groupings

**Problem Statement:**

Calculate two expressions using different parentheses and compare their results.

### Code

```python
result1 = (2 ** 3) ** 2

result2 = 2 ** (3 ** 2)

print(result1)
print(result2)
```

**Output:**

```text
64
512
```

### Dry Run

First expression:

```text
(2 ** 3) ** 2
8 ** 2
64
```

Second expression:

```text
2 ** (3 ** 2)
2 ** 9
512
```

**Concept:** Parentheses control grouping.

---

## Problem 7: Shift Associativity

**Problem Statement:**

Take a non-negative integer and perform two right shifts.

### Code

```python
number = 64

first_shift = 1

second_shift = 1

result = number >> first_shift >> second_shift

print(result)
```

**Output:**

```text
16
```

### Dry Run

```text
64 >> 1 >> 1
(64 >> 1) >> 1
32 >> 1
16
```

**Concept:** Left-to-right grouping of shift operators.

---

## Problem 8: Bitwise AND Associativity

**Problem Statement:**

Take three integers and perform bitwise AND.

### Code

```python
first = 15

second = 7

third = 3

result = first & second & third

print(result)
```

**Output:**

```text
3
```

### Dry Run

Binary values:

```text
15 = 1111
 7 = 0111
 3 = 0011
```

First operation:

```text
1111
0111
----
0111
```

Second operation:

```text
0111
0011
----
0011
```

Final result:

```text
3
```

**Concept:** Bitwise AND grouping.

---

## Problem 9: Logical AND Associativity

**Problem Statement:**

Check whether a student passes three subjects, requiring at least 40 marks in every subject.

### Code

```python
first_marks = 75

second_marks = 60

third_marks = 80

result = (
    first_marks >= 40
    and second_marks >= 40
    and third_marks >= 40
)

print(result)
```

**Output:**

```text
True
```

### Dry Run

```text
75 >= 40
True

60 >= 40
True

80 >= 40
True
```

Combined:

```text
True and True and True
True
```

**Concept:** Logical AND.

---

## Problem 10: Logical OR Associativity

**Problem Statement:**

Check whether at least one contact method is available.

### Code

```python
has_email = False

has_phone = False

has_contact_form = True

result = has_email or has_phone or has_contact_form

print(result)
```

**Output:**

```text
True
```

### Dry Run

```text
False or False or True
(False or False) or True
False or True
True
```

**Concept:** Logical OR.

---

## Problem 11: Chained Comparison

**Problem Statement:**

Check whether a number belongs to an inclusive range.

### Code

```python
start = 10

number = 50

stop = 100

result = start <= number <= stop

print(result)
```

**Output:**

```text
True
```

### Dry Run

```text
10 <= 50
True

50 <= 100
True

Final result = True
```

### Invalid Example

```python
start = 10
number = 120
stop = 100

print(start <= number <= stop)
```

Output:

```text
False
```

**Concept:** Chained comparisons.

---

## Problem 12: Nested Conditional Expression

**Problem Statement:**

Take student marks and assign a grade using nested conditional expressions.

### Conditions

| Marks | Grade |
|---|---|
| 90–100 | A |
| 75–89.99 | B |
| 60–74.99 | C |
| 40–59.99 | D |
| 0–39.99 | F |

### Code

```python
marks = 82

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print(grade)
```

**Output:**

```text
B
```

### Dry Run

```text
marks >= 90
82 >= 90
False
```

Check the next condition:

```text
marks >= 75
82 >= 75
True
```

Therefore:

```text
Grade = B
```

### Concept

Right-nested conditional expressions.

---

# 27. Ten Unsolved Practice Questions

Try to solve these questions without looking at the examples.

| No. | Practice Question | Hint |
|---|---|---|
| 1 | Evaluate `30 - 10 - 5`. | Subtraction is left-associative |
| 2 | Evaluate `120 / 10 / 3`. | Division is left-associative |
| 3 | Evaluate `80 / 10 * 4`. | Multiplication and division share precedence |
| 4 | Evaluate `50 + 10 - 5 + 2`. | Addition and subtraction group left to right |
| 5 | Evaluate `3 ** 2 ** 2`. | Exponentiation is right-associative |
| 6 | Compare `(3 ** 2) ** 2` and `3 ** (2 ** 2)`. | Use parentheses |
| 7 | Evaluate `128 >> 1 >> 2`. | Shift operations group left to right |
| 8 | Evaluate `15 & 7 & 3`. | Bitwise AND is left-associative |
| 9 | Check whether a number is between 20 and 80. | Use chained comparison |
| 10 | Create a nested conditional expression for grades. | Use conditional expressions |

## Additional Challenge Problems

### Challenge 1: Subtraction with Parentheses

Calculate the result of:

```python
100 - 20 - 10
100 - (20 - 10)
```

Explain why the results are different.

### Challenge 2: Division Grouping

Calculate:

```python
120 / 10 / 2
120 / (10 / 2)
```

### Challenge 3: Exponentiation

Compare:

```python
3 ** 2 ** 2
(3 ** 2) ** 2
3 ** (2 ** 2)
```

### Challenge 4: Logical AND

Write a program that checks whether a student satisfies four subject requirements.

### Challenge 5: Logical OR

Check whether at least one of five user accounts is active.

### Challenge 6: Shift Operations

Evaluate three consecutive right shifts.

### Challenge 7: Bitwise AND

Use bitwise AND with three different masks.

### Challenge 8: Chained Comparison

Check whether a student's marks belong to a valid range.

### Challenge 9: Nested Conditional Expression

Write a nested conditional expression to classify temperatures as hot, warm, or cold.

### Challenge 10: Function Call and Grouping

Create three functions that return numbers and use them in a subtraction expression. Observe the function evaluation order.

---

# 28. Common Mistakes and Their Solutions

## Mistake 1: Assuming Subtraction Is Right-Associative

Incorrect assumption:

```python
20 - 5 - 2
```

Some beginners may group this as:

```text
20 - (5 - 2)
17
```

Actual Python grouping:

```text
(20 - 5) - 2
13
```

## Mistake 2: Assuming Division Groups from Right to Left

Incorrect assumption:

```python
100 / 10 / 2
```

Actual grouping:

```text
(100 / 10) / 2
5.0
```

## Mistake 3: Assuming Exponentiation Is Left-Associative

Incorrect assumption:

```python
2 ** 3 ** 2
```

Actual grouping:

```text
2 ** (3 ** 2)
512
```

## Mistake 4: Ignoring Parentheses

```python
result = 100 / (10 / 2)
```

Output:

```text
20.0
```

Parentheses change the grouping.

## Mistake 5: Assuming All Operators Are Left-Associative

Most common binary operators group left to right, but exponentiation is right-associative.

Comparison expressions and conditional expressions also have special grouping behavior.

## Mistake 6: Confusing Precedence and Associativity

Precedence determines priority.

Associativity determines grouping when precedence is equal.

## Mistake 7: Confusing Chained Comparisons with Ordinary Grouping

```python
1 < 5 < 10
```

This is a chained comparison.

It is not evaluated as:

```python
(1 < 5) < 10
```

The chained comparison checks both relationships.

## Mistake 8: Ignoring Short-Circuit Evaluation

```python
False and some_function()
```

The function may not be executed because the result is already known.

## Mistake 9: Making Nested Conditional Expressions Too Long

Long nested conditional expressions can become difficult to understand.

Prefer `if-elif-else` statements when the conditions become complicated.

## Mistake 10: Forgetting That Grouping and Evaluation Order Are Different

Associativity describes grouping. Python also has operand evaluation rules and short-circuit behavior.

Do not assume that every grouped operand is evaluated unconditionally.

---

# 29. Best Practices

1. Understand operator precedence before studying associativity.
2. Remember that most ordinary binary operators group left to right.
3. Remember that exponentiation groups right to left.
4. Understand the special behavior of unary minus and exponentiation.
5. Use parentheses to change grouping explicitly.
6. Understand that comparisons can be chained.
7. Remember that logical operators use short-circuit evaluation.
8. Understand that `and` and `or` can return operands rather than Booleans.
9. Avoid deeply nested conditional expressions.
10. Break complex expressions into intermediate variables.
11. Check division denominators.
12. Practise evaluating expressions manually.
13. Compare expressions with different parentheses.
14. Do not assume all operators have identical associativity.
15. Distinguish grouping from operand evaluation order.
16. Test expressions with several different inputs.
17. Use meaningful variable names.
18. Use parentheses when an expression is difficult to read.
19. Review the Python precedence table when needed.
20. Practise associativity using real programming problems.

---

# 30. Debugging and Troubleshooting

If an expression gives an unexpected result, follow these steps.

## Step 1: Identify the Operators

Write down each operator present in the expression.

## Step 2: Check Their Precedence

Determine whether the operators share the same precedence.

## Step 3: Check Associativity

Identify whether grouping should be left-to-right, right-to-left, or follow special comparison or conditional rules.

## Step 4: Add Parentheses

Make the intended grouping explicit.

## Step 5: Evaluate One Operation at a Time

Example:

```python
result = 20 - 5 - 2
```

Rewrite conceptually:

```python
first = 20 - 5

result = first - 2
```

## Step 6: Check Intermediate Values

```python
print(first)
print(result)
```

## Step 7: Check Data Types

```python
print(type(result))
```

## Step 8: Check Short-Circuit Conditions

For `and` and `or`, confirm whether Python skips an operand.

## Step 9: Check Function Calls

If an expression contains functions, print messages inside them to understand their execution order.

## Step 10: Compare with a Parenthesized Version

Test the expression using explicit parentheses.

This makes grouping easier to understand.

---

# 31. Practice Test

Solve these questions without running the code first.

### Question 1

```python
print(20 - 5 - 2)
```

What is the output?

### Question 2

```python
print(100 / 10 / 2)
```

What is the output?

### Question 3

```python
print(100 / 10 * 2)
```

What is the output?

### Question 4

```python
print(20 + 5 - 3 + 2)
```

What is the output?

### Question 5

```python
print(2 ** 3 ** 2)
```

What is the output?

### Question 6

```python
print((2 ** 3) ** 2)
```

What is the output?

### Question 7

```python
print(64 >> 1 >> 1)
```

What is the output?

### Question 8

```python
print(15 & 7 & 3)
```

What is the output?

### Question 9

```python
print(True and False and True)
```

What is the output?

### Question 10

```python
print(False or False or True)
```

What is the output?

### Question 11

```python
number = 5

print(1 < number < 10)
```

What is the output?

### Question 12

```python
condition1 = False
condition2 = True

result = (
    "A" if condition1
    else "B" if condition2
    else "C"
)

print(result)
```

What is the output?

## Answer Key

| Question | Answer | Explanation |
|---|---|---|
| 1 | `13` | Subtraction groups left to right |
| 2 | `5.0` | Division groups left to right |
| 3 | `20.0` | Division then multiplication |
| 4 | `24` | Addition and subtraction group left to right |
| 5 | `512` | Exponentiation groups right to left |
| 6 | `64` | Parentheses group the left exponentiation |
| 7 | `16` | Shifts group left to right |
| 8 | `3` | Bitwise AND groups left to right |
| 9 | `False` | One operand is false |
| 10 | `True` | The final operand is true |
| 11 | `True` | Both comparison conditions are satisfied |
| 12 | `B` | First condition fails, second succeeds |

---

# 32. Viva Questions and Answers

Prepare these questions for college practical examinations and technical interviews.

## A. Basic Questions

**Q1. What is operator associativity in Python?**

Operator associativity determines how operators with the same precedence are grouped.

**Q2. What are the two commonly discussed associativity directions?**

Left to right and right to left.

**Q3. What is left-to-right associativity?**

It means that same-precedence operators are grouped from the left side.

**Q4. What is right-to-left associativity?**

It means that operators are grouped from the right side.

**Q5. What is the difference between precedence and associativity?**

Precedence determines operator priority; associativity determines grouping for equal-precedence operators.

**Q6. Are all Python operators left-associative?**

No.

**Q7. Which common arithmetic operator is right-associative?**

Exponentiation.

**Q8. Why is associativity important?**

It determines the grouping of expressions and helps Python produce predictable results.

**Q9. Can parentheses change associativity-based grouping?**

Yes. Parentheses explicitly determine grouping.

**Q10. What is expression grouping?**

It is the way the parts of an expression are organized for evaluation.

## B. Arithmetic Questions

**Q11. Is subtraction left-associative?**

Yes.

**Q12. Is division left-associative?**

Yes.

**Q13. Is multiplication left-associative?**

Yes.

**Q14. Do addition and subtraction have equal precedence?**

Yes.

**Q15. Do multiplication and division have equal precedence?**

Yes.

**Q16. What is the output of `20 - 5 - 2`?**

`13`.

**Q17. What is the output of `100 / 10 / 2`?**

`5.0`.

**Q18. What is the output of `100 / 10 * 2`?**

`20.0`.

**Q19. Which direction does exponentiation associate?**

Right to left.

**Q20. What is the output of `2 ** 3 ** 2`?**

`512`.

## C. Exponentiation Questions

**Q21. What is the result of `(2 ** 3) ** 2`?**

`64`.

**Q22. What is the result of `2 ** (3 ** 2)`?**

`512`.

**Q23. Why does `2 ** 3 ** 2` produce 512?**

Because exponentiation groups from right to left.

**Q24. What is the result of `-2 ** 2`?**

`-4`.

**Q25. What is the result of `(-2) ** 2`?**

`4`.

## D. Bitwise and Logical Questions

**Q26. Are shift operators left-associative?**

Yes, they group left to right.

**Q27. Is bitwise AND left-associative?**

Yes.

**Q28. Is bitwise OR left-associative?**

Yes.

**Q29. Is logical AND left-associative in its expression grammar?**

Yes, logical AND expressions group from left to right.

**Q30. Is logical OR left-associative in its expression grammar?**

Yes, logical OR expressions group from left to right.

**Q31. What is short-circuit evaluation?**

It means Python skips evaluating an operand when the result is already determined.

**Q32. Does logical AND always return a Boolean?**

No. It can return one of its operands.

**Q33. Does logical OR always return a Boolean?**

No. It can return one of its operands.

**Q34. Which logical operator has higher precedence: `and` or `or`?**

`and`.

**Q35. Which logical operator has higher precedence: `not` or `and`?**

`not`.

## E. Comparison and Conditional Questions

**Q36. What is a chained comparison?**

It is a comparison expression containing multiple comparisons, such as `0 <= marks <= 100`.

**Q37. Is chained comparison ordinary left-to-right binary grouping?**

No. Python evaluates it using special comparison chaining behavior.

**Q38. Is the middle expression in a chained comparison evaluated more than once?**

No. It is evaluated only once.

**Q39. What is a conditional expression?**

An expression that selects one of two values based on a condition.

**Q40. How do nested conditional expressions group?**

They group to the right.

## F. Practical and Advanced Questions

**Q41. Can parentheses change the result of subtraction?**

Yes.

**Q42. Can parentheses change the result of division?**

Yes.

**Q43. What happens if you divide by zero?**

Python raises `ZeroDivisionError`.

**Q44. What is the difference between associativity and evaluation order?**

Associativity determines grouping, while evaluation order determines when expression components are evaluated.

**Q45. Are function operands always evaluated according to associativity?**

No. Python has separate rules for operand evaluation order.

**Q46. Why do logical operators skip some operands?**

Because of short-circuit evaluation.

**Q47. What is the most important right-associative arithmetic operator in Python?**

Exponentiation.

**Q48. Why should complex expressions use parentheses?**

They improve readability and make the intended grouping explicit.

**Q49. Is the expression `1 < 5 < 10` a chained comparison?**

Yes.

**Q50. Why is operator associativity important in DSA?**

It ensures that mathematical, logical, and bitwise expressions are grouped as intended inside algorithms.

---

# 33. Connection with Data Structures and Algorithms (DSA)

Associativity is important in DSA because algorithms frequently use expressions containing multiple operators.

Understanding grouping helps prevent incorrect calculations and conditions.

## 33.1 Mathematical Calculations

```python
result = 100 - 20 - 10

print(result)
```

Output:

```text
70
```

The subtraction operations group from left to right.

## 33.2 Exponentiation in Algorithms

```python
result = 2 ** 3 ** 2

print(result)
```

Output:

```text
512
```

Right-associative exponentiation matters in mathematical expressions.

## 33.3 Binary Search

```python
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

middle = (left + right) // 2

print(numbers[middle])
```

Output:

```text
30
```

The grouping in:

```python
(left + right) // 2
```

ensures that the sum is calculated before division.

## 33.4 Two-Pointer Algorithm

```python
numbers = [1, 2, 4, 6, 8]

left = 0
right = len(numbers) - 1

target = 10

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print("Pair found")
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1
```

The algorithm uses several expressions for comparisons and calculations.

## 33.5 Bit Manipulation

```python
number = 13
mask = 5

result = (number & mask) == mask

print(result)
```

Output:

```text
True
```

Parentheses make the intended grouping explicit.

## 33.6 Logical Conditions in Algorithms

```python
age = 22
has_id = True
is_registered = True

eligible = (
    age >= 18
    and has_id
    and is_registered
)

print(eligible)
```

Output:

```text
True
```

Multiple conditions are combined using logical AND.

### DSA Topics to Practise

1. Binary Search.
2. Two-Pointer Technique.
3. Sliding Window.
4. Mathematical Problems.
5. Bit Manipulation.
6. Sorting.
7. Searching.
8. Array Conditions.
9. Expression Evaluation.
10. Dynamic Programming.

---

# 34. Interview Preparation

Practise these questions to prepare for programming interviews.

### Conceptual Questions

1. Explain operator associativity.
2. What is the difference between associativity and precedence?
3. Why does Python evaluate subtraction from left to right?
4. Why does exponentiation group from right to left?
5. How do parentheses affect associativity?
6. What is the special behavior of chained comparisons?
7. What is short-circuit evaluation?
8. How do nested conditional expressions group?
9. What is the difference between grouping and evaluation order?
10. Why are parentheses useful in algorithms?

### Coding Questions

1. Evaluate a subtraction expression.
2. Evaluate a division expression.
3. Compare two exponentiation expressions.
4. Demonstrate multiplication and division grouping.
5. Write an expression using chained comparison.
6. Create a nested conditional expression for grades.
7. Evaluate multiple logical AND conditions.
8. Demonstrate logical OR short-circuiting.
9. Use bitwise AND in a condition.
10. Write a function expression that demonstrates left-to-right function evaluation.

### Interview Practice Checklist

- [ ] Explain left-to-right associativity.
- [ ] Explain right-to-left associativity.
- [ ] Explain exponentiation grouping.
- [ ] Explain unary minus and power.
- [ ] Explain logical short-circuiting.
- [ ] Explain chained comparisons.
- [ ] Explain nested conditional expressions.
- [ ] Solve basic expression problems.
- [ ] Evaluate expressions without running code.
- [ ] Explain the importance of parentheses.

---

# 35. Mini Project: Associativity Comparison Tool

Create a small program that compares expressions with different grouping.

### Requirements

1. Evaluate subtraction with default grouping.
2. Evaluate subtraction with parentheses.
3. Evaluate division with default grouping.
4. Evaluate division with parentheses.
5. Evaluate exponentiation with default grouping.
6. Evaluate exponentiation with both grouping choices.
7. Display all results.
8. Explain the differences.

### Example Code

```python
print("SUBTRACTION")

a = 20 - 5 - 2

b = 20 - (5 - 2)

print("Default grouping:", a)
print("Parentheses grouping:", b)


print("\nDIVISION")

c = 100 / 10 / 2

d = 100 / (10 / 2)

print("Default grouping:", c)
print("Parentheses grouping:", d)


print("\nEXPONENTIATION")

e = 2 ** 3 ** 2

f = (2 ** 3) ** 2

g = 2 ** (3 ** 2)

print("Default grouping:", e)
print("Left grouping:", f)
print("Right grouping:", g)
```

### Output

```text
SUBTRACTION
Default grouping: 13
Parentheses grouping: 17

DIVISION
Default grouping: 5.0
Parentheses grouping: 20.0

EXPONENTIATION
Default grouping: 512
Left grouping: 64
Right grouping: 512
```

### Extension Tasks

1. Add multiplication and division comparisons.
2. Add logical AND expressions.
3. Add logical OR expressions.
4. Add bitwise operations.
5. Add chained comparisons.
6. Add nested conditional expressions.
7. Allow user input.
8. Display step-by-step grouping.
9. Add a menu to select expressions.
10. Add your own practice expressions.

---

# 36. Glossary

| Term | Meaning |
|---|---|
| Associativity | Rule determining how equal-precedence operators are grouped |
| Left-to-Right | Grouping starting from the left side |
| Right-to-Left | Grouping starting from the right side |
| Precedence | Priority of operators |
| Expression | Code that produces a value |
| Operator | Symbol or keyword performing an operation |
| Operand | Value on which an operator operates |
| Grouping | Arrangement of operations in an expression |
| Parentheses | Symbols used to explicitly group expressions |
| Exponentiation | Raising a number to a power |
| Unary Operator | Operator working on one operand |
| Binary Operator | Operator working on two operands |
| Comparison | Checking relationships between values |
| Chained Comparison | Multiple connected comparisons |
| Short-Circuit Evaluation | Skipping unnecessary operand evaluation |
| Logical AND | Logical operation requiring both operands to be truthy |
| Logical OR | Logical operation requiring at least one operand to be truthy |
| Conditional Expression | Selects a value based on a condition |
| Bitwise AND | Bit-level AND operation |
| Bitwise OR | Bit-level OR operation |
| Bitwise XOR | Bit-level exclusive OR operation |
| Shift Operator | Moves bits left or right |
| Evaluation Order | Order in which expression operands are evaluated |
| DSA | Data Structures and Algorithms |
| Nested Expression | Expression containing another expression |

---

# 37. Quick Revision Notes

### Left-to-Right Subtraction

```python
20 - 5 - 2
```

Grouping:

```python
(20 - 5) - 2
```

### Left-to-Right Division

```python
100 / 10 / 2
```

Grouping:

```python
(100 / 10) / 2
```

### Multiplication and Division

```python
100 / 10 * 2
```

Grouping:

```python
(100 / 10) * 2
```

### Addition and Subtraction

```python
20 + 5 - 3 + 2
```

Grouping:

```python
((20 + 5) - 3) + 2
```

### Right-to-Left Exponentiation

```python
2 ** 3 ** 2
```

Grouping:

```python
2 ** (3 ** 2)
```

### Parentheses with Exponentiation

```python
(2 ** 3) ** 2
```

### Shift Operators

```python
64 >> 1 >> 1
```

Grouping:

```python
(64 >> 1) >> 1
```

### Bitwise AND

```python
15 & 7 & 3
```

Grouping:

```python
(15 & 7) & 3
```

### Logical AND

```python
True and False and True
```

### Logical OR

```python
False or False or True
```

### Chained Comparison

```python
1 < number < 10
```

### Nested Conditional Expression

```python
"A" if condition1 else "B" if condition2 else "C"
```

### Most Important Rules

1. Associativity determines grouping for equal-precedence operators.
2. Most ordinary binary operators group from left to right.
3. Exponentiation groups from right to left.
4. Parentheses can change grouping.
5. Addition and subtraction share precedence.
6. Multiplication and division share precedence.
7. Shift operators group from left to right.
8. Bitwise binary operators of the same level group from left to right.
9. Logical AND and OR group from left to right, with short-circuit evaluation.
10. Comparisons support special chaining behavior.
11. Conditional expressions can be nested right to left.
12. Grouping and operand evaluation order are not the same thing.

---

# 38. Learning Checklist

Complete the following checklist before moving to the next topic.

## Basic Concepts

- [ ] I understand operator associativity.
- [ ] I understand left-to-right associativity.
- [ ] I understand right-to-left associativity.
- [ ] I understand the difference between precedence and associativity.
- [ ] I can identify equal-precedence operators.

## Arithmetic Associativity

- [ ] I understand subtraction grouping.
- [ ] I understand addition grouping.
- [ ] I understand division grouping.
- [ ] I understand multiplication and division grouping.
- [ ] I understand exponentiation grouping.
- [ ] I understand unary minus and exponentiation.
- [ ] I can use parentheses to change grouping.

## Bitwise and Logical Associativity

- [ ] I understand shift operator associativity.
- [ ] I understand bitwise AND grouping.
- [ ] I understand bitwise XOR grouping.
- [ ] I understand bitwise OR grouping.
- [ ] I understand logical AND grouping.
- [ ] I understand logical OR grouping.
- [ ] I understand short-circuit evaluation.

## Special Expression Behavior

- [ ] I understand chained comparisons.
- [ ] I understand nested conditional expressions.
- [ ] I understand grouping versus evaluation order.
- [ ] I can manually evaluate complicated expressions.

## Programming Practice

- [ ] I have run all 12 examples.
- [ ] I have completed all 12 solved problems.
- [ ] I have attempted all 10 unsolved questions.
- [ ] I have completed the practice test.
- [ ] I have built the Associativity Comparison Tool.
- [ ] I can explain each expression in my own words.

## DSA Preparation

- [ ] I understand associativity in mathematical calculations.
- [ ] I understand expressions used in binary search.
- [ ] I understand expressions used in two-pointer algorithms.
- [ ] I understand bitwise expression grouping.
- [ ] I can write readable algorithm conditions.

---

# 39. How to Run the Python Program

The folder contains:

```text
03-operator-associativity/
│
├── README.md
│
└── 03_operator_associativity.py
```

### Step 1: Open PowerShell or VS Code Terminal

Navigate to the folder:

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\08-Expressions\03-operator-associativity"
```

### Step 2: Run the Python File

```powershell
python 03_operator_associativity.py
```

### Step 3: Select a Menu Option

The program provides:

```text
=============================================================
              PYTHON OPERATOR ASSOCIATIVITY
=============================================================

1. View 12 Associativity Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

### Step 4: Follow the Learning Order

Recommended sequence:

1. Select option `1` to understand all examples.
2. Select option `2` to solve the interactive problems.
3. Select option `3` to attempt the unsolved questions.
4. Select option `4` to check your progress.

### Step 5: Practise Manually

Before running each example:

1. Identify its operators.
2. Check their precedence.
3. Determine their associativity.
4. Add parentheses to show grouping.
5. Calculate the result.
6. Run the Python program.
7. Compare your answer.

---

# 40. Folder Structure

The completed folder should have this structure:

```text
08-Expressions/
│
├── README.md
│
├── 01-expressions/
│   ├── README.md
│   └── 01_expressions.py
│
├── 02-operator-precedence/
│   ├── README.md
│   └── 02_operator_precedence.py
│
├── 03-operator-associativity/
│   ├── README.md
│   └── 03_operator_associativity.py
│
├── 04-parentheses-and-grouping/
│
└── 05-conditional-expressions/
```

### File Responsibilities

| File | Purpose |
|---|---|
| `README.md` | Complete theoretical notes and study material |
| `03_operator_associativity.py` | Executable examples and interactive problems |

Keep the Python program and documentation inside the same folder.

---

# 41. Navigation

### Previous Topic

[02 - Operator Precedence](../02-operator-precedence/README.md)

### Current Topic

**03 - Operator Associativity**

### Next Topic

[04 - Parentheses and Grouping](../04-parentheses-and-grouping/README.md)

### Expressions Main Folder

[08 - Expressions](../README.md)

### Parent Folder

[05 - Operators and Expressions](../../README.md)

---

# 42. Final Summary

Operator associativity determines how operators with equal precedence are grouped in an expression.

In this topic, you studied:

1. Meaning of operator associativity.
2. Left-to-right grouping.
3. Right-to-left grouping.
4. Difference between precedence and associativity.
5. Subtraction associativity.
6. Division associativity.
7. Multiplication and division grouping.
8. Addition and subtraction grouping.
9. Exponentiation associativity.
10. Unary operators and exponentiation.
11. Shift operator grouping.
12. Bitwise operator grouping.
13. Logical AND and OR grouping.
14. Short-circuit evaluation.
15. Chained comparisons.
16. Nested conditional expressions.
17. Parentheses and explicit grouping.
18. Difference between grouping and evaluation order.

### Most Important Examples to Remember

**Left-to-right:**

```python
20 - 5 - 2
```

Output:

```text
13
```

**Right-to-left:**

```python
2 ** 3 ** 2
```

Output:

```text
512
```

**Parentheses change grouping:**

```python
(2 ** 3) ** 2
```

Output:

```text
64
```

**Chained comparison:**

```python
1 < 5 < 10
```

Output:

```text
True
```

**Final Advice:**

Do not just memorize the associativity table. Practise grouping expressions manually and understand why Python produces each result.

Complete all twelve examples, solve all twelve problems, attempt the ten unsolved questions, and revise the viva questions before moving to the next topic.

Strong understanding of precedence and associativity will make complex expressions and DSA algorithms much easier to write and debug.

Keep practising and keep improving your Python fundamentals.