# Multiple Variables in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Variables  
**Topic:** Multiple Variables  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. What Are Multiple Variables?
4. Assigning Values to Multiple Variables
5. Chained Assignment
6. Tuple Unpacking
7. List Unpacking
8. Starred Unpacking
9. Swapping Variables
10. Returning Multiple Values from Functions
11. Using `zip()` with Multiple Collections
12. Using `enumerate()` to Access Index and Value
13. The `divmod()` Function
14. Multiple Assignment in Loops
15. Variable Naming and Readability
16. Explanation of the 12 Guided Examples
17. Explanation of the 12 Solved Problems
18. Five Unsolved Practice Questions
19. Common Errors and Debugging
20. Best Practices
21. Frequently Asked Questions
22. How to Run the Program
23. Folder Structure
24. Revision Checklist

---

# 1. Introduction

A Python program often needs to work with multiple related values.

For example, a student record may contain a name, age, and course. A geometric calculation may require length and width. A function may need to return both an area and a perimeter.

Python provides several ways to assign, exchange, group, and unpack multiple values.

This topic introduces:

- Multiple assignment.
- Chained assignment.
- Tuple and list unpacking.
- Starred unpacking.
- Swapping values.
- Functions that return multiple values.
- Parallel iteration using `zip()`.
- Index-value pairs using `enumerate()`.
- Quotient and remainder using `divmod()`.

These techniques make code more concise and help organize related values clearly.

# 2. Learning Objectives

After completing this topic, you should be able to:

- Assign several values to several variable names in one statement.
- Assign one value to multiple names using chained assignment.
- Unpack tuples and lists into separate variables.
- Use starred unpacking for a variable number of middle elements.
- Swap two variable values.
- Return and unpack multiple results from a function.
- Iterate over related lists using `zip()`.
- Iterate over indices and values using `enumerate()`.
- Use `divmod()` to obtain quotient and remainder.
- Understand the difference between chained assignment and parallel assignment.
- Recognize unpacking errors.
- Apply these techniques to mathematical and programming problems.

# 3. What Are Multiple Variables?

Multiple variables are separate names used to represent multiple values in a program.

Example:

```python
student_name = "Amaan"
student_age = 20
course_name = "Computer Science"
```

Each variable refers to its own value.

Python also allows multiple assignments to be written on a single line.

```python
student_name, student_age, course_name = (
    "Amaan",
    20,
    "Computer Science",
)
```

In this example, three values are assigned to three variables.

The two approaches express the same assignments. The second form is particularly useful when related values are naturally grouped together.

**Important:** Using multiple variables does not mean they must contain values of the same type. A single assignment can assign a string, an integer, and another string to different names.

# 4. Assigning Values to Multiple Variables

Python supports assignment to multiple targets in one statement.

### Syntax

```python
first, second, third = 10, 20, 30
```

This is called multiple assignment.

Python evaluates the right-hand values and assigns them to the corresponding targets on the left.

Example:

```python
name, age, score = "Sara", 19, 92

print(name)
print(age)
print(score)
```

Output:

```text
Sara
19
92
```

### Practical Example

```python
length, width = 8, 5

area = length * width
perimeter = 2 * (length + width)

print(area)
print(perimeter)
```

Output:

```text
40
26
```

### Matching the Number of Values

The number of targets should match the number of unpacked values unless a starred target is used.

Valid:

```python
a, b = 10, 20
```

Invalid:

```python
a, b = 10, 20, 30
```

The second example raises a `ValueError` because there are three values but only two targets.

# 5. Chained Assignment

Chained assignment assigns one value to multiple targets.

### Syntax

```python
first_count = second_count = third_count = 0
```

All three names receive the same assigned object.

Example:

```python
x = y = z = 100

print(x, y, z)
```

Output:

```text
100 100 100
```

This is convenient when initializing multiple counters with the same immutable value.

### Important Note About Mutable Objects

Be careful when using chained assignment with mutable objects, such as lists.

```python
first_list = second_list = []

first_list.append(10)

print(first_list)
print(second_list)
```

Output:

```text
[10]
[10]
```

Both names refer to the same list object. Updating the list through one name is visible through the other.

If independent lists are required, assign separate list objects:

```python
first_list = []
second_list = []
```

This distinction is important when working with lists, dictionaries, and other mutable objects.

# 6. Tuple Unpacking

A tuple is an ordered collection that can contain multiple values.

Tuple unpacking assigns the tuple's items to separate variable names.

Example:

```python
student_record = ("Amaan", 20, "Diploma")

student_name, student_age, qualification = student_record

print(student_name)
print(student_age)
print(qualification)
```

Output:

```text
Amaan
20
Diploma
```

### How It Works

The tuple contains three values in order.

The first value is assigned to `student_name`, the second to `student_age`, and the third to `qualification`.

### Returning Values from a Function

Python functions can return a tuple containing multiple values.

```python
def calculate_values(a, b):
    return a + b, a - b

total, difference = calculate_values(10, 4)

print(total)
print(difference)
```

Output:

```text
14
6
```

Technically, the function returns one tuple object containing two results. The assignment unpacks its elements into two separate names.

# 7. List Unpacking

A list can also be unpacked into multiple variables.

Example:

```python
dimensions = [12, 8, 5]

length, width, height = dimensions

print(length)
print(width)
print(height)
```

Output:

```text
12
8
5
```

### List Unpacking Requirements

Without a starred target, the number of list elements must match the number of targets.

For example:

```python
a, b, c = [10, 20, 30]
```

This is valid because there are three elements and three targets.

However:

```python
a, b = [10, 20, 30]
```

raises `ValueError` because the list contains more values than there are targets.

The same principle applies to tuple unpacking and other iterable unpacking operations.

# 8. Starred Unpacking

Starred unpacking uses `*` before one target name to collect multiple remaining values into a list.

Example:

```python
scores = [75, 82, 91, 68, 88]

first_score, *remaining_scores = scores

print(first_score)
print(remaining_scores)
```

Output:

```text
75
[82, 91, 68, 88]
```

The starred target collects all remaining values after the first one into a list.

## First, Middle, and Last Values

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
10
[20, 30, 40]
50
```

### When Is Starred Unpacking Useful?

- Separating the first item from the remaining items.
- Separating the first and last items from a sequence.
- Processing a variable number of values.
- Handling function arguments or data records with a flexible middle section.

Only one starred target may appear in a single unpacking target list at a given unpacking level.

# 9. Swapping Variables

Swapping means exchanging the values associated with two variables.

Suppose:

```python
first_value = 10
second_value = 20
```

After swapping, `first_value` should refer to `20`, and `second_value` should refer to `10`.

## Method 1: Using a Temporary Variable

```python
first_value = 10
second_value = 20

temporary_value = first_value
first_value = second_value
second_value = temporary_value

print(first_value, second_value)
```

Output:

```text
20 10
```

### Explanation

1. Preserve the original first value in `temporary_value`.
2. Assign the second value to the first variable.
3. Copy the preserved value into the second variable.

The temporary variable prevents the original first value from being lost.

## Method 2: Python Tuple Assignment

Python provides a concise alternative:

```python
first_value = 10
second_value = 20

first_value, second_value = second_value, first_value

print(first_value, second_value)
```

Output:

```text
20 10
```

The right-hand expressions are evaluated before the unpacking assignments take effect, so both original values remain available.

This is a common and readable Python idiom.

# 10. Returning Multiple Values from Functions

A function may need to calculate and return more than one result.

Example:

```python
def rectangle_measurements(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


area, perimeter = rectangle_measurements(8, 5)

print(area)
print(perimeter)
```

Output:

```text
40
26
```

### Explanation

1. The function receives the length and width.
2. It calculates the area.
3. It calculates the perimeter.
4. It returns the results together as a tuple.
5. The calling statement unpacks the tuple into two variables.

### Why Return Multiple Values?

Returning related results can make a function convenient to use.

Examples include:

- Returning minimum and maximum values.
- Returning quotient and remainder.
- Returning area and perimeter.
- Returning hours, minutes, and seconds.
- Returning total and average.

Use descriptive variable names so that each returned value is easy to understand.

# 11. Using `zip()` with Multiple Collections

The built-in `zip()` function combines corresponding elements from multiple iterables.

Example:

```python
student_names = ["Amaan", "Sara", "Imran"]
student_marks = [85, 92, 78]

for student_name, marks in zip(student_names, student_marks):
    print(f"{student_name}: {marks}")
```

Output:

```text
Amaan: 85
Sara: 92
Imran: 78
```

Each iteration produces a pair containing the corresponding name and mark.

### Important Behavior

By default, `zip()` stops when the shortest input iterable is exhausted.

For example, if the first list contains three names and the second list contains two marks, only two pairs are produced.

If equal lengths are required, validate the lengths before using `zip()`.

For strict length checking on Python versions that support it, `zip(first, second, strict=True)` can raise a `ValueError` when the lengths differ. The examples in this topic use equal-length collections.

# 12. Using `enumerate()` to Access Index and Value

The `enumerate()` function produces index-value pairs while iterating over an iterable.

Example:

```python
subjects = ["Python", "Mathematics", "English"]

for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")
```

Output:

```text
1. Python
2. Mathematics
3. English
```

### Why Is It Useful?

`enumerate()` avoids manually creating and updating a counter when you need both the position and the value.

Without `enumerate()`, you may need a separate index variable. With `enumerate()`, both values are provided together.

Use `start=1` when human-friendly numbering is desired. The default starting index is `0`.

# 13. The `divmod()` Function

The built-in `divmod()` function returns the quotient and remainder from division as a tuple.

Example:

```python
quotient, remainder = divmod(17, 5)

print(quotient)
print(remainder)
```

Output:

```text
3
2
```

The relationship is:

```text
17 = (3 * 5) + 2
```

### Practical Application: Time Conversion

```python
total_seconds = 3665

total_minutes, remaining_seconds = divmod(total_seconds, 60)
hours, minutes = divmod(total_minutes, 60)

print(hours, minutes, remaining_seconds)
```

Output:

```text
1 1 5
```

This separates the total into one hour, one minute, and five seconds.

For negative values, Python's floor-division and modulo conventions determine the returned quotient and remainder. The examples in this topic use non-negative time or amount inputs unless stated otherwise.

# 14. Multiple Assignment in Loops

Multiple assignment is particularly useful when several related variables must be updated together.

### Example: Fibonacci Sequence

```python
first, second = 0, 1

for _ in range(7):
    print(first, end=" ")
    first, second = second, first + second
```

Output:

```text
0 1 1 2 3 5 8
```

The update calculates the next pair of values using the old values on the right-hand side.

The assignment:

```python
first, second = second, first + second
```

updates both variables based on the values before that assignment.

This pattern is useful when implementing iterative algorithms that maintain two related states.

# 15. Variable Naming and Readability

Using multiple variables makes good naming practices even more important.

Compare:

```python
a, b, c = 8, 5, 0
c = a * b
```

with:

```python
length, width = 8, 5
area = length * width
```

The second approach communicates the meaning of the calculation more clearly.

### Recommended Practices

- Use `snake_case` for ordinary variables.
- Choose names that describe the values they represent.
- Keep the order of variables consistent.
- Use names such as `first`, `second`, `quotient`, and `remainder` when they accurately describe their roles.
- Avoid overly short names for complicated calculations.
- Ensure the number and order of unpacked values match the intended data.

# 16. Explanation of the 12 Guided Examples

The Python file contains twelve interactive examples.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Multiple assignment | Assign several values in one statement |
| 2 | Same-value assignment | Initialize several names together |
| 3 | Temporary-variable swap | Exchange two stored values |
| 4 | Tuple unpacking | Assign tuple elements to variables |
| 5 | List unpacking | Unpack a list into multiple names |
| 6 | Starred unpacking | Capture remaining elements in a list |
| 7 | Returning multiple values | Return related results as a tuple |
| 8 | Unpacking function results | Receive multiple results |
| 9 | `zip()` | Iterate through corresponding list elements |
| 10 | `enumerate()` | Access indices and values together |
| 11 | Parallel state update | Update related state variables together |
| 12 | Tuple-assignment swap | Swap values without a temporary variable |

Study each example by predicting the output, running the program, and explaining what each variable represents.

# 17. Explanation of the 12 Solved Problems

## Problem 1: Swap Two Numbers

Reads two integers and exchanges them using Python's tuple assignment.

This illustrates how simultaneous assignment provides a concise alternative to a temporary variable.

## Problem 2: Student Record

Collects a student's name, age, course, and city into separate variables.

It demonstrates multiple values of different types and the use of descriptive variable names.

## Problem 3: Quotient and Remainder

Uses `divmod()` to obtain two related results from one operation.

The divisor must not be zero.

## Problem 4: Time Conversion

Converts total seconds into hours, minutes, and remaining seconds.

Integer division determines whole units, while modulo preserves the remainder.

## Problem 5: Minimum and Maximum

Uses `min()` and `max()` to retrieve the smaller and larger of two numeric values.

## Problem 6: Coordinates

Stores the x-coordinate and y-coordinate separately and then combines them into a tuple representation of a point.

## Problem 7: Split a Name

Uses string splitting to separate the first word of an entered name from the remaining text.

An empty input is handled separately.

## Problem 8: Rectangle Measurements

Defines a function that calculates both area and perimeter, returns them together, and unpacks the returned values.

## Problem 9: Total and Average Marks

Calculates the total and average of three entered marks and displays both results.

## Problem 10: Pair Names with Marks

Uses `zip()` to iterate over corresponding student names and marks.

## Problem 11: Divide an Amount

Uses `divmod()` to divide a non-negative amount into whole units and a remainder.

## Problem 12: Unpack Distance Conversions

Uses a function to calculate a distance in metres and centimetres, returning both results together.

# 18. Five Unsolved Practice Questions

Attempt the following independently.

## Question 1: Swap Three Variables

Given three values in `a`, `b`, and `c`, rotate them so that the old value of `b` becomes `a`, the old value of `c` becomes `b`, and the old value of `a` becomes `c`.

Example:

```text
Before: a = 1, b = 2, c = 3
After:  a = 2, b = 3, c = 1
```

**Hint:** Consider tuple assignment.

## Question 2: Unpack the First Three Values

Given a list containing at least three integers, assign its first three values to separate variables and display them.

**Hint:** Try list unpacking and think about what should happen when the list is too short.

## Question 3: Return Multiple Statistics

Write a function that receives three numbers and returns their minimum, maximum, and average.

**Hint:** Return the calculated values as a tuple and unpack the result.

## Question 4: Pair Prices with Quantities

Given equal-length lists of prices and quantities, calculate the cost of each item by multiplying the corresponding values.

**Hint:** Use `zip()` to process the related values together.

## Question 5: Starred Unpacking

Given a sequence containing at least four values, store its first and last values in individual variables and store the middle values in a list.

**Hint:** Use a starred target in an unpacking statement.

For each question, write a short algorithm, implement the solution, and test the expected behavior.

# 19. Common Errors and Debugging

## Error 1: Wrong Number of Values

Incorrect:

```python
first, second = 10, 20, 30
```

This produces a `ValueError` because the number of values does not match the number of targets.

**Solution:** Ensure the number of targets matches the number of values, or use starred unpacking when appropriate.

## Error 2: Incorrect Unpacking Order

```python
first, second = second, first
```

This is a correct swap in Python. However, replacing it with sequential assignments without a temporary variable may lose the original value.

**Solution:** Understand whether an assignment uses the original values or values that have already been overwritten.

## Error 3: Mismatched Collection Lengths

When related lists have different lengths, `zip()` stops at the shortest iterable by default.

**Solution:** Validate the lengths when equal-size collections are required.

## Error 4: Assuming Chained Assignment Creates Independent Objects

```python
first_list = second_list = []
```

Both names refer to the same list.

**Solution:** Create separate lists when independent mutation is intended.

## Error 5: Confusing a Tuple with Separate Return Values

A function that returns several comma-separated values returns a tuple in this context.

**Solution:** Understand the returned tuple and unpack it into names when separate values are needed.

## Error 6: Ignoring Empty Input

A function may need to handle an empty string or list before unpacking values.

**Solution:** Validate the number of values or provide suitable behavior for empty collections.

# 20. Best Practices

1. Use multiple assignment when it makes related values easier to read.
2. Use tuple or list unpacking when the order of values is clear.
3. Prefer descriptive target names.
4. Use tuple assignment for concise swaps.
5. Use `divmod()` for quotient-and-remainder calculations.
6. Use `zip()` for corresponding values from related iterables.
7. Validate collection lengths when required.
8. Use `enumerate()` when both index and value are needed.
9. Be careful with starred unpacking and variable-length sequences.
10. Avoid chained assignment with mutable objects when independent objects are intended.
11. Write a function that returns multiple related values when that improves the interface.
12. Test the unpacking behavior with edge cases.

# 21. Frequently Asked Questions

### Q1. What is multiple assignment?

It is assigning several values to several targets in one statement.

### Q2. What is chained assignment?

It assigns the same value or object to multiple target names, such as `a = b = 0`.

### Q3. What is unpacking?

Unpacking assigns elements from an iterable, such as a tuple or list, to separate variables.

### Q4. What is starred unpacking?

Starred unpacking uses `*` to collect a variable number of remaining values into a list.

### Q5. How can I swap two variables in Python?

Use `a, b = b, a`.

### Q6. Can a function return multiple values?

Yes. In the common form `return first, second`, Python returns a tuple containing the results.

### Q7. What does `zip()` do?

It iterates over corresponding elements from multiple iterables and stops at the shortest input by default.

### Q8. What does `enumerate()` do?

It produces index-value pairs while iterating over an iterable.

### Q9. What does `divmod()` return?

It returns a tuple containing the quotient and remainder according to Python's division rules.

### Q10. What should I study next?

Continue to `04_variable_swap`, where variable swapping is covered as a dedicated topic with additional practice.

# 22. How to Run the Program

Run the following command from the repository root:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\03_multiple_variables\03_multiple_variables.py"
```

The main menu provides:

```text
=================================================================
MULTIPLE VARIABLES IN PYTHON
=================================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View multiple variables checklist
0. Exit
Choose an option:
```

Choose an option and follow the prompts. The program retries invalid integer and floating-point inputs where the helper functions are used.

# 23. Folder Structure

```text
03_multiple_variables/
│
├── 03_multiple_variables.py
└── README.md
```

**`03_multiple_variables.py`** contains the twelve guided examples, twelve solved problems, five unsolved questions, checklist, and interactive menu.

**`README.md`** contains the topic theory, syntax examples, detailed explanations, test guidance, and revision notes.

# 24. Revision Checklist

Before moving to the next topic, confirm that you can:

- [ ] Assign multiple values in a single statement.
- [ ] Explain chained assignment.
- [ ] Unpack tuples and lists.
- [ ] Use starred unpacking.
- [ ] Swap two variables with and without a temporary variable.
- [ ] Return and unpack multiple function results.
- [ ] Use `zip()` with related collections.
- [ ] Use `enumerate()` to access index-value pairs.
- [ ] Use `divmod()` to calculate quotient and remainder.
- [ ] Recognize unpacking errors.
- [ ] Explain why chained assignment of mutable objects can be surprising.
- [ ] Complete the five unsolved practice questions.

## Completion Goal

By completing this topic, you should be able to assign, group, unpack, swap, and process multiple values confidently using Python.

**Next topic:** `04_variable_swap` — swapping variable values, temporary variables, tuple assignment, and practice problems.