# Python Membership Operators

**Topic:** Python Programming Fundamentals  
**Folder:** `06-Membership-Operators`  
**Python File:** `01_membership_operators.py`  
**Level:** Beginner to Intermediate

---

# 1. Introduction to Membership Operators

Membership operators are an important part of Python programming. They are used to check whether a particular value, character, or element exists inside another object, such as a string, list, tuple, set, dictionary, or range.

In simple words, membership operators help us answer two questions:

1. Does this value exist in the collection?
2. Does this value not exist in the collection?

Python provides two membership operators:

| Operator | Name | Purpose |
|---|---|---|
| `in` | Membership operator | Checks whether an element exists |
| `not in` | Non-membership operator | Checks whether an element does not exist |

Both operators are frequently used in conditional statements, loops, searching operations, data validation, and DSA problems.

### Real-Life Example

Imagine that a college has a list of registered students:

```python
registered_students = ["Amaan", "Rahul", "Arjun", "Sameer"]
```

A program needs to check whether a particular student is registered.

```python
student_name = "Amaan"

if student_name in registered_students:
    print("Student is registered")
else:
    print("Student is not registered")
```

**Output:**

```text
Student is registered
```

The program checks whether `"Amaan"` exists inside the `registered_students` list.

Because the name exists, the membership expression returns `True`.

### Another Example

Suppose a website maintains a list of blocked users.

```python
blocked_users = ["user01", "user02", "user03"]

username = "user10"

if username not in blocked_users:
    print("Username is not blocked")
else:
    print("Username is blocked")
```

**Output:**

```text
Username is not blocked
```

Here, `not in` checks whether the username is absent from the list.

### Why Are Membership Operators Important?

Membership operators are useful because many programs need to search for information.

For example:

- Checking whether a username exists.
- Checking whether a product is present in a shopping cart.
- Checking whether a number exists in a list.
- Checking whether a character is a vowel.
- Checking whether a file extension is allowed.
- Checking whether a student selected a particular subject.
- Checking whether a dictionary contains a particular key.
- Checking whether all required values are available.

Understanding membership operators also helps in Data Structures and Algorithms because searching and lookup operations are common in programming.

---

# 2. Learning Objectives

After completing this topic, you should be able to:

1. Understand the meaning of membership operators.
2. Identify the two membership operators in Python.
3. Understand how the `in` operator works.
4. Understand how the `not in` operator works.
5. Check characters inside strings.
6. Search for substrings inside strings.
7. Understand the difference between substring search and word search.
8. Check elements inside lists.
9. Check elements inside tuples.
10. Check elements inside sets.
11. Understand membership checking with dictionaries.
12. Check dictionary keys using `in`.
13. Check dictionary values using `.values()`.
14. Check key-value pairs using `.items()`.
15. Check numbers inside `range()`.
16. Understand case-sensitive string membership.
17. Perform case-insensitive membership checks.
18. Use membership expressions with `all()` and `any()`.
19. Understand membership checking with different data types.
20. Identify common membership-related errors.
21. Understand basic time complexity.
22. Apply membership checking to practical programming problems.
23. Understand how membership operators are used in DSA.
24. Solve the 12 interactive problems in the Python program.
25. Attempt all 10 additional practice questions independently.

---

# 3. Prerequisites

Before studying membership operators, you should understand the following Python concepts.

| Concept | Why It Is Required |
|---|---|
| Variables | To store the values being checked |
| Data types | To understand integers, strings, and Boolean values |
| Strings | To search for characters and substrings |
| Lists | To search through collections |
| Tuples | To understand membership in immutable sequences |
| Sets | To understand unique elements and fast lookup |
| Dictionaries | To check keys, values, and pairs |
| Conditional statements | To perform actions based on membership results |
| Functions | To organize the solved programs |
| Loops | To understand repeated searching operations |

You do not need advanced Python knowledge to understand this topic, but familiarity with these concepts will make learning easier.

---

# 4. What Are Membership Operators?

A membership operator checks whether a specified value is present inside another object.

### General Syntax

```python
value in collection
```

The `in` operator checks whether `value` exists inside `collection`.

```python
value not in collection
```

The `not in` operator checks whether `value` does not exist inside `collection`.

### Example

```python
numbers = [10, 20, 30, 40, 50]

result = 30 in numbers

print(result)
```

**Output:**

```text
True
```

### Explanation Step by Step

**Step 1:** Create a list.

```python
numbers = [10, 20, 30, 40, 50]
```

**Step 2:** Search for the value `30`.

```python
30 in numbers
```

**Step 3:** Python checks whether the value is present.

**Step 4:** Since `30` exists in the list, the expression returns `True`.

**Step 5:** The result is stored in `result`.

```python
result = True
```

**Step 6:** Print the result.

```text
True
```

### Important Point

Membership operators are expressions. They can be used:

- Directly inside `print()`.
- Inside an `if` statement.
- Inside a `while` statement.
- As part of a larger condition.
- Inside a list comprehension.
- With functions such as `all()` and `any()`.

Example:

```python
languages = ["Python", "Java", "C++"]

if "Python" in languages:
    print("Python is available")
```

---

# 5. Types of Membership Operators

Python has two membership operators.

## 5.1 `in` Operator

The `in` operator checks whether an element exists inside a collection.

**Syntax:**

```python
value in collection
```

Example:

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("grapes" in fruits)
```

**Output:**

```text
True
False
```

Explanation:

- `"banana"` exists in the list.
- `"grapes"` does not exist in the list.

Therefore, the first expression returns `True`, and the second returns `False`.

## 5.2 `not in` Operator

The `not in` operator checks whether an element is absent from a collection.

**Syntax:**

```python
value not in collection
```

Example:

```python
fruits = ["apple", "banana", "mango"]

print("grapes" not in fruits)
print("apple" not in fruits)
```

**Output:**

```text
True
False
```

Explanation:

- `"grapes"` is absent, so the first expression returns `True`.
- `"apple"` exists, so the second expression returns `False`.

## 5.3 Difference Between Both Operators

| `in` | `not in` |
|---|---|
| Checks presence | Checks absence |
| Returns `True` when found | Returns `True` when not found |
| Returns `False` when not found | Returns `False` when found |
| Used for searching | Used for exclusion checks |

### Example Showing Both Operators

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(20 not in numbers)

print(50 in numbers)
print(50 not in numbers)
```

**Output:**

```text
True
False
False
True
```

---

# 6. How Does the `in` Operator Work?

When Python evaluates a membership expression, it determines whether the given value is present in the specified object.

For example:

```python
students = ["Amaan", "Rahul", "Arjun"]

print("Rahul" in students)
```

Python checks the list elements for a matching value.

Conceptually, the search looks like this:

| Element Checked | Matches `"Rahul"`? |
|---|---|
| `"Amaan"` | No |
| `"Rahul"` | Yes |

Once a match is found, Python can finish the search.

The membership operation returns `True`.

### Conceptual Searching Process

```text
Start
  |
  v
Take the collection
  |
  v
Take the value to search
  |
  v
Check whether the value exists
  |
  +------ Found ------> True
  |
  +------ Not Found --> False
```

### Important Technical Note

Python supports membership testing through its membership protocol.

For ordinary built-in collections, Python uses the collection's membership behavior. Depending on the object, this may involve:

- A specialized membership operation.
- Iterating through elements and comparing them.
- Hash-based lookup.
- Arithmetic checking for ranges.

The exact implementation depends on the type of object.

---

# 7. Membership Operators with Strings

A string is a sequence of Unicode characters.

Membership operators can check whether a character or substring exists inside another string.

### Example

```python
message = "Python Programming"

print("Python" in message)
print("Programming" in message)
print("Java" in message)
```

**Output:**

```text
True
True
False
```

### Explanation

The string contains:

```text
Python Programming
```

The program performs three checks:

1. `"Python"` exists, so the result is `True`.
2. `"Programming"` exists, so the result is `True`.
3. `"Java"` does not exist, so the result is `False`.

### Practical Example: Search a Word in a Message

```python
message = "Welcome to Python programming"

word = "Python"

if word in message:
    print("Word found")
else:
    print("Word not found")
```

**Output:**

```text
Word found
```

### Important String Rules

1. String membership is case-sensitive.
2. The searched text must occur continuously.
3. Spaces are characters too.
4. Punctuation is treated as part of the string.
5. An empty string is considered a substring of every string.

---

# 8. Character Membership

Membership operators can check whether an individual character exists inside a string.

### Example 1: Check a Character

```python
name = "Amaan"

print("A" in name)
print("m" in name)
print("z" in name)
```

**Output:**

```text
True
True
False
```

### Explanation

The string `"Amaan"` contains the characters:

```text
A m a a n
```

- `A` exists.
- `m` exists.
- `z` does not exist.

### Example 2: Check Whether a Character Is a Vowel

```python
character = "e"

if character in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

**Output:**

```text
Vowel
```

### Explanation

The string `"aeiou"` contains the lowercase vowels:

```text
a e i o u
```

The program checks whether the entered character is part of that string.

### Example 3: Check Uppercase and Lowercase Characters

```python
character = "A"

vowels = "aeiou"

print(character in vowels)
print(character.lower() in vowels)
```

**Output:**

```text
False
True
```

The first expression fails because `"A"` is uppercase.

The second expression converts it to lowercase before checking.

### Practical Applications

Character membership is useful in:

- Vowel checking.
- Password validation.
- Character filtering.
- Input validation.
- Text processing.
- Basic lexical analysis.

---

# 9. Substring Membership

A substring is a continuous sequence of characters that occurs inside a larger string.

For example:

```text
Original string: Python Programming
Substring:       Programming
```

The word `"Programming"` is a substring of `"Python Programming"`.

### Example

```python
sentence = "Python is easy to learn"

print("Python" in sentence)
print("easy" in sentence)
print("learn" in sentence)
print("difficult" in sentence)
```

**Output:**

```text
True
True
True
False
```

### Example: Partial Matching

```python
text = "Programming"

print("Program" in text)
print("gram" in text)
print("ming" in text)
```

**Output:**

```text
True
True
True
```

### Why Does Partial Matching Work?

Python checks whether the requested sequence of characters appears continuously in the original string.

It does not require the searched substring to be a complete word.

### Example: Substring vs Complete Word

```python
sentence = "Python programming is useful"

print("program" in sentence)
print("programming" in sentence)
```

**Output:**

```text
True
True
```

The first expression returns `True` because `"program"` is part of `"programming"`.

### Checking Complete Words

To check whether a word is one of the whitespace-separated words, use `split()`.

```python
sentence = "Python programming is useful"

words = sentence.split()

print("program" in words)
print("programming" in words)
```

**Output:**

```text
False
True
```

### Limitation of Basic `split()`

Consider:

```python
sentence = "Python is useful."

words = sentence.split()

print(words)
print("useful" in words)
```

**Output:**

```text
['Python', 'is', 'useful.']
False
```

The full stop remains attached to the word.

For punctuation-independent word matching, the text must be normalized or tokenized appropriately.

---

# 10. Membership Operators with Lists

A list is an ordered and mutable collection.

Lists can contain:

- Integers.
- Floating-point numbers.
- Strings.
- Boolean values.
- Other collections.
- Objects of different types.

Membership operators can search for an element in a list.

### Example 1: String List

```python
fruits = ["apple", "banana", "mango", "orange"]

print("apple" in fruits)
print("mango" in fruits)
print("grapes" in fruits)
```

**Output:**

```text
True
True
False
```

### Example 2: Number List

```python
numbers = [10, 20, 30, 40, 50]

print(10 in numbers)
print(35 in numbers)
print(50 not in numbers)
```

**Output:**

```text
True
False
False
```

The final result is `False` because `50` exists in the list.

### Example 3: User Registration

```python
students = ["Amaan", "Rahul", "Arjun"]

name = "Rahul"

if name in students:
    print("Student is registered")
else:
    print("Student is not registered")
```

**Output:**

```text
Student is registered
```

### Example 4: Product Search

```python
shopping_cart = ["Laptop", "Mouse", "Keyboard"]

product = "Mouse"

if product in shopping_cart:
    print("Product is already in the cart")
else:
    print("Product is not in the cart")
```

**Output:**

```text
Product is already in the cart
```

### How Does List Membership Search Work?

For a list, Python generally checks elements one by one until it finds a match or reaches the end.

Suppose:

```python
numbers = [10, 20, 30, 40]
```

Searching for `30` conceptually involves:

| Step | Current Element | Result |
|---|---:|---|
| 1 | 10 | Not found |
| 2 | 20 | Not found |
| 3 | 30 | Found |

The membership expression returns `True`.

### Complexity

List membership has a worst-case time complexity of \(O(n)\), where \(n\) is the number of elements.

This is because Python may need to inspect every element.

---

# 11. Membership Operators with Tuples

A tuple is an ordered and immutable collection.

Membership checking works with tuples in the same general way as with lists.

### Example 1: String Tuple

```python
colors = ("red", "green", "blue")

print("red" in colors)
print("green" in colors)
print("yellow" in colors)
```

**Output:**

```text
True
True
False
```

### Example 2: Numeric Tuple

```python
numbers = (10, 20, 30, 40, 50)

print(20 in numbers)
print(100 not in numbers)
```

**Output:**

```text
True
True
```

### Example 3: Days of the Week

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

day = "Sunday"

if day in days:
    print("Valid day")
else:
    print("Invalid day")
```

**Output:**

```text
Valid day
```

### When Should You Use a Tuple?

Tuples are helpful when you have a fixed collection of values that should not be changed during normal program execution.

Examples include:

- Days of the week.
- Fixed menu options.
- Month names.
- Coordinates.
- Constant configuration choices.

### Complexity

Tuple membership is generally \(O(n)\) in the worst case because Python may need to compare elements one by one.

---

# 12. Membership Operators with Sets

A set is an unordered collection of unique, hashable elements.

Unlike lists and tuples, sets do not retain duplicate values.

### Example 1: Set Membership

```python
numbers = {10, 20, 30, 40, 50}

print(20 in numbers)
print(100 in numbers)
print(100 not in numbers)
```

**Output:**

```text
True
False
True
```

### Example 2: Duplicate Values

```python
fruits = {"apple", "banana", "apple", "mango"}

print(fruits)
print("apple" in fruits)
```

The set stores `"apple"` only once.

The displayed order of elements is not something a program should rely upon.

### Example 3: Check Allowed Choices

```python
allowed_roles = {"admin", "editor", "viewer"}

role = "editor"

if role in allowed_roles:
    print("Valid role")
else:
    print("Invalid role")
```

**Output:**

```text
Valid role
```

### Why Are Sets Useful for Membership Checking?

Sets use hashing to organize elements.

For hashable elements, set membership is typically average-case \(O(1)\).

This makes sets useful when a program needs to perform many repeated searches.

### Important Set Rule

Set elements must be hashable.

For example, integers and strings can be set elements.

Lists cannot be set elements because lists are mutable and unhashable.

```python
numbers = {1, 2, 3}

# This raises TypeError:
# print([1, 2] in numbers)
```

A tuple containing hashable elements can be used:

```python
pairs = {(1, 2), (3, 4)}

print((1, 2) in pairs)
```

**Output:**

```text
True
```

---

# 13. Membership Operators with Dictionaries

A dictionary stores values as key-value pairs.

Example:

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}
```

This dictionary contains:

| Key | Value |
|---|---|
| `"name"` | `"Amaan"` |
| `"age"` | `22` |
| `"course"` | `"Python"` |

When membership operators are used directly with a dictionary, Python checks its keys.

### Example

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

print("name" in student)
print("course" in student)
print("Amaan" in student)
```

**Output:**

```text
True
True
False
```

### Explanation

- `"name"` is a key.
- `"course"` is a key.
- `"Amaan"` is a value.

A direct membership test on the dictionary searches its keys.

### Practical Example: Checking a Student Field

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

key = "age"

if key in student:
    print("Value:", student[key])
else:
    print("Key not found")
```

**Output:**

```text
Value: 22
```

This is a useful pattern because it checks whether a key exists before accessing its value.

### Complexity

Dictionary key membership is typically average-case \(O(1)\), assuming normal hash behavior.

---

# 14. Dictionary Keys, Values, and Items

Python dictionaries provide three useful methods for inspecting their contents:

1. `.keys()`
2. `.values()`
3. `.items()`

Understanding these methods is essential for using membership operators correctly.

## 14.1 Checking Dictionary Keys

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

print("name" in student)
print("name" in student.keys())
```

**Output:**

```text
True
True
```

Both expressions check for a key.

The direct form `key in dictionary` is usually preferred because dictionaries already perform key membership checks by default.

## 14.2 Checking Dictionary Values

Use `.values()` to check whether a value exists.

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

print("Amaan" in student.values())
print(22 in student.values())
print("Java" in student.values())
```

**Output:**

```text
True
True
False
```

### Explanation

`student.values()` provides a dynamic view of the dictionary's values.

The membership operator checks whether the specified value occurs in that view.

Unlike dictionary key lookup, checking dictionary values generally requires scanning the values.

Its typical complexity is \(O(n)\).

## 14.3 Checking Dictionary Key-Value Pairs

Use `.items()` to check whether a particular pair exists.

```python
student = {
    "name": "Amaan",
    "age": 22
}

print(("name", "Amaan") in student.items())
print(("name", "Rahul") in student.items())
```

**Output:**

```text
True
False
```

The searched object is a tuple containing a key and its corresponding value.

### Complete Comparison

| Expression | Checks |
|---|---|
| `"name" in student` | Keys |
| `"name" in student.keys()` | Keys |
| `"Amaan" in student.values()` | Values |
| `("name", "Amaan") in student.items()` | Key-value pairs |

### Common Interview Question

**Question:** Does `"Amaan" in student` check whether `"Amaan"` is a value?

**Answer:** No. Direct membership checking on a dictionary checks keys. To check a value, use `student.values()`.

---

# 15. Membership Operators with Range

The `range()` function represents an arithmetic progression of integers.

Membership operators can check whether a particular integer belongs to that progression.

### Syntax

```python
range(start, stop, step)
```

| Parameter | Meaning |
|---|---|
| `start` | First value, included |
| `stop` | Boundary value, excluded |
| `step` | Difference between consecutive values |

### Example 1: Basic Range

```python
numbers = range(1, 11)

print(1 in numbers)
print(5 in numbers)
print(10 in numbers)
print(11 in numbers)
```

**Output:**

```text
True
True
True
False
```

The generated sequence is:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

The value `11` is excluded.

### Example 2: Range with Step

```python
even_numbers = range(2, 11, 2)

print(2 in even_numbers)
print(4 in even_numbers)
print(5 in even_numbers)
print(10 in even_numbers)
```

**Output:**

```text
True
True
False
True
```

The sequence contains:

```text
2, 4, 6, 8, 10
```

The number `5` is not present.

### Example 3: Odd Numbers

```python
odd_numbers = range(1, 12, 2)

print(7 in odd_numbers)
print(8 in odd_numbers)
```

**Output:**

```text
True
False
```

### Example 4: Inclusive User-Defined Range

The stop parameter of `range()` is exclusive.

To create a range that includes both the start and end values:

```python
start = 1
end = 10

numbers = range(start, end + 1)

print(10 in numbers)
```

**Output:**

```text
True
```

### Important Technical Note

For integer values, `range` membership can be checked efficiently through arithmetic conditions.

Python does not need to construct a complete list of all values in the range.

---

# 16. Case-Sensitive Membership

String membership is case-sensitive.

This means uppercase and lowercase letters are treated as different characters.

### Example

```python
language = "Python"

print("Python" in language)
print("python" in language)
print("PYTHON" in language)
```

**Output:**

```text
True
False
False
```

### Explanation

The string contains:

```text
Python
```

The first search matches the exact letter sequence.

The other two searches use different capitalization.

### Another Example

```python
username = "Amaan"

print("Amaan" in username)
print("amaan" in username)
print("AMAAN" in username)
```

**Output:**

```text
True
False
False
```

### Why Does This Matter?

Imagine a program storing registered usernames.

Without normalization:

```python
registered_users = ["amaan", "rahul", "arjun"]

username = "AMAAN"

print(username in registered_users)
```

The result is `False`.

The entered username differs in case from the stored username.

If the application intends case-insensitive matching, the strings must be normalized before checking.

---

# 17. Case-Insensitive Membership

Case-insensitive membership means comparing text without treating uppercase and lowercase characters as different.

Python provides methods such as:

- `lower()`
- `casefold()`

## 17.1 Using `lower()`

```python
registered_users = ["amaan", "rahul", "arjun"]

username = "AMAAN"

if username.lower() in registered_users:
    print("User found")
else:
    print("User not found")
```

**Output:**

```text
User found
```

### Explanation

The expression:

```python
username.lower()
```

converts `"AMAAN"` into `"amaan"`.

The normalized value matches the value stored in the list.

## 17.2 Using `casefold()`

```python
registered_users = {"amaan", "rahul", "arjun"}

username = "AMAAN"

normalized_users = {
    user.casefold()
    for user in registered_users
}

if username.casefold() in normalized_users:
    print("User found")
else:
    print("User not found")
```

**Output:**

```text
User found
```

### Difference Between `lower()` and `casefold()`

| `lower()` | `casefold()` |
|---|---|
| Converts text to lowercase | Performs more comprehensive case normalization |
| Suitable for many ordinary comparisons | Useful for Unicode-aware case-insensitive matching |
| General lowercase conversion | Designed for caseless matching |

### Important Point

Case normalization does not automatically:

- Remove spaces.
- Remove punctuation.
- Correct spelling.
- Remove accents.
- Make different words equivalent.

For example:

```python
text = " Python "

print("python" in text.casefold())
```

The result is `False` because the original string contains spaces around `"Python"`.

To ignore surrounding spaces:

```python
text = " Python "

print("python" in text.strip().casefold())
```

**Output:**

```text
True
```

---

# 18. Membership with `all()` and `any()`

Python provides two useful built-in functions:

- `all()`
- `any()`

These functions can be combined with membership expressions.

## 18.1 The `all()` Function

The `all()` function returns `True` when every item in an iterable evaluates to `True`.

### Syntax

```python
all(iterable)
```

### Example

```python
required_subjects = ["Python", "DSA", "Database"]

available_subjects = [
    "Python",
    "DSA",
    "Database",
    "Networking"
]

result = all(
    subject in available_subjects
    for subject in required_subjects
)

print(result)
```

**Output:**

```text
True
```

### Explanation Step by Step

Required subjects:

```text
Python
DSA
Database
```

Available subjects:

```text
Python
DSA
Database
Networking
```

Python evaluates the membership condition for every required subject:

| Subject | Available? |
|---|---|
| Python | True |
| DSA | True |
| Database | True |

All three checks return `True`.

Therefore, `all()` returns `True`.

### When One Subject Is Missing

```python
required_subjects = ["Python", "DSA", "Database"]

available_subjects = ["Python", "DSA"]

result = all(
    subject in available_subjects
    for subject in required_subjects
)

print(result)
```

**Output:**

```text
False
```

The `"Database"` subject is missing, so not all required conditions are true.

## 18.2 The `any()` Function

The `any()` function returns `True` when at least one item in an iterable evaluates to `True`.

### Example

```python
available_roles = ["Developer", "Tester", "Designer"]

preferred_roles = ["Developer", "Data Analyst"]

result = any(
    role in available_roles
    for role in preferred_roles
)

print(result)
```

**Output:**

```text
True
```

The preferred role `"Developer"` is available.

Therefore, at least one membership condition is true.

## 18.3 Difference Between `all()` and `any()`

| `all()` | `any()` |
|---|---|
| Every condition must be true | At least one condition must be true |
| Stops when it finds a false item | Stops when it finds a true item |
| Useful for checking all requirements | Useful for checking alternative choices |

### Important Advanced Point

Both `all()` and `any()` use short-circuit evaluation.

They do not need to evaluate every item after the final answer is already known.

---

# 19. Membership Operator Truth Table

Membership operators return opposite Boolean results for the same membership condition.

| Value Exists? | `value in collection` | `value not in collection` |
|---|---|---|
| Yes | `True` | `False` |
| No | `False` | `True` |

### Example

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("Python" not in languages)

print("Ruby" in languages)
print("Ruby" not in languages)
```

**Output:**

```text
True
False
False
True
```

### Remember

`not in` does not mean that the collection is empty.

It means only that the specified value was not found.

---

# 20. Word Search vs Substring Search

This difference is especially important for text-processing programs.

Consider:

```python
sentence = "Python programming is useful"
```

### Substring Search

```python
print("program" in sentence)
```

**Output:**

```text
True
```

The substring `"program"` is part of `"programming"`.

### Exact Word Search

```python
words = sentence.split()

print("program" in words)
print("programming" in words)
```

**Output:**

```text
False
True
```

Here, the program searches individual whitespace-separated tokens.

### Example with Punctuation

```python
sentence = "Python is useful."

words = sentence.split()

print(words)
print("useful" in words)
print("useful." in words)
```

**Output:**

```text
['Python', 'is', 'useful.']
False
True
```

### Important Lesson

Use string membership to search for substrings.

Use tokenized collections when you need to search for complete tokens.

For production text processing, use suitable normalization and tokenization rules that match the language and requirements.

---

# 21. Membership Operators with Different Data Types

Membership operators work with many built-in Python objects.

| Type | Example | Result |
|---|---|---|
| String | `"Py" in "Python"` | `True` |
| List | `10 in [10, 20, 30]` | `True` |
| Tuple | `10 in (10, 20, 30)` | `True` |
| Set | `10 in {10, 20, 30}` | `True` |
| Dictionary | `"name" in student` | Depends on keys |
| Dictionary values | `"Amaan" in student.values()` | Depends on values |
| Range | `5 in range(1, 10)` | `True` |

### Type Matching Matters

```python
numbers = [10, 20, 30]

print(10 in numbers)
print("10" in numbers)
```

**Output:**

```text
True
False
```

The integer `10` and the string `"10"` are different objects with different values.

Python does not automatically convert the string into an integer during membership testing.

### Another Example

```python
values = [True, False]

print(1 in values)
print(0 in values)
```

Python considers Boolean values closely related to integers:

```text
True
True
```

This is a useful reminder that Python equality and membership follow the equality behavior of the objects involved.

---

# 22. Membership Operators and Comparison Operators

Membership operators and comparison operators perform different tasks.

### Membership Operators

They check whether an element exists inside a collection.

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

### Comparison Operators

They compare two values.

```python
a = 10
b = 20

print(a == b)
print(a < b)
print(a > b)
```

Output:

```text
False
True
False
```

### Difference

| Membership Operators | Comparison Operators |
|---|---|
| `in` | `==` |
| `not in` | `!=` |
| Check presence or absence | Compare two values |
| Work with supported containers and objects | Compare values using their comparison behavior |

### Combined Example

```python
numbers = [10, 20, 30]

result = 20 in numbers and 10 < 15

print(result)
```

Output:

```text
True
```

The first condition checks membership.

The second condition compares two numbers.

The logical operator `and` combines the results.

---

# 23. Membership Operators and Logical Operators

Logical operators combine or reverse conditions.

Python provides:

- `and`
- `or`
- `not`

Membership operators answer whether an element exists in a collection.

### Example

```python
subjects = ["Python", "DSA", "Database"]

condition1 = "Python" in subjects
condition2 = "DSA" in subjects

print(condition1 and condition2)
```

**Output:**

```text
True
```

### Explanation

- The first membership check returns `True`.
- The second membership check returns `True`.
- The `and` operator requires both conditions to be true.

Therefore, the final result is `True`.

### Combined `or` Example

```python
languages = ["Python", "Java"]

if "Python" in languages or "C++" in languages:
    print("At least one language is available")
```

**Output:**

```text
At least one language is available
```

At least one of the two membership conditions is true.

---

# 24. Membership Operators and Identity Operators

Membership and identity operators look similar in purpose, but they answer different questions.

| Membership | Identity |
|---|---|
| `in` | `is` |
| `not in` | `is not` |
| Checks whether an element exists | Checks whether references point to the same object |

### Membership Example

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

### Identity Example

```python
first = [10, 20, 30]
second = first
third = [10, 20, 30]

print(first is second)
print(first is third)
```

Output:

```text
True
False
```

`first` and `second` refer to the same list object.

`first` and `third` contain equal values but refer to different list objects.

Identity operators will be covered in the next topic.

---

# 25. Membership Operator Precedence

Membership operators belong to Python's comparison-operator group.

They have the same general precedence as comparison operators such as:

- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`

Logical operators have lower precedence.

The relevant logical order is:

1. `not`
2. `and`
3. `or`

### Example

```python
numbers = [10, 20, 30]

result = 20 in numbers and 10 < 15

print(result)
```

**Output:**

```text
True
```

### Recommended Style

Use parentheses when a condition contains several operators.

```python
result = (20 in numbers) and (10 < 15)
```

Parentheses make the intended grouping easier to read.

A complete explanation of operator precedence will appear in the Expressions section of this repository.

---

# 26. Important Rules and Edge Cases

## Rule 1: String Membership Is Case-Sensitive

```python
print("python" in "Python")
```

Output:

```text
False
```

## Rule 2: Dictionary Membership Checks Keys

```python
student = {"name": "Amaan"}

print("name" in student)
print("Amaan" in student)
```

Output:

```text
True
False
```

## Rule 3: Use `.values()` to Check Dictionary Values

```python
student = {"name": "Amaan"}

print("Amaan" in student.values())
```

Output:

```text
True
```

## Rule 4: Empty String Is a Substring of Every String

```python
print("" in "Python")
print("" in "")
```

Output:

```text
True
True
```

## Rule 5: Range Stop Is Exclusive

```python
numbers = range(1, 5)

print(4 in numbers)
print(5 in numbers)
```

Output:

```text
True
False
```

## Rule 6: Sets Require Hashable Elements

```python
numbers = {1, 2, 3}

# This raises TypeError:
# print([1, 2] in numbers)
```

A list is unhashable, so it cannot be searched as a set element.

## Rule 7: Membership Does Not Normally Modify a Collection

```python
numbers = [10, 20, 30]

result = 20 in numbers

print(numbers)
print(result)
```

Output:

```text
[10, 20, 30]
True
```

The list remains unchanged.

## Rule 8: A Generator May Be Consumed

Membership checks on iterators and generators can consume elements while searching.

Example:

```python
numbers = (value for value in range(5))

print(3 in numbers)
print(list(numbers))
```

Output:

```text
True
[4]
```

The generator produced `0`, `1`, `2`, and `3` during the search.

Only `4` remains.

Do not assume that an iterator is unchanged after membership testing.

## Rule 9: Not Every Object Supports Membership

Membership requires a supported membership behavior or an iterable.

For example, attempting membership against an ordinary integer raises `TypeError`:

```python
# This raises TypeError:
# print(10 in 100)
```

An integer is not a collection or iterable that supports this membership check.

---

# 27. Time Complexity of Membership Operators

Time complexity depends on the type of collection.

| Collection | Typical Membership Complexity |
|---|---|
| List | \(O(n)\) worst case |
| Tuple | \(O(n)\) worst case |
| Set | Average \(O(1)\) |
| Dictionary keys | Average \(O(1)\) |
| Dictionary values | \(O(n)\) |
| Dictionary items | Typically \(O(n)\) for a particular pair |
| Integer range membership | Efficient arithmetic check |
| String | Depends on the searching algorithm and input |

### 27.1 List Membership

Consider:

```python
numbers = [10, 20, 30, 40, 50]

print(50 in numbers)
```

Python may need to check every element before finding the last value.

For a list of \(n\) elements, worst-case membership checking is \(O(n)\).

### 27.2 Set Membership

```python
numbers = {10, 20, 30, 40, 50}

print(50 in numbers)
```

Sets use hashing to support efficient lookup.

Average-case membership is \(O(1)\), although collisions and unusual hashing behavior can affect performance.

### 27.3 Dictionary Key Membership

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

print("age" in student)
```

Dictionary key lookup is typically average-case \(O(1)\).

### 27.4 Dictionary Value Membership

```python
print("Amaan" in student.values())
```

Checking values usually requires searching through the values.

Its typical complexity is \(O(n)\).

### 27.5 Why Does This Matter?

Imagine checking whether 100,000 usernames exist.

Repeatedly searching through a list may be much slower than using a set.

The correct collection can improve performance significantly.

---

# 28. Practical Applications of Membership Operators

Membership operators are widely used in real-world applications.

## 28.1 Login and Registration Systems

A program can check whether a username is registered.

```python
registered_users = {"amaan", "rahul", "arjun"}

username = "rahul"

if username in registered_users:
    print("Account found")
else:
    print("Account not found")
```

## 28.2 Access Control

A program can check whether a role belongs to the permitted roles.

```python
allowed_roles = {"admin", "editor", "viewer"}

role = "editor"

if role in allowed_roles:
    print("Role is permitted")
else:
    print("Role is not permitted")
```

## 28.3 Shopping Cart

```python
cart = ["Laptop", "Mouse", "Keyboard"]

product = "Mouse"

if product in cart:
    print("Product already exists")
else:
    print("Add product to cart")
```

## 28.4 Student Subject Registration

```python
available_subjects = ["Python", "DSA", "Database"]

subject = "DSA"

if subject in available_subjects:
    print("Subject is available")
else:
    print("Subject is not available")
```

## 28.5 File Extension Validation

```python
filename = "notes.pdf"

allowed_extensions = {"py", "txt", "md", "pdf"}

extension = filename.rsplit(".", 1)[-1].lower()

if extension in allowed_extensions:
    print("Allowed file type")
else:
    print("Unsupported file type")
```

**Output:**

```text
Allowed file type
```

For production file validation, extension checks alone are not sufficient to verify the actual contents or safety of a file.

## 28.6 Form Validation

```python
allowed_choices = {"Yes", "No"}

answer = "Yes"

if answer in allowed_choices:
    print("Valid answer")
else:
    print("Invalid answer")
```

## 28.7 Data Cleaning

```python
invalid_values = {"", "unknown", "n/a", "null"}

value = "unknown"

if value.casefold() in invalid_values:
    print("Invalid data")
else:
    print("Valid data")
```

---

# 29. Twelve Examples Explained

The Python program `01_membership_operators.py` contains twelve examples.

Each example demonstrates one important membership concept.

## Example 1: `in` with String

**Objective:** Check whether a substring exists inside a string.

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
```

**Output:**

```text
True
False
```

**Step-by-step explanation:**

1. Create a string named `text`.
2. Search for `"Python"`.
3. Python finds the substring.
4. Search for `"Java"`.
5. Python cannot find that substring.

**Concept learned:** String membership using `in`.

## Example 2: `not in` with String

**Objective:** Check whether a substring is absent.

```python
text = "Hello World"

print("Python" not in text)
print("Hello" not in text)
```

**Output:**

```text
True
False
```

**Explanation:**

- `"Python"` is absent.
- `"Hello"` is present.

**Concept learned:** Non-membership checking.

## Example 3: `in` with List

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
```

**Output:**

```text
True
```

The value exists in the list.

**Concept learned:** List membership.

## Example 4: `not in` with List

```python
numbers = [10, 20, 30, 40]

print(50 not in numbers)
```

**Output:**

```text
True
```

The number `50` does not exist in the list.

**Concept learned:** Exclusion checking.

## Example 5: `in` with Tuple

```python
colors = ("red", "green", "blue")

print("green" in colors)
```

**Output:**

```text
True
```

The value exists in the tuple.

**Concept learned:** Tuple membership.

## Example 6: `in` with Set

```python
numbers = {10, 20, 30}

print(20 in numbers)
```

**Output:**

```text
True
```

The number exists in the set.

**Concept learned:** Set membership.

## Example 7: Dictionary Key Membership

```python
student = {
    "name": "Amaan",
    "age": 22
}

print("name" in student)
```

**Output:**

```text
True
```

The expression checks dictionary keys.

**Concept learned:** Dictionary key membership.

## Example 8: Dictionary Value Membership

```python
student = {
    "name": "Amaan",
    "age": 22
}

print("Amaan" in student.values())
```

**Output:**

```text
True
```

The expression checks dictionary values.

**Concept learned:** `.values()`.

## Example 9: Membership with Range

```python
numbers = range(1, 11)

print(5 in numbers)
print(15 in numbers)
```

**Output:**

```text
True
False
```

The first value is inside the range; the second is not.

**Concept learned:** Membership in integer ranges.

## Example 10: Case-Sensitive Membership

```python
language = "Python"

print("Python" in language)
print("python" in language)
```

**Output:**

```text
True
False
```

The second expression returns `False` because capitalization differs.

**Concept learned:** Case sensitivity.

## Example 11: Character Membership

```python
vowels = "aeiou"

print("a" in vowels)
print("z" in vowels)
```

**Output:**

```text
True
False
```

The program checks whether the characters exist in the vowel string.

**Concept learned:** Character search.

## Example 12: Membership with `all()`

```python
required_subjects = ["Python", "DSA"]

available_subjects = ["Python", "DSA", "Database"]

result = all(
    subject in available_subjects
    for subject in required_subjects
)

print(result)
```

**Output:**

```text
True
```

Both required subjects are available.

**Concept learned:** Combining membership checks with `all()`.

---

# 30. Twelve Solved Problems

The Python file contains twelve interactive solved problems.

Every problem has a practical purpose and helps you understand how membership operators work with different data structures.

## Problem 1: Check Whether a Character Exists in a String

**Problem statement:**

Take a string and a single character from the user. Check whether the character exists in the given string.

### Example

```text
Enter a string: Python
Enter a character: P

Character found.
```

### Logic

1. Read a string from the user.
2. Read the character to search for.
3. Validate that the entered search value contains exactly one character.
4. Use the `in` operator.
5. Display the result.

### Code

```python
text = "Python"

character = "P"

if character in text:
    print("Character found")
else:
    print("Character not found")
```

### Output

```text
Character found
```

### Dry Run

| Variable | Value |
|---|---|
| `text` | `"Python"` |
| `character` | `"P"` |
| Membership expression | `"P" in "Python"` |
| Result | `True` |

### Complexity

For a string of length \(n\), membership checking depends on the string-search implementation and input.

---

## Problem 2: Check Whether a Substring Exists

**Problem statement:**

Take a sentence and a word or substring from the user. Check whether the entered text exists inside the sentence.

### Example

```text
Enter a sentence: Python is easy to learn
Enter text to search: easy

Substring found.
```

### Logic

1. Read the complete sentence.
2. Read the text to search.
3. Apply `search_text in sentence`.
4. Print the appropriate message.

### Code

```python
sentence = "Python is easy to learn"

search_text = "easy"

if search_text in sentence:
    print("Substring found")
else:
    print("Substring not found")
```

### Output

```text
Substring found
```

### Dry Run

```text
Sentence: Python is easy to learn
Search:   easy

Is "easy" present?
Yes

Result: True
```

### Important Note

This checks substring membership, not complete-word membership.

---

## Problem 3: Check Whether an Item Exists in a List

**Problem statement:**

Create a list of fruits. Ask the user for a fruit name and check whether that fruit exists in the list.

### Code

```python
fruits = ["apple", "banana", "mango", "orange"]

fruit = "mango"

if fruit in fruits:
    print("Fruit is available")
else:
    print("Fruit is not available")
```

**Output:**

```text
Fruit is available
```

### Logic

1. Create the predefined list.
2. Read the fruit name.
3. Search the list using `in`.
4. Display whether the fruit is available.

### Dry Run

| Search | Present? |
|---|---|
| apple | Yes |
| banana | Yes |
| mango | Yes |
| grapes | No |

### Complexity

Worst-case list membership: \(O(n)\).

---

## Problem 4: Check Whether an Item Is Not in a Blocked List

**Problem statement:**

Create a list of blocked items and check whether a user-entered item is not included in that list.

### Code

```python
blocked_items = ["spam", "fraud", "malware"]

item = "normal"

if item not in blocked_items:
    print("Item is not blocked")
else:
    print("Item is blocked")
```

**Output:**

```text
Item is not blocked
```

### Logic

1. Store blocked values.
2. Read an item.
3. Use the `not in` operator.
4. If it is absent, display that it is not blocked.
5. Otherwise, display that it is blocked.

### Dry Run

```text
blocked_items = ["spam", "fraud", "malware"]
item = "normal"

"normal" not in blocked_items

True
```

### Concept Learned

The `not in` operator is useful for checking exclusions.

---

## Problem 5: Check Membership in a Tuple

**Problem statement:**

Create a tuple of numbers and check whether a user-entered number belongs to it.

### Code

```python
values = (10, 20, 30, 40, 50)

number = 30

if number in values:
    print("Number found")
else:
    print("Number not found")
```

**Output:**

```text
Number found
```

### Logic

1. Create a tuple.
2. Read a number.
3. Search using `in`.
4. Display the result.

### Concept Learned

Tuple membership works similarly to list membership.

---

## Problem 6: Check Membership in a Set

**Problem statement:**

Create a set of numbers and check whether a user-entered value exists in the set.

### Code

```python
numbers = {10, 20, 30, 40, 50}

number = 20

if number in numbers:
    print("Number exists in set")
else:
    print("Number does not exist")
```

**Output:**

```text
Number exists in set
```

### Logic

1. Create a set.
2. Read the input value.
3. Check membership.
4. Display the result.

### Concept Learned

Sets are useful for repeated membership checks because they generally provide average-case \(O(1)\) lookup for hashable values.

---

## Problem 7: Check Whether a Key Exists in a Dictionary

**Problem statement:**

Create a student dictionary and ask the user for a key. Check whether the key exists. If it exists, display its associated value.

### Code

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

key = "name"

if key in student:
    print("Key found")
    print("Value:", student[key])
else:
    print("Key not found")
```

**Output:**

```text
Key found
Value: Amaan
```

### Logic

1. Create a dictionary.
2. Read the key.
3. Check whether the key exists in the dictionary.
4. If found, access the corresponding value.
5. Otherwise, display an error message.

### Dry Run

| Key | Exists? |
|---|---|
| name | Yes |
| age | Yes |
| course | Yes |
| address | No |

### Important Point

Direct dictionary membership checks keys.

---

## Problem 8: Check Whether a Value Exists in a Dictionary

**Problem statement:**

Create a student dictionary and check whether an entered value exists among the dictionary's values.

### Code

```python
student = {
    "name": "Amaan",
    "age": 22,
    "course": "Python"
}

value = "Amaan"

if value in student.values():
    print("Value found")
else:
    print("Value not found")
```

**Output:**

```text
Value found
```

### Logic

1. Create the dictionary.
2. Read a value.
3. Use `.values()` to obtain the values view.
4. Search that view using `in`.
5. Display the result.

### Important Difference

```python
value in student
```

checks keys.

```python
value in student.values()
```

checks values.

---

## Problem 9: Check Whether a Number Belongs to a Range

**Problem statement:**

Take a starting number, an ending number, and a value from the user. Check whether the value belongs to the inclusive range.

### Code

```python
start = 1
stop = 10
number = 5

if start > stop:
    print("Invalid range")
else:
    numbers = range(start, stop + 1)

    if number in numbers:
        print("Number belongs to the range")
    else:
        print("Number does not belong to the range")
```

**Output:**

```text
Number belongs to the range
```

### Logic

1. Read the start value.
2. Read the ending value.
3. Read the number to search.
4. Validate that the start is not greater than the stop.
5. Create `range(start, stop + 1)`.
6. Check membership.

### Why Is `stop + 1` Used?

Python's range excludes its stop value.

For an inclusive range from 1 to 10, we use:

```python
range(1, 11)
```

The generated sequence includes 10.

---

## Problem 10: Check Whether a File Extension Is Allowed

**Problem statement:**

Take a filename and check whether its extension belongs to the allowed extensions.

Allowed extensions:

```text
py
txt
md
pdf
```

### Code

```python
filename = "notes.PDF"

allowed_extensions = {"py", "txt", "md", "pdf"}

if "." not in filename or filename.endswith("."):
    print("No valid extension")
else:
    extension = filename.rsplit(".", 1)[-1].lower()

    if extension in allowed_extensions:
        print("Allowed file extension")
    else:
        print("Unsupported file extension")
```

**Output:**

```text
Allowed file extension
```

### Logic

1. Read the filename.
2. Check whether it has a usable extension.
3. Use `rsplit(".", 1)` to separate the final extension.
4. Convert the extension to lowercase.
5. Check the extension against the allowed set.
6. Display the result.

### Why Use `rsplit()`?

A filename can contain multiple dots.

For example:

```text
project.final.version.py
```

Using:

```python
filename.rsplit(".", 1)
```

splits at the last dot only.

### Why Use `lower()`?

The program should treat `.PDF` and `.pdf` as the same extension.

### Limitation

This checks the filename extension only. It does not verify the actual content or safety of the file.

---

## Problem 11: Case-Insensitive Username Lookup

**Problem statement:**

Create a set of registered usernames and check whether the entered username exists without considering letter case.

### Code

```python
registered_users = {"amaan", "rahul", "arjun"}

username = "AMAAN"

normalized_users = {
    user.casefold()
    for user in registered_users
}

if username.casefold() in normalized_users:
    print("Username is registered")
else:
    print("Username is not registered")
```

**Output:**

```text
Username is registered
```

### Logic

1. Create a set of registered users.
2. Read the username.
3. Normalize all stored usernames using `casefold()`.
4. Normalize the entered username.
5. Check membership in the normalized set.
6. Display the result.

### Dry Run

| Original Username | Normalized Username |
|---|---|
| amaan | amaan |
| rahul | rahul |
| arjun | arjun |
| AMAAN | amaan |

The normalized username exists in the set.

### Complexity

- Creating the normalized set requires processing the stored usernames.
- Checking membership in the resulting set is typically average-case \(O(1)\).

The full program performs the normalization before the check; it is not just a single lookup operation.

---

## Problem 12: Check Whether All Required Subjects Are Available

**Problem statement:**

Take a list of subjects from the user and check whether all required subjects are available.

Required subjects:

```text
Python
DSA
Database
```

### Code

```python
required_subjects = {"python", "dsa", "database"}

entered_subjects = ["Python", "DSA", "Database", "Networking"]

available_subjects = {
    subject.casefold()
    for subject in entered_subjects
}

missing_subjects = required_subjects - available_subjects

if not missing_subjects:
    print("All required subjects are available")
else:
    print("Missing subjects:", missing_subjects)
```

**Output:**

```text
All required subjects are available
```

### Logic

1. Store the required subjects in a set.
2. Read the available subject names.
3. Normalize the names using `casefold()`.
4. Convert the normalized values into a set.
5. Find the missing subjects using set difference.
6. If the missing set is empty, all subjects are available.
7. Otherwise, display the missing subjects.

### Understanding Set Difference

```python
required_subjects - available_subjects
```

This produces the elements that are present in `required_subjects` but absent from `available_subjects`.

### Example with Missing Subjects

```python
required_subjects = {"python", "dsa", "database"}

available_subjects = {"python", "dsa"}

missing_subjects = required_subjects - available_subjects

print(missing_subjects)
```

**Output:**

```text
{'database'}
```

### Important Implementation Detail

The interactive program uses normalized sets and set difference to find missing subjects. This is an additional set operation that builds on the membership concepts studied in this topic.

---

# 31. Ten Unsolved Practice Questions

Try to solve these problems independently before viewing other solutions.

For every question:

1. Understand the problem statement.
2. Identify the appropriate data type.
3. Decide whether `in` or `not in` is needed.
4. Write the program.
5. Test at least one positive case.
6. Test at least one negative case.
7. Explain the logic in your own words.

| No. | Problem | Hint |
|---|---|---|
| 1 | Check whether a character exists in a string. | Use `in` |
| 2 | Check whether a word or substring exists in a sentence. | String membership |
| 3 | Check whether an element exists in a list. | List membership |
| 4 | Check whether an unwanted item is absent from a list. | Use `not in` |
| 5 | Check whether a number exists in a tuple. | Tuple membership |
| 6 | Check whether an element exists in a set. | Set membership |
| 7 | Check whether a key exists in a dictionary. | Direct dictionary membership |
| 8 | Check whether a value exists in a dictionary. | Use `.values()` |
| 9 | Check whether a number belongs to a range. | Use `range()` |
| 10 | Check whether all required subjects are available. | Use `all()` or set difference |

## Additional Challenge Problems

These are optional problems for additional practice.

### Challenge 1: Vowel Checker

Take one character and determine whether it is a vowel.

### Challenge 2: Email Domain Checker

Check whether an email address belongs to one of the allowed domains.

### Challenge 3: Shopping Cart Search

Check whether a product is already present in a shopping cart.

### Challenge 4: Username Search

Perform a case-insensitive username search using a set.

### Challenge 5: Duplicate Detection

Use a set to identify duplicate values in a list.

### Challenge 6: Allowed File Extension

Check whether a filename has a supported extension.

### Challenge 7: Required Skills

Check whether a candidate possesses all required skills.

### Challenge 8: Blocked Words

Check whether a sentence contains any word from a blocked-word collection.

### Challenge 9: Valid Menu Choice

Check whether a user's menu selection belongs to a collection of valid choices.

### Challenge 10: Two Sum

Use set membership to find a pair of numbers whose sum equals a target.

---

# 32. Common Mistakes and Their Solutions

Understanding mistakes is as important as understanding correct syntax.

## Mistake 1: Checking a Dictionary Value Directly

Incorrect:

```python
student = {"name": "Amaan"}

print("Amaan" in student)
```

Output:

```text
False
```

Why?

Because direct dictionary membership checks keys.

Correct:

```python
print("Amaan" in student.values())
```

Output:

```text
True
```

## Mistake 2: Ignoring String Case

Incorrect assumption:

```python
print("python" in "Python")
```

Some beginners expect `True`.

Actual output:

```text
False
```

Correct for case-insensitive checking:

```python
print("python".casefold() in "Python".casefold())
```

Output:

```text
True
```

## Mistake 3: Confusing Substring and Complete Word Search

```python
text = "programming"

print("program" in text)
```

Output:

```text
True
```

The searched substring exists inside the larger word.

For complete whitespace-separated words, use a tokenized collection.

## Mistake 4: Forgetting the Exclusive Range Stop

Incorrect expectation:

```python
numbers = range(1, 5)

print(5 in numbers)
```

Actual output:

```text
False
```

Correct inclusive range:

```python
numbers = range(1, 6)

print(5 in numbers)
```

Output:

```text
True
```

## Mistake 5: Searching with the Wrong Data Type

```python
numbers = [10, 20, 30]

print("10" in numbers)
```

Output:

```text
False
```

The string `"10"` is not the integer `10`.

Convert input to the correct data type when numerical comparison is intended.

## Mistake 6: Treating a Set Like a List

Sets do not support indexing.

Incorrect:

```python
numbers = {10, 20, 30}

# print(numbers[0])
```

Use membership for existence checks rather than indexing.

## Mistake 7: Assuming Sets Preserve Display Order

The order in which a set displays elements should not be relied upon.

Use a list or tuple when order matters.

## Mistake 8: Forgetting the Empty String Edge Case

```python
print("" in "Python")
```

Output:

```text
True
```

An empty string is considered present as a substring.

## Mistake 9: Using an Unhashable Item in a Set Membership Check

```python
numbers = {1, 2, 3}

# print([1, 2] in numbers)
```

This raises `TypeError`.

Use an appropriate hashable representation when checking membership in a set.

## Mistake 10: Assuming Membership Always Takes Constant Time

List membership is generally \(O(n)\) in the worst case.

For repeated lookups, consider whether a set or dictionary is a better choice.

## Mistake 11: Forgetting `.lower()` or `.casefold()` on Both Sides

Normalize both the searched text and the stored text when case-insensitive matching is required.

## Mistake 12: Assuming Membership Changes the Collection

A normal membership expression does not add or remove elements.

For example:

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(numbers)
```

The list remains unchanged.

---

# 33. Best Practices

Follow these practices while writing Python programs.

1. Use `in` when checking whether an element exists.
2. Use `not in` when checking whether an element is absent.
3. Use `.values()` to search dictionary values.
4. Use `.items()` to check dictionary key-value pairs.
5. Use sets for repeated membership checks when appropriate.
6. Use lists when order and repeated values matter.
7. Use tuples for fixed collections.
8. Normalize text for case-insensitive comparisons.
9. Use `casefold()` for comprehensive Unicode-aware caseless matching.
10. Use tokenization when searching for complete words.
11. Remember that `range()` excludes the stop value.
12. Validate user input before processing it.
13. Use meaningful variable names.
14. Keep membership expressions readable.
15. Select a data structure according to the operation you need.
16. Consider performance when working with large collections.
17. Test both positive and negative membership cases.
18. Do not assume dictionary membership searches values.
19. Be aware that generator membership checks can consume elements.
20. Add clear messages for unsuccessful searches.

---

# 34. Debugging and Troubleshooting

When a membership expression produces an unexpected result, follow these steps.

## Step 1: Print the Collection

```python
print(collection)
```

Make sure the collection contains the values you expect.

## Step 2: Print the Value Being Searched

```python
print(value)
```

Check for unexpected spaces, capitalization, or punctuation.

## Step 3: Check the Data Types

```python
print(type(value))
print(type(collection))
```

For example, user input is normally returned as a string.

If you intend to search for an integer, convert the input first.

## Step 4: Check String Normalization

```python
print(value.casefold())
print(text.casefold())
```

Verify that both sides are normalized.

## Step 5: Inspect Dictionary Keys and Values

```python
print(dictionary.keys())
print(dictionary.values())
```

Make sure you are checking the correct part of the dictionary.

## Step 6: Inspect Range Boundaries

```python
print(list(range(1, 6)))
```

Verify the exact values in the range.

## Step 7: Test a Known Positive Value

Use a value that you know exists.

## Step 8: Test a Known Negative Value

Use a value that you know does not exist.

## Step 9: Check for Whitespace

```python
text = " Python "

print(repr(text))
print(text.strip())
```

The `repr()` function makes leading and trailing spaces easier to notice.

## Step 10: Check Whether an Iterator Was Consumed

If you are checking membership in a generator, remember that the generator may have advanced during the operation.

---

# 35. Practice Test

Attempt these questions before reading the answer key.

## Question 1

What is the output?

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

## Question 2

What is the output?

```python
numbers = [10, 20, 30]

print(40 not in numbers)
```

## Question 3

What is the output?

```python
text = "Python"

print("P" in text)
```

## Question 4

What is the output?

```python
text = "Python"

print("python" in text)
```

## Question 5

What is the output?

```python
student = {"name": "Amaan", "age": 22}

print("Amaan" in student)
```

## Question 6

What is the output?

```python
student = {"name": "Amaan", "age": 22}

print("Amaan" in student.values())
```

## Question 7

What is the output?

```python
numbers = range(1, 6)

print(6 in numbers)
```

## Question 8

What is the output?

```python
colors = ("red", "green", "blue")

print("yellow" not in colors)
```

## Question 9

What is the output?

```python
print("" in "Python")
```

## Question 10

What is the output?

```python
required = ["Python", "DSA"]
available = ["Python", "DSA", "Database"]

print(all(subject in available for subject in required))
```

## Question 11

What is the output?

```python
numbers = {10, 20, 30}

print(20 in numbers)
```

## Question 12

What is the output?

```python
text = "Programming"

print("gram" in text)
```

## Answer Key

| Question | Answer | Reason |
|---|---|---|
| 1 | `True` | 20 exists in the list |
| 2 | `True` | 40 is absent |
| 3 | `True` | P exists in Python |
| 4 | `False` | String membership is case-sensitive |
| 5 | `False` | Amaan is a value, not a key |
| 6 | `True` | Amaan exists in dictionary values |
| 7 | `False` | Range stop is excluded |
| 8 | `True` | Yellow is absent |
| 9 | `True` | Empty string is a substring of every string |
| 10 | `True` | Every required subject exists |
| 11 | `True` | 20 exists in the set |
| 12 | `True` | gram occurs inside Programming |

---

# 36. Viva Questions and Answers

Prepare these questions for practical examinations and interviews.

## A. Basic Questions

**Q1. What are membership operators in Python?**

Membership operators check whether a value is present inside another object or collection.

**Q2. How many membership operators are available in Python?**

Two: `in` and `not in`.

**Q3. What is the purpose of the `in` operator?**

It checks whether a specified element exists.

**Q4. What is the purpose of the `not in` operator?**

It checks whether a specified element is absent.

**Q5. What result do membership operators return for normal built-in collection checks?**

A Boolean result: `True` or `False`.

**Q6. Can membership operators be used with strings?**

Yes.

**Q7. Can membership operators be used with lists?**

Yes.

**Q8. Can membership operators be used with tuples?**

Yes.

**Q9. Can membership operators be used with sets?**

Yes.

**Q10. Can membership operators be used with dictionaries?**

Yes. Direct dictionary membership checks keys.

## B. String Questions

**Q11. What is a substring?**

A substring is a continuous sequence of characters within a larger string.

**Q12. Is string membership case-sensitive?**

Yes.

**Q13. How can you perform case-insensitive membership checking?**

Normalize the compared strings using `lower()` or `casefold()`.

**Q14. What does `"" in "Python"` return?**

`True`.

**Q15. Does `"program" in "programming"` return `True`?**

Yes, because `"program"` occurs inside `"programming"`.

**Q16. Does string membership automatically check complete words?**

No. It checks for a substring.

**Q17. How can you check a complete whitespace-separated word?**

Use `word in sentence.split()`, while considering punctuation.

**Q18. What is the difference between `lower()` and `casefold()`?**

`lower()` converts text to lowercase, whereas `casefold()` performs more comprehensive case normalization for caseless matching.

## C. Collection Questions

**Q19. Does dictionary membership check keys or values by default?**

Keys.

**Q20. How can you check dictionary values?**

Use `.values()`.

**Q21. How can you check dictionary key-value pairs?**

Use `.items()`.

**Q22. Can membership operators be used with a set?**

Yes.

**Q23. Why are sets useful for membership checking?**

They generally provide average-case constant-time lookup for hashable values.

**Q24. Can a list be stored as a set element?**

No. Lists are unhashable.

**Q25. Can a tuple be stored as a set element?**

Yes, when all its elements are hashable.

**Q26. Are duplicate values stored in a set?**

No. A set stores unique elements.

**Q27. Does membership checking modify a list?**

No. A normal membership check does not modify the list.

## D. Range and Function Questions

**Q28. Can `in` be used with `range()`?**

Yes.

**Q29. Is the stop value included in `range()`?**

No. The stop value is excluded.

**Q30. What is the purpose of `all()`?**

It returns `True` when all elements in the iterable are truthy.

**Q31. What is the purpose of `any()`?**

It returns `True` when at least one element in the iterable is truthy.

**Q32. How can you check whether all required subjects are available?**

Use `all()` with membership expressions or use set difference to identify missing subjects.

**Q33. Can membership be checked with a generator?**

Yes, but the membership test may consume elements from the generator.

## E. Conceptual Questions

**Q34. What is the difference between `in` and `not in`?**

`in` checks presence, while `not in` checks absence.

**Q35. What is the difference between membership and comparison operators?**

Membership checks whether a value exists in a collection. Comparison operators compare values.

**Q36. What is the difference between membership and identity operators?**

Membership checks for an element. Identity checks whether two references point to the same object.

**Q37. What is the worst-case time complexity of list membership?**

\(O(n)\).

**Q38. What is the average-case time complexity of set membership?**

Typically \(O(1)\).

**Q39. What is the average-case time complexity of dictionary key membership?**

Typically \(O(1)\).

**Q40. What is the time complexity of checking dictionary values?**

Typically \(O(n)\).

## F. Practical Questions

**Q41. How do you check whether a username exists in a list?**

Use `username in usernames`.

**Q42. How do you check whether a file extension is allowed?**

Extract and normalize the extension, then check it against an allowed set.

**Q43. How do you check whether a number exists in a range?**

Use `number in range(start, stop)`.

**Q44. How do you check whether a value is absent from a blocked list?**

Use `value not in blocked_list`.

**Q45. How do you check whether a student selected a subject?**

Use `subject in selected_subjects`.

**Q46. How do you search for a dictionary value?**

Use `value in dictionary.values()`.

**Q47. Why does `"10" in [10, 20]` return `False`?**

Because `"10"` is a string and `10` is an integer.

**Q48. How do parentheses help with membership expressions?**

They make the intended grouping of a complex condition clearer.

**Q49. Can membership operators be used inside an `if` statement?**

Yes.

**Q50. Give one real-world application of membership operators.**

Checking whether a username, product, subject, role, or file extension belongs to an allowed collection.

---

# 37. Connection with Data Structures and Algorithms (DSA)

Membership operators are important in DSA because many problems require searching for a particular element.

They are especially useful when learning:

- Linear Search.
- Hashing.
- Sets.
- Dictionaries.
- Duplicate Detection.
- Frequency Counting.
- Searching and Filtering.
- Two Sum.
- Array and String Problems.

## 37.1 Linear Search

Linear search checks elements one by one.

Example:

```python
numbers = [10, 20, 30, 40, 50]

target = 30

if target in numbers:
    print("Element found")
else:
    print("Element not found")
```

Output:

```text
Element found
```

For a list, this is generally a linear-time membership operation.

## 37.2 Hashing

Sets and dictionaries use hashing to support efficient lookups.

```python
visited = {10, 20, 30, 40}

print(30 in visited)
```

Output:

```text
True
```

This is useful when a program needs to check whether a value has already been seen.

## 37.3 Duplicate Detection

```python
numbers = [10, 20, 10, 30, 40, 20]

unique_numbers = set(numbers)

print(unique_numbers)
```

The set contains each value once.

The order of its display should not be relied upon.

## 37.4 Two Sum Problem

**Problem:** Find two numbers whose sum equals a target.

```python
numbers = [2, 7, 11, 15]

target = 9

seen = set()

for number in numbers:
    complement = target - number

    if complement in seen:
        print("Pair found:", complement, number)
        break

    seen.add(number)
```

**Output:**

```text
Pair found: 2 7
```

### Explanation

The target is 9.

The first number is 2.

Its complement is:

```text
9 - 2 = 7
```

The value 7 is not yet in the set, so 2 is added.

The next number is 7.

Its complement is:

```text
9 - 7 = 2
```

The value 2 exists in `seen`.

Therefore, the program finds the pair `(2, 7)`.

For this standard approach, set lookup is average-case \(O(1)\), so the overall expected time is \(O(n)\).

## 37.5 Filtering Data

```python
allowed_skills = {"Python", "Java"}

candidate_skills = [
    "Python",
    "C++",
    "Java",
    "HTML"
]

selected_skills = [
    skill
    for skill in candidate_skills
    if skill in allowed_skills
]

print(selected_skills)
```

**Output:**

```text
['Python', 'Java']
```

The program keeps only skills found in the allowed set.

## 37.6 Future DSA Learning Path

After completing this topic, study these concepts:

1. Linear Search.
2. Binary Search.
3. Hashing.
4. Hash Tables.
5. Sets and Dictionaries.
6. Duplicate Detection.
7. Frequency Counting.
8. Two Sum.
9. Array Searching Problems.
10. String Searching Problems.

---

# 38. Interview Preparation

Prepare the following practical interview tasks.

## Coding Task 1: Search an Element

Given a list and a target, determine whether the target exists.

## Coding Task 2: Search a Username

Check whether a username is registered without considering uppercase and lowercase differences.

## Coding Task 3: Check Allowed Extensions

Validate a filename against an allowed collection of extensions.

## Coding Task 4: Find Missing Subjects

Given required and available subjects, identify all missing subjects.

## Coding Task 5: Detect Duplicates

Use a set to detect whether a list contains duplicate elements.

## Coding Task 6: Check Vowels

Determine whether a character is a vowel.

## Coding Task 7: Find a Pair

Use set membership to solve a simple Two Sum problem.

## Coding Task 8: Check a Dictionary Key

Determine whether a particular key exists before accessing its value.

## Coding Task 9: Search for a Word

Explain the difference between substring search and complete-word search.

## Coding Task 10: Optimize Repeated Searching

Explain why a set may be more appropriate than a list when performing many membership checks.

### Interview Preparation Checklist

- [ ] Explain `in`.
- [ ] Explain `not in`.
- [ ] Explain dictionary key membership.
- [ ] Explain dictionary value membership.
- [ ] Explain case sensitivity.
- [ ] Explain substring searching.
- [ ] Explain set membership complexity.
- [ ] Explain list membership complexity.
- [ ] Solve a basic searching problem.
- [ ] Solve the Two Sum problem using a set.

---

# 39. Glossary

| Term | Meaning |
|---|---|
| Membership | Checking whether an element exists |
| `in` | Checks whether an item is present |
| `not in` | Checks whether an item is absent |
| Collection | An object that stores or provides multiple values |
| Sequence | An ordered collection of values |
| String | A sequence of Unicode characters |
| Substring | A continuous sequence of characters inside a string |
| List | An ordered, mutable collection |
| Tuple | An ordered, immutable collection |
| Set | An unordered collection of unique hashable elements |
| Dictionary | A collection of key-value pairs |
| Key | The identifier used to access a dictionary value |
| Value | Data associated with a dictionary key |
| `.keys()` | Dictionary keys view |
| `.values()` | Dictionary values view |
| `.items()` | Dictionary key-value pairs view |
| `range()` | Represents an arithmetic progression of integers |
| Case-sensitive | Treats uppercase and lowercase differently |
| Case-insensitive | Compares text without considering case differences |
| `casefold()` | Performs comprehensive case normalization |
| `all()` | Checks whether all iterable elements are truthy |
| `any()` | Checks whether at least one iterable element is truthy |
| Hashing | A process used to map hashable values to hash values |
| Time complexity | Describes how an operation's running time grows |
| Linear Search | Searching elements one by one |
| Hash Table | A data structure based on hashing |
| Iterator | An object that produces values one at a time |
| Generator | An iterator commonly created using generator syntax |

---

# 40. Quick Revision Notes

Revise these points before your examination.

### Operators

```python
value in collection
value not in collection
```

### String

```python
"Python" in "Python Programming"
```

### List

```python
10 in [10, 20, 30]
```

### Tuple

```python
20 in (10, 20, 30)
```

### Set

```python
30 in {10, 20, 30}
```

### Dictionary Keys

```python
"name" in student
```

### Dictionary Values

```python
"Amaan" in student.values()
```

### Dictionary Pairs

```python
("name", "Amaan") in student.items()
```

### Range

```python
5 in range(1, 10)
```

### Case Normalization

```python
text.casefold()
```

### All Conditions

```python
all(condition for item in collection)
```

### Any Condition

```python
any(condition for item in collection)
```

### Most Important Rules

1. `in` checks presence.
2. `not in` checks absence.
3. String membership is case-sensitive.
4. String membership searches substrings.
5. Direct dictionary membership checks keys.
6. Use `.values()` to search dictionary values.
7. Use `.items()` to search key-value pairs.
8. The stop value of `range()` is excluded.
9. Set membership is typically average-case \(O(1)\).
10. List membership is \(O(n)\) in the worst case.
11. An empty string is present in every string.
12. Membership checks on generators may consume elements.

---

# 41. Learning Checklist

Complete this checklist before moving to the next topic.

## Basic Understanding

- [ ] I understand membership operators.
- [ ] I can explain `in`.
- [ ] I can explain `not in`.
- [ ] I understand Boolean results.

## String Membership

- [ ] I can search for a character.
- [ ] I can search for a substring.
- [ ] I understand case sensitivity.
- [ ] I can perform case-insensitive matching.
- [ ] I understand substring vs complete-word search.
- [ ] I understand the empty-string edge case.

## Collection Membership

- [ ] I can check list membership.
- [ ] I can check tuple membership.
- [ ] I can check set membership.
- [ ] I can check dictionary keys.
- [ ] I can check dictionary values.
- [ ] I can check dictionary key-value pairs.
- [ ] I can check range membership.

## Advanced Concepts

- [ ] I understand `all()`.
- [ ] I understand `any()`.
- [ ] I understand set difference.
- [ ] I understand basic time complexity.
- [ ] I understand how membership works with generators.
- [ ] I can combine membership expressions with logical operators.

## Programming Practice

- [ ] I have run all 12 examples.
- [ ] I have tried all 12 solved problems.
- [ ] I have attempted all 10 unsolved questions.
- [ ] I have completed the practice test.
- [ ] I can explain the solution to each problem.

## DSA Preparation

- [ ] I understand linear searching.
- [ ] I understand why sets are useful for lookup.
- [ ] I can explain basic hashing.
- [ ] I have tried the Two Sum example.
- [ ] I understand why choosing the right data structure matters.

---

# 42. How to Run the Python Program

The folder contains:

```text
06-Membership-Operators/
│
├── README.md
│
└── 01_membership_operators.py
```

### Step 1: Open PowerShell

Open PowerShell or the VS Code terminal.

### Step 2: Navigate to the Topic Folder

```powershell
cd "C:\Users\Amaan Syed\OneDrive\Desktop\DSA-Python\PYTHON\Week-1-Programming-Fundamentals\05-Operators-Expressions\06-Membership-Operators"
```

### Step 3: Run the Python File

```powershell
python 01_membership_operators.py
```

### Step 4: Select a Menu Option

The program displays a main menu similar to:

```text
============================================================
             PYTHON MEMBERSHIP OPERATORS
============================================================

1. View 12 Membership Operator Examples
2. Practice 12 Solved Problems
3. View 10 Unsolved Practice Questions
4. View Learning Checklist
0. Exit
```

### Step 5: Practice

Start with option `1` to understand the examples.

Then select option `2` to practise the solved problems.

After that, attempt option `3` without looking at solutions.

Finally, use option `4` to review the checklist.

---

# 43. Folder Structure

The completed topic should have this structure:

```text
06-Membership-Operators/
│
├── README.md
│
└── 01_membership_operators.py
```

### File Responsibilities

| File | Purpose |
|---|---|
| `README.md` | Complete theoretical notes, examples, practice, and revision |
| `01_membership_operators.py` | Executable examples and interactive exercises |

Keep the documentation and executable code in separate files. This makes the repository easier to understand and maintain.

---

# 44. Navigation

### Previous Topic

[05 - Bitwise Operators](../05-Bitwise-Operators/README.md)

### Current Topic

**06 - Membership Operators**

### Next Topic

[07 - Identity Operators](../07-Identity-Operators/README.md)

### Parent Folder

[05 - Operators and Expressions](../README.md)

---

# 45. Final Summary

Membership operators allow Python programs to check whether a particular value exists inside a supported collection or object.

Python provides two membership operators:

- `in`
- `not in`

They can be used with strings, lists, tuples, sets, dictionaries, ranges, and other objects that support membership testing.

The most important concepts from this topic are:

1. Use `in` to check whether a value exists.
2. Use `not in` to check whether a value is absent.
3. Remember that string membership is case-sensitive.
4. Understand that string membership checks substrings, not complete words.
5. Remember that direct dictionary membership checks keys.
6. Use `.values()` to check dictionary values.
7. Use `.items()` to check key-value pairs.
8. Use sets when efficient repeated membership checks are important.
9. Understand the difference between list and set lookup complexity.
10. Combine membership with `all()` and `any()` when checking multiple conditions.

Membership operators are not just a small Python feature. They are used in searching, validation, filtering, hashing, and many practical DSA problems.

**Complete the examples, solve the practice problems, and revise the viva questions before moving to the next topic.**

Keep practising Python every day. Strong fundamentals make advanced programming much easier.