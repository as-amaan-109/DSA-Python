# Python Complex Data Type — Complete Study Notes

**Week:** 1 — Programming Fundamentals  
**Part:** Variables and Data Types  
**Topic:** Complex Data Type  
**Code File:** `05_complex.py`

---

# Table of Contents

1. Introduction to Complex Numbers
2. Complex Numbers in Mathematics
3. Creating Complex Numbers in Python
4. The `complex()` Constructor
5. Real and Imaginary Components
6. Arithmetic Operations
7. Magnitude of a Complex Number
8. Complex Conjugate
9. Comparing Complex Numbers
10. The `cmath` Module
11. Polar Representation
12. Converting Between Rectangular and Polar Forms
13. Complex Numbers and 2D Geometry
14. Floating-Point Precision
15. Twelve Solved Problems
16. Ten Unsolved Practice Questions
17. Common Errors and Mistakes
18. Best Practices
19. Quick Revision Table
20. Interview and Viva Questions
21. Final Learning Checklist
22. How to Run the Program

---

# 1. Introduction to Complex Numbers

A **complex number** is a number that has a real component and an imaginary component.

Mathematically, it is written as:

\[
z = a + bi
\]

Where:

- \(a\) is the real part.
- \(b\) is the imaginary component's coefficient.
- \(i\) is the imaginary unit, defined by \(i^2=-1\).

Python uses the letter `j` instead of `i` for the imaginary unit.

For example:

```python
number = 3 + 4j

print(number)
print(type(number))
```

Output:

```text
(3+4j)
<class 'complex'>
```

Here:

- Real part: `3`
- Imaginary component: `4j`
- Imaginary coefficient: `4`

Python's built-in data type for complex numbers is called `complex`.

## Why do we use complex numbers?

Complex numbers are useful in:

- Mathematics and algebra
- Electrical engineering
- Signal processing
- Physics
- Control systems
- Digital signal processing
- Scientific computing
- Two-dimensional geometry
- Solving equations that have negative discriminants

For a beginner learning Python, complex numbers introduce another built-in numeric data type and show how Python can perform advanced mathematical calculations.

---

# 2. Complex Numbers in Mathematics

A complex number has two components:

\[
z = a + bi
\]

For example:

\[
z = 5 + 2i
\]

The real part is \(5\), and the imaginary component is \(2i\).

In Python, write:

```python
z = 5 + 2j
```

## Example 1: Positive imaginary component

```python
z = 3 + 4j
print(z)
```

Output:

```text
(3+4j)
```

## Example 2: Negative imaginary component

```python
z = 5 - 2j
print(z)
```

Output:

```text
(5-2j)
```

## Example 3: Purely real complex number

```python
z = 7 + 0j

print(z)
print(z.real)
print(z.imag)
```

Output:

```text
(7+0j)
7.0
0.0
```

A complex value can have a zero imaginary component while still being represented using Python's `complex` type.

## Example 4: Purely imaginary number

```python
z = 0 + 6j

print(z)
print(z.real)
print(z.imag)
```

Output:

```text
6j
0.0
6.0
```

A purely imaginary number has a zero real component.

## Example 5: Zero

```python
z = 0 + 0j

print(z)
print(z.real)
print(z.imag)
```

Output:

```text
0j
0.0
0.0
```

Zero is both purely real and purely imaginary under the usual component-based definitions because both components are zero.

---

# 3. Creating Complex Numbers in Python

Python supports more than one way to create complex numbers.

## 3.1 Using `j` notation

```python
first = 3 + 4j
second = 5 - 2j
third = 7j

print(first)
print(second)
print(third)
```

Output:

```text
(3+4j)
(5-2j)
7j
```

The imaginary unit must be written using `j` or `J`.

```python
print(3 + 4j)
print(3 + 4J)
```

Both represent equivalent complex values.

For normal beginner code, lowercase `j` is the usual convention.

## 3.2 Using the `complex()` constructor

```python
first = complex(3, 4)
second = complex(5, -2)

print(first)
print(second)
```

Output:

```text
(3+4j)
(5-2j)
```

The constructor has the following form:

```python
complex(real, imag)
```

The first argument is the real component, and the second is the imaginary component.

## 3.3 Creating a complex number from a string

```python
number = complex("3+4j")

print(number)
```

Output:

```text
(3+4j)
```

The text must use valid complex-number notation.

```python
print(complex("5-2j"))
print(complex("7j"))
print(complex("8"))
```

Output:

```text
(5-2j)
7j
(8+0j)
```

A plain numeric string passed to `complex()` creates a complex value with a zero imaginary component.

Invalid text raises a `ValueError`.

---

# 4. The `complex()` Constructor

The `complex()` function converts suitable numeric values into a complex number.

## Syntax

```python
complex(real, imag)
```

Both arguments are optional, and each defaults to zero.

## Example 1: Only a real component

```python
number = complex(5)

print(number)
```

Output:

```text
(5+0j)
```

## Example 2: Real and imaginary components

```python
number = complex(5, 2)

print(number)
```

Output:

```text
(5+2j)
```

## Example 3: Negative imaginary component

```python
number = complex(3, -7)

print(number)
```

Output:

```text
(3-7j)
```

## Example 4: Floating-point components

```python
number = complex(2.5, 1.5)

print(number)
```

Output:

```text
(2.5+1.5j)
```

## Important detail

The two-argument form of `complex()` expects its arguments to be real numeric values, not already-complex values.

For example, use:

```python
number = complex(3, 4)
```

rather than passing two complex objects as separate arguments.

---

# 5. Real and Imaginary Components

Python provides two read-only attributes for accessing a complex number's components:

- `.real`
- `.imag`

## Example

```python
number = 3 + 4j

print(number.real)
print(number.imag)
```

Output:

```text
3.0
4.0
```

Notice that these attributes return floating-point values.

## Example with a negative imaginary component

```python
number = 7 - 5j

print("Real part:", number.real)
print("Imaginary part:", number.imag)
```

Output:

```text
Real part: 7.0
Imaginary part: -5.0
```

The imaginary part returned by `.imag` is the coefficient of \(j\). It does not include the letter `j`.

## Accessing components through `complex()`

```python
number = complex(8, 3)

real_part = number.real
imaginary_part = number.imag

print(real_part)
print(imaginary_part)
```

Output:

```text
8.0
3.0
```

## Common mistake

The real and imaginary attributes cannot be assigned directly.

Incorrect:

```python
number = 3 + 4j

# number.real = 10
```

Instead, construct a new value:

```python
number = complex(10, number.imag)

print(number)
```

Output:

```text
(10+4j)
```

Complex numbers are immutable, just like Python strings.

---

# 6. Arithmetic Operations

Python supports the standard arithmetic operations on complex numbers.

Let:

\[
z_1 = a + bi
\]

\[
z_2 = c + di
\]

## 6.1 Addition

Add the real components and the imaginary components separately.

\[
z_1 + z_2 = (a+c) + (b+d)i
\]

Example:

```python
first = 3 + 4j
second = 1 + 2j

print(first + second)
```

Output:

```text
(4+6j)
```

The real components add to \(4\), and the imaginary coefficients add to \(6\).

## 6.2 Subtraction

Subtract the corresponding components.

\[
z_1-z_2=(a-c)+(b-d)i
\]

Example:

```python
first = 3 + 4j
second = 1 + 2j

print(first - second)
```

Output:

```text
(2+2j)
```

## 6.3 Multiplication

Multiply the expressions using the distributive rule and \(i^2=-1\).

\[
(a+bi)(c+di)=(ac-bd)+(ad+bc)i
\]

Example:

```python
first = 2 + 3j
second = 4 - 1j

print(first * second)
```

Output:

```text
(11+10j)
```

Calculation:

\[
(2+3i)(4-i)
\]

\[
=8-2i+12i-3i^2
\]

Since \(i^2=-1\):

\[
=11+10i
\]

Python's output is `(11+10j)`.

## 6.4 Division

Complex division can be performed directly using `/`.

Example:

```python
first = 3 + 4j
second = 1 - 2j

print(first / second)
```

Output:

```text
(-1+2j)
```

Mathematically, division can be simplified by multiplying the numerator and denominator by the conjugate of the denominator.

For \(c+di \ne 0\):

\[
\frac{a+bi}{c+di}
=
\frac{(a+bi)(c-di)}{c^2+d^2}
\]

This converts the denominator into a real number.

### Division by zero

```python
number = 3 + 4j

# This raises ZeroDivisionError:
# print(number / 0)
```

Before dividing by a user-supplied complex number, check whether it equals zero.

```python
numerator = 3 + 4j
denominator = 0 + 0j

if denominator != 0:
    print(numerator / denominator)
else:
    print("Division by zero is not allowed.")
```

## 6.5 Exponentiation

Python supports raising complex numbers to powers using `**`.

```python
number = 1 + 1j

print(number ** 2)
```

Output:

```text
2j
```

Calculation:

\[
(1+i)^2=1+2i+i^2=2i
\]

## 6.6 Modulo and floor division

Python does not support `%` or `//` for complex-number operands.

```python
number = 3 + 4j

# These operations are unsupported:
# print(number % 2)
# print(number // 2)
```

Use the mathematical operations appropriate for complex numbers, such as addition, subtraction, multiplication, division and exponentiation.

---

# 7. Magnitude of a Complex Number

The **magnitude**, also called the modulus or absolute value, measures the distance of the complex number from zero in the complex plane.

For:

\[
z=a+bi
\]

The magnitude is:

\[
|z|=\sqrt{a^2+b^2}
\]

In Python, use `abs()`.

## Example

```python
number = 3 + 4j

print(abs(number))
```

Output:

```text
5.0
```

Calculation:

\[
|3+4i|=\sqrt{3^2+4^2}
\]

\[
=\sqrt{9+16}=\sqrt{25}=5
\]

## Example with negative components

```python
number = -5 - 12j

print(abs(number))
```

Output:

```text
13.0
```

Both components are squared, so their signs do not make the magnitude negative.

## Magnitude is always non-negative

For any complex number \(z\):

\[
|z|\ge 0
\]

Only the zero complex number has magnitude zero.

```python
print(abs(0 + 0j))
print(abs(1 + 1j))
print(abs(-3 + 4j))
```

Output:

```text
0.0
1.4142135623730951
5.0
```

## Applications

Magnitude is useful for:

- Measuring distance in a complex plane
- Comparing how far complex values lie from zero
- Signal-processing calculations
- Analyzing vectors represented by complex numbers

---

# 8. Complex Conjugate

The **complex conjugate** of a number changes the sign of its imaginary component while keeping the real component unchanged.

For:

\[
z=a+bi
\]

The conjugate is:

\[
\overline{z}=a-bi
\]

Python provides the `.conjugate()` method.

## Example

```python
number = 3 + 4j

print(number.conjugate())
```

Output:

```text
(3-4j)
```

## Example with a negative imaginary component

```python
number = 5 - 2j

print(number.conjugate())
```

Output:

```text
(5+2j)
```

## Conjugate of a purely real number

```python
number = 7 + 0j

print(number.conjugate())
```

Output:

```text
(7-0j)
```

The value is mathematically equivalent to \(7+0j\).

## Multiplying a complex number by its conjugate

An important identity is:

\[
z\overline{z}=a^2+b^2=|z|^2
\]

Example:

```python
number = 3 + 4j

result = number * number.conjugate()

print(result)
```

Output:

```text
(25+0j)
```

The result is a non-negative real value represented as a complex number.

This relationship is useful in mathematical simplification and complex division.

---

# 9. Comparing Complex Numbers

Complex numbers support equality and inequality comparisons, but they do not support ordinary ordering comparisons.

## 9.1 Equality

```python
first = 3 + 4j
second = 3 + 4j

print(first == second)
```

Output:

```text
True
```

The components of the two numbers match.

## 9.2 Inequality

```python
first = 3 + 4j
second = 4 + 3j

print(first != second)
```

Output:

```text
True
```

The component values differ, so the complex numbers are not equal.

## 9.3 Why `<` and `>` are not supported

```python
first = 3 + 4j
second = 2 + 1j

# Both operations raise TypeError:
# print(first < second)
# print(first > second)
```

Python does not define an ordinary less-than or greater-than ordering for complex values.

## How do we compare the sizes of complex numbers?

If the task is to compare their magnitudes, use `abs()`.

```python
first = 3 + 4j
second = 2 + 1j

if abs(first) > abs(second):
    print("The first number has greater magnitude.")
else:
    print("The second number has equal or greater magnitude.")
```

Output:

```text
The first number has greater magnitude.
```

The first magnitude is \(5\), and the second magnitude is \(\sqrt{5}\).

**Important:** Comparing magnitudes is not the same as ordering complex numbers themselves.

---

# 10. The `cmath` Module

Python's `cmath` module provides mathematical functions designed to work with complex numbers.

Import it using:

```python
import cmath
```

Some useful functions are:

| Function | Purpose |
|---|---|
| `cmath.sqrt(z)` | Calculates a complex square root |
| `cmath.phase(z)` | Calculates the angle of a complex value in radians |
| `cmath.polar(z)` | Returns magnitude and phase |
| `cmath.rect(r, phi)` | Builds a complex number from magnitude and phase |
| `cmath.exp(z)` | Calculates the complex exponential |
| `cmath.log(z)` | Calculates the principal complex logarithm |
| `cmath.sin(z)` | Calculates complex sine |
| `cmath.cos(z)` | Calculates complex cosine |

## 10.1 Square root

```python
import cmath

print(cmath.sqrt(-16))
```

Output:

```text
4j
```

A real square-root operation cannot return a real number for a negative input. The complex square-root function can return a complex result.

For \(-16\), the principal square root is \(4i\), represented in Python as `4j`.

## 10.2 Phase

The phase is the angle of a complex number, measured in radians.

```python
import cmath

number = 1j

print(cmath.phase(number))
```

Output:

```text
1.5707963267948966
```

This is approximately \(\pi/2\) radians, or 90 degrees.

## 10.3 Convert radians to degrees

```python
import cmath
import math

number = 1j

angle_radians = cmath.phase(number)
angle_degrees = math.degrees(angle_radians)

print(angle_degrees)
```

Output:

```text
90.0
```

Use the `math` module for ordinary real-valued operations such as degree/radian conversion. Use `cmath` for complex-valued mathematical operations.

---

# 11. Polar Representation

A complex number can be represented in two common forms:

1. Rectangular form
2. Polar form

## Rectangular form

The usual form is:

\[
z=a+bi
\]

For example:

\[
z=3+4i
\]

## Polar form

The polar representation uses:

- \(r\): magnitude
- \(\theta\): angle or phase

The relationship is:

\[
z=r(\cos\theta+i\sin\theta)
\]

The magnitude is:

\[
r=\sqrt{a^2+b^2}
\]

The phase is the angle measured from the positive real axis.

## Example

For:

\[
z=3+4i
\]

The magnitude is:

\[
r=\sqrt{3^2+4^2}=5
\]

The angle is approximately:

\[
\theta=\tan^{-1}\left(\frac{4}{3}\right)
\]

The angle is approximately \(0.9273\) radians or \(53.13^\circ\).

Use `cmath.polar()` to calculate the magnitude and phase.

```python
import cmath

number = 3 + 4j

radius, angle = cmath.polar(number)

print("Magnitude:", radius)
print("Angle in radians:", angle)
```

Output:

```text
Magnitude: 5.0
Angle in radians: 0.9272952180016122
```

The phase is expressed in radians.

---

# 12. Converting Between Rectangular and Polar Forms

Python provides two useful functions:

- `cmath.polar(z)` converts a complex value to magnitude and phase.
- `cmath.rect(r, phi)` converts a magnitude and phase to a complex value.

## 12.1 Rectangular to polar

```python
import cmath

number = 3 + 4j

radius, angle = cmath.polar(number)

print(radius)
print(angle)
```

Output:

```text
5.0
0.9272952180016122
```

## 12.2 Polar to rectangular

```python
import cmath
import math

radius = 5
angle_degrees = 90

angle_radians = math.radians(angle_degrees)

number = cmath.rect(radius, angle_radians)

print(number)
```

The result is approximately:

```text
(3.061616997868383e-16+5j)
```

The real component is extremely close to zero, but floating-point rounding prevents it from being exactly zero in this calculation.

Mathematically, the result is \(5i\).

## Why are there small decimal errors?

Computers represent many real numbers using finite-precision floating-point arithmetic. Trigonometric calculations can therefore produce very small residual values.

For comparisons involving calculated floating-point values, consider `math.isclose()` when comparing real components.

```python
import math

print(math.isclose(3.061616997868383e-16, 0.0, abs_tol=1e-12))
```

Output:

```text
True
```

For general complex calculations, `cmath.isclose()` can compare complex values using tolerances.

```python
import cmath

first = cmath.rect(5, math.radians(90))
second = 5j

print(cmath.isclose(first, second, abs_tol=1e-12))
```

Output:

```text
True
```

---

# 13. Complex Numbers and 2D Geometry

A complex number can represent a point in a two-dimensional plane.

For:

\[
z=x+yi
\]

The real part represents the horizontal coordinate, and the imaginary coefficient represents the vertical coordinate.

A point \((x,y)\) can therefore be represented as:

```python
point = complex(x, y)
```

## 13.1 Represent a point

```python
point = complex(3, 4)

print(point.real)
print(point.imag)
```

Output:

```text
3.0
4.0
```

This represents the point \((3,4)\).

## 13.2 Distance from the origin

The distance from the origin is the magnitude.

```python
point = 3 + 4j

print(abs(point))
```

Output:

```text
5.0
```

This follows from the Pythagorean theorem.

## 13.3 Distance between two points

For two points \(z_1\) and \(z_2\), their distance is:

\[
d=|z_2-z_1|
\]

Example:

```python
first = complex(1, 2)
second = complex(4, 6)

distance = abs(second - first)

print(distance)
```

Output:

```text
5.0
```

The horizontal difference is \(3\), and the vertical difference is \(4\).

Therefore:

\[
d=\sqrt{3^2+4^2}=5
\]

## Applications

This representation can simplify:

- Distance calculations
- Two-dimensional coordinate operations
- Rotations and transformations
- Geometric reasoning
- Signal representation

---

# 14. Floating-Point Precision

Complex numbers can contain floating-point real and imaginary components. Calculations may produce small rounding differences.

For example:

```python
import cmath
import math

radius = 5
angle = math.radians(90)

number = cmath.rect(radius, angle)

print(number)
```

You may see a real component that is very close to zero instead of exactly zero.

This is a normal consequence of floating-point computation.

## Avoid fragile equality tests

For computed values, avoid assuming that two independently calculated floating-point results will always be exactly equal.

For complex values, use:

```python
cmath.isclose(first, second, abs_tol=1e-9)
```

when a suitable tolerance is appropriate.

The tolerance should depend on the scale and precision requirements of the problem.

For simple exact values, direct equality is appropriate:

```python
print((3 + 4j) == (3 + 4j))
```

Output:

```text
True
```

---

# 15. Twelve Solved Problems

The file `05_complex.py` contains twelve programs in its interactive solved-problems menu.

## Problem 1: Display Real and Imaginary Parts

**Question:** Read a complex number and display its real and imaginary components.

Example:

```text
Input: 3+4j
Real part: 3.0
Imaginary part: 4.0
```

### Logic

1. Read a valid complex number.
2. Access `.real`.
3. Access `.imag`.
4. Print the number and its components.

```python
number = complex(input("Enter a complex number: "))

print("Real part:", number.real)
print("Imaginary part:", number.imag)
```

## Problem 2: Add Two Complex Numbers

**Question:** Add two complex numbers.

Example:

```text
First: 3+4j
Second: 1+2j
Sum: (4+6j)
```

### Logic

Read two values and add them with `+`.

```python
first = 3 + 4j
second = 1 + 2j

print(first + second)
```

## Problem 3: Subtract Two Complex Numbers

**Question:** Subtract the second complex number from the first.

```python
first = 3 + 4j
second = 1 + 2j

print(first - second)
```

Output:

```text
(2+2j)
```

## Problem 4: Multiply Two Complex Numbers

**Question:** Multiply two complex numbers.

```python
first = 2 + 3j
second = 4 - 1j

print(first * second)
```

Output:

```text
(11+10j)
```

## Problem 5: Divide Two Complex Numbers

**Question:** Divide a numerator by a non-zero complex denominator.

```python
first = 3 + 4j
second = 1 - 2j

if second != 0:
    print(first / second)
else:
    print("Division by zero.")
```

Output:

```text
(-1+2j)
```

The program must check for a zero denominator before attempting division.

## Problem 6: Calculate Magnitude

**Question:** Find the magnitude of a complex number.

```python
number = 3 + 4j

print(abs(number))
```

Output:

```text
5.0
```

The magnitude is the square root of the sum of the squared real and imaginary components.

## Problem 7: Calculate the Conjugate

**Question:** Find the complex conjugate.

```python
number = 3 + 4j

print(number.conjugate())
```

Output:

```text
(3-4j)
```

The sign of the imaginary component changes.

## Problem 8: Classify the Complex Number

**Question:** Determine whether a complex value is purely real, purely imaginary or has both non-zero components.

Example:

```text
Input: 0+5j
Purely real: False
Purely imaginary: True
```

### Logic

- A zero imaginary component indicates a purely real number.
- A zero real component indicates a purely imaginary number.
- If both components are non-zero, neither classification applies.

Zero satisfies both component-based conditions.

## Problem 9: Compare Magnitudes

**Question:** Determine which of two complex numbers has the greater magnitude.

```python
first = 3 + 4j
second = 2 + 1j

print(abs(first))
print(abs(second))
```

Output:

```text
5.0
2.23606797749979
```

Compare the values returned by `abs()`. Do not use `<` or `>` directly on complex numbers.

## Problem 10: Distance Between Two Points

**Question:** Calculate the distance between two points in two-dimensional space.

```python
first_point = complex(1, 2)
second_point = complex(4, 6)

distance = abs(second_point - first_point)

print(distance)
```

Output:

```text
5.0
```

Subtracting the points gives their displacement. The magnitude gives the distance.

## Problem 11: Solve a Quadratic Equation

**Question:** Solve:

\[
ax^2+bx+c=0
\]

For a non-zero coefficient \(a\), calculate the discriminant:

\[
D=b^2-4ac
\]

The roots are:

\[
x=\frac{-b\pm\sqrt{D}}{2a}
\]

Python's `cmath.sqrt()` can calculate complex square roots when the discriminant is negative.

```python
import cmath

a = 1
b = 2
c = 5

discriminant = b ** 2 - 4 * a * c

first_root = (-b + cmath.sqrt(discriminant)) / (2 * a)
second_root = (-b - cmath.sqrt(discriminant)) / (2 * a)

print(first_root)
print(second_root)
```

Output:

```text
(-1+2j)
(-1-2j)
```

The supplied program also handles the case where \(a=0\), which makes the equation linear or degenerate.

## Problem 12: Convert Polar Form to a Complex Number

**Question:** Convert a magnitude and an angle in degrees into a complex number.

```python
import cmath
import math

radius = 5
angle_degrees = 90

angle_radians = math.radians(angle_degrees)
number = cmath.rect(radius, angle_radians)

print(number)
```

The result is approximately \(5i\). It may have a tiny non-zero real component due to floating-point precision.

The program uses `math.radians()` to convert degrees to radians before calling `cmath.rect()`.

---

# 16. Ten Unsolved Practice Questions

Try these independently before looking at sample solutions elsewhere.

## Practice 1: Calculate Magnitude Manually

Write a program that calculates the magnitude of a complex number **without using `abs()`**.

Example:

```text
Input: 3+4j
Expected magnitude: 5
```

Hint: Use the real and imaginary components and the square-root operation.

## Practice 2: Verify the Conjugate Identity

Write a program to verify that multiplying a complex number by its conjugate gives a non-negative real result.

Example:

```text
Number: 3+4j
Expected product: 25+0j
```

Hint: Use `.conjugate()` and compare the product's components.

## Practice 3: Check Additive Inverses

Write a program to check whether two complex numbers are additive inverses.

Two numbers are additive inverses when their sum is zero.

Example:

```text
First: 3+4j
Second: -3-4j
Expected result: True
```

Hint: Add the two complex values.

## Practice 4: Find the Midpoint of Two Points

Write a program to calculate the midpoint between two 2D points represented as complex numbers.

Example:

```text
Point 1: 1+2j
Point 2: 5+6j
Expected midpoint: 3+4j
```

Hint: The midpoint is the average of the two complex values.

## Practice 5: Classify a Complex Number

Write a program to determine whether a number is:

- Purely real
- Purely imaginary
- Neither
- Zero

Decide how the zero case should be reported and explain your choice.

Hint: Inspect both components.

## Practice 6: Convert a Number to Polar Form

Read a complex number and display its magnitude and angle in degrees.

Example:

```text
Input: 3+4j
Expected magnitude: 5
Expected angle: approximately 53.13 degrees
```

Hint: Use `cmath.polar()` and convert the phase from radians to degrees.

## Practice 7: Calculate a Complex Square

Write a program to calculate the square of a complex number using multiplication and the `**` operator. Compare the results.

Example:

```text
Number: 1+1j
Expected square: 2j
```

Hint: Use `number * number` and `number ** 2`.

## Practice 8: Classify Quadratic Roots

Write a program to solve a quadratic equation and classify its roots as real or complex.

Hint: Calculate the discriminant and use it to determine the root type. Handle a zero leading coefficient separately.

## Practice 9: Distance Between Complex Values

Read two complex numbers and calculate the distance between them.

Example:

```text
First: 1+2j
Second: 4+6j
Expected distance: 5
```

Hint: Take the magnitude of their difference.

## Practice 10: Build a Complex Calculator

Create a menu-driven calculator that supports:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Magnitude

The program should allow users to choose an operation and enter the necessary complex values.

**Requirements:**

- Reject invalid complex-number input.
- Handle division by zero.
- Keep the menu readable.
- Allow multiple operations without restarting the program.

---

# 17. Common Errors and Mistakes

## Mistake 1: Using `i` instead of `j`

Incorrect:

```python
# number = 3 + 4i
```

Correct:

```python
number = 3 + 4j
```

Python uses `j` or `J` for the imaginary unit in complex literals.

## Mistake 2: Treating a complex value as an ordinary string

```python
number = "3+4j"

print(type(number))
```

Output:

```text
<class 'str'>
```

The quotes make the value a string.

Correct:

```python
number = complex("3+4j")

print(type(number))
```

Output:

```text
<class 'complex'>
```

## Mistake 3: Using `<` or `>` on complex numbers

Complex numbers do not support ordinary ordering comparisons.

Incorrect:

```python
first = 3 + 4j
second = 2 + 1j

# print(first > second)
```

To compare distance from zero, compare magnitudes instead.

```python
print(abs(first) > abs(second))
```

## Mistake 4: Dividing by zero

A zero complex denominator raises `ZeroDivisionError`.

Check the denominator before dividing.

```python
if denominator != 0:
    result = numerator / denominator
```

## Mistake 5: Confusing the imaginary component and its coefficient

```python
number = 3 + 4j

print(number.imag)
```

Output:

```text
4.0
```

The imaginary component's coefficient is `4`, while the mathematical imaginary term is \(4i\).

## Mistake 6: Assuming the real part must always be an integer

```python
number = 2.5 + 1.5j

print(number.real)
print(number.imag)
```

Output:

```text
2.5
1.5
```

Complex values may contain floating-point components.

## Mistake 7: Expecting perfect floating-point results

Trigonometric and other numerical operations may produce tiny rounding errors. Use an appropriate tolerance when checking approximate results.

## Mistake 8: Forgetting that complex numbers are immutable

You cannot change a complex value's `.real` or `.imag` attribute directly. Build a new complex number to change a component.

---

# 18. Best Practices

1. Use `j` consistently when writing complex literals.
2. Use `complex()` when the real and imaginary components are available separately.
3. Use `.real` and `.imag` to inspect the components.
4. Use `abs()` to calculate magnitude.
5. Use `.conjugate()` to obtain the conjugate.
6. Use the `cmath` module for complex-valued mathematical functions.
7. Use `math.radians()` and `math.degrees()` for angle conversion.
8. Never use `<` or `>` directly with complex values.
9. Validate user input and handle `ValueError`.
10. Check for a zero denominator before division.
11. Use approximate comparisons when working with floating-point results.
12. Use descriptive names such as `first_number`, `magnitude` and `angle_radians`.
13. Test calculations using simple numbers with known results.
14. Keep input, calculation and output logic easy to follow.

---

# 19. Quick Revision Table

| Concept | Syntax | Purpose |
|---|---|---|
| Complex literal | `3 + 4j` | Creates a complex value |
| Constructor | `complex(3, 4)` | Builds a number from components |
| Type | `complex` | Complex data type |
| Real component | `z.real` | Returns the real component |
| Imaginary coefficient | `z.imag` | Returns the imaginary coefficient |
| Addition | `z1 + z2` | Adds complex values |
| Subtraction | `z1 - z2` | Subtracts complex values |
| Multiplication | `z1 * z2` | Multiplies complex values |
| Division | `z1 / z2` | Divides by a non-zero complex value |
| Power | `z ** 2` | Raises a complex value to a power |
| Magnitude | `abs(z)` | Distance from zero |
| Conjugate | `z.conjugate()` | Reverses the sign of the imaginary component |
| Equality | `z1 == z2` | Checks equality |
| Polar conversion | `cmath.polar(z)` | Returns magnitude and phase |
| Rectangular conversion | `cmath.rect(r, phi)` | Converts magnitude and phase to a complex value |
| Square root | `cmath.sqrt(z)` | Calculates a complex square root |
| Phase | `cmath.phase(z)` | Returns angle in radians |
| Degree conversion | `math.degrees(phi)` | Converts radians into degrees |
| Radian conversion | `math.radians(degrees)` | Converts degrees into radians |
| Approximate equality | `cmath.isclose(z1, z2)` | Compares complex values using tolerances |

---

# 20. Important Interview and Viva Questions

### Q1. What is a complex number?

A complex number has a real component and an imaginary component and can be represented as \(a+bi\).

### Q2. Which symbol does Python use for the imaginary unit?

Python uses `j` or `J`.

### Q3. What is the data type of a complex number?

The data type is `complex`.

### Q4. How do you create a complex number in Python?

Use a literal such as `3 + 4j` or the constructor `complex(3, 4)`.

### Q5. What is the difference between `.real` and `.imag`?

`.real` returns the real component, while `.imag` returns the coefficient of the imaginary component.

### Q6. What does `abs()` do for a complex number?

It calculates the magnitude, or distance of the complex number from zero.

### Q7. What is a complex conjugate?

It is obtained by changing the sign of the imaginary component while keeping the real component unchanged.

### Q8. Can Python compare two complex numbers using `<`?

No. Python supports equality comparisons but not ordinary ordering comparisons between complex values.

### Q9. Can you multiply complex numbers in Python?

Yes. The `*` operator performs complex multiplication.

### Q10. What happens when a complex number is divided by zero?

Python raises `ZeroDivisionError`.

### Q11. What is the purpose of `cmath`?

The `cmath` module provides mathematical functions that support complex numbers.

### Q12. What does `cmath.sqrt(-16)` return?

It returns `4j`, the principal complex square root of negative sixteen.

### Q13. What is the magnitude of `3 + 4j`?

Its magnitude is `5.0`.

### Q14. What does `.conjugate()` return for `3 + 4j`?

It returns `(3-4j)`.

### Q15. What is polar representation?

Polar representation describes a complex value using its magnitude and phase angle.

### Q16. What does `cmath.phase()` return?

It returns the phase angle of a complex number in radians.

### Q17. What do `cmath.polar()` and `cmath.rect()` do?

`cmath.polar()` returns magnitude and phase. `cmath.rect()` constructs a complex value from magnitude and phase.

### Q18. What is the relationship between a complex number and its conjugate?

The product of a complex number and its conjugate is a non-negative real value equal to the square of its magnitude.

### Q19. Can the real and imaginary components be floating-point numbers?

Yes. Both components can have floating-point values.

### Q20. Why can a polar conversion produce a tiny real component instead of exactly zero?

Floating-point representation and trigonometric calculations can introduce very small rounding errors.

---

# 21. Final Learning Checklist

Before moving to the next topic, make sure you can:

- [ ] Explain a complex number using real and imaginary components.
- [ ] Create complex numbers with `j` notation.
- [ ] Use `complex()` to construct numbers.
- [ ] Access `.real` and `.imag`.
- [ ] Perform arithmetic operations on complex values.
- [ ] Calculate magnitude using `abs()`.
- [ ] Calculate a conjugate.
- [ ] Explain why complex values cannot be ordered using `<` and `>`.
- [ ] Use `cmath.sqrt()`, `cmath.phase()` and `cmath.polar()`.
- [ ] Convert between polar and rectangular representations.
- [ ] Represent two-dimensional points using complex values.
- [ ] Handle invalid input and division by zero.
- [ ] Understand floating-point rounding.
- [ ] Complete the twelve solved problems.
- [ ] Attempt all ten unsolved practice questions.

---

# 22. How to Run the Program

Open PowerShell in the root directory of the `DSA-Python` repository.

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python"

python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\02-Data-Types\05_complex\05_complex.py"
```

The program provides the following menu:

1. View 12 complex number examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit

Start with the examples, then test each solved problem using different inputs. Finish by attempting the ten unsolved exercises independently.

---

## Final Advice

Complex numbers are an important mathematical data type supported directly by Python. Focus on understanding the real and imaginary components, arithmetic operations, magnitude, conjugate and `cmath` functions.

Practise the problems in `05_complex.py`, and do not move forward until you can explain your calculations and handle invalid input correctly.
