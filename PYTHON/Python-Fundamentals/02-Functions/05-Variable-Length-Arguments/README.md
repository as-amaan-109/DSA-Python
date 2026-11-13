# Variable-Length Arguments in Python

**Part 2: Python Fundamentals**  
**Section: 02 – Functions**  
**Topic: 05 – Variable-Length Arguments**

---

# 1. Introduction

In Python, a function normally receives a fixed number of arguments according to its parameters.

But sometimes we do not know in advance how many values the caller will provide.

For example:

- A calculator may need to add two, three, or ten numbers.
- A student record may contain different numbers of subjects.
- A user profile may contain different numbers of optional details.
- An invoice may contain any number of products.
- An application configuration may contain different settings.

Python provides **variable-length arguments** to handle these situations.

There are two important techniques:

1. `*args` – Accepts a variable number of positional arguments.
2. `**kwargs` – Accepts a variable number of keyword arguments.

### Example

```python
def add_numbers(*numbers):
    return sum(numbers)


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40, 50))
```

**Output:**

```text
30
60
150
```

The function accepts different numbers of arguments without changing its definition.

## Learning Objectives

After completing this topic, you should be able to:

- Understand variable-length arguments.
- Understand the purpose of `*args`.
- Understand the purpose of `**kwargs`.
- Accept multiple positional arguments.
- Accept multiple keyword arguments.
- Iterate through `args` and `kwargs`.
- Combine normal parameters with variable-length arguments.
- Combine `*args` and `**kwargs`.
- Understand keyword-only parameters.
- Unpack lists and tuples using `*`.
- Unpack dictionaries using `**`.
- Develop flexible functions for practical applications.

---

# 2. What Are Variable-Length Arguments?

Variable-length arguments allow a function to receive an unspecified number of arguments.

Instead of defining a separate parameter for every value, we use special syntax to collect arguments.

Python provides two main forms:

| Syntax | Purpose | Collected Data Type |
|---|---|---|
| `*args` | Variable positional arguments | Tuple |
| `**kwargs` | Variable keyword arguments | Dictionary |

The names `args` and `kwargs` are conventions. They are not reserved keywords.

For example, these are also valid:

```python
def display(*numbers):
    print(numbers)


def profile(**details):
    print(details)
```

The important part is the `*` or `**` syntax.

---

# 3. Understanding *args

`*args` allows a function to accept any number of additional positional arguments.

Python collects those positional arguments into a tuple.

### Syntax

```python
def function_name(*args):
    statements
```

### Example

```python
def show_numbers(*numbers):
    print(numbers)


show_numbers(10, 20, 30)
show_numbers(5, 15)
show_numbers(100, 200, 300, 400)
```

**Output:**

```text
(10, 20, 30)
(5, 15)
(100, 200, 300, 400)
```

### Explanation

1. `*numbers` collects all extra positional arguments.
2. Python stores them in a tuple.
3. The tuple can be printed, accessed, or iterated over.
4. The same function can accept different numbers of values.

### Important Points

- `*args` collects extra positional arguments.
- The collected values form a tuple.
- The tuple preserves the order of supplied arguments.
- It can contain values of different data types.
- A function can receive zero additional positional arguments.

### Example with Different Data Types

```python
def display_values(*values):
    for value in values:
        print(value, type(value).__name__)


display_values(
    "Python",
    100,
    25.5,
    True
)
```

**Output:**

```text
Python str
100 int
25.5 float
True bool
```

---

# 4. Iterating Through *args

Since `*args` creates a tuple, we can use loops to process its elements.

### Example

```python
def display_subjects(*subjects):
    for subject in subjects:
        print(subject)


display_subjects(
    "Python",
    "Java",
    "Data Structures",
    "Database Management"
)
```

**Output:**

```text
Python
Java
Data Structures
Database Management
```

### Using enumerate()

```python
def show_subjects(*subjects):
    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")


show_subjects("Python", "DSA", "MERN Stack")
```

**Output:**

```text
1. Python
2. DSA
3. MERN Stack
```

### When Is *args Useful?

Use `*args` when:

- The number of inputs is not fixed.
- A function needs to process many values.
- You need to calculate a sum or average.
- You need to combine multiple strings.
- You need to process a flexible collection of items.

---

# 5. Understanding **kwargs

`**kwargs` allows a function to accept any number of additional keyword arguments.

Python collects these arguments into a dictionary.

### Syntax

```python
def function_name(**kwargs):
    statements
```

### Example

```python
def create_profile(**details):
    print(details)


create_profile(
    name="Amaan",
    age=22,
    city="Mumbai"
)
```

**Output:**

```text
{'name': 'Amaan', 'age': 22, 'city': 'Mumbai'}
```

### Explanation

1. `**details` collects additional keyword arguments.
2. Python stores them inside a dictionary.
3. Each keyword becomes a dictionary key.
4. Each supplied value becomes the corresponding dictionary value.

### Important Points

- `**kwargs` collects keyword arguments.
- The collected values form a dictionary.
- Each argument needs a keyword name.
- Values can be of different data types.
- A function can receive zero additional keyword arguments.

### Example with Different Data Types

```python
def display_profile(**details):
    for key, value in details.items():
        print(key, ":", value)


display_profile(
    name="Amaan",
    age=22,
    student=True,
    percentage=85.5
)
```

**Output:**

```text
name : Amaan
age : 22
student : True
percentage : 85.5
```

---

# 6. Iterating Through **kwargs

A dictionary provides methods to access its contents.

The `items()` method returns key-value pairs.

### Example

```python
def display_employee(**details):
    for key, value in details.items():
        print(f"{key.title()}: {value}")


display_employee(
    name="Amaan",
    department="IT",
    designation="Developer",
    city="Mumbai"
)
```

**Output:**

```text
Name: Amaan
Department: IT
Designation: Developer
City: Mumbai
```

### Common Dictionary Operations

| Operation | Purpose |
|---|---|
| `kwargs.keys()` | Returns dictionary keys |
| `kwargs.values()` | Returns dictionary values |
| `kwargs.items()` | Returns key-value pairs |
| `kwargs.get("name")` | Safely retrieves a value |
| `kwargs["name"]` | Accesses a value by key |

### Example

```python
def display_details(**details):
    print("Keys:", details.keys())
    print("Values:", details.values())
    print("Items:", details.items())


display_details(
    name="Amaan",
    course="Computer Science"
)
```

---

# 7. Difference Between *args and **kwargs

Both techniques accept variable numbers of arguments, but they handle different forms of input.

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Purpose | Positional arguments | Keyword arguments |
| Collected type | Tuple | Dictionary |
| Argument format | `10, 20, 30` | `name="Amaan"` |
| Access | By index or iteration | By key or iteration |
| Naming | Conventional name `args` | Conventional name `kwargs` |
| Number of values | Variable | Variable |

### Example Using Both

```python
def student_profile(*subjects, **details):
    print("Subjects:", subjects)
    print("Details:", details)


student_profile(
    "Python",
    "DSA",
    "MERN Stack",
    name="Amaan",
    age=22,
    city="Mumbai"
)
```

**Output:**

```text
Subjects: ('Python', 'DSA', 'MERN Stack')
Details: {'name': 'Amaan', 'age': 22, 'city': 'Mumbai'}
```

The positional values are collected into a tuple, while the keyword values are collected into a dictionary.

---

# 8. Combining Normal Parameters with *args

A function can contain ordinary parameters and `*args`.

### Example

```python
def student_details(name, *subjects):
    print("Student:", name)
    print("Subjects:", subjects)


student_details(
    "Amaan",
    "Python",
    "DSA",
    "Database Management"
)
```

**Output:**

```text
Student: Amaan
Subjects: ('Python', 'DSA', 'Database Management')
```

### Explanation

- `name` receives the first positional argument.
- Remaining positional arguments are collected into `subjects`.
- `subjects` is a tuple.

### Parameter Order

A common function definition is:

```python
def function_name(required_parameter, *args):
    statements
```

A required parameter can appear before `*args`.

### Important Example

```python
def display(first, *remaining):
    print("First:", first)
    print("Remaining:", remaining)


display("Python", "Java", "C++")
```

**Output:**

```text
First: Python
Remaining: ('Java', 'C++')
```

---

# 9. Combining Default Parameters with *args

Default parameters can also be combined with variable positional arguments.

Consider:

```python
def greet_multiple(prefix="Hello", *names):
    for name in names:
        print(f"{prefix}, {name}!")


greet_multiple(
    "Good morning",
    "Amaan",
    "Rahul"
)
```

**Output:**

```text
Good morning, Amaan!
Good morning, Rahul!
```

### Important Detail

In this definition:

```python
def greet_multiple(prefix="Hello", *names):
    ...
```

The first positional value is assigned to `prefix`. Remaining positional values are collected in `names`.

Therefore:

```python
greet_multiple()
```

uses the default prefix but supplies no names.

When you need to change a default parameter while passing values to `*args`, keyword arguments can be clearer:

```python
def greet_multiple(*names, prefix="Hello"):
    for name in names:
        print(f"{prefix}, {name}!")


greet_multiple(
    "Amaan",
    "Rahul",
    prefix="Welcome"
)
```

Here, `prefix` is keyword-only because it appears after `*names`.

---

# 10. Keyword-Only Parameters

A keyword-only parameter must be supplied using its parameter name.

The `*` marker can separate positional parameters from keyword-only parameters.

### Example

```python
def calculate_total(*prices, tax_rate=0.05):
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


print(
    calculate_total(
        100,
        200,
        300,
        tax_rate=0.10
    )
)
```

**Output:**

```text
660.0
```

### Explanation

- `*prices` collects positional price arguments.
- `tax_rate` is keyword-only.
- The caller must specify `tax_rate=...` when changing it.

This call is invalid:

```python
calculate_total(100, 200, 0.10)
```

The `0.10` is treated as another price, not as the tax rate.

### Why Are Keyword-Only Parameters Useful?

They:

- Make function calls more readable.
- Reduce confusion between similar numeric values.
- Make optional configuration explicit.
- Help prevent accidental argument-order mistakes.

---

# 11. Unpacking Arguments Using *

The `*` operator can unpack an iterable such as a list or tuple into individual positional arguments.

### Example

```python
def add_numbers(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

result = add_numbers(*numbers)

print(result)
```

**Output:**

```text
60
```

### Explanation

The expression:

```python
add_numbers(*numbers)
```

is equivalent to:

```python
add_numbers(10, 20, 30)
```

The list elements are passed as separate positional arguments.

### Unpacking a Tuple

```python
def display(a, b, c):
    print(a, b, c)


values = ("Python", "Java", "C++")

display(*values)
```

**Output:**

```text
Python Java C++
```

### Important Rules

- The iterable must contain the correct number of values for the receiving parameters.
- Unpacking can be used with lists, tuples, and other iterables.
- The unpacking operator does not modify the original collection.

---

# 12. Unpacking Dictionaries Using **

The `**` operator unpacks dictionary entries into keyword arguments.

### Example

```python
def create_user(name, age, city):
    print(name, age, city)


user_data = {
    "name": "Amaan",
    "age": 22,
    "city": "Mumbai"
}

create_user(**user_data)
```

**Output:**

```text
Amaan 22 Mumbai
```

### Explanation

The expression:

```python
create_user(**user_data)
```

is equivalent to:

```python
create_user(
    name="Amaan",
    age=22,
    city="Mumbai"
)
```

### Important Rules

- Dictionary keys must match acceptable parameter names unless the receiving function accepts `**kwargs`.
- Keys must be strings when used as keyword argument names.
- Required parameters must receive values.
- Passing the same parameter more than once causes a `TypeError`.

### Example with Duplicate Values

```python
def greet(name):
    print(name)


details = {"name": "Amaan"}

# This would raise TypeError:
# greet("Rahul", **details)
```

Both the positional argument and dictionary expansion try to assign a value to `name`.

---

# 13. Combining *args and **kwargs

A function can receive both variable positional and keyword arguments.

### Example

```python
def create_profile(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", details)


create_profile(
    "Amaan",
    "Python",
    "DSA",
    "MERN Stack",
    age=22,
    city="Mumbai",
    education="Diploma"
)
```

**Output:**

```text
Name: Amaan
Skills: ('Python', 'DSA', 'MERN Stack')
Details: {
    'age': 22,
    'city': 'Mumbai',
    'education': 'Diploma'
}
```

### General Function Parameter Order

A useful simplified order for a flexible function is:

```python
def function_name(
    required_parameter,
    default_parameter="value",
    *args,
    keyword_only_parameter="value",
    **kwargs
):
    statements
```

Python also supports more advanced parameter markers, but this pattern covers many everyday use cases.

---

# 14. Important Function Parameter Ordering

A typical flexible function may use this structure:

```python
def example(
    name,
    age=18,
    *subjects,
    city="Unknown",
    **extra_details
):
    return {
        "name": name,
        "age": age,
        "subjects": subjects,
        "city": city,
        "extra_details": extra_details
    }
```

### Calling the Function

```python
result = example(
    "Amaan",
    22,
    "Python",
    "DSA",
    city="Mumbai",
    college="Polytechnic"
)

print(result)
```

### Explanation

| Parameter | Value Received |
|---|---|
| `name` | `"Amaan"` |
| `age` | `22` |
| `subjects` | `("Python", "DSA")` |
| `city` | `"Mumbai"` |
| `extra_details` | `{"college": "Polytechnic"}` |

Understanding parameter order is important when writing functions with many types of arguments.

---

# SECTION 1: TWELVE TOPIC EXAMPLES

The following examples are included in:

`05_variable_length_arguments.py`

## Example 01 – Basic *args

**Concept:** Accepting multiple positional arguments.

```python
def show_numbers(*numbers):
    print("Received arguments:", numbers)
    print("Data type:", type(numbers).__name__)


show_numbers(10, 20, 30, 40)
```

**Output:**

```text
Received arguments: (10, 20, 30, 40)
Data type: tuple
```

**Explanation:** The function collects all supplied positional arguments into a tuple.

## Example 02 – *args Without Values

**Concept:** Calling a function without supplying extra positional arguments.

```python
def show_values(*values):
    if not values:
        print("No positional arguments were provided.")
        return

    print("Received values:", values)


show_values()
show_values("Python", 100, True)
```

**Output:**

```text
No positional arguments were provided.
Received values: ('Python', 100, True)
```

**Explanation:** A function using `*args` can receive zero or more positional arguments.

## Example 03 – Iterating Through *args

**Concept:** Using a loop to process positional arguments.

```python
def display_subjects(*subjects):
    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")


display_subjects(
    "Python",
    "Java",
    "Data Structures",
    "Database Management"
)
```

**Output:**

```text
1. Python
2. Java
3. Data Structures
4. Database Management
```

**Explanation:** `enumerate()` supplies an index and value for each tuple element.

## Example 04 – Sum Using *args

**Concept:** Calculating the sum of a variable number of values.

```python
def add_all_numbers(*numbers):
    return sum(numbers)


result = add_all_numbers(10, 20, 30, 40, 50)

print("Sum:", result)
```

**Output:**

```text
Sum: 150
```

**Explanation:** The built-in `sum()` function processes all values collected in the tuple.

## Example 05 – Basic **kwargs

**Concept:** Accepting a variable number of keyword arguments.

```python
def display_profile(**details):
    print("Received arguments:", details)
    print("Data type:", type(details).__name__)


display_profile(
    name="Amaan",
    age=22,
    city="Mumbai"
)
```

**Output:**

```text
Received arguments: {'name': 'Amaan', 'age': 22, 'city': 'Mumbai'}
Data type: dict
```

**Explanation:** The supplied keyword arguments are collected into a dictionary.

## Example 06 – Iterating Through **kwargs

**Concept:** Processing dictionary key-value pairs.

```python
def display_user_details(**details):
    for key, value in details.items():
        print(f"{key.title()}: {value}")


display_user_details(
    name="Amaan",
    course="Computer Science",
    college="Polytechnic",
    year=2
)
```

**Output:**

```text
Name: Amaan
Course: Computer Science
College: Polytechnic
Year: 2
```

**Explanation:** The `items()` method provides each dictionary key and value.

## Example 07 – Required Parameter with *args

**Concept:** Combining a fixed required parameter with variable positional arguments.

```python
def display_student(name, *subjects):
    print("Student:", name)
    print("Subjects:")

    for subject in subjects:
        print("-", subject)


display_student(
    "Amaan",
    "Python",
    "DSA",
    "Database Management"
)
```

**Output:**

```text
Student: Amaan
Subjects:
- Python
- DSA
- Database Management
```

**Explanation:** The first positional value is assigned to `name`. Remaining values are collected into `subjects`.

## Example 08 – Default Parameter with *args

**Concept:** Combining a default parameter and variable positional arguments.

```python
def greet_multiple(prefix="Hello", *names):
    if not names:
        print("No names provided.")
        return

    for name in names:
        print(f"{prefix}, {name}!")


greet_multiple("Good morning", "Amaan", "Rahul")
greet_multiple("Welcome", "Amaan")
greet_multiple()
```

**Output:**

```text
Good morning, Amaan!
Good morning, Rahul!
Welcome, Amaan!
No names provided.
```

**Explanation:** The first positional value is used as `prefix`. Remaining positional values are collected into `names`.

## Example 09 – Combining *args and **kwargs

**Concept:** Collecting positional and keyword information together.

```python
def create_student_profile(name, *subjects, **details):
    return {
        "name": name,
        "subjects": subjects,
        "details": details
    }


profile = create_student_profile(
    "Amaan",
    "Python",
    "DSA",
    "MERN Stack",
    age=22,
    city="Mumbai",
    semester=4
)

print(profile)
```

**Output:**

```text
{
    'name': 'Amaan',
    'subjects': ('Python', 'DSA', 'MERN Stack'),
    'details': {
        'age': 22,
        'city': 'Mumbai',
        'semester': 4
    }
}
```

**Explanation:** Positional subjects are collected into a tuple and additional keyword details are collected into a dictionary.

## Example 10 – Keyword-Only Arguments

**Concept:** Requiring optional settings to be supplied by keyword.

```python
def calculate_order_total(
    *prices,
    tax_rate=0.05,
    discount=0
):
    subtotal = sum(prices)
    discounted_total = subtotal * (1 - discount / 100)

    return discounted_total * (1 + tax_rate)


total = calculate_order_total(
    100,
    200,
    300,
    tax_rate=0.10,
    discount=5
)

print("Final order total:", round(total, 2))
```

**Output:**

```text
Final order total: 627.0
```

**Explanation:** Both `tax_rate` and `discount` are keyword-only because they follow `*prices`.

## Example 11 – Unpacking a Sequence

**Concept:** Passing elements of a list as separate positional arguments.

```python
def show_values(*values):
    print("Received values:", values)


numbers = [10, 20, 30, 40]

show_values(*numbers)
```

**Output:**

```text
Received values: (10, 20, 30, 40)
```

**Explanation:** The `*` operator unpacks the list into individual positional arguments.

## Example 12 – Unpacking a Dictionary

**Concept:** Passing dictionary entries as keyword arguments.

```python
def describe_user(name, age, city="Unknown"):
    return f"{name}, age {age}, lives in {city}."


user_data = {
    "name": "Amaan",
    "age": 22,
    "city": "Mumbai"
}

result = describe_user(**user_data)

print(result)
```

**Output:**

```text
Amaan, age 22, lives in Mumbai.
```

**Explanation:** The `**` operator unpacks the dictionary entries into keyword arguments.

---

# SECTION 2: TWELVE SOLVED PROGRAMMING PROBLEMS

## Problem 01 – Sum of Multiple Numbers

**Problem Statement:**

Write a function that accepts any number of numeric values using `*args` and returns their sum.

**Code:**

```python
def sum_numbers(*numbers):
    return sum(numbers)


print(sum_numbers(10, 20))
print(sum_numbers(10, 20, 30, 40))
```

**Output:**

```text
30
100
```

**Explanation:**

1. `*numbers` accepts multiple positional arguments.
2. Python collects them into a tuple.
3. `sum()` calculates the total.
4. The function returns the sum.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding storage of the collected argument tuple.

## Problem 02 – Average of Multiple Numbers

**Problem Statement:**

Write a function that calculates the average of any number of supplied values.

Return `None` if no values are supplied.

**Code:**

```python
def average_numbers(*numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


print(average_numbers(10, 20, 30))
print(average_numbers(5, 10))
```

**Output:**

```text
20.0
7.5
```

**Explanation:**

- The function checks if the tuple is empty.
- It calculates the sum of values.
- It divides by the number of values.
- It returns the average.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the argument tuple.

## Problem 03 – Find Maximum

**Problem Statement:**

Write a function that accepts any number of values and returns the largest.

Return `None` when no values are supplied.

**Code:**

```python
def find_maximum(*numbers):
    if not numbers:
        return None

    return max(numbers)


print(find_maximum(10, 45, 20, 80, 30))
```

**Output:**

```text
80
```

**Explanation:**

The function collects all values and uses `max()` to find the largest.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the argument tuple.

## Problem 04 – Multiply Multiple Numbers

**Problem Statement:**

Write a function that multiplies any number of supplied numeric values.

**Code:**

```python
def multiply_numbers(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


print(multiply_numbers(2, 3, 4))
print(multiply_numbers(5, 10))
```

**Output:**

```text
24
50
```

**Explanation:**

The function starts with `1` and multiplies each supplied value.

For no arguments, the result is `1`, the multiplicative identity.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the argument tuple.

## Problem 05 – Count Arguments

**Problem Statement:**

Write a function that counts the number of positional arguments supplied by the caller.

**Code:**

```python
def count_arguments(*values):
    return len(values)


print(count_arguments(10, 20, 30))
print(count_arguments("Python", "Java"))
print(count_arguments())
```

**Output:**

```text
3
2
0
```

**Explanation:**

The `len()` function returns the number of elements stored in the tuple.

**Complexity:**

- Time: O(1)
- Auxiliary Space: O(1), excluding argument collection.

## Problem 06 – Join Multiple Words

**Problem Statement:**

Write a function that accepts any number of words and combines them using a configurable separator.

**Code:**

```python
def join_words(*words, separator=" "):
    return separator.join(words)


print(join_words("Python", "is", "easy"))
print(
    join_words(
        "Python",
        "is",
        "easy",
        separator="-"
    )
)
```

**Output:**

```text
Python is easy
Python-is-easy
```

**Explanation:**

- `*words` collects all strings.
- `separator` is keyword-only.
- `join()` combines the values into a single string.

**Complexity:**

- Time: O(L), where L is the total length of the output.
- Auxiliary Space: O(L), for the resulting string.

## Problem 07 – Student Record Using **kwargs

**Problem Statement:**

Write a function that accepts a student's name and additional details through `**kwargs`.

**Code:**

```python
def create_student_record(name, **details):
    record = {
        "name": name
    }

    record.update(details)

    return record


student = create_student_record(
    "Amaan",
    course="Computer Science",
    city="Mumbai",
    semester=4
)

print(student)
```

**Output:**

```text
{
    'name': 'Amaan',
    'course': 'Computer Science',
    'city': 'Mumbai',
    'semester': 4
}
```

**Explanation:**

1. The name is received through a normal parameter.
2. Additional keyword arguments are collected into a dictionary.
3. `update()` adds those details to the record.
4. The completed dictionary is returned.

**Complexity:**

- Time: O(k), where k is the number of additional details.
- Auxiliary Space: O(k), for the returned record.

## Problem 08 – Total with Tax

**Problem Statement:**

Write a function that accepts a tax rate and any number of product prices. Return the total including tax.

**Code:**

```python
def calculate_total_with_tax(tax_rate, *prices):
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative.")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")

    subtotal = sum(prices)

    return subtotal + (subtotal * tax_rate / 100)


result = calculate_total_with_tax(
    10,
    100,
    200,
    300
)

print("Total:", result)
```

**Output:**

```text
Total: 660.0
```

**Explanation:**

- `tax_rate` receives the first positional argument.
- `*prices` collects the remaining values.
- The function calculates the subtotal.
- It adds the tax amount and returns the final total.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the argument tuple.

## Problem 09 – Format Multiple Tags

**Problem Statement:**

Write a function that accepts multiple tags and combines them using a separator.

**Code:**

```python
def format_tags(*tags, separator=", "):
    cleaned_tags = [
        tag.strip()
        for tag in tags
        if tag.strip()
    ]

    return separator.join(cleaned_tags)


print(format_tags("Python", "DSA", "MERN"))
print(
    format_tags(
        "Python",
        "DSA",
        "MERN",
        separator=" | "
    )
)
```

**Output:**

```text
Python, DSA, MERN
Python | DSA | MERN
```

**Explanation:**

The function accepts multiple strings, removes surrounding whitespace, filters empty tags, and joins them using the selected separator.

**Complexity:**

- Time: O(L), where L is the combined length of the input strings and output.
- Auxiliary Space: O(L), for the cleaned collection and returned string.

## Problem 10 – Application Settings

**Problem Statement:**

Write a function that accepts any number of keyword settings and combines them with default application settings.

**Code:**

```python
def create_settings(**settings):
    default_settings = {
        "theme": "light",
        "language": "English",
        "notifications": True
    }

    default_settings.update(settings)

    return default_settings


result = create_settings(
    theme="dark",
    language="Hindi",
    notifications=False
)

print(result)
```

**Output:**

```text
{
    'theme': 'dark',
    'language': 'Hindi',
    'notifications': False
}
```

**Explanation:**

The function creates default settings and then updates them using the supplied keyword arguments.

**Complexity:**

- Time: O(k), where k is the number of supplied settings.
- Auxiliary Space: O(k), for the settings dictionary.

## Problem 11 – Contact Card

**Problem Statement:**

Create a function that accepts a name and any number of optional contact details.

**Code:**

```python
def create_contact_card(name, **contact_info):
    contact = {
        "name": name
    }

    contact.update(contact_info)

    return contact


contact = create_contact_card(
    "Amaan",
    email="amaan@example.com",
    phone="9876543210",
    city="Mumbai"
)

print(contact)
```

**Output:**

```text
{
    'name': 'Amaan',
    'email': 'amaan@example.com',
    'phone': '9876543210',
    'city': 'Mumbai'
}
```

**Explanation:**

The function receives a fixed name parameter and flexible keyword contact details.

**Complexity:**

- Time: O(k), where k is the number of contact details.
- Auxiliary Space: O(k), for the resulting dictionary.

## Problem 12 – Calculate Statistics

**Problem Statement:**

Write a function that accepts any number of numeric values and returns their sum, average, minimum, and maximum.

**Code:**

```python
def calculate_statistics(*numbers):
    if not numbers:
        return None

    return {
        "total": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers)
    }


result = calculate_statistics(
    10,
    20,
    30,
    40,
    50
)

print(result)
```

**Output:**

```text
{
    'total': 150,
    'average': 30.0,
    'minimum': 10,
    'maximum': 50
}
```

**Explanation:**

The function collects the supplied values and calculates four statistics. The results are returned in a dictionary.

**Complexity:**

- Time: O(n)
- Auxiliary Space: O(1), excluding the argument tuple and fixed-size result dictionary.

---

# SECTION 3: TEN UNSOLVED PRACTICE QUESTIONS

Try solving the following problems yourself.

## Question 01 – Sum of Even Numbers

Write a function using `*args` that accepts any number of integers and returns the sum of only the even numbers.

**Example:**

```text
Input: 10, 15, 20, 25, 30
Expected Output: 60
```

## Question 02 – Longest String

Write a function that accepts multiple strings using `*args` and returns the longest string.

**Example:**

```text
Input: "Python", "JavaScript", "Java"
Expected Output: JavaScript
```

## Question 03 – Student Average

Write a function that receives a student's name and any number of subject marks.

Return the student's name and average marks.

**Example:**

```text
Name: Amaan
Marks: 80, 90, 85

Expected Average: 85
```

## Question 04 – Product Details

Write a function that accepts a product name and any number of keyword details using `**kwargs`.

**Example:**

```text
Product: Laptop
Brand: Dell
Price: 50000
Color: Black
```

Return the complete product dictionary.

## Question 05 – Minimum and Maximum

Write a function that accepts multiple numbers using `*args` and returns both the minimum and maximum values.

**Example:**

```text
Input: 10, 5, 40, 20

Expected Output: (5, 40)
```

## Question 06 – Remove Duplicates

Write a function using `*args` that removes duplicate values while preserving their original order.

**Example:**

```text
Input: 10, 20, 10, 30, 20

Expected Output: (10, 20, 30)
```

## Question 07 – Employee Record

Write a function that accepts an employee name and additional details using `**kwargs`.

Include department, salary, city, and designation.

Return a dictionary.

## Question 08 – Numeric Statistics

Write a function that accepts any number of numeric values and returns:

- Count.
- Sum.
- Average.

Handle the case when no values are supplied.

## Question 09 – Multiple Recipients

Write a function that accepts a required message, multiple recipient names using `*args`, and optional settings using `**kwargs`.

Return a structured message report.

## Question 10 – Flexible Summary

Write a function that accepts a list of values through positional arguments and additional information through keyword arguments.

Return a dictionary containing both collections.

---

# SECTION 4: COMMON MISTAKES

## Mistake 01 – Confusing *args with a List

Incorrect understanding:

```python
def display(*values):
    print(type(values))


display(10, 20, 30)
```

The received object is a tuple, not a list.

**Output:**

```text
<class 'tuple'>
```

## Mistake 02 – Confusing **kwargs with a List

```python
def display(**details):
    print(type(details))


display(name="Amaan", age=22)
```

**Output:**

```text
<class 'dict'>
```

`**kwargs` collects keyword arguments into a dictionary.

## Mistake 03 – Forgetting to Use the Unpacking Operator

Suppose:

```python
def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]
```

Incorrect:

```python
# add(numbers)
```

The function expects three arguments, but this supplies only one list.

Correct:

```python
print(add(*numbers))
```

## Mistake 04 – Using ** with an Incorrect Dictionary Key

```python
def greet(name):
    print(name)


details = {
    "username": "Amaan"
}

# greet(**details)
```

This fails because `username` does not match the parameter name `name`.

Correct:

```python
greet(**{"name": "Amaan"})
```

## Mistake 05 – Supplying an Argument Twice

```python
def greet(name):
    print(name)


details = {
    "name": "Amaan"
}

# greet("Rahul", **details)
```

This raises a `TypeError` because `name` receives two values.

## Mistake 06 – Incorrect Parameter Ordering

Incorrect:

```python
# def example(**kwargs, *args):
#     pass
```

Correct:

```python
def example(*args, **kwargs):
    pass
```

In an ordinary function signature, `**kwargs` appears after `*args`.

## Mistake 07 – Treating kwargs Like a Tuple

Incorrect:

```python
def display(**details):
    print(details[0])
```

`details` is a dictionary, so integer indexing is not appropriate unless such a key exists.

Correct:

```python
def display(**details):
    print(details.get("name"))
```

## Mistake 08 – Forgetting Keyword-Only Parameters

```python
def calculate(*prices, tax_rate=5):
    return sum(prices) * (1 + tax_rate / 100)


result = calculate(100, 200, tax_rate=10)
```

The `tax_rate` must be supplied using its keyword.

---

# SECTION 5: BEST PRACTICES

1. Use `*args` when the number of positional arguments is not fixed.
2. Use `**kwargs` when the number of named arguments is not fixed.
3. Remember that `args` is a tuple.
4. Remember that `kwargs` is a dictionary.
5. Choose descriptive names such as `*prices` and `**details` when they improve readability.
6. Use keyword-only parameters for configuration options.
7. Validate collected arguments when required.
8. Use `enumerate()` when both index and value are needed.
9. Use dictionary methods to process keyword arguments.
10. Avoid unnecessarily complex function signatures.
11. Document what kinds of arguments a flexible function accepts.
12. Avoid accepting arbitrary keyword values when the function should allow only a specific set of options.

### Recommended Style

```python
def create_profile(
    name: str,
    *skills: str,
    city: str = "Unknown",
    **details
):
    """Create a user profile with flexible skills and details."""
    return {
        "name": name,
        "skills": skills,
        "city": city,
        "details": details
    }
```

This structure separates fixed information, variable positional arguments, keyword-only configuration, and extra keyword details.

---

# SECTION 6: REAL-WORLD APPLICATIONS

Variable-length arguments are useful in many software applications.

## 1. Calculator Application

```python
def add_numbers(*numbers):
    return sum(numbers)
```

A calculator can add any number of values.

## 2. Student Management System

```python
def student_record(name, *subjects, **details):
    return {
        "name": name,
        "subjects": subjects,
        "details": details
    }
```

A student can have different numbers of subjects and additional details.

## 3. E-Commerce Application

```python
def calculate_cart(*prices):
    return sum(prices)
```

A shopping cart can contain any number of products.

## 4. Employee Management System

```python
def create_employee(name, **details):
    return {
        "name": name,
        **details
    }
```

Employee records may contain different optional fields.

## 5. Application Configuration

```python
def configure_application(**settings):
    return settings
```

An application can receive flexible configuration settings.

## 6. Logging Systems

Flexible arguments can help logging utilities accept multiple values and optional metadata.

## 7. Report Generation

A report function can receive a variable number of sections and additional metadata.

## 8. Testing Utilities

Test helper functions can accept different inputs and options without requiring many separate function definitions.

---

# SECTION 7: CONNECTION WITH DSA

Variable-length arguments help create reusable functions for algorithms and problem-solving.

## 1. Sum of Numbers

```python
def sum_numbers(*numbers):
    return sum(numbers)
```

This function can process an arbitrary number of values.

## 2. Minimum and Maximum

```python
def find_min_max(*numbers):
    if not numbers:
        return None

    return min(numbers), max(numbers)
```

## 3. Sorting

```python
def sort_values(*numbers):
    return sorted(numbers)
```

## 4. Flexible Searching

```python
def search_targets(numbers, *targets):
    results = {}

    for target in targets:
        results[target] = target in numbers

    return results
```

## 5. Graph Algorithms

Functions for graph processing can use variable arguments for flexible options and metadata.

## 6. Problem-Solving Functions

Functions can accept variable numbers of inputs when problem constraints do not specify a fixed count.

**Important:** Use `*args` and `**kwargs` only when flexibility is genuinely useful. A normal fixed parameter list is often clearer when the number of inputs is known.

---

# SECTION 8: TIME AND SPACE COMPLEXITY

The syntax `*args` and `**kwargs` does not automatically determine the complexity of a function.

The operations performed on the collected values determine the complexity.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Collect n positional arguments | O(n) | O(n) |
| Collect k keyword arguments | O(k) | O(k) |
| Count arguments using len() | O(1) | O(1) |
| Sum n numbers | O(n) | O(1), excluding argument storage |
| Average of n numbers | O(n) | O(1), excluding argument storage |
| Find maximum of n numbers | O(n) | O(1), excluding argument storage |
| Multiply n numbers | O(n) | O(1), excluding argument storage |
| Join strings | O(L), based on total output length | O(L) |
| Update dictionary with k fields | O(k) average | O(k) for the resulting data |
| Sort n values | O(n log n) | Depends on the sorting implementation |

Here:

- `n` represents the number of positional values.
- `k` represents the number of keyword arguments.
- `L` represents the combined string or output length.

Remember that the collected tuple and dictionary themselves require storage proportional to the number of arguments.

---

# SECTION 9: MINI PROJECT – FLEXIBLE STUDENT PROFILE GENERATOR

## Project Objective

Create a student profile generator using `*args` and `**kwargs`.

The program should:

- Accept a student's name.
- Accept any number of skills.
- Accept flexible additional student details.
- Store the information in a dictionary.
- Display the complete profile.

### Project Code

```python
from typing import Any, Dict


def create_student_profile(
    name: str,
    *skills: str,
    **details: Any
) -> Dict[str, Any]:
    """Create a profile with flexible skills and extra details."""

    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    profile = {
        "name": name,
        "skills": skills,
        "details": details
    }

    return profile


def display_profile(
    profile: Dict[str, Any]
) -> None:
    """Display student profile information."""

    print("\n========== STUDENT PROFILE ==========")

    print("Name:", profile["name"])

    print("\nSkills:")

    if profile["skills"]:
        for index, skill in enumerate(
            profile["skills"],
            start=1
        ):
            print(f"{index}. {skill}")
    else:
        print("No skills provided.")

    print("\nAdditional Details:")

    if profile["details"]:
        for key, value in profile["details"].items():
            print(f"{key.title()}: {value}")
    else:
        print("No additional details provided.")


def main() -> None:
    """Collect input and generate a flexible student profile."""

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    skills_input = input(
        "Enter skills separated by commas: "
    ).strip()

    skills = [
        skill.strip()
        for skill in skills_input.split(",")
        if skill.strip()
    ]

    try:
        age_input = input("Enter age: ").strip()
        city = input("Enter city: ").strip()
        course = input("Enter course: ").strip()
        semester_input = input("Enter semester: ").strip()

        age = int(age_input) if age_input else None
        semester = (
            int(semester_input)
            if semester_input
            else None
        )

        details = {}

        if age is not None:
            details["age"] = age

        if city:
            details["city"] = city

        if course:
            details["course"] = course

        if semester is not None:
            details["semester"] = semester

        profile = create_student_profile(
            name,
            *skills,
            **details
        )

        display_profile(profile)

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
```

### Sample Input

```text
Enter student name: Amaan
Enter skills separated by commas: Python, DSA, HTML, CSS
Enter age: 22
Enter city: Mumbai
Enter course: Computer Science
Enter semester: 4
```

### Output

```text
========== STUDENT PROFILE ==========
Name: Amaan

Skills:
1. Python
2. DSA
3. HTML
4. CSS

Additional Details:
Age: 22
City: Mumbai
Course: Computer Science
Semester: 4
```

### Concepts Used

- User-defined functions.
- Variable positional arguments.
- Variable keyword arguments.
- Tuple operations.
- Dictionary operations.
- Argument unpacking.
- Input validation.
- Return statements.

---

# SECTION 10: 50 VIVA QUESTIONS AND ANSWERS

## Basic Concepts

**Q1. What are variable-length arguments in Python?**

Ans: They allow a function to accept a variable number of arguments.

**Q2. What are the two main types of variable-length arguments?**

Ans: `*args` and `**kwargs`.

**Q3. What is `*args`?**

Ans: It collects extra positional arguments into a tuple.

**Q4. What is `**kwargs`?**

Ans: It collects extra keyword arguments into a dictionary.

**Q5. Is `args` a Python keyword?**

Ans: No. It is a conventional parameter name.

**Q6. Is `kwargs` a Python keyword?**

Ans: No. It is also a conventional parameter name.

**Q7. Can we use another name instead of args?**

Ans: Yes. The `*` syntax is what matters.

**Q8. Can `*args` receive zero arguments?**

Ans: Yes.

**Q9. Can `**kwargs` receive zero arguments?**

Ans: Yes.

**Q10. Why are variable-length arguments useful?**

Ans: They allow functions to accept flexible numbers of input values.

## Questions Related to *args

**Q11. What data type does `*args` create?**

Ans: A tuple.

**Q12. Can `*args` contain different data types?**

Ans: Yes.

**Q13. Can we iterate through args?**

Ans: Yes, using a loop.

**Q14. Can we access args using an index?**

Ans: Yes, because it is a tuple.

**Q15. How can we count arguments inside args?**

Ans: Use `len(args)`.

**Q16. Can a normal parameter be used with args?**

Ans: Yes.

**Q17. Can we calculate a sum using args?**

Ans: Yes, using `sum()`.

**Q18. Can args be empty?**

Ans: Yes. It becomes an empty tuple.

**Q19. Can we pass a list using the unpacking operator?**

Ans: Yes, using `*list_name`.

**Q20. What is the result of unpacking a list into a function?**

Ans: Its elements are passed as individual positional arguments.

## Questions Related to **kwargs

**Q21. What data type does kwargs create?**

Ans: A dictionary.

**Q22. Can we pass keyword arguments using kwargs?**

Ans: Yes.

**Q23. How can we iterate through kwargs?**

Ans: Use a loop with `kwargs.items()`.

**Q24. How can we access a particular value in kwargs?**

Ans: Use a key, such as `kwargs["name"]`, or `kwargs.get("name")`.

**Q25. Can kwargs contain different data types?**

Ans: Yes.

**Q26. Can kwargs be empty?**

Ans: Yes. It becomes an empty dictionary.

**Q27. Can a normal parameter be combined with kwargs?**

Ans: Yes.

**Q28. Can we unpack a dictionary into a function?**

Ans: Yes, using `**dictionary_name`.

**Q29. What should dictionary keys generally match during unpacking?**

Ans: They should match the receiving function's parameter names unless the function accepts arbitrary keyword arguments.

**Q30. What happens when the same parameter receives two values?**

Ans: Python raises a `TypeError`.

## Combining Arguments

**Q31. Can args and kwargs be used together?**

Ans: Yes.

**Q32. What is the common parameter order?**

Ans: Normal parameters, optional parameters, `*args`, keyword-only parameters, and finally `**kwargs`, with certain additional syntax rules for advanced signatures.

**Q33. Can a function have a default parameter and args?**

Ans: Yes.

**Q34. What is a keyword-only parameter?**

Ans: A parameter that must be supplied using its name.

**Q35. How can we create keyword-only parameters after args?**

Ans: By placing them after `*args`.

**Q36. What is argument unpacking?**

Ans: It is the process of expanding a collection into individual function arguments.

**Q37. Which operator unpacks lists and tuples?**

Ans: The single-star `*` operator.

**Q38. Which operator unpacks dictionaries into keyword arguments?**

Ans: The double-star `**` operator.

**Q39. Can a tuple be unpacked into a function?**

Ans: Yes.

**Q40. Can multiple dictionaries be unpacked into a function?**

Ans: Yes, provided there are no conflicting keyword assignments.

## Practical and Advanced Questions

**Q41. Does args preserve the order of positional arguments?**

Ans: Yes.

**Q42. Does kwargs preserve insertion order?**

Ans: Yes. Python dictionaries preserve insertion order.

**Q43. Can args be converted into a list?**

Ans: Yes, using `list(args)`.

**Q44. Can kwargs be converted into another dictionary?**

Ans: Yes, using `dict(kwargs)`.

**Q45. What is the advantage of keyword-only arguments?**

Ans: They make optional settings explicit and reduce accidental argument-order mistakes.

**Q46. What happens when a list contains more values than the receiving function expects during unpacking?**

Ans: Python raises a `TypeError` because too many positional arguments were supplied.

**Q47. What happens when a required parameter is missing during dictionary unpacking?**

Ans: Python raises a `TypeError`.

**Q48. Can variable-length arguments be useful in DSA?**

Ans: Yes. They can support flexible algorithms and utility functions.

**Q49. What is the time complexity of summing n values using args?**

Ans: O(n).

**Q50. Why are args and kwargs important in software development?**

Ans: They make functions flexible and reusable and are especially useful when designing APIs, utilities, configuration functions, and frameworks.

---

# SECTION 11: IMPORTANT TERMINOLOGY

| Term | Meaning |
|---|---|
| Variable-Length Arguments | Arguments with a flexible number of values |
| `*args` | Collects positional arguments into a tuple |
| `**kwargs` | Collects keyword arguments into a dictionary |
| Positional Argument | Argument assigned according to position |
| Keyword Argument | Argument supplied using a parameter name |
| Tuple | Ordered collection of values |
| Dictionary | Collection of key-value pairs |
| Unpacking | Expanding a collection into arguments |
| Keyword-Only Parameter | Parameter that must be passed by name |
| `enumerate()` | Provides index-value pairs |
| `items()` | Returns dictionary key-value pairs |
| Parameter | Variable declared in a function definition |
| Argument | Value supplied when calling a function |

---

# SECTION 12: QUICK REVISION NOTES

Remember these important concepts:

1. Variable-length arguments allow flexible function calls.
2. `*args` collects positional arguments.
3. `*args` creates a tuple.
4. `**kwargs` collects keyword arguments.
5. `**kwargs` creates a dictionary.
6. Both can receive zero or more additional values.
7. Normal parameters can be combined with variable-length arguments.
8. Keyword-only parameters can follow `*args`.
9. `*list_name` unpacks a sequence into positional arguments.
10. `**dict_name` unpacks dictionary entries into keyword arguments.
11. Positional and keyword arguments can be combined.
12. Function parameter order must be written correctly.

### Important Syntax

**Using *args**

```python
def display(*values):
    print(values)
```

**Using **kwargs**

```python
def display(**details):
    print(details)
```

**Combining Both**

```python
def profile(name, *skills, **details):
    print(name)
    print(skills)
    print(details)
```

**Unpacking a List**

```python
numbers = [10, 20, 30]

display(*numbers)
```

**Unpacking a Dictionary**

```python
user = {
    "name": "Amaan",
    "age": 22
}

profile(**user)
```

---

# SECTION 13: LEARNING CHECKLIST

Before moving to the next topic, make sure you can:

- [ ] Explain variable-length arguments.
- [ ] Define a function using `*args`.
- [ ] Explain why `*args` creates a tuple.
- [ ] Iterate through args.
- [ ] Define a function using `**kwargs`.
- [ ] Explain why `**kwargs` creates a dictionary.
- [ ] Iterate through kwargs.
- [ ] Combine normal parameters and args.
- [ ] Combine args and kwargs.
- [ ] Use keyword-only parameters.
- [ ] Unpack lists and tuples using `*`.
- [ ] Unpack dictionaries using `**`.
- [ ] Understand duplicate argument errors.
- [ ] Complete all 12 solved problems.
- [ ] Attempt all 10 unsolved questions.
- [ ] Complete the Student Profile Generator mini project.
- [ ] Answer the 50 viva questions.

---

# SECTION 14: HOW TO RUN THIS FILE

### File Location

```text
PYTHON/
└── Python-Fundamentals/
    └── 02-Functions/
        └── 05-Variable-Length-Arguments/
            ├── README.md
            └── 05_variable_length_arguments.py
```

### Run Command

Open PowerShell or the VS Code terminal from your repository root.

Execute:

```powershell
python PYTHON/Python-Fundamentals/02-Functions/05-Variable-Length-Arguments/05_variable_length_arguments.py
```

### Main Menu

```text
1. View 12 topic examples
2. Practice 12 solved problems
3. View 10 unsolved questions
4. View learning checklist
0. Exit
```

---

# FINAL LEARNING GOAL

After completing this topic, you should understand how to write flexible functions that accept different numbers of positional and keyword arguments.

You should also understand how to unpack lists, tuples, and dictionaries when calling functions.

These concepts are frequently useful in real-world Python development, reusable utility functions, APIs, and advanced programming.

**Next Topic: 06 – Keyword and Positional Arguments**

In the next topic, we will study positional arguments, keyword arguments, argument ordering, keyword-only parameters, positional-only parameters, and function-call rules in greater detail.