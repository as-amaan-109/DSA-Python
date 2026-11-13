# Python List Basics – Complete Learning Guide

**Section:** Python Fundamentals – Part 2  
**Topic:** 01 – List Basics  
**Folder:** `01-List-Basics`  
**Programming Language:** Python 3  
**Difficulty:** Beginner  
**Focus:** Python Lists, Collections and DSA Preparation

---

# 1. Introduction to Lists

A list is one of the most commonly used built-in data structures in Python.

A list is an ordered and mutable collection of elements. It allows us to store multiple values inside a single variable.

Instead of creating separate variables for every value, we can store all the values together in one list.

### Example Without a List

```python
student1 = "Amaan"
student2 = "Rahul"
student3 = "Sara"
student4 = "Arjun"

print(student1)
print(student2)
print(student3)
print(student4)
```

### Example Using a List

```python
students = ["Amaan", "Rahul", "Sara", "Arjun"]

print(students)
```

### Output

```text
['Amaan', 'Rahul', 'Sara', 'Arjun']
```

A list makes it easier to store, access, update and process multiple values.

### Why Are Lists Important?

Lists are useful when:

1. We need to store multiple values together.
2. We want to maintain an ordered collection.
3. We need to update elements.
4. We want to add or remove elements dynamically.
5. We need to search for values.
6. We want to perform operations on collections of data.
7. We need to implement algorithms using arrays and sequences.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

- Understand what a Python list is.
- Understand the characteristics of lists.
- Create lists using square brackets.
- Create empty lists.
- Store different data types in a list.
- Understand ordered collections.
- Understand duplicate elements.
- Access elements using positive indexing.
- Access elements using negative indexing.
- Modify list elements.
- Add elements using `append()`.
- Add multiple elements using `extend()`.
- Insert elements using `insert()`.
- Remove elements using `remove()`.
- Remove elements using `pop()`.
- Find the length of a list using `len()`.
- Check membership using `in` and `not in`.
- Perform basic list calculations.
- Combine lists.
- Copy lists.
- Understand list aliasing and shallow copying.
- Use lists in practical programming and DSA problems.

---

# 3. What Is a Python List?

A list is an ordered, mutable collection that can hold multiple elements.

Lists are created using square brackets `[]`.

### Syntax

```python
list_name = [element1, element2, element3]
```

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

### Output

```text
[10, 20, 30, 40, 50]
```

### Important Characteristics of Lists

A Python list has the following properties:

**1. Ordered**

Elements maintain their sequence. Their positions are represented by indexes.

**2. Mutable**

Elements can be changed after a list is created.

**3. Allows Duplicate Values**

The same value can appear multiple times.

**4. Supports Different Data Types**

A list can contain integers, floats, strings, booleans and other objects.

**5. Dynamically Sized**

Elements can be added or removed after creating a list.

**6. Indexed Collection**

Every element has a position, starting from index zero.

### Example

```python
student = ["Amaan", 22, 85.5, True]

print(student)
```

### Output

```text
['Amaan', 22, 85.5, True]
```

---

# 4. Creating Lists in Python

Python provides different ways to create lists.

## A. Creating a List Using Square Brackets

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
```

## B. Creating an Empty List

```python
numbers = []

print(numbers)
```

Output:

```text
[]
```

## C. Creating a List Using `list()`

```python
numbers = list((10, 20, 30, 40))

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

## D. Creating a List of Integers

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

## E. Creating a List of Strings

```python
languages = ["Python", "Java", "C++", "JavaScript"]

print(languages)
```

## F. Creating a Mixed Data-Type List

```python
student = ["Amaan", 22, 85.5, True]

print(student)
```

## G. Creating a List With Duplicate Elements

```python
numbers = [10, 20, 10, 30, 20]

print(numbers)
```

Output:

```text
[10, 20, 10, 30, 20]
```

**Important:** Python lists allow duplicate values. They do not automatically remove repeated elements.

---

# 5. List Indexing

Indexing is the method of accessing an individual element from a list using its position.

Python uses zero-based indexing.

This means that the first element has index `0`, the second has index `1`, and so on.

### Example

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
```

### Output

```text
Apple
Banana
Mango
Orange
```

### Positive Indexing

| Element | Index |
|---|---:|
| Apple | 0 |
| Banana | 1 |
| Mango | 2 |
| Orange | 3 |

### Negative Indexing

Python also supports negative indexing.

Negative indexing starts from the end of the list.

| Element | Negative Index |
|---|---:|
| Apple | -4 |
| Banana | -3 |
| Mango | -2 |
| Orange | -1 |

### Example

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
```

### Output

```text
Orange
Mango
Banana
Apple
```

### Important Points

- Positive indexing begins at `0`.
- Negative indexing begins at `-1`.
- The last element can be accessed using `list_name[-1]`.
- An invalid index raises `IndexError`.

---

# 6. Updating List Elements

Lists are mutable, which means their elements can be changed after creation.

We can update an element by assigning a new value to an existing index.

### Syntax

```python
list_name[index] = new_value
```

### Example

```python
marks = [70, 80, 65, 90]

print("Before updating:", marks)

marks[2] = 85

print("After updating:", marks)
```

### Output

```text
Before updating: [70, 80, 65, 90]
After updating: [70, 80, 85, 90]
```

### Updating Multiple Elements

```python
numbers = [10, 20, 30, 40, 50]

numbers[0] = 100
numbers[2] = 300
numbers[4] = 500

print(numbers)
```

### Output

```text
[100, 20, 300, 40, 500]
```

**Remember:** Index-based assignment changes an existing position. It does not automatically insert a new element.

---

# 7. Adding Elements to a List

Python provides different methods for adding elements.

## A. `append()` Method

The `append()` method adds one element at the end of a list.

### Syntax

```python
list_name.append(element)
```

### Example

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### Output

```text
[10, 20, 30, 40]
```

### Appending a List

```python
numbers = [10, 20, 30]

numbers.append([40, 50])

print(numbers)
```

Output:

```text
[10, 20, 30, [40, 50]]
```

**Important:** `append()` adds its argument as a single element. It does not merge the contents of another list.

## B. `extend()` Method

The `extend()` method adds all elements from an iterable to the end of the original list.

### Syntax

```python
list_name.extend(iterable)
```

### Example

```python
first_list = [10, 20, 30]
second_list = [40, 50]

first_list.extend(second_list)

print(first_list)
```

### Output

```text
[10, 20, 30, 40, 50]
```

## C. `insert()` Method

The `insert()` method adds an element at a specified position.

### Syntax

```python
list_name.insert(index, element)
```

### Example

```python
fruits = ["Apple", "Mango", "Orange"]

fruits.insert(1, "Banana")

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

### Difference Between `append()`, `extend()` and `insert()`

| Method | Purpose | Example Result |
|---|---|---|
| `append()` | Add one element at the end | `[1, 2, [3, 4]]` |
| `extend()` | Add elements from an iterable | `[1, 2, 3, 4]` |
| `insert()` | Add an element at an index | `[1, 9, 2, 3]` |

---

# 8. Removing Elements From a List

Python provides methods to remove elements.

## A. `remove()` Method

The `remove()` method removes the first occurrence of a specified value.

### Syntax

```python
list_name.remove(value)
```

### Example

```python
numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)
```

### Output

```text
[10, 30, 20, 40]
```

**Important:** If the value does not exist, `remove()` raises `ValueError`.

## B. `pop()` Method

The `pop()` method removes and returns an element.

When no index is provided, it removes the last element.

### Example

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed:", removed)
print("Updated list:", numbers)
```

### Output

```text
Removed: 40
Updated list: [10, 20, 30]
```

### Pop at a Particular Index

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print("Removed:", removed)
print("Updated list:", numbers)
```

### Output

```text
Removed: 20
Updated list: [10, 30, 40]
```

**Important:** `pop()` with an invalid index raises `IndexError`. Calling `pop()` on an empty list also raises `IndexError`.

## C. `del` Statement

The `del` statement removes an element by index or deletes the entire list variable.

```python
numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)
```

Output:

```text
[10, 30, 40]
```

## D. `clear()` Method

The `clear()` method removes all elements from the list.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

### Difference Between Removal Methods

| Method | How It Works |
|---|---|
| `remove(value)` | Removes the first matching value |
| `pop(index)` | Removes and returns an element |
| `del` | Deletes an element or slice using indexes |
| `clear()` | Removes every element |

---

# 9. Basic List Properties and Operations

Python provides useful built-in functions and operators for working with lists.

Assume:

```python
numbers = [10, 20, 30, 40, 50]
```

## A. `len()`

Returns the number of elements in a list.

```python
print(len(numbers))
```

Output:

```text
5
```

## B. `sum()`

Calculates the sum of numeric elements.

```python
print(sum(numbers))
```

Output:

```text
150
```

## C. `min()`

Returns the smallest element.

```python
print(min(numbers))
```

Output:

```text
10
```

## D. `max()`

Returns the largest element.

```python
print(max(numbers))
```

Output:

```text
50
```

## E. Membership Operator `in`

Checks whether an element exists in the list.

```python
print(30 in numbers)
```

Output:

```text
True
```

## F. Membership Operator `not in`

Checks whether an element does not exist in the list.

```python
print(100 not in numbers)
```

Output:

```text
True
```

## G. List Concatenation

The `+` operator combines two lists into a new list.

```python
first = [10, 20]
second = [30, 40]

result = first + second

print(result)
```

Output:

```text
[10, 20, 30, 40]
```

## H. List Repetition

The `*` operator repeats the list contents.

```python
numbers = [1, 2, 3]

print(numbers * 2)
```

Output:

```text
[1, 2, 3, 1, 2, 3]
```

---

# 10. Copying Lists

Copying is an important operation because two variables can refer to the same list or to different lists.

## A. Assignment and Aliasing

When we assign one list variable to another, both names refer to the same list object.

```python
first = [10, 20, 30]

second = first

second.append(40)

print("First:", first)
print("Second:", second)
```

### Output

```text
First: [10, 20, 30, 40]
Second: [10, 20, 30, 40]
```

Changing the list using one variable also affects the other because both refer to the same object.

## B. Copy Using `copy()`

The `copy()` method creates a shallow copy of a list.

```python
first = [10, 20, 30]

second = first.copy()

second.append(40)

print("First:", first)
print("Second:", second)
```

### Output

```text
First: [10, 20, 30]
Second: [10, 20, 30, 40]
```

## C. Copy Using Slicing

```python
first = [10, 20, 30]

second = first[:]

print(second)
```

## D. Copy Using `list()`

```python
first = [10, 20, 30]

second = list(first)

print(second)
```

### Important Note About Shallow Copy

A shallow copy creates a new outer list, but nested objects inside it are still shared.

For nested lists, modifying an inner object may therefore affect both outer lists.

Use `copy.deepcopy()` from the `copy` module when an independent copy of nested mutable objects is required.

---

# 11. Twelve Important Topic Examples

The following examples match the twelve topic examples in `01_list_basics.py`.

## Example 1 – Creating a List

**Concept:** Creating a list using square brackets.

```python
fruits = ["Apple", "Banana", "Mango"]

print("Fruits:", fruits)
print("Data type:", type(fruits))
```

### Output

```text
Fruits: ['Apple', 'Banana', 'Mango']
Data type: <class 'list'>
```

**Explanation:** The `fruits` variable stores three string elements inside a list.

## Example 2 – Ordered Collection and Duplicates

**Concept:** Lists preserve element order and allow duplicate values.

```python
numbers = [10, 20, 30, 20, 40, 10]

print("Original list:", numbers)
print("First element:", numbers[0])
print("Third element:", numbers[2])
```

### Output

```text
Original list: [10, 20, 30, 20, 40, 10]
First element: 10
Third element: 30
```

**Explanation:** Duplicate values remain in the list, and elements can be accessed by their positions.

## Example 3 – Mixed Data Types

**Concept:** Storing different kinds of data in one list.

```python
student = ["Amaan", 22, 85.5, True]

print("Student information:", student)

for item in student:
    print(item, "->", type(item).__name__)
```

### Output

```text
Student information: ['Amaan', 22, 85.5, True]
Amaan -> str
22 -> int
85.5 -> float
True -> bool
```

**Explanation:** Python lists can store elements with different data types.

## Example 4 – Creating an Empty List

**Concept:** Creating an empty list using two methods.

```python
first_list = []
second_list = list()

print("Empty list using brackets:", first_list)
print("Empty list using list():", second_list)

print("Length of first list:", len(first_list))
print("Length of second list:", len(second_list))
```

### Output

```text
Empty list using brackets: []
Empty list using list(): []
Length of first list: 0
Length of second list: 0
```

**Explanation:** Both methods create an empty list.

## Example 5 – Positive Indexing

**Concept:** Accessing elements using zero-based indexes.

```python
colors = ["Red", "Green", "Blue", "Yellow"]

print("Colors:", colors)
print("Index 0:", colors[0])
print("Index 1:", colors[1])
print("Index 2:", colors[2])
print("Index 3:", colors[3])
```

### Output

```text
Colors: ['Red', 'Green', 'Blue', 'Yellow']
Index 0: Red
Index 1: Green
Index 2: Blue
Index 3: Yellow
```

## Example 6 – Negative Indexing

**Concept:** Accessing elements from the end of a list.

```python
animals = ["Dog", "Cat", "Lion", "Tiger"]

print("Animals:", animals)
print("Last element:", animals[-1])
print("Second-last element:", animals[-2])
print("Third-last element:", animals[-3])
```

### Output

```text
Animals: ['Dog', 'Cat', 'Lion', 'Tiger']
Last element: Tiger
Second-last element: Lion
Third-last element: Cat
```

## Example 7 – Updating List Elements

**Concept:** Modifying an existing element.

```python
marks = [75, 80, 65, 90]

print("Original marks:", marks)

marks[2] = 85

print("Updated marks:", marks)
```

### Output

```text
Original marks: [75, 80, 65, 90]
Updated marks: [75, 80, 85, 90]
```

## Example 8 – Appending Elements

**Concept:** Adding one new element to the end.

```python
numbers = [10, 20, 30]

print("Before append:", numbers)

numbers.append(40)

print("After append:", numbers)
```

### Output

```text
Before append: [10, 20, 30]
After append: [10, 20, 30, 40]
```

## Example 9 – Extending a List

**Concept:** Adding multiple elements from another iterable.

```python
first_list = [10, 20, 30]
second_list = [40, 50, 60]

print("First list:", first_list)
print("Second list:", second_list)

first_list.extend(second_list)

print("After extending:", first_list)
```

### Output

```text
First list: [10, 20, 30]
Second list: [40, 50, 60]
After extending: [10, 20, 30, 40, 50, 60]
```

## Example 10 – Inserting an Element

**Concept:** Adding an element at a specified index.

```python
fruits = ["Apple", "Mango", "Orange"]

print("Before insertion:", fruits)

fruits.insert(1, "Banana")

print("After insertion:", fruits)
```

### Output

```text
Before insertion: ['Apple', 'Mango', 'Orange']
After insertion: ['Apple', 'Banana', 'Mango', 'Orange']
```

## Example 11 – Remove and Pop

**Concept:** Removing an element by value and by position.

```python
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

numbers.remove(30)

print("After remove(30):", numbers)

removed_value = numbers.pop()

print("Popped value:", removed_value)
print("After pop():", numbers)
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
After remove(30): [10, 20, 40, 50]
Popped value: 50
After pop(): [10, 20, 40]
```

## Example 12 – Basic List Properties

**Concept:** Using built-in functions and membership operators.

```python
numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

print("Is 30 present?", 30 in numbers)
print("Is 100 absent?", 100 not in numbers)
```

### Output

```text
Numbers: [10, 20, 30, 40, 50]
Length: 5
Sum: 150
Minimum: 10
Maximum: 50
Is 30 present? True
Is 100 absent? True
```

---

# 12. Twelve Solved Programming Problems

These problems match the twelve solved problem functions in `01_list_basics.py`.

## Problem 1 – Create and Display a List

**Question:** Accept multiple names from the user, create a list and display the list with its length.

### Logic

1. Take comma-separated input.
2. Separate the values.
3. Store the names in a list.
4. Calculate the length.
5. Display the list.

### Code

```python
names = input("Enter names separated by commas: ")

student_names = [
    name.strip()
    for name in names.split(",")
]

print("Created list:", student_names)
print("Total names:", len(student_names))
```

### Sample Input

```text
Enter names separated by commas: Amaan, Rahul, Sara, Arjun
```

### Output

```text
Created list: ['Amaan', 'Rahul', 'Sara', 'Arjun']
Total names: 4
```

**Complexity:** O(n) time for processing n characters and producing the list; O(n) auxiliary storage.

## Problem 2 – Access First and Last Elements

**Question:** Accept a list of integers and display its first and last elements.

### Logic

- Use index `0` to access the first element.
- Use index `-1` to access the last element.

### Code

```python
numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
```

### Output

```text
First element: 10
Last element: 50
```

**Complexity:** O(1) time and O(1) auxiliary space.

**Note:** The source program first validates that at least one integer has been entered.

## Problem 3 – Update a List Element

**Question:** Update an element at an index provided by the user.

### Code

```python
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

index = int(input("Enter the index to update: "))
new_value = int(input("Enter the new value: "))

if 0 <= index < len(numbers):
    numbers[index] = new_value
    print("Updated list:", numbers)
else:
    print("Invalid index.")
```

### Sample Input

```text
Enter the index to update: 2
Enter the new value: 100
```

### Output

```text
Original list: [10, 20, 30, 40, 50]
Updated list: [10, 20, 100, 40, 50]
```

**Complexity:** O(1) time and O(1) auxiliary space.

## Problem 4 – Append an Element

**Question:** Add a new integer to the end of an existing list.

### Code

```python
numbers = [10, 20, 30]

print("Before append:", numbers)

numbers.append(40)

print("After append:", numbers)
```

### Output

```text
Before append: [10, 20, 30]
After append: [10, 20, 30, 40]
```

**Complexity:** Amortized O(1) time and O(1) auxiliary space, excluding occasional internal resizing.

## Problem 5 – Combine Two Lists

**Question:** Combine two lists into a third list.

### Code

```python
first_list = [10, 20, 30]
second_list = [40, 50, 60]

combined_list = first_list + second_list

print("First list:", first_list)
print("Second list:", second_list)
print("Combined list:", combined_list)
```

### Output

```text
First list: [10, 20, 30]
Second list: [40, 50, 60]
Combined list: [10, 20, 30, 40, 50, 60]
```

**Complexity:** O(n + m) time and O(n + m) output space, where n and m are the two list lengths.

## Problem 6 – Insert an Element at a Position

**Question:** Insert a new value at a user-selected position.

### Code

```python
numbers = [10, 20, 30, 40]

position = int(input("Enter insertion position: "))
value = int(input("Enter the value to insert: "))

if 0 <= position <= len(numbers):
    numbers.insert(position, value)
    print("Updated list:", numbers)
else:
    print("Invalid insertion position.")
```

### Sample Input

```text
Enter insertion position: 2
Enter the value to insert: 25
```

### Output

```text
Updated list: [10, 20, 25, 30, 40]
```

**Complexity:** O(n) time in the worst case and O(1) auxiliary space.

## Problem 7 – Remove an Element

**Question:** Remove the first occurrence of a user-selected fruit.

### Code

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

value = input("Enter the fruit to remove: ").strip()

if value in fruits:
    fruits.remove(value)
    print("Updated list:", fruits)
else:
    print("Fruit not found.")
```

### Sample Input

```text
Enter the fruit to remove: Mango
```

### Output

```text
Updated list: ['Apple', 'Banana', 'Orange']
```

**Complexity:** O(n) time and O(1) auxiliary space.

**Note:** The source program performs an exact, case-sensitive match.

## Problem 8 – Count Element Occurrences

**Question:** Count how many times a particular number appears in a list.

### Code

```python
numbers = [10, 20, 10, 30, 10, 40]

target = int(input("Enter the number to count: "))

occurrences = numbers.count(target)

print("Occurrences:", occurrences)
```

### Sample Input

```text
Enter the number to count: 10
```

### Output

```text
Occurrences: 3
```

**Complexity:** O(n) time and O(1) auxiliary space.

## Problem 9 – Calculate List Sum

**Question:** Calculate the sum of every element in a numeric list.

### Code

```python
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("Numbers:", numbers)
print("Total sum:", total)
```

### Output

```text
Numbers: [10, 20, 30, 40, 50]
Total sum: 150
```

**Complexity:** O(n) time and O(1) auxiliary space for the summation itself.

## Problem 10 – Find Minimum and Maximum

**Question:** Find the smallest and largest elements of a numeric list.

### Code

```python
numbers = [45, 12, 89, 34, 67]

smallest = min(numbers)
largest = max(numbers)

print("Minimum value:", smallest)
print("Maximum value:", largest)
```

### Output

```text
Minimum value: 12
Maximum value: 89
```

**Complexity:** O(n) time and O(1) auxiliary space.

## Problem 11 – Check Element Membership

**Question:** Check whether a given element exists in a list.

### Code

```python
numbers = [10, 20, 30, 40, 50]

target = int(input("Enter the value to search for: "))

if target in numbers:
    print("Element exists in the list.")
else:
    print("Element does not exist in the list.")
```

### Sample Input

```text
Enter the value to search for: 30
```

### Output

```text
Element exists in the list.
```

**Complexity:** O(n) worst-case time and O(1) auxiliary space.

## Problem 12 – Copy a List

**Question:** Create an independent copy of a list and demonstrate that modifying the copy does not modify the original list.

### Code

```python
original = [10, 20, 30, 40]

copied_list = original.copy()

copied_list.append(50)

print("Original list:", original)
print("Copied list:", copied_list)
```

### Output

```text
Original list: [10, 20, 30, 40]
Copied list: [10, 20, 30, 40, 50]
```

**Complexity:** O(n) time and O(n) additional space for a shallow copy of n elements.

**Note:** This example uses integers. For nested mutable objects, `copy()` is shallow, so inner objects remain shared.

---

# 13. Ten Unsolved Practice Questions

Try these questions independently before reviewing any solutions.

| No. | Question | Difficulty |
|---|---|---|
| 1 | Create a list containing five student names and display the complete list. | Easy |
| 2 | Write a program to display the second element of a list. Handle invalid list sizes. | Easy |
| 3 | Create a list of five integers and replace its third element with a new value. | Easy |
| 4 | Create a list and add three new elements to its end. | Easy |
| 5 | Take two lists from the user and combine them into a third list. | Easy |
| 6 | Insert a new element at a position entered by the user. | Medium |
| 7 | Remove the first occurrence of a user-selected value from a list, if present. | Medium |
| 8 | Count how many times a particular number appears in a list. | Easy |
| 9 | Find the sum, minimum and maximum of a non-empty numeric list. | Easy |
| 10 | Copy a list, modify the copy and demonstrate that the original remains unchanged. | Medium |

### Practice Guidelines

For each question:

1. Understand what the question is asking.
2. Identify which list operation is required.
3. Write the code independently.
4. Test different inputs.
5. Handle empty lists and invalid positions.
6. Understand the time complexity.
7. Explain your solution in your own words.

---

# 14. Time and Space Complexity of List Operations

Understanding complexity is important for DSA.

Python lists are dynamic arrays. Their operations have different performance characteristics.

Let `n` be the number of elements in a list and `k` be the number of elements being added.

| Operation | Time Complexity | Explanation |
|---|---|---|
| Access by index | O(1) | Direct indexing |
| Update by index | O(1) | Direct assignment |
| `len(list)` | O(1) | List length is maintained |
| `append(value)` | Amortized O(1) | Adds at the end |
| `extend(iterable)` | O(k) | Adds k elements |
| `insert(0, value)` | O(n) | Existing elements shift |
| `insert(index, value)` | O(n) | Elements may shift |
| `remove(value)` | O(n) | Searches and may shift elements |
| `pop()` | O(1) | Removes last element |
| `pop(index)` | O(n) | May shift elements |
| `clear()` | O(n) | Removes references to all elements |
| `value in list` | O(n) | Sequential membership search |
| `count(value)` | O(n) | Checks all elements |
| `sum(list)` | O(n) | Traverses all numeric values |
| `min(list)` | O(n) | Traverses the list |
| `max(list)` | O(n) | Traverses the list |
| List concatenation | O(n + m) | Creates a new combined list |
| Shallow copy | O(n) | Copies references to elements |

### Important Complexity Concepts

**O(1) – Constant Time**

The operation takes approximately constant time regardless of list length.

Example: Accessing an element using its index.

**O(n) – Linear Time**

The work grows proportionally with the number of elements.

Example: Searching for a value using `in`.

**O(n + m) – Linear in Both Lists**

The work depends on the lengths of both input lists.

Example: Concatenating two lists.

**Amortized O(1)**

An individual append can occasionally require resizing, but over many append operations the average cost per append is constant.

### Important DSA Observation

Lists provide fast access by index, but inserting or removing elements near the beginning can be expensive because other elements may need to shift.

---

# 15. Common Mistakes in Python Lists

## Mistake 1 – Using an Invalid Index

Incorrect:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

This raises `IndexError` because index 5 does not exist.

Correct:

```python
numbers = [10, 20, 30]

if len(numbers) > 2:
    print(numbers[2])
```

## Mistake 2 – Confusing `append()` and `extend()`

```python
first = [1, 2]
second = [3, 4]

first.append(second)

print(first)
```

Output:

```text
[1, 2, [3, 4]]
```

Using `extend()`:

```python
first = [1, 2]
second = [3, 4]

first.extend(second)

print(first)
```

Output:

```text
[1, 2, 3, 4]
```

## Mistake 3 – Forgetting That `remove()` Uses Values

```python
numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)
```

`remove()` removes the first matching value, not the element at index 30.

## Mistake 4 – Confusing `remove()` and `pop()`

- `remove(value)` removes by value.
- `pop(index)` removes by position and returns the removed element.

## Mistake 5 – Assuming Assignment Creates a New Copy

Incorrect assumption:

```python
first = [10, 20, 30]
second = first

second.append(40)

print(first)
```

The original list also changes because both variables reference the same list object.

Use:

```python
second = first.copy()
```

when a separate shallow copy is needed.

## Mistake 6 – Calling `min()` or `max()` on an Empty List

```python
numbers = []

# min(numbers) raises ValueError.
# max(numbers) raises ValueError.
```

Check the list before using these operations.

## Mistake 7 – Modifying a List While Iterating Over It

Changing a list while iterating through it can cause some elements to be skipped or processed unexpectedly.

A safer approach is to iterate over a copy or build a new list when removing selected elements.

---

# 16. Mini Project – Student Marks Management System

## Project Description

Create a program that manages the marks of students using Python lists.

The program should allow the user to:

1. Store student marks.
2. Display all marks.
3. Add a new mark.
4. Update a mark.
5. Remove a mark.
6. Calculate total marks.
7. Calculate average marks.
8. Find the highest and lowest marks.

### Concepts Used

- List creation.
- List indexing.
- List updating.
- `append()`.
- `remove()` and `pop()` concepts.
- `len()`.
- `sum()`.
- `min()` and `max()`.
- Functions.
- Loops and conditional statements.

### Complete Code

```python
def display_marks(marks):
    if not marks:
        print("No marks available.")
        return

    print("\nStudent Marks:")

    for index, mark in enumerate(marks, start=1):
        print(f"Student {index}: {mark}")


def add_mark(marks):
    mark = float(input("Enter new mark (0-100): "))

    if 0 <= mark <= 100:
        marks.append(mark)
        print("Mark added successfully.")
    else:
        print("Invalid mark. Enter a value from 0 to 100.")


def update_mark(marks):
    if not marks:
        print("No marks available.")
        return

    display_marks(marks)

    index = int(input("Enter student number to update: ")) - 1

    if 0 <= index < len(marks):
        new_mark = float(input("Enter new mark: "))

        if 0 <= new_mark <= 100:
            marks[index] = new_mark
            print("Mark updated successfully.")
        else:
            print("Invalid mark.")
    else:
        print("Invalid student number.")


def remove_mark(marks):
    if not marks:
        print("No marks available.")
        return

    display_marks(marks)

    index = int(input("Enter student number to remove: ")) - 1

    if 0 <= index < len(marks):
        removed = marks.pop(index)
        print("Removed mark:", removed)
    else:
        print("Invalid student number.")


def calculate_statistics(marks):
    if not marks:
        print("No marks available.")
        return

    total = sum(marks)
    average = total / len(marks)

    print("\n========== RESULT STATISTICS ==========")
    print("Total Students:", len(marks))
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
    print("=======================================")


def main():
    marks = [75, 80, 85, 90, 65]

    while True:
        print("\n====== STUDENT MARKS MANAGER ======")
        print("1. Display marks")
        print("2. Add mark")
        print("3. Update mark")
        print("4. Remove mark")
        print("5. Calculate statistics")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                display_marks(marks)

            elif choice == "2":
                add_mark(marks)

            elif choice == "3":
                update_mark(marks)

            elif choice == "4":
                remove_mark(marks)

            elif choice == "5":
                calculate_statistics(marks)

            elif choice == "0":
                print("Thank you for using Student Marks Manager.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid numeric input.")


if __name__ == "__main__":
    main()
```

### Sample Output

```text
====== STUDENT MARKS MANAGER ======
1. Display marks
2. Add mark
3. Update mark
4. Remove mark
5. Calculate statistics
0. Exit

Enter your choice: 5

========== RESULT STATISTICS ==========
Total Students: 5
Total Marks: 395
Average Marks: 79.0
Highest Marks: 90
Lowest Marks: 65
=======================================
```

### Project Extension Ideas

1. Store student names along with marks.
2. Calculate grades for each student.
3. Search for a particular student's result.
4. Sort students by marks.
5. Display the top three scores.
6. Remove duplicate marks.
7. Store results in a file.
8. Build a menu-driven student database.

---

# 17. Real-World Applications of Python Lists

Lists are used in many practical software applications.

## 1. Student Management Systems

Lists can store student names, marks, roll numbers and other information.

## 2. E-Commerce Applications

Lists can store cart items, product IDs, product quantities and order details.

## 3. Banking Applications

Lists can store transaction records and account activity.

## 4. Web Development

Lists can hold records returned by database queries or API responses.

## 5. Data Science

Lists can store collected values, transformed information and intermediate data.

## 6. Automation

Lists can track files, folder names, tasks and processing results.

## 7. Game Development

Lists can store player scores, inventory items and game states.

## 8. Software Development

Lists are used when applications need an ordered collection of values that can change dynamically.

---

# 18. Connection Between Python Lists and DSA

Lists are an important foundation for learning Data Structures and Algorithms.

A Python list is a dynamic array. It offers efficient access by index and supports many operations used in algorithm design.

### DSA Applications

| DSA Concept | List Application |
|---|---|
| Arrays | Store sequential elements |
| Linear Search | Search elements one by one |
| Binary Search | Search a sorted list |
| Sorting | Arrange values in ascending or descending order |
| Two Pointers | Process elements using two indexes |
| Sliding Window | Process contiguous portions of a list |
| Prefix Sum | Calculate cumulative sums |
| Stack | Use list operations such as `append()` and `pop()` |
| Dynamic Programming | Store previously computed results |
| Matrix | Represent rows and columns using nested lists |

### Recommended DSA Learning Path

```text
List Basics
    |
    v
List Indexing and Slicing
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
Nested Lists
    |
    v
Searching Algorithms
    |
    v
Sorting Algorithms
    |
    v
Two Pointers
    |
    v
Sliding Window
    |
    v
Dynamic Programming
```

---

# 19. Fifty Important Viva Questions and Answers

## Basic List Questions

**Q1. What is a list in Python?**

A list is an ordered and mutable collection of elements.

**Q2. Which brackets are used to create a list?**

Square brackets `[]`.

**Q3. Is a Python list mutable?**

Yes. List elements can be modified after creation.

**Q4. Is a Python list ordered?**

Yes. It maintains the sequence of its elements.

**Q5. Does a list allow duplicate elements?**

Yes. A list can contain duplicate values.

**Q6. Can a list contain different data types?**

Yes. It can store integers, strings, floats, booleans and other objects.

**Q7. What is an empty list?**

A list containing zero elements.

**Q8. How can you create an empty list?**

Using `[]` or `list()`.

**Q9. What is indexing?**

Indexing is the process of accessing an element using its position.

**Q10. What is the index of the first element in a list?**

Zero.

## Indexing and Updating Questions

**Q11. What is positive indexing?**

Accessing elements starting from index zero at the beginning of a list.

**Q12. What is negative indexing?**

Accessing elements by counting from the end of a list.

**Q13. What is the index of the last element using negative indexing?**

`-1`.

**Q14. Can list elements be updated?**

Yes. Lists are mutable, so elements can be reassigned.

**Q15. What happens when an invalid index is accessed?**

Python raises `IndexError`.

**Q16. How can you find the number of elements in a list?**

Using the `len()` function.

**Q17. What does `append()` do?**

It adds one element to the end of a list.

**Q18. What does `extend()` do?**

It adds all elements from an iterable to the end of a list.

**Q19. What does `insert()` do?**

It inserts an element at a specified position.

**Q20. What is the difference between `append()` and `extend()`?**

`append()` adds its argument as one element, whereas `extend()` adds the elements of an iterable individually.

## List Methods Questions

**Q21. What does `remove()` do?**

It removes the first occurrence of a specified value.

**Q22. What does `pop()` do?**

It removes and returns an element, using the final position by default.

**Q23. What is the difference between `remove()` and `pop()`?**

`remove()` deletes by value, while `pop()` deletes and returns an element by index.

**Q24. What does `clear()` do?**

It removes all elements from the list.

**Q25. What does `del` do?**

It deletes an element, a slice or the entire list variable.

**Q26. What is the use of `count()`?**

It counts how many times a value appears in a list.

**Q27. What is the use of `index()`?**

It returns the index of the first occurrence of a value.

**Q28. What is the use of `copy()`?**

It creates a shallow copy of a list.

**Q29. How can you calculate the sum of a numeric list?**

Using `sum()`.

**Q30. How can you find the smallest element in a list?**

Using `min()`.

## Intermediate List Questions

**Q31. How can you find the largest element in a list?**

Using `max()`.

**Q32. What does the `in` operator do with a list?**

It checks whether a value exists in the list.

**Q33. What is list concatenation?**

Combining two lists using the `+` operator to create a new list.

**Q34. What does list repetition do?**

It repeats a list's contents using the `*` operator.

**Q35. What is list aliasing?**

It occurs when multiple variables refer to the same list object.

**Q36. What is shallow copying?**

It creates a new outer list but keeps references to the original inner objects.

**Q37. How can a shallow copy be created?**

Using `copy()`, slicing or `list()`.

**Q38. Does `append()` return the updated list?**

No. It modifies the list in place and returns `None`.

**Q39. What happens when `remove()` is used with a value that does not exist?**

It raises `ValueError`.

**Q40. What happens when `pop()` is called on an empty list?**

It raises `IndexError`.

## DSA and Practical Questions

**Q41. What is the average or typical time complexity of accessing a list element by index?**

O(1).

**Q42. What is the time complexity of searching for an element using `in`?**

O(n) in the worst case.

**Q43. What is the average time complexity of appending an element?**

Amortized O(1).

**Q44. What is the time complexity of inserting at the beginning of a list?**

O(n).

**Q45. What is the time complexity of removing the last element using `pop()`?**

O(1).

**Q46. Why are lists useful in DSA?**

They provide an efficient way to store ordered elements and support algorithms such as searching, sorting and sliding-window operations.

**Q47. Can a list contain another list?**

Yes. Such a structure is called a nested list.

**Q48. What is the difference between a Python list and an array in basic data structure terminology?**

A Python list is a dynamic array that can contain references to objects of different types, whereas a traditional fixed-type array generally stores elements of a single specified type.

**Q49. Can a Python list be used to implement a stack?**

Yes. `append()` can be used for push, and `pop()` can be used for pop at the end.

**Q50. Why should we learn lists before advanced DSA?**

Lists provide the foundation for understanding indexing, iteration, searching, sorting, arrays, stacks and many other algorithmic techniques.

---

# 20. Important List Terminology

| Term | Meaning |
|---|---|
| List | Ordered, mutable collection |
| Element | A value stored inside a list |
| Index | Position of an element |
| Positive Indexing | Indexing from the beginning |
| Negative Indexing | Indexing from the end |
| Mutable | Can be modified |
| Duplicate | Repeated value |
| Append | Add one element at the end |
| Extend | Add elements from an iterable |
| Insert | Add an element at a position |
| Remove | Delete the first matching value |
| Pop | Remove and return an element |
| Clear | Remove all elements |
| Concatenation | Combine lists |
| Aliasing | Multiple names referring to the same object |
| Shallow Copy | New outer list with shared references to inner objects |
| Dynamic Array | Resizable array-backed collection |

---

# 21. Quick Revision Notes

Remember the following points:

1. A list is an ordered collection.
2. Lists are mutable.
3. Lists allow duplicate values.
4. Lists can store different data types.
5. Lists are created using square brackets.
6. The first element has index `0`.
7. The last element can be accessed using `-1`.
8. Use `append()` to add one element at the end.
9. Use `extend()` to add multiple elements.
10. Use `insert()` to add an element at a specific position.
11. Use `remove()` to delete the first matching value.
12. Use `pop()` to remove and return an element.
13. Use `clear()` to remove all elements.
14. Use `len()` to find list length.
15. Use `sum()` to calculate a numeric total.
16. Use `min()` and `max()` to find minimum and maximum values.
17. Use `in` to check membership.
18. Use `+` to concatenate two lists.
19. Use `copy()` to create a shallow copy.
20. List indexing is generally O(1).
21. Searching using `in` is O(n) in the worst case.
22. Appending is amortized O(1).
23. Inserting at the beginning is O(n).
24. Lists are commonly used to implement arrays and stacks.

---

# 22. Learning Checklist

Complete this checklist before moving to the next topic.

## List Fundamentals

- [ ] Understand what a list is.
- [ ] Understand ordered collections.
- [ ] Understand mutable collections.
- [ ] Understand duplicate elements.
- [ ] Create lists using square brackets.
- [ ] Create empty lists.
- [ ] Store mixed data types in a list.

## Indexing and Updating

- [ ] Understand positive indexing.
- [ ] Understand negative indexing.
- [ ] Access first and last elements.
- [ ] Update an element using an index.
- [ ] Handle invalid indexes.

## Adding Elements

- [ ] Use `append()`.
- [ ] Use `extend()`.
- [ ] Use `insert()`.
- [ ] Understand the differences between these methods.

## Removing Elements

- [ ] Use `remove()`.
- [ ] Use `pop()`.
- [ ] Use `del`.
- [ ] Use `clear()`.
- [ ] Handle missing values and invalid positions.

## List Operations

- [ ] Find list length.
- [ ] Calculate list sum.
- [ ] Find minimum value.
- [ ] Find maximum value.
- [ ] Check membership.
- [ ] Combine two lists.
- [ ] Repeat list elements.
- [ ] Copy lists.
- [ ] Understand list aliasing.

## Problem Solving

- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Understand the solution logic.
- [ ] Analyze time complexity.
- [ ] Analyze auxiliary space complexity.
- [ ] Complete the mini project.
- [ ] Review all 50 viva questions.

---

# 23. Python File Information

**Topic Name:** List Basics

**Topic Number:** 01

**Section:** Python Fundamentals – Lists and Tuples

**Python File:**

```text
01_list_basics.py
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
        └── 01-List-Basics/
            ├── README.md
            └── 01_list_basics.py
```

### How to Run the Program

Open your terminal from the repository root directory and execute:

```bash
python PYTHON/Python-Fundamentals/03-Lists-and-Tuples/01-List-Basics/01_list_basics.py
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

Choose an option to explore examples, execute solved programs, review practice questions or revise the concepts.

---

# 24. Conclusion

Python lists are one of the most important foundations of Python programming and Data Structures and Algorithms.

By completing this topic, you have learned how to create lists, store multiple values, access elements, update data, add and remove elements, calculate basic statistics, combine lists and create copies.

These skills are useful in real-world software applications and prepare you for advanced topics such as list comprehensions, nested lists, searching, sorting, arrays, stacks and dynamic programming.

**Do not memorize list methods only. Understand how every operation changes the list and what its time complexity is.**

---

## Next Topic

**Topic 02 – List Indexing and Slicing**

In the next topic, you will learn:

- Positive indexing in detail.
- Negative indexing in detail.
- Accessing list ranges.
- Basic slicing syntax.
- Start, stop and step.
- Omitting slice parameters.
- Reversing a list using slicing.
- Copying lists using slicing.
- Practical indexing and slicing problems.

**Keep Practicing. Keep Building. Keep Coding!**