# Python Bitwise Operators

> A complete learning guide covering binary numbers, bitwise AND, bitwise OR, bitwise XOR, bitwise NOT, left shift, right shift, bit masks, and practical bit manipulation techniques in Python.

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [Learning Objectives](#2-learning-objectives)
3. [What Are Bitwise Operators?](#3-what-are-bitwise-operators)
4. [Understanding Binary Number System](#4-understanding-binary-number-system)
5. [Binary Conversion](#5-binary-conversion)
6. [Understanding Bits and Bit Positions](#6-understanding-bits-and-bit-positions)
7. [Bitwise Operator Overview](#7-bitwise-operator-overview)
8. [Bitwise AND Operator (&)](#8-bitwise-and-operator-)
9. [Bitwise OR Operator (|)](#9-bitwise-or-operator-)
10. [Bitwise XOR Operator (^)](#10-bitwise-xor-operator-)
11. [Bitwise NOT Operator (~)](#11-bitwise-not-operator-)
12. [Left Shift Operator (<<)](#12-left-shift-operator-)
13. [Right Shift Operator (>>)](#13-right-shift-operator-)
14. [Bitwise Assignment Operators](#14-bitwise-assignment-operators)
15. [Understanding Bit Masks](#15-understanding-bit-masks)
16. [Set, Clear, Toggle, and Check Bits](#16-set-clear-toggle-and-check-bits)
17. [Counting Set Bits](#17-counting-set-bits)
18. [Python Binary Representation](#18-python-binary-representation)
19. [Bitwise Operators vs Logical Operators](#19-bitwise-operators-vs-logical-operators)
20. [Understanding the Python Program](#20-understanding-the-python-program)
21. [Twelve Examples Explained](#21-twelve-examples-explained)
22. [Twelve Solved Programming Problems](#22-twelve-solved-programming-problems)
23. [Ten Unsolved Practice Questions](#23-ten-unsolved-practice-questions)
24. [Dry Run and Output Prediction](#24-dry-run-and-output-prediction)
25. [Common Programming Mistakes](#25-common-programming-mistakes)
26. [Error Handling and Input Validation](#26-error-handling-and-input-validation)
27. [Best Practices](#27-best-practices)
28. [Real-World Applications](#28-real-world-applications)
29. [Bitwise Operators in DSA](#29-bitwise-operators-in-dsa)
30. [Time and Space Complexity](#30-time-and-space-complexity)
31. [Interview and Viva Questions](#31-interview-and-viva-questions)
32. [Practice Test](#32-practice-test)
33. [Quick Revision Notes](#33-quick-revision-notes)
34. [Important Terminology](#34-important-terminology)
35. [Learning Checklist](#35-learning-checklist)
36. [How to Run the Python Program](#36-how-to-run-the-python-program)
37. [Recommended Learning Sequence](#37-recommended-learning-sequence)
38. [Topic Completion Summary](#38-topic-completion-summary)

---

# 1. Introduction

Bitwise operators are used to perform operations on the individual bits of integer values.

Computers internally represent information using binary digits:

- `0`
- `1`

Each binary digit is called a bit.

Unlike arithmetic operators, which perform mathematical calculations, bitwise operators manipulate the binary representation of integers.

Python provides six fundamental bitwise operators:

- `&` – Bitwise AND.
- `|` – Bitwise OR.
- `^` – Bitwise XOR.
- `~` – Bitwise NOT.
- `<<` – Left Shift.
- `>>` – Right Shift.

Consider the following example:

```python
a = 12
b = 10

print(a & b)
```

**Output:**

```text
8
```

The AND operator compares the corresponding binary bits of both numbers.

Binary representation:

```text
12 = 1100
10 = 1010
------------
     1000
```

The binary result `1000` represents decimal value `8`.

Therefore:

```python
12 & 10
```

returns `8`.

## 1.1 Why Are Bitwise Operators Important?

Bitwise operators are important because they allow programmers to work directly with binary data.

They are useful in:

- Bit manipulation.
- Binary calculations.
- Permission systems.
- Hardware-level programming.
- Data compression.
- Cryptographic algorithms.
- Flags and status management.
- Memory-efficient operations.
- Computer graphics.
- Data Structures and Algorithms.

## 1.2 Where Will You Use Bitwise Operators?

| Area | Example Usage |
|---|---|
| Basic Python | Binary calculations |
| Computer Science | Number representation |
| Operating Systems | Flags and permissions |
| Networking | Network masks |
| Security | Bit manipulation |
| Graphics | Pixel and color operations |
| Data Compression | Bit-level encoding |
| DSA | Set-bit problems |
| Competitive Programming | Bit manipulation |
| Algorithms | Bit masks and subsets |

## 1.3 Real-Life Example

Suppose a system stores three permissions using individual bits:

```text
Bit 0 = Read Permission
Bit 1 = Write Permission
Bit 2 = Execute Permission
```

A number can represent multiple permissions simultaneously.

For example:

```text
Binary: 101
Decimal: 5
```

This indicates that the first and third permissions are enabled.

Bitwise operators make it possible to check, enable, disable, and toggle these permissions.

---

# 2. Learning Objectives

After completing this topic, you should be able to understand and use Python bitwise operators.

## 2.1 Basic Concepts

- Understand the binary number system.
- Understand bits and bit positions.
- Convert decimal values to binary.
- Read binary representations.
- Understand how computers represent integers.

## 2.2 Bitwise Operators

Learn and use:

- Bitwise AND (`&`).
- Bitwise OR (`|`).
- Bitwise XOR (`^`).
- Bitwise NOT (`~`).
- Left Shift (`<<`).
- Right Shift (`>>`).

## 2.3 Bit Manipulation

- Check whether a bit is set.
- Set a particular bit.
- Clear a particular bit.
- Toggle a particular bit.
- Count set bits.
- Check even or odd using bitwise AND.
- Create and use bit masks.

## 2.4 Programming Skills

After completing this topic, you should be able to:

1. Convert integers into binary representations.
2. Perform AND, OR, and XOR operations.
3. Understand Python's bitwise NOT behavior.
4. Perform left and right shifts.
5. Apply bit masks.
6. Check specific bit positions.
7. Set, clear, and toggle bits.
8. Count set bits efficiently.
9. Write reusable bit manipulation programs.
10. Solve beginner-level bitwise DSA problems.

---

# 3. What Are Bitwise Operators?

Bitwise operators are symbols that perform operations on individual bits of integer values.

They compare or manipulate the binary digits of numbers.

## 3.1 General Syntax

```python
value1 bitwise_operator value2
```

Example:

```python
a = 12
b = 10

result = a & b

print(result)
```

**Output:**

```text
8
```

## 3.2 How Do Bitwise Operators Work?

Consider:

```python
a = 12
b = 10

result = a & b
```

First, Python represents the values in binary:

```text
12 = 1100
10 = 1010
```

Then it applies the bitwise AND operation.

```text
1100
1010
----
1000
```

Finally, the binary result is interpreted as a decimal integer:

```text
1000 = 8
```

## 3.3 Why Do We Need Binary Representation?

The computer stores and processes data using binary representations.

Understanding binary is necessary for learning:

- Bitwise operations.
- Memory representation.
- Bit manipulation.
- Digital electronics.
- Low-level programming.
- Network addressing.
- Computer architecture.

---

# 4. Understanding Binary Number System

The binary number system is a base-2 number system.

It uses only two digits:

```text
0 and 1
```

The decimal number system is base 10 and uses digits from `0` to `9`.

The binary system is based on powers of two.

## 4.1 Decimal Number System

The decimal number system uses ten digits:

```text
0 1 2 3 4 5 6 7 8 9
```

For example:

```text
345
```

Its expanded representation is:

```text
345 = 3 × 100 + 4 × 10 + 5 × 1
```

## 4.2 Binary Number System

Binary uses only:

```text
0 and 1
```

Each position represents a power of two.

| Position | Power | Value |
|---:|---|---:|
| 0 | 2⁰ | 1 |
| 1 | 2¹ | 2 |
| 2 | 2² | 4 |
| 3 | 2³ | 8 |
| 4 | 2⁴ | 16 |
| 5 | 2⁵ | 32 |
| 6 | 2⁶ | 64 |
| 7 | 2⁷ | 128 |

## 4.3 Example: Binary Representation of 10

```text
Binary: 1010
```

Expanded form:

```text
1 × 8
0 × 4
1 × 2
0 × 1
```

Therefore:

```text
8 + 0 + 2 + 0 = 10
```

So:

```text
Decimal 10 = Binary 1010
```

## 4.4 Binary Representation of Common Numbers

| Decimal | Binary |
|---:|---|
| 0 | `0` |
| 1 | `1` |
| 2 | `10` |
| 3 | `11` |
| 4 | `100` |
| 5 | `101` |
| 6 | `110` |
| 7 | `111` |
| 8 | `1000` |
| 9 | `1001` |
| 10 | `1010` |
| 11 | `1011` |
| 12 | `1100` |
| 13 | `1101` |
| 14 | `1110` |
| 15 | `1111` |
| 16 | `10000` |
| 20 | `10100` |
| 25 | `11001` |
| 30 | `11110` |

## 4.5 Why Does Binary Matter for Bitwise Operators?

Bitwise operators operate on individual binary digits.

For example:

```python
12 & 10
```

cannot be understood properly without knowing the binary representations:

```text
12 = 1100
10 = 1010
```

Once binary conversion becomes familiar, bitwise calculations become much easier.

---

# 5. Binary Conversion

Binary conversion means converting a decimal number into its binary representation or converting a binary value into decimal.

## 5.1 Decimal to Binary Using Python

Python provides the built-in `bin()` function.

### Syntax

```python
bin(number)
```

### Example

```python
number = 10

print(bin(number))
```

**Output:**

```text
0b1010
```

The prefix `0b` indicates that the number is represented in binary notation.

## 5.2 More Examples

```python
print(bin(5))
print(bin(8))
print(bin(12))
print(bin(15))
```

**Output:**

```text
0b101
0b1000
0b1100
0b1111
```

## 5.3 Binary to Decimal Using `int()`

Python provides `int()` with a base argument.

### Syntax

```python
int(binary_string, 2)
```

### Example

```python
binary_value = "1010"

decimal_value = int(binary_value, 2)

print(decimal_value)
```

**Output:**

```text
10
```

## 5.4 Binary Conversion Manually

Consider converting decimal `13` into binary.

Repeatedly divide by 2 and record the remainders.

| Division | Quotient | Remainder |
|---|---:|---:|
| 13 ÷ 2 | 6 | 1 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Read the remainders from bottom to top:

```text
1101
```

Therefore:

```text
Decimal 13 = Binary 1101
```

## 5.5 Important Points

- `bin()` converts an integer into a binary string with a `0b` prefix.
- `int(value, 2)` converts a base-2 string into an integer.
- Binary digits are only `0` and `1`.
- The rightmost bit represents position zero.
- Python integers are not restricted to an 8-bit or 32-bit fixed width.

---

# 6. Understanding Bits and Bit Positions

A bit is the smallest unit of binary information.

It can represent either:

```text
0 or 1
```

Every position in a binary number has a corresponding power of two.

## 6.1 Example

Consider the binary number:

```text
1101
```

Its bit positions are:

```text
Position:  3  2  1  0
Binary:    1  1  0  1
```

| Bit Position | Bit Value | Place Value |
|---:|---:|---:|
| 3 | 1 | 8 |
| 2 | 1 | 4 |
| 1 | 0 | 2 |
| 0 | 1 | 1 |

Decimal value:

```text
8 + 4 + 0 + 1 = 13
```

## 6.2 Zero-Based Bit Indexing

In programming, bit positions are commonly counted from zero.

The rightmost bit is position `0`.

Example:

```text
Binary:    1 1 0 1
Position:  3 2 1 0
```

This is important when setting, clearing, checking, or toggling a specific bit.

## 6.3 Example: Checking Bit Position 1

```python
number = 10

print(bin(number))
```

Output:

```text
0b1010
```

Binary without prefix:

```text
1010
```

Positions:

```text
Position: 3 2 1 0
Bit:      1 0 1 0
```

Bit position `1` contains `1`.

## 6.4 Important Points

- The rightmost bit is position zero.
- The next bit is position one.
- Every position represents a power of two.
- Bit positions are used to create masks.
- Correctly counting bit positions is important in bit manipulation.

---

# 7. Bitwise Operator Overview

Python provides six fundamental bitwise operators.

| Operator | Name | Purpose |
|---|---|---|
| `&` | Bitwise AND | Compares corresponding bits |
| `|` | Bitwise OR | Combines corresponding bits |
| `^` | Bitwise XOR | Returns 1 when bits are different |
| `~` | Bitwise NOT | Inverts the integer's bits according to Python's integer model |
| `<<` | Left Shift | Shifts bits toward the left |
| `>>` | Right Shift | Shifts bits toward the right |

## 7.1 Quick Examples

```python
a = 12
b = 10

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
```

**Output:**

```text
8
14
6
-13
24
6
```

## 7.2 Bitwise Truth Table

| A | B | AND | OR | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

This truth table is used to understand AND, OR, and XOR.

---

# 8. Bitwise AND Operator (&)

The bitwise AND operator compares corresponding bits of two integers.

A result bit becomes `1` only when both corresponding bits are `1`.

### Syntax

```python
value1 & value2
```

## 8.1 AND Truth Table

| A | B | A & B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## 8.2 Example 1: Basic AND Operation

```python
a = 12
b = 10

result = a & b

print(result)
```

**Output:**

```text
8
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     1000
```

Decimal result:

```text
1000 = 8
```

## 8.3 Example 2: AND with Different Values

```python
a = 5
b = 3

print(a & b)
```

**Output:**

```text
1
```

Binary calculation:

```text
5 = 101
3 = 011
--------
    001
```

## 8.4 Example 3: AND with Zero

```python
number = 15

print(number & 0)
```

**Output:**

```text
0
```

AND with zero always produces zero.

## 8.5 Example 4: AND with the Same Number

```python
number = 12

print(number & number)
```

**Output:**

```text
12
```

Every bit matches itself.

## 8.6 Practical Application: Checking Whether a Bit Is Set

Suppose we want to check bit position `2`.

```python
number = 13
position = 2

mask = 1 << position

result = number & mask

if result:
    print("Bit is set.")
else:
    print("Bit is not set.")
```

**Output:**

```text
Bit is set.
```

### Explanation

Original number:

```text
13 = 1101
```

Mask:

```text
1 << 2 = 0100
```

AND operation:

```text
1101
0100
----
0100
```

The result is non-zero, so the selected bit is set.

## 8.7 Important Points

- AND returns 1 only when both bits are 1.
- AND with zero produces zero.
- AND with the same number returns the original number.
- AND is commonly used for checking and masking bits.
- It is useful in permission systems and DSA.

---

# 9. Bitwise OR Operator (|)

The bitwise OR operator compares corresponding bits.

A result bit becomes `1` when at least one corresponding bit is `1`.

### Syntax

```python
value1 | value2
```

## 9.1 OR Truth Table

| A | B | A \| B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

## 9.2 Example 1: Basic OR Operation

```python
a = 12
b = 10

result = a | b

print(result)
```

**Output:**

```text
14
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     1110
```

Decimal result:

```text
1110 = 14
```

## 9.3 Example 2: OR with Different Values

```python
a = 5
b = 3

print(a | b)
```

**Output:**

```text
7
```

Binary calculation:

```text
5 = 101
3 = 011
--------
    111
```

## 9.4 Example 3: OR with Zero

```python
number = 12

print(number | 0)
```

**Output:**

```text
12
```

OR with zero preserves the original value.

## 9.5 Example 4: OR with the Same Number

```python
number = 10

print(number | number)
```

**Output:**

```text
10
```

## 9.6 Practical Application: Setting a Bit

Suppose we want to enable bit position `1`.

```python
number = 8
position = 1

mask = 1 << position

result = number | mask

print(result)
```

**Output:**

```text
10
```

### Binary Calculation

```text
Number = 1000
Mask   = 0010
--------------
Result = 1010
```

The selected bit is set to one.

## 9.7 Important Points

- OR returns one when at least one corresponding bit is one.
- OR with zero preserves the number.
- OR is useful for enabling bits.
- OR is widely used in flags and permission management.
- OR assignment can enable selected bits without clearing other bits.

---

# 10. Bitwise XOR Operator (^)

The bitwise XOR operator compares corresponding bits.

A result bit becomes `1` when the two corresponding bits are different.

### Syntax

```python
value1 ^ value2
```

## 10.1 XOR Truth Table

| A | B | A ^ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## 10.2 Example 1: Basic XOR Operation

```python
a = 12
b = 10

result = a ^ b

print(result)
```

**Output:**

```text
6
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     0110
```

Decimal result:

```text
0110 = 6
```

## 10.3 Example 2: XOR with Different Values

```python
a = 5
b = 3

print(a ^ b)
```

**Output:**

```text
6
```

Binary calculation:

```text
5 = 101
3 = 011
--------
    110
```

## 10.4 Example 3: XOR with the Same Number

```python
number = 10

print(number ^ number)
```

**Output:**

```text
0
```

Every bit is equal to itself, so all result bits are zero.

## 10.5 Example 4: XOR with Zero

```python
number = 15

print(number ^ 0)
```

**Output:**

```text
15
```

XOR with zero preserves the original number.

## 10.6 Important XOR Properties

| Property | Expression | Result |
|---|---|---|
| Self XOR | `a ^ a` | `0` |
| XOR with zero | `a ^ 0` | `a` |
| Commutative | `a ^ b` | `b ^ a` |
| Associative | `(a ^ b) ^ c` | `a ^ (b ^ c)` |

## 10.7 Practical Application: Toggling a Bit

```python
number = 12
position = 1

mask = 1 << position

result = number ^ mask

print(result)
```

**Output:**

```text
14
```

Binary calculation:

```text
Number = 1100
Mask   = 0010
--------------
Result = 1110
```

XOR changes the selected bit from `0` to `1`.

If the selected bit was already `1`, XOR changes it to `0`.

## 10.8 Important Points

- XOR returns 1 when bits are different.
- XOR of a number with itself is zero.
- XOR with zero preserves the original number.
- XOR is commonly used to toggle bits.
- XOR is useful in many DSA problems.

---

# 11. Bitwise NOT Operator (~)

The bitwise NOT operator is used to invert the bits of an integer.

### Syntax

```python
~number
```

It is a unary operator because it works on one operand.

## 11.1 Example

```python
number = 5

result = ~number

print(result)
```

**Output:**

```text
-6
```

## 11.2 Important Python Behavior

Python integers have arbitrary precision and are not restricted to a fixed number of bits.

For Python integers, bitwise NOT follows this identity:

```text
~n = -(n + 1)
```

Therefore:

```text
~5 = -(5 + 1)
~5 = -6
```

## 11.3 More Examples

```python
print(~0)
print(~1)
print(~2)
print(~5)
print(~10)
```

**Output:**

```text
-1
-2
-3
-6
-11
```

## 11.4 Why Does NOT Produce Negative Values?

Python's integer bitwise operations use an infinite sign-extension model for negative integers.

Conceptually, for positive integers, NOT flips all bits, including infinitely many leading zero bits.

This produces a negative result.

For example, the identity:

```text
~5 = -(5 + 1)
```

gives `-6`.

## 11.5 Binary Display of Negative Numbers

```python
number = 5

print(bin(number))
print(bin(~number))
```

**Output:**

```text
0b101
-0b110
```

The second output is Python's textual binary representation of the negative integer `-6`.

It is not a complete fixed-width two's-complement bit pattern.

## 11.6 Practical Example: Inverting a Mask

Bitwise NOT is commonly used when clearing a selected bit with AND.

```python
number = 10
mask = 1 << 1

result = number & ~mask

print(result)
```

**Output:**

```text
8
```

## 11.7 Important Points

- `~` performs bitwise inversion.
- It is a unary operator.
- Python's identity is `~n = -(n + 1)`.
- Python integers are not restricted to a fixed bit width.
- Do not assume that `bin()` displays a fixed-width two's-complement pattern.
- NOT is useful for creating inverse masks.

---

# 12. Left Shift Operator (<<)

The left shift operator moves bits toward the left.

### Syntax

```python
number << positions
```

It shifts the bits by the specified number of positions.

## 12.1 Example 1: Left Shift by One

```python
number = 5

result = number << 1

print(result)
```

**Output:**

```text
10
```

### Binary Calculation

```text
5 = 0101

After shifting left by 1:

  = 1010
```

Therefore:

```text
1010 = 10
```

## 12.2 Example 2: Left Shift by Two

```python
number = 5

print(number << 2)
```

**Output:**

```text
20
```

Binary representation:

```text
5 = 0101

Shift left by 2:

  = 10100
```

## 12.3 Example 3: Left Shift by Three

```python
number = 2

print(number << 3)
```

**Output:**

```text
16
```

## 12.4 Relationship with Multiplication

For integer values, shifting left by `n` positions is equivalent to multiplying by \(2^n\).

```text
number << 1 = number × 2
number << 2 = number × 4
number << 3 = number × 8
```

Example:

```python
number = 5

print(number << 1)
print(number << 2)
print(number << 3)
```

**Output:**

```text
10
20
40
```

## 12.5 Important Points

- `<<` shifts bits to the left.
- Each shift position corresponds to a power of two.
- For integers, left shift is equivalent to multiplication by a power of two.
- The result can become a very large integer.
- The shift count must not be negative.

---

# 13. Right Shift Operator (>>)

The right shift operator moves bits toward the right.

### Syntax

```python
number >> positions
```

It shifts the bits by the specified number of positions.

## 13.1 Example 1: Right Shift by One

```python
number = 20

result = number >> 1

print(result)
```

**Output:**

```text
10
```

### Binary Calculation

```text
20 = 10100

After right shift by 1:

   = 01010
```

Decimal result:

```text
01010 = 10
```

## 13.2 Example 2: Right Shift by Two

```python
number = 20

result = number >> 2

print(result)
```

**Output:**

```text
5
```

### Binary Calculation

```text
20 = 10100

After right shift by 2:

   = 00101
```

Decimal result:

```text
00101 = 5
```

## 13.3 Example 3: Right Shift by Three

```python
number = 40

print(number >> 3)
```

**Output:**

```text
5
```

## 13.4 Relationship with Floor Division

For integers, a right shift by `n` positions is equivalent to floor division by \(2^n\).

```text
number >> 1 = number // 2
number >> 2 = number // 4
number >> 3 = number // 8
```

Example:

```python
number = 20

print(number >> 1)
print(number >> 2)
print(number >> 3)
```

**Output:**

```text
10
5
2
```

This relationship also works for negative Python integers because right shift uses sign extension.

## 13.5 Important Points

- `>>` shifts bits toward the right.
- Right shifting non-negative values removes lower-order bits.
- For integers, it corresponds to floor division by a power of two.
- The shift count must not be negative.
- Python uses arithmetic right shift behavior for negative integers.

---

# 14. Bitwise Assignment Operators

Python also supports augmented assignment versions of bitwise operators.

They combine a bitwise operation with assignment.

## 14.1 Complete Table

| Operator | Meaning | Example |
|---|---|---|
| `&=` | AND assignment | `x &= 5` |
| `|=` | OR assignment | `x |= 5` |
| `^=` | XOR assignment | `x ^= 5` |
| `<<=` | Left shift assignment | `x <<= 1` |
| `>>=` | Right shift assignment | `x >>= 1` |

## 14.2 AND Assignment (`&=`)

```python
number = 12

number &= 10

print(number)
```

**Output:**

```text
8
```

Equivalent form:

```python
number = number & 10
```

## 14.3 OR Assignment (`|=`)

```python
number = 8

number |= 3

print(number)
```

**Output:**

```text
11
```

Equivalent form:

```python
number = number | 3
```

## 14.4 XOR Assignment (`^=`)

```python
number = 12

number ^= 10

print(number)
```

**Output:**

```text
6
```

Equivalent form:

```python
number = number ^ 10
```

## 14.5 Left Shift Assignment (`<<=`)

```python
number = 5

number <<= 1

print(number)
```

**Output:**

```text
10
```

Equivalent form:

```python
number = number << 1
```

## 14.6 Right Shift Assignment (`>>=`)

```python
number = 20

number >>= 2

print(number)
```

**Output:**

```text
5
```

Equivalent form:

```python
number = number >> 2
```

## 14.7 Important Points

- Bitwise assignment updates the original variable name.
- It makes repeated bitwise updates easier to write.
- It is useful for flags and bit masks.
- The operand types must support the operation.

---

# 15. Understanding Bit Masks

A bit mask is an integer used to select, check, set, clear, or toggle particular bits.

Masks are commonly created using left shift.

## 15.1 Creating a Bit Mask

### Syntax

```python
mask = 1 << position
```

A mask contains a `1` at the selected position and zeros elsewhere.

## 15.2 Example: Creating a Mask for Position 0

```python
mask = 1 << 0

print(mask)
print(bin(mask))
```

**Output:**

```text
1
0b1
```

## 15.3 Example: Creating a Mask for Position 2

```python
mask = 1 << 2

print(mask)
print(bin(mask))
```

**Output:**

```text
4
0b100
```

## 15.4 Common Bit Masks

| Position | Expression | Decimal | Binary |
|---:|---|---:|---|
| 0 | `1 << 0` | 1 | `1` |
| 1 | `1 << 1` | 2 | `10` |
| 2 | `1 << 2` | 4 | `100` |
| 3 | `1 << 3` | 8 | `1000` |
| 4 | `1 << 4` | 16 | `10000` |
| 5 | `1 << 5` | 32 | `100000` |

## 15.5 Why Are Masks Useful?

Masks allow programmers to work with individual bits without changing unrelated bits.

For example:

- Check whether a permission is active.
- Enable a feature.
- Disable a feature.
- Toggle a status.
- Store multiple Boolean flags in one integer.

---

# 16. Set, Clear, Toggle, and Check Bits

These four operations are fundamental bit manipulation techniques.

## 16.1 Checking Whether a Bit Is Set

To check a particular bit, use bitwise AND with a mask.

### Formula

```python
number & (1 << position)
```

If the result is non-zero, the selected bit is set.

### Example

```python
number = 10
position = 1

mask = 1 << position

if number & mask:
    print("Bit is set.")
else:
    print("Bit is not set.")
```

**Output:**

```text
Bit is set.
```

### Binary Explanation

```text
Number = 1010
Mask   = 0010
--------------
Result = 0010
```

The selected bit is `1`.

## 16.2 Setting a Particular Bit

Setting a bit means changing it to `1`.

### Formula

```python
number | (1 << position)
```

### Example

```python
number = 8
position = 1

mask = 1 << position

result = number | mask

print(result)
```

**Output:**

```text
10
```

### Binary Explanation

```text
Number = 1000
Mask   = 0010
--------------
Result = 1010
```

## 16.3 Clearing a Particular Bit

Clearing a bit means changing it to `0`.

### Formula

```python
number & ~(1 << position)
```

### Example

```python
number = 10
position = 1

mask = 1 << position

result = number & ~mask

print(result)
```

**Output:**

```text
8
```

### Binary Explanation

For the lowest four bits:

```text
Number      = 1010
Mask        = 0010
Inverse Mask= 1101
-------------------
Result      = 1000
```

The selected bit is cleared.

## 16.4 Toggling a Particular Bit

Toggling means reversing a selected bit:

- `0` becomes `1`.
- `1` becomes `0`.

### Formula

```python
number ^ (1 << position)
```

### Example

```python
number = 10
position = 1

mask = 1 << position

result = number ^ mask

print(result)
```

**Output:**

```text
8
```

### Binary Explanation

```text
Number = 1010
Mask   = 0010
--------------
Result = 1000
```

The selected bit changes from `1` to `0`.

## 16.5 Complete Bit Manipulation Summary

| Operation | Formula | Purpose |
|---|---|---|
| Check | `n & (1 << p)` | Check whether bit `p` is set |
| Set | `n | (1 << p)` | Change bit `p` to 1 |
| Clear | `n & ~(1 << p)` | Change bit `p` to 0 |
| Toggle | `n ^ (1 << p)` | Reverse bit `p` |

Here:

- `n` represents the original integer.
- `p` represents the zero-based bit position.

## 16.6 Important Points

- Bit positions start from zero.
- A mask is created using `1 << position`.
- AND is commonly used for checking bits.
- OR is commonly used for setting bits.
- AND with an inverted mask is used for clearing bits.
- XOR is commonly used for toggling bits.

---

# 17. Counting Set Bits

A set bit is a binary digit whose value is `1`.

Counting set bits means calculating how many binary positions contain `1`.

## 17.1 Example

Consider:

```text
Number = 13
Binary = 1101
```

The number of set bits is:

```text
3
```

Because the binary representation contains three `1` digits.

## 17.2 Method 1: Using `bin()` and `count()`

```python
number = 13

count = bin(number).count("1")

print(count)
```

**Output:**

```text
3
```

This method is easy to understand for beginner programs.

## 17.3 Method 2: Using a Loop and Right Shift

```python
number = 13
count = 0

while number > 0:
    count += number & 1
    number >>= 1

print(count)
```

**Output:**

```text
3
```

### Explanation

1. AND with `1` checks the rightmost bit.
2. Add that bit to the counter.
3. Shift the number one position right.
4. Repeat until the number becomes zero.

## 17.4 Method 3: Brian Kernighan's Algorithm

This algorithm repeatedly clears the lowest set bit.

### Code

```python
number = 13
count = 0

while number > 0:
    number &= number - 1
    count += 1

print(count)
```

**Output:**

```text
3
```

### Why Does It Work?

When we subtract `1` from a positive integer, the lowest set bit becomes zero and the bits below it become ones.

Applying AND between the original value and the value after subtraction clears the lowest set bit.

### Example

Initial value:

```text
13 = 1101
```

First iteration:

```text
1101
1100
----
1100
```

One set bit has been cleared.

Second iteration:

```text
1100
1011
----
1000
```

Another set bit has been cleared.

Third iteration:

```text
1000
0111
----
0000
```

The third set bit has been cleared.

The loop stops because the number becomes zero.

Total number of set bits:

```text
3
```

## 17.5 Important Points

- A set bit has value `1`.
- Counting set bits is a common DSA problem.
- `bin(number).count("1")` is a simple approach for non-negative integers.
- Brian Kernighan's algorithm runs in O(k) bit-clearing iterations, where `k` is the number of set bits.
- The loop in this program accepts only non-negative values.

---

# 18. Python Binary Representation

Python provides several useful ways to display and convert binary values.

## 18.1 Using `bin()`

```python
number = 10

print(bin(number))
```

**Output:**

```text
0b1010
```

## 18.2 Using `format()`

```python
number = 10

print(format(number, "b"))
```

**Output:**

```text
1010
```

## 18.3 Using Formatted Strings

```python
number = 10

print(f"{number:b}")
```

**Output:**

```text
1010
```

## 18.4 Displaying Binary with a Fixed Minimum Width

```python
number = 5

print(format(number, "08b"))
```

**Output:**

```text
00000101
```

This displays at least eight binary digits, adding leading zeros when necessary.

It is useful for visualizing a fixed-width representation, but it does not change Python's underlying integer type.

## 18.5 Converting Binary to Decimal

```python
binary_number = "1101"

decimal_number = int(binary_number, 2)

print(decimal_number)
```

**Output:**

```text
13
```

## 18.6 Important Points

- `bin()` adds the `0b` prefix.
- `format(number, "b")` displays binary digits without the prefix.
- `int(value, 2)` converts a base-2 string.
- Formatting to eight digits does not make the underlying integer an eight-bit integer.

---

# 19. Bitwise Operators vs Logical Operators

Bitwise operators and logical operators are different.

They may look similar, but their purposes are not the same.

## 19.1 Logical AND

```python
print(True and False)
```

**Output:**

```text
False
```

It combines truth values.

## 19.2 Bitwise AND

```python
print(5 & 3)
```

**Output:**

```text
1
```

It performs an operation on the binary digits.

## 19.3 Comparison Table

| Logical Operators | Bitwise Operators |
|---|---|
| `and` | `&` |
| `or` | `|` |
| `not` | `~` for integer inversion |
| Used for condition logic | Used for bit manipulation |
| AND and OR short-circuit | Bitwise operations do not short-circuit |
| `True and False` | `5 & 3` |

## 19.4 When Should You Use Each?

Use logical operators when:

- Checking multiple conditions.
- Writing `if` statements.
- Validating user input.
- Controlling loops.

Use bitwise operators when:

- Manipulating binary data.
- Working with bit masks.
- Setting or clearing flags.
- Solving bit manipulation problems.

---

# 20. Understanding the Python Program

**File Name:** `01_bitwise_operators.py`

The program is divided into multiple sections to make learning and practice easier.

## 20.1 Module Documentation

The program begins with a module-level docstring.

It explains:

- The topic name.
- The purpose of the program.
- The bitwise operators included.
- The augmented assignment operators.
- The program sections.

This helps developers understand the purpose of the file.

## 20.2 Helper Functions

The program includes four helper functions.

| Function | Purpose |
|---|---|
| `print_heading()` | Displays formatted headings. |
| `read_int()` | Reads a valid integer. |
| `read_non_negative_int()` | Reads a non-negative integer. |
| `read_bit_position()` | Reads a bit position between 0 and 1024. |
| `print_binary()` | Displays an integer and its binary representation. |

### Why Are These Functions Useful?

- They reduce repeated code.
- They keep input validation consistent.
- They improve readability.
- They make the program easier to maintain.
- They separate input handling from calculations.

## 20.3 Section 1: Twelve Examples

| No. | Example | Concept |
|---:|---|---|
| 1 | Binary representation | `bin()` |
| 2 | Bitwise AND | `&` |
| 3 | Bitwise OR | `|` |
| 4 | Bitwise XOR | `^` |
| 5 | Bitwise NOT | `~` |
| 6 | Left shift | `<<` |
| 7 | Right shift | `>>` |
| 8 | AND assignment | `&=` |
| 9 | OR assignment | `|=` |
| 10 | XOR assignment | `^=` |
| 11 | Shift assignment | `<<=`, `>>=` |
| 12 | Bit mask operations | Check, set, clear, toggle |

## 20.4 Section 2: Twelve Solved Problems

The second section contains twelve practical programs.

These problems cover:

1. Bitwise AND.
2. Bitwise OR.
3. Bitwise XOR.
4. Bitwise NOT.
5. Left shift.
6. Right shift.
7. Even or odd using bitwise AND.
8. Checking a particular bit.
9. Setting a particular bit.
10. Clearing a particular bit.
11. Toggling a particular bit.
12. Counting set bits.

## 20.5 `SOLVED_PROBLEMS` Dictionary

The program uses a dictionary named:

```python
SOLVED_PROBLEMS
```

It connects each problem number with:

- The problem description.
- Its corresponding function.

This allows problems to be selected and executed using their numbers.

## 20.6 `show_solved_problems()`

This function displays all twelve solved problems.

It helps users identify the problem they want to practise.

## 20.7 `run_solved_problems()`

This function:

1. Displays all twelve problems.
2. Accepts the selected problem number.
3. Validates the selection.
4. Executes the corresponding function.
5. Displays the result.
6. Allows the user to continue or return to the menu.

## 20.8 Section 3: Ten Unsolved Questions

This section contains ten independent practice questions.

Each question includes a hint.

The purpose is to help students practise bit manipulation without immediately viewing complete solutions.

## 20.9 Section 4: Learning Checklist

The checklist contains important bitwise concepts.

Use it to review your progress.

## 20.10 Section 5: Main Menu

The main menu connects every section.

| Option | Action |
|---:|---|
| 1 | View twelve examples |
| 2 | Practise twelve solved problems |
| 3 | View ten unsolved questions |
| 4 | View learning checklist |
| 0 | Exit |

---

# 21. Twelve Examples Explained

This section explains the twelve examples included in `01_bitwise_operators.py`.

## Example 1: Binary Representation

**Concept:** `bin()`

Purpose:

- Display integer values in binary.
- Understand the binary number system.

Code:

```python
a = 10
b = 5

print(bin(a))
print(bin(b))
```

**Output:**

```text
0b1010
0b101
```

Explanation:

- Decimal `10` becomes binary `1010`.
- Decimal `5` becomes binary `101`.

The prefix `0b` indicates binary notation.

## Example 2: Bitwise AND

**Concept:** `&`

Code:

```python
a = 12
b = 10

result = a & b

print(result)
print(bin(result))
```

**Output:**

```text
8
0b1000
```

Binary calculation:

```text
1100
1010
----
1000
```

## Example 3: Bitwise OR

**Concept:** `|`

Code:

```python
a = 12
b = 10

result = a | b

print(result)
print(bin(result))
```

**Output:**

```text
14
0b1110
```

A result bit becomes one when either corresponding bit is one.

## Example 4: Bitwise XOR

**Concept:** `^`

Code:

```python
a = 12
b = 10

result = a ^ b

print(result)
print(bin(result))
```

**Output:**

```text
6
0b110
```

A result bit becomes one when the corresponding bits are different.

## Example 5: Bitwise NOT

**Concept:** `~`

Code:

```python
number = 5

result = ~number

print(result)
print(-(number + 1))
```

**Output:**

```text
-6
-6
```

Python follows:

```text
~n = -(n + 1)
```

## Example 6: Left Shift

**Concept:** `<<`

Code:

```python
number = 5

result = number << 1

print(result)
print(bin(result))
```

**Output:**

```text
10
0b1010
```

The bits shift one position to the left.

## Example 7: Right Shift

**Concept:** `>>`

Code:

```python
number = 20

result = number >> 2

print(result)
print(bin(result))
```

**Output:**

```text
5
0b101
```

The bits shift two positions to the right.

## Example 8: AND Assignment

**Concept:** `&=`

Code:

```python
number = 12

number &= 10

print(number)
```

**Output:**

```text
8
```

The result of bitwise AND is assigned back to `number`.

## Example 9: OR Assignment

**Concept:** `|=`

Code:

```python
number = 8

number |= 3

print(number)
```

**Output:**

```text
11
```

OR assignment enables the selected bits.

## Example 10: XOR Assignment

**Concept:** `^=`

Code:

```python
number = 12

number ^= 10

print(number)
```

**Output:**

```text
6
```

XOR assignment toggles the bits selected by the second operand.

## Example 11: Shift Assignment

**Concept:** `<<=` and `>>=`

Code:

```python
left_number = 5
right_number = 20

left_number <<= 1
right_number >>= 2

print(left_number)
print(right_number)
```

**Output:**

```text
10
5
```

The first operation shifts left, and the second shifts right.

## Example 12: Bit Mask Operations

**Concept:** Check, set, clear, and toggle bits.

Code:

```python
number = 10
position = 1

mask = 1 << position

print("Is Bit Set:", bool(number & mask))

set_result = number | mask
print("After Setting Bit:", set_result)

clear_result = number & ~mask
print("After Clearing Bit:", clear_result)

toggle_result = number ^ mask
print("After Toggling Bit:", toggle_result)
```

**Output:**

```text
Is Bit Set: True
After Setting Bit: 10
After Clearing Bit: 8
After Toggling Bit: 8
```

### Explanation

Original number:

```text
10 = 1010
```

Selected position:

```text
1
```

Mask:

```text
1 << 1 = 0010
```

The selected bit is already set.

Therefore:

- Checking returns true.
- Setting leaves the number unchanged.
- Clearing changes `1010` to `1000`.
- Toggling changes `1010` to `1000`.

---

# 22. Twelve Solved Programming Problems

This section explains the twelve practical problems included in the Python file.

Each problem includes:

1. Problem statement.
2. Required operator.
3. Logic.
4. Example code.
5. Expected output.
6. Binary calculation.
7. Learning point.

---

## Problem 1: Perform Bitwise AND

**Concept:** Bitwise AND (`&`)

### Problem Statement

Accept two integers and perform a bitwise AND operation.

### Logic

1. Accept the first integer.
2. Accept the second integer.
3. Apply bitwise AND.
4. Display the decimal result.
5. Display the binary result.

### Example Code

```python
a = 12
b = 10

result = a & b

print("AND Result:", result)
print("Binary Result:", bin(result))
```

### Output

```text
AND Result: 8
Binary Result: 0b1000
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     1000
```

### Explanation

Only corresponding bits that are both one remain one.

### Learning Point

AND is frequently used for checking and masking bits.

---

## Problem 2: Perform Bitwise OR

**Concept:** Bitwise OR (`|`)

### Problem Statement

Accept two integers and perform a bitwise OR operation.

### Example Code

```python
a = 12
b = 10

result = a | b

print("OR Result:", result)
```

### Output

```text
OR Result: 14
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     1110
```

### Explanation

At least one corresponding bit is one in every result position except the rightmost two positions.

### Learning Point

OR is useful for enabling selected bits.

---

## Problem 3: Perform Bitwise XOR

**Concept:** Bitwise XOR (`^`)

### Problem Statement

Accept two integers and perform a bitwise XOR operation.

### Example Code

```python
a = 12
b = 10

result = a ^ b

print("XOR Result:", result)
```

### Output

```text
XOR Result: 6
```

### Binary Calculation

```text
12 = 1100
10 = 1010
------------
     0110
```

### Explanation

Only positions where the two bits differ become one.

### Learning Point

XOR is useful for toggling bits and solving several DSA problems.

---

## Problem 4: Perform Bitwise NOT

**Concept:** Bitwise NOT (`~`)

### Problem Statement

Accept an integer and calculate its bitwise NOT result.

### Example Code

```python
number = 5

result = ~number

print("NOT Result:", result)
```

### Output

```text
NOT Result: -6
```

### Explanation

Python's integer behavior follows:

```text
~n = -(n + 1)
```

Therefore:

```text
~5 = -(5 + 1)
~5 = -6
```

### Learning Point

Understand Python's negative integer behavior before using NOT in more advanced bit manipulation.

---

## Problem 5: Perform Left Shift

**Concept:** Left shift (`<<`)

### Problem Statement

Accept an integer and a shift count. Move its bits toward the left.

### Logic

1. Read the integer.
2. Read the shift count.
3. Validate the shift count.
4. Apply the left shift.
5. Display the decimal and binary results.

### Example Code

```python
number = 5
positions = 2

result = number << positions

print("Left Shift Result:", result)
```

### Output

```text
Left Shift Result: 20
```

### Binary Calculation

```text
5 = 00101

Shift left by 2:

  = 10100
```

### Learning Point

Left shift multiplies the integer by a power of two.

---

## Problem 6: Perform Right Shift

**Concept:** Right shift (`>>`)

### Problem Statement

Accept an integer and a shift count. Move its bits toward the right.

### Example Code

```python
number = 20
positions = 2

result = number >> positions

print("Right Shift Result:", result)
```

### Output

```text
Right Shift Result: 5
```

### Binary Calculation

```text
20 = 10100

Shift right by 2:

   = 00101
```

### Learning Point

Right shift corresponds to floor division by a power of two.

---

## Problem 7: Check Even or Odd Using Bitwise AND

**Concept:** Bitwise AND (`&`)

### Problem Statement

Accept an integer and determine whether it is even or odd using the lowest bit.

### Logic

1. Accept an integer.
2. Perform AND with `1`.
3. If the result is non-zero, the number is odd.
4. Otherwise, it is even.

### Example Code

```python
number = 15

if number & 1:
    print("ODD")
else:
    print("EVEN")
```

### Output

```text
ODD
```

### Binary Explanation

```text
15 = 1111
 1 = 0001
---------
     0001
```

The result is one, so the number is odd.

### Another Example

```python
number = 14

print(number & 1)
```

Output:

```text
0
```

The number is even.

### Learning Point

The last binary bit indicates parity:

- Last bit `0`: Even.
- Last bit `1`: Odd.

This method also works for negative integers in Python.

---

## Problem 8: Check Whether a Particular Bit Is Set

**Concept:** AND (`&`) and left shift (`<<`)

### Problem Statement

Accept a non-negative integer and a bit position. Determine whether that bit is set.

### Logic

1. Accept the integer.
2. Accept the bit position.
3. Create a mask using `1 << position`.
4. Apply bitwise AND.
5. If the result is non-zero, the bit is set.

### Example Code

```python
number = 10
position = 1

mask = 1 << position

result = number & mask

if result:
    print("Bit is set.")
else:
    print("Bit is not set.")
```

### Output

```text
Bit is set.
```

### Binary Calculation

```text
Number = 1010
Mask   = 0010
--------------
Result = 0010
```

### Learning Point

AND is the standard operation for checking a selected bit.

---

## Problem 9: Set a Particular Bit

**Concept:** OR (`|`) and left shift (`<<`)

### Problem Statement

Accept a non-negative integer and a bit position. Set that bit to one.

### Example Code

```python
number = 8
position = 1

mask = 1 << position

result = number | mask

print("Updated Number:", result)
```

### Output

```text
Updated Number: 10
```

### Binary Calculation

```text
Number = 1000
Mask   = 0010
--------------
Result = 1010
```

### Explanation

The selected bit changes from `0` to `1`.

If the bit was already one, the number remains unchanged.

### Learning Point

OR is used to set selected bits.

---

## Problem 10: Clear a Particular Bit

**Concept:** AND (`&`), NOT (`~`), and left shift (`<<`)

### Problem Statement

Accept a non-negative integer and a bit position. Clear that bit.

### Example Code

```python
number = 10
position = 1

mask = 1 << position

result = number & ~mask

print("Updated Number:", result)
```

### Output

```text
Updated Number: 8
```

### Binary Calculation

Considering the lowest four positions:

```text
Number       = 1010
Mask         = 0010
Inverse Mask = 1101
-------------------
Result       = 1000
```

### Learning Point

AND with an inverted mask clears a selected bit.

---

## Problem 11: Toggle a Particular Bit

**Concept:** XOR (`^`) and left shift (`<<`)

### Problem Statement

Accept a non-negative integer and a bit position. Toggle that bit.

### Example Code

```python
number = 10
position = 1

mask = 1 << position

result = number ^ mask

print("Updated Number:", result)
```

### Output

```text
Updated Number: 8
```

### Binary Calculation

```text
Number = 1010
Mask   = 0010
--------------
Result = 1000
```

### Explanation

The selected bit changes from `1` to `0`.

If the selected bit were zero, it would become one.

### Learning Point

XOR is useful when a bit must be reversed without changing other bits.

---

## Problem 12: Count Set Bits

**Concept:** AND (`&`), subtraction (`-`), and assignment (`&=`)

### Problem Statement

Accept a non-negative integer and count how many binary digits have the value one.

### Logic

1. Accept a non-negative integer.
2. Create a counter initialized to zero.
3. Repeatedly clear the lowest set bit.
4. Increase the counter after each operation.
5. Stop when the number becomes zero.

### Example Code

```python
number = 13

original_number = number
count = 0

while number > 0:
    number &= number - 1
    count += 1

print("Original Number:", original_number)
print("Number of Set Bits:", count)
```

### Output

```text
Original Number: 13
Number of Set Bits: 3
```

### Binary Representation

```text
13 = 1101
```

There are three set bits.

### Dry Run

| Iteration | Number Before | Number After Clearing Lowest Set Bit | Count |
|---:|---|---|---:|
| 1 | `1101` | `1100` | 1 |
| 2 | `1100` | `1000` | 2 |
| 3 | `1000` | `0000` | 3 |

The number becomes zero after three iterations.

### Learning Point

Brian Kernighan's algorithm is an efficient method for counting set bits.

---

# 23. Ten Unsolved Practice Questions

Solve the following problems independently.

Try to identify the correct bitwise operator before writing the program.

## Question 1: Perform Bitwise AND

**Concept:** `&`

Write a program that:

1. Accepts two integers.
2. Performs bitwise AND.
3. Displays the decimal result.
4. Displays the binary result.

**Hint:** Use `&`.

## Question 2: Perform Bitwise OR

**Concept:** `|`

Accept two integers and perform bitwise OR.

Display the result in decimal and binary.

**Hint:** Use `|`.

## Question 3: Perform Bitwise XOR

**Concept:** `^`

Accept two integers and perform bitwise XOR.

Display the result.

**Hint:** Use `^`.

## Question 4: Perform Bitwise NOT

**Concept:** `~`

Accept an integer and display its bitwise NOT result.

Also verify the formula:

```python
~number == -(number + 1)
```

**Hint:** Use the unary NOT operator.

## Question 5: Perform Left Shift

**Concept:** `<<`

Accept an integer and a shift count.

Display the result after shifting left.

**Hint:** Use the left shift operator.

## Question 6: Perform Right Shift

**Concept:** `>>`

Accept an integer and a shift count.

Display the result after shifting right.

**Hint:** Use the right shift operator.

## Question 7: Check Whether a Selected Bit Is Set

**Concept:** `&` and `<<`

Accept a non-negative number and a bit position.

Check whether that bit contains one.

**Hint:** Create a mask using:

```python
1 << position
```

Then use AND.

## Question 8: Set the Second Bit

**Concept:** `|` and `<<`

Accept a non-negative integer and set the bit at position `2`.

Display the updated number.

**Hint:** Use OR with a mask.

## Question 9: Toggle the Third Bit

**Concept:** `^` and `<<`

Accept a non-negative integer and toggle bit position `3`.

Display the updated value.

**Hint:** Use XOR with a mask.

## Question 10: Count Set Bits

**Concept:** Bit manipulation

Accept a non-negative integer and calculate the number of set bits.

**Hint:** Use a loop and repeatedly clear the lowest set bit.

---

# 24. Dry Run and Output Prediction

Dry running means manually tracing the execution of a program to understand how values change.

It is an important skill for practical examinations and DSA interviews.

## Question 1

Predict the output:

```python
a = 12
b = 10

print(a & b)
print(a | b)
print(a ^ b)
```

### Answer

```text
8
14
6
```

### Explanation

```text
12 = 1100
10 = 1010

AND = 1000 = 8
OR  = 1110 = 14
XOR = 0110 = 6
```

## Question 2

Predict the output:

```python
number = 5

print(number << 1)
print(number << 2)
```

### Answer

```text
10
20
```

## Question 3

Predict the output:

```python
number = 20

print(number >> 1)
print(number >> 2)
```

### Answer

```text
10
5
```

## Question 4

Predict the output:

```python
number = 5

print(~number)
```

### Answer

```text
-6
```

## Question 5

Predict the output:

```python
print(10 & 1)
print(11 & 1)
```

### Answer

```text
0
1
```

The first number is even, and the second is odd.

## Question 6

Predict the output:

```python
number = 8

number |= 2

print(number)
```

### Answer

```text
10
```

## Question 7

Predict the output:

```python
number = 12

number ^= 10

print(number)
```

### Answer

```text
6
```

## Question 8

Predict the output:

```python
number = 10
mask = 1 << 1

print(number & mask)
```

### Answer

```text
2
```

## Question 9

Predict the output:

```python
number = 13
count = 0

while number > 0:
    number &= number - 1
    count += 1

print(count)
```

### Answer

```text
3
```

## Question 10

Predict the output:

```python
a = 5
b = 3

a ^= b
b ^= a
a ^= b

print(a, b)
```

### Answer

```text
3 5
```

This is an XOR-based swapping technique for integer values, although ordinary Python swapping with `a, b = b, a` is clearer and generally preferable.

---

# 25. Common Programming Mistakes

Understanding common mistakes helps you write accurate bitwise programs.

## Mistake 1: Confusing Logical AND and Bitwise AND

Logical AND:

```python
True and False
```

Output:

```text
False
```

Bitwise AND:

```python
5 & 3
```

Output:

```text
1
```

These are different operations.

## Mistake 2: Using OR Instead of XOR

OR:

```python
5 | 3
```

Output:

```text
7
```

XOR:

```python
5 ^ 3
```

Output:

```text
6
```

OR sets a result bit when either bit is one.

XOR sets a result bit when the bits are different.

## Mistake 3: Forgetting Zero-Based Bit Positions

Incorrect understanding:

```text
Rightmost bit = position 1
```

Correct:

```text
Rightmost bit = position 0
```

Always start counting bit positions from zero.

## Mistake 4: Using the Wrong Mask

Incorrect:

```python
mask = position << 1
```

Correct:

```python
mask = 1 << position
```

The correct expression creates a mask with one selected bit.

## Mistake 5: Incorrect Bit Clearing

Incorrect:

```python
result = number & mask
```

This checks or selects bits. It does not clear a selected bit by itself.

Correct:

```python
result = number & ~mask
```

## Mistake 6: Forgetting Python's Negative NOT Behavior

```python
print(~5)
```

Output:

```text
-6
```

Use the identity:

```text
~n = -(n + 1)
```

Do not assume a fixed eight-bit NOT result unless you explicitly restrict and format values to that width.

## Mistake 7: Using a Negative Shift Count

Incorrect:

```python
number = 10
print(number << -1)
```

This raises a `ValueError`.

Shift counts must be non-negative integers.

## Mistake 8: Forgetting That Integers Are Not Fixed-Width

Python integers can represent arbitrarily large values.

Do not assume all Python integer operations automatically wrap around at 8, 16, or 32 bits.

## Mistake 9: Counting Bits Only for Positive Values Without Validation

The simple set-bit counting loop:

```python
while number > 0:
    ...
```

is intended for non-negative integers.

Validate the input before using it.

## Mistake 10: Confusing Decimal and Binary

For example:

```python
number = 1010
```

This creates decimal one thousand ten, not binary ten.

To represent binary ten using a string:

```python
number = int("1010", 2)
```

Result:

```text
10
```

---

# 26. Error Handling and Input Validation

Input validation ensures that a program receives acceptable input before performing calculations.

## 26.1 Handling Invalid Integer Input

```python
try:
    number = int(input("Enter an integer: "))
    print(number)
except ValueError:
    print("Please enter a valid integer.")
```

If the entered value is not a valid integer, Python raises a `ValueError`.

## 26.2 Validating Non-Negative Numbers

```python
number = int(input("Enter a number: "))

if number >= 0:
    print("Valid non-negative number.")
else:
    print("Please enter a non-negative number.")
```

## 26.3 Validating Bit Position

```python
position = int(input("Enter bit position: "))

if position >= 0:
    mask = 1 << position
    print(mask)
else:
    print("Bit position cannot be negative.")
```

## 26.4 Validating a Shift Count

```python
number = 10
positions = int(input("Enter shift count: "))

if positions >= 0:
    print(number << positions)
else:
    print("Shift count cannot be negative.")
```

## 26.5 Why Is Validation Important?

- Prevents invalid shift operations.
- Prevents unexpected exceptions.
- Ensures bit positions are valid.
- Makes programs easier to use.
- Improves reliability.

---

# 27. Best Practices

Follow these practices while writing bitwise programs.

1. Understand binary representation before performing bit manipulation.
2. Count bit positions from zero.
3. Use `bin()` when debugging binary operations.
4. Use descriptive variable names such as `mask`, `position`, and `result`.
5. Create masks using `1 << position`.
6. Use AND to check bits.
7. Use OR to set bits.
8. Use AND with an inverted mask to clear bits.
9. Use XOR to toggle bits.
10. Validate shift counts.
11. Validate integer inputs.
12. Remember Python's negative integer behavior.
13. Avoid assuming a fixed integer width.
14. Use parentheses to make complex bitwise expressions readable.
15. Test operations with different binary patterns.
16. Use built-in functions when they make the code simpler.
17. Understand the time complexity of bit manipulation algorithms.

---

# 28. Real-World Applications

Bitwise operators are used in many areas of software development.

## 28.1 Permission Management

Different permissions can be represented using individual bits.

```python
READ = 1
WRITE = 2
EXECUTE = 4

permissions = READ | WRITE

print(permissions)
```

**Output:**

```text
3
```

The number `3` represents the combined READ and WRITE flags.

Checking permissions:

```python
if permissions & READ:
    print("Read permission enabled.")
```

## 28.2 Feature Flags

Applications can store several enabled or disabled features in one integer.

```python
FEATURE_A = 1
FEATURE_B = 2
FEATURE_C = 4

features = FEATURE_A | FEATURE_C

print(features)
```

**Output:**

```text
5
```

## 28.3 Networking

Bitwise AND is used when working with network addresses and subnet masks.

A simplified example:

```python
ip_value = 192
mask = 240

network_part = ip_value & mask

print(network_part)
```

**Output:**

```text
192
```

Actual IP subnet calculations operate on complete IP addresses and their corresponding masks.

## 28.4 Graphics and Colors

Some graphics systems store color channels inside packed integers.

Bitwise shifts and masks can extract individual channels.

Example:

```python
color = 0xFF336699

red = (color >> 16) & 0xFF
green = (color >> 8) & 0xFF
blue = color & 0xFF

print(red, green, blue)
```

**Output:**

```text
51 102 153
```

## 28.5 Game Development

Game applications can use bits to store player status.

```python
IS_ALIVE = 1
HAS_KEY = 2
IS_INVISIBLE = 4

status = IS_ALIVE | HAS_KEY

print(status)
```

**Output:**

```text
3
```

## 28.6 Data Compression

Bit-level operations can help encode information compactly.

A compression system may store multiple small values inside a single sequence of bits.

## 28.7 Low-Level Programming

Bitwise operations are useful in:

- Hardware registers.
- Device control.
- Embedded systems.
- Processor instructions.
- Binary protocol parsing.

---

# 29. Bitwise Operators in DSA

Bitwise operations are important in Data Structures and Algorithms, especially in competitive programming.

Many DSA problems can be solved efficiently using bit manipulation.

## 29.1 Checking Even or Odd

```python
number = 15

if number & 1:
    print("Odd")
else:
    print("Even")
```

The lowest bit determines whether an integer is even or odd.

## 29.2 Checking Whether a Number Is a Power of Two

A positive integer is a power of two when exactly one bit is set.

An important property is:

```python
n & (n - 1) == 0
```

for positive powers of two.

Example:

```python
number = 16

if number > 0 and (number & (number - 1)) == 0:
    print("Power of Two")
else:
    print("Not a Power of Two")
```

**Output:**

```text
Power of Two
```

## 29.3 Counting Set Bits

```python
number = 13
count = 0

while number > 0:
    number &= number - 1
    count += 1

print(count)
```

**Output:**

```text
3
```

## 29.4 Finding the Unique Element

Suppose every element appears twice except one element.

XOR can identify the unique element.

```python
numbers = [4, 1, 2, 1, 2]

result = 0

for number in numbers:
    result ^= number

print(result)
```

**Output:**

```text
4
```

### Why Does It Work?

XOR properties:

```text
a ^ a = 0
a ^ 0 = a
```

Duplicate values cancel each other.

The remaining value is the unique element.

## 29.5 Finding the Lowest Set Bit

```python
number = 12

lowest_set_bit = number & -number

print(lowest_set_bit)
```

**Output:**

```text
4
```

For non-zero integers, `n & -n` isolates the lowest set bit as a power of two.

## 29.6 Bit Masking

Bit masks help represent subsets of a small collection.

For example, a three-bit mask can represent selections from three elements:

| Mask | Selected Positions |
|---|---|
| `000` | None |
| `001` | Position 0 |
| `010` | Position 1 |
| `011` | Positions 0 and 1 |
| `100` | Position 2 |
| `101` | Positions 0 and 2 |
| `110` | Positions 1 and 2 |
| `111` | All three positions |

There are:

```text
2³ = 8
```

possible subsets.

## 29.7 Important DSA Applications

| DSA Topic | Bitwise Usage |
|---|---|
| Number Theory | Parity and divisibility |
| Bit Manipulation | Set, clear, toggle |
| Arrays | Unique element problems |
| Dynamic Programming | Bitmask DP |
| Subsets | Represent subset selections |
| Graph Algorithms | Store visited flags |
| Competitive Programming | Fast bit operations |
| Mathematics | Power of two checks |
| Searching | Binary representation |
| Combinatorics | Subset generation |

---

# 30. Time and Space Complexity

Bitwise operations are generally efficient.

However, their actual complexity depends on integer size and the algorithm in which they are used.

## 30.1 Basic Bitwise Operations

Examples:

```python
a & b
a | b
a ^ b
~a
a << 1
a >> 1
```

For fixed-width integers, these are commonly treated as O(1).

Python integers can grow arbitrarily large, so operations involving very large integers depend on their number of internal digits.

## 30.2 Checking a Particular Bit

```python
number & (1 << position)
```

For ordinary small integers, this is generally treated as O(1).

## 30.3 Setting or Clearing a Bit

```python
number | (1 << position)
```

```python
number & ~(1 << position)
```

These operations are efficient and commonly used in bit manipulation.

## 30.4 Counting Set Bits with Brian Kernighan's Algorithm

The algorithm clears one set bit per iteration.

If there are `k` set bits, it performs `k` iterations.

Time complexity:

```text
O(k)
```

Since `k` cannot exceed the number of binary digits, this is also bounded by the integer's bit length.

Auxiliary space complexity:

```text
O(1)
```

for the loop variables.

## 30.5 Binary String Counting

```python
bin(number).count("1")
```

This creates a binary string and counts its one characters.

Its time and auxiliary space depend on the bit length of the integer.

## 30.6 Complexity Summary

| Operation | Typical Complexity |
|---|---|
| Bitwise AND | O(1) for fixed-width integers |
| Bitwise OR | O(1) for fixed-width integers |
| Bitwise XOR | O(1) for fixed-width integers |
| Bitwise NOT | O(1) for fixed-width integers |
| Left shift | Depends on integer size |
| Right shift | Depends on integer size |
| Check a bit | Depends on integer size |
| Set a bit | Depends on integer size |
| Clear a bit | Depends on integer size |
| Toggle a bit | Depends on integer size |
| Count set bits using Kernighan's algorithm | O(k) iterations |

**Note:** Python uses arbitrary-precision integers. Complexity statements for O(1) bitwise operations usually assume fixed-width machine integers or small integer sizes.

---

# 31. Interview and Viva Questions

Prepare these questions for college practical examinations and technical interviews.

## Section A: Basic Concepts

**Q1. What are bitwise operators?**

Bitwise operators perform operations on individual bits of integer values.

**Q2. What is a bit?**

A bit is a binary digit that can be either `0` or `1`.

**Q3. What is the binary number system?**

It is a base-2 number system that uses only zero and one.

**Q4. How many fundamental bitwise operators are available in Python?**

Six.

**Q5. Name the six bitwise operators.**

`&`, `|`, `^`, `~`, `<<`, and `>>`.

**Q6. Which function converts an integer to a binary string?**

`bin()`.

**Q7. What does the `0b` prefix represent?**

It indicates binary notation.

**Q8. What is the least significant bit?**

The rightmost bit.

**Q9. What is the most significant bit of a positive integer's ordinary binary representation?**

The leftmost bit of that representation.

**Q10. Do Python integers have a fixed bit width?**

No. Python integers support arbitrary precision.

## Section B: AND, OR, XOR

**Q11. What does bitwise AND do?**

It returns one only when both corresponding bits are one.

**Q12. What is the result of `12 & 10`?**

`8`.

**Q13. What does bitwise OR do?**

It returns one when at least one corresponding bit is one.

**Q14. What is the result of `12 | 10`?**

`14`.

**Q15. What does bitwise XOR do?**

It returns one when corresponding bits are different.

**Q16. What is the result of `12 ^ 10`?**

`6`.

**Q17. What is the result of `a ^ a`?**

`0`.

**Q18. What is the result of `a ^ 0`?**

`a`.

**Q19. What is the result of `a & 0`?**

`0`.

**Q20. What is the result of `a | 0`?**

`a`.

## Section C: NOT and Shift Operators

**Q21. What does bitwise NOT do?**

It performs integer bitwise inversion according to Python's integer model.

**Q22. What is the result of `~5` in Python?**

`-6`.

**Q23. What is the formula for bitwise NOT in Python?**

`~n = -(n + 1)`.

**Q24. What is left shift?**

It moves bits toward the left by a specified number of positions.

**Q25. What is right shift?**

It moves bits toward the right by a specified number of positions.

**Q26. What is the result of `5 << 1`?**

`10`.

**Q27. What is the result of `20 >> 2`?**

`5`.

**Q28. What is the relationship between left shift and multiplication?**

Left shift by `n` positions multiplies an integer by `2**n`.

**Q29. What is the relationship between right shift and division?**

Right shift corresponds to floor division by `2**n`.

**Q30. What happens when a negative shift count is used?**

Python raises a `ValueError`.

## Section D: Bit Manipulation

**Q31. What is a bit mask?**

A bit mask is an integer used to select or modify particular bits.

**Q32. How do you create a mask for a bit position?**

```python
mask = 1 << position
```

**Q33. How do you check whether a bit is set?**

Use AND with a mask.

**Q34. How do you set a particular bit?**

Use OR with a mask.

**Q35. How do you clear a particular bit?**

Use AND with an inverted mask.

**Q36. How do you toggle a particular bit?**

Use XOR with a mask.

**Q37. What is a set bit?**

A bit whose value is one.

**Q38. What is the bitwise method for checking even or odd?**

Use `number & 1`.

**Q39. What is Brian Kernighan's algorithm?**

An algorithm that counts set bits by repeatedly clearing the lowest set bit.

**Q40. What is the result of `number & (number - 1)` for a positive integer with at least one set bit?**

It clears the lowest set bit.

## Section E: Advanced and Practical Questions

**Q41. What is the result of `10 & 1`?**

`0`.

**Q42. What is the result of `11 & 1`?**

`1`.

**Q43. What is a power of two check using bitwise AND?**

For positive `n`, check whether:

```python
n & (n - 1) == 0
```

**Q44. What is the difference between logical AND and bitwise AND?**

Logical AND works with truth-value logic and short-circuits. Bitwise AND manipulates binary bits.

**Q45. Where are bitwise operators used?**

They are used in permissions, masks, binary processing, and algorithms.

**Q46. What is the purpose of XOR in array problems?**

It can cancel duplicate elements when every duplicate occurs exactly twice and one value occurs once.

**Q47. What is the difference between setting and toggling a bit?**

Setting always makes a bit one. Toggling reverses its current value.

**Q48. What is the difference between clearing and checking a bit?**

Checking inspects a bit without changing the original value. Clearing produces a value in which that bit is zero.

**Q49. What is bitmask dynamic programming?**

A dynamic programming technique that represents subsets or states using integer bit masks.

**Q50. Why are bitwise operators important in DSA?**

They are useful for efficient bit manipulation, counting set bits, subset generation, and solving number-related problems.

---

# 32. Practice Test

Use this test to check your understanding of bitwise operators.

## Part A: Predict the Output

### Question 1

```python
print(12 & 10)
```

### Question 2

```python
print(12 | 10)
```

### Question 3

```python
print(12 ^ 10)
```

### Question 4

```python
print(~5)
```

### Question 5

```python
print(5 << 2)
```

### Question 6

```python
print(20 >> 2)
```

### Question 7

```python
print(10 & 1)
```

### Question 8

```python
print(11 & 1)
```

### Question 9

```python
number = 8
number |= 2

print(number)
```

### Question 10

```python
number = 12
number ^= 10

print(number)
```

## Part B: Identify the Correct Operator

1. Compare corresponding bits and keep one only when both are one.
2. Enable a selected bit.
3. Toggle selected bits.
4. Invert the integer's bits.
5. Shift bits toward the left.
6. Shift bits toward the right.
7. Check whether a bit is set.
8. Clear a particular bit.
9. Count the number of one bits.
10. Check whether an integer is even using its lowest bit.

## Part C: Programming Challenges

1. Accept two integers and perform bitwise AND.
2. Accept two integers and perform bitwise OR.
3. Accept two integers and perform bitwise XOR.
4. Display the bitwise NOT result of an integer.
5. Perform left shift using user input.
6. Perform right shift using user input.
7. Check even or odd using bitwise AND.
8. Check whether a selected bit is set.
9. Set and clear a particular bit.
10. Count the set bits using Brian Kernighan's algorithm.

---

# 33. Quick Revision Notes

## Binary Representation

```python
bin(10)
```

Result:

```text
0b1010
```

## Bitwise Operators

```python
a & b     # AND
a | b     # OR
a ^ b     # XOR
~a        # NOT
a << 1    # Left Shift
a >> 1    # Right Shift
```

## Bitwise Assignment

```python
a &= b
a |= b
a ^= b
a <<= 1
a >>= 1
```

## Bit Manipulation Formulas

Check a bit:

```python
n & (1 << p)
```

Set a bit:

```python
n | (1 << p)
```

Clear a bit:

```python
n & ~(1 << p)
```

Toggle a bit:

```python
n ^ (1 << p)
```

Count set bits:

```python
while n > 0:
    n &= n - 1
    count += 1
```

## Important Identities

```text
a & 0 = 0
a | 0 = a
a ^ 0 = a
a ^ a = 0
~a = -(a + 1)
```

For non-negative integers:

```text
a << n = a × 2ⁿ
a >> n = a // 2ⁿ
```

## Important Reminders

- Binary digits are zero and one.
- Bit positions start from zero.
- The rightmost bit is the least significant bit.
- AND checks bits.
- OR sets bits.
- XOR toggles bits.
- NOT inverts bits.
- Left shift moves bits left.
- Right shift moves bits right.
- Python integers do not have a fixed width.
- Negative NOT results follow Python's integer model.

---

# 34. Important Terminology

| Term | Meaning |
|---|---|
| Bit | A binary digit, zero or one |
| Binary | Base-2 number system |
| Decimal | Base-10 number system |
| Bitwise operator | Operator that manipulates integer bits |
| Bitwise AND | Operation that keeps only matching one bits |
| Bitwise OR | Operation that sets a result bit if either bit is one |
| Bitwise XOR | Operation that sets a bit when corresponding bits differ |
| Bitwise NOT | Integer bitwise inversion |
| Left shift | Moving bits toward the left |
| Right shift | Moving bits toward the right |
| Bit position | Zero-based location of a bit |
| Set bit | A binary digit with value one |
| Unset bit | A binary digit with value zero |
| Bit mask | Integer used to select or modify particular bits |
| LSB | Least Significant Bit |
| MSB | Most Significant Bit |
| Masking | Selecting particular bits using bitwise operations |
| Toggle | Reversing a selected bit |
| Set | Changing a bit to one |
| Clear | Changing a bit to zero |
| Set-bit counting | Counting the number of one bits |
| Binary conversion | Converting between binary and another number system |
| Bitmask DP | Dynamic programming using integer bit masks |

---

# 35. Learning Checklist

Complete this checklist after studying the topic.

## Binary Basics

- [ ] I understand the binary number system.
- [ ] I understand the decimal number system.
- [ ] I can convert decimal numbers to binary.
- [ ] I can convert binary numbers to decimal.
- [ ] I understand bits and bit positions.
- [ ] I know that bit positions start from zero.
- [ ] I can use Python's `bin()` function.

## Bitwise Operators

- [ ] I understand bitwise AND (`&`).
- [ ] I understand bitwise OR (`|`).
- [ ] I understand bitwise XOR (`^`).
- [ ] I understand bitwise NOT (`~`).
- [ ] I understand left shift (`<<`).
- [ ] I understand right shift (`>>`).
- [ ] I can apply bitwise truth tables.
- [ ] I understand augmented bitwise assignment.

## Bit Manipulation

- [ ] I can create bit masks.
- [ ] I can check whether a bit is set.
- [ ] I can set a particular bit.
- [ ] I can clear a particular bit.
- [ ] I can toggle a particular bit.
- [ ] I can check even or odd using bitwise AND.
- [ ] I can count set bits.
- [ ] I understand Brian Kernighan's algorithm.
- [ ] I understand Python's bitwise NOT behavior.

## Programming Practice

- [ ] I can perform AND operations.
- [ ] I can perform OR operations.
- [ ] I can perform XOR operations.
- [ ] I can perform NOT operations.
- [ ] I can perform left and right shifts.
- [ ] I can work with bit masks.
- [ ] I have practised all twelve solved problems.
- [ ] I have attempted all ten unsolved questions.
- [ ] I have completed the practice test.

---

# 36. How to Run the Python Program

Make sure Python is installed on your computer.

Open a terminal in the Bitwise Operators folder.

## 36.1 Run the Program

```bash
python 01_bitwise_operators.py
```

On systems where `python3` is used:

```bash
python3 01_bitwise_operators.py
```

## 36.2 Expected Main Menu

```text
1. View 12 Bitwise Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

## 36.3 Recommended Usage

### Step 1: Study the Examples

Select option `1`.

Understand the six basic bitwise operators and their binary representations.

### Step 2: Practise Solved Problems

Select option `2`.

Execute all twelve solved problems.

Experiment with different integers and bit positions.

### Step 3: Attempt Unsolved Questions

Select option `3`.

Solve all ten questions independently.

### Step 4: Review the Checklist

Select option `4`.

Check which concepts you understand and which require further practice.

### Step 5: Exit

Select option `0` when you finish.

---

# 37. Recommended Learning Sequence

Follow this sequence to study bitwise operators properly.

| Order | Topic | What to Learn |
|---:|---|---|
| 1 | Binary Number System | Understand base-2 |
| 2 | Binary Conversion | Convert decimal and binary |
| 3 | Bits and Positions | Understand zero-based positions |
| 4 | Bitwise AND | Compare corresponding bits |
| 5 | Bitwise OR | Combine corresponding bits |
| 6 | Bitwise XOR | Understand different-bit behavior |
| 7 | Bitwise NOT | Understand integer inversion |
| 8 | Left Shift | Move bits toward the left |
| 9 | Right Shift | Move bits toward the right |
| 10 | Bit Masks | Create masks using left shift |
| 11 | Set, Clear, Toggle, Check | Practise individual bit operations |
| 12 | Counting Set Bits | Learn bit-counting algorithms |

## Before Moving to the Next Topic

Make sure that:

1. You understand binary representation.
2. You can use all six bitwise operators.
3. You understand the bitwise truth tables.
4. You can create masks.
5. You can check, set, clear, and toggle bits.
6. You can count set bits.
7. You understand Python's negative NOT behavior.
8. You have completed all twelve solved problems.
9. You have attempted all ten unsolved questions.
10. You have revised the viva questions.

---

# 38. Topic Completion Summary

In this topic, you learned how Python performs operations on the binary representation of integers.

You covered:

- Binary number system.
- Decimal-to-binary conversion.
- Binary-to-decimal conversion.
- Bits and bit positions.
- Bitwise AND.
- Bitwise OR.
- Bitwise XOR.
- Bitwise NOT.
- Left shift.
- Right shift.
- Bitwise assignment operators.
- Bit masks.
- Checking bits.
- Setting bits.
- Clearing bits.
- Toggling bits.
- Counting set bits.
- Brian Kernighan's algorithm.
- Real-world bit manipulation.
- DSA applications.
- Time and space complexity.
- Programming practice.
- Interview and viva questions.

Bitwise operators are especially important when learning advanced programming and Data Structures and Algorithms.

You will use them in number theory, bit manipulation, bitmask dynamic programming, subset problems, and competitive programming.

**Do not move forward without practising binary calculations and the set, clear, toggle, and check operations. These are the foundation of bit manipulation.**

---

## Navigation

**Previous Topic:** [Logical Operators](../04-Logical-Operators/README.md)

**Next Topic:** [Membership Operators](../06-Membership-Operators/README.md)

**Parent Section:** [Operators and Expressions](../README.md)