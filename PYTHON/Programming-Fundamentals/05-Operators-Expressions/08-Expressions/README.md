---
title: Python Expressions
topic: 08 - Expressions
week: Week 1 - Programming Fundamentals
section: 05 - Operators and Expressions
level: Beginner to Intermediate
---

# 08 - Expressions in Python
**Master README | Theory Guide | 500 Worked Expression Cards | Practice Workbook | Interview Reference**
**Repository location:** `PYTHON/Week-1-Programming-Fundamentals/05-Operators-Expressions/08-Expressions/README.md`

This README is the parent guide for all five expression subtopics in this folder. It is designed to be used with the five topic-specific Python programs and their individual README files. Study each chapter in order, predict outputs before running code, write dry runs in a notebook, and complete the practice bank without copying the examples.

The objective is not to memorize hundreds of outputs. The objective is to understand the rules that generate those outputs: data types, operator precedence, associativity, grouping, truthiness, short-circuit evaluation and conditional value selection.

## How to study this README
- Read the expression fundamentals first.
- Study precedence before associativity.
- Learn how parentheses change grouping.
- Finish with conditional expressions and compare them with if-else statements.
- Run the matching `.py` file in every subtopic folder.
- Predict an output before using the Python interpreter.
- Record each intermediate value during a dry run.
- Test boundaries, negative numbers, zero, empty strings and empty collections.
- When an answer differs from your prediction, identify the exact rule you missed.
- Use the 500 worked cards as a guided practice bank, not as a memorization list.

## Folder structure
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
│   ├── README.md
│   └── 04_parentheses_and_grouping.py
│
└── 05-conditional-expressions/
    ├── README.md
    └── 05_conditional_expressions.py
```

## Five-subtopic roadmap
| Order | Folder | Main learning question | Core skills |
|---|---|---|---|
| 01 | 01-expressions | What is an expression? | Values, operands, operators, arithmetic, strings, comparisons, membership and identity. |
| 02 | 02-operator-precedence | Which operation is grouped first? | The precedence hierarchy and default grouping. |
| 03 | 03-operator-associativity | How are equal-precedence operators grouped? | Left associativity, right associativity, exponentiation and comparison chaining. |
| 04 | 04-parentheses-and-grouping | How do I make my intended grouping clear? | Parentheses, nested groups, formulas, Boolean grouping and tuple syntax. |
| 05 | 05-conditional-expressions | How can an expression choose a value? | Ternary syntax, nested conditional expressions, truthiness and short-circuiting. |

## Learning outcomes
- Identify values, operands and operators in an expression.
- Distinguish an expression from a statement.
- Evaluate arithmetic and string expressions.
- Use comparison and logical expressions correctly.
- Understand bitwise, membership and identity expressions.
- Apply the Python precedence hierarchy.
- Explain the associativity of common operators.
- Understand the special right-associativity of exponentiation.
- Use parentheses to alter default grouping.
- Trace nested parentheses from the inside outward.
- Distinguish `(10)`, `(10,)` and `()`.
- Write conditional expressions with the correct syntax.
- Distinguish truthiness from checking specifically for None.
- Explain short-circuit evaluation.
- Debug expression-related syntax, type and logic errors.
- Use expression patterns in basic DSA algorithms.

## Prerequisites
You should know variables, assignment, basic data types, input, output, comparison operators and simple if-else statements. Advanced mathematics is not required. The important skill is reading the expression carefully and applying Python rules in the correct order.

# Part A - Expression Fundamentals
## 1. What is an expression?
An expression is a combination of literals, variables, operators, function calls or other Python constructs that Python evaluates to produce a value. A literal such as `10` is an expression. A name such as `score` is an expression. A calculation such as `score + 5` is also an expression.

```python
price = 250
quantity = 3
total = price * quantity
print(total)
```
The expression `price * quantity` is evaluated to 750, then the assignment statement stores that value in `total`. The call `print(total)` displays it.

## 2. Expression, statement and value
| Term | Meaning | Example |
|---|---|---|
| Value | A piece of data. | `42`, `3.5`, `"Python"`, `True` |
| Expression | Code evaluated to produce a value. | `a + b`, `len(name)`, `x > 0` |
| Statement | An instruction that performs an action. | `total = a + b`, `if x > 0:` |
| Assignment statement | Stores a value in a target. | `count = 10` |
| Function call | Calls a function and may return a value. | `max(a, b)` |

## 3. Operands and operators
An operand is a value or expression on which an operator acts. In `a + b`, the names `a` and `b` are operands and `+` is the operator. In `-number`, the expression has one operand and a unary operator.

| Expression | Operator | Operands |
|---|---|---|
| `8 + 4` | `+` | `8`, `4` |
| `score >= 40` | `>=` | `score`, `40` |
| `not logged_in` | `not` | `logged_in` |
| `name in names` | `in` | `name`, `names` |
| `2 ** 5` | `**` | `2`, `5` |

## 4. Main expression families
| Family | Purpose | Example |
|---|---|---|
| Arithmetic | Numeric calculations. | `(a + b) / 2` |
| Comparison | Compare values. | `age >= 18` |
| Logical | Combine or negate truth values. | `has_id and age >= 18` |
| Bitwise | Operate on integer bits. | `flags & mask` |
| Membership | Check containment. | `"py" in language` |
| Identity | Check object identity. | `value is None` |
| Conditional | Select one of two values. | `"Pass" if marks >= 40 else "Fail"` |
| Sequence | Index, slice, join or repeat sequences. | `names[0]`, `text[1:4]` |
| Assignment expression | Assign a value inside an expression. | `(n := len(items)) > 0` |

## 5. Numeric types and arithmetic
Python commonly uses `int`, `float` and `complex` for numeric expressions. `/` performs true division and returns a float. `//` performs floor division, rounding down toward negative infinity. `%` returns a remainder consistent with Python division rules. `**` performs exponentiation.

```python
print(7 + 3)       # 10
print(7 / 2)       # 3.5
print(7 // 2)      # 3
print(7 % 2)       # 1
print(2 ** 3)      # 8
print(-7 // 2)     # -4
```

## 6. String and sequence expressions
Strings support concatenation, repetition, length, indexing, slicing and membership tests. Lists and tuples also support indexing, slicing and membership. Dictionary membership checks keys by default.

```python
word = "Py" + "thon"
print(word)          # Python
print(word * 2)      # PythonPython
print(len(word))     # 6
print(word[0])       # P
print(word[1:4])     # yth
print("Py" in word)  # True
```

## 7. Boolean expressions, membership and identity
Comparisons usually produce `True` or `False`. `and` and `or` combine truthy/falsy operands and return one of their operands. `not` returns a Boolean. Membership uses `in` and `not in`. Identity uses `is` and `is not`. Use `==` to compare values and `is None` to test for None.

```python
age = 20
has_id = True
print(age >= 18 and has_id)       # True
print("Py" in "Python")          # True
value = None
print(value is None)              # True
print("" or "Guest")              # Guest
```

## 8. A disciplined evaluation method
- Identify the type of every operand.
- Locate parentheses and evaluate the innermost group first.
- Apply operator precedence inside the current group.
- Use associativity for operators sharing the same precedence.
- Respect short-circuit evaluation for and/or and conditional expressions.
- Check whether the operation changes the result type.
- Write intermediate values instead of skipping steps.
- Verify the final value and its type.

# Part B - Python Operator Precedence Reference
The table is ordered from higher precedence to lower precedence. It is a practical learning summary. Parentheses and primary expressions bind very tightly.

| Relative order | Operators or syntax | Meaning |
|---|---|---|
| Highest | Grouping `(x)`, displays, subscription `x[i]`, slicing `x[i:j]`, call `f(...)`, attribute `x.name` | Primary expressions and grouping. |
|  | `await x` | Await expression. |
|  | `**` | Exponentiation. |
|  | `+x`, `-x`, `~x` | Unary plus, unary minus and bitwise invert. |
|  | `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division and modulo. |
|  | `+`, `-` | Addition and subtraction. |
|  | `<<`, `>>` | Bitwise shifts. |
|  | `&` | Bitwise AND. |
|  | `^` | Bitwise XOR. |
|  | `|` | Bitwise OR. |
|  | Comparisons, `in`, `not in`, `is`, `is not` | Comparison, membership and identity. |
|  | `not x` | Boolean NOT. |
|  | `and` | Boolean AND. |
|  | `or` | Boolean OR. |
|  | `x if condition else y` | Conditional expression. |
|  | `lambda` | Lambda expression. |
| Lowest | `:=` | Assignment expression. |

## Precedence facts
- Multiplication, division, floor division and modulo bind more tightly than addition and subtraction.
- Addition and subtraction bind more tightly than bitwise shifts.
- Bitwise AND binds more tightly than XOR, which binds more tightly than OR.
- Comparisons bind more tightly than not.
- not binds more tightly than and.
- and binds more tightly than or.
- A conditional expression has lower precedence than or.
- Exponentiation groups right-to-left in a chain.
- Parentheses can override default grouping and should be used when they improve clarity.

## Precedence versus associativity
Precedence answers which operator group binds more tightly. Associativity answers how operators of equal precedence are grouped. In `20 - 5 - 2`, subtraction operators have equal precedence and group left-to-right, so the expression means `(20 - 5) - 2`.

```python
print(10 + 5 * 2)       # 20
print((10 + 5) * 2)     # 30
print(20 - 5 - 2)       # 13
print(20 - (5 - 2))     # 17
```

# 01 - Expressions
Expressions produce values from operands, operators, function calls and sequence operations.

## 100 worked cards - 01 - Expressions
Each card uses a different sample set. Read the expression, predict the result, run it, inspect its type, and then change one input to see how the result changes.

### 001. Arithmetic addition - set 01
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 12 + 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
17
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 002. Mixed arithmetic - set 01
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 12 + 5 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
22
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 003. Explicit arithmetic grouping - set 01
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (12 + 5) * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
34
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 004. True division - set 01
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 12 / 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2.4
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 005. Floor division - set 01
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 12 // 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 006. Modulo remainder - set 01
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 12 % 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 007. Exponentiation - set 01
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 2 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 008. Comparison - set 01
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 12 > 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 009. Logical comparison - set 01
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (12 > 5) and (5 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 010. Membership - set 01
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 5 in [12, 5, 2]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 011. Arithmetic addition - set 02
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 18 + 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
22
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 012. Mixed arithmetic - set 02
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 18 + 4 * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
30
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 013. Explicit arithmetic grouping - set 02
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (18 + 4) * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
66
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 014. True division - set 02
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 18 / 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 015. Floor division - set 02
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 18 // 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 016. Modulo remainder - set 02
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 18 % 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 017. Exponentiation - set 02
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 3 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
27
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 018. Comparison - set 02
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 18 > 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 019. Logical comparison - set 02
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (18 > 4) and (4 > 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 020. Membership - set 02
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 4 in [18, 4, 3]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 021. Arithmetic addition - set 03
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 25 + 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 022. Mixed arithmetic - set 03
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 25 + 6 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
37
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 023. Explicit arithmetic grouping - set 03
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (25 + 6) * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
62
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 024. True division - set 03
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 25 / 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4.166666666666667
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 025. Floor division - set 03
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 25 // 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 026. Modulo remainder - set 03
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 25 % 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 027. Exponentiation - set 03
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 2 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 028. Comparison - set 03
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 25 > 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 029. Logical comparison - set 03
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (25 > 6) and (6 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 030. Membership - set 03
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 6 in [25, 6, 2]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 031. Arithmetic addition - set 04
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 31 + 7
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
38
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 032. Mixed arithmetic - set 04
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 31 + 7 * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
59
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 033. Explicit arithmetic grouping - set 04
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (31 + 7) * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
152
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 034. True division - set 04
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 31 / 7
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4.428571428571429
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 035. Floor division - set 04
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 31 // 7
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 036. Modulo remainder - set 04
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 31 % 7
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 037. Exponentiation - set 04
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 4 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
64
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 038. Comparison - set 04
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 31 > 7
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 039. Logical comparison - set 04
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (31 > 7) and (7 > 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 040. Membership - set 04
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 7 in [31, 7, 4]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 041. Arithmetic addition - set 05
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 42 + 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
50
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 042. Mixed arithmetic - set 05
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 42 + 8 * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
66
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 043. Explicit arithmetic grouping - set 05
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (42 + 8) * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
150
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 044. True division - set 05
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 42 / 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5.25
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 045. Floor division - set 05
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 42 // 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 046. Modulo remainder - set 05
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 42 % 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 047. Exponentiation - set 05
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 3 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
27
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 048. Comparison - set 05
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 42 > 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 049. Logical comparison - set 05
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (42 > 8) and (8 > 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 050. Membership - set 05
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 8 in [42, 8, 3]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 051. Arithmetic addition - set 06
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 50 + 9
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
59
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 052. Mixed arithmetic - set 06
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 50 + 9 * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
95
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 053. Explicit arithmetic grouping - set 06
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (50 + 9) * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
295
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 054. True division - set 06
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 50 / 9
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5.555555555555555
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 055. Floor division - set 06
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 50 // 9
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 056. Modulo remainder - set 06
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 50 % 9
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 057. Exponentiation - set 06
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 5 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
125
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 058. Comparison - set 06
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 50 > 9
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 059. Logical comparison - set 06
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (50 > 9) and (9 > 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 060. Membership - set 06
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 9 in [50, 9, 5]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 061. Arithmetic addition - set 07
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 64 + 11
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
75
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 062. Mixed arithmetic - set 07
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 64 + 11 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
86
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 063. Explicit arithmetic grouping - set 07
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (64 + 11) * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
150
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 064. True division - set 07
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 64 / 11
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5.818181818181818
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 065. Floor division - set 07
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 64 // 11
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 066. Modulo remainder - set 07
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 64 % 11
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 067. Exponentiation - set 07
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 2 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 068. Comparison - set 07
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 64 > 11
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 069. Logical comparison - set 07
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (64 > 11) and (11 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 070. Membership - set 07
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 11 in [64, 11, 2]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 071. Arithmetic addition - set 08
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 75 + 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
83
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 072. Mixed arithmetic - set 08
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 75 + 8 * 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
123
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 073. Explicit arithmetic grouping - set 08
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (75 + 8) * 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
498
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 074. True division - set 08
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 75 / 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9.375
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 075. Floor division - set 08
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 75 // 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 076. Modulo remainder - set 08
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 75 % 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 077. Exponentiation - set 08
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 6 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
216
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 078. Comparison - set 08
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 75 > 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 079. Logical comparison - set 08
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (75 > 8) and (8 > 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 080. Membership - set 08
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 8 in [75, 8, 6]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 081. Arithmetic addition - set 09
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 90 + 10
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
100
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 082. Mixed arithmetic - set 09
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 90 + 10 * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
130
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 083. Explicit arithmetic grouping - set 09
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (90 + 10) * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
400
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 084. True division - set 09
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 90 / 10
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9.0
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 085. Floor division - set 09
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 90 // 10
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 086. Modulo remainder - set 09
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 90 % 10
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
0
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 087. Exponentiation - set 09
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 4 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
64
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 088. Comparison - set 09
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 90 > 10
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 089. Logical comparison - set 09
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (90 > 10) and (10 > 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 090. Membership - set 09
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 10 in [90, 10, 4]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 091. Arithmetic addition - set 10
**Learning focus:** Addition combines two integers.
**Python code:**
```python
result = 100 + 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
112
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the left operand and right operand.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 092. Mixed arithmetic - set 10
**Learning focus:** Multiplication has higher precedence than addition.
**Python code:**
```python
result = 100 + 12 * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
160
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the second and third values before adding the first.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 093. Explicit arithmetic grouping - set 10
**Learning focus:** Parentheses group the addition before multiplication.
**Python code:**
```python
result = (100 + 12) * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
560
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add the first two values, then multiply by the third.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 094. True division - set 10
**Learning focus:** True division returns a floating-point quotient.
**Python code:**
```python
result = 100 / 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8.333333333333334
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 095. Floor division - set 10
**Learning focus:** Floor division rounds the quotient down.
**Python code:**
```python
result = 100 // 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the mathematical floor of the quotient.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 096. Modulo remainder - set 10
**Learning focus:** Modulo returns the remainder.
**Python code:**
```python
result = 100 % 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide the first value by the second and retain the remainder.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 097. Exponentiation - set 10
**Learning focus:** Exponentiation raises a base to a power.
**Python code:**
```python
result = 5 ** 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
125
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply the base by itself three times.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 098. Comparison - set 10
**Learning focus:** A comparison produces a Boolean.
**Python code:**
```python
result = 100 > 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the first value is greater than the second.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 099. Logical comparison - set 10
**Learning focus:** AND combines the two comparison results.
**Python code:**
```python
result = (100 > 12) and (12 > 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 100. Membership - set 10
**Learning focus:** Membership checks whether an item occurs in a collection.
**Python code:**
```python
result = 12 in [100, 12, 5]
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Check whether the second value is one of the list items.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

# 02 - Operator Precedence
Precedence determines the default grouping of operators that have different precedence levels.

## 100 worked cards - 02 - Operator Precedence
Each card uses a different sample set. Read the expression, predict the result, run it, inspect its type, and then change one input to see how the result changes.

### 001. Multiplication before addition - set 01
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 12 + 5 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
22
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 002. Power before multiplication - set 01
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 12 * 2 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
48
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 003. Addition before shift - set 01
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 12 + 5 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
34
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 004. Bitwise AND before XOR - set 01
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 12 ^ 5 & 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
12
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 005. Bitwise XOR before OR - set 01
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 12 | 5 ^ 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
15
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 006. Comparison before NOT - set 01
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (12 == 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 007. AND before OR - set 01
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (12 > 5) and (5 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 008. Arithmetic before comparison - set 01
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 12 + 5 * 2 > 17
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 009. Function call before addition - set 01
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 2 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
10
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 010. Indexing before addition - set 01
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [12, 5, 2][1] + 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
7
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 011. Multiplication before addition - set 02
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 18 + 4 * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
30
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 012. Power before multiplication - set 02
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 18 * 3 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
162
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 013. Addition before shift - set 02
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 18 + 4 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
44
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 014. Bitwise AND before XOR - set 02
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 18 ^ 4 & 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
18
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 015. Bitwise XOR before OR - set 02
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 18 | 4 ^ 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
23
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 016. Comparison before NOT - set 02
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (18 == 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 017. AND before OR - set 02
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (18 > 4) and (4 > 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 018. Arithmetic before comparison - set 02
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 18 + 4 * 3 > 22
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 019. Function call before addition - set 02
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 3 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
12
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 020. Indexing before addition - set 02
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [18, 4, 3][1] + 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
7
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 021. Multiplication before addition - set 03
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 25 + 6 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
37
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 022. Power before multiplication - set 03
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 25 * 2 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
100
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 023. Addition before shift - set 03
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 25 + 6 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
62
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 024. Bitwise AND before XOR - set 03
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 25 ^ 6 & 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
27
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 025. Bitwise XOR before OR - set 03
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 25 | 6 ^ 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
29
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 026. Comparison before NOT - set 03
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (25 == 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 027. AND before OR - set 03
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (25 > 6) and (6 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 028. Arithmetic before comparison - set 03
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 25 + 6 * 2 > 31
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 029. Function call before addition - set 03
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 2 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
10
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 030. Indexing before addition - set 03
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [25, 6, 2][1] + 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 031. Multiplication before addition - set 04
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 31 + 7 * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
59
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 032. Power before multiplication - set 04
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 31 * 4 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
496
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 033. Addition before shift - set 04
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 31 + 7 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
76
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 034. Bitwise AND before XOR - set 04
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 31 ^ 7 & 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
27
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 035. Bitwise XOR before OR - set 04
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 31 | 7 ^ 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 036. Comparison before NOT - set 04
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (31 == 7)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 037. AND before OR - set 04
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (31 > 7) and (7 > 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 038. Arithmetic before comparison - set 04
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 31 + 7 * 4 > 38
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 039. Function call before addition - set 04
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 4 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
14
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 040. Indexing before addition - set 04
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [31, 7, 4][1] + 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
11
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 041. Multiplication before addition - set 05
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 42 + 8 * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
66
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 042. Power before multiplication - set 05
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 42 * 3 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
378
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 043. Addition before shift - set 05
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 42 + 8 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
100
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 044. Bitwise AND before XOR - set 05
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 42 ^ 8 & 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
42
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 045. Bitwise XOR before OR - set 05
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 42 | 8 ^ 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
43
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 046. Comparison before NOT - set 05
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (42 == 8)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 047. AND before OR - set 05
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (42 > 8) and (8 > 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 048. Arithmetic before comparison - set 05
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 42 + 8 * 3 > 50
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 049. Function call before addition - set 05
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 3 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
12
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 050. Indexing before addition - set 05
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [42, 8, 3][1] + 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
11
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 051. Multiplication before addition - set 06
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 50 + 9 * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
95
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 052. Power before multiplication - set 06
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 50 * 5 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1250
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 053. Addition before shift - set 06
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 50 + 9 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
118
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 054. Bitwise AND before XOR - set 06
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 50 ^ 9 & 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
51
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 055. Bitwise XOR before OR - set 06
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 50 | 9 ^ 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
62
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 056. Comparison before NOT - set 06
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (50 == 9)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 057. AND before OR - set 06
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (50 > 9) and (9 > 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 058. Arithmetic before comparison - set 06
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 50 + 9 * 5 > 59
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 059. Function call before addition - set 06
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 5 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 060. Indexing before addition - set 06
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [50, 9, 5][1] + 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
14
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 061. Multiplication before addition - set 07
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 64 + 11 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
86
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 062. Power before multiplication - set 07
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 64 * 2 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
256
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 063. Addition before shift - set 07
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 64 + 11 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
150
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 064. Bitwise AND before XOR - set 07
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 64 ^ 11 & 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
66
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 065. Bitwise XOR before OR - set 07
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 64 | 11 ^ 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
73
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 066. Comparison before NOT - set 07
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (64 == 11)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 067. AND before OR - set 07
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (64 > 11) and (11 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 068. Arithmetic before comparison - set 07
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 64 + 11 * 2 > 75
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 069. Function call before addition - set 07
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 2 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
10
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 070. Indexing before addition - set 07
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [64, 11, 2][1] + 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
13
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 071. Multiplication before addition - set 08
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 75 + 8 * 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
123
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 072. Power before multiplication - set 08
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 75 * 6 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2700
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 073. Addition before shift - set 08
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 75 + 8 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
166
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 074. Bitwise AND before XOR - set 08
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 75 ^ 8 & 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
75
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 075. Bitwise XOR before OR - set 08
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 75 | 8 ^ 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
79
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 076. Comparison before NOT - set 08
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (75 == 8)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 077. AND before OR - set 08
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (75 > 8) and (8 > 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 078. Arithmetic before comparison - set 08
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 75 + 8 * 6 > 83
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 079. Function call before addition - set 08
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 6 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
18
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 080. Indexing before addition - set 08
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [75, 8, 6][1] + 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
14
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 081. Multiplication before addition - set 09
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 90 + 10 * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
130
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 082. Power before multiplication - set 09
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 90 * 4 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1440
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 083. Addition before shift - set 09
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 90 + 10 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
200
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 084. Bitwise AND before XOR - set 09
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 90 ^ 10 & 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
90
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 085. Bitwise XOR before OR - set 09
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 90 | 10 ^ 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
94
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 086. Comparison before NOT - set 09
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (90 == 10)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 087. AND before OR - set 09
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (90 > 10) and (10 > 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 088. Arithmetic before comparison - set 09
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 90 + 10 * 4 > 100
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 089. Function call before addition - set 09
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 4 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
14
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 090. Indexing before addition - set 09
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [90, 10, 4][1] + 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
14
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 091. Multiplication before addition - set 10
**Learning focus:** Multiplication binds more tightly than addition.
**Python code:**
```python
result = 100 + 12 * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
160
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b*c before adding a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 092. Power before multiplication - set 10
**Learning focus:** Exponentiation binds more tightly than multiplication.
**Python code:**
```python
result = 100 * 5 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2500
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then multiply by a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 093. Addition before shift - set 10
**Learning focus:** Addition binds more tightly than shifting.
**Python code:**
```python
result = 100 + 12 << 1
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
224
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then shift the sum left once.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 094. Bitwise AND before XOR - set 10
**Learning focus:** Bitwise AND binds more tightly than XOR.
**Python code:**
```python
result = 100 ^ 12 & 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
96
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b&c before applying XOR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 095. Bitwise XOR before OR - set 10
**Learning focus:** Bitwise XOR binds more tightly than bitwise OR.
**Python code:**
```python
result = 100 | 12 ^ 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
109
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate b^c before OR with a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 096. Comparison before NOT - set 10
**Learning focus:** The comparison is evaluated before NOT.
**Python code:**
```python
result = not (100 == 12)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Compare the values, then reverse the Boolean result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 097. AND before OR - set 10
**Learning focus:** AND binds more tightly than OR.
**Python code:**
```python
result = False or (100 > 12) and (12 > 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the AND group before the OR operation.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 098. Arithmetic before comparison - set 10
**Learning focus:** Arithmetic is completed before comparison.
**Python code:**
```python
result = 100 + 12 * 5 > 112
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Calculate both numeric sides, then compare.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 099. Function call before addition - set 10
**Learning focus:** Function calls and multiplication are evaluated before the addition.
**Python code:**
```python
result = len("Python") + 5 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Find the string length and product, then add them.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 100. Indexing before addition - set 10
**Learning focus:** Subscription selects the item before addition.
**Python code:**
```python
result = [100, 12, 5][1] + 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
17
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Select the second list item and add c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

# 03 - Operator Associativity
Associativity determines the grouping direction for equal-precedence operator chains, with special rules such as exponentiation and comparison chaining.

## 100 worked cards - 03 - Operator Associativity
Each card uses a different sample set. Read the expression, predict the result, run it, inspect its type, and then change one input to see how the result changes.

### 001. Subtraction chain - set 01
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 12 - 5 - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 002. Division chain - set 01
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 12 / 5 / 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.2
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 003. Floor division chain - set 01
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 12 // 5 // 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 004. Modulo chain - set 01
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 12 % 5 % 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
0
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 005. Multiplication and division - set 01
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 12 / 5 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4.8
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 006. Addition and subtraction - set 01
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 12 + 5 - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
15
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 007. Exponentiation chain - set 01
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 4 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
65536
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 008. Shift chain - set 01
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 2 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 009. Logical AND chain - set 01
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 12 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 010. Chained comparison - set 01
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 2 < 5 < 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 011. Subtraction chain - set 02
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 18 - 4 - 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
11
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 012. Division chain - set 02
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 18 / 4 / 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 013. Floor division chain - set 02
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 18 // 4 // 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 014. Modulo chain - set 02
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 18 % 4 % 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 015. Multiplication and division - set 02
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 18 / 4 * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
13.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 016. Addition and subtraction - set 02
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 18 + 4 - 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
19
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 017. Exponentiation chain - set 02
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 3 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
512
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 018. Shift chain - set 02
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 3 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
24
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 019. Logical AND chain - set 02
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 18 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 020. Chained comparison - set 02
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 3 < 4 < 18
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 021. Subtraction chain - set 03
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 25 - 6 - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
17
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 022. Division chain - set 03
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 25 / 6 / 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2.0833333333333335
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 023. Floor division chain - set 03
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 25 // 6 // 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 024. Modulo chain - set 03
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 25 % 6 % 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 025. Multiplication and division - set 03
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 25 / 6 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8.333333333333334
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 026. Addition and subtraction - set 03
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 25 + 6 - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
29
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 027. Exponentiation chain - set 03
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 2 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 028. Shift chain - set 03
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 2 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 029. Logical AND chain - set 03
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 25 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 030. Chained comparison - set 03
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 2 < 6 < 25
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 031. Subtraction chain - set 04
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 31 - 7 - 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
20
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 032. Division chain - set 04
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 31 / 7 / 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.1071428571428572
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 033. Floor division chain - set 04
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 31 // 7 // 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 034. Modulo chain - set 04
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 31 % 7 % 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 035. Multiplication and division - set 04
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 31 / 7 * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
17.714285714285715
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 036. Addition and subtraction - set 04
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 31 + 7 - 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
34
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 037. Exponentiation chain - set 04
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 3 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
512
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 038. Shift chain - set 04
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 4 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
32
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 039. Logical AND chain - set 04
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 31 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 040. Chained comparison - set 04
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 4 < 7 < 31
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 041. Subtraction chain - set 05
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 42 - 8 - 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 042. Division chain - set 05
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 42 / 8 / 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.75
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 043. Floor division chain - set 05
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 42 // 8 // 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 044. Modulo chain - set 05
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 42 % 8 % 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 045. Multiplication and division - set 05
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 42 / 8 * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
15.75
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 046. Addition and subtraction - set 05
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 42 + 8 - 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
47
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 047. Exponentiation chain - set 05
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 4 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
65536
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 048. Shift chain - set 05
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 3 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
24
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 049. Logical AND chain - set 05
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 42 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 050. Chained comparison - set 05
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 3 < 8 < 42
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 051. Subtraction chain - set 06
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 50 - 9 - 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
36
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 052. Division chain - set 06
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 50 / 9 / 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.1111111111111112
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 053. Floor division chain - set 06
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 50 // 9 // 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 054. Modulo chain - set 06
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 50 % 9 % 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
0
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 055. Multiplication and division - set 06
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 50 / 9 * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
27.77777777777778
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 056. Addition and subtraction - set 06
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 50 + 9 - 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
54
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 057. Exponentiation chain - set 06
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 2 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 058. Shift chain - set 06
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 5 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
40
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 059. Logical AND chain - set 06
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 50 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 060. Chained comparison - set 06
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 5 < 9 < 50
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 061. Subtraction chain - set 07
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 64 - 11 - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
51
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 062. Division chain - set 07
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 64 / 11 / 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2.909090909090909
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 063. Floor division chain - set 07
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 64 // 11 // 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 064. Modulo chain - set 07
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 64 % 11 % 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 065. Multiplication and division - set 07
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 64 / 11 * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
11.636363636363637
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 066. Addition and subtraction - set 07
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 64 + 11 - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
73
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 067. Exponentiation chain - set 07
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 4 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
65536
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 068. Shift chain - set 07
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 2 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 069. Logical AND chain - set 07
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 64 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 070. Chained comparison - set 07
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 2 < 11 < 64
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 071. Subtraction chain - set 08
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 75 - 8 - 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
61
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 072. Division chain - set 08
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 75 / 8 / 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.5625
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 073. Floor division chain - set 08
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 75 // 8 // 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 074. Modulo chain - set 08
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 75 % 8 % 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 075. Multiplication and division - set 08
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 75 / 8 * 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
56.25
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 076. Addition and subtraction - set 08
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 75 + 8 - 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
77
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 077. Exponentiation chain - set 08
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 4 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
65536
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 078. Shift chain - set 08
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 6 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
48
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 079. Logical AND chain - set 08
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 75 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 080. Chained comparison - set 08
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 6 < 8 < 75
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 081. Subtraction chain - set 09
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 90 - 10 - 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
76
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 082. Division chain - set 09
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 90 / 10 / 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2.25
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 083. Floor division chain - set 09
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 90 // 10 // 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 084. Modulo chain - set 09
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 90 % 10 % 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
0
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 085. Multiplication and division - set 09
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 90 / 10 * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
36.0
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 086. Addition and subtraction - set 09
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 90 + 10 - 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
96
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 087. Exponentiation chain - set 09
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 3 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
512
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 088. Shift chain - set 09
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 4 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
32
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 089. Logical AND chain - set 09
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 90 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 090. Chained comparison - set 09
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 4 < 10 < 90
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 091. Subtraction chain - set 10
**Learning focus:** Subtraction is left-associative.
**Python code:**
```python
result = 100 - 12 - 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
83
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a-b)-c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 092. Division chain - set 10
**Learning focus:** Division is left-associative.
**Python code:**
```python
result = 100 / 12 / 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.6666666666666667
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a/b)/c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 093. Floor division chain - set 10
**Learning focus:** Floor division is left-associative.
**Python code:**
```python
result = 100 // 12 // 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a//b)//c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 094. Modulo chain - set 10
**Learning focus:** Modulo is left-associative.
**Python code:**
```python
result = 100 % 12 % 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as (a%b)%c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 095. Multiplication and division - set 10
**Learning focus:** Division and multiplication share precedence and group left-to-right.
**Python code:**
```python
result = 100 / 12 * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
41.66666666666667
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Divide first, then multiply.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 096. Addition and subtraction - set 10
**Learning focus:** Addition and subtraction share precedence and group left-to-right.
**Python code:**
```python
result = 100 + 12 - 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
107
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add first, then subtract.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 097. Exponentiation chain - set 10
**Learning focus:** Exponentiation is right-associative.
**Python code:**
```python
result = 2 ** 2 ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Group as 2 ** (middle ** 2).
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 098. Shift chain - set 10
**Learning focus:** Shift operators group left-to-right.
**Python code:**
```python
result = 5 << 1 << 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
40
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Shift c once, then shift the result twice.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 099. Logical AND chain - set 10
**Learning focus:** AND returns the first falsy operand, or the final operand if all are truthy.
**Python code:**
```python
result = True and 100 and "ready"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'ready'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: All earlier operands are truthy, so the final string is returned.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 100. Chained comparison - set 10
**Learning focus:** A comparison chain checks both adjacent comparisons.
**Python code:**
```python
result = 5 < 12 < 100
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Both comparisons must be true.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

# 04 - Parentheses and Grouping
Parentheses force a particular grouping and make complex expressions easier to inspect.

## 100 worked cards - 04 - Parentheses and Grouping
Each card uses a different sample set. Read the expression, predict the result, run it, inspect its type, and then change one input to see how the result changes.

### 001. Addition grouped before multiplication - set 01
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (12 + 5) * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
34
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 002. Right-hand multiplication group - set 01
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 12 + (5 * 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
22
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 003. Left-grouped subtraction - set 01
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (12 - 5) - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 004. Right-grouped subtraction - set 01
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 12 - (5 - 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 005. Grouped denominator - set 01
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 12 / (5 + 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1.7142857142857142
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 006. Grouped numerator - set 01
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (12 + 5) / 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
8.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 007. Grouped power left - set 01
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (2 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 008. Grouped logical alternative - set 01
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (12 > 5) or (5 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 009. Negated logical group - set 01
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (12 < 5 or 5 < 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 010. Grouped bitwise test - set 01
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((12 & 5) == 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
False
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 011. Addition grouped before multiplication - set 02
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (18 + 4) * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
66
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 012. Right-hand multiplication group - set 02
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 18 + (4 * 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
30
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 013. Left-grouped subtraction - set 02
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (18 - 4) - 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
11
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 014. Right-grouped subtraction - set 02
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 18 - (4 - 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
17
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 015. Grouped denominator - set 02
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 18 / (4 + 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2.5714285714285716
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 016. Grouped numerator - set 02
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (18 + 4) / 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
7.333333333333333
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 017. Grouped power left - set 02
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (3 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
81
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 018. Grouped logical alternative - set 02
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (18 > 4) or (4 > 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 019. Negated logical group - set 02
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (18 < 4 or 4 < 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 020. Grouped bitwise test - set 02
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((18 & 4) == 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
False
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 021. Addition grouped before multiplication - set 03
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (25 + 6) * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
62
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 022. Right-hand multiplication group - set 03
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 25 + (6 * 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
37
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 023. Left-grouped subtraction - set 03
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (25 - 6) - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
17
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 024. Right-grouped subtraction - set 03
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 25 - (6 - 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
21
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 025. Grouped denominator - set 03
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 25 / (6 + 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3.125
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 026. Grouped numerator - set 03
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (25 + 6) / 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
15.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 027. Grouped power left - set 03
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (2 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 028. Grouped logical alternative - set 03
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (25 > 6) or (6 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 029. Negated logical group - set 03
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (25 < 6 or 6 < 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 030. Grouped bitwise test - set 03
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((25 & 6) == 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
False
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 031. Addition grouped before multiplication - set 04
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (31 + 7) * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
152
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 032. Right-hand multiplication group - set 04
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 31 + (7 * 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
59
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 033. Left-grouped subtraction - set 04
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (31 - 7) - 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
20
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 034. Right-grouped subtraction - set 04
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 31 - (7 - 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
28
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 035. Grouped denominator - set 04
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 31 / (7 + 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
2.8181818181818183
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 036. Grouped numerator - set 04
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (31 + 7) / 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
9.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 037. Grouped power left - set 04
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (4 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
256
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 038. Grouped logical alternative - set 04
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (31 > 7) or (7 > 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 039. Negated logical group - set 04
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (31 < 7 or 7 < 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 040. Grouped bitwise test - set 04
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((31 & 7) == 7)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 041. Addition grouped before multiplication - set 05
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (42 + 8) * 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
150
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 042. Right-hand multiplication group - set 05
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 42 + (8 * 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
66
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 043. Left-grouped subtraction - set 05
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (42 - 8) - 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 044. Right-grouped subtraction - set 05
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 42 - (8 - 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
37
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 045. Grouped denominator - set 05
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 42 / (8 + 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3.8181818181818183
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 046. Grouped numerator - set 05
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (42 + 8) / 3
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16.666666666666668
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 047. Grouped power left - set 05
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (3 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
81
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 048. Grouped logical alternative - set 05
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (42 > 8) or (8 > 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 049. Negated logical group - set 05
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (42 < 8 or 8 < 3)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 050. Grouped bitwise test - set 05
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((42 & 8) == 8)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 051. Addition grouped before multiplication - set 06
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (50 + 9) * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
295
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 052. Right-hand multiplication group - set 06
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 50 + (9 * 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
95
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 053. Left-grouped subtraction - set 06
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (50 - 9) - 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
36
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 054. Right-grouped subtraction - set 06
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 50 - (9 - 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
46
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 055. Grouped denominator - set 06
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 50 / (9 + 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
3.5714285714285716
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 056. Grouped numerator - set 06
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (50 + 9) / 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
11.8
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 057. Grouped power left - set 06
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (5 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
625
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 058. Grouped logical alternative - set 06
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (50 > 9) or (9 > 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 059. Negated logical group - set 06
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (50 < 9 or 9 < 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 060. Grouped bitwise test - set 06
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((50 & 9) == 9)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
False
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 061. Addition grouped before multiplication - set 07
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (64 + 11) * 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
150
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 062. Right-hand multiplication group - set 07
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 64 + (11 * 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
86
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 063. Left-grouped subtraction - set 07
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (64 - 11) - 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
51
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 064. Right-grouped subtraction - set 07
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 64 - (11 - 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
55
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 065. Grouped denominator - set 07
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 64 / (11 + 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
4.923076923076923
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 066. Grouped numerator - set 07
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (64 + 11) / 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
37.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 067. Grouped power left - set 07
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (2 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
16
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 068. Grouped logical alternative - set 07
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (64 > 11) or (11 > 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 069. Negated logical group - set 07
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (64 < 11 or 11 < 2)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 070. Grouped bitwise test - set 07
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((64 & 11) == 11)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
False
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 071. Addition grouped before multiplication - set 08
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (75 + 8) * 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
498
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 072. Right-hand multiplication group - set 08
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 75 + (8 * 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
123
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 073. Left-grouped subtraction - set 08
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (75 - 8) - 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
61
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 074. Right-grouped subtraction - set 08
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 75 - (8 - 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
73
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 075. Grouped denominator - set 08
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 75 / (8 + 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5.357142857142857
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 076. Grouped numerator - set 08
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (75 + 8) / 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
13.833333333333334
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 077. Grouped power left - set 08
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (6 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
1296
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 078. Grouped logical alternative - set 08
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (75 > 8) or (8 > 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 079. Negated logical group - set 08
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (75 < 8 or 8 < 6)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 080. Grouped bitwise test - set 08
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((75 & 8) == 8)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 081. Addition grouped before multiplication - set 09
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (90 + 10) * 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
400
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 082. Right-hand multiplication group - set 09
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 90 + (10 * 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
130
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 083. Left-grouped subtraction - set 09
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (90 - 10) - 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
76
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 084. Right-grouped subtraction - set 09
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 90 - (10 - 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
84
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 085. Grouped denominator - set 09
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 90 / (10 + 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
6.428571428571429
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 086. Grouped numerator - set 09
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (90 + 10) / 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
25.0
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 087. Grouped power left - set 09
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (4 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
256
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 088. Grouped logical alternative - set 09
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (90 > 10) or (10 > 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 089. Negated logical group - set 09
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (90 < 10 or 10 < 4)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 090. Grouped bitwise test - set 09
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((90 & 10) == 10)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 091. Addition grouped before multiplication - set 10
**Learning focus:** Parentheses force addition first.
**Python code:**
```python
result = (100 + 12) * 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
560
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then multiply by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 092. Right-hand multiplication group - set 10
**Learning focus:** Parentheses show the product as a group.
**Python code:**
```python
result = 100 + (12 * 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
160
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Multiply b and c, then add a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 093. Left-grouped subtraction - set 10
**Learning focus:** The left subtraction is evaluated first.
**Python code:**
```python
result = (100 - 12) - 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
83
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract b from a, then subtract c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 094. Right-grouped subtraction - set 10
**Learning focus:** The right subtraction is evaluated first.
**Python code:**
```python
result = 100 - (12 - 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
93
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Subtract c from b, then subtract the result from a.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 095. Grouped denominator - set 10
**Learning focus:** Parentheses group the complete denominator.
**Python code:**
```python
result = 100 / (12 + 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
5.882352941176471
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add b and c, then divide a by that sum.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 096. Grouped numerator - set 10
**Learning focus:** Parentheses group the complete numerator.
**Python code:**
```python
result = (100 + 12) / 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
22.4
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Add a and b, then divide by c.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 097. Grouped power left - set 10
**Learning focus:** Parentheses force the inner power first.
**Python code:**
```python
result = (5 ** 2) ** 2
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
625
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Square c, then square the result.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 098. Grouped logical alternative - set 10
**Learning focus:** Each comparison is grouped before OR.
**Python code:**
```python
result = (100 > 12) or (12 > 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate both comparisons and combine their truth values.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 099. Negated logical group - set 10
**Learning focus:** NOT applies to the complete OR group.
**Python code:**
```python
result = not (100 < 12 or 12 < 5)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
True
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Evaluate the OR expression, then reverse it.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 100. Grouped bitwise test - set 10
**Learning focus:** Parentheses group bitwise AND before equality.
**Python code:**
```python
result = ((100 & 12) == 12)
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
False
```
**Result type:** `bool`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: Apply the mask, then compare with b.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

# 05 - Conditional Expressions
Conditional expressions evaluate a condition and choose exactly one result branch.

## 100 worked cards - 05 - Conditional Expressions
Each card uses a different sample set. Read the expression, predict the result, run it, inspect its type, and then change one input to see how the result changes.

### 001. Even or odd - set 01
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 12 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 002. Positive or negative - set 01
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 12 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 003. Greater of two - set 01
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 12 if 12 > 5 else 5
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
12
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 004. Pass or fail - set 01
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 12 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Fail'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 005. Nested grade - set 01
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 12 >= 90 else "B" if 12 >= 75 else "C" if 12 >= 60 else "D" if 12 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'F'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 006. Discount selection - set 01
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 12 * 0.9 if 12 >= 50 else 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
12
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 007. Default string - set 01
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 008. None check - set 01
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 12 if 12 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
12
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 009. Boolean label - set 01
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (12 >= 5 and 5 >= 2) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 010. Membership label - set 01
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 5 in [12, 5, 2] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 011. Even or odd - set 02
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 18 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 012. Positive or negative - set 02
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 18 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 013. Greater of two - set 02
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 18 if 18 > 4 else 4
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
18
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 014. Pass or fail - set 02
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 18 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Fail'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 015. Nested grade - set 02
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 18 >= 90 else "B" if 18 >= 75 else "C" if 18 >= 60 else "D" if 18 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'F'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 016. Discount selection - set 02
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 18 * 0.9 if 18 >= 50 else 18
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
18
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 017. Default string - set 02
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 018. None check - set 02
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 18 if 18 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
18
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 019. Boolean label - set 02
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (18 >= 4 and 4 >= 3) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 020. Membership label - set 02
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 4 in [18, 4, 3] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 021. Even or odd - set 03
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 25 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Odd'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 022. Positive or negative - set 03
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 25 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 023. Greater of two - set 03
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 25 if 25 > 6 else 6
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
25
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 024. Pass or fail - set 03
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 25 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Fail'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 025. Nested grade - set 03
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 25 >= 90 else "B" if 25 >= 75 else "C" if 25 >= 60 else "D" if 25 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'F'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 026. Discount selection - set 03
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 25 * 0.9 if 25 >= 50 else 25
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
25
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 027. Default string - set 03
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 028. None check - set 03
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 25 if 25 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
25
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 029. Boolean label - set 03
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (25 >= 6 and 6 >= 2) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 030. Membership label - set 03
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 6 in [25, 6, 2] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 031. Even or odd - set 04
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 31 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Odd'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 032. Positive or negative - set 04
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 31 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 033. Greater of two - set 04
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 31 if 31 > 7 else 7
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 034. Pass or fail - set 04
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 31 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Fail'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 035. Nested grade - set 04
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 31 >= 90 else "B" if 31 >= 75 else "C" if 31 >= 60 else "D" if 31 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'F'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 036. Discount selection - set 04
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 31 * 0.9 if 31 >= 50 else 31
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 037. Default string - set 04
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 038. None check - set 04
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 31 if 31 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
31
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 039. Boolean label - set 04
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (31 >= 7 and 7 >= 4) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 040. Membership label - set 04
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 7 in [31, 7, 4] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 041. Even or odd - set 05
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 42 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 042. Positive or negative - set 05
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 42 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 043. Greater of two - set 05
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 42 if 42 > 8 else 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
42
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 044. Pass or fail - set 05
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 42 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Pass'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 045. Nested grade - set 05
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 42 >= 90 else "B" if 42 >= 75 else "C" if 42 >= 60 else "D" if 42 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'D'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 046. Discount selection - set 05
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 42 * 0.9 if 42 >= 50 else 42
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
42
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 047. Default string - set 05
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 048. None check - set 05
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 42 if 42 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
42
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 049. Boolean label - set 05
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (42 >= 8 and 8 >= 3) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 050. Membership label - set 05
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 8 in [42, 8, 3] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 051. Even or odd - set 06
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 50 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 052. Positive or negative - set 06
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 50 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 053. Greater of two - set 06
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 50 if 50 > 9 else 9
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
50
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 054. Pass or fail - set 06
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 50 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Pass'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 055. Nested grade - set 06
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 50 >= 90 else "B" if 50 >= 75 else "C" if 50 >= 60 else "D" if 50 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'D'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 056. Discount selection - set 06
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 50 * 0.9 if 50 >= 50 else 50
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
45.0
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 057. Default string - set 06
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 058. None check - set 06
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 50 if 50 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
50
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 059. Boolean label - set 06
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (50 >= 9 and 9 >= 5) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 060. Membership label - set 06
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 9 in [50, 9, 5] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 061. Even or odd - set 07
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 64 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 062. Positive or negative - set 07
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 64 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 063. Greater of two - set 07
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 64 if 64 > 11 else 11
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
64
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 064. Pass or fail - set 07
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 64 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Pass'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 065. Nested grade - set 07
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 64 >= 90 else "B" if 64 >= 75 else "C" if 64 >= 60 else "D" if 64 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'C'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 066. Discount selection - set 07
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 64 * 0.9 if 64 >= 50 else 64
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
57.6
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 067. Default string - set 07
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 068. None check - set 07
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 64 if 64 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
64
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 069. Boolean label - set 07
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (64 >= 11 and 11 >= 2) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 070. Membership label - set 07
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 11 in [64, 11, 2] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 071. Even or odd - set 08
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 75 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Odd'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 072. Positive or negative - set 08
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 75 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 073. Greater of two - set 08
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 75 if 75 > 8 else 8
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
75
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 074. Pass or fail - set 08
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 75 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Pass'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 075. Nested grade - set 08
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 75 >= 90 else "B" if 75 >= 75 else "C" if 75 >= 60 else "D" if 75 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'B'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 076. Discount selection - set 08
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 75 * 0.9 if 75 >= 50 else 75
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
67.5
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 077. Default string - set 08
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 078. None check - set 08
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 75 if 75 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
75
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 079. Boolean label - set 08
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (75 >= 8 and 8 >= 6) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 080. Membership label - set 08
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 8 in [75, 8, 6] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 081. Even or odd - set 09
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 90 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 082. Positive or negative - set 09
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 90 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 083. Greater of two - set 09
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 90 if 90 > 10 else 10
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
90
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 084. Pass or fail - set 09
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 90 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Pass'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 085. Nested grade - set 09
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 90 >= 90 else "B" if 90 >= 75 else "C" if 90 >= 60 else "D" if 90 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'A'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 086. Discount selection - set 09
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 90 * 0.9 if 90 >= 50 else 90
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
81.0
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 087. Default string - set 09
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 088. None check - set 09
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 90 if 90 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
90
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 089. Boolean label - set 09
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (90 >= 10 and 10 >= 4) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 090. Membership label - set 09
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 10 in [90, 10, 4] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 091. Even or odd - set 10
**Learning focus:** The condition checks the remainder after division by two.
**Python code:**
```python
result = "Even" if 100 % 2 == 0 else "Odd"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Even'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A zero remainder selects Even; otherwise Odd.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 092. Positive or negative - set 10
**Learning focus:** A comparison chooses one text value.
**Python code:**
```python
result = "Positive" if 100 > 0 else "Non-positive"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Positive'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true value is selected only when a is greater than zero.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 093. Greater of two - set 10
**Learning focus:** The comparison chooses one of two values.
**Python code:**
```python
result = 100 if 100 > 12 else 12
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
100
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first value is selected only when it is greater.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 094. Pass or fail - set 10
**Learning focus:** The expression tests a pass threshold.
**Python code:**
```python
result = "Pass" if 100 >= 40 else "Fail"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Pass'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The true branch is selected at or above 40.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 095. Nested grade - set 10
**Learning focus:** Nested conditions test thresholds from high to low.
**Python code:**
```python
result = "A" if 100 >= 90 else "B" if 100 >= 75 else "C" if 100 >= 60 else "D" if 100 >= 40 else "F"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'A'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The first matching threshold selects the grade.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 096. Discount selection - set 10
**Learning focus:** A discount calculation is selected only above a threshold.
**Python code:**
```python
result = 100 * 0.9 if 100 >= 50 else 100
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
90.0
```
**Result type:** `float`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: A value at least 50 is multiplied by 0.9.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 097. Default string - set 10
**Learning focus:** Non-empty strings are truthy.
**Python code:**
```python
result = "Python" if "Python" else "Guest"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Python'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The original non-empty string is selected.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 098. None check - set 10
**Learning focus:** The condition checks identity with None.
**Python code:**
```python
result = 100 if 100 is not None else 0
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
100
```
**Result type:** `int`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The numeric value is not None, so it is preserved.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 099. Boolean label - set 10
**Learning focus:** An AND group requires both comparisons.
**Python code:**
```python
result = "Eligible" if (100 >= 12 and 12 >= 5) else "Not eligible"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Eligible'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The label depends on both conditions.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

### 100. Membership label - set 10
**Learning focus:** Membership selects a label.
**Python code:**
```python
result = "Found" if 12 in [100, 12, 5] else "Missing"
print(result)
print(type(result).__name__)
```
**Expected value:**
```text
'Found'
```
**Result type:** `str`
**Dry-run instructions:**
- Identify the values and their types before evaluating the operation.
- Apply the relevant operator rule: The item b occurs in the list.
- Compare the interpreter result with your hand calculation.
**Variation:** Change one input value while keeping the expression structure the same. Predict the new result before running it.
**Self-check:** Can you explain the result without using the phrase “because Python says so”? Name the exact expression rule that applies.

# Part C - Integrated Expression Applications
The following scenarios combine two or more subtopics. In real programs, expressions are rarely isolated: a calculation can contain arithmetic, grouping, comparisons and a conditional selection at the same time.

## 01. Shopping bill
**Code:**
```python
price = 2000
discount = 0.10
tax = 0.05
final_price = (price * (1 - discount)) * (1 + tax)
print(final_price)
```
**Expected output:**
```text
1890.0
```
**Dry run:** The discount is applied first; tax is calculated on the discounted amount.
**Review point:** Use named intermediate variables if the billing policy becomes more complicated.

## 02. Student weighted score
**Code:**
```python
assignment = 80
midterm = 70
final_exam = 90
score = (assignment * 0.2) + (midterm * 0.3) + (final_exam * 0.5)
print(score)
```
**Expected output:**
```text
82.0
```
**Dry run:** The weighted components are 16, 21 and 45. Their sum is 82.
**Review point:** The weights should add to 1.0 when they represent 100 percent.

## 03. Eligibility decision
**Code:**
```python
age = 19
has_id = True
member = False
allowed = (age >= 18 and has_id) or member
print("Allowed" if allowed else "Denied")
```
**Expected output:**
```text
Allowed
```
**Dry run:** The first group is true because the age condition and ID condition are both true.
**Review point:** Write policy requirements in named Boolean variables before nesting many conditions.

## 04. Binary search midpoint
**Code:**
```python
left = 2
right = 8
mid = left + ((right - left) // 2)
print(mid)
```
**Expected output:**
```text
5
```
**Dry run:** right-left is 6; 6//2 is 3; left+3 is 5.
**Review point:** The search algorithm must maintain a valid left/right range.

## 05. Array index validation
**Code:**
```python
index = 3
size = 5
valid = 0 <= index < size
print("Valid" if valid else "Invalid")
```
**Expected output:**
```text
Valid
```
**Dry run:** Both comparisons in the chain are true.
**Review point:** The upper index bound is exclusive.

## 06. Safe dictionary fallback
**Code:**
```python
record = {"name": "Amaan"}
name = record.get("name")
label = name if name is not None else "Guest"
print(label)
```
**Expected output:**
```text
Amaan
```
**Dry run:** The dictionary lookup returns a non-None value, so the conditional keeps it.
**Review point:** An empty string is not the same as a missing None value.

## 07. Filter even values
**Code:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```
**Expected output:**
```text
[2, 4, 6]
```
**Dry run:** The comprehension filter includes only values whose remainder is zero.
**Review point:** A comprehension filter removes items that do not pass the condition.

## 08. Label every number
**Code:**
```python
numbers = [1, 2, 3, 4]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)
```
**Expected output:**
```text
['Odd', 'Even', 'Odd', 'Even']
```
**Dry run:** The conditional expression selects one label for each number.
**Review point:** A conditional expression inside a comprehension maps every input item to an output.

## 09. Bit-mask check
**Code:**
```python
value = 13
mask = 5
all_set = (value & mask) == mask
print(all_set)
```
**Expected output:**
```text
True
```
**Dry run:** 13 is 1101 and 5 is 0101 in binary. The AND result is 0101, which equals the mask.
**Review point:** Parenthesize the bitwise operation before comparing it with the mask.

## 10. Leap year
**Code:**
```python
year = 2100
leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
print("Leap" if leap else "Common")
```
**Expected output:**
```text
Common
```
**Dry run:** 2100 is not divisible by 400 and is divisible by 100, so the rule returns false.
**Review point:** Group the AND condition to make the calendar rule easier to audit.

## 11. Temperature conversion
**Code:**
```python
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(fahrenheit)
```
**Expected output:**
```text
77.0
```
**Dry run:** 25*9 is 225; 225/5 is 45.0; 45.0+32 is 77.0.
**Review point:** Use parentheses to make the formula components visible.

## 12. Rectangle dimensions
**Code:**
```python
length = 8
width = 5
area = length * width
perimeter = 2 * (length + width)
print(area, perimeter)
```
**Expected output:**
```text
40 26
```
**Dry run:** Area is 40. The grouped sum is 13 and perimeter is 26.
**Review point:** The perimeter formula requires grouping the sum of the sides.

## 13. Time conversion
**Code:**
```python
hours = 2
minutes = 35
seconds = (hours * 3600) + (minutes * 60)
print(seconds)
```
**Expected output:**
```text
9300
```
**Dry run:** Two hours are 7200 seconds; 35 minutes are 2100 seconds; the total is 9300.
**Review point:** Separate conversions make unit reasoning clearer.

## 14. Absolute difference
**Code:**
```python
a = 17
b = 9
difference = abs(a - b)
print(difference)
```
**Expected output:**
```text
8
```
**Dry run:** 17-9 is 8; abs preserves the non-negative magnitude.
**Review point:** Use abs when the requirement is distance or magnitude rather than signed difference.

## 15. Shipping fee
**Code:**
```python
order_amount = 1200
fee = 0 if order_amount >= 1000 else 50
print(fee)
```
**Expected output:**
```text
0
```
**Dry run:** The threshold comparison is true, so the zero-fee branch is selected.
**Review point:** A simple conditional expression is suitable for one value selection.

## 16. Password length
**Code:**
```python
password = "python123"
valid = len(password) >= 8
print("Valid" if valid else "Too short")
```
**Expected output:**
```text
Valid
```
**Dry run:** The length is 9, so the comparison is true.
**Review point:** A comparison can be stored in a named Boolean and reused.

## 17. Required validation flags
**Code:**
```python
email_ok = True
phone_ok = False
identity_ok = True
complete = email_ok and phone_ok and identity_ok
print(complete)
```
**Expected output:**
```text
False
```
**Dry run:** The phone flag is false, so the AND expression returns a falsy operand.
**Review point:** AND is appropriate when all required checks must pass.

## 18. Alternative contact methods
**Code:**
```python
email_ok = False
phone_ok = True
contactable = email_ok or phone_ok
print(contactable)
```
**Expected output:**
```text
True
```
**Dry run:** Email is false, but phone is true, so OR returns true.
**Review point:** OR is appropriate when any one option is sufficient.

## 19. Display fallback
**Code:**
```python
name = ""
display = (name if name else "Guest").title()
print(display)
```
**Expected output:**
```text
Guest
```
**Dry run:** The empty name is falsy; Guest is selected and title() returns Guest.
**Review point:** Group a conditional expression before chaining a method call.

## 20. Conditional function return
**Code:**
```python
def classify(n):
    return "positive" if n > 0 else "zero or negative"
print(classify(-2))
```
**Expected output:**
```text
zero or negative
```
**Dry run:** The function receives -2 and the condition is false.
**Review point:** Conditional expressions can be useful in concise return statements.

# Part D - Solved Problem Planning Guide
The five topic programs contain interactive examples and solved problems. Use these plans to understand the problem-solving process before running the complete code.

## 01 - Expressions
### 01. Add two user-entered values.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 02. Calculate the average of three or more marks.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 03. Calculate rectangle area from length and width.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 04. Calculate rectangle perimeter using a grouped sum.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 05. Convert Celsius to Fahrenheit.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 06. Calculate simple interest using principal, rate and time.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 07. Calculate a discount amount from a percentage.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 08. Calculate tax on a taxable amount.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 09. Convert hours and minutes into seconds.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 10. Select Pass or Fail using a score threshold.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 11. Check whether normalized text is a palindrome.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 12. Create a formatted sentence from variables.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

## 02 - Operator Precedence
### 01. Evaluate multiplication before addition.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 02. Group a calculation with parentheses and compare outputs.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 03. Combine true division with subtraction.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 04. Evaluate a power before multiplication.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 05. Explain unary minus with exponentiation.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 06. Evaluate a shift after arithmetic addition.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 07. Evaluate bitwise AND, XOR and OR in precedence order.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 08. Combine comparisons with logical operators.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 09. Use NOT with a membership expression.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 10. Evaluate a conditional expression with a comparison test.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 11. Use indexing before arithmetic.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 12. Use a function call as a comparison operand.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

## 03 - Operator Associativity
### 01. Trace subtraction from left to right.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 02. Trace division from left to right.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 03. Trace floor division and modulo chains.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 04. Compare addition/subtraction grouping.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 05. Trace exponentiation from right to left.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 06. Compare left- and right-grouped powers.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 07. Trace left-shift chains.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 08. Trace bitwise operator chains.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 09. Use chained comparisons for a range.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 10. Trace nested conditional expressions.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 11. Explain short-circuit behavior in logical chains.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 12. Distinguish tuple syntax from arithmetic associativity.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

## 04 - Parentheses and Grouping
### 01. Override precedence with parentheses.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 02. Evaluate nested arithmetic from inside outward.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 03. Calculate an average using a grouped numerator.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 04. Compare left- and right-grouped subtraction.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 05. Compare left- and right-grouped division.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 06. Group exponentiation explicitly.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 07. Group alternative logical requirements.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 08. Apply De Morgan’s laws to a grouped condition.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 09. Group a bitwise mask calculation before comparison.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 10. Distinguish a one-element tuple from a parenthesized integer.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 11. Use function-call parentheses correctly.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 12. Split a long formula into named components.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

## 05 - Conditional Expressions
### 01. Select Even or Odd.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 02. Classify a value as positive, negative or zero.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 03. Find the greater of two values.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 04. Find the largest of three values.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 05. Select Pass or Fail.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 06. Choose an Adult or Minor label.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 07. Calculate a price with a conditional discount.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 08. Select a delivery charge.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 09. Assign a grade using nested conditional expressions.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 10. Select a leap-year label.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 11. Choose a fallback name.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

### 12. Preserve zero by checking explicitly for None.
**Step 1 - Understand the requirement:** Write down the input values, the expected output and the rule that connects them.
**Step 2 - Identify the expression family:** Decide whether the solution needs arithmetic, comparison, logical, bitwise, membership, identity, grouping or conditional selection.
**Step 3 - Draft the expression:** Keep the first version simple. Add parentheses where they clarify the intended grouping.
**Step 4 - Dry run:** Substitute the sample values and calculate each intermediate result.
**Step 5 - Validate:** Test a typical case, a boundary case and an edge case.
**Step 6 - Refactor:** If the expression becomes difficult to read, give meaningful names to intermediate results.

# Part E - Practice Workbook: 250 Questions
Complete each task in your own Python file or notebook. For every expression question, record the expected output before executing the code. For validation questions, test a normal input, a boundary input and an invalid or unusual input.

## Practice bank - 01 - Expressions
For every question: write the code, predict the output, execute it, explain the result and test one boundary or edge case.
**01. Add two numeric inputs and print the sum.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**02. Find the difference between two numbers.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**03. Calculate the product of three integers.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**04. Calculate a true-division quotient.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**05. Find the number of complete groups of six using floor division.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**06. Find the remainder after division by seven.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**07. Calculate the square and cube of a value.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**08. Calculate the average of four subject marks.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**09. Calculate a percentage from obtained and maximum marks.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**10. Convert seconds into whole minutes and remaining seconds.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**11. Join first and last names with a space.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**12. Repeat a separator string ten times.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**13. Find the length of a user-entered sentence.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**14. Extract the first character of a non-empty string.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**15. Extract the last three characters of a filename.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**16. Check whether a word occurs in a sentence.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**17. Check whether an item is present in a list.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**18. Check whether a key exists in a dictionary.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**19. Find the maximum of three values.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**20. Find the minimum of four values.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**21. Round a float for display.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**22. Convert numeric text to an integer before addition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**23. Compare two values for equality.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**24. Compare a score against a passing threshold.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**25. Use AND to require two conditions.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**26. Use OR when either contact method is available.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**27. Use NOT to reverse a Boolean variable.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**28. Use a chained comparison for a valid score range.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**29. Check whether a value is None.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**30. Select a status label with a conditional expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**31. Use a list expression to select each pair’s second element.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**32. Slice a string to obtain every second character.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**33. Concatenate two lists without mutating them.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**34. Repeat a list containing an immutable value.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**35. Use sum() to total a list.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**36. Use all() to check all validation flags.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**37. Use any() to check at least one validation flag.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**38. Use sorted() to create an ordered copy.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**39. Use dict.get() with a fallback.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**40. Use set membership to check a permission.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**41. Combine sets using union.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**42. Use abs() to calculate magnitude.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**43. Use round() before presenting a score.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**44. Call a function inside a larger expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**45. Use a comprehension to square every number.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**46. Use a conditional expression to label numbers.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**47. Use a dictionary comprehension to map values to squares.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**48. Use a walrus expression to capture a string length.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**49. Read the second coordinate from a tuple.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**50. Check whether a list contains at least three items.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

## Practice bank - 02 - Operator Precedence
For every question: write the code, predict the output, execute it, explain the result and test one boundary or edge case.
**01. Evaluate 8 + 4 * 3 and explain the order.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**02. Add parentheses so addition occurs before multiplication.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**03. Evaluate 40 - 18 / 3 and state the result type.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**04. Evaluate 2 + 3 ** 2 * 4.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**05. Explain the difference between -5 ** 2 and (-5) ** 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**06. Evaluate 24 // 5 + 2 * 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**07. Evaluate 31 % 6 * 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**08. Evaluate 1 + 2 << 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**09. Evaluate 12 & 10 ^ 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**10. Evaluate 12 | 10 ^ 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**11. Evaluate not 5 > 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**12. Evaluate True or False and False.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**13. Add parentheses to make the preceding expression False.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**14. Evaluate 3 < 5 == 5.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**15. Evaluate 4 in [1, 4, 9] and 9 > 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**16. Evaluate not "x" in "example".**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**17. Compare 6 * 2 + 1 with 6 * (2 + 1).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**18. Compare 100 / 5 * 2 with 100 / (5 * 2).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**19. Explain len("Python") + 2 * 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**20. Evaluate [10, 20, 30][1] + 5.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**21. Evaluate 2 ** 3 ** 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**22. Combine comparison, AND and OR in one condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**23. Parenthesize a bitwise comparison.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**24. Evaluate 10 >= 5 and 4 != 4 or True.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**25. Evaluate not False or False and False.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**26. Explain why comparison binds more tightly than NOT.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**27. Use a comparison and AND in a conditional expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**28. Use a shift expression as one side of a comparison.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**29. Multiply values before applying bitwise AND.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**30. Explain call syntax in len(text) * 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**31. Evaluate 25 // 4 * 2 + 1.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**32. Add parentheses to a weighted sum.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**33. Evaluate 8 + 12 / 4 - 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**34. Evaluate 2 * 3 ** 2 + 4.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**35. Evaluate 5 ^ 2 & 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**36. Explain a < b < c.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**37. Write an expression with indexing and addition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**38. Write an expression with a function call and comparison.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**39. Explain precedence and associativity with one example.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**40. Negate a complete OR expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**41. Group a denominator containing a sum.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**42. Select a computed value with a conditional expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**43. Explain why multiplication is grouped before addition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**44. Compare a | b ^ c with (a | b) ^ c.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**45. Compare a & b == c with (a & b) == c.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**46. Validate a percentage with a chained comparison.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**47. Group an account eligibility condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**48. Explain AND and OR precedence with a truth table.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**49. Trace an expression containing five precedence levels.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**50. Refactor a long expression into named variables.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

## Practice bank - 03 - Operator Associativity
For every question: write the code, predict the output, execute it, explain the result and test one boundary or edge case.
**01. Group 50 - 20 - 5.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**02. Compare (50 - 20) - 5 with 50 - (20 - 5).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**03. Group 120 / 6 / 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**04. Compare (120 / 6) / 2 with 120 / (6 / 2).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**05. Group 100 // 7 // 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**06. Group 47 % 10 % 4.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**07. Explain 48 / 6 * 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**08. Explain 18 + 4 - 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**09. Evaluate 3 ** 2 ** 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**10. Compare (3 ** 2) ** 2 with 3 ** (2 ** 2).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**11. Explain why 2 ** 3 ** 2 is right-grouped.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**12. Compare -4 ** 2 with (-4) ** 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**13. Evaluate 2 ** -3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**14. Group 1 << 2 << 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**15. Group 31 & 15 & 7.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**16. Group 1 | 2 | 4 | 8.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**17. Group 15 ^ 7 ^ 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**18. Compare 2 < 3 < 4 with (2 < 3) < 4.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**19. Write a range comparison from 10 to 50.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**20. Write a percentage comparison from 0 through 100.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**21. Evaluate False or 0 or "ready".**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**22. Evaluate "ok" and 5 and [].**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**23. Explain AND short-circuiting.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**24. Explain OR short-circuiting.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**25. Compare True or False and False with a parenthesized alternative.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**26. Explain the grouping of 10 + 5 - 2 + 1.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**27. Explain the grouping of 100 / 10 * 5 / 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**28. Create a string concatenation chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**29. Create a list concatenation chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**30. Create a three-power chain and write explicit parentheses.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**31. Explain a nested conditional expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**32. Rewrite a nested conditional with explicit grouping.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**33. Explain why associativity is not a universal operand evaluation schedule.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**34. Compare two integer sums with different grouping.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**35. Compare floating-point sums with different grouping.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**36. Create a division example where grouping changes the result.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**37. Create a subtraction example where grouping changes the result.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**38. Explain addition and multiplication associativity.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**39. Explain why exponentiation is a special case.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**40. Force the left grouping of a power chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**41. Force the right grouping of a power chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**42. Combine multiplication and division in a chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**43. Combine bitwise shifts and arithmetic.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**44. Explain chained comparison behavior.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**45. Explain short-circuit behavior in a logical chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**46. Nest a conditional expression in an else branch.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**47. Write three comparisons in one chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**48. Identify associativity rules in a supplied expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**49. Dry-run a five-operator arithmetic chain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**50. Explain how parentheses clarify associativity.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

## Practice bank - 04 - Parentheses and Grouping
For every question: write the code, predict the output, execute it, explain the result and test one boundary or edge case.
**01. Evaluate (12 + 8) * 3.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**02. Evaluate 12 + (8 * 3) and compare.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**03. Evaluate ((8 + 2) * 3) - 4.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**04. Calculate an average of five values using grouped addition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**05. Compare (40 - 10) - 5 with 40 - (10 - 5).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**06. Compare (90 / 3) / 5 with 90 / (3 / 5).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**07. Compare (2 ** 3) ** 2 with 2 ** (3 ** 2).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**08. Explain (-3) ** 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**09. Explain -3 ** 2.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**10. Group the numerator of a simple-interest formula.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**11. Group the denominator of a rate formula.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**12. Write a triangle-area expression with clear grouping.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**13. Write a rectangle-perimeter expression with grouping.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**14. Group two requirements for a verified adult account.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**15. Group OR alternatives in a login policy.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**16. Apply NOT to a grouped OR expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**17. Rewrite not (A and B) using De Morgan’s law.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**18. Group a bitwise mask before comparison.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**19. Compare (5 | 2) & 1 with 5 | (2 & 1).**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**20. Explain why (10) is not a tuple.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**21. Create a one-element tuple containing 10.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**22. Create an empty tuple.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**23. Group a function result with a number.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**24. Group a conditional expression before concatenation.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**25. Group a list before indexing it.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**26. Pass a generator expression to sum().**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**27. Explain function-call parentheses.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**28. Write a weighted score formula with grouped components.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**29. Write a Fahrenheit conversion formula.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**30. Convert time to seconds with grouped components.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**31. Clarify an expression that uses max() and min().**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**32. Create a Boolean expression with three visible groups.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**33. Explain grouping versus function-call syntax.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**34. Explain the comma rule for one-element tuples.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**35. Group a per-item calculation in a list comprehension.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**36. Use parentheses in a lambda body.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**37. Create nested arithmetic and show intermediate results.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**38. Group two alternative eligibility paths.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**39. Create a denominator containing addition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**40. Group an expression containing modulo.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**41. Explain when redundant parentheses are useful.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**42. Correct a missing closing parenthesis.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**43. Correct a misplaced parenthesis in a formula.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**44. Explain how grouping helps debug a long expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**45. Rewrite a grouped formula with intermediate variables.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**46. Distinguish a negative base from a negative result.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**47. Clarify a nested conditional expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**48. Explain why parentheses do not prevent division by zero.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**49. Group a tax-after-discount rule.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**50. Compare tax-before-discount and tax-after-discount formulas.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

## Practice bank - 05 - Conditional Expressions
For every question: write the code, predict the output, execute it, explain the result and test one boundary or edge case.
**01. Write Adult or Minor selection.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**02. Write Even or Odd selection.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**03. Write Pass or Fail selection.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**04. Select the larger of two values.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**05. Select the smaller of two values.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**06. Classify positive, negative and zero.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**07. Choose a shipping fee from an order threshold.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**08. Choose a discounted price from a threshold.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**09. Select Guest when a username is empty.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**10. Use a default only when a value is None.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**11. Explain why zero is lost by value or fallback.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**12. Assign one of five grade labels using nested conditionals.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**13. Rewrite grade logic using if-elif-else.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**14. Compare ternary readability with ordinary branching.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**15. Use a conditional expression inside print().**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**16. Pass a conditional expression as a function argument.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**17. Use a conditional expression in a dictionary value.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**18. Use a conditional expression in a list comprehension.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**19. Distinguish a comprehension filter from conditional selection.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**20. Select a login label from a Boolean flag.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**21. Use AND in the condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**22. Use OR in the condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**23. Use NOT in the condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**24. Use a chained comparison in the condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**25. Select a leap-year label.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**26. Select an absolute-value result.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**27. Call a function in one branch.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**28. Show that an unselected branch is not evaluated.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**29. Show a division error when the error branch is selected.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**30. Explain truthiness versus None checking.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**31. Use a non-empty string as a condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**32. Use an empty list as a condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**33. Use an empty dictionary as a condition.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**34. Select one of two lists.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**35. Select one of two tuples.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**36. Use a conditional expression in a return statement.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**37. Classify a temperature.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**38. Select a membership message.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**39. Select the first available display label.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**40. Explain why deeply nested conditionals are difficult to maintain.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**41. Rewrite a confusing nested expression as if-elif-else.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**42. Write a status function using a conditional expression.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**43. Select a computed arithmetic result.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**44. Use branches with different types and discuss the result type.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**45. Choose a fallback for a missing dictionary key.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**46. Show whether a list has items.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**47. Select a score category with explicit boundaries.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**48. Test both branches.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**49. Explain short-circuit evaluation.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

**50. Identify a case where if-else is better.**
- **Plan:** Identify the operands, condition and expected result type.
- **Dry run:** Write intermediate values or condition results in order.
- **Verify:** Run the code and compare the result with your prediction.
- **Extend:** Change one input and explain how the result changes.

# Part F - Debugging Clinic: 50 Common Problems
For each issue, find the cause, correct the expression and write a test that would catch the same bug in the future.

### 01. Using assignment instead of equality
**Problem:**
```python
if score = 40:
```
**Cause:** Use `==` for comparison.
**Correction:**
```python
if score == 40:
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 02. Missing else branch
**Problem:**
```python
result = "Pass" if marks >= 40
```
**Cause:** A conditional expression requires else.
**Correction:**
```python
result = "Pass" if marks >= 40 else "Fail"
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 03. Wrong ternary order
**Problem:**
```python
result = if ready "Go" else "Wait"
```
**Cause:** The true value must come before if.
**Correction:**
```python
result = "Go" if ready else "Wait"
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 04. Missing closing parenthesis
**Problem:**
```python
result = (a + b * c
```
**Cause:** The opening parenthesis is not closed.
**Correction:**
```python
result = (a + b) * c
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 05. Unexpected tuple
**Problem:**
```python
value = (10,)
```
**Cause:** A comma creates a one-element tuple.
**Correction:**
```python
value = (10)
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 06. Zero replaced by fallback
**Problem:**
```python
display = score or 100
```
**Cause:** Zero is falsy.
**Correction:**
```python
display = score if score is not None else 100
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 07. Identity used for numeric equality
**Problem:**
```python
if value is 100:
```
**Cause:** Use value equality, not object identity.
**Correction:**
```python
if value == 100:
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 08. Equality used for None check
**Problem:**
```python
if value == None:
```
**Cause:** Use identity for None.
**Correction:**
```python
if value is None:
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 09. Average grouped incorrectly
**Problem:**
```python
average = a + b + c / 3
```
**Cause:** Only c is divided by 3.
**Correction:**
```python
average = (a + b + c) / 3
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 10. Wrong denominator grouping
**Problem:**
```python
rate = total / a + b
```
**Cause:** Addition occurs after division.
**Correction:**
```python
rate = total / (a + b)
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 11. Negative square confusion
**Problem:**
```python
square = -number ** 2
```
**Cause:** The power is negated.
**Correction:**
```python
square = (-number) ** 2
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 12. Exponentiation grouped unexpectedly
**Problem:**
```python
value = (2 ** 3) ** 2
```
**Cause:** This forces left grouping.
**Correction:**
```python
value = 2 ** (3 ** 2)
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 13. Division in selected branch
**Problem:**
```python
answer = 10 if valid else 1 / 0
```
**Cause:** False selects the division branch.
**Correction:**
```python
Check the denominator before calculating.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 14. Assuming both branches run
**Problem:**
```python
result = first() if condition else second()
```
**Cause:** Only one branch executes.
**Correction:**
```python
Use an if-else statement for two actions.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 15. Grade conditions in wrong order
**Problem:**
```python
grade = "D" if m >= 40 else "A" if m >= 90 else "F"
```
**Cause:** The first branch catches passing scores.
**Correction:**
```python
Check the highest threshold first.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 16. Missing final grade category
**Problem:**
```python
grade = "A" if m >= 90 else None
```
**Cause:** All lower scores become None.
**Correction:**
```python
Add every required grade branch.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 17. AND used instead of OR
**Problem:**
```python
valid = email_ok and phone_ok
```
**Cause:** Both are required.
**Correction:**
```python
valid = email_ok or phone_ok
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 18. OR used instead of AND
**Problem:**
```python
allowed = adult or verified
```
**Cause:** Only one condition is required.
**Correction:**
```python
allowed = adult and verified
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 19. NOT scope misunderstood
**Problem:**
```python
allowed = not adult or verified
```
**Cause:** NOT applies only to adult.
**Correction:**
```python
allowed = not (adult or verified)
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 20. Dictionary key/value confusion
**Problem:**
```python
"name" in user.values()
```
**Cause:** This checks values.
**Correction:**
```python
"name" in user
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 21. Membership/identity confusion
**Problem:**
```python
a is b
```
**Cause:** This checks object identity.
**Correction:**
```python
a == b
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 22. Indexing empty list
**Problem:**
```python
first = values[0]
```
**Cause:** The list may be empty.
**Correction:**
```python
Check the list before indexing.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 23. Slice stop misunderstood
**Problem:**
```python
part = text[1:4]
```
**Cause:** Index 4 is excluded.
**Correction:**
```python
Use text[1:5] for four positions starting at 1.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 24. String/integer concatenation
**Problem:**
```python
message = "Score: " + score
```
**Cause:** The types are incompatible.
**Correction:**
```python
message = f"Score: {score}"
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 25. True division chosen accidentally
**Problem:**
```python
pages = total / per_page
```
**Cause:** The result is a float.
**Correction:**
```python
Use // when complete groups are required.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 26. Negative floor division misunderstood
**Problem:**
```python
print(-7 // 2)
```
**Cause:** The result is -4.
**Correction:**
```python
Remember floor rounds down toward negative infinity.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 27. Money rounded too early
**Problem:**
```python
subtotal = round(price * quantity, 0)
```
**Cause:** Early rounding may affect later calculations.
**Correction:**
```python
Keep precision and round at the defined presentation boundary.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 28. Range excludes boundaries
**Problem:**
```python
0 < score < 100
```
**Cause:** Zero and 100 are excluded.
**Correction:**
```python
Use 0 <= score <= 100 if both are allowed.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 29. Mixed types compared
**Problem:**
```python
"10" > 5
```
**Cause:** String and integer ordering is not supported here.
**Correction:**
```python
Convert the string to int first.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 30. Logical and bitwise mixed
**Problem:**
```python
ready & verified
```
**Cause:** This is not the clearest logical form.
**Correction:**
```python
ready and verified
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 31. Mask grouping unclear
**Problem:**
```python
flags & mask == mask
```
**Cause:** The precedence is defined, but grouping may be hard to scan.
**Correction:**
```python
(flags & mask) == mask
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 32. Caret used as power
**Problem:**
```python
square = n ^ 2
```
**Cause:** Caret is XOR.
**Correction:**
```python
square = n ** 2
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 33. NOT precedence misunderstood
**Problem:**
```python
answer = not x == y
```
**Cause:** This is parsed as not (x == y).
**Correction:**
```python
Write not (x == y) or x != y.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 34. Assuming AND returns bool
**Problem:**
```python
result = "ok" and 5
```
**Cause:** The result is 5.
**Correction:**
```python
Use bool(...) if a Boolean is required.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 35. Assuming OR returns bool
**Problem:**
```python
result = 0 or "fallback"
```
**Cause:** The result is the string fallback.
**Correction:**
```python
Use bool(...) if a Boolean is required.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 36. Nested conditional is unreadable
**Problem:**
```python
grade = "A" if a else "B" if b else "C"
```
**Cause:** The nesting may be difficult to scan.
**Correction:**
```python
Use parentheses or if-elif-else.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 37. Side effects hidden in ternary
**Problem:**
```python
result = update() if ready else cleanup()
```
**Cause:** The expression hides action flow.
**Correction:**
```python
Use an explicit if-else statement.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 38. Empty list truthiness surprise
**Problem:**
```python
label = "Items" if items else "Empty"
```
**Cause:** An empty list is falsy.
**Correction:**
```python
Use this only when emptiness is the intended test.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 39. None and empty string confused
**Problem:**
```python
name = input_value or "Guest"
```
**Cause:** Both None and empty string trigger the fallback.
**Correction:**
```python
Use explicit None checking when needed.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 40. Walrus grouping unclear
**Problem:**
```python
if n := len(items) > 0:
```
**Cause:** n may receive the Boolean result.
**Correction:**
```python
if (n := len(items)) > 0:
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 41. Walrus used unnecessarily
**Problem:**
```python
if (length := len(text)) > 0:
```
**Cause:** The name may not be needed later.
**Correction:**
```python
Use len(text) directly when no reuse is needed.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 42. Threshold equality wrong
**Problem:**
```python
label = "High" if score > 50 else "Low"
```
**Cause:** Exactly 50 selects Low.
**Correction:**
```python
Use >= if 50 belongs to High.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 43. Method called on wrong object
**Problem:**
```python
name = value if value else None.upper()
```
**Cause:** The call attaches to None.
**Correction:**
```python
name = (value if value else "Guest").upper()
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 44. Mutable fallback confusion
**Problem:**
```python
items = supplied or []
```
**Cause:** An empty supplied list triggers the fallback.
**Correction:**
```python
Check `supplied is not None` if empty list is meaningful.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 45. Print used as selected value
**Problem:**
```python
value = print("yes") if condition else print("no")
```
**Cause:** print returns None.
**Correction:**
```python
Use if-else for output actions.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 46. Parentheses mistaken for tuple
**Problem:**
```python
value = (x)
```
**Cause:** This is the value x.
**Correction:**
```python
value = (x,)
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 47. Parentheses enclose wrong part
**Problem:**
```python
result = (a + b * c)
```
**Cause:** Multiplication still occurs first.
**Correction:**
```python
result = (a + b) * c
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 48. Excessive parentheses
**Problem:**
```python
result = (((a))) + (((b)))
```
**Cause:** The code is valid but visually noisy.
**Correction:**
```python
result = a + b
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 49. Input conversion not validated
**Problem:**
```python
age = int(user_text)
```
**Cause:** Non-numeric text raises ValueError.
**Correction:**
```python
Validate input or handle ValueError.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

### 50. Division denominator not checked
**Problem:**
```python
ratio = total / count
```
**Cause:** count may be zero.
**Correction:**
```python
Check count != 0 before division.
```
**Prevention:** Test the expression with a normal value, a boundary value and an edge case.

# Part G - Expression Patterns in DSA
Expression rules appear in array indexing, binary search, sorting, sliding windows, graph traversal, bit manipulation and dynamic programming. Each expression must be paired with its preconditions.

### 01. Binary search midpoint
**Expression:** `mid = left + (right - left) // 2`
**Concepts:** Subtraction, floor division and addition.
**Precondition:** Maintain a valid search interval.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 02. Index range
**Expression:** `valid = 0 <= index < len(values)`
**Concepts:** Chained comparison and len().
**Precondition:** The upper boundary is exclusive.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 03. Last index
**Expression:** `last = len(values) - 1`
**Concepts:** Function call and subtraction.
**Precondition:** An empty list has no valid last index.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 04. Sliding window width
**Expression:** `width = right - left + 1`
**Concepts:** Subtraction and addition.
**Precondition:** The +1 assumes an inclusive interval.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 05. Even index
**Expression:** `is_even = index % 2 == 0`
**Concepts:** Modulo and comparison.
**Precondition:** Use parity to alternate a process.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 06. Absolute pointer distance
**Expression:** `distance = abs(right - left)`
**Concepts:** Subtraction and abs().
**Precondition:** The distance is non-negative.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 07. Array update
**Expression:** `next_value = values[i] + increment`
**Concepts:** Indexing and addition.
**Precondition:** Check that i is valid.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 08. Prefix sum
**Expression:** `prefix[i] = prefix[i - 1] + values[i]`
**Concepts:** Indexing and addition.
**Precondition:** Handle the first position separately.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 09. Update maximum
**Expression:** `best = candidate if candidate > best else best`
**Concepts:** Conditional expression.
**Precondition:** Retain the best value found so far.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 10. Update minimum
**Expression:** `best = candidate if candidate < best else best`
**Concepts:** Conditional expression.
**Precondition:** Retain the smallest value found so far.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 11. Selection sort test
**Expression:** `values[j] < values[min_index]`
**Concepts:** Comparison.
**Precondition:** Ensure both indices are valid.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 12. Bubble sort test
**Expression:** `values[j] > values[j + 1]`
**Concepts:** Comparison and indexing.
**Precondition:** Ensure j+1 is inside the list.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 13. Bit flag check
**Expression:** `(flags & mask) == mask`
**Concepts:** Bitwise AND and equality.
**Precondition:** Use a mask with the intended set of bits.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 14. Set a bit
**Expression:** `updated = flags | mask`
**Concepts:** Bitwise OR.
**Precondition:** OR turns on every bit present in mask.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 15. Clear a bit
**Expression:** `updated = flags & ~mask`
**Concepts:** Bitwise NOT and AND.
**Precondition:** Understand the integer representation and mask.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 16. Toggle a bit
**Expression:** `updated = flags ^ mask`
**Concepts:** Bitwise XOR.
**Precondition:** XOR flips selected bits.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 17. Power-of-two check
**Expression:** `n > 0 and (n & (n - 1)) == 0`
**Concepts:** Logical AND and bitwise grouping.
**Precondition:** This check requires positive n.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 18. Graph visited test
**Expression:** `neighbor not in visited`
**Concepts:** Membership.
**Precondition:** A set is often suitable for repeated membership tests.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 19. Queue empty check
**Expression:** `not queue`
**Concepts:** Truthiness.
**Precondition:** An empty collection is falsy.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 20. Stack top index
**Expression:** `len(stack) - 1`
**Concepts:** Function call and subtraction.
**Precondition:** Check stack non-empty before reading the top.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 21. Tree leaf check
**Expression:** `node.left is None and node.right is None`
**Concepts:** Identity and AND.
**Precondition:** None indicates a missing child reference.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 22. Tree child check
**Expression:** `node.left is not None or node.right is not None`
**Concepts:** Identity and OR.
**Precondition:** At least one child exists.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 23. DP minimum
**Expression:** `dp[i] = min(dp[i], candidate)`
**Concepts:** Function call.
**Precondition:** The recurrence must define valid candidate states.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 24. DP maximum
**Expression:** `dp[i] = max(dp[i], candidate)`
**Concepts:** Function call.
**Precondition:** The recurrence must define valid candidate states.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 25. Clamp lower boundary
**Expression:** `low if value < low else value`
**Concepts:** Conditional expression.
**Precondition:** This only enforces the lower limit.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 26. Clamp both boundaries
**Expression:** `max(low, min(value, high))`
**Concepts:** Nested function calls.
**Precondition:** Ensure low is not greater than high.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 27. Binary search stopping rule
**Expression:** `left <= right`
**Concepts:** Comparison.
**Precondition:** Use the interval convention consistently.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 28. Two-pointer crossing
**Expression:** `left < right`
**Concepts:** Comparison.
**Precondition:** Choose strict or inclusive bounds from the algorithm design.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 29. Range membership
**Expression:** `low <= target <= high`
**Concepts:** Chained comparison.
**Precondition:** Both boundaries are inclusive here.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

### 30. Optional child reference
**Expression:** `child is not None`
**Concepts:** Identity.
**Precondition:** Use is for None checks.
**Practice:** Place the expression in a small function, run it with a normal input and a boundary input, and explain the expected result.

# Part H - Viva and Interview Questions
Practice speaking each answer aloud. For coding questions, demonstrate the idea with a tiny Python snippet.

### Viva 001 - What is an expression?
**Answer:** Code that Python evaluates to produce a value.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 002 - What is an operand?
**Answer:** A value or expression on which an operator acts.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 003 - What is an operator?
**Answer:** A symbol or keyword that performs an operation.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 004 - Expression versus statement?
**Answer:** An expression produces a value; a statement performs an instruction.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 005 - Name expression families.
**Answer:** Arithmetic, comparison, logical, bitwise, membership, identity, sequence and conditional.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 006 - What does + do with integers?
**Answer:** It performs addition.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 007 - What does + do with strings?
**Answer:** It concatenates strings.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 008 - Difference between / and //?
**Answer:** True division versus floor division.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 009 - What does modulo return?
**Answer:** A remainder according to Python division rules.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 010 - What is exponentiation syntax?
**Answer:** Use **.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 011 - What is a comparison expression?
**Answer:** An expression that compares values.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 012 - Name comparison operators.
**Answer:** ==, !=, <, <=, > and >=.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 013 - What does in test?
**Answer:** Membership.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 014 - What does is test?
**Answer:** Object identity.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 015 - How do you check None?
**Answer:** Use is None.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 016 - What is precedence?
**Answer:** The default grouping hierarchy for operators.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 017 - What is associativity?
**Answer:** The grouping direction among equal-precedence operators.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 018 - Which binds more tightly, multiplication or addition?
**Answer:** Multiplication.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 019 - Which binds more tightly, and or or?
**Answer:** and.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 020 - Where does not sit relative to comparisons?
**Answer:** Comparisons bind more tightly than not.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 021 - How does exponentiation associate?
**Answer:** Right-to-left.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 022 - What is 2 ** 3 ** 2?
**Answer:** 512, because it is 2 ** (3 ** 2).
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 023 - What is (2 ** 3) ** 2?
**Answer:** 64.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 024 - What is -2 ** 2?
**Answer:** -4.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 025 - What is (-2) ** 2?
**Answer:** 4.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 026 - What is left associativity?
**Answer:** A chain groups from the left.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 027 - Is subtraction associative?
**Answer:** No.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 028 - Is division associative?
**Answer:** No.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 029 - How is 24 / 3 * 2 grouped?
**Answer:** (24 / 3) * 2.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 030 - What is a chained comparison?
**Answer:** A comparison chain such as 0 <= x < 10.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 031 - Can and return a non-Boolean?
**Answer:** Yes, it returns one of its operands.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 032 - Can or return a non-Boolean?
**Answer:** Yes, it returns one of its operands.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 033 - What is short-circuit evaluation?
**Answer:** Evaluation stops once the result is determined.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 034 - What is falsy?
**Answer:** A value treated as false in a Boolean context.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 035 - Give examples of falsy values.
**Answer:** False, None, 0, 0.0, empty string, empty list, empty tuple and empty dictionary.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 036 - What is truthy?
**Answer:** A value treated as true in a Boolean context.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 037 - Purpose of parentheses?
**Answer:** Group expressions and clarify or change the default grouping.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 038 - Which nested group is evaluated first?
**Answer:** The innermost group.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 039 - Do parentheses alone create a tuple?
**Answer:** No, a comma is required for a one-element tuple.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 040 - What is the type of (10)?
**Answer:** int.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 041 - What is the type of (10,)?
**Answer:** tuple.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 042 - How do you create an empty tuple?
**Answer:** Use ().
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 043 - What are function-call parentheses?
**Answer:** They enclose the arguments passed to a function.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 044 - What is a conditional expression?
**Answer:** An expression that selects one of two values based on a condition.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 045 - What is its syntax?
**Answer:** true_value if condition else false_value.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 046 - Why is it ternary?
**Answer:** It has three components.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 047 - Is else compulsory?
**Answer:** Yes.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 048 - Are both result branches evaluated?
**Answer:** No, only the selected branch is evaluated.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 049 - When is a conditional expression suitable?
**Answer:** When a simple condition selects a value.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 050 - When is if-else clearer?
**Answer:** When branches contain multiple statements or complex logic.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 051 - What is nested conditional expression?
**Answer:** A conditional expression in another conditional expression.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 052 - How should grade thresholds be arranged?
**Answer:** Usually highest to lowest.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 053 - How do you select Guest for an empty string?
**Answer:** Use name if name else Guest.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 054 - How do you preserve zero with a fallback?
**Answer:** Check value is not None.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 055 - What does bool("") return?
**Answer:** False.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 056 - What does bool("Python") return?
**Answer:** True.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 057 - What does bool([]) return?
**Answer:** False.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 058 - What does bool([0]) return?
**Answer:** True, because the list is non-empty.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 059 - Conditional expression in a list comprehension?
**Answer:** It selects a value for each item.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 060 - How is a comprehension filter different?
**Answer:** A filter controls inclusion; a conditional expression controls the produced value.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 061 - How do you test evenness?
**Answer:** n % 2 == 0.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 062 - How do you select the greater of two values?
**Answer:** a if a > b else b, or max(a, b).
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 063 - How do you classify positive, negative and zero?
**Answer:** Use nested conditionals or if-elif-else.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 064 - State De Morgan first law.
**Answer:** not (A or B) equals (not A) and (not B).
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 065 - State De Morgan second law.
**Answer:** not (A and B) equals (not A) or (not B).
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 066 - What does bitwise AND do?
**Answer:** A result bit is set when both corresponding bits are set.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 067 - What does bitwise OR do?
**Answer:** A result bit is set when either corresponding bit is set.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 068 - What does XOR do?
**Answer:** A result bit is set when corresponding bits differ.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 069 - What is ~n for Python integers?
**Answer:** -n - 1.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 070 - How can all selected mask bits be checked?
**Answer:** (value & mask) == mask.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 071 - Why use parentheses in a bit mask test?
**Answer:** They make the bitwise grouping explicit.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 072 - What is a common binary search midpoint?
**Answer:** left + (right - left) // 2.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 073 - Why group an average numerator?
**Answer:** To add all values before dividing by their count.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 074 - Does float represent all decimal fractions exactly?
**Answer:** No.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 075 - Why handle money carefully?
**Answer:** Rounding policy and binary floating-point representation can affect totals.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 076 - What error can division by zero raise?
**Answer:** ZeroDivisionError.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 077 - What error can int("abc") raise?
**Answer:** ValueError.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 078 - What error can an invalid list index raise?
**Answer:** IndexError.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 079 - What error can a missing parenthesis cause?
**Answer:** Usually SyntaxError.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 080 - Why use intermediate variables?
**Answer:** To improve readability, testing and debugging.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 081 - What is a dry run?
**Answer:** A manual trace of expression evaluation.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 082 - What values should threshold tests include?
**Answer:** Below, exactly at and above the threshold.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 083 - What is a boundary test?
**Answer:** A test of an edge value in an accepted range.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 084 - What is a truth table?
**Answer:** A table of logical outcomes for input truth combinations.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 085 - How should a conditional expression be tested?
**Answer:** Test both branches and boundaries.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 086 - What is the walrus operator?
**Answer:** The assignment expression operator :=.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 087 - When should walrus be avoided?
**Answer:** When it reduces clarity or the value is not reused.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 088 - Can a conditional expression return a list?
**Answer:** Yes.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 089 - Can its branches have different types?
**Answer:** Yes, but consistent types often simplify later use.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 090 - Risk of deeply nested ternaries?
**Answer:** Reduced readability and maintainability.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 091 - Difference between == and is?
**Answer:** Value equality versus object identity.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 092 - Why is is None recommended?
**Answer:** None is a singleton and identity is the intended test.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 093 - Common membership use in DSA?
**Answer:** Checking whether an item or node exists in a collection.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 094 - Why can a set help membership tests?
**Answer:** Sets usually offer efficient average-case membership lookup.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 095 - How can a confusing expression be clarified?
**Answer:** Add meaningful parentheses or split it into named variables.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 096 - Should code always be shortened?
**Answer:** No, clarity and correctness matter more.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

### Viva 097 - Main goal of this section?
**Answer:** Read, evaluate, explain, write and debug Python expressions.
**Practice follow-up:** Write one short Python statement that demonstrates this answer, predict its output and then execute it.

# Part I - Assessment and Revision
## Self-assessment rubric
| Level | Description | Evidence |
|---|---|---|
| 1 - Beginner | Recognizes simple expressions but needs help evaluating them. | Can identify operands and operators. |
| 2 - Developing | Evaluates basic arithmetic and comparisons. | Can explain a short precedence example. |
| 3 - Practicing | Uses grouping and associativity correctly. | Can dry-run nested arithmetic and conditions. |
| 4 - Confident | Writes and debugs nested expressions. | Can explain branch selection, truthiness and edge cases. |
| 5 - Ready | Applies expression rules to unfamiliar DSA problems. | Can reason about types, grouping and boundaries independently. |

## One-week revision timetable
| Day | Focus | Practice target | Expected result |
|---|---|---|---|
| 1 | Expression fundamentals | 20 short expression evaluations | Expression family summary. |
| 2 | Precedence | 25 precedence traces | Marked precedence reference. |
| 3 | Associativity | 20 grouping comparisons | Explanation of exponentiation and chained comparisons. |
| 4 | Parentheses | 20 nested dry runs | Before-and-after grouping examples. |
| 5 | Conditional expressions | 20 true/false branch tests | Ternary versus if-else comparison. |
| 6 | Integrated examples and debugging | 15 mixed problems | Debugging log. |
| 7 | Practice test and viva | Timed review | Weak-topic revision list. |

## Daily practice routine
- Review the relevant rule before coding.
- Write the expression by hand and predict the output.
- Record intermediate values.
- Run the code and compare actual and predicted results.
- Identify whether a mismatch came from precedence, associativity, type, grouping or logic.
- Rewrite a confusing expression with parentheses or variables.
- Solve one unseen problem without copying an example.

## Exam preparation checklist
- [ ] Define expression and distinguish it from a statement.
- [ ] Evaluate arithmetic expressions with several operators.
- [ ] Explain the precedence hierarchy relevant to an expression.
- [ ] Identify left- and right-associative cases.
- [ ] Explain exponentiation and unary-minus behavior.
- [ ] Trace nested parentheses.
- [ ] Distinguish `(10)`, `(10,)` and `()`.
- [ ] Evaluate comparison and logical expressions.
- [ ] Explain why and/or may return operands.
- [ ] Write a conditional expression correctly.
- [ ] Distinguish truthiness from a None check.
- [ ] Explain short-circuit evaluation.
- [ ] Test branches and comparison boundaries.
- [ ] Apply expression skills in binary search or bit masks.

# Part J - Quick Reference
| Task | Expression pattern |
|---|---|
| Addition | `a + b` |
| Subtraction | `a - b` |
| Multiplication | `a * b` |
| True division | `a / b` |
| Floor division | `a // b` |
| Remainder | `a % b` |
| Exponentiation | `a ** b` |
| Equality | `a == b` |
| Inequality | `a != b` |
| Range | `low <= value <= high` |
| Logical AND | `condition_a and condition_b` |
| Logical OR | `condition_a or condition_b` |
| Logical NOT | `not condition` |
| Membership | `item in collection` |
| Non-membership | `item not in collection` |
| Identity with None | `value is None` |
| Bitwise AND | `a & b` |
| Bitwise OR | `a | b` |
| Bitwise XOR | `a ^ b` |
| Left shift | `a << n` |
| Right shift | `a >> n` |
| Conditional expression | `true_value if condition else false_value` |
| Single-item tuple | `(value,)` |
| Slice | `sequence[start:stop:step]` |
| List comprehension | `[expression for item in iterable]` |

## Ten rules to remember
1. An expression produces a value.
2. Know operand types before evaluating.
3. Precedence determines default grouping.
4. Associativity determines grouping among equal-precedence operators.
5. Exponentiation is right-associative.
6. Subtraction and division are not associative.
7. Parentheses make intended grouping explicit.
8. A one-element tuple requires a comma.
9. A conditional expression requires else and selects one branch.
10. Readable code is more important than an unnecessarily short expression.

## Final summary
The Expressions section connects essential Python skills. You learned to recognize expressions, evaluate operators, apply precedence and associativity, use parentheses to state grouping, and select values with conditional expressions. These ideas appear in calculators, validation rules, binary search, sorting, bit manipulation and dynamic programming.

Do not guess an expression output. Identify the types, grouping, evaluation rules and conditions, then trace each intermediate step. Continue practicing with the five topic files and the worked cards in this README.

## Topic file navigation
| Topic | Python file | Individual README |
|---|---|---|
| 01 - Expressions | `01_expressions.py` | `01-expressions/README.md` |
| 02 - Operator Precedence | `02_operator_precedence.py` | `02-operator-precedence/README.md` |
| 03 - Operator Associativity | `03_operator_associativity.py` | `03-operator-associativity/README.md` |
| 04 - Parentheses and Grouping | `04_parentheses_and_grouping.py` | `04-parentheses-and-grouping/README.md` |
| 05 - Conditional Expressions | `05_conditional_expressions.py` | `05-conditional-expressions/README.md` |

## Git commands for this folder
```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"

git status

git add "PYTHON/Week-1-Programming-Fundamentals/05-Operators-Expressions/08-Expressions/README.md"

git status

git commit -m "Add comprehensive Python expressions master guide"

git push origin main
```

# Part K - Independent Mastery Cards: 200 Additional Tasks
These cards are designed for active recall. A card is complete only after you have written a runnable example, predicted the result, tested the result and explained the Python rule.

### Mastery Card 001 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 002 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 003 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 004 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 005 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 006 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 007 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 008 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 009 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 010 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 011 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 012 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 013 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 014 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 015 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 016 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 017 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 018 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 019 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 020 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 021 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 022 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 023 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 024 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 025 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 026 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 027 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 028 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 029 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 030 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 031 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 032 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 033 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 034 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 035 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 036 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 037 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 038 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 039 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 040 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 041 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 042 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 043 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 044 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 045 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 046 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 047 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 048 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 049 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 050 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 051 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 052 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 053 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 054 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 055 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 056 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 057 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 058 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 059 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 060 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 061 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 062 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 063 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 064 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 065 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 066 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 067 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 068 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 069 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 070 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 071 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 072 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 073 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 074 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 075 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 076 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 077 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 078 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 079 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 080 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 081 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 082 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 083 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 084 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 085 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 086 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 087 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 088 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 089 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 090 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 091 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 092 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 093 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 094 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 095 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 096 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 097 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 098 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 099 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 100 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 101 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 102 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 103 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 104 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 105 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 106 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 107 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 108 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 109 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 110 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 111 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 112 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 113 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 114 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 115 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 116 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 117 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 118 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 119 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 120 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 121 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 122 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 123 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 124 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 125 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 126 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 127 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 128 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 129 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 130 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 131 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 132 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 133 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 134 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 135 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 136 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 137 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 138 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 139 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 140 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 141 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 142 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 143 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 144 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 145 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 146 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 147 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 148 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 149 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 150 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 151 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 152 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 153 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 154 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 155 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 156 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 157 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 158 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 159 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 160 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 161 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 162 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 163 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 164 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 165 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 166 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 167 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 168 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 169 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 170 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 171 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 172 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 173 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 174 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 175 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 176 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 177 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 178 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 179 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 180 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 181 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 182 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 183 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 184 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 185 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 186 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 187 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 188 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 189 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 190 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 191 - Expression identification
**Task:** Identify operands, operators, function calls and result type.
**Required variation:** Include an arithmetic, string and comparison expression.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 192 - Precedence trace
**Task:** Mark the first operation grouped and show intermediate values.
**Required variation:** Use at least four precedence levels.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 193 - Associativity trace
**Task:** Add parentheses that show the default grouping.
**Required variation:** Compare the default grouping with an alternative grouping.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 194 - Parentheses redesign
**Task:** Rewrite a long expression using meaningful groups or variables.
**Required variation:** Explain why the rewritten version is easier to review.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 195 - Conditional branch test
**Task:** Create one input for the true branch and another for the false branch.
**Required variation:** Verify that only the selected branch is evaluated.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 196 - Truthiness check
**Task:** Determine whether an object is truthy or falsy.
**Required variation:** Include zero, an empty string and an empty collection.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 197 - None check
**Task:** Test whether a value is missing without discarding valid falsy values.
**Required variation:** Demonstrate that zero is preserved.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 198 - Boundary validation
**Task:** Test below, on and above a comparison boundary.
**Required variation:** Use a comparison that matches the written requirement.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 199 - Bitwise reasoning
**Task:** Convert small operands to binary and calculate the result.
**Required variation:** Verify AND, OR or XOR with Python.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

### Mastery Card 200 - DSA transfer
**Task:** Use an expression in an algorithm or data-structure example.
**Required variation:** State the precondition that makes the expression safe.
**Write in your notebook:**
- The input values and their data types.
- The complete Python expression.
- Every intermediate group or condition result.
- The final output and result type.
- One boundary or edge case.
**Explain:** Name the Python rule that determines the result. Do not rely on memorizing an earlier output.
**Extension:** Change the values and create a second example that uses the same rule in a practical scenario.

# Part L - Mixed Review Cards: 150 Tasks
### Mixed Review Card 001
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 002
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 003
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 004
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 005
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 006
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 007
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 008
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 009
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 010
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 011
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 012
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 013
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 014
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 015
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 016
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 017
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 018
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 019
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 020
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 021
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 022
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 023
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 024
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 025
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 026
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 027
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 028
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 029
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 030
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 031
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 032
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 033
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 034
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 035
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 036
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 037
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 038
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 039
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 040
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 041
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 042
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 043
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 044
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 045
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 046
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 047
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 048
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 049
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 050
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 051
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 052
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 053
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 054
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 055
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 056
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 057
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 058
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 059
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 060
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 061
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 062
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 063
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 064
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 065
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 066
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 067
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 068
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 069
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 070
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 071
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 072
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 073
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 074
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 075
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 076
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 077
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 078
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 079
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 080
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 081
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 082
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 083
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 084
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 085
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 086
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 087
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 088
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 089
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 090
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 091
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 092
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 093
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 094
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 095
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 096
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 097
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 098
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 099
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 100
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 101
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 102
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 103
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 104
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 105
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 106
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 107
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 108
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 109
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 110
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 111
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 112
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 113
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 114
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 115
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 116
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 117
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 118
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 119
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 120
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 121
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 122
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 123
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 124
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 125
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 126
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 127
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 128
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 129
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 130
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 131
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 132
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 133
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 134
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 135
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 136
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 137
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 138
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 139
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 140
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 141
**Prompt:** Calculate an expression and state the result type.
**Method:** Write intermediate values and note any type conversion.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 142
**Prompt:** Rewrite an expression so its grouping is obvious.
**Method:** Use parentheses without changing the intended meaning.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 143
**Prompt:** Explain which conditional branch is selected.
**Method:** Evaluate the condition first.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 144
**Prompt:** Compare two expressions and state whether the outputs differ.
**Method:** Look for changed grouping or a non-associative operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 145
**Prompt:** Find useful boundary inputs.
**Method:** Test below, exactly at and above the threshold.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 146
**Prompt:** Determine whether a logical expression returns a Boolean or another operand.
**Method:** Track short-circuit behavior.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 147
**Prompt:** Classify a value as truthy or falsy.
**Method:** Use its type and content.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 148
**Prompt:** Convert a bitwise expression to binary.
**Method:** Write operand bit patterns and apply the operation.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 149
**Prompt:** Apply an expression pattern to a DSA task.
**Method:** State the algorithm invariant and precondition.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

### Mixed Review Card 150
**Prompt:** Refactor a long expression.
**Method:** Use names that describe each intermediate result.
**Deliverable:** A runnable Python example, predicted output, actual output and a written explanation.
**Quality test:** The example must test the named concept and must include meaningful values.
**Reflection:** Identify one incorrect assumption a beginner might make about this expression.

# Part M - Study Completion Record
Use this checklist to track each subtopic.

| Subtopic | Read theory | Run Python file | Complete examples | Complete practice | Can explain independently |
|---|---|---|---|---|---|
| 01 - Expressions | [ ] | [ ] | [ ] | [ ] | [ ] |
| 02 - Operator Precedence | [ ] | [ ] | [ ] | [ ] | [ ] |
| 03 - Operator Associativity | [ ] | [ ] | [ ] | [ ] | [ ] |
| 04 - Parentheses and Grouping | [ ] | [ ] | [ ] | [ ] | [ ] |
| 05 - Conditional Expressions | [ ] | [ ] | [ ] | [ ] | [ ] |

**Definition of completion:** You can solve unfamiliar expressions using Python rules, explain each intermediate step, identify likely errors, test boundaries and write clear code without depending on copied outputs.

---
**End of 08 - Expressions Master README**
