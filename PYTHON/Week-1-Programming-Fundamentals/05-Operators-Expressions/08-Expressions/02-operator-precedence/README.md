# Python Operator Precedence

**Week:** 01 – Programming Fundamentals  
**Main Topic:** Operators and Expressions  
**Subtopic:** Operator Precedence  
**Folder:** `02-operator-precedence`  
**Python File:** `02_operator_precedence.py`  
**Level:** Beginner to Intermediate

---

# 1. Introduction to Operator Precedence

Operator precedence is one of the most important concepts in Python expressions.

When an expression contains multiple operators, Python needs rules to determine which operation should be performed first.

These rules are called **operator precedence**.

In simple words:

**Operator precedence determines the order in which operators are evaluated in an expression.**

### Example 1: Basic Expression

```python
result = 10 + 5 * 2

print(result)
```

**Output:**

```text
20
```

A beginner might expect the following calculation:

```text
10 + 5 = 15
15 * 2 = 30
```

But Python does not evaluate the expression this way.

Multiplication has higher precedence than addition.

Therefore:

```text
10 + 5 * 2
10 + 10
20
```

The correct answer is `20`.

### Example 2: Using Parentheses

Now consider:

```python
result = (10 + 5) * 2

print(result)
```

**Output:**

```text
30
```

This time, parentheses tell Python to evaluate `10 + 5` first.

```text
(10 + 5) * 2
15 * 2
30
```

### Why Is Operator Precedence Important?

Operator precedence helps Python evaluate complicated expressions consistently.

It is important in:

- Mathematical calculations.
- Financial calculations.
- Conditional statements.
- Logical expressions.
- Bitwise operations.
- Data validation.
- Programming algorithms.
- DSA problems.
- Scientific calculations.
- Complex expressions containing multiple operators.

Without understanding precedence, a program may produce an incorrect result even when every individual operator is correct.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Define operator precedence.
2. Understand why operator precedence is required.
3. Understand Python's operator precedence rules.
4. Read and understand the precedence table.
5. Understand parentheses and grouping.
6. Understand exponentiation precedence.
7. Understand unary operator precedence.
8. Understand multiplication, division, floor division, and modulus precedence.
9. Understand addition and subtraction precedence.
10. Understand shift operator precedence.
11. Understand bitwise AND, XOR, and OR precedence.
12. Understand comparison operator precedence.
13. Understand chained comparisons.
14. Understand `not`, `and`, and `or` precedence.
15. Understand conditional expression precedence.
16. Understand the relationship between precedence and associativity.
17. Evaluate complicated expressions step by step.
18. Use parentheses to make expressions readable.
19. Identify common precedence mistakes.
20. Apply precedence rules to practical programming problems.
21. Solve mathematical expressions.
22. Solve logical expressions.
23. Solve bitwise expressions.
24. Understand precedence in DSA conditions.
25. Complete all 12 solved problems and 10 unsolved questions.

---

# 3. Prerequisites

Before studying operator precedence, you should understand the following Python concepts.

| Concept | Why It Is Required |
|---|---|
| Variables | To store values used in expressions |
| Data Types | To understand integers, floats, strings, and Boolean values |
| Arithmetic Operators | To understand mathematical expression evaluation |
| Assignment Operators | To understand variable updates |
| Comparison Operators | To compare values |
| Logical Operators | To combine conditions |
| Bitwise Operators | To understand bitwise precedence |
| Membership Operators | To understand membership expressions |
| Identity Operators | To understand identity expressions |
| Expressions | To understand how Python produces results |

You have already covered these concepts in the previous folders.

Recommended revision:

- `01-Arithmetic-Operators`
- `02-Assignment-Operators`
- `03-Comparison-Operators`
- `04-Logical-Operators`
- `05-Bitwise-Operators`
- `06-Membership-Operators`
- `07-Identity-Operators`
- `01-expressions`

---

# 4. What Is Operator Precedence?

Operator precedence is the priority assigned to operators in an expression.

An operator with higher precedence is generally evaluated before an operator with lower precedence, subject to grouping and other language rules.

### Example

```python
a = 10
b = 5
c = 2

result = a + b * c

print(result)
```

**Output:**

```text
20
```

### Explanation

The expression is:

```text
a + b * c
```

Substitute the values:

```text
10 + 5 * 2
```

Multiplication has higher precedence than addition.

Therefore:

```text
10 + 10
```

Final result:

```text
20
```

### Another Example

```python
result = 100 - 20 / 5

print(result)
```

**Output:**

```text
96.0
```

Evaluation:

```text
100 - 20 / 5
100 - 4.0
96.0
```

Division is performed before subtraction.

### Important Point

Precedence determines operator priority. When operators have equal precedence, associativity or special rules determine how they are grouped or evaluated.

---

# 5. Why Is Operator Precedence Required?

Consider the expression:

```python
result = 10 + 5 * 2 - 4
```

There are three operations:

- Addition.
- Multiplication.
- Subtraction.

Without precedence rules, it would be unclear which operation should be performed first.

Python provides a consistent order.

### Correct Evaluation

```text
10 + 5 * 2 - 4
10 + 10 - 4
20 - 4
16
```

**Output:**

```text
16
```

### Another Expression

```python
result = 20 / 5 + 3 * 2

print(result)
```

**Output:**

```text
10.0
```

Evaluation:

```text
20 / 5 + 3 * 2
4.0 + 6
10.0
```

Both division and multiplication are performed before addition.

### Main Benefits of Precedence Rules

1. They make expression evaluation predictable.
2. They allow multiple operations in one expression.
3. They make mathematical calculations easier to write.
4. They prevent ambiguity in complex conditions.
5. They help programmers understand existing code.
6. They provide a consistent evaluation structure.

---

# 6. Complete Python Operator Precedence Table

This is the important reference table for Python operator precedence.

The table is arranged from **highest precedence to lowest precedence**.

| Priority | Operators or Expression Forms | Description |
|---|---|---|
| Highest | `(...)`, `[...]`, `{...}` | Grouping and collection displays |
|  | `x[index]`, `x[index:index]` | Subscription and slicing |
|  | `x(...)`, `x.attribute` | Function calls and attribute access |
|  | `await x` | Await expression |
|  | `**` | Exponentiation |
|  | `+x`, `-x`, `~x` | Unary plus, minus, and bitwise NOT |
|  | `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division, modulus |
|  | `+`, `-` | Addition and subtraction |
|  | `<<`, `>>` | Bitwise shifts |
|  | `&` | Bitwise AND |
|  | `^` | Bitwise XOR |
|  | `\|` | Bitwise OR |
|  | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership, and identity |
|  | `not x` | Boolean NOT |
|  | `and` | Boolean AND |
|  | `or` | Boolean OR |
|  | `x if condition else y` | Conditional expression |
|  | `lambda` | Lambda expression |
| Lowest | `:=` | Assignment expression |

### Important Notes

- Parentheses can explicitly group an expression.
- Function calls and indexing have very high binding priority.
- Exponentiation has higher precedence than unary minus on its left.
- Multiplication, division, floor division, and modulus share a precedence level.
- Addition and subtraction share a precedence level.
- Bitwise AND has higher precedence than bitwise XOR, which has higher precedence than bitwise OR.
- Comparison operators share a precedence level.
- `not` has lower precedence than comparisons.
- `and` has lower precedence than `not`.
- `or` has lower precedence than `and`.
- Conditional expressions have lower precedence than `or`.
- Assignment expressions have very low precedence.

### Scope of the Table

This table includes important expression forms as well as operators. Some entries, such as function calls and indexing, are expression constructions rather than operators in the usual mathematical sense.

The `await` form is relevant when working with asynchronous Python functions.

The `:=` operator is called the assignment expression operator, also known as the walrus operator.

---

# 7. Parentheses Have High Precedence

Parentheses are used to group parts of an expression.

The expression inside parentheses is evaluated as a grouped unit.

### Example 1

```python
result = 10 + 5 * 2

print(result)
```

**Output:**

```text
20
```

### Example 2

```python
result = (10 + 5) * 2

print(result)
```

**Output:**

```text
30
```

### Explanation

Without parentheses:

```text
10 + 5 * 2
10 + 10
20
```

With parentheses:

```text
(10 + 5) * 2
15 * 2
30
```

### Another Example

```python
a = 10
b = 20
c = 5

result = (a + b) / c

print(result)
```

**Output:**

```text
6.0
```

### Why Use Parentheses?

Parentheses are useful when:

- An expression has many operators.
- The intended grouping is not obvious.
- A mathematical formula must be represented accurately.
- Logical conditions contain multiple `and` and `or` operations.
- A bitwise expression is combined with comparisons.

### Best Practice

Even when Python's precedence rules make the result clear, use parentheses in complex conditions when they improve readability.

---

# 8. Exponentiation Precedence

Exponentiation uses the `**` operator.

It calculates a number raised to a power.

### Syntax

```python
base ** exponent
```

### Example

```python
result = 2 ** 3

print(result)
```

**Output:**

```text
8
```

### Exponentiation with Addition

```python
result = 2 + 3 ** 2

print(result)
```

**Output:**

```text
11
```

Evaluation:

```text
2 + 3 ** 2
2 + 9
11
```

Exponentiation has higher precedence than addition.

### Exponentiation with Multiplication

```python
result = 2 + 3 ** 2 * 2

print(result)
```

**Output:**

```text
20
```

Evaluation:

```text
2 + 3 ** 2 * 2
2 + 9 * 2
2 + 18
20
```

### Important Example: Multiple Powers

```python
result = 2 ** 3 ** 2

print(result)
```

**Output:**

```text
512
```

Exponentiation groups from right to left.

```text
2 ** 3 ** 2
2 ** (3 ** 2)
2 ** 9
512
```

### Important Rule

Exponentiation is right-associative.

This special behavior will be explored further in the operator associativity topic.

---

# 9. Unary Minus and Exponentiation

Unary minus is used to make a value negative.

Example:

```python
number = 10

print(-number)
```

**Output:**

```text
-10
```

A common precedence question involves unary minus and exponentiation.

### Example 1

```python
result = -2 ** 2

print(result)
```

**Output:**

```text
-4
```

Why?

Exponentiation has higher precedence than unary minus on its left.

```text
-2 ** 2
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

Here, parentheses make `-2` the base.

```text
(-2) ** 2
(-2) * (-2)
4
```

### Important Difference

| Expression | Result |
|---|---:|
| `-2 ** 2` | `-4` |
| `(-2) ** 2` | `4` |
| `-(2 ** 2)` | `-4` |
| `(-2) * (-2)` | `4` |

### Example with Negative Exponent

```python
result = 2 ** -2

print(result)
```

**Output:**

```text
0.25
```

The exponentiation operator binds more tightly than unary minus on its left, but the exponent on its right can itself contain a unary expression.

Conceptually:

```text
2 ** (-2)
1 / (2 ** 2)
0.25
```

This behavior is a useful exception to remember.

---

# 10. Multiplication, Division, Floor Division, and Modulus

The following operators share the same precedence level:

- `*`
- `@`
- `/`
- `//`
- `%`

The `@` operator is used for matrix multiplication with compatible objects.

For ordinary arithmetic calculations, the other five operators are more common.

### Example 1: Multiplication and Addition

```python
result = 10 + 5 * 2

print(result)
```

**Output:**

```text
20
```

Multiplication is performed before addition.

### Example 2: Division and Addition

```python
result = 20 / 4 + 5

print(result)
```

**Output:**

```text
10.0
```

Evaluation:

```text
20 / 4 + 5
5.0 + 5
10.0
```

### Example 3: Floor Division

```python
result = 20 // 3 * 2

print(result)
```

**Output:**

```text
12
```

Evaluation:

```text
20 // 3 * 2
6 * 2
12
```

### Example 4: Modulus

```python
result = 20 % 6 * 2

print(result)
```

**Output:**

```text
4
```

Evaluation:

```text
20 % 6 * 2
2 * 2
4
```

### Important Rule

Multiplication, division, floor division, and modulus have equal precedence.

When they occur together, they are grouped from left to right.

Example:

```python
result = 100 / 10 * 2

print(result)
```

**Output:**

```text
20.0
```

Evaluation:

```text
100 / 10 * 2
10.0 * 2
20.0
```

---

# 11. Addition and Subtraction Precedence

Addition and subtraction have the same precedence level.

They are normally grouped from left to right.

### Example

```python
result = 20 - 5 + 2

print(result)
```

**Output:**

```text
17
```

Evaluation:

```text
20 - 5 + 2
15 + 2
17
```

### Another Example

```python
result = 50 + 10 - 20

print(result)
```

**Output:**

```text
40
```

Evaluation:

```text
50 + 10 - 20
60 - 20
40
```

### Important Point

Do not assume addition is always evaluated before subtraction.

They share the same precedence level.

The normal left-to-right grouping determines the result.

### Parentheses Example

```python
result = 20 - (5 + 2)

print(result)
```

**Output:**

```text
13
```

The parentheses change the grouping.

---

# 12. Bitwise Shift Operator Precedence

The shift operators are:

- `<<` — Left shift.
- `>>` — Right shift.

They have lower precedence than addition and higher precedence than bitwise AND.

### Example 1: Addition and Left Shift

```python
result = 1 + 2 << 2

print(result)
```

**Output:**

```text
12
```

Evaluation:

```text
1 + 2 << 2
3 << 2
12
```

Addition is evaluated before shifting.

### Example 2: Parentheses

```python
result = 1 + (2 << 2)

print(result)
```

**Output:**

```text
9
```

Evaluation:

```text
1 + (2 << 2)
1 + 8
9
```

The parentheses change the result.

### Example 3: Right Shift

```python
result = 16 >> 2 + 1

print(result)
```

**Output:**

```text
2
```

Evaluation:

```text
16 >> (2 + 1)
16 >> 3
2
```

### Important Rule

Addition and subtraction have higher precedence than bitwise shifts.

For more details about the binary representation and shift operators, refer to:

`../05-Bitwise-Operators/README.md`

---

# 13. Bitwise AND, XOR, and OR Precedence

Python provides three important bitwise operators:

- `&` — Bitwise AND.
- `^` — Bitwise XOR.
- `|` — Bitwise OR.

Their precedence order is:

```text
Bitwise AND
     |
     v
Bitwise XOR
     |
     v
Bitwise OR
```

In other words:

`&` has higher precedence than `^`, and `^` has higher precedence than `|`.

### Example 1: Bitwise AND Before OR

```python
result = 5 | 2 & 1

print(result)
```

**Output:**

```text
5
```

Evaluation:

```text
5 | 2 & 1
5 | (2 & 1)
5 | 0
5
```

### Example 2: Bitwise XOR Before OR

```python
result = 5 | 3 ^ 1

print(result)
```

**Output:**

```text
7
```

Evaluation:

```text
5 | 3 ^ 1
5 | (3 ^ 1)
5 | 2
7
```

### Example 3: Using Parentheses

```python
result = (5 | 2) & 1

print(result)
```

**Output:**

```text
1
```

The parentheses make the OR operation happen before the AND operation.

### Important Point

Bitwise operators work on integer bit patterns.

Do not confuse them with Boolean logical operators such as `and` and `or`.

---

# 14. Comparison Operator Precedence

Comparison operators compare two values and return Boolean results.

Python's comparison group includes:

- `<`
- `<=`
- `>`
- `>=`
- `==`
- `!=`
- `in`
- `not in`
- `is`
- `is not`

These operators share the same precedence level.

### Example 1: Arithmetic Before Comparison

```python
result = 10 + 5 > 3 * 4

print(result)
```

**Output:**

```text
True
```

Evaluation:

```text
10 + 5 > 3 * 4
15 > 12
True
```

### Example 2: Comparison with Addition

```python
result = 10 == 5 + 5

print(result)
```

**Output:**

```text
True
```

Addition happens before comparison.

### Example 3: Comparison with Membership

```python
numbers = [10, 20, 30]

result = 20 in numbers

print(result)
```

**Output:**

```text
True
```

### Example 4: Comparison with Identity

```python
value = None

result = value is None

print(result)
```

**Output:**

```text
True
```

### Important Note

Although these operators share a precedence level, comparisons have special chaining behavior.

---

# 15. Chained Comparisons

Python allows multiple comparison operators to be chained together.

### Example

```python
number = 5

result = 1 < number < 10

print(result)
```

**Output:**

```text
True
```

This checks whether the number is greater than 1 and less than 10.

### Equivalent Logical Form

```python
result = 1 < number and number < 10
```

Both expressions have the same comparison meaning, and the middle expression is evaluated only once in a chained comparison.

### Another Example

```python
marks = 85

result = 0 <= marks <= 100

print(result)
```

**Output:**

```text
True
```

This is useful for validating values within a range.

### Example with Invalid Value

```python
marks = 120

result = 0 <= marks <= 100

print(result)
```

**Output:**

```text
False
```

### Step-by-Step Evaluation

For:

```python
0 <= 85 <= 100
```

Python checks:

```text
0 <= 85
85 <= 100
```

Both comparisons are true.

Therefore, the complete chained comparison is `True`.

### Important Point

Chained comparisons are not evaluated in exactly the same way as simply joining unrelated comparison expressions with `and`, especially when the middle expression has side effects.

For ordinary variable comparisons, the chained form is convenient and readable.

---

# 16. Logical NOT Precedence

The `not` operator reverses a truth value.

It has lower precedence than comparisons but higher precedence than `and` and `or`.

### Example 1

```python
result = not True

print(result)
```

**Output:**

```text
False
```

### Example 2: NOT with Comparison

```python
number = 10

result = not number > 5

print(result)
```

**Output:**

```text
False
```

Python interprets this as:

```python
result = not (number > 5)
```

Evaluation:

```text
number > 5
10 > 5
True

not True
False
```

### Example 3: Parentheses

```python
number = 10

result = (not number) > 5
```

This expression is different from `not number > 5`.

For the given integer, `not number` becomes `False`, and comparing that Boolean value with `5` produces `False`.

Use parentheses only when you intentionally want a different grouping.

### Important Rule

Comparisons are evaluated before logical `not`.

---

# 17. Logical AND and OR Precedence

The logical precedence order is:

1. `not`
2. `and`
3. `or`

### Example 1

```python
result = True or False and False

print(result)
```

**Output:**

```text
True
```

Evaluation:

```text
True or False and False
True or (False and False)
True or False
True
```

### Example 2

```python
result = False or True and False

print(result)
```

**Output:**

```text
False
```

Evaluation:

```text
False or True and False
False or (True and False)
False or False
False
```

### Example 3: All Three Operators

```python
result = not False and False or True

print(result)
```

**Output:**

```text
True
```

Evaluation:

```text
not False and False or True
True and False or True
False or True
True
```

### Logical Precedence Table

| Operator | Priority |
|---|---|
| `not` | Higher |
| `and` | Middle |
| `or` | Lower |

### Best Practice

When writing complicated logical expressions, use parentheses to show the intended grouping.

---

# 18. Conditional Expression Precedence

A conditional expression is a compact way of selecting one of two values.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
marks = 75

result = "PASS" if marks >= 40 else "FAIL"

print(result)
```

**Output:**

```text
PASS
```

### Explanation

1. Python evaluates `marks >= 40`.
2. The condition is `True`.
3. Python selects `"PASS"`.
4. The selected value is assigned to `result`.

### Another Example

```python
age = 16

category = "Adult" if age >= 18 else "Minor"

print(category)
```

**Output:**

```text
Minor
```

### Conditional Expression vs If-Else Statement

Conditional expression:

```python
result = "PASS" if marks >= 40 else "FAIL"
```

If-else statement:

```python
if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"
```

Both can be used to select a value based on a condition.

Use the normal `if-else` statement when the logic becomes long or complicated.

---

# 19. Complete Logical Precedence Summary

The logical operators have this order:

```text
not
 |
 v
and
 |
 v
or
```

### Example

```python
result = not False and True or False

print(result)
```

**Output:**

```text
True
```

### Evaluation

```text
not False and True or False
True and True or False
True or False
True
```

### Another Example with Parentheses

```python
result = not (False and True) or False

print(result)
```

**Output:**

```text
True
```

Evaluation:

```text
False and True
False

not False
True

True or False
True
```

### Remember

- `not` reverses truthiness.
- `and` requires both conditions to be truthy.
- `or` requires at least one condition to be truthy.

---

# 20. Operator Precedence vs Operator Associativity

Operator precedence and operator associativity are related but different.

### Operator Precedence

Determines which operator has higher priority.

Example:

```python
10 + 5 * 2
```

Multiplication has higher precedence than addition.

### Operator Associativity

Determines how operators with equal precedence are grouped or evaluated.

Example:

```python
20 - 5 + 2
```

Addition and subtraction have equal precedence.

They group from left to right:

```text
(20 - 5) + 2
15 + 2
17
```

### Difference

| Operator Precedence | Operator Associativity |
|---|---|
| Determines operator priority | Determines grouping for equal-precedence operators |
| Compares different precedence levels | Matters when operators share a precedence level |
| Example: `+` and `*` | Example: `-` and `+` |
| Multiplication before addition | Subtraction and addition group left to right |

### Important Exception

Exponentiation groups from right to left:

```python
2 ** 3 ** 2
```

This means:

```python
2 ** (3 ** 2)
```

The complete associativity topic will be covered in the next subtopic.

---

# 21. Step-by-Step Expression Solving Method

Whenever you see a complicated expression in an exam or programming problem, follow this method.

### Step 1: Identify All Operators

Example:

```python
result = 10 + 5 * 2 ** 3
```

Operators:

- Addition.
- Multiplication.
- Exponentiation.

### Step 2: Check Operator Precedence

Exponentiation has the highest precedence among these operators.

Multiplication comes next.

Addition comes last.

### Step 3: Evaluate the Highest-Precedence Operation

```text
2 ** 3 = 8
```

### Step 4: Evaluate Multiplication

```text
5 * 8 = 40
```

### Step 5: Evaluate Addition

```text
10 + 40 = 50
```

### Final Answer

```text
50
```

### Another Example

```python
result = 20 + 12 / 4 * 2 - 3
```

Evaluation:

```text
12 / 4 = 3.0
3.0 * 2 = 6.0
20 + 6.0 = 26.0
26.0 - 3 = 23.0
```

**Output:**

```text
23.0
```

### Recommended Method

1. Identify the operators.
2. Apply parentheses first.
3. Check precedence.
4. Apply associativity where needed.
5. Evaluate comparisons and logical conditions.
6. Check the final result and its data type.

---

# 22. Parentheses and Grouping in Complex Expressions

Parentheses can make complex expressions easier to understand.

### Example 1: Without Parentheses

```python
result = 10 + 5 * 2 - 4 / 2

print(result)
```

**Output:**

```text
18.0
```

Evaluation:

```text
10 + 5 * 2 - 4 / 2
10 + 10 - 2.0
20 - 2.0
18.0
```

### Example 2: With Parentheses

```python
result = (10 + 5) * (2 - 4) / 2

print(result)
```

**Output:**

```text
-15.0
```

Evaluation:

```text
(10 + 5) * (2 - 4) / 2
15 * (-2) / 2
-30 / 2
-15.0
```

### Example 3: Financial Calculation

```python
price = 2000
discount = 10

final_price = price - (price * discount / 100)

print(final_price)
```

**Output:**

```text
1800.0
```

Parentheses make the discount calculation clear.

### Example 4: Eligibility Condition

```python
age = 20
has_id = True
has_guardian = False

eligible = (age >= 18 and has_id) or (
    age >= 16 and has_guardian
)

print(eligible)
```

**Output:**

```text
True
```

Parentheses make the intended groups of conditions clear.

---

# 23. Common Precedence Mistakes

### Mistake 1: Assuming Addition Happens Before Multiplication

Incorrect expectation:

```python
result = 10 + 5 * 2
```

Actual result:

```text
20
```

Correct grouping when addition should happen first:

```python
result = (10 + 5) * 2
```

Result:

```text
30
```

### Mistake 2: Ignoring Exponentiation Priority

```python
result = 2 + 3 ** 2
```

Actual result:

```text
11
```

Exponentiation is evaluated before addition.

### Mistake 3: Incorrectly Understanding Unary Minus

```python
print(-2 ** 2)
```

Output:

```text
-4
```

Use:

```python
print((-2) ** 2)
```

when the negative value is intended to be the base.

### Mistake 4: Assuming Multiplication Is Always Evaluated Before Division

Multiplication and division have equal precedence.

```python
result = 100 / 10 * 2
```

Output:

```text
20.0
```

They group from left to right.

### Mistake 5: Incorrectly Grouping Logical Expressions

```python
result = True or False and False
```

Output:

```text
True
```

`and` has higher precedence than `or`.

### Mistake 6: Confusing Bitwise AND and OR Priority

```python
result = 5 | 2 & 1
```

Output:

```text
5
```

Bitwise AND is evaluated before bitwise OR.

### Mistake 7: Forgetting Addition Before Shifting

```python
result = 1 + 2 << 2
```

Output:

```text
12
```

Addition has higher precedence than shifting.

### Mistake 8: Ignoring Parentheses in Comparison Conditions

```python
result = 10 + 5 > 3 * 4
```

The arithmetic calculations happen before comparison.

Result:

```text
True
```

### Mistake 9: Confusing Chained Comparisons

```python
number = 5

print(1 < number < 10)
```

Output:

```text
True
```

This is a chained comparison, not a mathematical expression that Python evaluates as two unrelated comparisons.

### Mistake 10: Writing Unclear Complex Expressions

Even when Python can evaluate an expression, unclear grouping makes programs harder to read.

Use parentheses when they help communicate intent.

---

# 24. Best Practices

Follow these practices while writing Python expressions.

1. Understand the precedence table.
2. Remember that parentheses have priority.
3. Understand the relationship between precedence and associativity.
4. Use parentheses for complex arithmetic expressions.
5. Use parentheses for complicated logical conditions.
6. Remember exponentiation's special grouping behavior.
7. Remember that multiplication, division, floor division, and modulus share precedence.
8. Remember that addition and subtraction share precedence.
9. Remember that bitwise AND has higher precedence than XOR and OR.
10. Remember that comparisons come before logical `not`.
11. Remember the order `not`, `and`, `or`.
12. Break complicated expressions into intermediate variables when needed.
13. Avoid unnecessary nesting.
14. Keep mathematical formulas readable.
15. Test expressions with different values.
16. Check the result type.
17. Use descriptive variable names.
18. Avoid relying on mental shortcuts when a dry run can verify the result.
19. Use the correct grouping for financial and mathematical formulas.
20. Practise evaluating expressions manually.

---

# 25. Time Complexity and Operator Precedence

Operator precedence itself is a rule for evaluation order. It does not automatically determine the time complexity of an expression.

The computational cost depends on the operations and objects involved.

| Operation | Typical Cost |
|---|---|
| Basic comparison of built-in numeric values | Usually constant for ordinary fixed-size values |
| Addition of arbitrary-size integers | Depends on integer size |
| Multiplication of large integers | Depends on integer size and multiplication algorithm |
| List indexing | \(O(1)\) |
| List slicing | \(O(k)\), where \(k\) is the output length |
| List membership | \(O(n)\) worst case |
| Set membership | Average \(O(1)\) |
| Dictionary key lookup | Average \(O(1)\) |
| `len()` on built-in lists and strings | \(O(1)\) |

### Important Difference

Precedence tells Python which operation binds first.

Time complexity tells us how the cost of an operation grows as input size increases.

These are different concepts.

---

# 26. Twelve Examples Explained

The Python file `02_operator_precedence.py` contains twelve examples.

Each example demonstrates an important precedence rule.

## Example 1: Parentheses

**Objective:** Understand how parentheses change expression evaluation.

```python
result1 = 10 + 5 * 2

result2 = (10 + 5) * 2

print(result1)
print(result2)
```

**Output:**

```text
20
30
```

**Explanation:**

- In the first expression, multiplication happens first.
- In the second expression, addition happens first because of parentheses.

**Concept:** Grouping and parentheses precedence.

## Example 2: Exponentiation Before Multiplication

```python
result = 2 + 3 ** 2 * 2

print(result)
```

**Output:**

```text
20
```

**Explanation:**

```text
2 + 3 ** 2 * 2
2 + 9 * 2
2 + 18
20
```

**Concept:** Exponentiation, multiplication, and addition priority.

## Example 3: Unary Minus and Exponentiation

```python
result1 = -2 ** 2

result2 = (-2) ** 2

print(result1)
print(result2)
```

**Output:**

```text
-4
4
```

**Explanation:**

- `-2 ** 2` is interpreted as `-(2 ** 2)`.
- `(-2) ** 2` uses `-2` as the base.

**Concept:** Unary minus and exponentiation.

## Example 4: Multiplication and Division

```python
result = 100 / 10 * 2

print(result)
```

**Output:**

```text
20.0
```

**Explanation:**

Division and multiplication have equal precedence.

They group from left to right.

**Concept:** Equal-precedence arithmetic operators.

## Example 5: Floor Division and Multiplication

```python
result = 20 // 3 * 2

print(result)
```

**Output:**

```text
12
```

**Explanation:**

```text
20 // 3 = 6
6 * 2 = 12
```

**Concept:** Floor division and multiplication.

## Example 6: Addition and Subtraction

```python
result = 20 - 5 + 2

print(result)
```

**Output:**

```text
17
```

**Explanation:**

Subtraction and addition share the same precedence.

They are grouped from left to right.

**Concept:** Addition and subtraction precedence.

## Example 7: Addition and Left Shift

```python
result = 1 + 2 << 2

print(result)
```

**Output:**

```text
12
```

**Explanation:**

```text
1 + 2 = 3
3 << 2 = 12
```

**Concept:** Arithmetic precedence over shift operations.

## Example 8: Bitwise Precedence

```python
result = 5 | 2 & 1

print(result)
```

**Output:**

```text
5
```

**Explanation:**

```text
2 & 1 = 0
5 | 0 = 5
```

**Concept:** Bitwise AND before bitwise OR.

## Example 9: Arithmetic and Comparison

```python
result = 10 + 5 > 3 * 4

print(result)
```

**Output:**

```text
True
```

**Explanation:**

```text
10 + 5 = 15
3 * 4 = 12
15 > 12
True
```

**Concept:** Arithmetic before comparison.

## Example 10: Chained Comparison

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

- `1 < 5` is true.
- `5 < 10` is true.

Both comparisons are satisfied.

**Concept:** Chained comparisons.

## Example 11: NOT, AND, OR Precedence

```python
result1 = not False and False or True

result2 = not (False and False) or True

print(result1)
print(result2)
```

**Output:**

```text
True
True
```

**Explanation:**

First expression:

```text
not False and False or True
True and False or True
False or True
True
```

Second expression:

```text
not (False and False) or True
not False or True
True or True
True
```

Both expressions produce `True`, even though their grouping differs.

**Concept:** Logical precedence and parentheses.

## Example 12: Conditional Expression

```python
marks = 75

result = "PASS" if marks >= 40 else "FAIL"

print(result)
```

**Output:**

```text
PASS
```

**Explanation:**

The condition `marks >= 40` is true.

Therefore, the conditional expression selects `"PASS"`.

**Concept:** Conditional expression evaluation.

---

# 27. Twelve Solved Problems

The Python file contains twelve interactive solved problems.

Each problem applies operator precedence to a practical calculation or condition.

## Problem 1: Arithmetic Precedence

**Problem Statement:**

Take three values from the user and evaluate:

\[
a+b\times c
\]

### Code

```python
a = 10
b = 5
c = 2

result = a + b * c

print(result)
```

**Output:**

```text
20
```

### Dry Run

```text
10 + 5 * 2
10 + 10
20
```

### Logic

1. Read three numbers.
2. Evaluate multiplication.
3. Add the first number.
4. Display the result.

**Concept:** Multiplication before addition.

---

## Problem 2: Parentheses Comparison

**Problem Statement:**

Evaluate the same values using two expressions: one without parentheses and another with parentheses.

### Code

```python
a = 10
b = 5
c = 2

result1 = a + b * c

result2 = (a + b) * c

print(result1)
print(result2)
```

**Output:**

```text
20
30
```

### Dry Run

First expression:

```text
10 + 5 * 2
10 + 10
20
```

Second expression:

```text
(10 + 5) * 2
15 * 2
30
```

### Concept

Parentheses control grouping.

---

## Problem 3: Average Using Parentheses

**Problem Statement:**

Calculate the average of three marks.

### Formula

\[
Average = \frac{a+b+c}{3}
\]

### Code

```python
a = 70
b = 80
c = 90

average = (a + b + c) / 3

print(average)
```

**Output:**

```text
80.0
```

### Dry Run

```text
(70 + 80 + 90) / 3
240 / 3
80.0
```

### Concept

Parentheses in mathematical formulas.

---

## Problem 4: Discount and Tax Calculation

**Problem Statement:**

Calculate the final product price after applying a discount and then adding tax to the discounted price.

### Formulas

\[
Discount = \frac{Price\times DiscountRate}{100}
\]

\[
DiscountedPrice = Price-Discount
\]

\[
Tax = \frac{DiscountedPrice\times TaxRate}{100}
\]

\[
FinalPrice = DiscountedPrice+Tax
\]

### Code

```python
price = 2000

discount_rate = 10

tax_rate = 18

discount = price * discount_rate / 100

discounted_price = price - discount

tax = discounted_price * tax_rate / 100

final_price = discounted_price + tax

print("Final Price:", final_price)
```

**Output:**

```text
Final Price: 2124.0
```

### Dry Run

```text
Original Price = 2000

Discount = 2000 * 10 / 100
Discount = 200

Discounted Price = 2000 - 200
Discounted Price = 1800

Tax = 1800 * 18 / 100
Tax = 324

Final Price = 1800 + 324
Final Price = 2124
```

### Concept

Multiple expressions and real-world financial calculations.

---

## Problem 5: Convert Time into Total Seconds

**Problem Statement:**

Take hours, minutes, and seconds and calculate the total number of seconds.

### Formula

\[
TotalSeconds = Hours\times3600 + Minutes\times60 + Seconds
\]

### Code

```python
hours = 2
minutes = 30
seconds = 15

total_seconds = hours * 3600 + minutes * 60 + seconds

print(total_seconds)
```

**Output:**

```text
9015
```

### Dry Run

```text
2 * 3600 + 30 * 60 + 15
7200 + 1800 + 15
9015
```

### Concept

Multiplication has higher precedence than addition.

---

## Problem 6: Unary Minus and Exponentiation

**Problem Statement:**

Take a number and demonstrate the difference between `-number ** 2` and `(-number) ** 2`.

### Code

```python
number = 3

result1 = -number ** 2

result2 = (-number) ** 2

print(result1)
print(result2)
```

**Output:**

```text
-9
9
```

### Dry Run

First expression:

```text
-3 ** 2
-(3 ** 2)
-9
```

Second expression:

```text
(-3) ** 2
(-3) * (-3)
9
```

### Concept

Exponentiation and unary operator precedence.

---

## Problem 7: Floor Division and Remainder

**Problem Statement:**

Take the total number of items and the capacity of each box. Calculate the number of complete boxes and remaining items.

### Formulas

\[
FullBoxes = TotalItems//Capacity
\]

\[
RemainingItems = TotalItems\%Capacity
\]

### Code

```python
items = 25

capacity = 6

full_boxes = items // capacity

remaining_items = items % capacity

print("Full Boxes:", full_boxes)
print("Remaining:", remaining_items)
```

**Output:**

```text
Full Boxes: 4
Remaining: 1
```

### Dry Run

```text
25 // 6 = 4

25 % 6 = 1
```

Four boxes contain six items each, with one item remaining.

### Concept

Floor division and modulus expressions.

---

## Problem 8: Eligibility with Logical Operators

**Problem Statement:**

Check eligibility using two alternative conditions.

Conditions:

- A person aged 18 or above must have a valid ID.
- A person aged 16 or above may qualify when a guardian is available.

### Expression

```python
(age >= 18 and has_id) or (age >= 16 and has_guardian)
```

### Code

```python
age = 17

has_id = False

has_guardian = True

eligible = (
    (age >= 18 and has_id)
    or (age >= 16 and has_guardian)
)

print(eligible)
```

**Output:**

```text
True
```

### Dry Run

First group:

```text
age >= 18
17 >= 18
False

False and False
False
```

Second group:

```text
age >= 16
17 >= 16
True

True and True
True
```

Complete expression:

```text
False or True
True
```

### Concept

Combining logical operators with parentheses.

---

## Problem 9: Validate Marks Using Chained Comparison

**Problem Statement:**

Check whether entered marks are between 0 and 100, including both boundaries.

### Code

```python
marks = 85

result = 0 <= marks <= 100

print(result)
```

**Output:**

```text
True
```

### Dry Run

```text
0 <= 85
True

85 <= 100
True

Final result = True
```

### Invalid Example

```python
marks = 120

print(0 <= marks <= 100)
```

Output:

```text
False
```

### Concept

Chained comparison expressions.

---

## Problem 10: Triangle Validation

**Problem Statement:**

Check whether three positive side lengths can form a valid triangle.

### Conditions

For three positive lengths \(a\), \(b\), and \(c\):

\[
a+b>c
\]

\[
a+c>b
\]

\[
b+c>a
\]

All three conditions must be true.

### Code

```python
a = 3
b = 4
c = 5

valid_triangle = (
    (a + b > c)
    and (a + c > b)
    and (b + c > a)
)

print(valid_triangle)
```

**Output:**

```text
True
```

### Dry Run

```text
3 + 4 > 5
7 > 5
True

3 + 5 > 4
8 > 4
True

4 + 5 > 3
9 > 3
True
```

All conditions are true.

### Important Point

The supplied interactive program also checks that all three side lengths are positive before applying the triangle inequalities.

### Concept

Comparison and logical expressions.

---

## Problem 11: Bitwise AND and Comparison Precedence

**Problem Statement:**

Check whether all required bits are set in an integer flag value.

### Expression

```python
(flags & required_mask) == required_mask
```

### Code

```python
flags = 13

required_mask = 5

result = (flags & required_mask) == required_mask

print(result)
```

**Output:**

```text
True
```

### Binary Representation

```text
flags         = 13 = 1101
required_mask =  5 = 0101
```

Bitwise AND:

```text
1101
0101
----
0101
```

The AND result is 5.

Comparison:

```text
5 == 5
True
```

### Why Use Parentheses?

The parentheses explicitly make the bitwise operation happen before the comparison.

### Important Edge Case

If the required mask is zero, this check returns `True`, because no bits are required.

If your application does not consider an empty requirement valid, add a separate validation.

### Concept

Bitwise and comparison precedence.

---

## Problem 12: Conditional Expression for Pass or Fail

**Problem Statement:**

Take marks and use a conditional expression to determine whether the student passes or fails.

### Code

```python
marks = 75

result = "PASS" if marks >= 40 else "FAIL"

print(result)
```

**Output:**

```text
PASS
```

### Dry Run

```text
marks >= 40
75 >= 40
True
```

Because the condition is true, Python selects:

```text
PASS
```

### Another Example

```python
marks = 30

result = "PASS" if marks >= 40 else "FAIL"

print(result)
```

**Output:**

```text
FAIL
```

### Concept

Conditional expressions.

---

# 32. Ten Unsolved Practice Questions

Try to solve these questions independently.

| No. | Practice Question | Hint |
|---|---|---|
| 1 | Evaluate `15 + 5 * 3`. | Multiplication before addition |
| 2 | Evaluate `(15 + 5) * 3`. | Parentheses first |
| 3 | Evaluate `2 + 4 ** 2 * 3`. | Exponentiation first |
| 4 | Compare `-3 ** 2` and `(-3) ** 2`. | Unary minus and power |
| 5 | Evaluate `50 / 5 * 2`. | Left-to-right for equal precedence |
| 6 | Evaluate `30 - 10 + 5`. | Addition and subtraction |
| 7 | Evaluate `1 + 3 << 2`. | Addition before shifting |
| 8 | Evaluate `7 \| 4 & 2`. | Bitwise AND before OR |
| 9 | Check whether a number is between 10 and 100. | Chained comparison |
| 10 | Write a conditional expression for pass or fail. | `if ... else` expression |

### Additional Challenge Problems

**Challenge 1: Complex Arithmetic**

Evaluate:

```python
result = 20 + 5 * 3 ** 2 - 10 / 2
```

**Challenge 2: Parentheses**

Evaluate both expressions and explain the difference:

```python
a = 10 + 5 * 2

b = (10 + 5) * 2
```

**Challenge 3: Logical Precedence**

Evaluate:

```python
result = not False or True and False
```

**Challenge 4: Bitwise Precedence**

Evaluate:

```python
result = 7 | 4 & 2
```

**Challenge 5: Eligibility**

Write an expression that checks whether a student meets both marks and attendance requirements.

**Challenge 6: Temperature Range**

Check whether a temperature is between 20 and 40.

**Challenge 7: Discount Calculation**

Calculate a product's final price after two percentage-based calculations.

**Challenge 8: Time Conversion**

Convert 3 hours, 20 minutes, and 15 seconds into total seconds.

**Challenge 9: Triangle Validation**

Use comparison and logical expressions to validate three side lengths.

**Challenge 10: Bit Mask**

Check whether the required bits of an integer are set.

---

# 33. Common Mistakes and Their Solutions

## Mistake 1: Assuming Addition Happens Before Multiplication

Incorrect expectation:

```python
10 + 5 * 2
```

Actual result:

```text
20
```

Correct when addition should happen first:

```python
(10 + 5) * 2
```

Result:

```text
30
```

## Mistake 2: Incorrectly Understanding Exponentiation

```python
print(-2 ** 2)
```

Output:

```text
-4
```

For a negative base:

```python
print((-2) ** 2)
```

Output:

```text
4
```

## Mistake 3: Assuming Every Operator Has Different Precedence

Multiplication, division, floor division, and modulus share one precedence level.

Addition and subtraction also share a precedence level.

## Mistake 4: Forgetting Left-to-Right Grouping

```python
print(20 - 5 + 2)
```

Output:

```text
17
```

The expression is grouped as:

```text
(20 - 5) + 2
```

## Mistake 5: Incorrect Logical Grouping

```python
result = True or False and False

print(result)
```

Output:

```text
True
```

`and` has higher precedence than `or`.

## Mistake 6: Confusing Bitwise and Logical Operators

```python
5 & 3
```

performs bitwise AND.

```python
True and False
```

performs logical AND.

They are different operations.

## Mistake 7: Ignoring Addition Before Shift Operations

```python
print(1 + 2 << 2)
```

Output:

```text
12
```

Addition occurs before the shift.

## Mistake 8: Forgetting Comparison Precedence

```python
print(10 + 5 > 3 * 4)
```

Output:

```text
True
```

Arithmetic calculations happen before the comparison.

## Mistake 9: Forgetting Chained Comparisons

```python
number = 5

print(1 < number < 10)
```

Output:

```text
True
```

Both comparisons must be satisfied.

## Mistake 10: Writing Unclear Expressions

Avoid unnecessarily complicated one-line expressions.

Break them into meaningful variables when that improves understanding.

---

# 34. Best Practices

1. Memorize the major precedence groups.
2. Understand the difference between precedence and associativity.
3. Use parentheses for complex expressions.
4. Learn exponentiation's special behavior.
5. Remember that multiplication, division, floor division, and modulus have equal precedence.
6. Remember that addition and subtraction have equal precedence.
7. Remember the bitwise precedence order: `&`, then `^`, then `|`.
8. Remember the logical precedence order: `not`, then `and`, then `or`.
9. Understand that comparisons occur before logical `not`.
10. Use chained comparisons for simple numerical range checks.
11. Use parentheses for complex eligibility conditions.
12. Avoid unnecessarily long expressions.
13. Break complex calculations into smaller steps.
14. Test expressions with different values.
15. Check boundary cases.
16. Use descriptive intermediate variables.
17. Use the correct mathematical formula.
18. Keep bitwise expressions separate from logical expressions when appropriate.
19. Explain your expression step by step.
20. Practise manually evaluating expressions.

---

# 35. Debugging and Troubleshooting

When an expression produces an unexpected result, follow these steps.

### Step 1: Identify Operators

Write down every operator present in the expression.

### Step 2: Check Precedence

Refer to the precedence table.

### Step 3: Identify Parentheses

Evaluate grouped sections first.

### Step 4: Check Associativity

If operators have equal precedence, determine their grouping rules.

### Step 5: Calculate Intermediate Results

For example:

```python
result = 10 + 5 * 2
```

Use:

```python
first_result = 5 * 2

final_result = 10 + first_result

print(final_result)
```

### Step 6: Check Data Types

```python
print(type(result))
```

### Step 7: Check Logical Conditions

Evaluate the individual Boolean conditions separately.

### Step 8: Check Division

Make sure that the denominator is not zero.

### Step 9: Check Bitwise Values

For bitwise expressions, write down the binary representation.

### Step 10: Use Parentheses

Add parentheses to make the intended grouping explicit.

---

# 36. Practice Test

Solve the following questions without running the code.

## Question 1

```python
print(10 + 5 * 2)
```

What is the output?

## Question 2

```python
print((10 + 5) * 2)
```

What is the output?

## Question 3

```python
print(2 + 3 ** 2)
```

What is the output?

## Question 4

```python
print(-2 ** 2)
```

What is the output?

## Question 5

```python
print((-2) ** 2)
```

What is the output?

## Question 6

```python
print(100 / 10 * 2)
```

What is the output?

## Question 7

```python
print(20 - 5 + 2)
```

What is the output?

## Question 8

```python
print(1 + 2 << 2)
```

What is the output?

## Question 9

```python
print(5 | 2 & 1)
```

What is the output?

## Question 10

```python
number = 5

print(1 < number < 10)
```

What is the output?

## Question 11

```python
print(not False and False or True)
```

What is the output?

## Question 12

```python
marks = 75

result = "PASS" if marks >= 40 else "FAIL"

print(result)
```

What is the output?

### Answer Key

| Question | Answer | Explanation |
|---|---|---|
| 1 | `20` | Multiplication before addition |
| 2 | `30` | Parentheses first |
| 3 | `11` | Exponentiation before addition |
| 4 | `-4` | Exponentiation before unary minus |
| 5 | `4` | Negative value is grouped as the base |
| 6 | `20.0` | Division and multiplication left to right |
| 7 | `17` | Subtraction and addition left to right |
| 8 | `12` | Addition before shifting |
| 9 | `5` | Bitwise AND before OR |
| 10 | `True` | Both comparisons are satisfied |
| 11 | `True` | `not`, then `and`, then `or` |
| 12 | `PASS` | Marks satisfy the condition |

---

# 37. Viva Questions and Answers

Prepare these questions for college practical examinations and interviews.

## A. Basic Questions

**Q1. What is operator precedence in Python?**

Operator precedence determines the priority of operators when evaluating an expression.

**Q2. Why is operator precedence required?**

It provides consistent rules for evaluating expressions containing multiple operators.

**Q3. What happens when an expression contains multiplication and addition?**

Multiplication is evaluated before addition.

**Q4. Which has higher precedence: addition or multiplication?**

Multiplication.

**Q5. Which has higher precedence: parentheses or multiplication?**

Parenthesized grouping.

**Q6. What is the purpose of parentheses in expressions?**

They group parts of an expression and control evaluation.

**Q7. What is the highest-level grouping used in ordinary expressions?**

Parenthesized grouping and primary expressions such as function calls and indexing bind very tightly.

**Q8. Does operator precedence determine the meaning of every expression by itself?**

No. Associativity and special expression rules can also matter.

**Q9. What is the difference between precedence and associativity?**

Precedence determines operator priority, whereas associativity determines grouping when equal-precedence operators occur.

**Q10. What is expression evaluation?**

It is the process of calculating or determining an expression's result.

## B. Arithmetic Precedence

**Q11. Which operator has higher precedence: `+` or `*`?**

`*`.

**Q12. Which operator has higher precedence: `+` or `**`?**

`**`.

**Q13. What is the output of `10 + 5 * 2`?**

`20`.

**Q14. What is the output of `(10 + 5) * 2`?**

`30`.

**Q15. What is the result of `-2 ** 2`?**

`-4`.

**Q16. What is the result of `(-2) ** 2`?**

`4`.

**Q17. Which direction does exponentiation group?**

Right to left.

**Q18. Do multiplication and division have equal precedence?**

Yes.

**Q19. Do addition and subtraction have equal precedence?**

Yes.

**Q20. What is the result of `20 - 5 + 2`?**

`17`.

## C. Bitwise Precedence

**Q21. Which has higher precedence: bitwise AND or bitwise OR?**

Bitwise AND.

**Q22. Which has higher precedence: bitwise XOR or bitwise OR?**

Bitwise XOR.

**Q23. What is the bitwise precedence order?**

`&`, then `^`, then `|`.

**Q24. Which has higher precedence: addition or left shift?**

Addition.

**Q25. What is the result of `1 + 2 << 2`?**

`12`.

## D. Comparison and Logical Precedence

**Q26. Which has higher precedence: arithmetic operators or comparison operators?**

Arithmetic operators.

**Q27. Do comparison operators have equal precedence?**

They belong to the same comparison group.

**Q28. What is a chained comparison?**

A comparison expression containing multiple comparison operators, such as `0 <= marks <= 100`.

**Q29. What is the result of `1 < 5 < 10`?**

`True`.

**Q30. Which logical operator has the highest precedence?**

`not`.

**Q31. Which logical operator has the lowest precedence among `not`, `and`, and `or`?**

`or`.

**Q32. What is the logical precedence order?**

`not`, then `and`, then `or`.

**Q33. What is the result of `True or False and False`?**

`True`.

**Q34. Why should parentheses be used in logical conditions?**

They make the intended grouping clear.

**Q35. Does `not` have higher precedence than comparison operators?**

No. Comparisons have higher precedence than `not`.

## E. Practical and Advanced Questions

**Q36. What is a conditional expression?**

An expression that selects one of two values based on a condition.

**Q37. What is the syntax of a conditional expression?**

`value_if_true if condition else value_if_false`.

**Q38. What is the precedence of a conditional expression compared with `or`?**

A conditional expression has lower precedence.

**Q39. What is the walrus operator?**

`:=` is an assignment expression operator.

**Q40. What is the precedence of `:=`?**

It has very low precedence.

**Q41. Why should complicated expressions be divided into smaller calculations?**

It improves readability, debugging, and maintenance.

**Q42. What happens when operators share the same precedence?**

Their associativity or special language rules determine grouping.

**Q43. Which operators typically group from left to right?**

Most binary operators, such as addition and subtraction, group from left to right.

**Q44. Which common arithmetic operator groups from right to left?**

Exponentiation.

**Q45. What is the difference between `and` and `&`?**

`and` is logical AND, while `&` is bitwise AND.

**Q46. Does operator precedence determine time complexity?**

No. Time complexity depends on the operations and objects being processed.

**Q47. Can parentheses change the result of an expression?**

Yes, by changing how operations are grouped.

**Q48. What is the output of `2 + 3 ** 2 * 2`?**

`20`.

**Q49. What is the output of `100 / 10 * 2`?**

`20.0`.

**Q50. Why is operator precedence important in DSA?**

It ensures mathematical, comparison, bitwise, and logical expressions are evaluated as intended.

---

# 38. Connection with Data Structures and Algorithms (DSA)

Operator precedence is used throughout Data Structures and Algorithms.

Algorithms frequently combine:

- Arithmetic operations.
- Comparisons.
- Logical conditions.
- Index calculations.
- Bitwise operations.
- Loop conditions.

Understanding precedence helps prevent logical errors.

## 38.1 Array Index Calculations

```python
numbers = [10, 20, 30, 40, 50, 60]

middle = (0 + len(numbers) - 1) // 2

print(middle)
```

**Output:**

```text
2
```

The expression calculates an index.

Such calculations appear in binary search and other algorithms.

## 38.2 Binary Search Conditions

```python
numbers = [10, 20, 30, 40, 50]

left = 0
right = len(numbers) - 1

target = 30

while left <= right:

    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Element found")
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1
```

**Output:**

```text
Element found
```

Important expressions:

```python
(left + right) // 2
```

Calculates the middle index.

```python
left <= right
```

Checks whether the search interval is valid.

```python
numbers[middle] == target
```

Checks whether the target has been found.

## 38.3 Two-Pointer Conditions

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

The expression `numbers[left] + numbers[right]` calculates a sum.

The comparison determines which pointer should move.

## 38.4 Bit Manipulation

```python
number = 13

mask = 4

result = (number & mask) != 0

print(result)
```

**Output:**

```text
True
```

Parentheses clearly group the bitwise operation before the comparison.

## 38.5 Filtering Values

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = [
    number
    for number in numbers
    if number % 2 == 0 and number > 3
]

print(result)
```

**Output:**

```text
[4, 6, 8]
```

This expression combines:

- Modulus.
- Comparison.
- Logical AND.
- List comprehension.

## 38.6 Why Is Precedence Important in DSA?

A small expression mistake can produce an incorrect algorithm.

For example, incorrect grouping in:

- Binary search middle-index calculations.
- Two-pointer conditions.
- Sliding window boundaries.
- Bitmask checks.
- Sorting comparisons.
- Dynamic programming transitions.

can cause logical errors.

### DSA Topics to Practise

1. Linear Search.
2. Binary Search.
3. Two-Pointer Technique.
4. Sliding Window.
5. Bit Manipulation.
6. Array Indexing.
7. Sorting.
8. Mathematical Algorithms.
9. Conditional Logic.
10. Dynamic Programming Expressions.

---

# 39. Mini Project: Expression Evaluation Practice Tool

Build a small program that calculates selected mathematical expressions.

### Requirements

1. Take three numbers from the user.
2. Calculate `a + b * c`.
3. Calculate `(a + b) * c`.
4. Calculate `a - b + c`.
5. Calculate `a ** b` when reasonable.
6. Calculate a comparison expression.
7. Display each result.
8. Explain the grouping of each expression.

### Example Code

```python
a = 10
b = 5
c = 2

result1 = a + b * c

result2 = (a + b) * c

result3 = a - b + c

result4 = a + b ** c

result5 = a + b > c * 2

print("Expression 1:", result1)
print("Expression 2:", result2)
print("Expression 3:", result3)
print("Expression 4:", result4)
print("Expression 5:", result5)
```

### Output

```text
Expression 1: 20
Expression 2: 30
Expression 3: 7
Expression 4: 20
Expression 5: True
```

### Extension Tasks

1. Add division.
2. Add floor division.
3. Add modulus.
4. Add exponentiation.
5. Add logical operators.
6. Add bitwise operators.
7. Add user input.
8. Display the evaluation steps.
9. Add error handling for zero division.
10. Allow the user to select expressions from a menu.

---

# 40. Glossary

| Term | Meaning |
|---|---|
| Operator Precedence | Priority of operators in an expression |
| Associativity | Grouping rule for operators of equal precedence |
| Expression | Code that evaluates to a value |
| Operand | Value or object on which an operator acts |
| Operator | Symbol or keyword that performs an operation |
| Parentheses | Symbols used to group expressions |
| Grouping | The way subexpressions are arranged |
| Exponentiation | Raising a number to a power |
| Unary Operator | Operator acting on one operand |
| Binary Operator | Operator acting on two operands |
| Floor Division | Division rounded down |
| Modulus | Remainder after division |
| Bitwise AND | Bit-level AND operation |
| Bitwise OR | Bit-level OR operation |
| Bitwise XOR | Bit-level exclusive OR operation |
| Shift Operator | Operator that shifts bits |
| Comparison | Checking a relationship between values |
| Chained Comparison | Multiple comparison expressions connected together |
| Logical NOT | Reverses truthiness |
| Logical AND | Combines conditions requiring both to be truthy |
| Logical OR | Combines conditions requiring at least one to be truthy |
| Conditional Expression | Selects a value based on a condition |
| Walrus Operator | `:=`, assignment expression operator |
| Evaluation | Determining the result of an expression |
| Short-Circuiting | Skipping unnecessary logical evaluation |

---

# 41. Quick Revision Notes

### Parentheses

```python
(10 + 5) * 2
```

### Exponentiation

```python
2 ** 3
```

### Unary Minus

```python
-2 ** 2
```

### Multiplication and Division

```python
100 / 10 * 2
```

### Addition and Subtraction

```python
20 - 5 + 2
```

### Shift Operators

```python
1 + 2 << 2
```

### Bitwise Operators

```python
5 | 2 & 1
```

### Comparison

```python
10 + 5 > 3 * 4
```

### Chained Comparison

```python
1 < number < 10
```

### Logical NOT, AND, OR

```python
not False and False or True
```

### Conditional Expression

```python
"PASS" if marks >= 40 else "FAIL"
```

### Important Rules

1. Parentheses group expressions.
2. Exponentiation comes before multiplication.
3. Unary minus has a special relationship with exponentiation.
4. Multiplication, division, floor division, and modulus share precedence.
5. Addition and subtraction share precedence.
6. Shift operators come after addition and subtraction.
7. Bitwise AND comes before XOR.
8. Bitwise XOR comes before OR.
9. Comparisons come after arithmetic and bitwise operations.
10. Comparisons come before logical `not`.
11. Logical `not` comes before `and`.
12. Logical `and` comes before `or`.
13. Conditional expressions have lower precedence than `or`.
14. Assignment expressions have very low precedence.
15. Use parentheses when expressions become difficult to read.

---

# 42. Learning Checklist

Complete this checklist before moving to the next topic.

## Basic Understanding

- [ ] I understand operator precedence.
- [ ] I understand why precedence rules are important.
- [ ] I know the general precedence table.
- [ ] I understand the difference between precedence and associativity.
- [ ] I can evaluate a simple expression.

## Arithmetic Precedence

- [ ] I understand parentheses precedence.
- [ ] I understand exponentiation.
- [ ] I understand unary minus.
- [ ] I understand multiplication and division.
- [ ] I understand floor division and modulus.
- [ ] I understand addition and subtraction.
- [ ] I can evaluate multiple arithmetic operators.

## Bitwise Precedence

- [ ] I understand shift operator precedence.
- [ ] I understand bitwise AND precedence.
- [ ] I understand bitwise XOR precedence.
- [ ] I understand bitwise OR precedence.
- [ ] I can evaluate a bitwise expression.

## Comparison and Logical Precedence

- [ ] I understand comparison precedence.
- [ ] I understand chained comparisons.
- [ ] I understand logical NOT.
- [ ] I understand logical AND.
- [ ] I understand logical OR.
- [ ] I can combine comparison and logical expressions.

## Advanced Understanding

- [ ] I understand conditional expression precedence.
- [ ] I understand assignment expression precedence.
- [ ] I can evaluate expressions step by step.
- [ ] I can use parentheses for grouping.
- [ ] I can explain all twelve examples.

## Programming Practice

- [ ] I have run the 12 examples.
- [ ] I have completed the 12 solved problems.
- [ ] I have attempted the 10 unsolved questions.
- [ ] I have completed the practice test.
- [ ] I have tried the expression evaluation project.

## DSA Preparation

- [ ] I understand precedence in array indexing.
- [ ] I understand precedence in binary search.
- [ ] I understand precedence in two-pointer conditions.
- [ ] I understand precedence in bit manipulation.
- [ ] I can write readable algorithm conditions.

---

# 43. How to Run the Python Program

The folder contains:

```text
02-operator-precedence/
│
├── README.md
│
└── 02_operator_precedence.py
```

### Step 1: Open PowerShell or VS Code Terminal

Navigate to your project folder.

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\08-Expressions\02-operator-precedence"
```

### Step 2: Run the Python File

```powershell
python 02_operator_precedence.py
```

### Step 3: Select a Menu Option

The program provides the following menu:

```text
=============================================================
                PYTHON OPERATOR PRECEDENCE
=============================================================

1. View 12 Operator Precedence Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

### Step 4: Follow the Learning Order

Recommended sequence:

1. Select option `1` and understand all twelve examples.
2. Select option `2` and solve all twelve programming problems.
3. Select option `3` and attempt all ten questions independently.
4. Select option `4` and review your learning progress.

### Step 5: Practise Manually

Before running an example, calculate its output yourself.

Then execute the program and compare your result.

This helps strengthen your understanding of expression evaluation.

---

# 44. Folder Structure

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
│
├── 04-parentheses-and-grouping/
│
└── 05-conditional-expressions/
```

### File Responsibilities

| File | Purpose |
|---|---|
| `README.md` | Complete theoretical study material |
| `02_operator_precedence.py` | Executable precedence examples and interactive problems |

Keep the Python code and README in the same folder.

---

# 45. Navigation

### Previous Topic

[01 - Expressions](../01-expressions/README.md)

### Current Topic

**02 - Operator Precedence**

### Next Topic

[03 - Operator Associativity](../03-operator-associativity/README.md)

### Expressions Main Folder

[08 - Expressions](../README.md)

### Parent Folder

[05 - Operators and Expressions](../../README.md)

---

# 46. Final Summary

Operator precedence determines the priority of operators when Python evaluates an expression containing multiple operations.

In this topic, you studied:

1. Meaning and importance of operator precedence.
2. The complete Python precedence table.
3. Parentheses and grouping.
4. Exponentiation precedence.
5. Unary operator precedence.
6. Multiplication and division precedence.
7. Addition and subtraction precedence.
8. Bitwise shift precedence.
9. Bitwise AND, XOR, and OR precedence.
10. Comparison operator precedence.
11. Chained comparisons.
12. Logical NOT, AND, and OR precedence.
13. Conditional expression precedence.
14. Difference between precedence and associativity.
15. Step-by-step expression evaluation.
16. Practical calculations.
17. Precedence in DSA algorithms.

### Most Important Concept to Remember

Consider:

```python
result = 10 + 5 * 2
```

Output:

```text
20
```

Now consider:

```python
result = (10 + 5) * 2
```

Output:

```text
30
```

The difference comes from grouping and operator precedence.

**Before moving to the next topic, practise all twelve examples, solve all twelve problems, attempt the ten unsolved questions, and revise the complete precedence table.**

A strong understanding of operator precedence will make complex expressions, logical conditions, and DSA algorithms much easier.

Keep practising and keep improving your Python fundamentals.