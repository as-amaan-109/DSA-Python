# Topic 10 – Pattern Printing in Python

**Part 2:** Python Fundamentals  
**Section:** 01 – Loops  
**Topic Number:** 10  
**Source File:** `10_pattern_printing.py`  
**Language:** Python 3.9+

---

# Table of Contents

1. Introduction to Pattern Printing
2. Learning Objectives
3. What Is Pattern Printing?
4. Importance of Nested Loops
5. Understanding Rows and Columns
6. Important Print Function Concepts
7. Understanding Spaces and Alignment
8. Star Patterns
9. Number Patterns
10. Alphabet Patterns
11. Hollow Patterns
12. Twelve Topic Examples
13. Twelve Solved Programming Problems
14. Ten Unsolved Practice Questions
15. Common Mistakes
16. Best Practices
17. Debugging Pattern Programs
18. Real-Life Applications
19. Connection with Data Structures and Algorithms
20. Time and Space Complexity
21. Mini Project – Pattern Generator
22. Fifty Python Viva Questions and Answers
23. Important Terminology
24. Quick Revision Notes
25. Learning Checklist
26. How to Run the Python File
27. Repository Structure
28. Git Commands
29. Final Summary

---

# 1. Introduction to Pattern Printing

Pattern printing is an important programming exercise used to understand loops, nested loops, conditions and the `print()` function.

In pattern printing, we display characters, numbers, alphabets or symbols in a particular arrangement.

Examples include:

- Square patterns.
- Triangle patterns.
- Inverted triangles.
- Pyramid patterns.
- Diamond patterns.
- Number triangles.
- Alphabet patterns.
- Hollow shapes.

Pattern printing is especially useful for beginners because it helps develop logical thinking.

It teaches us how to control the number of rows, columns, spaces and characters using loops.

## Simple Example

```python
for row in range(1, 5):

    for column in range(1, 5):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

This program prints a square containing four rows and four columns.

## Why Do We Study Pattern Printing?

Pattern printing helps you understand:

1. How nested loops work.
2. How an outer loop controls rows.
3. How an inner loop controls columns.
4. How the `range()` function works.
5. How to print multiple characters on the same line.
6. How to move to the next line.
7. How conditions control character placement.
8. How spaces help with alignment.
9. How to develop logical problem-solving skills.
10. How to translate a visual pattern into code.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand pattern printing in Python.
2. Understand the importance of nested loops.
3. Differentiate between outer and inner loops.
4. Control the number of rows.
5. Control the number of columns.
6. Use `print()` with `end`.
7. Print square star patterns.
8. Print right-angled triangles.
9. Print inverted triangles.
10. Print right-aligned triangles.
11. Print centered pyramids.
12. Print inverted pyramids.
13. Print diamond patterns.
14. Print repeated number patterns.
15. Print Floyd's triangle.
16. Print alphabet triangles.
17. Print hollow squares and pyramids.
18. Use conditions inside nested loops.
19. Understand time and space complexity.
20. Solve pattern-based programming problems.

---

# 3. What Is Pattern Printing?

Pattern printing means displaying values in a specific visual arrangement using programming statements.

The displayed values can include:

- `*` – Star
- `#` – Hash
- `$` – Dollar sign
- `1, 2, 3` – Numbers
- `A, B, C` – Alphabets

## Example 1 – Star Pattern

```python
print("*")
print("* *")
print("* * *")
print("* * * *")
```

**Output:**

```text
*
* *
* * *
* * * *
```

This pattern can also be created using loops.

```python
for row in range(1, 5):

    for column in range(row):
        print("*", end=" ")

    print()
```

## Example 2 – Number Pattern

```python
for row in range(1, 5):

    for column in range(row):
        print(row, end=" ")

    print()
```

**Output:**

```text
1
2 2
3 3 3
4 4 4 4
```

## Example 3 – Alphabet Pattern

```python
for row in range(1, 5):

    for column in range(row):
        print(chr(65 + column), end=" ")

    print()
```

**Output:**

```text
A
A B
A B C
A B C D
```

Pattern printing is mainly about understanding how the number of characters changes from one row to another.

---

# 4. Importance of Nested Loops

A nested loop is a loop inside another loop.

Nested loops are commonly used for pattern printing because patterns usually contain rows and columns.

## Basic Structure

```python
for row in range(1, 4):

    for column in range(1, 4):
        print("*", end=" ")

    print()
```

Here:

- The outer loop controls the rows.
- The inner loop controls the columns.
- The inner loop runs completely for every outer-loop iteration.
- The final `print()` moves the output to the next line.

## Understanding Outer and Inner Loops

Consider this code:

```python
for row in range(1, 4):

    for column in range(1, 4):
        print("*", end=" ")

    print()
```

The execution happens as follows:

| Outer Loop | Inner Loop Values | Number of Stars |
|---|---|---:|
| Row 1 | 1, 2, 3 | 3 |
| Row 2 | 1, 2, 3 | 3 |
| Row 3 | 1, 2, 3 | 3 |

The inner loop executes three times for every outer-loop iteration.

Total stars:

\[
3 \times 3 = 9
\]

## Important Points

1. The outer loop generally controls rows.
2. The inner loop generally controls columns.
3. Every inner loop completes before the outer loop moves to its next iteration.
4. A nested loop can contain more than two levels.
5. Changing the inner loop's range changes the pattern.
6. Changing the outer loop's range changes the number of rows.

---

# 5. Understanding Rows and Columns

Rows and columns are the foundation of most patterns.

A row is a horizontal line of output.

A column is a vertical position within a row.

## Example

```text
* * * *
* * * *
* * * *
```

This pattern contains:

- 3 rows.
- 4 columns.
- 12 stars.

## Code

```python
rows = 3
columns = 4

for row in range(rows):

    for column in range(columns):
        print("*", end=" ")

    print()
```

## Output

```text
* * * *
* * * *
* * * *
```

## Row-Based Triangle

```python
for row in range(1, 5):

    for column in range(row):
        print("*", end=" ")

    print()
```

The number of stars increases with the row number.

| Row | Number of Stars |
|---|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |

This is called a right-angled triangle pattern.

---

# 6. Important Print Function Concepts

The `print()` function is very important in pattern printing.

By default, `print()` moves the cursor to the next line.

We can change this behaviour using the `end` parameter.

## 6.1 Default Print

```python
print("*")
print("*")
print("*")
```

**Output:**

```text
*
*
*
```

Every print statement displays its output on a separate line.

## 6.2 Print with end

```python
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
```

**Output:**

```text
* * *
```

The `end=" "` parameter adds a space instead of moving to a new line.

## 6.3 Print Empty Line

```python
print("*", end=" ")
print("*", end=" ")

print()

print("*", end=" ")
print("*", end=" ")
```

**Output:**

```text
* *
* *
```

The empty `print()` moves the output to the next line.

## 6.4 Print with end=""

```python
print("*", end="")
print("*", end="")
print("*", end="")
```

**Output:**

```text
***
```

No additional space is printed between characters.

## Important Comparison

| Code | Behaviour |
|---|---|
| `print("*")` | Prints star and moves to next line |
| `print("*", end=" ")` | Prints star followed by a space |
| `print("*", end="")` | Prints star without a separator |
| `print()` | Moves to the next line |

---

# 7. Understanding Spaces and Alignment

Spaces are important for creating properly aligned patterns.

They help us print:

- Right-aligned triangles.
- Centered pyramids.
- Inverted pyramids.
- Diamond patterns.
- Hollow shapes.

## Example – Right-Aligned Triangle

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end=" ")

    for star in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
        *
      * *
    * * *
  * * * *
* * * * *
```

## Understanding Spaces

For size 5:

| Row | Spaces | Stars |
|---|---:|---:|
| 1 | 4 | 1 |
| 2 | 3 | 2 |
| 3 | 2 | 3 |
| 4 | 1 | 4 |
| 5 | 0 | 5 |

Formula:

\[
\text{Spaces} = N - \text{Row}
\]

\[
\text{Stars} = \text{Row}
\]

## Centered Pyramid

```python
size = 4

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
   *
  ***
 *****
*******
```

The number of stars follows:

\[
\text{Stars} = 2 \times \text{Row} - 1
\]

This produces the odd numbers 1, 3, 5 and 7.

---

# 8. Star Patterns

Star patterns are among the first pattern-printing exercises.

They teach how to control the arrangement of repeated characters.

## 8.1 Square Pattern

A square pattern has the same number of rows and columns.

```python
size = 4

for row in range(size):

    for column in range(size):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

## 8.2 Right-Angled Triangle

```python
size = 5

for row in range(1, size + 1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

## 8.3 Inverted Right-Angled Triangle

```python
size = 5

for row in range(size, 0, -1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * * *
* * * *
* * *
* *
*
```

## 8.4 Right-Aligned Triangle

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end=" ")

    for star in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
        *
      * *
    * * *
  * * * *
* * * * *
```

## 8.5 Pyramid Pattern

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
    *
   ***
  *****
 *******
*********
```

## 8.6 Inverted Pyramid

```python
size = 5

for row in range(size, 0, -1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
*********
 *******
  *****
   ***
    *
```

## 8.7 Diamond Pattern

A diamond is made by combining an upper pyramid and a lower inverted pyramid.

```python
size = 4

# Upper half
for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()

# Lower half
for row in range(size - 1, 0, -1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

# 9. Number Patterns

Number patterns use digits instead of stars.

They help develop logical thinking about row numbers, column numbers and running counters.

## 9.1 Repeated Number Triangle

```python
size = 5

for row in range(1, size + 1):

    for column in range(row):
        print(row, end=" ")

    print()
```

**Output:**

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

The row number is printed repeatedly.

## 9.2 Increasing Number Triangle

```python
size = 5

for row in range(1, size + 1):

    for column in range(1, row + 1):
        print(column, end=" ")

    print()
```

**Output:**

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Here, the inner loop starts from 1 in every row.

## 9.3 Inverted Number Triangle

```python
size = 5

for row in range(size, 0, -1):

    for column in range(1, row + 1):
        print(column, end=" ")

    print()
```

**Output:**

```text
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

## 9.4 Floyd's Triangle

Floyd's triangle contains consecutive natural numbers arranged in triangular form.

```python
size = 5
number = 1

for row in range(1, size + 1):

    for column in range(row):
        print(number, end=" ")
        number += 1

    print()
```

**Output:**

```text
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

Important: The counter is initialized before the outer loop so that numbering continues across rows.

---

# 10. Alphabet Patterns

Alphabet patterns are similar to number patterns.

Python provides the `chr()` function to convert a Unicode code point into a character.

For English uppercase letters:

- A = 65
- B = 66
- C = 67
- D = 68
- E = 69

## Example – Alphabet Triangle

```python
size = 5

for row in range(1, size + 1):

    for column in range(row):
        character = chr(65 + column)
        print(character, end=" ")

    print()
```

**Output:**

```text
A
A B
A B C
A B C D
A B C D E
```

## Understanding chr()

```python
print(chr(65))
print(chr(66))
print(chr(67))
```

**Output:**

```text
A
B
C
```

## Example – Repeated Alphabet Rows

```python
size = 5

for row in range(1, size + 1):

    character = chr(64 + row)

    for column in range(row):
        print(character, end=" ")

    print()
```

**Output:**

```text
A
B B
C C C
D D D D
E E E E E
```

**Important:** The alphabet examples in the supplied Python file use `chr(65 + column)`. To display ordinary uppercase English letters without moving beyond Z, use a pattern size from 1 to 26.

---

# 11. Hollow Patterns

A hollow pattern displays characters only on its boundaries.

The inner portion remains empty.

Hollow patterns use conditions inside nested loops.

## 11.1 Hollow Square

```python
size = 5

for row in range(size):

    for column in range(size):

        if (
            row == 0
            or row == size - 1
            or column == 0
            or column == size - 1
        ):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
```

**Output:**

```text
* * * * *
*       *
*       *
*       *
* * * * *
```

## Understanding the Condition

A star is printed when:

- The row is the first row.
- The row is the last row.
- The column is the first column.
- The column is the last column.

Otherwise, spaces are printed.

## 11.2 Hollow Right-Angled Triangle

```python
size = 5

for row in range(1, size + 1):

    for column in range(1, row + 1):

        if (
            row == size
            or column == 1
            or column == row
        ):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
```

**Output:**

```text
*
* *
*   *
*     *
* * * * *
```

The pattern displays stars on the left boundary, right boundary and bottom boundary.

## 11.3 Hollow Pyramid

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for column in range(1, 2 * row):

        if (
            column == 1
            or column == 2 * row - 1
            or row == size
        ):
            print("*", end="")

        else:
            print(" ", end="")

    print()
```

**Output:**

```text
    *
   * *
  *   *
 *     *
*********
```

---

# 12. Twelve Topic Examples

These examples correspond to the twelve examples in `10_pattern_printing.py`.

## Example 01 – Square Star Pattern

**Objective:** Print a square with four rows and four columns.

```python
size = 4

for row in range(size):

    for column in range(size):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

**Explanation:**

The outer loop executes four times. The inner loop prints four stars during each iteration.

## Example 02 – Right-Angled Triangle

**Objective:** Print a triangle with five rows.

```python
size = 5

for row in range(1, size + 1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

**Explanation:**

The number of stars is equal to the current row number.

## Example 03 – Inverted Right-Angled Triangle

**Objective:** Print an inverted triangle.

```python
size = 5

for row in range(size, 0, -1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
* * * * *
* * * *
* * *
* *
*
```

**Explanation:**

The outer loop decreases from five to one.

## Example 04 – Right-Aligned Triangle

**Objective:** Print a triangle aligned to the right.

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end=" ")

    for star in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
        *
      * *
    * * *
  * * * *
* * * * *
```

**Explanation:**

The first inner loop prints spaces and the second prints stars.

## Example 05 – Pyramid Pattern

**Objective:** Print a centered pyramid.

```python
size = 5

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
    *
   ***
  *****
 *******
*********
```

**Explanation:**

Each row contains `2 × row - 1` stars.

## Example 06 – Inverted Pyramid

**Objective:** Print an inverted centered pyramid.

```python
size = 5

for row in range(size, 0, -1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
*********
 *******
  *****
   ***
    *
```

**Explanation:**

The number of stars decreases by two in each successive row.

## Example 07 – Diamond Pattern

**Objective:** Print a diamond shape.

```python
size = 4

for row in range(1, size + 1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()

for row in range(size - 1, 0, -1):

    for space in range(size - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Output:**

```text
   *
  ***
 *****
*******
 *****
  ***
   *
```

**Explanation:**

The upper half is a pyramid. The lower half is an inverted pyramid without repeating the middle row.

## Example 08 – Number Triangle

**Objective:** Display the row number repeatedly.

```python
size = 5

for row in range(1, size + 1):

    for column in range(row):
        print(row, end=" ")

    print()
```

**Output:**

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

**Explanation:**

The current outer-loop variable is printed during every inner-loop iteration.

## Example 09 – Floyd's Triangle

**Objective:** Print consecutive numbers in triangular form.

```python
size = 5
number = 1

for row in range(1, size + 1):

    for column in range(row):
        print(number, end=" ")
        number += 1

    print()
```

**Output:**

```text
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

**Explanation:**

The number variable increases every time a value is printed.

## Example 10 – Alphabet Triangle

**Objective:** Print alphabets in triangular form.

```python
size = 5

for row in range(1, size + 1):

    for column in range(row):
        character = chr(65 + column)
        print(character, end=" ")

    print()
```

**Output:**

```text
A
A B
A B C
A B C D
A B C D E
```

**Explanation:**

The `chr()` function converts numeric character codes into alphabet characters.

## Example 11 – Hollow Square

**Objective:** Print stars on the boundaries of a square.

```python
size = 5

for row in range(size):

    for column in range(size):

        if (
            row == 0
            or row == size - 1
            or column == 0
            or column == size - 1
        ):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
```

**Output:**

```text
* * * * *
*       *
*       *
*       *
* * * * *
```

**Explanation:**

The condition checks whether the current position lies on one of the four boundaries.

## Example 12 – Hollow Right-Angled Triangle

**Objective:** Print a hollow triangle.

```python
size = 5

for row in range(1, size + 1):

    for column in range(1, row + 1):

        if (
            row == size
            or column == 1
            or column == row
        ):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
```

**Output:**

```text
*
* *
*   *
*     *
* * * * *
```

**Explanation:**

Stars are printed on the left side, right side and bottom boundary.

---

# 13. Twelve Solved Programming Problems

Each problem includes a statement, logic, code, sample output, explanation and complexity.

## Problem 01 – Square Star Pattern

**Problem Statement:**

Take a number N from the user and print a square star pattern containing N rows and N columns.

**Logic:**

1. Read N.
2. Start an outer loop from zero to N-1.
3. Start an inner loop from zero to N-1.
4. Print a star in every inner-loop iteration.
5. Move to the next line after the inner loop completes.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(n):

    for column in range(n):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

**Explanation:**

Both loops execute N times.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 02 – Right-Angled Triangle

**Problem Statement:**

Print a right-angled triangle where each row contains as many stars as its row number.

**Logic:**

1. Read N.
2. Start the outer loop from 1 to N.
3. Execute the inner loop from zero to row-1.
4. Print a star.
5. Move to the next row.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(1, n + 1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
*
* *
* * *
* * * *
```

**Explanation:**

Each row adds one additional star.

**Complexity:**

- Time Complexity: O(N²), because the total number of printed stars is N(N+1)/2.
- Auxiliary Space Complexity: O(1)

## Problem 03 – Inverted Right-Angled Triangle

**Problem Statement:**

Print an inverted right-angled triangle containing N rows.

**Logic:**

1. Read N.
2. Start the outer loop from N and decrease to 1.
3. Print as many stars as the current row value.
4. Move to the next line.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(n, 0, -1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
* * * *
* * *
* *
*
```

**Explanation:**

The number of stars decreases by one in every row.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 04 – Right-Aligned Triangle

**Problem Statement:**

Print a right-aligned triangle containing N rows.

**Logic:**

1. Read N.
2. Calculate the spaces required for the current row.
3. Print `N - row` spaces.
4. Print `row` stars.
5. Move to the next line.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end=" ")

    for star in range(row):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
      *
    * *
  * * *
* * * *
```

**Explanation:**

The number of leading spaces decreases as the number of stars increases.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 05 – Centered Pyramid

**Problem Statement:**

Print a centered pyramid with N rows.

**Logic:**

1. Read N.
2. Print the required leading spaces.
3. Print an odd number of stars.
4. Move to the next row.

Number of stars:

\[
2 \times row - 1
\]

**Code:**

```python
n = int(input("Enter size: "))

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
   *
  ***
 *****
*******
```

**Explanation:**

The number of stars increases by two in each row.

**Complexity:**

- Time Complexity: O(N²), including the spaces printed.
- Auxiliary Space Complexity: O(1)

## Problem 06 – Inverted Pyramid

**Problem Statement:**

Print an inverted pyramid containing N rows.

**Logic:**

1. Read N.
2. Start the outer loop from N and decrease to 1.
3. Print leading spaces.
4. Print `2 × row - 1` stars.
5. Move to the next line.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(n, 0, -1):

    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
*******
 *****
  ***
   *
```

**Explanation:**

The number of stars decreases by two in every row.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 07 – Diamond Pattern

**Problem Statement:**

Print a diamond pattern using stars.

**Logic:**

1. Read N.
2. Print the upper pyramid.
3. Print the lower inverted pyramid.
4. Avoid repeating the middle row.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()

for row in range(n - 1, 0, -1):

    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Sample Input:**

```text
Enter size: 3
```

**Sample Output:**

```text
  *
 ***
*****
 ***
  *
```

**Explanation:**

The upper half contains N rows. The lower half contains N-1 rows.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 08 – Repeated Number Triangle

**Problem Statement:**

Print a triangle in which each row displays its row number repeatedly.

**Logic:**

1. Read N.
2. Start the outer loop from 1 to N.
3. Print the current row value as many times as the row number.
4. Move to the next line.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(1, n + 1):

    for column in range(row):
        print(row, end=" ")

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
1
2 2
3 3 3
4 4 4 4
```

**Explanation:**

The inner loop repeats the current row number.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 09 – Floyd's Triangle

**Problem Statement:**

Print Floyd's triangle containing consecutive natural numbers.

**Logic:**

1. Read N.
2. Initialize a counter with 1.
3. Start the outer loop from 1 to N.
4. Print the current counter.
5. Increase the counter.
6. Move to the next row.

**Code:**

```python
n = int(input("Enter size: "))

number = 1

for row in range(1, n + 1):

    for column in range(row):
        print(number, end=" ")
        number += 1

    print()
```

**Sample Input:**

```text
Enter size: 4
```

**Sample Output:**

```text
1
2 3
4 5 6
7 8 9 10
```

**Explanation:**

The counter is maintained outside the loops so that numbering continues across rows.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 10 – Alphabet Triangle

**Problem Statement:**

Print an alphabet triangle where each row begins with A and extends to the appropriate letter.

**Logic:**

1. Read N.
2. Keep the pattern size between 1 and 26.
3. Start the outer loop from 1 to N.
4. Convert the inner-loop position into an uppercase alphabet.
5. Print the character.
6. Move to the next row.

**Code:**

```python
n = int(input("Enter size (1-26): "))

if not 1 <= n <= 26:
    print("Enter a size between 1 and 26.")

else:
    for row in range(1, n + 1):

        for column in range(row):
            character = chr(65 + column)
            print(character, end=" ")

        print()
```

**Sample Input:**

```text
Enter size (1-26): 4
```

**Sample Output:**

```text
A
A B
A B C
A B C D
```

**Explanation:**

`chr()` converts the character codes 65, 66, 67 and 68 into A, B, C and D.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 11 – Hollow Square

**Problem Statement:**

Print a hollow square using stars.

**Logic:**

1. Read N.
2. Traverse every row and column.
3. Check whether the current position is on the boundary.
4. Print a star for boundary positions.
5. Print a space for inner positions.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(n):

    for column in range(n):

        if (
            row == 0
            or row == n - 1
            or column == 0
            or column == n - 1
        ):
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
```

**Sample Input:**

```text
Enter size: 5
```

**Sample Output:**

```text
* * * * *
*       *
*       *
*       *
* * * * *
```

**Explanation:**

The first and last rows, as well as the first and last columns, contain stars.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Problem 12 – Hollow Pyramid

**Problem Statement:**

Print a hollow centered pyramid using stars.

**Logic:**

1. Read N.
2. Print the leading spaces for each row.
3. Calculate the number of character positions.
4. Print stars on the left and right boundaries.
5. Print stars across the last row.
6. Print spaces in the interior.

**Code:**

```python
n = int(input("Enter size: "))

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end="")

    for column in range(1, 2 * row):

        if (
            column == 1
            or column == 2 * row - 1
            or row == n
        ):
            print("*", end="")

        else:
            print(" ", end="")

    print()
```

**Sample Input:**

```text
Enter size: 5
```

**Sample Output:**

```text
    *
   * *
  *   *
 *     *
*********
```

**Explanation:**

The first and last positions of every row contain stars. The bottom row is completely filled.

**Complexity:**

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

---

# 14. Ten Unsolved Practice Questions

Try solving these questions independently.

## Question 01 – Square Number Pattern

Print a square pattern using numbers instead of stars.

Example for N = 4:

```text
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

## Question 02 – Inverted Right-Aligned Triangle

Print an inverted right-aligned triangle using stars.

## Question 03 – Repeated Number Pyramid

Print a pyramid where each row contains its row number repeated an odd number of times.

Example for N = 4:

```text
   1
  222
 33333
4444444
```

## Question 04 – Inverted Number Triangle

Print the following pattern:

```text
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

## Question 05 – Alphabet Triangle

Print an alphabet triangle in which each row starts again from A.

## Question 06 – Number Diamond

Print a diamond pattern using numbers.

## Question 07 – Hollow Inverted Pyramid

Print an inverted hollow pyramid using stars.

## Question 08 – Hollow Rectangle

Print a hollow rectangle with user-defined rows and columns.

## Question 09 – Multiplication Table Pattern

Print a multiplication-table pattern in triangular form.

## Question 10 – Butterfly Star Pattern

Print a butterfly star pattern using nested loops.

---

# 15. Common Mistakes

## Mistake 01 – Forgetting the Inner Loop

Incorrect:

```python
for row in range(1, 5):
    print("*")
```

This prints four stars vertically, not a square.

Correct:

```python
for row in range(1, 5):

    for column in range(1, 5):
        print("*", end=" ")

    print()
```

## Mistake 02 – Forgetting the Newline

Incorrect:

```python
for row in range(1, 4):

    for column in range(row):
        print("*", end=" ")
```

All stars are printed on the same line.

Correct:

```python
for row in range(1, 4):

    for column in range(row):
        print("*", end=" ")

    print()
```

## Mistake 03 – Incorrect Range

Incorrect:

```python
for row in range(1, 5):
    print(row)
```

This creates four rows, not five.

Correct:

```python
for row in range(1, 6):
    print(row)
```

Python's stop value in `range()` is excluded.

## Mistake 04 – Incorrect Pyramid Formula

Incorrect:

```python
for row in range(1, 6):

    for star in range(row):
        print("*", end="")
```

This produces a triangle, not a centered pyramid.

Correct star-count formula:

\[
2 \times row - 1
\]

## Mistake 05 – Forgetting Spaces

Without spaces or alignment logic, a pyramid may appear as a left-aligned triangle.

Always calculate the required leading spaces.

## Mistake 06 – Incorrect Inverted Loop

For a decreasing pattern, remember that the stop value is exclusive.

Correct:

```python
for row in range(5, 0, -1):
    print(row)
```

## Mistake 07 – Misplacing Conditions in Hollow Patterns

The boundary checks must use the correct row and column indices.

For a hollow square:

```python
row == 0 or row == n - 1 or column == 0 or column == n - 1
```

## Mistake 08 – Reinitializing Floyd's Triangle Counter

Incorrect:

```python
for row in range(1, 5):

    number = 1

    for column in range(row):
        print(number)
        number += 1
```

The counter resets in every row.

Correct:

```python
number = 1

for row in range(1, 5):

    for column in range(row):
        print(number, end=" ")
        number += 1

    print()
```

## Mistake 09 – Exceeding the English Alphabet

When using `chr(65 + column)`, limit the regular alphabet pattern to 26 positions.

Otherwise, the sequence moves beyond Z into other Unicode characters.

## Mistake 10 – Incorrect Indentation

Nested loops require correct indentation.

Statements inside the inner loop must be indented more than statements inside the outer loop.

---

# 16. Best Practices

Follow these practices while writing pattern programs.

1. Identify the number of rows before writing code.
2. Calculate how many characters each row should contain.
3. Decide whether spaces are required.
4. Write the outer loop first.
5. Add the inner loop for columns.
6. Use meaningful variable names such as row, column, space and star.
7. Use `print(..., end=...)` carefully.
8. Use an empty `print()` after completing each row.
9. Check `range()` start, stop and step values.
10. Use conditions for hollow patterns.
11. Initialize running counters outside loops when values must continue across rows.
12. Test small pattern sizes first.
13. Avoid unnecessary loops.
14. Keep pattern formulas readable.
15. Add input validation for user-defined sizes.
16. Use string repetition for simple patterns when nested loops are not the learning objective.
17. Understand the logic instead of memorizing code.

---

# 17. Debugging Pattern Programs

Debugging helps identify why an output pattern is not aligned or does not match the expected design.

## Debugging Checklist

Check the following:

- Is the outer loop controlling the correct number of rows?
- Is the inner loop controlling the correct number of columns?
- Is `range()` using the correct start and stop values?
- Is the step correct for decreasing patterns?
- Are stars printed in the correct positions?
- Are spaces calculated correctly?
- Is the newline printed after each row?
- Is the running number initialized outside the correct loop?
- Are boundary conditions correct?
- Is the pattern size valid?

## Debugging Example

```python
size = 4

for row in range(1, size + 1):

    print("Current row:", row)

    for column in range(row):
        print("*", end=" ")

    print()
```

**Output:**

```text
Current row: 1
*

Current row: 2
* *

Current row: 3
* * *

Current row: 4
* * * *
```

The debug message shows how the outer loop changes the number of stars.

## Testing Different Sizes

Always test:

- Size 1.
- Size 2.
- A medium size such as 5.
- The maximum allowed size.

This helps identify range and boundary mistakes.

---

# 18. Real-Life Applications

Pattern printing is mainly an educational exercise, but the concepts behind it appear in real programming.

## 18.1 Console-Based Menus

Nested loops can display structured rows and columns in text-based applications.

## 18.2 Multiplication Tables

Nested loops are used to generate multiplication tables.

```python
for row in range(1, 6):

    for column in range(1, 6):
        print(row * column, end="\t")

    print()
```

## 18.3 Seating Layouts

A program can represent seats arranged in rows and columns.

```python
rows = 3
columns = 4

for row in range(rows):

    for column in range(columns):
        print("Seat", end=" ")

    print()
```

## 18.4 Grid-Based Games

Games may represent a board using rows and columns.

For example, a small game board can be represented with a two-dimensional list.

## 18.5 Data Tables

Nested loops can display tabular information in a terminal.

## 18.6 Matrix Representation

Nested loops help display rows and columns of matrix elements.

## 18.7 ASCII Art

Text characters can be arranged to create simple shapes, designs and illustrations.

## 18.8 Educational Programming Tools

Pattern generators help beginners understand how loop variables affect output.

---

# 19. Connection with Data Structures and Algorithms

Pattern printing provides a foundation for understanding nested iterations.

These ideas are useful in data structures and algorithms.

## 19.1 Matrix Traversal

A matrix contains rows and columns.

Nested loops can access each element.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):

    for column in range(len(matrix[row])):
        print(matrix[row][column], end=" ")

    print()
```

**Output:**

```text
1 2 3
4 5 6
7 8 9
```

## 19.2 Two-Dimensional Arrays

Pattern printing and two-dimensional arrays both use row-column indexing.

```python
for row in range(3):

    for column in range(3):
        print(f"({row}, {column})", end=" ")

    print()
```

## 19.3 Nested Loop Comparison

Some algorithms compare every element with other elements.

Example:

```python
numbers = [10, 20, 30, 40]

for first in numbers:

    for second in numbers:
        print(first, second)
```

The total number of pairs is:

\[
N \times N = N^2
\]

## 19.4 Algorithm Analysis

Pattern printing helps demonstrate:

- Single-loop complexity.
- Nested-loop complexity.
- Triangular nested-loop complexity.
- Conditional execution inside loops.
- Output-dependent time complexity.

Understanding nested loops will help when studying:

- Bubble Sort.
- Selection Sort.
- Matrix Traversal.
- Pair Comparisons.
- Two-Dimensional Arrays.
- Brute-Force Algorithms.

Pattern printing itself does not implement these algorithms, but it develops the loop logic used by them.

---

# 20. Time and Space Complexity

Complexity analysis describes how the work performed by a program changes as the pattern size increases.

Let N represent the pattern size.

## 20.1 Square Pattern

A square has N rows and N columns.

Total stars:

\[
N \times N = N^2
\]

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## 20.2 Right-Angled Triangle

The number of stars is:

\[
1 + 2 + 3 + \cdots + N
\]

Using the sum formula:

\[
\frac{N(N+1)}{2}
\]

Therefore:

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## 20.3 Pyramid

The number of stars in each row is:

\[
2r - 1
\]

The total number of stars grows quadratically.

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## 20.4 Floyd's Triangle

Floyd's triangle contains:

\[
1 + 2 + 3 + \cdots + N
\]

numbers.

Therefore:

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## 20.5 Hollow Square

The program checks N × N positions, even though only boundary positions display stars.

- Time Complexity: O(N²)
- Auxiliary Space Complexity: O(1)

## Complexity Summary

| Pattern | Time Complexity | Auxiliary Space |
|---|---|---|
| Square | O(N²) | O(1) |
| Right-angled triangle | O(N²) | O(1) |
| Inverted triangle | O(N²) | O(1) |
| Right-aligned triangle | O(N²) | O(1) |
| Pyramid | O(N²) | O(1) |
| Inverted pyramid | O(N²) | O(1) |
| Diamond | O(N²) | O(1) |
| Number triangle | O(N²) | O(1) |
| Floyd's triangle | O(N²) | O(1) |
| Alphabet triangle | O(N²) | O(1) |
| Hollow square | O(N²) | O(1) |
| Hollow triangle | O(N²) | O(1) |

The space figures refer to auxiliary working space and exclude the terminal output itself.

---

# 21. Mini Project – Pattern Generator

## Project Objective

Create a small Pattern Generator program that allows the user to select a pattern and specify its size.

The application should support:

1. Square star pattern.
2. Right-angled triangle.
3. Inverted triangle.
4. Pyramid.
5. Diamond.
6. Number triangle.

## Project Code

```python
"""
Mini Project: Pattern Generator

Concepts:
- Functions
- Nested loops
- Conditional statements
- Range function
- Input validation
"""


def square_pattern(size: int) -> None:
    """Print a square star pattern."""
    for row in range(size):

        for column in range(size):
            print("*", end=" ")

        print()


def triangle_pattern(size: int) -> None:
    """Print a right-angled triangle."""
    for row in range(1, size + 1):

        for column in range(row):
            print("*", end=" ")

        print()


def inverted_triangle(size: int) -> None:
    """Print an inverted triangle."""
    for row in range(size, 0, -1):

        for column in range(row):
            print("*", end=" ")

        print()


def pyramid_pattern(size: int) -> None:
    """Print a centered pyramid."""
    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


def diamond_pattern(size: int) -> None:
    """Print a diamond."""
    for row in range(1, size + 1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()

    for row in range(size - 1, 0, -1):

        for space in range(size - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


def number_triangle(size: int) -> None:
    """Print a repeated number triangle."""
    for row in range(1, size + 1):

        for column in range(row):
            print(row, end=" ")

        print()


def main() -> None:
    """Run the pattern generator menu."""
    print("=" * 40)
    print("PYTHON PATTERN GENERATOR")
    print("=" * 40)

    print("1. Square Pattern")
    print("2. Right-Angled Triangle")
    print("3. Inverted Triangle")
    print("4. Pyramid")
    print("5. Diamond")
    print("6. Number Triangle")

    try:
        choice = int(input("\nSelect pattern: "))
        size = int(input("Enter pattern size (1-30): "))

    except ValueError:
        print("Invalid input. Enter integers only.")
        return

    if not 1 <= size <= 30:
        print("Pattern size must be between 1 and 30.")
        return

    patterns = {
        1: square_pattern,
        2: triangle_pattern,
        3: inverted_triangle,
        4: pyramid_pattern,
        5: diamond_pattern,
        6: number_triangle
    }

    if choice not in patterns:
        print("Invalid pattern selection.")
        return

    print("\nGenerated Pattern:")
    print("-" * 40)

    patterns[choice](size)


if __name__ == "__main__":
    main()
```

## Sample Input

```text
PYTHON PATTERN GENERATOR
1. Square Pattern
2. Right-Angled Triangle
3. Inverted Triangle
4. Pyramid
5. Diamond
6. Number Triangle

Select pattern: 4
Enter pattern size (1-30): 4
```

## Sample Output

```text
Generated Pattern:
----------------------------------------
   *
  ***
 *****
*******
```

## Concepts Used

- Functions.
- Nested loops.
- Dictionaries.
- Input validation.
- Conditional statements.
- Pattern logic.
- Function calls.

## Possible Improvements

1. Add alphabet patterns.
2. Add hollow patterns.
3. Add custom characters.
4. Add rectangular patterns.
5. Add a repeat menu.
6. Add pattern saving to a text file.

---

# 22. Fifty Python Viva Questions and Answers

## Basic Questions

**Q1. What is pattern printing in Python?**

Pattern printing is the process of displaying characters, numbers or symbols in a specific arrangement using programming statements.

**Q2. Which concept is mainly used in pattern printing?**

Nested loops.

**Q3. What is a nested loop?**

A loop written inside another loop.

**Q4. What does the outer loop generally control?**

The number of rows.

**Q5. What does the inner loop generally control?**

The number of columns or characters in a row.

**Q6. Which function is used to display patterns?**

The `print()` function.

**Q7. What is the purpose of `end=" "`?**

It keeps output on the same line and adds a space after the printed value.

**Q8. What does an empty `print()` do?**

It moves the cursor to the next line.

**Q9. Can pattern printing be performed with a single loop?**

Yes, simple patterns can be created using a single loop or string repetition. Nested loops are common for more complex patterns.

**Q10. Why are nested loops useful?**

They allow us to control rows and columns independently.

## Conceptual Questions

**Q11. What is a square pattern?**

A pattern with equal numbers of rows and columns.

**Q12. What is a right-angled triangle?**

A triangular pattern in which each successive row contains one additional character.

**Q13. What is an inverted triangle?**

A triangle in which the number of characters decreases with each row.

**Q14. What is a pyramid pattern?**

A centered triangular pattern generally containing an odd number of symbols in each row.

**Q15. What is a diamond pattern?**

A pattern formed by combining an upper pyramid and a lower inverted pyramid.

**Q16. What is a hollow pattern?**

A pattern that displays characters on its boundaries while leaving interior positions empty.

**Q17. Why are spaces important in pattern printing?**

They help control alignment and positioning.

**Q18. What does `range(1, 5)` generate?**

It generates 1, 2, 3 and 4.

**Q19. Why is the stop value excluded in range()?**

Python's range function generates values up to, but not including, its stop value.

**Q20. What is the purpose of a negative step in range()?**

It allows iteration in decreasing order.

## Programming Questions

**Q21. How can you print a square pattern?**

Use two loops, both executing N times.

**Q22. How can you print a right-angled triangle?**

Make the inner loop execute as many times as the current row number.

**Q23. How can you print an inverted triangle?**

Use a decreasing range for the outer loop.

**Q24. How do you align a triangle to the right?**

Print leading spaces before printing stars in each row.

**Q25. What is the formula for pyramid stars?**

`2 * row - 1`.

**Q26. How can you print a diamond?**

Combine a pyramid and an inverted pyramid without repeating the middle row.

**Q27. How can you print a number triangle?**

Use a nested loop and print the row number or column number.

**Q28. What is Floyd's triangle?**

A triangular arrangement of consecutive positive integers.

**Q29. Which function converts an integer character code to a character?**

`chr()`.

**Q30. What is the character code of uppercase A?**

65.

## Advanced Questions

**Q31. How can a hollow square be printed?**

Use conditions to print stars only on the first row, last row, first column and last column.

**Q32. What is the difference between a solid square and a hollow square?**

A solid square fills every position, whereas a hollow square displays characters only on its boundaries.

**Q33. What is the time complexity of a square pattern with N rows?**

O(N²).

**Q34. What is the total number of stars in a right-angled triangle of size N?**

N(N+1)/2.

**Q35. What is the time complexity of a triangular pattern?**

O(N²).

**Q36. What is the role of indentation in pattern printing?**

It determines which statements belong to the outer and inner loops.

**Q37. Can conditions be used inside nested loops?**

Yes. They help decide which character should be printed at each position.

**Q38. How is an alphabet pattern generated?**

By converting character codes into characters using `chr()`.

**Q39. Why should Floyd's triangle counter be initialized outside the loops?**

So that numbering continues across all rows instead of restarting in every row.

**Q40. Can a loop print both spaces and stars in the same row?**

Yes. Separate loops can print the spaces and stars.

## Practical and DSA Questions

**Q41. How is pattern printing related to matrix traversal?**

Both commonly use nested loops to process rows and columns.

**Q42. What is a two-dimensional array?**

A data structure arranged in rows and columns.

**Q43. Can nested loops be used to display a multiplication table?**

Yes.

**Q44. What is the difference between a row and a column?**

A row is horizontal, while a column is vertical.

**Q45. What is the purpose of the outer loop in matrix traversal?**

It generally selects each row.

**Q46. What is the worst-case time complexity of comparing all pairs in a list using two nested loops?**

O(N²).

**Q47. Does pattern printing itself implement sorting algorithms?**

No. It teaches nested-loop logic that can later help with understanding algorithms such as Bubble Sort and Selection Sort.

**Q48. What happens when the inner loop executes zero times?**

No values are printed by the inner loop during that outer iteration.

**Q49. How can pattern size be validated?**

Read an integer and check that it falls within an allowed range.

**Q50. What is the most important skill developed through pattern printing?**

Logical thinking about loops, conditions, rows, columns and repeated execution.

---

# 23. Important Terminology

| Term | Meaning |
|---|---|
| Pattern Printing | Displaying values in a structured arrangement |
| Nested Loop | A loop inside another loop |
| Outer Loop | Loop that commonly controls rows |
| Inner Loop | Loop that commonly controls columns |
| Row | Horizontal arrangement of characters |
| Column | Vertical position |
| Star Pattern | Pattern created using star symbols |
| Number Pattern | Pattern created using digits |
| Alphabet Pattern | Pattern created using letters |
| Pyramid | Centered triangular pattern |
| Diamond | Combination of two pyramid sections |
| Hollow Pattern | Pattern with boundary characters and empty interior |
| Range | Sequence generator used in Python loops |
| Step | Difference between consecutive values in a range |
| End Parameter | Controls what print adds after output |
| ASCII Code | Commonly used character-code reference for basic English characters |
| Unicode | Standard for representing text characters |
| Matrix | Two-dimensional arrangement of values |
| Time Complexity | Measure of how work grows with input size |
| Auxiliary Space | Additional memory used during execution |

---

# 24. Quick Revision Notes

## Important Code Patterns

**Square:**

```python
for row in range(n):

    for column in range(n):
        print("*", end=" ")

    print()
```

**Right-Angled Triangle:**

```python
for row in range(1, n + 1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Inverted Triangle:**

```python
for row in range(n, 0, -1):

    for column in range(row):
        print("*", end=" ")

    print()
```

**Right-Aligned Triangle:**

```python
for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end=" ")

    for star in range(row):
        print("*", end=" ")

    print()
```

**Pyramid:**

```python
for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end="")

    for star in range(2 * row - 1):
        print("*", end="")

    print()
```

**Floyd's Triangle:**

```python
number = 1

for row in range(1, n + 1):

    for column in range(row):
        print(number, end=" ")
        number += 1

    print()
```

**Hollow Square Condition:**

```python
if (
    row == 0
    or row == n - 1
    or column == 0
    or column == n - 1
):
    print("*", end=" ")

else:
    print(" ", end=" ")
```

## Important Formulas

| Pattern | Formula |
|---|---|
| Square columns | N |
| Triangle stars | Row |
| Inverted triangle stars | N - Row + 1 |
| Right-aligned spaces | N - Row |
| Pyramid stars | 2 × Row - 1 |
| Floyd's triangle values | N(N+1)/2 |
| Diamond rows | 2N - 1 |

## Important Rules

1. Outer loop generally controls rows.
2. Inner loop generally controls columns.
3. `end=" "` keeps output on the same line.
4. `print()` moves to the next line.
5. Spaces control alignment.
6. Conditions control hollow patterns.
7. A counter outside the loops can preserve consecutive numbering.
8. The stop value of range is excluded.
9. A negative step supports decreasing patterns.
10. Pattern size should be validated.

---

# 25. Learning Checklist

Mark each item after understanding and practising it.

- [ ] Understand pattern printing.
- [ ] Understand nested loops.
- [ ] Understand outer and inner loops.
- [ ] Understand rows and columns.
- [ ] Understand the `end` parameter.
- [ ] Print square star patterns.
- [ ] Print right-angled triangles.
- [ ] Print inverted triangles.
- [ ] Print right-aligned triangles.
- [ ] Print centered pyramids.
- [ ] Print inverted pyramids.
- [ ] Print diamond patterns.
- [ ] Print repeated number triangles.
- [ ] Print increasing number triangles.
- [ ] Print Floyd's triangle.
- [ ] Print alphabet triangles.
- [ ] Understand character conversion using `chr()`.
- [ ] Print hollow squares.
- [ ] Print hollow triangles.
- [ ] Print hollow pyramids.
- [ ] Understand spaces and alignment.
- [ ] Understand pattern complexity.
- [ ] Complete all twelve solved problems.
- [ ] Attempt all ten unsolved questions.
- [ ] Complete the Pattern Generator mini project.
- [ ] Revise the fifty viva questions.

---

# 26. How to Run the Python File

## Step 1 – Open the Repository

Open your `DSA-Python` repository in VS Code.

## Step 2 – Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 10-Pattern-Printing/
```

## Step 3 – Open the Python File

Open:

```text
10_pattern_printing.py
```

## Step 4 – Open the Terminal

Open the integrated terminal in VS Code.

## Step 5 – Run the Python File

From the repository root, execute:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/10-Pattern-Printing/10_pattern_printing.py
```

## Step 6 – Select an Option

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Select an option to explore the topic.

---

# 27. Repository Structure

Store both files in the following location:

```text
DSA-Python/
└── PYTHON/
    └── Python-Fundamentals/
        └── 01-Loops/
            └── 10-Pattern-Printing/
                ├── README.md
                └── 10_pattern_printing.py
```

## File Description

| File | Purpose |
|---|---|
| README.md | Detailed theory, examples, problems, practice questions and viva |
| 10_pattern_printing.py | Executable Python examples and interactive practice menu |

---

# 28. Git Commands

After adding both files, execute these commands from your repository root:

```powershell
git status
```

```powershell
git add "PYTHON/Python-Fundamentals/01-Loops/10-Pattern-Printing/"
```

```powershell
git commit -m "Add pattern printing lesson"
```

```powershell
git push origin main
```

These commands stage, commit and push your topic if each operation completes successfully.

---

# 29. Final Summary

Pattern printing is an important programming topic that develops logical thinking and improves understanding of nested loops.

It helps you learn:

- Outer and inner loops.
- Rows and columns.
- Range function.
- Print function.
- Spaces and alignment.
- Star patterns.
- Number patterns.
- Alphabet patterns.
- Hollow patterns.
- Pattern complexity.

These concepts also provide a foundation for understanding matrix traversal and nested-loop algorithms.

Before moving to the next section:

1. Understand all twelve examples.
2. Practise the twelve solved problems.
3. Attempt the ten unsolved questions.
4. Complete the Pattern Generator mini project.
5. Revise the fifty viva questions.

**Topic 10 – Pattern Printing: Completed Study Notes.**

**01-Loops: All 10 topics completed.**