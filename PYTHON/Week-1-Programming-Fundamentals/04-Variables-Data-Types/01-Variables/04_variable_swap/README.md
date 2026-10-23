# Variable Swapping in Python

**Week:** 1 — Programming Fundamentals  
**Part:** 4 — Variables and Data Types  
**Section:** Variables  
**Topic:** Variable Swapping  
**Language:** Python 3  
**Level:** Beginner

---

## Table of Contents

1. Introduction
2. Learning Objectives
3. What Is Variable Swapping?
4. Why Is Swapping Important?
5. Swapping with a Temporary Variable
6. Swapping with Tuple Assignment
7. Step-by-Step Comparison of Both Methods
8. A Common Incorrect Swapping Method
9. Swapping User-Entered Values
10. Swapping Strings and Other Values
11. Swapping List Elements
12. Swapping First and Last Elements
13. Swapping Minimum and Maximum Positions
14. Swapping Dictionary Values
15. Swapping Multiple Variables
16. Conditional Swapping
17. Explanation of the 12 Guided Examples
18. Explanation of the 12 Solved Problems
19. Five Unsolved Practice Questions
20. Testing and Edge Cases
21. Complexity Analysis
22. Common Mistakes
23. Best Practices
24. Frequently Asked Questions
25. How to Run the Program
26. Folder Structure
27. Revision Checklist

---

# 1. Introduction

Variable swapping is the process of exchanging the values associated with two or more variables.

Suppose two variables contain these values:

```python
first_value = 10
second_value = 20
```

After swapping, the values should be:

```text
first_value = 20
second_value = 10
```

Swapping is a fundamental programming operation used in arithmetic exercises, sorting algorithms, list manipulation, data rearrangement, and many algorithmic problems.

Python provides a convenient method for swapping values using tuple assignment, although the traditional temporary-variable method is also important for understanding the underlying logic.

This topic explains both methods and demonstrates how swapping can be applied to variables, lists, dictionaries, coordinates, and related collections.

# 2. Learning Objectives

After completing this topic, you should be able to:

- Explain what variable swapping means.
- Swap two variables using a temporary variable.
- Swap two variables using Python tuple assignment.
- Explain why a common incorrect swapping method fails.
- Trace the values of variables during a swap.
- Swap integers, floating-point values, and strings.
- Swap two list elements using their indices.
- Swap the first and last elements of a list.
- Swap the positions of minimum and maximum elements.
- Swap values associated with dictionary keys.
- Rotate multiple variable values.
- Use conditional swapping to arrange values.
- Validate list indices before performing a swap.
- Test swapping logic with appropriate edge cases.

# 3. What Is Variable Swapping?

Variable swapping means exchanging the values associated with two variable names.

Consider:

```python
a = 5
b = 9
```

Before swapping:

```text
a = 5
b = 9
```

After swapping:

```text
a = 9
b = 5
```

The original values have exchanged places.

### Mathematical Representation

Let the initial values be:

\[
a = 5,\qquad b = 9
\]

After swapping:

\[
a = 9,\qquad b = 5
\]

The values are exchanged, but the pair of values remains the same.

### Important Distinction

Swapping does not necessarily mean changing the values themselves. It means assigning the original values to different variables or positions.

For example, exchanging two strings or the references held by two variables follows the same basic idea as swapping two integers.

# 4. Why Is Swapping Important?

Swapping is used in many programming tasks.

## 4.1 Sorting Algorithms

Sorting algorithms may exchange elements to arrange values in a required order.

Example:

```text
Before: [30, 10]
After:  [10, 30]
```

## 4.2 Rearranging Lists

Swapping list elements allows values to move between positions without removing and reinserting elements.

## 4.3 Updating Related Values

A program may need to exchange two coordinates, two scores, or two positions in a data collection.

## 4.4 Iterative Algorithms

Some algorithms maintain multiple variables that must be updated together.

For example, Fibonacci generation commonly updates two related values using tuple assignment.

## 4.5 Learning Assignment Semantics

Swapping is an excellent way to understand how assignment, variable names, temporary storage, and Python's evaluation rules work.

# 5. Swapping with a Temporary Variable

A temporary variable preserves an original value while the other variables are updated.

### Example

```python
first_value = 10
second_value = 20

temporary_value = first_value
first_value = second_value
second_value = temporary_value

print(first_value)
print(second_value)
```

Output:

```text
20
10
```

### Algorithm

1. Assign `10` to `first_value`.
2. Assign `20` to `second_value`.
3. Save `first_value` in `temporary_value`.
4. Assign `second_value` to `first_value`.
5. Assign `temporary_value` to `second_value`.
6. Display both updated variables.

### Pseudocode

```text
START

    INPUT first_value
    INPUT second_value

    temporary_value = first_value
    first_value = second_value
    second_value = temporary_value

    OUTPUT first_value
    OUTPUT second_value

STOP
```

### Step-by-Step Trace Table

| Step | Statement | `first_value` | `second_value` | `temporary_value` |
|---:|---|---:|---:|---:|
| 1 | Initial values | 10 | 20 | — |
| 2 | Save first value | 10 | 20 | 10 |
| 3 | Copy second into first | 20 | 20 | 10 |
| 4 | Copy temporary into second | 20 | 10 | 10 |

Final result:

```text
first_value = 20
second_value = 10
```

### Why Is the Temporary Variable Necessary in This Method?

Without preserving the original value, an assignment may overwrite information that is needed for the next step.

The temporary variable provides a safe place to keep that original value until the exchange is complete.

# 6. Swapping with Tuple Assignment

Python allows two variable values to be exchanged in a single statement.

### Syntax

```python
a, b = b, a
```

### Example

```python
a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)
```

Output:

```text
Before: 10 20
After: 20 10
```

### How Does It Work?

Python evaluates the right-hand side before completing the assignments to the targets on the left.

In this example, the right-hand side produces the pair of original values `(20, 10)`. Those values are then unpacked into `a` and `b`.

As a result, the original value of `a` is not lost before it can be assigned to `b`.

This is the standard concise Python idiom for swapping two variables.

### Advantages

- Requires no explicitly named temporary variable.
- Expresses the exchange clearly.
- Works with many kinds of values.
- Makes the intended operation easy to recognize.

### Important Note

Tuple assignment does not make the referenced objects immutable. It changes which values the target names refer to.

For ordinary variable swapping, the statement is generally concise and readable.

# 7. Step-by-Step Comparison of Both Methods

Both methods can perform the same exchange.

| Feature | Temporary variable | Tuple assignment |
|---|---|---|
| Number of main statements | Three assignments | One assignment statement |
| Explicit temporary name | Yes | No |
| Suitable for beginner explanations | Very useful | Very useful |
| Standard Python idiom | Valid | Commonly preferred for simple swaps |
| Risk of overwriting a required original value | Avoided if written correctly | Avoided by Python's evaluation and unpacking behavior |

### Temporary-Variable Method

```python
a = 5
b = 8

temp = a
a = b
b = temp
```

### Tuple-Assignment Method

```python
a = 5
b = 8

a, b = b, a
```

Both produce:

```text
a = 8
b = 5
```

For Python programs, tuple assignment is usually the most concise way to swap two variables. The temporary-variable approach remains important for understanding the process and for translating swapping algorithms into other programming languages.

# 8. A Common Incorrect Swapping Method

Consider this code:

```python
a = 5
b = 10

a = b
b = a

print(a, b)
```

Output:

```text
10 10
```

This does not swap the values correctly.

### Why Does It Fail?

Initially:

```text
a = 5
b = 10
```

After `a = b`:

```text
a = 10
b = 10
```

The original value `5` is no longer available through either of these variable names.

The next assignment:

```python
b = a
```

copies `10` to `b`; it cannot restore the overwritten original value.

### Correct Solution Using a Temporary Variable

```python
a = 5
b = 10

temp = a
a = b
b = temp

print(a, b)
```

Output:

```text
10 5
```

### Correct Solution Using Tuple Assignment

```python
a = 5
b = 10

a, b = b, a

print(a, b)
```

Output:

```text
10 5
```

The main lesson is that a swap must preserve both original values until the exchange has been completed.

# 9. Swapping User-Entered Values

The same methods work when values come from user input.

Example:

```python
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("Before swapping:", first_number, second_number)

first_number, second_number = second_number, first_number

print("After swapping:", first_number, second_number)
```

Possible input:

```text
Enter first number: 15
Enter second number: 25
```

Output:

```text
Before swapping: 15 25
After swapping: 25 15
```

The program reads the values, performs the exchange, and displays the new order.

If a program expects integers, it should also consider what to do when a user enters non-integer text.

The supplied Python file includes an input helper that retries when integer input is invalid.

# 10. Swapping Strings and Other Values

The tuple-assignment method is not restricted to numeric values.

Example:

```python
first_name = "Amaan"
second_name = "Sara"

first_name, second_name = second_name, first_name

print(first_name)
print(second_name)
```

Output:

```text
Sara
Amaan
```

The same basic assignment works with floats and other objects.

### Swapping Variables That Refer to Lists

```python
first_list = [1, 2, 3]
second_list = [10, 20, 30]

first_list, second_list = second_list, first_list
```

After this statement, each variable name refers to the list previously associated with the other name.

The lists themselves have not been exchanged element by element; the references held by the variable names have changed.

This distinction matters when learning the difference between swapping variable references and swapping elements inside a collection.

# 11. Swapping List Elements

Swapping variables and swapping list elements are related but different operations.

Given:

```python
numbers = [10, 20, 30, 40]
```

The variable `numbers` continues to refer to the list, but two elements within the list can be exchanged.

### Swap Two Positions

```python
numbers[0], numbers[2] = numbers[2], numbers[0]

print(numbers)
```

Output:

```text
[30, 20, 10, 40]
```

Index `0` contained `10`, and index `2` contained `30`. After the exchange, their positions are reversed.

### General Algorithm

1. Read or create a list.
2. Identify the two required indices.
3. Check that both indices are valid.
4. Exchange the two elements.
5. Display the updated list.

### Pseudocode

```text
INPUT numbers
INPUT first_index
INPUT second_index

IF both indices are valid
    numbers[first_index], numbers[second_index] =
        numbers[second_index], numbers[first_index]
    OUTPUT numbers
ELSE
    OUTPUT "Invalid index"
END IF
```

The exact pseudocode formatting may vary, but the validation and exchange operations should be clear.

### Why Index Validation Matters

For a list of length `4`, the valid positive indices are `0`, `1`, `2`, and `3`.

Trying to access an index outside that range raises an `IndexError`.

# 12. Swapping First and Last Elements

The first element of a non-empty list is at index `0`. The last element can be accessed using index `-1`.

Example:

```python
numbers = [5, 10, 15, 20, 25]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)
```

Output:

```text
[25, 10, 15, 20, 5]
```

### Edge Cases

- An empty list has no first or last element.
- A single-element list has no distinct pair of endpoints to exchange.
- A list containing two elements will have both elements exchanged.

A robust program should define its behavior for empty or one-element lists rather than assuming that a swap is always possible.

# 13. Swapping Minimum and Maximum Positions

A common list problem asks you to exchange the positions of the smallest and largest values.

Example:

```text
Original list: [8, 3, 12, 5, 1]
Minimum value: 1
Maximum value: 12
```

The minimum appears at index `4` and the maximum at index `2`.

After swapping those positions:

```text
Updated list: [8, 3, 1, 5, 12]
```

### Python

```python
numbers = [8, 3, 12, 5, 1]

minimum_index = numbers.index(min(numbers))
maximum_index = numbers.index(max(numbers))

numbers[minimum_index], numbers[maximum_index] = (
    numbers[maximum_index],
    numbers[minimum_index],
)

print(numbers)
```

### Duplicate Minimums or Maximums

The `index()` method returns the first occurrence of a value.

Therefore, this example swaps the first occurrence of the minimum and the first occurrence of the maximum.

If a problem specifies a different rule for duplicates, implement that rule explicitly.

# 14. Swapping Dictionary Values

A dictionary stores key-value pairs. Two values associated with different keys can also be exchanged.

Example:

```python
student_record = {
    "first_mark": 75,
    "second_mark": 90,
}

student_record["first_mark"], student_record["second_mark"] = (
    student_record["second_mark"],
    student_record["first_mark"],
)

print(student_record)
```

Output:

```text
{'first_mark': 90, 'second_mark': 75}
```

The keys remain the same, but their associated values are exchanged.

This operation can be useful when reorganizing records or moving values between known fields.

Before swapping dictionary values, ensure the required keys exist. Otherwise, accessing a missing key can raise a `KeyError`.

# 15. Swapping Multiple Variables

Tuple assignment can exchange more than two variable values at a time.

Example: Rotate three values to the left.

```python
a = "A"
b = "B"
c = "C"

a, b, c = b, c, a

print(a, b, c)
```

Output:

```text
B C A
```

The old value of `b` becomes the new value of `a`, the old value of `c` becomes the new value of `b`, and the old value of `a` becomes the new value of `c`.

This is a cyclic rotation of variable values.

### Difference Between Swapping and Rotation

A swap normally exchanges two values.

A rotation rearranges three or more values according to a specified sequence.

Both operations can use multiple assignment, but their intended final arrangements are different.

# 16. Conditional Swapping

Sometimes values should be exchanged only when a condition is satisfied.

For example, to arrange two integers in ascending order:

```python
first_number = 25
second_number = 10

if first_number > second_number:
    first_number, second_number = second_number, first_number

print(first_number, second_number)
```

Output:

```text
10 25
```

If the first number is already smaller than or equal to the second, the condition is false and no swap occurs.

### Algorithm

1. Read two values.
2. Compare them.
3. If the first value is greater, exchange the values.
4. Display the values in ascending order.

This pattern introduces a simple form of conditional reordering and is useful for understanding more involved sorting algorithms.

# 17. Explanation of the 12 Guided Examples

The Python program contains twelve guided examples.

| No. | Example | Main concept |
|---:|---|---|
| 1 | Temporary-variable swap | Preserve the original value |
| 2 | Tuple-assignment swap | Exchange two variables in one statement |
| 3 | Trace a swap | Track values after every step |
| 4 | Swap input integers | Work with user-provided values |
| 5 | Swap strings | Exchange non-numeric values |
| 6 | Swap list variables | Exchange the references held by names |
| 7 | Swap list elements | Exchange elements by index |
| 8 | Swap endpoints | Exchange first and last elements |
| 9 | Swap dictionary values | Exchange values under two keys |
| 10 | Swap coordinates | Exchange two related measurements |
| 11 | Rotate three values | Reassign multiple values simultaneously |
| 12 | Incorrect swapping method | Understand why overwriting a value fails |

When studying an example, predict the output first, run it, and compare the result with your prediction.

# 18. Explanation of the 12 Solved Problems

## Problem 1: Swap Two Integers

Reads two integers and exchanges them using tuple assignment.

The result demonstrates the basic swapping operation with input.

## Problem 2: Swap Two Strings

Exchanges two text values using the same tuple-assignment technique.

It demonstrates that swapping is not limited to numbers.

## Problem 3: Swap Two Decimal Numbers

Reads two floating-point values and swaps them. The operation changes the order of the variable references, not the underlying numerical values.

## Problem 4: Swap List Elements by Index

Reads a list and two zero-based indices, validates the indices, and swaps the corresponding elements.

## Problem 5: Swap First and Last Elements

Exchanges the endpoints of a list. The program requires at least two elements.

## Problem 6: Swap Minimum and Maximum Positions

Finds the first index of the minimum and maximum values, then exchanges the values at those positions.

## Problem 7: Swap Dictionary Values

Swaps the values stored under `morning_score` and `evening_score`, leaving the keys unchanged.

## Problem 8: Swap Coordinates

Reads two coordinates and exchanges their values. It demonstrates multiple assignment with floating-point numbers.

## Problem 9: Rotate Three Values

Rotates three entered text values to the left, demonstrating how tuple assignment can reassign several variables at once.

## Problem 10: Swap Student Records

Maintains two parallel lists containing student names and marks. It exchanges both lists' values at the selected indices so each student's mark remains associated with that student.

This example illustrates why related collections must be updated consistently.

## Problem 11: Swap Adjacent Pairs

Exchanges elements at positions `(0, 1)`, `(2, 3)`, and so on.

If the list has an odd number of values, the final unpaired value stays in place.

## Problem 12: Sort Two Values with a Conditional Swap

Compares two integers and swaps them only if the first is greater than the second.

The output is therefore in ascending order.

# 19. Five Unsolved Practice Questions

Attempt the following problems independently.

## Question 1: Rotate Three Variables to the Right

Given values `a`, `b`, and `c`, rotate their values so that the new order is `c`, `a`, and `b`.

Example:

```text
Before: A B C
After:  C A B
```

**Hint:** Carefully map the original values to their final destinations.

## Question 2: Swap Adjacent Pairs

Given a list of integers, swap each pair starting at index `0`.

Example:

```text
Input:  [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
```

The final element remains unchanged when no partner is available.

## Question 3: Swap First and Middle Elements

Given a list with at least three elements and an odd number of elements, exchange the first element with the middle element.

Test this on lists of different odd lengths.

## Question 4: Swap Two Words in a List

Read a list of words and two zero-based indices, then exchange the words at those positions.

Make sure your program handles invalid indices.

## Question 5: Conditional Swap

Read two numbers and exchange them only when the first is smaller than the second.

Test values where the first is greater, smaller, and equal to the second.

For every exercise, write an algorithm first, implement it, and test multiple cases.

# 20. Testing and Edge Cases

A correct swapping algorithm should be checked against several cases.

| Case | Example | Expected behavior |
|---|---|---|
| Different values | `10`, `20` | Values exchange places |
| Equal values | `5`, `5` | Visible values remain unchanged |
| Negative values | `-3`, `8` | Values exchange places |
| Zero | `0`, `10` | Values exchange places |
| Empty list | `[]` | A list-element swap cannot be performed |
| Single-element list | `[7]` | No distinct elements to exchange |
| Same index | Index `1`, index `1` | List remains unchanged |
| Invalid index | Index `10` in a short list | Input should be rejected |

Additional considerations:

- Duplicate minimum or maximum values require a clear selection rule.
- Related collections must remain aligned when records are swapped.
- Dictionary keys must exist before accessing them.
- Inputs must match the data type expected by the program.

# 21. Complexity Analysis

For ordinary variable swapping, the amount of work does not grow with input size.

### Swapping Two Variables

```python
a, b = b, a
```

- Time complexity: `O(1)`.
- Auxiliary space: `O(1)` in the usual algorithmic analysis.

### Swapping Two List Elements

```python
numbers[i], numbers[j] = numbers[j], numbers[i]
```

The number of element positions involved is fixed.

- Time complexity: `O(1)`.
- Auxiliary space: `O(1)` for the swap operation, excluding the existing list.

### Finding and Swapping Minimum and Maximum Positions

The implementation scans the list to identify the minimum and maximum positions.

- Time complexity: `O(n)` for a list of `n` elements.
- Auxiliary space: `O(1)` additional space for the tracked indices and values.

The swapping operation itself is constant-time in these examples; locating the elements may require additional work.

# 22. Common Mistakes

## Mistake 1: Overwriting a Value

Incorrect:

```python
a = b
b = a
```

The first assignment loses the original value of `a`.

**Solution:** Use a temporary variable or tuple assignment.

## Mistake 2: Using Invalid List Indices

An index outside a list's valid range raises an error.

**Solution:** Validate the indices before swapping elements.

## Mistake 3: Swapping Only Part of a Record

When names and marks are stored in separate lists, swapping names without swapping their associated marks can corrupt the relationship between the records.

**Solution:** Exchange all corresponding fields consistently, or consider using a more suitable record structure.

## Mistake 4: Assuming an Empty List Has Endpoints

An empty list does not have a first or last element.

**Solution:** Check the list length.

## Mistake 5: Confusing Rotation with Swapping

A two-value swap and a three-value rotation have different final arrangements.

**Solution:** Write down the required final values before implementing the assignment.

## Mistake 6: Assuming a Temporary Variable Is Always Necessary in Python

Python provides tuple assignment for concise swaps.

**Solution:** Understand both methods and use the one that communicates the logic most clearly.

# 23. Best Practices

1. Prefer tuple assignment for simple Python swaps.
2. Learn the temporary-variable method to understand value preservation.
3. Validate indices when swapping collection elements.
4. Test equal and negative values where applicable.
5. Define the expected behavior of empty and small lists.
6. Keep related data fields aligned during a swap.
7. Use descriptive names for values and indices.
8. Trace the original and final states when debugging.
9. Do not use sequential assignments that overwrite a needed value.
10. Distinguish variable swapping from list-element swapping and cyclic rotation.

# 24. Frequently Asked Questions

### Q1. What is variable swapping?

Variable swapping is exchanging the values associated with two or more variables.

### Q2. Why is a temporary variable useful?

It preserves an original value while the other variable is updated.

### Q3. How do I swap two variables in Python?

Use tuple assignment:

```python
a, b = b, a
```

### Q4. Can I swap strings?

Yes. Tuple assignment works with strings and many other object types.

### Q5. Can I swap elements inside a list?

Yes. Use their indices:

```python
numbers[i], numbers[j] = numbers[j], numbers[i]
```

The indices must be valid.

### Q6. What is the difference between swapping variables and swapping list elements?

Swapping variables changes which values their names refer to. Swapping list elements changes values at particular positions inside a list.

### Q7. Can I swap three variables at once?

Yes. Multiple assignment can rotate several variable values according to a specified order.

### Q8. What happens if both values are equal?

Swapping them leaves their visible values unchanged.

### Q9. Is tuple assignment better than a temporary variable?

For a simple swap in Python, tuple assignment is concise and idiomatic. The temporary-variable method is still useful for learning and for understanding how swapping can be implemented in languages with different assignment capabilities.

### Q10. What should I study next?

After completing this folder, proceed to the Data Types section and begin with the `int` topic.

# 25. How to Run the Program

From the repository root, run:

```powershell
python "PYTHON\Week-1-Programming-Fundamentals\04-Variables-Data-Types\01-Variables\04_variable_swap\04_variable_swap.py"
```

The program provides the following menu:

```text
=================================================================
VARIABLE SWAPPING IN PYTHON
=================================================================
1. Explore 12 guided examples
2. Practise 12 solved problems
3. View 5 unsolved questions
4. View swapping checklist
0. Exit
Choose an option:
```

Choose an option and follow the prompts. The program retries invalid integer and floating-point input where the relevant helper functions are used.

# 26. Folder Structure

```text
04_variable_swap/
│
├── 04_variable_swap.py
└── README.md
```

**`04_variable_swap.py`** contains the runnable guided examples, solved problems, unsolved questions, checklist, and interactive menus.

**`README.md`** contains the detailed theory, algorithms, pseudocode, dry-run tables, explanations, complexity analysis, and revision notes.

# 27. Revision Checklist

Before moving on, confirm that you can:

- [ ] Explain variable swapping.
- [ ] Swap values using a temporary variable.
- [ ] Swap values using tuple assignment.
- [ ] Explain why the incorrect sequential method fails.
- [ ] Swap integers, floats, and strings.
- [ ] Swap list elements by index.
- [ ] Swap the first and last elements of a list.
- [ ] Swap minimum and maximum positions.
- [ ] Swap dictionary values under two keys.
- [ ] Rotate three variable values.
- [ ] Perform a conditional swap.
- [ ] Validate indices and list lengths.
- [ ] Explain the expected result before running the code.
- [ ] Attempt all five unsolved questions.

## Completion Goal

By completing this topic, you should understand how to exchange variable values safely, apply swapping to collections, trace changes step by step, and use Python's tuple-assignment syntax confidently.

**Next topic:** Begin the `02-Data-Types` section with `01_int`, which introduces integers and whole-number operations in Python.