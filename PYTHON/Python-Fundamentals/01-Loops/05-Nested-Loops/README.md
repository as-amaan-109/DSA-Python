# Nested Loops in Python

## 1. Introduction

Nested loops are an important concept in Python programming.

A nested loop means writing one loop inside another loop.

The loop written outside is called the **outer loop**, and the loop written inside it is called the **inner loop**.

The inner loop executes completely for every iteration of the outer loop.

Nested loops are useful when a task involves multiple levels of repetition.

For example, consider printing a square pattern containing three rows and three columns.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

In this example:

- The outer loop controls the rows.
- The inner loop controls the columns.
- The inner loop executes three times for every outer-loop iteration.
- The outer loop executes three times.
- The total number of inner-loop executions is nine.

Nested loops are commonly used in:

- Pattern printing.
- Matrix operations.
- Two-dimensional lists.
- Multiplication tables.
- Coordinate generation.
- Pair comparisons.
- Searching and sorting.
- Combinations and permutations.
- Data processing.
- Data Structures and Algorithms.

Understanding nested loops is important before learning matrix operations and several basic DSA algorithms.

---

## 2. Learning Objectives

After completing this topic, you should be able to:

1. Define nested loops.
2. Understand why nested loops are used.
3. Identify the outer loop.
4. Identify the inner loop.
5. Understand how nested loops execute.
6. Understand the relationship between rows and columns.
7. Print square star patterns.
8. Print rectangular star patterns.
9. Print right-angled triangle patterns.
10. Print inverted triangle patterns.
11. Print number patterns.
12. Generate multiplication grids.
13. Generate coordinate pairs.
14. Understand two-dimensional lists.
15. Traverse a matrix using nested loops.
16. Accept matrix input from the user.
17. Display matrix elements.
18. Calculate the sum of matrix elements.
19. Calculate row-wise sums.
20. Calculate the main diagonal sum.
21. Count occurrences of an element in a matrix.
22. Understand nested-loop iteration counts.
23. Analyze nested-loop time complexity.
24. Identify unnecessary nested loops.
25. Apply nested loops to beginner-level DSA problems.

---

## 3. What Are Nested Loops?

A nested loop is a loop placed inside another loop.

The outer loop controls the main repetition.

The inner loop performs repeated operations during every outer-loop iteration.

### Basic Syntax

```python
for outer_variable in outer_iterable:
    for inner_variable in inner_iterable:
        statement
```

A nested loop can also contain `while` loops.

### Example

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

### Explanation

The outer loop executes three times.

For every outer-loop iteration, the inner loop executes three times.

The inner loop prints three stars.

The `print()` statement after the inner loop moves the output to the next line.

The complete pattern contains three rows and three columns.

### Important Terms

**Outer Loop:** The loop that contains another loop.

**Inner Loop:** The loop written inside the outer loop.

**Nested Loop:** A loop placed inside another loop.

**Iteration:** One complete execution of a loop body.

**Row:** A horizontal group of elements.

**Column:** A vertical group of elements.

**Matrix:** A rectangular arrangement of values in rows and columns.

---

## 4. Why Do We Use Nested Loops?

Some programming tasks require repetition at more than one level.

A normal loop is sufficient for processing a simple sequence.

However, when a problem involves rows and columns, pairs of elements, or multiple dimensions, nested loops can make the solution easier to express.

### Example Without Nested Loops

Suppose we need to print a square containing three rows and three columns.

Writing every row separately would create repeated code.

### Using Nested Loops

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

The loops handle the repeated operations automatically.

### Advantages of Nested Loops

1. Simplify two-dimensional repetition.
2. Make row and column processing easier.
3. Help generate patterns.
4. Support matrix operations.
5. Help compare pairs of values.
6. Support combinations and pair generation.
7. Help implement basic sorting algorithms.
8. Make multidimensional data processing possible.
9. Reduce repeated statements.
10. Support several DSA techniques.

### Common Applications

- Star patterns.
- Number patterns.
- Multiplication grids.
- Matrix traversal.
- Matrix addition.
- Matrix multiplication.
- Pair comparisons.
- Table generation.
- Data analysis.
- Algorithm implementation.

---

## 5. Understanding the Outer Loop

The outer loop is the loop that contains another loop.

It usually controls the larger repetition structure.

For example, when printing a pattern, the outer loop commonly controls the number of rows.

### Example

```python
for row in range(1, 4):
    print("Row:", row)
```

Output:

```text
Row: 1
Row: 2
Row: 3
```

The outer loop executes three times.

### Outer Loop in a Nested Structure

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

The outer loop controls the three rows.

For every new row, the inner loop starts again.

### Important Point

The outer loop does not execute the inner loop only once.

The inner loop executes completely during every outer-loop iteration.

---

## 6. Understanding the Inner Loop

The inner loop is written inside the outer loop.

It executes repeatedly for every iteration of the outer loop.

### Example

```python
for row in range(1, 3):
    for column in range(1, 4):
        print(column, end=" ")

    print()
```

Output:

```text
1 2 3
1 2 3
```

### Explanation

The outer loop executes twice.

For each outer-loop iteration, the inner loop generates:

```text
1 2 3
```

Therefore, the sequence is printed twice.

### Important Point

When the outer loop moves to its next iteration, the inner loop starts its execution again from the beginning of its iterable or initial condition.

---

## 7. How Nested Loops Execute

Consider this program:

```python
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

### Execution Explanation

During the first outer-loop iteration:

```text
row = 1
```

The inner loop executes:

```text
column = 1
column = 2
column = 3
```

During the second outer-loop iteration:

```text
row = 2
```

The inner loop executes again:

```text
column = 1
column = 2
column = 3
```

### Execution Table

| Outer Iteration | Row Value | Inner Iteration | Column Value |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 1 | 1 | 2 | 2 |
| 1 | 1 | 3 | 3 |
| 2 | 2 | 1 | 1 |
| 2 | 2 | 2 | 2 |
| 2 | 2 | 3 | 3 |

### Total Iterations

The outer loop executes two times.

The inner loop executes three times for each outer iteration.

Therefore:

```text
Total iterations = 2 × 3
                 = 6
```

This multiplication rule is important for understanding nested-loop complexity.

---

## 8. Nested For Loops

A nested `for` loop contains one `for` loop inside another `for` loop.

### Syntax

```python
for outer in outer_iterable:
    for inner in inner_iterable:
        statement
```

### Example

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

### Applications

- Printing patterns.
- Processing matrices.
- Generating coordinate pairs.
- Comparing elements.
- Generating multiplication tables.
- Creating combinations.

Nested `for` loops are especially convenient when the iteration boundaries are known or based on iterable objects.

---

## 9. Nested While Loops

A `while` loop can also be placed inside another `while` loop.

### Syntax

```python
outer = 1

while outer <= 3:
    inner = 1

    while inner <= 3:
        print("*", end=" ")
        inner += 1

    print()
    outer += 1
```

Output:

```text
* * *
* * *
* * *
```

### Explanation

The outer loop controls the rows.

The inner loop controls the columns.

The inner variable is initialized inside the outer loop because it must restart for every new row.

### Important Point

When using nested `while` loops, initialize and update each control variable correctly.

Incorrect initialization or updates can result in unexpected output or an infinite loop.

---

## 10. Rows and Columns

Rows and columns are important concepts in nested-loop programming.

A row represents a horizontal group of elements.

A column represents a vertical group of elements.

### Example: Three Rows and Four Columns

```python
for row in range(1, 4):
    for column in range(1, 5):
        print("*", end=" ")

    print()
```

Output:

```text
* * * *
* * * *
* * * *
```

### Explanation

The outer loop controls three rows.

The inner loop controls four columns.

Total elements:

```text
3 × 4 = 12
```

### General Structure

```python
for row in range(number_of_rows):
    for column in range(number_of_columns):
        statement
```

### Row and Column Reference

| Row | Column 1 | Column 2 | Column 3 |
|---|---|---|---|
| Row 1 | Element | Element | Element |
| Row 2 | Element | Element | Element |
| Row 3 | Element | Element | Element |

The same row-column structure is used in matrices and two-dimensional lists.

---

## 11. Nested Loops for Square Patterns

A square pattern contains the same number of rows and columns.

### Example: Three-by-Three Square

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

### Example: Five-by-Five Square

```python
for row in range(5):
    for column in range(5):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### Logic

The outer loop creates the rows.

The inner loop prints five stars in each row.

The outer loop repeats this five times.

---

## 12. Nested Loops for Rectangular Patterns

A rectangle can contain different numbers of rows and columns.

### Example: Three Rows and Five Columns

```python
for row in range(3):
    for column in range(5):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * * *
* * * * *
```

### Explanation

The row count is three.

The column count is five.

The total number of printed stars is:

```text
3 × 5 = 15
```

### General Pattern

```python
rows = 3
columns = 5

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")

    print()
```

This structure is useful for displaying rectangular data and grids.

---

## 13. Right-Angled Triangle Pattern

A right-angled triangle can be created by changing the number of columns for each row.

### Example

```python
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")

    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

### Explanation

The outer loop starts from one and ends at five.

The inner loop executes according to the current row number.

For example:

- Row 1 prints one star.
- Row 2 prints two stars.
- Row 3 prints three stars.
- Row 4 prints four stars.
- Row 5 prints five stars.

### Important Pattern Logic

The number of stars increases by one in each row.

---

## 14. Inverted Triangle Pattern

An inverted triangle starts with the maximum number of stars and decreases the count after every row.

### Example

```python
for row in range(5, 0, -1):
    for column in range(row):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * *
* * *
* *
*
```

### Explanation

The outer loop starts at five and decreases to one.

The inner loop prints the number of stars indicated by the current row value.

### Important Pattern Logic

The number of stars decreases by one after every row.

---

## 15. Number Triangle Pattern

Nested loops can also generate number patterns.

### Example 1: Increasing Numbers in Each Row

```python
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")

    print()
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Explanation

The outer loop controls the rows.

The inner loop prints numbers from one to the current row number.

### Example 2: Repeating the Row Number

```python
for row in range(1, 6):
    for column in range(row):
        print(row, end=" ")

    print()
```

Output:

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

### Example 3: Increasing Number Grid

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end=" ")

    print()
```

Output:

```text
1 2 3
2 4 6
3 6 9
```

Different inner-loop expressions create different patterns.

---

## 16. Generating Multiplication Grids

Nested loops can generate multiplication grids.

### Example

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end="\t")

    print()
```

Output:

```text
1       2       3
2       4       6
3       6       9
```

### Explanation

The outer loop controls the first multiplication value.

The inner loop controls the second multiplication value.

Every combination is multiplied and displayed.

### Example: Five-by-Five Multiplication Grid

```python
for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end="\t")

    print()
```

Output:

```text
1       2       3       4       5
2       4       6       8       10
3       6       9       12      15
4       8       12      16      20
5       10      15      20      25
```

---

## 17. Generating Coordinate Pairs

Nested loops can generate all possible pairs from two numeric sequences.

### Example

```python
for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x}, {y})")
```

Output:

```text
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
```

### Explanation

The outer loop generates three values for X.

The inner loop generates two values for Y.

Every X value is paired with every Y value.

### Total Number of Pairs

```text
3 × 2 = 6
```

### Applications

- Coordinate generation.
- Pair comparisons.
- Combinations.
- Testing all possible pairs.
- Grid-based problems.

---

## 18. Nested Loops with Two Lists

Nested loops can combine elements from two different lists.

### Example

```python
colors = ["Red", "Green"]
sizes = ["Small", "Large"]

for color in colors:
    for size in sizes:
        print(color, size)
```

Output:

```text
Red Small
Red Large
Green Small
Green Large
```

### Explanation

Every color is combined with every size.

The outer loop processes the colors.

The inner loop processes the sizes for the current color.

### Total Combinations

There are two colors and two sizes.

Therefore:

```text
2 × 2 = 4 combinations
```

This is useful for generating possible combinations of two sets of values.

---

## 19. Introduction to Two-Dimensional Lists

A two-dimensional list is a list that contains other lists.

It is commonly used to represent tabular data and matrices.

### Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

This matrix contains three rows and three columns.

### Structure

```text
1 2 3
4 5 6
7 8 9
```

### Accessing an Element

```python
print(matrix[0][0])
```

Output:

```text
1
```

The first index selects the row.

The second index selects the column.

### Another Example

```python
print(matrix[1][2])
```

Output:

```text
6
```

The row index is one and the column index is two.

### Important Point

Python list indexes start from zero.

For a matrix with three rows and three columns, valid indexes are zero, one, and two for both dimensions.

---

## 20. Matrix Traversal Using Nested Loops

Matrix traversal means visiting every element in a matrix.

Nested loops are commonly used for this operation.

### Example

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

Output:

```text
1 2 3
4 5 6
7 8 9
```

### Explanation

The outer loop accesses each row.

The inner loop accesses each element in the current row.

The expression:

```python
matrix[row][column]
```

accesses an individual matrix element.

### Important Functions

`len(matrix)` returns the number of rows.

`len(matrix[row])` returns the number of elements in the current row.

### General Pattern

```python
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])
```

This approach also supports rows with different lengths.

---

## 21. Reading Matrix Input from the User

A matrix can be created by accepting row and column values from the user.

### Example

```python
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

matrix = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        value = int(input("Enter element: "))
        current_row.append(value)

    matrix.append(current_row)

print("\nMatrix:")

for row in matrix:
    for value in row:
        print(value, end="\t")

    print()
```

### Explanation

The outer loop creates each row.

The inner loop accepts the elements in that row.

After completing a row, the row is appended to the matrix.

### Sample Input

```text
Enter rows: 2
Enter columns: 3
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Enter element: 6
```

### Sample Output

```text
Matrix:
1       2       3
4       5       6
```

---

## 22. Sum of Matrix Elements

Nested loops can calculate the sum of every element in a matrix.

### Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        total += matrix[row][column]

print("Matrix sum:", total)
```

Output:

```text
Matrix sum: 21
```

### Explanation

The matrix elements are:

```text
1, 2, 3, 4, 5, 6
```

Their sum is:

```text
1 + 2 + 3 + 4 + 5 + 6 = 21
```

### General Formula

The sum of matrix elements is the sum of every individual value.

For an R by C matrix, the traversal processes R × C elements.

---

## 23. Row-Wise and Column-Wise Operations

Nested loops can perform calculations for every row or every column.

### 23.1 Row-Wise Sum

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):
    total = 0

    for column in range(len(matrix[row])):
        total += matrix[row][column]

    print("Row sum:", total)
```

Output:

```text
Row sum: 6
Row sum: 15
Row sum: 24
```

### 23.2 Column-Wise Sum

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for column in range(len(matrix[0])):
    total = 0

    for row in range(len(matrix)):
        total += matrix[row][column]

    print("Column sum:", total)
```

Output:

```text
Column sum: 12
Column sum: 15
Column sum: 18
```

### Important Difference

For row-wise calculations, the outer loop selects rows.

For column-wise calculations, the outer loop selects columns.

The inner loop processes the corresponding elements.

---

## 24. Main Diagonal of a Matrix

The main diagonal of a square matrix contains elements whose row index and column index are equal.

### Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if row == column:
            print(matrix[row][column], end=" ")
```

Output:

```text
1 5 9
```

### Explanation

The main diagonal elements are located at:

```text
matrix[0][0]
matrix[1][1]
matrix[2][2]
```

The row and column indexes are equal.

### Main Diagonal Sum

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for index in range(len(matrix)):
    total += matrix[index][index]

print("Main diagonal sum:", total)
```

Output:

```text
Main diagonal sum: 15
```

The diagonal sum is:

```text
1 + 5 + 9 = 15
```

---

## 25. Twelve Topic Examples

These examples correspond to the twelve examples in `05_nested_loops.py`.

### Example 1: Basic Nested Loop

**Objective:** Print a three-by-three square of stars.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")

    print()
```

Output:

```text
* * *
* * *
* * *
```

Explanation:

The outer loop creates the rows.

The inner loop prints three stars in every row.

### Example 2: Rectangular Star Pattern

**Objective:** Print three rows and five columns.

```python
for row in range(1, 4):
    for column in range(1, 6):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * * *
* * * * *
```

Explanation:

The outer loop controls three rows.

The inner loop controls five columns.

### Example 3: Right-Angled Triangle

**Objective:** Print an increasing star triangle.

```python
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")

    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

Explanation:

The number of columns depends on the current row value.

### Example 4: Inverted Triangle

**Objective:** Print a decreasing star triangle.

```python
for row in range(5, 0, -1):
    for column in range(row):
        print("*", end=" ")

    print()
```

Output:

```text
* * * * *
* * * *
* * *
* *
*
```

Explanation:

The outer loop decreases the row count.

The inner loop prints the required number of stars.

### Example 5: Number Triangle

**Objective:** Print numbers from one to the current row number.

```python
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")

    print()
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

Explanation:

The inner loop prints an increasing sequence in every row.

### Example 6: Multiplication Grid

**Objective:** Generate a three-by-three multiplication grid.

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end="\t")

    print()
```

Output:

```text
1       2       3
2       4       6
3       6       9
```

Explanation:

Each row and column value is multiplied.

### Example 7: Coordinate Pairs

**Objective:** Generate coordinate pairs.

```python
for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x}, {y})", end=" ")

    print()
```

Output:

```text
(1, 1) (1, 2)
(2, 1) (2, 2)
(3, 1) (3, 2)
```

Explanation:

Every X value is paired with every Y value.

### Example 8: Pairs from Two Lists

**Objective:** Generate all color and size combinations.

```python
colors = ["Red", "Green"]
sizes = ["Small", "Large"]

for color in colors:
    for size in sizes:
        print(color, size)
```

Output:

```text
Red Small
Red Large
Green Small
Green Large
```

Explanation:

The inner loop completes for every color.

### Example 9: Matrix Traversal

**Objective:** Display every element of a matrix.

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

Output:

```text
1 2 3
4 5 6
7 8 9
```

Explanation:

The outer loop selects the row.

The inner loop accesses the elements of the current row.

### Example 10: Sum of Matrix Elements

**Objective:** Calculate the sum of all matrix values.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        total += matrix[row][column]

print("Matrix sum:", total)
```

Output:

```text
Matrix sum: 21
```

Explanation:

Each matrix element is added to the accumulator.

### Example 11: Main Diagonal Elements

**Objective:** Display the main diagonal of a square matrix.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if row == column:
            print(matrix[row][column], end=" ")

print()
```

Output:

```text
1 5 9
```

Explanation:

The condition selects elements whose row and column indexes are equal.

### Example 12: Checkerboard Pattern

**Objective:** Print an alternating X and O pattern.

```python
for row in range(1, 5):
    for column in range(1, 5):
        if (row + column) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")

    print()
```

Output:

```text
X O X O
O X O X
X O X O
O X O X
```

Explanation:

The sum of the row and column positions determines which character is printed.

---

## 26. Twelve Solved Programming Problems

### Problem 1: Square Star Pattern

**Problem Statement:**

Accept a positive integer N and print a square pattern containing N rows and N columns.

**Logic:**

1. Read N.
2. Start the outer loop for rows.
3. Start the inner loop for columns.
4. Print one star for each inner-loop iteration.
5. Move to the next line after completing a row.

**Code:**

```python
n = int(input("Enter the size of the square: "))

for row in range(n):
    for column in range(n):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter the size of the square: 3
```

**Sample Output:**

```text
* * *
* * *
* * *
```

**Explanation:**

Both loops execute three times.

The outer loop creates three rows.

The inner loop prints three stars in every row.

**Complexity:**

- Time: O(N²).
- Auxiliary space: O(1).

### Problem 2: Rectangle Star Pattern

**Problem Statement:**

Accept the number of rows and columns and print a rectangular star pattern.

**Logic:**

1. Read the row count.
2. Read the column count.
3. Use the outer loop for rows.
4. Use the inner loop for columns.
5. Print a star during every inner-loop iteration.

**Code:**

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for row in range(rows):
    for column in range(columns):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter the number of rows: 3
Enter the number of columns: 5
```

**Sample Output:**

```text
* * * * *
* * * * *
* * * * *
```

**Explanation:**

The outer loop executes three times.

The inner loop executes five times for every row.

Total stars:

```text
3 × 5 = 15
```

**Complexity:**

- Time: O(R × C).
- Auxiliary space: O(1).

### Problem 3: Right-Angled Triangle

**Problem Statement:**

Accept a number N and print a right-angled triangle containing N rows.

**Logic:**

1. Read N.
2. Start the outer loop from one.
3. Use the current row number to determine the number of stars.
4. Print the stars.
5. Move to the next row.

**Code:**

```python
n = int(input("Enter the number of rows: "))

for row in range(1, n + 1):
    for column in range(row):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter the number of rows: 5
```

**Sample Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

**Explanation:**

The first row contains one star.

The second row contains two stars.

The pattern continues until the final row contains N stars.

**Complexity:**

- Time: O(N²), because the total number of stars is N(N + 1)/2.
- Auxiliary space: O(1).

### Problem 4: Inverted Triangle

**Problem Statement:**

Accept a number N and print an inverted right-angled triangle.

**Logic:**

1. Read N.
2. Start the outer loop from N.
3. Decrease the row value after each iteration.
4. Print the number of stars indicated by the row value.
5. Continue until one row remains.

**Code:**

```python
n = int(input("Enter the number of rows: "))

for row in range(n, 0, -1):
    for column in range(row):
        print("*", end=" ")

    print()
```

**Sample Input:**

```text
Enter the number of rows: 5
```

**Sample Output:**

```text
* * * * *
* * * *
* * *
* *
*
```

**Explanation:**

The first row contains N stars.

The next row contains N - 1 stars.

The number of stars decreases until it reaches one.

**Complexity:**

- Time: O(N²).
- Auxiliary space: O(1).

### Problem 5: Number Triangle

**Problem Statement:**

Accept N and print a number triangle where every row contains numbers from one up to the current row number.

**Logic:**

1. Read N.
2. Use the outer loop to control rows.
3. Use the inner loop to generate numbers.
4. Print the current column value.
5. Move to the next row.

**Code:**

```python
n = int(input("Enter the number of rows: "))

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(column, end=" ")

    print()
```

**Sample Input:**

```text
Enter the number of rows: 4
```

**Sample Output:**

```text
1
1 2
1 2 3
1 2 3 4
```

**Explanation:**

The inner loop starts at one and ends at the current row number.

**Complexity:**

- Time: O(N²).
- Auxiliary space: O(1).

### Problem 6: Multiplication Grid

**Problem Statement:**

Accept an integer N and display an N-by-N multiplication grid.

**Logic:**

1. Read N.
2. Use the outer loop for rows.
3. Use the inner loop for columns.
4. Multiply the current row and column values.
5. Display each product.

**Code:**

```python
n = int(input("Enter the grid size: "))

for row in range(1, n + 1):
    for column in range(1, n + 1):
        print(row * column, end="\t")

    print()
```

**Sample Input:**

```text
Enter the grid size: 3
```

**Sample Output:**

```text
1       2       3
2       4       6
3       6       9
```

**Explanation:**

Each row and column value is multiplied.

The result is displayed in its corresponding grid position.

**Complexity:**

- Time: O(N²).
- Auxiliary space: O(1).

### Problem 7: Coordinate Pairs

**Problem Statement:**

Accept two positive integers and generate all coordinate pairs from the corresponding ranges.

**Logic:**

1. Read the X range limit.
2. Read the Y range limit.
3. Use the outer loop to generate X values.
4. Use the inner loop to generate Y values.
5. Display every combination.

**Code:**

```python
x_limit = int(input("Enter the X range limit: "))
y_limit = int(input("Enter the Y range limit: "))

for x in range(1, x_limit + 1):
    for y in range(1, y_limit + 1):
        print(f"({x}, {y})")
```

**Sample Input:**

```text
Enter the X range limit: 2
Enter the Y range limit: 3
```

**Sample Output:**

```text
(1, 1)
(1, 2)
(1, 3)
(2, 1)
(2, 2)
(2, 3)
```

**Explanation:**

Every X value is combined with every Y value.

The total number of pairs is X limit multiplied by Y limit.

**Complexity:**

- Time: O(X × Y).
- Auxiliary space: O(1).

### Problem 8: Display Matrix

**Problem Statement:**

Accept a matrix from the user and display its elements in row and column format.

**Logic:**

1. Read the number of rows.
2. Read the number of columns.
3. Create an empty matrix.
4. Use the outer loop to create rows.
5. Use the inner loop to read column values.
6. Append each completed row.
7. Display the matrix using nested loops.

**Code:**

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        value = int(
            input(
                f"Enter element at row {row + 1}, "
                f"column {column + 1}: "
            )
        )

        current_row.append(value)

    matrix.append(current_row)

print("\nMatrix:")

for row in range(rows):
    for column in range(columns):
        print(matrix[row][column], end="\t")

    print()
```

**Sample Input:**

```text
Enter the number of rows: 2
Enter the number of columns: 2
Enter element at row 1, column 1: 1
Enter element at row 1, column 2: 2
Enter element at row 2, column 1: 3
Enter element at row 2, column 2: 4
```

**Sample Output:**

```text
Matrix:
1       2
3       4
```

**Explanation:**

The outer loop creates rows.

The inner loop accepts the values in each row.

The completed matrix is displayed using another pair of loops.

**Complexity:**

- Time: O(R × C) for reading and displaying.
- Auxiliary space: O(R × C) for the matrix.

### Problem 9: Sum of Matrix Elements

**Problem Statement:**

Accept a matrix and calculate the sum of all its elements.

**Logic:**

1. Read the matrix dimensions.
2. Accept all matrix values.
3. Initialize the total with zero.
4. Traverse every row and column.
5. Add every element to total.
6. Display the final sum.

**Code:**

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        value = int(input("Enter element: "))
        current_row.append(value)

    matrix.append(current_row)

total = 0

for row in range(rows):
    for column in range(columns):
        total += matrix[row][column]

print("Sum of matrix elements:", total)
```

**Sample Input:**

```text
Enter the number of rows: 2
Enter the number of columns: 3
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Enter element: 6
```

**Sample Output:**

```text
Sum of matrix elements: 21
```

**Explanation:**

All matrix values are added:

```text
1 + 2 + 3 + 4 + 5 + 6 = 21
```

**Complexity:**

- Time: O(R × C) for traversal, excluding input overhead.
- Auxiliary space: O(R × C) for storing the matrix.
- Additional summation space: O(1).

### Problem 10: Row-Wise Matrix Sum

**Problem Statement:**

Accept a matrix and calculate the sum of each row separately.

**Logic:**

1. Read the matrix dimensions.
2. Accept matrix elements.
3. Start the outer loop for rows.
4. Initialize a row total with zero.
5. Use the inner loop to process the current row.
6. Add every element to the row total.
7. Display the sum of that row.

**Code:**

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        value = int(input("Enter element: "))
        current_row.append(value)

    matrix.append(current_row)

print("\nRow-wise sums:")

for row in range(rows):
    row_total = 0

    for column in range(columns):
        row_total += matrix[row][column]

    print(f"Row {row + 1} sum:", row_total)
```

**Sample Input:**

```text
Enter the number of rows: 3
Enter the number of columns: 2
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Enter element: 6
```

**Sample Output:**

```text
Row-wise sums:
Row 1 sum: 3
Row 2 sum: 7
Row 3 sum: 11
```

**Explanation:**

Each row gets a separate accumulator.

The inner loop calculates the sum of the current row.

**Complexity:**

- Time: O(R × C).
- Auxiliary space: O(R × C) for the matrix.
- Additional calculation space: O(1).

### Problem 11: Main Diagonal Sum

**Problem Statement:**

Accept a square matrix and calculate the sum of its main diagonal elements.

**Logic:**

1. Read the matrix size.
2. Accept a square matrix.
3. Initialize the diagonal sum with zero.
4. Traverse the matrix.
5. Check whether row and column indexes are equal.
6. Add the corresponding element to the diagonal sum.
7. Display the result.

**Code:**

```python
n = int(input("Enter the matrix size: "))

matrix = []

for row in range(n):
    current_row = []

    for column in range(n):
        value = int(input("Enter element: "))
        current_row.append(value)

    matrix.append(current_row)

diagonal_sum = 0

for row in range(n):
    for column in range(n):
        if row == column:
            diagonal_sum += matrix[row][column]

print("Main diagonal sum:", diagonal_sum)
```

**Sample Input:**

```text
Enter the matrix size: 3
Enter element: 1
Enter element: 2
Enter element: 3
Enter element: 4
Enter element: 5
Enter element: 6
Enter element: 7
Enter element: 8
Enter element: 9
```

**Sample Output:**

```text
Main diagonal sum: 15
```

**Explanation:**

The main diagonal is:

```text
1 5 9
```

The sum is:

```text
1 + 5 + 9 = 15
```

**Complexity:**

- Time: O(N²) for the full nested traversal.
- Auxiliary space: O(N²) for the matrix.
- Additional summation space: O(1).

### Problem 12: Count Matrix Element

**Problem Statement:**

Accept a matrix and a target value. Count how many times the target appears in the matrix.

**Logic:**

1. Read the matrix dimensions.
2. Accept all matrix values.
3. Read the target value.
4. Initialize a counter with zero.
5. Traverse every matrix element.
6. Compare each value with the target.
7. Increase the counter when a match is found.
8. Display the count.

**Code:**

```python
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for row in range(rows):
    current_row = []

    for column in range(columns):
        value = int(input("Enter element: "))
        current_row.append(value)

    matrix.append(current_row)

target = int(input("Enter the value to search: "))

count = 0

for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == target:
            count += 1

print(f"Occurrences of {target}:", count)
```

**Sample Input:**

```text
Enter the number of rows: 2
Enter the number of columns: 3
Enter element: 1
Enter element: 2
Enter element: 2
Enter element: 3
Enter element: 2
Enter element: 4
Enter the value to search: 2
```

**Sample Output:**

```text
Occurrences of 2: 3
```

**Explanation:**

The value two appears three times in the matrix.

The loops examine every element and increase the counter for each match.

**Complexity:**

- Time: O(R × C).
- Auxiliary space: O(R × C) for the matrix.
- Additional counting space: O(1).

---

## 27. Ten Unsolved Practice Questions

Attempt these problems independently before looking for solutions.

### Question 1: Hollow Square Pattern

Write a program to print a hollow square star pattern.

Example:

```text
Input:
N = 5

Expected Output:
* * * * *
*       *
*       *
*       *
* * * * *
```

### Question 2: Pyramid Star Pattern

Write a program to print a centered pyramid of stars.

Example:

```text
Input:
N = 4

Expected Output:
      *
    * * *
  * * * * *
* * * * * * *
```

### Question 3: Inverted Number Triangle

Write a program to print a decreasing number triangle.

Example:

```text
Input:
N = 4

Expected Output:
1 2 3 4
1 2 3
1 2
1
```

### Question 4: Floyd's Triangle

Write a program to generate Floyd's triangle.

Example:

```text
Input:
N = 4

Expected Output:
1
2 3
4 5 6
7 8 9 10
```

### Question 5: Multiplication Table Grid

Write a program to generate a multiplication grid from one to ten.

Example:

```text
Expected Output:
1   2   3   ... 10
2   4   6   ... 20
3   6   9   ... 30
...
10  20  30  ... 100
```

### Question 6: Column-Wise Matrix Sum

Write a program to calculate the sum of each column of a matrix.

Example:

```text
Input Matrix:
1 2 3
4 5 6
7 8 9

Expected Output:
Column 1 sum: 12
Column 2 sum: 15
Column 3 sum: 18
```

### Question 7: Secondary Diagonal Sum

Write a program to calculate the sum of the secondary diagonal elements of a square matrix.

Example:

```text
Input Matrix:
1 2 3
4 5 6
7 8 9

Expected Output:
Secondary diagonal sum: 15
```

### Question 8: Transpose of a Matrix

Write a program to find the transpose of a matrix using nested loops.

Example:

```text
Input Matrix:
1 2 3
4 5 6

Expected Output:
1 4
2 5
3 6
```

### Question 9: Count Even and Odd Matrix Elements

Write a program to count even and odd values in a matrix.

Example:

```text
Input Matrix:
1 2 3
4 5 6

Expected Output:
Even elements: 3
Odd elements: 3
```

### Question 10: Find Pairs with a Target Sum

Write a program to find all pairs of elements whose sum equals a given target.

Example:

```text
Input:
Numbers = [1, 2, 3, 4, 5]
Target = 6

Expected Output:
(1, 5)
(2, 4)
```

---

## 28. Common Mistakes While Using Nested Loops

### Mistake 1: Confusing the Outer and Inner Loops

The outer loop generally controls the larger repetition.

The inner loop processes values during each outer iteration.

Understand which loop is responsible for rows and which is responsible for columns.

### Mistake 2: Incorrect Indentation

Incorrect:

```python
for row in range(3):
for column in range(3):
    print("*")
```

Correct:

```python
for row in range(3):
    for column in range(3):
        print("*")
```

The inner loop must be indented inside the outer loop.

### Mistake 3: Placing print() at the Wrong Level

Incorrect:

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")
        print()
```

This moves to a new line after every star.

Correct:

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")

    print()
```

The final `print()` is outside the inner loop but inside the outer loop.

### Mistake 4: Incorrect Inner Loop Boundary

Incorrect:

```python
for row in range(3):
    for column in range(row):
        print("*", end=" ")

    print()
```

For row zero, the inner loop has no iterations.

Correct for a triangle starting with one star:

```python
for row in range(1, 4):
    for column in range(row):
        print("*", end=" ")

    print()
```

### Mistake 5: Forgetting to Reset the Inner While Variable

Incorrect:

```python
row = 1
column = 1

while row <= 3:
    while column <= 3:
        print("*", end=" ")
        column += 1

    print()
    row += 1
```

The inner variable is not reset for the next outer iteration.

Correct:

```python
row = 1

while row <= 3:
    column = 1

    while column <= 3:
        print("*", end=" ")
        column += 1

    print()
    row += 1
```

### Mistake 6: Using Incorrect Matrix Indexes

Incorrect:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in range(len(matrix)):
    for column in range(len(matrix)):
        print(matrix[row][column])
```

The number of columns is three, but the inner loop only executes twice.

Correct:

```python
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])
```

### Mistake 7: Forgetting to Initialize an Accumulator

Incorrect:

```python
for row in range(3):
    for column in range(3):
        total += matrix[row][column]
```

The variable `total` must be initialized.

Correct:

```python
total = 0

for row in range(3):
    for column in range(3):
        total += matrix[row][column]
```

### Mistake 8: Not Resetting the Row Total

Incorrect:

```python
total = 0

for row in range(3):
    for column in range(3):
        total += matrix[row][column]

    print(total)
```

This prints cumulative totals, not individual row sums.

Correct:

```python
for row in range(3):
    row_total = 0

    for column in range(3):
        row_total += matrix[row][column]

    print(row_total)
```

### Mistake 9: Incorrect Diagonal Condition

The main diagonal uses equal row and column indexes.

Correct condition:

```python
if row == column:
    print(matrix[row][column])
```

The secondary diagonal uses:

```python
if row + column == n - 1:
    print(matrix[row][column])
```

### Mistake 10: Ignoring the Complexity of Nested Loops

Two loops do not always automatically mean O(N²).

The iteration count depends on the loop boundaries.

For example, a rectangular matrix with R rows and C columns takes O(R × C) time to traverse.

Always analyze the actual number of iterations.

---

## 29. Best Practices for Nested Loops

1. Give meaningful names to row and column variables.
2. Keep inner loops properly indented.
3. Understand the role of each loop.
4. Initialize inner `while` variables for each outer iteration when necessary.
5. Use `len()` to determine sequence boundaries.
6. Check list indexes before accessing elements.
7. Use row-wise and column-wise logic carefully.
8. Initialize accumulators before their use.
9. Reset row-wise accumulators for every row.
10. Use suitable formatting for patterns and matrices.
11. Avoid unnecessary nested loops.
12. Do not modify a collection unexpectedly while iterating over it.
13. Test small matrix dimensions first.
14. Check rectangular matrices as well as square matrices.
15. Use separate functions for complex matrix operations.
16. Handle empty or irregular input structures where relevant.
17. Avoid unnecessary repeated calculations.
18. Understand the number of iterations.
19. Analyze time and space complexity.
20. Prefer a simpler algorithm when one exists.

---

## 30. Debugging Nested Loop Programs

Debugging helps identify mistakes in loop structure, conditions, indexing, and calculations.

### 30.1 Print the Outer Loop Variable

```python
for row in range(3):
    print("Current row:", row)

    for column in range(2):
        print("*", end=" ")

    print()
```

This helps identify how many times the outer loop executes.

### 30.2 Print the Inner Loop Variable

```python
for row in range(2):
    for column in range(3):
        print("Row:", row, "Column:", column)
```

This displays the row and column values during execution.

### 30.3 Check the Total Iterations

For a rectangular nested loop:

```python
for row in range(rows):
    for column in range(columns):
        print(row, column)
```

The total number of inner-loop executions is:

```text
rows × columns
```

### 30.4 Check Matrix Dimensions

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Rows:", len(matrix))
print("Columns in first row:", len(matrix[0]))
```

Output:

```text
Rows: 2
Columns in first row: 3
```

### 30.5 Check Index Boundaries

For a row of length three, valid indexes are:

```text
0, 1, 2
```

Index three is invalid.

### 30.6 Test Small Inputs

For pattern programs, begin with one, two, or three rows.

For matrix programs, begin with a two-by-two or two-by-three matrix.

Small inputs make incorrect execution easier to identify.

### 30.7 Common Errors

| Error | Possible Cause |
|---|---|
| `SyntaxError` | Incorrect Python syntax |
| `IndentationError` | Incorrect indentation |
| `IndexError` | Invalid row or column index |
| `TypeError` | Unsupported operation |
| `ValueError` | Invalid input conversion |
| `NameError` | Undefined variable |

---

## 31. Real-Life Applications of Nested Loops

### 31.1 Student Marks Tables

A program can use rows for students and columns for subjects.

The loops can process each student's marks.

### 31.2 Matrix Operations

Matrix addition, subtraction, multiplication, and traversal commonly use nested loops.

### 31.3 Seating Arrangements

A classroom seating arrangement can be represented using rows and columns.

### 31.4 Game Boards

Chessboards and other grid-based games use row-column structures.

### 31.5 Product Combinations

An application can generate combinations of products, colors, and sizes.

### 31.6 Image Processing

Images can be represented as grids of pixels.

Loops can process rows, columns, and pixel values.

### 31.7 Timetables

A timetable can represent days as rows and periods as columns.

### 31.8 Spreadsheet Processing

Nested loops can process rows and columns of tabular data.

### 31.9 Data Analysis

Programs can compare values and calculate statistics across multiple groups.

### 31.10 Pattern Generation

Nested loops can create visual patterns and repeated layouts.

---

## 32. Connection Between Nested Loops and DSA

Nested loops play an important role in several Data Structures and Algorithms concepts.

They are commonly used when an algorithm needs to examine multiple elements in relation to one another.

### 32.1 Two-Dimensional Array Traversal

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])
```

Time complexity: O(R × C).

### 32.2 Pair Comparisons

```python
numbers = [1, 2, 3, 4]

for first in range(len(numbers)):
    for second in range(first + 1, len(numbers)):
        print(
            numbers[first],
            numbers[second]
        )
```

This generates pairs with distinct positions where the first index is smaller than the second.

Time complexity: O(N²).

### 32.3 Finding Duplicate Values

```python
numbers = [1, 2, 3, 2, 4, 1]

for first in range(len(numbers)):
    for second in range(first + 1, len(numbers)):
        if numbers[first] == numbers[second]:
            print("Duplicate:", numbers[first])
```

This compares pairs of elements to identify duplicates.

Time complexity: O(N²).

### 32.4 Bubble Sort

Bubble Sort compares adjacent values and swaps them when required.

A basic implementation uses nested loops.

### 32.5 Selection Sort

Selection Sort repeatedly searches for the minimum value in the unsorted part of an array.

Nested loops are commonly used in its basic implementation.

### 32.6 Matrix Addition

Two matrices of the same dimensions can be added element by element using nested loops.

### 32.7 Matrix Multiplication

Standard matrix multiplication uses nested iteration to calculate the resulting matrix values.

A basic implementation commonly uses three nested loops.

### 32.8 Combinations

Nested loops can generate pairs and combinations of collection elements.

### 32.9 Search Problems

Some brute-force search problems examine multiple element pairs using nested loops.

### 32.10 Complexity Analysis

Nested loops are important when learning Big O notation.

They help demonstrate how the number of operations grows with the input size.

---

## 33. Time and Space Complexity

Time complexity describes how the running time of an algorithm grows with input size.

Space complexity describes how much additional memory an algorithm requires.

Nested loops require careful analysis because their iteration counts multiply when their bounds depend independently on input sizes.

### 33.1 Fixed Nested Loops

```python
for row in range(3):
    for column in range(3):
        print("*")
```

The loops always perform nine inner-loop iterations.

Time complexity: O(1), because both dimensions are constant.

### 33.2 Two Linear Nested Loops

```python
for row in range(n):
    for column in range(n):
        print(row, column)
```

The outer loop executes N times.

The inner loop executes N times for every outer iteration.

Total operations:

```text
N × N = N²
```

Time complexity: O(N²).

### 33.3 Rectangular Matrix Traversal

```python
for row in range(rows):
    for column in range(columns):
        print(row, column)
```

Total operations:

```text
R × C
```

Time complexity: O(R × C).

### 33.4 Three Nested Loops

```python
for first in range(n):
    for second in range(n):
        for third in range(n):
            print(first, second, third)
```

Total iterations:

```text
N × N × N = N³
```

Time complexity: O(N³).

### 33.5 Triangular Nested Loop

```python
for row in range(n):
    for column in range(row + 1):
        print(row, column)
```

The inner-loop iteration counts are:

```text
1 + 2 + 3 + ... + N
```

The total is:

```text
N(N + 1) / 2
```

Time complexity: O(N²).

### 33.6 Two Consecutive Nested Loop Structures

```python
for row in range(n):
    for column in range(n):
        print(row, column)

for row in range(n):
    print(row)
```

Total operations grow as:

```text
N² + N
```

The dominant term is N².

Time complexity: O(N²).

### 33.7 Space Complexity of Matrix Storage

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

A matrix containing R rows and C columns stores R × C elements.

Space complexity for the matrix: O(R × C).

### Complexity Reference

| Loop Structure | Typical Time Complexity |
|---|---|
| Two fixed-size loops | O(1) |
| Two nested N-sized loops | O(N²) |
| Three nested N-sized loops | O(N³) |
| Rows R and columns C | O(R × C) |
| Triangular nested loop | O(N²) |
| One loop followed by nested loops | O(N²), when nested work is N² |
| Matrix storage | O(R × C) space |

### Important Note

Nested loops do not always mean O(N²).

The actual complexity depends on:

- The number of outer-loop iterations.
- The number of inner-loop iterations.
- Whether the inner-loop boundary depends on the outer-loop variable.
- The work performed inside the innermost loop.

---

## 34. Mini Project: Matrix Analyzer

### Project Objective

Create a program that accepts a matrix and performs different operations using nested loops.

The project should:

1. Accept the number of rows.
2. Accept the number of columns.
3. Read all matrix elements.
4. Display the matrix.
5. Calculate the total sum.
6. Calculate row-wise sums.
7. Calculate column-wise sums.
8. Count even and odd elements.
9. Search for a target value.

### Project Code

```python
"""
Project: Matrix Analyzer

Description:
Accept a matrix and perform basic operations
using nested loops.
"""


def read_matrix(rows: int, columns: int) -> list[list[int]]:
    """
    Read matrix elements from the user.
    """
    matrix = []

    for row in range(rows):
        current_row = []

        for column in range(columns):
            value = int(
                input(
                    f"Enter element at row {row + 1}, "
                    f"column {column + 1}: "
                )
            )

            current_row.append(value)

        matrix.append(current_row)

    return matrix


def display_matrix(matrix: list[list[int]]) -> None:
    """
    Display all elements of a matrix.
    """
    for row in matrix:
        for value in row:
            print(value, end="\t")

        print()


def calculate_total(matrix: list[list[int]]) -> int:
    """
    Calculate the sum of all matrix elements.
    """
    total = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            total += matrix[row][column]

    return total


def display_row_sums(matrix: list[list[int]]) -> None:
    """
    Display the sum of every row.
    """
    for row in range(len(matrix)):
        total = 0

        for column in range(len(matrix[row])):
            total += matrix[row][column]

        print(f"Row {row + 1} sum:", total)


def display_column_sums(matrix: list[list[int]]) -> None:
    """
    Display the sum of every column.
    """
    if not matrix:
        return

    column_count = len(matrix[0])

    for column in range(column_count):
        total = 0

        for row in range(len(matrix)):
            total += matrix[row][column]

        print(f"Column {column + 1} sum:", total)


def count_even_odd(matrix: list[list[int]]) -> None:
    """
    Count even and odd matrix elements.
    """
    even_count = 0
    odd_count = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            value = matrix[row][column]

            if value % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    print("Even elements:", even_count)
    print("Odd elements:", odd_count)


def search_matrix(
    matrix: list[list[int]],
    target: int
) -> int:
    """
    Count occurrences of a target value.
    """
    count = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == target:
                count += 1

    return count


def main() -> None:
    """
    Accept a matrix and display its analysis.
    """
    try:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))

        if rows <= 0 or columns <= 0:
            print("Rows and columns must be positive.")
            return

        matrix = read_matrix(rows, columns)

        print("\nMATRIX")
        display_matrix(matrix)

        print("\nMATRIX ANALYSIS")
        print("Total sum:", calculate_total(matrix))

        print("\nROW-WISE SUMS")
        display_row_sums(matrix)

        print("\nCOLUMN-WISE SUMS")
        display_column_sums(matrix)

        print("\nEVEN AND ODD ELEMENTS")
        count_even_odd(matrix)

        target = int(input("\nEnter a value to search: "))

        occurrences = search_matrix(matrix, target)

        print(
            f"Occurrences of {target}:",
            occurrences
        )

    except ValueError:
        print("Invalid input. Please enter integers.")


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter the number of rows: 2
Enter the number of columns: 3
Enter element at row 1, column 1: 1
Enter element at row 1, column 2: 2
Enter element at row 1, column 3: 3
Enter element at row 2, column 1: 4
Enter element at row 2, column 2: 5
Enter element at row 2, column 3: 6
Enter a value to search: 2
```

### Sample Output

```text
MATRIX
1       2       3
4       5       6

MATRIX ANALYSIS
Total sum: 21

ROW-WISE SUMS
Row 1 sum: 6
Row 2 sum: 15

COLUMN-WISE SUMS
Column 1 sum: 5
Column 2 sum: 7
Column 3 sum: 9

EVEN AND ODD ELEMENTS
Even elements: 3
Odd elements: 3

Occurrences of 2: 1
```

### Concepts Used

- Nested loops.
- Two-dimensional lists.
- Matrix traversal.
- Rows and columns.
- Accumulators.
- Counters.
- Conditions.
- Functions.
- Input validation.
- Basic data processing.

---

## 35. Fifty Viva Questions and Answers

### Basic Nested Loop Questions

**Q1. What is a nested loop?**

A nested loop is a loop written inside another loop.

**Q2. What is an outer loop?**

The outer loop is the loop that contains another loop.

**Q3. What is an inner loop?**

The inner loop is the loop written inside the outer loop.

**Q4. Why are nested loops used?**

They are used when a task requires multiple levels of repetition.

**Q5. What is the basic syntax of a nested for loop?**

```python
for outer in iterable:
    for inner in iterable:
        statement
```

**Q6. How many times does the inner loop execute?**

It executes completely for every outer-loop iteration.

**Q7. What is an iteration?**

One complete execution of a loop body.

**Q8. Can a while loop be nested inside a for loop?**

Yes. Python allows different loop types to be nested.

**Q9. Can a for loop be nested inside a while loop?**

Yes. Python allows a `for` loop inside a `while` loop.

**Q10. What is the role of indentation in nested loops?**

Indentation identifies which statements belong to each loop.

### Execution Questions

**Q11. What is the outer loop commonly used for in pattern printing?**

It commonly controls the rows.

**Q12. What is the inner loop commonly used for in pattern printing?**

It commonly controls the columns or repeated items in each row.

**Q13. If the outer loop executes three times and the inner loop executes four times, how many inner-loop executions occur?**

Twelve executions.

**Q14. How do you print a square star pattern?**

Use two loops with the same iteration count.

**Q15. How do you print a rectangular pattern?**

Use an outer loop for rows and an inner loop for columns.

**Q16. How do you print a right-angled triangle?**

Make the inner-loop boundary depend on the current row.

**Q17. How do you print an inverted triangle?**

Decrease the outer-loop value after each row and use it as the inner-loop boundary.

**Q18. What does `print()` do after the inner loop in a pattern?**

It moves the output to the next line.

**Q19. How can coordinate pairs be generated?**

Use two loops to generate combinations of the values from two sequences.

**Q20. What is a multiplication grid?**

A two-dimensional arrangement of products generated using row and column values.

### Matrix Questions

**Q21. What is a matrix in Python?**

A matrix can be represented using a two-dimensional list.

**Q22. What is a two-dimensional list?**

A list containing other lists as elements.

**Q23. How do you access an element of a matrix?**

Use `matrix[row][column]`.

**Q24. What does `len(matrix)` return for a non-empty rectangular matrix?**

It returns the number of rows.

**Q25. How do you find the number of columns in a rectangular matrix?**

Use `len(matrix[0])` when the matrix contains at least one row.

**Q26. How do you traverse every matrix element?**

Use nested loops over the row and column indexes.

**Q27. What is the main diagonal?**

It is the diagonal containing elements whose row and column indexes are equal in a square matrix.

**Q28. What condition identifies a main diagonal element?**

`row == column`.

**Q29. How do you calculate the sum of matrix elements?**

Initialize a total and add each element while traversing the matrix.

**Q30. What is row-wise sum?**

The sum of all elements belonging to an individual row.

### Programming and DSA Questions

**Q31. What is column-wise sum?**

The sum of all elements belonging to an individual column.

**Q32. What is matrix traversal?**

Visiting every element in a matrix.

**Q33. What is the time complexity of traversing an R-by-C matrix?**

O(R × C).

**Q34. What is the time complexity of two nested loops that both execute N times?**

O(N²).

**Q35. What is the time complexity of three nested loops of size N?**

O(N³).

**Q36. What is the time complexity of a triangular nested loop?**

O(N²), because its total iterations grow proportionally to N(N + 1)/2.

**Q37. What is the purpose of a counter in nested loops?**

A counter tracks the number of occurrences or operations.

**Q38. What is the purpose of an accumulator?**

An accumulator stores a running result such as a sum.

**Q39. What is Bubble Sort?**

Bubble Sort is a comparison-based sorting algorithm that repeatedly compares adjacent elements and swaps them when necessary.

**Q40. Which loop structure is commonly used in basic Bubble Sort?**

Nested loops.

### Complexity and Advanced Questions

**Q41. Does every nested loop have O(N²) complexity?**

No. Complexity depends on the actual iteration counts and loop boundaries.

**Q42. What is the complexity of R rows and C columns?**

O(R × C).

**Q43. Why should unnecessary nested loops be avoided?**

They can increase execution time significantly as input size grows.

**Q44. What is matrix addition?**

It is the element-by-element addition of two matrices having compatible dimensions.

**Q45. What is matrix multiplication?**

It is a matrix operation that combines rows of the first matrix with columns of the second matrix.

**Q46. How many nested loops are commonly used in standard matrix multiplication?**

Three nested loops are commonly used in a basic implementation.

**Q47. What is a pair-comparison problem?**

A problem that compares one element with another element or with multiple other elements.

**Q48. What is brute-force pair generation?**

It is the process of generating and checking possible element pairs directly.

**Q49. What is auxiliary space?**

Auxiliary space is the additional memory used by an algorithm, excluding the input storage.

**Q50. Which topics should be understood before solving advanced nested-loop DSA problems?**

Loop execution, arrays, two-dimensional lists, indexing, matrix traversal, pair comparisons, and complexity analysis.

---

## 36. Important Terminology

| Term | Meaning |
|---|---|
| Nested Loop | A loop inside another loop |
| Outer Loop | The loop containing another loop |
| Inner Loop | The loop placed inside an outer loop |
| Iteration | One execution of a loop body |
| Row | Horizontal collection of elements |
| Column | Vertical collection of elements |
| Matrix | Rectangular arrangement of values |
| Two-Dimensional List | A list containing other lists |
| Matrix Traversal | Visiting matrix elements |
| Matrix Element | An individual value in a matrix |
| Main Diagonal | Diagonal where row and column indexes are equal |
| Secondary Diagonal | Opposite diagonal in a square matrix |
| Row-Wise Sum | Sum of values in an individual row |
| Column-Wise Sum | Sum of values in an individual column |
| Coordinate Pair | Pair of values representing a position |
| Pattern Printing | Creating repeated visual arrangements |
| Multiplication Grid | Two-dimensional arrangement of products |
| Counter | Variable used for counting |
| Accumulator | Variable used to collect a running result |
| Brute Force | Directly checking possible candidates |
| Pair Comparison | Comparing pairs of elements |
| Time Complexity | Growth of algorithm execution time |
| Space Complexity | Growth of memory requirements |
| Big O | Asymptotic growth notation |

---

## 37. Quick Revision Notes

### Nested Loop Syntax

```python
for outer in iterable:
    for inner in iterable:
        statement
```

### Basic Square Pattern

```python
for row in range(3):
    for column in range(3):
        print("*", end=" ")

    print()
```

### Rectangular Pattern

```python
for row in range(3):
    for column in range(5):
        print("*", end=" ")

    print()
```

### Right-Angled Triangle

```python
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")

    print()
```

### Inverted Triangle

```python
for row in range(5, 0, -1):
    for column in range(row):
        print("*", end=" ")

    print()
```

### Number Triangle

```python
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")

    print()
```

### Coordinate Pairs

```python
for x in range(1, 4):
    for y in range(1, 3):
        print(x, y)
```

### Matrix Traversal

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column])
```

### Matrix Sum

```python
total = 0

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        total += matrix[row][column]

print(total)
```

### Row-Wise Sum

```python
for row in range(len(matrix)):
    total = 0

    for column in range(len(matrix[row])):
        total += matrix[row][column]

    print(total)
```

### Main Diagonal

```python
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if row == column:
            print(matrix[row][column])
```

### Important Rules

- The outer loop controls the main repetition.
- The inner loop executes completely for every outer iteration.
- Indentation defines loop nesting.
- Rows are commonly handled by the outer loop.
- Columns are commonly handled by the inner loop.
- A matrix can be represented as a two-dimensional list.
- The first matrix index selects the row.
- The second matrix index selects the column.
- Matrix traversal processes every element.
- Row-wise and column-wise calculations require different iteration orders.
- Nested-loop complexity depends on actual iteration counts.

### Complexity Reference

| Structure | Complexity |
|---|---|
| Two fixed-size loops | O(1) |
| Two N-sized nested loops | O(N²) |
| Three N-sized nested loops | O(N³) |
| R-by-C matrix traversal | O(R × C) |
| Triangular nested loops | O(N²) |
| Matrix storage | O(R × C) space |

---

## 38. Learning Checklist

### Nested Loop Fundamentals

- [ ] I understand what a nested loop is.
- [ ] I understand the outer loop.
- [ ] I understand the inner loop.
- [ ] I understand how nested loops execute.
- [ ] I can calculate the number of inner-loop executions.
- [ ] I understand loop indentation.
- [ ] I can use nested `for` loops.
- [ ] I can use nested `while` loops.

### Pattern Printing

- [ ] I can print a square star pattern.
- [ ] I can print a rectangular star pattern.
- [ ] I can print a right-angled triangle.
- [ ] I can print an inverted triangle.
- [ ] I can print a number triangle.
- [ ] I can generate a multiplication grid.
- [ ] I can generate coordinate pairs.

### Matrix Fundamentals

- [ ] I understand a two-dimensional list.
- [ ] I can access matrix elements.
- [ ] I can accept matrix input.
- [ ] I can display a matrix.
- [ ] I can traverse a matrix.
- [ ] I can calculate the matrix sum.
- [ ] I can calculate row-wise sums.
- [ ] I can calculate column-wise sums.
- [ ] I can calculate the main diagonal sum.
- [ ] I can count occurrences of a matrix element.

### Problem Solving

- [ ] I can distinguish rows from columns.
- [ ] I can control inner-loop boundaries.
- [ ] I can reset accumulators correctly.
- [ ] I can avoid invalid matrix indexes.
- [ ] I can generate pairs of elements.
- [ ] I can identify duplicate values using pair comparisons.

### DSA Preparation

- [ ] I understand matrix traversal.
- [ ] I understand pair comparisons.
- [ ] I understand nested-loop time complexity.
- [ ] I can identify O(N²).
- [ ] I can identify O(N³).
- [ ] I understand O(R × C).
- [ ] I understand matrix space complexity.

---

## 39. How to Run the Python File

### Step 1: Open Your Repository

Open your `DSA-Python` repository in VS Code.

### Step 2: Navigate to the Topic Folder

```text
PYTHON/
└── Python-Fundamentals/
    └── 01-Loops/
        └── 05-Nested-Loops/
            ├── README.md
            └── 05_nested_loops.py
```

### Step 3: Open the Terminal

Open the integrated terminal in VS Code.

### Step 4: Run the Python File

Execute this command from the repository root:

```powershell
python PYTHON/Python-Fundamentals/01-Loops/05-Nested-Loops/05_nested_loops.py
```

### Step 5: Select a Menu Option

The program displays:

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Enter the option you want to execute.

---

## 40. Repository Structure

```text
DSA-Python/
│
└── PYTHON/
    │
    └── Python-Fundamentals/
        │
        └── 01-Loops/
            │
            ├── README.md
            │
            ├── 01-Introduction-to-Loops/
            │   ├── README.md
            │   └── 01_introduction_to_loops.py
            │
            ├── 02-For-Loop/
            │   ├── README.md
            │   └── 02_for_loop.py
            │
            ├── 03-Range-Function/
            │   ├── README.md
            │   └── 03_range_function.py
            │
            ├── 04-While-Loop/
            │   ├── README.md
            │   └── 04_while_loop.py
            │
            └── 05-Nested-Loops/
                ├── README.md
                └── 05_nested_loops.py
```

### File Responsibilities

**README.md**

Contains:

- Introduction.
- Learning objectives.
- Nested loop definition.
- Outer and inner loops.
- Execution flow.
- Nested `for` loops.
- Nested `while` loops.
- Rows and columns.
- Star patterns.
- Number patterns.
- Multiplication grids.
- Coordinate pairs.
- Two-dimensional lists.
- Matrix traversal.
- Matrix input.
- Matrix calculations.
- Twelve topic examples.
- Twelve solved problems.
- Ten unsolved practice questions.
- Common mistakes.
- Best practices.
- Debugging.
- Real-life applications.
- DSA connections.
- Complexity analysis.
- Mini project.
- Fifty viva questions and answers.
- Important terminology.
- Quick revision notes.
- Learning checklist.
- Execution instructions.

**05_nested_loops.py**

Contains:

- Twelve executable topic examples.
- Twelve selectable solved problems.
- Ten unsolved practice questions.
- Learning checklist.
- Interactive menu.
- Matrix input helper.
- Matrix display helper.
- Input validation.

---

## 41. Final Summary

Nested loops are an important programming concept used when a task requires more than one level of repetition.

A nested loop contains an inner loop inside an outer loop.

The outer loop controls the main repetition, while the inner loop executes for every outer-loop iteration.

Nested loops are useful for:

- Pattern printing.
- Row and column processing.
- Matrix traversal.
- Coordinate generation.
- Pair comparisons.
- Multiplication grids.
- Basic sorting algorithms.

Two-dimensional lists are commonly processed using nested loops.

Understanding rows, columns, matrix indexes, and iteration counts is important for solving matrix-based problems.

Nested loops also introduce important DSA complexity concepts.

Two independent loops of size N generally produce O(N²) work, while three such loops generally produce O(N³) work.

However, always analyze the actual loop boundaries instead of assuming that every nested loop has the same complexity.

### What You Should Do Next

1. Understand the difference between outer and inner loops.
2. Learn how nested loops execute.
3. Practise star and number patterns.
4. Understand rows and columns.
5. Run `05_nested_loops.py`.
6. Execute all twelve examples.
7. Attempt all twelve solved problems.
8. Solve the ten unsolved questions.
9. Complete the learning checklist.
10. Revise the fifty viva questions.
11. Practise matrix traversal and matrix calculations.
12. Understand nested-loop time complexity.

**Topic Completed: Nested Loops in Python**

The next topic in this repository is:

`06-Break-Statement`

Its Python source file will be:

`06_break_statement.py`