# Python List Indexing and Slicing – Complete Learning Guide

**Section:** Python Fundamentals – Part 2  
**Topic:** 02 – List Indexing and Slicing  
**Folder:** `02-List-Indexing-and-Slicing`  
**Programming Language:** Python 3  
**Difficulty:** Beginner to Intermediate  
**Focus:** List Access, Indexing, Slicing and DSA Preparation

---

# 1. Introduction to List Indexing and Slicing

Lists are one of the most important data structures in Python. After learning how to create and modify lists, the next step is understanding how to access individual elements and extract specific portions of a list.

Python provides two important techniques for working with lists:

**1. Indexing**

Indexing allows us to access an individual element using its position in the list.

**2. Slicing**

Slicing allows us to extract multiple elements from a list by specifying a range of indexes.

These techniques are useful when we need to retrieve specific values, reverse a list, create copies, process selected portions of data or implement algorithms.

### Why Are Indexing and Slicing Important?

They help us:

- Access elements efficiently.
- Retrieve values from the beginning or end.
- Extract a specific range of elements.
- Select elements at regular intervals.
- Reverse a list.
- Create a shallow copy of a list.
- Process nested lists.
- Split collections into smaller portions.
- Implement list-based programming problems.
- Develop techniques used in DSA.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

### Indexing

- Understand zero-based indexing.
- Access elements using positive indexes.
- Access elements using negative indexes.
- Identify the first and last elements.
- Understand how indexes map to list positions.
- Handle invalid indexes.

### Slicing

- Understand the basic slicing syntax.
- Use start and stop indexes.
- Understand why the stop index is excluded.
- Use omitted start and stop values.
- Use positive step values.
- Use negative step values.
- Reverse a list using slicing.
- Extract selected list portions.
- Handle out-of-range slice boundaries.

### Advanced Applications

- Create a shallow list copy using slicing.
- Access elements inside nested lists.
- Modify lists using slice assignment.
- Rotate a list using slicing.
- Check list palindromes.
- Split a list into multiple portions.
- Understand slicing time and space complexity.

---

# 3. Understanding List Indexing

Indexing is the process of accessing an individual list element using its position.

Python uses zero-based indexing, which means indexing starts from zero.

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
```

### Output

```text
10
20
30
40
50
```

### Positive Indexing Table

| Element | Positive Index |
|---|---:|
| 10 | 0 |
| 20 | 1 |
| 30 | 2 |
| 40 | 3 |
| 50 | 4 |

### Important Points

- The first element has index `0`.
- The second element has index `1`.
- The index of the last element is `len(list) - 1`.
- Indexing beyond the valid range raises `IndexError`.

## Positive Indexing Syntax

```python
list_name[index]
```

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[2])
```

Output:

```text
Apple
Mango
```

---

# 4. Negative Indexing

Python also supports negative indexing.

Negative indexing allows us to access elements by counting positions from the end of the list.

The last element has index `-1`, the second-last has index `-2`, and so on.

### Example

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
```

### Output

```text
Grapes
Orange
Mango
```

### Negative Indexing Table

| Element | Positive Index | Negative Index |
|---|---:|---:|
| Apple | 0 | -5 |
| Banana | 1 | -4 |
| Mango | 2 | -3 |
| Orange | 3 | -2 |
| Grapes | 4 | -1 |

### Positive vs Negative Indexing

| Positive Indexing | Negative Indexing |
|---|---|
| Starts from the beginning | Starts from the end |
| First index is `0` | Last index is `-1` |
| Increases from left to right | Decreases from right to left |
| Useful for accessing elements by position | Useful for accessing elements from the end |

### Important Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])    # First element
print(numbers[-1])   # Last element
print(numbers[-2])   # Second-last element
```

Output:

```text
10
50
40
```

---

# 5. Understanding List Slicing

Slicing is used to extract a portion of a list.

Instead of accessing only one element, slicing allows us to retrieve multiple elements using a range.

### Basic Syntax

```python
list_name[start:stop:step]
```

There are three parameters:

| Parameter | Meaning |
|---|---|
| `start` | Starting index of the slice |
| `stop` | Ending boundary, which is excluded |
| `step` | Number of positions to move between selected elements |

### Example

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

result = numbers[1:5]

print(result)
```

### Output

```text
[20, 30, 40, 50]
```

### Explanation

The expression is:

```python
numbers[1:5]
```

- Start index is `1`.
- Stop index is `5`.
- Index `5` is excluded.
- Elements from index `1` through index `4` are selected.

### Visual Representation

```text
List:          [10, 20, 30, 40, 50, 60, 70]
Index:           0   1   2   3   4   5   6

Selected:            [20, 30, 40, 50]
                       ^           ^
                    Start         Stop
                                  excluded
```

**Remember:** The start index is included, but the stop index is excluded.

---

# 6. Slicing With an Omitted Start Index

When the start index is omitted, Python starts slicing from the beginning of the list for a positive step.

### Syntax

```python
list_name[:stop]
```

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
```

### Output

```text
[10, 20, 30]
```

### Explanation

- Start is omitted.
- Python starts from index `0`.
- Stop is `3`, which is excluded.

Another example:

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[:2])
```

Output:

```text
['Apple', 'Banana']
```

---

# 7. Slicing With an Omitted Stop Index

When the stop index is omitted, Python continues slicing until the end of the list for a positive step.

### Syntax

```python
list_name[start:]
```

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
```

### Output

```text
[30, 40, 50]
```

### Explanation

- Start index is `2`.
- Stop is omitted.
- Python selects elements until the end.

Another example:

```python
languages = ["Python", "Java", "C++", "JavaScript"]

print(languages[1:])
```

Output:

```text
['Java', 'C++', 'JavaScript']
```

---

# 8. Slicing With a Step Value

The step parameter determines how many positions Python moves between selected elements.

### Syntax

```python
list_name[start:stop:step]
```

### Example 1: Select Every Second Element

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::2])
```

Output:

```text
[10, 30, 50, 70]
```

### Explanation

The slice is:

```python
numbers[::2]
```

- Start is omitted.
- Stop is omitted.
- Step is `2`.
- Python selects every second element.

### Example 2: Start From Index 1

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1::2])
```

Output:

```text
[20, 40, 60]
```

### Example 3: Use Step 3

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::3])
```

Output:

```text
[10, 40, 70]
```

### Important Points

- A positive step moves from left to right.
- A negative step moves from right to left.
- Step `1` selects consecutive elements.
- Step `2` selects every second eligible element.
- Step `3` selects every third eligible element.
- Step `0` is invalid and raises `ValueError`.

---

# 9. Slicing With a Negative Step

A negative step makes Python move through a list from right to left.

### Syntax

```python
list_name[start:stop:-step]
```

The start and stop boundaries must be appropriate for reverse traversal.

### Example 1

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::-1])
```

Output:

```text
[60, 50, 40, 30, 20, 10]
```

### Example 2: Reverse With Step 2

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::-2])
```

Output:

```text
[60, 40, 20]
```

### Example 3: Reverse a Selected Range

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[5:1:-1])
```

Output:

```text
[60, 50, 40, 30]
```

### Explanation

- Start index is `5`.
- Stop index is `1`.
- Step is `-1`.
- Python moves backward.
- Index `1` is excluded.

### Understanding Reverse Slicing

| Slice | Result |
|---|---|
| `numbers[::-1]` | Entire list in reverse |
| `numbers[::-2]` | Every second element from the end |
| `numbers[5:1:-1]` | Reverse selection from index 5 up to, but excluding, index 1 |
| `numbers[4:0:-2]` | Reverse selection at intervals of two |

---

# 10. Reversing a List Using Slicing

One of the common applications of slicing is reversing an entire list.

### Syntax

```python
reversed_list = original_list[::-1]
```

### Example

```python
numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("Original list:", numbers)
print("Reversed list:", reversed_list)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Reversed list: [50, 40, 30, 20, 10]
```

**Important:** Reverse slicing creates a new list. It does not modify the original list.

### Comparison With `reverse()`

```python
numbers = [10, 20, 30, 40]

reversed_list = numbers[::-1]

print(reversed_list)
print(numbers)
```

Output:

```text
[40, 30, 20, 10]
[10, 20, 30, 40]
```

Using `reverse()`:

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

`reverse()` modifies the original list in place, while `[::-1]` creates a new shallow list.

---

# 11. Copying a List Using Slicing

Slicing can be used to create a shallow copy of a list.

### Syntax

```python
copied_list = original_list[:]
```

### Example

```python
original = [10, 20, 30, 40]

copied_list = original[:]

copied_list.append(50)

print("Original:", original)
print("Copied:", copied_list)
```

### Output

```text
Original: [10, 20, 30, 40]
Copied: [10, 20, 30, 40, 50]
```

### Why Does the Original List Remain Unchanged?

The slice creates a new outer list. Changing the new list by appending an element does not add that element to the original list.

### Important Note: Shallow Copy

A shallow copy does not recursively copy nested mutable objects.

Example:

```python
original = [[10, 20], [30, 40]]

copied = original[:]

copied[0].append(50)

print("Original:", original)
print("Copied:", copied)
```

Output:

```text
Original: [[10, 20, 50], [30, 40]]
Copied: [[10, 20, 50], [30, 40]]
```

The outer lists are different, but their inner lists are shared.

For a deep independent copy of nested mutable objects:

```python
import copy

original = [[10, 20], [30, 40]]

copied = copy.deepcopy(original)
```

---

# 12. Nested List Indexing

A nested list is a list that contains other lists as elements.

Indexing can be applied multiple times to access values inside nested lists.

### Example

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix[0])
print(matrix[1])
print(matrix[2])
```

### Output

```text
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
```

### Access an Individual Element

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix[1][2])
```

Output:

```text
60
```

### Explanation

- `matrix[1]` accesses the second row.
- `matrix[1][2]` accesses the third element of that row.

### Slice a Nested List

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix[-1][:2])
```

Output:

```text
[70, 80]
```

This technique is useful when working with matrices, tables and two-dimensional data.

---

# 13. Slicing With Out-of-Range Indexes

One important difference between indexing and slicing is how they handle out-of-range boundaries.

### Indexing With an Invalid Position

```python
numbers = [10, 20, 30]

print(numbers[10])
```

This raises:

```text
IndexError: list index out of range
```

### Slicing With Out-of-Range Boundaries

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:10])
print(numbers[10:20])
print(numbers[-10:3])
print(numbers[3:100])
```

Output:

```text
[10, 20, 30, 40, 50]
[]
[10, 20, 30]
[40, 50]
```

### Important Difference

| Indexing | Slicing |
|---|---|
| Accesses an individual element | Extracts a sequence of elements |
| Invalid index generally raises `IndexError` | Out-of-range boundaries are safely adjusted |
| Example: `numbers[2]` | Example: `numbers[1:4]` |
| Returns one element | Returns a new list |

**Remember:** Slicing with a step of zero is still invalid, even though out-of-range boundaries are handled safely.

---

# 14. Slice Assignment

Python also allows us to modify a list using slice assignment.

Slice assignment replaces the selected portion of the original list with elements from another iterable.

### Syntax

```python
list_name[start:stop] = iterable
```

### Example

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:3] = [200, 300, 400]

print(numbers)
```

### Output

```text
[10, 200, 300, 400, 40, 50]
```

### Explanation

The original selected range contains:

```text
[20, 30]
```

It is replaced by:

```text
[200, 300, 400]
```

As a result, the list length increases by one.

### Delete a Range Using Slice Assignment

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:3] = []

print(numbers)
```

Output:

```text
[10, 40, 50]
```

### Important Difference

- Regular slicing produces a new list.
- Slice assignment modifies the original list.

---

# 15. Twelve Important Topic Examples

The following examples match the twelve examples in `02_list_indexing_and_slicing.py`.

## Example 1 – Positive Indexing

**Concept:** Access list elements using positive indexes.

```python
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Last element:", numbers[4])
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
First element: 10
Second element: 20
Third element: 30
Last element: 50
```

**Explanation:** Positive indexing begins at zero and increases toward the end.

## Example 2 – Negative Indexing

**Concept:** Access list elements using negative indexes.

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Original list:", fruits)
print("Last element:", fruits[-1])
print("Second-last element:", fruits[-2])
print("Third-last element:", fruits[-3])
print("First element:", fruits[-5])
```

### Output

```text
Original list: ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']
Last element: Grapes
Second-last element: Orange
Third-last element: Mango
First element: Apple
```

## Example 3 – Basic List Slicing

**Concept:** Extract elements between two indexes.

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

result = numbers[1:5]

print("Original list:", numbers)
print("numbers[1:5]:", result)
```

### Output

```text
Original list: [10, 20, 30, 40, 50, 60, 70]
numbers[1:5]: [20, 30, 40, 50]
```

## Example 4 – Slicing With Omitted Start

**Concept:** Extract elements from the beginning.

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[:3]

print("Original list:", numbers)
print("numbers[:3]:", result)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
numbers[:3]: [10, 20, 30]
```

## Example 5 – Slicing With Omitted Stop

**Concept:** Extract elements from a selected index until the end.

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[2:]

print("Original list:", numbers)
print("numbers[2:]:", result)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
numbers[2:]: [30, 40, 50]
```

## Example 6 – Slicing With Step

**Concept:** Select elements at regular intervals.

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Original list:", numbers)
print("numbers[::2]:", numbers[::2])
print("numbers[1::2]:", numbers[1::2])
```

### Output

```text
Original list: [10, 20, 30, 40, 50, 60, 70, 80]
numbers[::2]: [10, 30, 50, 70]
numbers[1::2]: [20, 40, 60, 80]
```

## Example 7 – Slicing With Negative Step

**Concept:** Select elements while moving from right to left.

```python
numbers = [10, 20, 30, 40, 50, 60]

print("Original list:", numbers)
print("numbers[::-2]:", numbers[::-2])
print("numbers[5:1:-1]:", numbers[5:1:-1])
```

### Output

```text
Original list: [10, 20, 30, 40, 50, 60]
numbers[::-2]: [60, 40, 20]
numbers[5:1:-1]: [60, 50, 40, 30]
```

## Example 8 – Reverse a List Using Slicing

**Concept:** Reverse a complete list using a negative step.

```python
numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("Original list:", numbers)
print("Reversed list:", reversed_list)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Reversed list: [50, 40, 30, 20, 10]
```

## Example 9 – Copy a List Using Slicing

**Concept:** Create a shallow copy using `[:]`.

```python
original = [10, 20, 30, 40, 50]

copied_list = original[:]

print("Original list:", original)
print("Copied list:", copied_list)

copied_list[0] = 100

print("\nAfter modifying the copied list:")
print("Original list:", original)
print("Copied list:", copied_list)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Copied list: [10, 20, 30, 40, 50]

After modifying the copied list:
Original list: [10, 20, 30, 40, 50]
Copied list: [100, 20, 30, 40, 50]
```

## Example 10 – Nested List Indexing

**Concept:** Access elements and ranges inside nested lists.

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in matrix:
    print(row)

print("First row:", matrix[0])
print("Second row:", matrix[1])
print("Element at row 1, column 2:", matrix[1][2])
print("First two elements of the last row:", matrix[-1][:2])
```

### Output

```text
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
First row: [10, 20, 30]
Second row: [40, 50, 60]
Element at row 1, column 2: 60
First two elements of the last row: [70, 80]
```

## Example 11 – Out-of-Range Slicing

**Concept:** Slicing handles out-of-range boundaries without raising an index error.

```python
numbers = [10, 20, 30, 40, 50]

print("numbers[0:10]:", numbers[0:10])
print("numbers[10:20]:", numbers[10:20])
print("numbers[-10:3]:", numbers[-10:3])
print("numbers[3:100]:", numbers[3:100])
```

### Output

```text
numbers[0:10]: [10, 20, 30, 40, 50]
numbers[10:20]: []
numbers[-10:3]: [10, 20, 30]
numbers[3:100]: [40, 50]
```

## Example 12 – Slice Assignment

**Concept:** Replace a range of elements using slice assignment.

```python
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

numbers[1:3] = [200, 300, 400]

print("After slice assignment:", numbers)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
After slice assignment: [10, 200, 300, 400, 40, 50]
```

**Explanation:** The two selected elements are replaced with three new elements, increasing the list length.

---

# 16. Twelve Solved Programming Problems

These problems match the twelve solved problem functions in `02_list_indexing_and_slicing.py`.

## Problem 1 – Access Using Positive Index

**Question:** Accept a list of integers and access an element using its positive index.

### Logic

1. Create a numeric list.
2. Display the available indexes.
3. Ask the user for a valid positive index.
4. Access the element at that position.

### Code

```python
numbers = [10, 20, 30, 40, 50]

index = int(input("Enter positive index: "))

if 0 <= index < len(numbers):
    print("Element:", numbers[index])
else:
    print("Invalid index.")
```

### Sample Input

```text
Enter positive index: 2
```

### Output

```text
Element: 30
```

**Complexity:** O(1) time and O(1) auxiliary space for accessing the selected element.

## Problem 2 – Access Using Negative Index

**Question:** Access an element using a negative index.

### Code

```python
numbers = [10, 20, 30, 40, 50]

index = int(input("Enter negative index: "))

if -len(numbers) <= index <= -1:
    print("Element:", numbers[index])
else:
    print("Invalid negative index.")
```

### Sample Input

```text
Enter negative index: -2
```

### Output

```text
Element: 40
```

**Complexity:** O(1) time and O(1) auxiliary space.

## Problem 3 – Extract First N Elements

**Question:** Extract the first N elements from a list.

### Logic

Use `numbers[:count]` to select the first N elements.

### Code

```python
numbers = [10, 20, 30, 40, 50, 60]

count = int(input("How many initial elements do you want? "))

if 0 <= count <= len(numbers):
    result = numbers[:count]
    print("First elements:", result)
else:
    print("Invalid count.")
```

### Sample Input

```text
How many initial elements do you want? 3
```

### Output

```text
First elements: [10, 20, 30]
```

**Complexity:** O(k) time and O(k) output space, where k is the number of selected elements.

## Problem 4 – Extract Last N Elements

**Question:** Extract the last N elements using negative indexing and slicing.

### Code

```python
numbers = [10, 20, 30, 40, 50, 60]

count = int(input("How many ending elements do you want? "))

if 0 <= count <= len(numbers):
    result = numbers[-count:] if count > 0 else []
    print("Last elements:", result)
else:
    print("Invalid count.")
```

### Sample Input

```text
How many ending elements do you want? 3
```

### Output

```text
Last elements: [40, 50, 60]
```

**Complexity:** O(k) time and O(k) output space.

**Important:** When count is zero, the program explicitly returns an empty list. This avoids the special behavior of `numbers[-0:]`, which would return the entire list.

## Problem 5 – Extract a Range

**Question:** Extract elements between user-provided start and stop indexes.

### Code

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

start = int(input("Enter start index: "))
stop = int(input("Enter stop index: "))

result = numbers[start:stop]

print("Original list:", numbers)
print("Selected slice:", result)
```

### Sample Input

```text
Enter start index: 1
Enter stop index: 5
```

### Output

```text
Original list: [10, 20, 30, 40, 50, 60, 70]
Selected slice: [20, 30, 40, 50]
```

**Complexity:** O(k) time and O(k) output space, where k is the number of selected elements.

## Problem 6 – Extract Elements Using Step

**Question:** Select elements at regular intervals using the step parameter.

### Code

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

start = int(input("Enter starting index: "))
step = int(input("Enter a positive step value: "))

if 0 <= start <= len(numbers) and step > 0:
    result = numbers[start::step]
    print("Selected elements:", result)
else:
    print("Invalid starting index or step.")
```

### Sample Input

```text
Enter starting index: 0
Enter a positive step value: 2
```

### Output

```text
Selected elements: [10, 30, 50, 70]
```

**Complexity:** O(k) time and O(k) output space, where k is the number of selected elements.

## Problem 7 – Reverse a List

**Question:** Reverse a list using slicing without changing the original list.

### Code

```python
numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("Original list:", numbers)
print("Reversed list:", reversed_list)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Reversed list: [50, 40, 30, 20, 10]
```

**Complexity:** O(n) time and O(n) output space.

## Problem 8 – Copy a List Using Slicing

**Question:** Create a shallow copy of a list and modify the copy independently.

### Code

```python
original = [10, 20, 30, 40, 50]

copied_list = original[:]

copied_list.append(60)

print("Original list:", original)
print("Copied list:", copied_list)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Copied list: [10, 20, 30, 40, 50, 60]
```

**Complexity:** O(n) time and O(n) additional space.

## Problem 9 – Remove First and Last Elements

**Question:** Extract only the middle elements of a list using slicing.

### Code

```python
numbers = [10, 20, 30, 40, 50, 60]

if len(numbers) < 2:
    result = []
else:
    result = numbers[1:-1]

print("Original list:", numbers)
print("Middle elements:", result)
```

### Output

```text
Original list: [10, 20, 30, 40, 50, 60]
Middle elements: [20, 30, 40, 50]
```

**Complexity:** O(n) time and O(n) output space in the general case.

## Problem 10 – Rotate a List to the Right

**Question:** Rotate the elements of a list to the right by a user-provided number of positions.

### Logic

For a list of length n, normalize the rotation count using:

```python
shift = positions % len(numbers)
```

Then combine two slices:

```python
numbers[-shift:] + numbers[:-shift]
```

### Code

```python
numbers = [10, 20, 30, 40, 50]

positions = int(input("Enter rotation positions: "))

shift = positions % len(numbers)

if shift == 0:
    rotated_list = numbers.copy()
else:
    rotated_list = numbers[-shift:] + numbers[:-shift]

print("Original list:", numbers)
print("Rotated list:", rotated_list)
```

### Sample Input

```text
Enter rotation positions: 2
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Rotated list: [40, 50, 10, 20, 30]
```

**Complexity:** O(n) time and O(n) output space.

## Problem 11 – Check a List Palindrome

**Question:** Check whether a list reads the same forward and backward.

### Code

```python
numbers = [10, 20, 30, 20, 10]

reversed_list = numbers[::-1]

print("Original list:", numbers)
print("Reversed list:", reversed_list)

if numbers == reversed_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
```

### Output

```text
Original list: [10, 20, 30, 20, 10]
Reversed list: [10, 20, 30, 20, 10]
The list is a palindrome.
```

**Complexity:** O(n) time and O(n) additional space due to reverse slicing.

## Problem 12 – Split a List Into Two Halves

**Question:** Divide a list into two portions using slicing.

### Code

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

middle = len(numbers) // 2

first_half = numbers[:middle]
second_half = numbers[middle:]

print("Original list:", numbers)
print("First half:", first_half)
print("Second half:", second_half)
```

### Output

```text
Original list: [10, 20, 30, 40, 50, 60, 70]
First half: [10, 20, 30]
Second half: [40, 50, 60, 70]
```

**Complexity:** O(n) time and O(n) total output space.

**Note:** When the number of elements is odd, the second half receives the extra element.

---

# 17. Ten Unsolved Practice Questions

Try these questions independently before looking for solutions.

| No. | Practice Question | Difficulty |
|---|---|---|
| 1 | Write a program to access the third-last element using negative indexing. | Easy |
| 2 | Extract elements between two user-provided slice indexes. | Easy |
| 3 | Use slicing to select elements at indexes 0, 2, 4 and so on. | Easy |
| 4 | Use a negative step to traverse a list in reverse, selecting every second element. | Medium |
| 5 | Use slicing to display the first three and last three elements of a list. | Easy |
| 6 | Create a reversed copy without modifying the original list. | Easy |
| 7 | Return all elements except the first and last elements using slicing. | Easy |
| 8 | Rotate a list to the left by a user-provided number of positions using slicing. | Medium |
| 9 | Determine whether a list is a palindrome using reverse slicing. | Medium |
| 10 | Divide a list into three approximately equal parts using slicing. | Medium |

### Practice Guidelines

For every problem:

1. Understand the expected result.
2. Identify the start, stop and step values.
3. Remember that the stop index is excluded.
4. Test positive and negative indexes.
5. Handle empty slice results.
6. Check whether the original list changes.
7. Test different list lengths.
8. Analyze time and auxiliary space complexity.

---

# 18. Time and Space Complexity of Indexing and Slicing

Understanding complexity is important because slicing creates new list objects.

Let:

- n = original list length.
- k = number of elements selected by slicing.

| Operation | Time Complexity | Additional Space |
|---|---|---|
| Positive indexing | O(1) | O(1) |
| Negative indexing | O(1) | O(1) |
| Update by index | O(1) | O(1) |
| Slice with k selected elements | O(k) | O(k) |
| Full list copy using `[:]` | O(n) | O(n) |
| Reverse using `[::-1]` | O(n) | O(n) |
| Slice with step | O(k) | O(k) |
| Slice assignment | Depends on replaced and inserted ranges; generally O(n + k) | Depends on resizing |
| Nested list element access | O(1) for a fixed number of index operations | O(1) |
| Compare original and reversed list | O(n) | O(n) for constructing reversed copy |
| Right rotation using slicing | O(n) | O(n) |

### Important Complexity Concepts

**1. Indexing – O(1)**

Python can directly access an element by its index.

**2. Slicing – O(k)**

Python creates a new list containing the selected elements. The work depends on the number of selected elements.

**3. Full Reversal – O(n)**

Reverse slicing creates a new list containing all n elements in reverse order.

**4. Copying – O(n)**

A shallow copy creates a new outer list and copies references to the elements.

**5. Slice Assignment**

Replacing a range may require shifting elements and resizing the list. Its cost depends on the size of the original list, selected range and replacement iterable.

**Important:** A slice creates a new outer list, but it does not automatically create independent copies of nested mutable objects.

---

# 19. Common Mistakes in List Indexing and Slicing

## Mistake 1 – Forgetting Zero-Based Indexing

Incorrect assumption:

```python
numbers = [10, 20, 30, 40]

print(numbers[1])
```

Some beginners expect `10`, but the output is:

```text
20
```

The first element is at index zero.

## Mistake 2 – Using an Invalid Index

```python
numbers = [10, 20, 30]

# numbers[5] raises IndexError.
```

Always check whether the index is in the valid range before accessing it.

## Mistake 3 – Forgetting That the Stop Index Is Excluded

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Index 4 is excluded.

## Mistake 4 – Confusing Start and Stop

The slice:

```python
numbers[1:4]
```

means start at index 1 and stop before index 4.

It does not mean that the slice contains four elements.

## Mistake 5 – Using a Zero Step

Incorrect:

```python
# numbers[::0]
```

This raises:

```text
ValueError: slice step cannot be zero
```

A slicing step cannot be zero.

## Mistake 6 – Incorrect Negative Step Direction

A negative step moves backward.

For example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[4:1:-1])
```

Output:

```text
[50, 40, 30]
```

The stop index `1` is excluded.

## Mistake 7 – Assuming Slicing Modifies the Original List

```python
numbers = [10, 20, 30, 40]

result = numbers[::-1]

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

Reverse slicing creates a new list.

## Mistake 8 – Confusing Shallow Copy With Deep Copy

For nested mutable objects, slicing copies only the outer list. Inner objects remain shared.

Use `copy.deepcopy()` when a deep independent copy is necessary.

## Mistake 9 – Forgetting the Special Case of Zero in Negative Slicing

```python
numbers = [10, 20, 30]

print(numbers[-0:])
```

Output:

```text
[10, 20, 30]
```

Because `-0` equals `0`, this returns the full list.

For extracting the last N elements when N may be zero, explicitly handle zero:

```python
count = 0

result = numbers[-count:] if count > 0 else []
```

---

# 20. Mini Project – List Segment Analyzer

## Project Description

Create a menu-driven program that accepts a list of numbers and provides different operations using indexing and slicing.

### Features

The program should:

1. Display the original list.
2. Display the first and last elements.
3. Extract the first N elements.
4. Extract the last N elements.
5. Display a selected range.
6. Select elements at regular intervals.
7. Reverse the list.
8. Create a shallow copy.
9. Display the middle elements.
10. Rotate the list to the right.

### Concepts Used

- Positive indexing.
- Negative indexing.
- List slicing.
- Start, stop and step.
- Negative step.
- List copying.
- Slice-based rotation.
- Functions.
- Input validation.

### Complete Code

```python
def get_number_list():
    """Read a non-empty list of integers."""

    while True:
        raw = input("Enter integers separated by commas: ").strip()

        try:
            values = [int(item.strip()) for item in raw.split(",")]

            if raw and all(item.strip() for item in raw.split(",")):
                return values

        except ValueError:
            pass

        print("Invalid input. Example: 10, 20, 30, 40")


def display_original_list(numbers):
    """Display the original list with its indexes."""

    print("\nOriginal List:", numbers)

    print("Positive Index:", list(range(len(numbers))))
    print("Negative Index:", list(range(-len(numbers), 0)))


def display_first_and_last(numbers):
    """Display the first and last list elements."""

    print("First Element:", numbers[0])
    print("Last Element:", numbers[-1])


def extract_first_n(numbers):
    """Extract the first N elements."""

    count = int(input("Enter number of elements: "))

    if 0 <= count <= len(numbers):
        print("Result:", numbers[:count])
    else:
        print("Invalid count.")


def extract_last_n(numbers):
    """Extract the last N elements."""

    count = int(input("Enter number of elements: "))

    if 0 <= count <= len(numbers):
        result = numbers[-count:] if count > 0 else []
        print("Result:", result)
    else:
        print("Invalid count.")


def extract_range(numbers):
    """Extract a selected range."""

    start = int(input("Enter start index: "))
    stop = int(input("Enter stop index: "))

    print("Result:", numbers[start:stop])


def select_using_step(numbers):
    """Select elements at a specified positive interval."""

    start = int(input("Enter start index: "))
    step = int(input("Enter positive step: "))

    if 0 <= start <= len(numbers) and step > 0:
        print("Result:", numbers[start::step])
    else:
        print("Invalid start index or step.")


def reverse_list(numbers):
    """Return the reversed list using slicing."""

    print("Reversed List:", numbers[::-1])


def create_copy(numbers):
    """Create a shallow copy of the list."""

    copied = numbers[:]

    print("Original List:", numbers)
    print("Copied List:", copied)


def display_middle_elements(numbers):
    """Display all elements except the first and last."""

    if len(numbers) < 2:
        print("Middle Elements: []")
    else:
        print("Middle Elements:", numbers[1:-1])


def rotate_right(numbers):
    """Rotate the list to the right."""

    positions = int(input("Enter rotation positions: "))
    shift = positions % len(numbers)

    if shift == 0:
        result = numbers.copy()
    else:
        result = numbers[-shift:] + numbers[:-shift]

    print("Rotated List:", result)


def main():
    """Run the interactive List Segment Analyzer."""

    numbers = get_number_list()

    while True:
        print("\n========== LIST SEGMENT ANALYZER ==========")
        print("1. Display Original List and Indexes")
        print("2. Display First and Last Elements")
        print("3. Extract First N Elements")
        print("4. Extract Last N Elements")
        print("5. Extract a Range")
        print("6. Select Elements Using Step")
        print("7. Reverse List")
        print("8. Create List Copy")
        print("9. Display Middle Elements")
        print("10. Rotate List Right")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                display_original_list(numbers)

            elif choice == "2":
                display_first_and_last(numbers)

            elif choice == "3":
                extract_first_n(numbers)

            elif choice == "4":
                extract_last_n(numbers)

            elif choice == "5":
                extract_range(numbers)

            elif choice == "6":
                select_using_step(numbers)

            elif choice == "7":
                reverse_list(numbers)

            elif choice == "8":
                create_copy(numbers)

            elif choice == "9":
                display_middle_elements(numbers)

            elif choice == "10":
                rotate_right(numbers)

            elif choice == "0":
                print("Thank you for using List Segment Analyzer!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid integer input.")

        except IndexError:
            print("The requested position is not available.")


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter integers separated by commas: 10, 20, 30, 40, 50
```

### Sample Output

```text
========== LIST SEGMENT ANALYZER ==========
1. Display Original List and Indexes
2. Display First and Last Elements
3. Extract First N Elements
4. Extract Last N Elements
5. Extract a Range
6. Select Elements Using Step
7. Reverse List
8. Create List Copy
9. Display Middle Elements
10. Rotate List Right
0. Exit

Enter your choice: 7

Reversed List: [50, 40, 30, 20, 10]
```

### Project Extension Ideas

1. Add left rotation.
2. Extract elements using negative indexes.
3. Split the list into three portions.
4. Check whether the list is a palindrome.
5. Allow the user to update a range using slice assignment.
6. Display the length of every extracted portion.
7. Add list statistics.
8. Support decimal values.

---

# 21. Real-World Applications of Indexing and Slicing

Indexing and slicing are useful in many programming applications.

### 1. Data Processing

Extract a particular portion of a dataset for analysis.

### 2. Student Management Systems

Retrieve marks, subject records and student-specific information by index.

### 3. E-Commerce Applications

Access product records, selected cart items and groups of products.

### 4. Log Processing

Extract selected entries from a sequence of log records.

### 5. Text Processing

Select portions of character sequences and process them further.

### 6. Image and Matrix Processing

Access individual rows and nested elements in structured data.

### 7. Data Analysis

Create smaller collections from larger datasets for processing.

### 8. Algorithm Development

Use subranges of lists when implementing sorting, searching and divide-and-conquer algorithms.

---

# 22. Connection With Data Structures and Algorithms

List indexing and slicing are important foundations for DSA.

### DSA Applications

| DSA Concept | Application of Indexing and Slicing |
|---|---|
| Arrays | Access elements by index |
| Binary Search | Calculate and inspect middle positions |
| Merge Sort | Work with smaller portions of data |
| Quick Sort | Process selected partitions |
| Two Pointers | Maintain positions using indexes |
| Sliding Window | Identify ranges of elements |
| Prefix Sum | Access previous and current positions |
| Matrix | Access rows and individual columns |
| Rotation Problems | Rearrange list portions |
| Palindrome Problems | Compare forward and reversed sequences |

### Recommended Learning Path

```text
List Basics
      |
      v
Positive and Negative Indexing
      |
      v
Basic Slicing
      |
      v
Start, Stop and Step
      |
      v
Negative Step and Reversal
      |
      v
List Copying and Slice Assignment
      |
      v
List Methods
      |
      v
List Iteration
      |
      v
List Comprehensions
      |
      v
Searching and Sorting
      |
      v
Two Pointers and Sliding Window
```

---

# 23. Fifty Important Viva Questions and Answers

## Basic Indexing Questions

**Q1. What is indexing in Python?**

Indexing is the process of accessing an individual element using its position in a collection.

**Q2. What is zero-based indexing?**

It is an indexing system where the first element is assigned index zero.

**Q3. What is the index of the first element in a Python list?**

Zero.

**Q4. What is the index of the last element in a list of length n?**

`n - 1`.

**Q5. What is negative indexing?**

Negative indexing accesses list elements by counting positions from the end.

**Q6. What is the negative index of the last element?**

`-1`.

**Q7. What is the negative index of the second-last element?**

`-2`.

**Q8. What happens when an invalid index is accessed?**

Python raises `IndexError`.

**Q9. How can you access the last element of a list?**

Using `list_name[-1]`.

**Q10. Can list elements be modified using indexing?**

Yes. Lists are mutable, so an existing element can be updated using its index.

## Slicing Questions

**Q11. What is list slicing?**

List slicing extracts a portion of a list using specified index boundaries.

**Q12. What is the basic syntax of slicing?**

`list_name[start:stop:step]`.

**Q13. What is the purpose of the start parameter?**

It specifies the starting boundary of the slice.

**Q14. What is the purpose of the stop parameter?**

It specifies the ending boundary, which is excluded from the result.

**Q15. What is the purpose of the step parameter?**

It specifies how many positions Python moves between selected elements.

**Q16. Is the stop index included in slicing?**

No. The stop index is excluded.

**Q17. What happens when the start index is omitted?**

For a positive step, slicing starts from the beginning.

**Q18. What happens when the stop index is omitted?**

For a positive step, slicing continues to the end.

**Q19. What does `numbers[:]` return?**

A shallow copy of the entire list.

**Q20. What does `numbers[1:4]` mean?**

It returns elements from index 1 up to, but excluding, index 4.

## Step and Reversal Questions

**Q21. What does `numbers[::2]` do?**

It selects every second element starting from the beginning.

**Q22. What does a negative step do?**

It makes slicing traverse the sequence from right to left.

**Q23. How can you reverse a list using slicing?**

Using `numbers[::-1]`.

**Q24. Does reverse slicing modify the original list?**

No. It creates a new shallow list.

**Q25. What happens when the slicing step is zero?**

Python raises `ValueError`.

**Q26. What does `numbers[::-2]` do?**

It selects every second element while moving backward from the end.

**Q27. What does `numbers[-3:]` return?**

The last three elements, provided the list contains at least three elements.

**Q28. What does `numbers[:-1]` return?**

Every element except the last one.

**Q29. What does `numbers[1:-1]` return?**

All elements except the first and last elements.

**Q30. What does `numbers[5:1:-1]` mean?**

It selects elements beginning at index 5 and moves backward until, but excluding, index 1.

## Copying and Advanced Questions

**Q31. How can a list be copied using slicing?**

Using `copied_list = original_list[:]`.

**Q32. What is shallow copying?**

Shallow copying creates a new outer object while retaining references to nested objects.

**Q33. Does slicing create a deep copy?**

No. Normal list slicing creates a shallow copy.

**Q34. What is aliasing?**

Aliasing occurs when multiple variables refer to the same object.

**Q35. What is slice assignment?**

Slice assignment replaces a selected range of elements with elements from an iterable.

**Q36. Can slice assignment change the length of a list?**

Yes. The replacement iterable can contain a different number of elements.

**Q37. Can slicing handle out-of-range boundaries?**

Yes. Python safely adjusts out-of-range slice boundaries.

**Q38. Does indexing handle invalid positions in the same way as slicing?**

No. Indexing raises `IndexError` for an invalid position, while ordinary out-of-range slice boundaries are adjusted.

**Q39. Can nested lists be accessed using multiple indexes?**

Yes. For example, `matrix[1][2]` accesses an element in a nested list.

**Q40. Which module can be used to create a deep copy?**

The `copy` module, using `copy.deepcopy()`.

## Complexity and DSA Questions

**Q41. What is the time complexity of list indexing?**

O(1).

**Q42. What is the time complexity of full-list slicing?**

O(n), because a new list of n elements is created.

**Q43. What is the auxiliary space complexity of full-list slicing?**

O(n) additional output storage.

**Q44. What is the time complexity of reversing a list using slicing?**

O(n).

**Q45. What is the time complexity of copying a list using slicing?**

O(n).

**Q46. What is the purpose of list rotation?**

It changes the arrangement of elements by moving elements from one end to another.

**Q47. How can a list be rotated to the right using slicing?**

For a non-empty list, use `numbers[-shift:] + numbers[:-shift]`, after normalizing `shift`.

**Q48. What is a list palindrome?**

A list that reads the same from left to right and right to left.

**Q49. How is slicing useful in Merge Sort?**

It can extract smaller portions of a collection while implementing divide-and-conquer logic, although copying slices has additional time and space costs.

**Q50. Why are indexing and slicing important in DSA?**

They help access elements, process ranges, implement array-based algorithms and solve problems involving searching, sorting, rotation and sequence manipulation.

---

# 24. Important Terminology

| Term | Meaning |
|---|---|
| Indexing | Accessing an element using its position |
| Positive Index | Position counted from the beginning |
| Negative Index | Position counted from the end |
| Slicing | Extracting a sequence of elements |
| Start | Starting boundary of a slice |
| Stop | Excluded ending boundary |
| Step | Interval between selected positions |
| Reverse Slicing | Traversing a sequence backward |
| Slice Assignment | Replacing a selected list range |
| Shallow Copy | New outer collection with shared inner references |
| Deep Copy | Recursive copying of nested objects |
| Aliasing | Multiple references to the same object |
| Nested List | A list containing other lists |
| Rotation | Moving elements around the collection |
| List Palindrome | A list equal to its reversed sequence |

---

# 25. Quick Revision Notes

- Python uses zero-based indexing.
- The first element has index `0`.
- The last element has negative index `-1`.
- Positive indexing starts from the beginning.
- Negative indexing starts from the end.
- Indexing accesses one element.
- Slicing extracts multiple elements.
- Slicing syntax is `[start:stop:step]`.
- The start boundary is included.
- The stop boundary is excluded.
- An omitted start uses the default starting boundary.
- An omitted stop uses the default ending boundary.
- A positive step moves forward.
- A negative step moves backward.
- A zero step raises `ValueError`.
- `[::-1]` reverses a list into a new list.
- `[:]` creates a shallow copy.
- Slicing handles out-of-range boundaries.
- Indexing an invalid position raises `IndexError`.
- Slice assignment modifies the original list.
- Nested lists can be accessed using multiple indexes.
- Full-list slicing takes O(n) time and O(n) output space.

---

# 26. Learning Checklist

Complete this checklist before moving to the next topic.

## Indexing Fundamentals

- [ ] Understand zero-based positive indexing.
- [ ] Understand negative indexing.
- [ ] Access the first element.
- [ ] Access the last element.
- [ ] Access elements using positive indexes.
- [ ] Access elements using negative indexes.
- [ ] Understand invalid index errors.

## Slicing Fundamentals

- [ ] Understand basic slicing syntax.
- [ ] Use start and stop parameters.
- [ ] Remember that the stop index is excluded.
- [ ] Use an omitted start index.
- [ ] Use an omitted stop index.
- [ ] Use positive step values.
- [ ] Understand negative step values.
- [ ] Handle out-of-range slicing.

## Advanced Slicing

- [ ] Reverse a list using slicing.
- [ ] Copy a list using slicing.
- [ ] Understand shallow copying.
- [ ] Understand deep copying.
- [ ] Access nested list elements.
- [ ] Use slice assignment.
- [ ] Extract selected ranges.
- [ ] Rotate a list using slicing.
- [ ] Check list palindromes.
- [ ] Split a list into multiple portions.

## Problem Solving

- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Understand every solution.
- [ ] Analyze time complexity.
- [ ] Analyze auxiliary space complexity.
- [ ] Complete the mini project.
- [ ] Review all 50 viva questions.

---

# 27. Python File Information

**Topic Name:** List Indexing and Slicing

**Topic Number:** 02

**Section:** Python Fundamentals – Lists and Tuples

**Python File:**

```text
02_list_indexing_and_slicing.py
```

**README File:**

```text
README.md
```

### Folder Structure

```text
PYTHON/
└── Python-Fundamentals/
    └── 03-Lists-and-Tuples/
        └── 02-List-Indexing-and-Slicing/
            ├── README.md
            └── 02_list_indexing_and_slicing.py
```

### How to Run the Program

Open the terminal from your repository root and execute:

```bash
python PYTHON/Python-Fundamentals/03-Lists-and-Tuples/02-List-Indexing-and-Slicing/02_list_indexing_and_slicing.py
```

### Main Menu

When the program runs, the following menu appears:

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

Choose an option to explore the topic examples, execute solved programs, review practice questions or revise the concepts.

---

# 28. Conclusion

List indexing and slicing are essential concepts in Python programming.

Indexing helps us access individual elements, whereas slicing allows us to extract, reverse, copy and process selected portions of a list.

Understanding start, stop and step parameters will make it easier to work with collections and solve more complex programming problems.

These concepts are also useful when learning searching, sorting, two pointers, sliding window and divide-and-conquer algorithms.

**Focus on understanding how each slice works. Practice identifying the selected indexes manually before executing the code.**

---

# Next Topic

## Topic 03 – List Methods

In the next topic, you will study Python's built-in list methods in detail.

### Concepts to Explore

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`
- `clear()`
- `index()`
- `count()`
- `sort()`
- `reverse()`
- `copy()`
- `list()` and method behavior
- Practical list-method problems

**Keep Learning. Keep Practicing. Keep Coding!**