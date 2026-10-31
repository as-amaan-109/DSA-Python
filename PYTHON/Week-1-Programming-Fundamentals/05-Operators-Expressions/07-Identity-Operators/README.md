# Python Identity Operators

**Topic:** Python Programming Fundamentals  
**Folder:** `07-Identity-Operators`  
**Python File:** `01_identity_operators.py`  
**Level:** Beginner to Intermediate

---

# 1. Introduction to Identity Operators

Identity operators are used to check whether two variables refer to the same object in Python.

In simple words, identity operators answer the following question:

**Are these two variables pointing to the exact same object?**

Python provides two identity operators:

| Operator | Name | Purpose |
|---|---|---|
| `is` | Identity operator | Checks whether two references point to the same object |
| `is not` | Non-identity operator | Checks whether two references point to different objects |

Identity operators return Boolean results:

- `True` — when the identity condition is satisfied.
- `False` — when the identity condition is not satisfied.

### Real-Life Example

Imagine that you have created a student record:

```python
student = {
    "name": "Amaan",
    "age": 22
}
```

Now you create another variable that refers to the same dictionary:

```python
another_student = student
```

Both variables refer to the same dictionary object.

```python
print(student is another_student)
```

**Output:**

```text
True
```

The result is `True` because both variables refer to the same object.

### Another Example

Now create two separate dictionaries with the same data:

```python
student1 = {
    "name": "Amaan",
    "age": 22
}

student2 = {
    "name": "Amaan",
    "age": 22
}

print(student1 == student2)
print(student1 is student2)
```

**Output:**

```text
True
False
```

Why?

- `==` checks whether the values are equal.
- `is` checks whether both references point to the same object.

Both dictionaries have equal contents, but they are separate objects.

This difference is the most important concept in identity operators.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand identity operators.
2. Identify the `is` operator.
3. Identify the `is not` operator.
4. Understand object identity.
5. Understand the difference between equality and identity.
6. Compare two object references.
7. Understand Python object references.
8. Understand object aliasing.
9. Understand mutable and immutable objects.
10. Understand how list references work.
11. Understand list copying.
12. Understand dictionary references.
13. Compare separate dictionary objects.
14. Check whether a variable is `None`.
15. Check whether a variable is not `None`.
16. Understand Python's `None` singleton.
17. Understand sentinel objects.
18. Understand identity with custom classes.
19. Understand identity through function returns.
20. Understand how functions return `None`.
21. Learn about the `id()` function.
22. Avoid incorrect uses of `is`.
23. Understand common identity-related errors.
24. Complete all 12 solved programming problems.
25. Attempt all 10 unsolved practice questions.

---

# 3. Prerequisites

Before learning identity operators, you should understand these basic Python concepts.

| Concept | Why It Is Required |
|---|---|
| Variables | To store references to objects |
| Data types | To understand different Python objects |
| Lists | To understand mutable objects |
| Tuples | To understand immutable collections |
| Dictionaries | To understand key-value objects |
| Functions | To understand returned objects |
| Conditional statements | To perform identity-based checks |
| `None` | To represent the absence of a value |
| `==` operator | To understand value equality |
| Object references | To understand identity |

You do not need advanced object-oriented programming knowledge to start this topic. Basic knowledge of variables, lists, and dictionaries is sufficient.

---

# 4. What Are Identity Operators?

Identity operators check whether two variables refer to the same object.

### General Syntax

```python
object1 is object2
```

This expression checks whether `object1` and `object2` refer to the same object.

Similarly:

```python
object1 is not object2
```

This expression checks whether they refer to different objects.

### Example

```python
first = [10, 20, 30]

second = first

print(first is second)
```

**Output:**

```text
True
```

### Explanation Step by Step

**Step 1:** Create a list.

```python
first = [10, 20, 30]
```

Python creates a list object.

**Step 2:** Assign `first` to `second`.

```python
second = first
```

This does not create another list.

Instead, both variable names refer to the same list.

**Step 3:** Check object identity.

```python
first is second
```

Because both references point to the same object, the result is `True`.

### Visual Representation

```text
        first
          |
          |
          v
     +-----------+
     | 10        |
     | 20        |
     | 30        |
     +-----------+
          ^
          |
          |
        second
```

Both variables point to one list object.

### Important Point

Identity operators compare objects, not merely the values stored inside those objects.

---

# 5. Types of Identity Operators

Python provides two identity operators.

## 5.1 `is` Operator

The `is` operator checks whether two references point to the same object.

### Syntax

```python
object1 is object2
```

### Example

```python
first_list = [10, 20, 30]

second_list = first_list

print(first_list is second_list)
```

**Output:**

```text
True
```

### Explanation

1. A list is created.
2. A second variable refers to the first list.
3. Both variables reference the same object.
4. The `is` operator returns `True`.

### Practical Use

The most common recommended use of `is` is checking whether a value is `None`.

```python
username = None

if username is None:
    print("Username is not provided")
```

**Output:**

```text
Username is not provided
```

## 5.2 `is not` Operator

The `is not` operator checks whether two references point to different objects.

### Syntax

```python
object1 is not object2
```

### Example

```python
first_list = [10, 20, 30]

second_list = [10, 20, 30]

print(first_list is not second_list)
```

**Output:**

```text
True
```

### Explanation

Both lists contain the same elements, but Python created two separate list objects.

Therefore, the identity condition is `True`.

### Practical Use

```python
username = "Amaan"

if username is not None:
    print("Username is available")
else:
    print("Username is missing")
```

**Output:**

```text
Username is available
```

---

# 6. Difference Between `is` and `==`

This is the most important concept in identity operators.

Python provides different operators for comparing identity and equality.

| Operator | Purpose |
|---|---|
| `==` | Checks whether values are equal |
| `!=` | Checks whether values are not equal |
| `is` | Checks whether references point to the same object |
| `is not` | Checks whether references point to different objects |

### Example 1: Equal Values, Different Objects

```python
first = [10, 20, 30]

second = [10, 20, 30]

print(first == second)
print(first is second)
```

**Output:**

```text
True
False
```

### Explanation

The first expression:

```python
first == second
```

Checks the values inside both lists.

Because their contents are equal, the result is `True`.

The second expression:

```python
first is second
```

Checks whether both variables point to the same list object.

They do not, so the result is `False`.

### Example 2: Same Object

```python
first = [10, 20, 30]

second = first

print(first == second)
print(first is second)
```

**Output:**

```text
True
True
```

Both expressions return `True`, but for different reasons:

- `==` returns `True` because the values are equal.
- `is` returns `True` because both references point to the same object.

### Example 3: Different Values and Different Objects

```python
first = [10, 20, 30]

second = [40, 50, 60]

print(first == second)
print(first is second)
```

**Output:**

```text
False
False
```

Both the values and the object identities are different.

### Comparison Table

| Situation | `==` | `is` |
|---|---|---|
| Same object | `True` | `True` |
| Different lists with equal values | `True` | `False` |
| Different lists with different values | `False` | `False` |

### Remember

Use `==` for normal value comparison.

Use `is` when checking object identity.

Use `is None` and `is not None` for `None` checks.

---

# 7. Understanding Objects and References

To understand identity operators properly, you need to understand how variables work in Python.

Python variables are names that refer to objects.

For example:

```python
name = "Amaan"
age = 22
```

Here:

- `name` refers to a string object.
- `age` refers to an integer object.

The variable itself is not the object. It is a reference to the object.

### Example

```python
numbers = [10, 20, 30]

another_reference = numbers

print(numbers)
print(another_reference)
```

**Output:**

```text
[10, 20, 30]
[10, 20, 30]
```

Both variables refer to the same list.

### Visual Explanation

```text
numbers ------------+
                    |
                    v
              +-----------+
              |    10     |
              |    20     |
              |    30     |
              +-----------+
                    ^
                    |
another_reference --+
```

### Why Is This Important?

When multiple variables reference the same mutable object, modifying that object through one reference is visible through the other reference.

This is called aliasing.

---

# 8. Understanding Object Aliasing

Aliasing occurs when multiple variable names refer to the same object.

### Example

```python
original = [10, 20, 30]

alias = original

print(original is alias)
```

**Output:**

```text
True
```

Both references point to the same list.

### Modifying an Alias

```python
original = [10, 20, 30]

alias = original

alias.append(40)

print("Original:", original)
print("Alias:", alias)
```

**Output:**

```text
Original: [10, 20, 30, 40]
Alias: [10, 20, 30, 40]
```

### Step-by-Step Explanation

1. Create a list named `original`.
2. Assign `original` to `alias`.
3. Both variables refer to the same list.
4. Append `40` through `alias`.
5. The shared list is modified.
6. Printing `original` also shows `40`.

### Identity Check

```python
print(original is alias)
```

Output:

```text
True
```

### Real-Life Example

Imagine two people sharing access to the same document.

If one person edits the document, the other person sees the updated version.

Similarly, when two variables reference the same mutable Python object, a change made through one reference can be observed through the other.

---

# 9. Identity with Mutable Objects

Mutable objects can be changed after creation.

Examples include:

- Lists.
- Dictionaries.
- Sets.
- Many custom class instances.

### Example with a List

```python
first = [10, 20, 30]

second = first

second.append(40)

print(first)
print(second)

print(first is second)
```

**Output:**

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
True
```

### Explanation

Both variables refer to the same list.

The list changes when an element is appended through `second`.

### Example with a Dictionary

```python
student = {
    "name": "Amaan",
    "age": 22
}

another_reference = student

another_reference["course"] = "Python"

print(student)
print(another_reference)

print(student is another_reference)
```

**Output:**

```text
{'name': 'Amaan', 'age': 22, 'course': 'Python'}
{'name': 'Amaan', 'age': 22, 'course': 'Python'}
True
```

### Important Point

An assignment such as:

```python
second = first
```

does not copy a list or dictionary.

It creates another reference to the same object.

---

# 10. Identity with Immutable Objects

Immutable objects cannot be changed after they are created.

Common immutable types include:

- Integers.
- Floating-point numbers.
- Strings.
- Tuples.
- Booleans.
- `NoneType`.

### Example with Strings

```python
first = "Python"

second = first

print(first == second)
print(first is second)
```

The equality result is `True`, and the identity result is also `True` because `second` refers to the object referenced by `first`.

### Important Warning

Do not depend on the identity behavior of separate immutable values.

For example:

```python
a = 1000
b = 1000

print(a == b)
```

The equality result is `True`.

However, you should not use assumptions about object reuse or memory optimization to decide whether two independently created values are identical.

Python implementations may reuse or cache some immutable objects, but that behavior is not a substitute for value comparison.

### Correct Practice

```python
a = 1000
b = 1000

print(a == b)
```

Use `==` when your requirement is to compare numerical values.

Do not use `is` for numerical equality.

---

# 11. Identity Operators with Lists

Lists are mutable objects.

Identity operators can help determine whether two variables refer to the same list.

### Example 1: Same Reference

```python
first = [10, 20, 30]

second = first

print(first is second)
```

**Output:**

```text
True
```

### Example 2: Separate Lists

```python
first = [10, 20, 30]

second = [10, 20, 30]

print(first == second)
print(first is second)
```

**Output:**

```text
True
False
```

### Example 3: Copying a List

```python
original = [10, 20, 30]

copied = original.copy()

print(original == copied)
print(original is copied)
```

**Output:**

```text
True
False
```

### Explanation

The `copy()` method creates a new outer list.

The copied list contains equal elements, but it is a different object.

### Shallow Copy Important Note

A list's `.copy()` method makes a shallow copy.

That means nested objects are not recursively copied.

Example:

```python
original = [[10, 20], [30, 40]]

copied = original.copy()

print(original is copied)
print(original[0] is copied[0])
```

**Output:**

```text
False
True
```

The outer lists are separate objects, but their inner lists are shared.

This is an important concept for advanced Python programming.

---

# 12. Identity Operators with Dictionaries

Dictionaries are mutable collections of key-value pairs.

Identity operators can compare references to dictionary objects.

### Example 1: Same Dictionary Reference

```python
student = {
    "name": "Amaan",
    "age": 22
}

another_reference = student

print(student is another_reference)
```

**Output:**

```text
True
```

### Example 2: Different Dictionaries

```python
first = {
    "name": "Amaan",
    "age": 22
}

second = {
    "name": "Amaan",
    "age": 22
}

print(first == second)
print(first is second)
```

**Output:**

```text
True
False
```

### Example 3: Dictionary Copy

```python
original = {
    "name": "Amaan",
    "course": "Python"
}

copied = original.copy()

print(original == copied)
print(original is copied)
```

**Output:**

```text
True
False
```

### Important Difference

Dictionary equality compares key-value contents.

Dictionary identity checks whether both variables refer to the same dictionary object.

---

# 13. The `None` Value in Python

`None` is a special Python object that represents the absence of a value.

Its data type is `NoneType`.

### Example

```python
result = None

print(result)
print(type(result))
```

**Output:**

```text
None
<class 'NoneType'>
```

### Why Is `None` Used?

`None` is commonly used to represent:

- A missing value.
- An optional value.
- An uninitialized result.
- A function that has no meaningful return value.
- The absence of a result.

### Example: An Optional Username

```python
username = None

if username is None:
    print("Username was not provided")
else:
    print("Username:", username)
```

**Output:**

```text
Username was not provided
```

### Important Point

`None` is a singleton object in Python.

There is one `None` object, so identity checking is appropriate:

```python
value = None

print(value is None)
```

**Output:**

```text
True
```

---

# 14. Checking `None` with `is`

The recommended way to check whether a variable is `None` is:

```python
value is None
```

### Example 1

```python
username = None

if username is None:
    print("No username")
else:
    print("Username:", username)
```

**Output:**

```text
No username
```

### Example 2

```python
result = None

if result is None:
    print("Result is missing")
```

### Why Use `is None` Instead of `== None`?

`None` has a unique identity.

Therefore, identity checking expresses the intended condition directly.

Preferred:

```python
if value is None:
    print("No value")
```

Less preferred:

```python
if value == None:
    print("No value")
```

Use `is None` in normal Python code.

### Important Distinction

`None` is different from:

| Value | Meaning |
|---|---|
| `None` | Absence of a value |
| `0` | Integer zero |
| `False` | Boolean false |
| `""` | Empty string |
| `[]` | Empty list |
| `{}` | Empty dictionary |
| `()` | Empty tuple |

These values must not be confused with one another.

---

# 15. Checking `None` with `is not`

The `is not` operator can check whether a variable contains an object other than `None`.

### Example

```python
username = "Amaan"

if username is not None:
    print("Username is provided")
else:
    print("Username is missing")
```

**Output:**

```text
Username is provided
```

### Another Example

```python
age = None

if age is not None:
    print("Age:", age)
else:
    print("Age is not available")
```

**Output:**

```text
Age is not available
```

### Practical Example: Optional User Input

```python
def get_username():
    username = input("Enter username: ").strip()

    if username == "":
        return None

    return username


username = get_username()

if username is not None:
    print("Welcome", username)
else:
    print("No username was entered")
```

Here, the function returns `None` when the user does not enter a username.

The calling code uses `is not None` to distinguish the missing value from an actual username.

---

# 16. Difference Between `None`, `False`, and Empty Values

This is a common source of beginner mistakes.

### Example

```python
a = None
b = False
c = 0
d = ""
e = []

print(a is None)
print(b is None)
print(c is None)
print(d is None)
print(e is None)
```

**Output:**

```text
True
False
False
False
False
```

Only `a` is `None`.

### Truthiness Is Different from Identity

The following values are considered falsy:

- `None`
- `False`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`
- `()`

Example:

```python
values = [None, False, 0, "", [], {}, set(), ()]

for value in values:
    print(value, bool(value), value is None)
```

The `bool()` result and the identity result are different kinds of checks.

### Important Example

```python
value = 0

if value is None:
    print("Missing")
else:
    print("A value exists:", value)
```

**Output:**

```text
A value exists: 0
```

This is useful because zero can be a valid numerical value.

### Common Mistake

Do not automatically replace:

```python
if value is None:
```

with:

```python
if not value:
```

The second condition also treats zero, empty strings, and empty collections as false.

Choose the condition according to the meaning you need.

---

# 17. Understanding the `id()` Function

Python provides a built-in function called `id()`.

The function returns an integer that identifies an object during its lifetime.

### Syntax

```python
id(object)
```

### Example

```python
first = [10, 20, 30]

second = first

print(id(first))
print(id(second))
```

Both expressions return the same identity value because both variables refer to the same object.

### Example with Separate Lists

```python
first = [10, 20, 30]

second = [10, 20, 30]

print(id(first))
print(id(second))
```

The identity values will be different while both list objects exist.

### Comparing IDs

```python
first = [10, 20, 30]

second = first

print(id(first) == id(second))
print(first is second)
```

**Output:**

```text
True
True
```

### Important Rules About `id()`

1. It returns an integer.
2. The returned identity is unique among objects that exist simultaneously.
3. An object's identity remains unchanged throughout its lifetime.
4. Identity values may be reused after an object is destroyed.
5. The exact representation of the identity is implementation-dependent.

### Important Warning

Do not use `id()` as a replacement for `is`.

For identity comparisons, write:

```python
first is second
```

rather than:

```python
id(first) == id(second)
```

The `is` operator directly expresses the identity check.

---

# 18. Understanding the `object()` Function

Python provides the built-in `object()` constructor.

It creates a new base object.

### Example

```python
first = object()

second = object()

print(first is second)
```

**Output:**

```text
False
```

Each call to `object()` creates a new object.

### Why Is This Useful?

The `object()` constructor is useful when creating sentinel objects.

A sentinel is a unique object used to represent a special state.

For example, an application might need to distinguish between:

1. A value was not supplied.
2. A value was explicitly supplied as `None`.

A unique sentinel can represent the first state.

---

# 19. Sentinel Objects

A sentinel object is a unique object used as a special marker.

### Example

```python
MISSING = object()

value = MISSING

if value is MISSING:
    print("Value was not supplied")
else:
    print("Value:", value)
```

**Output:**

```text
Value was not supplied
```

### Why Not Always Use `None`?

Sometimes `None` is itself a valid user-supplied value.

For example, an application might need to distinguish:

- No argument was supplied.
- The user explicitly supplied `None`.

A unique sentinel can distinguish those cases.

### Example

```python
MISSING = object()

def display_value(value=MISSING):

    if value is MISSING:
        print("No argument was supplied")

    elif value is None:
        print("The supplied value is None")

    else:
        print("Value:", value)


display_value()
display_value(None)
display_value(100)
```

**Output:**

```text
No argument was supplied
The supplied value is None
Value: 100
```

### Explanation

| Function Call | Meaning |
|---|---|
| `display_value()` | Argument not supplied |
| `display_value(None)` | Explicitly supplied `None` |
| `display_value(100)` | Normal value supplied |

### Why Use `is`?

The sentinel is a unique object.

Checking:

```python
value is MISSING
```

is an appropriate identity comparison.

---

# 20. Identity Operators with Functions

Functions can return objects.

Identity operators can determine whether a function returns the exact object passed to it.

### Example

```python
def return_same_object(value):
    return value


numbers = [10, 20, 30]

result = return_same_object(numbers)

print(result is numbers)
```

**Output:**

```text
True
```

### Explanation

1. A list is created.
2. The list is passed to the function.
3. The function returns the same object.
4. The result variable receives a reference to that object.
5. Identity checking returns `True`.

### Returning a Copy

```python
def return_copy(value):
    return value.copy()


numbers = [10, 20, 30]

result = return_copy(numbers)

print(result == numbers)
print(result is numbers)
```

**Output:**

```text
True
False
```

The function returns a separate list with equal values.

### Why Is This Important?

Understanding identity with functions helps when working with:

- Mutable arguments.
- Object copying.
- Data processing functions.
- Shared state.
- Custom objects.
- APIs that return references to existing objects.

---

# 21. Identity of Functions Returning `None`

In Python, a function that does not explicitly return a value returns `None`.

### Example

```python
def display_message():
    print("Hello Python")


result = display_message()

print(result)
print(result is None)
```

**Output:**

```text
Hello Python
None
True
```

### Explanation

The function prints a message.

However, it does not contain a `return` statement.

Python therefore returns `None` implicitly.

### Another Example

```python
def add_numbers(a, b):
    result = a + b
    print(result)


answer = add_numbers(10, 20)

print(answer is None)
```

**Output:**

```text
30
True
```

The function prints the result but does not return it.

Therefore, `answer` receives `None`.

### Important Difference

Printing a value and returning a value are different operations.

| `print()` | `return` |
|---|---|
| Displays information | Sends a result back to the caller |
| Does not automatically provide that displayed value | Provides the returned object |
| Useful for output | Useful for calculations and data transfer |

---

# 22. Identity Operators with Custom Classes

Python classes can define their own objects.

By default, user-defined objects typically use identity-based equality unless the class defines a different equality behavior.

### Example Without Custom Equality

```python
class Student:
    def __init__(self, name):
        self.name = name


first = Student("Amaan")

second = Student("Amaan")

print(first is second)
```

**Output:**

```text
False
```

Both student objects have the same name, but they are separate objects.

### Example with Custom Equality

A class can define `__eq__()` to specify value-based equality.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):

        if not isinstance(other, Student):
            return NotImplemented

        return self.name == other.name


first = Student("Amaan")

second = Student("Amaan")

print(first == second)
print(first is second)
```

**Output:**

```text
True
False
```

### Explanation

The equality method compares the `name` attributes.

Both objects have the same name, so `==` returns `True`.

However, the objects are separate, so `is` returns `False`.

### Important Technical Note

When a class defines `__eq__()` but does not provide a suitable `__hash__()`, Python normally makes its instances unhashable.

This matters when custom objects are used as dictionary keys or set elements.

---

# 23. Identity Operators with Copying

Copying is an important concept when working with mutable objects.

Python provides common copying techniques:

- Assignment.
- Shallow copying.
- Deep copying.

### 23.1 Assignment

```python
original = [10, 20, 30]

another = original

print(original is another)
```

**Output:**

```text
True
```

Assignment creates another reference.

It does not copy the original list.

### 23.2 Shallow Copy

```python
original = [10, 20, 30]

copied = original.copy()

print(original == copied)
print(original is copied)
```

**Output:**

```text
True
False
```

A new outer list is created.

### 23.3 Deep Copy

Deep copying creates a new outer object and recursively copies nested objects.

```python
import copy

original = [[10, 20], [30, 40]]

copied = copy.deepcopy(original)

print(original == copied)
print(original is copied)
print(original[0] is copied[0])
```

**Output:**

```text
True
False
False
```

### Comparison

| Operation | New Outer Object? | Nested Mutable Objects Shared? |
|---|---|---|
| Assignment | No | Yes |
| Shallow copy | Yes | Usually yes |
| Deep copy | Yes | Normally no, subject to object-specific copy behavior |

### Practical Importance

Copying is important when:

- You want to avoid accidental changes to original data.
- You work with nested lists or dictionaries.
- You pass mutable objects between functions.
- You need independent data structures.

---

# 24. Common Uses of Identity Operators

Identity operators are particularly useful in the following situations.

## 24.1 Checking None

```python
value = None

if value is None:
    print("No value")
```

## 24.2 Checking Non-None

```python
username = "Amaan"

if username is not None:
    print("Username provided")
```

## 24.3 Detecting Shared References

```python
first = [10, 20, 30]

second = first

print(first is second)
```

## 24.4 Working with Sentinel Objects

```python
MISSING = object()

value = MISSING

if value is MISSING:
    print("Missing")
```

## 24.5 Checking Returned Objects

```python
def return_same(value):
    return value


data = [1, 2, 3]

result = return_same(data)

print(result is data)
```

## 24.6 Debugging Aliasing

```python
original = {"a": 10}

alias = original

print(original is alias)
```

These are practical identity-related checks.

---

# 25. Difference Between Identity and Membership Operators

Identity operators and membership operators perform different tasks.

| Identity Operators | Membership Operators |
|---|---|
| `is` | `in` |
| `is not` | `not in` |
| Check whether references point to the same object | Check whether a value exists in a collection |
| Work with object identity | Work with supported membership testing |
| Commonly used for `None` checks | Commonly used for searching |

### Identity Example

```python
first = [10, 20, 30]

second = first

print(first is second)
```

Output:

```text
True
```

### Membership Example

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

Both results are `True`, but the expressions answer different questions.

---

# 26. Identity Operators and Boolean Values

Python has two Boolean objects:

- `True`
- `False`

They can be compared by identity.

### Example

```python
first = True

second = True

print(first is second)
```

**Output:**

```text
True
```

Both variables refer to the same Boolean singleton object.

### Another Example

```python
first = True

second = False

print(first is second)
```

**Output:**

```text
False
```

### Important Point

Use equality when you want to compare Boolean values.

Identity checking is suitable for the two Boolean singleton objects, but `is` should not replace normal value comparisons throughout your program.

---

# 27. Identity and Object Lifetime

An object's identity remains stable throughout its lifetime.

Python's `id()` returns an integer representing object identity.

### Example

```python
numbers = [10, 20, 30]

first_id = id(numbers)

numbers.append(40)

second_id = id(numbers)

print(first_id == second_id)
print(numbers)
```

**Output:**

```text
True
[10, 20, 30, 40]
```

The list was modified, but it remained the same object.

### Important Point

Modifying a mutable object does not normally change its identity.

### Reassignment Is Different

```python
numbers = [10, 20, 30]

first = numbers

numbers = [40, 50, 60]

print(first)
print(numbers)
print(first is numbers)
```

**Output:**

```text
[10, 20, 30]
[40, 50, 60]
False
```

The variable `numbers` now refers to a different list.

The original list remains accessible through `first`.

---

# 28. Important Rules and Edge Cases

### Rule 1: Equal Values Do Not Always Mean Identical Objects

```python
a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

### Rule 2: Assignment Creates Another Reference

```python
a = [1, 2, 3]

b = a

print(a is b)
```

Output:

```text
True
```

### Rule 3: `None` Should Be Checked with `is`

```python
value = None

print(value is None)
```

Output:

```text
True
```

### Rule 4: `is not` Checks Different Identity

```python
a = []
b = []

print(a is not b)
```

Output:

```text
True
```

### Rule 5: `id()` Is Not a Substitute for Equality

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

The values are equal even though the objects are different.

### Rule 6: Object IDs Can Be Reused

After an object is destroyed, its old identity value may be reused for a different object.

Do not use `id()` values as permanent identifiers.

### Rule 7: Don't Depend on Integer or String Interning

Python implementations may reuse some immutable objects.

Do not use `is` to compare ordinary numerical or string values.

Use `==`.

### Rule 8: A Shallow Copy Can Share Nested Objects

```python
a = [[1, 2]]

b = a.copy()

print(a is b)
print(a[0] is b[0])
```

Output:

```text
False
True
```

### Rule 9: An Implicit Function Return Is None

```python
def display():
    print("Hello")

result = display()

print(result is None)
```

Output:

```text
Hello
True
```

### Rule 10: Empty and False Values Are Not None

```python
print(0 is None)
print(False is None)
print([] is None)
```

Output:

```text
False
False
False
```

---

# 29. Identity Operator Precedence

Identity operators belong to the comparison-operator group in Python.

They have the same general precedence level as:

- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`
- `in`
- `not in`

Logical operators have lower precedence.

The relevant logical order is:

1. `not`
2. `and`
3. `or`

### Example

```python
value = None

result = value is None and value is not False

print(result)
```

**Output:**

```text
True
```

### Recommended Style

Use parentheses in longer conditions to make the intended grouping clear:

```python
result = (value is None) and (value is not False)
```

---

# 30. Twelve Examples Explained

The Python file `01_identity_operators.py` contains twelve examples.

## Example 1: `is` with the Same Object

**Objective:** Check whether two variables refer to the same list.

```python
first_list = [10, 20, 30]

second_list = first_list

print(first_list is second_list)
```

**Output:**

```text
True
```

**Explanation:**

- A list is created.
- The second variable refers to the first list.
- Both references point to the same object.
- Therefore, identity returns `True`.

## Example 2: `is not` with Different Objects

```python
first_list = [10, 20, 30]

second_list = [10, 20, 30]

print(first_list is second_list)
print(first_list is not second_list)
```

**Output:**

```text
False
True
```

**Explanation:**

Both lists contain equal values but are separate objects.

## Example 3: Difference Between `is` and `==`

```python
first = [1, 2, 3]

second = [1, 2, 3]

print(first == second)
print(first is second)
```

**Output:**

```text
True
False
```

**Explanation:**

Equality and identity are different comparisons.

## Example 4: Checking None with `is`

```python
username = None

print(username is None)
```

**Output:**

```text
True
```

**Explanation:**

The variable refers to Python's `None` singleton.

## Example 5: Checking Not None

```python
username = "Amaan"

print(username is not None)
```

**Output:**

```text
True
```

The variable contains a string object instead of `None`.

## Example 6: Aliasing a Mutable List

```python
original = [10, 20, 30]

alias = original

alias.append(40)

print(original)
print(alias)

print(original is alias)
```

**Output:**

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
True
```

Both variables refer to the same mutable list.

## Example 7: Identity of a Copied List

```python
original = [10, 20, 30]

copied = original.copy()

print(original == copied)
print(original is copied)
```

**Output:**

```text
True
False
```

The copy has equal values but a separate outer list object.

## Example 8: Dictionary Aliasing

```python
student = {
    "name": "Amaan",
    "age": 22
}

another_reference = student

another_reference["course"] = "Python"

print(student)
print(student is another_reference)
```

**Output:**

```text
{'name': 'Amaan', 'age': 22, 'course': 'Python'}
True
```

The dictionary is modified through another reference to the same object.

## Example 9: Two Different Dictionaries

```python
first = {
    "name": "Amaan",
    "age": 22
}

second = {
    "name": "Amaan",
    "age": 22
}

print(first == second)
print(first is second)
```

**Output:**

```text
True
False
```

Both dictionaries are equal but not identical.

## Example 10: Sentinel Object

```python
MISSING = object()

value = MISSING

print(value is MISSING)
```

**Output:**

```text
True
```

The program checks whether the variable refers to the unique sentinel object.

## Example 11: Custom Class Object Identity

```python
first_student = Student("Amaan", 101)

second_student = Student("Amaan", 101)

print(first_student == second_student)
print(first_student is second_student)
```

**Output:**

```text
True
False
```

In the supplied Python file, the `Student` class defines value-based equality through `__eq__()`. The objects have equal data but different identities.

## Example 12: Function Returning None

```python
def function_without_return():
    print("Function executed successfully.")

result = function_without_return()

print(result is None)
```

**Output:**

```text
Function executed successfully.
True
```

A function that does not explicitly return a value returns `None`.

---

# 31. Twelve Solved Problems

The Python file contains twelve interactive problems.

Each problem focuses on a practical identity-related situation.

## Problem 1: Check Whether a Value Is None

**Problem Statement:**

Ask the user for a value. If they press Enter without entering anything, treat the value as `None`. Otherwise, store the entered text.

### Logic

1. Read the input.
2. Remove surrounding spaces.
3. Convert blank input into `None`.
4. Check using `is None`.
5. Display the result.

### Code

```python
raw_value = input("Enter a value: ").strip()

value = None if raw_value == "" else raw_value

if value is None:
    print("The value is None.")
else:
    print("Entered value:", value)
```

### Output 1

```text
Enter a value:
The value is None.
```

### Output 2

```text
Enter a value: Python
Entered value: Python
```

**Concept:** `None` and identity checking.

## Problem 2: Check Whether a Value Is Not None

**Problem Statement:**

Ask the user for a username and check whether it was provided.

### Code

```python
username = input("Enter username: ").strip()

if username == "":
    username = None

if username is not None:
    print("Username:", username)
    print("Username was provided.")
else:
    print("No username was provided.")
```

**Output:**

```text
Enter username: Amaan
Username: Amaan
Username was provided.
```

**Concept:** `is not None`.

## Problem 3: Check the Same List Reference

**Problem Statement:**

Create a list and assign it to another variable. Check whether both references point to the same object.

### Code

```python
first_list = ["Python", "Java", "C++"]

second_list = first_list

print(first_list is second_list)
```

**Output:**

```text
True
```

**Concept:** Assignment and aliasing.

## Problem 4: Compare Equality and Identity

**Problem Statement:**

Create two separate lists with equal contents. Compare them using `==` and `is`.

### Code

```python
first_list = [10, 20, 30]

second_list = [10, 20, 30]

print(first_list == second_list)
print(first_list is second_list)
```

**Output:**

```text
True
False
```

**Concept:** Value equality versus object identity.

## Problem 5: Check List Copy Identity

**Problem Statement:**

Create a list and make a copy using `copy()`. Check whether they are equal and whether they are the same object.

### Code

```python
original = [10, 20, 30]

copied = original.copy()

print(original == copied)
print(original is copied)
```

**Output:**

```text
True
False
```

**Concept:** Shallow copying and identity.

## Problem 6: Check Dictionary Copy Identity

**Problem Statement:**

Create a dictionary and make a shallow copy. Compare their identity.

### Code

```python
original = {
    "name": "Amaan",
    "roll_number": 101
}

copied = original.copy()

print(original == copied)
print(original is copied)
```

**Output:**

```text
True
False
```

**Concept:** Dictionary copying.

## Problem 7: Understand Shared List References

**Problem Statement:**

Create two references to the same list. Modify the list using one reference and display both variables.

### Code

```python
original = [10, 20, 30]

alias = original

alias.append(40)

print("Original:", original)
print("Alias:", alias)

print(original is alias)
```

**Output:**

```text
Original: [10, 20, 30, 40]
Alias: [10, 20, 30, 40]
True
```

**Concept:** Shared mutable objects.

## Problem 8: Check a Function Returning None

**Problem Statement:**

Create a function without an explicit return statement. Check the value received by the calling variable.

### Code

```python
def display():
    print("Hello Python")

result = display()

print(result)
print(result is None)
```

**Output:**

```text
Hello Python
None
True
```

**Concept:** Implicit function returns.

## Problem 9: Detect a Sentinel Object

**Problem Statement:**

Create a unique marker using `object()` and check whether a variable refers to that marker.

### Code

```python
MISSING = object()

value = MISSING

if value is MISSING:
    print("Value is missing")
else:
    print("Value:", value)
```

**Output:**

```text
Value is missing
```

**Concept:** Sentinel objects and identity.

## Problem 10: Check Object Identity Through a Function

**Problem Statement:**

Pass an object to a function and return the same object. Check whether the returned object is identical to the original.

### Code

```python
def return_same_object(value):
    return value

numbers = [10, 20, 30]

result = return_same_object(numbers)

print(result is numbers)
```

**Output:**

```text
True
```

**Concept:** Object references and function returns.

## Problem 11: Compare Three Object References

**Problem Statement:**

Create one object, a second reference to that object, and a third independently created object. Compare their identities.

### Code

```python
first = object()

second = first

third = object()

print(first is second)
print(first is third)
print(second is third)
```

**Output:**

```text
True
False
False
```

**Concept:** Multiple references and separate objects.

## Problem 12: Compare Custom Object Equality and Identity

**Problem Statement:**

Create two `Student` objects with the same name and roll number. Compare their values and identities.

### Code

```python
class Student:

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __eq__(self, other):

        if not isinstance(other, Student):
            return NotImplemented

        return (
            self.name == other.name
            and self.roll_number == other.roll_number
        )


first_student = Student("Amaan", 101)

second_student = Student("Amaan", 101)

print(first_student == second_student)
print(first_student is second_student)
```

**Output:**

```text
True
False
```

**Concept:** Custom equality and object identity.

---

# 32. Ten Unsolved Practice Questions

Try these questions independently.

| No. | Practice Question | Hint |
|---|---|---|
| 1 | Check whether a variable contains `None`. | Use `is None` |
| 2 | Check whether an optional value is not `None`. | Use `is not None` |
| 3 | Create two references to the same list and compare their identity. | Use assignment and `is` |
| 4 | Create two different lists with equal contents and compare them. | Use `==` and `is` |
| 5 | Copy a list and check whether the original and copied objects are identical. | Use `copy()` |
| 6 | Create two references to the same dictionary and compare their identity. | Use assignment |
| 7 | Modify a list through an alias and observe the original variable. | Understand aliasing |
| 8 | Write a function without a return statement and check its result. | Check for `None` |
| 9 | Create a sentinel object and detect it using identity. | Use `object()` |
| 10 | Create two custom objects with equal data and compare equality and identity. | Define a class and `__eq__()` |

## Additional Challenge Problems

### Challenge 1: Check Empty Input

Write a function that returns `None` when the user enters an empty string.

### Challenge 2: Shared Dictionary

Create two references to a dictionary. Modify one reference and observe the other.

### Challenge 3: Shallow Copy

Create a nested list, copy it using `.copy()`, and compare the identity of the outer and inner lists.

### Challenge 4: Deep Copy

Use the `copy` module to create a deep copy and check the identity of nested objects.

### Challenge 5: Sentinel Default

Write a function that distinguishes between an omitted argument and an explicitly supplied `None`.

---

# 33. Common Mistakes

## Mistake 1: Using `is` Instead of `==`

Incorrect:

```python
a = 100
b = 100

if a is b:
    print("Equal")
```

This relies on identity behavior and is not the correct way to compare numerical values.

Correct:

```python
if a == b:
    print("Equal")
```

## Mistake 2: Assuming Equal Lists Are the Same Object

```python
a = [10, 20, 30]

b = [10, 20, 30]

print(a == b)
print(a is b)
```

The outputs are `True` and `False`.

Equal contents do not automatically mean identical objects.

## Mistake 3: Confusing Assignment with Copying

Incorrect assumption:

```python
a = [1, 2, 3]

b = a
```

This does not create a copy.

Both variables point to the same list.

## Mistake 4: Using `== None` Instead of `is None`

Less preferred:

```python
if value == None:
    print("Missing")
```

Recommended:

```python
if value is None:
    print("Missing")
```

## Mistake 5: Confusing None with Empty Values

```python
value = 0

print(value is None)
```

Output:

```text
False
```

Zero is not `None`.

## Mistake 6: Assuming Every Copy Is Deep

```python
original = [[1, 2]]

copied = original.copy()

print(original[0] is copied[0])
```

Output:

```text
True
```

The nested list is shared because `.copy()` is shallow.

## Mistake 7: Using `is` to Compare Strings

Incorrect:

```python
name1 = "Python"

name2 = "Python"

print(name1 is name2)
```

Do not depend on the identity result.

Correct:

```python
print(name1 == name2)
```

## Mistake 8: Assuming `id()` Is a Permanent Identifier

Object identity values are not permanent identifiers that can safely be stored and reused indefinitely.

The identity value may be reused after an object's lifetime ends.

## Mistake 9: Confusing Printing with Returning

```python
def display():
    print("Hello")
```

The function displays text but returns `None`.

## Mistake 10: Thinking Modification Changes Identity

Appending an element to a list changes its contents, not its identity.

---

# 34. Best Practices

Follow these practices while working with identity operators.

1. Use `is None` to check whether a value is `None`.
2. Use `is not None` to check whether a value is present instead of `None`.
3. Use `==` for normal value comparisons.
4. Use `is` when object identity actually matters.
5. Understand assignment before working with mutable collections.
6. Understand the difference between aliasing and copying.
7. Use `.copy()` when you need a shallow copy.
8. Use `copy.deepcopy()` when an independent nested copy is required and the objects support it.
9. Do not depend on integer or string interning.
10. Do not use `id()` as a permanent object identifier.
11. Understand that a function without an explicit return returns `None`.
12. Use sentinel objects when `None` is a valid value and a distinct missing state is required.
13. Avoid unnecessary identity checks.
14. Use meaningful variable names.
15. Test both equal and separate objects.
16. Understand the effect of modifying mutable objects through aliases.

---

# 35. Debugging and Troubleshooting

When an identity expression gives an unexpected result, follow these steps.

## Step 1: Print the Values

```python
print(first)
print(second)
```

Check whether the objects contain the expected data.

## Step 2: Compare Values

```python
print(first == second)
```

This checks equality.

## Step 3: Compare Identity

```python
print(first is second)
```

This checks whether both references point to the same object.

## Step 4: Inspect Object Identity

```python
print(id(first))
print(id(second))
```

Use this only as a debugging aid while the objects are alive.

## Step 5: Check for Aliasing

Look for assignments such as:

```python
second = first
```

This creates another reference to the same object.

## Step 6: Check Whether a Copy Was Created

```python
second = first.copy()
```

This creates a separate outer list or dictionary.

## Step 7: Check Whether a Function Returns a Value

```python
result = some_function()

print(result)
print(result is None)
```

A function without an explicit return value returns `None`.

## Step 8: Check None Separately from Falsy Values

```python
print(value is None)
print(bool(value))
```

These expressions answer different questions.

---

# 36. Practice Test

Try solving these questions without executing the code.

### Question 1

```python
a = [10, 20, 30]

b = a

print(a is b)
```

What is the output?

### Question 2

```python
a = [10, 20, 30]

b = [10, 20, 30]

print(a == b)
```

What is the output?

### Question 3

```python
a = [10, 20, 30]

b = [10, 20, 30]

print(a is b)
```

What is the output?

### Question 4

```python
value = None

print(value is None)
```

What is the output?

### Question 5

```python
value = 0

print(value is None)
```

What is the output?

### Question 6

```python
a = [1, 2, 3]

b = a.copy()

print(a is not b)
```

What is the output?

### Question 7

```python
a = [10, 20]

b = a

b.append(30)

print(a)
```

What is the output?

### Question 8

```python
def display():
    print("Hello")

result = display()

print(result is None)
```

What is the output?

### Question 9

```python
MISSING = object()

value = MISSING

print(value is MISSING)
```

What is the output?

### Question 10

```python
a = {"name": "Amaan"}

b = a

print(a is b)
```

What is the output?

### Question 11

```python
a = [[1, 2]]

b = a.copy()

print(a[0] is b[0])
```

What is the output?

### Question 12

```python
value = ""

print(value is None)
```

What is the output?

## Answer Key

| Question | Answer | Explanation |
|---|---|---|
| 1 | `True` | Both variables refer to the same list |
| 2 | `True` | List values are equal |
| 3 | `False` | Separate list objects |
| 4 | `True` | Value is the None singleton |
| 5 | `False` | Zero is not None |
| 6 | `True` | The copied outer list is a different object |
| 7 | `[10, 20, 30]` | The shared list was modified |
| 8 | `Hello`, then `True` | Function returns None implicitly |
| 9 | `True` | Both references point to the sentinel |
| 10 | `True` | Both references point to the same dictionary |
| 11 | `True` | The nested list is shared in a shallow copy |
| 12 | `False` | Empty string is not None |

---

# 37. Viva Questions and Answers

Prepare these questions for practical examinations, oral exams, and interviews.

## A. Basic Questions

**Q1. What are identity operators in Python?**

Identity operators check whether two variables refer to the same object.

**Q2. How many identity operators are available in Python?**

Two: `is` and `is not`.

**Q3. What is the purpose of the `is` operator?**

It checks whether two references point to the same object.

**Q4. What is the purpose of the `is not` operator?**

It checks whether two references point to different objects.

**Q5. What type of result do identity operators return?**

A Boolean result: `True` or `False`.

**Q6. What is object identity?**

Object identity is the identity of a particular object during its lifetime.

**Q7. Can two variables refer to the same object?**

Yes. They can both refer to the same object.

**Q8. What happens when one variable is assigned to another?**

The new variable refers to the same object; it does not automatically create a copy.

**Q9. What is aliasing?**

Aliasing occurs when multiple variable names refer to the same object.

**Q10. What is the difference between object identity and object value?**

Identity describes which object it is. Value describes the data it contains.

## B. Equality and Identity

**Q11. What is the difference between `is` and `==`?**

`is` checks object identity, whereas `==` checks value equality.

**Q12. Can two different objects have equal values?**

Yes.

**Q13. Can two variables refer to the same object?**

Yes.

**Q14. What happens when two different lists contain the same elements?**

They can compare equal with `==` while comparing different with `is`.

**Q15. Which operator should be used for numerical value comparison?**

`==`.

**Q16. Should `is` be used to compare strings?**

Generally no. Use `==` for string value comparison.

**Q17. Does equality always mean identity?**

No.

**Q18. Does identity normally imply equality?**

For ordinary equality behavior, identical references compare equal to themselves, but custom equality methods can define unusual behavior. Identity and equality remain separate concepts.

**Q19. What does `is not` mean?**

It checks that two references do not refer to the same object.

**Q20. Why should you not depend on integer interning?**

Because object reuse is implementation-dependent and should not be used for value comparison.

## C. None Questions

**Q21. What is None in Python?**

`None` is a special singleton object representing the absence of a value.

**Q22. What is its data type?**

`NoneType`.

**Q23. How do you check whether a variable is None?**

Use `variable is None`.

**Q24. How do you check whether a variable is not None?**

Use `variable is not None`.

**Q25. Is zero equal to None?**

No.

**Q26. Is False equal to None?**

No.

**Q27. Is an empty string None?**

No.

**Q28. What is the difference between `if value is None` and `if not value`?**

The first checks specifically for None. The second checks general falsiness.

**Q29. Why is `is None` preferred over `== None`?**

It directly checks the identity of the None singleton.

**Q30. What is a sentinel object?**

A unique object used to represent a special state, such as a missing argument.

## D. Object and Reference Questions

**Q31. What is the `id()` function?**

It returns an integer representing an object's identity.

**Q32. Can an object's identity change during its lifetime?**

No. Its identity remains stable during its lifetime.

**Q33. Can Python reuse an object identity value?**

Yes, after the original object no longer exists.

**Q34. What is the difference between assignment and copying?**

Assignment creates another reference. Copying creates a new object according to the copying operation.

**Q35. What is a shallow copy?**

A copy that creates a new outer object while retaining references to nested objects.

**Q36. What is a deep copy?**

A copy that recursively copies nested objects where supported.

**Q37. Does modifying an alias affect the original mutable object?**

Yes, because both references point to the same object.

**Q38. Does modifying a copied outer list necessarily modify its nested objects?**

No, but a shallow copy may still share nested objects.

**Q39. What does `object()` do?**

It creates a new base object.

**Q40. Why are sentinel objects useful?**

They help distinguish a special missing state from valid values such as None.

## E. Practical and Technical Questions

**Q41. What does a function without an explicit return statement return?**

It returns `None`.

**Q42. Does `print()` return the displayed value?**

No. `print()` returns `None`.

**Q43. Can identity operators be used with dictionaries?**

Yes.

**Q44. Can identity operators be used with custom objects?**

Yes.

**Q45. Can a custom class define its own equality behavior?**

Yes, using `__eq__()`.

**Q46. Does defining `__eq__()` automatically change the meaning of `is`?**

No. Identity checking remains based on whether references point to the same object.

**Q47. What is the difference between `is` and `in`?**

`is` checks object identity; `in` checks membership.

**Q48. Which identity operator should normally be used with None?**

`is`.

**Q49. Does changing a list's contents normally change its identity?**

No. The same list object can be modified without changing its identity.

**Q50. Give a real-world use of identity operators.**

Checking for None, detecting sentinel objects, and determining whether two references share the same mutable object.

---

# 38. Connection with Data Structures and Algorithms (DSA)

Identity is useful when understanding how data structures and objects are stored, referenced, passed, and modified.

It is particularly important when studying:

- Lists and arrays.
- Linked lists.
- Trees and graphs.
- Hash tables.
- Object references.
- Memory management.
- Copying and aliasing.
- Mutable data structures.

## 38.1 Object References in Lists

```python
first = [10, 20, 30]

second = first

print(first is second)
```

Understanding references helps prevent accidental modification of shared data.

## 38.2 Linked Lists

A linked list node contains a reference to another node.

Conceptually:

```text
Head
 |
 v
+------+------+
| Data | Next |
+------+------+
         |
         v
      +------+------+
      | Data | Next |
      +------+------+
                |
                v
               None
```

In linked-list implementations, references connect one node to another.

Identity checks can help determine whether two variables refer to the exact same node.

## 38.3 Trees and Graphs

Trees and graphs frequently contain references to nodes.

Identity matters when determining whether two references identify the same node.

For example, two graph edges may point to one shared node.

## 38.4 Shared References

When different parts of a program share the same object, changing that object through one reference may affect other parts.

Understanding identity helps avoid unexpected changes.

## 38.5 Copying Data Structures

A shallow copy and deep copy behave differently with nested objects.

This matters when building:

- Nested lists.
- Trees.
- Graphs.
- Dictionaries containing other collections.
- Complex application state.

## 38.6 Practical DSA Exercise

```python
first = [10, 20, 30]

second = first

third = first.copy()

print(first is second)
print(first is third)
print(first == third)
```

**Output:**

```text
True
False
True
```

This example demonstrates the difference between shared references and separate copies.

### DSA Topics to Study Next

1. Arrays and Lists.
2. Linked Lists.
3. Stack and Queue.
4. Trees.
5. Graphs.
6. Object References.
7. Shallow Copy and Deep Copy.
8. Hash Tables.
9. Memory Management.
10. Mutable and Immutable Data Structures.

---

# 39. Interview Preparation

Prepare these questions for technical interviews.

### Conceptual Interview Questions

1. Explain identity operators in Python.
2. What is the difference between `is` and `==`?
3. What does object identity mean?
4. How does assignment differ from copying?
5. What is aliasing?
6. Why should `is None` be used?
7. What is the purpose of `id()`?
8. What is a sentinel object?
9. What is a shallow copy?
10. What is a deep copy?

### Practical Interview Questions

1. Write a program to compare two list references.
2. Create two equal lists and compare their identities.
3. Check whether an optional function parameter is None.
4. Write a function that returns the same object.
5. Write a function that returns a copy.
6. Demonstrate how aliasing works.
7. Demonstrate a shallow copy with a nested list.
8. Create a unique sentinel object.
9. Explain why an empty string is not None.
10. Create a custom class with value-based equality.

### Common Interview Trap

Consider:

```python
a = [1, 2, 3]

b = a

c = [1, 2, 3]

print(a == b)
print(a is b)

print(a == c)
print(a is c)
```

**Output:**

```text
True
True
True
False
```

Be prepared to explain each result.

---

# 40. Mini Project: Object Reference Inspector

This is an additional practical exercise.

Create a small program that compares object references.

### Requirements

1. Create a list.
2. Create another reference to the same list.
3. Create a separate list with equal values.
4. Compare values using `==`.
5. Compare identities using `is`.
6. Display object IDs.
7. Modify one reference and observe the changes.

### Example Code

```python
first = [10, 20, 30]

second = first

third = [10, 20, 30]

print("First:", first)
print("Second:", second)
print("Third:", third)

print("\nEquality Checks:")

print("first == second:", first == second)
print("first == third:", first == third)

print("\nIdentity Checks:")

print("first is second:", first is second)
print("first is third:", first is third)

print("\nObject IDs:")

print("First ID:", id(first))
print("Second ID:", id(second))
print("Third ID:", id(third))

print("\nModifying second:")

second.append(40)

print("First:", first)
print("Second:", second)
print("Third:", third)
```

### Expected Concepts

- Assignment.
- Aliasing.
- Object identity.
- Equality.
- Mutable objects.
- Object IDs.

### Your Task

Extend this project by adding:

- A dictionary comparison.
- A shallow copy.
- A deep copy.
- A None check.
- A sentinel object.

---

# 41. Glossary

| Term | Meaning |
|---|---|
| Identity | The identity of a particular object |
| `is` | Checks whether references point to the same object |
| `is not` | Checks whether references point to different objects |
| Equality | Whether two values compare equal |
| `==` | Equality comparison operator |
| Object | An instance of a Python data type or class |
| Reference | A variable name or reference that identifies an object |
| Aliasing | Multiple names referring to the same object |
| Mutable | An object that can be modified |
| Immutable | An object that cannot be modified after creation |
| `None` | Special object representing absence of a value |
| `NoneType` | Data type of None |
| Singleton | A concept where one unique instance represents a value |
| `id()` | Returns the integer identity of an object |
| `object()` | Creates a new base object |
| Sentinel | A special object used as a marker |
| Shallow Copy | A new outer object with nested references shared |
| Deep Copy | A recursively copied object structure |
| `copy()` | Common shallow-copy method on lists and dictionaries |
| `deepcopy()` | Recursive copying operation from the copy module |
| `__eq__()` | Special method used to customize equality |
| Hashable | An object suitable for hash-based collections |
| Reference Sharing | Multiple variables referring to one object |
| Object Lifetime | The period during which an object exists |
| DSA | Data Structures and Algorithms |

---

# 42. Quick Revision Notes

### Identity Operators

```python
a is b
a is not b
```

### Same Reference

```python
a = [10, 20, 30]

b = a

print(a is b)
```

### Separate Objects

```python
a = [10, 20, 30]

b = [10, 20, 30]

print(a is b)
```

### Equality

```python
print(a == b)
```

### None Check

```python
value = None

print(value is None)
```

### Not None Check

```python
value = "Python"

print(value is not None)
```

### Object Identity

```python
print(id(value))
```

### Sentinel Object

```python
MISSING = object()

value = MISSING

print(value is MISSING)
```

### Function Returning Same Object

```python
def return_same(value):
    return value
```

### Shallow Copy

```python
copied = original.copy()
```

### Deep Copy

```python
import copy

copied = copy.deepcopy(original)
```

### Most Important Rules

1. `is` checks object identity.
2. `is not` checks different object identity.
3. `==` checks value equality.
4. Assignment does not automatically copy an object.
5. Multiple variables can refer to the same object.
6. Mutable objects can be modified through shared references.
7. `None` is a singleton.
8. Use `is None` for None checks.
9. Use `is not None` for non-None checks.
10. Do not rely on interning or caching.
11. `id()` identifies an object during its lifetime.
12. A shallow copy may share nested objects.
13. A function without an explicit return returns `None`.
14. A sentinel object can represent a unique missing state.

---

# 43. Learning Checklist

Complete this checklist before moving to the next topic.

## Basic Concepts

- [ ] I understand identity operators.
- [ ] I can explain the `is` operator.
- [ ] I can explain the `is not` operator.
- [ ] I understand object identity.
- [ ] I understand Boolean results.

## Equality and Identity

- [ ] I understand `==`.
- [ ] I understand the difference between `==` and `is`.
- [ ] I can compare separate lists.
- [ ] I can compare equal dictionaries.
- [ ] I can explain why equal objects need not be identical.

## Objects and References

- [ ] I understand Python object references.
- [ ] I understand aliasing.
- [ ] I understand mutable objects.
- [ ] I understand immutable objects.
- [ ] I understand list copying.
- [ ] I understand dictionary copying.
- [ ] I understand shallow copying.
- [ ] I understand deep copying.
- [ ] I understand how object references work with functions.

## None and Sentinel Objects

- [ ] I understand `None`.
- [ ] I can use `is None`.
- [ ] I can use `is not None`.
- [ ] I can distinguish None from False and zero.
- [ ] I understand sentinel objects.
- [ ] I understand the purpose of `object()`.

## Advanced Concepts

- [ ] I understand the `id()` function.
- [ ] I understand function return values.
- [ ] I understand custom object equality.
- [ ] I understand identity with custom classes.
- [ ] I understand why integer and string interning should not be relied upon.

## Programming Practice

- [ ] I have run all 12 examples.
- [ ] I have attempted all 12 solved problems.
- [ ] I have attempted all 10 unsolved questions.
- [ ] I have completed the practice test.
- [ ] I can explain the difference between `is` and `==`.
- [ ] I can explain aliasing and copying.

## Interview and DSA

- [ ] I can explain object references.
- [ ] I understand linked-list references.
- [ ] I understand shared objects in data structures.
- [ ] I can solve the object reference inspector project.
- [ ] I have prepared the viva questions.

---

# 44. How to Run the Python Program

The folder contains two files:

```text
07-Identity-Operators/
│
├── README.md
│
└── 01_identity_operators.py
```

### Step 1: Open PowerShell or VS Code Terminal

Navigate to your identity operators folder.

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\07-Identity-Operators"
```

### Step 2: Run the Python Program

```powershell
python 01_identity_operators.py
```

### Step 3: Select a Menu Option

The program provides the following options:

```text
=============================================================
                  PYTHON IDENTITY OPERATORS
=============================================================

1. View 12 Identity Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

### Step 4: Learn and Practise

Recommended learning order:

1. Select option `1` and study all examples.
2. Select option `2` and practise all solved problems.
3. Select option `3` and attempt the questions yourself.
4. Select option `4` and check your progress.

### Step 5: Experiment with Your Own Examples

Change the list values, dictionary data, and function inputs.

Observe the difference between `is` and `==`.

---

# 45. Folder Structure

The completed topic should have the following structure:

```text
05-Operators-Expressions/
│
├── 01-Arithmetic-Operators/
│
├── 02-Assignment-Operators/
│
├── 03-Comparison-Operators/
│
├── 04-Logical-Operators/
│
├── 05-Bitwise-Operators/
│
├── 06-Membership-Operators/
│
└── 07-Identity-Operators/
    │
    ├── README.md
    │
    └── 01_identity_operators.py
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `README.md` | Theory, explanations, examples, viva, and practice material |
| `01_identity_operators.py` | Executable examples and interactive problems |

Keep both files in the same folder.

---

# 46. Navigation

### Previous Topic

[06 - Membership Operators](../06-Membership-Operators/README.md)

### Current Topic

**07 - Identity Operators**

### Next Topic

[08 - Expressions](../08-Expressions/README.md)

### Parent Folder

[05 - Operators and Expressions](../README.md)

---

# 47. Final Summary

Identity operators are used to check whether two variables refer to the same Python object.

Python provides two identity operators:

- `is`
- `is not`

The most important distinction in this topic is between value equality and object identity.

Consider:

```python
first = [10, 20, 30]

second = [10, 20, 30]

third = first

print(first == second)
print(first is second)

print(first == third)
print(first is third)
```

**Output:**

```text
True
False
True
True
```

From this example, remember:

- `==` checks whether values are equal.
- `is` checks whether references point to the same object.
- Assignment creates another reference.
- Copying creates a separate outer object.
- A shallow copy may share nested objects.
- `None` is a singleton.
- `is None` is the recommended way to check for None.
- Sentinel objects can represent special missing states.

Identity operators are especially important when working with mutable objects, functions, object references, and complex data structures.

Understanding these concepts will help you write safer Python programs and prepare for advanced concepts such as linked lists, trees, graphs, and object-oriented programming.

**Complete all examples, solve the practice problems, and revise the viva questions before moving to the next topic.**

Keep learning, keep practising, and keep building strong Python fundamentals.